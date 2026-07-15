# Q002: Light-Like Propagation in a Recursive Medium — From Mechanical-Wave Analogies to Joint \(S_0/S_{-1}\) Eigenmodes

Date: 2026-07-15  
Status: [OPEN] Conceptual route defined; mathematical closure, conservation proofs, and numerical tests remain incomplete  
Stage: Q002-M0 → Q002-M5  
Related: Q001 (boundary collision statistics and scale-mapped forces), Q003 (shared environment and entanglement)

## 1. Main advance

This session established a clearer working postulate:

> **[POSTULATE] Within EP, electromagnetic waves are not initially treated as a separate fundamental category. They are investigated as generalized mechanical eigenmodes of the recursive \(S_0/S_{-1}\) medium under a special parameter regime, symmetry class, and set of constraints.**

“Mechanical” here does not mean an ordinary material such as air, water, or steel. It means that a deeper state-carrying environment, local coupling, restoring response, inertia, momentum exchange, and continuous pattern reconstruction are present.

This is a research starting point, not an established claim about nature.

## 2. Scientific discipline

The program may remove established equations from the input, but it cannot remove observed facts from the output tests.

We do not initially assume Maxwell equations, a fundamental electric or magnetic field, a deepest causal speed equal to visible light speed, Lorentz symmetry as a microscopic axiom, optical interface formulas, or photon quantization.

The model must nevertheless recover or approximate the observed \(S_0\)-level outputs: stable vacuum propagation, two transverse polarizations, very low vacuum dispersion and attenuation, medium-dependent propagation, reflection, refraction, interference, diffraction, and eventually discrete energy-momentum exchange.

\[
\boxed{\text{Do not insert the target equations; retain the data as falsification gates.}}
\]

## 3. Common wave structure

Strings, membranes, shear waves, water waves, and light are not identical physical objects, but they share a broad eigenmode structure:

\[
\text{local state difference}
\rightarrow
\text{restoring response}
\rightarrow
\text{inertial motion}
\rightarrow
\text{neighboring reconstruction}
\rightarrow
\text{propagating mode}
\]

A generic linear form is:

\[
\mathbf M\,\partial_t^2\mathbf Q+\mathcal D(-i\nabla)\mathbf Q=0
\]

with plane-wave condition:

\[
\det[\mathcal D(\mathbf k)-\omega^2\mathbf M]=0
\]

The propagation speed is therefore an eigenvalue property of the combined system, not necessarily the speed of its microscopic members.

The model must distinguish phase, group, front, and deep update speeds:

\[
v_p=\omega/k,\qquad v_g=d\omega/dk,\qquad v_{\rm front},\qquad u_{-1}.
\]

## 4. Joint \(S_0/S_{-1}\) propagation

A light-like mode cannot be represented only by the trajectory of one \(S_0\) object. A minimal joint vector state is:

\[
\mathbf Q=
\begin{pmatrix}
\mathbf q_0\\
\mathbf q_{-1}
\end{pmatrix}.
\]

The visible packet may be only the \(S_0\)-projection of a joint eigenmode:

\[
\text{visible packet}=\mathcal P_0[\mathbf q_0,\mathbf q_{-1}].
\]

Its carrier members may be replaced while its phase, momentum flux, direction, and pattern identity remain stable.

## 5. Slow visible and fast deep branches

The working hypothesis allows:

\[
u_{-1}\gg c_\gamma.
\]

A coupled two-layer system may produce a slow branch \(\omega_-(k)\), mainly visible at \(S_0\), and a fast branch \(\omega_+(k)\), mainly supported by \(S_{-1}\).

A target low-\(k\) expansion is:

\[
\omega_-^2=c_\gamma^2k^2+\beta k^4+O(k^6).
\]

The hidden \(S_{-1}\) carrier or reconstruction phase may be much faster than \(c_\gamma\), while the observable optical branch still satisfies approximately:

\[
\Omega_\gamma/K_\gamma\simeq c_\gamma.
\]

Fast hidden phase evolution must not be confused with observable packet, energy, or controllable information speed.

## 6. Polarization requires vector degrees of freedom

A scalar density model naturally favors longitudinal compression modes and is not sufficient for full polarization.

For a propagation vector \(\mathbf k\), transverse amplitudes satisfy:

\[
\mathbf A_T\cdot\mathbf k=0.
\]

An isotropic three-dimensional medium then has a two-dimensional transverse subspace, allowing linear, circular, and elliptical combinations.

However, geometry alone does not eliminate a longitudinal branch. The model must derive why it is constrained, gapped, decoupled from ordinary detectors, or otherwise absent from visible vacuum optics. A candidate mechanism is a rapid \(S_{-1}\) response producing a low-energy constraint:

\[
\nabla\cdot\mathbf q_0\simeq0.
\]

## 7. Motion as an in/out moving equilibrium

An \(S_0\) phase object is maintained by continuous in/out exchange. Uniform motion may be a front-back asymmetric but globally balanced traveling fixed point:

\[
f_{-1}(\mathbf x,\mathbf p,t)=f_{\mathbf v}(\mathbf x-\mathbf vt,\mathbf p),
\]

\[
\chi(\mathbf x,t)=\chi_{\mathbf v}(\mathbf x-\mathbf vt).
\]

Thus:

\[
\text{static symmetric state}\rightarrow\text{moving asymmetric state}.
\]

Inertia may arise from the momentum required to reconstruct the full \(S_0/S_{-1}\) dressing:

\[
\mathbf P(\mathbf v)=\mathbf P_0+\mathbf P_{-1}^{\rm dressing},
\qquad
M_{ij}=\partial P_i/\partial v_j.
\]

A Lorentz-like energy-momentum relation remains to be derived.

## 8. Tails are not deleted

The earlier requirement of “no wake” was too strong. The response should be separated into:

1. **Dressing tail** — travels with the packet and may be part of its identity.
2. **Memory/dispersion tail** — finite response time and nonlocality produce phase delay and weak long-distance dispersion.
3. **Free radiative tail** — carries independent energy-momentum and must be included in the decay budget.

The model should calculate:

\[
E_{\rm dress},\qquad P_{\rm rad},\qquad
\Delta t(\omega_1,\omega_2;L),
\]

rather than forcing every tail to vanish.

## 9. Media, reflection, refraction, and diffraction

Material media should be represented as changes in the local joint background:

\[
X_{\rm bg}=
(\rho_0,\rho_{-1},\mathbf M,\mathbf K_T,\mathbf K_L,\mathbf G,\tau,\xi).
\]

They modify:

\[
D(\omega,\mathbf k;X_{\rm bg})=0.
\]

Reflection and transmission should emerge from the same equations and flux-matching conditions across a parameter boundary. Refraction follows from phase matching and distinct dispersion relations. Diffraction follows from the transverse wave-vector spectrum created by a finite aperture, not from an added “diffraction force.”

## 10. Link to Q001

If \(S_0\) is a phase boundary in \(S_{-1}\), define:

\[
\Pi_{ij}=\int p_i v_j f_{-1}\,d^3p,
\qquad
F_i=-\oint_{\partial\Omega}\Pi_{ij}n_j\,dA.
\]

Different regions of one response tail may contribute to different effective phenomena:

\[
\begin{aligned}
\text{near-field gradient}&\rightarrow\text{phase transition and short-range exchange},\\
\text{moving asymmetric dressing}&\rightarrow\text{inertia},\\
\text{far-field stress tail}&\rightarrow\text{gravity candidate},\\
\text{temporal memory}&\rightarrow\text{dispersion and phase delay}.
\end{aligned}
\]

This is a unification conjecture, not a derivation.

## 11. Candidate Q002-M0 skeleton

A provisional quadratic energy is:

\[
E=\frac12\int d^3x\left[
\dot{\mathbf Q}^{T}\mathbf M\dot{\mathbf Q}
+(\nabla\cdot\mathbf Q)^T\mathbf K_L(\nabla\cdot\mathbf Q)
+(\nabla\times\mathbf Q)^T\mathbf K_T(\nabla\times\mathbf Q)
+\mathbf Q^T\mathbf G\mathbf Q
\right].
\]

The first model must test positivity, total energy and momentum conservation, absence of numerical drift, slow and fast branches, two transverse modes, explicit treatment of the longitudinal sector, and computable dispersion and attenuation.

The matrices must ultimately be derived from a unified local update or collision rule rather than chosen to encode the target result.

## 12. Relation to observation

EP does not logically have to contradict existing experiments, but possible compatibility is not established compatibility.

Current experiments operate at \(S_0\) and higher observable levels. They may not directly measure internal \(S_{-1}\) states or speeds, but they constrain the mapping:

\[
S_{-1}\text{ dynamics}\longrightarrow S_0\text{ outputs}.
\]

Path- or environment-dependent corrections may be investigated, but measured data cannot be dismissed solely because the detector is an \(S_0\)-level object.

## 13. Research stages

- **Q002-M0:** joint variables, energy, momentum, local exchange, and conservation.
- **Q002-M1:** homogeneous-background eigenvalue spectrum.
- **Q002-M2:** polarization, direction memory, and carrier replacement.
- **Q002-M3:** medium response, dispersion, absorption, and mixed modes.
- **Q002-M4:** interfaces, reflection, refraction, interference, diffraction, waveguides, and cavities.
- **Q002-M5:** freeze parameters and confront unused empirical tests.

## 14. Current conclusion

> **[CONJECTURE] Light may be a special transverse joint eigenmode of the recursive \(S_0/S_{-1}\) medium. Its visible core propagates at \(c_\gamma\), while deep reconstruction, phase, and broad \(S_{-1}\) response may occur on much faster scales. Polarization, interfaces, inertia, far-field interaction, and weak dispersion may be different scale projections of one response kernel.**

Next step: build Q002-M0 and prove or falsify the existence of two stable transverse slow modes, a controlled longitudinal sector, and a fast deep branch.
