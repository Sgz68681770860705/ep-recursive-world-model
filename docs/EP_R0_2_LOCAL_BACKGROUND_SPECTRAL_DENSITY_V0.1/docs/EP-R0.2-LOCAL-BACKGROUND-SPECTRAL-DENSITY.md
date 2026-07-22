# EP-R0.2: Spectral Density from an Explicit Local Background Field

Status:

`[DERIVED IN THE LOCAL LINEAR FIELD MODEL] + [NUMERICAL GATE PASSED] + [FINITE-N EP ORIGIN OPEN]`

A finite \(S_0\) shear coordinate is coupled locally to a three-dimensional background field with dispersion

\[
\Omega_{\mathbf q}
=
\sqrt{\omega_g^2+c_b^2q^2}.
\]

For a normalized Gaussian source of scale \(a\), the gapless spectral density is

\[
J_k(\Omega)
=
\gamma\Omega
e^{-a^2(k^2+\Omega^2/c_b^2)}
\operatorname{sinhc}
\left(
\frac{2a^2k\Omega}{c_b}
\right),
\]

where

\[
\gamma
=
\frac{2\sqrt{\pi}g^2a^3}{c_b^3}.
\]

At \(k=0\),

\[
J_0(\Omega)
=
\gamma\Omega
e^{-(\Omega/\Omega_c)^2},
\qquad
\Omega_c=\frac{c_b}{a}.
\]

The channel is Ohmic at low frequency and gives

\[
\eta_0
=
\gamma.
\]

The static spatial response is

\[
\eta(k,0)
=
\gamma e^{-a^2k^2},
\]

so the finite source scale is directly encoded in the wave-number dependence.

For a \(d\)-dimensional linearly dispersive bath and an \(m\)-derivative coupling,

\[
J(\Omega)\sim\Omega^{d-2+2m}.
\]

A finite nonzero Newtonian viscosity therefore requires \(d+2m=3\). In three dimensions a non-derivative effective channel is Ohmic, while a first-derivative channel is super-Ohmic. A fully gapped channel gives zero DC viscosity.

This package does not yet derive the effective non-derivative coupling from quaternion spin, phase boundaries, or finite-\(N\) EP collisions.
