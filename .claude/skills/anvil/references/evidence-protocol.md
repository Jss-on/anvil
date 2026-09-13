# Evidence, manifests and handoffs

## Ledger

`anvil-results.tsv` has exactly these named fields:

```text
n<TAB>dimension<TAB>assertion<TAB>status<TAB>weight<TAB>evidence<TAB>traces
```

`assertion` is an ID from `lifecycle-plan.json`, or `REQ-HR-n` for a project requirement.
Rows have unique IDs and sequence numbers. Dimensions are electrical, simulation, layout,
manufacturing, testability, documentation, mechanical, integration, system, firmware,
security, compliance, or commercial. Weights are finite positive values for diagnostics.
Statuses: `not_run`, `pass`, `fail`, `blocked`, `error`, `na`; legacy `skip` remains unverified.
`evidence` is a project-relative JSON receipt. `traces` contains only exact `HR-n` identifiers
separated by semicolons, commas or whitespace; orphan IDs are errors.

Only `pass` or reviewed `na` can close a gate check. A requirement cannot be waived as NA;
change or retire it through a reviewed requirements baseline and impact assessment. Required
automatic checks likewise cannot be waived. A plan, a screenshot path, a cached log, or a high
score alone cannot close a release gate.

## Manifest

Declare all controlled source files, dependency models/libraries/locks, intermediate definitions,
and manufacturing outputs in project `artifacts`. `manifest <project>` verifies mandatory
roles and writes `release-manifest.json`, with per-file SHA-256 and a canonical configuration
digest. Do not include the ledger, receipts or manifest itself as design inputs.

Changes to any release file invalidate G3+ receipts. Regenerate the manifest, reassess the
impact and rerun/review applicable evidence; changing only the stored hash is not verification.
G0–G2 receipts bind the product profile and their reviewed files so later artifact additions
do not by themselves invalidate the opportunity decision. Changing intended scope, markets,
features or requirement path reopens those reviews.

## Automatic execution

Example `checks` configuration:

```json
{
  "AUTO-ERC": ["erc", "pcb/controller.kicad_sch"],
  "AUTO-DRC": ["drc", "pcb/controller.kicad_pcb"],
  "AUTO-SIM": ["sim", "sim"],
  "AUTO-BOM": ["bom-cost", "fab/bom.csv", "catalog/parts-catalog.csv"],
  "AUTO-PINOUT": ["pinout", "harness/harness.tsv", "system/icd.tsv", "harness/mates.tsv"],
  "AUTO-PRODUCT-BOM": ["product-bom", "bom/product-bom.csv"],
  "AUTO-BUDGET": ["sys-budget", "system/budgets.tsv"],
  "AUTO-FIT": ["fit", "mech"],
  "AUTO-MASS": ["mass", "mech"],
  "AUTO-DFM": ["mech-dfm", "mech"],
  "AUTO-FIRMWARE": ["firmware", "firmware/release.json"],
  "AUTO-FACTORY": ["factory", "manufacturing"],
  "AUTO-COST": ["commercial", "commercial/cost-model.csv"]
}
```

Configure the checks applicable to the product. `record <project> AUTO-...` runs the corresponding
checker, hashes its inputs/reports/transcript, records method, command, tool version and result,
then updates the ledger. Failed observations record `fail`; execution failures leave the row
unverified. Beginning a new recording clears the earlier pass, so an unsuccessful rerun cannot
silently retain that pass.

KiCad gets a fresh temporary report, validates exit status and report schema, and only then
replaces the report. Warnings, errors and reported exclusions all count; resolve them through
the project's reviewed rule settings rather than hiding them in a generic clean summary.
Simulation executes every declared corner separately and reads only that run's measure.
There is no `SKIP_NGSPICE` or cached-log fallback.

Firmware and factory checkers validate imported build/manufacturing records and cross-file
consistency. They do not operate a compiler, device, HIL rig or factory themselves. The skill
executes the project's approved build/test tools and imports their real records; the external
EVT/DVT/PVT reviews remain independently required.

## Reviewed and external evidence

Use `evidence/receipt-template.json` as a data contract, not as a passing example. A completed
receipt contains:

| Field | Contract |
|---|---|
| `schema_version` | `1` |
| `check_id`, `method` | Exact planned ID and verification method |
| `check_sha256` | Canonical digest of the planned criterion, gate, method and ownership record |
| `status` | `pass`, or justified `na` for an eligible lifecycle check |
| `producer` | `review` for engineering review; `external` for actual physical/authority/customer approval |
| `created_at` | Real ISO-8601 timestamp with timezone, not in the future |
| `profile_sha256` | SHA-256 of canonical project profile JSON |
| `release_sha256` | Configuration digest in `release-manifest.json`, required for G3+ |
| `files` | Nonempty map of relative paths to actual SHA-256; include inputs, raw evidence and approval record |
| `approval` | `reviewer`, `role`, `decision: approved`, and `record` path included in `files` |

Use `prepare <project> <check-id> <relative-evidence-files...>` to compute the canonical profile,
criterion and release hashes and write an unverified draft. G1/G2 drafts also bind the authoritative
requirements file. The draft cannot pass a gate until the real evidence and approval have been
supplied; preparing it never updates a ledger to pass. Preserve an existing draft rather than
overwriting it. An evidence preparer may compute hashes and format a record but cannot invent
the substantive review or attribute approval to someone.

For NA, use `status: na`, `approval.decision: not_applicable`, a specific `rationale` of at least
20 characters, and future timezone-qualified `expires_at`. Record the actual scope justification
and accountable approval. A failed test or missing resource is not a reason for NA.

Import with `record <project> <check-id> --evidence <receipt-path>`. The receipt must already
reside inside the project. It is validated before copying into the ledger's evidence directory.
For actual tests, include unit serial/revisions, procedure, conditions, calibrated instrumentation,
operator/time, raw measurements, pass criteria, rework/deviations and disposition. Anvil does
not sign these records, authenticate the named reviewer, or decide whether a lab is accredited.
Store authoritative approvals in the organization's controlled system; retain its signed export
and reference here. A hostile editor who can rewrite all files and receipts is outside this
filesystem integrity model. Use external signing/access controls when authenticity is required.

## Verification method and coverage

The requirement author chooses `test`, `simulation`, `analysis`, or `inspection` to suit the
claim and its conditions. A simulated plant response does not satisfy a physical environmental
test; a physical measurement does not establish a software dependency license inspection.
Change the planned method only through an approved requirements change. There is no automatic
upgrade/downgrade hierarchy.

`coverage <ledger> <requirements.tsv|legacy.md>` measures planned trace linkage, not passed
verification. Definitions alone count in legacy Markdown, and incomplete coverage cannot round
to 1.00. Gate evaluation uses exact check/requirement sets and receipts, never displayed ratios.
The TSV requirements path is mandatory for releases, including G0/G1 planning.

## Handoff

```sh
python anvil.py handoff product --write build --gate G3
bash validate-handoff.sh product/handoff.json
```

Schema 1 records an allowed command, relative project location, gate, actual verdict and blockers,
and hashes of the project config and ledger. Validation recomputes the gate and rejects invented
readiness, stale files, missing dependencies, unknown commands or invalid numeric metrics.
Every Anvil command must validate before chaining. A valid blocked handoff can carry work
forward but cannot authorize its blocked release action.
