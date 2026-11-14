# Getting started

Prerequisites for reading: none. This repository is documents.

## Where to start

| Reader | Start with |
|--------|------------|
| Someone new to the programme | [CLRP-000](../clrp/CLRP-000-foundational-concepts.md), then the [open research overview](https://synapticfour.com/en/research/) |
| Someone citing the programme | [CITATION.cff](../CITATION.cff), then [citation/citation-guide.md](citation/citation-guide.md) |
| Someone implementing a model or a questionnaire | [CLRP-009](../clrp/CLRP-009-implementations-and-conformance.md), then [ecosystem/](ecosystem/) |
| An institutional reviewer | [FOR-EVALUATORS.md](FOR-EVALUATORS.md), then [CLRP-007](../clrp/CLRP-007-non-diagnostic-commitment.md) and [validation/](../validation/) |
| A programme steward | [GOVERNANCE.md](../GOVERNANCE.md), then [ROADMAP.md](../ROADMAP.md) |

The numbered specifications are listed in [../clrp/index.md](../clrp/index.md).

## Check the catalog

Prerequisites: Python 3, and the packages in `requirements-dev.txt` (PyYAML and pytest).

```bash
pip install -r requirements-dev.txt
python3 scripts/validate-catalog.py
```

When the catalog matches the files, the script exits 0. `python3 -m pytest tests -q` runs the validator's own tests. Neither command is a scientific result.
