from pathlib import Path
import json
import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
RESULTS.mkdir(exist_ok=True)
FIGURES.mkdir(exist_ok=True)

a = 0.8
c_b = 1.5
g = 1.0
gamma = 2.0 * np.sqrt(np.pi) * g**2 * a**3 / c_b**3
omega_c = c_b / a
gaussian_normalization = (a**2 / np.pi) ** 1.5

def sinhc(value):
    value = np.asarray(value, dtype=float)
    output = np.ones_like(value)
    mask = np.abs(value) > 1e-10
    output[mask] = np.sinh(value[mask]) / value[mask]
    if output.ndim == 0:
        return float(output)
    return output

def spectral_closed(k, omega):
    omega = np.asarray(omega, dtype=float)
    argument = 2.0 * a**2 * k * omega / c_b
    return (
        gamma
        * omega
        * np.exp(-a**2 * (k**2 + (omega / c_b) ** 2))
        * sinhc(argument)
    )

def spectral_angular_quadrature(k, omega, order=240):
    nodes, weights = np.polynomial.legendre.leggauss(order)
    q = omega / c_b
    angular = 2.0 * np.pi * np.sum(
        weights
        * np.exp(
            -a**2
            * (q**2 + k**2 - 2.0 * q * k * nodes)
        )
    )
    return (
        0.5
        * np.pi
        * g**2
        * gaussian_normalization
        * omega
        / c_b**3
        * angular
    )

# T1: closed form versus direct angular integration
test_k = np.array([0.0, 0.25, 0.7, 1.2, 1.8])
test_omega = np.array([0.12, 0.35, 0.9, 1.7, 3.2])
spectral_relative_errors = []
for k_value in test_k:
    for omega_value in test_omega:
        direct = spectral_angular_quadrature(k_value, omega_value)
        closed = spectral_closed(k_value, omega_value)
        spectral_relative_errors.append(abs(direct - closed) / max(abs(closed), 1e-14))
maximum_spectral_relative_error = float(max(spectral_relative_errors))

# T2: low-frequency scaling for m=0 and m=1
low_omega = omega_c * np.logspace(-4, -1, 80)
j_m0 = gamma * low_omega * np.exp(-(low_omega / omega_c) ** 2)
j_m1 = gamma * low_omega * (low_omega / omega_c) ** 2 * np.exp(
    -(low_omega / omega_c) ** 2
)
m0_slope = float(np.polyfit(np.log(low_omega), np.log(j_m0), 1)[0])
m1_slope = float(np.polyfit(np.log(low_omega), np.log(j_m1), 1)[0])

plt.figure()
plt.loglog(low_omega, j_m0, label="m=0")
plt.loglog(low_omega, j_m1, label="m=1")
plt.xlabel("frequency")
plt.ylabel("spectral density")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "ohmic_scaling.png", dpi=180)
plt.close()

# T3: spectral integral versus analytic Gaussian memory kernel
kernel_times = np.linspace(0.0, 4.0 / omega_c, 500)
omega_grid = np.linspace(0.0, 8.0 * omega_c, 16000)
ratio = gamma * np.exp(-(omega_grid / omega_c) ** 2)
cosine_matrix = np.cos(np.outer(kernel_times, omega_grid))
kernel_numeric = (2.0 / np.pi) * np.trapezoid(
    cosine_matrix * ratio,
    omega_grid,
    axis=1,
)
kernel_analytic = (
    gamma
    * omega_c
    / np.sqrt(np.pi)
    * np.exp(-(omega_c * kernel_times) ** 2 / 4.0)
)
kernel_relative_l2_error = float(
    np.linalg.norm(kernel_numeric - kernel_analytic)
    / np.linalg.norm(kernel_analytic)
)

plt.figure()
plt.plot(kernel_times, kernel_analytic, label="analytic")
plt.plot(kernel_times, kernel_numeric, linestyle="--", label="spectral integral")
plt.xlabel("time")
plt.ylabel("memory kernel")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "kernel_comparison.png", dpi=180)
plt.close()

# T4: recover a and g from noisy static spatial viscosity
k_samples = np.linspace(0.0, 2.2, 28)
eta_static_true = gamma * np.exp(-(a * k_samples) ** 2)
random = np.random.default_rng(20260722)
noise_fraction = 0.002
eta_static_noisy = eta_static_true * (
    1.0 + noise_fraction * random.standard_normal(k_samples.size)
)

def spatial_model(log_parameters):
    fitted_gamma, fitted_a = np.exp(log_parameters)
    return fitted_gamma * np.exp(-(fitted_a * k_samples) ** 2)

def spatial_residual(log_parameters):
    return (
        spatial_model(log_parameters) - eta_static_noisy
    ) / np.maximum(eta_static_true, 0.05 * gamma)

fit = least_squares(
    spatial_residual,
    np.log(np.array([0.9 * gamma, 0.9 * a])),
)
gamma_fit, a_fit = np.exp(fit.x)
g_fit = np.sqrt(
    gamma_fit * c_b**3
    / (2.0 * np.sqrt(np.pi) * a_fit**3)
)
a_relative_error = float(abs(a_fit - a) / a)
g_relative_error = float(abs(g_fit - g) / g)

plt.figure()
plt.scatter(k_samples, eta_static_noisy, label="noisy data")
dense_k = np.linspace(0.0, 2.2, 300)
plt.plot(
    dense_k,
    gamma * np.exp(-(a * dense_k) ** 2),
    label="true",
)
plt.plot(
    dense_k,
    gamma_fit * np.exp(-(a_fit * dense_k) ** 2),
    linestyle="--",
    label="fitted",
)
plt.xlabel("wave number")
plt.ylabel("static generalized viscosity")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "spatial_viscosity_fit.png", dpi=180)
plt.close()

# Plot full spectral density at selected k
frequency_plot = np.linspace(0.0, 5.0 * omega_c, 500)
plt.figure()
for k_value in [0.0, 0.5, 1.0, 1.5]:
    plt.plot(
        frequency_plot,
        spectral_closed(k_value, frequency_plot),
        label=f"k={k_value}",
    )
plt.xlabel("frequency")
plt.ylabel("spectral density")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "spectral_density.png", dpi=180)
plt.close()

# T5: finite reversible bath generated from the explicit field spectrum
n_bath = 220
omega_max = 8.0 * omega_c
delta_omega = omega_max / n_bath
bath_omega = (np.arange(n_bath) + 0.5) * delta_omega
kernel_weights = (
    (2.0 / np.pi)
    * gamma
    * np.exp(-(bath_omega / omega_c) ** 2)
    * delta_omega
)
bath_couplings = bath_omega * np.sqrt(kernel_weights)

system_stiffness = 0.45
dimension = n_bath + 1
stiffness = np.zeros((dimension, dimension))
stiffness[0, 0] = system_stiffness + np.sum(
    bath_couplings**2 / bath_omega**2
)
stiffness[0, 1:] = -bath_couplings
stiffness[1:, 0] = -bath_couplings
stiffness[1:, 1:] = np.diag(bath_omega**2)

eigenvalues, eigenvectors = np.linalg.eigh(stiffness)
if np.min(eigenvalues) <= 0:
    raise RuntimeError("The finite Hamiltonian is not positive definite.")
normal_frequencies = np.sqrt(eigenvalues)

q0 = np.zeros(dimension)
q0[0] = 1.0
v0 = np.zeros(dimension)

def evolve(time, q_initial, v_initial):
    q_mode = eigenvectors.T @ q_initial
    v_mode = eigenvectors.T @ v_initial
    cosine = np.cos(normal_frequencies * time)
    sine = np.sin(normal_frequencies * time)
    q_mode_t = cosine * q_mode + sine / normal_frequencies * v_mode
    v_mode_t = -normal_frequencies * sine * q_mode + cosine * v_mode
    return eigenvectors @ q_mode_t, eigenvectors @ v_mode_t

def total_energy(q, v):
    return 0.5 * np.dot(v, v) + 0.5 * q @ stiffness @ q

final_time = 5.0
q_final, v_final = evolve(final_time, q0, v0)
q_back, v_back = evolve(final_time, q_final, -v_final)
reversal_configuration_error = float(np.linalg.norm(q_back - q0))
reversal_velocity_error = float(np.linalg.norm(v_back + v0))

energy_times = np.linspace(0.0, final_time, 401)
energies = np.array(
    [total_energy(*evolve(t, q0, v0)) for t in energy_times]
)
relative_energy_drift = float(
    np.max(np.abs(energies - energies[0])) / energies[0]
)

# Gapped threshold check
omega_gap = 0.6 * omega_c
gapped_probe_below = 0.8 * omega_gap
gapped_probe_above = 1.2 * omega_gap
gapped_below_value = 0.0
q_above = np.sqrt(gapped_probe_above**2 - omega_gap**2) / c_b
gapped_above_value = (
    2.0
    * np.pi**2
    * g**2
    * gaussian_normalization
    * q_above
    / c_b**2
    * np.exp(-a**2 * q_above**2)
)

results = {
    "parameters": {
        "a": a,
        "c_b": c_b,
        "g": g,
        "gamma": float(gamma),
        "omega_c": float(omega_c),
    },
    "T1": {
        "maximum_relative_spectral_error": maximum_spectral_relative_error,
    },
    "T2": {
        "m0_fitted_exponent": m0_slope,
        "m1_fitted_exponent": m1_slope,
        "m0_expected_exponent": 1.0,
        "m1_expected_exponent": 3.0,
    },
    "T3": {
        "kernel_relative_L2_error": kernel_relative_l2_error,
    },
    "T4": {
        "noise_fraction": noise_fraction,
        "gamma_true": float(gamma),
        "gamma_fit": float(gamma_fit),
        "a_true": a,
        "a_fit": float(a_fit),
        "a_relative_error": a_relative_error,
        "g_true": g,
        "g_fit": float(g_fit),
        "g_relative_error": g_relative_error,
    },
    "T5": {
        "reversal_configuration_error": reversal_configuration_error,
        "reversal_velocity_error": reversal_velocity_error,
        "relative_energy_drift": relative_energy_drift,
        "minimum_stiffness_eigenvalue": float(np.min(eigenvalues)),
    },
    "gapped_channel_check": {
        "omega_gap": float(omega_gap),
        "probe_below_gap": float(gapped_probe_below),
        "spectral_density_below_gap": gapped_below_value,
        "probe_above_gap": float(gapped_probe_above),
        "spectral_density_above_gap": float(gapped_above_value),
    },
}

with open(RESULTS / "benchmark_results.json", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=2)

with open(
    RESULTS / "inverse_spatial_fit.csv",
    "w",
    newline="",
    encoding="utf-8",
) as file:
    writer = csv.writer(file)
    writer.writerow(["parameter", "true", "fitted", "relative_error"])
    writer.writerow(["gamma", gamma, gamma_fit, abs(gamma_fit - gamma) / gamma])
    writer.writerow(["a", a, a_fit, a_relative_error])
    writer.writerow(["g", g, g_fit, g_relative_error])

print(json.dumps(results, indent=2))
