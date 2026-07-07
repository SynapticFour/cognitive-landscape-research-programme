# CLRP and the Perceptual & Cognitive Mapping System (PCMS)

## Summary

| | CLRP | PCMS |
|---|------|------|
| **What it is** | Research programme constitution | Production web assessment instrument |
| **Repository** | `cognitive-landscape-research-programme` | `perceptual-cognitive-mapping-system` |
| **Answers** | What may an instrument claim? How is validity evidenced? | How does the adaptive questionnaire produce coordinates? |
| **Live deployment** | — | https://map.synapticfour.com |

**PCMS is one instrument within the programme. CLRP does not document PCMS UI, question banks, or scoring code.**

## Dependency direction

```
CLRP (measurement principles, ethics, validation framework)
         │
         │ constrains
         ▼
PCMS (adaptive engine, item banks, results UI)
         │
         │ optional export
         ▼
CLM (modelling, simulation)
```

PCMS never defines programme principles in isolation. If PCMS behaviour embodies a new principle, that principle is proposed to CLRP first.

## What belongs in CLRP vs PCMS

| Topic | CLRP | PCMS |
|-------|------|------|
| Non-diagnostic commitment | CLRP-007 | UI copy, consent flow |
| Measurement vs interpretation | CLRP-005 | Pipeline architecture ADRs |
| What "validation" means | CLRP-006 | VALIDATION_PROTOCOL.md (implementation status) |
| F–V dimension definitions | CLRP-002 (programme terms) | Item routing, scoring weights |
| Adaptive stopping rules | CLRP-003 (requirements) | Engine code |
| Ghana cultural adaptation method | CLRP-008 | Question bank locale files |
| Session export format | CLRP-009 | Export implementation |

PCMS `docs/VALIDATION_PROTOCOL.md` should evolve into **CLRP-VR** reports plus a short PCMS-specific status pointer.

## Validation relationship

```
CLRP-006  ──defines──▶  evidence standards
CLRP-VR   ──reports──▶  study results
PCMS      ──implements──▶  instrument under test
```

Honest status framing (required by CLRP-006):

- PCMS weights are design hypotheses until CLRP-VR reports empirical calibration
- Session confidence ≠ reliability
- Locale banks may be culturally informed without being locally normed

## Ethics and deployment

CLRP-007 is authoritative for programme ethics. PCMS must:

- Reference CLRP-007 in ethics documentation
- Implement consent, privacy, and non-gatekeeping in deployment-specific artifacts
- Not claim clinical utility beyond what validation reports support

Institutional reviewers should read CLRP-007 and relevant CLRP-VR documents before PCMS technical specs.

## ATLAS and extensions

High-dimensional extensions (e.g. ATLAS micro-trait architecture) are **separate instruments** that may share infrastructure. Each requires:

- CLRP proposal for programme extension (if new principles)
- Independent validation track (CLRP-VR)
- Clear naming so users do not conflate with PCMS F–V profiles

## Website and public communication

The Synaptic Four website describes PCMS as open research (see [relationship-to-synapticfour.md](relationship-to-synapticfour.md)). Public pages should link to CLRP for programme principles, not only to PCMS.

---

See also: [relationship-to-clm.md](relationship-to-clm.md) · [relationship-to-synapticfour.md](relationship-to-synapticfour.md)
