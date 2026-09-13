#!/usr/bin/env bash
# Executable software contracts, not a score for physical product capability.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
bash "$ROOT/tests/score.test.sh"
bash "$ROOT/scripts/sync-plugin.sh" --check
echo 'ANVIL_SOFTWARE_CHECKS: PASS (physical product qualification requires external evidence)'
