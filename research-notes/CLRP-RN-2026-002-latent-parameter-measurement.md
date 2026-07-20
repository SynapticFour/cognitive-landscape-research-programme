---
note-id: CLRP-RN-2026-002
title: Latent parameter measurement and geology/environment framing
date: 2026-07-20
authors:
  - Synaptic Four
license: CC-BY-4.0
status: Exploratory
clrp-references:
  - CLRP-001
  - CLRP-002
  - CLRP-003
  - CLRP-007
  - CLRP-010
---

# CLRP-RN-2026-002: Latent parameter measurement and geology/environment framing

Discussion note following [CLRP-010](../clrp/CLRP-010-structural-theory-geology-of-the-landscape.md) (Draft) and exploratory CLM work referenced in [CLRP-RN-2026-001](CLRP-RN-2026-001-emergent-topology-derivation.md).

**Date:** 2026-07-20  
**Status:** Exploratory — not normative programme text

## Summary

[CLRP-010](../clrp/CLRP-010-structural-theory-geology-of-the-landscape.md) separates **geology** (latent structural parameters, slow or fixed) from **dynamics** (feedback graphs, environment-mediated and fluid). A working-session question on 2026-07-20 asked whether the informal distinction “fixed brain givens vs. fluid brain feedback loops” maps onto that architecture. This note records a **provisional yes**, an identified **measurement gap** under [CLRP-003](../clrp/CLRP-003-measurement-principles.md) M4, a **non-normative proposal** for how PCMS might eventually support posterior estimation, an **open ethics tension** with [CLRP-007](../clrp/CLRP-007-non-diagnostic-commitment.md), and a **flood analogy** linking stability vocabulary to recent exploratory simulation artefacts.

## Context

CLRP-010 develops CLRP-002’s structure/dynamics split into a geological metaphor: latent parameters shape which trajectories are probable; feedback dynamics unfold within that constraint field. Separately, the Cognitive Landscape Model (`@clm/structural`, `@clm/dynamics`) already implements `StructuralModel` latent parameters, `ProbabilisticDynamicsModulator`, and `FeedbackGraph` coupling — but, as [CLRP-RN-2026-001](CLRP-RN-2026-001-emergent-topology-derivation.md) documents, topology derivation still runs on **design-informed priors only**, not on estimates from real PCMS administrations.

This note captures programme-level discussion from 2026-07-20 before any specification change is proposed.

## Geology vs. dynamics: does the brain-givens / feedback-loops split fit?

**Question (informal):** Do “fixed brain givens” correspond to geology (latent structure) and “fluid brain feedback loops” to dynamics (environment-mediated coupling)?

**Provisional answer:** Yes — at the level of **current CLM architecture and naming**, the mapping is already plausible:

| Informal term | CLRP / CLM layer | Current PCMS-aligned example |
|---------------|------------------|------------------------------|
| Fixed, slow “brain givens” | Geology — `StructuralModel` latent parameters | `latent.sensory-gain`, `latent.prediction-stability`, `latent.stress-reactivity`, `latent.cognitive-bandwidth`, `latent.routing-flexibility` (PCMS preset in `@clm/structural`) |
| Fluid, context-sensitive coupling | Dynamics — `FeedbackGraph` edges and loops | Directed influences and cyclic gains over observed routing dimensions F–V |

The PCMS structural preset parameters are **already named** as putatively brain-based, relatively stable quantities — not as momentary routing scores. Dynamics, by contrast, modulates how observed dimensions co-evolve under feedback and (when sampled) structural bias. Nothing in this note **asserts** neurobiological validity of those labels; it only records that the **architectural slot** for “givens vs. loops” exists and is populated with semantically aligned placeholders.

## Identified gap: design hypotheses only (CLRP-003 M4)

[CLRP-003 §M4](../clrp/CLRP-003-measurement-principles.md) states that parameters derived from literature or expert design are **hypotheses** until CLRP-VR reports empirical estimation — and must not be presented as calibrated when they are not.

**Current state:**

- Latent parameters in `createPcmsStructuralModel()` carry **prior** means and variances set by design.
- `CalibrationEngine` can update posteriors in principle, but **nothing in the PCMS → CLM pipeline** currently supplies observational constraints that identify those latent parameters from real response data.
- Landscape-layer PCMS output (routing profiles F–V) constrains **observed state**, not **latent geology** directly.

So the geology/dynamics distinction is **architecturally real** but **empirically unoccupied** at the latent layer: geology remains a design story, consistent with M4, not a measured one.

## Proposal for discussion (non-normative)

**Idea only — not a programme commitment:**

PCMS could be extended with **item families** whose response patterns are intended to inform specific latent parameters — e.g. items probing sensory filtering or reactivity → updates to `latent.sensory-gain`; items probing predictability tolerance → `latent.prediction-stability`; and similarly for the other preset parameters.

If such items existed and met measurement-quality thresholds (future CLRP-VR work), `CalibrationEngine` could move from **prior-only** structural models toward **posterior** estimates anchored in administrations — a concrete step toward [CLRP-001](../clrp/CLRP-001-discovering-the-cognitive-landscape.md) **Layer 3 (Topology)** using **observed** rather than purely **simulated** structure.

**Explicit limits of this proposal:**

- No item content, scoring rules, or validation design are specified here.
- No claim that current PCMS dimensions F–V already identify latent parameters (they do not, by construction).
- No timeline or implementation mandate for PCMS or CLM.

## Open tension: clinical proximity and CLRP-007

Items that probe sensory reactivity, prediction rigidity, or stress baseline can sit **content-wise adjacent** to items found in **clinical screening instruments** (e.g. autism-spectrum screening questionnaires). That proximity is not accidental — it reflects overlapping construct language — but it triggers [CLRP-007](../clrp/CLRP-007-non-diagnostic-commitment.md) directly:

- PCMS must not silently become a diagnostic or screening tool through item accretion.
- Any latent-parameter item bank would likely need an **explicit, labelled category** in PCMS (separate from core routing assessment, separate UI framing, separate consent copy) — **not** a quiet expansion of the existing questionnaire.

**Status:** recorded as an **open question**, not resolved. This note does **not** propose a CLRP-007 exception or a PCMS product decision.

## Illustrative analogy: flood as instability episode (not formal definition)

The following mapping is **pedagogical only** — not a new CLRP definition:

| Analogy element | Landscape vocabulary | Role |
|-----------------|---------------------|------|
| Soil permeability (fixed) | Geology / latent structure | Slow constraint on how much “saturation” the system can absorb |
| Current terrain shape | Landscape state (PCMS routing profile) | What is **measured** now |
| Rain | Environment / external input | Perturbation on top of current state |
| Flood | **Instability episode** | Feedback between saturation and runoff **tips**; control loss of dynamics — **not** a new stable attractor basin |

This aligns with [CLRP-002](../clrp/CLRP-002-vocabulary.md) stability/instability language: instability is a **regime of dynamics**, not a permanent geological feature.

**Link to exploratory CLM work (technical, not empirical):** Recent exploratory runs of `deriveEmergentTopology()` (see [CLRP-RN-2026-001](CLRP-RN-2026-001-emergent-topology-derivation.md) context; CLM branch `feat/emergent-topology`, not normative) showed frequent **boundary saturation** — converged states with many dimensions at 0 or 1 after clamping — when step budgets were sufficient. That pattern is **conceptually parallel** to “feedback running against a limit rather than settling in an interior equilibrium,” but it is **almost certainly a simulation and calibration artefact** (design priors, uncalibrated dynamics, finite steps), **not** evidence about real people. Worth noting as a **technical echo** of the flood metaphor; **must not** be cited as a psychological or clinical finding.

## Provisional conclusions

| Claim | Epistemic level (CLRP-004) |
|-------|----------------------------|
| CLM’s geology/dynamics split can host “givens vs. loops” informally | L2 — architectural fit, not validated construct mapping |
| Latent PCMS-preset parameters are design hypotheses only (M4) | L3 — consistent with CLRP-003 and current implementation |
| Latent-parameter items + calibration → Topology with real data | L2 — proposed direction, not specified or approved |
| Screening-adjacent items require explicit PCMS category + CLRP-007 review | L2 — open governance/design question |
| Flood analogy clarifies instability vs. attractor | L2 — illustrative only |
| Boundary saturation in exploratory simulation | L2 — technical artefact; parallel to metaphor, not human data |

## Next steps

- [ ] Decide whether to open a **CLRP proposal** (or CLRP-010 amendment) on latent-parameter measurement boundaries — **after** separate review of this note.
- [ ] If PCMS item work proceeds: draft **non-diagnostic** item-category specification and CLRP-007 alignment checklist before any item text.
- [ ] If calibration proceeds: define **CLRP-VR** requirements for identifying latent parameters (identifiability, not just face validity).
- [ ] Keep exploratory CLM topology runs clearly labelled **simulation-on-priors** (CLRP-RN-2026-001; CLRP-003 M4).

## References

- [CLRP-001 — Discovering the Cognitive Landscape](../clrp/CLRP-001-discovering-the-cognitive-landscape.md) — Layer model; Layer 3 Topology
- [CLRP-002 — Landscape Vocabulary](../clrp/CLRP-002-vocabulary.md) — Stability / instability
- [CLRP-003 — Measurement Principles](../clrp/CLRP-003-measurement-principles.md) — §M4 design vs calibrated parameters
- [CLRP-007 — Non-Diagnostic Commitment](../clrp/CLRP-007-non-diagnostic-commitment.md)
- [CLRP-010 — Structural Theory (Geology of the Landscape)](../clrp/CLRP-010-structural-theory-geology-of-the-landscape.md)
- [CLRP-RN-2026-001 — Emergent topology derivation (CLM design)](CLRP-RN-2026-001-emergent-topology-derivation.md)
