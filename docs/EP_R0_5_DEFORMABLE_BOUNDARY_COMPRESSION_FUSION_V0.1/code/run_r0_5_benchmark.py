
from pathlib import Path
import json
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.ndimage import label as connected_components

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
RESULTS.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)

MASS = np.array([1.0, 1.0])
SHAPE_MASS = 0.16
K_SHAPE = 18.0
K_AREA = 36.0
OVERLAP_STRENGTH = 16.0
COMPLEX_STEP = 1e-30

def rotation_matrix(theta):
    dtype = np.result_type(theta)
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=dtype)

def axes_from_beta(base_axes, beta):
    return np.asarray(base_axes, dtype=np.result_type(beta)) * np.exp(beta)

def shape_matrix(theta, base_axes, beta):
    axes = axes_from_beta(base_axes, beta)
    R = rotation_matrix(theta)
    return R @ np.diag(axes ** -2) @ R.T

def moment_of_inertia(mass, base_axes, beta):
    axes = axes_from_beta(base_axes, beta)
    return mass * np.sum(axes ** 2)

def overlap_integral(displacement, theta1, theta2, beta1, beta2, base_axes):
    A1 = shape_matrix(theta1, base_axes[0], beta1)
    A2 = shape_matrix(theta2, base_axes[1], beta2)
    S = A1 + A2
    invS = np.linalg.inv(S)
    C = A1 - A1 @ invS @ A1
    C = 0.5 * (C + C.T)
    displacement = np.asarray(
        displacement,
        dtype=np.result_type(theta1, theta2, beta1, beta2),
    )
    return (
        2.0 * np.pi
        / np.sqrt(np.linalg.det(S))
        * np.exp(-0.5 * displacement @ (C @ displacement))
    )

def overlap_energy(displacement, theta1, theta2, beta1, beta2, base_axes):
    return OVERLAP_STRENGTH * overlap_integral(
        displacement, theta1, theta2, beta1, beta2, base_axes
    )

def normalized_overlap(displacement, theta1, theta2, beta1, beta2, base_axes):
    overlap = overlap_integral(
        displacement, theta1, theta2, beta1, beta2, base_axes
    )
    A1 = shape_matrix(theta1, base_axes[0], beta1)
    A2 = shape_matrix(theta2, base_axes[1], beta2)
    self1 = np.pi / np.sqrt(np.linalg.det(A1))
    self2 = np.pi / np.sqrt(np.linalg.det(A2))
    return float(np.real(overlap / np.sqrt(self1 * self2)))

def shape_potential(beta):
    beta = np.asarray(beta)
    return (
        0.5 * K_SHAPE * np.sum(beta ** 2)
        + 0.5 * K_AREA
        * ((beta[0] + beta[1]) ** 2 + (beta[2] + beta[3]) ** 2)
    )

def shape_potential_gradient(beta):
    beta = np.asarray(beta)
    gradient = K_SHAPE * beta.copy()
    gradient[0:2] += K_AREA * np.sum(beta[0:2])
    gradient[2:4] += K_AREA * np.sum(beta[2:4])
    return gradient

def interaction_derivatives(displacement, theta1, theta2, beta1, beta2, base_axes):
    A1 = shape_matrix(theta1, base_axes[0], beta1)
    A2 = shape_matrix(theta2, base_axes[1], beta2)
    S = A1 + A2
    C = A1 - A1 @ np.linalg.inv(S) @ A1
    C = 0.5 * (C + C.T)
    energy = overlap_energy(
        displacement, theta1, theta2, beta1, beta2, base_axes
    )
    force1 = np.real(energy * (C @ displacement))

    torque1 = -np.imag(
        overlap_energy(
            displacement,
            theta1 + 1j * COMPLEX_STEP,
            theta2,
            beta1,
            beta2,
            base_axes,
        )
    ) / COMPLEX_STEP
    torque2 = -np.imag(
        overlap_energy(
            displacement,
            theta1,
            theta2 + 1j * COMPLEX_STEP,
            beta1,
            beta2,
            base_axes,
        )
    ) / COMPLEX_STEP

    beta_gradient = np.zeros(4)
    for index in range(4):
        beta1_complex = np.array(beta1, dtype=complex)
        beta2_complex = np.array(beta2, dtype=complex)
        if index < 2:
            beta1_complex[index] += 1j * COMPLEX_STEP
        else:
            beta2_complex[index - 2] += 1j * COMPLEX_STEP
        beta_gradient[index] = np.imag(
            overlap_energy(
                displacement,
                theta1,
                theta2,
                beta1_complex,
                beta2_complex,
                base_axes,
            )
        ) / COMPLEX_STEP

    return (
        float(np.real(energy)),
        force1,
        float(torque1),
        float(torque2),
        beta_gradient,
    )

def unpack(state):
    return {
        "x1": state[0:2],
        "x2": state[2:4],
        "theta1": state[4],
        "theta2": state[5],
        "beta": state[6:10],
        "p1": state[10:12],
        "p2": state[12:14],
        "L1": state[14],
        "L2": state[15],
        "pi": state[16:20],
    }

def equations(time, state, base_axes):
    values = unpack(state)
    beta1 = values["beta"][0:2]
    beta2 = values["beta"][2:4]
    displacement = values["x1"] - values["x2"]

    _, force1, torque1, torque2, beta_u_gradient = interaction_derivatives(
        displacement,
        values["theta1"],
        values["theta2"],
        beta1,
        beta2,
        base_axes,
    )

    I1 = moment_of_inertia(MASS[0], base_axes[0], beta1)
    I2 = moment_of_inertia(MASS[1], base_axes[1], beta2)
    shape_gradient = shape_potential_gradient(values["beta"])

    axes1 = axes_from_beta(base_axes[0], beta1)
    axes2 = axes_from_beta(base_axes[1], beta2)
    rotational_beta_force = np.zeros(4)
    rotational_beta_force[0:2] = (
        values["L1"] ** 2 * MASS[0] * axes1 ** 2 / I1 ** 2
    )
    rotational_beta_force[2:4] = (
        values["L2"] ** 2 * MASS[1] * axes2 ** 2 / I2 ** 2
    )

    derivative = np.zeros_like(state)
    derivative[0:2] = values["p1"] / MASS[0]
    derivative[2:4] = values["p2"] / MASS[1]
    derivative[4] = values["L1"] / I1
    derivative[5] = values["L2"] / I2
    derivative[6:10] = values["pi"] / SHAPE_MASS
    derivative[10:12] = force1
    derivative[12:14] = -force1
    derivative[14] = torque1
    derivative[15] = torque2
    derivative[16:20] = (
        -shape_gradient - beta_u_gradient + rotational_beta_force
    )
    return derivative

def energy_channels(state, base_axes):
    values = unpack(state)
    beta1 = values["beta"][0:2]
    beta2 = values["beta"][2:4]
    I1 = moment_of_inertia(MASS[0], base_axes[0], beta1)
    I2 = moment_of_inertia(MASS[1], base_axes[1], beta2)
    interaction = float(
        np.real(
            overlap_energy(
                values["x1"] - values["x2"],
                values["theta1"],
                values["theta2"],
                beta1,
                beta2,
                base_axes,
            )
        )
    )
    translational = (
        np.dot(values["p1"], values["p1"]) / (2.0 * MASS[0])
        + np.dot(values["p2"], values["p2"]) / (2.0 * MASS[1])
    )
    rotational = (
        values["L1"] ** 2 / (2.0 * I1)
        + values["L2"] ** 2 / (2.0 * I2)
    )
    shape_kinetic = np.dot(values["pi"], values["pi"]) / (2.0 * SHAPE_MASS)
    shape_elastic = shape_potential(values["beta"])
    total = (
        translational
        + rotational
        + shape_kinetic
        + shape_elastic
        + interaction
    )
    return {
        "translation": float(translational),
        "rotation": float(rotational),
        "shape_kinetic": float(shape_kinetic),
        "shape_elastic": float(shape_elastic),
        "interaction": float(interaction),
        "total": float(total),
    }

def total_linear_momentum(state):
    values = unpack(state)
    return values["p1"] + values["p2"]

def cross2(a, b):
    return a[0] * b[1] - a[1] * b[0]

def total_angular_momentum(state):
    values = unpack(state)
    return float(
        cross2(values["x1"], values["p1"])
        + cross2(values["x2"], values["p2"])
        + values["L1"] + values["L2"]
    )

def integrate_collision(initial_state, base_axes, final_time, samples):
    solution = solve_ivp(
        lambda t, y: equations(t, y, base_axes),
        (0.0, final_time),
        initial_state,
        method="DOP853",
        rtol=2e-10,
        atol=2e-12,
        max_step=0.015,
        dense_output=True,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    times = np.linspace(0.0, final_time, samples)
    return solution, times, solution.sol(times)

def make_initial_state(positions, velocities, angles):
    state = np.zeros(20)
    state[0:2] = positions[0]
    state[2:4] = positions[1]
    state[4:6] = angles
    state[10:12] = MASS[0] * np.asarray(velocities[0])
    state[12:14] = MASS[1] * np.asarray(velocities[1])
    return state

# T1
rng = np.random.default_rng(20260722)
base_axes_test = np.array([[1.0, 0.62], [0.92, 0.54]])
minimum_axis = np.inf
maximum_beta_gradient_relative_error = 0.0
for _ in range(100):
    beta = rng.uniform(-0.45, 0.35, size=4)
    theta1, theta2 = rng.uniform(-1.0, 1.0, size=2)
    displacement = rng.uniform(-1.5, 1.5, size=2)
    axes = np.concatenate(
        (
            axes_from_beta(base_axes_test[0], beta[0:2]),
            axes_from_beta(base_axes_test[1], beta[2:4]),
        )
    )
    minimum_axis = min(minimum_axis, float(np.min(axes)))
    _, _, _, _, gradient_complex = interaction_derivatives(
        displacement,
        theta1,
        theta2,
        beta[0:2],
        beta[2:4],
        base_axes_test,
    )
    step = 2e-6
    gradient_fd = np.zeros(4)
    for index in range(4):
        plus = beta.copy()
        minus = beta.copy()
        plus[index] += step
        minus[index] -= step
        gradient_fd[index] = (
            overlap_energy(
                displacement,
                theta1,
                theta2,
                plus[0:2],
                plus[2:4],
                base_axes_test,
            )
            - overlap_energy(
                displacement,
                theta1,
                theta2,
                minus[0:2],
                minus[2:4],
                base_axes_test,
            )
        ) / (2.0 * step)
    relative_error = np.linalg.norm(
        gradient_complex - gradient_fd
    ) / max(np.linalg.norm(gradient_complex), 1e-8)
    maximum_beta_gradient_relative_error = max(
        maximum_beta_gradient_relative_error,
        float(relative_error),
    )

# Off-center collision
base_axes_offcenter = np.array([[1.0, 0.62], [0.92, 0.56]])
initial_offcenter = make_initial_state(
    positions=[[-3.2, -0.42], [3.2, 0.42]],
    velocities=[[1.10, 0.0], [-1.10, 0.0]],
    angles=[0.27, -0.34],
)
_, times, states = integrate_collision(
    initial_offcenter, base_axes_offcenter, 9.0, 1401
)

channel_names = (
    "translation",
    "rotation",
    "shape_kinetic",
    "shape_elastic",
    "interaction",
    "total",
)
channels = {
    name: np.array(
        [
            energy_channels(states[:, i], base_axes_offcenter)[name]
            for i in range(times.size)
        ]
    )
    for name in channel_names
}
momenta = np.array(
    [total_linear_momentum(states[:, i]) for i in range(times.size)]
)
angular_momenta = np.array(
    [total_angular_momentum(states[:, i]) for i in range(times.size)]
)

relative_energy_drift = float(
    np.max(np.abs(channels["total"] - channels["total"][0]))
    / abs(channels["total"][0])
)
linear_momentum_drift = float(
    np.max(np.linalg.norm(momenta - momenta[0], axis=1))
)
angular_momentum_drift = float(
    np.max(np.abs(angular_momenta - angular_momenta[0]))
)

final_state = states[:, -1].copy()
reversed_state = final_state.copy()
reversed_state[10:16] *= -1.0
reversed_state[16:20] *= -1.0
back_solution = solve_ivp(
    lambda t, y: equations(t, y, base_axes_offcenter),
    (0.0, 9.0),
    reversed_state,
    method="DOP853",
    rtol=2e-10,
    atol=2e-12,
    max_step=0.015,
)
recovered_state = back_solution.y[:, -1]
target_state = initial_offcenter.copy()
target_state[10:16] *= -1.0
target_state[16:20] *= -1.0
time_reversal_error = float(np.linalg.norm(recovered_state - target_state))

all_axes = []
overlaps = []
forces = []
for i in range(times.size):
    values = unpack(states[:, i])
    beta1 = values["beta"][0:2]
    beta2 = values["beta"][2:4]
    all_axes.extend(axes_from_beta(base_axes_offcenter[0], beta1).tolist())
    all_axes.extend(axes_from_beta(base_axes_offcenter[1], beta2).tolist())
    overlaps.append(
        normalized_overlap(
            values["x1"] - values["x2"],
            values["theta1"],
            values["theta2"],
            beta1,
            beta2,
            base_axes_offcenter,
        )
    )
    _, force1, _, _, _ = interaction_derivatives(
        values["x1"] - values["x2"],
        values["theta1"],
        values["theta2"],
        beta1,
        beta2,
        base_axes_offcenter,
    )
    forces.append(np.linalg.norm(force1))
all_axes = np.asarray(all_axes)
overlaps = np.asarray(overlaps)
forces = np.asarray(forces)

shape_energy = channels["shape_kinetic"] + channels["shape_elastic"]
maximum_shape_energy = float(np.max(shape_energy))
maximum_rotational_energy = float(np.max(channels["rotation"]))
maximum_interaction_energy = float(np.max(channels["interaction"]))
maximum_spin_transfer = float(
    np.max(np.abs(states[14:16, :] - states[14:16, [0]]))
)
minimum_axis_during_collision = float(np.min(all_axes))

collision_threshold = 1e-3
collision_indices = np.flatnonzero(overlaps > collision_threshold)
collision_entry_time = float(times[collision_indices[0]])
collision_exit_time = float(times[collision_indices[-1]])
collision_duration = collision_exit_time - collision_entry_time
post_mask = times > collision_exit_time
post_collision_mean_shape_energy = float(np.mean(shape_energy[post_mask]))
post_collision_shape_fraction = float(
    post_collision_mean_shape_energy / maximum_shape_energy
)
memory_fraction_threshold = 0.005
memory_mask = post_mask & (shape_energy > memory_fraction_threshold * maximum_shape_energy)
compression_memory_duration = (
    float(times[np.flatnonzero(memory_mask)[-1]] - collision_exit_time)
    if np.any(memory_mask)
    else 0.0
)

# Fast/slow centered runs
base_axes_centered = np.array([[0.86, 0.86], [0.86, 0.86]])

def centered_run(speed, final_time):
    initial = make_initial_state(
        positions=[[-3.0, 0.0], [3.0, 0.0]],
        velocities=[[speed, 0.0], [-speed, 0.0]],
        angles=[0.0, 0.0],
    )
    _, run_times, run_states = integrate_collision(
        initial, base_axes_centered, final_time, 1001
    )
    force = []
    shape_e = []
    beta_sum = []
    for i in range(run_times.size):
        values = unpack(run_states[:, i])
        beta1 = values["beta"][0:2]
        beta2 = values["beta"][2:4]
        _, force1, _, _, _ = interaction_derivatives(
            values["x1"] - values["x2"],
            values["theta1"],
            values["theta2"],
            beta1,
            beta2,
            base_axes_centered,
        )
        force.append(np.linalg.norm(force1))
        channel = energy_channels(run_states[:, i], base_axes_centered)
        shape_e.append(channel["shape_kinetic"] + channel["shape_elastic"])
        beta_sum.append(np.sum(values["beta"]))
    return {
        "times": run_times,
        "states": run_states,
        "force": np.asarray(force),
        "shape_energy": np.asarray(shape_e),
        "beta_sum": np.asarray(beta_sum),
    }

slow_run = centered_run(0.65, 11.0)
fast_run = centered_run(1.30, 6.5)
slow_peak_force = float(np.max(slow_run["force"]))
fast_peak_force = float(np.max(fast_run["force"]))
slow_peak_shape_energy = float(np.max(slow_run["shape_energy"]))
fast_peak_shape_energy = float(np.max(fast_run["shape_energy"]))
dynamic_repulsion_force_ratio = fast_peak_force / slow_peak_force
dynamic_shape_energy_ratio = fast_peak_shape_energy / slow_peak_shape_energy
slow_max_compression = float(-np.min(slow_run["beta_sum"]))
fast_max_compression = float(-np.min(fast_run["beta_sum"]))

# Unlabeled topology diagnostic
topology_threshold = 0.10
sample_indices = np.linspace(0, times.size - 1, 181, dtype=int)
def phase_field(points, center, theta, base_axes, beta):
    A = shape_matrix(theta, base_axes, beta)
    shifted = points - center
    quadratic = np.einsum("...i,ij,...j->...", shifted, A, shifted)
    return np.exp(-0.5 * quadratic)

component_counts = []
topology_times = []
for i in sample_indices:
    values = unpack(states[:, i])
    axes1_now = axes_from_beta(base_axes_offcenter[0], values["beta"][0:2])
    axes2_now = axes_from_beta(base_axes_offcenter[1], values["beta"][2:4])
    margin = 3.5 * max(np.max(axes1_now), np.max(axes2_now))
    xmin = min(values["x1"][0], values["x2"][0]) - margin
    xmax = max(values["x1"][0], values["x2"][0]) + margin
    ymin = min(values["x1"][1], values["x2"][1]) - margin
    ymax = max(values["x1"][1], values["x2"][1]) + margin
    grid_x = np.linspace(xmin, xmax, 301)
    grid_y = np.linspace(ymin, ymax, 181)
    GX, GY = np.meshgrid(grid_x, grid_y, indexing="xy")
    grid_points = np.stack((GX, GY), axis=-1)
    chi1 = phase_field(
        grid_points,
        values["x1"],
        values["theta1"],
        base_axes_offcenter[0],
        values["beta"][0:2],
    )
    chi2 = phase_field(
        grid_points,
        values["x2"],
        values["theta2"],
        base_axes_offcenter[1],
        values["beta"][2:4],
    )
    union = 1.0 - (1.0 - chi1) * (1.0 - chi2)
    binary = union >= topology_threshold
    labels, count = connected_components(
        binary,
        structure=np.array([[0,1,0],[1,1,1],[0,1,0]]),
    )
    retained = 0
    for component in range(1, count + 1):
        if np.sum(labels == component) >= 20:
            retained += 1
    component_counts.append(retained)
    topology_times.append(times[i])

component_counts = np.asarray(component_counts)
topology_times = np.asarray(topology_times)
initial_components = int(component_counts[0])
minimum_components = int(np.min(component_counts))
final_components = int(component_counts[-1])
fusion_mask = component_counts == 1
fusion_duration = (
    float(
        topology_times[np.flatnonzero(fusion_mask)[-1]]
        - topology_times[np.flatnonzero(fusion_mask)[0]]
    )
    if np.any(fusion_mask)
    else 0.0
)
if initial_components == 2 and minimum_components == 1 and final_components == 2:
    topology_classification = "temporary_geometric_fusion_then_scattering"
elif final_components == 1:
    topology_classification = "persistent_geometric_fusion_candidate"
else:
    topology_classification = "no_geometric_fusion_or_unresolved"

final_values = unpack(states[:, -1])
final_displacement = final_values["x1"] - final_values["x2"]
final_relative_velocity = (
    final_values["p1"] / MASS[0] - final_values["p2"] / MASS[1]
)
final_radial_velocity = float(
    np.dot(final_displacement, final_relative_velocity)
    / np.linalg.norm(final_displacement)
)
scattering_classification = (
    "labeled_scattering"
    if overlaps[-1] < collision_threshold and final_radial_velocity > 0.0
    else "persistent_overlap_or_unresolved"
)

# Figures
plt.figure()
plt.plot(times, channels["translation"], label="translation")
plt.plot(times, channels["rotation"], label="rotation")
plt.plot(times, shape_energy, label="shape")
plt.plot(times, channels["interaction"], label="overlap")
plt.xlabel("time")
plt.ylabel("energy channel")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "energy_channel_exchange.png", dpi=180)
plt.close()

plt.figure()
for row, label_name in zip(range(6, 10), ["beta1a","beta1b","beta2a","beta2b"]):
    plt.plot(times, states[row, :], label=label_name)
plt.axvline(collision_exit_time, linestyle="--", label="collision exit")
plt.xlabel("time")
plt.ylabel("log-shape coordinate")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "compression_memory.png", dpi=180)
plt.close()

plt.figure()
plt.plot(slow_run["times"], slow_run["force"], label="slow approach")
plt.plot(fast_run["times"], fast_run["force"], label="fast approach")
plt.xlabel("time")
plt.ylabel("normal force magnitude")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "dynamic_repulsion.png", dpi=180)
plt.close()

plt.figure()
plt.step(topology_times, component_counts, where="mid")
plt.xlabel("time")
plt.ylabel("connected components")
plt.yticks([1, 2])
plt.tight_layout()
plt.savefig(FIGURES / "unlabeled_topology_components.png", dpi=180)
plt.close()

plt.figure()
plt.plot(states[0, :], states[1, :], label="S0-1")
plt.plot(states[2, :], states[3, :], label="S0-2")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "deformable_collision_trajectories.png", dpi=180)
plt.close()

with open(RESULTS / "deformable_collision_timeseries.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "time","x1","y1","x2","y2","theta1","theta2",
        "beta1a","beta1b","beta2a","beta2b","L1","L2",
        "overlap","translation_energy","rotation_energy",
        "shape_energy","interaction_energy","total_energy"
    ])
    for i, time in enumerate(times):
        writer.writerow([
            time, states[0,i], states[1,i], states[2,i], states[3,i],
            states[4,i], states[5,i], states[6,i], states[7,i],
            states[8,i], states[9,i], states[14,i], states[15,i],
            overlaps[i], channels["translation"][i], channels["rotation"][i],
            shape_energy[i], channels["interaction"][i], channels["total"][i]
        ])

results = {
    "T1_shape_coordinates": {
        "minimum_axis_in_random_positive_parameter_test": float(minimum_axis),
        "maximum_beta_gradient_relative_error": float(maximum_beta_gradient_relative_error),
    },
    "T2_hamilton_ledger": {
        "relative_energy_drift": relative_energy_drift,
        "linear_momentum_drift": linear_momentum_drift,
        "angular_momentum_drift": angular_momentum_drift,
        "time_reversal_state_error": time_reversal_error,
        "minimum_axis_during_collision": minimum_axis_during_collision,
    },
    "T3_energy_exchange": {
        "maximum_shape_energy": maximum_shape_energy,
        "maximum_rotational_energy": maximum_rotational_energy,
        "maximum_interaction_energy": maximum_interaction_energy,
        "maximum_spin_transfer": maximum_spin_transfer,
    },
    "T4_compression_memory": {
        "collision_entry_time": collision_entry_time,
        "collision_exit_time": collision_exit_time,
        "collision_duration": collision_duration,
        "post_collision_mean_shape_energy": post_collision_mean_shape_energy,
        "post_collision_shape_fraction_of_peak": post_collision_shape_fraction,
        "memory_fraction_threshold": memory_fraction_threshold,
        "compression_memory_duration_above_threshold": compression_memory_duration,
    },
    "T5_dynamic_repulsion": {
        "slow_speed": 0.65,
        "fast_speed": 1.30,
        "slow_peak_force": slow_peak_force,
        "fast_peak_force": fast_peak_force,
        "force_ratio_fast_over_slow": dynamic_repulsion_force_ratio,
        "slow_peak_shape_energy": slow_peak_shape_energy,
        "fast_peak_shape_energy": fast_peak_shape_energy,
        "shape_energy_ratio_fast_over_slow": dynamic_shape_energy_ratio,
        "slow_max_compression": slow_max_compression,
        "fast_max_compression": fast_max_compression,
    },
    "T6_unlabeled_topology": {
        "threshold": topology_threshold,
        "initial_connected_components": initial_components,
        "minimum_connected_components": minimum_components,
        "final_connected_components": final_components,
        "temporary_one_component_duration": fusion_duration,
        "classification": topology_classification,
        "identity_reconstruction_status": "open_because_dynamics_retains_two_canonical_objects",
    },
    "T7_scattering": {
        "maximum_normalized_overlap": float(np.max(overlaps)),
        "final_normalized_overlap": float(overlaps[-1]),
        "final_radial_velocity": final_radial_velocity,
        "classification": scattering_classification,
    },
}

with open(RESULTS / "benchmark_results.json", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=2)

print(json.dumps(results, ensure_ascii=False, indent=2))
