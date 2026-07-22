# EP-R0.3: Symmetry-Compatible Ohmic Tensor and Quaternion Response

Status:

`[DERIVED IN THE LINEAR INTERNAL-FIELD MODEL] + [NUMERICAL — ALL PREREGISTERED GATES PASSED] + [NONLINEAR FINITE-BOUNDARY ORIGIN OPEN]`

R0.2 showed that a three-dimensional Newtonian viscosity requires an effective gapless Ohmic channel. R0.3 resolves the symmetry concern by coupling the bath to internal \(S_0\) variables rather than to an absolute spatial displacement field.

The minimal internal variables are:

- a symmetric traceless shape tensor \(Q_{ij}^{\rm dev}\);
- a scalar compactness mode \(\vartheta\);
- a quaternion orientation \(q\), linearized by an axial angle \(\boldsymbol\theta\).

They couple locally to matching \(S_{-1}\) tensor, scalar, and axial-vector fields. These couplings are invariant under common translations and rotations and are non-derivative in the internal variables. Each gapless three-dimensional channel is therefore Ohmic.

The isotropic generalized viscosity tensor is

\[
\widehat\eta_{ijmn}^{\rm iso}
=
\widehat\eta_TP_{ijmn}^{\rm dev}
+
\widehat\zeta_LP_{ijmn}^{\rm vol}
+
\widehat\eta_RP_{ijmn}^{\rm anti}.
\]

For an oriented irregular \(S_0\), quaternion orientation generates

\[
A_{ij}(q)
=
n_i(q)n_j(q)-\delta_{ij}/3
\]

and the minimal anisotropic term

\[
\widehat\eta_{ijmn}^{Q}
=
\widehat\eta_QA_{ij}A_{mn}.
\]

This term is positive semidefinite and produces a linear normal-stress difference for a pre-oriented object. Its isotropic orientation average vanishes.

A relative-rotor Hamiltonian bath conserves total angular momentum exactly while producing an effective rotational memory after the bath is eliminated. Quaternion group updates preserve the unit norm.

The package does not yet derive these internal variables from a nonlinear finite phase boundary or from finite-\(N\) EP collisions.
