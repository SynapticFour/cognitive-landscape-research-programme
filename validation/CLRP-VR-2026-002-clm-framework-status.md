---
report-id: CLRP-VR-2026-002
title: CLM Framework Validation Status
version: 0.1.0
status: Draft
date: 2026-07-07
authors:
  - Synaptic Four
license: CC-BY-4.0
instrument:
  id: clm
  version: 0.2.0
  repository: https://github.com/SynapticFour/cognitive-landscape-model
locales: []
validation-tier: T1
preregistration:
  url: null
  id: null
clrp-references:
  - id: CLRP-005
    version: 0.1.0
  - id: CLRP-006
    version: 0.1.0
  - id: CLRP-009
    version: 0.1.0
---

> **Status: Draft** — Status report for a **modelling framework**, not a psychometric instrument. Validation tier: **T1** (engineering verification).

# CLRP-VR-2026-002: CLM Framework Validation Status

## Abstract

This report documents the **current validation tier** of the Cognitive Landscape Model (CLM) v0.2 as of 2026-07-07. CLM is a layered TypeScript library for representing and simulating cognitive coordinates. Package tests demonstrate code consistency; **external psychometric validity** is the responsibility of integrator instruments (e.g. PCMS).

## 1. Framework under test

| Field | Value |
|-------|-------|
| System | CLM (Cognitive Landscape Model) |
| Version | v0.2 |
| Type | Research modelling library |
| Layers | landscape, dynamics, structural, trajectory-explanation, interpretation |
| Implementation | [cognitive-landscape-model](https://github.com/SynapticFour/cognitive-landscape-model) |

## 2. Validation tier

**Current tier: T1**

| Tier | Status |
|------|--------|
| T0 Specification | Layer architecture documented |
| T1 Engineering verification | Unit/integration tests, import boundaries |
| T2+ Psychometrics | **Applies to integrator instruments**, not CLM alone |

## 3. Current evidence (honest status)

### 3.1 Framework vs instrument

CLM provides typed layers, simulation mechanics, and separation of measurement from interpretation. It does **not** constitute a validated psychometric instrument. Tests demonstrate **internal consistency of code**, not **external validity** in human populations.

### 3.2 Structural and dynamics parameters

Latent priors, influence weights, and dynamics roles in presets are **design- and literature-informed hypotheses**, not parameters from a dedicated CLM normative corpus.

### 3.3 PCMS integration

When CLM consumes PCMS dimensions via `@clm/landscape`, **PCMS validation status applies to assessment input**. See [CLRP-VR-2026-001](./CLRP-VR-2026-001-pcms-instrument-status.md).

### 3.4 Simulation outputs

Simulated trajectories are **model outputs** under stated assumptions. They must not be presented as observed longitudinal data without explicit labelling ([CLRP-004](../clrp/CLRP-004-epistemic-commitments.md) L4).

## 4. Research roadmap (framework)

1. Define instrument boundary (landscape only vs full pipeline)
2. Document human data samples (N, locale, consent) entering any published pipeline
3. Report sample-based reliability for **observed dimensions** of the integrator's instrument
4. Report simulation sensitivity to priors, seeds, and graph specification when simulations support claims
5. Audit interpretation firewall in deployment (CLM boundary tests necessary, not sufficient)

## 5. Claims supported and not supported

| Claim | Supported? |
|-------|------------|
| Layer import boundaries enforced (T1) | Yes — automated tests |
| Simulated trajectories predict real-world outcomes | **No** — without longitudinal studies |
| Structural calibration identifies clinical traits | **No** |
| Interpretation plugins explain causes of coordinates | **No** — explicitly non-causal |
| Presets are locally normed | **No** — without integrator norm studies |

## 6. Integrator responsibilities (out of CLM scope)

- Privacy policy, consent, retention
- IRB / ethics approval
- Locale-appropriate non-stigmatising copy
- Institutional decision rules — **discouraged** ([CLRP-007](../clrp/CLRP-007-non-diagnostic-commitment.md))

## Revision history

| Version | Date | Summary |
|---------|------|---------|
| 0.1.0 | 2026-07-07 | Migrated from CLM VALIDATION_PROTOCOL.md; programme home |

## References

- [CLRP-005](../clrp/CLRP-005-layer-separation.md)
- [CLRP-VR-2026-001](./CLRP-VR-2026-001-pcms-instrument-status.md)
- CLM implementation pointer: [VALIDATION_PROTOCOL.md](https://github.com/SynapticFour/cognitive-landscape-model/blob/main/docs/VALIDATION_PROTOCOL.md)
