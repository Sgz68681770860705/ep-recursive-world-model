
from pathlib import Path
import json
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import label as connected_components

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
RESULTS.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)

# ============================================================
# Single unlabeled Hamiltonian field
# i psi_t = -1/2 Delta psi - g |psi|^2 psi + h |psi|^4 psi
# ============================================================

G = 2.0
H6 = 1.0
GRID_N = 128
DOMAIN_L = 40.0
DT = 0.004
DENSITY_THRESHOLD = 0.20
MIN_COMPONENT_PIXELS = 20

def make_grid(n=GRID_N, length=DOMAIN_L):
    x = np.linspace(-length / 2.0, length / 2.0, n, endpoint=False)
    dx = length / n
    X, Y = np.meshgrid(x, x, indexing="xy")
    k = 2.0 * np.pi * np.fft.fftfreq(n, d=dx)
    KX, KY = np.meshgrid(k, k, indexing="xy")
    K2 = KX**2 + KY**2
    return x, dx, X, Y, KX, KY, K2

def initial_two_packets(
    X,
    Y,
    amplitude=1.4,
    width=2.2,
    separation=12.0,
    speed=0.8,
    relative_phase=0.0,
    impact_parameter=0.0,
):
    r1_squared = (
        (X + separation / 2.0) ** 2
        + (Y + impact_parameter / 2.0) ** 2
    )
    r2_squared = (
        (X - separation / 2.0) ** 2
        + (Y - impact_parameter / 2.0) ** 2
    )
    packet1 = (
        amplitude
        * np.exp(-r1_squared / width**2)
        * np.exp(1j * speed * X)
    )
    packet2 = (
        amplitude
        * np.exp(-r2_squared / width**2)
        * np.exp(-1j * speed * X + 1j * relative_phase)
    )
    return packet1 + packet2, packet1, packet2

def split_step(psi, linear_multiplier, dt, g=G, h6=H6):
    density = np.abs(psi) ** 2
    psi = psi * np.exp(
        1j * (g * density - h6 * density**2) * dt / 2.0
    )
    psi = np.fft.ifft2(np.fft.fft2(psi) * linear_multiplier)
    density = np.abs(psi) ** 2
    psi = psi * np.exp(
        1j * (g * density - h6 * density**2) * dt / 2.0
    )
    return psi

def spectral_derivatives(psi, KX, KY):
    transformed = np.fft.fft2(psi)
    dpsi_x = np.fft.ifft2(1j * KX * transformed)
    dpsi_y = np.fft.ifft2(1j * KY * transformed)
    return dpsi_x, dpsi_y

def invariants(psi, X, Y, KX, KY, dx, g=G, h6=H6):
    density = np.abs(psi) ** 2
    dpsi_x, dpsi_y = spectral_derivatives(psi, KX, KY)
    norm = np.sum(density) * dx**2
    kinetic_density = 0.5 * (
        np.abs(dpsi_x) ** 2 + np.abs(dpsi_y) ** 2
    )
    hamiltonian_density = (
        kinetic_density
        - 0.5 * g * density**2
        + (h6 / 3.0) * density**3
    )
    hamiltonian = np.sum(hamiltonian_density) * dx**2
    current_x = np.imag(np.conj(psi) * dpsi_x)
    current_y = np.imag(np.conj(psi) * dpsi_y)
    momentum_x = np.sum(current_x) * dx**2
    momentum_y = np.sum(current_y) * dx**2
    angular_momentum = np.sum(
        np.imag(
            np.conj(psi)
            * (X * dpsi_y - Y * dpsi_x)
        )
    ) * dx**2
    return {
        "norm": float(np.real(norm)),
        "hamiltonian": float(np.real(hamiltonian)),
        "momentum_x": float(np.real(momentum_x)),
        "momentum_y": float(np.real(momentum_y)),
        "angular_momentum": float(np.real(angular_momentum)),
        "peak_density": float(np.max(density)),
    }

def extract_components(
    psi,
    X,
    Y,
    KX,
    KY,
    dx,
    density_threshold=DENSITY_THRESHOLD,
    min_pixels=MIN_COMPONENT_PIXELS,
):
    density = np.abs(psi) ** 2
    labels, raw_count = connected_components(
        density >= density_threshold,
        structure=np.array(
            [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
        ),
    )
    dpsi_x, dpsi_y = spectral_derivatives(psi, KX, KY)
    current_x = np.imag(np.conj(psi) * dpsi_x)
    current_y = np.imag(np.conj(psi) * dpsi_y)

    components = []
    for component_index in range(1, raw_count + 1):
        mask = labels == component_index
        pixel_count = int(np.sum(mask))
        if pixel_count < min_pixels:
            continue
        superlevel_mass = float(np.sum(density[mask]) * dx**2)
        centroid_x = float(
            np.sum(density[mask] * X[mask]) * dx**2
            / superlevel_mass
        )
        centroid_y = float(
            np.sum(density[mask] * Y[mask]) * dx**2
            / superlevel_mass
        )
        momentum_x = float(np.sum(current_x[mask]) * dx**2)
        momentum_y = float(np.sum(current_y[mask]) * dx**2)

        centered_x = X[mask] - centroid_x
        centered_y = Y[mask] - centroid_y
        q_xx = float(
            np.sum(density[mask] * centered_x**2) * dx**2
            / superlevel_mass
        )
        q_xy = float(
            np.sum(density[mask] * centered_x * centered_y)
            * dx**2
            / superlevel_mass
        )
        q_yy = float(
            np.sum(density[mask] * centered_y**2) * dx**2
            / superlevel_mass
        )
        shape_tensor = np.array([[q_xx, q_xy], [q_xy, q_yy]])
        eigenvalues, eigenvectors = np.linalg.eigh(shape_tensor)
        principal_vector = eigenvectors[:, np.argmax(eigenvalues)]
        orientation = float(
            np.arctan2(principal_vector[1], principal_vector[0])
        )
        anisotropy = float(
            (
                np.max(eigenvalues) - np.min(eigenvalues)
            )
            / max(np.sum(eigenvalues), 1e-14)
        )
        components.append(
            {
                "superlevel_mass": superlevel_mass,
                "centroid_x": centroid_x,
                "centroid_y": centroid_y,
                "momentum_x": momentum_x,
                "momentum_y": momentum_y,
                "orientation": orientation,
                "anisotropy": anisotropy,
                "pixel_count": pixel_count,
            }
        )
    components.sort(key=lambda item: item["centroid_x"])
    return components

def run_case(
    name,
    speed,
    relative_phase,
    final_time,
    impact_parameter=0.0,
    n=GRID_N,
    length=DOMAIN_L,
    dt=DT,
    save_stride=25,
    save_snapshots=True,
):
    x, dx, X, Y, KX, KY, K2 = make_grid(n, length)
    psi, packet1, packet2 = initial_two_packets(
        X,
        Y,
        speed=speed,
        relative_phase=relative_phase,
        impact_parameter=impact_parameter,
    )
    initial_field = psi.copy()
    steps = int(round(final_time / dt))
    linear_multiplier = np.exp(-0.5j * K2 * dt)

    times = []
    diagnostics = []
    component_counts = []
    snapshot_fields = {}
    snapshot_targets = np.array(
        [0.0, final_time * 0.35, final_time * 0.55, final_time]
    )
    next_snapshot = 0

    for step in range(steps + 1):
        time = step * dt
        if step % save_stride == 0 or step == steps:
            values = invariants(psi, X, Y, KX, KY, dx)
            components = extract_components(
                psi, X, Y, KX, KY, dx
            )
            times.append(time)
            diagnostics.append(values)
            component_counts.append(len(components))

        if (
            save_snapshots
            and next_snapshot < len(snapshot_targets)
            and time >= snapshot_targets[next_snapshot] - dt / 2.0
        ):
            snapshot_fields[
                f"{snapshot_targets[next_snapshot]:.3f}"
            ] = np.abs(psi) ** 2
            next_snapshot += 1

        if step == steps:
            break
        psi = split_step(
            psi, linear_multiplier, dt, G, H6
        )

    initial_components = extract_components(
        initial_field, X, Y, KX, KY, dx
    )
    final_components = extract_components(
        psi, X, Y, KX, KY, dx
    )

    diagnostics_array = {
        key: np.array([entry[key] for entry in diagnostics])
        for key in diagnostics[0]
    }
    times = np.asarray(times)
    component_counts = np.asarray(component_counts)

    result = {
        "name": name,
        "speed": speed,
        "relative_phase": relative_phase,
        "impact_parameter": impact_parameter,
        "final_time": final_time,
        "times": times,
        "component_counts": component_counts,
        "diagnostics": diagnostics_array,
        "initial_components": initial_components,
        "final_components": final_components,
        "initial_field": initial_field,
        "final_field": psi,
        "packet1": packet1,
        "packet2": packet2,
        "grid": {
            "x": x,
            "dx": dx,
            "X": X,
            "Y": Y,
            "KX": KX,
            "KY": KY,
            "K2": K2,
        },
        "snapshots": snapshot_fields,
    }
    return result

def count_sequence(counts):
    sequence = []
    for value in counts:
        value = int(value)
        if not sequence or sequence[-1] != value:
            sequence.append(value)
    return sequence

def conservation_summary(case):
    diagnostics = case["diagnostics"]
    initial_norm = diagnostics["norm"][0]
    initial_energy = diagnostics["hamiltonian"][0]
    norm_relative_drift = float(
        np.max(np.abs(diagnostics["norm"] - initial_norm))
        / abs(initial_norm)
    )
    energy_relative_drift = float(
        np.max(
            np.abs(diagnostics["hamiltonian"] - initial_energy)
        )
        / max(abs(initial_energy), 1e-14)
    )
    momentum_vector = np.column_stack(
        (
            diagnostics["momentum_x"],
            diagnostics["momentum_y"],
        )
    )
    momentum_absolute_drift = float(
        np.max(
            np.linalg.norm(
                momentum_vector - momentum_vector[0],
                axis=1,
            )
        )
    )
    angular_absolute_drift = float(
        np.max(
            np.abs(
                diagnostics["angular_momentum"]
                - diagnostics["angular_momentum"][0]
            )
        )
    )
    return {
        "norm_relative_drift": norm_relative_drift,
        "energy_relative_drift": energy_relative_drift,
        "momentum_absolute_drift": momentum_absolute_drift,
        "angular_momentum_absolute_drift": angular_absolute_drift,
    }

# ============================================================
# Main topology cases
# ============================================================

fusion_case = run_case(
    name="persistent_fusion_candidate",
    speed=0.40,
    relative_phase=0.0,
    final_time=15.0,
)
fission_case = run_case(
    name="fusion_then_fission",
    speed=0.80,
    relative_phase=np.pi / 2.0,
    final_time=15.0,
)
phase_blocked_case = run_case(
    name="phase_blocked_crossing",
    speed=0.80,
    relative_phase=np.pi,
    final_time=15.0,
)

# Higher-resolution conservation run for the same fusion-fission input.
conservation_case = run_case(
    name="fusion_then_fission_conservation",
    speed=0.80,
    relative_phase=np.pi / 2.0,
    final_time=15.0,
    n=192,
    length=50.0,
    dt=0.003,
    save_stride=50,
    save_snapshots=False,
)

# Time reversal for fission case
grid = fission_case["grid"]
reverse_field = np.conj(fission_case["final_field"])
reverse_steps = int(round(fission_case["final_time"] / DT))
reverse_linear_multiplier = np.exp(-0.5j * grid["K2"] * DT)
for _ in range(reverse_steps):
    reverse_field = split_step(
        reverse_field,
        reverse_linear_multiplier,
        DT,
        G,
        H6,
    )
time_reversal_relative_error = float(
    np.linalg.norm(
        reverse_field - np.conj(fission_case["initial_field"])
    )
    / np.linalg.norm(fission_case["initial_field"])
)

# Separate angular-momentum test on a larger box.
angular_case = run_case(
    name="offcenter_angular_ledger",
    speed=0.80,
    relative_phase=np.pi / 2.0,
    impact_parameter=1.0,
    final_time=4.5,
    n=192,
    length=50.0,
    dt=0.003,
    save_stride=25,
    save_snapshots=False,
)
angular_summary = conservation_summary(angular_case)
initial_angular = float(
    angular_case["diagnostics"]["angular_momentum"][0]
)
angular_relative_drift = float(
    angular_summary["angular_momentum_absolute_drift"]
    / max(abs(initial_angular), 1e-14)
)

# Linear superposition control
x, dx, X, Y, KX, KY, K2 = make_grid()
_, packet1, packet2 = initial_two_packets(
    X,
    Y,
    speed=0.80,
    relative_phase=np.pi / 2.0,
)
linear_time = 6.0
linear_multiplier_exact = np.exp(
    -0.5j * K2 * linear_time
)
combined_evolved = np.fft.ifft2(
    np.fft.fft2(packet1 + packet2) * linear_multiplier_exact
)
separate_evolved = (
    np.fft.ifft2(np.fft.fft2(packet1) * linear_multiplier_exact)
    + np.fft.ifft2(
        np.fft.fft2(packet2) * linear_multiplier_exact
    )
)
linear_superposition_relative_error = float(
    np.linalg.norm(combined_evolved - separate_evolved)
    / np.linalg.norm(combined_evolved)
)

# ============================================================
# Topology classifications and field-only component observables
# ============================================================

fusion_sequence = count_sequence(fusion_case["component_counts"])
fission_sequence = count_sequence(fission_case["component_counts"])
blocked_sequence = count_sequence(
    phase_blocked_case["component_counts"]
)

def interval_with_count(case, count):
    mask = case["component_counts"] == count
    if not np.any(mask) or len(case["times"]) < 2:
        return 0.0
    time_steps = np.diff(case["times"])
    return float(np.sum(time_steps * mask[:-1]))

fusion_one_component_duration = interval_with_count(
    fusion_case, 1
)
fission_one_component_duration = interval_with_count(
    fission_case, 1
)

final_fission_components = fission_case["final_components"]
if len(final_fission_components) == 2:
    outgoing_superlevel_mass_ratio = float(
        max(
            final_fission_components[0]["superlevel_mass"],
            final_fission_components[1]["superlevel_mass"],
        )
        / min(
            final_fission_components[0]["superlevel_mass"],
            final_fission_components[1]["superlevel_mass"],
        )
    )
    outgoing_momentum_difference = float(
        np.linalg.norm(
            np.array(
                [
                    final_fission_components[0]["momentum_x"],
                    final_fission_components[0]["momentum_y"],
                ]
            )
            - np.array(
                [
                    final_fission_components[1]["momentum_x"],
                    final_fission_components[1]["momentum_y"],
                ]
            )
        )
    )
else:
    outgoing_superlevel_mass_ratio = float("nan")
    outgoing_momentum_difference = float("nan")

# ============================================================
# Figures
# ============================================================

def plot_topology(case, filename):
    plt.figure()
    plt.step(
        case["times"],
        case["component_counts"],
        where="mid",
    )
    plt.xlabel("time")
    plt.ylabel("connected components")
    plt.yticks(sorted(set(case["component_counts"].tolist())))
    plt.tight_layout()
    plt.savefig(FIGURES / filename, dpi=180)
    plt.close()

plot_topology(fusion_case, "persistent_fusion_topology.png")
plot_topology(fission_case, "fusion_fission_topology.png")
plot_topology(phase_blocked_case, "phase_blocked_topology.png")

plt.figure()
for case, label_text in (
    (fusion_case, "phase 0, slow"),
    (fission_case, "phase pi/2"),
    (phase_blocked_case, "phase pi"),
):
    plt.plot(
        case["times"],
        case["diagnostics"]["peak_density"],
        label=label_text,
    )
plt.xlabel("time")
plt.ylabel("peak density")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "phase_sensitive_peak_density.png", dpi=180)
plt.close()

# Four density snapshots for fission case
snapshot_keys = sorted(
    fission_case["snapshots"].keys(),
    key=float,
)
for key in snapshot_keys:
    plt.figure()
    plt.imshow(
        fission_case["snapshots"][key],
        origin="lower",
        extent=[
            -DOMAIN_L / 2.0,
            DOMAIN_L / 2.0,
            -DOMAIN_L / 2.0,
            DOMAIN_L / 2.0,
        ],
    )
    plt.colorbar(label="density")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.savefig(
        FIGURES / f"fission_density_t_{key}.png",
        dpi=180,
    )
    plt.close()

plt.figure()
conservation = conservation_summary(fission_case)
energy = fission_case["diagnostics"]["hamiltonian"]
plt.plot(
    fission_case["times"],
    (energy - energy[0]) / max(abs(energy[0]), 1e-14),
)
plt.xlabel("time")
plt.ylabel("relative Hamiltonian error")
plt.tight_layout()
plt.savefig(FIGURES / "hamiltonian_conservation.png", dpi=180)
plt.close()

# ============================================================
# Save tables
# ============================================================

with open(
    RESULTS / "fusion_fission_timeseries.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "time",
            "component_count",
            "norm",
            "hamiltonian",
            "momentum_x",
            "momentum_y",
            "angular_momentum",
            "peak_density",
        ]
    )
    for index, time in enumerate(fission_case["times"]):
        writer.writerow(
            [
                time,
                fission_case["component_counts"][index],
                fission_case["diagnostics"]["norm"][index],
                fission_case["diagnostics"]["hamiltonian"][index],
                fission_case["diagnostics"]["momentum_x"][index],
                fission_case["diagnostics"]["momentum_y"][index],
                fission_case["diagnostics"]["angular_momentum"][index],
                fission_case["diagnostics"]["peak_density"][index],
            ]
        )

with open(
    RESULTS / "component_observables.json",
    "w",
    encoding="utf-8",
) as file:
    json.dump(
        {
            "fusion_then_fission_initial": fission_case[
                "initial_components"
            ],
            "fusion_then_fission_final": fission_case[
                "final_components"
            ],
            "persistent_fusion_final": fusion_case[
                "final_components"
            ],
            "phase_blocked_final": phase_blocked_case[
                "final_components"
            ],
        },
        file,
        ensure_ascii=False,
        indent=2,
    )

case_summaries = {}
for case in (
    fusion_case,
    fission_case,
    phase_blocked_case,
):
    case_summaries[case["name"]] = {
        "topology_sequence": count_sequence(
            case["component_counts"]
        ),
        "initial_component_count": int(
            case["component_counts"][0]
        ),
        "minimum_component_count": int(
            np.min(case["component_counts"])
        ),
        "final_component_count": int(
            case["component_counts"][-1]
        ),
        "one_component_duration": interval_with_count(
            case, 1
        ),
        "conservation": conservation_summary(case),
        "initial_components": case["initial_components"],
        "final_components": case["final_components"],
    }

results = {
    "model": {
        "equation": (
            "i psi_t = -1/2 Delta psi "
            "- g |psi|^2 psi + h |psi|^4 psi"
        ),
        "g": G,
        "h": H6,
        "grid_n": GRID_N,
        "domain_length": DOMAIN_L,
        "dt": DT,
        "density_threshold": DENSITY_THRESHOLD,
        "minimum_component_pixels": MIN_COMPONENT_PIXELS,
    },
    "T1_continuum_structure": {
        "single_unlabeled_complex_field": True,
        "hamiltonian": True,
        "global_U1_norm_symmetry": True,
        "translation_symmetry": True,
        "rotation_symmetry": True,
        "time_reversal_map": "psi(x,t) -> conjugate(psi(x,-t))",
    },
    "T2_numerical_conservation": {
        "fusion_then_fission": conservation_summary(
            conservation_case
        ),
        "time_reversal_relative_L2_error": (
            time_reversal_relative_error
        ),
        "offcenter_angular_test": {
            "initial_angular_momentum": initial_angular,
            "angular_momentum_absolute_drift": (
                angular_summary[
                    "angular_momentum_absolute_drift"
                ]
            ),
            "angular_momentum_relative_drift": (
                angular_relative_drift
            ),
            "norm_relative_drift": angular_summary[
                "norm_relative_drift"
            ],
            "energy_relative_drift": angular_summary[
                "energy_relative_drift"
            ],
            "momentum_absolute_drift": angular_summary[
                "momentum_absolute_drift"
            ],
        },
    },
    "T3_topology_cases": case_summaries,
    "T4_unlabeled_reconstruction": {
        "incoming_components": len(
            fission_case["initial_components"]
        ),
        "single_component_interval_duration": (
            fission_one_component_duration
        ),
        "outgoing_components": len(
            fission_case["final_components"]
        ),
        "outgoing_superlevel_mass_ratio": (
            outgoing_superlevel_mass_ratio
        ),
        "outgoing_component_momentum_difference": (
            outgoing_momentum_difference
        ),
        "component_label_continuation": (
            "not canonically defined through the "
            "one-component interval"
        ),
        "full_field_information_status": (
            "retained by reversible field dynamics"
        ),
    },
    "T5_phase_sensitivity": {
        "phase_0_slow_sequence": fusion_sequence,
        "phase_pi_over_2_sequence": fission_sequence,
        "phase_pi_sequence": blocked_sequence,
        "interpretation": (
            "topology depends on relative field phase "
            "and impact speed in the tested window"
        ),
    },
    "T6_linear_control": {
        "linear_superposition_relative_error": (
            linear_superposition_relative_error
        ),
        "interpretation": (
            "the linear field is exactly the sum of "
            "separately evolved packets, unlike the "
            "nonlinear topology-changing cases"
        ),
    },
}

with open(
    RESULTS / "benchmark_results.json",
    "w",
    encoding="utf-8",
) as file:
    json.dump(results, file, ensure_ascii=False, indent=2)

print(json.dumps(results, ensure_ascii=False, indent=2))
