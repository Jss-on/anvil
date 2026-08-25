<div align="center">

# Anvil

**AutoForge's hardware sibling — turn Claude Code into a relentless electronics-design engine, from requirements to fab-ready PCB.**

Anvil is the product; `anvil` is its command namespace — every command is `/anvil:*`.

Based on the same principles as [AutoForge](https://github.com/Jss-on/autoforge) and [Karpathy's autoresearch](https://github.com/karpathy/autoresearch): constraint + **mechanical metric** + autonomous iteration = compounding gains. Software forges on green tests; hardware forges on **clean ERC/DRC, passing simulation assertions, closed power budgets, and a BOM that costs what the spec says**.

![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)
![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)

*"Set the SPEC → The agent runs the LOOP → You wake up to a fab package."*

</div>

---

```
 REQUIREMENTS      ARCHITECTURE      SCHEMATIC          SIMULATION        LAYOUT            FAB PACKAGE
 ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
 │   HRS    │     │  Blocks  │     │ Netlist  │     │ ngspice  │     │  Place   │     │ Gerbers  │
 │  HR-n +  │────▶│  Power   │────▶│  as code │────▶│ .measure │────▶│  Route   │────▶│ BOM/CPL  │
 │ verify   │     │  budget  │     │  ERC=0   │     │ corners  │     │  DRC=0   │     │ DFM+cost │
 └──────────┘     └──────────┘     └──────────┘     └──────────┘     └──────────┘     └──────────┘
 /anvil:            (build P4)       (build P5)       (build P6)       (build P7)       (build P8)
   requirements    ─────────────────────── /anvil:build orchestrates all phases ───────────────────

                   ┌──────────┐     ┌──────────┐
                   │ Improve  │     │  Evals   │
                   │ cost/area│     │ trends   │
                   │ /margin  │     │ plateaus │
                   └──────────┘     └──────────┘
                   /anvil:improve   /anvil:evals
```

---

## Why This Exists

AutoForge proved the loop generalizes: one metric, constrained scope, fast mechanical verification, automatic rollback, git as memory. Hardware design is the next domain that fits the loop **exactly** — because EDA toolchains already emit machine-readable truth:

| Question | Mechanical answer | Tool |
|---|---|---|
| Is the schematic electrically sane? | ERC violation count → **0** | `kicad-cli sch erc --format json` |
| Does the circuit meet spec? | `.measure` values vs HRS limits, at worst-case corners | `ngspice -b` |
| Is the board manufacturable? | DRC + fab rule-deck violation count → **0** | `kicad-cli pcb drc --format json` |
| What does it cost? | BOM joined against a **pinned parts-catalog snapshot** | `score-anvil.sh bom-cost` |
| How big is it? | Edge.Cuts bounding box, mm² | `score-anvil.sh area` |
| Are parts stressed? | Derating table — no part above 80 % of rating | schematic protocol |

None of these are vibes. All of them are numbers a loop can ratchet.

## The Loop

```
LOOP (N iterations or until FAB_READY):
  1. Review current state + git history + anvil-results.tsv
  2. Pick the next change (lowest-scoring dimension first; electrical gate first of all)
  3. Make ONE focused change (netlist edit, value change, part swap, placement/route change)
  4. Git commit (before verification)
  5. Mechanical verification — cheap gates first: ERC → derating → affected sims → DRC → full
  6. If improved → keep. If worse → git revert. If crashed → fix or skip.
  7. Log to anvil-results.tsv / iterations.tsv
  8. Repeat.
```

**"Done" is passing weighted acceptance across six dimensions** — measured by `scripts/score-anvil.sh pass-rate`:

| Dimension | Weight | Covers | Gate |
|---|---|---|---|
| `electrical` | 0.30 | ERC = 0, connectivity golden cases, derating table green, power budget closes | **GATING** — any red row caps headline pass-rate at 0.50 |
| `simulation` | 0.25 | Every simulable HRS spec asserted via ngspice `.measure`, nominal + worst-case corners | must-pass rows |
| `layout` | 0.20 | DRC = 0 (incl. fab rule deck), stackup valid, critical-net constraints | DRC rows must-pass |
| `manufacturing` | 0.15 | Complete fab package (gerbers/drill/BOM/CPL), DFM clean, parts in stock + not EOL, BOM cost ≤ target | |
| `testability` | 0.10 | Test points on key nets, bring-up plan, DFT checklist | |
| `documentation` | 0.10 | Schematic PDF, board renders (viewed, not just exported), README, RTM complete | |

The `electrical` gate is the hardware analog of AutoForge's `logic` gate: a board can never ride a pretty layout or a cheap BOM to "done" while the electricity is wrong.

**Ordering parts and submitting fab/assembly jobs is always human-gated.** The loop produces the package; you spend the money.

## Commands (v0.1)

| Command | Does | Default iterations |
|---|---|---|
| `/anvil:build` | Full pipeline: charter → feasibility → HRS → architecture + parts → schematic → simulation → layout → fab package, every phase gated | 40 |
| `/anvil:requirements` | Hardware requirements elicitation → validated HRS (HR-n IDs, every spec measurable) + a ready `build` spec | N/A |
| `/anvil:improve` | Optimization loop on an existing design: minimize BOM cost / board area / part count or maximize worst-case margin, under a hard non-regression ratchet | 20 |
| `/anvil:evals` | Analyze iteration results: trends, plateaus, regressions, margin + cost trajectories | N/A |

Roadmap: `bringup` (physical board bring-up via measured evidence), `feature` (board revision with delta acceptance + ratchet), `test` (independent design review engagement), `panel` (panelization + assembly package).

## Quick Start

```bash
# 1. Check the toolchain (KiCad 9 CLI, ngspice, python, node, git)
bash scripts/doctor.sh

# 2. Elicit requirements → HRS
/anvil:requirements Goal: "USB-C powered 3.3V/1A buck regulator board, JLCPCB 2-layer, under $8 BOM @ qty 10"

# 3. Build to fab-ready
/anvil:build Spec: evals/hardware/buck-3v3.spec.yaml

# 4. Optimize what exists
/anvil:improve Metric: bom_cost Scope: boards/buck-3v3/
```

### Toolchain prerequisites

- **KiCad 9** (`winget install KiCad.KiCad`) — `kicad-cli` does ERC, DRC, netlist, gerber/drill/BOM/CPL export, PDF/PNG renders.
- **ngspice** (standalone CLI on PATH) — batch simulation with `.measure`.
- **Python 3** (`py -3` / `uv`) — SKiDL for netlist-as-code, kiutils for board file surgery.
- **node** — JSON parsing seam for the score scripts.
- Optional: **freerouting** (Java) as an autorouting seam.

`bash scripts/doctor.sh --require-build` fails fast if a build can't be verified in this environment — surfaced at Phase 0, not at iteration 30.

## Project layout (what `build` produces)

```
boards/<name>/
  charter.md                 P1 — objectives, in/out scope, iteration budget, risk register
  hrs/requirements.md        P3 — the HRS: HR-n, each with value + unit + tolerance + verify method
  arch/architecture.md       P4 — block diagram (mermaid), power budget table, interface map, trade study
  catalog/parts-catalog.csv  P4 — pinned parts snapshot: MPN, price @ qty, stock, lifecycle (Goodhart guard)
  sch/                       P5 — netlist source (SKiDL .py / .ato / .kicad_sch) + exported netlist
  sim/                       P6 — ngspice harnesses (*.cir), vendor models/, assertions.tsv
  pcb/<name>.kicad_pcb       P7 — board + pcb/rules/*.kicad_dru fab rule deck
  fab/                       P8 — gerbers/, drill, bom.csv, cpl.csv, DFM-REPORT.md
  docs/                      P8 — TEST-PLAN.md, BRINGUP.md, renders/ (viewed evidence)
  anvil-results.tsv          the acceptance ledger (7 cols, traces → HR-n)
  handoff.json               chain contract
```

Every build gets its **own private GitHub repo** (same transparency contract as AutoForge): CI runs ERC/DRC/sim on the actual output; found-but-deferred defects become issues; releases stay human-gated.

## Metric correctness (the autoresearch discipline)

A metric you can game is not a metric. Anvil's guards:

- **Violation counts come from tool JSON only** — never from the agent's reading of its own schematic.
- **Sim limits verify at worst-case corners** (line/load/temp/tolerance), not typicals; margins are logged in engineering units, and the improve loop may never trade a hard gate for a soft win.
- **BOM cost joins against a pinned catalog snapshot** committed to the repo — reproducible across runs; refreshing the snapshot is an explicit, logged event.
- **Renders and schematic PDFs must be VIEWED** by the agent (image reads) before a phase gate — exported-but-never-looked-at evidence hides ratsnest disasters the same way unviewed screenshots hid error overlays in software builds.
- **Anti-demo, hardware edition:** a board is not "done" as a floating-enable dev-board frankenstein. Bench-ready means: connector pinouts documented, polarity + pin-1 silkscreen marks, mounting holes, test points on every power rail and key signal, ESD on user-facing connectors, reverse-polarity protection where the spec implies field use.

## Safety invariants

- **Never order parts, submit fabrication or assembly jobs, or spend money** without explicit user approval. `FAB_READY` is a verdict, not a purchase.
- Designs with any net above 30 V trigger the **HV register**: IPC-2221 creepage/clearance rows are added to acceptance and require human review before `FAB_READY`. Mains-connected designs additionally require a human sign-off row that the loop can never mark pass.
- Bounded by default; unbounded is opt-in (`Iterations: unlimited`).
- All results logged to `anvil/{subcommand}-{YYMMDD}-{HHMM}/`; chain handoff via `handoff.json`.

## Relation to AutoForge

Same engine, different physics. AutoForge's gates are Playwright + test runners; Anvil's are `kicad-cli` + ngspice. The scoring contract (weighted TSV, gating dimension, coverage = RTM), the phase-gate SDLC shape, the handoff schema, and the loop discipline are deliberately isomorphic — learnings port both ways.

## License

Proprietary. Private harness — see [LICENSE](LICENSE).
