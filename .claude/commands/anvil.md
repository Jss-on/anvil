---
name: anvil
description: "Iterate any hardware design against a mechanical metric — modify, verify (ERC/sim/DRC), keep/discard — or route a spec/goal to the right subcommand"
argument-hint: "[Metric: bom_cost|board_area|part_count|worst_case_margin|<name>] [Verify: <shell cmd>] [Direction: minimize|maximize] [Scope: <dir>] [Spec: <file>] [Goal: <text>] [Iterations: N]"
---

EXECUTE IMMEDIATELY.

The bare-loop entry point. Print the banner `[anvil] mode: classic | build | wizard`, then dispatch:

| Condition | Mode |
|---|---|
| `Metric:` or `Verify:` present | **Classic** — the metric loop below |
| `Spec:` file or free-form `Goal:` | **Build** — confirm once, then run `/anvil:build` with the same arguments |
| Nothing | **Wizard** — one AskUserQuestion batch: what design, which metric (recommend from the named set), scope dir, iteration budget → then Classic |

## Seam & reference resolution (read once)
Resolve `ANVIL_ROOT` as in SKILL.md: first existing of `${CLAUDE_PLUGIN_ROOT}/skills/anvil`,
`.claude/skills/anvil`, the directory containing this command file, else glob
`**/skills/anvil/scripts/score-anvil.sh` and take its grandparent. Every `scripts/<x>` below means
`$ANVIL_ROOT/scripts/<x>` (repo-root `scripts/` when running inside the harness repo). Run
`bash scripts/doctor.sh` first; add `--require-build` when the metric needs kicad-cli/ngspice.

## Classic — the metric loop

**Setup (iteration #0):**
1. Resolve Scope (the board directory; ask if ambiguous). Read the in-scope files + git log +
   any prior `anvil/*/iterations.tsv`.
2. Resolve the metric command:
   - Named metric → `scripts/score-anvil.sh` subcommand: `bom_cost` → `bom-cost fab/bom.csv
     catalog/parts-catalog.csv` (minimize) · `board_area` → `area pcb/*.kicad_pcb` (minimize) ·
     `part_count` → distinct BOM lines (minimize) · `worst_case_margin` → min margin from
     `sim sim/` (maximize).
   - `Verify:` → that exact shell command; it must print a number. `Direction:` sets the sign
     (default: maximize). Safety-screen the command before first run; refuse destructive ones.
3. Baseline: run the metric on the untouched design. Record. A metric that won't run is a setup
   failure — fix the seam before iterating.
4. **Hardware ratchet applies whenever the Scope contains design files** (`*.kicad_sch`,
   `*.kicad_pcb`, `sim/`): ERC = 0 ∧ DRC = 0 ∧ every `sim/assertions.tsv` row green are hard
   gates on every keep, regardless of what the metric rewards. The loop optimizes the metric
   INSIDE the gates, never through them.
5. Show the config (Scope · Metric · Direction · baseline · Iterations, default 25) and begin.

**Loop (N iterations, default 25):**
1. Review state + history + what worked/failed so far.
2. Pick ONE focused change.
3. `git commit` before verification.
4. Cheap gates first (ERC → derating → affected sims → DRC), then the metric.
5. Improved AND gates green → keep. Else → `git revert`. Crashed → fix or skip.
6. Log to `anvil/anvil-{YYMMDD}-{HHMM}/iterations.tsv`
   (`n timestamp change metric gates verdict notes`) + `score-log.tsv`.
7. Plateau: 5 consecutive non-improvements → stop, report `PLATEAU`.

**Finish:** report `IMPROVED <baseline> → <final>` | `PLATEAU` | `NO_GAIN`; write `handoff.json`
(command, verdict, metric, baseline, final, results_tsv). Safety invariants from SKILL.md hold
throughout — never order parts, never submit fab jobs, HV-register rows untouchable.
