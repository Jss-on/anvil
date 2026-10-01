# Making Embedded Systems: Design Patterns for Great Software (2nd ed.) — Anvil rulebook

## 0. Citation

[1] E. White, *Making Embedded Systems: Design Patterns for Great Software*, 2nd ed. Sebastopol, CA, USA: O'Reilly Media, Mar. 2024 (first release 2024-03-01). ISBN 978-1-098-15154-6.

BOOKTAG: WHITE. Source text: `refs-text/Elecia_White_Making_Embedded_Systems_Design_Patterns_for_Gre.txt` (6056 lines, 864 KB).

Chapters covered by THIS extraction: Preface; Ch.1 Introduction; Ch.2 Creating a System Architecture; Ch.3 Getting Your Hands on the Hardware; Ch.4 Inputs, Outputs, and Timers; Ch.5 Interrupts; Ch.6 Managing the Flow of Activity; Ch.7 Communicating with Peripherals; Ch.8 Putting Together a System; Ch.9 Getting into Trouble; Ch.10 Building Connected Devices; Ch.11 Doing More with Less; Ch.12 Math; Ch.13 Reducing Power Consumption; Ch.14 Motors and Movement. (See §8 Coverage log for exact line ranges and anything skipped.)

Chapters NOT read: none (index pages and end-of-chapter interview questions skipped — non-technical).

Confidence tag usage in this file: `high` = explicitly stated in the text (numeric/formula, or a checkable qualitative rule stated verbatim); `medium` = derived from a stated relation/example; `low` = qualitative guidance quantified by the extractor (marked).

Page citations `p.NN` are the printed page numbers that appear as stray lines in the text; `§` cites a section title when no page is visible.

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| WHITE-001 | test | Code executing from flash/ROM needs hardware breakpoints, which are scarce (frequently only two); compiled-in breakpoint instructions (`BKPT`, `bkpt #0`, `break`) do not consume the hardware-breakpoint budget | HW breakpoints available: frequently 2 | processor debug spec | XIP from flash | review | p.4, p.82 | high |
| WHITE-002 | bringup | Firmware cannot run immediately at power-on: the design/bring-up plan must account for power sequencing, power ramp-up time, clock stabilization time, and processor reset/initialization delay | t_boot = t_seq + t_ramp + t_clk_stab + t_reset (each from datasheets) | rail ramp specs, oscillator start-up, reset supervisor delay | all boards | review | p.10 | high |
| WHITE-003 | process | Prototype-to-product gate list: firmware update path, sleep/low-power mode, watchdog for catastrophic errors, reserved code space and CPU cycles for future fixes, manufacturing method for volume, tests for safety / bad user commands / corner cases / broken hardware | each item present = pass | product plan | dev-board prototypes → product | review | p.8 | high |
| WHITE-004 | hw-fw | A custom board loses the dev board's built-in programmer/debugger: the custom PCB must carry an external programmer/debugger interface | debug/program connector count ≥ 1 | netlist | custom PCB | inspect | p.8 | high |
| WHITE-005 | hw-fw | Any bus/driver/peripheral shared by ≥ 2 software users (e.g., SPI flash serving display assets AND serial-number read; two subsystems on one SPI) is a design red flag requiring an explicit ownership mechanism (flag/semaphore) and contention analysis | shared users ≥ 2 → arbitration required | block diagram / organigram | all | review | p.15, p.18–19 | high |
| WHITE-006 | firmware | Model each driver on the POSIX interface (open, close, read, write, ioctl; optionally select/poll, mmap) and give every driver/module a `test` entry point | — | — | drivers | review | p.24–26 | high |
| WHITE-007 | firmware | Every module init must be safe to call multiple times; a very good init resets the subsystem/hardware to a known-good state after partial failure; high-level modules initialize what they depend on | — | — | all modules | review | p.27 | high |
| WHITE-008 | firmware | Logging interface = `Log(subsystem, level, msg)` + `LogWithNum`; levels {none, info, debug, warning, error, critical}; per-subsystem level; global on/off switch because logging changes timing | — | — | all | review | p.28–29 | high |
| WHITE-009 | firmware | Firmware version must be retrievable: printed automatically on boot over the primary comms path (USB/WiFi/UART/bus); else via query; else compiled into its own object file at a fixed address for inspection | — | — | all | inspect | p.29 | high |
| WHITE-010 | firmware | Semantic version A.B.C packed as major = 1 byte, minor = 1 byte, build = 2 bytes; build indicator increments automatically or often | version = 4 bytes | — | all | inspect | p.30 | high |
| WHITE-011 | hw-fw | Every separately built or separately programmed artifact (e.g., EEPROM programmed in manufacturing) carries its own version, and code checks it before use; all moving pieces must be verified mutually compatible | — | — | multi-image systems | inspect | p.30 | high |
| WHITE-012 | firmware | Back-door accessors to module-private state (for RAM reuse or external test) must be compiled out in production (`#if PRODUCTION` → `#error`) | — | — | — | inspect | p.33 | high |
| WHITE-013 | test | Algorithms are developed in a sandbox (MVC): inputs replayed from a timestamped script file (`time, action, args`), outputs to log files; enables PC debugging and regression tests | — | — | complex algorithms | review | p.35–37 | high |
| WHITE-014 | process | Schedule dependencies: schematic review precedes board build; boards precede FW alpha; HW + FW durations do not add serially (12 wk boards + 14 wk FW ≠ 26 wk) — enumerate which FW tasks run in parallel vs. after hardware | — | — | — | review | p.42 | high |
| WHITE-015 | process | Buy development kits for the riskiest parts (processor and least-understood peripherals) before custom hardware; FW meanwhile builds toolchain, debugger, debug subsystem, tries peripherals, builds sandbox | — | — | — | review | p.43 | high |
| WHITE-016 | hw-fw | The hardware engineer delivers an I/O map (what is attached to every processor pin) with the schematic; FW generates a header from it; master copy kept in CSV/Excel and script-generated per board version so identifiers match schematic net names | — | pin map | all | inspect | p.44, p.98 | high |
| WHITE-017 | dfm | BOM is started during schematic capture; every line needs the exact orderable part (e.g., which 10-pin header) with a datasheet link; long-lead parts block kitting/assembly | — | BOM | all | inspect | p.44 | high |
| WHITE-018 | process | Hardware tests are defined and written while layout/fab is running; ask the EE which subsystems are riskiest and prioritize those tests (and try them on a dev kit) | — | — | — | review | p.44 | high |
| WHITE-019 | bringup | First power-on of a new PCBA is done by the hardware engineer to verify no power issues (and other purely hardware subsystems) before firmware gets a board | — | — | — | inspect | p.44 | high |
| WHITE-020 | bringup | Bring-up method: make every component individually testable (separate HW-test firmware project if code space is short, sharing modules); start at the lowest level in the smallest steps (set an I/O for a short time with an LED → then minimum motor twitch → then full controller); tools runnable without the author present so issues are reproducible | — | — | — | review | p.45 | high |
| WHITE-021 | test | Hardware verification code is kept under version control and expected to be reused on the next board revision and to evolve into manufacturing tests | — | — | — | review | p.46 | high |
| WHITE-022 | components | Use the latest datasheet revision for the component revision actually used; check the vendor site for errata (both datasheet errors and part errors) — search "<part number> errata"; most parts have errata | — | — | all parts | inspect | p.50 | high |
| WHITE-023 | components | Component evaluation order: (1) absolute maximum ratings + electrical characteristics vs. must-have list → reject non-fits and note why; (2) typical/performance characteristics (speed, output, sensor noise); (3) application-section similarity; (4) mental/real prototype of the driver; keep 2–4 candidate datasheets per part; check the family for a pin-for-pin compatible larger part (headroom) | 2 ≤ candidates ≤ 4 | datasheets, requirement list | part selection | review | p.53–55 | high |
| WHITE-024 | components | Datasheets lack price and lead time; verify both with vendor/distributor (DigiKey for estimates); the perfect part may have a six-month lead time | lead time ≤ project need | — | part selection | review | p.53 | high |
| WHITE-025 | components | Check performance-characteristic conditions against placement/environment: e.g., a part rated 0 °C–70 °C placed next to a very warm processor; accuracy falls off outside the specified input range | T_ambient_local within rated range | thermal layout | all | review | p.49 | high |
| WHITE-026 | hw-fw | Skim the processor errata for every peripheral used (e.g., seven I2C bugs listed → investigate before using I2C) | — | errata list, peripheral usage | all MCUs | review | p.58 | high |
| WHITE-027 | hw-fw | Read the vendor user/reference manual, not the core (Arm) manual: for STM32F103, ~88 % of the Arm manual is extraneous and ~10 % is duplicated in the STM32F10x manual | — | — | — | review | p.56 | high |
| WHITE-028 | hw-fw | Schematic reading conventions: ICs are U-designators, connectors are J-designators; active-low signals shown with an overbar or /NAME, nNAME, #NAME, _NAME, NAME*, NAME_N; a junction dot marks connected crossings (no dotted four-way crosses); part numbers on the schematic carry package/temperature suffixes (AT91R40008-66AI) | — | — | — | inspect | p.48–49, p.60–61 | high |
| WHITE-029 | connectors | A board schematic must contain a power connector (≥ 2 pins: power and ground) and a processor debug connector (e.g., J1) | count(power conn) ≥ 1; count(debug conn) ≥ 1 | netlist | all | inspect | p.60 | high |
| WHITE-030 | hw-fw | Pull-ups are weak (high resistance) so the processor can drive the line low; an input with neither pull-up nor pull-down is floating (hi-Z/tri-state) → every processor input must have a defined default level (external resistor or enabled internal pull) | for each input: pull ∈ {external, internal} | pin map, netlist | all inputs | inspect | p.61–62 | high |
| WHITE-031 | dfm | Provide dedicated programming connector(s) used to program boards in manufacturing (Arduino UNO: ICSP and ICSP1), distinct from general I/O headers | programming header ≥ 1 | netlist | production | inspect | p.64 | high |
| WHITE-032 | bringup | Board-handling rules: ESD protection (antistatic bag/mat/wrist band), standoffs, rework wires glued as well as soldered, photograph/note orientation of non-keyed connectors, hardware on a switchable power strip separate from the PC, know where the fire extinguisher is | — | — | lab | inspect | p.64 | high |
| WHITE-033 | bringup | Request spare boards: verify HW tests on more than one board, keep a third as tie-breaker when two disagree; early dense-board builds commonly have solder opens/shorts that bare-board continuity test cannot catch | boards for FW ≥ 3 | — | first article | review | p.65 | high |
| WHITE-034 | test | Minimum DMM for bring-up: voltage 0–20 V at 0.1 V resolution and 0–2 V at 0.01 V resolution; resistance/continuity only on an unpowered board touching exactly two points; current mode in mA (nA-class not required) | V: 0–20 V/0.1 V; 0–2 V/0.01 V; I: mA | — | lab | measure | p.66–67 | high |
| WHITE-035 | test | Scope setup: ground clip to the correct ground (ask EE when AC/DC/analog grounds exist — wrong choice can damage the scope); start ≈ 100 ms/div and ≈ 2 V/div, zoom from there; check 10x probe attenuation; DC coupling unless known otherwise; "Auto" may be autoset (avoid) | 100 ms/div, 2 V/div start | — | lab | measure | p.68–70 | high |
| WHITE-036 | test | Three test classes: POST — every boot, must not modify flash, boot-time cost accepted, POST output retrievable later without power-cycle; unit tests — before every release, left in production code, field-accessible via a special criterion (e.g., two buttons held at boot); bring-up tests — throwaway OK but checked into VCS | — | — | all | review | p.70–71 | high |
| WHITE-037 | test | SPI-flash bring-up test ladder: (1) I/O lines under software control (verify with DMM), (2) SPI sends/receives bytes (verify with logic analyzer), (3) flash reads/writes (verify via debug output); run the umbrella test first and drop to lower tests on failure | — | — | SPI flash | measure | p.72 | high |
| WHITE-038 | components | Flash geometry example (Macronix MX25V8035): sector = 4 KB (4,096 B); device = 8 Mb = 1 MB = 256 sectors; byte-writable but sector-erase only; endurance often 100,000 erase/write cycles (from datasheet) | sector 4096 B; endurance ≈ 1e5 cycles | flash datasheet | NOR flash | calc | p.73 | high |
| WHITE-039 | test | Memory test pattern: (1) read original block; (2) erase, write formulaic changing data byte-wise (value = index + 0x55, never the address itself); (3) verify byte-wise; (4) erase, rewrite original as a block; (5) verify. Test signature `(address, buffer*, length)`; length = sector size ⇒ no data loss. Excluded from POST (wear + destructive) | — | — | flash/EEPROM | measure | p.73–75 | high |
| WHITE-040 | test | POST check for flash = read a header containing a known key, a version and/or a checksum (proves communication) — never a write test | — | — | all NVM | inspect | p.73 | high |
| WHITE-041 | test | Driver-level flash tests do not detect sticky bits; only a manufacturing (or vendor) test that confirms every bit changes does | — | — | production test | measure | p.75 | high |
| WHITE-042 | test | Command-line test handler: table of {name, function pointer, help string} terminated by `{"",0,""}`; minimum command set: version, flash test (prints error count), blink LED (frequency parameter), help | — | — | all | inspect | p.76–77 | high |
| WHITE-043 | firmware | One codebase-wide error-code header: 0 = no error (always), unknown error, bad parameter, bad index/null, uninitialized, catastrophic (→ processor reset in production, breakpoint/spin loop in development); keep the set small and generic | NO_ERROR == 0 | — | all | inspect | p.82 | high |
| WHITE-044 | firmware | Implement `assert()` per system (debugger console message, log, BKPT instruction, or I/O line/LED toggle); keep error output separate from printf so error signalling does not change timing | — | — | all | inspect | p.81 | high |
| WHITE-045 | firmware | Error library with ErrorSet/ErrorGet/ErrorPrint/ErrorClear; ErrorSet never overwrites a prior error; mechanism remains in production (ErrorPrint may become an I/O toggle) | — | — | all | inspect | p.83 | high |
| WHITE-046 | test | Timing-sensitive debugging: record 1–2-byte event signatures into a 4–16-byte RAM buffer (circular for last-N) at trigger points (ASSERT/ErrorSet); dump after leaving the time-critical region instead of printing inside it | buffer 4–16 B; event 1–2 B | RAM availability | timing bugs | inspect | p.84 | high |
| WHITE-047 | hw-fw | Board exposes spare processor I/Os on an easily accessible header as test points (timing debug, status, profiling); the EE asks FW how many during schematic capture | test points ≥ N agreed (≥ 1) | pin map | all | inspect | p.84 | high |
| WHITE-048 | firmware | Use recognizable sentinels: 0xDEADBEEF / 0xDEADC0DE for memory anomaly markers; 0xAA / 0x55 as test patterns (alternating bits, easy to see on a scope) | — | — | — | inspect | p.89 | high |
| WHITE-049 | hw-fw | Pin map records both the pin *name* (port/pin, e.g., IO1_2, inside the symbol) and the package pin *number* (e.g., 10, outside the symbol); for shared pins (e.g., SCLK/IO1_2) state the default function and how to switch | — | schematic | all | inspect | p.92–93 | high |
| WHITE-050 | firmware | Never hardcode register addresses; use the vendor HAL/header (or make one); register read-modify-write sequences must be atomic (no interruption between read and write) | — | — | all | review | p.93–94 | high |
| WHITE-051 | bringup | GPIO/LED troubleshooting order: math/typos → correct pin per schematic → board powered → alternate function on shared pin → pin config (power control, accidental interrupt) → I/O subsystem clock enabled → verify the loaded code is the compiled code (bump revision) → correct target in build → strip non-critical init (waiting on absent devices) → interrupts/asserts off → watchdog off → inverted logic (MCU pins sink more than they source, so LED cathode on pin ⇒ write 0 = on) → pin drive current vs LED → try other boards → LED backwards / shorted high-density pins | — | — | bring-up | measure | p.95–96 | high |
| WHITE-052 | hw-fw | Board-specific header `ioMapping_vN.h` selected by `COMPILING_FOR_Vn`; `#error` if no map selected; retain old-board maps (cost is only a file) | — | — | multi-rev boards | inspect | p.97, p.123 | high |
| WHITE-053 | firmware | Each subsystem initializes the I/Os it needs (not one global init); the only centralized artifact is the I/O map header | — | — | all | review | p.98 | high |
| WHITE-054 | power | Enabled internal pull-ups/pull-downs on inputs draw current (order of µA each); in low-power designs disable unneeded ones | I_pull ≈ µA per input | pin config | low power | calc | p.101 | high |
| WHITE-055 | hw-fw | Input pin setup checklist: (1) add to I/O map header; (2) configure as input and verify no other peripheral claims it; (3) configure pull-up/down explicitly; a switch to ground with pull-up is active-low | — | — | all inputs | inspect | p.101 | high |
| WHITE-056 | requirements | Human input response-time thresholds: > 250 ms sluggish; 100 ms noticeable to impatient users; < 50 ms feels snappy | t_response: target < 50 ms; acceptable ≤ 100 ms; limit 250 ms | — | buttons/UI | measure | p.102 | high |
| WHITE-057 | firmware | Button interrupts trigger on the rising edge (release), not on level, to avoid repeated activations while held | — | — | buttons | review | p.104 | high |
| WHITE-058 | firmware | All memory-mapped registers and all globals shared between ISR and main code are declared `volatile`; symptom of omission: works unoptimized, fails with optimization on | — | — | all | inspect | p.104, p.124 | high |
| WHITE-059 | firmware | Never interrupt directly on a bouncy switch signal (glitch edges waste cycles and can destabilize the processor); poll and debounce | — | — | mechanical switches | review | p.105 | high |
| WHITE-060 | components | Switch datasheet specifies the bounce/uncertainty period; do not rely solely on empirical testing (batches differ) | t_bounce from datasheet | switch datasheet | switches | inspect | p.106 | high |
| WHITE-061 | firmware | Debounce algorithm: sample at a period several times faster than the desired response; declare a change after N consecutive consistent samples; variables = raw reading, counter, debounced value, changed flag; counter may be asymmetric (fast press, slow release) | t_response ≈ N × T_sample; T_sample ≪ t_response | t_bounce, t_response | switches | calc | p.106–107 | high |
| WHITE-062 | firmware | Debounce numbers: 120 wpm × 5 chars/word = 10 keys/s ⇒ key held ≈ 50 ms; example switch rings ≤ 12.5 ms; to accept a ≥ 50 ms hold, sample every 10 ms (100 Hz) and require 5 consecutive samples (conservative; 3 acceptable with a slower poll) | N = 5 @ 10 ms (or 3 with longer T_sample); N × T_sample ≥ t_bounce | — | switches | calc | p.107 | high |
| WHITE-063 | timing | Internal RC oscillators are inaccurate and accumulate considerable drift → communication errors and real-time errors; use a crystal/external oscillator when timing precision matters; PLL multiplies a slow, cheap, low-power oscillator to the processor clock | — | clock source | timing-critical / comms | review | p.112 | high |
| WHITE-064 | timing | Timer relation: interruptFrequency = clockIn / (prescaler × compare); prescaler and compare are integers bounded by register width (compare ≤ 2^bits − 1: 8-bit → 255, 16-bit → 65,535; ATtiny45 prescaler 10-bit → 1,023); some registers are zero-based (divide-by-2 ⇒ write 1) | f_int = f_clk / (P × C) | f_clk, P, C, register widths | all timers | calc | p.112–115 | high |
| WHITE-065 | timing | Timer frequency error = 100 × |f_goal − f_actual| / f_goal (%); accept registers once error ≤ tolerance (book examples 0.1 %, 0.04 %, 0.03 %, 0.02 %, 0.08 %, 0.0009 %) | error% = 100·|f_goal − f_act|/f_goal | — | all timers | calc | p.117–118 | high |
| WHITE-066 | timing | Register-selection heuristic: (1) if f_clk/f_goal is an integer, factor it into P × C (4 MHz/20 Hz = 200,000 = 1,000 × 200); (2) else minP = f_clk/(f_goal × C_max) rounded up (4 MHz/(255×20 Hz) = 784.31 → 785 → 19.98 Hz, < 0.1 % error; 784/255 → 0.04 %); (3) try P_max (17 Hz: 1,023/230 → < 0.02 %); (4) brute force P from minP..P_max with C = round(f_clk/(f_goal × P)), pick min error (17 Hz: 997/236 → 0.0009 %) | see formulas | f_clk, f_goal, widths | all timers | calc | p.116–118 | high |
| WHITE-067 | timing | When the needed division exceeds timer × prescaler range (e.g., 13 Hz on an 8-bit timer with 10-bit prescaler at 4 MHz), use a wider timer (16-bit, C_max 65,535) or software-divide a faster interrupt (26 Hz ISR toggling every other call) — the latter is less precise due to interrupt jitter | P_min = f_clk/(f_goal × C_max) ≤ P_max else escalate | — | all timers | calc | p.119 | high |
| WHITE-068 | timing | Overflow-only timers have an implicit match value of 2^bits − 1 (8-bit: 255); tune via prescaler | C_implicit = 2^bits − 1 | — | timers without compare | calc | p.114 | high |
| WHITE-069 | hw-fw | Pin map must record timer-output and PWM-capable pins (PWM pins are usually a subset of timer-output pins; some processors need special settings or cannot route a timer to a given pin) | — | user manual pin tables | timer/PWM outputs | inspect | p.119, p.121 | high |
| WHITE-070 | timing | LED-dimming PWM must run at hundreds of Hz (period ≈ ms); 20 Hz produces visible flashes; implement with two compare registers (A = period/reset, B = duty) rather than interrupts; 100 % duty = always on, 0 % = driven low | f_PWM ≥ ~100s Hz for LEDs | — | LEDs | review | p.120–121 | high |
| WHITE-071 | firmware | Before ship: delete unneeded prototype code (no commented-out code); tag/branch the development version in VCS; keep the I/O map for old boards | — | — | release | review | p.122–123 | high |
| WHITE-072 | firmware | Fault-class interrupts (memory error, divide-by-zero, invalid instruction, brownout) do not return; handlers must go to a defined end state: infinite loop (development) or processor reset (production) | — | — | all | review | p.127 | high |
| WHITE-073 | hw-fw | NMI cannot be masked; typically one I/O pin can route to NMI (commonly the "on" button) — record it in the pin map; NMI handler must be valid even inside critical sections | — | pin map | all | inspect | p.128 | high |
| WHITE-074 | firmware | Disable nested interrupts unless they solve a specific system problem; customary to disable other interrupts while in an ISR (configure at system init) | — | — | all | review | p.128 | high |
| WHITE-075 | firmware | System latency = processor interrupt latency (cycles, from user manual) + longest interval with interrupts disabled (≈ longest ISR when nesting is disabled); keep ISRs short, avoid function calls, never call nonreentrant functions (printf, malloc/new, any I/O or file function) | t_sys_latency = t_proc_latency + max(t_int_disabled) | ISR durations | all | calc | p.130–131, p.135 | high |
| WHITE-076 | timing | Interrupt entry overhead fraction = f_int × latency_cycles / f_cpu: 100 Hz × 10 cycles / 100 Hz = 10 %; 44,100 Hz × 10 cycles / 30 MHz = 1.47 % (excludes ISR body and return) | overhead = f_int·N_lat/f_cpu | f_int, N_lat, f_cpu | all | calc | p.131 | high |
| WHITE-077 | timing | ISR CPU budget: total cycles = entry + calls + work (example 10 + 5 × 10 + 275 = 335 cycles = 11 µs @ 30 MHz); at 44,100 Hz → 0.492 s per s ≈ 49 % CPU inside the ISR and no other interrupt serviced for 335 cycles | CPU_frac = f_int × N_isr / f_cpu | f_int, N_isr, f_cpu | audio/high-rate ISRs | calc | p.131 | high |
| WHITE-078 | firmware | Default (unhandled) interrupt handler: infinite loop during development (to expose it); return-to-normal in production (slowdown instead of hang) | — | — | all | inspect | p.132 | high |
| WHITE-079 | firmware | Vector table lives at the address the user manual specifies (STM32F103: 0x00000000 via the `.isr_vector` linker section); entry 0 = initial stack pointer (`_estack`), entry 1 = Reset_Handler, then NMI_Handler…; each ISR is registered before its interrupt is enabled | — | linker script | all | inspect | p.132–133 | high |
| WHITE-080 | firmware | Stack grows down, heap grows up; when they meet (or the stack runs into globals) data or return addresses are corrupted → crash; see WHITE map-file rules | — | — | all | review | p.129 | high |
| WHITE-081 | firmware | Functions using static/global variables (and many C++ objects) are nonreentrant; protect globals shared with ISRs; assume interrupts occur at the worst possible time | — | — | all | review | p.134–135 | high |
| WHITE-082 | firmware | Minimal ISR shape: disable nesting (`__disable_irq`), set a volatile flag, re-enable, return; no debug prints, no actuator driving inside; acknowledge/clear the interrupt as the manual requires (often by reading a status register, which may clear it as a side effect) | — | — | all ISRs | review | p.135 | high |
| WHITE-083 | firmware | Register access semantics from the user manual: use indirect set/clear registers for atomic bit changes; keep a shadow variable for write-only registers (or write-functional/read-status registers); expect read-to-clear status registers | — | register map | all | review | p.136 | high |
| WHITE-084 | firmware | For one interrupt with many sources (single-vector MCUs, GPIO bank interrupts, SPI/timer status), the ISR reads the cause/status register and must continue checking after the first hit — multiple causes can be pending | — | — | all | review | p.137 | high |
| WHITE-085 | firmware | Critical sections: the disable-interrupts primitive must return the previous interrupt state and the enable primitive must restore it (nesting-safe); name functions that disable interrupts so accidental nesting is visible; keep critical sections short | — | — | all | review | p.138–139 | high |
| WHITE-086 | firmware | Interrupt bring-up order: (1) disable/mask the interrupt (NVIC ICER) even though power-on cleared it; (2) configure the peripheral; (3) peripheral-level interrupt enable (e.g., TIM2->DIER); (4) global/NVIC enable (ISER); (5) start the peripheral (TIM_CR1_CEN). Both peripheral-level and controller-level enables are required (STM32: SCS 0xE000E000, NVIC = +0x0100, ISER offset 0x000, ICER 0x080) | — | — | all | inspect | p.140–141 | high |
| WHITE-087 | firmware | Use interrupts only for: comm buffers that need filling/emptying, input changes with real-time deadlines, events expensive to poll and rare, short background tasks, and waking from sleep (mandatory); otherwise avoid them (overhead, non-determinism, harder debugging, poor portability) | — | — | all | review | p.142–143 | high |
| WHITE-088 | firmware | Any polling loop that waits on hardware must have a timeout (missed event or command not received) | timeout present per poll loop | — | all | inspect | p.143 | high |
| WHITE-089 | timing | System tick: 1 ms is the popular choice, or the system's natural rate (e.g., 44,100 Hz audio); `DelayMs` suffers fencepost (+1 tick to guarantee coverage) and jitter (starts after a tick) so it is not a 1 ms measure; error is negligible for 10–100 ms delays; choose "no more than" or "no less than" semantics explicitly | delay_actual ∈ (N−1, N+1) ticks | tick period | all | calc | p.143–144 | high |
| WHITE-090 | timing | Tick-counter rollover: uint16 at 1 ms rolls over every 65.5 s; uint32 every 4,294,967,296 ms ≈ 49.7 days; uint64 ≈ 0.58 billion years; `TimePassed(since)` must handle rollover (`now + (1 + TIME_MAX − since)`) | t_roll = 2^bits × T_tick | tick width, T_tick | all | calc | p.145 | high |
| WHITE-091 | firmware | Cooperative mini-scheduler: tasks run to completion (no preemption), not for real-time constraints; each task must yield quickly; watchdog timeout must cover all tasks running back-to-back in one pass | T_wdt > Σ(task worst-case durations) | task durations | schedulers | calc | p.146–147, p.173 | high |
| WHITE-092 | firmware | Every read or write of memory shared between an ISR and main code is a critical section (even a Boolean); make ownership changes atomic by disabling interrupts; this raises system latency; real-time deadlines are typically µs–ms | — | — | all | review | p.152–154 | high |
| WHITE-093 | firmware | Priority inversion: a medium-priority interrupt (e.g., debug output over a comm port) must not preempt the handling of a higher-priority event (button); disable all lower-priority interrupts during the high-priority handler; the most important thing the processor does must hold the highest priority | — | interrupt priority table | prioritized interrupts | review | p.154–155 | high |
| WHITE-094 | firmware | A state machine must handle every event in every state, including invalid/rare ones (ignore with loop-back or log an error); represent it as a state × event table (spreadsheet → CSV → generated code) to expose unhandled combinations; prefer table-driven engines; unit-test each state in isolation | unhandled (state, event) cells = 0 | state table | reactive systems | inspect | p.157, p.161–163 | high |
| WHITE-095 | firmware | Hardware watchdog: reset the processor if not serviced within a (configurable) timeout; service in exactly ONE place the code must pass through that proves all subsystems run (normally the main loop); NEVER service from a timer interrupt; not from DelayMs; not scattered in long functions; prefer a longer timeout watching the whole system over a short one watching part of it | service sites = 1 | — | all products | inspect | p.164–165 | high |
| WHITE-096 | bringup | Watchdog off during bring-up and debugger use (a breakpoint would trigger reset); provide a simple way to disable it; log "watchdog on" at boot so production units are verified to have it enabled; optionally toggle an LED at each service as an external heartbeat | boot log contains WDT state | — | all | inspect | p.165 | high |
| WHITE-097 | firmware | Main-loop patterns in order of decoupling: blocking delay loop → timer-interrupt LED + watchdog in loop → interrupts-do-everything (copying data inside ISRs is NOT short: avoid) → interrupts set volatile event flags (modified with interrupts disabled) handled in main, with sleep between events → cooperative scheduler → active objects (needs RTOS) | — | — | all | review | p.166–175 | high |
| WHITE-098 | firmware | Active object/actor: each task owns private data, communicates only via message queues, and has a single blocking point (the message-pump wait) with no other blocking calls | blocking points per task = 1 | — | RTOS designs | review | p.175–176 | high |
| WHITE-099 | hw-fw | Characterize any new bus before estimating a driver: clock generation (async/sync, who generates), symmetric vs asymmetric (controller), full vs half duplex, number of hardware lines, point-to-point vs multipoint and addressing method (protocol vs chip select), max throughput and overhead share, maximum signal distance | — | bus spec | all buses | review | p.183 | high |
| WHITE-100 | hw-fw | TTL serial levels equal the processor I/O voltage (0–5 V, 0–3 V, 0–1.8 V …); TX and RX must cross between devices (not swapping TX/RX — or clock/data — is the most common hardware issue); USB-to-serial (FTDI) cable voltage must match the TTL side | V_TTL = V_IO; TX→RX, RX→TX | pin map, cable spec | UART links | inspect | p.184 | high |
| WHITE-101 | hw-fw | Debug UART default 8N1, no flow control; baud 2,400–115,200 (up to 921,600); popular 9,600 / 19,200 / 115,200; byte throughput ≈ baud/10 (19,200 baud → ≈ 1,920 B/s); 100 Mb Ethernet ≈ 11 MB/s; ~20 % of an async bitstream is start/stop overhead | B/s ≈ baud/10 | baud | UART | calc | p.185, p.187 | high |
| WHITE-102 | cables | RS-232: ±12 V signals, eight signals + ground; up to 50 ft (15 m) on a normal serial/null-modem cable; low-capacitance cable extends distance ≈ 20×; DTE (usually the PC) is bus controller; modems / serial-to-Ethernet may need RTS/CTS hardware flow control | L ≤ 15 m (standard cable); ≈ 300 m low-C cable | cable type | RS-232 | inspect | p.185–186 | high |
| WHITE-103 | hw-fw | SPI: 4 wires — MISO/SDI, MOSI/SDO, SCK, CS (one per peripheral, usually active low); synchronous, asymmetric; clock from tens of Hz to 100 MHz; zero overhead so 8 MHz clock → 1 MB/s; clock need not be precise (8.1234 or 7.9876 MHz fine); controller must transmit (traditionally 0xFF) to clock data out; set CPOL/CPHA from the peripheral datasheet; signals usually stay on-board; check datasheets — not all peripherals share a bus cleanly | B/s = f_SCK/8 | f_SCK | SPI | calc | p.187–188 | high |
| WHITE-104 | hw-fw | Bit-bang SPI needs 3 spare I/Os (+CS) and a timer interrupting at 4× the bit clock (8 MHz timer for 2 MHz SPI): toggle clock, write MOSI, toggle clock, read MISO; 32 interrupts per byte — reserve only for missing hardware | f_timer = 4 × f_SCK | — | bit-bang | calc | p.189 | high |
| WHITE-105 | hw-fw | I2C/TWI: SCL + SDA, half duplex, multi-controller possible, 7-bit address + R/W, ACK, STOP; device count limited by address space AND bus capacitance; address LSBs often set via pull-ups; speeds 100 kb/s (standard), 10 kb/s (low-speed), 400 kb/s, 1 Mb/s, 3.4 Mb/s; standard mode ≈ 12.5 KB/s bulk throughput; reach: a few meters without transceivers; 4-wire cable (SDA, SCL, power, ground) | f ∈ {10 k, 100 k, 400 k, 1 M, 3.4 M} b/s; no duplicate 7-bit addresses on a bus | address list, bus C | I2C | inspect | p.189–190 | high |
| WHITE-106 | hw-fw | 1-Wire: data + power over one wire (plus ground), implicit clock 16.3 kb/s, up to 10 m (100 m with special cables); parasitic power option; common for temperature sensors and consumable authentication chips | 16.3 kb/s; L ≤ 10 m | — | 1-Wire | inspect | p.191 | high |
| WHITE-107 | hw-fw | Parallel bus sizing: a 320×480 color LCD needs 450 KB per full frame; at ≥ 30 Hz that is ≈ 13 MB/s (105.5 Mb/s) — beyond SPI; an 8-bit parallel bus reduces the per-line rate to 13 Mb/s; parallel write sequence: de-assert WR → select chip → set data → assert WR → repeat; check datasheet timing between steps; data bits on one I/O bank so one register write sets all | B/s = W × H × bytes/px × f_refresh; per-line rate = total/N_lines | display size, refresh | displays, external memory | calc | p.191–192 | high |
| WHITE-108 | hw-fw | Bring spare I/O lines to a header/test points as a parallel debug bus: write error/event codes and capture with a logic analyzer (profiling without the timing change of serial output) | spare I/Os on header ≥ 1 | pin map | all | inspect | p.192 | high |
| WHITE-109 | hw-fw | USB: implicit clock, up to 127 devices, host/device asymmetric, 1.5 / 12 / 480 / 4,000 Mb/s by version, cable up to 5 m, differential signalling, supplies power; do not bit-bang; needs a protocol stack/OS | L ≤ 5 m; devices ≤ 127 | — | USB | inspect | p.193 | high |
| WHITE-110 | process | Driver-effort heuristics: more OSI layers ⇒ harder; point-to-point easier than addressed networks; half duplex harder than full; synchronous easier than asynchronous; asymmetric (bus controller) easier than arbitration; explicit clock easier than implicit. Examples: ISO-7816 smart card — half-duplex, point-to-point, asymmetric, controller clock 1–5 MHz, 4+ OSI layers ⇒ ≥ 3× the estimate of a simple driver; RS-485 — implicit clock 100 kHz–10 MHz, full or half duplex, only physical + data-link specified | — | protocol attributes | planning | review | p.193–194 | high |
| WHITE-111 | test | Serial scope-debug pattern: send "UU3" (0x55, 0x55, 0x33) — alternating bits look like a clock and half-rate clock; ASCII is 7-bit so MSB = 0; anchors '0' = 0x30, 'A' = 0x41, 'a' = 0x61; start transmission high to show the falling edge; trigger on chip select | — | — | serial bring-up | measure | p.194–195 | high |
| WHITE-112 | hw-fw | External ADC/digital sensor over SPI: I/O config (CS, SCK, MOSI outputs; MISO input; assign to SPI function), SPI config per sensor datasheet (clock rate, CPOL, CPHA, frame length), TX-empty interrupt; route the sensor's data-ready line to a processor interrupt-capable pin so data is fetched on demand instead of polled | data-ready pin → EXTI-capable pin | pin map | ADC/sensors | inspect | p.196–197 | high |
| WHITE-113 | firmware | FIFO trigger level for continuous streaming: bytes_remaining_at_interrupt ≥ t_int_latency / t_byte; example SPI 10 MHz → 1.25 MB/s → 0.8 µs/byte; 3 µs worst-case latency ⇒ 3.75 → interrupt with 4 bytes remaining; FIFOs are usually 8 or 16 bytes deep; balance trigger levels for constant stream with fewest interrupts | N_trig ≥ ceil(t_lat / t_byte) | f_bus, t_lat, FIFO depth | streaming | calc | p.198–199 | high |
| WHITE-114 | firmware | DMA: give pointer + count; use ping-pong (two-buffer) DMA for continuous streams to avoid copies; example 32 KB RAM → 2 KB variables + 2 × 15 KB buffers ⇒ interrupt 8×/s at 1 MHz SPI; DMA config: channel/peripheral address, direction, interrupt on empty/half/full | f_int = f_bytes / buffer_size | RAM, data rate | high-throughput peripherals | calc | p.199–202 | high |
| WHITE-115 | timing | Interrupt-overhead comparison for 1 MHz SPI, 8-bit transfers, 10-cycle overhead (Table 7-2): bit-bang 40 M cycles/s (1×); hardware SPI byte interrupts 1.25 M (32×, interrupt at 125 kHz every 8 µs); 16-byte FIFO half-full 156 k (256×, 15.6 kHz, 64 µs slack; full-FIFO trigger 7.8 kHz but only 8 µs slack); DMA 512-byte buffer 2.44 k (16,384×) | cycles/s = f_int × 10 | f_bus, buffering scheme | driver architecture | calc | p.202–203 | high |
| WHITE-116 | firmware | Circular buffer: size a power of two; empty when read == write; full detected by one-slot gap (wastes one element) or a length variable; interrupt-safe when producer/consumer variables are isolated and read/write updates are atomic; length = (write − read) & (size − 1) | size = 2^n | — | all data pipes | inspect | p.203–205 | high |
| WHITE-117 | firmware | Circular-buffer pointer updates must be single atomic stores (a uint16_t index is not atomic on an 8-bit MCU; usually but not always on 32-bit); define the overflow policy explicitly (reject new data vs. drop oldest); avoid modulo arithmetic in ISRs (slow) — hence power-of-two sizes; add free/processed pointers to avoid copies in ADC→process→DAC chains | — | index width vs CPU width | all | review | p.207–209 | high |
| WHITE-118 | components | Processor selection: assume ≥ previous platform's processing, RAM and code space but verify; prefer popular parts with broad compiler/debugger/RTOS support; check lead time and end-of-life (never start a platform on a dying chip); pick a part in the middle of a family (upgrade and cost-down paths); offload the CPU with peripherals; weigh volume and cost goals | — | — | platform selection | review | p.210 | high |
| WHITE-119 | hw-fw | Key matrix I/O count: row/column scan gives M × N keys with M + N lines (12-key pad as 3 × 4 → 7 lines vs 12 direct); Charlieplexing gives N² − N inputs from N pins plus diodes (12 keys → 4 lines + 12 diodes); rows configured as outputs high, columns inputs with internal pull-ups; scan = row low → read columns → row high; matrices must be polled (no interrupt-on-change) and misread simultaneous presses | lines_rc = M + N; keys_charlie = N² − N | key count | keypads/LED arrays | calc | p.211–213 | high |
| WHITE-120 | hw-fw | Multiplexed segment display: 8 characters × (7 segments + DP) = 64 segments driven as 8 × 8 matrix → 16 I/O lines; each LED is on 1/8 of the time (LED brightness OK, LCD washes out); refresh the whole matrix faster than 30 Hz to avoid flicker (check with peripheral vision); LCD segments need AC drive → use an LCD controller (ST AN1447); 7-segment code for "3" = 0x79 in abcdefg order; 17 calculator buttons fit a 4 × 5 matrix (9 lines) | f_refresh > 30 Hz; duty = 1/rows | segments, rows | segmented displays | calc | p.213–214 | high |
| WHITE-121 | firmware | Graphic-asset store (fonts + images) carries a version for the file and the asset list, checked by firmware before use, or garbage may be displayed | — | — | displays | inspect | p.215 | high |
| WHITE-122 | firmware | Font/bitmap sizing: font_bytes = chars × H_px × W_px × bpp / 8; 94 chars × 8 × 6 × 8 bpp = 36,096 bits = 4,512 B; 8 × 8 mono glyph = 8 B, at 8 bpp = 64 B; full A–Z/a–z/0–9 mono font ≈ 500 B vs ≈ 4 KB at 8 bpp for 8-px letters; 30 × 40 px chars, 94 chars, 16-bit color = 220 KB; 5-level antialiasing needs 3 bpp; English needs 94 glyphs (+94 for FR/IT/DE/ES); RLE gives no saving at 1 bpp but is effective at ≥ 1 B/px | font_bytes = N × H × W × bpp/8 | glyph set, size, bpp | displays | calc | p.216–222 | high |
| WHITE-123 | firmware | Frame-buffer sizing: 2.4-inch 240 × 320 24-bit LCD = 225 KB per screen; 320 × 480 color = 450 KB; update time = pixels × max(bus time/bit, display receive time/bit); compute separately for animated regions; avoid tearing by synchronizing updates with the display refresh | frame_B = W × H × bpp/8; t_update = px × bpp × t_bit_max | display, bus | displays | calc | p.217, p.222 | high |
| WHITE-124 | requirements | Size external display-asset flash: sum fonts (count × sizes × bpp) + glyphs/icons/images, then leave ≥ 25 % extra for growth; plan a SPI flash as soon as "animation" or "internationalization" is required | asset_flash ≥ 1.25 × Σ assets | asset list | displays | calc | p.221–222 | high |
| WHITE-125 | test | Asset packing tool (script): map image filename → code identifier → flash offset, add metadata (width, height, default position), pack into one binary; provide a debug/manufacturing command to load the SPI flash over the serial port (manufacturing may use a direct flash programmer instead); keep the script maintained — it is reused many times | — | — | displays, production | inspect | p.222–223 | high |
| WHITE-126 | hw-fw | External flash is almost always attached via SPI (fastest common protocol); SD cards can also be accessed via SPI | — | — | storage | inspect | p.221 | high |
| WHITE-127 | firmware | EEPROM/NV map example: serial number 4 B @ 0; last boot time 4 B @ 4; cause of last reboot 1 B @ 8; boot count 3 B @ 9 — keep an address/size header; update boot status every reset; EEPROMs are more expensive, smaller and slower than flash but byte-writable with higher endurance | — | — | NV data | inspect | p.223 | high |
| WHITE-128 | firmware | Emulated EEPROM / KV store on flash needs ≥ 2 flash blocks (write into one while the other erases), contains a find-erase-write state machine and takes more space than the data (invalidated entries); use the vendor/RTOS implementation rather than writing one | blocks ≥ 2 | flash geometry | NV parameters | inspect | p.224 | high |
| WHITE-129 | reliability | Flash endurance budget: some flash lasts ≈ 10,000 erase/write cycles — writing one address once per second wears it out in < 20 min (10,000 / 60 = 16.7 min); worn cells show sticky bits (0x55 "U" reads back 0x57 "W"); file systems must be power-loss resilient, wear-level all blocks equally and map out bad blocks (e.g., littlefs) | life = endurance / write_rate | endurance, write rate | flash storage | calc | p.224–225 | high |
| WHITE-130 | firmware | Sampling RAM buffer must cover the flash erase time: at 20 kHz (0.05 ms/sample) with 25 ms max erase → 500 samples buffered; buffer ≥ f_sample × t_erase_max × sample_size (erase takes tens of ms; erase ≫ write ≫ read) | N_buf ≥ f_s × t_erase_max | f_s, t_erase_max, sample size | data loggers | calc | p.225, p.239 | high |
| WHITE-131 | requirements | Data-store sizing inputs: sample rate and size; continuous vs burst (longest burst); collection interval / maximum time between transfers; erase-after-transfer vs retain; overwrite-vs-keep when never collected; plus metadata (timestamps etc.) — budget ≈ 10 % overhead if unknown | store ≥ rate × size × t_max_between_transfers × 1.10 | — | data loggers | calc | p.226 | high |
| WHITE-132 | timing | Timestamps: a 32-bit ms counter wraps in 2^32 ms ≈ 49 days — a tick counter is not a timestamp; an RTC needs a battery/supercap, initial time set and re-set after battery loss; record UTC only; RTC accuracy follows its clock and runs slower when cold; server corrects device time, or use GPS PPS for precision | — | — | data loggers/IoT | review | p.226 | high |
| WHITE-133 | firmware | Power-loss-safe flash erase: keep a modification list in a separate flash area (allocate 2 sectors for it): write "about to erase block X", erase, write "erase X complete"; on boot scan for unmatched start marks; for writes, add a checksum per written block and size blocks by how much data may be lost per power failure; receiver must tolerate duplicate data after reset-before-mark | mod-list sectors = 2 | — | data loggers | inspect | p.227 | high |
| WHITE-134 | components | ADC/DAC resolution: 8-bit = 256 levels, 16-bit = 65,536 levels; sample rate × bits constrain CPU speed and RAM; integer math on small values distorts (raise input amplitude or use more bits); "all sensors are temperature sensors" — plan temperature calibration | levels = 2^bits | bits | analog | calc | p.228–229 | high |
| WHITE-135 | components | Prefer digital sensors when budget allows: integrated ADC, filtering and temperature compensation, lower EMI susceptibility; check that the processor has the sensor's bus, the throughput fits, and how data-ready is signalled | — | — | sensors | review | p.229–230 | high |
| WHITE-136 | emc | US FCC Part 15: any system with a clock over 9 kHz needs EMC (radiated emissions) testing in an anechoic chamber; also susceptibility testing; prepare an EMC test firmware build that drives all communication paths at maximum rate; shield analog paths (Faraday cage to ground); digital signals emit more but are more immune | f_clk > 9 kHz ⇒ EMC test required | clock list | all products | measure | p.230 | high |
| WHITE-137 | firmware | Data-driven systems: producer (ADC) and consumer (DAC) rates must balance with processing slightly faster than generation; define the fall-behind policy (skip data vs. reduced processing) and consequences of missed data | t_process < t_sample | rates | streaming | calc | p.231 | high |
| WHITE-138 | firmware | Pipeline latency accumulates with every buffered filter stage (example 3-point noise filter + 16-point low-pass); write to flash in chunks; windowed detectors use overlapping windows sized from physics (e.g., heart rate ≤ 250 bpm) | latency = Σ(stage buffer − 1) samples | filter lengths | signal chains | calc | p.234–235 | high |
| WHITE-139 | requirements | Bandwidth: bandwidth = sampleRate × channels × sampleSize; 44,100 × 4 × 16 bit = 352,800 B/s; minimum SPI clock = bandwidth in bits = 2.8 MHz (assuming DMA); sum every device on a shared bus, compute nominal and worst case, keep margin; burst snippet = bandwidth × duration (4 s → 1.3 MB) vs 512 KB RAM ⇒ external RAM or flash write speed check; verify readout speed while still sampling | BW = f_s × ch × bits/8; f_SPI_min = f_s × ch × bits; snippet = BW × t | — | all | calc | p.236–237 | high |
| WHITE-140 | components | Memory selection questions: size (Mb vs MB!), read/write time (bus + device), erase granularity and time, rewrite endurance; external shared memory needs mutexes and can lock up via priority inversion (KV-store erase blocks data writes and asset reads) | — | memory datasheets | all | review | p.238–239 | high |
| WHITE-141 | bringup | Debug checklist: powered? (sure?); running the code you think?; can you test only that part?; errata and exact part number checked?; intermittent → timing or stack overflow?; uninitialized variables (does making them global change behaviour?); optimizations off?; map file reviewed?; last resort: ground loop? | — | — | debugging | review | p.243 | high |
| WHITE-142 | firmware | Enable every compiler warning and fix all (e.g., assignment in conditional, uninitialized use, returning address of local); bracket modifications to vendor code with START/END comments or keep them as patch files | warnings = 0 | build log | all | inspect | p.244, p.261 | high |
| WHITE-143 | firmware | Optimization-dependent failures: mark ISR/main shared variables volatile; uninitialized globals/statics are zero but uninitialized locals are random; temporarily add slack at array ends (off-by-one), make locals global, or slow the system to localize | — | — | all | review | p.245–246 | high |
| WHITE-144 | process | Bug method A (reproduce): reproduce; with minimal code; check last working version / find the introducing change; reproduce on command or at boot; confirm you run the code you think; re-minimize. Method B (explain): describe symptoms; list all possible causes; explain to a duck; log every change and effect; diff against last known good; code review. Alternate between A and B | — | — | debugging | review | p.246–247 | high |
| WHITE-145 | firmware | Cortex-M divide-by-zero returns 0 silently unless SCB->CCR is configured to trap it (DIVBYZERO usage fault → hard fault); enable fault traps so errors surface | — | CCR config | Cortex-M | inspect | p.248–249 | high |
| WHITE-146 | firmware | NULL (address 0) may be flash or unmapped: writes cause data/bus faults only if the processor is configured to detect them; uninitialized pointers are worse (random, sometimes valid); use hardware watchpoints (limited count) to catch memory corruption and stack overflow | — | — | all | review | p.249–250 | high |
| WHITE-147 | firmware | Bad function pointers execute address 0 (reset vector) or invalid opcodes (0xE0000000 → bad-instruction fault); code executed from RAM can be overwritten by memory bugs; pulling a 32-bit value from an odd offset in a byte array causes misaligned-access/bus faults or slow byte-wise access | — | — | all | review | p.250–251 | high |
| WHITE-148 | firmware | Never return a pointer to stack (local) memory; stack memory is ephemeral and uninitialized; freed heap memory reuse is unmonitored (no fault) — prefer fixed buffers to malloc/new | — | — | all | inspect | p.252–253, p.261 | high |
| WHITE-149 | firmware | Bound every input copy (unbounded `getchar` fill overflows the stack buffer and can hijack the return address); enable compiler stack-smashing protection (canaries); size RTOS per-task stacks for real call depth; recursion in parsers overflows stacks | — | — | all | inspect | p.253–254 | high |
| WHITE-150 | firmware | Hard-fault handler: assembly selects MSP vs PSP (`tst lr, #4`) and passes the stack pointer to a C handler; C handler does `BKPT #0` when a debugger is attached else spins until watchdog reset; decode the memory/bus/usage fault status registers | — | — | Cortex-M | inspect | p.255 | high |
| WHITE-151 | firmware | Core dump: reserve a RAM region in the linker script excluded from C startup (NOLOAD, e.g., 255 B at 0x017F00 carved from a 32 KB RAM); store key 0x0BADC04E, fault cause, r0–r3, return address, stack pointer, last battery ADC reading; on boot validate key → log (flash/serial/cloud) → clear; commit the .map file with every released binary | — | linker script | all products | inspect | p.256–260 | high |
| WHITE-152 | firmware | Linker script: segments bss (uninitialized globals → RAM), data (initialized globals → RAM), text (code + const → ROM or RAM), vectors (in text, first); declare MEMORY regions with ORIGIN/LENGTH and attributes (Flash rx 0x000000 64 KB; RAM rwx 0x010000 32 KB in the example) so the linker errors when sections do not fit; never write one from scratch — modify the vendor's | — | memory map | all | inspect | p.257–258 | high |
| WHITE-153 | test | Memory-bug tools: red zones between buffers filled with 0xDEADBEEF / 0xA5A5A5A5 and inspected after runtime; fill stacks with a known pattern at boot and read the high-water mark after long runs; vary stack size to change time-to-failure; making variables static/global only hides stack bugs | stack margin = size − high-water > 0 | — | all | measure | p.260–261 | high |
| WHITE-154 | requirements | Document the device↔host interface like any peripheral datasheet (commands, data, versions) so both sides can change independently; base it on the command interpreter | — | — | connected devices | inspect | p.263 | high |
| WHITE-155 | rf | Do not build your own radio: use a precertified radio module; estimate custom-radio difficulty at ≥ 10× intuition; environment matters (tree leaves absorb 2.4 GHz — installations that work in November fail in spring) | — | — | wireless | review | p.265 | high |
| WHITE-156 | requirements | Gateway (phone/Linux) software is part of the system and must be specified (which data goes to cloud, device-health data); mesh networks (Zigbee, Thread, BLE, Matter) have throughput/latency/range that cannot be calculated simply — prototype | — | — | IoT | review | p.266–267 | high |
| WHITE-157 | power | Cell/satellite modems (AT commands over serial) are expensive and power hogs: keep the modem powered off except during transmissions or scheduled listen windows; fleet configuration must scale beyond a spreadsheet | — | — | remote devices | review | p.267–268 | high |
| WHITE-158 | firmware | Every application-layer protocol carries a protocol version (per command or dedicated command) so cloud and devices on different versions can negotiate | — | — | connected devices | inspect | p.269 | high |
| WHITE-159 | firmware | Error detection: 8-bit sum of {10, 20, 40, 60, 80, 90} = 300 → 44 (mod 256), undetected-error chance 1/256 for random data; sum as 16-bit words for more data; simple sums catch single-bit errors but not swapped bytes or cancelling errors; bursty channels need a CRC (use the processor's CRC engine if present); hashes identify data rather than detect errors | P_undetected(8-bit sum) ≈ 1/256 | — | comms, storage | calc | p.269–270 | high |
| WHITE-160 | firmware | Security: never invent algorithms — use RSA/DES/AES (smaller keys if needed, with an estimated crack time); use the processor's crypto acceleration; let the server do the asymmetric-heavy side; encrypt only critical data if the CPU is small; assume the attacker knows the algorithm (Kerckhoffs); detect cloned consumables by counting serial-number reuse in a database; the weakest link is usually key handling, not the cipher | — | — | all connected | review | p.270–272 | high |
| WHITE-161 | firmware | Firmware-update architecture: split bootloader + application; application downloads the new image into auxiliary flash; bootloader (no network code) on boot: (1) image in aux flash? (2) compare version with running code, same → run; (3) verify hash + signature with the public key, mismatch → erase image and reboot; (4) newer → decrypt in sections and program; (5) reboot. Optionally verify the running image and re-program from aux flash if corrupt. Start update development early — an update bug in the field cannot be fixed | — | — | all updatable devices | inspect | p.273–277 | high |
| WHITE-162 | firmware | Code-read protection: on-chip code unreadable via debugger/loader; may force whole-chip erase (no sector erase) or block writes entirely — account for it in the update design; firmware bundle = signed + hashed + encrypted image with version | — | — | secure devices | inspect | p.275–276 | high |
| WHITE-163 | process | Per-unit keys: programmed in manufacturing, serial-number↔key pairs tracked for product life, per-unit update bundles built by script and routed by the server; key store protected for millions of units — budget by threat level | — | — | high-security devices | review | p.277 | high |
| WHITE-164 | firmware | Fallback lifeboat: keep factory images (e.g., v1.0 runtime + OS) in auxiliary flash so a failed update falls back to a factory reset instead of a brick; multi-image systems (OS, app, second core) need independent update paths | fallback images ≥ 1 | aux flash size | updatable devices | inspect | p.277–278 | high |
| WHITE-165 | process | Staged rollout: desk → team → whole company beta (push-button update) → small customer groups → all; server tracks which groups get which build; watch crash rate and battery drain against build contents; field-only failures seen: customer power fluctuations, time zones/DST, GPS parsing, salt-fog ADC readings, one manufacturing run's battery drain | — | — | fleets | review | p.279–280 | high |
| WHITE-166 | firmware | Device-health telemetry: boot cause code (hard fault with core dump, user reboot, battery depletion — each distinct), voltage over time with active-vs-sleep time, periodic heartbeats sized/frequency per power budget carrying firmware version and diagnostics; crash handling becomes statistics at fleet scale | — | — | connected devices | inspect | p.281 | high |
| WHITE-167 | test | Manufacturing test firmware returns pass/fail (green/red) only; supports multi-unit programming; provisioning (keys, cloud enrolment) is separate from user onboarding and may be done in-house; radio tests on a busy line need a Faraday cage — do not plan Bluetooth firmware loading in manufacturing | — | — | production | inspect | p.282 | high |
| WHITE-168 | firmware | Map-file review: library inclusion list shows which module pulled a library (e.g., memcpy → libcr_c.a); "common symbols" lists globals (statics appear later or not at all); discarded input sections list unreferenced code; memory configuration echoes the linker regions and used amounts; diff map files between builds to attribute size changes | — | .map | all | inspect | p.286–287 | high |
| WHITE-169 | firmware | Code-space audit from the map: compare `.text` size to flash length (example 0x7CCD of 0x8000 ⇒ nearly full); list function sizes and attack the largest — libraries (floating point, printf/scanf, iostream) and hidden operators (signed long divide `__bhs_ldivmod` = 0x20C bytes, > 2× main); `.rodata` holds strings (`str1.1`) and static-initialized local arrays (unnamed); `#define` constants are embedded in code, `const` in `.rodata`; `fill` = alignment padding (5-char string on 32-bit = 1.25 words → 3 fill bytes) | used/available per region | .map | all | inspect | p.287–289 | high |
| WHITE-170 | process | Code-size reduction: first try size optimization (`-Os`), then keep a scorecard per change (Table 11-1 example: baseline text 31,949 + data 324 = 32,273 B; removing test code freed 5,320; reimplementing abs() freed 2,104; computing a const table at init freed 40 (text +40, data −80); reverted changes counted) so trade-offs are quantified ("uglier but saves 2 KB") | Δbytes per change recorded | .map sizes | all | calc | p.290–291 | high |
| WHITE-171 | firmware | Library footprint cuts: fixed-point instead of floating point; `Log`/`LogWithNum` instead of printf; own strcpy to drop the strings library; abs() as a macro to drop the floating-point library; consider a reduced embedded libc (Embedded Artistry LibC); but do not write libraries you do not have to | — | .map library list | all | review | p.291–292 | high |
| WHITE-172 | firmware | Macro vs function code-size crossover (Table 11-2, min-of-three): macro 0 / 76 / 152 B for 1 / 2 / 3 calls, function 20 / 60 / 96 B; with size optimization macro −40 / 8 / 56, function −40 / −20 / 0 ⇒ prefer a function beyond 2 call sites (1 with optimization); min-of-two crossover ≈ 3 calls; `inline` is only a hint (force with `__attribute__((noinline))` when measuring); macros cost no stack frame (RAM) | crossover ≈ 2 calls (unoptimized), 1 call (optimized) | call-site count | all | calc | p.292–293, p.301 | high |
| WHITE-173 | firmware | Debug strings consume code space: compile them out per subsystem (`#define MOTOR_LOG 1/0` wrapping Log/LogWithNum) while keeping runtime level control elsewhere; for further savings replace strings with constants plus a post-processing dictionary script | — | .rodata size | all | inspect | p.294 | high |
| WHITE-174 | firmware | Ban dynamic allocation in constrained systems: malloc is invisible in the map file, nondeterministic, carries metadata overhead, costs search cycles and fragments (30-byte heap: allocate 10 + 5, free 10 → 25 free but no contiguous 20 → NULL); use ping-pong buffers, circular buffers or a chunk allocator instead; if you'd rebuild malloc, use the built-in one | heap = 0 (or library minimum) | — | all | inspect | p.295–296 | high |
| WHITE-175 | firmware | RAM audit: map `.data` (initialized globals, also needs `.rodata` for initial values) and `.bss` (zeroed globals/statics) totals vs RAM (example 0x144 + 0x1B7C of 0x2000) exclude heap and stack; size the stack by filling with a canary pattern (0xDEADC0DE), exercising everything, measuring the high-water mark, then allocating ≈ 25 % more; avoid recursion | stack_alloc ≥ 1.25 × high_water | high-water measurement | all | measure | p.296–297 | high |
| WHITE-176 | firmware | Register-friendly code: fewer than four parameters per function; use N-bit native variables on an N-bit processor (narrow types cost sign/zero-extension instructions); pass scalars by value (taking an address forces RAM) but structures by pointer; minimize each variable's live scope; verify by reading the assembly listing (.lst) with optimization off first | params < 4; var width = register width | — | all | review | p.298–300, p.309–310 | high |
| WHITE-177 | firmware | Deep function chains push earlier locals/parameters to the stack — flatten call trees; tail calls let the compiler drop the caller's frame; a global can short-circuit passing one value through a chain (but globals always occupy RAM and are slower than registers) | — | — | all | review | p.300–302 | high |
| WHITE-178 | firmware | RAM overlays: large buffers (display, comms, sensor) that are never live simultaneously may share memory (example: buffers exceeding a 4 KB RAM fit with overlay) via a single-accessor module, a union with owner tag, or linker-script overlay; the mutual-exclusion dependency must be documented — it breaks encapsulation | Σ(peak concurrent buffers) ≤ RAM | buffer lifetimes | RAM-starved | review | p.302–303 | high |
| WHITE-179 | test | Profiling: (a) I/O-line profiler — set a test-point pin high on function entry, low on exit (also inside ISRs), view on a scope; shrinking wait time before a periodic input means the system is about to miss data; (b) timer profiler — profiled section ≥ 2× (preferably ≥ 10×) the tick, verify zero overhead by profiling an empty section, average many samples (1,000 samples → 10,435 ms ⇒ 10.4 ms); (c) sampling profiler — timer asynchronous to every periodic interrupt (e.g., 1.7 Hz when 10 Hz and 15 Hz exist), log return addresses to RAM, map to functions with the map file; can stay in the code with timer off | t_section ≥ 10 × T_tick (timer profiler) | test points, timer | all | measure | p.304–308 | high |
| WHITE-180 | firmware | Memory wait states: code from N-wait-state flash stalls unless pipeline depth > N (stalls at branches/calls anyway); copy critical functions to zero-wait-state RAM (`ramfunc` + linker section), overlaying with a buffer if RAM is tight — profile to confirm copy overhead is repaid | pipeline_depth > wait_states | memory timing | speed-critical | calc | p.309 | high |
| WHITE-181 | firmware | Cycle optimization order: compiler optimization on → variables into registers → examine the whole call chain (hoist chip-select out of the per-byte LCD write) → pointer arithmetic instead of index math → no math or `if` inside loops → count loops down to zero (compare-with-zero is cheapest) → unroll loops (10 → 8 instructions per 16-bit pixel = 20 %) while watching code space (a fully unrolled 240 × 320 screen = 12,243+ copies); optimize loops, not one-time code; avoid signed/unsigned mixing (signed promotes to unsigned in comparisons) — prefer unsigned | — | profile data | speed-critical | review | p.310–316 | high |
| WHITE-182 | firmware | Lookup tables trade code space or RAM for cycles (AES has a fast/large table version and a slow/small computed one); RAM tables when RAM is fast or values change; `switch` may compile to a jump table — check the assembly; byte bit-reversal: 256-byte LUT or three masked swap steps (0x55/0xAA <<1, 0x33/0xCC <<2, 0x0F/0xF0 <<4) | LUT_bytes = entries × width | — | all | calc | p.317–318, p.321–322 | high |
| WHITE-183 | firmware | Hand assembly only for a proven hot spot: start from the compiler's optimized output (never a blank slate) and paste the C source in as comments | — | — | rare | review | p.318 | high |
| WHITE-184 | requirements | Resource margin: leave spare code space, RAM and cycles at design time for bug fixes and hardware changes; medical/safety products need larger margins (every recompile is paperwork); each further 10 % of optimization costs about twice the previous; if you need 40 % reduction at the end, the hardware was misjudged; manage resources continuously, not at the end | margin_reserved > 0 at ship (larger for regulated) | budget | all | review | p.319–320 | high |
| WHITE-185 | firmware | Accuracy vs precision: carry only the precision the error budget needs (state results with uncertainty, e.g., (9.1092 ± 0.0002) × 10⁻³¹ kg); surplus precision costs RAM and cycles and is noise | — | error budget | algorithms | review | p.323–324 | high |
| WHITE-186 | firmware | Operation cost ranking: add/subtract fast; constant shifts one cycle; multiply between add and divide but nearer add (single MAC on DSPs); divide very slow (library call visible in the map); floating point extremely slow without an FPU; modulo is a hidden divide — use power-of-two intervals and masks (`i & 0x07`); real `#define` constants beat `const` variables (which get loaded into registers) | — | — | all | review | p.324–325 | high |
| WHITE-187 | firmware | Averaging choices: rolling N-point needs an N-sample buffer and a divide per step; block average (accumulate, divide once when needed) is as accurate at its output points with far less RAM/cycles; cumulative average needs no buffer but is slightly less responsive; median (3- or 5-point) rejects ADC glitches at sort cost | — | output rate vs sample rate | signal chains | calc | p.325–328 | high |
| WHITE-188 | firmware | Integer-division truncation: never divide similar-magnitude numbers (e.g., (new − old)/N in a rolling average yields junk); pre-scale samples by a constant > N so numerators stay large, check for overflow, and document the assumed input range — a 10 % range change can break a fixed-point design | numerator ≫ divisor; scaled max < type max | input range | fixed-point | calc | p.328–329 | high |
| WHITE-189 | firmware | Variance: skip the square root unless standard deviation itself is needed; use Welford's one-pass algorithm — intermediate M2 needs only 2× the sample width (8-bit samples → 16-bit M2) whereas a naïve sum-of-squares grows with N (two 8-bit samples at 127 → 32,258 ≈ 15 bits; five → 17 bits; 16-bit samples → 64-bit accumulator); Welford divides every step and small deltas can truncate the mean to zero; statement order is load-bearing; choose sqrt approximations by profiling against the math library | M2 width = 2 × sample width | sample width, N | statistics | calc | p.329–332 | high |
| WHITE-190 | firmware | Factor polynomials (Horner): A·x³ + B·x² + C·x = ((A·x + B)·x + C)·x → 3 multiplies + 2 adds instead of 9 + 2; truncated Taylor series (sin x ≈ x − x³/3! + x⁵/5! − x⁷/7!) rearranged via Horner give "accurate enough" transcendental functions | ops = n mult + n add for degree n | — | algorithms | calc | p.332–333 | high |
| WHITE-191 | firmware | Truncated Taylor sine: 4 terms (through x⁷/7!) give error ≈ 0.000003 over −π…π; add x⁹/9! for more; for inputs within ±0.2π, sin x ≈ x meets 10 % accuracy and 2 terms meet < 1 %; choose term count from input range and error budget (angles in radians) | terms = f(range, error) | input range, tolerance | trig on small MCUs | calc | p.334 | high |
| WHITE-192 | firmware | Divide by a constant with multiply + shift: choose (m, s) with m/2^s ≈ 1/k (Table 12-1 for 1/6: 171/1,024 → 0.19 % error; 683/4,096 → 0.04 %); error halves for each extra shift bit; a 16-bit input needs a 32-bit intermediate; skipping the final shift keeps extra precision (value is ×2^s) | y = (x × m) >> s; err halves per +1 shift | k, tolerance | integer math | calc | p.335–336 | high |
| WHITE-193 | firmware | Scaled-input fixed-point evaluation: scale x by 2^n (e.g., 1,024) and shift right by n after every x·x so the scale is applied once; scale constants too (1,024/3! ≈ 171; 1,024/5! = 8.533 → 8 adds error; 7! = 5,040 still needs a real divide); spend error analysis on the largest error contributors (larger scale reduces error) | each product of scaled terms >> n | n, term constants | polynomial evaluation | calc | p.336–337 | high |
| WHITE-194 | firmware | Implicit-input lookup tables: valid only inside the tabulated input range (guard inputs — index 19 into a 13-entry table is undefined behaviour); use power-of-two step so index = (x − base) >> shift (no divide); add half a step to the base to center each bin (index = (x − (base − step/2)) >> shift) — "prevalent in almost every well-implemented lookup table"; document each entry's covered range | index = (x − base + step/2) >> log2(step); 0 ≤ index < N | table range, step | LUT algorithms | calc | p.338–340 | high |
| WHITE-195 | firmware | Linear interpolation between table points: y = p0.y + ((x − p0.x)·(p1.y − p0.y))/(p1.x − p0.x) computed in a 32-bit intermediate for 16-bit points; power-of-two x steps turn the divide into a shift (but couple code to table data); explicit (x, y) tables allow variable step size (dense where curvy, sparse where linear) and are the form used for manufacturing calibration data (e.g., temperature vs offset); ordered search then interpolate, extrapolating with the first/last pair beyond range | see formula | table, x | LUT algorithms, calibration | calc | p.341–344 | high |
| WHITE-196 | firmware | Floating-point cost without an FPU: turning one integer add into a float add cost 532 bytes of code (`__aeabi_fadd`, `__aeabi_fsub`); printf/iostream drag in the floating-point library even if you never use floats — check the map file; avoid floats "like the plague" unless an FPU exists | Δcode ≈ 532 B for first float op (example toolchain) | .map | all | inspect | p.345–346 | high |
| WHITE-197 | firmware | Binary-scaled ("fake float"/Q) numbers {numerator, shift}: value = num / 2^shift (negative shift = left shift); precision vs numerator width for 12.345 (Table 12-2): 4-bit/shift 0 → error 0.345; 7-bit/3 → 0.030; 9-bit/5 → 0.00125; 14-bit/10 → 0.000273; 24-bit/20 → 2.67e−7; 29-bit/25 → 1.19e−9; larger shift ⇒ more numerator bits; use a fixed-point/Q library rather than hand-rolling; huge values fit by dividing (10,000,000,001 → {1,250,000,000, −3} loses the last digit) | error ≈ 2^−shift; bits_needed ≈ log2(value) + shift | value range, tolerance | fixed-point | calc | p.346–348 | high |
| WHITE-198 | firmware | Fixed-point arithmetic rules: addition — align shifts by left-shifting the smaller-shift operand into a wider temporary, add, then right-shift (decrementing the shift) until the result fits (example 99/2³ + 111/2⁵ → 126/2³ = 15.75 vs ideal 15.84); the shift difference must itself fit the shift type; multiplication — promote before multiplying (32×32 needs 64-bit temp, 16×16 needs 32), add shifts, normalize, assert shift sum < INT8_MAX (example 12.345 × 0.5 = {1,656,917,852, 28} = 6.1725); division — divide numerators, subtract shifts; the designer must know min/max at every step or precision errors occur silently | temp_bits ≥ bits(a) + bits(b) | operand ranges | fixed-point | calc | p.348–351 | high |
| WHITE-199 | firmware | On-device ML: usually inference only; the optimized on-device implementation must be tested against the original algorithm's outputs and re-tested after every retraining; consider sending features to the cloud for inference; traditional algorithms are often adequate and easier to debug; use CMSIS-DSP / CMSIS-NN / TinyML libraries instead of custom math | — | reference outputs | ML on MCU | measure | p.351–352 | high |
| WHITE-200 | firmware | Integer growth: sum 1..N = N·(N+1)/2 needs about twice the bits of N ((2¹⁶)² = 2³²); size output buffers at 2× input width for products; prefer unsigned types when negatives are not needed | bits(out) = 2 × bits(in) for products | operand widths | all | calc | p.353–354 | high |
| WHITE-201 | cost | Engineer hourly cost ≈ annual salary / 1,000; buy a tool when its price < hours saved × hourly cost (e.g., $3.50 tool saving four $1-hours) — but capital vs. sunk cost may still block the purchase | cost_h ≈ salary/1000 | salary | process | calc | p.355 | high |
| WHITE-202 | power | Power/energy relations: P = I²·R; P = V·I; V = I·R; E = P·t (J = W·s); reduce energy by reducing voltage (choose 1.8 V parts — low core voltage is why cores run at 1.8 V while I/O runs at 3–5 V), resistance (e.g., MEMS over mechanical sensors), current (GPIO settings, processor features) and time on (turn things off) | E = P·t; P = V·I = I²·R | V, I, R, duty | all | calc | p.356–357 | high |
| WHITE-203 | power | Current-measurement setup: disconnect the debugger/programmer (JTAG can power the processor from the PC) and the serial console (ground differences) — exactly one power and one ground into the DUT; running small systems draw tens–hundreds of mA (DMM mA range); sleep currents need µA or better (beyond cheap DMMs); DMM range too high reads zero, too low blows the fuse | connections to DUT = {power, ground} | — | power test | measure | p.357–358 | high |
| WHITE-204 | power | Series-shunt method: I = V_shunt / R; pick R so V is readable without burdening the DUT (Table 13-1: 12 mA·1 Ω = 12 mV readable; 23 µA·1 Ω = 23 µV unreadable; 34 µA·10 Ω = 0.34 mV only on a very good DMM; 45 µA·100 Ω = 4.5 mV readable but R getting large); measure the actual shunt resistance afterwards (tolerance); use 0 Ω on production boards; DMM gives static current only — use a scope or a power profiler for dynamic/orders-of-magnitude (active vs sleep) measurements | I = V/R; R ≪ R_DUT | expected I, DMM resolution | power test | measure | p.358–360 | high |
| WHITE-205 | power | Battery life estimate: alkaline AA ≈ 1.5 V nominal, ≈ 3,000 mAh; t ≈ capacity / I_avg (30 mA → 100 h ≈ 4 days; 300 mA → 10 h); the linear rule breaks at high draw (3,000 mA lasts < 1 h) — read the battery datasheet for chemistry, peak current, capacity vs load; batteries in series add voltage, in parallel add current | t_h = C_mAh / I_mA (I ≪ C/1 h) | capacity, average current | battery products | calc | p.360, p.377 | high |
| WHITE-206 | power | Current budget spreadsheet: rows = components, columns = device states (on, asleep, radio-transmit "high power", motion …); currents add at the same voltage (screen 12 mA + processor 0.6 mA = 12.6 mA); sleeping processor ≈ 80 µA class; I_avg = Σ_states(I_state × time fraction); design questions: battery cost/size, time between charges, major consumers, states and their draw, allowable time per state | I_avg = Σ I_s·t_s/Σt_s | component datasheets, state timing | battery products | calc | p.360–361 | high |
| WHITE-207 | power | Unused external chips: remove power (zero current) if the processor controls the rail; else hold in reset (near-zero, verify in datasheet); account for reset-recovery time (ADCs are slow to recover but big consumers, so usually worth it); external RAM can be powered down after moving data | — | rail control, recovery times | low power | review | p.362 | high |
| WHITE-208 | power | Unused / peripheral-off GPIO configuration preference: input with internal pull-down > tri-state (floating) > output low > input with pull-up; make internal pulls match external ones (or delete the redundant external resistor) — fighting resistors wastes power; never leave lines pulled up or driven high into an unpowered/reset chip (protection diodes back-power and can damage it) | each unused pin ∈ {in+PD, hi-Z, out-low, in+PU}; no high level into unpowered part | pin map, power domains | low power | inspect | p.362–363 | high |
| WHITE-209 | power | Disable unused processor subsystems (e.g., a second SPI port): fully off is best, clock-gating is next best; processor power ∝ clock frequency — cutting the clock ≈ 10 % cuts chip power ≈ 10 %; use slow/medium/fast performance modes; trade "tortoise" (slow, always on) against "hare" (sprint then sleep) | P_chip ∝ f_clk | clock config | low power | calc | p.363 | high |
| WHITE-210 | timing | Low-power systems use a 32.768 kHz oscillator (1 s = 15-bit count) for RTC/sleep timing plus a more accurate crystal fast clock; discipline the slow clock: feed it to a capture timer, interrupt after 1 s of fast clock (e.g., 50 MHz), read captured ticks (e.g., 32,760 vs ideal 32,768) and use the ratio; fractional ambiguity and jitter limit accuracy to no better than the best clock; redo periodically because the error is temperature dependent; with GPS, interrupt on PPS, count ticks since last PPS, adjust | ratio = ticks_captured / 32,768 | fast/slow clocks | RTC/timekeeping | measure | p.363–364 | high |
| WHITE-211 | power | Sleep-mode ladder (decreasing power, increasing wake latency): slow-down (clock to hundreds of Hz) → idle/sleep (core off; timers, peripherals, RAM alive; any interrupt wakes) → deep sleep (peripherals selectively off — never the one that must wake you) → deep hibernation/power-down (RAM unstable, registers kept; only wake pin or a few interrupts) → power off (clean restart); choose the deepest mode whose wake latency meets the product need; wake sources: buttons, timers, other chips (ADC done), bus traffic | latency_wake(mode) ≤ t_response_req | user manual | low power | review | p.365 | high |
| WHITE-212 | firmware | Interrupt-based low-power main loop: ISRs set a bit in a volatile cause word and keep the CPU awake; main reads the cause word atomically (interrupts off), dispatches handlers that clear their bits, feeds the watchdog while awake, then re-checks with interrupts off and sleeps only when cause == 0. MSP430 G2231 Launchpad measurement: busy-wait 9 mW (3 mA @ 3 V); sleep mode 3 ≈ 0.9 µA (2.7 µW) per datasheet — 100 Ω shunt read 300 mV at 3 mA but nothing in sleep (would need ≈ 100 kΩ or a profiler). Try it first with a ≈ 2 Hz LED-toggle timer | — | — | low power | measure | p.366–368 | high |
| WHITE-213 | firmware | Choosing the sleep level at runtime: a power-management module holds a table of registered callbacks; every module that can preclude a sleep level (busy peripheral, active bus) can veto; the deepest un-vetoed level is entered | — | module states | multi-level sleep | review | p.369 | high |
| WHITE-214 | firmware | Watchdog vs sleep: decide whether the watchdog runs during sleep (power + forced wake-ups) or sleeps with the processor (loses fail-safe); if it runs, program a timer wake-up before it expires — the accepted exception to "never service from a timer", because here it also proves wake-up works; deep sleep usually disables internal watchdogs automatically | t_wake_timer < T_wdt | WDT config | low power | inspect | p.369 | high |
| WHITE-215 | power | Wake-up overhead scales with sleep depth: avoid frequent wake-ups; piggyback low-priority housekeeping on other wake-ups and skip timer wake-ups when nothing is due; chained processors — a tiny MCU triages buttons/alarms/low-battery and wakes the larger (OS) processor only when needed | — | wake rate | low power | review | p.369–370 | high |
| WHITE-216 | components | Motor selection by type: stepper — precise open-loop positioning, high holding torque, multiple I/O lines with commutation pattern, expensive, jerky, high current when holding; brushed DC — cheap, 1 I/O (2 for reverse), speed ∝ voltage (PWM), torque ∝ current, needs feedback for position, high start/stall current; brushless — longer life, quiet, efficient, several I/O, priced between; linear motors; "servo" = any motor + feedback controller (hobby/RC servos: 2 power + 1 control wire with potentiometer feedback); define torque, speed, accuracy, precision, cost, life-span and control mechanism before choosing | — | requirements | motors | review | p.374–375, p.385–387 | high |
| WHITE-217 | hw-fw | Position sensing: a home sensor gives one absolute reference (usually at an end of travel, sometimes center) — home by moving slowly toward it until the edge is sensed, then count relative moves (stepper steps or optical encoder pulses via the processor counter/timer capture); a 3-track rotary encoder → 3 GPIOs → 8 positions per turn (1/8-turn resolution); add limit switches where the motor may run away or fail | positions = 2^tracks | mechanics | motion | inspect | p.375–376, p.381 | high |
| WHITE-218 | protection | Never connect a processor GPIO/PWM directly to a motor: drive through a transistor (FET/BJT) from a higher-current supply; H-bridge for reversal (includes snubber diodes); a linear regulator cannot sink current — a snubber/flyback diode is required for a directly-driven DC motor or the reverse current spikes the voltage; FET switching delays in bridges can crowbar (shoot-through); keep the motor supply separate from the processor supply with lots of decoupling — inrush/torque current sags the rail and resets or hard-faults the processor, worst on low batteries | motor supply ≠ MCU supply; flyback path present | schematic | motors | inspect | p.376–377, p.385–386 | high |
| WHITE-219 | power | Motor supply sizing heuristic: the supply must source and sink 3× the maximum normal full-load current; steppers draw high current holding position, DC motors at start and stall; a single small motor ≈ 1 A (like 200 LEDs at 5 mA) so motors dominate the power budget; system current is additive (3 mA processor + 2 A motor = 2.003 A); measure with a bench supply; a stall test gives max current but damages motors — do it rarely; driver chips get hot (self-desoldering indicates a circuit-design problem) | I_supply ≥ 3 × I_full_load (source and sink) | motor datasheet/measurement | motors | calc | p.377–378, p.385 | high |
| WHITE-220 | control-loop | Motion profiles: jerk = d(accel)/dt causes vibration and wear — change acceleration smoothly; triangular profile (max accel then max decel) is fastest but hard on parts; trapezoidal is gentler and slower; S-curve minimizes jerk and lands between them in time depending on max speed; profiles are velocity-vs-time because speed (voltage) is easier to control than position; use the vendor's motor-control library for point-to-point moves | — | accel limits | motion | review | p.378, p.382–384 | high |
| WHITE-221 | control-loop | PID position control: error = setpoint − measured; P = Kp·e (too much → oscillation/ringing, too little → steady-state error), I = Ki·Σe (removes steady-state error, causes overshoot — too much can smash the mechanism), D = Kd·(e − e_prev) (damps; noisy error makes it erratic → average the error over several samples at the cost of responsiveness); output → PWM duty (example driver divides output by 2); tune P first, then D for overshoot, then I for residual error; Ziegler–Nichols as a starting method; sanity-check commands (e.g., negative PWM) and disable non-essential interrupts (debug UART) during control | u = Kp·e + Ki·Σe + Kd·Δe | gains, sample rate | feedback control | measure | p.379–381, p.386 | high |
| WHITE-222 | control-loop | Open-loop (feed-forward) control suffices for steppers (known step size, count steps); closed-loop is needed to stop DC motors at a position without bang-bang overshoot; feedback systems can be unstable — include limit switches and a human-safety stop philosophy; bring up motor systems from the lowest level (twitch) before profiles | — | — | motion | review | p.379, p.386 | high |

## 2. Formulas & tables (numbers)

### 2.1 Core formulas (plain ASCII)

| # | Formula | Symbols / units | Source |
|---|---|---|---|
| F1 | `f_int = f_clk / (P * C)` | f_int interrupt frequency (Hz); f_clk timer input clock (Hz); P prescaler (integer, ≤ 2^bits_P − 1); C compare/match value (integer, ≤ 2^bits_C − 1) | p.114 |
| F2 | `err_pct = 100 * abs(f_goal - f_actual) / f_goal` | percent | p.117–118 |
| F3 | `P_min = ceil(f_clk / (f_goal * C_max))`; `P_max = f_clk / (f_goal * 1)` clipped to register max; for P in [P_min, P_max]: `C = round(f_clk / (f_goal * P))` → pick min err | brute-force timer solver | p.117–118 |
| F4 | `C_implicit = 2^bits - 1` for overflow-only timers | — | p.114 |
| F5 | `t_response ≈ N * T_sample` (debounce), with `N * T_sample ≥ t_bounce` | N consecutive samples; T_sample poll period (s); t_bounce switch ring time (s) | p.106–107 |
| F6 | `t_rollover = 2^bits * T_tick` (uint16 @ 1 ms → 65.5 s; uint32 → 4,294,967,296 ms ≈ 49.7 days; uint64 ≈ 0.58e9 years) | bits of tick counter; T_tick (s) | p.145 |
| F7 | `TimePassed(since) = now >= since ? now - since : now + (1 + TIME_MAX - since)` | rollover-safe elapsed time | p.145 |
| F8 | `t_sys_latency = t_proc_latency + max(t_interrupts_disabled)` | cycles or s | p.130–131 |
| F9 | `overhead_frac = f_int * N_latency / f_cpu` (100 Hz·10/100 Hz = 10 %; 44,100·10/30e6 = 1.47 %) | f_int (Hz), N_latency (cycles), f_cpu (Hz) | p.131 |
| F10 | `cpu_frac_ISR = f_int * N_ISR / f_cpu` (44,100 × 335 / 30e6 = 0.492) | N_ISR total ISR cycles | p.131 |
| F11 | `bytes_per_s_UART ≈ baud / 10` (8N1) | baud (bit/s) | p.185 |
| F12 | `bytes_per_s_SPI = f_SCK / 8` (8 MHz → 1 MB/s) | f_SCK (Hz) | p.188 |
| F13 | `f_timer_bitbang = 4 * f_bit` (2 MHz SPI → 8 MHz timer; 32 interrupts/byte) | — | p.189 |
| F14 | `N_FIFO_trigger ≥ ceil(t_int_latency / t_byte)`, `t_byte = 8 / f_SCK` (10 MHz → 0.8 µs/byte; 3 µs → 3.75 → 4 bytes) | — | p.198 |
| F15 | `f_int_DMA = bytes_per_s / buffer_bytes` (125 kB/s / 15 kB ≈ 8 /s) | — | p.202 |
| F16 | `len = (write - read) & (size - 1)` (size = 2^n circular buffer) | — | p.205 |
| F17 | `lines_rowcol = M + N` for M×N keys; `keys_charlie = N^2 - N` for N pins | — | p.211–212 |
| F18 | `font_bytes = chars * H * W * bpp / 8` (94·8·6·8 = 36,096 bit = 4,512 B) | — | p.222 |
| F19 | `frame_bytes = W * H * bpp / 8` (240·320·24/8 = 225 KB; 320·480 color = 450 KB) | — | p.191, p.217 |
| F20 | `t_update = pixels * bpp * max(t_bit_bus, t_bit_display)` | — | p.222 |
| F21 | `N_buf ≥ f_sample * t_erase_max` (20 kHz × 25 ms = 500 samples) | — | p.225 |
| F22 | `life_s = endurance_cycles / write_rate` (10,000 / (1/s) = 10,000 s = 16.7 min → "< 20 min") | — | p.224 |
| F23 | `BW_Bps = f_s * channels * bits / 8` (44,100·4·16/8 = 352,800 B/s); `f_SPI_min = BW_Bps * 8` (= 2.8 MHz); `snippet = BW * t` (4 s → 1.3 MB) | — | p.236–237 |
| F24 | `checksum8 = sum(bytes) mod 256` ({10,20,40,60,80,90} → 300 → 44); `P_undetected ≈ 1/256` | — | p.269 |
| F25 | `err_pct(sum_1_to_N) = N*(N+1)/2`; output bits ≈ 2 × input bits | — | p.353 |
| F26 | `y = (x * m) >> s ≈ x / k` with `m/2^s ≈ 1/k`; error halves per +1 in s | Table 12-1 | p.335–336 |
| F27 | `index = (x - (base - step/2)) >> log2(step)` (centered LUT lookup) | — | p.340 |
| F28 | `y = p0.y + ((x - p0.x) * (p1.y - p0.y)) / (p1.x - p0.x)` (32-bit intermediate) | — | p.342 |
| F29 | `value = num / 2^shift` (fixed point); add: align shifts, add, normalize; mul: `tmp64 = a.num * b.num`, `shift = a.shift + b.shift`, normalize; div: divide nums, subtract shifts | — | p.346–350 |
| F30 | `sigma^2 = (1/N) * sum((x_i - x_mean)^2) = (1/N) * sum(x_i^2) - x_mean^2`; Welford: `delta = x - mean; n++; mean += delta/n; M2 += delta*(x - mean); var = M2/n` | — | p.330–331 |
| F31 | Horner: `A*x^3 + B*x^2 + C*x = ((A*x + B)*x + C)*x`; `sin x ≈ x*(1 - x^2*(1/3! - x^2*(1/5! - x^2/7!)))` | radians | p.333–334 |
| F32 | `P = I^2 * R`; `P = V * I`; `V = I * R`; `E = P * t` | W, A, Ω, V, J, s | p.356 |
| F33 | `I = V_shunt / R_shunt` | A, V, Ω | p.358 |
| F34 | `t_battery_h = C_mAh / I_mA` (3,000 mAh / 30 mA = 100 h) | valid only for I ≪ C/1h | p.360 |
| F35 | `I_avg = sum_states(I_state * t_state) / sum(t_state)` | mA | p.361 |
| F36 | `ratio_32k = ticks_captured_per_1s / 32768` (e.g., 32,760/32,768) | clock disciplining | p.364 |
| F37 | `I_motor_supply ≥ 3 * I_full_load` (source and sink) | A | p.385 |
| F38 | PID: `e = SP - PV; u = Kp*e + Ki*sum(e) + Kd*(e - e_prev)` | — | p.379–380 |
| F39 | `v = d/t; a = v/t; F = m*a; jerk = da/dt` | SI | p.378 |
| F40 | `cost_per_hour ≈ salary_per_year / 1000` | currency | p.355 |

### 2.2 Powers of two (sidebar, p.114–115)

| Bits | 2^bits | Max unsigned value | Significance |
|---|---|---|---|
| 4 | 16 | 15 | nibble |
| 7 | 128 | 127 | signed 8-bit max (min −128) |
| 8 | 256 | 255 | byte / uint8 |
| 10 | 1,024 | 1,023 | many 10-bit peripherals (ADC, prescaler) |
| 12 | 4,096 | 4,095 | many 12-bit peripherals |
| 15 | 32,768 | 32,767 | signed 16-bit |
| 16 | 65,536 | 65,535 | uint16 |
| 24 | 16,777,216 | — | 24-bit color (book prints "~1.6 million"; exact value is 16,777,216) |
| 31 | 2,147,483,648 | ~2 billion | signed 32-bit |
| 32 | 4,294,967,296 | ~4 billion | uint32 |

### 2.3 Communication bus comparison (Ch.7, p.181–194)

| Bus | Wires (excl. GND/power) | Clock | Duplex / topology | Speed | Reach | Notes |
|---|---|---|---|---|---|---|
| TTL UART | TX, RX (cross-connected) | implicit (async), both sides preset baud/parity/stop/flow | full duplex, point-to-point, symmetric | 2,400–115,200 baud typical (to 921,600); popular 9,600/19,200/115,200; ≈ baud/10 B/s; ≈ 20 % overhead | short (board/cable) | levels = processor I/O voltage (0–5, 0–3, 0–1.8 V); default 8N1 no flow; cable must match voltage |
| RS-232 | TX, RX (+ up to 8 signals) | implicit | full duplex, DTE (controller)/DCE | as UART | 50 ft (15 m) normal cable; ≈ 20× with low-capacitance cable | ±12 V; RTS/CTS for modems |
| SPI | MISO, MOSI, SCK, CS×n | explicit, from controller | full duplex, asymmetric, one CS per peripheral | tens of Hz … 100 MHz; B/s = f/8 (8 MHz → 1 MB/s) | usually on-board only | clock need not be exact; CPOL/CPHA per peripheral; send 0xFF to clock data out; some parts don't share a bus |
| Dual/Quad SPI | 2 / 4 data lines | explicit | half-duplex phases | 2× / 4× SPI | on-board | data lines switch direction per operation |
| I2C / TWI | SDA, SCL | explicit, from controller (multi-controller allowed) | half duplex, multipoint, 7-bit address | 10 kb/s (low-speed), 100 kb/s (standard, ≈ 12.5 KB/s bulk), 400 kb/s, 1 Mb/s, 3.4 Mb/s | a few meters (more with transceivers) | node count limited by addresses and bus capacitance; address LSBs by pull-ups; needs driver state machine |
| 1-Wire | 1 data (+ optional parasitic power) | implicit 16.3 kb/s | half duplex, multipoint | 16.3 kb/s | 10 m (100 m special cable) | temp sensors, authentication chips |
| Parallel (8/16-bit) | data bus + RD/WR/CS | control lines act as clock | half duplex | e.g., 13 MB/s needed for 320×480 @ 30 Hz → 13 Mb/s per line on 8-bit bus | on-board | data bits on one I/O bank |
| USB | differential pair (+ power) | implicit | full or half by version; host/device; ≤ 127 devices | 1.5 / 12 / 480 / 4,000 Mb/s | 5 m | needs protocol stack; do not bit-bang |
| RS-485 | differential | implicit 100 kHz–10 MHz | full or half; usually a controller | — | long distance | only physical + data-link layers specified |
| ISO-7816 smart card | contact interface | controller clock 1–5 MHz | half duplex, point-to-point, asymmetric | — | contact | 4+ OSI layers ⇒ ≥ 3× driver effort |
| Ethernet 100 Mb | — | — | — | ≈ 11 MB/s | — | implies OS/stack; TCP reliable, UDP simpler |

### 2.4 OSI model as used in embedded (Table 7-1, p.187)

| Layer | Function | Embedded question | PC Ethernet example |
|---|---|---|---|
| 1 Physical | electrical/physical spec | how many wires, what voltage, what speed | cable |
| 2 Data link | how bytes flow over wires | parity? bits per frame? | Ethernet 802.xx |
| 3 Network | packets from place to place | addressing; splitting/re-forming blocks | IP |
| 4 Transport | reliable blocks larger than lower layers | error recovery, guaranteed delivery | TCP |
| 5 Session | connection management | how data is sent here to there | sockets |
| 6 Presentation | data structure/encryption | how data is organized | TLS/SSL |
| 7 Application | user request → communication | which command on a button press | HTTP |

### 2.5 Interrupt overhead vs buffering scheme (Table 7-2, p.203; 1 MHz SPI, 8-bit transfers, 10-cycle interrupt overhead)

| Scheme | Interrupt-overhead cycles per second | × faster than bit-bang | Interrupt rate / slack |
|---|---|---|---|
| Bit-bang | 40 million | 1 | 4 interrupts per bit |
| Hardware SPI, byte interrupt | 1.25 million | 32 | 125 kHz, every 8 µs |
| 16-byte FIFO, interrupt at half | 156 thousand | 256 | 15.6 kHz, 64 µs slack (full-FIFO trigger: 7.8 kHz but only 8 µs slack) |
| DMA, 512-byte buffer | 2.44 thousand | 16,384 | — |

### 2.6 Flash / NVM numbers

| Parameter | Value | Source |
|---|---|---|
| MX25V8035 sector | 4 KB (4,096 B); device 8 Mb = 1 MB = 256 sectors | p.73 |
| Typical NOR endurance | often 100,000 erase/write cycles; some flash ≈ 10,000 | p.73, p.224 |
| Sector erase time | tens of ms (example max 25 ms) | p.225 |
| Erase vs write vs read | erase ≫ write ≫ read | p.239 |
| KV store minimum | 2 flash blocks | p.224 |
| Modification-list sectors | 2 | p.227 |
| Metadata overhead budget | ≈ 10 % starting number | p.226 |
| Sticky-bit signature | 0x55 read back as 0x57 | p.224 |
| EEPROM vs flash | EEPROM byte-erasable, smaller, more expensive, slower, higher endurance | p.223 |

### 2.7 Display / asset sizing (p.216–222)

| Item | Value |
|---|---|
| 8×8 mono glyph | 8 B; at 8 bpp 64 B |
| Full mono A–Z a–z 0–9 font (8 px) | ≈ 500 B; ≈ 4 KB at 8 bpp |
| 94 chars × 8 × 6 × 8 bpp | 36,096 bit = 4,512 B |
| 30×40 px chars, 94 chars, 16-bit color | 220 KB |
| 2.4-inch 240×320 24-bit screen | up to 225 KB per frame |
| 320×480 color frame | 450 KB; 30 Hz → ≈ 13 MB/s (105.5 Mb/s) |
| Glyph counts | 94 (English) + 94 (FR/IT/DE/ES) |
| Antialiasing 5 levels | 3 bpp |
| Asset flash growth reserve | ≥ 25 % |
| Segment refresh | > 30 Hz; 8×8 matrix → 16 lines, 1/8 duty |

### 2.8 Optimization scorecards (Ch.11)

Table 11-1 (bytes):

| Action | text | data | total | freed | total freed |
|---|---|---|---|---|---|
| Baseline | 31,949 | 324 | 32,273 (0x7E11) | — | — |
| Commented-out test code | 26,629 | 324 | 26,953 (0x6949) | 5,320 | (reverted) |
| Reimplemented abs() | 29,845 | 324 | 30,169 (0x75D9) | 2,104 | 2,104 |
| Const table computed at init | 29,885 | 244 | 30,129 (0x75B1) | 40 | 2,144 |

Table 11-2 (code-size delta vs baseline, bytes, min-of-three):

| Implementation | 1 call | 2 calls | 3 calls |
|---|---|---|---|
| Macro | 0 | 76 | 152 |
| Function (local or external) | 20 | 60 | 96 |
| Macro, size-optimized | −40 | 8 | 56 |
| Function, size-optimized | −40 | −20 | 0 |

Other Ch.11 numbers: first float add costs 532 B (p.346); signed long divide helper 0x20C B (p.288); stack allocation = 1.25 × measured high-water (p.297); stack fill pattern 0xDEADC0DE; red-zone patterns 0xDEADBEEF / 0xA5A5A5A5 (p.261); loop unroll 10 → 8 instructions per pixel (20 %) (p.315); function parameters < 4 (p.298).

### 2.9 Divide-by-constant approximations for 1/6 (Table 12-1, p.335–336)

| Multiplier | Divisor (2^s) | Shift s | Result | % error |
|---|---|---|---|---|
| 1 | 6 | none | 0.166666667 | 0 |
| 3 | 16 | 4 | 0.1875 | 12.5 |
| 5 | 32 | 5 | 0.15625 | 6.2 |
| 11 | 64 | 6 | 0.171875 | 3.1 |
| 21 | 128 | 7 | 0.164063 | 1.5 |
| 43 | 256 | 8 | 0.167969 | 0.78 |
| 85 | 512 | 9 | 0.166016 | 0.39 |
| 171 | 1,024 | 10 | 0.166992 | 0.19 |
| 341 | 2,048 | 11 | 0.166504 | 0.09 |
| 683 | 4,096 | 12 | 0.166748 | 0.04 |

### 2.10 Binary scaling of 12.345 (Table 12-2, p.347)

| Numerator | Numerator bits | Shift | Represented value | Error |
|---|---|---|---|---|
| 12 | 4 | 0 | 12 | 0.345 |
| 25 | 5 | 1 | 12.5 | 0.155 |
| 99 | 7 | 3 | 12.375 | 0.030 |
| 395 | 9 | 5 | 12.34375 | 0.00125 |
| 12,641 | 14 | 10 | 12.34472656 | 0.000273 |
| 12,944,671 | 24 | 20 | 12.34500027 | 2.67E−07 |
| 414,229,463 | 29 | 25 | 12.345 | 1.19E−09 |
| 1,656,917,852 | 31 | 27 | 12.345 | 1.19E−09 |

Taylor sine (p.334): 4 terms → error 0.000003 on −π…π; ±0.2π: 1 term for 10 %, 2 terms for < 1 %.

### 2.11 Current measurement with a series resistor (Table 13-1, p.359)

| Expected current | Resistor | Voltage on DMM | Readability |
|---|---|---|---|
| 12 mA | 1 Ω | 0.012 V | easy on most DMMs |
| 23 µA | 1 Ω | 0.000023 V | impossible on most DMMs |
| 34 µA | 10 Ω | 0.00034 V | very good DMM only |
| 45 µA | 100 Ω | 0.0045 V | most DMMs, but R getting too large (burden) |

MSP430 G2231 example (p.368): active busy-wait 3 mA @ 3 V = 9 mW (300 mV across 100 Ω); sleep level 3 ≈ 0.9 µA = 2.7 µW (needs ≈ 100 kΩ shunt or profiler).

### 2.12 Power budget constants (Ch.13)

| Item | Value | Source |
|---|---|---|
| Alkaline AA | 1.5 V nominal, ≈ 3,000 mAh | p.360 |
| Battery life examples | 30 mA → 100 h (~4 days); 300 mA → 10 h; 3,000 mA → < 1 h (nonlinear) | p.360 |
| Screen + processor example | 12 mA + 0.6 mA = 12.6 mA | p.361 |
| Sleeping processor | ≈ 80 µA class | p.361 |
| Low-power oscillator | 32.768 kHz (15-bit count = 1 s) | p.363 |
| Clock-vs-power | −10 % clock ≈ −10 % power | p.363 |
| Slow-down mode | clock to hundreds of Hz | p.365 |
| Engineer cost | salary/1000 per hour | p.355 |

### 2.13 Human/response/timing constants

| Item | Value | Source |
|---|---|---|
| UI response | > 250 ms sluggish; 100 ms noticeable; < 50 ms snappy | p.102 |
| Typing rate | 120 wpm × 5 chars = 10 keys/s → key down ≈ 50 ms | p.107 |
| Debounce example | bounce ≤ 12.5 ms; sample 10 ms (100 Hz); 5 consecutive (3 acceptable) | p.107 |
| LED PWM | hundreds of Hz (20 Hz visibly flashes) | p.120 |
| Segment display refresh | > 30 Hz | p.214 |
| System tick | 1 ms popular | p.143 |
| Interrupt latency example | 10 cycles "decent" | p.131 |
| Heart-rate window bound | ≤ 250 bpm | p.235 |
| Processor stats | STM32F103 (Cortex-M3) 32-bit 72 MHz; MSP430G2201 16-bit 16 MHz; ATtiny45 8-bit 4 MHz | p.111 |
| Hardware breakpoints | frequently only 2 | p.4 |
| DMM voltage spec | 0–20 V @ 0.1 V; 0–2 V @ 0.01 V | p.66 |
| Scope starting point | 100 ms/div, 2 V/div | p.69 |
| Timing-debug RAM buffer | 4–16 B | p.84 |
| Version field widths | major 1 B, minor 1 B, build 2 B | p.30 |
| Core-dump key | 0x0BADC04E | p.260 |
| Core-dump region example | 255 B (0xFF) at 0x017F00 | p.258 |

### 2.14 Sleep-mode ladder (p.365)

| Mode | What stays on | Wake source | Relative power / latency |
|---|---|---|---|
| Slow-down | everything, clock to 100s of Hz | — | highest power, no latency |
| Idle / sleep | timers, peripherals, RAM; core off | any interrupt | ↓ |
| Deep sleep / light hibernation | selected peripherals; core off | configured interrupt (keep its peripheral on) | ↓↓ |
| Deep hibernation / power down | registers only (RAM unstable) | wake pin or few interrupts | ↓↓↓ |
| Power off | nothing | power/reset | lowest, full re-init |

## 3. Mechanizable checks

Each check: inputs (columns, units) → formula → pass criterion → margin → source rows.

- `CHECK-input-default-level`: pin map [pin, direction, ext_pull (PU/PD/none), int_pull_enabled] → for every input: ext_pull ≠ none OR int_pull_enabled → pass if no floating input → margin = count of floating inputs (must be 0) → WHITE-030, WHITE-055.
- `CHECK-unused-io-config`: pin map [pin, connected (bool), config] → unused pins must be in {input+PD, hi-Z, output-low, input+PU} (preference order) → pass if all unused pins in set → margin = count of unused pins configured as output-high or peripheral → WHITE-208.
- `CHECK-no-drive-into-unpowered`: netlist [net, driver_domain, load_domain, load_can_be_unpowered] → any net from an always-on driver into a switchable/reset-held chip must be low or hi-Z when that domain is off → pass if no high-level/pull-up nets cross into an off domain → WHITE-208.
- `CHECK-internal-vs-external-pull`: pin map [pin, ext_pull, int_pull] → int_pull must equal ext_pull or be disabled → pass if no opposing pulls → margin = count of conflicts → WHITE-208.
- `CHECK-uart-crossover`: ICD [link, A.TX→B.pin, A.RX→B.pin, V_IO_A, V_IO_B] → A.TX connects to B.RX and A.RX to B.TX; V_IO_A == V_IO_B (or level shifter present) → pass/fail → WHITE-100.
- `CHECK-uart-settings`: ICD [baud, data bits, parity, stop, flow] → both ends identical; debug port 8N1 no flow; baud ∈ common set {2,400…921,600} → pass; report throughput ≈ baud/10 B/s → WHITE-101.
- `CHECK-i2c-bus`: bus table [bus, device, address7, speed_supported] → addresses unique per bus; bus speed = min(speed_supported) ∈ {10k,100k,400k,1M,3.4M}; pull-ups present on SDA and SCL → pass if unique and speed common → margin = address collisions (0), throughput headroom = bus_speed/8 − Σ demand → WHITE-105.
- `CHECK-spi-bus`: bus table [bus, device, has_CS, CPOL, CPHA, f_max] → one dedicated CS line per peripheral; f_SCK ≤ min(f_max); mode conflicts flagged (controller must reconfigure per device) → pass if CS unique and f_SCK ≤ min → margin = min(f_max)/f_SCK → WHITE-103.
- `CHECK-bus-bandwidth`: per bus [device, f_s (Hz), channels, bits, burst_s] → BW = Σ f_s·ch·bits/8 (nominal and worst case); f_bus_min = BW·8 (SPI) → pass if f_bus ≥ f_bus_min_worst → margin = f_bus/f_bus_min_worst − 1 (require > 0) → WHITE-139.
- `CHECK-debug-port-present`: connector list [refdes, type] → count(type == debug/SWD/JTAG) ≥ 1 AND count(type == power, pins ≥ 2) ≥ 1 → pass → WHITE-004, WHITE-029.
- `CHECK-programming-header`: connector list → count(type == programming/ICSP) ≥ 1, distinct from user I/O headers → pass → WHITE-031.
- `CHECK-test-points`: pin map [pin, function] → count(function == spare GPIO on header/test point) ≥ N_agreed (default ≥ 1; ≥ 4 recommended for I/O-line profiling of 4 stages) → pass; margin = count − N_agreed → WHITE-047, WHITE-108, WHITE-179.
- `CHECK-pwm-pin-capable`: pin map [pin, function=PWM, timer_channel_capable (bool)] → every PWM net lands on a timer/PWM-capable pin; every timer-driven output on a routable pin → pass if all true → WHITE-069.
- `CHECK-data-ready-on-exti`: sensor table [sensor, data_ready_pin, exti_capable] → each streaming sensor's data-ready/interrupt line goes to an interrupt-capable processor pin → pass → WHITE-112.
- `CHECK-nmi-documented`: pin map → if any pin routes to NMI, its function is documented and its handler exists → pass → WHITE-073.
- `CHECK-boot-straps-and-alt-functions`: pin map [pin, alt_functions, default_function, boot_strap (bool), strap_level] → every shared pin has default function and switch recorded; every boot-strap pin has a defined level at reset (pull) → pass if no undefined → WHITE-049, WHITE-030.
- `CHECK-watchdog-present`: firmware manifest [wdt_enabled, wdt_timeout_s, service_sites (count), service_in_isr (bool)] → wdt_enabled AND service_sites == 1 AND NOT service_in_isr → pass → WHITE-095.
- `CHECK-watchdog-timeout`: [wdt_timeout_s, Σ task_worst_case_s (one scheduler pass), boot/POST time] → wdt_timeout > Σ tasks (and > longest main-loop pass) → pass; margin = wdt_timeout/Σ − 1 → WHITE-091, WHITE-095.
- `CHECK-boot-log-contents`: boot log spec [fields] → contains firmware version (A.B.C 1+1+2 bytes), watchdog state, POST results retrievable later → pass → WHITE-009, WHITE-010, WHITE-036, WHITE-096.
- `CHECK-artifact-versions`: manifest [artifact (app, bootloader, EEPROM image, asset pack, OS, second core), has_version, checked_before_use] → all true; protocol has version field → pass → WHITE-011, WHITE-121, WHITE-158.
- `CHECK-update-path`: manifest [bootloader_separate, aux_image_storage, hash+signature verify, version compare, fallback_image_count, code_read_protection, wdt_off_in_debug] → bootloader separate AND verify AND fallback ≥ 1 → pass; margin = aux flash free after images → WHITE-161, WHITE-162, WHITE-164.
- `CHECK-timer-registers`: [f_clk, f_goal, bits_P, bits_C, tol_pct] → run F3 → pass if min err ≤ tol_pct; if P_min > 2^bits_P − 1 → FAIL "needs wider timer or software divide" → margin = tol − err → WHITE-064…068.
- `CHECK-tick-rollover`: [tick_bits, T_tick_s, longest_interval_measured_s] → 2^bits·T_tick > longest interval AND TimePassed is rollover-safe → pass → WHITE-090.
- `CHECK-isr-budget`: ISR table [f_int, N_latency, N_body] → Σ f_int·(N_latency + N_body)/f_cpu → pass if < budget (e.g., 50 %); also max single ISR cycles → system latency vs deadline → margin = budget − usage → WHITE-075…077.
- `CHECK-fifo-trigger`: [f_bus, bytes_per_transfer, t_int_latency_max, fifo_depth] → N_trig = ceil(t_lat·f_bus/8) → pass if N_trig ≤ fifo_depth/2 (half-trigger scheme) → margin = fifo_depth/2 − N_trig → WHITE-113.
- `CHECK-dma-buffer`: [bytes_per_s, buffer_bytes, RAM_total, variables_bytes] → 2·buffer + variables ≤ RAM; interrupt rate = bytes_per_s/buffer → pass if fits and rate acceptable → WHITE-114.
- `CHECK-circular-buffer`: [size] → size is power of two; index type atomic on target width → pass → WHITE-116, WHITE-117.
- `CHECK-flash-endurance`: [endurance_cycles, write_rate_per_s per address, product_life_s] → life = endurance/rate ≥ product_life (or wear-leveling present) → margin = life/product_life → WHITE-129.
- `CHECK-erase-buffer`: [f_sample, sample_bytes, t_erase_max] → N = f_s·t_erase → RAM_buf ≥ N·sample_bytes → pass → WHITE-130.
- `CHECK-datastore-size`: [rate, size, t_max_between_transfers, metadata_frac=0.10] → store ≥ rate·size·t·(1+meta) → pass; margin = flash_alloc/needed − 1 → WHITE-131.
- `CHECK-asset-flash`: [Σ assets_bytes, asset_flash_bytes] → asset_flash ≥ 1.25·Σ → margin = asset_flash/Σ − 1.25 → WHITE-124.
- `CHECK-frame-update`: [W, H, bpp, t_bit_bus, t_bit_display, f_refresh] → t_update = W·H·bpp·max(t_bit) ≤ 1/f_refresh → pass → WHITE-123.
- `CHECK-code-ram-margin`: map [text+rodata used, flash size, data+bss used, stack_alloc, heap, RAM size, reserve_frac] → used ≤ size·(1 − reserve) for both; heap == 0 unless justified → margin = free/size; reserve larger for regulated products → WHITE-169, WHITE-175, WHITE-184.
- `CHECK-stack-margin`: [stack_alloc, high_water_measured] → stack_alloc ≥ 1.25·high_water → margin = stack_alloc/high_water − 1.25 → WHITE-175.
- `CHECK-emc-threshold`: clock list [f_clk] → any f_clk > 9 kHz ⇒ EMC test required (FCC Part 15) and EMC test firmware build exists → pass if plan present → WHITE-136.
- `CHECK-battery-life`: [C_mAh, states {I_mA, t_frac}] → I_avg = Σ I·t; life_h = C/I_avg ≥ requirement (flag if any I_state > C/1h — linear rule invalid) → margin = life/req − 1 → WHITE-205, WHITE-206.
- `CHECK-shunt-selection`: [I_expected, DMM_V_resolution, V_supply] → V = I·R ≥ 10·resolution AND R·I ≪ V_supply (e.g., < 1 %) → pick R from {1, 10, 100, 100k Ω}; report burden → WHITE-204.
- `CHECK-motor-supply`: [I_full_load per motor, supply_source, supply_sink, flyback_present, separate_rail] → source ≥ 3·I AND sink ≥ 3·I (or H-bridge) AND flyback AND separate rail with decoupling → pass → WHITE-218, WHITE-219.
- `CHECK-fixed-point-precision`: [value_max, tolerance, numerator_bits] → shift = ceil(−log2(tolerance)); need bits = ceil(log2(value_max)) + shift + 1 ≤ numerator_bits → pass → WHITE-197.
- `CHECK-lut-range`: [x_min, x_max, base, step, N] → base ≤ x_min AND base + N·step ≥ x_max AND step power of two → pass; guard code required otherwise → WHITE-194.
- `CHECK-debounce`: [t_bounce_datasheet, t_response_req, T_sample, N] → N·T_sample ≥ t_bounce AND N·T_sample ≤ t_response_req AND T_sample ≤ t_response_req/3 → pass → WHITE-061, WHITE-062.
- `CHECK-ui-response`: [t_response_measured] → < 50 ms target, ≤ 100 ms acceptable, ≤ 250 ms hard limit → grade → WHITE-056.
- `CHECK-state-table-complete`: state table [state × event cells] → no empty cell (each has action or explicit ignore/log) → pass; margin = empty cells (0) → WHITE-094.
- `CHECK-shared-resource-arbitration`: block diagram [resource, users[]] → for count(users) ≥ 2 an arbitration mechanism is named → pass → WHITE-005.
- `CHECK-warnings-zero`: build log → warning count == 0 (excluding untouched vendor code) → pass → WHITE-142.
- `CHECK-ram-collision`: [ISR-shared globals declared volatile, modified under interrupts-off] → all true → pass → WHITE-058, WHITE-092.
- `CHECK-key-management`: [per_unit_keys (bool), key_store_protected, serial↔key tracking] → if per_unit_keys then both true → pass → WHITE-163.
- `CHECK-datasheet-currency`: BOM [part, datasheet_rev, part_rev, errata_checked] → all errata_checked true and datasheet rev matches part rev → pass → WHITE-022, WHITE-026.
- `CHECK-lead-time`: BOM [part, lead_time_weeks, need_date] → lead_time ≤ time-to-need for every part; flag candidates without price/lead-time data → WHITE-024.
- `CHECK-operating-range-vs-placement`: BOM [part, T_min, T_max, local_T_est] → local_T within range → pass → WHITE-025.
- `CHECK-spare-boards`: build plan [boards_to_firmware] → ≥ 3 → pass → WHITE-033.

## 4. Verification procedures & plots

| Property | Procedure / plot | Axes, sweep | "Good" looks like / pass | Notes | Source |
|---|---|---|---|---|---|
| Rails present before bring-up | EE powers PCBA first; DMM voltage on every rail test point | rail vs expected V | every rail within tolerance; no smoke; current draw sane | only then hand board to FW | p.44, p.66 |
| GPIO under software control | toggle each mapped pin from command line; DMM/scope | pin vs time | pin follows command; sink/source polarity (inverted logic) confirmed | check alt-function, clocks, watchdog off | p.72, p.95–96 |
| SPI link | send "UU3" (0x55 0x55 0x33) with CS trigger; logic analyzer/protocol decode | SCK, MOSI, MISO, CS vs time | decoded bytes match; CPOL/CPHA match datasheet timing diagram | reproduce datasheet timing diagram on scope | p.188, p.194–195 |
| Flash driver | 5-step read/erase/write-formulaic/verify/restore test at a spare sector; command-line invocable; returns error count | — | 0 errors on ≥ 3 boards | not in POST; watch endurance | p.73–75 |
| Debounce tuning | log raw pin samples at 100 Hz during presses; plot raw vs debounced | level vs time (ms) | one event per press; no chatter; response ≤ requirement | check batches of switches | p.105–107 |
| Timer accuracy | sweep prescaler P over [P_min, P_max], compute error (F2) | err % vs P | min error below tolerance; chosen (P, C) documented | brute-force script | p.117–118 |
| Interrupt overhead | measure ISR duration with test-point pin high inside ISR; scope | pin vs time | ISR width × rate ≤ CPU budget; system latency ≤ deadline | I/O-line profiler | p.131, p.304–305 |
| Throughput / bandwidth | speeds-and-feeds spreadsheet: per element input rate, buffer, output rate; verify on hardware by streaming at max rate | B/s per bus vs capacity | worst-case Σ ≤ capacity with margin; no wait-time collapse (Fig 11-4 pattern) | plot data-wait gap shrinking = about to miss data | p.236–238, p.304–305 |
| FIFO/DMA correctness | run continuous stream at target rate with half-full trigger; count under/overruns | overruns vs time | zero overruns over long soak | trigger level from F14 | p.198–202 |
| Stack usage | fill stack with 0xDEADC0DE at boot; exercise all features; read high-water | bytes used | alloc ≥ 1.25 × high-water | per task with RTOS | p.297, p.261 |
| Memory corruption | red zones 0xDEADBEEF/0xA5A5A5A5 between buffers; inspect after soak | — | patterns intact | vary stack size to change TTF | p.260–261 |
| Hard-fault capture | inject each fault class (div/0, NULL write, bad instruction, misaligned, stack overflow) from a test command; verify core dump key/cause/PC logged after reboot | — | every class produces a correct core dump; boot log shows cause | keep .map with release | p.248–260 |
| Code/RAM budget | map-file diff between builds; scorecard table | bytes per section vs build | totals under reserve line; every change attributed | script to parse .map | p.286–297 |
| Profiling hot spots | (a) I/O lines per stage on scope; (b) timer profiler ≥ 10 ticks per section; (c) sampling profiler at non-harmonic rate (e.g., 1.7 Hz) → histogram of return addresses via map | % time per function | dominant stage identified; after optimization, wait gap restored | check profiler overhead ≈ 0 | p.304–308 |
| Current profile | shunt (Table 13-1) or power profiler; scope current vs time through state transitions | I (µA/mA, log scale) vs time | active/sleep levels match budget spreadsheet; wake events short | debugger and console disconnected | p.357–360, p.368 |
| Battery life | I_avg from measured state currents × state times; compare to capacity | hours | ≥ requirement with margin; no state exceeding battery peak-current rating | validate linear rule | p.360–361 |
| Sleep correctness | 2 Hz timer-toggle experiment with and without sleep; current before/after | mA | large drop; LED still toggles; watchdog/wake timer behaviour verified | — | p.367–368 |
| Clock disciplining | capture 32 kHz ticks per 1 s of fast clock over temperature | ticks vs T (°C) | ratio stable enough for requirement; re-calibration interval chosen | GPS PPS if available | p.363–364 |
| EMC pre-scan | EMC test firmware build drives all comm paths at max rate; lab radiated scan and susceptibility | dBµV/m vs frequency | under limit at all frequencies | required if any clock > 9 kHz (US) | p.230 |
| Firmware update robustness | pull power at random points during download/programming; corrupt image; wrong signature; older version | — | device always boots a valid image (fallback); bad images erased; no brick | test early in project | p.273–279 |
| Motor bring-up | lowest level first: I/O twitch → PWM ramp → encoder count → homing → PID step response | position/velocity vs time (Fig 14-2 style) | homing repeatable; step response without sustained oscillation; overshoot within spec; supply rail no sag/reset | motor and MCU on separate rails; limit switches wired | p.45, p.376–384 |
| PID tuning | step set-point; plot PV, P/I/D terms, output | value vs time | P first (no ringing), then D (overshoot damped), then I (steady-state error → 0) | average error for D if noisy | p.380–381 |
| State machine coverage | table-driven tests: every (state, event) cell exercised in unit tests | pass/fail matrix | all cells handled; invalid events logged/ignored per table | — | p.161–164 |
| Manufacturing test | CM-run pass/fail (green/red) sequence: program, provision, POST, radio in Faraday cage | pass/fail | binary result, no debugging on the line | derived from bring-up tests | p.282 |

## 5. Pitfalls, failure modes, review checklist

- Board not powered / probe on wrong pin — check first, every time (p.95, p.243).
- TX/RX (or clock/data) not crossed — the most common hardware issue (p.184).
- USB-to-serial cable voltage doesn't match TTL level (p.184).
- Floating (hi-Z) inputs without pull-up/down (p.62).
- Shared pin still assigned to its alternate peripheral (SPI vs GPIO) (p.93, p.95).
- I/O subsystem clock not enabled; delay loops too fast to see (p.96).
- LED wired to sink (cathode on pin) → inverted logic; pin cannot source enough current (p.96).
- Running yesterday's binary — bump the version string to prove the load (p.96, p.243).
- Wrong target processor in build; watchdog resetting during debug; interrupts/asserts interfering (p.96, p.165).
- Hardware breakpoints limited (often 2) when running from flash (p.4).
- Register read-modify-write not atomic → lost bits when an interrupt intervenes (p.94, p.136).
- Write-only registers read back as status → need shadow variables (p.136).
- Stopping at the first pending cause bit — multiple sources may be pending (p.137).
- Nested critical sections re-enabling interrupts early (p.138–139).
- Enabling an interrupt before its ISR/vector is installed → crash (p.132, p.140).
- Only peripheral-level OR only NVIC-level interrupt enabled (needs both) (p.141).
- Missing `volatile` on ISR-shared globals/registers: works at −O0, fails optimized (p.104, p.245).
- printf/malloc/I/O calls inside ISRs (nonreentrant) (p.134–135).
- Copying data inside ISRs (long ISR → latency, missed interrupts) (p.171).
- Debug output interrupt preempting a higher-priority handler (priority inversion) (p.155).
- Polling without timeout (p.143).
- DelayMs fencepost (+1 tick) and jitter; unsafe for 1 ms accuracy (p.144).
- Tick counter rollover (uint16 = 65.5 s; uint32 = 49.7 days) breaking time comparisons (p.145).
- Servicing the watchdog from a timer interrupt or DelayMs — defeats it (p.165).
- Watchdog timeout shorter than one full cooperative scheduler pass (p.173).
- Shipping without a boot message that the watchdog is enabled (p.165).
- Unhandled-interrupt default handler that hangs production units (p.132).
- Debouncing by interrupt on a bouncy line → glitch storms/instability (p.105).
- Switch bounce differing between batches; not consulting switch datasheet (p.106).
- Interrupting on button level instead of release edge → repeat activations (p.104).
- Internal RC oscillator drift breaking comms/real-time (p.112).
- Timer registers zero-based (divide-by-2 = write 1) (p.112).
- Division needed exceeds timer×prescaler range (p.119).
- LED PWM at 20 Hz visibly flickers (p.120).
- Two subsystems sharing a bus/driver without arbitration (p.15, p.18).
- Circular buffer index update not atomic on narrow CPUs; read/write pointers crossing; modulo in ISR (p.204–207).
- Bit-banging a bus when a hardware peripheral exists (16,000× overhead vs DMA) (p.202–203).
- FIFO interrupt on "full" leaves only one byte-time to respond (p.202).
- Mb vs MB confusion in memory sizing (p.239).
- Flash written every second at one address dies in < 20 min (p.224).
- Flash write during a sector erase (tens of ms) with no RAM buffer → lost samples (p.225).
- Power loss mid-erase/mid-write without modification list/checksums; duplicate data after reset (p.227).
- Using a ms tick counter as a timestamp (49 days) (p.226).
- Local time instead of UTC; DST/time-zone surprises in the field (p.226, p.280).
- Sticky bits on worn flash (0x55 → 0x57) unmarked (p.224).
- Unversioned asset packs or EEPROM images → garbage on screen / misparsed data (p.30, p.215).
- Display asset flash with no growth reserve (< 25 %) (p.222).
- Tearing from unsynchronized frame updates (p.217).
- Multiplexed LCD segments wash out at low duty; refresh < 30 Hz flickers (p.214).
- Multiple simultaneous key presses misread in matrices (p.213).
- Analog signal wires acting as antennas; no shielding; "all sensors are temperature sensors" (p.229–230).
- Skipping EMC planning for any clock > 9 kHz (p.230).
- Integer division of similar magnitudes (rolling-average shortcut) yields junk (p.328).
- Pre-scaled fixed point breaking when the input range changes by 10 % (p.329).
- Sum-of-squares overflow (16-bit samples need 64-bit accumulator) (p.331).
- Welford mean truncating to zero for small deltas; statement-order dependence (p.332).
- Modulo by non-power-of-two (hidden divide) in hot loops (p.324).
- `const` variables not treated as compile-time constants; use `#define` (p.325).
- Floating point on FPU-less parts (532 B for one add; printf pulls float libs) (p.346).
- LUT index out of range (2π on a −π…π table) → wrong result or crash (p.340).
- LUT bins not centered (half-step) → systematic offset (p.339–340).
- Fixed-point shift-difference overflow; forgetting to promote before multiplying (p.348–350).
- malloc fragmentation (25 free bytes, no contiguous 20) and invisibility in map (p.295).
- Stack sized without high-water measurement; recursion (p.297, p.301).
- Returning pointers to stack memory; using freed heap memory (p.252–253).
- Unbounded input copy → stack smash / hijacked return address (p.253–254).
- Divide-by-zero silently returns 0 on Cortex-M unless CCR traps it (p.248).
- Unaligned 32-bit access into byte arrays (p.251).
- Core dump placed in normal globals/stack/heap (wiped or corrupt); no valid-key; not cleared after logging (p.256–260).
- Releasing binaries without archiving the .map (p.260).
- Ignoring compiler warnings (assignment in condition, uninitialized use, address of local returned) (p.244, p.261).
- Optimization "fixed" by making variables global — hidden, not solved (p.260).
- Debug strings filling code space (p.294).
- Function chains pushing registers to stack; > 4 parameters; narrow locals on wide CPUs (p.298–301).
- Signed/unsigned comparison promoting negatives to huge values (p.310).
- RAM overlays without documentation → subsystems silently exclusive (p.303).
- Optimizing init code instead of the loop; tuning left to the end of the project (p.304, p.320).
- No spare resources at ship for bug fixes (regulated products need more) (p.319).
- Building your own radio, crypto algorithm, KV store, malloc, or libc when proven ones exist (p.224, p.265, p.271, p.296).
- 2.4 GHz link that works in winter and fails when leaves grow (p.265).
- Protocol without version field; checksum instead of CRC on bursty channels; 8-bit checksum on large data (p.269).
- Keys leaked via email/repo — weakest link is key handling (p.271).
- Firmware update developed last; no fallback image; network code inside the bootloader; no staged rollout (p.273–279).
- Code-read protection preventing sector erase — update design must account for it (p.275).
- Same key on every unit when the product is a target (p.277).
- Manufacturing test returning numbers instead of pass/fail; radio test without Faraday cage; BLE updates on a noisy line (p.282).
- Debugger/JTAG or serial console attached while measuring current (p.357).
- DMM current range wrong (reads zero or blows fuse); shunt burden voltage; not measuring the actual shunt value (p.358–359).
- Fighting external pull resistors with internal ones; driving high into an unpowered chip (p.362–363).
- Turning off the peripheral that generates the wake interrupt in deep sleep (p.365).
- Frequent wake-ups; watchdog left running in sleep without a wake timer (p.369).
- Motor on the processor rail → brownout resets/hard faults; GPIO driving a motor directly; no flyback diode with a linear regulator; H-bridge shoot-through (p.377, p.385–386).
- Supply that cannot sink current or supply < 3× full-load (p.385).
- Unchecked negative PWM or debug-UART interrupt during motor control → blown FETs (p.385–386).
- Too much P (ringing) or I (overshoot smashing hardware); noisy D term (p.380–381).
- No home sensor / limit switches; relative encoder without homing (p.375, p.381).
- Triangular motion profile (max jerk) shortening mechanism life (p.382).

## 6. Standards referenced

| Standard / document | Edition / date | Clause / table | Governs | Page |
|---|---|---|---|---|
| FCC Part 15 (US) | — | — | EMC radiated-emissions testing required for any system with a clock > 9 kHz | p.230 |
| ISO-7816 | — | — | contact smart-card interface: half-duplex, point-to-point, asymmetric, controller clock 1–5 MHz, ≥ 4 OSI layers | p.194 |
| RS-232 | — | — | ±12 V serial, 8 signals + ground, 50 ft (15 m) typical, DTE/DCE | p.185–186 |
| RS-485 | — | — | differential long-distance serial, 100 kHz–10 MHz implicit clock, physical + data-link only | p.194 |
| I2C (inter-integrated circuit) / TWI | — | — | 7-bit addressing, standard 100 kb/s, low-speed 10 kb/s, fast 400 kb/s, 1 Mb/s, 3.4 Mb/s | p.189–190 |
| USB (versions) | — | — | 1.5 / 12 / 480 / 4,000 Mb/s, 127 devices, 5 m | p.193 |
| OSI model (ISO/IEC 7498) | — | Table 7-1 | seven-layer communication model | p.186–187 |
| POSIX/Unix driver model | — | — | open/close/read/write/ioctl (+select/poll, mmap) driver interface | p.23–25 |
| ASCII | — | — | 7-bit character encoding ('0'=0x30, 'A'=0x41, 'a'=0x61); Unicode for internationalization | p.194–195 |
| Semantic versioning | — | — | A.B.C version scheme (1+1+2 bytes recommended) | p.30 |
| STM32F101xx–107xx Reference Manual RM0008 | Rev 21, Feb 2021 | GPIO, TIM, NVIC registers | example register interfaces | p.123 |
| MSP430F2xx/G2xx Family User's Guide SLAU144K | Aug 2022 | P1DIR/P1OUT | example register interfaces | p.123 |
| Atmel ATtiny25/45/85 datasheet Rev. 2586Q–AVR–08/2013; AVR130 (timers); AVR035 (efficient C for AVR) | 2013 | timers, DDRB/PORTB | timer math example, optimization | p.123, p.320 |
| STMicroelectronics AN1447 | — | — | driving LCD segments by matrix (AC drive) | p.214 |
| Macronix MX25V8035 datasheet | — | — | flash geometry for test example (4 KB sector, 8 Mb) | p.72–73 |
| Arm Cortex-M (CMSIS-DSP, CMSIS-NN); Interrupt Blog "How to Debug a HardFault"; Embedded Artistry LibC | — | — | hard-fault handling, DSP/ML libraries, reduced libc | p.255, p.291, p.352 |
| Kerckhoffs's principle | — | — | cryptosystem security must not depend on algorithm secrecy | p.271 |
| Ziegler–Nichols method | — | — | PID tuning starting point | p.381 |
| Google Style Guides; C4 model; 4+1 view model; UML | — | — | coding style, architecture documentation | p.24, p.39, p.219 |

## 7. Process / lifecycle guidance

| Stage | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| Concept | High-level product design (features, cost, time to market); schedule with dependencies; identify parallel vs post-hardware tasks | schedule (Fig 3-1), dependency list | HW/FW dependencies identified; ship date not a simple sum | p.41–43 |
| Architecture | Context, block, organigram and layering diagrams; identify shared resources, hardware abstraction layers, sandbox | four sketches; interface list; version scheme; logging/error interfaces | shared resources have arbitration; interfaces describable in a few sentences | p.13–38 |
| Component selection | Datasheet triage (abs-max/electrical → typical → applications → mental prototype); dev kits for processor and riskiest peripherals; check price, lead time, family headroom, errata | must/want lists; 2–4 candidates per part; dev-kit bring-up | candidates meet electrical/mechanical/environment; lead times within schedule | p.43, p.53–58 |
| Schematic | Schematic capture with comments ("Processor I/Os"); I/O map (CSV → header); BOM with exact orderable parts; test points and spare I/Os; debug, power, programming connectors; schematic review | PDF schematic, I/O map, BOM | schematic review passed before layout; FW asked how many test points | p.43–44, p.60, p.84 |
| Layout / fab / assembly | Layout (often a specialist); fab; kitting (long-lead parts); PCBA | PCBAs (≥ 3 for FW) | bare-board continuity passed; kits complete | p.44, p.65 |
| Pre-hardware firmware | Toolchain, debugger, debug subsystem (logging, errors, version, command line), drivers for known peripherals, sandbox algorithms, hardware tests prioritized by EE risk | HW-test firmware, command handler, unit tests | tests run on dev kit; each component individually testable | p.43–46, p.70–80 |
| Board bring-up | EE first power-on; then lowest-level tests in smallest steps (GPIO → bus → device → subsystem); watchdog off; multiple boards; reproducible tools; POST/unit/bring-up test triage | bring-up log, working drivers, updated errata list | all subsystems verified on ≥ 2 boards; tests checked in | p.44–46, p.70–75, p.165 |
| Development | Main-loop pattern chosen; state machines tabulated; speeds-and-feeds spreadsheet; resource scorecards maintained continuously; firmware update path developed early; EMC test build | speeds-and-feeds sheet; scorecards; update mechanism; core-dump support | resources within budget with reserve; update tested against power loss | p.166–177, p.236–238, p.273–275, p.290, p.320 |
| Pre-ship | Prune prototype code; tag VCS; unit tests before release; watchdog on with boot message; archive binaries + .map; POST defined; security risk analysis | release build, .map, test report | POST passes; watchdog verified; margins retained (larger for medical/safety) | p.122–123, p.165, p.260, p.271–272, p.319 |
| Manufacturing | CM test firmware (pass/fail); multi-unit programming; provisioning (keys, cloud); asset-flash programming; Faraday cage for radio test | manufacturing test spec, provisioning procedure | green/red result per unit; keys tracked per serial | p.223, p.277, p.282 |
| Deployment / sustaining | Staged rollout (desk → team → company → customer groups); device-health telemetry (boot cause, voltage, heartbeats); crash statistics; fallback image; per-group update server | rollout plan, dashboard, fleet stats | no crash-rate/battery regression before widening rollout | p.278–281 |

## 8. Coverage log

- Source: `Elecia_White_Making_Embedded_Systems_Design_Patterns_for_Gre.txt`, 6,056 lines, 864,333 bytes. Whole file assigned; whole file read in order.
- Lines 1–300: front matter, copyright, TOC (read via numbered `awk` dump).
- Lines 300–1,300: rest of TOC, Preface, Ch.1, start of Ch.2 (Bash dump exceeded the display cap and was persisted; the persisted file was read in full).
- Lines 1,301–6,056: read with the Read tool in ≤ 300-line chunks; one 300-line chunk (1,301–1,600) exceeded the token cap and was re-read as two 150-line chunks. Chunk boundaries: 1301–1450, 1451–1600, 1601–1900, 1901–2200, 2201–2400, 2401–2600, 2601–2800, 2801–3000, 3001–3200, 3201–3400, 3401–3600, 3601–3800, 3801–4000, 4001–4200, 4201–4400, 4401–4600, 4601–4800, 4801–5000, 5001–5200, 5201–5400, 5401–5600, 5601–5800, 5801–6056. No gaps.
- Chapters covered: Preface, 1–14 (all). Skimmed only: end-of-chapter interview-question narratives (numeric content from them was still extracted, e.g., p.10 power-on sequence, p.210 processor selection, p.321 bit reversal, p.353 large numbers); index (lines 5,635–6,044) and colophon skipped (non-technical).
- Extraction limitations: figures are absent from the text — rules depending on figures (Fig 3-1 schedule, 4-6 button signals, 4-9 timer heuristic, 4-10 PWM, 7-1 bus comparison, 8-10 speeds-and-feeds, 11-4 I/O-line profile, 12-4…12-9 Taylor/LUT/interpolation errors, 13-1 current measurement, 13-2 interrupt flow, 14-2…14-5 PID and motion profiles) were transcribed from captions and surrounding prose. Equations 12-1/12-2 and the brute-force timer formulas were rendered as fragmented tokens by the extraction and were reconstructed from the prose (F3, F30, F31). Tables were flattened to one cell per line and reconstructed positionally (Tables 4-1, 7-1, 7-2, 11-1, 11-2, 12-1, 12-2, 13-1). The powers-of-two sidebar prints 2^24 ≈ "~1.6 million" (apparent typo; exact 16,777,216 recorded).
- The book is deliberately processor-agnostic and mostly qualitative; numeric anchors are concentrated in Ch.4 (timers, debounce), Ch.5 (latency), Ch.7 (bus speeds, FIFO/DMA), Ch.8 (flash, display, bandwidth), Ch.11 (scorecards), Ch.12 (fixed point), Ch.13 (power), Ch.14 (motor supply). No PCB-layout numerics (pull-up ohms, bus capacitance limits, trace rules) are given in this book — those must come from other references; the I2C "limited by bus capacitance" statement is qualitative here.
- Rule count: 222 (WHITE-001 … WHITE-222); 40 formulas (F1–F40); 14 numeric tables; 51 mechanizable checks; 23 verification procedures.
