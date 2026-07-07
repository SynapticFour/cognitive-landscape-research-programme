---
report-id: CLRP-VR-2026-001
title: PCMS Instrument Validation Status
version: 0.1.0
status: Draft
date: 2026-07-07
authors:
  - Synaptic Four
license: CC-BY-4.0
instrument:
  id: pcms
  version: 1.0.0
  repository: https://github.com/SynapticFour/perceptual-cognitive-mapping-system
locales:
  - en
  - de
  - gh-oriented
validation-tier: T0
preregistration:
  url: null
  id: null
clrp-references:
  - id: CLRP-003
    version: 0.1.0
  - id: CLRP-006
    version: 0.1.0
  - id: CLRP-008
    version: 0.1.0
---

> **Status: Draft** — Status report, not empirical study results. Validation tier: **T0** (specification / design hypothesis).

# CLRP-VR-2026-001: PCMS Instrument Validation Status

## Abstract

This report documents the **current validation tier** of the Perceptual & Cognitive Mapping System (PCMS) v1.0 as of 2026-07-07. It states what psychometric and cross-cultural evidence exists, what does not, and the Phase 1 study design required to reach tier T2. No empirical sample results are reported here.

## 1. Instrument under test

| Field | Value |
|-------|-------|
| Instrument | PCMS (Perceptual & Cognitive Mapping System) |
| Version | v1.0 |
| Type | Adaptive web questionnaire |
| Dimensions | Ten routing axes (F–V) |
| Implementation | [perceptual-cognitive-mapping-system](https://github.com/SynapticFour/perceptual-cognitive-mapping-system) |

## 2. Validation tier

**Current tier: T0 → T1**

| Tier | Status |
|------|--------|
| T0 Specification | Design documented; weights literature-informed |
| T1 Engineering verification | CI tests, scoring reproducibility |
| T2 Pilot psychometrics | **Not yet completed** |
| T3 Extended validity | Not started |
| T4 Field readiness | Not started |

Per [CLRP-006](../clrp/CLRP-006-evidence-and-validation.md).

## 3. Current evidence (honest status)

### 3.1 Scoring weights

Dimension scores and routing weights are **derived from literature and expert design**, not from **empirical calibration** on a dedicated PCMS response corpus. Weights are **hypotheses to be tested**, not parameters estimated from this instrument's normative data.

### 3.2 Cultural adaptation

The Ghana question bank was developed with **cultural input** in item wording and framing. It has **not** been validated against a **local normative sample** (Ghana or West Africa) with reported reliability, structure, and score comparability. Ghana deployments should be described as **culturally informed**, not **locally normed** ([CLRP-008](../clrp/CLRP-008-cultural-adaptation.md)).

### 3.3 Reliability

**Internal consistency** (Cronbach's α, McDonald's ω) has **not** been computed from **real PCMS response data** at scale per dimension per locale. Session-level application "confidence" is **not** sample-based reliability.

### 3.4 Predictive validity

**Predictive validity** has **not** been tested in peer-reviewed or pre-registered PCMS studies.

## 4. Phase 1 study design (planned)

Minimum bar to reach **T2** (subject to pre-registration):

1. **Pilot:** N = 150 adults per locale (English, German, Ghana-oriented), convenience sampling, documented consent
2. **Reliability:** α and ω per dimension with confidence intervals
3. **Test–retest:** Two-week interval, N = 40 per locale
4. **Convergent validity:** Pre-registered correlations with BIS/BAS (E-related facets), HSPS (S), and other mapped constructs
5. **Local norms:** Mean and SD per dimension per locale; no cross-locale comparability claims without invariance work

## 5. Claims supported and not supported

| Claim | Supported? |
|-------|------------|
| Software scoring is reproducible (T1) | Yes — engineering tests |
| Dimensions are internally consistent in locale L | **No** — no sample yet |
| Ghana scores comparable to DE/EN scores | **No** |
| Adaptive stopping is empirically calibrated per locale | **No** |
| Suitable for clinical or placement decisions | **Forbidden** ([CLRP-007](../clrp/CLRP-007-non-diagnostic-commitment.md)) |

## 6. Facilitation gaps (programme note)

Responsible classroom or youth use would require artefacts not yet validated:

- Plain-language observation guides (not diagnostic labels)
- Evidence-backed threshold guides (only after norms exist)
- Observer instruments for children under ~12 with separate pilots

## 7. Next update trigger

Revise this report when:

- Phase 1 pilot completes (new CLRP-VR or major version bump)
- A locale bank receives local normative evidence
- Pre-registration is published (link in frontmatter)

## Revision history

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-07-07 | Migrated from PCMS VALIDATION_PROTOCOL.md; programme home |

## References

- [CLRP-006](../clrp/CLRP-006-evidence-and-validation.md)
- PCMS implementation status pointer: [VALIDATION_PROTOCOL.md](https://github.com/SynapticFour/perceptual-cognitive-mapping-system/blob/main/docs/VALIDATION_PROTOCOL.md)
