---
name: anvil:improve
description: "Optimize hardware cost, area, mass, part count, or worst-case margin while preserving requirements and release checks"
argument-hint: "Metric: bom_cost|board_area|part_count|worst_case_margin|product_cost|auw_mass|worst_budget_margin [Scope: <project>] [Floor: <margin floor>] [Iterations: N]"
---

EXECUTE IMMEDIATELY.

The **optimizer** of the hardware pipeline — the purest autoresearch loop. Takes a design that
already passes acceptance and ratchets ONE declared metric, keeping only changes that improve it
**without breaking any hard gate**. This is where compounding gains live: a part substitution here,
a value re-spec there, a layer dropped — each verified mechanically, each reverted on regression.

## Seam & reference resolution (read once)
Resolve `ANVIL_ROOT` as in SKILL.md. Run `bash scripts/doctor.sh --require-build` at start —
optimization without verification is vandalism.

## Parse Arguments
- `Metric:` — REQUIRED, one of:
  - `bom_cost` — minimize `scripts/score-anvil.sh bom-cost fab/bom.csv catalog/parts-catalog.csv`
    (joins the **pinned catalog snapshot only** — never live prices mid-loop).
  - `board_area` — minimize `scripts/score-anvil.sh area pcb/<board>.kicad_pcb` (Edge.Cuts bbox mm²).
  - `part_count` — minimize distinct BOM lines (assembly cost proxy).
  - `worst_case_margin` — maximize the MINIMUM margin across all sim assertions at corners
    (from `scripts/score-anvil.sh sim sim/` margin output). Maximin, not average — averaging lets
    one spec go to the cliff edge while another coasts.
  - `product_cost` — minimize the source-joined product BOM total; keep the full commercial model current.
  - `auw_mass` — minimize the product BOM mass rollup while preserving capability and mechanical requirements.
  - `worst_budget_margin` — maximize the minimum normalized system-budget margin; keep units and source calculations explicit.
- `Scope:` — the board directory. Default: the only board in the repo; ask if ambiguous.
- `Floor:` — margin floor as a fraction of baseline (default 0.80): no change may cut ANY
  assertion's margin below `floor × baseline_margin`, even while optimizing cost/area. Prevents
  the classic Goodhart failure — trading silent robustness for visible dollars.
- `Iterations:` — default 20. `--evals`, `--evals-interval N`.

## The Ratchet (hard gates — non-negotiable every iteration)
1. `ERC_VIOLATIONS: 0` and `DRC_VIOLATIONS: 0` (incl. fab rule deck + schematic parity).
2. Every `sim/assertions.tsv` row still PASSES at its declared corners.
3. No assertion margin below the Floor.
4. Derating stays within the project's approved, source-backed limits under its stated conditions.
5. Safety/risk controls and compliance assumptions retain the required responsible review.
6. Regenerate the release manifest after a retained change; run the applicable automatic checks
   with `record` and renew affected review evidence. Earlier G3+ receipts are stale after an input
   change. A metric gain never substitutes for the cumulative `gate` result.
A change failing ANY gate is reverted, whatever the metric says.

Also append every iteration to the project ledger: `anvil.py log <scope> iteration phase=improve change=...
metric=<metric> value=<after> checks=erc,drc,sim,rules result=keep|discard rules=<TAG-nnn> note=...`, and cite
the rulebook id that motivated each mutation. `report <scope>` turns the ledger into the audit/paper tables.

## Run directory
`anvil/improve-{YYMMDD}-{HHMM}/`: `improve-results.tsv`
(`n change metric_before metric_after gates verdict notes`), `score-log.tsv`, `handoff.json`.

## Phase 1 — Baseline (iteration #0)
Run the FULL gate suite + the metric on the untouched design. Record every assertion's baseline
margin (the Floor references these). A design that doesn't pass its own gates at baseline →
STOP, report `IMPROVE_BLOCKED: baseline red`, recommend `/anvil:build` convergence or `fix` first.
Never optimize a broken design.

## Phase 2 — The mutation menu (pick ONE per iteration)
Ordered by expected value-per-verification-cost:
1. **Part substitution** — same function, cheaper/smaller/better-stocked MPN from the catalog;
   re-check derating + affected sims. (bom_cost, part_count)
2. **Value re-spec** — component value changes that hold specs with margin to spare (e.g. smaller
   inductor at acceptable ripple; re-run the affected assertion at corners). (bom_cost, board_area)
3. **Consolidation** — merge duplicate values/packages into one BOM line; delete
   provably-redundant parts (the sim must prove redundancy, not intuition). (part_count, bom_cost)
4. **Placement/route compaction** — tighten placement (`design/placement.tsv` + `place`), shrink outline;
   full DRC + renders VIEWED + every released board analysis (`layout`, `si`, `pdn`, `thermal`, `emc`;
   `em` when an RF path moved) after every layout change: a smaller board that loses impedance,
   return path, spacing, PDN or thermal margin is discarded. (board_area)
5. **Margin hunting** — re-tune compensation/filtering to lift the weakest assertion's corner
   margin. (worst_case_margin)
6. **Layer/stackup change** — LAST: cheapest per-board but most disruptive; full re-route + full
   suite. (bom_cost at volume)
Never mutate: connector pinouts, mounting geometry, or any interface an HRS `HR-n` pins — those
are contracts, not fat.

## Phase 3 — The loop
Review → pick from the menu (informed by what worked/failed in `improve-results.tsv`) → ONE change
→ **cheap checks first** (ERC → derating → affected sims → DRC), full suite before any
keep → metric → keep if improved AND checks pass, else restore only the agent's change → log.
Preserve unrelated user changes; commit according to session authorization and repository rules.
Do not automatically create or push a remote repository. Plateau rule: 5
consecutive no-improvement iterations → stop, report `PLATEAU` with the best kept state.

## Verdict & handoff
`IMPROVED: <metric> <baseline> → <final> (<n> kept / <m> tried)` or `PLATEAU` or `NO_GAIN`.
Write the optimization details to the run report. Run `handoff <scope> --write improve`, then
`validate-handoff.sh <scope>/handoff.json` before `--chain evals`. The handoff carries the actual
current lifecycle verdict and blockers; `IMPROVED` is a metric result, not release authorization.
