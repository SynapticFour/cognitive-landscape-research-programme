#!/usr/bin/env python3
"""Validate catalog.yaml structure and cross-references to CLRP files."""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog.yaml"
RESEARCH_NOTE_STATUSES = {"Exploratory", "Superseded", "Accepted-into-spec"}


def main() -> int:
    if not CATALOG.exists():
        print(f"Missing {CATALOG}")
        return 1

    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    errors: list[str] = []

    for key in ("catalog-version", "programme", "specifications", "releases"):
        if key not in data:
            errors.append(f"Missing top-level key: {key}")

    spec_ids: set[str] = set()
    for spec in data.get("specifications", []):
        for field in ("id", "title", "version", "status", "path"):
            if field not in spec:
                errors.append(f"Specification missing '{field}': {spec}")
        sid = spec.get("id", "")
        if sid in spec_ids:
            errors.append(f"Duplicate specification id: {sid}")
        spec_ids.add(sid)
        path = ROOT / spec.get("path", "")
        if not path.is_file():
            errors.append(f"Specification file not found: {spec.get('path')}")

    note_ids: set[str] = set()
    for note in data.get("research-notes", []):
        for field in ("id", "title", "date", "status", "path"):
            if field not in note:
                errors.append(f"Research note missing '{field}': {note}")
        nid = note.get("id", "")
        if nid in note_ids:
            errors.append(f"Duplicate research note id: {nid}")
        note_ids.add(nid)
        if note.get("status") not in RESEARCH_NOTE_STATUSES:
            errors.append(f"Invalid research note status: {note.get('status')}")
        path = ROOT / note.get("path", "")
        if not path.is_file():
            errors.append(f"Research note file not found: {note.get('path')}")

    for release in data.get("releases", []):
        tag = release.get("tag")
        if not tag:
            errors.append(f"Release missing tag: {release}")
        if release.get("status") == "published" and not release.get("doi"):
            errors.append(f"Published release {tag} missing doi")

    clrp_index = ROOT / "clrp" / "index.md"
    if clrp_index.is_file():
        text = clrp_index.read_text(encoding="utf-8")
        for sid in spec_ids:
            if sid not in text:
                errors.append(f"clrp/index.md does not mention {sid}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        return 1

    print(
        f"OK: catalog v{data.get('catalog-version')} — "
        f"{len(spec_ids)} specifications, {len(data.get('releases', []))} releases, "
        f"{len(note_ids)} research-notes"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
