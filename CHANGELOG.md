# Changelog

## 0.2.0 — 2026-08-26

Claude Code plugin packaging — installable in any repo.

- **Plugin tree** `claude-plugin/` (commands + skill + references + the three gate scripts at
  `skills/anvil/scripts/` so `${CLAUDE_PLUGIN_ROOT}` seam resolution works in installed repos)
  and marketplace manifest `.claude-plugin/marketplace.json` — install with
  `/plugin marketplace add Jss-on/anvil`, then install `anvil`.
- **Bare `/anvil` command** — classic metric loop (`Metric:`/`Verify:` with the hardware
  ratchet: ERC/DRC/sim gates hold whatever the metric rewards), build routing, setup wizard.
- **`scripts/sync-plugin.sh`** — canonical `.claude/` → `claude-plugin/` as pure byte copies with
  orphan pruning; `--check` mode is the parity gate (test 11, runs in CI). Mirrors are never
  transformed — divergence hides until an install breaks.

## 0.1.0 — 2026-08-26

Initial release: AutoForge's hardware sibling.

- **Core loop** ported to electronics design: modify → verify (ERC → derating → sim → DRC) → keep/discard, git as memory.
- **Six weighted acceptance dimensions** with a gating `electrical` dimension (ERC = 0 + connectivity golden cases + derating + power budget; any red row caps pass-rate at 0.50) — the hardware analog of AutoForge's `logic` gate.
- **Commands:** `/anvil:build` (8-phase gated pipeline, requirements → fab package), `/anvil:requirements` (HRS elicitation, every spec measurable), `/anvil:improve` (cost/area/margin optimization under a non-regression ratchet), `/anvil:evals` (trend analysis).
- **Mechanical gates:** `scripts/score-anvil.sh` (pass-rate · coverage · erc · drc · sim · bom-cost · area · verdict), `scripts/doctor.sh` (toolchain check), `scripts/validate-handoff.sh`.
- **References:** hardware-requirements, schematic, simulation, layout, fab protocols + metrics contract + toolchain guide.
- **Eval:** `evals/hardware/buck-3v3.spec.yaml` (USB-powered 5V→3.3V/1A buck, JLCPCB 2-layer).
- **Templates:** project scaffold, sim assertions example, JLCPCB 2-layer `.kicad_dru` rule deck.
- **Safety:** ordering parts / submitting fab jobs always human-gated; HV register (nets > 30 V) adds IPC-2221 creepage/clearance rows requiring human review.
