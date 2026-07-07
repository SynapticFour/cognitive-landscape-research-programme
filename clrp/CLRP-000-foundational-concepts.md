---
clrp-id: CLRP-000
title: Foundational Concepts
version: 0.1.0
status: Draft
date: 2026-07-07
authors:
  - Synaptic Four
license: CC-BY-4.0
---

> **Status: Draft** — This document is work in progress and does not yet represent an accepted programme commitment.

# CLRP-000: Foundational Concepts

## Abstract

The Cognitive Landscape Research Programme (CLRP) investigates human cognitive diversity using **continuous dimensional models** rather than categorical labels. Cognition is treated as **position and movement within a multidimensional landscape**—a metaphor with explicit mathematical and epistemic limits. This document states the programme's purpose, scope, and foundational commitments.

## 1. Purpose

CLRP exists to:

1. Develop and maintain **implementation-independent** standards for researching cognitive diversity as a landscape.
2. Define **principles**, **vocabulary**, and **evidence norms** that implementations (instruments, libraries, studies) can reference.
3. Coordinate **validation**, **cultural adaptation**, and **publication** without collapsing into a single codebase.
4. Preserve **intellectual honesty** about what is designed, hypothesised, simulated, or empirically supported.

CLRP does **not** exist to ship a product, provide clinical services, or certify individuals.

## 2. Core metaphor: the cognitive landscape

### 2.1 What the metaphor claims

- Cognitive variation can be **represented** as coordinates in a continuous space.
- Coordinates may **change over time** (trajectories), subject to measurement and modelling assumptions.
- **Density and topology** language (peaks, valleys, paths) aids intuition but must map to explicit operational definitions when used normatively.

### 2.2 What the metaphor does not claim

- The landscape is not a literal neural map or neuroanatomical model.
- Coordinates are not innate essences or fixed identities.
- Simulation trajectories are not observations of future behaviour without explicit labelling.
- Low-dimensional projections are not exhaustive descriptions of a person.

See [CLRP-001](CLRP-001-discovering-the-cognitive-landscape.md) for the discovery-oriented framing.

## 3. Programme boundaries

### 3.1 In scope

- Dimensional measurement theory (programme level)
- Separation of measurement, dynamics, structure, explanation, and interpretation
- Validation and cross-cultural adaptation standards
- Ethical constraints (non-diagnostic, non-gatekeeping)
- Conformance model for implementations

### 3.2 Out of scope

- Clinical diagnosis, treatment planning, or screening
- Employment, education, or immigration decision systems
- Specific question text, UI copy, or API signatures
- Claims of genetic determinism or hierarchical human worth

## 4. Foundational commitments

| # | Commitment | Document |
|---|------------|----------|
| 1 | Continuous dimensional modelling | CLRP-001, CLRP-003 |
| 2 | Shared controlled vocabulary | CLRP-002 |
| 3 | Measurement ≠ interpretation | CLRP-005 |
| 4 | Explicit epistemic status of claims | CLRP-004 |
| 5 | Evidence before utility claims | CLRP-006 |
| 6 | Non-diagnostic, non-gatekeeping use | CLRP-007 |
| 7 | Cultural adaptation ≠ translation | CLRP-008 |
| 8 | Implementations reference CLRP; do not redefine it | CLRP-009 |

## 5. Relationship to implementations

CLRP is **constitution**; implementations are **statutes and case law**:

- **Instruments** (e.g. adaptive questionnaires) produce coordinates under stated protocols.
- **Libraries** (e.g. simulation frameworks) represent and transform coordinates under stated models.
- **Studies** (validation reports) test whether instruments and models meet programme evidence standards.

No implementation is authoritative for programme principles.

## 6. Audience

- Researchers in differential psychology, psychometrics, cognitive science
- Instrument designers and open-source contributors
- Ethics reviewers and institutional boards
- Educators and self-directed learners (with appropriate disclaimers)
- Implementers building conformant systems

## 7. Non-goals

CLRP will not:

- Certify individuals or organisations
- Rank cultures or populations on cognitive "quality"
- Replace peer review
- Mandate a single programming language or instrument

## 8. Open questions

See [open-questions/](../open-questions/README.md). Initial examples:

- Optimal dimensionality for public-facing vs research-facing instruments
- Conditions under which simulated trajectories inform hypotheses about real change
- Community governance beyond initial stewardship

## Revision history

| Version | Date | Status | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-07 | Draft | Initial publication |

## References

- Kotov et al. (2017). The Hierarchical Taxonomy of Psychopathology (HiTOP). *Journal of Abnormal Psychology*.
- Insel et al. (2010). Research Domain Criteria (RDoC). *American Journal of Psychiatry*.
- See [bibliography/](../bibliography/README.md).
