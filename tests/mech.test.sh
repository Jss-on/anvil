#!/usr/bin/env bash
# mech.test.sh — mechanical-gate self-test (mesh / fit / mass / mech-dfm).
# Usage: mech.test.sh [gate] — run every case, or only the named gate's cases.
# Zero matched cases for a filter is a FAILURE (a gate with no tests is untested).
set -uo pipefail
export LC_ALL=C

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCORE="$ROOT/scripts/score-anvil.sh"
FIX="$ROOT/tests/fixtures/mech"
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

# --- mesh: watertight/manifold STL analysis ---------------------------------
if want mesh; then
  assert_eq "mesh: watertight cube = 0 defects" "MESH_DEFECTS: 0" \
    "$(bash "$SCORE" mesh "$FIX/cube-good.stl" 2>/dev/null)"
  assert_eq "mesh: open top = 4 boundary edges" "MESH_DEFECTS: 4" \
    "$(bash "$SCORE" mesh "$FIX/cube-open.stl" 2>/dev/null)"
fi

# --- fit: measures.json vs fit-class assertions ------------------------------
if want fit; then
  assert_eq "fit: interference/clearance/boss all green" "FIT_PASS: 3/3" \
    "$(bash "$SCORE" fit "$FIX/encl" 2>/dev/null)"
fi

# --- mass: measures.json vs mass-class assertions ----------------------------
if want mass; then
  assert_eq "mass: 36.2g within 20..38 budget rows" "MASS_PASS: 2/2" \
    "$(bash "$SCORE" mass "$FIX/encl" 2>/dev/null)"
fi

# --- mech-dfm: wall green, overhang 62° > 55° limit red ----------------------
if want mech-dfm; then
  assert_eq "mech-dfm: catches 62deg overhang over 55 limit" "DFM_PASS: 1/2" \
    "$(bash "$SCORE" mech-dfm "$FIX/encl" 2>/dev/null)"
fi

echo
if [[ $n -eq 0 ]]; then
  echo "NO MECH CASES matched filter '${only}'"
  exit 1
fi
if [[ $fails -eq 0 ]]; then
  echo "ALL $n MECH TESTS PASSED"
  exit 0
else
  echo "$fails/$n MECH TESTS FAILED"
  exit 1
fi
