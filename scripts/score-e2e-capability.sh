#!/usr/bin/env bash
# score-e2e-capability.sh — end-to-end PRODUCT-capability coverage of the anvil harness.
#
# The harness today builds boards (requirements → fab-ready PCB). The target is a harness that
# builds PRODUCTS: electronics + mechanical enclosure/frame + COTS module integration + wiring
# harness + product-level BOM + assembly package — everything needed to assemble the final unit
# (exemplar: a rugged FPV drone).
#
# One row per capability. A row passes only if its check exits 0. Grep rows verify wiring
# (protocol exists, phase gated, dispatch present); executable-test rows are the teeth.
#
# Emits:  E2E_CAPABILITY: N/M   and   E2E_SCORE: 0.NN   (stdout)
#         per-row PASS/FAIL → stderr
#
# FROZEN SCORER: the improvement loop's Scope must EXCLUDE this file (and this file only).
# Editing the scorer to make rows pass is the one move the loop is never allowed.

set -u
cd "$(dirname "$0")/.." || exit 2

PASS=0; TOTAL=0
row() { # id  description  cmd...
  local id="$1" desc="$2"; shift 2
  TOTAL=$((TOTAL+1))
  if "$@" >/dev/null 2>&1; then
    PASS=$((PASS+1)); printf 'PASS  %-8s %s\n' "$id" "$desc" >&2
  else
    printf 'FAIL  %-8s %s\n' "$id" "$desc" >&2
  fi
}
g()  { grep -qiE "$1" "$2" 2>/dev/null; }                 # grep pattern in file (file may not exist)
d()  { grep -qE "^\s*$1\)" scripts/score-anvil.sh; }       # dispatch entry in score-anvil.sh

REF=".claude/skills/anvil/references"
BUILD=".claude/commands/anvil/build.md"

# ---- CORE — electronics pipeline (the existing strength; regression guard) ------------------
row CORE-1 "electrical gates wired (erc + drc dispatch)" \
  bash -c 'grep -qE "^\s*erc\)" scripts/score-anvil.sh && grep -qE "^\s*drc\)" scripts/score-anvil.sh'
row CORE-2 "sim + bom-cost gates wired" \
  bash -c 'grep -qE "^\s*sim\)" scripts/score-anvil.sh && grep -qE "^\s*bom-cost\)" scripts/score-anvil.sh'
row CORE-3 "score self-test green (tests/score.test.sh)" bash tests/score.test.sh
row CORE-4 "build: phase-gated electronics pipeline (ERC=0 … DRC=0)" g 'Phase 7 — PCB layout' "$BUILD"
row CORE-5 "doctor: electronics toolchain (kicad-cli, ngspice)" \
  bash -c 'grep -qi kicad scripts/doctor.sh && grep -qi ngspice scripts/doctor.sh'
row CORE-6 "HRS protocol: measurability contract" g 'measurability' "$REF/hardware-requirements-protocol.md"

# ---- MECH — mechanical design pipeline (enclosure / frame as code) --------------------------
row MECH-1 "mechanical protocol: CAD-as-code contract" g 'cadquery|build123d|cad-as-code' "$REF/mechanical-protocol.md"
row MECH-2 "mesh gate wired (manifold/watertight STL)" d mesh
row MECH-3 "mesh gate test green" bash tests/mech.test.sh mesh
row MECH-4 "fit gate wired (board+components vs cavity clearance)" d fit
row MECH-5 "fit gate test green" bash tests/mech.test.sh fit
row MECH-6 "mass gate wired (mass properties vs budget)" d mass
row MECH-7 "mass gate test green" bash tests/mech.test.sh mass
row MECH-8 "printability/mfg gate wired (slice or mech-dfm)" \
  bash -c 'grep -qE "^\s*(slice|mech-dfm)\)" scripts/score-anvil.sh'
row MECH-9 "doctor: mechanical toolchain checks" g 'cadquery|build123d|trimesh|openscad|prusaslicer' scripts/doctor.sh

# ---- SYS — system integration (COTS modules, wiring, product BOM, budgets) ------------------
row SYS-1 "system protocol: product decomposition + ICD" g 'interface control|ICD' "$REF/system-protocol.md"
row SYS-2 "COTS module selection protocol (datasheet-anchored, availability)" g 'COTS|module catalog' "$REF/cots-protocol.md"
row SYS-3 "wiring-harness protocol (from-to, connector mates, AWG vs current)" g 'from-to|awg|harness table' "$REF/harness-protocol.md"
row SYS-4 "pinout-consistency gate wired+tested (harness ↔ netlist/ICD)" \
  bash -c 'grep -qE "^\s*pinout\)" scripts/score-anvil.sh && bash tests/system.test.sh pinout'
row SYS-5 "product-BOM rollup gate wired+tested (PCB+COTS+mech+fasteners+wire)" \
  bash -c 'grep -qE "^\s*product-bom\)" scripts/score-anvil.sh && bash tests/system.test.sh product-bom'
row SYS-6 "system-budget gate wired+tested (mass/power/endurance close)" \
  bash -c 'grep -qE "^\s*sys-budget\)" scripts/score-anvil.sh && bash tests/system.test.sh sys-budget'

# ---- PROD — product pipeline, docs, exemplar ------------------------------------------------
row PROD-1 "build: mechanical phase gated (mesh/fit in pipeline)" g 'watertight|manifold|cavity|fit gate' "$BUILD"
row PROD-2 "build: integration phases (wiring harness, assembly, budgets)" g 'wiring harness|assembly plan|system budget' "$BUILD"
row PROD-3 "metrics: product dimensions (mechanical/integration/system)" \
  bash -c 'grep -qiE "^\|\s*.?(mechanical|integration|system).?\s*\|" .claude/skills/anvil/references/metrics.md'
row PROD-4 "assembly protocol (technician-followable, exploded views VIEWED)" g 'exploded|technician' "$REF/assembly-protocol.md"
row PROD-5 "requirements: rugged/environment domains (IP rating, vibration, shock)" \
  g 'IP ?(rating|5[45]|6[57])|vibration|shock' "$REF/hardware-requirements-protocol.md"
row PROD-6 "product exemplar spec exists (FPV-drone class)" bash -c 'ls evals/product/*.spec.yaml'
row PROD-7 "template layout: product tree (mech/, harness/, assembly/)" g 'mech/|assembly/' templates/anvil-project/README.md
row PROD-8 "plugin mirror parity" bash scripts/sync-plugin.sh --check
row PROD-9 "README declares end-to-end product scope (enclosure et al.)" g 'enclosure' README.md

# ---- emit -----------------------------------------------------------------------------------
SCORE=$(awk -v p="$PASS" -v t="$TOTAL" 'BEGIN{printf "%.2f", (t>0)? p/t : 0}')
echo "E2E_CAPABILITY: $PASS/$TOTAL"
echo "E2E_SCORE: $SCORE"
exit 0
