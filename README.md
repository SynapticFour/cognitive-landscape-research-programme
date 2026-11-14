# Cognitive Landscape Research Programme (CLRP)

CLRP is the open foundation for describing differences in thinking as positions on continuous scales, without turning those positions into a diagnosis. The texts are meant to outlast any one piece of software.

For a researcher, a funder, or an institution that wants the assumptions and the limits in writing, separate from the questionnaire and from the computational library.

**Status: No public status is recorded.** The claims registry has no maturity stage for this repository. Each specification has its own document status in [clrp/index.md](clrp/index.md). The tags `clrp-v2026.1` and `clrp-v2026.2` are releases. A tag is not a public status label.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Documentation: CC BY 4.0](https://img.shields.io/badge/Documentation-CC%20BY%204.0-lightgrey.svg)](LICENSE-docs)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21389829.svg)](https://doi.org/10.5281/zenodo.21389829)

## What it does

- It holds the numbered specifications in `clrp/`, from foundational concepts through implementations. The index is [clrp/index.md](clrp/index.md).
- It holds draft validation reports. The questionnaire report records tier T0. The model report records tier T1 for engineering verification. See [docs/STATUS.md](docs/STATUS.md).
- It states a working assumption: cognitive traits are mostly distributed along a continuum, and fixed labels represent them poorly (CLRP-RATIONALE-001). That assumption is not an established finding.
- The four parts of the work are this programme, the model [CLM](https://github.com/SynapticFour/cognitive-landscape-model), the tool [PCMS](https://github.com/SynapticFour/perceptual-cognitive-mapping-system), and the validation reports (CLRP-STRUCTURE-001). Existence of the parts is not a measure of how well they are validated.

## Limits

- Not the public questionnaire, and not the computational library. Those are the repositories linked above.
- Not a diagnostic instrument. The non-diagnostic text is [CLRP-007](clrp/CLRP-007-non-diagnostic-commitment.md), and its status is Proposed, pending steward disposition.
- Not an empirical sample. The questionnaire report is a draft at tier T0: there is no empirical sample yet (PCMS-VALIDATION-001).
- A catalog check confirms files. It does not confirm a scientific result.

The boundary is [docs/SCOPE.md](docs/SCOPE.md). The previous README, including the specification table, is [docs/FROM-README.md](docs/FROM-README.md).

## How to read

Prerequisites: none. This repository is documents.

Start with [CLRP-000](clrp/CLRP-000-foundational-concepts.md) for the concepts, or with [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md) for the reader-specific path. To check the catalog:

```bash
pip install -r requirements-dev.txt
python3 scripts/validate-catalog.py
```

When the catalog matches the files, the script exits 0.

## Documentation

Every file under `docs/` is listed in [docs/README.md](docs/README.md). The groups are a tutorial, how-to guides, reference, and explanation.

### Tutorial

- [Getting started](docs/GETTING-STARTED.md)

### How-to guides

- [Versioning policy](docs/versioning/versioning-policy.md)
- [Zenodo](docs/zenodo-integration.md)
- [Contributing](CONTRIBUTING.md)

### Reference

- [Evidence status](docs/STATUS.md)
- [What this is not](docs/SCOPE.md)
- [For evaluators](docs/FOR-EVALUATORS.md)
- [Citation guide](docs/citation/citation-guide.md)
- [Specification index](clrp/index.md)

### Explanation

- [Architecture of the archive](docs/ARCHITECTURE.md)
- [Repository layout](docs/architecture/repository-architecture.md)
- [Relationship to the website](docs/ecosystem/relationship-to-synapticfour.md)

## Licence

Two files, and they cover different things.

- [LICENSE](LICENSE) is the MIT licence. It covers the software: the scripts and tooling in this repository.
- [LICENSE-docs](LICENSE-docs) is Creative Commons Attribution 4.0. It covers the programme documents: specifications, reports, and notes.

The rationale is in [docs/REPOSITORY-GUIDE.md](docs/REPOSITORY-GUIDE.md). This is not legal advice.

## Cite

Use [CITATION.cff](CITATION.cff). Prefer that file over a hand-copied line. It names release `clrp-v2026.2` and a DOI. To cite one specification, use that document's ID and version, as the citation guide describes.

## Website

- Open research: [https://synapticfour.com/en/offene-forschung/](https://synapticfour.com/en/offene-forschung/)
- The research programme: [https://synapticfour.com/en/offene-forschung/forschungsprogramm/](https://synapticfour.com/en/offene-forschung/forschungsprogramm/)
- Technical profile: [https://synapticfour.com/en/technical/code/](https://synapticfour.com/en/technical/code/)

The same pages exist in German (`/de/offene-forschung/`, `/de/offene-forschung/forschungsprogramm/`, `/de/technik/code/`) and in French (`/fr/offene-forschung/`, `/fr/offene-forschung/forschungsprogramm/`, `/fr/technique/code/`).

The map of repositories: [profile/README.md](https://github.com/SynapticFour/.github/blob/main/profile/README.md).

Contact: [contact@synapticfour.com](mailto:contact@synapticfour.com)

Governance: [GOVERNANCE.md](GOVERNANCE.md). Changelog: [CHANGELOG.md](CHANGELOG.md). Security: [SECURITY.md](SECURITY.md).
