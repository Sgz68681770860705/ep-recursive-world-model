# EP-R0.4: Finite Phase Boundary, Quaternion Orientation, and Collision Stress Ledger

Status:

`[DERIVED IN THE GAUSSIAN FINITE-BOUNDARY MODEL] + [NUMERICAL — COLLISION LEDGER GATE PASSED] + [TOPOLOGY RECONSTRUCTION OPEN]`

A finite \(S_0\) is represented by

\[
\chi_i(\mathbf x)
=
\exp
\left[
-\frac12
(\mathbf x-\mathbf X_i)^TA_i(q_i)
(\mathbf x-\mathbf X_i)
\right].
\]

The level set \(\chi_i=e^{-1/2}\) is an ellipse in the benchmark and an ellipsoid in the direct three-dimensional extension.

The phase-field moments give

\[
V_i=\frac{2\pi}{\sqrt{\det A_i}},
\qquad
M_i=A_i^{-1},
\]

while the boundary-gradient tensor is

\[
B_i
=
\frac{\pi}{2\sqrt{\det A_i}}A_i.
\]

The normalized anisotropy of \(B_i\) supplies a geometry form factor for the tensor and rotational channels introduced in R0.3. It vanishes for a circle and is nonzero for an irregular boundary.

The overlap energy is

\[
U_{12}
=
\varepsilon_b
\int\chi_1\chi_2d^2x.
\]

It creates a finite collision interval and gives continuous forces and torques. Euclidean invariance yields

\[
\mathbf F_1+\mathbf F_2=0
\]

and

\[
\mathbf d\times\mathbf F_1+\tau_1+\tau_2=0.
\]

The antisymmetric pair stress closes against the internal torque ledger.

A planar Hamiltonian benchmark embedded in the quaternion \(K\)-axis subgroup passed energy, momentum, angular-momentum, and time-reversal tests. A circular head-on collision produced no spin, while an off-center collision of anisotropic boundaries transferred orbital angular momentum into internal spin.

The model preserves two object labels. It therefore validates scattering and persistent-overlap diagnostics, but it cannot yet demonstrate unlabeled fusion, breakup, or reconstruction.
