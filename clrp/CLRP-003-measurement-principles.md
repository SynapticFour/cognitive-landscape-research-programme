---
clrp-id: CLRP-003
title: Measurement Principles
version: 0.1.0
status: Draft
date: 2026-07-07
authors:
  - Synaptic Four
license: CC-BY-4.0
---

> **Status: Draft** — This document is work in progress and does not yet represent an accepted programme commitment.

# CLRP-003: Measurement Principles

## Abstract

Normative principles for how coordinates are produced, reported, and revised within CLRP. This document is independent of any specific item bank, scoring function, or software package.

## 1. Principles

### M1 — Continuity

Dimensions are **continuous** scales with explicitly defined bounds. Categorical bucketing for user display must be labelled as simplification, not ontology.

### M2 — Uncertainty

Point estimates must be accompanied by **uncertainty** where feasible (standard errors, credible intervals, engine confidence separate from reliability).

### M3 — Provenance

Every coordinate vector must be reproducible from:

- Instrument ID and version
- Protocol / bank ID and version
- Locale and administration context
- Analysis pipeline version
- CLRP release reference

### M4 — Design vs calibrated parameters

Parameters derived from literature or expert design are **hypotheses** until CLRP-VR reports empirical estimation. Documents and UIs must not imply calibration that has not occurred.

### M5 — Adaptive transparency

Adaptive instruments must document:

- Stopping rules
- Item exposure dependencies
- Implications for score comparability across administrations

### M6 — No feedback from interpretation to measurement

Narrative frames, user preferences, or worldview selections must not alter scoring functions (see CLRP-005).

### M7 — Locale integrity

Scores are interpreted relative to **stated locale norms** when available. Cross-locale comparison requires invariance evidence (CLRP-008, CLRP-006).

## 2. Measurement outputs (minimum)

A conforming measurement export includes:

| Field | Description |
|-------|-------------|
| `dimensions` | ID → value map |
| `uncertainty` | Per-dimension if available |
| `instrumentId` | Instrument identifier |
| `protocolVersion` | Protocol semver |
| `locale` | Locale descriptor |
| `timestamp` | ISO 8601 administration time |
| `clrpReference` | CLRP release or document IDs |

Exact serialisation belongs in CLRP-009 and implementation specs—not here.

## 3. What measurement must not output

- Diagnostic categories (DSM, ICD, etc.) as primary results
- Rank ordering of human worth
- Single scalar "ability" without dimensional decomposition
- Clinical treatment recommendations

## 4. Revision of dimensions

Dimension sets may be added, split, or retired when:

1. Proposal accepted (CLRP-P or CLRP amendment)
2. Validation plan published
3. Migration path documented for historical data

## 5. Non-goals

- Defining item content or translation strings
- Mandating a single adaptive algorithm
- Establishing clinical cut scores

## Revision history

| Version | Date | Status | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-07 | Draft | Initial publication |

## References

- [CLRP-002](CLRP-002-vocabulary.md)
- [CLRP-006](CLRP-006-evidence-and-validation.md)
- [CLRP-005](CLRP-005-layer-separation.md)
