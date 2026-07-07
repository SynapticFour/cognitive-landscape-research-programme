# CLRP and the Cognitive Landscape Model (CLM)

## Summary

| | CLRP | CLM |
|---|------|-----|
| **What it is** | Research programme constitution | Research-grade TypeScript modelling library |
| **Repository** | `cognitive-landscape-research-programme` | `cognitive-landscape-model` |
| **Answers** | What should we commit to? How is evidence judged? | How do we represent, simulate, and explain coordinates? |
| **Authority** | Normative for programme name and principles | Descriptive for APIs and packages |

**CLM implements aspects of CLRP. CLRP does not document CLM.**

## Dependency direction

```
CLRP (principles, vocabulary, validation standards)
         │
         │ references / constrains
         ▼
CLM (@clm/landscape, @clm/dynamics, @clm/structural, …)
         │
         │ optional export
         ▼
Instruments (e.g. PCMS session data)
```

CLM must declare in its README and provenance metadata:

- Which `clrp-v*` release it targets
- Which CLRP documents govern its semantics
- Known gaps between implementation and Accepted CLRP text

## What belongs in CLRP vs CLM

| Topic | CLRP | CLM |
|-------|------|-----|
| Layer separation principle | CLRP-005 | Import boundary tests |
| Meaning of "measurement" | CLRP-003 | `@clm/landscape` types |
| Simulation ethics | CLRP-007 | Package README, integrator docs |
| Feedback graph API | — | `@clm/dynamics` documentation |
| PCMS bridge functions | CLRP-009 (conformance) | `@clm/landscape` code |
| Golden test vectors | CLRP-TR or validation | `tests/integration/` |

When CLM behaviour changes programme semantics (e.g. a dimension definition), the change **starts** as a CLRP proposal, not as a merged PR in CLM alone.

## Conformance

CLM may claim **CLRP conformance** only when:

1. It references Accepted CLRP documents by ID and version
2. It passes published conformance tests (CLRP-TR or CLM test suite documented in CLRP-009)
3. It does not violate CLRP-007 (non-diagnostic) in defaults or examples

Conformance is **partial** until explicitly listed. Example: "CLM v0.3 conforms to CLRP-005 v1.0.0 and CLRP-009 v0.2.0 (landscape layer only)."

## Migration path

Existing CLM documentation (`docs/ethics.md`, `docs/ARCHITECTURE.md`, etc.) should:

1. **Reference** CLRP for programme-level statements
2. **Retain** implementation-specific detail locally
3. **Remove** duplicated normative text over time (point to CLRP instead)

Suggested CLM README addition:

```markdown
## Programme foundation

CLM is an implementation within the [Cognitive Landscape Research Programme](https://github.com/SynapticFour/cognitive-landscape-research-programme).
Normative principles: CLRP-005, CLRP-007. This repository documents APIs and packages.
```

## Publications

A future CLM methods paper cites CLRP for definitions and CLM-TR/CLRP-TR for reproducible methods. CLRP does not substitute for the paper.

---

See also: [relationship-to-pcms.md](relationship-to-pcms.md) · [relationship-to-synapticfour.md](relationship-to-synapticfour.md)
