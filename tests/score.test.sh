#!/usr/bin/env bash
# score.test.sh — mechanical self-test of the anvil scoring seam.
# The harness that preaches gates has its own gate. Runs on bash + node only
# (kicad-cli / ngspice paths are exercised in parse-only mode).
set -uo pipefail
export LC_ALL=C

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCORE="$ROOT/scripts/score-anvil.sh"
HANDOFF="$ROOT/scripts/validate-handoff.sh"
FIX="$ROOT/tests/fixtures"

fails=0
n=0

assert_eq() { # name expected actual
  n=$((n + 1))
  if [[ "$2" == "$3" ]]; then
    echo "ok $n — $1"
  else
    echo "FAIL $n — $1: expected [$2] got [$3]"
    fails=$((fails + 1))
  fi
}

# 1. weighted pass-rate: E=1, S=0.5, L=1, D=0 over ran dims (.30+.25+.20+.10)
#    → (.30 + .125 + .20 + 0)/.85 = 0.7353 → 0.74
assert_eq "pass-rate weighted" "PASS_RATE: 0.74" \
  "$(bash "$SCORE" pass-rate "$FIX/sample-results.tsv" 2>/dev/null)"

# 2. electrical gate: raw 0.65 but a red electrical row caps at 0.50
assert_eq "electrical gate cap" "PASS_RATE: 0.50" \
  "$(bash "$SCORE" pass-rate "$FIX/gate-results.tsv" 2>/dev/null)"

# 3. gate cap overridable via env
assert_eq "gate cap env override" "PASS_RATE: 0.25" \
  "$(ELECTRICAL_GATE_CAP=0.25 bash "$SCORE" pass-rate "$FIX/gate-results.tsv" 2>/dev/null)"

# 4. coverage: HRS has HR-1..HR-3, rows trace HR-1,HR-2 → 0.67
assert_eq "coverage RTM" "REQ_COVERAGE: 0.67" \
  "$(bash "$SCORE" coverage "$FIX/cov-results.tsv" "$FIX/cov-hrs.md" 2>/dev/null)"

# 5. sim assertions, parse-only (canned ngspice log): 3.28 within 3.3±3% ✓,
#    ripple 12mV ≤ 30mV ✓, eff 0.82 ≥ 0.85 ✗ → 2/3
assert_eq "sim assertion parse" "SIM_PASS: 2/3" \
  "$(SKIP_NGSPICE=1 bash "$SCORE" sim "$FIX/sim" 2>/dev/null)"

# 6. BOM cost against pinned catalog: 2×0.01 + 1×0.85 = 0.87, DNP line skipped
assert_eq "bom-cost pinned join" "BOM_COST: 0.87 USD" \
  "$(bash "$SCORE" bom-cost "$FIX/bom.csv" "$FIX/parts-catalog.csv" 2>/dev/null)"

# 7. Edge.Cuts bbox area: 50 × 40 board → 2000.0 mm²
assert_eq "area bbox" "AREA_MM2: 2000.0" \
  "$(bash "$SCORE" area "$FIX/edge.kicad_pcb" 2>/dev/null)"

# 8. verdict on a red ledger → FAB_BLOCKED
assert_eq "verdict blocked" "FAB_BLOCKED" \
  "$(bash "$SCORE" verdict "$FIX/sample-results.tsv" 2>/dev/null)"

# 9. handoff validation
assert_eq "handoff valid" "HANDOFF: VALID" \
  "$(bash "$HANDOFF" "$FIX/handoff-good.json" 2>/dev/null)"
out="$(bash "$HANDOFF" "$FIX/handoff-bad.json" 2>/dev/null || true)"
case "$out" in
  "HANDOFF: INVALID"*) echo "ok $((n + 1)) — handoff invalid detected"; n=$((n + 1)) ;;
  *) echo "FAIL $((n + 1)) — handoff invalid: got [$out]"; n=$((n + 1)); fails=$((fails + 1)) ;;
esac

echo
if [[ $fails -eq 0 ]]; then
  echo "ALL $n TESTS PASSED"
  exit 0
else
  echo "$fails/$n TESTS FAILED"
  exit 1
fi
