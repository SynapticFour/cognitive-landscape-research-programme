# Cognitive Landscape Research Programme (CLRP)

**A public, implementation-independent foundation for research on cognitive diversity as a continuous landscape.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Documentation: CC BY 4.0](https://img.shields.io/badge/Documentation-CC%20BY%204.0-lightgrey.svg)](LICENSE-docs)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21389829.svg)](https://doi.org/10.5281/zenodo.21389829)

---

## What this repository is

The Cognitive Landscape Research Programme (CLRP) is the **constitutional home** of a long-term scientific research programme. It defines what the programme seeks to accomplish, the principles it follows, the assumptions it explicitly does not make, and how evidence should be interpreted.

This repository is **not** software documentation. It is not the home of the [Cognitive Landscape Model (CLM)](https://github.com/SynapticFour/cognitive-landscape-model) or the [Perceptual & Cognitive Mapping System (PCMS)](https://github.com/SynapticFour/perceptual-cognitive-mapping-system). Those are *implementations* and *instruments* that **reference** CLRP.

Think of CLRP as sitting between:

- an RFC series (numbered, versioned, citable specifications),
- an open scientific research programme (questions, evidence standards, validation),
- a design constitution (principles, boundaries, non-goals),
- and a living archive of foundational documentation.

## What this repository is not

- **Not a codebase.** Any scripts here exist only to maintain documentation integrity.
- **Not an instrument manual.** Question banks, scoring pipelines, and UI copy belong in PCMS or successor instruments.
- **Not a simulation library.** Dynamics, structural models, and layer APIs belong in CLM or successor libraries.
- **Not a substitute for peer review.** CLRP documents state programme commitments; publications and validation reports provide evidence.

## Start here

| Audience | Start with |
|----------|------------|
| New contributors | [CONTRIBUTING.md](CONTRIBUTING.md) → [CLRP-000](clrp/CLRP-000-foundational-concepts.md) |
| Researchers citing the programme | [CITATION.cff](CITATION.cff) → [docs/citation/citation-guide.md](docs/citation/citation-guide.md) |
| Implementers (CLM, PCMS, others) | [CLRP-009](clrp/CLRP-009-implementations-and-conformance.md) → [docs/ecosystem/](docs/ecosystem/) |
| Institutional reviewers | [CLRP-007](clrp/CLRP-007-non-diagnostic-commitment.md) → [validation/](validation/) |
| Programme stewards | [GOVERNANCE.md](GOVERNANCE.md) → [ROADMAP.md](ROADMAP.md) |

## Document series

### CLRP specifications (`clrp/`)

Numbered foundational documents. Each has a lifecycle (Draft → Proposed → Accepted → Deprecated/Superseded). See [docs/versioning/versioning-policy.md](docs/versioning/versioning-policy.md).

| ID | Title | Status |
|----|-------|--------|
| [CLRP-000](clrp/CLRP-000-foundational-concepts.md) | Foundational Concepts | Draft |
| [CLRP-001](clrp/CLRP-001-discovering-the-cognitive-landscape.md) | Discovering the Cognitive Landscape | Draft |
| [CLRP-002](clrp/CLRP-002-vocabulary.md) | Vocabulary | Draft |
| [CLRP-003](clrp/CLRP-003-measurement-principles.md) | Measurement Principles | Draft |
| [CLRP-004](clrp/CLRP-004-epistemic-commitments.md) | Epistemic Commitments | Draft |
| [CLRP-005](clrp/CLRP-005-layer-separation.md) | Layer Separation | Draft |
| [CLRP-006](clrp/CLRP-006-evidence-and-validation.md) | Evidence and Validation | Draft |
| [CLRP-007](clrp/CLRP-007-non-diagnostic-commitment.md) | Non-Diagnostic Commitment | Draft |
| [CLRP-008](clrp/CLRP-008-cultural-adaptation.md) | Cultural Adaptation | Draft |
| [CLRP-009](clrp/CLRP-009-implementations-and-conformance.md) | Implementations and Conformance | Draft |

Full index: [clrp/index.md](clrp/index.md)

### Other collections

| Collection | Purpose |
|------------|---------|
| [technical-reports/](technical-reports/) | Long-form methods, analyses, and design studies (CLRP-TR series) |
| [research-notes/](research-notes/) | Short, dated exploratory notes (CLRP-RN series) |
| [validation/](validation/) | Validation protocols, study reports, and evidence summaries |
| [proposals/](proposals/) | Proposed extensions awaiting acceptance |
| [open-questions/](open-questions/) | Explicitly unresolved programme questions |
| [bibliography/](bibliography/) | Shared references |
| [historical-influences/](historical-influences/) | Intellectual lineage and acknowledged predecessors |

## Core commitments (summary)

CLRP rests on commitments that apply to **all** programme work, including future implementations:

1. **Continuous dimensional modelling** — cognition as coordinates in a landscape, not categorical labels.
2. **Measurement ≠ interpretation** — coordinates, dynamics, and narrative frames are strictly separated.
3. **Non-diagnostic, non-gatekeeping** — no clinical claims; no access control based on scores.
4. **Honest evidence stance** — distinguish design hypotheses from empirically validated claims.
5. **Reproducibility** — versioned protocols, pinned references, and explicit provenance.
6. **Cultural humility** — adaptation is not translation; cross-locale claims require invariance evidence.
7. **Implementation independence** — CLRP defines *what* and *why*; implementations define *how*.

Details: [CLRP-000](clrp/CLRP-000-foundational-concepts.md) through [CLRP-009](clrp/CLRP-009-implementations-and-conformance.md).

## Ecosystem

```
                    ┌─────────────────────────────┐
                    │  CLRP (this repository)     │
                    │  Principles · Evidence ·    │
                    │  Vocabulary · Validation    │
                    └──────────────┬──────────────┘
                                   │ references
           ┌───────────────────────┼───────────────────────┐
           ▼                       ▼                       ▼
    ┌─────────────┐         ┌─────────────┐         ┌─────────────┐
    │    PCMS     │         │     CLM     │         │  Future     │
    │ instrument  │         │  modelling  │         │ systems     │
    └─────────────┘         └─────────────┘         └─────────────┘
```

See [docs/ecosystem/](docs/ecosystem/) and [docs/architecture/repository-architecture.md](docs/architecture/repository-architecture.md).

## Licensing

| Content type | License | File |
|--------------|---------|------|
| Documentation (CLRP specs, reports, notes) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | [LICENSE-docs](LICENSE-docs) |
| Scripts and tooling | [MIT](https://opensource.org/licenses/MIT) | [LICENSE](LICENSE) |

Rationale: [docs/README.md](docs/README.md#licensing-rationale)

## Citation

To cite the programme as a whole, use [CITATION.cff](CITATION.cff). To cite a specific document, use its document ID, version, and release DOI when available. See [docs/citation/citation-guide.md](docs/citation/citation-guide.md).

**Latest release:** [clrp-v2026.2](https://github.com/SynapticFour/cognitive-landscape-research-programme/releases/tag/clrp-v2026.2) · **DOI:** [10.5281/zenodo.21389829](https://doi.org/10.5281/zenodo.21389829) · Concept DOI: [10.5281/zenodo.21236099](https://doi.org/10.5281/zenodo.21236099)

## Governance and contact

- **Governance:** [GOVERNANCE.md](GOVERNANCE.md)
- **Roadmap:** [ROADMAP.md](ROADMAP.md)
- **Changelog:** [CHANGELOG.md](CHANGELOG.md)
- **Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Code of conduct:** [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- **Security:** [SECURITY.md](SECURITY.md)
- **Contact:** [contact@synapticfour.com](mailto:contact@synapticfour.com)

## Status

**Programme maturity:** Foundational (2026). CLRP documents are in **Draft** status until accepted through the governance process. Implementations may exist ahead of validation; CLRP requires that gap to be stated explicitly.

---

*Synaptic Four · Cognitive Landscape Research Programme*
