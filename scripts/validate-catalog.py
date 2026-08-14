#!/usr/bin/env python3
"""Validate catalog.yaml structure and cross-references to CLRP files."""
from __future__ import annotations

import fnmatch
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install -r requirements-dev.txt")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent

SPEC_STATUSES = frozenset(
    {"Draft", "Proposed", "Accepted", "Deprecated", "Superseded"}
)
RESEARCH_NOTE_STATUSES = frozenset(
    {"Exploratory", "Superseded", "Accepted-into-spec"}
)
REPORT_STATUSES = SPEC_STATUSES
RELEASE_STATUSES = frozenset({"published", "draft", "planned"})

ID_SPEC = re.compile(r"^CLRP-\d{3}$")
ID_RN = re.compile(r"^CLRP-RN-\d{4}-\d{3}$")
ID_VR = re.compile(r"^CLRP-VR-\d{4}-\d{3}$")
ID_TR = re.compile(r"^CLRP-TR-\d{4}-\d{3}$")
ID_P = re.compile(r"^CLRP-P-\d{4}-\d{3}$")

REQUIRED_TOP_LEVEL = (
    "catalog-version",
    "programme",
    "last-updated",
    "specifications",
    "releases",
    "research-notes",
    "validation-reports",
    "technical-reports",
    "proposals",
)

FRONTMATTER_COMMON = ("title", "status", "date", "authors", "license")


@dataclass(frozen=True)
class Series:
    key: str
    kind: str
    directory: str
    filename_glob: str
    required: tuple[str, ...]
    statuses: frozenset[str]
    id_pattern: re.Pattern[str]
    frontmatter_id_key: str
    index_rel: str | None
    index_min_cols: int
    # catalog field name -> markdown table column index
    index_fields: tuple[tuple[str, int], ...]


SERIES: tuple[Series, ...] = (
    Series(
        key="specifications",
        kind="specification",
        directory="clrp",
        filename_glob="CLRP-*.md",
        required=("id", "title", "version", "status", "path"),
        statuses=SPEC_STATUSES,
        id_pattern=ID_SPEC,
        frontmatter_id_key="clrp-id",
        index_rel="clrp/index.md",
        index_min_cols=5,
        index_fields=(("title", 1), ("version", 2), ("status", 3)),
    ),
    Series(
        key="research-notes",
        kind="research note",
        directory="research-notes",
        filename_glob="CLRP-*.md",
        required=("id", "title", "date", "status", "path"),
        statuses=RESEARCH_NOTE_STATUSES,
        id_pattern=ID_RN,
        frontmatter_id_key="note-id",
        index_rel="research-notes/README.md",
        index_min_cols=4,
        index_fields=(("title", 1), ("date", 2), ("status", 3)),
    ),
    Series(
        key="validation-reports",
        kind="validation report",
        directory="validation",
        filename_glob="CLRP-*.md",
        required=("id", "title", "version", "status", "path"),
        statuses=REPORT_STATUSES,
        id_pattern=ID_VR,
        frontmatter_id_key="report-id",
        index_rel="validation/README.md",
        index_min_cols=5,
        index_fields=(("title", 1), ("status", 4)),
    ),
    Series(
        key="technical-reports",
        kind="technical report",
        directory="technical-reports",
        filename_glob="CLRP-*.md",
        required=("id", "title", "version", "status", "path"),
        statuses=REPORT_STATUSES,
        id_pattern=ID_TR,
        frontmatter_id_key="report-id",
        index_rel=None,
        index_min_cols=0,
        index_fields=(),
    ),
    Series(
        key="proposals",
        kind="proposal",
        directory="proposals",
        filename_glob="CLRP-*.md",
        required=("id", "title", "status", "path"),
        statuses=REPORT_STATUSES,
        id_pattern=ID_P,
        frontmatter_id_key="proposal-id",
        index_rel=None,
        index_min_cols=0,
        index_fields=(),
    ),
)


def _norm(value: Any) -> str:
    if value is None:
        return ""
    if hasattr(value, "isoformat"):
        return value.isoformat()
    return str(value).strip()


def _strip_md(cell: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", cell)
    text = re.sub(r"\*+", "", text)
    return text.strip()


def _leading_status(cell: str, statuses: frozenset[str]) -> str | None:
    text = _strip_md(cell)
    for status in sorted(statuses, key=len, reverse=True):
        if text == status or text.startswith(status + " ") or text.startswith(
            status + "—"
        ):
            return status
        if text.startswith(status + "(") or text.startswith(status + ":"):
            return status
    return None


def _extract_id(cell: str, pattern: re.Pattern[str]) -> str | None:
    text = _strip_md(cell)
    if not text:
        return None
    token = text.split()[0].strip("[]()*")
    if pattern.fullmatch(token):
        return token
    if pattern.fullmatch(text):
        return text
    return None


def _parse_md_table(text: str, min_cols: int) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cols = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cols) < min_cols:
            continue
        if set(cols[0]) <= {"-", ":"} or cols[0].lower() in {
            "id",
            "range",
            "status",
            "study",
        }:
            continue
        rows.append(cols)
    return rows


def _parse_frontmatter(path: Path) -> tuple[dict[str, Any] | None, str, str | None]:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3 or parts[0].strip():
        return None, text, "missing YAML frontmatter"
    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        return None, parts[2], f"invalid frontmatter YAML: {exc}"
    if not isinstance(fm, dict):
        return None, parts[2], "frontmatter is not a mapping"
    return fm, parts[2], None


def _resolve_in_root(root: Path, rel: Any) -> tuple[Path | None, str | None]:
    if not isinstance(rel, str) or not rel.strip():
        return None, "path is empty"
    candidate = Path(rel)
    if candidate.is_absolute():
        return None, f"path must be relative to the repository: {rel}"
    root_res = root.resolve()
    resolved = (root / rel).resolve()
    if not resolved.is_relative_to(root_res):
        return None, f"path escapes the repository: {rel}"
    return resolved, None


def _load_catalog(root: Path) -> tuple[dict[str, Any] | None, list[str]]:
    catalog_path = root / "catalog.yaml"
    if not catalog_path.is_file():
        return None, [f"Missing {catalog_path}"]
    try:
        data = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return None, [f"Invalid YAML in catalog.yaml: {exc}"]
    if not isinstance(data, dict):
        return None, ["catalog.yaml must be a mapping"]
    return data, []


def _require_list(data: dict[str, Any], key: str, errors: list[str]) -> list[Any]:
    if key not in data:
        return []
    value = data[key]
    if value is None:
        errors.append(f"{key} must be a list, not null")
        return []
    if not isinstance(value, list):
        errors.append(f"{key} must be a list")
        return []
    return value


def _disk_paths(root: Path, series: Series) -> list[str]:
    directory = root / series.directory
    if not directory.is_dir():
        return []
    found: list[str] = []
    for path in sorted(directory.iterdir()):
        if path.is_file() and fnmatch.fnmatch(path.name, series.filename_glob):
            found.append(path.relative_to(root).as_posix())
    return found


def _check_entry(
    errors: list[str],
    root: Path,
    series: Series,
    entry: Any,
    seen_ids: set[str],
    seen_paths: set[str],
) -> dict[str, Any] | None:
    if not isinstance(entry, dict):
        errors.append(f"{series.kind} entry is not a mapping: {entry!r}")
        return None

    for field in series.required:
        if field not in entry:
            errors.append(f"{series.kind} missing '{field}': {entry}")

    entry_id = entry.get("id")
    if not isinstance(entry_id, str) or not entry_id:
        errors.append(f"{series.kind} missing or invalid id: {entry}")
        entry_id = None
    elif not series.id_pattern.fullmatch(entry_id):
        errors.append(f"{series.kind} id {entry_id!r} does not match {series.id_pattern.pattern}")
    elif entry_id in seen_ids:
        errors.append(f"Duplicate {series.kind} id: {entry_id}")
    else:
        seen_ids.add(entry_id)

    status = entry.get("status")
    if status is not None and status not in series.statuses:
        errors.append(f"Invalid {series.kind} status: {status}")

    if (
        series.key == "specifications"
        and status == "Proposed"
        and not entry.get("review_until")
    ):
        errors.append(f"Proposed specification {entry_id} missing review_until")

    rel = entry.get("path")
    resolved, path_err = _resolve_in_root(root, rel)
    if path_err:
        errors.append(f"{series.kind} {entry_id or rel}: {path_err}")
        return entry
    assert resolved is not None
    assert isinstance(rel, str)

    posix = Path(rel).as_posix()
    if posix in seen_paths:
        errors.append(f"Duplicate path {posix}")
    else:
        seen_paths.add(posix)

    expected_prefix = f"{series.directory}/"
    if not posix.startswith(expected_prefix):
        errors.append(
            f"{series.kind} {entry_id} path {posix} is not under {series.directory}/"
        )

    if not fnmatch.fnmatch(Path(posix).name, series.filename_glob):
        errors.append(
            f"{series.kind} {entry_id} filename does not match {series.filename_glob}"
        )

    if entry_id and not Path(posix).name.startswith(entry_id):
        errors.append(
            f"{series.kind} {entry_id} filename {Path(posix).name} does not start with the id"
        )

    if not resolved.is_file():
        errors.append(f"{series.kind} file not found: {posix}")
        return entry

    fm, body, fm_err = _parse_frontmatter(resolved)
    if fm_err:
        errors.append(f"{posix}: {fm_err}")
        return entry
    assert fm is not None

    fm_id = fm.get(series.frontmatter_id_key)
    if entry_id and _norm(fm_id) != entry_id:
        errors.append(
            f"{posix}: frontmatter {series.frontmatter_id_key} {_norm(fm_id)!r} "
            f"!= catalog id {entry_id!r}"
        )
    for field in ("title", "status"):
        if field in entry and _norm(fm.get(field)) != _norm(entry.get(field)):
            errors.append(
                f"{posix}: frontmatter {field} {_norm(fm.get(field))!r} "
                f"!= catalog {_norm(entry.get(field))!r}"
            )
    if "version" in series.required and "version" in entry:
        if _norm(fm.get("version")) != _norm(entry.get("version")):
            errors.append(
                f"{posix}: frontmatter version {_norm(fm.get('version'))!r} "
                f"!= catalog {_norm(entry.get('version'))!r}"
            )
    if "date" in series.required and "date" in entry:
        if _norm(fm.get("date")) != _norm(entry.get("date")):
            errors.append(
                f"{posix}: frontmatter date {_norm(fm.get('date'))!r} "
                f"!= catalog {_norm(entry.get('date'))!r}"
            )

    for field in FRONTMATTER_COMMON:
        if field not in fm:
            errors.append(f"{posix}: frontmatter missing '{field}'")
    if series.frontmatter_id_key not in fm:
        errors.append(f"{posix}: frontmatter missing '{series.frontmatter_id_key}'")

    if status in {"Draft", "Proposed"}:
        banner = re.search(
            r"^>\s*\*\*Status:\s*([^*]+)\*\*",
            body.lstrip(),
            flags=re.MULTILINE,
        )
        if not banner or banner.group(1).strip() != status:
            errors.append(
                f"{posix}: Draft/Proposed document must start with a "
                f"'Status: {status}' banner"
            )

    return entry


def _check_series(
    errors: list[str],
    root: Path,
    data: dict[str, Any],
    series: Series,
) -> list[dict[str, Any]]:
    raw = _require_list(data, series.key, errors)
    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    entries: list[dict[str, Any]] = []
    for item in raw:
        checked = _check_entry(errors, root, series, item, seen_ids, seen_paths)
        if isinstance(checked, dict):
            entries.append(checked)

    catalog_paths = {
        Path(e["path"]).as_posix()
        for e in entries
        if isinstance(e.get("path"), str) and e["path"]
    }
    disk = _disk_paths(root, series)
    for rel in disk:
        if rel not in catalog_paths:
            errors.append(f"{rel} exists on disk but is not in catalog {series.key}")
    for rel in sorted(catalog_paths):
        if rel not in disk and (root / rel).is_file():
            errors.append(
                f"{rel} is in catalog {series.key} but does not match {series.filename_glob}"
            )

    if series.index_rel and (entries or disk):
        _check_index(errors, root, series, entries)

    return entries


def _check_index(
    errors: list[str],
    root: Path,
    series: Series,
    entries: list[dict[str, Any]],
) -> None:
    assert series.index_rel is not None
    index_path = root / series.index_rel
    if not index_path.is_file():
        errors.append(f"Missing index {series.index_rel}")
        return

    rows = _parse_md_table(
        index_path.read_text(encoding="utf-8"), series.index_min_cols
    )
    by_id: dict[str, list[str]] = {}
    for cols in rows:
        sid = _extract_id(cols[0], series.id_pattern)
        if sid is None:
            continue
        if sid in by_id:
            errors.append(f"{series.index_rel} lists {sid} more than once")
        by_id[sid] = cols

    catalog_ids = {
        e["id"] for e in entries if isinstance(e.get("id"), str) and e["id"]
    }
    for sid in sorted(catalog_ids - by_id.keys()):
        errors.append(f"{series.index_rel} does not list {sid}")
    for sid in sorted(by_id.keys() - catalog_ids):
        errors.append(f"{series.index_rel} lists {sid} which is not in the catalog")

    for entry in entries:
        sid = entry.get("id")
        if not isinstance(sid, str) or sid not in by_id:
            continue
        cols = by_id[sid]
        for field, col_i in series.index_fields:
            if col_i >= len(cols) or field not in entry:
                continue
            cell = cols[col_i]
            if field == "status":
                got = _leading_status(cell, series.statuses)
                want = _norm(entry.get("status"))
                if got != want:
                    errors.append(
                        f"{series.index_rel}: {sid} status {got!r} != catalog {want!r}"
                    )
            else:
                got = _strip_md(cell)
                want = _norm(entry.get(field))
                if got != want:
                    errors.append(
                        f"{series.index_rel}: {sid} {field} {got!r} != catalog {want!r}"
                    )


def _check_releases(errors: list[str], data: dict[str, Any]) -> list[dict[str, Any]]:
    raw = _require_list(data, "releases", errors)
    seen: set[str] = set()
    releases: list[dict[str, Any]] = []
    for item in raw:
        if not isinstance(item, dict):
            errors.append(f"Release entry is not a mapping: {item!r}")
            continue
        tag = item.get("tag")
        if not isinstance(tag, str) or not tag:
            errors.append(f"Release missing tag: {item}")
            tag = None
        elif tag in seen:
            errors.append(f"Duplicate release tag: {tag}")
        else:
            seen.add(tag)
        status = item.get("status")
        if status not in RELEASE_STATUSES:
            errors.append(f"Invalid release status: {status}")
        if status == "published" and not item.get("doi"):
            errors.append(f"Published release {tag} missing doi")
        releases.append(item)
    return releases


def _normalize_doi(value: Any) -> str:
    text = _norm(value).removeprefix("https://doi.org/").removeprefix("http://doi.org/")
    return text.strip()


def _check_citation(errors: list[str], root: Path, releases: list[dict[str, Any]]) -> None:
    published = [r for r in releases if r.get("status") == "published" and r.get("doi")]
    if not published:
        return
    citation_path = root / "CITATION.cff"
    if not citation_path.is_file():
        errors.append("CITATION.cff missing while published releases exist")
        return
    try:
        citation = yaml.safe_load(citation_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"Invalid YAML in CITATION.cff: {exc}")
        return
    if not isinstance(citation, dict):
        errors.append("CITATION.cff must be a mapping")
        return
    latest = published[-1]
    want = _normalize_doi(latest.get("doi"))
    preferred = citation.get("preferred-citation")
    got = ""
    if isinstance(preferred, dict):
        got = _normalize_doi(preferred.get("doi"))
    if not got:
        got = _normalize_doi(citation.get("doi"))
    if want and got != want:
        errors.append(
            f"CITATION.cff DOI {got!r} != latest published release "
            f"{latest.get('tag')} DOI {want!r}"
        )


def validate(root: Path) -> list[str]:
    data, errors = _load_catalog(root)
    if data is None:
        return errors

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            errors.append(f"Missing top-level key: {key}")

    if data.get("programme") != "CLRP":
        errors.append(f"programme must be 'CLRP', got {data.get('programme')!r}")

    counts: dict[str, int] = {}
    for series in SERIES:
        entries = _check_series(errors, root, data, series)
        counts[series.key] = len(entries)

    releases = _check_releases(errors, data)
    counts["releases"] = len(releases)
    _check_citation(errors, root, releases)

    if not errors:
        print(
            f"OK: catalog v{data.get('catalog-version')} — "
            f"{counts['specifications']} specifications, "
            f"{counts['releases']} releases, "
            f"{counts['research-notes']} research-notes, "
            f"{counts['validation-reports']} validation-reports, "
            f"{counts['technical-reports']} technical-reports, "
            f"{counts['proposals']} proposals"
        )
    return errors


def main(root: Path | None = None) -> int:
    errors = validate(root or ROOT)
    if errors:
        for message in errors:
            print(f"ERROR: {message}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
