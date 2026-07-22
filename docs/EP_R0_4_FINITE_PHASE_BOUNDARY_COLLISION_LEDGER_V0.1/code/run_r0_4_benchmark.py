from pathlib import Path
import json
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
RESULTS.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)

# ---------- quaternion and phase-boundary helpers ----------
def qmul(a, b):
    aw, av = a[0], a[1:]
    bw, bv = b[0], b[1:]
    return np.concatenate(
        (
            [aw * bw - np.dot(av, bv)],
            aw * bv + bw * av + np.cross(av, bv),
        )
    )

def qconj(q):
    return np.concatenate(([q[0]], -q[1:]))

def q_from_theta(theta):
    return np.array(
        [np.cos(theta / 2.0), 0.0, 0.0, np.sin(theta / 2.0)]
    )

def rotate_vector(q, v):
    return qmul(qmul(q, np.concatenate(([0.0], v))), qconj(q))[1:]

def rotation_matrix(theta):
    dtype = np.result_type(theta)
    c = np.cos(theta)
    s = np.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=dtype)

def shape_matrix(theta, a, b):
    R = rotation_matrix(theta)
    D = np.diag([1.0 / a**2, 1.0 / b**2]).astype(
        np.result_type(theta)
    )
    return R @ D @ R.T

def phase_value(points, center, theta, a, b):
    A = shape_matrix(theta, a, b)
    shifted = points - np.asarray(center)
    quadratic = np.einsum(
        "...i,ij,...j->...", shifted, A, shifted
    )
    return np.exp(-0.5 * quadratic)

def boundary_tensor_analytic(theta, a, b):
    A = shape_matrix(theta, a, b)
    return np.pi * A / (2.0 * np.sqrt(np.linalg.det(A)))

def anisotropy_factor(B):
    normalized = B / np.trace(B) - np.eye(2) / 2.0
    return float(np.sqrt(2.0) * np.linalg.norm(normalized))

# ---------- overlap energy ----------
def overlap_integral(displacement, theta1, theta2, parameters):
    a1, b1, a2, b2, _ = parameters
    A1 = shape_matrix(theta1, a1, b1)
    A2 = shape_matrix(theta2, a2, b2)
    S = A1 + A2
    inverse_S = np.linalg.inv(S)
    C = A1 - A1 @ inverse_S @ A1
    C = 0.5 * (C + C.T)
    displacement = np.asarray(
        displacement, dtype=np.result_type(theta1, theta2)
    )
    return (
        2.0
        * np.pi
        / np.sqrt(np.linalg.det(S))
        * np.exp(-0.5 * displacement @ (C @ displacement))
    )

def overlap_energy(displacement, theta1, theta2, parameters):
    return parameters[-1] * overlap_integral(
        displacement, theta1, theta2, parameters
    )

def normalized_overlap(displacement, theta1, theta2, parameters):
    a1, b1, a2, b2, _ = parameters
    overlap = overlap_integral(
        displacement, theta1, theta2, parameters
    )
    A1 = shape_matrix(theta1, a1, b1)
    A2 = shape_matrix(theta2, a2, b2)
    self1 = np.pi / np.sqrt(np.linalg.det(A1))
    self2 = np.pi / np.sqrt(np.linalg.det(A2))
    return float(np.real(overlap / np.sqrt(self1 * self2)))

def force_and_torques(displacement, theta1, theta2, parameters):
    a1, b1, a2, b2, _ = parameters
    A1 = shape_matrix(theta1, a1, b1)
    A2 = shape_matrix(theta2, a2, b2)
    S = A1 + A2
    C = A1 - A1 @ np.linalg.inv(S) @ A1
    C = 0.5 * (C + C.T)
    energy = overlap_energy(
        displacement, theta1, theta2, parameters
    )
    force1 = np.real(energy * (C @ displacement))

    complex_step = 1e-30
    torque1 = -np.imag(
        overlap_energy(
            displacement,
            theta1 + 1j * complex_step,
            theta2,
            parameters,
        )
    ) / complex_step
    torque2 = -np.imag(
        overlap_energy(
            displacement,
            theta1,
            theta2 + 1j * complex_step,
            parameters,
        )
    ) / complex_step
    return (
        float(np.real(energy)),
        force1,
        float(torque1),
        float(torque2),
    )

# ---------- T1 geometry extraction ----------
a_geometry = 1.1
b_geometry = 0.55
theta_geometry = 0.37
center_geometry = np.array([0.2, -0.1])
grid_size = 601
grid_limit = 6.0
axis = np.linspace(-grid_limit, grid_limit, grid_size)
dx = axis[1] - axis[0]
X, Y = np.meshgrid(axis, axis, indexing="xy")
points = np.stack((X, Y), axis=-1)
chi = phase_value(
    points,
    center_geometry,
    theta_geometry,
    a_geometry,
    b_geometry,
)
volume_numeric = float(np.sum(chi) * dx * dx)
volume_analytic = float(2.0 * np.pi * a_geometry * b_geometry)
centroid_numeric = np.array(
    [
        np.sum(chi * X) * dx * dx / volume_numeric,
        np.sum(chi * Y) * dx * dx / volume_numeric,
    ]
)
shifted = points - centroid_numeric
flat_shifted = shifted.reshape(-1, 2)
flat_chi = chi.reshape(-1)
shape_moment_numeric = (
    flat_shifted.T
    @ (flat_chi[:, None] * flat_shifted)
    * dx
    * dx
    / volume_numeric
)
A_geometry = shape_matrix(
    theta_geometry, a_geometry, b_geometry
)
shape_moment_analytic = np.linalg.inv(A_geometry)
grad_chi = (
    -np.einsum(
        "ij,...j->...i",
        A_geometry,
        points - center_geometry,
    )
    * chi[..., None]
)
flat_grad = grad_chi.reshape(-1, 2)
boundary_tensor_numeric = flat_grad.T @ flat_grad * dx * dx
boundary_tensor_exact = boundary_tensor_analytic(
    theta_geometry, a_geometry, b_geometry
)

volume_relative_error = float(
    abs(volume_numeric - volume_analytic) / volume_analytic
)
centroid_error = float(
    np.linalg.norm(centroid_numeric - center_geometry)
)
shape_moment_relative_error = float(
    np.linalg.norm(shape_moment_numeric - shape_moment_analytic)
    / np.linalg.norm(shape_moment_analytic)
)
boundary_tensor_relative_error = float(
    np.linalg.norm(boundary_tensor_numeric - boundary_tensor_exact)
    / np.linalg.norm(boundary_tensor_exact)
)

circle_factor = anisotropy_factor(
    boundary_tensor_analytic(0.4, 0.8, 0.8)
)
ellipse_factor = anisotropy_factor(boundary_tensor_exact)

plt.figure()
plt.contour(
    X,
    Y,
    chi,
    levels=[np.exp(-0.5)],
)
plt.scatter(
    [center_geometry[0]],
    [center_geometry[1]],
    label="centroid",
)
plt.axis("equal")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "finite_phase_boundary.png", dpi=180)
plt.close()

# ---------- T2 force and torque gradients ----------
rng = np.random.default_rng(20260722)
parameters_gradient = (1.0, 0.58, 0.9, 0.47, 7.0)
force_errors = []
torque_errors = []
for _ in range(120):
    displacement = rng.uniform(-1.6, 1.6, size=2)
    if np.linalg.norm(displacement) < 0.25:
        displacement[0] += 0.4
    theta1 = rng.uniform(-1.0, 1.0)
    theta2 = rng.uniform(-1.0, 1.0)
    energy, force1, torque1, torque2 = force_and_torques(
        displacement, theta1, theta2, parameters_gradient
    )
    step = 1e-6

    force_fd = np.empty(2)
    for component in range(2):
        shift = np.zeros(2)
        shift[component] = step
        derivative = (
            overlap_energy(
                displacement + shift,
                theta1,
                theta2,
                parameters_gradient,
            )
            - overlap_energy(
                displacement - shift,
                theta1,
                theta2,
                parameters_gradient,
            )
        ) / (2.0 * step)
        force_fd[component] = -derivative

    torque1_fd = -(
        overlap_energy(
            displacement,
            theta1 + step,
            theta2,
            parameters_gradient,
        )
        - overlap_energy(
            displacement,
            theta1 - step,
            theta2,
            parameters_gradient,
        )
    ) / (2.0 * step)
    torque2_fd = -(
        overlap_energy(
            displacement,
            theta1,
            theta2 + step,
            parameters_gradient,
        )
        - overlap_energy(
            displacement,
            theta1,
            theta2 - step,
            parameters_gradient,
        )
    ) / (2.0 * step)

    force_errors.append(
        np.linalg.norm(force1 - force_fd)
        / max(np.linalg.norm(force1), 1e-8)
    )
    torque_scale = max(
        abs(torque1), abs(torque2), 1e-8
    )
    torque_errors.append(
        max(
            abs(torque1 - torque1_fd),
            abs(torque2 - torque2_fd),
        )
        / torque_scale
    )

maximum_force_relative_error = float(max(force_errors))
maximum_torque_relative_error = float(max(torque_errors))

# ---------- T3/T4 invariance and local ledgers ----------
rotation_errors = []
angular_ledger_residuals = []
stress_couple_residuals = []
control_volume = 2.7
for _ in range(1000):
    displacement = rng.uniform(-2.0, 2.0, size=2)
    theta1 = rng.uniform(-np.pi, np.pi)
    theta2 = rng.uniform(-np.pi, np.pi)
    phi = rng.uniform(-np.pi, np.pi)
    parameters = (
        rng.uniform(0.7, 1.2),
        rng.uniform(0.35, 0.65),
        rng.uniform(0.7, 1.2),
        rng.uniform(0.35, 0.65),
        rng.uniform(2.0, 10.0),
    )
    energy, force1, torque1, torque2 = force_and_torques(
        displacement, theta1, theta2, parameters
    )
    R = rotation_matrix(phi)
    rotated_energy = overlap_energy(
        R @ displacement,
        theta1 + phi,
        theta2 + phi,
        parameters,
    )
    rotation_errors.append(
        abs(rotated_energy - energy) / max(abs(energy), 1e-12)
    )
    orbital_torque = (
        displacement[0] * force1[1]
        - displacement[1] * force1[0]
    )
    angular_ledger_residuals.append(
        abs(orbital_torque + torque1 + torque2)
    )

    pair_stress = -np.outer(displacement, force1) / control_volume
    stress_couple_residuals.append(
        abs(
            control_volume
            * (pair_stress[0, 1] - pair_stress[1, 0])
            - (torque1 + torque2)
        )
    )

maximum_rotation_invariance_error = float(max(rotation_errors))
maximum_angular_ledger_residual = float(
    max(angular_ledger_residuals)
)
maximum_stress_couple_residual = float(
    max(stress_couple_residuals)
)

# ---------- Hamilton dynamics ----------
m1 = 1.0
m2 = 1.0
I1 = 0.4
I2 = 0.35

def equations(time, state, parameters):
    x1 = state[0:2]
    x2 = state[2:4]
    theta1 = state[4]
    theta2 = state[5]
    p1 = state[6:8]
    p2 = state[8:10]
    L1 = state[10]
    L2 = state[11]

    _, force1, torque1, torque2 = force_and_torques(
        x1 - x2, theta1, theta2, parameters
    )

    derivative = np.zeros_like(state)
    derivative[0:2] = p1 / m1
    derivative[2:4] = p2 / m2
    derivative[4] = L1 / I1
    derivative[5] = L2 / I2
    derivative[6:8] = force1
    derivative[8:10] = -force1
    derivative[10] = torque1
    derivative[11] = torque2
    return derivative

def total_energy(state, parameters):
    x1 = state[0:2]
    x2 = state[2:4]
    theta1 = state[4]
    theta2 = state[5]
    p1 = state[6:8]
    p2 = state[8:10]
    L1 = state[10]
    L2 = state[11]
    return float(
        np.dot(p1, p1) / (2.0 * m1)
        + np.dot(p2, p2) / (2.0 * m2)
        + L1**2 / (2.0 * I1)
        + L2**2 / (2.0 * I2)
        + overlap_energy(
            x1 - x2, theta1, theta2, parameters
        )
    )

def total_linear_momentum(state):
    return state[6:8] + state[8:10]

def cross2(a, b):
    return a[0] * b[1] - a[1] * b[0]

def total_angular_momentum(state):
    return float(
        cross2(state[0:2], state[6:8])
        + cross2(state[2:4], state[8:10])
        + state[10]
        + state[11]
    )

parameters_collision = (1.0, 0.55, 0.9, 0.5, 10.0)
initial_state = np.zeros(12)
initial_state[0:2] = [-3.0, -0.45]
initial_state[2:4] = [3.0, 0.45]
initial_state[4] = 0.25
initial_state[5] = -0.30
initial_state[6:8] = [1.2, 0.0]
initial_state[8:10] = [-1.2, 0.0]

final_time = 8.0
solution = solve_ivp(
    lambda t, y: equations(t, y, parameters_collision),
    (0.0, final_time),
    initial_state,
    method="DOP853",
    rtol=1e-11,
    atol=1e-13,
    max_step=0.02,
    dense_output=True,
)
times = np.linspace(0.0, final_time, 1001)
states = solution.sol(times)

energies = np.array(
    [
        total_energy(states[:, index], parameters_collision)
        for index in range(times.size)
    ]
)
momenta = np.array(
    [
        total_linear_momentum(states[:, index])
        for index in range(times.size)
    ]
)
angular_momenta = np.array(
    [
        total_angular_momentum(states[:, index])
        for index in range(times.size)
    ]
)
overlaps = np.array(
    [
        normalized_overlap(
            states[0:2, index] - states[2:4, index],
            states[4, index],
            states[5, index],
            parameters_collision,
        )
        for index in range(times.size)
    ]
)
distances = np.linalg.norm(
    states[0:2, :] - states[2:4, :],
    axis=0,
)

relative_energy_drift = float(
    np.max(np.abs(energies - energies[0])) / abs(energies[0])
)
linear_momentum_drift = float(
    np.max(
        np.linalg.norm(
            momenta - momenta[0],
            axis=1,
        )
    )
)
angular_momentum_drift = float(
    np.max(np.abs(angular_momenta - angular_momenta[0]))
)

final_state = states[:, -1].copy()
reversed_final_state = final_state.copy()
reversed_final_state[6:10] *= -1.0
reversed_final_state[10:12] *= -1.0

backward_solution = solve_ivp(
    lambda t, y: equations(t, y, parameters_collision),
    (0.0, final_time),
    reversed_final_state,
    method="DOP853",
    rtol=1e-11,
    atol=1e-13,
    max_step=0.02,
)
recovered_state = backward_solution.y[:, -1]
reversal_target = initial_state.copy()
reversal_target[6:10] *= -1.0
reversal_target[10:12] *= -1.0
time_reversal_state_error = float(
    np.linalg.norm(recovered_state - reversal_target)
)

# ---------- centered circular collision ----------
circle_parameters = (0.8, 0.8, 0.8, 0.8, 10.0)
centered_torques = []
for separation in np.linspace(0.4, 3.0, 200):
    _, _, torque1, torque2 = force_and_torques(
        np.array([separation, 0.0]),
        0.37,
        -0.61,
        circle_parameters,
    )
    centered_torques.extend([abs(torque1), abs(torque2)])
maximum_centered_circle_torque = float(max(centered_torques))

offcenter_spin_transfer = float(
    np.max(
        np.abs(states[10:12, :] - states[10:12, [0]])
    )
)

# ---------- collision interval and classifier ----------
collision_threshold = 1e-3
collision_mask = overlaps > collision_threshold
if np.any(collision_mask):
    collision_indices = np.flatnonzero(collision_mask)
    collision_duration = float(
        times[collision_indices[-1]]
        - times[collision_indices[0]]
    )
else:
    collision_duration = 0.0

final_displacement = states[0:2, -1] - states[2:4, -1]
final_relative_velocity = (
    states[6:8, -1] / m1
    - states[8:10, -1] / m2
)
final_radial_velocity = float(
    np.dot(final_displacement, final_relative_velocity)
    / np.linalg.norm(final_displacement)
)
final_overlap = float(overlaps[-1])
maximum_overlap = float(np.max(overlaps))
collision_class = (
    "labeled_scattering"
    if final_overlap < collision_threshold
    and final_radial_velocity > 0.0
    else "persistent_overlap_or_unresolved"
)

# ---------- pair stress time series ----------
pair_stress_antisymmetry = []
internal_torque_sum = []
for index in range(times.size):
    displacement = states[0:2, index] - states[2:4, index]
    _, force1, torque1, torque2 = force_and_torques(
        displacement,
        states[4, index],
        states[5, index],
        parameters_collision,
    )
    pair_stress = -np.outer(displacement, force1) / control_volume
    pair_stress_antisymmetry.append(
        control_volume * (pair_stress[0, 1] - pair_stress[1, 0])
    )
    internal_torque_sum.append(torque1 + torque2)
pair_stress_antisymmetry = np.asarray(pair_stress_antisymmetry)
internal_torque_sum = np.asarray(internal_torque_sum)

# ---------- figures ----------
plt.figure()
plt.plot(states[0, :], states[1, :], label="S0-1")
plt.plot(states[2, :], states[3, :], label="S0-2")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "offcenter_collision_trajectories.png", dpi=180)
plt.close()

plt.figure()
plt.plot(times, overlaps, label="normalized overlap")
plt.plot(times, states[10, :], label="spin L1")
plt.plot(times, states[11, :], label="spin L2")
plt.xlabel("time")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "overlap_and_spin_transfer.png", dpi=180)
plt.close()

plt.figure()
plt.plot(
    times,
    pair_stress_antisymmetry,
    label="V(Sigma_xy-Sigma_yx)",
)
plt.plot(
    times,
    internal_torque_sum,
    linestyle="--",
    label="tau1+tau2",
)
plt.xlabel("time")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "stress_couple_ledger.png", dpi=180)
plt.close()

plt.figure()
plt.plot(times, (energies - energies[0]) / energies[0])
plt.xlabel("time")
plt.ylabel("relative energy error")
plt.tight_layout()
plt.savefig(FIGURES / "energy_conservation.png", dpi=180)
plt.close()

# ---------- save time series ----------
with open(
    RESULTS / "offcenter_collision_timeseries.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "time",
            "x1",
            "y1",
            "x2",
            "y2",
            "theta1",
            "theta2",
            "L1",
            "L2",
            "normalized_overlap",
            "energy",
            "total_angular_momentum",
        ]
    )
    for index, time in enumerate(times):
        writer.writerow(
            [
                time,
                states[0, index],
                states[1, index],
                states[2, index],
                states[3, index],
                states[4, index],
                states[5, index],
                states[10, index],
                states[11, index],
                overlaps[index],
                energies[index],
                angular_momenta[index],
            ]
        )

results = {
    "T1_geometry": {
        "volume_relative_error": volume_relative_error,
        "centroid_error": centroid_error,
        "shape_moment_relative_error": shape_moment_relative_error,
        "boundary_tensor_relative_error": boundary_tensor_relative_error,
        "circle_anisotropy_factor": circle_factor,
        "ellipse_anisotropy_factor": ellipse_factor,
    },
    "T2_gradients": {
        "maximum_force_relative_error": maximum_force_relative_error,
        "maximum_torque_relative_error": maximum_torque_relative_error,
    },
    "T3_euclidean_ledger": {
        "maximum_rotation_invariance_relative_error": maximum_rotation_invariance_error,
        "maximum_angular_ledger_residual": maximum_angular_ledger_residual,
        "number_of_random_tests": 1000,
    },
    "T4_stress_couple": {
        "maximum_stress_couple_residual": maximum_stress_couple_residual,
        "control_volume": control_volume,
    },
    "T5_hamilton_collision": {
        "relative_energy_drift": relative_energy_drift,
        "linear_momentum_drift": linear_momentum_drift,
        "angular_momentum_drift": angular_momentum_drift,
        "time_reversal_state_error": time_reversal_state_error,
    },
    "T6_collision_type": {
        "maximum_centered_circle_torque": maximum_centered_circle_torque,
        "offcenter_spin_transfer_amplitude": offcenter_spin_transfer,
        "final_L1": float(states[10, -1]),
        "final_L2": float(states[11, -1]),
    },
    "T7_collision_interval": {
        "collision_threshold": collision_threshold,
        "maximum_normalized_overlap": maximum_overlap,
        "collision_duration": collision_duration,
        "final_normalized_overlap": final_overlap,
        "final_radial_velocity": final_radial_velocity,
        "classification": collision_class,
        "topology_reconstruction_status": "open_due_to_persistent_object_labels",
    },
}

with open(
    RESULTS / "benchmark_results.json",
    "w",
    encoding="utf-8",
) as file:
    json.dump(results, file, ensure_ascii=False, indent=2)

print(json.dumps(results, ensure_ascii=False, indent=2))
