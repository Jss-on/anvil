---
name: anvil:evals
description: "Analyze anvil iteration results: trends, plateaus, regressions, margin + cost trajectories, dimension breakdown, recommendations"
argument-hint: "[Run: <anvil/run-dir|latest>] [--compare <run-dir>]"
---

EXECUTE IMMEDIATELY.

The **analyst** of the pipeline. Reads a run's TSV ledgers and turns them into decisions: is the
loop still earning its iterations, which dimension is the bottleneck, did any margin quietly erode,
should the next run change strategy. Never modifies the design; produces analysis + a
recommendation block.

## Parse Arguments
- `Run:` — an `anvil/<cmd>-<ts>/` directory or `latest` (default: most recent by mtime).
- `--compare <run-dir>` — diff two runs (e.g. before/after an `improve` engagement).

## Inputs (whichever exist in the run dir / board dir)
`anvil-results.tsv` · `iterations.tsv` · `improve-results.tsv` · `score-log.tsv` ·
`sim/assertions.tsv` margins · `handoff.json`.

## Analysis (all mechanical, computed from the TSVs — never impressions)
1. **Trajectory** — pass-rate (or metric) per iteration; mark kept vs reverted; compute
   improvement-per-iteration over the last 5 vs the first 5.
2. **Plateau detection** — ≥5 consecutive non-improving iterations, or improvement-per-iteration
   below 10 % of the early rate → flag with the iteration number where it set in.
3. **Dimension breakdown** — per-dimension score from the last `anvil-results.tsv`; name the
   bottleneck dimension and its red rows.
4. **Margin trajectory** (hardware-specific) — for every sim assertion, margin at baseline vs now;
   flag ANY margin that shrank >20 % even while its row stayed green — the silent-erosion signal
   a pass/fail ledger hides.
5. **Cost/area trajectory** — when `improve` ran: metric per kept iteration, cumulative gain,
   gain per mutation class (which menu items actually paid).
6. **Regression audit** — any row that ever flipped green→red and when; any revert that failed to
   restore the metric.
7. **Churn** — files touched per kept change; high churn + flat metric = thrashing signal.

## Output
`anvil/evals-{YYMMDD}-{HHMM}/report.md`:
- Verdict line first: `CONTINUE | PLATEAU | REGRESSED | CONVERGED` + one sentence why.
- The seven analyses above, tables not prose where numbers carry it.
- **Recommendations:** next dimension to attack, mutation classes to prefer/retire, whether to
  re-run `build` convergence or hand to `improve`, iteration budget suggestion for the next run.
- `handoff.json` with the verdict + bottleneck dimension for chaining.
