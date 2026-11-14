# CLRP and Synaptic Four

## Summary

Synaptic Four is the **initial steward** of the Cognitive Landscape Research Programme. The website ([synapticfour.com](https://synapticfour.com)) is the public face of the organisation—not the programme constitution.

| Surface | Role relative to CLRP |
|---------|------------------------|
| **CLRP repository** | Authoritative programme text |
| **Synaptic Four website** | Orientation for the open research pages, contact. The constitution stays in this repository. |
| **CLM / PCMS repos** | Implementations referencing CLRP |
| **SF-TR series** (`technical-reports` repo) | Synaptic Four technical reports (genomics, infrastructure); distinct from CLRP-TR |

## Stewardship vs ownership

CLRP is designed to **outlive** any single product or website revision:

- Synaptic Four stewards the repository per [GOVERNANCE.md](../../GOVERNANCE.md)
- The programme name and specifications are open (CC BY 4.0)
- Forks and external research groups may build conformant work without Synaptic Four branding

Synaptic Four maintains CLM and PCMS but does not imply that all programme research happens only in those repositories.

## Website content strategy

### What the website should do

1. **Introduce** the Cognitive Landscape Research Programme with a link to the CLRP repository
2. **List** peer-reviewed and preprint publications arising from the programme
3. **Orient** visitors to PCMS as one instrument (`map.synapticfour.com`)
4. **Link** the computational model on the implementations page, [https://synapticfour.com/en/research/implementations/](https://synapticfour.com/en/research/implementations/)
5. **Separate** Synaptic Four consulting and services from programme research artifacts

### Live pages

English:

- Open research: [https://synapticfour.com/en/research/](https://synapticfour.com/en/research/)
- The map (the public questionnaire): [https://map.synapticfour.com](https://map.synapticfour.com)
- Research implementations (PCMS and the computational model): [https://synapticfour.com/en/research/implementations/](https://synapticfour.com/en/research/implementations/)
- Validation reports: [https://synapticfour.com/en/research/validation/](https://synapticfour.com/en/research/validation/)
- The research programme: [https://synapticfour.com/en/research/cognitive-landscape/](https://synapticfour.com/en/research/cognitive-landscape/)
- Open source and public code: [https://synapticfour.com/en/opensource/](https://synapticfour.com/en/opensource/)

The same paths exist in German under `/de/` and in French under `/fr/`.

The tree below is an earlier sketch of a deeper structure. The live pages are the list above.

### What the website should not do

- Host normative programme text that diverges from CLRP
- Imply clinical validation not supported by CLRP-VR reports
- Present PCMS scores as Synaptic Four products for hire
- Duplicate CLRP specifications (link instead)

### Suggested site structure

```
synapticfour.com/
├── research/
│   └── cognitive-landscape/          # Live page. The nested paths under it are an earlier sketch.
│       ├── overview → links to CLRP repo
│       ├── pcm-research-note/        # (existing) instrument orientation
│       └── publications/             # Programme bibliography
├── publications/                     # Organisation-wide index
└── contact/
```

## Publications index

Publications should cite CLRP documents and CLRP-VR/CLRP-TR artifacts. The website catalog entry format:

| Field | Example |
|-------|---------|
| Title | PCMS Phase 1 Pilot Report |
| Type | Validation report / Preprint / Article |
| CLRP references | CLRP-003 v1.0.0, CLRP-006 v1.0.0 |
| Repository link | CLRP-VR-2027-001 or journal DOI |
| Instrument | PCMS v1.0 |

## Branding

| Name | Usage |
|------|-------|
| **Cognitive Landscape Research Programme (CLRP)** | Programme specifications, academic citation |
| **Synaptic Four** | Steward organisation, website, contact |
| **PCMS** | Specific instrument; "open research" framing |
| **CLM** | Modelling library |

Third parties implementing CLRP should not use Synaptic Four logos without permission.

## Contact

- Programme / ethics / stewardship: [contact@synapticfour.com](mailto:contact@synapticfour.com)
- Security: see [SECURITY.md](../../SECURITY.md)

---

See also: [relationship-to-clm.md](relationship-to-clm.md) · [relationship-to-pcms.md](relationship-to-pcms.md)
