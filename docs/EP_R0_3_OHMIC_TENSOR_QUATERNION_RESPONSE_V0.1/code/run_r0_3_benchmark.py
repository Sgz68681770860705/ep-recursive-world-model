from pathlib import Path
import json
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
from scipy.special import erfi

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
RESULTS.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)

# ---------- tensor projectors ----------
delta = np.eye(3)
P_dev = np.zeros((3, 3, 3, 3))
P_vol = np.zeros_like(P_dev)
P_anti = np.zeros_like(P_dev)
for i in range(3):
    for j in range(3):
        for m in range(3):
            for n in range(3):
                P_dev[i, j, m, n] = (
                    0.5
                    * (
                        delta[i, m] * delta[j, n]
                        + delta[i, n] * delta[j, m]
                    )
                    - delta[i, j] * delta[m, n] / 3.0
                )
                P_vol[i, j, m, n] = (
                    delta[i, j] * delta[m, n] / 3.0
                )
                P_anti[i, j, m, n] = 0.5 * (
                    delta[i, m] * delta[j, n]
                    - delta[i, n] * delta[j, m]
                )

def compose_projectors(P, Q):
    return np.einsum("ijab,abmn->ijmn", P, Q)

projector_errors = [
    np.linalg.norm(compose_projectors(P_dev, P_dev) - P_dev),
    np.linalg.norm(compose_projectors(P_vol, P_vol) - P_vol),
    np.linalg.norm(compose_projectors(P_anti, P_anti) - P_anti),
    np.linalg.norm(compose_projectors(P_dev, P_vol)),
    np.linalg.norm(compose_projectors(P_dev, P_anti)),
    np.linalg.norm(compose_projectors(P_vol, P_anti)),
]
projector_algebra_error = float(max(projector_errors))

# ---------- quaternion helpers ----------
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

def rotate_vector(q, v):
    return qmul(qmul(q, np.concatenate(([0.0], v))), qconj(q))[1:]

def increment_quaternion(omega, dt):
    magnitude = np.linalg.norm(omega)
    if magnitude < 1e-15:
        return np.array([1.0, 0.0, 0.0, 0.0])
    half_angle = 0.5 * magnitude * dt
    return np.concatenate(
        (
            [np.cos(half_angle)],
            np.sin(half_angle) * omega / magnitude,
        )
    )

# ---------- passivity ----------
rng = np.random.default_rng(20260722)
eta_T = 0.8
zeta_L = 0.55
eta_R = 0.4
eta_Q = 0.65
powers = []
for _ in range(5000):
    raw_D = rng.normal(size=(3, 3))
    D = 0.5 * (raw_D + raw_D.T)
    raw_W = rng.normal(size=(3, 3))
    W = 0.5 * (raw_W - raw_W.T)

    q = rng.normal(size=4)
    q /= np.linalg.norm(q)
    n = rotate_vector(q, np.array([0.0, 0.0, 1.0]))
    A = np.outer(n, n) - np.eye(3) / 3.0

    D_dev = D - np.trace(D) * np.eye(3) / 3.0
    sigma = (
        2.0 * eta_T * D_dev
        + zeta_L * np.trace(D) * np.eye(3)
        + 2.0 * eta_R * W
        + 2.0 * eta_Q * A * np.sum(A * D)
    )
    powers.append(float(np.sum(sigma * (D + W))))
minimum_power = float(np.min(powers))

# ---------- quaternion norm preservation ----------
q = np.array([1.0, 0.0, 0.0, 0.0])
dt = 0.001
quaternion_norm_errors = []
for step in range(10000):
    t = step * dt
    omega = np.array(
        [
            0.7 * np.sin(0.9 * t),
            0.4 * np.cos(1.3 * t),
            0.5 + 0.2 * np.sin(0.4 * t),
        ]
    )
    q = qmul(q, increment_quaternion(omega, dt))
    quaternion_norm_errors.append(abs(np.linalg.norm(q) - 1.0))
quaternion_norm_error = float(max(quaternion_norm_errors))

# ---------- exact relative-rotor bath ----------
n_bath = 90
kappa = 0.04 + 0.02 * (
    1.0 + np.sin(np.linspace(0.0, 3.0 * np.pi, n_bath))
)
dimension = n_bath + 1
stiffness = np.zeros((dimension, dimension))
for j, spring in enumerate(kappa, start=1):
    stiffness[0, 0] += spring
    stiffness[j, j] += spring
    stiffness[0, j] -= spring
    stiffness[j, 0] -= spring

eigenvalues, eigenvectors = np.linalg.eigh(stiffness)
normal_frequencies = np.sqrt(np.clip(eigenvalues, 0.0, None))

theta0 = np.zeros(dimension)
velocity0 = np.zeros(dimension)
velocity0[0] = 1.0

def evolve_rotors(time, theta_initial, velocity_initial):
    theta_mode = eigenvectors.T @ theta_initial
    velocity_mode = eigenvectors.T @ velocity_initial
    theta_mode_t = np.empty_like(theta_mode)
    velocity_mode_t = np.empty_like(velocity_mode)
    zero_mask = normal_frequencies < 1e-10
    nonzero_mask = ~zero_mask
    theta_mode_t[zero_mask] = (
        theta_mode[zero_mask] + time * velocity_mode[zero_mask]
    )
    velocity_mode_t[zero_mask] = velocity_mode[zero_mask]
    freq = normal_frequencies[nonzero_mask]
    cosine = np.cos(freq * time)
    sine = np.sin(freq * time)
    theta_mode_t[nonzero_mask] = (
        cosine * theta_mode[nonzero_mask]
        + sine / freq * velocity_mode[nonzero_mask]
    )
    velocity_mode_t[nonzero_mask] = (
        -freq * sine * theta_mode[nonzero_mask]
        + cosine * velocity_mode[nonzero_mask]
    )
    return (
        eigenvectors @ theta_mode_t,
        eigenvectors @ velocity_mode_t,
    )

def rotor_energy(theta, velocity):
    return 0.5 * np.dot(velocity, velocity) + 0.5 * theta @ stiffness @ theta

final_time = 7.0
theta_final, velocity_final = evolve_rotors(
    final_time, theta0, velocity0
)
theta_back, velocity_back = evolve_rotors(
    final_time, theta_final, -velocity_final
)
reversal_configuration_error = float(
    np.linalg.norm(theta_back - theta0)
)
reversal_velocity_error = float(
    np.linalg.norm(velocity_back + velocity0)
)

times = np.linspace(0.0, final_time, 501)
angular_momenta = []
energies = []
central_spin = []
for time in times:
    theta_t, velocity_t = evolve_rotors(time, theta0, velocity0)
    angular_momenta.append(np.sum(velocity_t))
    energies.append(rotor_energy(theta_t, velocity_t))
    central_spin.append(velocity_t[0])
angular_momenta = np.asarray(angular_momenta)
energies = np.asarray(energies)
central_spin = np.asarray(central_spin)
angular_momentum_drift = float(
    np.max(np.abs(angular_momenta - angular_momenta[0]))
)
relative_energy_drift = float(
    np.max(np.abs(energies - energies[0])) / energies[0]
)
central_spin_transfer = float(
    np.max(np.abs(central_spin - central_spin[0]))
)

plt.figure()
plt.plot(times, central_spin, label="central rotor")
plt.plot(
    times,
    angular_momenta,
    linestyle="--",
    label="total angular momentum",
)
plt.xlabel("time")
plt.ylabel("angular velocity / angular momentum")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "rotor_angular_momentum.png", dpi=180)
plt.close()

# ---------- normal stress difference ----------
alpha = np.deg2rad(25.0)
q_alpha = np.array(
    [np.cos(alpha / 2.0), 0.0, 0.0, np.sin(alpha / 2.0)]
)
n_alpha = rotate_vector(q_alpha, np.array([1.0, 0.0, 0.0]))
A_alpha = np.outer(n_alpha, n_alpha) - np.eye(3) / 3.0
shear_rate = 1.1
D_shear = np.zeros((3, 3))
D_shear[0, 1] = shear_rate / 2.0
D_shear[1, 0] = shear_rate / 2.0
sigma_Q = 2.0 * eta_Q * A_alpha * np.sum(A_alpha * D_shear)
N1_direct = float(sigma_Q[0, 0] - sigma_Q[1, 1])
N1_formula = float(
    2.0
    * eta_Q
    * (A_alpha[0, 0] - A_alpha[1, 1])
    * A_alpha[0, 1]
    * shear_rate
)
normal_stress_formula_relative_error = float(
    abs(N1_direct - N1_formula) / max(abs(N1_formula), 1e-14)
)

# Fibonacci-sphere isotropic average
n_orientations = 30000
indices = np.arange(n_orientations)
golden_ratio = (1.0 + np.sqrt(5.0)) / 2.0
z = 1.0 - 2.0 * (indices + 0.5) / n_orientations
phi = 2.0 * np.pi * indices / golden_ratio
radius = np.sqrt(np.maximum(0.0, 1.0 - z**2))
directions = np.column_stack(
    (radius * np.cos(phi), radius * np.sin(phi), z)
)
Axx_minus_Ayy = directions[:, 0] ** 2 - directions[:, 1] ** 2
Axy = directions[:, 0] * directions[:, 1]
N1_samples = (
    2.0
    * eta_Q
    * Axx_minus_Ayy
    * Axy
    * shear_rate
)
isotropic_average_N1 = float(np.mean(N1_samples))

# ---------- rotational channel inverse fit ----------
g_true = 0.9
a_true = 0.65
c_true = 1.3

def gamma_from(g_value, a_value, c_value):
    return (
        2.0
        * np.sqrt(np.pi)
        * g_value**2
        * a_value**3
        / c_value**3
    )

def eta_frequency(g_value, a_value, c_value, omega):
    gamma_value = gamma_from(g_value, a_value, c_value)
    omega_c_value = c_value / a_value
    x = omega / omega_c_value
    return gamma_value * np.exp(-x**2) * (1.0 + 1j * erfi(x))

def eta_static(g_value, a_value, c_value, k):
    gamma_value = gamma_from(g_value, a_value, c_value)
    return gamma_value * np.exp(-(a_value * k) ** 2)

k_data = np.linspace(0.0, 2.0, 24)
omega_data = np.linspace(0.0, 2.6, 30)
static_clean = eta_static(g_true, a_true, c_true, k_data)
frequency_clean = eta_frequency(
    g_true, a_true, c_true, omega_data
)

noise_fraction = 0.003
static_noisy = static_clean * (
    1.0 + noise_fraction * rng.standard_normal(k_data.size)
)
frequency_scale = np.maximum(np.abs(frequency_clean), 0.1 * abs(frequency_clean[0]))
frequency_noisy = frequency_clean + (
    noise_fraction
    * frequency_scale
    * (
        rng.standard_normal(omega_data.size)
        + 1j * rng.standard_normal(omega_data.size)
    )
    / np.sqrt(2.0)
)

def inverse_residual(log_parameters):
    g_value, a_value, c_value = np.exp(log_parameters)
    static_model = eta_static(g_value, a_value, c_value, k_data)
    frequency_model = eta_frequency(
        g_value, a_value, c_value, omega_data
    )
    static_residual = (
        static_model - static_noisy
    ) / np.maximum(static_clean, 0.1 * static_clean[0])
    frequency_residual = (
        frequency_model - frequency_noisy
    ) / frequency_scale
    return np.concatenate(
        (
            static_residual,
            frequency_residual.real,
            frequency_residual.imag,
        )
    )

fit = least_squares(
    inverse_residual,
    np.log(np.array([0.8, 0.6, 1.1])),
)
g_fit, a_fit, c_fit = np.exp(fit.x)
parameter_relative_errors = {
    "g": float(abs(g_fit - g_true) / g_true),
    "a": float(abs(a_fit - a_true) / a_true),
    "c": float(abs(c_fit - c_true) / c_true),
}

plt.figure()
plt.scatter(k_data, static_noisy, label="static data")
dense_k = np.linspace(0.0, 2.0, 300)
plt.plot(
    dense_k,
    eta_static(g_true, a_true, c_true, dense_k),
    label="true",
)
plt.plot(
    dense_k,
    eta_static(g_fit, a_fit, c_fit, dense_k),
    linestyle="--",
    label="fitted",
)
plt.xlabel("wave number")
plt.ylabel("rotational static viscosity")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "rotational_spatial_fit.png", dpi=180)
plt.close()

plt.figure()
dense_omega = np.linspace(0.0, 2.6, 300)
true_frequency_curve = eta_frequency(
    g_true, a_true, c_true, dense_omega
)
fit_frequency_curve = eta_frequency(
    g_fit, a_fit, c_fit, dense_omega
)
plt.plot(
    dense_omega,
    true_frequency_curve.real,
    label="true real",
)
plt.plot(
    dense_omega,
    fit_frequency_curve.real,
    linestyle="--",
    label="fit real",
)
plt.plot(
    dense_omega,
    true_frequency_curve.imag,
    label="true imaginary",
)
plt.plot(
    dense_omega,
    fit_frequency_curve.imag,
    linestyle="--",
    label="fit imaginary",
)
plt.xlabel("frequency")
plt.ylabel("rotational generalized viscosity")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "rotational_frequency_fit.png", dpi=180)
plt.close()

# ---------- low-frequency rotational poles ----------
I0 = 1.2
K_R = 0.9
gamma_R = gamma_from(g_true, a_true, c_true)
discriminant = 4.0 * I0 * K_R - gamma_R**2
rotational_poles = [
    (-1j * gamma_R + np.sqrt(discriminant + 0j)) / (2.0 * I0),
    (-1j * gamma_R - np.sqrt(discriminant + 0j)) / (2.0 * I0),
]

results = {
    "T1": {
        "projector_algebra_max_error": projector_algebra_error,
    },
    "T2": {
        "minimum_power_over_random_tests": minimum_power,
        "number_of_tests": 5000,
    },
    "T3": {
        "maximum_quaternion_norm_error": quaternion_norm_error,
        "number_of_group_updates": 10000,
    },
    "T4": {
        "angular_momentum_drift": angular_momentum_drift,
        "reversal_configuration_error": reversal_configuration_error,
        "reversal_velocity_error": reversal_velocity_error,
        "relative_energy_drift": relative_energy_drift,
        "central_spin_transfer_amplitude": central_spin_transfer,
        "minimum_stiffness_eigenvalue": float(np.min(eigenvalues)),
    },
    "T5": {
        "orientation_angle_degrees": 25.0,
        "N1_direct": N1_direct,
        "N1_formula": N1_formula,
        "formula_relative_error": normal_stress_formula_relative_error,
        "isotropic_average_N1": isotropic_average_N1,
        "orientation_samples": n_orientations,
    },
    "T6": {
        "noise_fraction": noise_fraction,
        "true_parameters": {
            "g": g_true,
            "a": a_true,
            "c": c_true,
        },
        "fitted_parameters": {
            "g": float(g_fit),
            "a": float(a_fit),
            "c": float(c_fit),
        },
        "relative_errors": parameter_relative_errors,
        "normalized_residual_rms": float(
            np.sqrt(np.mean(fit.fun**2))
        ),
    },
    "rotational_low_frequency_poles": [
        {
            "real": float(np.real(pole)),
            "imag": float(np.imag(pole)),
        }
        for pole in rotational_poles
    ],
}

with open(
    RESULTS / "benchmark_results.json",
    "w",
    encoding="utf-8",
) as file:
    json.dump(results, file, ensure_ascii=False, indent=2)

with open(
    RESULTS / "rotational_inverse_fit.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:
    writer = csv.writer(file)
    writer.writerow(["parameter", "true", "fitted", "relative_error"])
    writer.writerow(
        ["g", g_true, g_fit, parameter_relative_errors["g"]]
    )
    writer.writerow(
        ["a", a_true, a_fit, parameter_relative_errors["a"]]
    )
    writer.writerow(
        ["c", c_true, c_fit, parameter_relative_errors["c"]]
    )

print(json.dumps(results, ensure_ascii=False, indent=2))
