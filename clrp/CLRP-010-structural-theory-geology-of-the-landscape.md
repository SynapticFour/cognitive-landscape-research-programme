---
clrp-id: CLRP-010
title: Structural Theory (Geology of the Landscape)
version: 0.1.0
status: Draft
date: 2026-07-20
authors:
  - Synaptic Four
license: CC-BY-4.0
---

> **Status: Draft** — This document is work in progress and does not yet represent an accepted programme commitment. Given its subject matter, this document is expected to go through the full Draft → Proposed → Accepted cycle (see GOVERNANCE.md), not a single-steward direct acceptance.

# CLRP-010: Structural Theory (Geology of the Landscape)

## Abstract

CLRP-002 defines **structure** as the slow-moving latent organisation that shapes which states and trajectories are more or less probable, distinct from the moment-to-moment dynamics it constrains. This document develops that definition into a theory: how a small number of latent, non-observed parameters, coupled probabilistically and many-to-many to observed dimensions, give rise to the landscape's **topology** — its attractors, basins, and barriers (CLRP-001 §3.3). It also states, as a first-class commitment rather than an afterthought, what this layer must never be used to claim.

## 1. Core commitments

### G1 — Topology is emergent, not authored

Attractors, basins, and barriers are outputs of a structural model plus a feedback graph, computed or estimated — never hand-specified as a starting assumption. An implementation that lets someone directly declare "there is an attractor here" without deriving it from underlying structure and dynamics does not conform to this document.

### G2 — Latent parameters are not traits

A latent parameter is a hidden structural variable (CLRP-002, "Constraint"). It is not equivalent to, named after, or presented as any observed trait, diagnosis, or behavioural label. A latent parameter has no meaning on its own; it only has effects, mediated through influence fields onto observed dimensions.

### G3 — Coupling is many-to-many, never one-to-one

A latent parameter must influence more than one observed dimension; an observed dimension must be influenced by more than one latent parameter (already enforced in `@clm/structural`, `assertManyToManyStructure`). This is a structural safeguard against a latent parameter silently becoming a proxy diagnostic label.

### G4 — Multiple realisability

The same observed phenotype (region of the landscape) may be reached from different underlying structural configurations, and the same structural configuration may, under different dynamics, express as different observed phenotypes. Structure constrains what is reachable; it does not uniquely determine what is observed.

### G5 — Structure constrains; environment-mediated dynamics select

This is the central theoretical move of this document. Latent parameters and influence fields (geology) change slowly, if at all, and are not the intended target of intervention research under this programme. **Feedback loop edges** (`FeedbackGraph`, CLRP-002 "Feedback loop") are where environmental and contextual influence enters the model. A change in which attractor a trajectory converges toward can therefore be modelled as a change in feedback dynamics — how the person's environment and context couple their observed dimensions to one another — without any claim that the underlying latent structure itself has changed. This gives the programme a principled way to model "the same person, processing their environment differently, ending up in a different region of the landscape" without modelling "curing," "fixing," or "removing" any underlying structure.

### G6 — No structural claim is a diagnostic claim

Consistent with CLRP-007: no output of a structural model — a latent parameter estimate, a derived attractor, a basin membership — may be presented as, or used as a substitute for, a clinical or psychiatric diagnosis.

### G7 — No structural or topological claim is a value judgment

This document and any implementation built on it must not rank attractors, basins, or phenotypic regions as better or worse, healthier or less healthy, or more or less desirable. Distance, stability, and basin size are descriptive, dynamical properties (CLRP-002, "Stability / instability": *"not a value judgment"*). Whether movement toward a particular region is desirable for a given person is a question for that person (and, where relevant, their own worldview or clinicians) — never an output of the structural model itself. This document deliberately does not define "improvement," "severity," or "outcome" in evaluative terms; where it uses such words elsewhere in the programme's research (e.g. CLRP-001 §3.5 "Intervention"), they refer only to a measurable change in trajectory or topology, not to a claim about whether that change is good.

## 2. Deriving topology from structure

Given a `StructuralModel` (latent parameters + probabilistic influence fields, `@clm/structural`) and a `FeedbackGraph` (observed-dimension coupling, `@clm/dynamics`), emergent topology is derived, not declared, by:

1. Sampling latent parameter values from their priors (or posteriors, where calibrated).
2. Propagating each sample through the influence fields to obtain an initial bias over observed dimensions.
3. Relaxing many seeded initial states forward under the feedback graph's dynamics until convergence (or a step budget is exhausted).
4. Clustering the converged end-states across samples; each sufficiently supported cluster is an **emergent attractor**, with its basin support given by the fraction of samples that converged to it.

This treats topology as **probabilistic and sample-based**, consistent with CLRP-001's Topology layer methodology and with CLRP-004's commitment that structural parameters are working hypotheses, not discovered ground truth. See the companion implementation design ([CLRP-RN-2026-001](../research-notes/CLRP-RN-2026-001-emergent-topology-derivation.md); target module `@clm/dynamics` `emergent-topology`) for the computational design.

## 3. What this layer does not claim

- That a specific latent parameter or parameter combination *is* any named condition (e.g. autism, ADHD) — see G2, G6.
- That an emergent attractor represents a fixed, unchangeable destiny — attractors are properties of the current model, not metaphysical facts about a person (CLRP-002, "Attractor": *"a stable configuration, not a fixed destiny"*).
- That moving a trajectory away from one attractor toward another is inherently good, bad, therapeutic, or harmful — see G7.
- That environment-mediated dynamics changes (G5) are easy, fast, or currently demonstrated to work in practice; this document is theory, not an intervention efficacy claim (that is future, separate work — see §5).
- That this theory is validated against real longitudinal data. As of this version, it is design- and simulation-based (CLRP-001 §4, method 3), pending the Topology and Dynamics layers of empirical work (CLRP-001 §3.3–3.4).

## 4. Relationship to implementation

- `@clm/structural`: `LatentParameter`, `ProbabilisticInfluence`, `StructuralModel` — the geology.
- `@clm/dynamics`: `FeedbackGraph`, `AttractorState`, `structural-modulation.ts` — the dynamics, and the existing bridge from structure into dynamics.
- The derivation in §2 is new work; as of this version, `AttractorState` values in `@clm/dynamics` are still authored by hand rather than derived (see [CLRP-RN-2026-001](../research-notes/CLRP-RN-2026-001-emergent-topology-derivation.md) for the proposed `emergent-topology` module that closes this gap).

## 5. Non-goals

- This document is not an intervention protocol and does not claim any specific intervention changes any specific trajectory. That is deferred to a future, separate document (working title CLRP-011, Intervention Principles), which must independently establish the mechanistic/normative separation before any implementation work on interventions begins.
- This document does not claim to explain the aetiology of any specific condition.
- This document does not provide a severity scale intended for clinical or diagnostic use (see CLRP-007).

## Revision history

| Version | Date | Status | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-20 | Draft | Initial publication |

## References

- [CLRP-001](CLRP-001-discovering-the-cognitive-landscape.md) — §2 (Landscape discovery vs. model validation), §3.3–3.5 (Topology, Dynamics, Intervention layers)
- [CLRP-002](CLRP-002-vocabulary.md) — Structure, Attractor, Basin, Feedback loop, Stability/instability
- [CLRP-004](CLRP-004-epistemic-commitments.md) — Explicit non-assumptions
- [CLRP-005](CLRP-005-layer-separation.md) — Description / explanation / interpretation separation
- [CLRP-007](CLRP-007-non-diagnostic-commitment.md) — Non-diagnostic commitment
