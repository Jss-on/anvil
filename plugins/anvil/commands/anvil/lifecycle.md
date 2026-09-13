---
name: anvil:lifecycle
description: "Plan and execute G0–G7 hardware lifecycle gates, bring-up, EVT/DVT/PVT, market release, sustaining, and retirement"
argument-hint: "[Scope: <project>] [Target: G0..G7|Sustaining] [Action: plan|execute|review]"
---

Read the Anvil skill and lifecycle/evidence protocols. Resolve the project and target from
the request or `anvil-project.json`. `plan` produces the applicable checks and owners;
`execute` carries out available work; `review` inspects evidence and reports blockers.
Default to execute. Never stop at a plan when the user asked for implementation.

Run `plan <scope>` to preserve existing rows and add mandatory work. Evaluate the target
with `gate <scope> <target>` and use the failures as the work queue. Gates are cumulative.
Use the firmware, assembly/manufacturing, compliance, and sustaining references as appropriate.

- G4/EVT: staged bring-up of identified prototypes, current limits, safe states, rework log,
  hardware/firmware integration, core performance and fault tests. Physical test records
  identify serial, revisions, instruments, procedures, conditions, raw results and disposition.
- G5/DVT: production-intent configuration, risk-justified samples/corners, environmental and
  reliability tests, EMC/safety/radio evidence, security/update/recovery tests, user validation,
  closed deviations and requirements traceability. A build-only firmware test is not executed HIL.
- G6/PVT: controlled manufacturing transfer, trained personnel, suppliers, tooling, process and
  inspection instructions, fault-detection and measurement-system qualification, secure
  provisioning, calibration, serial traceability, throughput, rework and first-pass yield.
  Run the `factory` record checker in addition to the externally reviewed PVT evidence.
- G7: SKU/destination approvals, labels, instructions, declarations and responsible operators;
  complete cost model, price/margin and working-capital review; capacity, logistics, onboarding,
  spares, warranty, support and security response. Run `commercial` for cost completeness and
  retain the actual commercial approval. Regulatory submission and shipment are separate actions.
- Sustaining: field/production metrics, complaints and incidents, vulnerability deadlines,
  supplier changes, controlled ECOs, compatibility, revalidation, support funding, spares,
  customer communication, data/key retirement, service shutdown and disposal.

Use `record` for available tool checks and import actual external receipts. Prepare test plans,
fixtures, release documentation and evidence requests while external execution is pending;
do not fabricate results or request approval for unfinished packages. Respect existing action
authorization. Mark the exact gate blocked when its required evidence is unavailable.

After each configuration change, regenerate the release manifest and re-evaluate affected
gates. Anvil conservatively invalidates G3+ receipts for changed release inputs; carry-forward
requires a new documented impact review and new applicable receipts. Finish with the gate
result, package and blockers, then write and validate a `lifecycle` handoff.
