#!/usr/bin/env bash
# sync-plugin.sh — mirror canonical sources into the Claude Code and Codex
# distributable plugins as PURE BYTE COPIES.
#
#   sync-plugin.sh          → copy canonical → plugin tree, prune orphans
#   sync-plugin.sh --check  → verify byte-parity, no writes (CI gate)
#
# NEVER transform contents while mirroring — a transformed mirror diverges from
# canonical and the divergence hides until an install breaks (the forge lesson).
# Canonical sources: .claude/commands/**, .claude/skills/anvil/**, scripts/, templates/.
# Both plugins resolve tools and references from their loaded skills/anvil/SKILL.md.
set -uo pipefail
export LC_ALL=C

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT" || exit 2
CHECK=0
[[ "${1:-}" == "--check" ]] && CHECK=1

# --- build the src|dst mapping ---------------------------------------------
pairs=()
targets=(claude-plugin plugins/anvil)
manifests=(claude-plugin/.claude-plugin/plugin.json plugins/anvil/.codex-plugin/plugin.json)
add() {
  local target
  for target in "${targets[@]}"; do pairs+=("$1|$target/$2"); done
}

[[ -f .claude/commands/anvil.md ]] && add ".claude/commands/anvil.md" "commands/anvil.md"
for f in .claude/commands/anvil/*.md; do
  [[ -f "$f" ]] && add "$f" "commands/anvil/$(basename "$f")"
done
while IFS= read -r f; do
  add "$f" "${f#.claude/}"
done < <(find .claude/skills/anvil -type f | sort)
for s in anvil.py anvil_board.py anvil_em.py anvil_emc.py anvil_fields.py anvil_layout.py anvil_netlist.py anvil_pcb.py anvil_pdn.py anvil_plots.py anvil_report.py anvil_rules.py anvil_schematic.py anvil_si.py anvil_thermal.py jev_triage.py score-anvil.sh doctor.sh doctor.cmd validate-handoff.sh; do
  add "scripts/$s" "skills/anvil/scripts/$s"
done
while IFS= read -r f; do
  add "$f" "skills/anvil/$f"
done < <(find templates -type f | sort)
add LICENSE LICENSE

# --- expected destination set (for orphan detection) ------------------------
expected() {
  local p
  for p in "${pairs[@]}"; do echo "${p#*|}"; done
  printf '%s\n' "${manifests[@]}"
}

actual() {
  local target
  for target in "${targets[@]}"; do
    [[ ! -d "$target" ]] || find "$target" -type f | sort
  done
}

# --- check mode --------------------------------------------------------------
if [[ $CHECK -eq 1 ]]; then
  bad=0
  for p in "${pairs[@]}"; do
    src="${p%%|*}"; dst="${p#*|}"
    if [[ ! -f "$dst" ]]; then echo "missing in plugin: $dst" >&2; bad=$((bad + 1))
    elif ! cmp -s "$src" "$dst"; then echo "diverged: $dst != $src" >&2; bad=$((bad + 1)); fi
  done
  while IFS= read -r f; do
    expected | grep -qxF "$f" || { echo "orphan in plugin (no canonical source): $f" >&2; bad=$((bad + 1)); }
  done < <(actual)
  for manifest in "${manifests[@]}"; do
    [[ -f "$manifest" ]] || { echo "missing $manifest" >&2; bad=$((bad + 1)); }
  done
  if [[ $bad -eq 0 ]]; then echo "PLUGIN_PARITY: OK"; exit 0
  else echo "PLUGIN_PARITY: DIVERGED ($bad)"; exit 1; fi
fi

# --- sync mode ---------------------------------------------------------------
n=0
for p in "${pairs[@]}"; do
  src="${p%%|*}"; dst="${p#*|}"
  [[ -f "$src" ]] || { echo "sync-plugin: missing canonical source $src" >&2; exit 2; }
  mkdir -p "$(dirname "$dst")"
  cp -f "$src" "$dst"
  n=$((n + 1))
done
# prune orphans (stale copies of deleted canonical files)
while IFS= read -r f; do
  if ! expected | grep -qxF "$f"; then
    rm -f "$f"
    echo "pruned orphan: $f" >&2
  fi
done < <(actual)
echo "PLUGIN_SYNC: $n files"
