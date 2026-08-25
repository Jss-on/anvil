---
name: anvil
description: "Autonomous electronics-design iteration: modify, verify (ERC/sim/DRC), keep/discard against hardware-correct metrics — requirements to fab-ready PCB"
version: 0.2.1
---

# Anvil — Autonomous Goal-directed Hardware Iteration

AutoForge's hardware sibling. Same loop discipline — one metric, constrained scope, fast mechanical
verification, automatic rollback, git as memory — with electronics-correct gates: ERC/DRC violation
counts from `kicad-cli` JSON, ngspice `.measure` assertions against HRS limits at worst-case corners,
derating tables, pinned-catalog BOM cost, Edge.Cuts board area.

## Safety Invariants (all subcommands)

- **Never order parts, submit fabrication/assembly jobs, or spend money** without explicit user
  approval. `FAB_READY` is a verdict, not a purchase order. Quoting APIs may be read; checkout is
  human-gated, always.
- **HV register:** any net above 30 V adds IPC-2221 creepage/clearance acceptance rows that require
  human review before `FAB_READY`. Mains-connected designs additionally carry a human sign-off row
  the loop can never mark `pass` on its own.
- `build` pushes to the project's **own private output repo** as part of the standard loop (that is
  how its CI runs); everything beyond that repo is human-gated. Repo visibility is never changed.
- Bounded by default. Override with `Iterations: unlimited`.
- All results logged to `anvil/{subcommand}-{YYMMDD}-{HHMM}/`. Chain handoff via `handoff.json`.
  Evals reads `*-results.tsv`.
- **Violation counts come from tool JSON only** — the loop never self-certifies electrical or
  manufacturing cleanliness by prose.

## Dispatch (bare `/anvil`)

| Condition | Mode |
|---|---|
| `Metric:` or `Verify:` present | **Classic** — metric loop over an existing design (an `improve` alias) |
| `Spec:` file or free-form goal | Route to `build` (greenfield) — confirm once |
| Nothing | **Setup wizard** — interactive config builder |

Print a banner on every invocation: `[anvil] mode: classic | build | wizard`.

## Subcommands

| Command | Does | Default Iterations |
|---|---|---|
| `/anvil` | Bare metric loop over an existing design (`Metric:`/`Verify:`), route to `build` (`Spec:`/`Goal:`), or setup wizard | 25 |
| `/anvil:build` | Full gated pipeline: charter → feasibility → HRS → architecture + part selection → schematic (ERC=0) → simulation (spec assertions at corners) → layout (DRC=0) → fab package + docs, to passing weighted acceptance | 40 |
| `/anvil:requirements` | Hardware requirements elicitation → validated HRS (HR-n, every spec measurable: value + unit + tolerance + verification method) + a ready `build` spec | N/A |
| `/anvil:improve` | Optimization loop on an existing design: minimize `bom_cost` \| `board_area` \| `part_count` or maximize `worst_case_margin`, under a hard non-regression ratchet (ERC=0 ∧ DRC=0 ∧ sim assertions hold) | 20 |
| `/anvil:evals` | Analyze iteration results: trends, plateaus, regressions, margin + cost trajectories | N/A |

## The Six Dimensions (scoring contract)

Measured by `scripts/score-anvil.sh pass-rate` over `anvil-results.tsv`
(7 tab-separated cols: `n dimension assertion status weight evidence traces`):

| Dimension | Weight | Gate |
|---|---|---|
| `electrical` | 0.30 | **GATING** — any red row caps headline pass-rate at 0.50 |
| `simulation` | 0.25 | must-pass rows (HRS-derived) |
| `layout` | 0.20 | DRC rows must-pass |
| `manufacturing` | 0.15 | |
| `testability` | 0.10 | |
| `documentation` | 0.10 | |

Weights renormalize over the dimensions that actually ran. Full contract:
`references/metrics.md`.

## Universal Flags

| Flag | Applies To | Purpose |
|---|---|---|
| `Iterations: N` | All looping | Set iteration count |
| `Iterations: unlimited` | All looping | Opt-in unbounded |
| `--evals` / `--evals-interval N` | All looping | Mid-loop checkpoints + final summary |
| `--chain <targets>` | All | Sequential handoff after completion |
| `--dry-run` | build | Print derived config + planned pipeline; no execution |

## Seam & reference resolution

Gates ship in `skills/anvil/scripts/` and contracts in `skills/anvil/references/`. Resolve
`ANVIL_ROOT` to the FIRST that exists:
1. `${CLAUDE_PLUGIN_ROOT}/skills/anvil` — installed plugin.
2. `.claude/skills/anvil` — project-local install (or this repo's canonical tree).
3. The directory containing the invoked command file.
4. Last resort: glob `**/skills/anvil/scripts/score-anvil.sh` and take its grandparent.

Then read every `scripts/<x>` as `$ANVIL_ROOT/scripts/<x>` (falling back to the repo-root
`scripts/` when running inside this harness repo) and every `references/<x>` as
`$ANVIL_ROOT/references/<x>`. If nothing resolves, STOP and tell the user to reinstall — the gates
are mechanical requirements of the pipeline, not optional helpers.

Run `bash scripts/doctor.sh` once at Phase 0 of any command (`--require-build` for `build`): a
missing `kicad-cli` or `ngspice` means the electrical/simulation/layout dimensions cannot be
verified, which blocks convergence later — surface that now, not at iteration 30.
