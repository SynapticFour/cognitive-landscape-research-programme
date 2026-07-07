# Contributing to the Cognitive Landscape Research Programme

Thank you for considering a contribution. CLRP is designed for decades of collaborative scientific work. We prioritise **rigour, transparency, and long-term maintainability** over speed.

## Before you contribute

1. Read [CLRP-000](clrp/CLRP-000-foundational-concepts.md) and [CLRP-004](clrp/CLRP-004-epistemic-commitments.md).
2. Understand that CLRP is **implementation-independent**. Do not add instrument-specific scoring rules, API documentation, or UI copy here.
3. Review [GOVERNANCE.md](GOVERNANCE.md) for decision authority and document lifecycle.
4. Check [open-questions/](open-questions/) and existing CLRP documents to avoid duplicating settled or in-progress work.

## Ways to contribute

| Contribution type | Where | Process |
|-------------------|-------|---------|
| Foundational specification | `clrp/` | Proposal PR → review → acceptance |
| Technical report | `technical-reports/` | Use [template](templates/technical-report-template.md) |
| Research note | `research-notes/` | Use [template](templates/research-note-template.md) |
| Validation evidence | `validation/` | Use [template](templates/validation-report-template.md) |
| Programme extension proposal | `proposals/` | Use [template](templates/proposal-template.md) |
| Bibliography entry | `bibliography/references.bib` | PR with citation context |
| Open question | `open-questions/` | Issue or PR with rationale |
| Typo / clarity fix | Any | Small PR; no governance vote required |

## Document lifecycle

All CLRP specifications follow the lifecycle defined in [docs/versioning/versioning-policy.md](docs/versioning/versioning-policy.md):

```
Draft → Proposed → Accepted → (Deprecated | Superseded)
```

- **Draft:** Work in progress; may change without notice.
- **Proposed:** Ready for community review; comment period open.
- **Accepted:** Stable programme commitment; changes require version bump.
- **Deprecated:** Still readable; no longer recommended.
- **Superseded:** Replaced by a newer document (link required).

Do not mark a document **Accepted** in your own PR unless you are a programme steward with explicit authority (see [GOVERNANCE.md](GOVERNANCE.md)).

## Pull request guidelines

### All contributions

- Use clear, complete sentences. Avoid marketing language.
- State **what is claimed** and **what is not claimed**.
- Cite sources. Add bibliography entries where appropriate.
- Include YAML frontmatter (see templates).
- Sign off that you agree to license terms: documentation under [CC BY 4.0](LICENSE-docs); scripts under [MIT](LICENSE).

### CLRP specification changes

- One logical change per PR where possible.
- If changing an **Accepted** document, increment the document version and add a [CHANGELOG](CHANGELOG.md) entry.
- Cross-reference affected documents.
- For normative changes (principles, definitions), allow at least **14 days** review before acceptance.

### New CLRP numbers

- Request the next available ID in your PR description or open an issue first.
- Numbers are **never reused**.
- File naming: `CLRP-NNN-short-title.md` (three-digit zero-padded).

## Writing standards

### Tone

- Conservative and precise.
- Prefer "the programme holds that…" over "we believe…" for normative statements.
- Distinguish **programme commitments** from **research hypotheses** from **implementation details**.

### Structure

- Begin with a one-paragraph **abstract**.
- Include **Scope**, **Normative statements** (where applicable), **Non-goals**, and **Open questions**.
- End with **Revision history** and **References**.

### Terminology

- Use terms defined in [CLRP-002](clrp/CLRP-002-vocabulary.md).
- If introducing a new term, propose a vocabulary amendment (PR to CLRP-002 or a proposal document).
- Do not overload existing terms with implementation-specific meanings.

## What we will not accept

- Diagnostic or gatekeeping language without explicit rejection in context.
- Claims of validated psychometric properties without linked validation reports.
- Implementation documentation that belongs in CLM, PCMS, or other code repositories.
- Participant data, identifiable records, or raw survey responses.
- Changes that conflate measurement with interpretation layers (see [CLRP-005](clrp/CLRP-005-layer-separation.md)).

## Review process

1. **Triage** — Maintainers check scope, licensing, and safety within 7 days.
2. **Technical review** — At least one steward reviews substance and cross-references.
3. **Comment period** — Proposed CLRP specs: minimum 14 days for Accepted status.
4. **Merge** — Draft and Proposed documents merge on steward approval; Accepted status may require recorded consensus.

## Code of conduct

All participants must follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Report concerns to [contact@synapticfour.com](mailto:contact@synapticfour.com).

## Questions

Open a [GitHub Discussion](https://github.com/SynapticFour/cognitive-landscape-research-programme/discussions) (when enabled) or email [contact@synapticfour.com](mailto:contact@synapticfour.com).

---

*This document is itself a programme artifact. Propose amendments via PR.*
