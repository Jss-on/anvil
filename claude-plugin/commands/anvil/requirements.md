---
name: anvil:requirements
description: "Turn raw hardware needs into a validated HRS — every requirement measurable (value + unit + tolerance + verification method), latent must-be needs elicited — plus a ready-to-run anvil:build spec"
argument-hint: "[Goal: <text|file>] [Client: <who>] [Fab: jlcpcb|pcbway|generic] [--chain build]"
---

EXECUTE IMMEDIATELY.

The **requirements engineer** of the hardware pipeline. Takes raw client input — a sentence, a
napkin brief, an email thread — and runs a hardware-adapted requirements-engineering process to a
validated **Hardware Requirements Specification (HRS)** plus a ready `build` spec. The discipline:
**no requirement without a number, no number without a unit and tolerance, no spec without a
verification method, no method weaker than the spec demands.** Companion contract:
`references/hardware-requirements-protocol.md` (elicitation domains, HRS template, measurability
rules, must-be checklist, verification ladder).

## Seam & reference resolution (read once)
Resolve `ANVIL_ROOT` as in SKILL.md. `scripts/<x>` → `$ANVIL_ROOT/scripts/<x>`; `references/<x>` →
`$ANVIL_ROOT/references/<x>`. Run `bash scripts/doctor.sh` (CORE tools only) at start.

## Parse Arguments
- `Goal:` — raw need, inline or file. Required; if absent, ask.
- `Client:` — who deploys the board and where (bench, field, product, industrial). Calibrates the
  must-be checklist and environmental class.
- `Fab:` — target fab preset; constrains layer count, min features, finish options early.
- `--chain build` — hand the finished spec straight to `/anvil:build`.

## Run directory & deliverables
`anvil/requirements-{YYMMDD}-{HHMM}/` containing:
- `hrs/requirements.md` — the HRS (template in the protocol): G-n goals, HR-n requirements
  (functional, electrical, mechanical, environmental, EMC/regulatory, manufacturing, lifecycle,
  safety), each with value + unit + tolerance/limit + worst-case conditions + `verify:` method.
- `build-spec.yaml` — the ready `anvil:build` spec: targets (cost @ qty, area, layers), specs[]
  (id, text, dimension, verify), golden_connectivity[], sim_assertions[].
- `open-questions.md` — everything the client must still decide, each with a recommended default.
- `handoff.json`.

## Phase 1 — Domain recon (before the first question)
Read the goal. Identify the board archetype (power supply, MCU carrier, sensor node, interface
bridge, motor driver, RF, mixed) and pull its **standard failure modes and unstated expectations**
from the protocol's must-be checklist — reverse-polarity, ESD on user-facing connectors, brown-out
behavior, inrush, thermal ceiling at max ambient, connector retention, mounting. These become
candidate requirements BEFORE elicitation, so the client reacts instead of recalls.

## Phase 2 — Elicitation across the nine domains
Interview (interactive: batched AskUserQuestion rounds, max 4 per round; non-interactive: derive
and log as explicit assumptions) across the protocol's domains: function & performance · power
source/budget · electrical environment (line range, transients) · mechanical (size, mounting,
connectors, enclosure) · thermal/ambient · EMC + regulatory class · interfaces & protocols ·
manufacturing (fab preset, qty, budget, assembly, **IPC class election** — default 2, per
`references/standards.md`) · lifecycle (field-serviceable? expected years,
second-source policy) · safety (voltage class — triggers the HV register above 30 V).
**Day-in-the-life walkthrough:** narrate the board's first power-on, worst day (hot car, brownout,
wrong charger), and end of life; every friction point becomes a requirement or an open question.

## Phase 3 — Specification (measurability enforcement)
Write the HRS. EVERY requirement passes the four measurability checks:
1. **Value + unit** — "low ripple" is not a requirement; "≤ 30 mV p-p on 3V3" is.
2. **Conditions** — the corners it must hold at (line, load, temp). Unstated conditions = nominal
   only = almost never what the client means.
3. **Tolerance/limit direction** — `≤`, `≥`, or `±`.
4. **Verification method** — test | simulation | analysis | inspection, the STRONGEST feasible
   (the ladder in the protocol). `analysis` for a simulable spec requires a logged reason.
Assign stable `HR-n` IDs. Derive `golden_connectivity` entries and `sim_assertions` rows from the
specs. Cost target is stated **@ a quantity** and a catalog-snapshot date.

## Phase 4 — Validation & handoff
- Mechanical: `scripts/score-anvil.sh coverage --spec build-spec.yaml hrs/requirements.md` —
  every HR-n maps into the spec; every spec row traces back; orphans fail the gate.
- Read-back: one AskUserQuestion confirming the 5 highest-risk requirements + all open questions
  with recommended defaults (non-interactive: log as assumptions).
- Verdict: `HRS_READY | HRS_BLOCKED` + what blocks. `--chain build` passes `build-spec.yaml`
  through `handoff.json`.
