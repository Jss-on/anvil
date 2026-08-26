#!/usr/bin/env bash
# doctor.sh — anvil toolchain check. Prescribes, never installs.
#   usage: doctor.sh [--require-build] [--require-product]
#   FOUND/MISSING line per tool; last line "DOCTOR: READY" (exit 0) or
#   "DOCTOR: BLOCKED <n> missing" (exit 1). Without --require-build only CORE blocks.
#   --require-product additionally blocks on the mechanical/product toolchain
#   (CAD-as-code kernel) — end-to-end product builds check this at Phase 0.
set -uo pipefail
export LC_ALL=C

REQUIRE_BUILD=0
REQUIRE_PRODUCT=0
for a in "$@"; do
  [[ "$a" == "--require-build" ]] && REQUIRE_BUILD=1
  [[ "$a" == "--require-product" ]] && { REQUIRE_BUILD=1; REQUIRE_PRODUCT=1; }
done

core_missing=0
build_missing=0
product_missing=0

found()   { echo "FOUND   $1 $2"; }
missing() { echo "MISSING $1 — $2"; }

# --- CORE ------------------------------------------------------------------
if command -v git >/dev/null 2>&1; then found git "$(git --version | head -1)"; else missing git "install git"; core_missing=$((core_missing+1)); fi
if command -v node >/dev/null 2>&1; then found node "$(node --version)"; else missing node "install node (JSON parsing seam)"; core_missing=$((core_missing+1)); fi

# --- BUILD -----------------------------------------------------------------
KC=""
if [[ -n "${KICAD_CLI:-}" && -x "${KICAD_CLI:-}" ]]; then KC="$KICAD_CLI"
elif command -v kicad-cli >/dev/null 2>&1; then KC="kicad-cli"
else
  for g in "/c/Program Files/KiCad/"*/bin/kicad-cli.exe; do
    [[ -x "$g" ]] && { KC="$g"; break; }
  done
fi
if [[ -n "$KC" ]]; then
  ver="$("$KC" version 2>/dev/null | head -1)"
  found kicad-cli "${ver:-$KC}"
  [[ "$KC" != "kicad-cli" ]] && echo "        off-PATH — add:  export KICAD_CLI=\"$KC\"  (or add its bin/ to PATH)"
else
  missing kicad-cli "winget install KiCad.KiCad"
  build_missing=$((build_missing+1))
fi

if command -v ngspice >/dev/null 2>&1; then
  found ngspice "$(ngspice --version 2>/dev/null | head -1)"
else
  missing ngspice "standalone CLI from ngspice.sourceforge.io → add bin/ to PATH (KiCad's bundled DLL is not the batch CLI)"
  build_missing=$((build_missing+1))
fi

PY=""
if command -v py >/dev/null 2>&1 && py -3 --version >/dev/null 2>&1; then PY="py -3"
elif command -v uv >/dev/null 2>&1; then PY="uv run python"
fi
if [[ -n "$PY" ]]; then
  found python "$($PY --version 2>&1 | head -1) (via '$PY')"
  if $PY -c "import skidl" >/dev/null 2>&1; then found skidl "importable"; else missing skidl "uv pip install skidl (netlist-as-code default flow)"; build_missing=$((build_missing+1)); fi
  if $PY -c "import kiutils" >/dev/null 2>&1; then found kiutils "importable"; else missing kiutils "uv pip install kiutils (board-file surgery)"; build_missing=$((build_missing+1)); fi
else
  missing python "py -3 or uv — NEVER the Microsoft Store stub"
  build_missing=$((build_missing+3)) # python + skidl + kiutils unverifiable
fi

# --- PRODUCT (mechanical / end-to-end builds) ------------------------------
if [[ -n "$PY" ]]; then
  if $PY -c "import build123d" >/dev/null 2>&1; then
    found build123d "importable (CAD-as-code kernel)"
  elif $PY -c "import cadquery" >/dev/null 2>&1; then
    found cadquery "importable (CAD-as-code kernel, build123d also accepted)"
  else
    missing build123d "uv pip install build123d — CAD-as-code kernel (cadquery also accepted); mesh gate itself runs on node"
    product_missing=$((product_missing+1))
  fi
  if $PY -c "import trimesh" >/dev/null 2>&1; then found trimesh "importable (boolean interference helper)"; else echo "OPTIONAL trimesh — uv pip install trimesh; CAD-side interference/measures helper"; fi
else
  missing build123d "needs python first (py -3 / uv)"
  product_missing=$((product_missing+1))
fi
if command -v prusa-slicer >/dev/null 2>&1 || [[ -n "${PRUSA_SLICER:-}" && -x "${PRUSA_SLICER:-}" ]]; then
  found prusa-slicer "(mech-dfm slicer seam armed)"
else
  echo "OPTIONAL prusa-slicer — PrusaSlicer CLI (or set PRUSA_SLICER); mech-dfm slicer seam disabled"
fi
if command -v openscad >/dev/null 2>&1; then found openscad "(scad sources accepted)"; else echo "OPTIONAL openscad — only needed for .scad sources"; fi

# --- OPTIONAL --------------------------------------------------------------
if command -v java >/dev/null 2>&1; then found java "(freerouting seam available)"; else echo "OPTIONAL freerouting — needs java; autoroute seam disabled"; fi

# --- verdict ---------------------------------------------------------------
total_missing=$core_missing
[[ $REQUIRE_BUILD -eq 1 ]] && total_missing=$((core_missing + build_missing))
[[ $REQUIRE_PRODUCT -eq 1 ]] && total_missing=$((total_missing + product_missing))
if [[ $total_missing -eq 0 ]]; then
  echo "DOCTOR: READY"
  exit 0
else
  echo "DOCTOR: BLOCKED $total_missing missing"
  exit 1
fi
