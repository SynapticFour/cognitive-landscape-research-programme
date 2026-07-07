# Versioning policy

This document defines how CLRP documents evolve, how releases are tagged, and how draft status is communicated.

## Principles

1. **Immutability of history** — Accepted document versions remain readable; changes create new versions.
2. **Explicit status** — No reader should mistake a draft for an accepted programme commitment.
3. **Semantic clarity** — Version numbers encode meaning.
4. **Citable snapshots** — Releases produce DOI-backed archives when Zenodo integration is configured.

## Document lifecycle

```
┌────────┐    review     ┌──────────┐   consensus   ┌──────────┐
│ Draft  │ ────────────▶ │ Proposed │ ────────────▶ │ Accepted │
└────────┘               └──────────┘               └────┬─────┘
                                                         │
                        ┌────────────────────────────────┼────────────────┐
                        ▼                                ▼                ▼
                 ┌────────────┐                  ┌────────────┐    ┌────────────┐
                 │ Deprecated │                  │ Superseded │    │  (active)  │
                 └────────────┘                  └────────────┘    └────────────┘
```

| Status | Meaning | Banner colour (rendered docs) |
|--------|---------|-------------------------------|
| **Draft** | Work in progress; may change without version bump | Grey |
| **Proposed** | Ready for review; comment period open | Amber |
| **Accepted** | Normative programme content | Green |
| **Deprecated** | Retained for history; not recommended | Red |
| **Superseded** | Replaced by another document (link required) | Red |

### Transitions

| From | To | Requirements |
|------|-----|--------------|
| — | Draft | PR merge; index updated |
| Draft | Proposed | Steward approval; complete sections; no TBD in normative statements |
| Proposed | Accepted | ≥14 days in Proposed; objections addressed; version set to 1.0.0 |
| Accepted | Accepted (new version) | Semver bump; CHANGELOG + revision history |
| Accepted | Deprecated | Rationale; no replacement required |
| Accepted | Superseded | Link to successor CLRP ID |

## Document version numbers (semver)

Each CLRP specification carries an independent version `MAJOR.MINOR.PATCH`:

| Bump | When |
|------|------|
| **MAJOR** | Breaking change to normative meaning, removed commitments, redefined core terms |
| **MINOR** | Additive normative content, new sections, clarified non-goals |
| **PATCH** | Editorial fixes, typos, non-normative clarifications |

**Accepted** documents must update version on every merge that changes normative text.

## CLRP identifier rules

- Format: `CLRP-NNN` where NNN is zero-padded decimal (000–999).
- Numbers are **never reused**.
- Filename: `CLRP-NNN-short-kebab-title.md`
- Reserved: `CLRP-000` – `CLRP-099` for core programme specs; `CLRP-100+` for extensions.

## Series-specific numbering

| Series | ID format | Example |
|--------|-----------|---------|
| Programme specifications | `CLRP-NNN` | CLRP-003 |
| Technical reports | `CLRP-TR-YYYY-NNN` | CLRP-TR-2026-001 |
| Research notes | `CLRP-RN-YYYY-NNN` | CLRP-RN-2026-001 |
| Validation reports | `CLRP-VR-YYYY-NNN` | CLRP-VR-2026-001 |
| Proposals | `CLRP-P-YYYY-NNN` | CLRP-P-2026-001 |

Within a calendar year, NNN increments independently per series.

## Repository releases

### Programme release tags

```
clrp-vYYYY.M
```

Examples: `clrp-v2026.1`, `clrp-v2027.2`

- Cut quarterly or after significant Accepted batches.
- Annotated tags with release notes in GitHub Releases.
- Archive to Zenodo for DOI assignment (recommended).

### Document-level tags (optional)

```
CLRP-003-v1.2.0
```

Use when a single specification reaches a major milestone worth independent citation.

## Draft marking requirements

Every document must include YAML frontmatter:

```yaml
clrp-id: CLRP-003
title: Measurement Principles
version: 0.1.0
status: Draft
date: 2026-07-07
authors:
  - Synaptic Four
license: CC-BY-4.0
```

### Status banner (Markdown body)

Draft and Proposed documents must begin (after frontmatter) with:

```markdown
> **Status: Draft** — This document is work in progress and does not yet
> represent an accepted programme commitment.
```

Adjust status label accordingly.

Accepted documents omit the warning banner but retain frontmatter.

## Revision history

Each document ends with:

```markdown
## Revision history

| Version | Date | Status | Summary |
|---------|------|--------|---------|
| 0.1.0 | 2026-07-07 | Draft | Initial publication |
```

## Branch strategy

| Branch | Purpose |
|--------|---------|
| `main` | Default; reflects current programme state |
| `release/clrp-vYYYY.M` | Optional stabilization branch before tag |

Feature work happens on branches; **Accepted** documents merge only through reviewed PRs to `main`.

## Relationship to implementations

Implementation version numbers (CLM v0.2, PCMS v1.0) are **independent**. Implementations declare which CLRP release they conform to (see [CLRP-009](../../clrp/CLRP-009-implementations-and-conformance.md)).

## Errata

Factual errors in Accepted documents that do not change normative meaning:

- PATCH version bump
- Errata note in revision history
- Optional `ERRATA.md` entry for visibility

Errors that could cause ethical harm (misstated non-diagnostic boundary):

- Expedited PATCH or MINOR bump
- Notification in CHANGELOG and release notes

---

**Document:** docs/versioning/versioning-policy.md  
**Version:** 1.0.0  
**Status:** Accepted
