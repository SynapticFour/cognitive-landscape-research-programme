---
clrp-id: CLRP-001
title: Discovering the Cognitive Landscape
version: 0.2.0
status: Accepted
date: 2026-07-15
authors:
  - Synaptic Four
license: CC-BY-4.0
---

> **Status: Accepted** — This document represents an accepted programme commitment as of the stated version. Accepted directly during the initial single-steward phase of the programme (no separate Proposed comment period); the full Draft → Proposed → Accepted review cycle will apply once the steward group grows (see GOVERNANCE.md).

# CLRP-001: Discovering the Cognitive Landscape

## Abstract

This document frames CLRP's scientific orientation: **discovery** rather than classification. The programme treats cognitive diversity as observable structure in continuous spaces, explored through measurement, modelling, and honest reporting—not through assigning people to discrete types.

## 1. Discovery vs classification

### 1.1 Classification paradigm (explicitly not adopted)

- Assigning individuals to categories (types, disorders, labels)
- Optimising for crisp boundaries and diagnostic thresholds
- Implying normality as a single centre with deviation as deficit

### 1.2 Discovery paradigm (adopted)

- Estimating coordinates on dimensions with uncertainty
- Mapping **regions** of preference, sensitivity, or strategy
- Treating group differences as **statistical and contextual**, not hierarchical
- Revising dimensions when evidence fails to support them

### 1.3 The landscape is not any single model

The distinction this document depends on most: **the cognitive landscape is the enduring object of discovery; any given computational model is a provisional, evolving representation of it.** Physics is not the Standard Model; evolutionary biology is not one phylogenetic algorithm; meteorology is not one numerical weather model—in each case the model is expected to be superseded while the object of study is not. CLRP is, in the same sense, not CLM. CLM is one evolving computational representation of the landscape; the landscape's dimensions, topology, and dynamics are what the programme seeks to characterise, independent of whether CLM specifically succeeds.

## 2. Landscape discovery vs model validation

CLRP keeps two related but different activities explicitly separate:

| | Landscape discovery | Model validation |
|---|---|---|
| **Asks** | What does the cognitive landscape actually look like? | Does this specific model (e.g. CLM) adequately represent it? |
| **Example questions** | Which dimensions genuinely exist and are independent? What is the topology—attractors, barriers, stable regions? Which trajectories occur naturally? | Does CLM reproduce existing observations? Do its predictions hold up? Does it outperform alternative representations? |
| **Remains meaningful if the model changes** | Yes | No—it is a claim about that model |

**Rule:** every empirical result obtained at or beyond the Topology layer (§3) must explicitly name the computational model, method, or dataset through which it was obtained. A landscape-level claim ("dimensions X and Y appear independent in population P") must be reported separately from a model-level claim ("CLM's structural layer, as currently parameterised, reproduces this independence"). Neither may be stated in a way that implies the other without additional argument. This prevents two recurring errors: evidence about a model silently becoming evidence about the landscape, and landscape-level findings being read as validating one particular model.

## 3. What we are trying to discover

The question classes below correspond to five layers of increasing explanatory depth. They are not mandatory sequential phases—a project may begin at any layer for which it has appropriate data—but each layer presupposes what the shallower layers established.

| Layer | Question class | Example | Suitable evidence |
|-------|----------------|---------|--------------------|
| **Measurement** | Can dimensions be observed reliably at all? | Test-retest and internal consistency of a candidate dimension | Cross-sectional psychometric data |
| **Representation** | Is a landscape a better organising language than categories for the same data? | Dimensional vs. categorical scoring compared on one sample | Cross-sectional, dimensional and categorical scoring side by side |
| **Topology** | **Structure** — Which dimensions co-vary, and at what granularity? What is the landscape's shape—attractors, barriers, stable regions? | Consistent clustering across independent samples | Large-N cross-sectional, ideally multiple independent samples |
| **Dynamics** | **Dynamics** — How do coordinates change under feedback, context, or development? | Feedback and convergence patterns matching or diverging from modelled predictions | Repeated within-person measurement (longitudinal, EMA) — cross-sectional data cannot speak to this layer |
| **Intervention** | **Utility bounds** — Where does dimensional information help self-understanding without harm, and which changes alter trajectory or topology? | A specific intervention producing a measurable, replicable trajectory change | Longitudinal data with a clear intervention point |

**Latent organisation** (are there slow-moving parameters constraining fast measurement?) and **cross-cultural form** (do dimensions mean the same thing across locales?) cut across these layers rather than sitting at one of them; see CLRP-003 and CLRP-008 respectively.

## 4. Methods of discovery (programme level)

CLRP recognises multiple epistemic paths:

1. **Empirical psychometrics** — reliability, validity, invariance (see CLRP-006)
2. **Theoretical synthesis** — literature-informed dimension design (hypothesis status)
3. **Computational modelling** — simulation under explicit assumptions (not observation)
4. **Qualitative and participatory input** — especially for cultural adaptation (CLRP-008)
5. **Open replication** — external groups reproducing protocols

No single path alone establishes programme truth.

## 5. Honest reporting

Discoveries must be reported with:

- **Sample and locale**
- **Instrument and protocol version**
- **CLRP and implementation references**
- **Distinction** between exploratory and confirmatory analyses
- **Limitations** prominently stated
- **Which layer (§3) and which activity (§2)** the finding belongs to, so readers cannot mistake a model-level result for a landscape-level one

## 6. Non-goals

- Discovering "the true number of cognitive types"
- Proving superiority of one culture's cognitive profile
- Replacing clinical assessment with landscape coordinates
- Treating CLM, or any single computational model, as the definitive representation of the landscape (§1.3)

## Revision history

| Version | Date | Status | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-07 | Draft | Initial publication |
| 0.2.0 | 2026-07-15 | Accepted | Added §1.3 (programme vs. model), new §2 (landscape discovery vs. model validation with attribution rule), restructured §3 around five explanatory layers, extended §5 and §6 accordingly. Accepted directly during single-steward phase. |

## References

See [bibliography/](../bibliography/README.md) and [historical-influences/](../historical-influences/README.md).
