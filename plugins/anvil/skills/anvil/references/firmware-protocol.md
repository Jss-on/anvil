# Firmware, software services and device security

Firmware starts with requirements and architecture. Define hardware/software allocation,
supported board variants, pin/peripheral/DMA ownership, interrupt/timing budgets, memory map,
bootloader/application/storage partitions, power modes, watchdog and safe-state behavior.
Specify debug/programming access, calibration schema and physical units, identity/key ownership,
local/offline/cloud behavior, account/data handling and support lifetime.

## Controlled build and integration

Pin the source revision, toolchain and dependency lock; identify third-party licenses and SBOM.
Use the project's existing build system and reproducible build instructions. Execute its real
build command, retain the exit status and transcript, and hash the resulting binary. A compiled
test must not be reported as an executed target test. Record generated files and board settings.

`firmware/release.json` schema 1 contains `source_revision` (full commit hash), `toolchain`,
`build_command` (argument array), `dependency_lock`, `binary`, `binary_sha256`,
`supported_hardware`, `bootloader_versions`, `sbom`, `known_issues`, `support_until`,
`recovery_test`, `production_debug_policy`, `calibration_schema`, and `build_record`.
Paths in this record are relative to its directory. Lists and required fields cannot be empty.
`signing_key_id` identifies an owned key when signing applies; never put private keys, production
credentials or device secrets in the project or transcript.

The build record is JSON with `command`, `toolchain`, `source_revision`, `dependency_sha256`,
`binary_sha256`, `created_at`, `exit_code: 0`, and a transcript path relative to the release
manifest directory. `firmware <release.json>` checks those links and the actual binary/lock.
It validates the imported build record, not compiler execution authenticity; HW-021 review
also checks provenance, reproducibility and source completeness.

## Verification gates

- G3: build and source/dependency inventory, board interface agreement, debug/test hooks,
  initial boot/recovery procedure and bench limits. Recovery plans may be prepared now;
  their on-target validation is due in DVT.
- G4: staged board bring-up, peripherals, interrupts, communication and timing/power measures;
  identify exactly which tests ran on which board and fixture. Preserve rework and failures.
- G5: resource limits under load, watchdog/reset, brownout, corrupted storage, disconnected
  sensors, stuck actuators, communication timeouts and safe-state recovery. HIL covers real
  timing and fault interaction; simulation supports cases it can represent credibly.
- G5/G6: authentication, signed updates when required, compatibility checks, interrupted
  download/install, rollback or antirollback policy and safe recovery. Test across supported
  hardware/bootloader versions, including power loss. Production debug locking must preserve
  an authorized service/recovery strategy; prove test credentials cannot enter shipment builds.
- G6: controlled programming, serial/identity binding, calibration version/units, key custody,
  approved factory privileges, provisioning audit and rework/erase procedures. Record each unit.
- G7/sustaining: known issues, release notes, diagnostics, support end date, vulnerability
  contact, update delivery/monitoring, incident response, key rotation/revocation and dependency
  support. A cloud service and mobile app are part of product availability and recovery.

Choose the security controls from the product threat model and destination duties. Useful
primary references: [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final),
[NIST IoT capability baseline](https://csrc.nist.gov/pubs/ir/8259/a/final),
[Zephyr executed-device testing](https://docs.zephyrproject.org/latest/develop/twister/index.html),
and [MCUboot image/recovery design](https://docs.mcuboot.com/design.html). These guide engineering;
they do not imply a particular RTOS/bootloader is mandatory.
