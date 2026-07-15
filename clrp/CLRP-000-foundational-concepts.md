---
clrp-id: CLRP-000
title: Foundational Concepts
version: 0.2.0
status: Accepted
date: 2026-07-15
authors:
  - Synaptic Four
license: CC-BY-4.0
---

> **Status: Accepted** — This document represents an accepted programme commitment as of the stated version. Accepted directly during the initial single-steward phase of the programme (no separate Proposed comment period); the full Draft → Proposed → Accepted review cycle will apply once the steward group grows (see GOVERNANCE.md).

# CLRP-000: Foundational Concepts

## Abstract

The Cognitive Landscape Research Programme (CLRP) investigates human cognitive diversity using **continuous dimensional models** rather than categorical labels. Cognition is treated as **position and movement within a multidimensional landscape**—a metaphor with explicit mathematical and epistemic limits. This document states the programme's purpose, scope, and foundational commitments.

## 1. Purpose

### 1.0 Motivation

Human descriptions of cognitive difference have historically been categorical (temperaments, diagnoses, types) because categories are communicable and actionable, not because nature is organised that way. Wherever careful measurement has been possible, traits such as personality, intelligence, and temperament have turned out to vary continuously rather than in natural clusters. CLRP begins from a single question inherited from this history: **can human cognitive variation be represented in a way that reflects that continuity directly, rather than through the categorical compression the field inherited for practical reasons?** This is not a claim that current psychology, psychiatry, or neuroscience is mistaken—it is a research question worth organising a programme around.

CLRP exists to:

1. Develop and maintain **implementation-independent** standards for researching cognitive diversity as a landscape.
2. Define **principles**, **vocabulary**, and **evidence norms** that implementations (instruments, libraries, studies) can reference.
3. Coordinate **validation**, **cultural adaptation**, and **publication** without collapsing into a single codebase.
4. Preserve **intellectual honesty** about what is designed, hypothesised, simulated, or empirically supported.

CLRP does **not** exist to ship a product, provide clinical services, or certify individuals.

### 1.1 Two foundational contributions

CLRP rests on two contributions of equal standing:

| Contribution | Answers | Developed in |
|---|---|---|
| **Landscape representation** | Why the programme exists — treating cognitive variation as continuous position and movement rather than category membership | §2 |
| **Separation of claim-types** | How the programme had to be built once more than one discipline needed to describe the same landscape without collapsing into confusion | CLRP-004, CLRP-005 |

The first is not prior to or more important than the second: a landscape representation that does not also separate description, mechanistic explanation, and interpretation reproduces the same category-confusion problem it was built to avoid, one layer up.

## 2. Core metaphor: the cognitive landscape

### 2.1 Why geography, not just dimensions

A category answers "what is this?"; a landscape answers "where is this?" That difference is not decorative. A category has no interior geography—membership is binary. A landscape has neighbourhoods, distances, gradients, and barriers, which makes a different family of questions askable: where is someone positioned; what neighbouring regions exist; which directions of change are stable; where are the barriers to a given transition; does an intervention change the landscape itself or only movement through it. CLRP's vocabulary (CLRP-002) borrows consistently from geography for this reason—it is a working representational language, not a one-time illustrative device.

### 2.2 What the metaphor claims

- Cognitive variation can be **represented** as coordinates in a continuous space.
- Coordinates may **change over time** (trajectories), subject to measurement and modelling assumptions.
- **Density and topology** language (peaks, valleys, paths) aids intuition but must map to explicit operational definitions when used normatively.

### 2.3 What the metaphor does not claim

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

### 5.1 Ontology, epistemology, implementation

CLRP separates three layers that are easy to conflate: the landscape itself (**ontology**—what is there to be understood), the methods by which it is progressively characterised (**epistemology**—CLRP-001), and the computational models currently used to represent it (**implementation**—CLM, PCMS, and successors). An implementation improving is not a discovery about the landscape; a discovery about the landscape does not require any specific implementation to be correct. The programme is the enduring object across this separation; CLM and PCMS are not.

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
| 0.2.0 | 2026-07-15 | Accepted | Added §1.0 motivation, §1.1 two foundational contributions, §2.1 why-geography rationale, §5.1 ontology/epistemology/implementation separation. Accepted directly during single-steward phase. |

## References

- Kotov et al. (2017). The Hierarchical Taxonomy of Psychopathology (HiTOP). *Journal of Abnormal Psychology*.
- Insel et al. (2010). Research Domain Criteria (RDoC). *American Journal of Psychiatry*.
- See [bibliography/](../bibliography/README.md).
