---
name: anvil:build
description: "Build greenfield electronics — or a full end-to-end product (boards + enclosure + COTS modules + wiring + assembly package) — via the standard hardware V-model, every phase gated with its named deliverable, to passing weighted acceptance"
argument-hint: "[Spec: <file|glob>] [Goal: <text>] [Scope: <dir>] [Fab: jlcpcb|pcbway|generic] [Iterations: N] [--evals] [--dry-run] [--chain <targets>]"
---

EXECUTE IMMEDIATELY.

Greenfield **electronics builder** that follows the standard hardware engineering lifecycle (the
V-model, agile-right-sized): planning → feasibility → requirements → architecture + part selection →
schematic capture → simulation → PCB layout → fab package + verification docs. Every phase exits
through a gate carrying its **named deliverable** (charter, GO/NO-GO verdict, HRS + RTM, block
diagram + power budget + pinned parts catalog, ERC-clean netlist + derating table, sim report with
corner margins, DRC-clean board, fab package + test plan). "Done" is **passing acceptance across six
weighted dimensions** — **electrical 0.30** · simulation 0.25 · layout 0.20 · manufacturing 0.15 ·
testability 0.10 · documentation 0.10 — measured by `scripts/score-anvil.sh pass-rate`.

**`electrical` is the gating dimension** (the hardware analog of forge's `logic` gate): ERC = 0,
connectivity golden cases, derating table green, power budget closes. While ANY `electrical` row is
red the headline pass-rate is **capped at 0.50** — a board can never ride a pretty layout or a cheap
BOM to "done" while the electricity is wrong. **Done also requires full coverage** — every HRS
requirement (`HR-n`) traces to ≥1 acceptance assertion (`scripts/score-anvil.sh coverage`), and
every requirement must be **VERIFIED AT ITS DECLARED METHOD OR STRONGER** (test > simulation >
analysis > inspection): a spec marked `verify: simulation` satisfied only by a prose "analysis"
paragraph is **not** satisfied — the hardware edition of "defined but never called". Before
convergence, a **requirement-satisfaction audit** re-reads the HRS and confirms every HR-n is
genuinely exercised, not merely traced.

**Anti-demo, hardware edition:** the deliverable is a **bench-ready board**, not a floating-enable
dev-board frankenstein — connector pinouts documented, pin-1/polarity silkscreen marks, mounting
holes, test points on every power rail and key signal, ESD on user-facing connectors,
reverse-polarity or inrush protection where the spec implies field use, and a bring-up plan a
technician could follow cold.

**Product mode:** when the spec carries a `product:` block — or the Goal describes an assembled
unit (a drone, an instrument, a device in a case), not a bare board — the build additionally runs
the **product track** (after Phase 8 below): system decomposition + ICD, COTS module selection,
mechanical CAD track, wiring harness, product BOM, system budgets, assembly package. Product
ledgers add three must-pass dimensions — **mechanical 0.20 · integration 0.15 · system 0.15**
(renormalized; see `references/metrics.md`). The deliverable is then **everything needed to
assemble the final unit**, not just the fab package.

Companion contracts: `references/hardware-requirements-protocol.md`, `references/schematic-protocol.md`,
`references/simulation-protocol.md`, `references/layout-protocol.md`, `references/fab-protocol.md`,
`references/metrics.md`, `references/toolchain.md` — and for product mode:
`references/system-protocol.md`, `references/cots-protocol.md`, `references/mechanical-protocol.md`,
`references/harness-protocol.md`, `references/assembly-protocol.md`.

## Seam & reference resolution (read once)

Resolve `ANVIL_ROOT` exactly as in SKILL.md: first existing of `${CLAUDE_PLUGIN_ROOT}/skills/anvil`,
`.claude/skills/anvil`, the directory containing this command file, else glob
`**/skills/anvil/scripts/score-anvil.sh` and take its grandparent. Every `scripts/<x>` below means
`$ANVIL_ROOT/scripts/<x>` (repo-root `scripts/` when running inside the harness repo); every
`references/<x>` means `$ANVIL_ROOT/references/<x>`. Run `bash scripts/doctor.sh --require-build`
at Phase 0: missing `kicad-cli`/`ngspice` blocks the electrical/simulation/layout dimensions —
surface now, not at iteration 30.

## Output repository — every build lives on GitHub (transparency contract)

Every board this command builds gets its **own private GitHub repository** under the authenticated
`gh` account, created in Phase 1 right after the local `git init`:
`gh repo create <account>/<slug> --private` (slug = board name; `Repo:` argument overrides). Wire
`origin`, push at **every phase gate** and every green milestone. CI on the output repo runs the
mechanical gates (ERC, DRC, sim assertions, score) so evidence accumulates on the ACTUAL output.
Found-but-deferred defects become GitHub issues (label `anvil`). Releases are human-gated; the loop
never tags them. The repo stays private; visibility is never changed. If `gh` is unauthenticated,
say so and continue local-only — never silently skip the contract.

## Safety invariants (build-specific)

- **Money is human-gated:** never order parts, request quotes that create accounts, or submit
  fab/assembly jobs. The fab package + a cost roll-up is the terminal deliverable.
- **HV register:** any net > 30 V adds IPC-2221 creepage/clearance rows (human-review must-pass);
  mains-connected designs add a human sign-off row the loop can never mark `pass`.
- Never scaffold into the anvil skill tree — build into the declared Scope or a fresh
  `boards/<name>/`.

## Reuse before design (efficiency principle)

For every already-solved circuit — buck/boost/LDO power stages, USB-C CC/PD front ends, ESD
networks, level shifters, reset supervisors, crystal loading, standard MCU minimal circuits —
**prefer the vendor's reference design / datasheet application circuit over novel topology**, with
the reference cited in the schematic notes. Use the manufacturer's own SPICE model when published.
Hand-design ONLY the domain circuitry the HRS actually owns. A hand-rolled DC-DC compensation
network where the datasheet publishes one is a defect, not diligence. Record each major part choice
with a one-line rationale in `arch/architecture.md`.

## Parse Arguments

- `Spec:` / `--spec` — eval spec file (`evals/hardware/*.spec.yaml`). Declares targets + specs +
  golden connectivity + sim assertions.
- `Goal:` / `--goal` — free-text board description when no spec is given (an HRS is derived via the
  `requirements` protocol).
- `Scope:` / `--scope` — directory the build may write into (default `boards/<slug>/`).
- `Fab:` / `--fab` — rule-deck preset: `jlcpcb` (default) | `pcbway` | `generic`.
- `Iterations:` — default 40. `Target-rate:` — stop pass-rate (default 1.00).
- `--evals`, `--evals-interval N`, `--chain <targets>`, `--dry-run`, `Repo:`.

If neither Spec nor Goal is provided, AskUserQuestion (single batch): what board, power source +
budget, fab preset + layer count, launch mode (bounded 40 / unlimited / dry-run).

## Run directory & deliverables

`anvil/build-{YYMMDD}-{HHMM}/` for run logs; the board itself in Scope:
`charter.md`, `hrs/requirements.md`, `arch/architecture.md`, `catalog/parts-catalog.csv`, `sch/`,
`sim/` (+ `sim/assertions.tsv`), `pcb/`, `fab/`, `docs/`, `anvil-results.tsv`, `iterations.tsv`,
`handoff.json`.

---

# The Pipeline (phase-gated)

Standard phases, agile execution: the loop re-slices phases so every slice touches
requirement → verification at small scale; deliverables are just-enough living documents; the
pass-rate — not document completion — is the measure of progress.

## Phase 1 — Planning / Initiation
Produce the **charter** (`charter.md`, ~1 page): board mission + elevator pitch, explicit in/out
scope, stakeholders + deployment environment, iteration budget, constraints (size, cost @ qty,
connectors, compliance domains), and a **risk register** (≥3, each with mitigation — always
consider: single-source parts, long-lead parts, HV/EMC compliance, thermal, novel topology).
`git init` + create the private output repo.
**Gate:** charter committed; output repo wired (or local-only noted); Scope resolved.

## Phase 2 — Feasibility (GO/NO-GO spike)
- **Toolchain** — `doctor.sh --require-build` green: `kicad-cli`, `ngspice`, python, node.
- **Topology spike** — the candidate topology's bare sim boots in ngspice and converges (a buck
  that won't converge at nominal is a NO-GO signal, not an iteration-30 surprise).
- **Parts reality** — the 3–5 keystone parts (controller/MCU/sensor) exist, are in stock at ≥1
  major distributor, not EOL/NRND, and have SPICE models or enough datasheet data to model.
- **Budget sanity** — keystone parts alone vs BOM target; spec row count vs iteration budget.
**Gate:** verdict recorded in `charter.md` as **GO** (topology + keystone parts pinned) or
**NO-GO** → AskUserQuestion to re-scope. Never enter Phase 3 on an unproven toolchain.

## Phase 3 — Requirements (HRS)
Turn Spec/Goal into a concrete **HRS** per `references/hardware-requirements-protocol.md`: every
requirement gets a stable ID `HR-n`, a **value + unit + tolerance/limit**, worst-case conditions,
and a **verification method** ∈ {test, simulation, analysis, inspection}. Include the must-be
checklist (reverse polarity, ESD, brown-out, inrush, thermal ceiling) — what the client never says
but always expects. Seed `anvil-results.tsv` with every acceptance row as `fail` (baseline), each
carrying `traces` → HR-n. Seed `sim/assertions.tsv` from every `verify: simulation|test` spec.
**Gate:** `scripts/score-anvil.sh coverage anvil-results.tsv hrs/requirements.md` →
`REQ_COVERAGE: 1.00`; baseline `scripts/score-anvil.sh pass-rate` → `0.00` (honest zero).

## Phase 4 — Architecture & part selection
Per the protocol: **block diagram** (mermaid) where every HRS interface appears exactly once;
**power budget table** that CLOSES (per rail: worst-case load ≤ source capability × derating factor —
a budget that doesn't close is an `electrical` red row); interface map (connector pinouts);
**topology trade study** for contested blocks (reuse `reason`-style debate, 2–3 candidates, pick
with rationale); **part selection** with lifecycle (active, not NRND/EOL), stock at ≥2 distributors
or an approved second source, and datasheet-anchored deratings. Write the **pinned parts catalog**
`catalog/parts-catalog.csv` (`mpn,description,qty,unit_price,currency,stock,lifecycle,distributor,accessed`)
— the ONLY source `bom-cost` joins against (Goodhart guard: refreshing it is an explicit, logged
event). Derive **connectivity golden cases** — the `electrical` dimension's must-pass rows: every
block-diagram edge exists as a net; every power pin has its decoupling; every enable/reset pin
deliberately driven or strapped, never floating.
**Gate:** architecture.md committed; power budget closes; catalog pinned; golden cases seeded as
red `electrical` rows.

## Phase 5 — Schematic capture (connectivity-TDD)
Per `references/schematic-protocol.md`. **Netlist as code** — SKiDL python (default), atopile, or
native `.kicad_sch` — always a text artifact the loop can diff and revert. Red → green on the
connectivity goldens: goldens exist and fail before the netlist is built, then one block per
iteration to green. Then:
- `kicad-cli sch erc --format json --severity-error --exit-code-violations` → **ERC = 0**
  (`scripts/score-anvil.sh erc <sch>` emits `ERC_VIOLATIONS: N`).
- **Derating table** (`sch/derating.md`): every part's worst-case stress ≤ 80 % of rating
  (voltage, current, power, temp) — any exceedance is an `electrical` red row.
- Design-review checklist from the protocol (pull-ups, boot straps, bypass placement intent,
  connector ESD, test-point nets declared).
- Export schematic PDF (`kicad-cli sch export pdf`) and **VIEW every page** (Read the PDF) —
  unviewed evidence is not evidence.
**Gate:** ERC 0 · goldens green · derating green · PDF viewed. Electrical gate lifts only here.

## Phase 6 — Simulation (specs at corners)
Per `references/simulation-protocol.md`. One ngspice harness per simulable HRS spec
(`sim/<spec>.cir`), vendor models preferred, `.measure` directives named after assertion IDs.
`sim/assertions.tsv` (`id measure op limit units corners traces`) is the contract;
`scripts/score-anvil.sh sim sim/` runs every harness batch (`ngspice -b`), parses measures,
compares against limits, prints per-row PASS/FAIL + margin. **Nominal first, then worst-case
corners** (line min/max × load min/max × temp, tolerance sweeps where models allow) — a spec passes
only at its declared corners, and the **margin in engineering units** is logged (feeds `improve`).
Non-convergence is a red row, never a skip. A spec that genuinely cannot be simulated is downgraded
to `verify: analysis` **in the HRS, with a logged reason** — never silently.
**Gate:** every `simulation` row green at corners; margins recorded in `docs/SIM-REPORT.md`.

## Phase 7 — PCB layout
Per `references/layout-protocol.md`. Import netlist; stackup + board setup constraints from the fab
preset; install the fab rule deck (`pcb/rules/<fab>.kicad_dru`). Placement protocol (connectors →
power stage current loops → decoupling-at-pin → sensitive analog → the rest), then route
critical nets first (feedback, switch nodes, diff pairs, clocks) under the protocol's constraints.
- `kicad-cli pcb drc --format json --schematic-parity --severity-error --exit-code-violations` →
  **DRC = 0 including parity + rule deck** (`scripts/score-anvil.sh drc <pcb>` →
  `DRC_VIOLATIONS: N`). Unconnected items count as violations.
- `scripts/score-anvil.sh area <pcb>` → mm² vs the HRS target.
- Copper/thermal sanity per protocol; test points + mounting holes are DRC-checked footprints,
  not silkscreen fictions.
- Render (`kicad-cli pcb render` front + back PNG) and **VIEW the renders** before the gate.
**Gate:** DRC 0 · parity clean · area within target · renders viewed.

## Phase 8 — Fab package, docs & convergence
Per `references/fab-protocol.md`: export gerbers + drill (`kicad-cli pcb export gerbers|drill`),
BOM (`kicad-cli sch export bom` with MPN/qty fields → join catalog → `BOM_COST: $X @ qtyN` vs
target), CPL (`kicad-cli pcb export pos --format csv --units mm`), `fab/DFM-REPORT.md` (deck
version, violation zero-count, stackup, finish). Docs: `docs/TEST-PLAN.md` (per-HR bring-up
measurements with expected values ± tolerance — a technician-followable script),
`docs/BRINGUP.md` (power-on sequence, current-limit first-power values, smoke-test order),
assembly notes, README. **Requirement-satisfaction audit:** re-read the HRS; every HR-n verified at
its declared method or stronger, with evidence paths. Then the loop: pick lowest dimension →
one change → cheap gates first (ERC → derating → affected sims → DRC → full) → keep/revert → log —
until `Target-rate` or iterations exhausted.
**Verdict:** `scripts/score-anvil.sh verdict` → `FAB_READY` (all must-pass green, pass-rate ≥
target, coverage 1.00, HV register satisfied) | `FAB_BLOCKED` with the blocking rows. Ordering is
the user's move.

---

# Product track (end-to-end builds)

Runs when product mode is active. The electronics pipeline above executes unchanged **per custom
board** (multi-board products: one `boards/<n>/` tree each, aggregated into the product ledger);
these phases run alongside it and converge at the same weighted acceptance. Phase 0 runs
`doctor.sh --require-product` (CAD-as-code kernel checked up front). Scope grows to
`system/ cots/ mech/ harness/ assembly/ product-bom.csv` next to `boards/`.

## Phase P1 — System architecture (extends Phase 4)
Per `references/system-protocol.md` + `references/cots-protocol.md`: product decomposition +
subsystem registry (every physical thing owned by exactly one subsystem); **ICD**
(`system/icd.tsv`) — every subsystem interface exactly once, worst-case V/I on every
power/signal edge; COTS module selection with 2–3 candidate trade studies, pinned into
`cots/modules.csv` with datasheet-anchored `key_specs` (thrust tables, Wh, C-ratings — numbers
the budgets consume); `system/budgets.tsv` seeded (mass/power/endurance/cost) with formulas
shown in `system/budgets.md`. Seed system golden rows red: no decomposition orphans, every ICD
edge realized, module voltage/protocol compatibility.
**Gate:** decomposition + ICD committed · module catalog pinned · budgets seeded (red is honest).

## Phase P2 — Mechanical capture (parallel to Phases 5–7)
Per `references/mechanical-protocol.md`: CAD-as-code (`mech/cad/*.py`, params block first),
headless build → STL/STEP + kernel-emitted `measures.json`; `mech/assertions.tsv` seeded from
the HRS mechanical/environment specs (fit/mass/dfm classes, IP/vibration/drop-derived rules).
Red → green: `mesh` → 0 defects (watertight, manifold) on every build STL; `fit` green — board
envelope + component heights vs cavity (placeholder envelope until layout exists, **refreshed
against the DRC-clean board before the gate lifts**); `mech-dfm` green (process floors; slicer
seam when `PRUSA_SLICER` is set); section + exploded renders exported and **VIEWED**.
**Gate:** MESH_DEFECTS 0 · FIT_PASS full vs final board · DFM_PASS full · renders viewed.

## Phase P3 — Interconnect (parallel to Phases 7–8)
Per `references/harness-protocol.md`: `harness/harness.tsv` + `harness/mates.tsv` realizing
every power/signal ICD edge — the wiring harness is a table, not a diagram in someone's head.
Wire lengths from the mechanical model's routed paths; RF/loom/strain-relief rules applied.
**Gate:** `pinout` → PINOUT_VIOLATIONS 0 (ampacity floor, endpoint grammar, mate coverage,
no unrealized ICD edge).

## Phase P4 — Product roll-up & assembly package (extends Phase 8)
`product-bom.csv` — every physical thing in the unit (pcb, cots, mech, fastener, wire,
consumable, spare) priced, massed, sourced → `product-bom` costs out; `sys-budget` re-run on
rolled-up numbers (AUW from the product BOM is the mass budget's demand — the **system budgets**
close on measured rollups, not estimates). Assembly package per
`references/assembly-protocol.md`: `assembly/ASSEMBLY.md` (every step references product-BOM
ids — both-direction orphan check), `INTEGRATION.md` bring-up ladder with numbers,
`config/` artifacts committed (FC dump, VTX table, radio model), `QC.md`, exploded render
**VIEWED**. Region-gated rows (VTX power/band legality, drone-class rules) are human sign-off,
never loop-passed.
**Gate:** PRODUCT_COST ≤ target · SYS_BUDGET all close · assembly rows green · config committed.
**Verdict:** same `scripts/score-anvil.sh verdict` — `mechanical`/`integration`/`system` rows
are must-pass; a closing mass budget cannot ride over an interfering enclosure.

---

## Iteration & failure discipline

- ONE focused change per iteration; commit before verify; revert on regression — margins count:
  a change that keeps a sim green but halves its margin is a regression unless it buys a scoped
  metric win (logged).
- Cheap gates first every iteration; FULL gate suite before any `keep` that touches a phase
  deliverable.
- Non-convergent sims: fix the harness (ic/uic, gmin stepping per protocol) before touching the
  design; a sim that can't run is a red row.
- Every deferred defect → GitHub issue on the output repo (label `anvil`), never a lost note.
- `iterations.tsv`: `n timestamp phase change dimension result pass_rate notes`.
- Chain: `--chain improve` hands the converged board to the optimizer; `handoff.json` carries
  `verdict, pass_rate, erc_violations, drc_violations, sim_pass, bom_cost, board_area, repo`.
