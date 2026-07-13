# Q001: Can Collision Layers Map to Long-Range Attraction, Boundary Effects, and Short-Range Repulsion?

**Date: 2026-07-13**  
**Status: [OPEN] The concept is formulated; the mathematical and numerical model is not yet complete**  
**Stages: EP-F0 → EP-F4**

## 1. Why study this problem?

Early EP models can easily reduce collision dynamics to:

\[
\text{free motion}\rightarrow\text{contact}\rightarrow\text{instantaneous rebound}.
\]

However, gases, liquids, and bound systems suggest that objects may already affect one another through surrounding distributions, correlations, and boundary responses before what is ordinarily called a collision.

“Free motion” and “collision” may therefore be different coupling regimes of one continuous process rather than two fundamentally separate events.

This leads to the question:

> Can long-range attraction, boundary-dependent interaction, and short-range repulsion all arise from collision statistics and momentum-flux reconfiguration at different recursive layers and scales?

If not, EP must introduce additional degrees of freedom or abandon this unification route. If so, the result would provide an important common foundation.

## 2. What this means for EP

### 2.1 Force is not assumed as a primitive

Define the \(S_{-1}\) background distribution:

\[
f_{-1}(\mathbf x,\mathbf p,t).
\]

Define the momentum-flux tensor:

\[
\Pi_{ij}=\int p_i v_j f_{-1}\,d^3p.
\]

Define the net action on a boundary:

\[
F_i=-\oint_{\partial\Omega}\Pi_{ij}n_j\,dA.
\]

Gravity, the Casimir force, and repulsion are not inserted here. Only an imbalance of momentum flux across a boundary is measured.

### 2.2 Object and environment form a joint steady state

An \(S_0\) object is not placed inside an otherwise empty container. Its boundary changes the surrounding \(S_{-1}\) background, including:

- density;
- directional distribution;
- correlation length;
- collision rate;
- reflection and release probabilities;
- momentum flux.

The background response then affects the motion and stability of \(S_0\).

The actual object of study is therefore:

\[
S_0+\text{the surrounding }S_{-1}\text{ response as one joint steady state}.
\]

## 3. Central conjecture

[CONJECTURE]

> Long-range attraction, boundary effects, and short-range repulsion may be effective projections of one recursive collision–boundary stress mechanism in different regimes of distance, geometry, layer, and compression.

Symbolically:

\[
C[f,\chi]
\rightarrow
f_{\rm steady}
\rightarrow
\Pi[f]
\rightarrow
\begin{cases}
\text{far-field flux dilution},\\
\text{boundary-mode reconfiguration},\\
\text{high-density pressure reversal}.
\end{cases}
\]

Here \(C\) is the unified local update operator and \(\chi\) represents a boundary or phase state.

## 4. Why an inverse-square far field may emerge

Under the conditions that:

1. space is three-dimensional;
2. the response is isotropic;
3. a low-wavenumber flux is conserved;
4. the far field is not cut off by a finite correlation length;

the same total flux crosses a sphere of radius \(r\):

\[
A(r)=4\pi r^2.
\]

The flux per unit area is then:

\[
j(r)=\frac{Q}{4\pi r^2}.
\]

If the net action on a boundary is proportional to this flux bias, then:

\[
F(r)\propto-\frac1{r^2}.
\]

This is a conditional derivation, not a derivation of real-world gravity. Source strength, superposition, screening, drag, heating, and material dependence still have to be tested.

## 5. Why a short-range interaction may disappear at long distance

Candidate mechanisms include:

- a finite correlation length producing an exponential cutoff;
- cancellation of low-order sources when an object is neutral at a given layer;
- boundary effects that matter only when the constrained regions overlap;
- an interaction that appears short-ranged at the \(S_0\) level but remains continuous collision statistics at the \(S_{-1}\) level.

“Long range” and “short range” may therefore be effective descriptions relative to an observational scale.

## 6. Power laws should not be treated as one fixed sequence

The project is motivated by scalings such as \(1/r^2\), \(1/a^4\), and \(1/r^7\), but it must distinguish among:

- force;
- pressure;
- potential energy;
- geometry;
- boundary conditions;
- source structure;
- recursive-layer projection.

EP should not presuppose a universal sequence \(2\rightarrow4\rightarrow7\).

The actual test is:

> Can the same collision-statistics rule generate different effective powers as scale, geometry, and source structure change?

## 7. How attraction may emerge

Let the normal momentum flux between two objects be \(P_{\rm gap}\), and let the corresponding outer flux be \(P_{\rm out}\).

If:

\[
P_{\rm gap}<P_{\rm out},
\]

then:

\[
F_{\rm net}=A_{\rm eff}(P_{\rm gap}-P_{\rm out})<0.
\]

The exterior background pushes more strongly than the interior background, and the effective high-level description is attraction.

No attractive force has been inserted; only a momentum-flux imbalance has been measured.

## 8. Why further compression may produce repulsion

As the separation becomes smaller, the gap may exhibit:

- increasing constituent density;
- increasing collision rate;
- enhanced boundary reflection;
- compressed correlation structure;
- fewer available states;
- delayed release of deeper-layer constituents;
- additional directed momentum flux caused by relative motion.

A measurement decomposition can be written as:

\[
P_{\rm gap}(r,v)
=
P_{\rm eq}(r)
+
P_{\rm dyn}(r,v)
+
P_{\rm corr}(r,v).
\]

This does not represent three fundamental forces; it separates contributions to one total stress.

At large separation:

\[
P_{\rm gap}<P_{\rm out}.
\]

At a critical point:

\[
P_{\rm gap}=P_{\rm out}.
\]

At still smaller separation:

\[
P_{\rm gap}>P_{\rm out}.
\]

Attraction and repulsion may therefore be two branches of one pressure-response function.

## 9. Why approach speed may matter

At higher relative speed, the background in the gap may not have time to relax to a static steady state. The additional dynamic pressure may scale approximately as:

\[
\Delta P_{\rm dyn}\sim\rho_{\rm eff}v_{\rm rel}^2.
\]

A critical speed may satisfy:

\[
P_{\rm gap}(r,v_c)=P_{\rm out}.
\]

At the same separation, slow approach may remain attractive while fast approach enters a compressed rebound branch.

This does not yet justify saying that real gravity changes sign. The test is only whether the total collision stress can reverse sign continuously.

## 10. Stable scale and spring-like response

Suppose:

\[
F(r)>0\quad(r<r_*),
\]

and:

\[
F(r)<0\quad(r>r_*).
\]

Then a zero exists at:

\[
F(r_*)=0.
\]

If:

\[
\left.\frac{\partial F}{\partial r}\right|_{r_*}<0,
\]

the equilibrium is stable. Near that point:

\[
F(r)\approx-k_{\rm eff}(r-r_*).
\]

Spring-like restoring behavior would then be the linear approximation of a continuous attraction–repulsion curve near its stable zero, rather than a separately imposed rule.

## 11. Minimal model

### State

\[
f_{-1}(\mathbf x,\mathbf p,t),\qquad \chi(\mathbf x,t).
\]

### Update

\[
\partial_t f_{-1}
+\mathbf v\cdot\nabla_{\mathbf x}f_{-1}
=
C[f_{-1},\chi].
\]

### Boundary rule

\[
f_{\rm out}=\mathcal B_\chi[f_{\rm in}].
\]

The boundary may change only quantities such as outgoing direction, outgoing speed, temporary locking probability, release time, and cross-layer exchange probability.

### Measurement

\[
\Pi_{ij}=\int p_i v_j f_{-1}\,d^3p,
\]

\[
F_i=-\oint\Pi_{ij}n_j\,dA.
\]

Every attractive or repulsive response must be measured using this definition.

## 12. Experimental route

### EP-F0: Empty-background audit

Test isotropy, energy conservation, momentum conservation, and artificial drift.

### EP-F1: Single-boundary steady state

Measure \(f_{-1}\), \(\Pi\), and the spatial decay around one \(S_0\).

### EP-F2: Static two-boundary scan

Scan separation and measure \(P_{\rm gap}\), \(P_{\rm out}\), and the full \(F(r)\) curve without fitting a target power in advance.

### EP-F3: Geometry scan

Test two spheres, parallel boundaries, sphere–plane geometry, and localized neutral objects.

### EP-F4: Velocity scan

Measure:

\[
F(r,v_{\rm rel}),
\]

and search for a continuous attraction–zero–repulsion surface.

### EP-F5: Stability

Perturb candidate equilibria and determine whether they return, oscillate, decay, diverge, or collapse.

## 13. How success would improve the model

If one underlying rule passes these tests, EP would gain:

1. a unified definition of force as net boundary momentum flux;
2. a common source of attraction and repulsion;
3. a mechanism for stable finite-size phase-transition objects;
4. a generative explanation of long-range versus short-range behavior;
5. a microscopic bridge between the far-field and boundary-interaction routes in Paper I;
6. a concrete interpretation of an \(S_0\)-level interaction as an \(S_{-1}\)-level collision-statistics projection.

## 14. What success would not yet prove

Even a successful minimal model would not immediately prove:

- the nature of real gravity;
- that the Casimir effect originates from EP;
- dark matter, dark energy, or the Big Bang;
- a completed unification of quantum theory and relativity.

It would establish only that a local model without a primitive force concept can generate candidate cross-scale attraction, boundary effects, and high-density repulsion.

## 15. Failure criteria

The present route would be seriously undermined if:

1. target power laws must be inserted directly;
2. different geometries require different fundamental rules;
3. attraction and repulsion require unrelated mechanisms;
4. only one fine-tuned parameter point works;
5. unacceptable drag, heating, or screening appears;
6. energy or momentum fails to close;
7. results depend on the numerical grid or box boundary;
8. high density produces only numerical blow-up rather than a stable repulsive branch;
9. parameters cannot transfer across scales;
10. finite-sample noise cannot be separated from a genuine collective response.

## 16. Next step

Do not extend the model to cosmology yet. Complete EP-F0 first:

1. define \(f_{-1}\);
2. define the boundary state \(\chi\);
3. design a unified collision operator with no target force law;
4. define the momentum-flux tensor;
5. build an empty-background conservation audit;
6. build minimal two-dimensional single- and double-boundary simulations;
7. preregister pass and failure criteria.

## 17. Current conclusion

\[
\boxed{
\text{Attraction, boundary effects, and repulsion may be different branches of one recursive collision-stress function across scale, geometry, density, and relative velocity.}
}
\]

This proposition is worth publishing, formalizing, and attempting to falsify.
