---
clrp-id: CLRP-004
title: Epistemic Commitments
version: 0.2.0
status: Accepted
date: 2026-07-15
authors:
  - Synaptic Four
license: CC-BY-4.0
---

> **Status: Accepted** — This document represents an accepted programme commitment as of the stated version. Accepted directly during the initial single-steward phase of the programme (no separate Proposed comment period); the full Draft → Proposed → Accepted review cycle will apply once the steward group grows (see GOVERNANCE.md).

# CLRP-004: Epistemic Commitments

## Abstract

CLRP commits to explicit standards for **what kinds of knowledge** the programme pursues and **how claims are graded**. This document prevents silent escalation from metaphor to fact, or from simulation to observation.

## 1. Epistemic levels

All programme statements should be readable as one of:

| Level | Label | Example |
|-------|-------|---------|
| **L0** | Commitment | "Measurement and interpretation are separated." |
| **L1** | Definition | "A dimension is a continuous axis…" (CLRP-002) |
| **L2** | Design hypothesis | "Routing weights derived from literature X." |
| **L3** | Empirical finding | "α = 0.78 for dimension S in locale L (N=150)." |
| **L4** | Model output | "Simulated trajectory under graph G." |
| **L5** | Speculation / open question | "Micro-traits may improve imputation…" |

**Rule:** Higher-stakes claims require higher levels. L4 must never be presented as L3 without explicit labelling.

## 2. Knowledge acquisition

CLRP acquires knowledge through:

1. **Pre-registered studies** (preferred for confirmatory claims)
2. **Open datasets** (when ethics permit)
3. **Reproducible analysis** linked to CLRP-VR or CLRP-TR
4. **Adversarial review** (issues, recorded dissent)
5. **Replication by independent groups** (encouraged, not required for draft specs)

## 3. Falsification and revision

- Dimensions and models are **provisional**.
- Negative results belong in validation reports and research notes.
- Accepted documents are revised when evidence warrants—not to protect implementations.

## 4. Interpretation of evidence

| Evidence type | Supports |
|---------------|----------|
| Internal consistency | Reliability of scale scores in sample |
| Test–retest | Temporal stability under stated interval |
| Convergent validity | Theoretical overlap with external measures |
| Measurement invariance | Cross-group/locale comparability of parameters |
| Simulation fit | Plausibility of dynamics model—not truth of ontology |

No single study establishes "truth" of the landscape metaphor.

## 5. Explicit non-assumptions

CLRP does **not** assume:

- Cognition decomposes cleanly into independent dimensions
- Self-report captures all relevant variation
- Western-derived constructs universal without adaptation
- More dimensions are always better
- Simulation parameters identify real-world causal mechanisms
- Cognition can be completely reduced to mathematics, or that a coordinate representation exhausts what a person is
- Every meaningful aspect of human experience is measurable, or that what is not currently measurable is thereby unreal
- The current landscape representation is the only possible one—it is one workable choice, open to revision or replacement
- Future computational models must resemble any current implementation (e.g. CLM) in their specific mechanics
- Empirical success of a model validates, confirms, or lends evidential support to any particular metaphysical or worldview position (see CLRP-005 §5 on interpretation)
- A satisfying interpretation of a pattern is grounds to relax empirical standards for it
- Empirical findings can resolve metaphysical questions, or that the coexistence of measurement and interpretation layers implies either can settle questions belonging to the other
- Any implementation, representation, or measurement system currently in use should be regarded as definitive rather than provisional

## 6. Intellectual honesty requirements

Authors must:

- Disclose funding and conflicts of interest
- Separate exploratory from confirmatory analyses in reports
- Cite CLRP document versions used
- Acknowledge steward vs author roles

## Revision history

| Version | Date | Status | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-07 | Draft | Initial publication |
| 0.2.0 | 2026-07-15 | Accepted | Extended §5 explicit non-assumptions with eight additional items covering representational pluralism, worldview/validation independence, and provisionality of current implementations. Accepted directly during single-steward phase. |

## References

- [CLRP-006](CLRP-006-evidence-and-validation.md)
- Popper (1959). *The Logic of Scientific Discovery*.
