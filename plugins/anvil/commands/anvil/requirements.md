---
name: anvil:requirements
description: "Turn intended use into measurable hardware, firmware, manufacturing, compliance, and lifecycle requirements with owners and verification gates"
argument-hint: "[Goal: <text|file>] [Scope: <directory>] [Sectors: ...] [Markets: ...] [--chain build]"
---

Read the Anvil skill and hardware-requirements protocol. Inspect existing requirements and
session answers before asking anything. Identify users, intended purpose, environment,
product variants, sales destinations, production location, support duration, and commercial
constraints. Clarify only consequential missing information; record assumptions with owners.

Walk the product through installation, startup, normal operation, credible faults, updates,
maintenance, returns, and retirement. Cover electrical performance, power/transients, thermal,
mechanical tolerances, interfaces, firmware resources, security, safety, manufacturing/test,
supply, compliance, cost at volume, and service. Risk determines which needs become requirements.

Write `hrs/requirements.tsv` with stable `HR-n` IDs, statement, units, conditions, method,
due gate, and owner. Quantitative properties need numeric limits and tolerances; qualitative
properties need objective pass/fail acceptance criteria. Choose test, simulation, analysis, or
inspection to answer the claim. No method hierarchy or invented physical evidence.
Keep explanatory goals, hazard links, rationale, assumptions, and exclusions in the companion
`hrs/requirements.md`. Do not overwrite accepted constraints with convenient defaults.

Populate `anvil-project.json` with release scope, feature/sector/market selectors, and the
requirements path. Run `plan <scope>`; each requirement gets its own verification check at
its due gate. Complete the G0/G1 checklist evidence, including early sector and destination
applicability plans. A requirement's future test can remain `not_run` at G1 while its approved
definition and verification plan are reviewed.

Run `gate <scope> G1`. `HRS_READY` requires the actual reviewed G0/G1 records, rather than
mentions of HR IDs or a rounded coverage score. Write `handoff <scope> --write requirements
--gate G1` and validate it before chaining to build. Carry unresolved questions and blockers
into the next workflow; continue independent design work within the authorized scope.
