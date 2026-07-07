---
clrp-id: CLRP-009
title: Implementations and Conformance
version: 0.1.0
status: Draft
date: 2026-07-07
authors:
  - Synaptic Four
license: CC-BY-4.0
---

> **Status: Draft** — This document is work in progress and does not yet represent an accepted programme commitment.

# CLRP-009: Implementations and Conformance

## Abstract

How computational systems relate to CLRP: reference requirements, conformance levels, and extension process. **CLRP is not documentation for any implementation.**

## 1. Implementation categories

| Category | Role | Examples |
|----------|------|----------|
| **Instrument** | Produces coordinates | Adaptive questionnaires, observation protocols |
| **Library** | Models coordinates | Simulation, calibration, explanation |
| **Pipeline** | Connects instrument → library | Export adapters, ETL |
| **Platform** | Hosts deployments | Web apps, field tools |

One repository may span categories; conformance is declared per category.

## 2. Reference requirements

All implementations **should** include in README and export metadata:

```yaml
programme: CLRP
clrpRelease: clrp-v2026.1   # or commit SHA
clrpDocuments:
  - id: CLRP-003
    version: 0.1.0
  - id: CLRP-007
    version: 0.1.0
conformance: partial | full
conformanceScope: instrument-measurement | landscape-layer | ...
```

## 3. Conformance levels

### Partial conformance

Implementation satisfies a **declared subset** of Accepted CLRP documents (listed explicitly).

### Full conformance (instrument)

Requires, at minimum:

- CLRP-003, CLRP-005, CLRP-007 at Accepted versions
- Published CLRP-VR at T2+ for stated locales **or** honest T0/T1 disclosure
- No layer violations (tested)

### Full conformance (library)

Requires, at minimum:

- CLRP-005 at Accepted version
- Documented mapping to CLRP-002 terms
- Simulation labelling (CLRP-004 L4)

**Stewards do not certify.** Conformance is a **public declaration** subject to community scrutiny.

## 4. Extension process

1. Author submits [proposal](../proposals/README.md)
2. If accepted → CLRP amendment or new CLRP-NNN
3. Validation plan if empirical claims change
4. Implementations update conformance declarations

## 5. Anti-patterns

| Anti-pattern | Why forbidden |
|--------------|---------------|
| Defining programme principles only in code | Breaks implementation independence |
| CLRP doc describing API signatures | Belongs in implementation repo |
| Implying Synaptic Four endorsement of forks | Branding policy |
| "CLRP certified person" | Programme certifies nothing about individuals |

## 6. Known implementations (informative)

| System | Repository | Relationship |
|--------|------------|--------------|
| PCMS | `perceptual-cognitive-mapping-system` | Instrument |
| CLM | `cognitive-landscape-model` | Library |

See [docs/ecosystem/](../docs/ecosystem/).

## 7. Non-goals

- Compliance certification industry
- Trademark enforcement details (legal counsel outside CLRP)

## Revision history

| Version | Date | Status | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-07 | Draft | Initial publication |

## References

- [docs/ecosystem/relationship-to-clm.md](../docs/ecosystem/relationship-to-clm.md)
- [docs/ecosystem/relationship-to-pcms.md](../docs/ecosystem/relationship-to-pcms.md)
- [docs/citation/citation-guide.md](../docs/citation/citation-guide.md)
