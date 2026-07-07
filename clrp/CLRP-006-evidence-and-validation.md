---
clrp-id: CLRP-006
title: Evidence and Validation
version: 0.1.0
status: Draft
date: 2026-07-07
authors:
  - Synaptic Four
license: CC-BY-4.0
---

> **Status: Draft** — This document is work in progress and does not yet represent an accepted programme commitment.

# CLRP-006: Evidence and Validation

## Abstract

Standards for what counts as **evidence** within CLRP and how validation studies are designed, reported, and linked to programme claims. Software tests alone are insufficient for psychometric validity.

## 1. Validation hierarchy

| Tier | Name | Minimum bar |
|------|------|-------------|
| **T0** | Specification | Documented design hypothesis |
| **T1** | Engineering verification | Correct implementation of spec |
| **T2** | Pilot psychometrics | N≥150/locale, α/ω, basic structure |
| **T3** | Extended validity | Test–retest, convergent, invariance pilots |
| **T4** | Field readiness | Independent replication, pre-registered confirmatory |

Programme-facing instruments should state current tier **honestly**.

## 2. Required reporting elements (CLRP-VR)

Every validation report must include:

1. **Pre-registration or justification** for exploratory work
2. **Sample** size, demographics, locale, recruitment
3. **Instrument versions** and CLRP references
4. **Analysis plan** and deviations
5. **Results** with effect sizes and confidence intervals
6. **Limitations** including generalisability
7. **Data availability** statement (when ethical)

Use [validation report template](../templates/validation-report-template.md).

## 3. Claims matrix

| Claim | Minimum evidence |
|-------|------------------|
| "Internally consistent in locale L" | T2, per-dimension α or ω |
| "Stable over 2 weeks in locale L" | T3 test–retest |
| "Correlates with construct C" | T3, pre-specified hypothesis |
| "Comparable across locales" | T4 invariance study |
| "Suitable for classroom placement" | **Not supported by CLRP** |
| "Identifies need for clinical support" | **Forbidden claim** |

## 4. Relationship to software testing

| Software test | Validates |
|---------------|-----------|
| Golden vector match | Deterministic scoring reproducibility (T1) |
| Import boundary | Layer separation architecture (T1) |
| Property-based tests | Internal logic consistency (T1) |

None substitute for T2+ with human subjects.

## 5. Negative results

Failed validation is **publishable** in `validation/` or `research-notes/`. Suppressing negative results violates CLRP-004.

## 6. Programme review cycle

Stewards annually review:

- Which CLRP documents cite evidence no longer supported
- Whether implementations overstate validation tier

## 7. Non-goals

- Setting journal-specific formatting rules
- Mandating a single statistical software environment

## Revision history

| Version | Date | Status | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-07 | Draft | Initial publication |

## References

- American Educational Research Association et al. (2014). *Standards for Educational and Psychological Testing*.
- [CLRP-004](CLRP-004-epistemic-commitments.md)
