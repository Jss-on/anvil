# Manufacturing transfer, assembly and factory validation

## G3 assembly and bring-up preparation

Write sequential illustrated work instructions with part IDs/quantities, orientation, polarity,
tools, fastening/torque/adhesive requirements, inspection criteria and safe handling. Reconcile
every consumed part with the product BOM in both directions. Include harness routing/strain
relief, enclosure closure, firmware programming and calibration access. Supplier/process-specific
instructions control soldering, moisture, ESD, cleaning, seals and traceability.

The bring-up plan identifies configuration, serials, instrumentation, calibrated ranges,
current/voltage limits, staged power domains, safe outputs, expected observations, stop conditions
and rework capture. Hazardous energization, motion and battery testing need an actual approved
procedure, responsible operator and session action authorization. Do not reuse a drone, medical,
or mains procedure as a generic product default.

## EVT and DVT

Record first power, rails/clocks/reset, peripheral interfaces, programming/debug, core function,
fault states and integration with mechanics/harnesses. Tie raw results to unit serial, hardware,
firmware/bootloader, settings and rework. DVT uses representative production intent, justified
sample/corner/environment/reliability profiles and intended-user validation. Track deviations,
failures, corrective actions and regression results; a repaired prototype is not an untouched
production-intent sample.

## PVT and process transfer

Transfer released BOM/drawings, suppliers/alternates, firmware/programming, assembly and
inspection instructions, tooling, material handling and change controls. Qualify people and
equipment. `manufacturing/control-plan.csv` records operation, characteristic/limit, method,
fixture, frequency, owner, reaction plan and record. Select ICT/flying probe/boundary scan,
functional tests or other methods according to fault coverage and product constraints.

Demonstrate that tests detect representative defects and that measurements can distinguish
acceptable product: fault injection/known bad samples, repeatability/reproducibility, guardbands,
calibration/traceability and fixture maintenance. Validate provisioning, test privilege separation,
calibration schema, data upload, rework, retest and repair. Document cycle time, throughput,
capacity, first-pass yield, final yield, scrap, rework, escapes and acceptance targets.

## Executable factory record check

`factory <manufacturing-directory>` reads `acceptance.json`:

```json
{
  "hardware_revision": "A",
  "firmware_sha256": "<actual release binary SHA-256>",
  "minimum_units": 30,
  "first_pass_yield": 0.95,
  "fixtures": {"FCT-01": "3"}
}
```

The numbers above are examples; set justified pilot size/yield limits for the actual process.
Add this approved `acceptance.json` under the release artifact role `factory_policy` before PVT
recording. Changing a sample, yield, fixture or configuration criterion then invalidates the
release baseline and its reviews, instead of silently relaxing acceptance after a failed pilot.
`unit-records.csv` fields: serial, lot, hardware_revision, firmware_sha256, fixture_id,
fixture_revision, calibration_due, operator, timestamp, attempt, rework_reference, result,
measurement_record, provisioning_record. Timestamps include timezone. Calibration must cover
the actual test time. Each serial starts at attempt 1 with no omitted/duplicate attempts;
retest/rework needs a real disposition record. Evidence paths are relative to the factory folder.

The checker rejects mismatched configuration/fixture revisions, expired calibration, incomplete
records and hidden test attempts. It reports both first-pass and final yield; the agreed minimum
sample count, first-pass target and all units' final acceptance must pass. It does not measure
hardware or validate the factual truth of imported records. G6 also requires external review
of fault coverage, measurement qualification, provisioning and actual process capability.

Tie each shipped unit to its configuration, measurement/provisioning/calibration records and
release authority. Preserve failed attempts and nonconformances. Never copy a later configuration
over a historical unit record or log secret keys/passwords as provisioning evidence.
