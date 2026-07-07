---
clrp-id: CLRP-002
title: Vocabulary
version: 0.1.0
status: Draft
date: 2026-07-07
authors:
  - Synaptic Four
license: CC-BY-4.0
---

> **Status: Draft** — This document is work in progress and does not yet represent an accepted programme commitment.

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

## References

Internal: [CLRP-003](CLRP-003-measurement-principles.md), [CLRP-005](CLRP-005-layer-separation.md)
