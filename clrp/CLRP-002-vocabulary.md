---
clrp-id: CLRP-002
title: Vocabulary
version: 0.2.0
status: Accepted
date: 2026-07-15
authors:
  - Synaptic Four
license: CC-BY-4.0
---

> **Status: Accepted** — This document represents an accepted programme commitment as of the stated version. Accepted directly during the initial single-steward phase of the programme (no separate Proposed comment period); the full Draft → Proposed → Accepted review cycle will apply once the steward group grows (see GOVERNANCE.md).

# CLRP-002: Vocabulary

## Abstract

Controlled definitions for terms used across CLRP documents and conforming implementations. Terms here are **programme-level**; implementations may use additional internal names but must map to these definitions in conformance declarations.

## 1. Core terms

### Cognitive landscape

A **conceptual and mathematical space** in which cognitive variation is represented as locations and trajectories. Not a literal physical terrain.

### Coordinate / cognitive state

A vector of **dimension values** (typically bounded, e.g. unit interval) representing an estimate of standing on each dimension at a point in time, plus **uncertainty** where applicable.

### Dimension

A **continuous axis** hypothesised to capture meaningful variation. Dimensions are provisional until supported by evidence (CLRP-006). They are not diagnostic categories.

### Instrument

A procedure (questionnaire, observation protocol, task battery) that **produces coordinates** under a published protocol. PCMS is one instrument; others may exist.

### Measurement

The process of assigning coordinates and uncertainties from observed responses or behaviours, **without** assigning worldview meaning or clinical labels.

### Interpretation

A **non-causal reading** of coordinates within an explicit frame (e.g. scientific descriptive, systems metaphor). Interpretation must not modify measurement outputs.

### Trajectory

A time-ordered sequence of cognitive states. May be **observed** (repeated measurement) or **simulated** (model output). Must be labelled accordingly.

### Simulation

Model-generated evolution of coordinates under stated dynamics and structural assumptions. **Not** empirical prediction unless validated (CLRP-006).

### Structural layer

Slow-moving latent parameters that **constrain or modulate** dynamics and measurement relations—not directly observed in a single session.

### Validation

Empirical study demonstrating defined psychometric or scientific properties to stated thresholds. Design hypotheses alone are not validation.

### Locale

A **language–culture deployment context** (not ISO language code alone). Norms and items may be locale-specific.

### Conformance

A testable declaration that an implementation satisfies specified CLRP documents at stated versions.

### Feedback loop

A directed relationship in which change in one dimension influences another, which in turn influences the first, either amplifying or stabilising the pattern. Governs how coordinates change under the dynamics layer (CLRP-005).

### Attractor

A region of the state space toward which trajectories tend to converge under a model's dynamics. Describes a stable configuration, not a fixed destiny.

### Basin

The set of starting coordinates that converge toward a given attractor under a model's dynamics.

### Stability / instability

Descriptive, dynamical properties of a trajectory or region—how strongly the system resists or amplifies perturbation. **Not** a value judgment; stability is not "healthy" and instability is not "pathological."

### Similarity / distance

Formal relationships between two coordinates or trajectories, used to compare individuals or track change without invoking categorical sameness or difference.

### Calibration

The process of fitting structural parameters to observed patterns—a soft, regularised fit to design- and literature-informed priors, not discovery of a ground-truth latent trait.

### Ontology

A claim about what kind of thing something ultimately is (e.g. what a person fundamentally is). Ontological claims belong to the interpretation layer (CLRP-005), never to measurement.

### Worldview

A coherent set of ontological and value commitments (e.g. scientific-materialist, systems-theoretic, theological) through which interpretation occurs. The programme accommodates multiple worldviews without adjudicating between them.

### Intervention

An action intended to change a person's trajectory or position, evaluated against the landscape and dynamics (which feedback loop is targeted, which trajectory is intended)—not framed only as treatment for a named category.

## 2. Reserved terms (do not overload)

| Term | Reserved meaning |
|------|------------------|
| **Profile** | Coordinate vector at one time point—not a personality "type" |
| **Map** | Visualisation of coordinates—not a diagnosis |
| **Confidence** (instrument) | Engine stopping metric—not Cronbach's α |
| **Label** | Avoid for people; use "coordinate", "region", "pattern" |

## 3. Dimension naming (programme level)

Implementations may define concrete dimension sets (e.g. routing dimensions F–V in an instrument). CLRP does **not** fix the number or names of dimensions globally. New sets require:

- Definition in CLRP-002 amendment or extension document
- Validation plan (CLRP-006)

## 4. Abbreviations

| Abbrev | Meaning |
|--------|---------|
| CLRP | Cognitive Landscape Research Programme |
| CLRP-TR | CLRP Technical Report |
| CLRP-VR | CLRP Validation Report |
| CLRP-RN | CLRP Research Note |
| CLRP-P | CLRP Proposal |

## 5. Proposing new terms

Submit a PR amending this document or a [proposal](../proposals/README.md). Terms must not duplicate clinical diagnostic labels as dimension names.

## Revision history

| Version | Date | Status | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-07 | Draft | Initial controlled vocabulary |
| 0.2.0 | 2026-07-15 | Accepted | Added: feedback loop, attractor, basin, stability/instability, similarity/distance, calibration, ontology, worldview, intervention. Accepted directly during single-steward phase. |

## References

Internal: [CLRP-003](CLRP-003-measurement-principles.md), [CLRP-005](CLRP-005-layer-separation.md)
