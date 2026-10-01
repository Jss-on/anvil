---
name: anvil:build
description: "Build a board or complete hardware product through concurrent engineering tracks and evidence-backed lifecycle gates"
argument-hint: "[Goal: ...|Spec: <file>] [Scope: <directory>] [Release: pcb|assembly|product] [Target: G0..G7] [Iterations: N]"
---

Execute the authorized build. Read the Anvil skill, lifecycle protocol, evidence protocol, and
the technical protocols relevant to the product. Default Target to G3 and infer release kind
from the intended deliverable; an enclosure, multi-board assembly, or integrated device is a
product. Do not confuse PCB fabrication, assembled-board readiness, and complete-product build.

1. Inspect existing files, repository instructions, and user changes. Resolve Anvil's actual
   installed paths. Run `doctor.sh`; use `--require-build` when KiCad/ngspice execution is
   needed, and `--require-product` only when CAD generation is needed. Missing tooling blocks
   dependent verification while requirements and other useful work continue.
2. For a new empty project, use `anvil.py init <scope> --scope <release-kind> --sectors ...
   --markets ... --features ...`. For an existing design, add the template files individually
   without overwriting its work. Preserve legacy ledgers as history; migrate them as unverified
   until their evidence meets the new contract.
3. G0/G1: establish intended use, users, environments, variants, commercial stop criteria,
   measurable requirements, owners, verification methods and due gates, risk register,
   supply assumptions, and destination classification. Populate `hrs/requirements.tsv` and
   `anvil-project.json`; use `plan <scope>` to create the required checks.
4. G2: baseline architecture and both ends of every electrical/mechanical/software interface.
   Resolve critical feasibility experiments, worst-case budgets and margins, component and
   technology choices, safety states, security/update architecture, test access, and supplier
   manufacturing feedback. Start firmware, fixture and compliance plans now.
5. G3: develop schematic/connectivity, circuit corner verification, layout, mechanical CAD,
   harnesses, sourcing, firmware build and compatibility records, assembly/test procedures,
   and manufacturer outputs concurrently. Read the protocol for each track. Render and inspect
   schematic/PCB/mechanical exports; never imply that a generated image was reviewed if unseen.
   Accuracy loop for every track: size parts from the rulebook and record each calculation in
   `design/rules.tsv` with its `TAG-nnn` source; write the golden netlist `sch/circuit.json`, run
   `anvil.py schematic sch/circuit.json pcb/<board>.kicad_sch` (wired, reloaded, netlist == spec, ERC) and
   add `W-1 golden ../sch/circuit.json` to `sch/connectivity.tsv`; declare `sim/plots.tsv` and run `plots`.
   View every render/plot you cite. Each modify→verify→keep/discard step is one `log <scope> iteration ...`
   row (metric, value, checks, result, rules); sources read go to `log research`, choices to `log decision`.
   Board loop: `board` the schematic onto the fabricator-stackup template, iterate `design/placement.tsv`
   (`place`) and routing (`route` copy or KiCad by hand) until `layout` (nets.tsv/rf.tsv), `si`, `pdn`,
   `thermal` and `emc` pass on the copper, then run `em` once on RF paths/antennas before release.
   Release each intent table as its artifact role so its `AUTO-*` check gates G3 (`sparams` gates G4 on
   VNA data). Report model limits verbatim; never state RF/EMC/thermal compliance from a simulation.
6. Install active custom rules as `<board>.kicad_dru` beside the matching `.kicad_pcb`,
   `.kicad_pro`, and `.kicad_sch`. The bundled JLCPCB example is a starting deck requiring
   current manufacturer review; no other manufacturer preset is supplied.
7. Fill `artifacts` with every controlled file and dependency, and `checks` with input command
   arrays. Run `manifest <scope>`, then `record <scope> AUTO-...` for applicable automated
   checks. Import actual signed/reviewed evidence with `record --evidence` for all other checks.
   The tool prints the applicable check IDs in `lifecycle-plan.json`; do not improvise IDs.
8. Evaluate `gate <scope> G3`. Resolve errors and design defects, regenerate the manifest after
   changes, and repeat affected runs/reviews. A metric helps prioritize work; it cannot waive
   a requirement. Never auto-fill physical tests or third-party approvals to finish the ledger.
9. For a later target, continue with `/anvil:lifecycle` through bring-up/EVT, DVT, PVT, and
   destination release. Complete all available work, identify specific external evidence still
   needed, and preserve blocked gates until it arrives. Do not label a prototype marketable.

If `Jev: shadow` is enabled, follow the skill's Jev triage reference for ambiguous findings
after step 8. Record its advice separately; it cannot update evidence or remove blockers.

At completion run `renders`, `fabpack` for each board and `report <scope>`; provide the scoped gate
result, the artifact package, `audit/AUDIT.md`, exact remaining blockers, and known verification limits. Write `handoff <scope> --write build --gate <target>`, then run
`validate-handoff.sh <scope>/handoff.json` before a requested chain. Validate source inputs and
gate again after any handoff change. Ordering, submission, deployment, and shipment require
the session's authorization for those actions; no repeated confirmation after authorization.
