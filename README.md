# Anvil

**Hardware product development with explicit release gates and revision-bound evidence.**
Version **0.5.0** · Claude Code and Codex plugins · Proprietary license

Anvil carries a product from requirements and architecture through PCB fabrication, firmware,
mechanics, integration, EVT/DVT/PVT, market release, support and retirement. Its commands perform
authorized engineering work and keep missing external tests or approvals visible as blockers.

```mermaid
flowchart LR
  G0["G0 Opportunity"] --> G1["G1 Requirements"] --> G2["G2 Architecture"]
  G2 --> G3["G3 Prototype release"] --> G4["G4 EVT"] --> G5["G5 DVT"]
  G5 --> G6["G6 PVT"] --> G7["G7 Market release"] --> S["Support and retirement"]
  S -->|Controlled changes| G2
```

Electronics, firmware/services, mechanics, supply/manufacturing, quality/compliance and commercial
work proceed concurrently. The [lifecycle protocol](.claude/skills/anvil/references/lifecycle-protocol.md)
defines gates, owners, artifacts and checklists. The [research report](research/hardware-product-lifecycle.md)
and [original assessment](ASSESSMENT.md) explain the upgrade's basis.

## Use with Claude Code

Install the repository's marketplace in Claude Code, then its `anvil` plugin:

```text
/plugin marketplace add Jss-on/anvil
/plugin install anvil@anvil
```

For local development, load the actual packaged directory with `claude --plugin-dir ./claude-plugin`.
The repository's canonical command and skill files also support project-local development.
Do not assume editing this checkout changes an already cached installation; reload the local
plugin or update the installed package after publishing an authorized release.

| Command | Purpose |
|---|---|
| `/anvil` | Bounded custom metric loop or task routing |
| `/anvil:requirements` | Requirements, methods, owners, verification gates and applicability |
| `/anvil:build` | Concurrent product development, default target G3 |
| `/anvil:lifecycle` | Bring-up, EVT/DVT/PVT, market release and sustaining |
| `/anvil:improve` | Cost/area/mass/margin optimization with non-regression checks |
| `/anvil:evals` | Run analysis and evidence/gate review |

Examples:

```text
/anvil:build Goal: battery-powered environmental monitor Release: product Target: G3
/anvil:lifecycle Scope: ./sensor Target: G5 Action: execute
/anvil:improve Metric: bom_cost Scope: ./sensor Iterations: 10
```

## Use with Codex

Install and sign in using the [official Codex CLI setup](https://learn.chatgpt.com/docs/codex/cli).
Install Anvil's engineering tools under [Run the checks directly](#run-the-checks-directly).
From this checkout, register its local marketplace and install the native Codex plugin:

```sh
codex plugin marketplace add .
codex plugin add anvil@anvil
codex -C . --sandbox workspace-write
```

The [Codex marketplace](.agents/plugins/marketplace.json) selects the self-contained package
in [`plugins/anvil/`](plugins/anvil/.codex-plugin/plugin.json). Codex loads its `$anvil` skill;
Claude Code uses the separate marketplace and package above. This follows Codex's
[native plugin and marketplace format](https://learn.chatgpt.com/docs/enterprise/plugin-management).

Start a **new thread** after installation. In Codex CLI or the IDE extension, type `$` to select
Anvil, or paste a prompt such as:

```text
$anvil build Goal: battery-powered environmental monitor Scope: ./build-output/sensor Release: product Target: G3
$anvil lifecycle Scope: ./build-output/sensor Target: G5 Action: review
$anvil improve Metric: bom_cost Scope: ./build-output/sensor Iterations: 10
```

Send one prompt at a time. The skill also routes `requirements`, `evals`, and custom metric
loops. All six workflows use the same engineering protocols, Python checks, receipts and gates
as the Claude Code plugin. In the Codex app, select Anvil and describe the task in a new thread.

To work in an existing hardware repository, launch `codex -C <project-directory>` and use
`Scope: .`; installed Anvil tools resolve from the plugin cache. When working in this checkout,
`build-output/sensor` is ignored by Git; maintain the product's own source history and release
archive. Keep project outputs outside the plugin cache.

For a noninteractive review of an existing project, use single quotes so PowerShell and Bash
preserve the `$anvil` skill mention. See the [Codex CLI reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli).

```sh
codex exec -C . --sandbox workspace-write 'Use $anvil lifecycle Scope: ./build-output/sensor Target: G3 Action: review. Report the actual gate result and blockers.'
```

For development without installation, open this checkout and ask Codex to read
`.claude/skills/anvil/SKILL.md` and the desired `.claude/commands/anvil/<workflow>.md` directly.
Use the checkout's `scripts/` and `templates/`. Installed plugins are cached copies; editing
this repository does not update an existing session.

Scope tailoring supports embedded/connected, robotics/industrial, medical and automotive
products; US, EU, Great Britain, Northern Ireland and Taiwan markets; Taiwan manufacture/export;
firmware, mechanics, radio, battery and cloud features. Classification and dates are reviewed
per product. Selecting a profile does not certify a design.

## Run the checks directly

Python 3.10+ standard library is the core dependency. Git tracks controlled source; KiCad CLI
is needed for ERC/DRC/exports and standalone ngspice for simulation. Use only the CAD, firmware,
HIL and authoring tools the project actually needs. On Windows, `scripts\doctor.cmd` locates
Git Bash; direct `uv run --no-project --offline python scripts/anvil.py ...` also works.

```sh
python scripts/anvil.py doctor --require-build
python scripts/anvil.py init ../sensor --scope product --sectors embedded,connected --markets US,EU --features electronics,firmware,mechanics,radio,battery
# Populate real requirements, artifacts and checks in the generated project.
python scripts/anvil.py plan ../sensor
python scripts/anvil.py manifest ../sensor
python scripts/anvil.py record ../sensor AUTO-ERC
python scripts/anvil.py record ../sensor AUTO-DRC
python scripts/anvil.py gate ../sensor G3
python scripts/anvil.py handoff ../sensor --write build --gate G3
```

Initialization creates incomplete templates and cannot produce a ready verdict by itself. For an
existing hardware project, copy/add the required files individually and preserve its existing work.
See the [CLI contract](.claude/skills/anvil/references/metrics.md) and
[evidence schema](.claude/skills/anvil/references/evidence-protocol.md) for command arrays,
receipts, strict table formats and exit statuses.

## Readiness means evidence

- All **75 research checklist items** are bundled, with **19 early applicability checkpoints**.
  Planning adds applicable automatic checks and every project requirement; deleting a required
  ledger row cannot improve readiness.
- `pass-rate` and `coverage` are diagnostics. `gate` requires exact due checks, matching methods,
  scoped artifacts, current file hashes and substantive review/external records.
- G3 distinguishes `PCB_FAB_READY`, `ASSEMBLY_READY` and `PRODUCT_BUILD_READY`. G5 is
  `DESIGN_QUALIFIED`, G6 `PRODUCTION_READY`, and G7 `MARKET_READY`. Earlier gates remain required.
- KiCad reports must come from successful fresh runs with valid schemas and active adjacent
  rule/project files. Simulation runs every declared corner and never falls back to old logs.
- BOM/cost/mass/budget and wiring inputs have strict numeric and source-join checks. Firmware
  and factory records identify builds, unit revisions, fixtures/calibration, attempts and rework.
- Changed design inputs invalidate G3+ evidence. Handoffs recompute the actual verdict and
  include blockers; stale or unsupported readiness is rejected before chaining.

Physical measurements, factory qualification and legal/customer approvals must come from actual
execution and responsible reviewers. Anvil verifies record structure and file integrity; it does
not authenticate approval identities, certify products, or replace a regulated quality system.
The filesystem receipt model assumes trusted editors; externally signed records/access controls
are needed where adversarial tampering or authenticated approvals are in scope.

No remote publication, supplier contact, purchase, hardware energization, firmware deployment,
filing or shipment happens without the session's authorization for that action. Local work and
reviewable packages proceed without repeated permission requests.

## Migrate from 0.4

1. Archive the old ledger as history. Add `anvil-project.json`, structured
   `hrs/requirements.tsv`, complete artifact roles and explicit check command arrays.
2. Run `plan`; migrate a prior observation only after its actual input/configuration, execution
   and review provenance is established. Old `evidence:path` strings are not receipts.
3. Put `<board>.kicad_dru` beside its matching PCB/project/schematic. A nested `pcb/rules/`
   deck is inactive. Only the reviewed JLCPCB two-layer starter is bundled.
4. Add `circuit` to simulation rows. Declare each swept parameter on its own `.param` line.
   `SKIP_NGSPICE` and implicit cached logs are rejected.
5. Replace subsystem-only ICD endpoints with physical pins, qualified ratings, voltage/protocol
   and mate pin lists. Product BOM `source` becomes `relative.csv#item_id`; budget sources use
   `relative.json#key` with explicit value and units. Record firmware/build and factory evidence.
6. Generate the release manifest, record/review checks, and run `gate`. Legacy `verdict <tsv>`
   stays `FAB_BLOCKED`. Renew affected receipts after configuration changes.

## Develop and verify

Canonical sources: `.claude/commands/`, `.claude/skills/anvil/`, `scripts/` and `templates/`.
`claude-plugin/` and `plugins/anvil/` are their byte-for-byte installable mirrors for Claude Code
and Codex. Edit canonical files, then sync. Each package has its own native manifest.

```sh
python -B tests/test_anvil.py
bash scripts/sync-plugin.sh
bash scripts/sync-plugin.sh --check
bash scripts/score-e2e-capability.sh
```

For local Codex updates, use `$plugin-creator` to refresh Anvil from this checkout's `anvil`
marketplace. Its update flow adds a version cachebuster and reinstalls the plugin; start a new
thread afterward. The base version stays aligned with `VERSION`.

Tests cover valid observations and the assessment's negative cases, cumulative lifecycle gates,
stale receipts/handoffs, sector/market tailoring, firmware/cost/factory records and both isolated
installed payloads, including workflow links. CI runs the Python contracts on Linux and Windows
and verifies both packages.
Optional native checks run with `ANVIL_NATIVE_TESTS=1` when KiCad/ngspice are installed.
`score-e2e-capability.sh` runs executable software checks; it no longer reports grep matches
as end-to-end physical product capability.
