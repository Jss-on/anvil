# Changelog

Native Codex packaging is included in 0.5.0: an installable `$anvil` skill, local marketplace,
shared workflow routing, bundled tools/templates, and parity checks for both host packages.

## 0.5.0 ? 2026-09-14

- Implement the lifecycle research: all 75 checklist items, 19 early applicability checkpoints, G0?G7 plus sustaining, and a new lifecycle command. Distinguish PCB, assembly, product-build, design, production and market readiness.
- Replace score-derived release verdicts with required checks, exact requirement traces, method checks, review/NA dispositions, hashed release manifests and validated handoffs.
- Replace duplicated Bash/Node parsers with one Python standard-library seam. Fail closed on stale/invalid KiCad reports, failed or skipped simulations, missing corners, malformed numbers, mixed currencies, source drift and incorrect wiring. Correct curved outline bounds and degenerate mesh checks.
- Add firmware/build record, factory traceability/yield, full cost-model checks and templates; concurrent firmware, manufacturing, sector/market, commercial, support and retirement workflows.
- Bundle scripts, Windows doctor shim and all templates; align package versions and add executable regression/native-tool/installation checks. Remove unsupported manufacturer presets and universal engineering thresholds.
- Breaking migration: release claims require anvil-project.json, structured requirements, explicit evidence receipts and gate. Legacy score ledgers and SKIP_NGSPICE cannot authorize release; sim rows need circuit, product BOM needs pinned source joins, and ICDs need exact endpoints and qualified ratings. See README.

## 0.4.0 — 2026-08-26

Industry-process deepening — the protocols absorb the standard PCB design discipline (IPC
standards hierarchy, class election, grounding/PDN doctrine, obsolescence reality) from a
comprehensive process research pass.

- **New reference `standards.md`** — the numbers annex all protocols cite: IPC registry with
  current revisions (2221C, A-610J, 6012F, J-STD-020F…), **Class 1/2/3 gradient** (plating
  20/25 µm, barrel fill 50/75 %, annular-ring tolerance), IPC-2152 ampacity anchors (+ internal
  50–70 % derate), IPC-2221 Table 6-1 creepage/clearance anchors + >500 V formula + IEC
  60664-1/62368-1 override rule, IPC-7351 density levels, full MSL floor-life ladder,
  RoHS 3 / REACH-SVHC / UL 796 / 94V-0, and the obsolescence numbers (>50 % of EOLs ship
  with no PCN; LTB ≈ 6 months). Provenance caveat: secondary-source transcriptions — verify
  against the purchased standard for Class 3 / safety-critical.
- **IPC class is now a first-class early decision**: elected in the HRS manufacturing domain,
  fixed in the Phase 1 charter alongside requirements + stackup (the three early
  irreversibles), carried as `ipc_class` in `build-spec.yaml`, echoed on the DFM report and
  RFQs with the standard revision.
- **Schematic protocol**: sheet/naming conventions (hierarchy by function, IEEE 315/ASME
  Y14.44 refdes, scoped net labels, power ports, AGND/DGND single join drawn); IPC-7351
  Level-B footprint discipline (datasheet-verified, project-local pinned libs); quiet-
  obsolescence rules (active refresh checks, PCN/LTB = drop-everything issue, FFF alternate
  noted per keystone part); SWD/JTAG + boundary-scan row in the design review.
- **Layout protocol**: grounding doctrine section (one continuous plane, splits only with
  simulated justification, no routing over plane gaps, loop-area discipline, converter
  AGND/DGND per datasheet); stackup physics (thick 4-layer core carries no HF decoupling —
  MLCCs do; 6-layer thin PWR–GND pair; fab's real dielectrics for impedance); decoupling as
  loop inductance (≤ 2 mm, ~0.5–1 nH per via) + PDN target-Z formula; assembly-orientation +
  fiducial placement rules; thermal-via farm spec (Ø 0.2–0.33 mm @ 1.0–1.2 mm, must land on
  real copper); skew serpentines at the mismatch source; teardrops + mask-sliver rules.
- **Fab protocol**: DFM report grows IPC-class statement, reasoned surface-finish selection
  (HASL/ENIG/OSP/imm-Ag trade table, fine-pitch forces ENIG-class), symmetric-panel note,
  segmented-stencil rule for uncapped via farms, MSL ≥ 3 disclosure, declared-market
  compliance rows (RoHS/UL); IPC-2581 offered alongside RS-274X; PCN/LTB handling on the
  catalog refresh event.
- `build`: charter fixes the three early irreversibles; TEST-PLAN ordered up the DFT ladder
  (structural → boundary-scan → functional); DFM-report scope widened. `requirements`:
  class election in the manufacturing elicitation domain. Metrics: manufacturing/testability
  "owns" lines updated. `buck-3v3` exemplar spec carries `ipc_class: 2`.

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
