#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"
echo "ci-check: validate-catalog.py"
python3 scripts/validate-catalog.py
echo "ci-check: OK"
