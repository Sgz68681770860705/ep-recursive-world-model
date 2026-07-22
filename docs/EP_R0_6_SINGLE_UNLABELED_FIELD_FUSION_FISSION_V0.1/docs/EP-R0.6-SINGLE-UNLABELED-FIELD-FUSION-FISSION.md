# EP-R0.6: Single Unlabeled Field Fusion–Fission Dynamics

Status:

`[DERIVED IN THE SINGLE-FIELD CUBIC–QUINTIC NLS MODEL] + [EXPLORATORY NUMERICAL — ALL FROZEN GATES PASSED] + [FINITE-N EP ORIGIN OPEN]`

R0.6 removes the two canonical object labels used in R0.5. The dynamics now contain only one complex field,

\[
\psi(\mathbf x,t),
\qquad
\rho=|\psi|^2,
\]

governed by

\[
i\psi_t
=
-\frac12\Delta\psi
-g|\psi|^2\psi
+h|\psi|^4\psi.
\]

Objects are extracted only as connected components of a frozen density superlevel set. They are not variables of the field equation.

The action is Hamiltonian and has global phase, translation, rotation, and time-translation symmetries. The associated norm, momentum, angular momentum, and Hamiltonian are conserved in the continuum model. Numerical split-step tests also passed norm, energy, momentum, angular-momentum, and time-reversal gates.

Three topology branches were observed in the frozen exploratory window:

- equal phase and slow impact: two components became one persistent-fusion candidate;
- relative phase \(\pi/2\): \(2\to1\to2\), fusion followed by fission;
- relative phase \(\pi\): two components remained distinct.

During the one-component interval, incoming component labels have no canonical continuation. After fission, new connected components can be extracted, but the full reversible field retains information in amplitude, phase, and radiation. This is component-label reconstruction, not destruction of the complete state.

A linear control verified superposition to machine precision. Thus ordinary linear waves add and pass through one another; topology-changing fusion–fission requires nonlinear field dynamics.

The cubic–quintic field is a minimal postulated model. It has not been derived from finite-\(N\) EP dynamics, real light, real particles, or measured fluid response.
