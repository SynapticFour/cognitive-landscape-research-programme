# Governance

## Purpose

This document defines how the Cognitive Landscape Research Programme (CLRP) is stewarded, how decisions are made, and how conflicts are resolved. CLRP is intended to outlive any single implementation or maintainer team.

## Programme identity

| Field | Value |
|-------|-------|
| **Name** | Cognitive Landscape Research Programme (CLRP) |
| **Home repository** | `SynapticFour/cognitive-landscape-research-programme` |
| **Steward organisation** | Synaptic Four (initial steward) |
| **Contact** | [contact@synapticfour.com](mailto:contact@synapticfour.com) |

## Roles

### Programme stewards

Stewards maintain repository integrity, triage contributions, convene review, and may merge changes that affect **Accepted** documents.

Initial stewards are designated by Synaptic Four. Future stewards are appointed by existing stewards with public announcement in [CHANGELOG.md](CHANGELOG.md).

Stewards **do not** unilaterally declare scientific truth. They enforce **process**: lifecycle rules, citation standards, ethical boundaries, and separation from implementations.

### Contributors

Anyone may propose changes via pull request, issue, or research note, subject to [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

### Implementers

Teams building CLM, PCMS, ATLAS, or successor systems are not subordinate to stewards, but **Accepted CLRP documents are normative** for use of the "Cognitive Landscape Research Programme" name and for conformance claims (see [CLRP-009](clrp/CLRP-009-implementations-and-conformance.md)).

### External reviewers

Academic collaborators, ethics boards, and funders may comment during **Proposed** periods without merge rights.

## Decision types

| Decision | Authority | Record |
|----------|-----------|--------|
| Typo / clarity in Draft docs | Any steward | PR merge |
| New Draft document | Contributor + steward merge | PR + index update |
| Draft → Proposed | Steward | Status field + comment period announcement |
| Proposed → Accepted | Steward(s) after review period | Version bump + CHANGELOG |
| Deprecate / supersede | Steward | Supersession link + CHANGELOG |
| New CLRP number allocation | Steward | Index + filename |
| Programme roadmap change | Steward | [ROADMAP.md](ROADMAP.md) PR |
| Ethics boundary change | Steward + documented review | CLRP-007 amendment |
| Release tag | Steward | Git tag + Zenodo (when configured) |

## Consensus and dissent

- **Default:** lazy consensus after the review period if no unresolved objections remain.
- **Normative changes** (principles, definitions, non-diagnostic commitment): at least **14 days** in Proposed state; objections must be addressed in writing (in PR or linked issue).
- **Recorded dissent:** If a steward merges despite sustained objection, the dissenting view may be appended to the document's revision history or linked from [open-questions/](open-questions/).

## Relationship to implementations

```
CLRP (normative programme)  ──defines constraints──▶  Implementations
Implementations  ──must not redefine──✕  CLRP principles in code-only docs
Implementations  ──should reference──▶  Accepted CLRP IDs + versions
```

Implementations may **extend** the programme with proposals. Extensions become programme-wide only when accepted into CLRP (new spec, validation report, or vocabulary amendment).

Synaptic Four maintains CLM and PCMS but does not own the programme exclusively. Forks that comply with licensing may implement conformant systems; they must not imply Synaptic Four endorsement without permission.

## Intellectual property

- Documentation: [CC BY 4.0](LICENSE-docs)
- Scripts: [MIT](LICENSE)

Contributors retain copyright; contribution implies license grant per repository licenses.

## Publication and citation

Peer-reviewed publications are **evidence inputs**, not replacements for CLRP documents. Stewards maintain [bibliography/](bibliography/) and link validation reports to the CLRP specs they support.

Technical reports in this repository use the **CLRP-TR** series (distinct from Synaptic Four's genomics SF-TR series in the separate `technical-reports` repository).

## Transition and succession

If stewardship transfers:

1. Announcement in README, GOVERNANCE, and CHANGELOG
2. Update [CITATION.cff](CITATION.cff) maintainer fields
3. Minimum 90-day overlap period when possible
4. GitHub organisation ownership transfer documented

## Amendments to this document

Changes to GOVERNANCE.md require:

- PR with rationale
- 21-day comment period
- Merge by two stewards (or one steward if only one exists, with recorded notice)

---

**Version:** 1.0.0  
**Status:** Accepted  
**Effective:** 2026-07-07
