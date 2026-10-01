---
name: anvil
description: "Design, verify, improve, and release electronic hardware products through requirements, architecture, PCB fabrication, firmware, mechanics, EVT, DVT, PVT, market access, support, and retirement. Use for Anvil builds, hardware requirements, design optimization, lifecycle gates, and evidence audits."
metadata:
  version: "0.7.0"
---

# Anvil

Develop hardware products through explicit lifecycle gates. Run electronics, firmware,
mechanics, manufacturing, compliance, and commercial work concurrently from requirements.
Read [lifecycle-protocol.md](references/lifecycle-protocol.md) before a new product or gate review.

## Resolve the installed tools once

Resolve paths from this loaded `SKILL.md`, independently of the user's project directory.
In either installed plugin, its containing directory is `ANVIL_ROOT` and contains `references/`,
`scripts/`, and `templates/anvil-project/`. Claude Code may also expose that directory as
`${CLAUDE_PLUGIN_ROOT}/skills/anvil`; Codex does not need that variable. For the canonical
`.claude/skills/anvil/SKILL.md` in this repository, scripts and templates are at the repository
root instead. Workflow files are always at `../../commands/` relative to this skill directory.

Resolve every `scripts/...` and `templates/...` example below and in workflows to those actual
absolute paths. Run checks against the user's project scope; keep outputs in that project,
outside the installed plugin cache. Use Python 3.10+ with `scripts/anvil.py`, or Bash with
`scripts/score-anvil.sh`. On Windows, `scripts/doctor.cmd` finds Git Bash without the WSL stub;
direct Python invocation also works. No Node dependency.

## Route the request

| Request | Workflow (read before execution) | Contract |
|---|---|---|
| Raw need / requirements | [requirements](../../commands/anvil/requirements.md) | [hardware requirements](references/hardware-requirements-protocol.md) |
| New board or product | [build](../../commands/anvil/build.md) | G0–G3 by default; explicit release kind |
| Bring-up, EVT/DVT/PVT, launch, support | [lifecycle](../../commands/anvil/lifecycle.md) | [lifecycle](references/lifecycle-protocol.md) |
| Improve cost, area, mass, or margin | [improve](../../commands/anvil/improve.md) | Preserve requirements and gate evidence |
| Review an iteration run | [evals](../../commands/anvil/evals.md) | Diagnostic analysis; recompute claimed gate |
| Existing custom metric loop | [custom loop](../../commands/anvil.md) | Bounded change, verify, retain/discard |

In Codex, invoke `$anvil` with a workflow name or natural-language task, for example
`$anvil build Goal: environmental monitor Scope: ./sensor Release: product Target: G3`.
In Claude Code, use `/anvil:<workflow>` or `/anvil` for the custom loop. Any `/anvil:*`
references inside workflows mean read and follow the corresponding linked file in Codex;
they are not shell commands or a dependency on Claude Code.

Infer scope from the project and session. Clarify only missing consequential requirements;
continue independent work. Do not repeat approvals already granted in the session.

When the user enables `Jev: shadow`, read [Jev triage](references/jev-triage.md) and use
`scripts/jev_triage.py` for ambiguous failure review in build/evals. It only records advice;
all actual verification and release decisions remain with the existing tools and reviewers.

## Evidence and release rules

1. `pass-rate` and `coverage` describe progress. They never authorize fabrication or shipment.
2. `anvil-project.json` declares product scope, features, sectors, destinations, controlled
   artifacts, and automated checks. `hrs/requirements.tsv` is the authoritative requirement set.
3. `plan` derives the ledger from the bundled checklist and every project requirement. All
   75 research items are represented, with extra early planning checkpoints for market duties.
   Never delete required checks, reduce weights, or narrow product applicability to gain a pass.
4. Use `record` for actual tool runs; import reviewed receipts for analysis, inspection,
   physical tests, and approvals. Read [evidence-protocol.md](references/evidence-protocol.md).
   Never manufacture a reviewer, measurement, certificate, signature, or executed test.
5. `manifest` binds release files; `gate` checks cumulative readiness against exact hashes,
   methods, applicability, and review records. Missing, skipped, stale, failed, and errored work
   stays blocked. Product requirements define suitable methods; there is no universal ranking
   of test, simulation, analysis, and inspection.
6. A changed release input reopens G3 and later evidence. Reassess safety, compliance,
   manufacturing, firmware compatibility, and field effectivity before releasing a change.
7. Run `handoff <project> --write <command>` and `validate-handoff.sh <handoff.json>` before
   chaining. Carry blockers forward. A valid blocked handoff is not authorization to release.

## Accuracy: cited rules, wired schematics, proven outputs

- Choose values from [the rulebook](references/rulebook/INDEX.md): ~12,000 cited rules extracted from the
  whole reference library (IPC, Brooks, Bogatin, Coombs, Archambeault, Williams, Paul, Pozar, Balanis, Bowick,
  Johnson & Graham, Pressman, Erickson, Horowitz & Hill...).
  Grep by domain or id; cite `TAG-nnn` ids. [bibliography.json](references/bibliography.json) maps ids to IEEE references.
- Put every sizing calculation in `design/rules.tsv` (`anvil.py calc <check> k=v` to explore; `rules <dir>` to gate):
  trace current/temperature, IPC-2221 clearance, fusing, impedance, PDN target, converter ripple, EMC radiation,
  RF link/match, thermal. A value without a passing cited row is an assumption, not a design.
- Draw schematics from `sch/circuit.json` with `anvil.py schematic`: KiCad symbols, real orthogonal wires,
  power symbols, then KiCad reload + fresh netlist == spec + ERC. `schematic-spec` converts an existing
  label-only drawing. Gate the released drawing with a `golden` row in `sch/connectivity.tsv`.
- Evidence outputs: `plots` (ngspice corner waveforms + margin chart), `renders` (schematic/PCB SVG/PDF/3D/stats),
  `fabpack` (Gerber X2, drill, placement, IPC-2581, IPC-D-356, STEP with logged commands), `wiring` (net tables).
- Keep the loop auditable: `log <project> iteration|decision|research k=v ...` every modify/verify/keep-discard
  step, decision and source consulted; `report <project>` writes `audit/AUDIT.md`, `audit.json` and an
  IEEEtran `audit/paper/` skeleton from those ledgers, receipts, BOMs and plots. See [metrics](references/metrics.md).

## Board truth: layout, SI, PDN, thermal, EM, EMC

Every board claim is measured on the copper KiCad reports (zones refilled in memory), never on typed numbers.
Declare intent tables under `design/`, then iterate place/route/verify like any other metric loop:

| Command | Intent (release role) | What it proves |
|---|---|---|
| `board <sch> <template.kicad_pcb> <out>` / `place` / `route` | `placement.tsv` | Footprints + nets from the schematic, placement, Freerouting copy + DRC |
| `layout <pcb> design` | `nets.tsv` (+`rf.tsv`) | IPC-2152 heating, IPC-2221 spacing, field-solved Z0/Zdiff, return path, length match, RF fence/stitching/keep-out |
| `si <pcb> design` | `si.tsv` | Routed topology as field-solved lines in ngspice: overshoot, ringback, delay, settling |
| `pdn <pcb> design` | `pdn.tsv` (+`caps.tsv`) | Z(f) at the load from real cap mounting, cavity, VRM vs Z_target |
| `thermal <pcb> design` | `thermal.tsv` | Layered copper conduction + convection: Tj per part, heat map |
| `em <pcb> design` | `em.tsv` | openEMS FDTD S-parameters (Touchstone + plot) of the RF copper, ports and matching parts |
| `sparams design` | `sparams.tsv` | The same limits on VNA measurements of built boards (G4) |
| `emc <pcb> design` | `emc.tsv` | Loop x harmonic radiated-emission estimate vs FCC/CISPR lines (steering, not compliance) |

Releasing an intent table (`artifacts.<role>`) makes its `AUTO-*` check mandatory at its gate. Solvers are held to
analytic anchors in `tests/test_anvil_analysis.py` (Cohn/Hammerstad-Jensen Z0, K0 thermal, lattice overshoot).
What stays physical: VNA measurement of RF paths, antenna pattern/efficiency, chamber EMC, thermal validation.
Read [layout](references/layout-protocol.md) for the loop and the model limits each command states.

## Execution boundaries

Complete authorized local design, verification, documentation, and packaging work. Preserve
unrelated user changes; use isolated worktrees or targeted reversions when needed. Do not
automatically create/push a remote repository, contact suppliers, submit regulatory documents,
order parts, spend money, deploy firmware, energize hardware, or ship a product without session
authorization for that action. Prepare the concrete package before requesting any missing approval.

Select safety standards, derating, wire ratings, samples, and test stop conditions from the
actual product and risk assessment. The agent cannot approve hazardous testing or replace the
responsible safety, clinical, regulatory, production, or commercial authority. Continue other
work while an external gate is pending. `MARKET_READY` reports reviewed project evidence;
Anvil is not a certification body or a legally validated quality-management system.

## Read the relevant tracks

- Electronics: [schematic](references/schematic-protocol.md), [simulation](references/simulation-protocol.md),
  [layout](references/layout-protocol.md), [fabrication](references/fab-protocol.md).
- Product: [system](references/system-protocol.md), [COTS](references/cots-protocol.md),
  [harness](references/harness-protocol.md), [mechanical](references/mechanical-protocol.md).
- Delivery: [firmware](references/firmware-protocol.md), [manufacturing and assembly](references/assembly-protocol.md),
  [compliance](references/standards.md), [support and retirement](references/sustaining-protocol.md).
- Tool contracts: [metrics](references/metrics.md), [toolchain](references/toolchain.md).
