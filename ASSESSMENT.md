**Anvil has useful engineering workflows, but its current verification gates do not justify autonomous `FAB_READY` decisions.** It is suitable for supervised experimentation. Several ordinary failure conditions produce passing results, including missing design files, failed simulations, missing evidence, and inactive fabrication rules.

Assessed on 13 September 2026 at commit `f01f41a`, advertised version `0.4.0`. The review covered all 87 tracked files, with canonical instructions read directly and the generated plugin checked for byte parity. The repository contains 1,815 lines of canonical instructions, 935 lines of root Bash scripts, and 209 lines of test scripts. This is primarily a Claude Code instruction package with a scoring backend; phase execution, ledger updates, rollback decisions, and many engineering reviews are delegated to the model.

| Area | Assessment |
|---|---|
| Requirements and workflow design | Broad coverage of board and product deliverables; explicit requirements, evidence, and rollback contracts |
| Electrical and simulation verification | Release blockers: failed or incomplete verification can look successful |
| Mechanical and system verification | Useful initial checks, with significant geometry and cross-file consistency gaps |
| Packaging and updates | Byte parity passes; release metadata and bundled resources are incomplete |
| Security and safety | Small executable surface, but safety decisions rely on model instructions and editable ledger claims |
| Testing | All existing tests pass; CI and fixtures do not exercise the principal integration failures |
| Maintainability | Modest implementation size; fixing existing checks has higher value than adding more commands |

Validation performed:

| Check | Observed result |
|---|---|
| `bash tests/score.test.sh` | 13/13 passed, including plugin parity and two handoff cases |
| `bash tests/mech.test.sh` | 5/5 passed |
| `bash tests/system.test.sh` | 5/5 passed |
| Bash syntax validation | All 11 tracked `.sh` files passed `bash -n` |
| `claude plugin validate claude-plugin` | Manifest passed |
| Strict marketplace validation | Failed: marketplace `0.4.0` conflicts with plugin manifest `0.2.1` |
| `doctor.sh --require-build` | `DOCTOR: READY` on this machine |
| `doctor.sh --require-product` | Blocked: neither build123d nor CadQuery is installed |
| Targeted negative probes | Reproduced the defects below using isolated temporary inputs, real ngspice, and KiCad 10.0.5 |

The local environment was Windows with Git Bash, Node 24.14.0, Python 3.13.7 through uv, KiCad 10.0.5, and Claude Code 2.1.267. The documented KiCad 9 environment, a fresh installed-plugin command session, a complete spec-to-fabrication build, and physical hardware performance were not validated. Manifest validation is not a command-execution test.

The following findings are ranked by practical impact. P1 means fix before relying on autonomous fabrication-readiness decisions; P2 means a correctness or release-quality issue to address next.

1. **[P1] The final verdict accepts incomplete, unsupported acceptance ledgers.**

   [The verdict](C:/dev/anvil/scripts/score-anvil.sh:597) initializes coverage to `1.00` and only checks the HRS when explicitly supplied as a second argument. It neither requires the necessary dimensions/assertions nor validates evidence paths. [The score calculation](C:/dev/anvil/scripts/score-anvil.sh:433) accepts rows with only five columns and excludes `skip` rows. A single passing documentation row with no evidence produced `FAB_READY`. Explicitly skipped ERC, DRC, and simulation rows also produced `FAB_READY`. An existing HRS with an uncovered requirement was ignored by the default invocation; supplying that HRS explicitly correctly blocked the result.

   This directly affects the [build command's default verdict invocation](C:/dev/anvil/.claude/commands/anvil/build.md:220). Human-review requirements also have no independently checked approval field: the scorer trusts the same editable status column for every row.

   Minimum correction: validate the ledger schema and readable evidence, require the applicable acceptance set, resolve the HRS by default, and require explicit completion of mandatory and human-review rows. A partial progress score must not establish fabrication readiness.

2. **[P1] ERC and DRC can reuse a previous clean report after the current tool run fails.**

   [Both wrappers](C:/dev/anvil/scripts/score-anvil.sh:482) suppress tool errors with `|| true` and then accept any nonempty report at the output path. A nonexistent schematic plus a previous clean JSON report returned `ERC_VIOLATIONS: 0`; a nonexistent board returned `DRC_VIOLATIONS: 0`. Both exited successfully. With malformed report JSON, ERC printed an empty violation count and still exited zero because `echo` hid the parser failure.

   Minimum correction: reject missing inputs, distinguish a completed check with violations from execution failure, use a fresh report for each run, validate its structure, and propagate parser errors.

3. **[P1] Simulation does not execute declared corners and can pass after a failed run.**

   [The evaluator](C:/dev/anvil/scripts/score-anvil.sh:104) reads only the first five assertion columns; it never uses `corners`. [The runner](C:/dev/anvil/scripts/score-anvil.sh:500) executes each circuit once. A real ngspice circuit with nominal output 3.3 V and declared `VIN=1,5` corners passed a 3.2–3.4 V assertion after measuring only nominal operation.

   Separately, every `.log` in the directory is pooled by measure name, without binding it to a successful current run. A broken circuit plus an old passing log returned `SIM_PASS: 1/1` despite reporting ngspice's failure. No circuit files at all can also pass from old logs. These behaviors contradict the [corner cross-product contract](C:/dev/anvil/.claude/skills/anvil/references/simulation-protocol.md:41).

   Minimum correction: execute and identify every declared corner, require a successful current run for each, and reject missing or nonfinite measurements. Keep any deliberate log-replay mode separate from build acceptance.

4. **[P1] The documented fabrication-rule location is inactive.**

   [Layout instructions](C:/dev/anvil/.claude/skills/anvil/references/layout-protocol.md:18) put the deck at `pcb/rules/<fab>.kicad_dru`, but the DRC wrapper does not install or load that file. In a generated KiCad board, a 0.100 mm trace produced zero violations with the shipped deck in `rules/jlcpcb.kicad_dru`. Copying the identical deck to the active `board.kicad_dru` beside `board.kicad_pcb` produced a `track_width` violation against the deck's 0.127 mm minimum. This is a confirmed rule-loading failure, independent of the stale-report bug.

   Minimum correction: install the selected deck as the project's active custom-rules file and include a deliberately violating board in integration checks. KiCad documents custom rules as project artifacts that must accompany the board and project files. [KiCad custom-rules documentation](https://docs.kicad.org/9.0/en/pcbnew/pcbnew.html#custom-design-rules).

5. **[P1] The pinout gate checks labels and grammar, not electrical interface consistency.**

   [The ICD map](C:/dev/anvil/scripts/score-anvil.sh:313) retains only ID and kind; it discards endpoints, pin counts, voltage, protocol, and current. Ampacity uses the harness's independently entered current. Replacing all endpoints with nonexistent connectors still returned zero violations. Changing an ICD current requirement to 1000 A while leaving the harness at 22 A also returned zero. Nonnumeric harness current bypasses the comparison. An explicitly supplied missing mates file is silently ignored.

   Minimum correction: reconcile endpoints against the actual subsystem/netlist data, validate currents against the ICD, require finite values, and fail when a requested mates table is absent. Enforce the documented unique mate coverage instead of mere set membership.

6. **[P2] Coverage and rounded scores can falsely claim completeness.**

   [Coverage](C:/dev/anvil/scripts/score-anvil.sh:469) searches the entire input for `HR-n`, including comments and unrelated fields. A comment containing all requirement IDs produced `REQ_COVERAGE: 1.00` with an empty traces column. An orphan `HR-999` emitted a warning but did not fail, contrary to the requirements command's validation contract.

   The verdict also compares the [two-decimal display score](C:/dev/anvil/scripts/score-anvil.sh:459) to its target. A documentation ledger with passing weight 1000 and failing weight 1 produced `FAB_READY` at target 1.00 because 1000/1001 rounded up. Coverage has the same precision hazard for sufficiently large requirement sets.

   Minimum correction: parse the actual trace/spec fields, reject orphan references, and make completeness decisions using counts or unrounded values.

7. **[P2] Numeric inputs and claimed source provenance are insufficiently validated.**

   Confirmed examples from the [BOM](C:/dev/anvil/scripts/score-anvil.sh:158), [product BOM](C:/dev/anvil/scripts/score-anvil.sh:379), [budget](C:/dev/anvil/scripts/score-anvil.sh:413), and [mechanical-measure](C:/dev/anvil/scripts/score-anvil.sh:283) evaluators:

   | Input | Observed output |
   |---|---|
   | BOM quantity `not-a-number` | `BOM_COST: 0.00 USD` |
   | One USD-priced part plus one JPY-priced part | Values added directly; `BOM_COST: 101.00 JPY` |
   | Product price −20, mass −50, nonexistent source path | Negative cost and mass accepted |
   | Demand 100, capability 1, derate 100 | `SYS_BUDGET: 1/1` |
   | `interference_mm3: null` | Coerced to zero; `FIT_PASS: 1/1` |

   The product-BOM command does not read a pinned catalog; it merely requires a nonempty source string. System budgets compare supplied numbers without reconciling them to the BOM or module catalog. Thus the [claimed product-catalog joins](C:/dev/anvil/.claude/skills/anvil/references/metrics.md:74) are instructions for the model, not implemented safeguards.

   Minimum correction: require finite, appropriately bounded numeric values and consistent currencies; reject invalid quantities instead of converting them to zero; reconcile claimed catalog and rollup inputs where acceptance depends on them.

8. **[P2] Geometry checks accept invalid meshes and understate some board envelopes.**

   [Mesh degeneracy detection](C:/dev/anvil/scripts/score-anvil.sh:247) only detects repeated vertices. A closed tetrahedral connectivity pattern made entirely from four collinear, zero-area triangles returned `MESH_DEFECTS: 0`. Edge incidence alone does not establish a valid manufacturable solid.

   [Area calculation](C:/dev/anvil/scripts/score-anvil.sh:192) samples arc start/mid/end points without calculating intermediate extrema. A rotated radius-10 semicircle had a true enclosing rectangle of 291.4 mm² but returned `AREA_MM2: 200.0`. This is an error in the promised bounding box, separate from the documented choice to use bounding-box area instead of polygon area.

   Minimum correction: reject zero-area/nonfinite facets and calculate the extrema of supported outline primitives, or reject unsupported geometry explicitly. Add the two failing cases to existing tests.

9. **[P2] The plugin's stale version can prevent users receiving updates.**

   [The distributable manifest](C:/dev/anvil/claude-plugin/.claude-plugin/plugin.json:4) still declares `0.2.1`, while VERSION, the skill, and marketplace advertise `0.4.0`. Claude's strict marketplace validator reproduced the mismatch. Plugin-manifest version takes precedence, and unchanged versions can keep existing users on cached contents. [Claude Code version-resolution documentation](https://code.claude.com/docs/en/plugin-marketplaces#version-resolution-and-release-channels).

   Minimum correction: maintain one release version source, update the distributable manifest, and validate version agreement in CI. The byte-parity check deliberately excludes manifest content and cannot catch this.

10. **[P2] The installed payload omits resources that the workflows claim to ship.**

    [The sync mapping](C:/dev/anvil/scripts/sync-plugin.sh:22) packages commands, skill references, and three shell scripts. It does not package the fabrication template or `doctor.cmd`. The installed layout instructions therefore refer to a template unavailable inside the plugin. The repository itself provides only a JLCPCB two-layer deck, despite documenting JLCPCB, PCBWay, and generic presets and claiming both board-setup and rule-deck templates.

    Minimum correction: bundle the resources required by the supported path, and accurately describe the available presets. Smoke-test from an unrelated directory using only the distributable payload. Retaining the existing mirror/parity design is reasonable.

11. **[P2] Handoff validation is both unwired and permissive.**

    [The validator](C:/dev/anvil/scripts/validate-handoff.sh:17) accepts a numeric prefix via `parseFloat`, does not enforce ranges or known verdicts, and does not verify referenced results. A handoff with `pass_rate: "1oops"`, negative ERC violations, and a missing results file returned `HANDOFF: VALID`. No canonical command invokes the validator; repository references to running it are confined to tests.

    Minimum correction: invoke validation before chain consumption, enforce the fields required by that command, and require finite numbers with appropriate ranges. A generic two-field object check does not establish a usable chain contract.

12. **[P2] Passing tests do not establish end-to-end capability.**

    [CI](C:/dev/anvil/.github/workflows/ci.yml:11) runs only `tests/score.test.sh`; the mechanical and system suites are omitted. The core tests do not invoke ERC or DRC, despite their introductory comment suggesting parse-only coverage. Simulation is tested with a canned log; there is no committed runnable `.cir` fixture. Geometry tests cover a rectangular outline and two simple cubes.

    [The capability scorer](C:/dev/anvil/scripts/score-e2e-capability.sh:37) mostly checks text, command dispatch, and fixture-test results. It never builds the sample product, and exits zero even when capability rows fail. Its documented 30/30 score therefore measures implementation presence, not demonstrated spec-to-product success.

    Minimum correction: run all three existing suites in CI, add targeted negative cases, and exercise one real schematic/board/simulation path with active fabrication rules. Include a failure case that must prevent the final verdict. Use that evidence before expanding the claimed autonomy.

Additional workflow concerns merit correction, although they were not treated as separately reproduced release blockers. The default [SKiDL path](C:/dev/anvil/.claude/skills/anvil/references/schematic-protocol.md:8) documents netlist generation but omits the schematic-generation step required by subsequent KiCad ERC/PDF commands. Current SKiDL provides `generate_schematic()`; document and test the chosen supported version instead of leaving the conversion implicit. [SKiDL schematic-generation documentation](https://devbisme.github.io/skidl/#kicad-schematics).

The [doctor](C:/dev/anvil/scripts/doctor.sh:54) accepts `py -3` or uv but never checks an ordinary `python3` installation. Dependency versions are not pinned, and importability does not prove a working export pipeline. The [optimization metric](C:/dev/anvil/.claude/commands/anvil/improve.md:24) takes minimum margins across quantities with different units; it needs a specified normalization before values in volts, amperes, and dimensionless efficiency can be ranked consistently. The COTS compatibility inequality also applies derating on the opposite side from the system-budget contract; these should agree.

The [standards annex](C:/dev/anvil/.claude/skills/anvil/references/standards.md:6) acknowledges secondary-source transcriptions but supplies no source links for its numerical tables. This review does not certify those values or any regulatory compliance. Requirement IDs, CAD checks, and a generated test plan do not substitute for physical test evidence when a requirement calls for it.

There are useful foundations to retain: one canonical instruction tree, a working byte-parity gate, compact scripts without a new package dependency stack, stable requirement IDs, explicit pinned-catalog intent, corner-margin intent, and written boundaries around purchasing and fabrication submission. No hooks, MCP servers, background services, or credential-handling code are bundled. The main security concern found here is the integrity of acceptance evidence, not a demonstrated credential-exfiltration path. GitHub repository creation and pushes are directed by command prose, so their authority remains a host/session concern rather than a restriction enforced by the scorer.

The shortest repair sequence is to fix verdict completeness and tool failure propagation first; implement corner execution and activate the fab rules second; tighten wiring, numeric, geometry, and trace validation third; then repair release packaging and run the missing integration checks. Keep the current small architecture. Reuse the existing assertion-bound and CSV parsing logic when correcting it, rather than introducing a general workflow framework. Further commands have lower value until a broken design reliably produces a blocked result.

This assessment changed no plugin implementation or existing tests. Diagnostic scripts and their isolated inputs are available in the local temporary directory: [gate probes](C:/Users/tenso/AppData/Local/Temp/anvil-assessment-2e2fdf9b1c2244b78f295fe612915ba2/probes.cjs), [gate results](C:/Users/tenso/AppData/Local/Temp/anvil-assessment-2e2fdf9b1c2244b78f295fe612915ba2/probe-results.json), [geometry and rule-loading probe](C:/Users/tenso/AppData/Local/Temp/anvil-assessment-2e2fdf9b1c2244b78f295fe612915ba2/geometry.cjs), [additional wiring/currency results](C:/Users/tenso/AppData/Local/Temp/anvil-assessment-2e2fdf9b1c2244b78f295fe612915ba2/supplement-results.json), and [real corner-run result](C:/Users/tenso/AppData/Local/Temp/anvil-assessment-2e2fdf9b1c2244b78f295fe612915ba2/corner-results.json). These are diagnostic reproductions, not a new passing regression suite; temporary files may be removed by the operating system.
