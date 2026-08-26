# Changelog

## 0.3.0 — 2026-08-26

End-to-end product capability — anvil builds assemblable units, not just boards. A rugged FPV
drone's frame, COTS modules, wiring, budgets, and assembly kit are now first-class, gated
deliverables (E2E capability 7/30 → 30/30 by `scripts/score-e2e-capability.sh`).

- **Five new protocol contracts** (`skills/anvil/references/`): `system-protocol.md`
  (product decomposition, ICD, system goldens, budgets), `cots-protocol.md` (pinned module
  catalog, datasheet-anchored selection), `mechanical-protocol.md` (CAD-as-code —
  build123d/CadQuery, kernel-emitted `measures.json`, process floors, rugged rules),
  `harness-protocol.md` (wire table, ampacity floor, mates), `assembly-protocol.md`
  (technician-followable steps, integration ladder, QC).
- **Seven new mechanical-truth gates** in `score-anvil.sh`, all fixture-tested
  (`tests/mech.test.sh`, `tests/system.test.sh`): `mesh` (STL watertight/manifold defect
  count), `fit` / `mass` / `mech-dfm` (kernel measures vs assertion classes; optional
  `PRUSA_SLICER` slice-clean seam), `pinout` (harness ↔ ICD + AWG ampacity), `product-bom`
  (full-unit cost+mass rollup, incomplete line = hard error), `sys-budget`
  (demand ≤ capability × derate).
- **Scoring contract**: product dims `mechanical` 0.20 · `integration` 0.15 · `system` 0.15,
  renormalized, must-pass in `verdict`; product optimization metrics `product_cost`,
  `auw_mass`, `worst_budget_margin`.
- **`build` product track**: P1 system architecture (extends P4) → P2 mechanical capture →
  P3 interconnect → P4 product roll-up + assembly package; `doctor.sh --require-product`
  (build123d/cadquery kernel tier, trimesh/prusa-slicer/openscad optional).
- **Requirements protocol**: rugged/environment domains (IP class, vibration profile,
  shock/drop) + product must-be rows + `product:` spec block.
- **Reference product spec** `evals/product/fpv-drone.spec.yaml`; project template grows the
  product tree (`system/ cots/ mech/ harness/ assembly/ product-bom.csv`).
- New harness self-gate: `scripts/score-e2e-capability.sh` (frozen scorer, 30 rows).

## 0.2.1 — 2026-08-26

Windows entry-point fix (found by the first fresh-clone user).

- **`scripts\doctor.cmd`** — from PowerShell/cmd, bare `bash` resolves to the WSL relay stub in
  System32 and dies with `execvpe(/bin/bash) failed` when no distro is installed. The shim
  locates Git for Windows' bash (ANVIL_BASH override → `where git` → standard install paths) and
  never falls back to the stub.
- `.gitattributes`: `*.cmd eol=crlf` (batch files need CRLF); README quick start + toolchain.md
  document the PowerShell path.

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
