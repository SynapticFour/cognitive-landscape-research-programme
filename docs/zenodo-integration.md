# Zenodo integration

Guide to archiving CLRP releases on [Zenodo](https://zenodo.org) with citable DOIs.

## Why Zenodo

| Benefit | Description |
|---------|-------------|
| Persistent DOI | Standard identifier for grants, ethics submissions, and publications |
| Version archival | Each `clrp-v*` release receives a version DOI |
| GitHub integration | Automatic ingestion from GitHub Releases (source archive) |
| Open access | CC BY 4.0 documentation |

CLRP is a **documentation repository**. Zenodo archives the GitHub Release tarball (Markdown, YAML, BibTeX). No PDF build step is required.

## Prerequisites

- Public repository: `SynapticFour/cognitive-landscape-research-programme`
- Zenodo account linked to GitHub
- At least one **GitHub Release** (not tag alone): `clrp-v2026.1`

## One-time setup (web UI — cannot be automated)

1. Sign in to Zenodo with GitHub
2. Open **Account settings → GitHub**: https://zenodo.org/account/settings/github/
3. Grant access to the **SynapticFour** organisation if prompted
4. Find **`cognitive-landscape-research-programme`** in the repository list
5. Toggle the switch **ON**

Until the toggle is enabled, releases will not create Zenodo drafts.

## Release workflow

```
1. Merge changes to main
2. Tag: git tag -a clrp-vYYYY.M -m "..."
3. Push tag: git push origin clrp-vYYYY.M
4. Create GitHub Release from tag (Release notes required for clarity)
5. Zenodo creates draft deposition (if integration enabled)
6. Review draft at zenodo.org/me/uploads
7. Publish → version DOI minted
8. Update CITATION.cff and catalog.yaml with DOI
```

## Metadata

Repository metadata lives in [`.zenodo.json`](../.zenodo.json). Zenodo merges this with release information on first deposit.

## Citation after publish

Update root [CITATION.cff](../CITATION.cff):

```yaml
preferred-citation:
  doi: 10.5281/zenodo.XXXXXXX
```

Update [docs/citation/citation-guide.md](./citation/citation-guide.md) release examples.

## Private repository?

Zenodo GitHub integration requires a **public** repository. CLRP is public by design.

Manual upload alternative: create a deposition at https://zenodo.org/deposit/new and upload the release `.zip` from GitHub Releases.

## Related

- Synaptic Four SF-TR Zenodo workflow: `SynapticFour/technical-reports/docs/zenodo-integration.md` (PDF/HTML reports; different series)

---

**Status:** Integration configured in repository; steward must enable Zenodo GitHub toggle.
