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

# T1-T2: finite reversible oscillator bath approximating a Drude kernel
eta_kernel = 1.4
Lambda = 3.0
n_bath = 240
omega_max = 80.0
domega = omega_max / n_bath
omega = (np.arange(n_bath) + 0.5) * domega

weights = (
    (2.0 / np.pi)
    * eta_kernel
    * Lambda**2
    / (omega**2 + Lambda**2)
    * domega
)
couplings = omega * np.sqrt(weights)

system_stiffness = 0.5
dimension = n_bath + 1
K = np.zeros((dimension, dimension))
K[0, 0] = system_stiffness + np.sum(couplings**2 / omega**2)
K[0, 1:] = -couplings
K[1:, 0] = -couplings
K[1:, 1:] = np.diag(omega**2)

eigenvalues, eigenvectors = np.linalg.eigh(K)
if np.min(eigenvalues) <= 0:
    raise RuntimeError("Hamiltonian stiffness matrix is not positive definite.")
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

def energy(q, v):
    return 0.5 * np.dot(v, v) + 0.5 * q @ K @ q

final_time = 5.0
q_final, v_final = evolve(final_time, q0, v0)
q_back, v_back = evolve(final_time, q_final, -v_final)

reversal_configuration_error = float(np.linalg.norm(q_back - q0))
reversal_velocity_error = float(np.linalg.norm(v_back + v0))

times = np.linspace(0.0, final_time, 401)
energies = np.array([energy(*evolve(t, q0, v0)) for t in times])
relative_energy_drift = float(
    np.max(np.abs(energies - energies[0])) / energies[0]
)

kernel_times = np.linspace(0.0, 2.0, 1001)
kernel_discrete = np.cos(np.outer(kernel_times, omega)) @ weights
kernel_target = eta_kernel * Lambda * np.exp(-Lambda * kernel_times)
kernel_relative_l2_error = float(
    np.linalg.norm(kernel_discrete - kernel_target)
    / np.linalg.norm(kernel_target)
)
kernel_max_abs_error = float(np.max(np.abs(kernel_discrete - kernel_target)))

plt.figure()
plt.plot(kernel_times, kernel_target, label="continuous target")
plt.plot(kernel_times, kernel_discrete, linestyle="--", label="finite reversible bath")
plt.xlabel("time")
plt.ylabel("memory kernel")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "kernel_comparison.png", dpi=180)
plt.close()

plt.figure()
plt.plot(times, (energies - energies[0]) / energies[0])
plt.xlabel("time")
plt.ylabel("relative energy error")
plt.tight_layout()
plt.savefig(FIGURES / "energy_conservation.png", dpi=180)
plt.close()

# T3-T4: one-pole k-omega response and inverse fit
true_parameters = np.array([0.35, 1.25, 0.45, 0.70])
parameter_names = ["eta_infinity", "delta_eta", "tau", "xi"]

k_values = np.array([0.0, 0.3, 0.7, 1.1, 1.6])
omega_values = np.linspace(0.0, 5.0, 30)
k_data = np.repeat(k_values, len(omega_values))
omega_data = np.tile(omega_values, len(k_values))

def eta_model(parameters, k=k_data, angular_frequency=omega_data):
    eta_infinity, delta_eta, tau, xi = parameters
    return eta_infinity + delta_eta / (
        1.0 + (xi * k) ** 2 - 1j * angular_frequency * tau
    )

clean_response = eta_model(true_parameters)
random = np.random.default_rng(42)
noise_fraction = 0.003
response_scale = np.maximum(np.abs(clean_response), 0.2)
noisy_response = clean_response + (
    noise_fraction
    * response_scale
    * (
        random.standard_normal(clean_response.size)
        + 1j * random.standard_normal(clean_response.size)
    )
    / np.sqrt(2.0)
)

def residual(log_parameters):
    parameters = np.exp(log_parameters)
    normalized = (eta_model(parameters) - noisy_response) / response_scale
    return np.concatenate([normalized.real, normalized.imag])

fit_result = least_squares(
    residual,
    np.log(np.array([0.25, 1.0, 0.30, 0.50])),
)
fitted_parameters = np.exp(fit_result.x)
relative_parameter_errors = np.abs(
    (fitted_parameters - true_parameters) / true_parameters
)

eta_grid_k, eta_grid_omega = np.meshgrid(
    np.linspace(0.0, 2.0, 21),
    np.linspace(0.0, 6.0, 31),
    indexing="ij",
)
eta_infinity, delta_eta, tau, xi = true_parameters
eta_grid = eta_infinity + delta_eta / (
    1.0
    + (xi * eta_grid_k) ** 2
    - 1j * eta_grid_omega * tau
)
minimum_real_eta = float(np.min(eta_grid.real))
zero_frequency_zero_wave_eta = float(eta_grid[0, 0].real)

selected_k = 0.7
plot_omega = np.linspace(0.0, 5.0, 200)
true_curve = eta_model(
    true_parameters,
    np.full_like(plot_omega, selected_k),
    plot_omega,
)
fit_curve = eta_model(
    fitted_parameters,
    np.full_like(plot_omega, selected_k),
    plot_omega,
)

plt.figure()
plt.plot(plot_omega, true_curve.real, label="true real part")
plt.plot(plot_omega, fit_curve.real, linestyle="--", label="fitted real part")
plt.plot(plot_omega, true_curve.imag, label="true imaginary part")
plt.plot(plot_omega, fit_curve.imag, linestyle="--", label="fitted imaginary part")
plt.xlabel("angular frequency")
plt.ylabel("generalized viscosity")
plt.legend()
plt.tight_layout()
plt.savefig(FIGURES / "inverse_fit_response.png", dpi=180)
plt.close()

results = {
    "T1": {
        "reversal_configuration_error": reversal_configuration_error,
        "reversal_velocity_error": reversal_velocity_error,
        "relative_energy_drift": relative_energy_drift,
        "minimum_hamiltonian_eigenvalue": float(np.min(eigenvalues)),
    },
    "T2": {
        "kernel_relative_L2_error": kernel_relative_l2_error,
        "kernel_max_absolute_error": kernel_max_abs_error,
        "tested_time_window": [0.0, 2.0],
    },
    "T3": {
        "minimum_real_eta_on_test_grid": minimum_real_eta,
        "eta_0_0": zero_frequency_zero_wave_eta,
        "eta_infinity_plus_delta_eta": float(eta_infinity + delta_eta),
    },
    "T4": {
        "noise_fraction": noise_fraction,
        "true_parameters": dict(zip(parameter_names, true_parameters.tolist())),
        "fitted_parameters": dict(zip(parameter_names, fitted_parameters.tolist())),
        "relative_errors": dict(
            zip(parameter_names, relative_parameter_errors.tolist())
        ),
        "normalized_residual_rms": float(np.sqrt(np.mean(fit_result.fun**2))),
    },
}

with open(RESULTS / "benchmark_results.json", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=2)

with open(RESULTS / "inverse_fit.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["parameter", "true", "fitted", "relative_error"])
    for name, true, fitted, error in zip(
        parameter_names,
        true_parameters,
        fitted_parameters,
        relative_parameter_errors,
    ):
        writer.writerow([name, true, fitted, error])

print(json.dumps(results, indent=2))
