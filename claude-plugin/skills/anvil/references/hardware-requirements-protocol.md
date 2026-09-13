# Hardware and product requirements

Requirements are the common contract for hardware, firmware, mechanics, manufacturing,
compliance and support. Start with intended use, users, operating environment, market variants,
production location, expected volume/life and commercial stop criteria. Record goals, constraints,
hazards, assumptions, ownership, rationale and exclusions in `hrs/requirements.md`.

## Authoritative table

`hrs/requirements.tsv` columns: `id`, `statement`, `units`, `conditions`, `method`, `gate`, `owner`.

```text
id	statement	units	conditions	method	gate	owner
HR-1	3V3 output stays within 3.3 V +/- 3 percent	V	Vin 4.5..5.5 V; load 0..1 A; Ta -10..60 C	simulation	G3	Power lead
HR-2	Recovers to safe outputs after brownout within 100 ms	ms	Production-intent board; min/max input ramp; worst load	test	G5	Firmware/test lead
HR-3	Every supported SKU has approved destination labeling	boolean	All release markets and languages	inspection	G7	Regulatory owner
```

Each quantitative statement names limit direction, value/tolerance, units and conditions.
Qualitative requirements use observable pass/fail criteria, with `boolean` or another meaningful
unit instead of invented numbers. `owner` is accountable for closure; `gate` is the verification
due date in the lifecycle. Methods are test, simulation, analysis and inspection. Select the
method that answers the claim, not a universal hierarchy or the easiest available tool.
Split mixed claims into separate requirements when they need different methods or gates.

Stable `HR-n` IDs never change meaning or get silently reused. Retired requirements and their
reasons remain in the controlled history; removing an active row requires an impact review.
`plan` creates `REQ-HR-n` checks. `coverage` checks exact trace links and rejects orphan IDs;
it does not validate prose measurability or prove that planned tests were executed.

## Elicitation checklist

1. Function/performance and intended-user tasks, including startup, degraded behavior and misuse.
2. Supply range, transients, sequencing, inrush, reverse input, brownout, quiescent and load power.
3. Interfaces at both endpoints: physical pin, direction, voltage/current, timing/protocol,
   protection, connector/mate, shielding, mechanical datums and firmware ownership.
4. Mechanics: envelope, tolerances, mounting, material/process, thermal path, sealing, service
   access, strain relief, wear parts, assembly and packaging. Specify actual ingress/test profiles.
5. Environment/reliability: temperature, humidity, vibration/shock/drop and lifetime/duty cycle
   with a justified test method and acceptance limits. Avoid generic claims such as "rugged".
6. Firmware/services: boot, partitions, timing/memory/power, watchdog/fault states, identities,
   credentials, updates/recovery, offline/cloud behavior, diagnostics, privacy and support duration.
7. Safety/security: hazard analysis, risk controls, access/maintenance states, threat model,
   required residual-risk acceptance, verification and reporting responsibilities.
8. Manufacturing/supply: fabricator/process capability, quality/acceptance class and edition,
   yield, test coverage, calibration, traceability, repair/rework, alternates and lifecycle risks.
9. Compliance/market: intended-use classification, SKU destinations, dates, conformity route,
   evidence, labels/languages/operators, transport, environmental/producer and post-market duties.
10. Commercial/service: cost at volume, NRE, price/margin, capacity, working capital, logistics,
    warranty/returns, spares, support funding, customer communication and retirement.

A part number mandated by the customer is a constraint with provenance; other parts are design
choices. A quality class, derating factor, clearance or test sample count must be selected for
the actual product/process/risk. Neither "medical" nor "above 30 V" determines these by itself.

G1 review covers the requirements baseline, classification and verification plan. Later physical
requirements stay not_run until their due gate; this is expected, and is different from pretending
their tests passed. Unknowns get an owner, consequence and next experiment. Work continues on
independent tasks while a consequential product decision is pending.
