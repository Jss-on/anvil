#!/usr/bin/env bash
# system.test.sh — system-integration gate self-test (pinout / product-bom / sys-budget).
# Usage: system.test.sh [gate] — run every case, or only the named gate's cases.
# Zero matched cases for a filter is a FAILURE (a gate with no tests is untested).
set -uo pipefail
export LC_ALL=C

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCORE="$ROOT/scripts/score-anvil.sh"
FIX="$ROOT/tests/fixtures/system"
only="${1:-}"
fails=0
n=0

want() { [[ -z "$only" || "$only" == "$1" ]]; }
assert_eq() { # name expected actual
  n=$((n + 1))
  if [[ "$2" == "$3" ]]; then
    echo "ok $n — $1"
  else
    echo "FAIL $n — $1: expected [$2] got [$3]"
    fails=$((fails + 1))
  fi
}

# --- pinout: harness ↔ ICD consistency + ampacity ----------------------------
if want pinout; then
  assert_eq "pinout: consistent harness = 0 violations" "PINOUT_VIOLATIONS: 0" \
    "$(bash "$SCORE" pinout "$FIX/harness-good.tsv" "$FIX/icd.tsv" 2>/dev/null)"
  assert_eq "pinout: unknown ICD + overcurrent + malformed + unrealized = 4" "PINOUT_VIOLATIONS: 4" \
    "$(bash "$SCORE" pinout "$FIX/harness-bad.tsv" "$FIX/icd.tsv" 2>/dev/null)"
fi

echo
if [[ $n -eq 0 ]]; then
  echo "NO SYSTEM CASES matched filter '${only}'"
  exit 1
fi
if [[ $fails -eq 0 ]]; then
  echo "ALL $n SYSTEM TESTS PASSED"
  exit 0
else
  echo "$fails/$n SYSTEM TESTS FAILED"
  exit 1
fi
