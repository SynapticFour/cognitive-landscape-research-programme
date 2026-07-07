# Citation guide

This guide explains how to cite the Cognitive Landscape Research Programme (CLRP), its documents, releases, and related implementations.

## Citation hierarchy

```
Programme (whole repository)
    └── Release snapshot (Zenodo DOI)
            └── CLRP specification (CLRP-NNN + version)
                    └── Technical report / validation report (CLRP-TR / CLRP-VR)
                            └── External publication (journal article)
```

Cite the **most specific** artifact you relied upon.

## 1. Citing the programme (general reference)

Use when referring to CLRP as an ongoing research programme without pinning to a specific release. Resolves to the latest version via Zenodo.

**BibTeX:**

```bibtex
@misc{clrp2026concept,
  author       = {{Synaptic Four}},
  title        = {Cognitive Landscape Research Programme ({CLRP})},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21236099},
  url          = {https://doi.org/10.5281/zenodo.21236099},
  note         = {Concept DOI; documentation licensed under CC BY 4.0}
}
```

**APA:**

> Synaptic Four. (2026). *Cognitive Landscape Research Programme (CLRP)*. Zenodo. https://doi.org/10.5281/zenodo.21236099

For a **specific release**, use the version DOI (section 2) or GitHub tag.

Also see root [CITATION.cff](../../CITATION.cff) for machine-readable metadata.

## 2. Citing a release snapshot

When citing a frozen programme state (recommended for reproducibility):

```bibtex
@misc{clrp2026_1,
  author       = {{Synaptic Four}},
  title        = {Cognitive Landscape Research Programme ({CLRP})},
  year         = {2026},
  version      = {clrp-v2026.1},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21236100},
  url          = {https://doi.org/10.5281/zenodo.21236100}
}
```

**APA:**

> Synaptic Four. (2026). *Cognitive Landscape Research Programme (CLRP)* (Version clrp-v2026.1). Zenodo. https://doi.org/10.5281/zenodo.21236100

| DOI | Use when |
|-----|----------|
| [10.5281/zenodo.21236100](https://doi.org/10.5281/zenodo.21236100) | Citing **this** release (`clrp-v2026.1`) |
| [10.5281/zenodo.21236099](https://doi.org/10.5281/zenodo.21236099) | Citing the programme **in general** (always resolves to latest) |

GitHub tag (alternative): https://github.com/SynapticFour/cognitive-landscape-research-programme/releases/tag/clrp-v2026.1

## 3. Citing a CLRP specification

**Required elements:**

| Element | Example |
|---------|---------|
| Document ID | CLRP-003 |
| Title | Measurement Principles |
| Version | 1.0.0 |
| Status | Accepted |
| URL | Permalink to file on tag or commit |
| Access date | If no DOI |

**BibTeX:**

```bibtex
@techreport{clrp003,
  author       = {{Synaptic Four}},
  title        = {{CLRP-003}: Measurement Principles},
  institution  = {Cognitive Landscape Research Programme},
  year         = {2026},
  number       = {CLRP-003},
  version      = {0.1.0},
  url          = {https://github.com/SynapticFour/cognitive-landscape-research-programme/blob/clrp-v2026.1/clrp/CLRP-003-measurement-principles.md},
  note         = {Status: Draft}
}
```

Update `version`, `url`, and `note` to match the cited snapshot.

**In-text:**

> (Synaptic Four, 2026, CLRP-003 v0.1.0)

## 4. Citing technical reports and validation reports

```bibtex
@techreport{clrp_tr_2026_001,
  author       = {{Synaptic Four}},
  title        = {{CLRP-TR-2026-001}: Example Methods Study},
  institution  = {Cognitive Landscape Research Programme},
  year         = {2026},
  number       = {CLRP-TR-2026-001},
  url          = {https://github.com/SynapticFour/cognitive-landscape-research-programme/tree/main/technical-reports/CLRP-TR-2026-001}
}
```

Validation reports use `CLRP-VR-YYYY-NNN` with the same pattern.

## 5. How implementations should reference CLRP

### Software repositories (CLM, PCMS)

In README and academic exports:

```markdown
This implementation conforms to [CLRP-009 vX.Y.Z](URL) and references
[CLRP-003 Measurement Principles](URL) for scoring semantics.
```

In code provenance metadata:

```json
{
  "programme": "CLRP",
  "clrpRelease": "clrp-v2026.1",
  "clrpDoi": "10.5281/zenodo.21236100",
  "clrpDocuments": [
    {"id": "CLRP-003", "version": "1.0.0"},
    {"id": "CLRP-007", "version": "1.0.0"}
  ]
}
```

### Technical reports (CLRP-TR)

Must include in frontmatter:

```yaml
clrp-references:
  - id: CLRP-003
    version: 1.0.0
  - id: CLRP-006
    version: 1.0.0
```

### Peer-reviewed publications

Journal articles should cite:

1. The specific CLRP documents that define terms and constraints used
2. The validation report(s) supporting empirical claims
3. The implementation repository (if describing an instrument)
4. The CLRP release tag or commit SHA used in the study

CLRP documents should **not** replace citation of peer-reviewed literature where empirical claims are made.

## 6. Cross-reference syntax (internal)

Within this repository, link as:

```markdown
[CLRP-003: Measurement Principles](../clrp/CLRP-003-measurement-principles.md)
```

In external repositories:

```markdown
[CLRP-003 v1.0.0](https://github.com/SynapticFour/cognitive-landscape-research-programme/blob/clrp-v2026.1/clrp/CLRP-003-measurement-principles.md)
```

Always pin to a **tag or commit**, not `main`, in reproducible research.

## 7. DOI strategy

| Artifact | DOI |
|----------|-----|
| Programme releases | Version DOI per release + [concept DOI 10.5281/zenodo.21236099](https://doi.org/10.5281/zenodo.21236099) |
| `clrp-v2026.1` | [10.5281/zenodo.21236100](https://doi.org/10.5281/zenodo.21236100) |
| Individual CLRP specs | Included in release archive; optional standalone deposit for major specs |
| CLRP-TR / CLRP-VR | Encouraged per report via Zenodo or journal DOI |

Zenodo GitHub integration is **enabled**. See [zenodo-integration.md](../zenodo-integration.md).

## 8. What not to cite

- Draft documents in normative claims (mark as draft explicitly if necessary)
- Implementation READMEs as programme authority (they reference CLRP; they are not CLRP)
- Deprecated documents without noting supersession

---

**Version:** 1.0.0  
**Status:** Accepted
