# Product lifecycle and gates

This workflow implements the September 2026 hardware lifecycle research. The bundled
`templates/anvil-project/lifecycle-checks.csv` preserves HW-001 through HW-075. Nineteen
additional `-PLAN` checkpoints bring multi-stage obligations into G1. Automatic checks and
each project's requirements are added by `plan`; a project cannot delete the bundled obligations.

## Gates and evidence

| Gate | Decision and owner | Required output | Successful label |
|---|---|---|---|
| G0 | Opportunity; product owner | Intended use, problem, users, environment, markets, stop criteria, initial risks/assumptions | `OPPORTUNITY_REVIEWED` |
| G1 | Requirements; systems lead with product/regulatory owners | Measurable requirements and methods/due gates; classification, risk and commercial plans | `HRS_READY` |
| G2 | Architecture; engineering and safety leads | Allocations, ICDs, worst-case budgets, feasibility evidence, safety/security/test architecture, manufacturer feedback | `ARCHITECTURE_READY` |
| G3 | Prototype release; engineering/manufacturing | Controlled design package, compatible revisions, verified tools, DFM/DFA and bring-up preparation | `PCB_FAB_READY`, `ASSEMBLY_READY`, or `PRODUCT_BUILD_READY` |
| G4 | EVT; engineering/test | Identified prototype bring-up, rework, core performance, integration and failure investigation | `EVT_COMPLETE` |
| G5 | DVT; quality/test/regulatory | Representative design qualification, risk-based samples/corners, user and requirement validation, deviation disposition | `DESIGN_QUALIFIED` |
| G6 | PVT; manufacturing/quality | Process transfer and pilot capability, test coverage, calibration, provisioning, traceability, yield/rework/capacity | `PRODUCTION_READY` |
| G7 | Market release; product/quality/regulatory/operations | SKU/destination obligations, commercial approval, logistics, support and shipment authority | `MARKET_READY` |
| Sustaining | Periodic/change/retirement review; service/security/quality | Field metrics, incidents, ECO impact, revalidation, updates, spares, funded support and retirement | `SUSTAINING_REVIEWED` |

Gates are cumulative. `G5_BLOCKED`, for example, also includes unresolved earlier work.
EVT, DVT and PVT are industry planning conventions; a regulated product must map them onto its
actual quality system, legally required controls, customer process, and records. Sample counts,
reliability durations and acceptable yield come from risk and business requirements, not a
universal stage name. A gate label reports evidence readiness and does not execute a purchase,
deployment, regulatory filing, production release in a separate system, or shipment.

## Concurrent tracks

| Track | Start at G1/G2 | G3 package | G4–G6 evidence | G7 and sustaining |
|---|---|---|---|---|
| Electronics | Architecture, interfaces, component risks, power/thermal/timing budgets | Schematics, active rules, layout, libraries, stackup, BOM, manufacturing exports | Bring-up, tolerance/fault/environment tests, manufacturing control | Supplier monitoring, configuration and substitution revalidation |
| Firmware/cloud | HW/SW allocation, boot/debug, resource budgets, safe states, data/security architecture | Reproducible build, binary/lock/SBOM, board compatibility, test hooks | Target/HIL, failure/recovery/update tests, production identity and debug controls | Support duration, vulnerability response, staged updates, service dependencies |
| Mechanics/harness | Datums, tolerances, materials/process, interfaces, ingress/thermal/service requirements | CAD/drawings/exports, fit and process review, explicit endpoint/wire/mate definition | Real assembly/fit, environmental/dynamic tests, fixtures/tooling and process validation | Serviceability, spare parts, approved materials and effects of substitutions |
| Supply/manufacturing | Source strategy, DFM/DFA, test coverage and provisioning plans, volume economics | Complete assembly/build instructions, test access, quote and catalog snapshots | First articles, trained operators, measurement and fault-coverage studies, pilot yield | Capacity, inspection/rework, traceability, recalls and continuity |
| Quality/compliance | Intended-use classification, hazards, destinations, dates, standards and route | Design controls, risk-control implementation, test and conformity plans | Qualification and required external laboratory/authority/customer records | SKU release, labeling/operators, complaints/reporting, field actions |
| Commercial/service | Price, volume, cost, NRE, working capital and support assumptions | Packaging/logistics/onboarding/service design | Intended-user validation, capacity and service rehearsal | Margin approval, warranty/returns, support staffing, spares and retirement funding |

## Project contract

`anvil-project.json` declares:

- `schema_version: 1`, `name`, `hardware_revision`, `release_kind` (`pcb`, `assembly`, `product`), `target_gate`.
- `sectors`: any of `embedded`, `connected`, `robotics`, `industrial`, `medical`, `automotive`.
- `markets`: any of `US`, `EU`, `GB`, `NI`, `TW`. GB and NI are separate; select both for UK.
- `features`: `electronics`, plus applicable `firmware`, `mechanics`, `radio`, `battery`,
  `cloud`, `taiwan_export`. Radio/cloud products also select `connected`. Feature omissions
  require review of the actual intended product; they are not a scoring shortcut.
- `requirements`: authoritative TSV path. `verification_methods` may add planned methods;
  simulation requirements themselves force the simulation check even if this list is empty.
- `artifacts`: role to explicit relative file list, including dependencies. No globs, URLs or
  files outside the project. Vendor external libraries/models inside the controlled project.
- `checks`: applicable `AUTO-*` ID to a command array. These invoke only built-in checks,
  with project-relative operands; they are not arbitrary shell commands.

Run from the project parent, using the resolved installed Anvil executable:

```sh
python /path/to/anvil.py init sensor --scope product --sectors embedded,connected --markets US,EU,GB,NI,TW --features electronics,firmware,mechanics,radio,battery,taiwan_export
# Define real requirements and populate project configuration before planning.
python /path/to/anvil.py plan sensor
python /path/to/anvil.py manifest sensor
python /path/to/anvil.py record sensor AUTO-ERC
python /path/to/anvil.py record sensor AUTO-DRC
python /path/to/anvil.py gate sensor G3
python /path/to/anvil.py handoff sensor --write build --gate G3
```

Templates are intentionally incomplete and cannot produce a green gate without actual work.
`lifecycle-plan.json` lists the exact applicable IDs, gate, method, authority, criterion and owner.
`anvil-results.tsv` preserves existing rows when planning again. If product applicability changes,
archive the previous ledger and impact assessment before removing no-longer-applicable rows.

### Release artifact roles

| Scope/feature | Required roles |
|---|---|
| Every G3 release | `schematic`, `pcb`, `project`, `rules`, `gerbers`, `drill` |
| Assembly or product | `bom`, `placement`, `catalog`, `assembly` |
| Product | `icd`, `harness`, `product_bom`, `budgets` |
| Mechanics | `cad`, `mechanical_export`, `mechanical_measures` |
| Firmware | `firmware_source`, `firmware_lock`, `firmware_binary`, `firmware_manifest` |

Add other roles for source models, assertion tables, endpoints, mates, dependency locks,
process specifications and controlled drawings. Every dependency read by a G3 automatic check
must be present in the manifest. The approved factory acceptance policy must also be manifested
under `factory_policy` before PVT recording. Factory and commercial result records are later evidence; their
receipt binds them to the released configuration without adding each production record to the
design baseline. Manifest completeness and correct export layer/variant selection remain
explicit engineering review obligations HW-013 through HW-020.

Multi-board ERC and DRC recording runs on every schematic/board in the corresponding role.
For additional independent simulation sets, mechanical assemblies or integration partitions,
declare their verification as project requirements and retain their reviewed execution evidence.
Do not assume a single directory check proves an entire complex system.

## Sector tailoring

- Embedded/connected: account/cloud/local/offline behavior, device identity, permissions,
  personal data, update/recovery, vulnerability handling and disclosed support commitments.
- Robotics/industrial: distinguish robot, cell, machine, installation and service robot scope;
  derive stop/restart/maintenance states and safety functions; verify actual payload, tooling,
  safeguards and interfaces; require FAT/SAT where applicable. Industrial cyber processes and
  commissioning responsibility extend beyond the controller board.
- Medical: intended medical purpose, classification and jurisdiction route; applicable QMS,
  linked risk management/design controls, software lifecycle, electrical safety, usability,
  clinical/performance evidence, design transfer and post-market reporting.
- Automotive: OEM/supplier responsibility and assumptions, functional safety, SOTIF and
  cybersecurity applicability, customer-required APQP/control plan/PPAP and integration evidence.
  Vehicle-level approval responsibilities are not fulfilled by component documentation alone.

See `standards.md` for authoritative starting points and date-sensitive obligations. Sector
profiles add checks; they do not automatically classify a device or determine a certification route.

## Gate review checklist

- Does the evidence address the exact criterion, conditions, sample and configuration?
- Are raw records, deviations, method limitations, calibration and responsible approvals present?
- Are all due requirements verified using the planned method, with exact trace IDs?
- Are linked files unchanged, inputs complete, tool execution successful, and assumptions valid?
- Are exclusions specific, owned, approved, time-bounded and still applicable?
- Are unresolved safety/compliance/production risks visible to the actual release authority?
- Can the next team reproduce the build/test and distinguish prototype from production intent?

Do not turn a receipt into a substitute for substantive technical review. Anvil checks structure
and integrity; approval identity and the truth of externally supplied records belong to the
organization's controlled review system.
