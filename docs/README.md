# Documentation index

This directory contains **meta-documentation** for the Cognitive Landscape Research Programme: policies, architecture, citation, versioning, and ecosystem relationships.

Programme specifications live in [`../clrp/`](../clrp/). This directory explains **how the repository works**, not the scientific content itself.

## Contents

| Document | Purpose |
|----------|---------|
| [architecture/repository-architecture.md](architecture/repository-architecture.md) | Repository structure and information flow |
| [versioning/versioning-policy.md](versioning/versioning-policy.md) | Document lifecycle, releases, draft marking |
| [citation/citation-guide.md](citation/citation-guide.md) | How to cite CLRP, documents, and releases |
| [ecosystem/relationship-to-clm.md](ecosystem/relationship-to-clm.md) | CLRP ↔ Cognitive Landscape Model |
| [ecosystem/relationship-to-pcms.md](ecosystem/relationship-to-pcms.md) | CLRP ↔ Perceptual & Cognitive Mapping System |
| [ecosystem/relationship-to-synapticfour.md](ecosystem/relationship-to-synapticfour.md) | CLRP ↔ Synaptic Four website and organisation |
| [zenodo-integration.md](zenodo-integration.md) | DOI archival via Zenodo + GitHub Releases |
| [governance/active-reviews.md](governance/active-reviews.md) | Open Proposed document comment periods |

## Licensing rationale

CLRP uses a **dual license** model:

### Documentation — CC BY 4.0

All programme specifications, reports, notes, and validation documents are licensed under [Creative Commons Attribution 4.0 International](../LICENSE-docs).

**Why CC BY 4.0:**

| Requirement | How CC BY 4.0 serves it |
|-------------|--------------------------|
| Academic citation | Requires attribution — aligns with scientific norms |
| Decades-long maintenance | Permits republication in textbooks, course materials, and translations with credit |
| Institutional reuse | Ethics boards and funders can excerpt normative statements legally |
| Openness | Allows commercial reuse (e.g. integrated into paid training materials) with attribution — reduces friction for adoption |
| Fork independence | Does not impose share-alike on derivative implementations |

**Why not CC BY-SA:** Share-alike would require derivatives of documentation (including slides, localised pamphlets, or composite handbooks) to use the same license. That can impede institutional publishers and mixed-license anthologies without improving scientific integrity.

**Why not CC0:** Public domain dedication removes attribution requirements, weakening traceability of programme commitments over decades.

**Why not GFDL:** Less familiar to modern open-science tooling; incompatible with some reuse patterns.

### Software — MIT

Scripts in [`../scripts/`](../scripts/) use [MIT](../LICENSE). MIT is the programme's chosen license for all Synaptic Four research software (CLM, PCMS). Keeping tooling under MIT avoids license friction when scripts are copied into implementation repositories.

## Document types vs locations

```
clrp/              → Normative programme specifications (CLRP-NNN)
technical-reports/ → Long-form CLRP-TR studies
research-notes/    → Short exploratory CLRP-RN notes
validation/        → Evidence and protocol reports
proposals/         → Pre-acceptance extensions
open-questions/    → Unresolved programme questions
bibliography/      → Shared BibTeX
historical-influences/ → Intellectual lineage
docs/              → Repository policies (this directory)
```

## Contributing to docs/

Changes to versioning, citation, or governance policies follow the same review standards as CLRP specifications. See [../CONTRIBUTING.md](../CONTRIBUTING.md).
