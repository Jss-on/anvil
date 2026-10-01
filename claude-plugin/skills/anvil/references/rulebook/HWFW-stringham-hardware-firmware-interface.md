# Hardware/Firmware Interface Design: Best Practices for Improving Embedded Systems Development — Anvil rulebook

## 0. Citation

G. Stringham, *Hardware/Firmware Interface Design: Best Practices for Improving Embedded Systems Development*, 1st ed. Burlington, MA, USA: Newnes (Elsevier), 2010 (copyright 2010; best-practice database copyright 2009 Gary Stringham & Associates, LLC). ISBN 978-1-85617-605-7. DOI 10.1016/B978-1-85617-605-7.

Chapters covered by THIS extraction: Ch. 1 Introduction, Ch. 2 Principles, Ch. 3 Collaboration, Ch. 4 Planning, Ch. 5 Documentation, Ch. 6 Superblock, Ch. 7 Design, Ch. 8 Registers, Ch. 9 Interrupts, Ch. 10 Aborts etc., Ch. 11 Hooks, Ch. 12 Conclusion, App. A Best Practices (cross-checked against chapter text), App. B Block Specification template (register-map exemplar), App. C (university use — skimmed, no rules), App. D Glossary (skimmed).

Chapters NOT read: none (see §8 Coverage log for what was skimmed and why).

Copyright handling: the 300+ numbered Best Practices are reproduced here as **paraphrased, checkable rule statements** carrying the book's ID (X.Y.Z) and page so each can be looked up; the author's exact wording is not copied wholesale (the BP database carries its own copyright notice, p.xiii). Short quoted fragments are used only where the exact phrase is load-bearing.

Book structure notes: Best-practice IDs are `chapter.section.n`. The seven principles (Ch. 2) are: P1 Collaborate on the Design; P2 Set and Adhere to Standards; P3 Balance the Load; P4 Design for Compatibility; P5 Anticipate the Impacts; P6 Design for Contingencies; P7 Plan Ahead. Each chapter summary names the principles it supports; that mapping is used as the grouping key ("P-map") in §1. Domain is `hw-fw` for every BP row unless the rule is more precisely another domain (`process`, `requirements`, `test`, `bringup`, `firmware`).

## 1. Design rules

Column key: `id` = HWFW-NNN; `source` = book Best Practice ID (BP x.y.z) + printed page; `conf` = high (explicit rule/number in text), medium (derived from stated relation), low (qualitative guidance quantified here — flagged).

### 1.A Seven Principles (Ch. 2, pp.19–30) — P-map: all

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| HWFW-001 | process | P1 Collaborate on the Design: hardware and firmware teams jointly design the register/interrupt interface from early concept through final firmware; documentation (esp. register/bit spec) is the primary collaboration tool. | — | project plan, review records | all ASIC/ASSP/SoC/FPGA projects | review | Principle 2.1.1, p.21 | high |
| HWFW-002 | process | P2 Set and Adhere to Standards: implement industry standards unchanged; define internal standards (module style, quality checks, doc format); any change to an internal standard goes through review/approval and is published with a version number. "There is no such thing as a customized standard." | — | standards list, change log | all | review | Principle 2.1.2, p.22 | high |
| HWFW-003 | process | P3 Balance the Load: partition tasks between HW and FW by relative cost (e.g. byte parity = 8-iteration FW loop vs. 1 clock cycle of XOR tree in HW; FP in HW is faster but adds parts cost). Revisit I/O buffer sizes, interrupt priorities, handshakes. | parity: FW ~8 loop iterations x several instructions; HW 1 clk (Listing 2.1/2.2) | task list, CPU load, silicon area | all | review | Principle 2.1.3, pp.23–25 | high |
| HWFW-004 | hw-fw | P4 Design for Compatibility: any version of FW should pair with any version of HW where possible; do not move bits or registers between versions; new HW must work with old driver. | — | register map diff between versions | leveraged blocks | inspect | Principle 2.1.4, pp.25–26 | high |
| HWFW-005 | hw-fw | P5 Anticipate the Impacts: group bits into registers by usage; never mix bit types in one register; minimise registers shared by more than one driver; when changing a block keep the old driver working; do not move bit locations or register addresses. | — | register map | all | inspect | Principle 2.1.5, p.26 | high |
| HWFW-006 | hw-fw | P6 Design for Contingencies: add test/debug hooks (peek/poke of internal flip-flops and signals) so firmware can see inside the chip when it "won't turn on" six months later. | — | hook list per block | all | review | Principle 2.1.6, pp.27–29 | high |
| HWFW-007 | process | P7 Plan Ahead: put a framework in the design (modularity, abstraction, reuse) that allows new features and expansion without sacrificing the current product. | — | architecture doc | all | review | Principle 2.1.7, pp.29–30 | high |
| HWFW-008 | process | Business case: an ASIC respin costs up to 4 months and "several million dollars"; 45–70% of respins are due to functional/logical errors (Blyler/Ying surveys). Use as the risk weight for interface-defect prevention. | respin delay <= 4 months; cost = several $M; 45–70 % of respins functional/logic | — | fabricated ASIC/ASSP/SoC (not FPGA) | calc | §1.2.2, p.10; §1, p.1 | high |
| HWFW-009 | process | "First time right" expanded: chip must be (1) easier to program, (2) easier to debug, (3) easier to work around defects — even a flawed first silicon can ship if these hold. | — | — | all | review | §1.3, pp.10–12 | high |

### 1.B Ch. 3 Collaboration (pp.31–49) — P-map: P1, P2, P7

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| HWFW-010 | process | Designate one hardware-team member as best-practice champion (owns the living BP list; handles add/change/delete requests). | — | org chart | all | inspect | BP 3.1.1, p.33 | high |
| HWFW-011 | process | Designate a hardware-team member as ambassador to the firmware team (regular contact, delivers documents for review, sits in FW meetings). | — | org chart | all | inspect | BP 3.1.2, p.33 | high |
| HWFW-012 | process | Designate a firmware-team member as ambassador to the hardware team. | — | org chart | all | inspect | BP 3.1.3, p.34 | high |
| HWFW-013 | process | Hold a joint HW/FW kick-off meeting: product intro, industry standards involved, schedule/budget/margins/risk, team intros, points of contact, tools, meeting schedule. | — | kick-off agenda | project start | inspect | BP 3.1.4, p.35 | high |
| HWFW-014 | process | Collect and distribute contact info and spheres of responsibility of HW and FW members across both teams. | — | contact list | project start | inspect | BP 3.1.5, p.35 | high |
| HWFW-015 | process | Hold regular (weekly) HW/FW meetings on relevant topics with the appropriate engineers (Table 3.1 topics: high-level spec; block detailed design incl. error-handling use cases; block verification/test plans; HW test + HW/FW integration; system test/perf tuning). Do not force a meeting when there is nothing to discuss. | cadence = weekly | meeting log | all phases | inspect | BP 3.2.1, p.36; Table 3.1 | high |
| HWFW-016 | process | When teams are in different locations apply extra effort to meet (email, teleconference, video, wikis, travel). | — | — | distributed teams | review | BP 3.2.2, p.37 | high |
| HWFW-017 | process | Start HW/FW collaboration during the initial high-level hardware design phase (block selection, power/perf/area/cost trade-offs). | — | — | project start | inspect | BP 3.2.3, p.37 | high |
| HWFW-018 | process | Firmware must be represented in the overall chip design, the detailed design of each block, and the test plans. | — | review attendance | all | inspect | BP 3.2.4, p.38 | high |
| HWFW-019 | process | Firmware must be represented (sign-off) in reviews and checkpoints of hardware milestones throughout the life cycle. | — | sign-off records | all | inspect | BP 3.2.5, p.38 | high |
| HWFW-020 | process | Use co-development (virtual prototypes, FPGA prototypes, co-simulation, legacy hardware) so FW engineers write code and find problems before silicon arrives. Co-sim runs hours per few ms of activity — limited test cases; FPGA/legacy may need temporary register address changes. | co-sim: hours of wall time per few ms simulated | tool plan | all | review | BP 3.2.6, p.40; §3.2.3 | high |
| HWFW-021 | process | Provide hardware-engineering support to firmware through to the end of firmware development (post-silicon); HW ambassador monitors FW issues and pulls in the right HW engineer. | — | support roster | post-fab | inspect | BP 3.2.7, p.41 | high |
| HWFW-022 | process | Establish a repository of HW high-level and detailed design documents with appropriate FW access (password/site/sign-out as security needs dictate). | — | repo | all | inspect | BP 3.2.8, p.42 | high |
| HWFW-023 | process | Maintain a searchable chip-defect repository that firmware engineers can access. | — | defect DB | all | inspect | BP 3.2.9, p.43 | high |
| HWFW-024 | process | Push-notify all applicable firmware engineers of each chip defect as it is identified (do not rely on them re-checking the repository). | — | defect DB, notification log | all | inspect | BP 3.2.10, p.43 | high |
| HWFW-025 | process | Build bridges for informal HW/FW collaboration (direct engineer-to-engineer contact; liaison; managers cc'd if org structure requires). | — | — | all | review | BP 3.3.1, p.45 | high |
| HWFW-026 | process | HW: consult firmware engineers before any change to the HW/FW interface; for ASSPs consult a representative subset of FW teams. | — | change requests | all | inspect | BP 3.3.2, p.46 | high |
| HWFW-027 | process | FW: initiate contact with the block's HW engineer early in block design to discuss the block, its driver, and their interactions. | — | — | design phase | review | BP 3.3.3, p.46 | high |
| HWFW-028 | process | FW: request test/debug hooks for the block during design (use Ch. 11 list as the menu). | — | hook request list | design phase | inspect | BP 3.3.4, p.47 | high |
| HWFW-029 | process | FW: when a cumbersome HW/FW interaction is found (e.g. interrupt bits mixed with config bits; multi-step read/write sequence per buffer word) work with HW on a better design. | — | — | all | review | BP 3.3.5, p.47 | high |
| HWFW-030 | process | Root-cause complicated defects with both HW and FW engineers, then jointly design the firmware workaround. Problem classes: (1) FW wrong assumption, (2) FW wrong due to bad docs, (3) FW defect, (4) HW defect. | — | defect record | integration/test | review | BP 3.3.6, p.48; §3.3.4 | high |

### 1.C Ch. 4 Planning (pp.51–72) — P-map: P2, P3, P4

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| HWFW-031 | requirements | Use existing industry standards (USB, PCI, I2C, JPEG, ...) where possible. | — | interface list | all | inspect | BP 4.1.1, p.52 | high |
| HWFW-032 | requirements | Use a de facto standard (e.g. Hayes "AT" syntax, 16550 UART, EHCI USB host register layout) if no official standard exists. | — | interface list | all | inspect | BP 4.1.2, p.52 | high |
| HWFW-033 | requirements | Implement a standard exactly to its specification (no undocumented behavioural deviations; e.g. I2C block that lacked block-transfer mode; JPEG decoder mis-handling a marker). | — | standard, implementation | all | test | BP 4.1.3, p.55 | high |
| HWFW-034 | requirements | Implement the full standard or a *standard-defined* subset; never a non-standard subset or a derivation (so standard drivers, test suites and tools apply). | — | feature list vs standard | all | inspect | BP 4.1.4, p.55; §4.1.2 | high |
| HWFW-035 | requirements | If a standard is deviated from, document every deviation with motivation, justification and risks. | — | deviation list | when derivation unavoidable | inspect | BP 4.1.5, p.56 | high |
| HWFW-036 | process | Before designing anything new, research available designs/standards (author's own compression algorithm anecdote). | — | — | new protocol/format | review | §4.1.3, p.56 | high |
| HWFW-037 | process | Consult other project teams to identify the latest version of a block to leverage (Fig. 4.1: use Team X's v2, not your own v1). | — | block version registry | leveraged blocks | inspect | BP 4.2.1, p.57 | high |
| HWFW-038 | requirements | Consult marketing and partner teams for near-future features and add them to the block. | — | roadmap | new block version | review | BP 4.2.2, p.57 | high |
| HWFW-039 | requirements | When leveraging a common-version block to the next generation, add the changes needed for new requirements/features. | — | requirements | leveraged blocks | review | BP 4.2.3, p.58 | high |
| HWFW-040 | hw-fw | Develop internal design standards for style/format of register layout, register access, interrupt modules, DMA modules and other common elements (one DMA IP instantiated everywhere lets one FW DMA module serve all drivers). | — | internal standards doc | all | inspect | BP 4.2.4, p.58 | high |
| HWFW-041 | hw-fw | New block versions must be backward compatible with the old firmware where possible (old driver works on new chip; new driver works on old chip without using new features). | — | register map diff | leveraged blocks | inspect | BP 4.3.1, p.58 | high |
| HWFW-042 | hw-fw | When full backward compatibility is impossible, minimise FW impact by moving the change up the compatibility ladder: no-impact (e.g. widen an 8-bit integer field read as 32-bit) > superset bits > legacy mode at power-up > version number > version clues (set a bit that exists only in one version, read back) > incompatible (rewrite driver). | ladder rank 1..6 (lower = better) | change description | all changes | review | BP 4.3.2, p.60; §4.3.1 | high |
| HWFW-043 | process | Document each chip defect: behaviour, triggering conditions, impact, likelihood/frequency, FW steps to avoid/work around, list of chip versions containing it. | 6 required fields | defect record | all | inspect | BP 4.4.1, p.62 | high |
| HWFW-044 | process | Document all defects, including those deemed unlikely and those with vague cause/symptoms ("99% is not 100%"; e.g. set-bit race fixed by HW clearing the bit instead of FW). | — | defect record | all | inspect | BP 4.4.2, p.63 | high |
| HWFW-045 | process | Review the defect list of the previous chip and select which to fix in the next version, weighing FW-workaround complexity/risk against HW-fix complexity/risk (complex FW workaround + easy HW fix => fix HW; easy FW + risky HW => keep workaround). Notify FW when fixed so workarounds are removed. | — | defect list | next-gen planning | review | BP 4.4.3, p.65; §4.4.2 | high |
| HWFW-046 | test | Develop and review HW/FW interface test plans with the FW team so block tests reflect actual FW usage — same register values, same programming order, same flow/frequency (order-of-writes defect escaped sim; chaining not simulated). | — | test plan, driver sequence | block verification | review | BP 4.4.4, p.66 | high |
| HWFW-047 | connectors | Shared pins: two blocks may share package pins only if they are never needed simultaneously (mutually exclusive product sets; mutually exclusive configurations; boot-only use; test-mode-only use). If any product may need both, assign separate pins. | — | pin map with per-block usage windows | pin-limited packages | inspect | BP 4.5.1, p.67; §4.5.1 | high |
| HWFW-048 | hw-fw | Analyse each I/O block's buffer sizing and management: status, control, interrupts (full/overflow/empty/timeout), errors, debug visibility (buffer contents, fill level, control regs). Size examples: UART 8 -> 128 bytes cheap and cuts interrupt rate; DMA 128 -> 256 bytes x N instances too costly; low-traffic DMA ~32 bytes, high-traffic ~512 bytes. | UART buf 128 B; DMA low 32 B, high 512 B (examples) | buffer table per block | all I/O blocks | review | BP 4.5.2, p.67; §4.5.2 | high |
| HWFW-049 | hw-fw | Keep FW-block interactions as simple as possible; avoid address aliasing traps (Table 4.2: sub-table decoding only low address bits corrupts on writes to 0x04–0x07; fix by separate address ranges or ignoring out-of-range writes). | — | address decode of every register/table | all | inspect | BP 4.5.3, p.69; Table 4.2 | high |
| HWFW-050 | components | Third-party IP checklist: prior silicon history; existing device drivers (for target CPU/OS, or source available); strong technical support incl. access to original designers; register/bit/interrupt style consistent with other blocks in the chip. | 4 criteria | IP datasheet | IP purchase | review | BP 4.5.4, p.70 | high |
| HWFW-051 | process | Review previous chip's postmortem notes during the specification phase of the new chip; apply fixes and enhancements. | — | postmortem doc | spec phase | inspect | BP 4.6.1, p.70 | high |
| HWFW-052 | process | Conduct a joint HW/FW postmortem soon after product release (what went well/badly, defects to fix, docs, process, meetings, comms, testing holes); write up and distribute notes. | — | — | post-release | inspect | BP 4.6.2, p.71 | high |

### 1.D Ch. 5 Documentation (pp.73–120) — P-map: P1, P2, P4, P5

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| HWFW-053 | hw-fw | Chip-level documentation must list, for each instantiated block: block version, address offset from chip base, mapping of its interrupt line(s) into the chip-level interrupt register, bus priority, customisable parameter settings (buffer sizes, channel count), and mapping in global power/reset registers (Table 5.1 columns: Block, Rev, Base Address, Interrupt mask, Other Notes). | — | chip block table | every chip | inspect | BP 5.1.1, p.77; Table 5.1 | high |
| HWFW-054 | process | Distribute the block documentation to all applicable FW teams (in-house, end-customer, third-party). | — | distribution list | all | inspect | BP 5.1.2, p.78 | high |
| HWFW-055 | process | Distribute the block *unsupported* specification (test/debug registers, state diagrams) only to in-house FW teams. | — | distribution list | all | inspect | BP 5.1.3, p.78 | high |
| HWFW-056 | hw-fw | In supported registers, every unsupported/test bit must be flagged in the block doc: "write 0, ignore on read" — without explaining its function. | — | register map | all | inspect | BP 5.1.4, p.79 | high |
| HWFW-057 | process | Documentation standards (sections, register-map format, reference + tutorial) apply across the block, all blocks in the chip, and all chips of the organisation. | — | doc template | all | inspect | BP 5.2.1, p.80 | high |
| HWFW-058 | process | Write the block documentation at the beginning of the design phase, before RTL. | — | doc date vs RTL start | all | inspect | BP 5.2.2, p.80 | high |
| HWFW-059 | process | Update the documentation regularly as the block design changes (at the time of the change). | — | doc revision log | all | inspect | BP 5.2.3, p.81 | high |
| HWFW-060 | process | Review the documentation for accuracy/completeness soon after design freeze. | — | review record | design freeze | inspect | BP 5.2.4, p.81 | high |
| HWFW-061 | process | Use the leveraged block's documentation as the baseline for the new block's documentation. | — | — | leveraged blocks | inspect | BP 5.2.5, p.82 | high |
| HWFW-062 | hw-fw | Check for the common documentation errors: wrong register address, wrong bit position, wrong bit sense (1 vs 0; negative logic), old functions still listed, new functions not listed, missing information. | 6 error classes | doc vs RTL | all | inspect | BP 5.2.6, p.82 | high |
| HWFW-063 | hw-fw | Use clear, unambiguous names and descriptions for registers, bits and functions (e.g. define cold/warm, soft/hard, sync/async "reset" explicitly). | — | register names | all | review | BP 5.2.7, p.83 | high |
| HWFW-064 | process | Distribute documentation to FW for initial review right after it is written at the start of design. | — | review record | design start | inspect | BP 5.3.1, p.84 | high |
| HWFW-065 | process | Redistribute for subsequent reviews whenever the doc changes materially (updates, corrections, design changes). | — | review record | all | inspect | BP 5.3.2, p.84 | high |
| HWFW-066 | process | Explicitly mark all changes between current and previous distributed versions (change tracking, doc compare, highlighting, returned reviewer comments); remove old marks before the next round. | — | doc | each revision | inspect | BP 5.3.3, p.85 | high |
| HWFW-067 | process | FW: review the block doc and feed back issues on design, functionality and documentation; insert missing details you know. | — | review comments | each review | inspect | BP 5.3.4, p.86 | high |
| HWFW-068 | process | FW: respond to a doc review within a few days to a week; reply even if there are no comments. | turnaround <= ~1 week | review record | each review | inspect | BP 5.3.5, p.87 | high |
| HWFW-069 | hw-fw | Block doc must include: detailed description of the block and each task; why/when each task is used; all registers/bits to set up each task; required order of register writes; restrictions on valid conditions/values. | 5 required content items | block doc | all | inspect | BP 5.4.1, p.87 | high |
| HWFW-070 | process | Block doc must be sufficient for someone else to take ownership of the block (define nomenclature; include the "obvious"). | — | block doc | all | review | BP 5.4.2, p.88 | high |
| HWFW-071 | hw-fw | Include a top-down description: theory of operation, function in the system, and constituent parts (template §B.1.1). | — | block doc | all | inspect | BP 5.4.3, p.89 | high |
| HWFW-072 | process | Include a document version history (rev, date, changes, who), newest first (Table 5.3 / B1). | — | block doc | all | inspect | BP 5.4.4, p.89 | high |
| HWFW-073 | hw-fw | Include a block version history: FW-visible changes and defects fixed per silicon version, newest first (Table 5.4 / B2). | — | block doc | all | inspect | BP 5.4.5, p.90 | high |
| HWFW-074 | hw-fw | Include a chip-specific history per chip: rev, base address, interrupt mask, supported I/O pins, other notes (Table 5.5 / B3); keep consistent with chip-level Table 5.1 (data is duplicated). | — | block doc | all | inspect | BP 5.4.6, p.91 | high |
| HWFW-075 | hw-fw | Document features the block does support AND features it does not support (that one might reasonably assume). | — | block doc | all | inspect | BP 5.4.7, p.91 | high |
| HWFW-076 | hw-fw | Document the assumptions made about what firmware will do for this block. | — | block doc | all | inspect | BP 5.4.8, p.92 | high |
| HWFW-077 | process | Include a list of related documents (system docs, internal design spec, other blocks, external components, standards). | — | block doc | all | inspect | BP 5.4.9, p.92 | high |
| HWFW-078 | hw-fw | Provide both a reference section (all registers in address order with bits) and a tutorial section (step sequences per task). | — | block doc | all | inspect | BP 5.4.10, p.92 | high |
| HWFW-079 | hw-fw | Tutorial section: describe the steps for each task type incl. abort, error handling and resume (example: write ctrl 0x123; load start address; set Start bit 0x1; wait Task Complete IRQ 0x4; clear by writing 0x4 to Interrupt Status; read Data). | — | block doc | all | inspect | BP 5.4.11, p.94 | high |
| HWFW-080 | hw-fw | In the tutorial identify bit fields by register name and bit-field name exactly as in the reference section. | — | block doc | all | inspect | BP 5.4.12, p.94 | high |
| HWFW-081 | process | Include a glossary of terms unfamiliar to firmware readers. | — | block doc | all | inspect | BP 5.4.13, p.94 | high |
| HWFW-082 | hw-fw | Include an errata section per chip: where/how the block deviates from spec and the workaround (e.g. max packet 254 not 255; link mode broken; abort fails if last byte 0x00 — hit abort twice). Keep updated with FW-found defects. | — | block doc | all | inspect | BP 5.4.14, p.95 | high |
| HWFW-083 | hw-fw | Document ALL firmware-accessible registers, including test/debug registers (normal-use fully; test/debug briefly, listed after normal-use or in the unsupported doc). | — | register map vs RTL | all | inspect | BP 5.5.1, p.96 | high |
| HWFW-084 | process | Use an automated register design tool (single source -> .vh/.h/.rtf) to keep HW, FW, verification and documentation register/bit definitions in sync. | — | toolchain | all | inspect | BP 5.5.2, p.100 | high |
| HWFW-085 | hw-fw | Include a table of registers in address order (>= columns: address offset, register name; optional page); optionally a second table alphabetical by name. | — | block doc | all | inspect | BP 5.5.3, p.100; Table 5.6 | high |
| HWFW-086 | hw-fw | Document each register's name and its address *offset from the block base* (not absolute address), so the doc and driver are portable across chips/systems. | address = block_base + offset | register map | all | inspect | BP 5.5.4, p.101 | high |
| HWFW-087 | hw-fw | Document all inter-register interactions (register A used only if bit B of register C set; register D must be written before E; sub-block reads a register elsewhere in the block). | — | register map | all | inspect | BP 5.5.5, p.102 | high |
| HWFW-088 | hw-fw | For numeric fields document units, minimum and maximum legal values (a 6-bit field's max may be 50, not 63), zero- vs one-based counts, and the response to illegal values. | field: units, min, max, base (0/1), illegal-value response | register map | all numeric fields | inspect | BP 5.5.6, p.102 | high |
| HWFW-089 | hw-fw | For address/count registers document what a read returns before the task starts, during processing (live value or original?), and after completion. | — | register map | address/count regs | inspect | BP 5.5.7, p.103 | high |
| HWFW-090 | hw-fw | Display the register map horizontally, bits grouped in fours to align with hex digits (so 0x0000001D decodes visually). | — | register map | all | inspect | BP 5.6.1, p.104 | high |
| HWFW-091 | hw-fw | Put the LSB on the right of the register map. | — | register map | all | inspect | BP 5.6.2, p.105 | high |
| HWFW-092 | hw-fw | Number bits with the LSB as bit 0 (so bit n == 1<<n regardless of register width). | bit n mask = 1 << n | register map | all | inspect | BP 5.6.3, p.105 | high |
| HWFW-093 | hw-fw | Mark the type of every bit in the map: read-only, write-only, read/write (extra row per type when mixed). | — | register map | all | inspect | BP 5.6.4, p.105 | high |
| HWFW-094 | hw-fw | Document the power-on default of every bit in the map; use X for unknown (e.g. bit reflecting an input pin level; instantiation-dependent bits). | reset value ∈ {0,1,X} per bit | register map | all | inspect | BP 5.6.5, p.105 | high |
| HWFW-095 | hw-fw | Provide a detailed description for each bit under its register map (e.g. field D: 0x1=1 byte (default), 0x2=2, 0x3=4, 0x4=8 bytes). | — | register map | all | inspect | BP 5.6.6, p.106 | high |
| HWFW-096 | hw-fw | Sort bit descriptions under the map from LSB up to MSB. | — | register map | all | inspect | BP 5.6.7, p.106 | high |
| HWFW-097 | hw-fw | Document how each bit is (or is not) affected by an abort — at least for bits that are modified and bits a reader might wonder about. Interrupt Status/Enable bits are unchanged by abort (except abort-done). | — | register map | all | inspect | BP 5.6.8, p.106 | high |
| HWFW-098 | hw-fw | Explicitly indicate every bit reserved for test/debug. | — | register map | all | inspect | BP 5.6.9, p.107 | high |
| HWFW-099 | hw-fw | In third-party docs mark test/debug bits as "ignore on read, write 0" without describing function. | — | register map | third-party distribution | inspect | BP 5.6.10, p.107 | high |
| HWFW-100 | hw-fw | Wherever test/debug hooks are documented add a warning that they are unsupported and may change location/behaviour in the next version. | — | doc | all | inspect | BP 5.6.11, p.107 | high |
| HWFW-101 | hw-fw | Document each interrupt as edge- or level-triggered (level: service device before ack; edge: ack first then service). | — | interrupt table | every interrupt | inspect | BP 5.7.1, p.108 | high |
| HWFW-102 | hw-fw | Document trigger polarity: rising/falling edge, or high/low level; note any inversion of active-low external signals on read. | — | interrupt table | every interrupt | inspect | BP 5.7.2, p.108 | high |
| HWFW-103 | hw-fw | For level-triggered interrupts describe when and how firmware deasserts the source (pulse that self-clears; clear a bit; command to an external device). | — | interrupt table | level-triggered IRQs | inspect | BP 5.7.3, p.109 | high |
| HWFW-104 | hw-fw | Name the propagation-control register "Enable" (1 = propagate); do not use "Mask" (ambiguous polarity). | Enable: 1 = allow | register names | interrupt regs | inspect | BP 5.7.4, p.109 | high |
| HWFW-105 | hw-fw | Document the bit value (1 or 0) that acknowledges each interrupt (write-1-to-clear is the common convention; write-0-to-clear exists). | — | interrupt table | every interrupt | inspect | BP 5.7.5, p.109 | high |
| HWFW-106 | hw-fw | Document which interrupts can fire before the task is really complete (e.g. done posted 1–2 clocks before idle; done posted before data reaches memory through the bus/memory controller). | — | interrupt table | done IRQs | inspect | BP 5.7.6, p.110 | high |
| HWFW-107 | hw-fw | Document which interrupts can be generated repeatedly without firmware intervention (e.g. incoming I/O data) vs. one-shot per FW-launched task (e.g. DMA done). | — | interrupt table | every interrupt | inspect | BP 5.7.7, p.111 | high |
| HWFW-108 | hw-fw | Document how quickly an unhandled interrupt can recur (minimum inter-arrival time). | t_min_recur (us) | interrupt table | repeating IRQs | inspect | BP 5.7.8, p.111 | high |
| HWFW-109 | hw-fw | Document what happens if a repeating interrupt recurs before the first is serviced (nothing / counter increments / data overwritten / separate overflow interrupt). | — | interrupt table | repeating IRQs | inspect | BP 5.7.9, p.111 | high |
| HWFW-110 | timing | Document min, max and typical time from queue-bit set to task start (e.g. immediately = 0; waits for free port = bounded by max packet time; waits for external ready = unbounded). | t_start_min/typ/max (clk or s); min = 0 | timing table | every FW-launched task | inspect | BP 5.8.1, p.112 | high |
| HWFW-111 | timing | Document min/max/typical time to complete the task, process an abort, or produce other delayed events (examples: 128 clk fixed; ~1500 clk per 1 KB; abort >= 10 clk if active, immediate if idle, up to 20,480 clk if output pipe stalled before timeout). | t_done_min/typ/max; e.g. 1500 clk/KB; abort 10..20480 clk | timing table | every task/abort | inspect | BP 5.8.2, p.112 | high |
| HWFW-112 | timing | Document the minimum and typical inter-arrival times of successive identical hardware events (example: basic packets, no payload, as often as every 45 us; extended packets with 16-byte payload as often as every 105 us). | t_event_min, t_event_typ (us) | timing table | repeating external events | inspect | BP 5.8.3, p.113 | high |
| HWFW-113 | timing | Document the conditions and states that cause the min/typ/max timing variations (block state, data amount, external conditions). | — | timing table | every timed operation | inspect | BP 5.8.4, p.113 | high |
| HWFW-114 | timing | Document each duration in its *primary* unit: clock cycles if the work is cycle-bound, seconds if protocol-bound. Table 5.7: at 100 MHz, 10 ms = 1,000,000 clk; at 133 MHz, 10 ms = 1,330,000 clk but 1,000,000 clk = 7.5 ms. State both, e.g. "1 million chip clocks, which at 100 MHz is 10 ms". | t_s = N_clk / f_clk | timing table, f_clk | every timed operation | inspect | BP 5.8.5, p.114; Table 5.7 | high |
| HWFW-115 | hw-fw | Document normal operation in detail and every error check the block performs when starting or executing a task. Planning heuristic: ~20 % of code is normal path, ~80 % error handling. | — | block doc | all | inspect | BP 5.9.1, p.116; §5.9 p.114 | high |
| HWFW-116 | hw-fw | Document every error message (interrupt or status) the block can send to firmware. | — | error table | all | inspect | BP 5.9.2, p.116 | high |
| HWFW-117 | hw-fw | Document in detail all conditions that can cause each error message (one error bit had 6 distinct root causes in the Unity decompressor). | — | error table | all | inspect | BP 5.9.3, p.117 | high |
| HWFW-118 | hw-fw | For each error, state whether the operation stops or continues. | — | error table | all | inspect | BP 5.9.4, p.117 | high |
| HWFW-119 | hw-fw | Describe the block state after each error (self-reset / stuck in bad state / terminated normally to idle). | — | error table | all | inspect | BP 5.9.5, p.118 | high |
| HWFW-120 | hw-fw | Document the state of data after each error (unchanged / corrupted / partial / unknown). | — | error table | all | inspect | BP 5.9.6, p.118 | high |
| HWFW-121 | hw-fw | Describe the recovery action per error: ignore / log / abort the block / step sequence / power-cycle. | recovery in {ignore, log, abort, sequence, power-cycle} | error table | all | inspect | BP 5.9.7, p.118 | high |
| HWFW-122 | hw-fw | Describe the block's response to an invalid configuration (e.g. bits B and G both set at start): no-op / one bit overrides / unpredictable / clobbers / error bit set. | — | block doc | all | inspect | BP 5.10.1, p.119 | high |
| HWFW-123 | hw-fw | Document firmware-relevant state machines (does a write while busy corrupt? error in some states? second request aborts/holds/ignored? two simultaneous requests? bus signal protocol) — include the state diagram in the block doc where it affects FW. | — | block doc | all | inspect | BP 5.10.2, p.120 | high |
| HWFW-124 | hw-fw | Document the step sequence to cleanly abort the block when it is more than setting one bit (e.g. abort A; abort B; wait B abort-done; abort B again; wait; abort C). | — | block doc | all | inspect | BP 5.10.3, p.120 | high |

### 1.E Ch. 6 Superblock (pp.123–147) — P-map: P4, P5, P7

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| HWFW-125 | hw-fw | Design each block as a superblock: one set of design files providing the superset of features needed by all chips that instantiate it (Table 6.1 RS-232 example: A up to 115,200 baud; B HW handshaking; C 256-byte buffer; D auto speed sensing; E auto SW handshaking). | — | feature matrix across products | all reusable blocks | inspect | BP 6.1.1, p.131 | high |
| HWFW-126 | hw-fw | Consolidate all divergent versions of a block into one superblock (may take 2–3 generations). | — | block version tree | leveraged blocks | review | BP 6.1.2, p.132 | high |
| HWFW-127 | hw-fw | Instantiate the block in every chip from the same superblock design files; never from copies. | — | source control | all | inspect | BP 6.1.3, p.133 | high |
| HWFW-128 | hw-fw | Design common modules (DMA, interrupt) as supermodules with the superset of features needed by all blocks. | — | module list | all | inspect | BP 6.1.4, p.133 | high |
| HWFW-129 | hw-fw | Add new features to the common superblock, not to a separate branch (branch temporarily, merge before ship). | — | source control | all | inspect | BP 6.1.5, p.134 | high |
| HWFW-130 | hw-fw | Retain all known low-overhead functionality in a superblock even when current requirements do not need it (landscape-width raster buffers saved a new SoC). | — | feature list | space permitting | review | BP 6.1.6, p.134 | high |
| HWFW-131 | hw-fw | Leave old functionality in place until its replacement is proven; remove afterwards. | — | feature list | space permitting | review | BP 6.1.7, p.135 | high |
| HWFW-132 | hw-fw | Include low-impact, low-risk extras for future products: more GPIO pins, restored removed portions, more debug support, larger on-chip RAM buffers, higher clock. | — | spare pins/area budget | spare pins/area exist | review | BP 6.1.8, p.136 | high |
| HWFW-133 | hw-fw | Increment the block version register whenever the superblock design changes in a FW-visible way; do NOT change it when the same version is instantiated in different chips. | version = f(design), not f(chip) | version register table | all | inspect | BP 6.1.9, p.137 | high |
| HWFW-134 | hw-fw | Unused block outputs: leave unconnected at the block boundary (synthesis removes logic); do not edit block internals. | — | instantiation netlist | all instantiations | inspect | BP 6.2.1, p.138 | high |
| HWFW-135 | hw-fw | Unused block inputs: tie high or low at the block boundary to the enabled or disabled state appropriate for the driver view (e.g. unconnected UART handshake inputs tied to "ready"). Never leave inputs floating. | — | instantiation netlist | all instantiations | inspect | BP 6.2.2, p.138 | high |
| HWFW-136 | hw-fw | Document which I/O signals are active for each instantiation of the block. | — | chip-level doc | all instantiations | inspect | BP 6.2.3, p.139 | high |
| HWFW-137 | hw-fw | Parameterize superblock configuration (buffer size, channel count, optional sub-blocks) so the same source can be instantiated with different sizes in multiple chips. | — | parameter list | large blocks | inspect | BP 6.3.1, p.139 | high |
| HWFW-138 | hw-fw | Parameterize only where it significantly reduces silicon: a block taking ~25 % of the die is an obvious candidate; a ~7000-gate UART on a 10-million-gate die is not worth it. | remove if area_share large; skip if block ~7 kgates on 10 Mgate die | area per sub-block | all | calc | BP 6.3.2, p.140 | high |
| HWFW-139 | hw-fw | Review each large superblock for large optional sub-blocks (RAM, features, duplicate channels, supermodule FIFOs) to include/exclude by parameter. | — | area breakdown | large blocks | review | BP 6.3.3, p.140 | high |
| HWFW-140 | hw-fw | Use parameters to include new and exclude old features so one source produces current and previous block versions. | — | parameter list | evolving blocks | inspect | BP 6.3.4, p.141 | high |
| HWFW-141 | hw-fw | Optional sub-blocks must have clean boundaries to the rest of the block. | — | RTL hierarchy | parameterized blocks | review | BP 6.3.5, p.141 | high |
| HWFW-142 | hw-fw | Provide a fixed bypass path (mux) around any optional portion of a pipeline; when excluded, the mux select is tied to bypass. | — | pipeline diagram | parameterized pipelines | inspect | BP 6.3.6, p.142 | high |
| HWFW-143 | hw-fw | Store all instantiation parameter values in one or more read-only, FW-readable Instantiation registers (example UART Instantiation Register 0x0004: bit0 H = HW-handshake pins connected; bit1 S = SW-handshake sub-block present; bit2 A = auto-speed-sense present; bits[13:8] B = Rx/Tx buffer size in units of 8 bytes, min 0x1 = 8 B, max 0x20 = 256 B; reset values X = instantiation-dependent). | buffer_bytes = 8 * B, B in [0x01, 0x20] | register map | parameterized blocks | inspect | BP 6.3.7, p.144; register map p.143 | high |
| HWFW-144 | hw-fw | Increment the block version register when a new parameter (new instantiation-register bit) is added. | — | version/instantiation registers | all | inspect | BP 6.3.8, p.144 | high |
| HWFW-145 | hw-fw | Do not change the block version register for different parameterizations of the same version. | — | version register | all | inspect | BP 6.3.9, p.144 | high |
| HWFW-146 | hw-fw | Registers of an excluded optional sub-block ignore writes and read as all zeros (so a status read shows nothing pending). | read = 0x0; write = no-op | register map + parameters | parameterized blocks | test | BP 6.3.10, p.145 | high |
| HWFW-147 | hw-fw | Excluded optional bits inside fixed registers ignore writes and read zero; the remaining bits stay operational. | — | register map + parameters | parameterized blocks | test | BP 6.3.11, p.145 | high |
| HWFW-148 | hw-fw | Fixed and optional registers/bits keep the same address and bit position regardless of which options are excluded; excluded positions stay empty. Never auto-pack included bits. | — | register map per parameterization | parameterized blocks | inspect | BP 6.3.12, p.146 | high |
| HWFW-149 | power | Unused-logic cost: static (leakage) power of never-used logic is "a significant problem" at 65 nm and below — weigh against superblock retention. | node <= 65 nm | process node | superblock decision | review | §6.1.3, p.130 | high |

### 1.F Ch. 7 Design (pp.149–170) — P-map: P3, P5, P6

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| HWFW-150 | hw-fw | Always provide an indicator (status bit or interrupt) to firmware for every event/condition it must know about that is asynchronous to its register access; "no indication" is acceptable only for truly synchronous actions (config write, instantaneous abort). | — | event list per block | all | inspect | BP 7.1.1, p.151 | high |
| HWFW-151 | timing | Provide a general-purpose hardware timer that interrupts after short delays (< 100 ms). Rule of thumb: resolution >= 1 us; range >= 10 x OS tick (OS tick 10 ms -> count to 100 ms). | t_res <= 1 us; t_range >= 10 * t_tick | OS tick, timer spec | all | inspect | BP 7.1.2, p.153 | high |
| HWFW-152 | timing | OS-timer delay quantisation: a request for N ticks yields an actual delay in ((N-1)*tick, N*tick]; to guarantee a minimum T_min use N = floor(T_min/tick) + 2 (e.g. 25 ms min on 10 ms tick -> 4 ticks -> 30..40 ms; 1 ms min on 10 ms tick -> 2 ticks). A HW timer at 1 us resolution gives <= 25.002 ms for the same request. | N_ticks = floor(T_min / t_tick) + 2 (derived) | T_min, t_tick | firmware delays | calc | §7.1.2, pp.151–153; Fig. 7.1 | medium |
| HWFW-153 | hw-fw | Use a status bit for completion of tasks guaranteed to finish within an efficient polling period; polling loops must have a max count. Heuristic: ~10 clk task -> status bit; ~1000 clk -> interrupt. | poll if t_task ~ 10 clk; IRQ if ~ 1000 clk | t_task | all FW-launched tasks | review | BP 7.1.3, p.155; §7.1.4 | high |
| HWFW-154 | hw-fw | Use an interrupt for completion of tasks not guaranteed to finish within an efficient polling period. | — | t_task_max | all | review | BP 7.1.4, p.155 | high |
| HWFW-155 | hw-fw | Use an interrupt channel for tasks that only sometimes finish quickly (e.g. abort: 1–2 clk if idle, long if buffers must drain). | — | t_task_min/max | variable tasks | review | BP 7.1.5, p.156 | high |
| HWFW-156 | hw-fw | Wire every completion/delayed event to the interrupt module so FW can either poll the Pending bit (interrupt disabled) or enable the interrupt (Listing 7.2 poll-then-block pattern). Pending must be readable while disabled; enabling an already-pending interrupt must propagate it. | — | interrupt map | all | inspect | BP 7.1.6, p.157 | high |
| HWFW-157 | hw-fw | Size Rx/Tx buffers per Table 7.1: >= one full packet/burst (no mid-packet FW intervention); larger for high-speed bulk data to cut interrupt rate; larger with no/basic OS; smaller if die-constrained; sync protocols need only the largest synchronous batch, async need multiple batches; large/flexible buffers -> DMA to external memory. Doubling 8->16 B is negligible; 8->16 KB is significant. | buf >= max_packet_bytes; async: buf >= k * batch, k > 1 | packet size, data rate, OS, die area | all I/O blocks | calc | BP 7.2.1, p.159; Table 7.1 | high |
| HWFW-158 | hw-fw | Provide data buffering, queuing and DMA chaining so the block can work ahead while FW is busy. | — | DMA feature list | all data-moving blocks | inspect | BP 7.2.2, p.159 | high |
| HWFW-159 | hw-fw | Provide double-buffered configuration registers (working set + hold set) so FW queues the next task while the current runs; the block copies hold->working at the chunk boundary and interrupts FW that hold is empty (LaserJet needs chunk-to-chunk switch within 50 ns). | switch time <= 50 ns (example) | per-chunk config regs | continuous pipelines | inspect | BP 7.2.3, p.160 | high |
| HWFW-160 | hw-fw | Make performance parameters FW-tunable: bus priorities, DMA transfer sizes, clock speeds of buses/blocks (also enables battery-vs-performance modes). | — | tunable register list | all | inspect | BP 7.2.4, p.160 | high |
| HWFW-161 | hw-fw | Maximise performance margin (design with 10–20 % headroom) so the chip can be reused in faster products; a chip at 95 % utilisation cannot. | margin >= 10–20 % | utilisation | all | calc | BP 7.2.5, p.161 | high |
| HWFW-162 | bringup | Block must not require FW interaction immediately at power-on; power-on inter-block handshakes run without FW and post results in registers. | — | boot sequence | all | review | BP 7.3.1, p.162 | high |
| HWFW-163 | bringup | Block must still work at power-on when collaborating blocks/devices are not yet powered (treat inputs as unstable; report condition to driver; provide comms-reset). | — | power-sequence cases | multi-supply systems | test | BP 7.3.2, p.162 | high |
| HWFW-164 | bringup | GPIO pins default to input at reset; all lines controlling motors/switches/etc. wake in the off/safe state. | reset dir = input | pin map reset states | all | inspect | BP 7.3.3, p.163 | high |
| HWFW-165 | power | Provide FW-accessible power (or clock-gate) control for each block; handle "re-power-on" of a block while the rest of the chip runs. | — | power-control register | all | inspect | BP 7.3.4, p.163 | high |
| HWFW-166 | hw-fw | On error, provide copious status to FW: internal and external signal levels, state-machine states, counter values, current addresses. | — | error status regs | all | inspect | BP 7.4.1, p.164 | high |
| HWFW-167 | hw-fw | Include byte-swapping in the DMA controller module instantiated throughout the chip (endianness, and a respin-saving workaround). | — | DMA module spec | all DMA | inspect | BP 7.4.2, p.165 | high |
| HWFW-168 | hw-fw | Include a CRC and/or checksum generator in the common DMA module (same algorithm everywhere; compare signatures along the pipeline to localise memory corruption). | — | DMA module spec | all DMA | inspect | BP 7.4.3, p.165 | high |
| HWFW-169 | connectors | For each chip output pin driven by multiple blocks, multiplex block outputs so exactly one block drives at any time. | — | pin map | shared pins | inspect | BP 7.4.4, p.167 | high |
| HWFW-170 | connectors | For each chip input pin fanning to multiple blocks, multiplex so only the selected block(s) receive it; non-selected block inputs tied to a defined (usually deasserted) level. | — | pin map | shared pins | inspect | BP 7.4.5, p.167 | high |
| HWFW-171 | hw-fw | Hide FW-unfriendly implementations behind translator modules (two's-complement translator for count-up counters used as count-down; gray-to-binary translator) so FW sees the natural representation on every platform. | — | counter list | all | inspect | BP 7.4.6, p.169; Fig. 7.3 | high |

### 1.G Ch. 8 Registers (pp.171–226) — P-map: P3, P4, P5

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| HWFW-172 | hw-fw | Provide register access by memory-mapped I/O where possible (port I/O and multi-step I/O only when forced). | — | bus architecture | all | inspect | BP 8.1.1, p.173 | high |
| HWFW-173 | hw-fw | Assign a unique base address to each chip (static or dynamic). | — | system memory map | all | inspect | BP 8.1.2, p.175 | high |
| HWFW-174 | hw-fw | Assign each block an address offset relative to the chip base (block_base = chip_base + block_offset). | block_base = chip_base + block_offset | chip memory map | all | inspect | BP 8.1.3, p.177 | high |
| HWFW-175 | hw-fw | Block address ranges must not overlap. | for all i != j: [base_i, base_i+size_i) and [base_j, base_j+size_j) are disjoint | block table | all | calc | BP 8.1.4, p.177 | high |
| HWFW-176 | hw-fw | Leave spare room in each block's address range for future registers (pad to next block). | — | block table | all | inspect | BP 8.1.5, p.177 | high |
| HWFW-177 | hw-fw | Align each block's starting offset to a 256-byte boundary (low two hex digits 0x00 -> 64 x 32-bit registers per chunk; a 9-register block leaves 55 spare; 110 registers need 2 chunks with 18 spare). Use 64-byte alignment only if address space is tight. | block_offset mod 256 == 0 (fallback mod 64) | block table | all | calc | BP 8.1.6, p.178 | high |
| HWFW-178 | hw-fw | Assign each register an offset relative to the block base. | reg_addr = block_base + reg_offset | register table | all | inspect | BP 8.1.7, p.178 | high |
| HWFW-179 | hw-fw | Give each sub-block (multi-instance DMA, channels, removable sections, team partitions) its own base and range with room to grow, aligned to a boundary such as 16 bytes. | subblock_offset mod 16 == 0 | register table | blocks with sub-blocks | calc | BP 8.1.8, p.179 | high |
| HWFW-180 | hw-fw | If bursting is needed, place register groups written together at burst-aligned sequential addresses (e.g. Address, Count, Control, Start), first register aligned e.g. to a quad-word. | group contiguous; start aligned | register table, access sequence | burst buses (PCIe etc.) | inspect | BP 8.1.9, p.180 | high |
| HWFW-181 | hw-fw | Put the Start register LAST in address order of its burst group so setup completes before launch. | offset(Start) = max(offset in group) | register table | burst groups | calc | BP 8.1.10, p.180 | high |
| HWFW-182 | hw-fw | Reads from unused addresses within a block's range return zeros (drive the bus, never float). | read(unused) == 0 | register table + RTL | all | test | BP 8.1.11, p.181 | high |
| HWFW-183 | hw-fw | Writes to unused addresses are ignored; decode ALL address bits of the range to avoid aliasing (ignoring bit 2 of an 8-location range aliases 0x04–0x07 onto 0x00–0x03). | write(unused) = no-op; full decode | register table + RTL | all | test | BP 8.1.12, p.181; §8.1.7 | high |
| HWFW-184 | hw-fw | Preserve every register's offset within the block when the block is instantiated in a new chip (chip base and block offset may change; register offsets may not). | reg_offset(v_new) == reg_offset(v_old) | register tables of both versions | leveraged blocks | calc | BP 8.1.13, p.182 | high |
| HWFW-185 | hw-fw | Never reuse the address of a deleted register; new registers go to never-used offsets. | — | register tables of both versions | leveraged blocks | calc | BP 8.1.14, p.183 | high |
| HWFW-186 | hw-fw | Populate a new register starting at bit 0 (LSB) and grow leftwards (masks 0x1, 0x2 rather than 0x80000000). | — | register map | new registers | inspect | BP 8.2.1, p.184 | high |
| HWFW-187 | hw-fw | Reserve bit positions for foreseeable growth (e.g. leave a hole after a 1-bit mode that may become 2-bit; allocate 8 slots for 5 similar bits). | — | register map | new registers | review | BP 8.2.2, p.184 | high |
| HWFW-188 | hw-fw | 1-bit fields may be placed anywhere. | — | register map | all | inspect | BP 8.2.3, p.186; Table 8.1 | high |
| HWFW-189 | hw-fw | 2-bit fields: anywhere within a nibble (must not straddle a nibble boundary). | floor(lsb/4) == floor((lsb+1)/4) | register map | all | calc | BP 8.2.4, p.187; Table 8.1 | high |
| HWFW-190 | hw-fw | Field alignment by width (Table 8.1): 3–4 bits nibble-aligned; 5–8 bits byte-aligned; 9–16 bits 16-bit aligned; 17–32 bits 32-bit aligned; 33–64 bits 64-bit aligned. Nibble alignment makes hex readable (four 5-bit fields of 0x14: 0x000A5294 unaligned vs 0x14141414 aligned); byte alignment lets compilers use byte ops. | lsb mod A == 0, A = 4 (w 3–4), 8 (w 5–8), 16 (w 9–16), 32 (w 17–32), 64 (w 33–64) | register map | all multi-bit fields | calc | BP 8.2.5, p.187; Table 8.1 | high |
| HWFW-191 | hw-fw | Fields wider than the register: low-order bits fill the lower-address registers, the remaining MSBs are right-justified in the last register (21-bit field on 8-bit bus: 0x00 = bits 7:0, 0x01 = 15:8, 0x02 = 20:16 right-justified). | — | register map | fields > bus width | inspect | BP 8.2.6, p.188 | high |
| HWFW-192 | hw-fw | Unused bit positions read as zero (lets one driver handle a superset of bits across versions). | read(unused bit) == 0 | register map + RTL | all | test | BP 8.2.7, p.188 | high |
| HWFW-193 | hw-fw | Writes to unused bit positions are ignored (a driver can write 1 then read back to detect whether a version implements the bit). | write(unused bit) = no-op | register map + RTL | all | test | BP 8.2.8, p.189 | high |
| HWFW-194 | hw-fw | Do not change bit assignments between block versions (otherwise every driver needs per-chip mask tables). | bit_pos(v_new) == bit_pos(v_old) for surviving bits | register maps of both versions | leveraged blocks | calc | BP 8.2.9, p.190 | high |
| HWFW-195 | hw-fw | Never reuse the position of a deleted bit; add new bits to the left of existing ones, not into holes (unless the register is full). Reserved holes may be consumed by the field they were reserved for (0x0/0x1 keep old meaning). | — | register maps of both versions | leveraged blocks | calc | BP 8.2.10, p.192 | high |
| HWFW-196 | hw-fw | Avoid write-only bits; use read/write (exceptions: security; storage-less launch registers). | — | register map | all | inspect | BP 8.2.11, p.193 | high |
| HWFW-197 | hw-fw | Any write-only register must still read back as zero (never bus-float or garbage). | read(WO) == 0 | register map + RTL | WO registers | test | BP 8.2.12, p.194 | high |
| HWFW-198 | hw-fw | Five bit types (Table 8.2): R/W (FW set/clear/read; HW read only except reset); RO (HW set/clear; FW read); WO (avoid); Interrupt W1C (HW sets, FW clears by writing 1, FW reads); Queue W1S (FW sets by writing 1, HW clears, FW reads). Writing 0 to a W1C/W1S position has no effect. | — | register map | all | inspect | §8.2.6, pp.192–194; Table 8.2 | high |
| HWFW-199 | hw-fw | Never mix different writeable bit types (R/W, W1C, W1S) in one register (mixed registers force read-modify-write with interrupt masking, Listing 8.8). | per register: count(distinct writeable types) <= 1 | register map with bit types | all | calc | BP 8.2.13, p.196 | high |
| HWFW-200 | hw-fw | Put read-only bits in a register with writeable bits only if necessary (safe but confusing). | — | register map | all | inspect | BP 8.2.14, p.196 | high |
| HWFW-201 | hw-fw | Group bits into registers by operational mode: boot-up-only (modes, timeouts), regular operation (interrupt, data), test/debug (snoop, hooks); do not mix modes in one register. | per register: one mode class | register map with mode tags | all | calc | BP 8.2.15, p.197 | high |
| HWFW-202 | hw-fw | Each block instantiation gets its own register set: identical register offsets, separate base addresses (never pack two UARTs' 8-bit fields into one 32-bit register). | base_i != base_j; offsets identical | register map | multi-instance blocks | calc | BP 8.2.16, p.199 | high |
| HWFW-203 | hw-fw | Put each frequently used (unsigned) integer in its own register (so `*reg += 2` works without mask/shift). | — | register map | all | inspect | BP 8.3.1, p.200 | high |
| HWFW-204 | hw-fw | Put every signed integer in its own register. | — | register map | signed fields | inspect | BP 8.3.2, p.201 | high |
| HWFW-205 | hw-fw | Sign-extend every signed integer to the full register width (8-bit -2 = 0xFE reads as 0xFFFFFFFE on a 32-bit bus, not 0x000000FE = 254); the extension bits mirror the field MSB and need no flip-flops. | read[31:w] = field[w-1] replicated | register map | signed fields | test | BP 8.3.3, p.201 | high |
| HWFW-206 | hw-fw | Fixed-point ("real") numbers: fix the radix point at design time with spare unused bits on BOTH sides (left for range, right for precision) so later versions widen without moving the radix. Value = raw / 2^N. Odometer example: radix at 4 -> max 15.9375 mi, step 0.0625 mi (330 ft); radix at 8 with 24 integer bits -> 16 million mi, step 20 ft; radix at 13 -> 19 integer bits ~500,000 mi, step ~8 in (chosen). | value = raw / (1 << N); max = 2^(W_int) - 2^-N; step = 2^-N | register map | fixed-point fields | calc | BP 8.3.4, p.204; Listing 8.11 | high |
| HWFW-207 | hw-fw | Put every fixed-point (real) number in its own register. | — | register map | fixed-point fields | inspect | BP 8.3.5, p.205 | high |
| HWFW-208 | hw-fw | Memory-pointer registers hold BYTE addresses even on word-addressable systems (32-bit system: bits 1:0 present but always 0); never right-shift out the low bits. | pointer width = full byte-address width; low log2(word_bytes) bits reserved 0 | register map | address registers | inspect | BP 8.3.6, p.207 | high |
| HWFW-209 | hw-fw | Any "constant" (timeout, priority, size, count) is exposed as a read/write register whose power-on default IS the constant, not hard-coded logic (10 ms engine-protocol timeout example). | reset value = design constant | register map | all tunable constants | inspect | BP 8.3.7, p.207 | high |
| HWFW-210 | hw-fw | Provide a read-only chip ID register (vendor code + device code) that uniquely identifies the chip. | — | chip register map | every chip | inspect | BP 8.4.1, p.208 | high |
| HWFW-211 | hw-fw | Provide a chip version register identifying the silicon revision or FPGA programming. | — | chip register map | every chip | inspect | BP 8.4.2, p.208 | high |
| HWFW-212 | process | Bump the chip version register on EVERY revision — including small mask changes — and on every FPGA programming that is distributed. | version(rev_n) != version(rev_m) for n != m | revision log | every spin / FPGA release | inspect | BP 8.4.3, p.208 | high |
| HWFW-213 | hw-fw | For dies with multiple bonding options, provide a read-only die-bonding-configuration register. | — | chip register map | multi-bond dies | inspect | BP 8.4.4, p.209 | high |
| HWFW-214 | hw-fw | If no dedicated version register exists, make revisions distinguishable by: a new RO register that no longer reads zero; a new R/W register that retains written ones; a new R/W bit that stays set; or a stuck-on RO bit — and document which technique is used. | — | register maps of both versions | fallback only | inspect | BP 8.4.5, p.209 | high |
| HWFW-215 | hw-fw | Provide block-level ID and version registers in every block, at a fixed offset at/near the start of the block's range (e.g. 0x0000 and 0x0004) identical across all versions. | offset(ID/version) constant, e.g. 0x0000/0x0004 | register map | every block | inspect | BP 8.4.6, p.210 | high |
| HWFW-216 | hw-fw | Update a block's version only when that block changes, never because other chip content changed. | — | version log | every block | inspect | BP 8.4.7, p.210 | high |
| HWFW-217 | process | Collaborate with the FW team to decide what internal information each block exposes (state, I/O signals, performance data, buffer contents, error info; e.g. an I2C bus switch needs a downstream bus-busy monitor). | — | information list per block | design phase | review | BP 8.5.1, p.211 | high |
| HWFW-218 | hw-fw | Task life cycle handshake: (1) FW writes config + sets Queue bit; (2) block sets Active bit when it starts; (3) block clears Queue and Active and sets Interrupt when done; (4) FW acks and reads results. Queue time = 1->2, active time = 2->3, ack time = 3->4 (Fig. 8.5). | — | register map (queue/active/interrupt bits) | every FW-launched task | inspect | BP 8.5.2, p.213 | high |
| HWFW-219 | hw-fw | Launch tasks with a Queue bit (W1S: FW sets, only HW clears) — never with a R/W bit FW must clear itself (race: too short = missed, too long = task re-runs). | queue bit type = W1S | register map | every FW-launched task | inspect | BP 8.5.3, p.213 | high |
| HWFW-220 | hw-fw | Clear the Queue bit only when the block can accept another request (variant: clear at task start allows back-to-back queuing, Fig. 8.7; clear at end forbids it, Fig. 8.6). Whatever the variant, FW must be able to read the state of the task it launched. | — | register map + timing | every FW-launched task | inspect | BP 8.5.4, p.214 | high |
| HWFW-221 | timing | Poll-vs-interrupt threshold: if queue time + active time can exceed ~50–100 clock cycles, use the interrupt response; otherwise polling on the pending bit is acceptable. FW needs the documented maximum queue and active times to decide. | IRQ if t_queue_max + t_active_max > 50..100 clk | timing table | every FW-launched task | calc | §8.5.2, p.214 | high |
| HWFW-222 | hw-fw | Put Queue bits in the same register only if their tasks may start concurrently (data transfer + timer OK; data transfer + reset NOT). | — | register map + task concurrency matrix | multi-task blocks | calc | BP 8.5.5, p.215 | high |
| HWFW-223 | hw-fw | Use shadow registers to snapshot rapidly changing or wide values: reading the low word latches the high word (48-bit counter: read low 32 -> upper 16 latched so 0x002F FFFFFFFE is returned, not 0x0030 FFFFFFFE); shadow the state that detected an error plus key signal levels. | — | register map | wide/volatile registers | inspect | BP 8.5.6, p.216; Fig. 8.8 | high |
| HWFW-224 | hw-fw | Registers must return valid, accurate, documented values whether the block is idle or active; if nothing valid exists while active, return zeros plus a content-valid bit. Never "undefined while active". | — | register map | all | test | BP 8.5.7, p.217 | high |
| HWFW-225 | hw-fw | Avoid R/W registers accessed by more than one device driver (non-atomic read-modify-write collisions; disabling interrupts/mutexes only protects the driver that obeys the rule). | count(drivers per R/W register) <= 1 | register ownership table | all | calc | BP 8.5.8, p.220 | high |
| HWFW-226 | hw-fw | Give shared registers atomic access: two address portals onto one flip-flop bank — R/W1S (set) and R/W1C (clear), both readable with identical contents (example GPIO Output: R/W1S 0x0280, R/W1C 0x0284; precedent SiI3531A Port Interrupt Enable Set/Clear). Registers of RO, W1C or W1S bits are inherently atomic; R/W registers are not. | for shared reg: exists set-alias and clear-alias | register map | chip-level interrupt enable, GPIO config, any shared reg | inspect | BP 8.5.9, p.221 | high |

### 1.H Ch. 9 Interrupts (pp.223–261) — P-map: P2, P3, P4

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| HWFW-227 | hw-fw | Design the interrupt module as a supermodule: consistent behaviour, consistent register offsets, consistent bit positions, parameterised channel count, parameterised optional registers. | — | interrupt module spec | all | inspect | BP 9.1.1, p.224 | high |
| HWFW-228 | hw-fw | Each interrupt channel occupies the SAME bit position in Pending, Enable, Source Status, Masked, Post and every other module register (one mask constant per channel, Listing 9.1). | bit(ch, reg) == ch for all reg | interrupt register maps | all | calc | BP 9.1.2, p.226 | high |
| HWFW-229 | hw-fw | Instantiate one interrupt module per block handling that block's interrupts only (add a second module if > 32 channels on a 32-bit bus). | channels per module <= bus width | interrupt map | all | inspect | BP 9.1.3, p.226 | high |
| HWFW-230 | hw-fw | The module ORs all enabled pending channels into ONE upstream interrupt line. | Interrupt = OR_i(Pending_i & Enable_i) | interrupt map | all | inspect | BP 9.1.4, p.227 | high |
| HWFW-231 | hw-fw | Instantiate a chip-level interrupt module collecting each block's line into one chip interrupt (hierarchy Fig. 9.2); a system-level module (PIC-style) collects multiple chips. | — | interrupt map | all | inspect | BP 9.1.5, p.228 | high |
| HWFW-232 | hw-fw | One interrupt source per channel — no channel sharing at block, chip or system level (shared lines force polling every device). | sources per channel == 1 | interrupt map | all | calc | BP 9.1.6, p.230 | high |
| HWFW-233 | hw-fw | The interrupt module includes a clock-synchronisation circuit (2-flop) on every incoming source (sources may come from other clock domains or combinatorial logic). | — | RTL | all | inspect | BP 9.1.7, p.230 | high |
| HWFW-234 | hw-fw | Debounce / noise-suppress every EXTERNAL interrupt source (switch bounce, long wires: crosstalk, ESD, slow edges) before it reaches the module (unfiltered line produced "pending but no CPU interrupt"). | — | pin map, RTL | external sources | inspect | BP 9.1.8, p.231 | high |
| HWFW-235 | hw-fw | Make the interrupt module edge-triggered (latching). Edge wins in 7 of 9 use cases (pulse source, active condition, idle condition, source from another block, external source, nesting, power-on); level wins only for repeated-event and shared-line cases. | — | interrupt module spec | all | inspect | BP 9.1.9, p.234; §9.1.5 | high |
| HWFW-236 | hw-fw | Trigger on the RISING edge (0 -> 1) for every channel; route negative-logic sources through an inverter rather than configuring polarity per channel. Definitions: asserting edge = deasserted -> asserted; rising = 0 -> 1 regardless of logic sense (Fig. 9.4). | trigger = rising edge | interrupt map with source polarity | all | inspect | BP 9.1.10, p.235 | high |
| HWFW-237 | hw-fw | The module's outgoing interrupt is positive logic: 1 while one or more enabled interrupts are pending. | — | RTL | all | inspect | BP 9.1.11, p.235 | high |
| HWFW-238 | hw-fw | Provide a Pending register showing pending interrupts (one bit per channel). | — | interrupt register map | all | inspect | BP 9.2.1, p.236 | high |
| HWFW-239 | hw-fw | Pending register bits are interrupt-type (W1C): writing 0 to any position does nothing; writing 1 to a non-pending position does nothing. | — | interrupt register map | all | test | BP 9.2.2, p.236 | high |
| HWFW-240 | hw-fw | Ack = write 1 (W1C), never write 0 (W0C): `*regPending = intr` acks everything just read without inversion (Listing 9.2 shows the W0C inversion bug). | ack value = pending mask | interrupt register map | all | inspect | BP 9.2.3, p.238 | high |
| HWFW-241 | hw-fw | Never clear the Pending register on read (read-clear loses interrupts to loggers, debuggers, second reads). For write-buffer latency, ack as the SECOND step of the handler (after the pending read), not the last. | — | interrupt register map | all | test | BP 9.2.4, p.239 | high |
| HWFW-242 | hw-fw | Assign channels to Pending positions in descending priority from bit 0: most frequent first (fast exit from scan loop), urgent before frequent when the urgent one cannot wait out the frequent one's worst-case service. | priority(ch) decreasing with ch index | interrupt map with frequency/urgency | all | calc | BP 9.2.5, p.240 | high |
| HWFW-243 | hw-fw | Provide an Enable register at every level including chip level (omitting the chip-level enable left an un-disableable interrupt and forced ~400 us in the ISR to ack an external I2C interrupt over the serial bus). | — | interrupt register map | all levels | inspect | BP 9.3.1, p.241 | high |
| HWFW-244 | hw-fw | Enable register: 1 = interrupt propagates; name it Enable, not Mask. | — | interrupt register map | all | inspect | BP 9.3.2, p.241 | high |
| HWFW-245 | hw-fw | Enable controls PROPAGATION of pending interrupts, not their capture: the pending flip-flop always latches edges; enabling an already-pending channel propagates immediately (catches boot-time events; ack before enable if unwanted). | Interrupt = Pending & Enable (capture independent of Enable) | RTL | all | test | BP 9.3.3, p.242 | high |
| HWFW-246 | hw-fw | All Enable bits default to 0 (disabled) at power-on reset. | reset(Enable) = 0x0 | interrupt register map reset row | all | inspect | BP 9.3.4, p.243 | high |
| HWFW-247 | hw-fw | Provide a Source Status register (RO) showing the synchronised current level of each incoming source (asserted-now, missed-edge recovery after CPU reset, FIFO drain loops, which block still pending at chip level, which edge occurred last). | — | interrupt register map | optional register | inspect | BP 9.4.1, p.244 | high |
| HWFW-248 | hw-fw | Leave Source Status positions unused for uninteresting sources (1-clock pulses; inverted Block-Active feeding Task-Done would mislead); omit the register entirely if all positions unused. | — | interrupt map with source type | optional register | inspect | BP 9.4.2, p.244 | high |
| HWFW-249 | hw-fw | Provide a Post register (write-only W1S, reads zero) so firmware can raise any channel as if hardware had (ISR testing in real interrupt context). | — | interrupt register map | optional register | inspect | BP 9.4.3, p.245 | high |
| HWFW-250 | hw-fw | For modules accessed by multiple drivers (chip level) add Atomic Enable (R/W1S) and Atomic Disable (R/W1C) portals in addition to the R/W Enable; all three read identical contents. | — | interrupt register map | multi-driver modules | inspect | BP 9.4.4, p.245 | high |
| HWFW-251 | hw-fw | Provide a Masked register (RO) = Pending AND Enable. | Masked = Pending & Enable | interrupt register map | optional register | test | BP 9.4.5, p.246 | high |
| HWFW-252 | hw-fw | Provide an interrupt Instantiation register (RO) at module offset 0x0000: bit0 S = Source Status present; bit1 P = Post present; bit2 A = Atomic enable/disable present; bit3 M = Masked present; bits 7:4 reserved; bits 12:8 C = channel count; bits 19:16 T = top channel bit position. If packed from bit 0, T + 1 = C; with holes, T >= C. 16-bit systems omit T; 8-bit omit C and T (FW writes 0xFF to Enable and reads back, e.g. 0x57 => C = 5, T = 6). | T + 1 == C (packed) else T >= C | interrupt register map | parameterised module | calc | BP 9.4.6, p.247; register map p.246 | high |
| HWFW-253 | hw-fw | Every optional register has a fixed reserved offset whether instantiated or not (e.g. Source Status always at module offset 0x10); never shift other registers into the gap. | offset(optional reg) constant | interrupt register map | parameterised module | calc | BP 9.4.7, p.247; Listing 9.5 | high |
| HWFW-254 | hw-fw | Reference channel behaviour (Listing 9.6): SignalOut <= SignalIn; Q1 <= SignalOut (2-flop sync); Pending priority on each clock: Reset -> 0, else Acknowledge -> 0, else Post -> 1, else (SignalOut & ~Q1) -> 1; Interrupt = Pending & Enable. Outputs: Interrupt, Pending (readable even if disabled), SignalOut (readable). | Pending_next = Reset?0 : Ack?0 : Post?1 : (Sync & ~Sync_d1)?1 : Pending | RTL | all | sim | §9.5.1, pp.249–251; Listing 9.6 | high |
| HWFW-255 | hw-fw | Reference module register set (Fig. 9.7/9.8): Enable (R/W), Atomic Enable (R/W1S), Atomic Disable (R/W1C) — one flop bank, 3 portals; Pending write portal (W1C, no flops) + Pending read portal; Post (W1S, reads 0); Masked (RO); Source Status (RO); Instantiation (RO). 3 address bits (wired to A[4:2] on 32-bit); data lines = instantiated channel positions; POR clears Pending and Enable. | 8 register portals; 3 address bits | interrupt register map | all | inspect | §9.5.2–9.5.3, pp.251–253 | high |
| HWFW-256 | hw-fw | For both-edge interrupts use two channels: one on the source, one on the INVERTED source (leading and trailing edges separately enable-able). | — | interrupt map | double-edge sources | inspect | BP 9.5.1, p.254 | high |
| HWFW-257 | hw-fw | Consider a trailing-edge channel for every source that stays asserted for a while (external signals such as door-open, item sensors, GPIO); short pulses need none. | — | interrupt map with source duration | external/long-asserted sources | review | BP 9.5.2, p.255 | high |
| HWFW-258 | hw-fw | With only a few double-edge sources, put the trailing-edge channel in the bit immediately above the leading-edge channel (…G F E d D C B a A). | pos(trailing) = pos(leading) + 1 | interrupt map | few double-edge sources | calc | BP 9.5.3, p.256 | high |
| HWFW-259 | hw-fw | With several double-edge sources, segregate leading-edge and trailing-edge groups at the same relative positions (holes kept where a source has no trailing channel). | pos(trailing_i) - pos(leading_i) = constant shift | interrupt map | several double-edge sources | calc | BP 9.5.4, p.257 | high |
| HWFW-260 | hw-fw | Leading group in the lower half, trailing group in the upper half of one module (FALLING_EDGE_SHIFT = 16 on 32-bit); if they do not fit, use two modules with identical channel positions. | shift = bus_width / 2 | interrupt map | several double-edge sources | calc | BP 9.5.5, p.257; Listing 9.7 | high |
| HWFW-261 | hw-fw | Every externally initiated event (signal from another block, incoming packet) gets an interrupt channel. | — | event list | all | inspect | BP 9.6.1, p.258 | high |
| HWFW-262 | hw-fw | Every FW-launched task that is not ALWAYS instantaneous gets a completion interrupt channel. | — | task list with t_max | all | inspect | BP 9.6.2, p.258 | high |
| HWFW-263 | hw-fw | Do not spend a channel on tasks that always complete instantaneously (1–2 clocks; faster than FW can re-access the block). | t_task_max <= 1–2 clk => no channel | task list with t_max | all | calc | BP 9.6.3, p.258 | high |
| HWFW-264 | hw-fw | For interrupts that can recur without FW intervention provide a buffer/FIFO, an interrupt counter and/or an overflow (underrun) interrupt (Unity: 25–30 ms between done interrupts; a separate underrun interrupt flagged missed service). | — | interrupt map, buffer table | repeating interrupts | inspect | BP 9.6.4, p.259 | high |
| HWFW-265 | hw-fw | Place interrupt module registers in address space that is always visible (no page switching or indirection needed inside the ISR). | — | address map | paged/indirect architectures | inspect | BP 9.6.5, p.260 | high |
| HWFW-266 | hw-fw | Ack-before-enable vs enable-before-ack must not differ between chips; with the standard module (pending independent of enable) the sequence is: ack stray pending, then enable. | — | interrupt module spec | all | review | §9.8 tale, p.261 | high |

### 1.I Ch. 10 Aborts, etc. (pp.263–276) — P-map: P3, P5, P6

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| HWFW-267 | hw-fw | Three cancel levels (Table 10.1): Halt (stop/pause) — stops task, clears Active/go bit, all else unchanged, resume or abort follows; Abort (soft/warm reset) — FW-only, cancels task, task registers and state machines to idle, gracefully ends inter-block interaction, ready for next task; Reset (hard/cold/POR) — all registers/counters/buffers/state machines to defaults, FW must reconfigure incl. re-enabling interrupts. Map events (power-on, watchdog, button, FW, block error) to the right action. | — | block spec | all | inspect | §10.1, p.264; Table 10.1 | high |
| HWFW-268 | hw-fw | Provide a Halt function: stop the current task, clear the task Active (go) bit, leave every other register and buffer unchanged. | — | block spec | all | inspect | BP 10.1.1, p.265 | high |
| HWFW-269 | hw-fw | Give firmware access to Halt (troubleshooting, mid-operation config changes, resume where feasible). | — | register map | all | inspect | BP 10.1.2, p.265 | high |
| HWFW-270 | hw-fw | The block halts itself when it detects an error, leaving DMA address/count, config, status, state-machine state and buffers intact for inspection; FW then aborts. | — | block spec | all | test | BP 10.1.3, p.266 | high |
| HWFW-271 | hw-fw | Provide a Reset function: stop all tasks; all registers, counters, buffers, state machines to defaults. Buffers need only be marked empty (count 0, pointers home), not zero-filled. | — | block spec | all | test | BP 10.2.1, p.266 | high |
| HWFW-272 | hw-fw | Every control register comes out of reset in a "safe" state: inactive, disabled, idle (a stepper-motor control must reset to off). | reset(control bits) = inactive/off | register map reset row | all | inspect | BP 10.2.2, p.267 | high |
| HWFW-273 | bringup | Power-on circuitry drives a reset pin on every chip that resets every block. | — | schematic / reset tree | all | inspect | BP 10.2.3, p.267 | high |
| HWFW-274 | hw-fw | Firmware can invoke the synchronous and/or asynchronous reset (some designs: async assert, sync deassert). | — | register map | all | inspect | BP 10.2.4, p.267 | high |
| HWFW-275 | hw-fw | Provide an Abort function: stop the current task and reset the associated task registers and state machines (needed for internal errors, residual-data cleanup, producer/consumer failure, buffer full, corrupt data, timeout, FW-detected condition, user button; some products abort ~60 % of pages as normal flow). | — | block spec | all | test | BP 10.3.1, p.269 | high |
| HWFW-276 | hw-fw | Provide abort for EVERY task in the block (Tx and Rx, compress and decompress, pipeline stages, even a boot-time pulse generator). | count(tasks without abort) == 0 | task list | all | calc | BP 10.3.2, p.270 | high |
| HWFW-277 | hw-fw | Give firmware access to Abort; only firmware invokes abort (block invokes halt; power-on invokes reset). | — | register map | all | inspect | BP 10.3.3, p.270 | high |
| HWFW-278 | hw-fw | Keep firmware's role in abort minimal (ideally one bit). Abort must: return all state machines to idle, reset task counters/registers, mark buffers empty, erase residual data, shut down in order, respect non-reset neighbours; it must NOT reset interrupt enables or boot-time constants. | — | abort spec | all | inspect | BP 10.3.4, p.271; §10.4.2 | high |
| HWFW-279 | hw-fw | Provide an abort-done interrupt channel if abort is not always instantaneous (Listing 10.1: disable abort-done, clear pending, set abort queue bit, poll pending up to MAX_ABORT_LOOP = 10, else enable and block). | — | interrupt map, t_abort_max | all | inspect | BP 10.3.5, p.271; Listing 10.1 | high |
| HWFW-280 | hw-fw | Abort responds under every condition, including when the block is already idle (Unity: idle state ignored the abort bit, which then killed the NEXT job). | — | state machine spec | all | test | BP 10.3.6, p.273 | high |
| HWFW-281 | hw-fw | Abort outcome is identical busy or idle: always clears the abort queue bit and always generates the abort-done interrupt. | — | abort spec | all | test | BP 10.3.7, p.273 | high |
| HWFW-282 | hw-fw | Every state of every state machine in the block, including all idle states, responds to abort (cleanup and return to idle). | for all FSM, for all states: abort transition exists | RTL | all | sim | BP 10.3.8, p.274 | high |
| HWFW-283 | hw-fw | Each block owns an abort that services only itself; it never resets, cancels or erases anything in another block. | — | abort spec | all | inspect | BP 10.3.9, p.274 | high |
| HWFW-284 | hw-fw | Abort leaves collaborating blocks in the ready state via one of: cancel protocol (block A sends Cancel to B), driver coordination (driver A tells driver B; both abort), or dummy data (A completes B's byte count with dummy/ignored data). | — | inter-block protocol spec | inter-block pipelines | review | BP 10.3.10, p.275; Fig. 10.2 | high |
| HWFW-285 | process | Abort design and test get the same priority as normal operation (a defect-ridden block needed a 250-line abort routine with an 11-page explanation; fixed block: ~10 lines). | — | test plan | all | review | §10.4.3, p.274; §10.5 tale, p.276 | high |

### 1.J Ch. 11 Hooks (pp.277–299) — P-map: P1, P6, P7

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| HWFW-286 | hw-fw | Allocate silicon for test/debug hooks (insurance: if 1 of 10 hooks averts a respin all 10 paid off). Hooks must not add defects to the primary function. | — | area budget | all | review | BP 11.1.1, p.278 | high |
| HWFW-287 | hw-fw | Choose hooks from lessons learned on previous defects; put more hooks on new/risky logic than on mature logic. | — | defect history | all | review | BP 11.1.2, p.279 | high |
| HWFW-288 | process | Collaborate with firmware engineers on hook design. | — | — | design phase | review | BP 11.1.3, p.279 | high |
| HWFW-289 | hw-fw | Test/debug registers live in their own address range or page, placed AFTER the normal registers; they are unsupported and may move between versions. | offset(debug regs) > max offset(normal regs) | register map | all | calc | BP 11.1.4, p.280 | high |
| HWFW-290 | hw-fw | Design and document contingency plans per sub-block: what if it does not work — can it be disabled/bypassed and the rest used? | — | block spec | all | review | BP 11.1.5, p.280 | high |
| HWFW-291 | process | Fix defects in each new version so hook-based workarounds are removed; a hook needed for an architectural (not logic) defect gets promoted to a supported, documented, tested feature. | — | defect list, workaround list | next version | review | BP 11.1.6, p.281 | high |
| HWFW-292 | hw-fw | Provide read access to all internal (non-portal) registers — internal signals, conditions, values, shadow/working copies. | — | register map | all | inspect | BP 11.2.1, p.282 | high |
| HWFW-293 | hw-fw | Provide register(s) exposing key internal signals (busy/active, inter-section, FSM inputs/outputs, counter enables, mux selects; 32 signals per 32-bit register); take a snapshot when a set spans multiple registers. | — | register map | all | inspect | BP 11.2.2, p.283 | high |
| HWFW-294 | hw-fw | Provide register(s) showing the current level of key input and output pins (protocol/handshake diagnosis). | — | register map, pin map | all | inspect | BP 11.2.3, p.283 | high |
| HWFW-295 | hw-fw | Counter and address registers are readable even while changing rapidly (unchanging successive reads => stuck/stalled/done; optionally a Stalled bit next to Active). | — | register map | all | inspect | BP 11.2.4, p.283 | high |
| HWFW-296 | hw-fw | Expose in-progress DMA parameters: current address, bytes left in this link, initial address, initial count, pointer to next link (Table 11.1 diagnosis by where the pointers stopped). | — | DMA register map | all DMA | inspect | BP 11.2.5, p.284 | high |
| HWFW-297 | hw-fw | Provide read access to internal memories and their support registers (FIFOs, buffers, head/tail pointers, counters), including stale contents. | — | register map | all | inspect | BP 11.2.6, p.285 | high |
| HWFW-298 | hw-fw | Provide state-machine register(s) with nibble-aligned fields showing current state, next state, incoming and outgoing signals for each FSM (example State Machine Register 0x0220: X bits 2:0, Y bits 12:8, Z bits 19:16; Main FSM: C bits 4:0, N bits 12:8, Q/A/M inputs bits 16–18, B/R/D outputs bits 24–26). | field lsb mod 4 == 0 | register map | all FSMs | inspect | BP 11.2.7, p.287 | high |
| HWFW-299 | hw-fw | Provide access points in each pipeline for firmware to extract data from and insert data into inter-stage FIFOs (stage-isolated test; also drained stuck FIFOs during abort). | — | pipeline diagram | pipelines | inspect | BP 11.3.1, p.288 | high |
| HWFW-300 | hw-fw | Provide means to simulate external input/output signals (e.g. a test waveform/sync-pulse generator) so the block can be exercised without its partner. | — | block spec | blocks with external I/O | inspect | BP 11.3.2, p.288 | high |
| HWFW-301 | hw-fw | Allow firmware to load any value into each counter and state machine (preload almost-full FIFO counts; force hard-to-reach states; unstick). | — | register map | all | inspect | BP 11.3.3, p.289 | high |
| HWFW-302 | hw-fw | Provide FW-readable and resettable event counters on key events (512-pulse diagnosis: 0 = not connected; 1 = latch not clearing; 511/513 = off-by-one/noise; 512 = fault inside block; 1242 = heavy noise/floating pin); also usable for rate measurement over 1 s. | — | register map | all | inspect | BP 11.4.1, p.290 | high |
| HWFW-303 | hw-fw | Provide performance probes: bus busy/idle counters, bus-contention counter, memory-access counters, block idle-time counter, DMA-blocked counters, shared-resource utilisation/blocking. | utilisation = busy / (busy + idle) | counter registers | all | measure | BP 11.4.2, p.291 | high |
| HWFW-304 | hw-fw | One-shot timeout counters stop and retain their count when the awaited event arrives, readable until rewritten/restarted (a 10 ms timeout observed to complete in < 2 ms can be tightened to 3 ms). | — | timer registers | all timeouts | inspect | BP 11.4.3, p.291 | high |
| HWFW-305 | hw-fw | Periodic (reloading) timers copy their count into a snapshot register on every event. | — | timer registers | periodic watchdogs | inspect | BP 11.4.4, p.292 | high |
| HWFW-306 | hw-fw | Add a simple trace buffer (state visited + clocks dwelled, Table 11.2) for complicated/high-risk state machines. | — | FSM list | complex FSMs | inspect | BP 11.4.5, p.293 | high |
| HWFW-307 | hw-fw | Provide a data-transfer breakpoint: halt the pipe and interrupt firmware when specified data criteria (marker, null) are seen. | — | block spec | data pipes | inspect | BP 11.4.6, p.293 | high |
| HWFW-308 | hw-fw | Provide a bypass path around EVERY sub-block, even when there is only one (isolates faults; a decompressor bypass exposed a DMA byte-order defect). | for all sub-blocks: bypass mux exists | pipeline diagram | all | inspect | BP 11.5.1, p.295 | high |
| HWFW-309 | connectors | Provide extra unassigned GPIO pins for debugging and last-minute fixes. | — | pin map | spare pins exist | inspect | BP 11.5.2, p.295 | high |
| HWFW-310 | hw-fw | Provide muxes so firmware can route selected internal signals to GPIO pins for scope observation. | — | pin map, RTL | all | inspect | BP 11.5.3, p.295 | high |
| HWFW-311 | hw-fw | Instantiate a separate test/debug interrupt module fed by internal signals, pins, FSM idle/interesting states, counter zero/max; all channels default disabled; its one line feeds the block's main module. | — | interrupt map | all | inspect | BP 11.5.4, p.296 | high |
| HWFW-312 | hw-fw | Include a debug RS-232 UART with a generous hardware buffer (1 KB or 4 KB) so ISR-level logging need not re-enter interrupts; costs >= 2 pins. | buf >= 1–4 KB | pin map, block list | all | inspect | BP 11.5.5, p.297 | high |
| HWFW-313 | hw-fw | Consider a dedicated debug processor in multi-processor SoCs to monitor/peek/poke without disturbing the others. | — | SoC architecture | multi-CPU SoC | review | BP 11.5.6, p.298 | high |

### 1.K Appendix B block-specification exemplar (pp.327–343) — concrete values Anvil can pattern-match

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| HWFW-314 | hw-fw | Exemplar block register table (address order): 0x0000 ID/Version, 0x0004 Instantiation, 0x0020 Interrupt Instantiation, 0x0024 Interrupt Pending, 0x0028 Interrupt Enable, 0x002C Interrupt Source, 0x0040 Control, 0x0044 Configuration, 0x0048 Status, 0x0050 Current Speed, 0x0054 Current Distance, 0x0058 Trip Log Address, 0x005C Trip Log Byte Count, 0x0070 Debug — ID/version first, interrupt sub-block 16-byte aligned at 0x20, debug last with a gap. | sub-block offsets mod 16 == 0; debug after normal | register table | template usage | inspect | App. B, Table B4, p.331 | high |
| HWFW-315 | hw-fw | ID/Version register layout: bits 31:16 block ID (0x0017), bits 7:0 version code, RO; version-code map documented (Table B6: 0x04 = C, 0x03 = B, 0x02 = unreleased batch, 0x01 = A, 0x00 = prototypes). | — | register map | every block | inspect | App. B §B.2.2.1, p.332 | high |
| HWFW-316 | hw-fw | Control register as R/W1S queue bits (A abort bit0, S stop bit1, M monitor bit2, C calibrate bit3): only one may be set; if a write has several 1s the least-significant wins; abort overrides and clears others; reads show at most one bit; excluded feature bits do not exist and writes to them do nothing. | popcount(control) <= 1 | register map | multi-task control regs | test | App. B §B.2.2.7, p.335 | high |
| HWFW-317 | hw-fw | Fixed-point exemplar: Speed I bits 19:13, F bits 12:8; Distance I bits 24:13, F bits 12:5 — both radix at 13, unused bits read 0, one macro REG_2_REAL(reg) = reg / (1<<13). Speed 0–127.97 (mph or kph) step 0.03; distance 0–4095.996 mi step 0.004 mi (21 ft) or 0.004 km (4 m); refreshed every 0.1 s; hold last value on stop; zeroed on abort. | value = raw / 2^13 | register map | fixed-point fields | calc | App. B §B.2.2.10–11, B.3.3, pp.337–338, 342 | high |
| HWFW-318 | hw-fw | Buffer address/count exemplar: address 32-bit byte address, must be 16-byte (quad-word) aligned (low 4 bits ignored); writes ignored while logger active; read = next store location; unchanged by abort. Byte count: multiple of 12 (bytes per event) else unpredictable; min 0x0C (1 event), max 0xC0 (16 events); debug mode raises max to 256 events = 3072 bytes; read = bytes remaining this pass. | addr mod 16 == 0; count mod 12 == 0; 0x0C <= count <= 0xC0 | register map | DMA/log buffers | calc | App. B §B.2.2.12–13, p.339; §B.2.2.14 p.340 | high |
| HWFW-319 | hw-fw | Interrupt exemplar: Pending/Enable bits E event-stamp (bit0, <= ~1/s, circular buffer overwrites if unserviced), S speed alarm (bit1), B battery low (< 10 %, bit2), C calibration done (bit3), F calibration failure (bit4), A abort done (bit5); Source register exposes only S and B (long-asserted), not the pulses. Interrupt Instantiation reset = 0x00050601 (S=1, C=6, T=5). | — | register map | template usage | inspect | App. B §B.2.2.3–6, pp.333–335 | high |
| HWFW-320 | hw-fw | Chip-specific table exemplar (Table B3): per chip — block version, base address, interrupt mask bit, instantiated buffer size (128/64/128/32/32), notes such as "pedal strain input not tied to pin but tied low". Errata exemplar (§B.5): "reset logic defect — reset the block twice after power-up" (Criterion ASIC). | — | block doc | template usage | inspect | App. B Table B3 p.330; §B.5 p.343 | high |
| HWFW-321 | hw-fw | Debug register exemplar (0x0070): R/W bits D debug-mode, X 10x-multiplier, E debug-events; RO bits J, M mirror internal signals; documented with the warning that contents may change in future versions; must be 0 in normal operation. | — | register map | test/debug regs | inspect | App. B §B.2.2.14, p.340 | high |

## 2. Formulas & tables (numbers)

### 2.1 Numeric anchors stated in the text

| quantity | value | condition | source |
|---|---|---|---|
| ASIC respin delay | up to 4 months | fabricated chip (not FPGA) | §1, p.1; §1.2.2 p.10 |
| ASIC respin cost | "several million dollars" / "millions" | depends on node (90 nm, 65 nm ...) | §1, p.1 |
| Share of respins due to functional/logic errors | 45–70 % | Blyler / Ying surveys | §1.2.2, p.10 |
| Share of engineers who are introverts | 61 % (Capretz) / 75 % (anecdotal) | collaboration planning | §3.3, p.44 |
| Mono video driver lines that were workarounds | > 10 % of lines; ~50 % of dev time | Unity ASIC case | §4.4.2, p.65 |
| Race workaround | set bit 3x (platform-specific; 4x elsewhere) | R/W launch bit | §4.4.1, p.63 |
| UART buffer | 8 -> 128 bytes "very little impact" | single UART | §4.5.2, p.67 |
| DMA buffer | 128 -> 256 bytes too costly x N instances; low-traffic ~32 B, high-traffic ~512 B | multiple DMA controllers | §4.5.2, p.67 |
| Doc review turnaround | a few days to a week | FW reviewers | §5.3.3, p.86 |
| Packet inter-arrival example | basic every 45 us; extended (16 B payload) every 105 us | doc example | §5.8.1, p.113 |
| Clock/second conversion | 100 MHz: 1,000,000 clk = 10 ms; 133 MHz: 1,000,000 clk = 7.5 ms, 10 ms = 1,330,000 clk | Table 5.7 | p.114 |
| Task timing examples | 128 clk fixed; ~1500 clk per 1 KB; abort >= 10 clk active, immediate idle, up to 20,480 clk if output stalled; "less than 15 clk" typical abort | doc examples | §5.8.1, p.112 |
| Error-handling share of code | ~80 % error handling / ~20 % normal path | rule of thumb | §5.9, p.114 |
| Static power of unused logic | "significant problem at 65 nm and below" | superblock trade-off | §6.1.3, p.130 |
| Parameterisation threshold | remove a block at ~25 % of die; not a ~7000-gate UART on 10 M gates | superblock | §6.4.1, p.140 |
| UART instantiation buffer field | B = size / 8 bytes; 0x01 (8 B) .. 0x20 (256 B) | example register | p.143 |
| Time to market | product 3 months sooner; op-cost 10 % or 25 % | value questions | §6.1.2, p.128 |
| OS tick sizes | 1 ms, 10 ms, 100 ms typical | OS timers | §7.1.2, p.151 |
| OS timer quantisation | 3 ticks of 10 ms -> 20..30 ms; 4 ticks -> 30..40 ms; 1 tick -> 0..10 ms (10 % chance < 1 ms); 2 ticks guarantee >= 1 ms | Fig. 7.1 | pp.152–153 |
| HW timer rule of thumb | resolution >= 1 us; range >= 10 x OS tick (100 ms for 10 ms tick); gives <= 25.002 ms for 25 ms | general-purpose timer | §7.1.2, p.153 |
| Poll vs interrupt | 10 clk -> status bit; 1000 clk -> interrupt; boundary "50 to 100 clock cycles" | task completion | §7.1.4 p.155; §8.5.2 p.214 |
| Chunk switch time | 50 ns | LaserJet raster chunks -> double-buffered regs | §7.2.2, p.160 |
| Performance margin | design 10–20 % headroom; 95 % utilised cannot go faster | chip reuse | §7.2.4, p.161 |
| Block alignment | 256-byte boundary (64 x 32-bit regs); fallback 64-byte | address map | §8.1.3, p.177–178 |
| Sub-block alignment | 16-byte boundary | address map | §8.1.5, p.179 |
| Field alignment | Table 8.1 (below) | bit layout | p.186 |
| Odometer fixed point | radix 4: max 15.9375 mi step 0.0625 mi (330 ft); 8I.6F: ~256 mi step 1/64 mi (83 ft); radix 8 + 24 int bits: 16 M mi step 20 ft; radix 13: 19 int bits ~500,000 mi step ~8 in | example | §8.3.2, pp.202–204 |
| Engine timeout constant | 10 ms in a R/W register | example | §8.3.4, p.207 |
| Shadow counter example | 48-bit counter: low read latches upper 16 (0x002F not 0x0030) | Fig. 8.8 | p.216 |
| Atomic register example | R/W1S at 0x0280, R/W1C at 0x0284 | GPIO output | p.221 |
| ISR stuck acking external I2C interrupt | ~400 us | missing chip-level enable | §9.3 tale, p.240 |
| Done-interrupt window | 25–30 ms between done interrupts; underrun IRQ if missed | Unity video | §9.7.2, p.259 |
| Interrupt instantiation read-back | write 0xFF to Enable, read 0x57 => C = 5, T = 6 | 8-bit system | §9.4.5, p.247 |
| MAX_ABORT_LOOP | 10 polls before enabling abort-done interrupt | Listing 10.1 | p.272 |
| Abort routine size | 250 lines + 11-page doc (buggy block) vs ~10 lines (fixed) | Unity video | §10.5, p.276 |
| Pages needing abort in normal flow | ~60 % | one LaserJet product | §10.4.1, p.269 |
| Event counter diagnosis | expected 512: 0 / 1 / 511 / 512 / 513 / 1242 | §11.4.1 | p.290 |
| Timeout tuning | 10 ms timeout, events < 2 ms => set 3 ms | one-shot timer hook | §11.4.2, p.291 |
| Debug UART buffer | 1 KB or 4 KB; >= 2 pins | §11.5.2 | p.297 |
| Log buffer exemplar | 12 bytes/event; 0x0C..0xC0 (1..16 events); debug 256 events = 3072 B; 16-byte aligned address | App. B | pp.339–340 |
| Exemplar speed/distance | speed 0–127.97 step 0.03; distance 0–4095.996 step 0.004 (21 ft / 4 m); refresh 0.1 s; battery-low 10 %; event stamp <= 1/s; speed log >= 15 s apart; distance log every 0.1 mi; time stamp every 15 s | App. B | pp.336–338 |
| Exemplar block history | brake sampling 25 -> 75 samples/s; internal clock 100 -> 125 MHz | Table B2 | p.330 |

### 2.2 Table 8.1 — Field alignment by bit-field size (p.186)

| bit-field size (bits) | required alignment |
|---|---|
| 1 | any bit |
| 2 | anywhere within one nibble |
| 3–4 | nibble (4-bit) aligned |
| 5–8 | byte (8-bit) aligned |
| 9–16 | 16-bit aligned |
| 17–32 | 32-bit aligned |
| 33–64 | 64-bit aligned |

Alignment test: `lsb mod A == 0` with A from the table; for 2-bit fields `floor(lsb/4) == floor((lsb+1)/4)`.

### 2.3 Table 8.2 — Bit types and who may set / clear / read (p.194, reconstructed from prose)

| bit type | FW set | FW clear | FW read | HW set | HW clear | HW read | notes |
|---|---|---|---|---|---|---|---|
| Read/Write | yes | yes | yes | no (reset only) | no (reset only) | yes | config/control/enable/output level |
| Read-Only | no | no | yes | yes | yes | yes | status, pin level, timer value |
| Write-Only | yes | yes | no | no | no | yes | avoid; must still read 0 |
| Interrupt (W1C) | no | yes (write 1) | yes | yes | no | yes | write 0 = no-op |
| Queue (W1S) | yes (write 1) | no | yes | no | yes | yes | write 0 = no-op |

Atomicity: RO, W1C and W1S registers are atomically accessible; R/W registers are not (§8.5.4, p.219).

### 2.4 Table 10.1 — Halt / Abort / Reset (p.264)

| function (aliases) | who invokes | task | outcome |
|---|---|---|---|
| Halt (Stop, Pause) | block on error detection; FW for inspection | stop current task at a good stopping place (few clocks) | registers unchanged except Active/go bit cleared; FW resumes or aborts |
| Abort (Soft Reset, Warm Reset) | FW only | cancel task, all state machines to idle, gracefully end inter-block interaction, ready for new task | task-associated registers cleared; block ready for another task; interrupt enables and boot constants retained |
| Reset (Hard, Cold, Power-on Reset) | power-on circuitry; FW for unrecoverable problems | abort all operations regardless of consequence | all registers to defaults; block must be reconfigured incl. re-enabling interrupts |

### 2.5 Table 7.1 — Buffer-size guidelines (p.158)

| system attribute | guideline |
|---|---|
| packet / burst size | buffer >= all bytes of a multi-byte packet or burst; no mid-packet FW intervention |
| quantity of data | large, high-speed data: bigger buffer lowers interrupt frequency/overhead |
| operating system | no/basic OS: bigger HW buffer; full OS with per-driver threads/buffers: smaller HW buffer OK |
| space on chip | constrained die: smaller buffer, FW takes more load |
| synchronicity | synchronous protocol: buffer = largest synchronous batch; asynchronous: several batches |
| buffer location | small fixed buffers on chip; large/flexible: DMA to external memory |

Area sanity: 8 -> 16 B doubling negligible; 8 KB -> 16 KB significant (p.159).

### 2.6 Table 11.1 — Diagnosing DMA transfer problems from address/count registers (p.284)

| DMA register status | DMA from memory (read) | DMA to memory (write) |
|---|---|---|
| address & count unchanged from what FW wrote | transfer never started; DMA registers set up wrong | block never gave data; block set up wrong |
| one burst size off from start | DMA started but block did not consume data; block set up wrong | (one burst from end) last byte stuck inside block |
| somewhere mid-transfer | corrupt data caused block error/quit; current address marks the vicinity | block terminated early; count shows how much reached memory |
| indicates completed transfer but block not finished | block expects more data than DMA was programmed for | block has more data than DMA was programmed for |

### 2.7 Address arithmetic (Ch. 8)

```
block_base   = chip_base + block_offset           # chip_base static (#define) or dynamic (getChipBaseAddr(CHIP_ID))
reg_addr     = block_base + reg_offset            # reg_offset invariant across chips/versions
block_offset mod 256 == 0                          # 64 x 32-bit registers per 256-byte chunk
subblock_off mod 16  == 0
bit_mask(n)  = 1 << n                              # LSB = bit 0 => mask independent of register width
fixed_point  = raw / (1 << RADIX)                  # RADIX fixed for all versions
sign_extend  : read[W-1:w] = field[w-1]            # w-bit signed field in W-bit register
```

### 2.8 OS-timer / hardware-timer delay bounds (§7.1.2)

```
actual_delay(N ticks) in ( (N-1)*tick , N*tick ]          # request can start anywhere in a tick window
N_min_for(T_min)      = floor(T_min / tick) + 2           # derived; 25 ms @ 10 ms tick -> 4 ticks -> (30,40] ms
HW timer: resolution <= 1 us, range >= 10 * tick          # 25 ms request -> <= 25.002 ms
```

### 2.9 Interrupt channel truth table (Listing 9.6, p.250)

```
posedge Clock:  SignalOut <= SignalIn;  Q1 <= SignalOut          # 2-flop synchroniser
posedge Clock or Reset:
    if Reset          Pending <= 0
    else if Ack       Pending <= 0
    else if Post      Pending <= 1
    else if SignalOut & ~Q1   Pending <= 1                         # rising edge of synchronised source
Interrupt = Pending & Enable
```

### 2.10 Interrupt instantiation register (p.246)

| bits | field | meaning |
|---|---|---|
| 0 | S | Source Status register instantiated |
| 1 | P | Post register instantiated |
| 2 | A | Atomic enable/disable registers instantiated |
| 3 | M | Masked register instantiated |
| 7:4 | r | reserved for future optional registers |
| 12:8 | C | number of channels instantiated |
| 19:16 | T | bit position of top channel; packed => T + 1 = C; holes => T >= C |

### 2.11 Compatibility ladder (§4.3.1, pp.59–60) — rank the change, lower is better

| rank | change class | FW impact |
|---|---|---|
| 1 | no impact (e.g. widen 8-bit int field read as 32-bit) | none, forward + backward compatible |
| 2 | superset bits (old A,B,C; new A,B,D at new position) | driver handles superset; unused bits read 0 |
| 3 | legacy mode at power-up | old driver works; new driver switches modes |
| 4 | version number | driver keeps version->behaviour table; not forward compatible |
| 5 | version clues (set a bit only one version has; read back) | works on unknown future versions |
| 6 | incompatible | rewrite driver |

### 2.12 Table 4.1 — Old/new block x driver pairing (p.61)

| | driver: old only | driver: compatible-new only | driver: incompatible-new only | driver: old + new |
|---|---|---|---|---|
| old block | works | might work; confused by missing features | will not work | works |
| compatible new block | works (cannot use new features) | works | n/a | works, little version code |
| incompatible new block | will not work | n/a | works | works, lots of version code |

## 3. Mechanizable checks

All checks take Anvil's tabular ICD inputs: `registers` (block, name, offset, width, access, reset, mode_class, owner_drivers), `fields` (register, name, lsb, width, type ∈ {RW,RO,WO,W1C,W1S}, reset ∈ {0,1,X}, numeric_kind ∈ {bool,uint,sint,fixed,ptr,enum}, radix, units, min, max, illegal_response, abort_effect), `blocks` (name, offset, size, version, id_offset), `interrupts` (module, channel, source, edge, polarity, external, repeating, t_min_recur, priority, trailing_of), `tasks` (block, queue_bit, active_bit, done_irq, t_start_min/typ/max, t_done_min/typ/max, abort_irq, t_abort_max, concurrent_with), `pins` (pin, blocks[], usage_window, reset_dir, reset_level, mux), `errors` (block, code, causes[], stops, block_state, data_state, recovery), `timers` (resolution, range), `os` (tick). Margin is reported as slack in the check's own unit; pass = slack >= 0.

| check | inputs | formula | pass criterion | margin | source rows |
|---|---|---|---|---|---|
| CHECK-block-align | blocks.offset | offset mod 256 | == 0 (fallback: mod 64 == 0 if `tight_address_space`) | n/a (boolean) | HWFW-177 |
| CHECK-block-no-overlap | blocks.offset,size | pairwise interval intersection | empty for all pairs | min gap between consecutive blocks (bytes) | HWFW-175 |
| CHECK-block-spare | blocks.size, registers per block | spare = size - (max reg offset + width/8) | spare > 0 (recommend >= 25 %) | spare bytes | HWFW-176 |
| CHECK-subblock-align | sub-block base offsets | base mod 16 | == 0 | n/a | HWFW-179 |
| CHECK-reg-offset-invariant | registers(v_old), registers(v_new) by name | offset_new - offset_old | == 0 for every surviving register | count of moved registers (must be 0) | HWFW-184 |
| CHECK-reg-no-reuse | registers(v_old) deleted, registers(v_new) added | added.offset ∩ deleted.offset | empty | n/a | HWFW-185 |
| CHECK-bit-pos-invariant | fields(v_old), fields(v_new) by (register, name) | lsb_new - lsb_old | == 0 for surviving fields; new fields have lsb > max(lsb_old) unless filling a documented reserved hole | count moved (must be 0) | HWFW-194, HWFW-195 |
| CHECK-bit-no-reuse | deleted fields, added fields | overlap of bit ranges | empty (unless register full) | n/a | HWFW-195 |
| CHECK-field-align | fields.lsb,width | A(width) per Table 8.1; lsb mod A; 2-bit nibble straddle test | == 0 / no straddle | n/a | HWFW-188–190 |
| CHECK-field-lsb-first | fields per new register | min(lsb) | == 0 for a newly created register (bits packed from LSB) | n/a | HWFW-186 |
| CHECK-no-mixed-writeable | fields.type per register | distinct({RW,WO,W1C,W1S} ∩ types) | count <= 1 | n/a | HWFW-199 |
| CHECK-ro-with-writeable | fields.type per register | RO present AND writeable present | warn (allowed only "if necessary") | n/a | HWFW-200 |
| CHECK-mode-class | registers.mode_class of fields | distinct mode classes per register | == 1 (boot / regular / debug) | n/a | HWFW-201 |
| CHECK-instance-separation | fields.instance, registers.block | fields from >1 instance in one register | none; instance bases distinct; offsets identical across instances | n/a | HWFW-202 |
| CHECK-signed-own-reg | fields.numeric_kind == sint | other fields in same register | none; and width extension documented | n/a | HWFW-204, HWFW-205 |
| CHECK-fixed-own-reg | fields.numeric_kind == fixed | other fields in same register; spare bits left and right of field | none; spare_left >= 1 and spare_right >= 1; radix identical across versions | spare bits each side | HWFW-206, HWFW-207 |
| CHECK-int-own-reg | fields.numeric_kind == uint and frequent | other fields in same register | none (warn) | n/a | HWFW-203 |
| CHECK-ptr-byte-units | fields.numeric_kind == ptr | width == address bus width; low log2(word) bits reserved 0 | true | n/a | HWFW-208 |
| CHECK-wo-reads-zero | fields.type == WO | count | 0 preferred; if present, doc says reads 0 | n/a | HWFW-196, HWFW-197 |
| CHECK-reset-documented | fields.reset | value ∈ {0,1,X} for every bit of every register | 100 % | count undocumented | HWFW-094 |
| CHECK-type-documented | fields.type | non-empty for every field | 100 % | count missing | HWFW-093 |
| CHECK-numeric-doc | fields where numeric_kind != bool | units, min, max, illegal_response non-empty | 100 % | count missing | HWFW-088 |
| CHECK-abort-effect-doc | fields.abort_effect | non-empty for control/status/count fields | 100 % | count missing | HWFW-097 |
| CHECK-control-reset-safe | fields of mode_class boot/regular with type RW or W1S controlling outputs | reset value == inactive/disabled | true | n/a | HWFW-272 |
| CHECK-enable-reset-zero | interrupt Enable registers | reset value | == 0 | n/a | HWFW-246 |
| CHECK-enable-naming | interrupt registers.name | contains "Mask" | false; a register named Enable exists per module | n/a | HWFW-104, HWFW-244 |
| CHECK-pending-w1c | Pending register fields.type | type | == W1C for all channels; no read-clear flag | n/a | HWFW-239–241 |
| CHECK-irq-channel-align | interrupts.channel vs bit position in Pending/Enable/Source/Masked/Post | bit(ch, reg) | equal across all module registers | n/a | HWFW-228 |
| CHECK-irq-one-source | interrupts grouped by (module, channel) | count(sources) | == 1 | n/a | HWFW-232 |
| CHECK-irq-rising-edge | interrupts.edge, polarity | edge == rising; negative-logic sources flagged `inverted` | true | n/a | HWFW-235, HWFW-236 |
| CHECK-irq-external-conditioned | interrupts.external == true | debounce/sync attribute | present | n/a | HWFW-233, HWFW-234 |
| CHECK-irq-priority-order | interrupts.priority vs channel index | priority non-increasing with channel index from 0 | true | n/a | HWFW-242 |
| CHECK-irq-trailing-layout | interrupts.trailing_of | pos(trailing) - pos(leading) | all == 1 (few) or all == same shift (many; shift = bus_width/2) | n/a | HWFW-258–260 |
| CHECK-irq-optional-fixed | module register offsets per module | offset(Instantiation)=0x00 ... offset(SourceStatus)=0x10 etc. identical across modules | true | n/a | HWFW-253 |
| CHECK-irq-instantiation | Instantiation register fields C,T; actual channel list | packed ? T+1==C : T>=C; C == count(channels) | true | n/a | HWFW-252 |
| CHECK-irq-visible | interrupt registers.paged/indirect | false | true | n/a | HWFW-265 |
| CHECK-irq-per-block | interrupts.module per block | one module per block; chip-level module present; channels/module <= bus width | true | n/a | HWFW-229–231 |
| CHECK-irq-repeat-support | interrupts.repeating == true | buffer or counter or overflow-IRQ present | true | n/a | HWFW-264, HWFW-109 |
| CHECK-irq-doc-complete | interrupts | edge/level, polarity, ack value, deassert method, may-fire-early, repeating, t_min_recur, second-occurrence behaviour | all non-empty | count missing | HWFW-101–109 |
| CHECK-task-handshake | tasks | queue_bit.type == W1S; active_bit RO; done_irq channel exists unless t_done_max <= 2 clk | true | n/a | HWFW-218, HWFW-219, HWFW-262, HWFW-263 |
| CHECK-task-timing-doc | tasks | t_start_{min,typ,max}, t_done_{min,typ,max}, units present | all present | count missing | HWFW-110–114 |
| CHECK-poll-vs-irq | tasks.t_start_max + t_done_max | vs 50–100 clk | > 100 clk => done_irq required and driver uses interrupt; <= 50 => polling acceptable | slack = 100 - (sum) clk | HWFW-221, HWFW-153 |
| CHECK-queue-concurrency | tasks.queue_bit register grouping vs concurrent_with | queue bits in one register | only for mutually concurrent tasks | n/a | HWFW-222 |
| CHECK-abort-complete | tasks.abort available; abort_irq; t_abort_max | every task abortable; abort_irq exists if t_abort_max > 2 clk | true | n/a | HWFW-276, HWFW-279 |
| CHECK-start-reg-last | burst groups (register group + start register) | offset(start) | == max offset in group | n/a | HWFW-181 |
| CHECK-id-version | blocks.id_offset; chip ID/version regs | ID and version registers at fixed offset (e.g. 0x0000/0x0004) in every block; chip ID + version present | true | n/a | HWFW-210, HWFW-211, HWFW-215 |
| CHECK-version-monotonic | blocks.version per silicon revision | strictly increasing when FW-visible change; unchanged across chips/parameterisations | true | n/a | HWFW-133, HWFW-145, HWFW-212 |
| CHECK-instantiation-reg | blocks with parameters | RO instantiation register listing every parameter (buffer size, channels, options) | present | n/a | HWFW-143 |
| CHECK-shared-reg-atomic | registers.owner_drivers | count > 1 and type RW | must have set/clear alias portals | n/a | HWFW-225, HWFW-226, HWFW-250 |
| CHECK-debug-segregated | registers.mode_class == debug | offset > max offset(normal); own range/page; marked unsupported | true | n/a | HWFW-289, HWFW-098–100 |
| CHECK-unused-bits-flagged | fields marked unsupported in supported registers | note "write 0 / ignore on read" present | 100 % | count missing | HWFW-056 |
| CHECK-pin-shared-window | pins.blocks[] with count > 1 | usage_window sets pairwise disjoint AND mux present for outputs and inputs | true | n/a | HWFW-047, HWFW-169, HWFW-170 |
| CHECK-pin-reset | pins.reset_dir, reset_level | GPIO reset_dir == input; actuator control lines reset == off/safe | true | n/a | HWFW-164 |
| CHECK-unused-inputs-tied | block-boundary inputs not connected to pins | tie level defined (high/low) | 100 % | count floating | HWFW-135 |
| CHECK-io-active-doc | per instantiation | list of active I/O signals present | true | n/a | HWFW-136 |
| CHECK-buffer-vs-packet | I/O blocks: buffer bytes, max packet bytes, sync flag | buffer - max_packet (sync); buffer - k*batch (async, k>=2) | >= 0 | slack bytes | HWFW-157, HWFW-048 |
| CHECK-hw-timer | timers.resolution, range; os.tick | resolution <= 1 us; range >= 10 x tick | true | slack: 1 us - res; range - 10*tick | HWFW-151 |
| CHECK-perf-margin | utilisation estimates per bus/block | 1 - utilisation | >= 0.10 (target 0.10–0.20) | margin - 0.10 | HWFW-161 |
| CHECK-error-doc | errors | causes[], stops, block_state, data_state, recovery non-empty for every error code | 100 % | count missing | HWFW-116–121 |
| CHECK-chip-block-table | chip doc table | per block: rev, base, interrupt mask, params, power/reset mapping present | 100 % | count missing | HWFW-053 |
| CHECK-block-doc-sections | block doc | sections present: overview/theory, doc history, block history, chip history, features supported/unsupported, FW assumptions, references, register table (address order), register details, tutorial per task incl. abort, glossary, errata | all | count missing | HWFW-069–082, HWFW-085 |
| CHECK-optional-excluded-behaviour | parameterised registers/bits | excluded => read 0 / write ignored; positions unchanged | true (test) | n/a | HWFW-146–148 |
| CHECK-unused-space-behaviour | unused addresses & bits | read 0 / write ignored; full address decode (no aliasing) | true (test) | n/a | HWFW-182, HWFW-183, HWFW-192, HWFW-193 |
| CHECK-hooks-present | per block: hook inventory | internal-signal register, FSM state register, DMA progress regs, event counters, bypass per sub-block, debug IRQ module, spare GPIO, debug UART | score = present / 8 (advisory; weight higher for new/risky blocks) | count missing | HWFW-292–312 |

## 4. Verification procedures & plots

| property | procedure | axes / sweep | pass criteria | notes | source |
|---|---|---|---|---|---|
| Register reset state | After POR read every register; compare with reset row of map (X bits masked) | table: register x expected/actual | 100 % match | also after FW-invoked sync and async resets | HWFW-094, HWFW-271–274 |
| Unused space & aliasing | Walk the whole block range: read every unused offset; write 0xFFFFFFFF then re-read whole map | x = offset, y = read value; diff map before/after | unused reads 0; no register changed by writes to unused offsets (no aliasing) | catches partial address decode (Table 4.2 / §8.1.7) | HWFW-182, HWFW-183, HWFW-049 |
| Unused bits | Write 1s to unused bit positions of every register; read back; check neighbours | per register bit map | unused bits read 0; defined bits unchanged | enables write-1-read-back version probing | HWFW-192, HWFW-193 |
| Bit-type behaviour | Per field type: RW read-back; RO write ignored; WO reads 0; W1C: write 0 no-op, write 1 clears only that bit; W1S: write 1 sets only that bit, HW clears | per field truth table | matches Table 8.2 | — | HWFW-198, HWFW-239 |
| Sign extension | Load min/max/-1 into signed fields; read as full word | value table | read[W-1:w] == field MSB | — | HWFW-205 |
| Interrupt channel | Per channel: pulse source with enable=0 -> pending=1, line=0; enable=1 -> line=1 immediately; write 1 -> clears; write 0 -> no-op; read twice -> still pending (no read-clear); Post -> pending; hold source high -> no re-trigger until falling then rising | timing diagram per channel | matches Listing 9.6 truth table | also verify Masked == Pending & Enable; Source Status == synced level | HWFW-238–251, HWFW-254 |
| Interrupt synchroniser / debounce | Drive external source with glitches (< 1 clk) and slow edges; count pending events | x = glitch width, y = spurious pendings | 0 spurious; no "pending without CPU interrupt" | §9.1.4 tale | HWFW-233, HWFW-234 |
| Task life-cycle timing | Launch task N times under idle, busy-port, stalled-output; log queue time (1->2) and active time (2->3) from queue/active/interrupt bits with a free-running counter | histogram: x = clk, y = count; one series per condition | min/typ/max within documented bounds; max <= documented max | feeds poll-vs-IRQ decision (50–100 clk) | HWFW-110, HWFW-111, HWFW-218, HWFW-221 |
| Abort behaviour | Abort while idle, at every FSM state (force via poke hook), mid-DMA, with stalled output; record abort-done latency and post-abort register/FSM state | histogram of abort latency; table FSM state -> returned to idle? | abort-done IRQ every time; all FSMs idle; task regs cleared; config/enable regs unchanged; latency <= documented max (e.g. 20,480 clk) | Listing 10.1 poll-then-IRQ | HWFW-279–284, HWFW-097 |
| Halt on error | Inject each error cause; verify block halts with registers intact; read error status (state, signals, counters) | table error -> status snapshot | every documented cause sets its error; snapshot non-zero; recovery per doc works | — | HWFW-166, HWFW-270, HWFW-115–121 |
| Repeating-interrupt overrun | Stream events at t_min_recur while FW delays service | x = service delay, y = lost events / overflow IRQ | overflow IRQ or counter reports loss; no silent loss | Unity 25–30 ms window | HWFW-264, HWFW-108, HWFW-109 |
| OS-tick delay distribution | Request N-tick delays at random phase; measure actual | histogram x = actual delay (ms) | all samples in ((N-1)*tick, N*tick] | justifies +2 tick rule | HWFW-152 |
| HW timer | Program 1 us .. 10 x tick; measure IRQ latency | x = programmed, y = measured | error <= resolution (1 us) over full range | — | HWFW-151 |
| Power-on with partner absent | Power block with collaborating device off / powered later / already on | table of sequences | block reaches documented state, reports condition, comms-reset recovers | §7.3.1 tale | HWFW-162, HWFW-163 |
| GPIO / actuator reset state | Scope every GPIO and control output through POR | x = time, y = level per pin | GPIO high-Z input; actuators off | — | HWFW-164, HWFW-272 |
| Cross-version driver compatibility | Run old driver on new block and new driver on old block (Table 4.1 matrix) | pass/fail matrix | old-driver/new-block works (no new features); new-driver/old-block works | requires offset/bit invariance | HWFW-041, HWFW-042, HWFW-184, HWFW-194 |
| Shadow / coherent reads | Read a wide counter (e.g. 48-bit) across a carry boundary repeatedly | scatter: low word vs high word | never a mixed (pre/post carry) pair | Fig. 8.8 | HWFW-223 |
| Atomic set/clear | Two contexts hammer set-alias and clear-alias of a shared register concurrently | x = iterations, y = lost updates | 0 lost updates | — | HWFW-226 |
| Excluded-option behaviour | For each parameterisation, read/write excluded registers/bits | table | reads 0, writes ignored, remaining bits functional, positions unchanged | — | HWFW-146–148 |
| Event counter sanity | Clear counter, run task expected to produce K events (e.g. 512), read | value vs expected | == K; deviations classified per §11.4.1 table | — | HWFW-302 |
| Performance margin | Bus/memory busy-idle counters over representative workload | x = workload, y = utilisation % | <= 80–90 % (>= 10–20 % headroom) | — | HWFW-161, HWFW-303 |
| Buffer sizing | Drive max packet / burst at max rate; monitor overflow IRQ and interrupt rate | x = buffer size, y = overflow count and IRQ/s | 0 overflow; IRQ rate acceptable | Table 7.1 | HWFW-157 |

## 5. Pitfalls, failure modes, review checklist

- [ ] Address aliasing: a sub-table decoding only low address bits corrupts on writes to higher offsets (4-table example; fix: decode all bits or ignore out-of-range) — §4.5.3 p.68–69, §8.1.7 p.181.
- [ ] R/W bit used as task launch: block missed a set/clear pulse ~1 % of the time; workaround wrote the bit 3x; correct fix is a W1S queue bit cleared by HW — §4.4.1 p.63, BP 8.5.3.
- [ ] No ready indication after reset: busy-loop of 6 iterations tuned on one CPU failed on a faster CPU 3 years later (needed 30) — §7.1.3 tale p.154; BP 7.1.1.
- [ ] Undocumented cross-register dependency: sub-block silently read a register elsewhere in the block that the driver had not written — §5.5.4 tale p.101; BP 5.5.5.
- [ ] Single error bit with 6 root causes and no detail — §5.9.2 tale p.117; BP 5.9.3, 7.4.1.
- [ ] Write-only registers hid a broken block for days — §8.2.6 tale p.193; BP 8.2.11/8.2.12.
- [ ] Mixed R/W + interrupt bits in one register force masking gymnastics (Listing 8.8); leveraged code breaks — BP 8.2.13.
- [ ] Register contents "undefined while active" (third-party block) — BP 8.5.7.
- [ ] Auto-packed IP bits (no holes) make one super-driver impossible — §6.4.4 p.145; BP 6.3.12.
- [ ] Moving the radix point between versions: 0x00C0 read as 12.0 mi by the old driver and 3.0 mi by the new — §8.3.2 p.203; BP 8.3.4.
- [ ] Count-up counter exposed as count-down (two's complement everywhere in FW; differs FPGA vs ASIC) — §7.4.4; BP 7.4.6.
- [ ] Time documented in the wrong unit: 1 M clocks = 10 ms at 100 MHz but 7.5 ms at 133 MHz — Table 5.7; BP 5.8.5.
- [ ] 25 ms minimum delay requested as 3 x 10 ms ticks can yield 20 ms; 1-tick delay has a 10 % chance of < 1 ms — Fig. 7.1, §7.1.2 tale.
- [ ] W0C ack: inversion forgotten at one of several ack sites (Listing 9.2 line 18 bug); one ASIC mixed 1-ack and 0-ack bits — BP 9.2.3.
- [ ] Read-to-clear pending register loses interrupts to loggers/debuggers/multiple reads — BP 9.2.4.
- [ ] Unsynchronised, undebounced external interrupt: pending set but CPU never interrupted — §9.1.4 tale p.231; BP 9.1.7/9.1.8.
- [ ] Missing chip-level enable: an interrupt with no enable wiring had to be serviced always; pass-through I2C interrupt held the ISR ~400 us — §9.3 tale p.240; BP 9.3.1.
- [ ] Both edges on one channel: second edge lost if first not serviced; driver had to read source status every interrupt — §9.6.1 tale p.254; BP 9.5.1.
- [ ] Trailing edges not wired on 4 of 5 signals blocked a late workaround — §9.6.1 tale p.255; BP 9.5.2.
- [ ] Ack-before-enable on one chip, enable-before-ack on another introduced a defect — §9.8 tale p.261.
- [ ] Abort bit ignored in idle state: stale abort killed the next job — §10.4.3 tale p.273; BP 10.3.6.
- [ ] Bus had no way to abort a stalled transaction; added late, it shipped with a defect — §10.4.1 tale p.269; BP 10.3.1/§10.4.3 priority.
- [ ] FIFOs not emptied by abort; saved by a mid-pipeline test read port — §11.3.1 tale p.287; BP 11.3.1.
- [ ] FSM stuck waiting for an external sync pulse; artificial pulse generator (test hook) used in production workaround — §11.3.2 tale p.288; BP 11.3.2.
- [ ] FSM state register revealed a missing in-line resistor on the board (~3 days saved) — §11.2.4 tale p.286; BP 11.2.7.
- [ ] DMA wired with wrong byte order; byte-swap feature averted a respin; bypass path pinpointed it — §7.4.2 tale p.165, §11.5.1 tale p.294.
- [ ] Sub-block interfering with another; continuous bypass toggling as workaround — §11.5.1 tale p.294.
- [ ] Interrupt validity signal exposed to FW let it reject extraneous interrupts from a signal-integrity defect — §11.2.2 tale p.282.
- [ ] Sync-pulse cessation detection absent from one video block (not a superblock): 5 weeks + warranty cost vs 1 hour — §6.1.2 tale p.129.
- [ ] Raster buffers not downsized on a "portrait-only" SoC later enabled landscape reuse — §6.2.3 tale p.134; BP 6.1.6.
- [ ] I2C block implemented byte-mode only; JPEG decoder mis-handled a marker; config register hard-coded to one IRQ — §4.1.2 tales p.55; BP 4.1.3/4.1.4.
- [ ] Simulation tested one chunk, not chaining; test wrote registers in a different order than the driver — §4.4.3 tales p.65; BP 4.4.4.
- [ ] IP vendor knew a defect for months and did not tell (2 engineer-months lost) — §3.2.5 tale p.43; BP 3.2.10.
- [ ] CAN packet race: HW fix would have needed a die-crossing signal; robust FW workaround kept instead — §3.3.2 tale p.46 (weigh risk both ways, BP 4.4.3).
- [ ] Documentation errors to grep for: wrong address, wrong bit position, wrong bit sense, stale functions, missing new functions, missing info — BP 5.2.6.
- [ ] Term ambiguity: define cold/warm, soft/hard, sync/async reset; "Mask" polarity — BP 5.2.7, 5.7.4.
- [ ] Done interrupt before data lands in memory (bus/memory-controller latency) — BP 5.7.6.
- [ ] Shared pins needed simultaneously by two blocks in a future product set — BP 4.5.1.
- [ ] Leaving test hooks out of the next version: 4 hooks used 6 ways were needed to ship Unity; hooks retained and reused for new defects — §11.6 tale p.298.

## 6. Standards referenced

| standard / document | edition-year | clause | governs | page |
|---|---|---|---|---|
| ANSI C | — | — | firmware language standard example | §2.1.2 p.22 |
| POSIX | — | — | OS interface standard example | §2.1.2 p.22 |
| PCI Express | — | — | bus standard; bursting; MSI interrupts | §2.1.2 p.22; §8.1.6 p.179; §9.1.5 p.232 |
| JTAG | — | — | debug/test access | §2.1.2 p.22; §2.1.6 p.29 |
| USB 1.1 / 2.0 / 3.0; EHCI | — | — | interface standard; EHCI-compliant host controllers share a standard register interface | §2.1.2 p.22; §1.1.1 p.4; §4.1.1 p.53 |
| RS-232 | — | — | UART example: full standard incl. HW handshaking vs standard subset; derivation example (10-bit words) | §4.1.2 p.53; Table 6.1 p.124 |
| 16550 UART | — | — | de facto compatible register/bit layout | §1.1.1 p.4 |
| Hayes "AT" command syntax | — | — | de facto standard example | §4.1.1 p.52 |
| I2C | — | — | bus example (byte vs block transfer modes; bus switch monitor) | §4.1 p.51; §4.1.2 p.55; §8.5.1 p.211 |
| PCI, TCP/IP, JPEG, MP3 | — | — | examples of standards with supporting blocks | §4.1 p.51 |
| CAN | — | — | automotive/embedded network; race-condition tale | §3.3.2 p.46; Glossary |
| CMMI (sei.cmu.edu/cmmi), ISO (iso.org), Agile (agilealliance.org) | — | — | process-improvement frameworks for internal standards | §2.1.2 p.22 |
| Silicon Image SiI3531A Data Sheet, Doc # SiI-DS-0208-C rev C, 02/02/07 | 2007 | Port Interrupt Enable Set/Clear register | precedent for atomic set/clear register pair | §8.5.4 p.221 |
| x86 Programmable Interrupt Controller (PIC) / Southbridge | — | — | system-level interrupt module precedent | §9.1.3 p.229 |
| Verilog, VHDL, SystemC, SystemVerilog | — | — | HDL examples (book is HDL-agnostic) | §1.4.1 p.13 |
| Register design tools: Atrenta 1Team-Genesis Registers, Duolog Bitwise, Denali Blueprint, Semifore csrCompiler, Agnisys IDesignSpec, PDTi SpectaReg | 2009 | — | single-source register/bit generation (HW, FW, docs) | §5.5.2 pp.99–100 |

## 7. Process / lifecycle guidance

Life-cycle phases (Fig. 1.3, p.14): HW: Spec -> Design -> Verification -> Fab -> Test -> Firmware support. FW: Hardware support -> Spec -> Coding -> Integration -> System test. Product release follows system test. FW involvement is heaviest late; HW involvement heaviest early; each team supports the other in its off-peak.

| stage | activity | deliverable | exit criterion | source |
|---|---|---|---|---|
| Project start | Assign roles: BP champion (HW), HW ambassador, FW ambassador; kick-off meeting; contact/responsibility list; tools, email groups, wikis, meeting schedule | role assignments; contact list; meeting calendar | all roles named; list distributed to both teams | BP 3.1.1–3.1.5 (HWFW-010–014) |
| High-level HW spec | Review marketing features; decide HW/FW split (Balance the Load); block selection incl. latest common versions; postmortem notes of prior chip applied; standards chosen (full or standard subset); third-party IP evaluated; shared-pin analysis; buffer analysis | chip high-level specification (short) given to FW for review | FW architects reviewed and signed off; deviations from standards documented with risk | BP 3.2.3, 4.1.x, 4.2.x, 4.5.x, 4.6.1 (HWFW-017, 031–040, 047–051) |
| Block design start | Write block documentation BEFORE RTL (template App. B: overview, histories, features/assumptions, references, register reference, tutorial, glossary, errata); distribute for initial FW review; FW requests hooks | block-level documentation v1; hook request list | FW review returned within ~1 week; comments incorporated; redistributed | BP 5.2.2, 5.3.1, 5.3.4, 5.3.5, 3.3.4 (HWFW-058, 064, 067, 068, 028) |
| Detailed block design | Apply register/interrupt/abort/hook rules (Ch. 7–11); use register design tool as single source for .vh/.h/.rtf; weekly HW/FW meetings on use cases incl. error handling and inter-block interactions; consult FW before any interface change | RTL + generated headers + regenerated doc; change-tracked doc revisions | every doc change marked and re-reviewed; FW sign-off at checkpoint | BP 3.2.1, 3.3.2, 5.2.3, 5.3.2, 5.3.3, 5.5.2 (HWFW-015, 026, 059, 065, 066, 084) |
| Block verification / test plan | Test plan reviewed with FW so tests use FW's register values, order and flow (incl. chaining, abort at every state, error injection) | block test plan; co-development platform (FPGA/co-sim/virtual prototype/legacy HW) with driver running | FW reviewed test plan; driver runs on prototype platform | BP 4.4.4, 3.2.6 (HWFW-046, 020) |
| Design freeze | Final doc pass for accuracy/completeness; version registers set (chip, block); errata section opened | frozen block doc; chip-level block table (rev, base, IRQ mask, params) | doc matches RTL (no address/bit/sense/stale/missing errors) | BP 5.2.4, 5.2.6, 5.1.1, 8.4.x (HWFW-060, 062, 053, 210–216) |
| Fab / bring-up | HW brings up boards, basic tests; defects logged in searchable repository and pushed to FW; HW support continues to end of FW development | defect repository entries (behaviour, conditions, impact, likelihood, workaround, versions); errata updates | every known defect documented incl. rare ones; FW notified | BP 3.2.7–3.2.10, 4.4.1, 4.4.2, 5.4.14 (HWFW-021–024, 043, 044, 082) |
| Integration / system test | Joint root-causing (4 problem classes); FW workarounds designed jointly using hooks; performance tuning via tunable registers | workaround list tied to hooks/defects | product shippable; workaround list feeds next chip | BP 3.3.6, 7.2.4, 11.1.6 (HWFW-030, 160, 291) |
| Post-release | Joint postmortem (what went well, defects to fix, docs, process, meetings, comms, test holes); notes distributed; fix list for next version (remove hook-based workarounds, promote architectural hooks to features); BP list revised by champion | postmortem notes; next-chip fix list; updated BP database | notes distributed to all; defects selected for fix with FW agreement | BP 4.6.2, 4.4.3, 11.1.6 (HWFW-052, 045, 291) |
| Every new chip revision / FPGA load | Increment chip version; block versions only for changed blocks; keep register offsets and bit positions; new bits to the left; never reuse deleted addresses/bits | updated version registers; register-map diff | CHECK-reg-offset-invariant, CHECK-bit-pos-invariant, CHECK-version-monotonic all pass | BP 8.1.13, 8.1.14, 8.2.9, 8.2.10, 8.4.3, 8.4.7 |

Documentation deliverable set (§5.1.1, p.74): chip high-level specification; chip-level documentation (global interrupt/power/reset/GPIO registers, block table); block-level documentation (the "external reference specification" / programmer's guide — distributed to all FW teams incl. third parties); block unsupported specification (test/debug registers, state diagrams — in-house only); block test plan; block design specification (HW internal).

Block documentation template sections (App. B): B.1 Introduction (B.1.1 overview: system + block; B.1.2 history: document, block, chip-specific; B.1.3 features supported / not supported / firmware assumptions; B.1.4 references); B.2 Register reference (B.2.1 register tables address-order + alphabetical; B.2.2 per-register maps: horizontal, LSB right, bit 0 = LSB, type row, reset row, bit descriptions LSB-up, abort impact, units/min/max/illegal); B.3 Tutorial (per task incl. abort; real-number handling); B.4 Glossary; B.5 Defects/errata per chip.

## 8. Coverage log

- Source file: 7245 lines, 755 KB, long single-line paragraphs (746 lines > 300 chars, max 2817). Read in order: lines 1–350 via Bash (persisted output re-read in full), then Read tool in 400-line chunks 351–7245 (final chunk 7151–7245). No chunk was truncated.
- Read fully: Preface, Ch. 1–12, Appendix A (used to cross-check the BP list: 7 principles + 294 best practices = 301 items; every one is represented by a row in §1), Appendix B (bicycle-controller template, mined for exemplar values), Appendix D glossary (definitions of abort/halt/reset/W1C/W1S used in §2.4).
- Skipped: Index (lines 6842–7245, index pages — no rules). Chapter references lists were read but only the Silicon Image datasheet and named tools are engineering-relevant (§6).
- Not present in the file: Appendix C "Using This Book in a University" (announced in the preface, p.xii) — the text jumps from Appendix B (p.343) to Appendix D (p.345); nothing to extract.
- Extraction limitations: figures absent (register maps were reconstructed from the bit-letter rows and descriptions; Fig. 8.5–8.8, 9.1–9.9, 10.2, 11.1–11.2 described from captions/prose); Table 1.1 (chip-type comparison) is scrambled in the text and was not reproduced; Table 8.2 checkmarks are scrambled — §2.3 was rebuilt from the surrounding prose definitions; Listing 9.2 two-column layout is interleaved but its point (W0C inversion bug on line 18) is stated in prose; form-feed page markers are not visible, so citations use the printed page numbers that appear as stray lines ("Registers 181" etc.) and section numbers.
- Rule count: HWFW-001 … HWFW-321 (321 rows), of which 301 map 1:1 to the book's numbered principles/best practices and 20 are additional derived/numeric rules (marked by § citations). Confidence: all rows `high` except HWFW-152 (`medium`, derived tick formula). No numbers were invented; every value is traceable to the cited page.
- Copyright handling: best-practice statements are paraphrased into checkable rule form with the book's ID retained for lookup; the book's own wording is not reproduced wholesale (the BP database carries a separate copyright notice restricting redistribution).
