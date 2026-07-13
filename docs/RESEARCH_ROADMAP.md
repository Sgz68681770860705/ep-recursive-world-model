# EP Recursive Collision–Phase-Transition World Model: Research Roadmap

**Version: V0.1**  
**Status: Living research index**

## 1. Purpose of this roadmap

This file is neither a paper nor a final theory. It records:

1. the problems we are currently trying to solve;
2. why each problem matters;
3. the candidate explanations under consideration;
4. what has already been derived or simulated;
5. what remains conjectural;
6. what results would force us to revise or abandon a route.

We do not claim to have listed every core problem in advance. We document each problem as it becomes sufficiently clear to formulate and test.

## 2. Overall goal

The EP research program asks:

> Does there exist a sufficiently minimal and unified local update or collision model from which space, stable structures, propagation, inertia, effective interactions, and recursive layers can emerge without being inserted in advance?

EP is not currently presented as a confirmed theory. The immediate objective is to construct minimal models that can be calculated, compared with evidence, and falsified.

## 3. Current methodological position

At the fundamental level, EP does not yet treat “force” as a primitive concept. It starts from:

- local states;
- local motion;
- collision, exchange, or reconfiguration;
- boundary states;
- energy and momentum accounting;
- coarse-graining between recursive layers.

At an effective level, force is provisionally defined as the net momentum flux across a boundary:

\[
F_i=-\oint_{\partial\Omega}\Pi_{ij}n_j\,dA.
\]

Attraction and repulsion should therefore emerge from different signs of the same momentum-flux imbalance, rather than being introduced as separate fundamental forces.

## 4. Current problem index

### Q001: Can long-range attraction, boundary-mediated interaction, and short-range repulsion arise from one recursive collision-statistics mechanism?

**Status: A minimal mathematical model is being formulated**

Core question:

> Without presupposing gravity, the Casimir force, or short-range repulsion, can one \(S_0/S_{-1}\) collision–boundary response generate long-range attraction, boundary-dependent interaction, and high-density repulsion in different regimes of scale, geometry, and compression?

Detailed note:

- [Q001 research note](notes/Q001-2026-07-13-collision-statistics-and-scale-mapped-forces.md)

## 5. Problems to solve in sequence

### Layer 1: Definitions

1. What is \(S_0\)?
2. What is the \(S_{-1}\) background?
3. How does an \(S_0\) boundary alter the incidence, reflection, locking, and release of \(S_{-1}\) constituents?
4. Is a “collision” an instantaneous contact event, or the strong-coupling regime of a continuous interaction?
5. How should the momentum-flux tensor and the net boundary action be defined?

### Layer 2: Far field

1. Does a single boundary generate a gapless, conserved, low-wavenumber response?
2. Does that response dilute over spherical surfaces in three-dimensional isotropic space?
3. Can a far-field inverse-square law emerge without being written into the update rule?
4. Does the model generate unacceptable screening, drag, persistent heating, or material dependence?

### Layer 3: Boundary and intermediate-distance effects

1. How are allowed background modes changed when two boundaries approach?
2. Can a difference between inner and outer momentum flux produce attraction?
3. Are effective power laws determined by geometry, dimensionality, boundary conditions, and source structure?
4. Can one rule treat parallel boundaries, spherical objects, and localized neutral objects?

### Layer 4: High density and repulsion

1. As separation decreases, do density, collision rate, reflectivity, and correlation increase in the gap?
2. Is there a critical point at which \(P_{\rm gap}=P_{\rm out}\)?
3. At smaller separation, does a repulsive branch with \(P_{\rm gap}>P_{\rm out}\) emerge?
4. Does relative approach speed cause the sign change to occur earlier?
5. Near equilibrium, does the response reduce naturally to \(F\approx-k(r-r_*)\)?

### Layer 5: Unification

1. Can the far, intermediate, and near regimes use the same collision operator?
2. Can distance, geometry, boundary state, and velocity vary without changing the underlying rule?
3. Can the same parameters be carried across scales?
4. If every phenomenon requires an additional patch, the unification attempt should be judged unsuccessful.

## 6. Planned stages

- **EP-F0: Minimal definition of unified collision stress**
- **EP-F1: Single-boundary response**
- **EP-F2: Two-boundary attraction**
- **EP-F3: Geometry and boundary spectrum**
- **EP-F4: Compression and sign reversal**
- **EP-F5: Cross-scale unification test**

## 7. Research-status labels

```text
[POSTULATE]   Model postulate
[DEFINITION]  Definition
[CONJECTURE]  Conjecture
[DERIVED]     Derived result
[NUMERICAL]   Numerical result
[EMPIRICAL]   Empirical fact
[FAILED]      Failed route or test
[OPEN]        Unresolved problem
```

## 8. Current rules of practice

- Do not insert target power laws directly.
- Do not add separate “gravity,” “Casimir,” or “repulsion” terms.
- Measure attraction and repulsion from one momentum-flux definition.
- Preserve and publish failed results.
- Complete Q001 before extending the model to cosmological claims.
