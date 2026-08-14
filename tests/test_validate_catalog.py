"""Tests for scripts/validate-catalog.py."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "validate-catalog.py"


def _load_mod():
    spec = importlib.util.spec_from_file_location("validate_catalog", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["validate_catalog"] = module
    spec.loader.exec_module(module)
    return module


mod = _load_mod()


def _catalog(**overrides: Any) -> dict[str, Any]:
    data: dict[str, Any] = {
        "catalog-version": "1.0.0",
        "programme": "CLRP",
        "last-updated": "2026-07-20",
        "releases": [
            {"tag": "clrp-v2026.1", "status": "draft"},
        ],
        "specifications": [],
        "research-notes": [],
        "validation-reports": [],
        "technical-reports": [],
        "proposals": [],
    }
    data.update(overrides)
    return data


def _write_yaml(path: Path, data: dict[str, Any]) -> None:
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")


def _write_spec(
    root: Path,
    *,
    spec_id: str = "CLRP-000",
    title: str = "Foundational Concepts",
    version: str = "0.1.0",
    status: str = "Draft",
    slug: str = "foundational-concepts",
) -> str:
    rel = f"clrp/{spec_id}-{slug}.md"
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        (
            f"---\n"
            f"clrp-id: {spec_id}\n"
            f"title: {title}\n"
            f"version: {version}\n"
            f"status: {status}\n"
            f"date: 2026-07-07\n"
            f"authors:\n"
            f"  - Test\n"
            f"license: CC-BY-4.0\n"
            f"---\n\n"
            f"> **Status: {status}** — test banner.\n\n"
            f"# {spec_id}\n"
        ),
        encoding="utf-8",
    )
    return rel


def _write_vr(
    root: Path,
    *,
    report_id: str = "CLRP-VR-2026-001",
    title: str = "PCMS Instrument Validation Status",
) -> str:
    rel = f"validation/{report_id}-pcms-instrument-status.md"
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        (
            f"---\n"
            f"report-id: {report_id}\n"
            f"title: {title}\n"
            f"version: 0.1.0\n"
            f"status: Draft\n"
            f"date: 2026-07-07\n"
            f"authors:\n"
            f"  - Test\n"
            f"license: CC-BY-4.0\n"
            f"---\n\n"
            f"> **Status: Draft** — test banner.\n\n"
            f"# {report_id}\n"
        ),
        encoding="utf-8",
    )
    return rel


def _write_spec_index(root: Path, specs: list[dict[str, str]]) -> None:
    lines = [
        "# Index",
        "",
        "| ID | Title | Version | Status | File |",
        "|----|-------|---------|--------|------|",
    ]
    for spec in specs:
        name = Path(spec["path"]).name
        lines.append(
            f"| {spec['id']} | {spec['title']} | {spec['version']} | "
            f"{spec['status']} | [{name}]({name}) |"
        )
    (root / "clrp" / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_vr_index(root: Path, reports: list[dict[str, str]]) -> None:
    (root / "validation").mkdir(parents=True, exist_ok=True)
    lines = [
        "# Validation",
        "",
        "| ID | Title | Instrument | Tier | Status |",
        "|----|-------|------------|------|--------|",
    ]
    for report in reports:
        name = Path(report["path"]).name
        lines.append(
            f"| [{report['id']}](./{name}) | {report['title']} | X | T0 | "
            f"{report['status']} |"
        )
    (root / "validation" / "README.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


def _spec_entry(rel: str, **fields: str) -> dict[str, str]:
    entry = {
        "id": "CLRP-000",
        "title": "Foundational Concepts",
        "version": "0.1.0",
        "status": "Draft",
        "path": rel,
    }
    entry.update(fields)
    return entry


def _valid_repo(tmp_path: Path) -> Path:
    rel = _write_spec(tmp_path)
    spec = _spec_entry(rel)
    _write_spec_index(tmp_path, [spec])
    _write_yaml(tmp_path / "catalog.yaml", _catalog(specifications=[spec]))
    return tmp_path


def test_current_repository_passes() -> None:
    assert mod.validate(REPO) == []


def test_valid_fixture_passes(tmp_path: Path) -> None:
    assert mod.validate(_valid_repo(tmp_path)) == []


def test_missing_spec_file(tmp_path: Path) -> None:
    spec = _spec_entry("clrp/CLRP-000-foundational-concepts.md")
    (tmp_path / "clrp").mkdir()
    _write_spec_index(tmp_path, [spec])
    _write_yaml(tmp_path / "catalog.yaml", _catalog(specifications=[spec]))
    errors = mod.validate(tmp_path)
    assert any("file not found" in e for e in errors)


def test_empty_specifications_with_file_on_disk(tmp_path: Path) -> None:
    _write_spec(tmp_path)
    _write_yaml(tmp_path / "catalog.yaml", _catalog())
    errors = mod.validate(tmp_path)
    assert any("exists on disk but is not in catalog" in e for e in errors)
    assert errors  # must not exit 0


def test_broken_validation_report_path(tmp_path: Path) -> None:
    rel = _write_spec(tmp_path)
    spec = _spec_entry(rel)
    _write_spec_index(tmp_path, [spec])
    vr = {
        "id": "CLRP-VR-2026-001",
        "title": "PCMS Instrument Validation Status",
        "version": "0.1.0",
        "status": "Draft",
        "path": "validation/CLRP-VR-2026-001-missing.md",
    }
    (tmp_path / "validation").mkdir()
    _write_vr_index(tmp_path, [vr])
    _write_yaml(
        tmp_path / "catalog.yaml",
        _catalog(specifications=[spec], **{"validation-reports": [vr]}),
    )
    errors = mod.validate(tmp_path)
    assert any("CLRP-VR-2026-001" in e and "not found" in e for e in errors)


def test_validation_report_is_checked(tmp_path: Path) -> None:
    rel = _write_spec(tmp_path)
    spec = _spec_entry(rel)
    _write_spec_index(tmp_path, [spec])
    vr_rel = _write_vr(tmp_path)
    vr = {
        "id": "CLRP-VR-2026-001",
        "title": "PCMS Instrument Validation Status",
        "version": "0.1.0",
        "status": "Draft",
        "path": vr_rel,
    }
    _write_vr_index(tmp_path, [vr])
    _write_yaml(
        tmp_path / "catalog.yaml",
        _catalog(specifications=[spec], **{"validation-reports": [vr]}),
    )
    assert mod.validate(tmp_path) == []


def test_missing_index_md(tmp_path: Path) -> None:
    rel = _write_spec(tmp_path)
    spec = _spec_entry(rel)
    _write_yaml(tmp_path / "catalog.yaml", _catalog(specifications=[spec]))
    errors = mod.validate(tmp_path)
    assert any("Missing index clrp/index.md" in e for e in errors)


def test_null_id_is_collected_not_a_traceback(tmp_path: Path) -> None:
    rel = _write_spec(tmp_path)
    spec = _spec_entry(rel)
    spec["id"] = None
    _write_yaml(tmp_path / "catalog.yaml", _catalog(specifications=[spec]))
    errors = mod.validate(tmp_path)
    assert errors
    assert any("missing or invalid id" in e for e in errors)


def test_null_specifications_is_collected(tmp_path: Path) -> None:
    _write_yaml(tmp_path / "catalog.yaml", _catalog(specifications=None))
    errors = mod.validate(tmp_path)
    assert any("must be a list" in e for e in errors)


def test_absolute_path_rejected(tmp_path: Path) -> None:
    rel = _write_spec(tmp_path)
    spec = _spec_entry(rel)
    spec["path"] = "/etc/passwd"
    _write_spec_index(tmp_path, [spec])
    _write_yaml(tmp_path / "catalog.yaml", _catalog(specifications=[spec]))
    errors = mod.validate(tmp_path)
    assert any("must be relative" in e for e in errors)


def test_frontmatter_status_mismatch(tmp_path: Path) -> None:
    rel = _write_spec(tmp_path, status="Draft")
    spec = _spec_entry(rel, status="Accepted")
    _write_spec_index(tmp_path, [spec])
    _write_yaml(tmp_path / "catalog.yaml", _catalog(specifications=[spec]))
    errors = mod.validate(tmp_path)
    assert any("frontmatter status" in e for e in errors)


def test_unknown_spec_status(tmp_path: Path) -> None:
    rel = _write_spec(tmp_path)
    spec = _spec_entry(rel, status="Accpeted")
    _write_spec_index(tmp_path, [spec])
    _write_yaml(tmp_path / "catalog.yaml", _catalog(specifications=[spec]))
    errors = mod.validate(tmp_path)
    assert any("Invalid specification status" in e for e in errors)


def test_orphan_file_on_disk(tmp_path: Path) -> None:
    rel = _write_spec(tmp_path)
    spec = _spec_entry(rel)
    _write_spec(tmp_path, spec_id="CLRP-001", slug="discovering")
    _write_spec_index(tmp_path, [spec])
    _write_yaml(tmp_path / "catalog.yaml", _catalog(specifications=[spec]))
    errors = mod.validate(tmp_path)
    assert any("CLRP-001" in e and "not in catalog" in e for e in errors)


def test_extra_id_in_index(tmp_path: Path) -> None:
    rel = _write_spec(tmp_path)
    spec = _spec_entry(rel)
    extra = _spec_entry("clrp/CLRP-001-x.md", id="CLRP-001", title="Other")
    _write_spec_index(tmp_path, [spec, extra])
    _write_yaml(tmp_path / "catalog.yaml", _catalog(specifications=[spec]))
    errors = mod.validate(tmp_path)
    assert any("lists CLRP-001 which is not in the catalog" in e for e in errors)


def test_invalid_yaml_is_collected(tmp_path: Path) -> None:
    (tmp_path / "catalog.yaml").write_text(":\n  - broken\n", encoding="utf-8")
    errors = mod.validate(tmp_path)
    assert any("Invalid YAML" in e for e in errors)


def test_main_returns_1_on_errors(tmp_path: Path) -> None:
    _write_yaml(tmp_path / "catalog.yaml", _catalog(specifications=None))
    assert mod.main(tmp_path) == 1


def test_main_returns_0_on_success(tmp_path: Path) -> None:
    assert mod.main(_valid_repo(tmp_path)) == 0
