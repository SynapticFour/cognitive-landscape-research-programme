#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

if ! python3 -c "import yaml" 2>/dev/null; then
  echo "ci-check: PyYAML missing. pip install -r requirements-dev.txt" >&2
  exit 1
fi
if ! python3 -c "import pytest" 2>/dev/null; then
  echo "ci-check: pytest missing. pip install -r requirements-dev.txt" >&2
  exit 1
fi

echo "ci-check: validate-catalog.py"
python3 scripts/validate-catalog.py
echo "ci-check: pytest"
python3 -m pytest tests -q
echo "ci-check: OK"
