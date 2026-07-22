# EP-R0.1: Reversible Background Response and Generalized Viscosity

Status:

`[DERIVED IN THE MINIMAL LINEAR MODEL] + [NUMERICAL BENCHMARK PASSED] + [MICROSCOPIC EP ORIGIN OPEN]`

## Objective

The first EP bridge is

\[
S_0+S_{-1}\ \text{reversible dynamics}
\rightarrow
S_{-1}\ \text{memory kernel}
\rightarrow
\widehat\eta(k,\omega).
\]

A positive Hamiltonian oscillator continuum is used as the minimal \(S_{-1}\) background. Eliminating it gives a causal generalized Langevin term without inserting fundamental friction.

## Minimal response

For the spectral density

\[
J_k(\Omega)
=
\frac{\Delta\eta}{\tau}
\frac{\Omega\lambda_k}
{\Omega^2+\lambda_k^2},
\qquad
\lambda_k=\frac{1+\xi^2k^2}{\tau},
\]

the causal kernel is

\[
K_\eta(k,t)
=
\frac{\Delta\eta}{\tau}
e^{-(1+\xi^2k^2)t/\tau}H(t),
\]

and

\[
\widehat\eta(k,\omega)
=
\eta_\infty+
\frac{\Delta\eta}
{1+\xi^2k^2-i\omega\tau}.
\]

The conventional viscosity is

\[
\eta_0=\widehat\eta(0,0)=\eta_\infty+\Delta\eta.
\]

## Results

- finite bath time-reversal configuration error: \(2.06\times10^{-15}\);
- velocity reversal error: \(3.81\times10^{-14}\);
- maximum relative energy drift: \(1.08\times10^{-13}\);
- discrete-kernel relative error in the tested window: \(5.08\times10^{-3}\);
- all four one-pole parameters were recovered from noisy complex response data with relative errors below \(10^{-3}\).

## Boundary of the result

The package does not derive the spectral density from finite-\(N\) EP collisions. It does not yet include quaternion spin, deformable boundaries, a kinetic limit, or a rigorous Navier–Stokes limit.
