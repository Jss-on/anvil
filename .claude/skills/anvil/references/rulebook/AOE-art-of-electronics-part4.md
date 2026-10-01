# The Art of Electronics, 3rd ed. (Horowitz & Hill) — Part 4 of 4 — Anvil rulebook

## 0. Citation

P. Horowitz and W. Hill, *The Art of Electronics*, 3rd ed. Cambridge, U.K.: Cambridge University Press, 2015. ISBN 978-0-521-80926-9 (hardback).

BOOKTAG: AOE. This file = part 4 of 4 (text-file lines ~56850-75879; printed pp.~920-1170). Rule ids AOE-4001 .. AOE-4296.

**Chapters covered by THIS extraction**
- Chapter 13 "Digital meets Analog" from §13.8.6 (Agilent/Keysight multislope converters, p.919) to the end of the chapter: §13.9 delta-sigma ADCs/DACs, §13.10 ADC choices and tradeoffs (incl. micropower ADCs), §13.11 unusual converters (ADE7753, AD7873, AD7927, AD7730), §13.12 data-acquisition system examples, §13.13 phase-locked loops, §13.14 pseudorandom bit sequences and noise generation, Review of Chapter 13 (pp.919-988).
- Chapter 14 "Computers, Controllers, and Data Links" (all: architecture, x86 subset, PC104/ISA bus signals and timing, interrupts, DMA, memory types, parallel and serial buses: SPI, I2C, 1-wire, JTAG, SATA/SAS, PCIe, RS-232/485, Manchester/biphase/RLL/8b10b coding, USB, FireWire, CAN, Ethernet, number formats, review) (pp.989-1052).
- Chapter 15 "Microcontrollers" (all: five design examples — suntan monitor, ac power control, DDS synthesizer, RTD thermal PID controller, stabilized platform — peripheral ICs, hardware constraints, development environment, selection, review) (pp.1053-1096).
- Appendices A-P (pp.1097-1170): A Math review (no rules - pure math), B How to draw schematics, C Resistor types, D Thevenin/Norton/Millman, E LC Butterworth filters, F Load lines, G Curve tracer, H Transmission lines and impedance matching, I Television tutorial, J SPICE primer, K Where to buy, L Workbench instruments, M Catalogs (no rules), N Further reading (no rules), O The oscilloscope, P Acronyms (no rules).

**Chapters NOT read in this extraction**
- Chapters 1-12 and Chapter 13 §13.1-§13.8.5: assigned to other AOE part agents (parts 1-3).
- Index (text lines 74018-75879, pp.1171 ff.): skipped per brief (index pages).

Conventions: conf = high (explicit number/formula in text), medium (derived from a stated relation, reconstructed from OCR, or graph-based), low (qualitative guidance quantified). Formulas in plain ASCII. "p." = printed page. Domain and verify-by vocabularies per brief.

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| AOE-4001 | filter | Set an integrating ADC's measurement time to an integral number of power-line cycles (NPLC) to reject line-frequency pickup; longer NPLC buys more rejection and accuracy at the cost of reading rate | Tmeas = N/f_line (N integer). Keysight Multislope III normal-mode rejection: 1 PLC = 16.7 ms (6250 clocks @375 kHz) -> 60 dB; 10 PLC -> 95 dB; 100 PLC -> 105 dB; 200 PLC -> 110 dB; 0.02 and 0.2 PLC -> no line rejection | f_line (50/60 Hz), N, f_clk | Integrating/multislope DMM-class converters; 60 Hz setting, 375 kHz clock | calc | p.921, Table 13.8 | high |
| AOE-4002 | components | Multislope first-order estimate: count positive/negative reference cycles over Ncycles; +-12 V full scale gives net count +-2250 over 6250 cycles (~12 bits) | Vin = Vref * (n_minus - n_plus)/Ncycles * (Rin/Rref); Vref = 10 V, Rin = 100 kOhm, Rref = 30 kOhm, Ncycles = 6250 | n+, n-, Ncycles, Vref, Rin, Rref | Keysight Multislope III (Fig. 13.47); sign convention per figure | calc | p.919-920, Fig. 13.47 | medium |
| AOE-4003 | components | Endpoint (residue) correction adds resolution: read integrator residue with a modest ADC at start and end of measurement; a 12-bit residue ADC adds ~9 bits (512 subdivisions of first-order LSB) for ~21-bit total (ADC loses ~3 bits because its range exceeds one-clock ramp) | Vsig(2) = Vsig(1) + (Rin*C1/Tmeas)*(Vf - Vi) = Vsig(1) + 0.00264*(Vf - Vi) at Tmeas = 1 PLC (60 Hz) | Vi, Vf (V), Rin (Ohm), C1 (F), Tmeas (s) | Multislope III; coefficient shrinks as Tmeas grows | calc | p.920, Eq. in 13.8.6 | high |
| AOE-4004 | components | Use NP0/C0G ceramic for the integrating capacitor of precision integrating / charge-balance converters | TC = +-30 ppm/degC; dielectric absorption negligible on switching time scales; cost ~$0.06 | cap dielectric | Keysight 34401A-class integrators; any charge-balance ADC | inspect | p.920, §13.8.6B | high |
| AOE-4005 | components | In a factory-calibrated precision converter, the reference and gain resistors must be STABLE (time, temperature) rather than initially precise; specify matched resistor arrays for ratio tracking | ratio drift is the error term; initial ratio mismatch removed by calibration; 7.0 V zener reference (LTZ1000) -> +-10.0 V via precision op-amps | reference type, resistor-array tracking TC | Calibrated instruments | review | p.920, §13.8.6B | medium |
| AOE-4006 | components | Current-steering switches in a charge-balance integrator: keep all switch pins near 0 V (virtual ground) and use switches whose Ron is small vs the steering resistors and well matched | 74HC4053: Ron typ 85 Ohm, matched to 8 Ohm; Ron << R1..R3 so residual removed by auto-calibration | Ron, Ron match, R1..R3 | Switched-current integrators | calc | p.920, §13.8.6B | high |
| AOE-4007 | timing | Switches steering reference current into an integrator summing junction must be break-before-make | NXP 74HC4053 ton-toff difference implies 4 ns break-before-make (not directly specified); Siliconix DG4053 tD = 6 ns typ (2 ns min) | switch timing specs | Charge-balance / multislope ADCs | inspect | p.920, §13.8.6B | high |
| AOE-4008 | test | Budget bench-DMM uncertainty when using a 6.5-digit meter as the verification instrument | 34401A: initial factory-calibrated dc accuracy ~2 ppm; drift <= +-0.0015% over 24 h, +-0.0035% after one year | instrument, cal age | Verification of dc accuracy claims | calc | p.920, fn.57 | high |
| AOE-4009 | components | Auto-calibrate charge-balance converters before each high-resolution reading: alternate S1/S2 with no input to measure +/- reference-current mismatch; route Vref to input to measure signal/reference mismatch; primary reference drift needs an external known source (cal lab) | calibration sequence per reading | - | Multislope converters | review | p.921, §13.8.6B | medium |
| AOE-4010 | components | Charge-balance (first-order delta-sigma) current integrator design: (a) clock period << measurement time; (b) R must source more than full-scale input current; (c) C keeps integrator excursion per clock < Vcc/2 | R < Vcc/I_fs; dV_per_clock = Vcc/(R*C*f_clk) < Vcc/2; duty cycle D = I_in*R/Vcc; D = N/(f_clk*T). Example: I_fs = 1 uA, Vcc = 5 V -> R < 5 MOhm; chosen f_clk = 10 Hz, R = 3.3 MOhm, C = 100 nF -> <= 1.5 V per clock; peak count rate = f_clk, average 0.6 f_clk; 16-bit counter OK to 2 h | I_fs (A), Vcc (V), R (Ohm), C (F), f_clk (Hz) | Photodiode/current-input integrators; comparator accuracy and threshold not critical | calc | p.922-923, Fig. 13.49 | high |
| AOE-4011 | components | Dynamic range of a current-input charge-balance converter is limited by the integrator op-amp offset | I_err = Vos/R; example 0.2 nA worst case (LMC6482 -A grade, R = 3.3 MOhm) -> DR = 5x10^3 at 1 uA FS; bias current (4 pA max) negligible | Vos (V), R (Ohm), I_fs | Single-supply RRIO op-amp integrator | calc | p.923, §13.9.1(c) | high |
| AOE-4012 | components | A plain clock-counting (1-bit, boxcar) converter needs f_clk = 2^N x conversion rate; do not use it for high resolution at speed, use a delta-sigma with a weighted digital filter | full-scale count = Tmeas/Tclk; 100 ksps with 10 MHz clock -> 100 counts (~7 bits); 16 bits at 100 ksps needs 2^16 x 100 kHz = 6.5536 GHz | N bits, conversion rate | Counter-type converters | calc | p.923 | high |
| AOE-4013 | components | Delta-sigma modulator bit rate | f_bit = OSR * 2 * f_max (OSR = oversampling ratio, f_max = max signal frequency) | OSR, f_max | Delta-sigma ADC/DAC | calc | p.924, §13.9.4 | high |
| AOE-4014 | components | Delta-sigma ADC theoretical resolution vs oversampling ratio and modulator order | in-band quantization noise suppressed as OSR^(m+0.5); ENOB ~= log2(OSR)*(m + 1/2); each OSR doubling adds (m + 1/2) bits. Example OSR = 64, m = 2 -> ENOB ~= 15. 2-bit modulator: slopes doubled | OSR, m (order), bits in quantizer | 1-bit modulator; formula not strictly correct for m > 2 (weighted-sum structure) | calc | p.928, Fig. 13.56 | high |
| AOE-4015 | components | Plain cascades of integrators are stable only up to 2nd-order modulators; higher orders need a weighted sum of integrator outputs. Audio delta-sigma ADCs typically use 5th-order modulators at 64x OSR for ~20-bit effective dynamic range | order <= 2 for simple cascade | modulator order | Delta-sigma design | review | p.928, fn.81 | high |
| AOE-4016 | filter | First-order delta-sigma transfer functions: signal is lowpass, quantization noise is highpass, same breakpoint | abs(Gsig) = 1/sqrt(1+(w/w0)^2); abs(Gqn) = (w/w0)/sqrt(1+(w/w0)^2); w0 ~= 2*pi*f_clk (integrator unity-gain at oversampling clock) | w, f_clk | Linear model of 1st-order modulator; noise curve linear (1st order), quadratic (2nd), cubic (3rd) | calc | p.927, Figs. 13.53-13.54 | high |
| AOE-4017 | components | First-order delta-sigma modulators produce in-band idle tones for particular dc inputs; use >= 3rd-order modulators for audio | example: +0.625 V on +-1 V FS -> 16-clock repeating pattern; at 4x OSR tone at mid-band, 118 mV pp = ~6% FS = only ~25 dB suppression | modulator order, dc input | Audio/low-noise delta-sigma | review | p.932, Figs. 13.61-13.62 | high |
| AOE-4018 | filter | Anti-alias: lowpass-filter the analog signal before sampling to remove components above fs/2; aliases cannot be removed afterwards. Oversampling relaxes filter steepness (delta-sigma ADCs need only a low-order analog anti-alias filter) | f_signal_max < fs/2; CD audio: fs = 44.1 kHz for 20 kHz band (~10% oversampling) vs 2x oversampling fs = 80 kHz | fs, passband edge, filter order | Any sampled ADC | calc | p.931, Fig. 13.60 | high |
| AOE-4019 | timing | Delta-sigma ADC decimation-filter latency is tens of output-sample times (~ms for audio ADCs); pipelined flash ~10 sample intervals; audio ADCs 12 to 63 sample intervals. Check latency against any control-loop or trigger timing budget | latency_s = k/f_out, k ~ 10s (delta-sigma), ~10 (pipeline), 12-63 (audio) | output rate, loop budget | ADC in feedback loops | calc | p.931, p.937, p.938 | high |
| AOE-4020 | components | Delta-sigma bandwidth ceiling | max ~10-100 Msps (limited by GHz-scale oversampling clock) | required sample rate | Architecture selection | review | p.931, §13.9.9B | high |
| AOE-4021 | components | Delta-sigma DACs use an analog output LPF: expect clock feedthrough and broadband noise; continuous-time filters are jitter-sensitive (switched-capacitor filter sharing the clock suppresses jitter); R-2R DACs are "quiet" | DAC1220 (20-bit delta-sigma): ~1000 nV/rtHz at 1 kHz vs ~10 nV/rtHz for resistor-ladder DACs | DAC noise density | Precision/low-noise DAC selection | review | p.930-931, p.938 | high |
| AOE-4022 | hw-fw | A microcontroller-driven delta-sigma integrator is only as accurate as its switch ON-time and sampling-clock stability: generate the charge pulses with timer capture/compare hardware, not software timing | pulse width fixed by hardware timer | MCU timer resources | MCU-assisted charge-balance ADCs | review | p.933, fn.90 | medium |
| AOE-4023 | power | Low-side battery coulomb counter sizing: sense resistor sets burden at max load; chopper op-amp offset sets zero error; integrator C sized so ramp <= Vcc/5 per clock | Rsense = 10 Ohm -> 0.25 V burden at 25 mA max; Vos <= 10 uV -> 1 uA error -> 25,000:1 DR; FS integrator current 100 uA (I_fs = Vcc/R3); f_clk = 10 kHz; C1 = 5/(f_clk*R3) = 15 nF | I_load_max, Vos, f_clk, R3 | MSP430 + chopper op-amp gas gauge (Fig. 13.64) | calc | p.933-934 | high |
| AOE-4024 | power | Place the coulomb-counter sense resistor so it meters every load including regulator Iq, MCU, and the integrator op-amp; verify worst-case zero error << sleep current | zero error 1 uA vs system sleep ~45 uA; budget: MCU 0.3 mA @1 MHz active, 25 uA LPM2; chopper op-amp 17 uA typ; regulator 1.3 uA max (OCR prints "1.3 A", evidently uA) -> several months on 1 Ah Li-ion (processor active) | Iq list | Battery gas gauge | calc | p.934 | high |
| AOE-4025 | hw-fw | If the MCU sleeps while a charge integrator runs, wake often enough that the unobserved ramp cannot saturate | t_wake <= dV_allow*C/I_sleep; example ~45 uA sleep current -> measure every 80 ms to limit unobserved ramp to 1 V; MSP430 wakes in one 1 us clock | I_sleep, C, dV_allow | Sleep-mode coulomb counting | calc | p.934, fn.91 | high |
| AOE-4026 | components | Noise-limited effective resolution vs noise-free (peak-to-peak) resolution | ENOB = log2(Vspan/Vrms) = 1.44*ln(Vspan/Vrms); noise-free resolution = ENOB - 2.7 bits (p-p taken as 6.6 x rms, 6-sigma no code flicker) | Vspan (V), Vrms noise (V) | Delta-sigma datasheets (CS5532 definition) | calc | p.935-936, fn.93 | high |
| AOE-4027 | components | Worked example AD7734: +-10 V FS, chop mode, longest filter -> 9.6 uVrms noise -> 21-bit effective at 372 sps; peak-to-peak 18.1 bits; max offset drift +-2.5 uV/degC, gain drift +-3.2 ppm/degC; input tolerant to +-16.5 V without affecting other channels, +-50 V without damage | 21 bits = log2(20 V/~10 uV) | Vrms, span | AD7734 | calc | p.934-936 | high |
| AOE-4028 | components | Size PGA gain so sensor full scale fits the ADC span with no external front-end gain: CS5532 at G = 64 -> +-2.5 V/64 = +-40 mV FS; 20-bit LSB = 80 nV = 1/500 of a 1 degC thermocouple change; 0.0008% of strain-gauge FS | thermocouple ~40 uV/degC; strain gauge FS ~+-2 mV per volt of excitation | Vref, G, sensor FS | Low-level sensor digitizing | calc | p.936 | high |
| AOE-4029 | filter | Add a simple RC filter at precision ADC sensor inputs to suppress spikes and protect inputs; balance thermocouple signals about ground to reduce common-mode pickup on unshielded leads | tau = 0.1 ms | R, C | Thermocouple/bridge front ends (Fig. 13.67) | inspect | p.936 | high |
| AOE-4030 | components | Thermocouple digitizing requires cold-junction compensation (e.g., MAX31855 covers seven thermocouple types) | CJC present = pass | sensor type | Thermocouple inputs | inspect | p.937, Fig. 13.67 caption | medium |
| AOE-4031 | components | Check voltage-reference dropout against the available headroom | example: ADR441 chosen to operate with 500 mV headroom | Vin_min - Vref >= dropout | Low-voltage precision ADC references | calc | p.936 | medium |
| AOE-4032 | components | Do not use audio delta-sigma ADCs for dc/industrial measurements | audio ADCs: gain accuracy 5-10%, dc offset ~25 mV, internal digital HPF ~1 Hz, latency 12-63 sample intervals; channel matching 0.1 dB (1%); dc specs "several percent" or none | application type | ADC selection | review | p.937-938 | high |
| AOE-4033 | requirements | ADC architecture by speed/resolution | ~10 sps: multislope or 24-bit delta-sigma; to ~100s ksps: delta-sigma above 16 bits, SAR at <= 16 bits; to a few Msps: SAR vs delta-sigma (SAR faster, e.g. AD7690 18-bit 400 ksps); to 100s Msps: pipelined flash (latency ~10 samples; AD9626 12-bit 250 Msps, ADS6149 14-bit 250 Msps); > 250 Msps: flash/folding at 6-10 bits (ADC08D1520 8-bit 3000 Msps, ADC12D1800 12-bit 3600 Msps) | rate, bits | ADC selection | review | p.938, §13.10.1A | high |
| AOE-4034 | requirements | DAC architecture: highest linearity -> delta-sigma (to 20 bits at audio speeds, watch broadband/clock noise); medium speed high accuracy -> R-2R or linear ladder; competing technologies R-2R, linear resistor ladder + switch array, current-steering array | per §13.10.1B | rate, linearity, noise | DAC selection | review | p.938 | high |
| AOE-4035 | components | Audio signal-chain distortion target: harmonic distortion at 0.001% is inaudible; dynamic range (resolution + noise) matters more | THD <= 0.001% | THD | Audio ADC front ends | review | p.938 | medium |
| AOE-4036 | components | DAC candidates by class (2015): medium-speed high-accuracy ladder DACs; highest speed = current-steering | DAC8552 dual 16-bit, serial, V-out, ext ref, very low glitch, 10 us settle; AD5544/DAC8814 quad 16-bit MDAC, I-out, 0.5-2 us settle with external I-to-V op-amp; LTC1668 16-bit parallel, diff I-out, 20 ns settle into 50 Ohm; DAC9881 18-bit serial RRO V-out, low noise, 5 us settle; DAC5681/2 16-bit 1 Gsps; AD9739 14-bit 2.5 Gsps | settle time, bits, rate | DAC selection | review | p.938-939 | high |
| AOE-4037 | components | SAR vs delta-sigma trade (same vendor, same year): SAR gives ~25x lower data latency and ~13x lower power, single supply + internal ref; delta-sigma gives better SNR, ~15x smaller gain error (via gain-correction register) and trivial anti-alias filter (8x OSR) | AD7641 SAR vs AD7760 delta-sigma, see T-4.4 | latency, power, SNR, gain error | ADC architecture choice at ~2 Msps | review | p.939, shootout table | high |
| AOE-4038 | filter | An averaging (integrating) converter with aperture T is a lowpass: sinc response, first null at f = 1/T and nulls at all multiples of 1/T; roughly equivalent to an RC lowpass with -3 dB at f = 1/(2T). A sampling (SAR) converter on a slow signal admits wideband noise: add an input lowpass filter | abs(H(f)) = abs(sin(pi*f*T)/(pi*f*T)); nulls at k/T; RC-equivalent f_3dB = 1/(2T) | T (s) | Slow sensors (temperature, strain) sampled by SAR vs integrating ADC | calc | p.940, Fig. 13.69, fn.101-102 | high |
| AOE-4039 | power | SAR ADC average power scales with sample rate; duty-cycle the converter and power-switch the sensor after the sample is captured | AD7685: 2.7 mW continuous at 200 ksps (3 V) -> 1.4 uW average at 100 sps (2000x less) | P_active, f_s, f_s_max | Battery sensor nodes | calc | p.941 | high |
| AOE-4040 | power | Low-power ADC choice at 10 readings/s, 16 bits: SAR uses ~1/2000 the energy of a delta-sigma but the delta-sigma's 66 ms integration is quieter (the SAR may need ~2000 averaged samples for the same noise) | MCP3425 delta-sigma: 0.44 mW continuous at 15 sps (16-bit); 290 uW average at 10 sps; SAR (AD7685) 0.14 uW at 10 sps; datasheet "1.8 uW" applies only to 12-bit mode at 1 sps | rate, bits, noise | Micropower ADC selection | calc | p.941-942 | high |
| AOE-4041 | power | Count the serial-clock drive power of fast-clocked converters; gate SCLK to the data-shift interval | P = C*V^2*f; AD7091R: C = 5 pF, 3 V, 50 MHz -> 2.25 mW (> converter's 1 mW); clocking only 12-13 of 50 cycles -> 0.6 mW | C_pin (F), V (V), f (Hz), duty | External-clock SAR ADCs | calc | p.942, fn.105 | high |
| AOE-4042 | power | Lowering ADC supply voltage cuts power faster than V^2 (CMOS shoot-through), at some performance cost and analog-headroom difficulty | AD7466 at 100 ksps: 620 uW at 3.0 V, 120 uW at 1.6 V (5.2x power for 1.9x voltage) | Vsupply | Micropower ADCs | calc | p.942, fn.106 | high |
| AOE-4043 | hw-fw | Micropower ADC review items: on-chip input amp, internal reference, internal conversion oscillator (else extra external power); supply used as reference only for ratiometric sensors (thermistor, strain gauge); converters clocked by the interface shift clock force slow SCLK; non-trivial startup delay from sleep for intermittent power | checklist | datasheet | Intermittently powered ADCs | review | p.942 | medium |
| AOE-4044 | components | Current-sensing method selection for ac power metering | 4-wire resistive shunt: ac or dc, no isolation; current transformer: ac only, isolated; Rogowski coil: ac only, output proportional to dI/dt (needs integrator), linear (no core), installs without breaking the conductor | ac/dc, isolation need | Power-metering front ends (ADE7753) | review | p.944, Fig. 13.72 | high |
| AOE-4045 | protection | A metering IC connected directly to the line (chip ground on powerline neutral) makes all its logic line-referenced: isolate every interface to MCU/user | ADE7753 inputs +-0.5 V full-scale on PGA difference amps | connection scheme | Direct-connect single-phase metering (Fig. 13.71) | inspect | p.943, Fig. 13.71 | medium |
| AOE-4046 | components | ADE7753 power-metering IC: second-order 16-bit delta-sigma ADCs at ~28 ksps, 0.05 deg phase trim between V and I channels, 49-bit energy accumulators, CF pulse output proportional to active power, SPI with 64 registers, sag/peak detection, ~$4 | phase calibration resolution 0.05 deg | - | Single-phase (ADE7758 3-phase) | review | p.943-944 | high |
| AOE-4047 | components | Resistive touchscreen readout: energize one sheet, read the other; include the drive voltage as a MUX input for ratiometric measurement | AD7873: 12-bit SAR, +2.2 to +5.25 V, few mW, ~$2 (1000 pcs); capacitance converters (AD7140/50, AD7740 series) 16-24 bit, <= ~100 sps, ~$2 (qty 25) | - | Touch/capacitance sensing | review | p.944-945 | high |
| AOE-4048 | components | Bridge (strain gauge) front end: use a differential ratiometric reference from the bridge excitation, chopping to remove offset/drift, and ac (polarity-reversed) excitation to cancel residual and thermoelectric offsets | AD7730: 10 mV FS inputs, offset drift 5 nV/degC, gain drift 2 ppm/degC, 24-bit delta-sigma, single +5 V, ~$15 | bridge FS (mV), excitation | Weigh-scale / pressure bridges | review | p.945, Fig. 13.75 | high |
| AOE-4049 | protection | Analog MUX input overvoltage: verify MUX survives beyond-rail inputs and does not clamp when unpowered; add a current limiter for serious overvoltage | MPC506: inputs to 20 V beyond +-15 V rails without latchup or crosstalk; input current begins ~15 V beyond rails, ~20 mA at 40 V beyond; beyond that damage. Back-to-back depletion MOSFETs (TO-92/SOT-23) hold off 500 V and limit current to ~mA; Idss ~2 mA; without the extra 1 kOhm limit sustained overvoltage to ~100 V (dissipation) | V_overdrive, I_limit, P_diss | +-10 V DAQ inputs (Figs. 13.76-13.77) | calc | p.946-947, fn.110 | high |
| AOE-4050 | timing | Break-before-make MUX switching adds delay: budget switching time in scan rate | MPC506: switching time 0.3 us typ, "make" delayed 80 ns | t_switch, scan rate | Multiplexed DAQ | calc | p.946 | high |
| AOE-4051 | filter | A multiplexed DAQ cannot put the anti-alias filter after the MUX without limiting scan speed: band-limit each input upstream of the MUX | per-channel LPF before MUX | scan rate, filter settling | Multiplexed ADC systems | inspect | p.947 | high |
| AOE-4052 | components | Do not pick the lowest-Ron analog switch by default; trade Ron against leakage, capacitance and charge injection | IH5043/DG403: Ron 80 Ohm max, Cs(on) 22 pF, low leakage/charge injection; ADG884: Ron 0.4 Ohm max but Cs(on) 295 pF and 5 Vpp max swing; ADG1413: Ron 1.5 Ohm, +-15 V, charge injection +-300 pC (5-10x the 5043/DG403) | Ron, Cs(on), Q_inj, leakage | Signal-path switches ahead of high-Z amplifiers | review | p.947-948, fn.112 | high |
| AOE-4053 | timing | PGA settling must fit the ADC acquisition window | PGA202: gains 1/10/100/1000, settles 2 us to 0.01% (except G = 1000) for a 200 ksps ADC; ranges +-10, +-1, +-0.1 V; input 10 GOhm, 50 pA vs MUX leakage 2 nA typ | t_settle, 1/f_s, accuracy | Multiplexed DAQ | calc | p.948 | high |
| AOE-4054 | components | Refer ADC step size to the amplifier input and compare every RTI error (offset, drift, noise) against it | LSB_RTI = (V_span/2^N)/G; +-10 V, 16-bit -> 0.3 mV; RTI 300/30/3 uV at G = 1/10/100. PGA202 offset RTI = (0.5 + 5/G) mV -> 5.5, 1, 0.55 mV = 18, 33, 180 LSB_RTI -> requires manual trim + electronic nulling | V_span, N, G, Vos_RTI | Front-end + ADC error budget | calc | p.948-949 | high |
| AOE-4055 | components | Offset-nulling DAC sizing: trim range must cover worst-case offset (RTO) with step << LSB | 10-bit DAC 0-5 V -> +-7.5 mV trim at amplifier output, 15 uV step vs 300 uV ADC LSB | trim range, DAC bits | Electronic offset nulling | calc | p.949 | high |
| AOE-4056 | thermal | Check temperature drift per LSB at the highest gain | PGA202 offset drift (3 + 50/G) uV/degC, 50 uV/month, (10 + 250/G) uV/V supply; gain TC 3 ppm/degC (G = 1, 10), 40 ppm/degC (G = 100); LSB = 30 ppm of FS -> at G = 100 a 1 degC change = 1 LSB error | TC, G, LSB | Precision multiplexed DAQ | calc | p.949-950 | high |
| AOE-4057 | components | Integrate amplifier noise over the actual signal bandwidth and compare with LSB_RTI | PGA202: 1.7 uVpp typ (0.1-10 Hz); en = 12 nV/rtHz at 10 kHz; 1/f corner ~100 Hz; 0.1 Hz-10 kHz -> ~3 uV RTI (comparable to LSB_RTI at G = 100, negligible at lower G) | en, fc_1/f, BW | Front-end noise budget | calc | p.949 | high |
| AOE-4058 | components | Internal ADC references limit gain accuracy/drift; use a precision external reference for better performance | LTC1609 internal 2.5 V: +-1% worst, +-5 ppm/degC typ; best external refs +-0.02% worst, <= +-1 ppm/degC typ; LTC1609 REF pin overdrives 4 kOhm internal source; with external ref untrimmed gain error +-0.5%, gain drift +-2 ppm/degC; ADC worst-case zero +-10 mV and gain +-1.5% must be calibrated out | ref accuracy, TC | SAR DAQ | review | p.949-950 | high |
| AOE-4059 | hw-fw | Store per-channel/per-gain calibration (offset, full-scale) in non-volatile memory; optionally dedicate a shorted channel for zero and a channel reading Vref for full-scale self-calibration | cal table in NVM, loaded at startup | channel map | MCU-controlled DAQ | review | p.949-950, fn.113 | medium |
| AOE-4060 | components | Offsets and drifts specified RTO must be converted to RTI by dividing by gain (for attenuating G < 1 the RTI error grows) | Vos_RTI = Vos_RTO/G; AD8275 (G = 0.2): Vos < 0.5 mV RTO -> +-2.5 mV RTI = ~8 LSB (LSB_RTI = 2*10.24 V/2^16 = 0.31 mV); drift 7 uV/degC RTO -> 45 degC per LSB | Vos_RTO, G, LSB | Level-translating ADC drivers | calc | p.950 | high |
| AOE-4061 | components | Level-translate +-10 V into a single-supply ADC with a precision G = 0.2 difference amp and a 4.096 V reference: +-10.24 V FS gives round 10.0 mV steps at 11 bits and allows calibration with a 10.0 V standard without over-range; RRO driver on ADC supply protects against overdrive | AD8275: G = 0.2 +- 0.024%, 1 ppm/degC max, 0.45 us settle to 0.001%, rail-to-rail out | Vref = 4.096 V, G = 0.2 | Bipolar inputs to unipolar ADC | calc | p.950 | high |
| AOE-4062 | components | Charge-redistribution SAR input: put a capacitor across the ADC input isolated from the driving amp by a small resistor | 2.7 nF and 33 Ohm (AD7685) | C_in, R_iso | SAR ADC driver | inspect | p.950, fn.114 | high |
| AOE-4063 | components | Low-noise reference for 16-bit DAQ | ADR440 XFET: 1.8 uVpp (typ) noise, 3 ppm/degC (max); AD7685 16-bit SAR: 250 ksps, +-3 LSB INL max, +-0.3 ppm/degC gain drift, SPI daisy-chain | noise, TC | SAR DAQ | review | p.950 | high |
| AOE-4064 | timing | When a digital isolator's propagation delay is comparable to the SPI clock period, echo SCK back through the isolator and clock read data on the echoed clock; residual error = channel-to-channel skew | ADuM1402C: 90 Mbps, 27 ns typ delay, 2 ns max skew; readout ~50 Mbps | t_pd, t_skew, f_SCK | Isolated SPI ADC readout (Fig. 13.78) | calc | p.951 | high |
| AOE-4065 | emc | Galvanically isolate the digital interface of a quiet analog subsystem; serial (3-4 wire) interfaces make isolation cheap, parallel buses do not (MAX11046 would need 21 isolation channels incl. bidirectional lines) | isolate SPI with 4-ch isolator | interface width | Mixed-signal DAQ | review | p.950-951 | high |
| AOE-4066 | protection | ADC input clamps need external series resistors to limit clamp current | MAX11046 inputs clamp ~0.3 V beyond range (+-5.3 V); limit clamp current to 20 mA | V_fault, R_series | Clamped ADC inputs | calc | p.951 | high |
| AOE-4067 | components | Simultaneous-sampling integrated SAR: MAX11046 8 ch x 16-bit, 250 ksps, single +5 V, +-5 V range, +-0.01% max offset, +-2.4 uV/degC typ, +-2 LSB max INL, 0.1 ns sampling skew, conversion 3 us, T/H BW 4 MHz, ~$42; AD7608 8 T/H into one 18-bit 200 ksps ADC | skew 0.1 ns | - | Simultaneous multichannel capture | review | p.951-952 | high |
| AOE-4068 | hw-fw | I2C devices need unique 7-bit addresses (128 possible); low-pin-count parts pre-assign addresses by part number or offer one ADDR pin with 4 states (tied HIGH, LOW, SDA, SCL); plan address map or split buses | ADS1100: 8 part numbers, addresses 72-79 decimal; ADS1115: 4 addresses (72-75) -> 8 channels need 2 I2C buses | device count, address options | I2C sensor arrays | review | p.952-953 | high |
| AOE-4069 | emc | Normal-mode line rejection of a delta-sigma ADC depends on its clock accuracy: internal RC clocks give ~30 dB; use an accurate/external clock or a converter with a wide 50/60 Hz notch | ADS1100 internal clock +-20% / ADS1115 +-10% -> ~30 dB; CS5512 with external 32.768 kHz -> 80 dB min notch 47-63 Hz, ~90 dB at both 50 and 60 Hz; MCP3551 internal clock +-0.5% -> 85 dB typ at both 50 and 60 Hz; MCP3550-50/-60 -> 120 dB typ at one frequency | clock tolerance, notch spec | Slow precision delta-sigma | review | p.953-955, Fig. 13.83 | high |
| AOE-4070 | components | Read the datasheet's normal-mode (differential) rejection, not the common-mode rejection figure | ADS1115: lists 105 dB CMR at 50/60 Hz, but normal-mode rejection from graph only ~30 dB | datasheet NMR | Line-rejection claims | review | p.953, fn.116 | high |
| AOE-4071 | components | Gain error of ADCs using internal or supply reference in LSB terms | ADS1115: gain error 0.01% typ, 0.15% max = 100 LSB at 16 bits (1 LSB = 15 ppm); gain drift 40 ppm/degC max = ~3 LSB/degC; ADS1100 uses Vdd as reference (FS +-Vdd/G), INL 0.013% max | gain error ppm, bits | Ratiometric vs absolute measurements | calc | p.953 | high |
| AOE-4072 | components | Check a converter's full-scale (gain) tolerance even when it takes an external reference | CS5512: excellent linearity (+-0.0015% FS max), 0.06 uV/degC and 1 ppm/degC drift, but VFS = 2.5*Vref +-10% -> gain uncertain +-10% (needs system calibration) | VFS tolerance | Delta-sigma selection | review | p.954 | high |
| AOE-4073 | components | Without a PGA, a 22-bit converter is needed to match a 16-bit converter with 64x PGA | MCP3551: 22-bit -> 1.2 uV resolution; Vos +-12 uV max, FS error -10 ppm max, INL 6 ppm max, drift 0.04/0.028 ppm/degC; 12% over/under range; single-cycle conversion with self-cal; 2.7-5.5 V at ~0.1 mA; 8-channel system $38 incl. ADR441A | resolution, PGA | Multichannel slow DAQ | calc | p.955 | high |
| AOE-4074 | components | Low-cost multichannel codec-style delta-sigma ADCs need in-system calibration and ac coupling | AD73360: six 16-bit 64 ksps channels, PGA 0-38 dB, ~$8; gain accuracy +-10%, worst-case dc offset ~10% FS | - | Motor-drive / power monitoring | review | p.955 | high |
| AOE-4075 | components | High-speed multichannel delta-sigma exists but costs power | ADC12EU050: 8 x 12-bit at 50 Msps, 3rd-order modulators with 3-bit wordstreams, 16x oversampling clock from on-chip LC-VCO PLL, one LVDS pair per channel, ~0.4 W, ~$100 | - | Ultrasound-class DAQ | review | p.955-956, Fig. 13.84 | high |
| AOE-4076 | timing | Lock the integrating-ADC clock to the power line with a PLL frequency multiplier to get "infinite" rejection of line frequency and harmonics | f_clk = n*f_line; example 61.440 kHz = 60 Hz x 1024 -> 7.5 conversions/s, 4096-clock ramp-up and 4096-count FS | n, f_line | Dual-slope/charge-balance ADCs | calc | p.956, p.961 | high |
| AOE-4077 | timing | Phase-detector choice: type I (XOR/multiplier) needs 50% duty inputs, can lock on harmonics, rejects noise well, leaves high ripple at 2 f_in, capture range limited by loop filter; type II (edge/PFD) ignores duty cycle, no harmonic lock, poor noise rejection, low ripple, captures over full VCO range, gives zero phase error in 2nd-order loop | see T-4.6 | reference cleanliness, duty cycle | PLL design | review | p.957-958 | high |
| AOE-4078 | timing | Type II phase detectors with a noisy reference (e.g. 60 Hz line) false-trigger: condition the reference with a lowpass filter + Schmitt trigger, or use a type I (XOR) detector | LPF + Schmitt before PFD | reference SNR | Line-locked PLLs | inspect | p.963 | high |
| AOE-4079 | timing | Prevent PFD dead zone/backlash (hunting, jitter) with current-output charge pumps with intentional overlap; cheap cure: large resistor across the loop-filter capacitor (adds ill-defined static phase offset) | 74HCT9046 anti-backlash pulses ~15 ns | PD type | Low-jitter synthesizers | review | p.958-959, Figs. 13.92-13.93 | high |
| AOE-4080 | control-loop | Second-order PLL stability: VCO is an integrator (1/f, 90 deg lag); use a lead-lag loop filter whose zero sits a factor >= 3-5 below the unity-gain frequency so the loop gain rolls off at -6 dB/octave through unity | G(jw) = Kp * Kf(jw) * Kvco/(jw) * (1/n); Kp = VDD/(4*pi) V/rad (type II, 0..VDD over -360..+360 deg); Kvco = 2*pi*(f_max - f_min)/dV rad/s/V; Kf = (1 + jw*R4*C2)/(1 + jw*(R3 + R4)*C2); zero f1 = 1/(2*pi*R4*C2) <= fc/3..fc/5 | Kp, Kvco, n, R3, R4, C2 | PLL frequency multipliers/synthesizers | calc | p.961-963, Figs. 13.97-13.100, gain box | high |
| AOE-4081 | control-loop | Worked PLL example (60 Hz -> 61.440 kHz, n = 1024): unity-gain fc = 2 Hz (12.6 rad/s), zero f1 = 0.5 Hz (3.1 rad/s), C2 = 1 uF, R4 = 330 kOhm, R3 = 4.3 MOhm; VCO 20 kHz (V2 = 0) to 200 kHz (V2 = 5 V), Kvco printed as 2.26x10^5 rad/s/V | abs(G(j*2*pi*2 Hz)) = 1 claimed (Exercise 13.7). NOTE: with Kp = 0.40 V/rad the printed values give abs(G) ~0.5; abs(G) = 1 needs Kp*Kvco ~1.8x10^5 s^-1 (i.e. VDD = 10 V) - verify by calc | component values | CD74HC4046A (Fig. 13.99) | calc | p.962-963 | medium |
| AOE-4082 | control-loop | PLL bandwidth choice: wide enough to follow wanted input variations (FM demod: >= max modulating frequency; tone decode: response time << tone duration), low enough for flywheel action and low output phase noise when multiplying a stable reference | fc << f_ref; line-locked example fc = 2 Hz | f_ref, input dynamics | PLL design | review | p.962 | medium |
| AOE-4083 | control-loop | Loop-filter damping and jitter: R3*C2 sets response time, R4/R3 sets damping; start with R4 = 10-20% of R3; a fraction R4/(R3 + R4) of raw PD output reaches the VCO -> add a small capacitor ~C2/20 from VCO control pin to ground, close to the pin | R4 = 0.1..0.2*R3; C3 ~= C2/20 | R3, R4, C2 | Passive lead-lag PLL filters | calc | p.963-964 | high |
| AOE-4084 | components | Buffer the VCO control input with an op-amp if its input impedance is not very high relative to MOhm-level loop-filter resistors | CMOS 4046 VCO input ~10^12 Ohm typ | Z_in(VCO) vs R3 | PLL loop filters | inspect | p.963 | high |
| AOE-4085 | components | Mixed-signal functions inside logic ICs vary widely by manufacturer: (1) specify one manufacturer, no substitutes; (2) keep a wide VCO safety margin (e.g. 3x on f_min/f_max); (3) replace paper values with bench-measured values before production | 74HC4046A VCO with same R/C: NXP +5%, ON Semi +160%, Fairchild -60% vs TI; datasheet graphs off by 1.5x; within one maker < 5% over batches and 15 years | f_center margin | Phase comparators, oscillators, VCOs, mixers, Schmitt triggers, monostables, comparators in logic ICs | measure | p.964, fn.120-121 | high |
| AOE-4086 | control-loop | A nonlinear VCO tuning curve makes PLL loop gain vary with frequency; check stability at both ends of the tuning range | Kvco(f) spread | Kvco min/max | PLL design | calc | p.960 | medium |
| AOE-4087 | control-loop | Lock acquisition: type II PFD always locks (given VCO range) with a time constant of the loop bandwidth; type I with integrating filter locks slowly: t_lock ~ (df)^2/BW^3; for narrow loops add a slow sweep of VCO control until lock is detected | example: 100 Hz BW, 100 kHz comparison, 10% initial error -> ~1 min; Efratom FRS rubidium VCXO (20 MHz, +-1 kHz tuning, integrator 2 MOhm/1 uF) sweeps 250 mV/s until lock | df (Hz), BW (Hz) | Narrow-band PLLs, VCXOs | calc | p.965 | high |
| AOE-4088 | control-loop | Type I phase detector capture range shrinks with longer loop-filter time constant and lower loop gain (can be used to restrict lock to a band); lock range for both types spans the full VCO range | qualitative | tau_filter, loop gain | PLL capture | review | p.965 | medium |
| AOE-4089 | timing | State the PLL figure of merit for the application before choosing a part: tuning range vs phase noise/jitter/spurs vs step size vs loop bandwidth (switching speed) vs external part count; ADC sampling clocks and high-speed serial links are jitter-critical (jitter becomes distortion); CPU/memory clocks tolerate coarse steps and modest quality | requirement table per clock | application | Clock/synthesizer selection | review | p.966 | medium |
| AOE-4090 | timing | Integer-n synthesizer with input and output dividers: keep the phase-detector comparison frequency high; a low f_comp forces a long loop time constant (slow lock), leaves VCO noise uncorrected, and puts reference spurs at +-f_comp close to the carrier | f_out = (f_ref/r)*(n/m); f_comp = f_ref/r; step = f_comp/m; VCO = f_out*m. Example: 10 MHz ref, r = 10^4 (f_comp = 1 kHz), m = 10^3 -> 1 Hz steps, f_out to 100 kHz with VCO to 100 MHz; output-divider-only scheme (m = 10^7) would need a 1 GHz VCO for 100 Hz out | f_ref, r, n, m | Integer-n PLL synthesis | calc | p.966-967, Fig. 13.102 | high |
| AOE-4091 | timing | Fractional-n synthesis (modulus alternates n / n+1) keeps f_comp high with fine steps, but the periodic modulus change creates phase modulation/spurs: require compensation (charge-pulse injection or precomputed correction) or delta-sigma modulus modulation with dither; read datasheet spur specs | f_out = (f_ref/r)*n_frac | spur spec | Fractional-n PLLs | review | p.967-968 | high |
| AOE-4092 | timing | Rational-approximation synthesis: choose small integers r, n putting f_out within +-100 ppm of target, then pull the master reference (DDS + VCXO) to hit it exactly; keeps f_phi in MHz range for wide loop BW and low close-in noise; avoid round-number internal clock frequencies to prevent clock-collision artifacts; dither the DDS | example 1234.56789 MHz: r = 26, n = 321, reference offset -38.469 ppm (99.9961531 MHz), f_phi ~3.85 MHz; production f_phi typ > 10 MHz, worst 2.4 MHz; SRS SG380: dc-6 GHz, uHz resolution, -116 dBc at 20 kHz offset and -80 dBc at 10 Hz offset from 1 GHz | f_target, VCXO pull range | Low-noise signal generators | calc | p.968-969, Fig. 13.103 | high |
| AOE-4093 | control-loop | FM-demodulating PLL: loop response must be faster than the modulation (loop BW >= max modulating frequency) and the VCO should be highly linear to minimize audio distortion | BW_loop >= f_mod_max | f_mod_max, VCO linearity | PLL FM detectors | calc | p.969 | high |
| AOE-4094 | rf | Synchronous (homodyne) AM detection with an XOR (type I) PLL: the locked VCO is 90 deg from the reference, so insert 90 deg of shift in the path to the multiplier | 90 deg correction | PD type | Synchronous detection | review | p.970 | high |
| AOE-4095 | rf | BPSK has no spectral line at the carrier, so a plain PLL cannot recover it: use a squaring loop (2 f_c -> BPF -> narrow PLL -> /2 -> phase trim), a Costas loop, or a transmitted pilot tone; QPSK = 4-QAM (2 bits/symbol), 256-QAM = 8 bits/symbol | carrier recovery method present | modulation | Digital demodulators | review | p.970-971, Fig. 13.108 | high |
| AOE-4096 | rf | VCO technology tuning range vs noise: fully integrated cellphone VCOs ~5% tuning; MEMS/SAW/VCXO ~100 ppm with very low phase noise and jitter; use PLL chips with external VCOs (e.g. phase detectors to 6 GHz and beyond) for wide range or best purity | tuning range 5% (integrated LC), ~100 ppm (MEMS/SAW/VCXO) | tuning range, phase noise | Synthesizer VCO selection | review | p.971 | high |
| AOE-4097 | timing | Clock-and-data recovery PLL bandwidth: wide enough to track rate variations of the data source (tape/disk speed), narrow enough to reject cycle-to-cycle jitter of the received clock | BW between wander and jitter bands | data-rate wander spectrum | CDR (e.g. DIR9001, 28-108 ksps S/PDIF/AES3) | review | p.971 | medium |
| AOE-4098 | timing | PLL jitter transfer: reference-input jitter is lowpass-filtered, VCO jitter is highpass-filtered (removed inside loop BW), phase-detector jitter is bandpass-filtered. Clean reference -> widen loop BW; stable but noisy (transmitted) reference with clean VCO -> narrow loop BW; fractional-n divider jitter is also smoothed by narrow BW | BW choice rule | reference and VCO noise | PLL noise design | review | p.974 | high |
| AOE-4099 | components | Laser beat-note offset lock: photodetector outputs the difference frequency abs(f1 - f2); a limiting amplifier converts a 10 mV-1 V detector signal into a clean saturated 0.6 Vpp for the PLL prescaler | V_det 10 mV..1 V -> 0.6 Vpp | detector level | Optical offset locking (Fig. 13.109) | inspect | p.973-974 | high |
| AOE-4100 | test | LFSR PRBS: maximal length is 2^m - 1 states; the lock-up state (all 0s with XOR feedback, all 1s with XNOR feedback) must be excluded by initialization/reset; use tap pairs from T-4.9 (n or m - n) or three-tap sets from T-4.10 for multiple-of-8 lengths | K = 2^m - 1; maximal if 1 + x^n + x^m is irreducible and primitive over GF(2) | m, taps | PRBS generators | calc | p.975-976, Tables 13.14-13.15 | high |
| AOE-4101 | test | Standard PRBS lengths for bit-error-rate / eye-diagram testing | 2^7 - 1, 2^23 - 1, 2^31 - 1 | link type | Serial-link test | review | p.982, fn.141 | high |
| AOE-4102 | test | PRBS repeat time | T_rep = (2^m - 1)/f_clk; 32-bit at 1 MHz ~1 hour; 64-bit at 1 GHz ~6 centuries | m, f_clk | Choosing register length | calc | p.975 | high |
| AOE-4103 | filter | PRBS-derived analog noise: unfiltered PSD envelope ~ (sin x/x)^2 with lines every f_clk/K (no power at f_clk and harmonics); flat within +-0.1 dB to 0.12 f_clk, -0.6 dB at 0.2 f_clk, -3 dB at 0.44 f_clk. Lowpass at 5-10% of f_clk (simple RC: f_3dB < 1% of f_clk; sharper Butterworth/Chebyshev to use more of the band, then measure its ripple and gain) | e_n = a*sqrt(2/f_clk) V/rtHz for f < 0.2 f_clk (output swings +-a volts) | a (V), f_clk (Hz) | Bipolar (+-a) symmetric PRBS waveform | calc | p.977-979, Fig. 13.117 | high |
| AOE-4104 | filter | Noise bandwidth of a single-pole RC lowpass is (pi/2)*f_3dB; use it to predict filtered noise rms | V_rms = e_n*sqrt((pi/2)*f_3dB). Example: +-10 V PRBS at 1.0 MHz -> 14.14 mV/rtHz; RC 1 kHz -> NBW 1.57 kHz -> 560 mV rms | e_n, f_3dB | Filtered noise sources | calc | p.979, Fig. 13.118 | high |
| AOE-4105 | filter | Weighted-sum (FIR) filtering of shift-register taps with sin(x)/x weights gives a noise bandwidth that tracks the clock and reaches sub-Hz cutoffs; the finite tap count bounds the peak (crest factor), so set amplifier gains to avoid clipping | 32-tap design: cutoff ~0.05 f_clk; 1.0 Vrms into 50 Ohm (2.0 Vrms open), peak +-4.34 V into 50 Ohm -> crest factor 4.34; dc-50 kHz down to dc-0.006 Hz in 24 binary steps | tap weights, gain | Hybrid digital noise generator (Fig. 13.119) | calc | p.979-981 | high |
| AOE-4106 | test | Pseudorandom sequences mimic randomness only for draws r << K; use many feedback taps (~m/2) to reduce higher-order correlations | random-walk excursion X = [r(K - r)/(K - 1)]^0.5 vs sqrt(r) for true randomness | r, K | PRBS as noise source | calc | p.981 | medium |
| AOE-4107 | timing | When a feedback path (e.g. XOR) nearly consumes the clock period, route the clock opposite to the data flow (counter-rotating "racetrack") so the first stage's clock is usefully delayed; differential clock and data lines | 1.55 Gbps 7-bit PRBS (CG635): MC100EP52D setup 0.05 ns, hold 0, t_pd 0.33 ns typ; XOR 0.3 ns; first-stage clock delayed ~0.25 ns; each successive FF clock advances ~0.05 ns | t_pd, t_setup, T_clk | Multi-GHz discrete ECL/LVPECL logic (Fig. 13.120) | calc | p.982 | high |
| AOE-4108 | components | Hardware random-bit source: sample an avalanche-biased junction's noise (flat to ~50 MHz) with a latched comparator (~2 ns aperture) at 8x the output bit rate, XOR-fold 8 samples per output bit; expect 1-point bias of a few parts in 10^4 (provide a trim; needs >10^8 bits to measure); entropy deficit e < 0.01; post-process (encryption/shuffle) if needed | aperture 2 ns; fold 8:1; bias ~1e-4 | noise BW, sample rate | True RNG (Fig. 13.121) | measure | p.982-983 | high |
| AOE-4109 | components | Effective number of bits from SINAD | ENOB = (SINAD - 1.76 dB)/6.02; SINAD = 20*log10(S_rms/(N + D)_rms); noise-only ENOB = 1.44*ln(V_span/V_noise_rms) | SINAD (dB) | ADC characterization (ADI MT-003) | calc | p.985, fn.143 | high |
| AOE-4110 | components | DAC type selection: resistor-string (8-16 bits) is strictly monotonic (preferred inside digital control loops); R-2R needs only 2n resistors, not inherently monotonic, better INL (precise voltage setting); current-steering is fastest but compliance-limited (drive 50 Ohm, 75 Ohm video, or a current-input load; a transresistance amp limits speed); use the DAC's matched internal feedback resistor for I-to-V; MDAC capacitive feedthrough limits bandwidth at small codes | monotonic required -> string or guaranteed-monotonic | loop use, speed | DAC selection | review | p.985 | high |
| AOE-4111 | components | ADC type envelope: flash to 8 bits, to 20 Gsps (HMCAD5831 3-bit 20 Gsps); pipelined/folded to 16 bits, several Gsps, latency up to 20 clocks; SAR n steps, needs input T/H, may have missing codes; single-slope for pulse-height analysis / time-to-amplitude; dual/multislope 20-28 bits at ms speed; delta-sigma to 24 bits at a few Msps; > 250 Msps folding flash 8-12 bits to 3 Gsps | per architecture | rate, bits, latency | ADC selection | review | p.985-987 | high |
| AOE-4112 | termination | Shared parallel (multidrop) bus lines: drive with three-state or open-collector outputs; place pull-ups at the end of the bus where they also act as terminators; long buses need pull-ups even with three-state drivers | pull-up/terminator at bus end | bus length, driver type | Parallel backplane buses (PC104/ISA) | inspect | p.992 | medium |
| AOE-4113 | hw-fw | Only one device may assert a shared bus at a time; define and verify the bus-ownership protocol (who drives and when) so there is never contention | one active driver per bus cycle | timing diagram | Shared data buses | review | p.993 | medium |
| AOE-4114 | components | Memory basics for embedded design: RAM access ~100 ns; embedded MCUs 4K-64K RAM; DRAM is 1 transistor/bit and needs refresh, SRAM 6T/bit no refresh, both volatile; program in non-volatile flash/EEPROM (Harvard architecture typical); cache hit rate >= 95% in loops | K = 1024 for memory sizes | - | Processor/memory selection | review | p.991 | high |
| AOE-4115 | timing | Latch write data on the TRAILING edge of the write strobe, qualified by the decoded address; data are not guaranteed valid at the leading edge | PC104/ISA 8-bit I/O write: address valid >= 91 ns before IOW'; IOW' width >= 530 ns; data setup >= 474 ns before trailing edge, hold >= 25 ns (address hold 42 ns min) | strobe timing | Parallel bus peripherals | calc | p.998-999, Fig. 14.8 | high |
| AOE-4116 | timing | Programmed-input peripherals must drive the data bus within the read strobe with the bus-specified setup before the strobe's trailing edge | PC104/ISA read: IOR' asserted 530 ns min; peripheral data valid >= 26 ns before end of IOR' (<= 504 ns after IOR' falls); CPU latches at trailing edge | t_access vs 504 ns | ISA/PC104 read ports | calc | p.1001, Fig. 14.13 | high |
| AOE-4117 | hw-fw | Qualify all ISA/PC104 I/O address decoding with AEN LOW; AEN HIGH marks DMA cycles whose addresses are memory addresses and must not select I/O ports | decode = ADR_match AND NOT AEN | decode equation | PC104/ISA peripherals | inspect | p.998-999, p.1012 | high |
| AOE-4118 | hw-fw | Partial ("lazy") address decoding makes a peripheral respond to a range of aliased addresses; document the occupied range and check it does not collide with other devices | ignoring A1, A0 -> 4 aliases (3FCh-3FFh) | decoded address bits | Memory-mapped / port-mapped I/O | review | p.1000, fn.18 | high |
| AOE-4119 | components | Load multi-byte DAC words through double-buffered input registers and transfer them simultaneously (LDAC) so intermediate byte combinations never reach the output; delay any downstream strobe (e.g. display unblank) until the DAC has settled | AD660 16-bit: HBE'/LBE' byte loads then LDAC; z-unblank delayed ~5 us | DAC settling | Byte-wide bus to wide DAC | inspect | p.999-1000, Figs. 14.10-14.11 | high |
| AOE-4120 | hw-fw | Byte order: x86 stores multibyte quantities little-endian (low byte at the lower, even address); map LBE/HBE (low/high byte enables) to consecutive addresses accordingly | low byte at even address | endianness | Bus peripherals with multi-byte registers | review | p.1000, fn.19 | high |
| AOE-4121 | components | Never drive a bidirectional (shared) bus line with an active-pullup two-state output; use three-state (enabled only when selected) or open-collector drivers | driver type on shared lines = 3S or OC | driver type per net | Shared data buses, status bits | inspect | p.1003 | high |
| AOE-4122 | hw-fw | Give each peripheral status flags that the CPU can read; group all error flags into one "any error" bit at the word's MSB (sign test) and clear flags explicitly by command writes in complex interfaces | error summary at MSB | status register map | Peripheral register design | review | p.1003-1004 | medium |
| AOE-4123 | hw-fw | Use interrupts (not status polling) for devices that cannot wait; keep ISRs short (save registers, service, send end-of-interrupt, restore, IRET) and defer long work to main code via flags; buffer ISR-to-main data in a ring buffer | ring buffer e.g. 256 bytes; re-enable interrupts (STI) inside long handlers after critical work | ISR length, buffer depth | Interrupt-driven I/O | review | p.1005-1008 | high |
| AOE-4124 | hw-fw | Clear every interrupt-requesting flag with the bus RESET at power-up so no spurious interrupt occurs | RESET OR'ed into flag clear | reset path | Interrupting peripherals | inspect | p.1005 | high |
| AOE-4125 | hw-fw | Shared interrupt lines must be level-sensitive, active-LOW, wired-OR with open-collector (or 3-state emulating OC) drivers and one pull-up; poll status registers of all devices on a level (poll order = software priority); edge-triggered IRQs (ISA) cannot be shared | one pull-up per IRQ' line; each source individually maskable by its own I/O bit | IRQ topology | Multi-device interrupt systems | inspect | p.1008-1010, Fig. 14.17 | high |
| AOE-4126 | hw-fw | Connect latency-sensitive devices to higher-priority interrupt levels; each interrupt source must be maskable at the device (not only per level) | priority map | latency requirements | Interrupt planning | review | p.1009-1010 | medium |
| AOE-4127 | hw-fw | Use DMA for high-rate streams (disks, networks, real-time data) that cannot be serviced per-byte by interrupts; set up by programmed I/O, move by DMA, signal completion by status bit + interrupt | disk sustained rates to 500 MB/s; PC104/ISA DMA ~2 us per byte; PCIe hundreds of MB/s | data rate | I/O architecture | calc | p.1010-1012 | high |
| AOE-4128 | timing | Slow peripherals on ISA/PC104 request wait states by pulling open-collector IOCHRDY LOW before the second CLK rising edge of the cycle (normally 4 CLKs); a device asserting IOCHCK' (NMI) must expose a readable status bit | IOCHRDY LOW before 2nd CLK rise | device access time | PC104/ISA | calc | p.1012-1013 | high |
| AOE-4129 | hw-fw | DMA terminal count (TC) is asserted when ANY channel finishes; qualify it with the channel's DACK' | TC AND DACKn' | - | PC104/ISA DMA peripherals | inspect | p.1013 | high |
| AOE-4130 | emc | Use optical fiber (e.g. Ethernet media converter) instead of wire for data links from lightning-exposed sites to avoid lightning-induced damage | fiber link for exposed runs | site exposure | Outdoor/mountaintop installations | review | p.1013-1014 | medium |
| AOE-4131 | components | DRAM refresh budget: every row must be accessed within the retention interval; without refresh data are lost in < 1 s | 1 Gb DRAM: 8192 rows every 64 ms -> one row per 7.8 us average | rows, t_ref | DRAM controllers | calc | p.1015 | high |
| AOE-4132 | components | Memory selection: SRAM is simplest (no refresh), zero quiescent current, battery-backable; DRAM ~1/10 the cost per bit but needs refresh and multiplexed addressing; pseudo-static RAM = DRAM core with hidden refresh behind an async SRAM interface | fast async SRAM <= 8 ns; sync SRAM 100-400 MHz, 1-72 Mb, widths 9/18/36/72 (parity per byte); micropower SRAM ~1 uA standby, ~1 mA at 1 MHz; SRAM up to 16 Mb; PSRAM to 128 Mb, ~50 ns (~20 ns page mode), ~100 uA standby, deep power-down few uA (loses data) | speed, density, standby current | Embedded memory selection | review | p.1015-1018 | high |
| AOE-4133 | dfm | SRAM data (and address) lines may be connected in any permuted order to ease PCB routing, because data are unscrambled on readback | permutation allowed | net mapping | SRAM (not for NVM preloaded or cross-device shared data) | review | p.1017 | high |
| AOE-4134 | timing | Asynchronous SRAM read/write timing: data valid t_AA after address; write latched at end of WE' pulse after address setup t_AS | K6R4008V1D-08 (512 kB): t_AA = 8 ns, t_AS = 0 ns, WE' pulse >= 8 ns min, data setup >= 4 ns (Fig. 14.23 values) | t_AA, t_AS, t_WP | Fast SRAM interfaces | calc | p.1017, Figs. 14.22-14.23 | medium |
| AOE-4135 | components | DRAM cell physics sets sense margins: 1T1C cell C ~30 fF charged to ~1 V, bit line + sense amp ~200 fF, precharge VDD/2, designers aim for dV > 100 mV | dV = Q_cell/(C_cell + C_BL) | - | Background for DRAM behaviour | calc | p.1019, fn.32 | high |
| AOE-4136 | timing | SDRAM: the controller must program (LOAD MODE) and honor CAS latency and burst length; DDR clocks data on both edges of a differential clock | e.g. MT47H128M8HQ-25E: DDR2, CL = 5 at tCK = 2.5 ns; DDR3-1600 = 800 MHz clock; DDR3 400-1600 MT/s, 1-4 Gb/chip; DDR4 1600-3200 MT/s, >= 16 Gb | CL, tCK, burst | SDRAM interface design | calc | p.1021, Fig. 14.29 | high |
| AOE-4137 | components | Memory modules have many incompatible parameters (form factor, pins, density, width, ECC, buffering, generation, speed, CAS latency, voltage, rank, registered, parity): select from the motherboard spec / vendor configurator | e.g. DDR2 PC2-6400 CL = 4 1.9 V 240-pin | module params | Populating commercial boards | review | p.1014, fn.25 | high |
| AOE-4138 | reliability | Battery-backed "CMOS" memory: verify retention current and minimum retention voltage against the backup battery for the required hold-up time | boards lost settings after a few hours without ac due to out-of-spec leakage / retention voltage | I_ret, V_ret, battery capacity | Battery-backed RAM | calc | p.1022, fn.34 | high |
| AOE-4139 | reliability | Non-volatile memory endurance and write time: floating-gate EEPROM/flash endure 10^5-10^6 erase/write cycles, erase/write ~10 ms vs read ~100 ns, retention >= 10 years; budget write counts and use wear leveling / bad-block management for flash | N_writes_lifetime <= endurance; flash erase blocks 4-64 kB | writes per day, lifetime | Firmware storage of logs, parameters | calc | p.1022-1025 | high |
| AOE-4140 | components | Store small per-unit data (calibration constants, settings, lookup tables) in byte-rewritable EEPROM (on-chip or serial SPI/I2C/UNI/O/Microwire); use NOR flash for execute-in-place code (treat as read-only); NAND flash (with controller) for bulk storage | serial EEPROM 128 bit - 1 Mb; 1 kb I2C ~$0.17, 64 kb ~2x; NOR 1 Mb - 1 Gb; NAND to 1 Tb/IC | data size, rewrite granularity | NVM selection | review | p.1024-1027 | high |
| AOE-4141 | reliability | Multi-level-cell NAND stores 2-3 bits per ~0.3 fF floating gate; loss of ~3000 electrons over 10 years corrupts data: prefer SLC or controller-managed ECC for critical data | MLC 4 levels, TLC 8 levels | cell type | Long-retention data | review | p.1025 | medium |
| AOE-4142 | components | Emerging NVM with high endurance: FRAM (SPI/I2C to 2 Mb, 10^14 cycles; parallel MB85RE4M2T 150 ns, 10-year retention at 85 degC, 10^13 cycles); MRAM (MR2A16A 4 Mb x16, 35 ns, 20-year retention, "unlimited" endurance, ~$20); PRAM sampling (128 Mb) | endurance >= required write count | write frequency | Frequent-write non-volatile logging | review | p.1025-1026 | high |
| AOE-4143 | transmission-line | At Gb/s rates bus wires are electrically long (~20 cm/ns in cables and PCBs): multidrop stubs cause reflections and parallel-line skew limits clock rate; prefer point-to-point, impedance-matched, differential serial links with embedded clock | propagation ~20 cm/ns; SATA 6 Gb/s on 2 pairs vs PATA 1 Gb/s on 40 wires | edge rate, line length, topology | High-speed interconnect choice | calc | p.1027 | high |
| AOE-4144 | test | Eye-diagram measurement: trigger on (recovered or transmitted) clock with persistence; oscilloscope bandwidth must reach the 3rd (preferably 5th) harmonic of the clock frequency; transmit equalization reopens eyes on lossy channels | BW_scope >= 3..5 x f_clock | f_clock, scope BW | Serial-link verification (Fig. 14.33: 11.2 Gb/s over 60 cm 0.085" semi-rigid coax) | measure | p.1028 | high |
| AOE-4145 | timing | Fast parallel data links to converters: meet ns-scale setup/hold relative to an LVDS clock; configure through a separate slow serial (I2C/SPI) port | AD9748 8-bit DAC 210 Msps (new byte every ~5 ns), setup 2.0 ns, hold 1.5 ns; ADV7390 video encoder: 16-bit parallel data + I2C/SPI access to ~250 config registers | t_su, t_h | Converter data ports | calc | p.1030, Figs. 14.35-14.36 | high |
| AOE-4146 | transmission-line | Encode clock with data (e.g. 8b/10b) on high-rate serial lanes so the receiver recovers timing; encoding also gives dc balance for ac/transformer coupling | 8b/10b: never more than 5 consecutive identical bits; PCIe lane 2.5 (v1), 5 (v2), 8 Gb/s (v3), x1..x16 lanes | line code | PCIe/SATA-class links | review | p.1030, fn.43 | high |
| AOE-4147 | crosstalk | Differential signaling doubles wire count but cuts crosstalk, improves noise immunity and reduces ground/supply noise (balanced transitions), permitting smaller swings and drive currents | - | - | Cable/backplane buses (SCSI LVD) | review | p.1031, fn.45 | high |
| AOE-4148 | cables | PATA 80-wire cables interleave ground wires between signals to improve signal integrity (still limited to 133 MB/s); use ground-interleaved ribbon for fast parallel ribbon links | alternate signal/ground conductors | cable pinout | Ribbon-cable parallel links | inspect | p.1031 | high |
| AOE-4149 | requirements | Bus/link selection envelope (rate, topology, device count, cable length, hot-swap) — see T-4.13 | per Table 14.3 | rate, length, nodes | Interface selection | review | p.1029, Table 14.3 | high |
| AOE-4150 | hw-fw | SPI has no standard protocol: for each slave, take clock polarity/phase (4 SPI modes), bit count/meaning, and both max AND min SCLK from its datasheet; if slaves on one bus are incompatible, bit-bang or split buses | per-device mode, f_SCLK_min <= f_SCLK <= f_SCLK_max; AD7927: 10 kHz min, 20 MHz max | datasheet SPI params | SPI buses | review | p.1033-1034 | high |
| AOE-4151 | hw-fw | SPI topology: SCLK, MOSI, MISO bused to all slaves, one dedicated active-LOW slave-select per slave; master drives SS' then clocks; full duplex, no handshake (a master can "talk" to a non-existent chip - verify presence by readback) | one SS' per slave | device count, MCU pins | SPI buses (Fig. 14.38) | inspect | p.1032-1033 | high |
| AOE-4152 | hw-fw | I2C: two open-drain lines (SCL, SDA) with resistive pull-ups to V+; 7-bit address + R/W', ACK after every byte, START/STOP by changing SDA while SCL HIGH; register read = write register address then repeated START + read; slaves may clock-stretch; multi-master needs arbitration; assign unique addresses (address pins) | pull-ups on SCL and SDA; unique 7-bit address per bus (AD7294 pins select 61h-7Bh) | device list | I2C / SMBus (SMBus has tighter protocol and electrical specs) | inspect | p.1034-1035, Fig. 14.40 | high |
| AOE-4153 | hw-fw | Choose SPI for steady high-rate streaming and simple debugging; I2C for many register-rich devices on 2 wires (the peripheral usually dictates the choice; most MCUs support both) | - | data rate, pin budget | Inter-chip bus choice | review | p.1035 | medium |
| AOE-4154 | hw-fw | Dallas/Maxim 1-wire: single data line pulled up to +5 V also powers slaves (on-chip storage capacitor); LOW pulses encode bits: short (< 15 us) = 1, long (60 us) = 0; reset by long LOW pulse; each device has a unique factory 64-bit address incl. family byte | network <= 30 m normally, to 500 m with an appropriate driver (AN244) | cable length, device count | Remote sensors (iButton) | calc | p.1035-1036 | high |
| AOE-4155 | test | JTAG (IEEE 1149.1): TCK and TMS bused, TDI->TDO daisy-chained through devices (TDI sampled on TCK rising, TDO changes on falling), optional TRST; 1-100 Mb/s; used for boundary-scan test, in-circuit programming and debug of MCUs, CPLDs, FPGAs, flash; header pinout is vendor-specific - provide the vendor's header or an adapter | chain order documented; header per programmer pod | device chain | Programming/test access | inspect | p.1036-1037, Fig. 14.43 | high |
| AOE-4156 | transmission-line | Recover the clock from data (CDR) on fast links to eliminate clock-data skew; requires line coding with guaranteed transitions | - | bit rate | Serial link design | review | p.1037 | high |
| AOE-4157 | power | eSATA devices need separate power; SATA/SAS hot-swap requires OS support; SATA/SAS 6 Gb/s (12 Gb/s path) over LVDS with 8b/10b | - | - | Storage interfaces | review | p.1037 | high |
| AOE-4158 | stackup | PCIe routing load: each lane is two LVDS pairs (one per direction); an x16 slot = 32 pairs (64 wires) at 5 Gb/s raw each (4 Gb/s payload after 8b/10b, v2.0); two x16 slots need 128 wires; inexpensive motherboards use ~6 wiring layers with 0.12 mm (5 mil) traces | pairs = 2 x lanes per link | lane count | High-speed PCB planning | calc | p.1037 | high |
| AOE-4159 | timing | Parallel-bus speed history and limit: PCI 32 bit x 33 MHz = 133 MB/s; PCI-X 64 bit x 133 MHz ("1064 Mb/s" printed; = 1064 MB/s); further gains blocked by skew and multidrop stub reflections -> point-to-point serial (PCIe) | BW = width x f_clk | - | Background for bus choice | calc | p.1037 | medium |
| AOE-4160 | components | Asynchronous serial (UART) framing: idle = mark (1); START (0), 5-8 data bits LSB first, optional parity, 1-2 STOP bits; 8N1 uses 10 bit-times per byte -> payload = baud/10 bytes/s; receiver samples mid-bit after re-syncing on each START, so combined clock error must stay within a fraction of a bit over one character (a few percent) | 9600 baud 8N1 -> 960 bytes/s; clock tolerance ~few % total | baud, framing, clock ppm | UART links | calc | p.1038, Fig. 14.44 | high |
| AOE-4161 | cables | RS-232 levels are bipolar: mark/logic 1 = -5 to -15 V, space/logic 0 = +5 to +15 V; physical layer not standardized (connector gender, handshake, DTE/DCE) - specify pinout per Table 14.4 and test the cable; for runs to ~1 km or multidrop use RS-422/485, fiber, or 20 mA current loop | levels per above | DTE/DCE roles | RS-232 ports | inspect | p.1038-1039, Table 14.4 | high |
| AOE-4162 | components | Manchester (biphase-level) code: mandatory mid-cell transition (1 = LOW->HIGH), dc-balanced for transformer coupling, 100% bandwidth overhead; receiver phase ambiguity resolved by mixed data. Biphase-mark adds polarity-inversion immunity (AES3, S/PDIF, Toslink) | f_line = 2 x bit rate | code choice | Self-clocked links (10Base-T) | review | p.1040-1041, Fig. 14.46 | high |
| AOE-4163 | components | Run-length limiting: NRZ/NRZI alone allows long transition-free runs (breaks clock recovery and transformer coupling); USB NRZI bit-stuffs a 0 after six 1s (worst-case overhead 16%, < 1% for random data); CD EFM 8-to-14 with 2 <= RL <= 10; DVD EFMPlus 8-to-16 | max run = 6 (USB) | code | Serial line codes | calc | p.1041 | high |
| AOE-4164 | components | 8b/10b code: 25% overhead, max 5 consecutive identical bits, running disparity keeps 1s/0s within 2 over any 20+ bits; used by FireWire, SATA/SAS, GbE, DVI/HDMI, PCIe v1/v2; 4b/5b (25% overhead) in 100 Mb/s Ethernet | RL <= 5; abs(disparity) <= 2 per >= 20 bits | code | High-speed serial | review | p.1041-1042 | high |
| AOE-4165 | components | SERDES options: 8b/10b-coded (e.g. CY7C924) vs framed NRZ with start/stop (e.g. DS92LV18, 18 bits to 1.2 Gbps) which locks to random data without training patterns or a loss-of-lock back-channel; FTDI FT245/FT2232 bridge USB to byte-wide FIFO ports | - | - | Parallel-over-serial links | review | p.1032, p.1042 | high |
| AOE-4166 | power | USB bus power budget: a device may draw only low power (100 mA at 5 V) until it negotiates high power (500 mA, USB 2.0; 900 mA USB 3.0); USB 3.1 permits up to 10 W at 5 V and 100 W at 20 V (5 V at 2 A, or 5 A at 12 V or 20 V); use a protected power switch for the high-power rail | I_enum <= 100 mA; I_config <= 500 mA (USB 2.0) | device current profile | USB-powered products | calc | p.1042, fn.62 | high |
| AOE-4167 | cables | USB topology limits: tiered star, up to 127 devices per host controller, up to five hub tiers, each cable <= 5 m (passive extenders included), total reach ~20 m via hubs; USB 3.0 cable <= 3 m (Table 14.3); hot-plug connectors mate ground and power before signals | L_link <= 5 m | cable plan | USB installations | inspect | p.1042, Fig. 14.47 | high |
| AOE-4168 | power | FireWire (IEEE 1394) supplies up to 45 W and 30 V through its cable; links <= 4.5 m (FireWire 400), up to 72 m through repeaters; 400 or 800 Mb/s full duplex | P <= 45 W, V <= 30 V | - | FireWire-powered devices | review | p.1042-1043 | high |
| AOE-4169 | termination | CAN bus physical layer: shielded twisted pair terminated at BOTH ends in its characteristic impedance (usually 120 Ohm); up to 30 nodes; 1 Mb/s up to 40 m, falling to 10 kb/s at the maximum 1000 m; recessive (logic 1) both lines ~2.5 V, dominant (logic 0) CANH ~3.5 V / CANL ~1.5 V (~2 V differential) | R_term = Z0 (~120 Ohm) at each end; bit rate vs length per above | length, bit rate, nodes | ISO 11898 CAN (Fig. 14.48-14.49) | inspect | p.1043-1044 | high |
| AOE-4170 | protection | CAN transceivers must tolerate common-mode -2 V to +7 V (many parts -7..+12 V or -12..+12 V) and survive ISO 7637 +-150 V ns-scale pulse trains; add low-cost diode/zener protectors (NUP2105/NUP2202); on long runs use galvanically isolated transceivers (e.g. ISO1050) so there is only one ground point, powering the bus side from the cable's power pair | V_cm range; ISO 7637 pulses | environment | Automotive/industrial CAN | review | p.1044-1045, Fig. 14.50 | high |
| AOE-4171 | hw-fw | CAN messaging: <= 8 data bytes per frame, 11- or 29-bit identifier, lowest identifier wins non-destructive bitwise arbitration (dominant overrides recessive); built-in bit monitoring, stuff-bit check (opposite bit after 5 identical), CRC, ACK and form checks; use for short broadcast data, not bulk streams | payload <= 8 bytes | message set | CAN / DeviceNet | review | p.1043-1044 | high |
| AOE-4172 | components | Simplified CAN variants: single-wire CAN <= 40 kbps; LIN (pull-up to +12 V battery, open-collector to ground) <= 20 kbps; both slew-rate limited for noise immunity; no standard CAN connector (DB-9, 10-pin header, 4-pin open are common); CAN cables with power pair (Belden 3082/84, Alpha 6451/52) | rates per above | - | Automotive sub-buses | review | p.1045 | high |
| AOE-4173 | cables | Ethernet media limits: twisted-pair (Cat-5e/Cat-6 UTP) links ~100 m; fiber ~1 km multimode, tens of km single-mode; thin-coax (10Base2) ~200 m legacy with minimum packet 74 bytes (printed) per IEEE 802.3; use switches (collision-free) not hubs; 10Base-T Manchester 2-level, 100Base-TX 4b/5b 3-level, 1000Base-T all four pairs bidirectional via hybrids (fn.60: 5-level signaling; §14.7.16 text says 8b/10b coding) | L_UTP <= 100 m | link length | Ethernet links | inspect | p.1045-1046, fn.60 | high |
| AOE-4174 | power | Power over Ethernet: ~48 V dc applied common-mode ("phantom") between two pairs, picked off at transformer center taps at the far end | V_PoE ~48 V | device power | Remote APs, IP phones, cameras | review | p.1046, fn.73 | high |
| AOE-4175 | timing | IEEE 1588 Precision Time Protocol over Ethernet synchronizes clocks to ~100 ns with dedicated MAC/PHY hardware support (e.g. DP83640); LXI uses it for LAN instruments | sync ~100 ns | - | Distributed timing | review | p.1046, fn.74 | high |
| AOE-4176 | hw-fw | Store ADC results left-justified as fractions of full scale so a later higher-resolution converter only adds LSBs; signed integers are 2's complement (int8 -128..+127, int16 -32768..+32767, int32 -2147483648..+2147483647) | - | data format | Firmware data paths | review | p.1046-1047, Fig. 14.51 | high |
| AOE-4177 | hw-fw | IEEE 754-2008 floating-point ranges: half (binary16) +-6.1e-5..+-6.6e4 (max 65504, ~0.06% step, uniform fractional resolution over 9 decades); single +-1.2e-38..+-3.4e38 (denormals to +-1.4e-45); double +-2.2e-308..+-1.8e308; quad +-3.4e-4932..+-1.2e4932; biased exponent (single: +127) and hidden leading 1 | V = (-1)^s x 1.fff x 2^(e - bias); bias 15/127/1023/16383 | format | Numeric representation | calc | p.1047-1048, Fig. 14.51 | high |
| AOE-4178 | hw-fw | Byte order differs across processors (Intel little-endian, Motorola/Freescale big-endian, ARM bi-endian; some differ between integer and float): specify byte order explicitly for every multi-byte field sent over SPI/I2C/links | endianness declared per field | protocol spec | Inter-processor / peripheral data | review | p.1048 | high |
| AOE-4179 | reliability | MCU non-volatile memories have limited rewrite endurance: store frequently changed user data in EEPROM (byte-erasable), not program flash (block erase) | typical MCU flash 10,000 erase/write cycles vs EEPROM 100,000 (PIC16F627 EEPROM guarantees 1,000,000) | write frequency | Embedded parameter storage | calc | p.1053 fn.2, p.1062 | high |
| AOE-4180 | test | Provide an in-circuit programming/debug header (ICSP via SPI, JTAG, or vendor 1-/2-wire) on every MCU board, since embedded MCUs are not removable | header present and matched to pod | MCU family | All MCU designs | inspect | p.1053, §15.9.3 | high |
| AOE-4181 | components | Current-input sensing with an MCU: integrate the sensor current on a capacitor, detect threshold with the on-chip comparator and discharge (current-to-frequency) instead of I->V->ADC; accuracy at low current then does not need a low-offset amplifier | f = I/(C*V_th); counts integrate dose | I range, C, V_th | Photodiode dose monitors (Figs. 15.2-15.3) | calc | p.1054-1055 | high |
| AOE-4182 | components | Worst-case leakage of the discharge switch must be << the smallest signal current: MCU 3-state pins specify up to +-1 uA leakage -> use an external small MOSFET | BSS123: ~0.5 A at 2.5 V VGS, worst-case leakage 10 nA at VDS = 20 V, ~$0.05; comparator input leakage 50 nA max; photocurrent ~1 uA full sunlight | I_leak(T_max) vs I_signal_min | Charge-integrating inputs | calc | p.1055 | high |
| AOE-4183 | thermal | Evaluate semiconductor leakage at the maximum design temperature: leakage roughly doubles every 10 degC | I_leak(T) = I_leak(25 C)*2^((T - 25)/10); BSS123 50 nA typ at 25 degC -> 3.2 uA at 85 degC (64x); photodiode dark current 50 pA -> ~3 nA at 85 degC | T_max (85 degC here) | Low-current circuits, outdoor products | calc | p.1059 | high |
| AOE-4184 | power | Power resistive dividers/pots from a GPIO only while reading them, so their bias current can be large relative to ADC input leakage (1 uA spec) without draining the battery | divider current >> 1 uA only during conversion | duty, divider current | Battery MCU designs | review | p.1055 | high |
| AOE-4185 | decoupling | MCU analog supply: isolate AVCC from digital VCC with the LC (or RL) filter recommended in the datasheet; bypass pot/sensor readouts biased from noisy digital outputs; parallel a small ceramic (100 nF) with larger bypass caps to keep impedance low over frequency | e.g. 1 uH + 100 nF on AVCC; 100 nF // 1 uF on VCC | datasheet recommendation | MCU with on-chip ADC | inspect | p.1056, p.1072 | high |
| AOE-4186 | timing | MCU internal RC oscillators are coarse: use them only when timing tolerance permits; UART 8N1 needs a crystal or ceramic resonator | internal oscillators +-10% (AVR 8 MHz/128 kHz), +-7% (PIC16F627) -> inadequate for 8N1; 3-pin ceramic resonator with caps +-0.5% (~$0.40) OK | clock tolerance | Serial comms, timing | calc | p.1056, p.1063 | high |
| AOE-4187 | hw-fw | Firmware setup checklist: configure port directions and pull-ups, disassert outputs that drive relays/heaters before enabling them as outputs, configure ADC/comparator references and modes, disable unused peripherals and digital input buffers on analog pins (power), enable brownout reset and watchdog; configuration "fuse" bits (clock source, brownout level, debug, JTAG/SPI enable, watchdog) are set at programming time | init order per above | MCU register map | All MCU firmware | review | p.1056-1057, p.1064-1065 | high |
| AOE-4188 | hw-fw | Declare memory-mapped I/O variables volatile so the compiler cannot optimize away re-reads; beware compilers optimizing away inline assembly | volatile on every hardware register variable | source code | Embedded C | inspect | p.1057, p.1087 fn.49 | high |
| AOE-4189 | hw-fw | Allow for reference start-up time before using on-chip analog references | AVR bandgap reference needs 70 us to settle | t_settle | MCU analog | review | p.1057, Program 15.1 | high |
| AOE-4190 | hw-fw | Keep a hard power switch (or reset) even on sleep-capable designs: a crashed processor must be recoverable without removing the battery; use a watchdog and reset supervisor | sleep < 1 uA with level-interrupt wake | recovery path | Battery products | review | p.1057, p.1086 | high |
| AOE-4191 | requirements | Hold a human-interface review against the specification (e.g. whether a knob adjusted mid-cycle takes effect) and a design review including the thermal environment (sun-baked equipment design temperature 85 degC) before shipping a consumer product | HI test + design review gates | spec | Consumer products | review | p.1059 | medium |
| AOE-4192 | components | Solid-state relays for ac switching from logic: input 3-15 or 3-32 Vdc at 3-15 mA, isolation 3.5-5 kV, zero-voltage turn-on/zero-current turn-off, typ 10-20 A at 280 Vac (to 100 A, 660 Vac); SSR dissipates ~10 W at 10 A -> heat-sink it; a mechanical relay (e.g. 16 A/277 Vac, 80 mA coil via transistor, $1.60) is far cheaper than an SSR ($35) | P_SSR ~= 1 W/A | I_load | Mains load control (Fig. 15.4) | calc | p.1062-1063 | high |
| AOE-4193 | hw-fw | Drive SSRs/LEDs from MCU pins in the sinking (active-LOW) direction: port pins pull down harder than up | ~0.35 V saturation sinking 15 mA vs ~1.3 V below rail sourcing 15 mA (PIC16F627) | I_drive | GPIO drive of loads | calc | p.1062 | high |
| AOE-4194 | protection | SSR off-state leakage (0.1-10 mA spec; measured ~2 mA) can energize light loads and indicators: bridge the SSR output with a bleeder (15 kOhm, 2 W) which also powers the "load on" LED and an ac-input optocoupler for output verification | worst-case leakage 10 mA (D2425) / 100 uA (EZ240D18); bleeder ~8 mA when on | I_leak, load | SSR outputs (Fig. 15.4) | calc | p.1062 | high |
| AOE-4195 | components | Verify switched ac is actually present with an ac-input optocoupler (back-to-back LEDs; e.g. FOD814A 5 kV, CTR >= 50%, ~$0.25) rather than trusting the command bit | readback of ac presence | - | Remote power control | inspect | p.1062 | high |
| AOE-4196 | hw-fw | Hold an optocoupler-driven input LOW across the ~1 ms LED-off gaps near ac zero crossings with a capacitor sized against the pull-up current; MCU internal "weak" pull-ups (50-400 uA) are too strong - use external ~50 uA pull-ups | C >= I_pullup*t_gap/dV; 0.4 mA x 1 ms / 0.4 V -> 1 uF; 50 uA -> 0.1 uF | I_pullup, t_gap, V_IL | Opto ac-detect inputs | calc | p.1064 | high |
| AOE-4197 | components | RS-232 from a single 5 V rail: charge-pump translators (MAX202 with four 0.1 uF caps, ~$0.75; MAX203 internal caps ~$5; MAX3232E 15 kV ESD, 3.3/5 V); for USB use a bridge (FT232R ~$4) instead of implementing USB device classes; Ethernet-serial module (Lantronix XPort ~$50) | - | - | MCU host links | review | p.1063-1064, p.1081 | high |
| AOE-4198 | hw-fw | Debounce mechanical switches in software (e.g. ignore further changes for 10 ms after the first detected edge); optical encoders give bounce-free quadrature | t_debounce = 10 ms | switch type | Panel inputs | review | p.1064, p.1066 | high |
| AOE-4199 | hw-fw | Service the watchdog ("kick"/"pet") only from the main loop so a hung loop causes reset; enable brownout reset | watchdog timeout e.g. 1 s | loop period | All MCU firmware | review | p.1064, Pseudocode 15.2-15.3 | high |
| AOE-4200 | hw-fw | Keep ISRs short and never wait on a slow peripheral inside one; for instrument command sets consider SCPI syntax (e.g. MEASure:VOLTage:DC?) | ISR without busy-waits | ISR design | Instrument firmware | review | p.1065, fn.22 | high |
| AOE-4201 | filter | DDS output requires a reconstruction lowpass: the lowest spur is at f_ref - f_out; use a sharp (elliptic) LC filter below f_ref - f_out_max, differential if the DAC outputs are differential currents | AD9954: f_ref = 400 MHz, f_out 0-160 MHz, filter fc ~180 MHz; 32-bit tuning word -> ~0.1 Hz steps; 14-bit DAC; 14-bit phase word = 0.22 deg steps | f_ref, f_out_max | DDS synthesizers | calc | p.1065-1068 | high |
| AOE-4202 | timing | Phase-coherent multi-channel DDS requires a common reference clock to all DDS chips | shared f_ref | clock tree | Multi-channel synthesizers | inspect | p.1068 | high |
| AOE-4203 | test | Use MCU non-volatile memory to store a user/factory calibration table (e.g. measured output amplitude vs frequency and setting) and interpolate from it at run time | cal table in NVM | cal points | Programmable instruments | review | p.1067, p.1069 | medium |
| AOE-4204 | hw-fw | Keypad as row/column matrix saves pins (r + c instead of r x c) but ghosts with three or more simultaneous presses: scan by pulling columns LOW one at a time and reading pulled-up rows | N_pins = r + c | key count, simultaneous-press need | Keypads (Fig. 15.8) | calc | p.1068 | high |
| AOE-4205 | components | Temperature sensor selection: thermocouple 20-40 uV/degC; thermistor ~-4%/degC; silicon diode IC -2.1 mV/degC; Pt RTD 100 Ohm at 0 degC, +0.385%/degC, -200..+600 degC, best stability and linearity | Pt100: 80.31 Ohm at -50 degC, 157.33 Ohm at +150 degC (tables accurate to a few tenths Ohm) | range, stability | Temperature sensing | review | p.1070, fn.26 | high |
| AOE-4206 | thermal | Limit RTD excitation to keep self-heating negligible and use a 4-wire (Kelvin) connection | 2 mA bias -> 160-320 mV across 80-160 Ohm, max 0.6 mW self-heating | I_bias, R_RTD | RTD front ends (Fig. 15.10) | calc | p.1070 | high |
| AOE-4207 | components | Bridge the RTD against a reference so the differential signal is zero at mid-range and amplify the difference; use ratiometric referencing so the reference need not be precise | +-80 mV span for -50..+150 degC (null at +50 degC); ADuC848 16-bit, chop mode 15 bits on +-80 mV at 50 conv/s (~6 m-degC); offset 3 uV, 0.01 uV/degC vs AD623 in-amp 25 uV, 0.1 uV/degC | span, resolution | Precision temperature control | calc | p.1070-1072 | high |
| AOE-4208 | components | Single-supply in-amp mapping a small differential signal to a unipolar ADC: input CM range must include the negative rail; tie REF to ADC mid-scale | AD623: +3 to +12 V single supply, RRO; REF = +1.25 V maps +-80 mV to 0-2.5 V | V_CM, V_REF | In-amp -> ADC (Fig. 15.11) | calc | p.1071 | high |
| AOE-4209 | control-loop | Heater drive options: bang-bang (limit-cycles about setpoint), linear (dissipates in pass device), PWM (proportional with switch efficiency); slow thermal plants may use PWM at Hz rates with relays | PWM freq e.g. 10 kHz electronic; Hz-range with relay for large thermal mass | plant time constant | Thermal control | review | p.1070, fn.25 | high |
| AOE-4210 | control-loop | Digital PWM resolution = f_clk/f_PWM steps of 1/f_clk | ADuC848: 12.58 MHz / 1258 (04EAh) = 10 kHz PWM, 80 ns steps (~10.3 bits) | f_clk, f_PWM | MCU PWM | calc | p.1072, Fig. 15.12 | high |
| AOE-4211 | components | Drive power MOSFET gates from a dedicated gate driver (not MCU pins) to full VGS: MCU pins source/sink only mA (e.g. 1.6 mA sinking at 0.4 V, 80 uA sourcing at 2.4 V) | TC4428 dual 1.5 A driver; IRFZ44 55 V/36 A, Ron <= 14 mOhm at VGS = 10 V, 12 V gate drive | I_gate, Q_gd | PWM power stages | review | p.1073, Exercise 15.4 | high |
| AOE-4212 | thermal | MOSFET PWM switch losses: conduction I^2*Ron*D; switching ("class-A") per ramp E = Vp*Ip*t_ramp/6, two ramps per cycle, t_ramp ~ Q_gd/I_gate; repetitive avalanche from an output inductor P = (1/2)*L*I^2*f_sw | example: Q_gd = 15 nC with 10 mA gate drive -> 580 mW switching vs 320 mW conduction (10 kHz); avalanche contribution 115 mW; 1.5 A driver makes switching loss negligible | Vp, Ip, Q_gd, I_gate, L, f_sw | Hard-switched MOSFETs | calc | p.1073-1074, fn.33 | high |
| AOE-4213 | derating | Check single-pulse avalanche energy against the datasheet rating with margin; if the margin is < 20x, verify pulsed dissipation with the transient thermal impedance curves | E_AS = (1/2)*L*I^2 << 86 mJ (IRFZ44 max) | L, I | Inductive turn-off without clamp | calc | p.1074, fn.34 | high |
| AOE-4214 | emc | Add an LC output filter after a hard-switched PWM stage to limit slew rate and RFI (corner well above PWM frequency, below RFI band), accounting for the inductive kick it adds at turn-off | f_c = 1/(2*pi*sqrt(LC)) ~ 0.5 MHz; suppress RFI above ~1 MHz | L, C, f_PWM | PWM heater/motor drives (Figs. 15.10, 15.13) | calc | p.1073-1074 | high |
| AOE-4215 | thermal | Size an SMT MOSFET without heatsink by its junction-to-ambient resistance on the specified copper area | IRFZ44S: R_thJA = 40 degC/W on 6 cm^2 copper -> ~1 W budget; ~1/3 W conduction budget -> ~5 A max | P_total, R_thJA, T_amb | SMT power switches | calc | p.1074 | high |
| AOE-4216 | control-loop | PID tuning procedure: (a) I, D off, raise P until oscillation then back off; (b) add D until step response is critically damped; (c) add I for minimum settling time (Ziegler-Nichols is an alternative); implement at a fixed sample interval with derivative on measurement and some derivative filtering | P = kP(Tset - Tn); I = I + kI(Tset - Tn); D = -kD(Tn - Tn-1); PWM = P + I + D; loop period e.g. 10 ms | kP, kI, kD, T_s | Digital PID (Pseudocode 15.4) | sim | p.1074-1075, Fig. 15.14 | high |
| AOE-4217 | control-loop | Nonlinear "take-back-half" controller: pure integral control, and at each zero crossing of the error reset the output to the average of its current value and the value at the previous crossing; single tuning knob, but a tuned PID performs considerably better | 1 knob (integrator gain) | - | Plants with unknown dynamics | sim | p.1075-1076, Figs. 15.15-15.16 | high |
| AOE-4218 | protection | Include an independent resettable thermal cutout in heater loops to protect against hardware or firmware failure | hardware cutout in series with heater | T_cutout | Heater controllers (Fig. 15.10) | inspect | p.1071, Fig. 15.10 caption | high |
| AOE-4219 | control-loop | Balance-type (inverted-pendulum) control: tilt from 2-axis accelerometer (45 deg mounted) for P and I terms, gyro rate for D; fixed 100 Hz loop heartbeat from a hardware timer; expect heuristic patches (start-up boost, dead-zone correction, load-dependent gains) | loop rate 100 Hz | sensor set | Stabilized platforms (Figs. 15.17-15.19) | review | p.1077-1078 | medium |
| AOE-4220 | protection | Protect MCU logic inputs brought to the outside world against ESD with separate (user-repairable) input gates or buffers so the programmed MCU survives | buffer between connector and MCU pin | exposed inputs | External logic inputs | inspect | p.1081 item 6 | high |
| AOE-4221 | power | USB host ports need a current-limited power switch (500 mA per port, e.g. AP2156); isolate USB when grounds differ (ADuM4160; Linduino LTM2884: 560 V peak / 2.5 kVrms 1 s, isolated 5 V at 500 mA) | I_limit = 500 mA/port | port count | USB hosts | inspect | p.1081 item 22-23, p.1092 | high |
| AOE-4222 | cables | DMX512 lighting links: RS-485 at 250 kbaud over 120 Ohm twisted pair with 5-pin XLR connectors, to 1200 m, terminated at near and far ends, isolated transceiver recommended | R_term = 120 Ohm both ends; L <= 1200 m | cable, length | Theater lighting control | inspect | p.1081 item 24 | high |
| AOE-4223 | hw-fw | I2C bus capacitance must not exceed 400 pF (I2C spec v2.1); I2C uses open-drain wired-AND lines with pull-up resistors | C_bus <= 400 pF | trace + pin capacitances | I2C buses | calc | p.1081 item 26 | high |
| AOE-4224 | hw-fw | Save MCU pins for SPI chip selects with a 3-to-8 decoder ('LVC138); name SPI signals unambiguously MOSI/MISO (datasheet SDI/SDO/DI/DO naming is relative to each chip); some SPI slaves use one bidirectional data pin | 3 pins -> 8 CS' | slave count | SPI buses | review | p.1082 | high |
| AOE-4225 | components | SD/miniSD/microSD cards can be driven directly over SPI (socket only); pin 1 is CS' and also card-detect (50 kOhm pull-up in card) | pull CS' low to enter SPI mode | - | MCU data logging | inspect | p.1082 item 33 | high |
| AOE-4226 | components | Digital pots have accurate ratios (~1%) but poor absolute resistance tolerance (~20%) and low voltage ratings; use digital resistors (e.g. AD5292, 1%, to +-16 V) where absolute value matters | ratio ~1%, R_abs ~20% | use as divider vs rheostat | Digital trims | review | p.1082 items 35-36 | high |
| AOE-4227 | components | Useful MCU peripheral facts: MAX31855 thermocouple converter with cold-junction compensation (7 types, 0.25 degC resolution, -270..+1372 degC); DAC161S997 16-bit 4-20 mA loop DAC; LDC1000 inductance sensor 5 kHz-5 MHz; AD7745 24-bit capacitance 4 aF resolution, +-8 pF range; AD7147 1 fF touch sensing (13 inputs); RTC PCA8565 0.65 uA at 1.8-3.3 V | per part | - | Peripheral selection (Figs. 15.20-15.22) | review | p.1082-1086 | high |
| AOE-4228 | pdn | Low-voltage MCU cores present ns-scale load steps from standby to full current: supply them from efficient buck/point-of-load converters with low output impedance and good step response and use liberal SMT bypass capacitors | Z_out low over load-step bandwidth | dI/dt, Z_target | MCU/processor PDN | review | p.1086 §15.8.4A | medium |
| AOE-4229 | power | Multiple supply rails: provide logic-level translation between domains, seamless battery/ac-adaptor switchover with charging/protection, and correct power-up/power-down sequencing supervised by a reset supervisor with watchdog | supervisor + sequencing | rails | Mixed-voltage embedded systems | review | p.1086 §15.8.4B-E | medium |
| AOE-4230 | timing | Real-time bit-banged serial capture: compute worst-case loop timing against the peripheral's clock HIGH time and data-valid hold; if margin is thin, add a capture flip-flop or shift register rather than a faster CPU | LTC1609 internal-clock mode: 150 ns clock period, 75 ns HIGH, 40 ns data hold -> loop of 4 single-cycle instructions needs ~30 MHz CPU with only ~5 ns worst-case margin; a D-FF ('LVC1G74) on CLK rising edge adds ~35 ns; two '595 shift registers reduce software to < 10 instructions per 5 us | t_loop, t_high, t_hold | Software-timed interfaces | calc | p.1088-1089, Fig. 15.23 | high |
| AOE-4231 | timing | Command the next multiplexer channel/PGA gain immediately after starting the current conversion so settling overlaps conversion | PGA settle 2 us + ADC acquisition 2 us before next CONV'; ~200 ns after CONV' before data starts | t_settle, t_acq | Multiplexed ADC sequencing | calc | p.1088 | high |
| AOE-4232 | hw-fw | For standard serial protocols (UART, I2C, Ethernet, USB) use MCU hardware peripherals or an external bridge (e.g. FTDI), not bit-banged firmware | hardware peripheral present | protocol | Protocol implementation | review | p.1089 | high |
| AOE-4233 | hw-fw | Avoid bricking MCUs: never disable the only programming port (e.g. SPI) in early firmware, never select a clock-source fuse that does not match the fitted oscillator; prefer MCUs that boot from an internal oscillator; keep high-voltage parallel programming as a recovery path | programming port stays enabled; fuse matches hardware | fuse settings | MCU programming | review | p.1091 §15.9.3H | high |
| AOE-4234 | hw-fw | UART bootloaders need logic-level (not RS-232) signals: use a MAX232-type translator from a PC COM port, or a USB-to-UART bridge (FT232R) that matches MCU logic levels; some bootloaders require a pin asserted at reset (AVR SPI programming asserts RESET') | bootloader entry pin plan | MCU | Field reprogramming | inspect | p.1090-1091 | high |
| AOE-4235 | requirements | Use a microcontroller when the system has a character/graphic display, configurable chips, host/network/wireless communication, computation or format conversion, calibration/linearization, event sequencing, or expected upgrades; use PLD/FPGA for critical timing or high parallelism (usually alongside an MCU/soft core) | decision list | feature list | Architecture choice | review | p.1093 | high |
| AOE-4236 | requirements | MCU selection: prefer a family your team already has tools and experience for; then compare ports, internal peripherals, speed, flash/EEPROM/SRAM, packages, power modes, and toolchain; start with the premium (largest) family member; favor flat memory maps and good libraries | criteria list | requirements | MCU choice | review | p.1094 | high |
| AOE-4237 | hw-fw | Use MCU hardware timers routed to output pins to trigger external devices (e.g. ADC conversions) at precisely constant intervals rather than software timing | timer-output trigger | sample-rate jitter need | Periodic sampling | review | p.1088, p.1096 (review 15E) | high |
| AOE-4238 | requirements | Schematic must be unambiguous: every part has a reference designator and value/type; pin numbers outside the symbol, signal names inside; polarities marked | 100% of parts with refdes + value | schematic | Schematic capture/review | inspect | p.1101, App. B.1-B.2 | high |
| AOE-4239 | requirements | Schematic connectivity conventions: junctions shown by heavy dots, crossings without dots (no "jog"); never join four wires at one point (a missing dot changes the circuit); same symbol for same device type; wires horizontal/vertical | no 4-way junctions | schematic | Schematic drawing | inspect | p.1101, App. B.2 | high |
| AOE-4240 | requirements | Schematic layout conventions: signal flow left to right; positive supplies at top, negative at bottom; use ground/supply symbols rather than routing to common rails; keep functional blocks distinct and drawn in recognizable form (e.g. differential pair, flip-flop inputs left/outputs right) | layout rules | schematic | Schematic readability | inspect | p.1101-1103, App. B.1, B.3 | medium |
| AOE-4241 | requirements | Schematic content checklist: label signal lines (e.g. RESET', CLK) and show key waveforms; label non-obvious boxes (comparator vs op-amp); show unusual power connections (e.g. single-supply op-amp V- = ground) and disposition of unused inputs; include an IC table (part, type, power pins); title block (circuit, instrument, drawn by, designed/checked by, date, assembly number) and revision block (rev, date, subject) | all items present | schematic | Release documentation | inspect | p.1103, App. B.3 | high |
| AOE-4242 | cost | Default to 1% resistors: they cost hardly more than 5% parts and come in E96 values (96 per decade, ~2% spacing; 481 values 10 Ohm-1 MOhm); E192 for 0.1% parts; E24 for 5%, E12 for 10% | 0603 thick film: $0.025 (1%) vs $0.023 (5%) in qty 200 (~3x in qty 10, ~1/5 in 5000-reel) | tolerance class | BOM value selection | review | p.1104, App. C.2, fn.1 | high |
| AOE-4243 | dfm | SMT chip size code = length x width in units of 0.010 in (0603 = 0.06 x 0.03 in = 1.5 x 0.75 mm); prefer 0603 or 0805 for hand-prototyped boards; 0402, 0201, 01005 need a microscope | size code -> mm = code_digits x 0.254 | package | Prototype assembly | inspect | p.1104, App. C.1 | high |
| AOE-4244 | components | Resistor technology selection: metal-film (axial) or thick-film (SMT) for general use; thin-film for better accuracy/stability (incl. cryogenic); wirewound for power; metal-oxide above ~10 MOhm; ceramic or carbon-composition (not film) for high peak power/pulse; bulk metal foil for best stability and TC | per type | power, pulse, TC, value | Resistor selection | review | p.1105, App. C.4 | high |
| AOE-4245 | components | Resistor voltage coefficient matters at high voltage: 5 ppm/V gives 0.1% change over a 200 V range | dR/R = VCR x V | VCR, V | High-voltage dividers | calc | p.1106, Table C.1 note | high |
| AOE-4246 | components | Read resistor markings: color bands = 2 or 3 significant digits + multiplier + tolerance; printed codes use same digits + multiplier with a tolerance letter suffix (F 1%, G 2%, J 5%, K 10%, etc.) | yellow-violet-orange-gold = 47 kOhm +-5%; yellow-white-white-black-brown = 499 Ohm +-1% | marking | Incoming inspection, rework | inspect | p.1105, Fig. C.1 | high |
| AOE-4247 | components | Thevenin/Norton equivalents of any linear two-terminal source network: determine by analysis or by measuring open-circuit voltage and short-circuit current | V_Th = V_oc; R_Th = V_oc/I_sc; Norton I_N = I_sc, R_N = R_Th | V_oc, I_sc | Source/load interaction, drive analysis | calc | p.1107-1108, App. D | high |
| AOE-4248 | components | Millman's theorem for parallel branches (summing resistor networks, dividers) | V_out = (sum_i V_i*G_i + sum_k I_k)/(sum_i G_i), G_i = 1/R_i (current-source series resistances excluded from denominator) | V_i, R_i, I_k | Resistive summing networks | calc | p.1108, Fig. D.8 | high |
| AOE-4249 | filter | Use passive LC filters (not active) at ~100 kHz and above (op-amp slew/bandwidth limits); at UHF/microwave use stripline/cavity filters | f >= 100 kHz -> LC | f_c | Filter technology choice | review | p.1109, App. E | high |
| AOE-4250 | filter | LC Butterworth lowpass design by table scaling: pick order from the Butterworth response, choose pi (fewer inductors; use when R_load << R_source) or T (use when R_load >> R_source); equal terminations can use either | L = R_L*L_table/omega; C = C_table/(omega*R_L); omega = 2*pi*f_-3dB; tables normalized to 1 Ohm load, 1 rad/s (T-4.22) | order n, R_s, R_L, f_c | Butterworth LPF, n = 2..8 | calc | p.1109-1110, Table E.1 | high |
| AOE-4251 | filter | LC Butterworth highpass: transform the lowpass prototype by swapping L and C | C = 1/(R_L*omega*L_table); L = R_L/(omega*C_table) | as above | Butterworth HPF | calc | p.1109, Fig. E.2 | high |
| AOE-4252 | filter | Worked LC filter values (verify tools against these): (I) 5-pole LPF, 75 Ohm both ends, 1 MHz, pi: C1 = C5 = 1310 pF, L2 = L4 = 19.3 uH, C3 = 4240 pF; (II) 3-pole LPF, 50 Ohm source, 10 kOhm load, 100 kHz, T: L1 = 23.9 mH, C2 = 212 pF, L3 = 7.96 mH; (III) 4-pole LPF, voltage source, 75 Ohm load, 10 MHz, T: L1 = 1.83 uH, C2 = 335 pF, L3 = 1.29 uH, C4 = 81.2 pF; (IV) 2-pole LPF, current source, 1 kOhm, 10 kHz, pi: C1 = 0.0225 uF, L2 = 11.3 mH; (V) 3-pole HPF, 52 Ohm both ends, 6 MHz: C1 = C3 = 510 pF, L2 = 0.69 uH | per scaling rules | - | Regression tests for filter generators | calc | p.1110-1111, Figs. E.3-E.7 | high |
| AOE-4253 | components | Do not design transistor bias from load lines on "typical" device curves: manufacturing spread can be a factor of five; design around dependable parameters (re, Ic vs Vbe and T) | spread up to 5x | - | Discrete transistor design | review | p.1113, App. F.2 | high |
| AOE-4254 | components | A load resistance larger in magnitude than a device's negative resistance gives two stable intersections -> hysteretic (trigger) switching | abs(R_load) > abs(R_neg) -> bistable | R_load, R_neg | Tunnel-diode / negative-resistance circuits | calc | p.1113-1114, Fig. F.6 | high |
| AOE-4255 | test | Characterize and match transistors with a curve tracer or a source-measure unit (programmable dc/ramp/step/pulse excitation with logged measurement); e.g. 2N3904: beta ~200 (spec 100-300 at 10 mA), breakdown onset somewhat below 50 V (VCEO max 40 V) | measured vs datasheet | - | Device characterization, matched pairs | measure | p.1115, App. G | high |
| AOE-4256 | transmission-line | Treat a cable/trace as a transmission line when its electrical length is >= 1/20 wavelength of the highest frequency, or when round-trip delay >= ~20% of signal rise time; below that treat coax as a capacitance (~30 pF/ft) | l_elec >= lambda/20 or 2*t_pd >= 0.2*t_r | f_max or t_r, length, velocity | Cables, PCB traces | calc | p.1116, p.1122 | high |
| AOE-4257 | transmission-line | Coax characteristic impedance and propagation | Z0 = sqrt(L/C) = (138/sqrt(er))*log10(b/a) Ohm (a = inner-conductor OD, b = shield ID); v = 1/sqrt(LC) = c/sqrt(er); velocity factor 0.66 (solid PE) to 0.80 (foam PE); l_elec = l_phys*sqrt(er); C = sqrt(er)/(c*Z0) F/m. RG-58: a = 0.81 mm, b = 2.95 mm, er = 2.3 -> 51 Ohm; RG-8: 52 Ohm, VF 0.66 -> 97.1 pF/m (29.6 pF/ft; spec 29.5) | a, b, er | Coaxial lines | calc | p.1116-1117 | high |
| AOE-4258 | cables | Standard cable impedances: 50 Ohm RF/instrumentation (RG-58, RG-174, RG-316), 75 Ohm video (RG-59), 93 Ohm pulse (RG-62), 100 Ohm twisted pair (UTP/STP Cat-3 10 Mb/s, Cat-5 100 Mb/s, Cat-5e/6 for 1000Base-T using all four pairs with 5-level coding) | Z0 per application | application | Cable selection | review | p.1116-1117 | high |
| AOE-4259 | transmission-line | Reflection coefficient at a resistive termination | rho = (R - Z0)/(R + Z0); R = Z0 -> no reflection; short -> inverted reflection; open -> same-polarity reflection | R, Z0 | Termination design | calc | p.1117, Figs. H.2-H.4 | high |
| AOE-4260 | termination | Series (back) termination: drive the line through a source resistance equal to Z0 and leave the far end open (high-Z receiver); the far end sees one clean full step, the driver sees 2*Z0 only for the round-trip time. CMOS example: three paralleled 74HC buffers (~15 Ohm) + 33 Ohm into 50 Ohm RG-174/RG-316 | R_source_total = Z0 | driver R_out, Z0 | Point-to-point logic over coax/PCB traces | calc | p.1118-1119, Figs. H.5-H.6 | high |
| AOE-4261 | termination | A low-impedance driver into an unterminated line rings: the far end first sees 2x V_oc, then oscillates at the round-trip period; source impedance Z0/2 gives 33% far-end overshoot (false clocking risk) | overshoot = rho_source-related; Z_s = Z0/2 -> 33% | Z_s, Z0 | Fast CMOS/FPGA outputs on long traces | sim | p.1119-1120, Fig. H.7 | high |
| AOE-4262 | protection | Robust lab/front-panel logic input on coax: series resistor (e.g. 1 kOhm) into the gate's clamp diodes with a speed-up capacitor across it, a pull-down for a defined level when unplugged, and a resistor limiting overdrive current into the V+ rail (small regulators like a 78L05 can be back-driven); driver end = paralleled gates (5-10 Ohm) + series R to ~50 Ohm | R2 = 1 kOhm with C1 speed-up (1 kOhm x 10 pF = 10 ns otherwise) | fault voltages | BNC logic inputs (Fig. H.8) | inspect | p.1120 | high |
| AOE-4263 | transmission-line | Input impedance of a terminated line | Z_in = Z0*(Z_L + j*Z0*tan(2*pi*l/lambda))/(Z0 + j*Z_L*tan(2*pi*l/lambda)); matched -> Z0 at any length; lambda/4 -> Z0^2/Z_L; lambda/2 -> Z_L; short open line ~ capacitor C' = l/(v*Z0); short shorted line ~ inductor L' = Z0*l/v (book writes c for the propagation velocity) | Z_L, Z0, l, lambda | Stubs, cable loading | calc | p.1120 | high |
| AOE-4264 | transmission-line | An open-ended cable looks like a short at the frequency where it is lambda/4 long (5 ft coax ~32 MHz, repeating at odd multiples); a generator driving an unterminated cable into a high-Z circuit gives large response dips/bumps - terminate the far end in Z0 for flat amplitude (half the open-circuit amplitude) | f_short = v/(4*l)*(2k+1) | cable length, v | Signal-generator cabling | calc | p.1116, Fig. H.1 | high |
| AOE-4265 | matching | VSWR relations | VSWR = (1 + abs(rho))/(1 - abs(rho)); resistive: VSWR = R/Z0 (R > Z0) or Z0/R; abs(rho) = (VSWR - 1)/(VSWR + 1); from a directional power meter VSWR = (1 + sqrt(Pr/Pf))/(1 - sqrt(Pr/Pf)) | rho or Pf, Pr | RF feed lines | calc | p.1121 | high |
| AOE-4266 | transmission-line | Cable loss rises as sqrt(f) (skin effect) - quadrupling frequency doubles the dB loss; mismatch (VSWR > 1) increases loss and peak voltage for the same delivered power | dB_loss(f2) = dB_loss(f1)*sqrt(f2/f1) | f, cable type | Long RF runs (Fig. H.9) | calc | p.1121-1122 | high |
| AOE-4267 | current-carrying | Skin depth in copper limits the useful conductor thickness | delta_Cu(cm) = 6.6/sqrt(f[Hz]) at room temperature (~1 cm at 60 Hz; ~10 um at 40 MHz); current density falls to 1/e (37%) at depth delta | f | Busbars, RF conductors, plated shields | calc | p.1121-1122, Fig. H.10, fn.7 | high |
| AOE-4268 | matching | Quarter-wave transformer matches two impedances with a lambda/4 line of the geometric-mean impedance; other deliberate standing-wave uses: open/shorted stubs as high-Q L or C, shorted lambda/2 or open lambda/4 as RF bypass, open lambda/2 or shorted lambda/4 as RF choke | Z_line = sqrt(Z1*Z2) | Z1, Z2, f | Narrowband matching | calc | p.1121 fn.6 | high |
| AOE-4269 | matching | Resistive minimum-loss L-pad between resistive impedances r < R: shunt resistor across the lower-impedance port | X = R/r; Rp = r*sqrt(X/(X - 1)) (across r); Rs = r*sqrt(X*(X - 1)); loss = 20*log10(sqrt(X) + sqrt(X - 1)) dB. 50 -> 75 Ohm: Rp = 86.6 Ohm, Rs = 43.3 Ohm, 5.72 dB | r, R | Broadband instrument matching | calc | p.1123, Fig. H.11 | high |
| AOE-4270 | matching | Matched resistive T and Pi attenuators (equal Z0 in and out); use an attenuator to isolate impedance-sensitive stages (amplifiers, mixers) from reflective loads such as filters in their stopband (some amplifiers oscillate driving a sharp filter) | x = 10^(-dB/20); Pi: Rp = Z0*(1 + x)/(1 - x), Rs = Z0*(1 - x^2)/(2x); T: Rp = Z0*2x/(1 - x^2), Rs = Z0*(1 - x)/(1 + x); 50 Ohm values T-4.23 | dB, Z0 | RF attenuators | calc | p.1123-1124, Table H.1 | high |
| AOE-4271 | magnetics | Transformer impedance matching: Z ratio = (turns ratio)^2 (1:4 turns: 50 -> 800 Ohm); use thin laminations (audio), powdered iron or ferrite at RF, transmission-line transformers above ~10 MHz; typical ranges 1000:1 bandwidth per part (North Hills 20 Hz-100 MHz to 1200 Ohm; Mini-Circuits 4 kHz-2 GHz, 1:1-16:1) | Z2/Z1 = (N2/N1)^2 | Z1, Z2, band | Broadband lossless matching | calc | p.1124-1125 | high |
| AOE-4272 | grounding | Distribute signals/clocks between separately grounded instruments through an isolating 1:1 broadband transformer; instrument grounds in one lab can differ by several volts of 60 Hz | e.g. Mini-Circuits FTB1-6 (10 kHz-125 MHz), North Hills 0016PA (20 Hz-20 MHz) | ground offset | House clocks, inter-instrument links | review | p.1125 | high |
| AOE-4273 | matching | Lossless reactive L-network match (single frequency): put the parallel reactance across the higher-impedance port | Q_EL = sqrt(R_high/R_low - 1) (twice the network Q); abs(X_parallel) = R_high/Q_EL; abs(X_series) = Q_EL*R_low. Example 1 kOhm -> 50 Ohm at 10 MHz: Q_EL = 4.36, L_par = 3.65 uH, C_ser = 73 pF, Q ~ 2, ~50% bandwidth | R_high, R_low, f0 | Narrowband RF matching (Figs. H.13-H.14) | calc | p.1125 | high |
| AOE-4274 | matching | Q control in reactive matching: Pi or T networks (via an intermediate impedance beyond both ports) give higher Q; cascaded double-L (two half-ratio steps) gives lower Q than a single L; Q of a single L rises with impedance ratio and is not adjustable | - | desired bandwidth | RF matching | review | p.1125-1126 | high |
| AOE-4275 | transmission-line | Lumped LC delay line: per-section delay T_i = sqrt(LC), Z0 = sqrt(L/C), total t_p = N*sqrt(LC); it preserves detail only down to ~T_i and is a lowpass with cutoff f = 1/(2*pi*sqrt(LC)) | 1 us line with 20 sections loses details < ~50 ns | N, L, C | Delay lines, pulse-forming networks | calc | p.1126, Fig. H.15 | high |
| AOE-4276 | power | Resonant (inductor + diode) charging of a capacitor bank wastes no energy (resistive charging wastes exactly 50%), completes in half the LC resonant period, and charges to twice the supply voltage | V_cap = 2*V_supply; t = pi*sqrt(L*C_total) | L_charge, C_total | Pulse-forming networks, flashlamps, converters (Fig. H.16) | calc | p.1126 | high |
| AOE-4277 | requirements | Size digital audio/video data rates from first principles before choosing links/storage | audio: channels x f_s x bits (CD: 2 x 44,100 x 16 = 1,411,200 b/s; recorded ~3x with coding/ECC); video: lines x pixels x fps x bits/pixel (1080 x 1920 x 30 x 16 = 995 Mb/s raw HDTV; compressed to ~20 Mb/s, ~50x; SDTV ~4 Mb/s) | format | Media products | calc | p.1132, p.1137 fn.27 | high |
| AOE-4278 | rf | Channel capacity anchors: 6 MHz TV channel carries ~20 Mb/s over the air (8-VSB) and ~38 Mb/s on cable (256-QAM); satellite transponders 27 MHz wide at ~40 Mb/s (QPSK/8PSK), 32 per satellite with both circular polarizations; FM broadcast 150 kHz signal + 50 kHz guard = 200 kHz spacing | bits/s per Hz per modulation | modulation | Link budgeting background | review | p.1134, p.1137-1139, fn.31 | high |
| AOE-4279 | hw-fw | MPEG-2 transport streams use 188-byte packets tagged with program IDs (PIDs) and interleaved; streaming receivers buffer several seconds and adapt bitrate when underrun | packet = 188 bytes | - | Video transport firmware | review | p.1138 | high |
| AOE-4280 | connectors | Video interface selection: composite (CVBS, luma + 3.58 MHz chroma) and S-video are low quality; component YPbPr on three 75 Ohm coax carries full HDTV but no audio or content protection; HDMI (19-pin, NO required latch - provide strain relief/retention) carries 8-ch 24-bit 192 ksps audio + up to 1080p60 (4K from v1.4/2.0) over four twisted pairs (R, G, B, clock) with HDCP; VGA (15-pin D, RGBHV + I2C monitor ID) to ~1600 x 1200; DVI single-link to 1920 x 1200 at 60 Hz, dual-link beyond (e.g. 2560 x 1600); DisplayPort latching 20-pin, 4 pairs x 4.3 Gb/s = 17.3 Gb/s, fiber option to 50 m | resolution vs interface limit | resolution, audio need | Display interfaces | review | p.1143-1145, Fig. I.10 | high |
| AOE-4281 | cables | Satellite IF distribution uses 75 Ohm quad-shielded RG-6 coax from the LNBF (IF bands ~1.2 and ~1.9 GHz, 500 MHz wide each); the set-top box also powers the LNBF over the coax | Z0 = 75 Ohm | - | Satellite receivers | review | p.1139-1140 | high |
| AOE-4282 | test | SPICE usage rules: unit multipliers are f, p, n, u, m, k, meg - "M" means milli, not mega; AC analysis is small-signal (amplitude only normalizes the result); for transient runs set the Maximum Time Step explicitly (default output may be far coarser than the requested step, e.g. ~50 us instead of 1 us) and start recording only after start-up transients settle | meg for 1e6; Tmax set; record after settling | netlist, .tran params | ngspice/SPICE simulation setup | inspect | p.1146-1148, fn.1 | high |
| AOE-4283 | test | Sanity-check surprising simulation results with a transient run at the frequency of interest and, if still in doubt, on the bench (example: passive RC network with gain 1.142 at 1.096 kHz confirmed on a scope) | sim vs bench agreement | - | Simulation validation | measure | p.1147-1148, Figs. J.1-J.4 | medium |
| AOE-4284 | components | Check part lifecycle and availability with parts locators (Octopart, FindChips, NetComponents) - they show discontinued status and stocking distributors (factory-direct-only parts may be missing); for obsolete ICs use authorized aftermarket sources (e.g. Rochester Electronics) | availability check at design time and before release | part list | BOM risk | review | p.1078 fn.39, p.1150-1151 | medium |
| AOE-4285 | test | Bench instrument capability anchors for verification planning: 6.5-digit DMMs (e.g. 34410A, Keithley 2100) with LAN/USB; low-distortion generator 0.01 Hz-200 kHz at 0.001% distortion (SRS DS360); RF synthesizers to 6 GHz with low phase noise (SG380); GPS-disciplined time/frequency standard; source-measure units (B2900, Keithley 2600); LCR meters (HP 4263B, SR720) | instrument capability must exceed the DUT specification being verified (book gives no ratio) | DUT spec | Test equipment selection | review | p.1152, App. L | medium |
| AOE-4286 | test | Oscilloscope input: 1 MOhm in parallel with ~20 pF (capacitance NOT standardized - re-compensate a probe whenever it moves to another input/scope); 50 Ohm input option on scopes above ~100 MHz; input connector typically limited to +-400 V (use 100x HV probes beyond) | 1 MOhm // ~20 pF; V_in_max ~ +-400 V | signal level, BW | Bench verification | inspect | p.1158, p.1161 | high |
| AOE-4287 | test | Calibrated scope readings require the VARIABLE gain and sweep verniers in their CAL detent; AC coupling has a ~0.1 s time constant (tilts/shifts low-frequency and dc-bearing waveforms); GND position disconnects (does not short) the input | vernier = CAL | settings | Scope measurements | inspect | p.1158 | high |
| AOE-4288 | test | Probe loading: a 1x probe plus cable presents ~1 MOhm // ~100 pF (at 10 MHz ~160 Ohm) and can make circuits misbehave or oscillate; default to a compensated 10x probe (10 MOhm // few pF), 1x only for mV signals, active FET probes (< 1 pF, e.g. P6243, 1 GHz, into 50 Ohm) for sensitive/fast nodes | X_C = 1/(2*pi*f*C_probe); compensate on ~1 kHz calibrator square wave for no overshoot | node impedance, f | Probing sensitive/high-frequency nodes | calc | p.1160-1161, Fig. O.3 | high |
| AOE-4289 | test | Current probes: split-core transformer types are ac-only; Hall + transformer types respond to dc (Tek A622 dc-100 kHz; TCP312A dc-100 MHz with TCPA300 amplifier) | probe BW and dc capability vs signal | current waveform content | Current measurement | review | p.1161 | high |
| AOE-4290 | grounding | The scope's probe ground is mains protective earth: never clip it to a node that is not at ground (it shorts that node, and is dangerous on line-powered "hot" circuits such as offline SMPS); measure between two points with two channels (invert + ADD) or a differential probe/preamp (e.g. LeCroy DA1855A); do not float the scope | probe ground only on circuit ground | circuit reference | Test procedures, safety | review | p.1161 | high |
| AOE-4291 | grounding | For weak or high-frequency signals connect the probe's short ground lead directly to the local circuit ground at the measurement point and verify by probing that ground (should show no signal); keep short ground accessories with the probes | ground lead length minimal | - | Low-level/HF probing | measure | p.1161 | high |
| AOE-4292 | test | Trigger configuration: NORMAL (level/slope, stable display), AUTO (free-runs so a trace always shows), SINGLE (non-repetitive events), LINE (hum/ripple), EXT (clean sync or clock when the viewed signal is dirty); HF-REJ/LF-REJ trigger coupling to avoid false triggers; trigger holdoff for complex digital sequences | mode per signal | signal type | Scope setup | review | p.1159-1160, p.1162 | high |
| AOE-4293 | test | Digital scope acquisition: samples are ~8-bit, so resolution depends on the vertical scale (fill the screen); sample mode can alias at slow sweeps (speed up the sweep or use peak-detect if suspected); peak-detect catches narrow spikes; average (repetitive signals) lowers noise without reducing bandwidth; hi-res averaging within an interval reduces bandwidth | use the most sensitive V/div that keeps the signal on screen (resolution = full scale/2^8) | sweep, mode | Digital scope measurements | review | p.1162-1164 | high |
| AOE-4294 | test | Scope dead time hides rare events: at 1 us/div (10 us sweep) and 100 updates/s the scope is live only 0.1% of the time - use high waveform-update modes, smart triggers (glitch, runt, width, setup/hold violation, serial-bus conditions) or mask/limit testing (also usable for production go/no-go and jitter limits) | live fraction = sweep_time x updates/s | event rate | Glitch hunting, production test | calc | p.1164 | high |
| AOE-4295 | test | Before trusting digital-scope numbers, check hidden state: probe-skew compensation (mixed probe types differ by tens of ns), bandwidth limit, averaging, single-sweep/stop, probe attenuation readout; use bandwidth limit deliberately to remove wideband fuzz on slow signals | settings audit | scope state | Measurement integrity | inspect | p.1162, p.1164-1165 | high |
| AOE-4296 | test | Use digital-scope pretrigger (trigger point placed right of center) to see events leading up to a trigger, and single-shot capture with post-capture search for non-repetitive faults | pretrigger fraction | - | Debug of intermittent faults | review | p.1162-1163 | medium |

## 2. Formulas & tables (numbers)
### T-4.1 Keysight Multislope-III ADC: integration time vs resolution and line rejection (Table 13.8, p.921)
Instruments: 34401A DMM, 34420A microvoltmeter, 34970A DAQ; clock 375 kHz; values for 60 Hz setting.

| measurement duration (PLC) | duration | clocks | digits | readings/s | NMR at line freq (dB) |
|---|---|---|---|---|---|
| 0.02 (reported) | 0.4 ms | 150 | 4.5 | 1000 | - |
| 0.2 | 3 ms | 1500 | 5.5 | 300 | - |
| 1 | 16.7 ms | 6250 | 5.5 | 60 | 60 |
| 10 | 167 ms | 62.5k | 6.5 | 6 | 95 |
| 100 | 1.67 s | 625k | 6.5 (7.5 for 34420A) | 0.6 | 105 |
| 200 (34420A only) | 3.33 s | 1.25M | 7.5 | 0.3 | 110 |

Multislope IV (2006, 34410A/34411A): 4.5 digits in 20 us (0.001 PLC), 20x faster than Multislope III; 34411A: 1000 readings/s at 6.5 digits, 50,000 readings/s at 4.5 digits (p.921, fn.58, fn.61). OCR of table layout is noisy; row alignment reconstructed from clock counts (clocks/375 kHz = duration). conf=medium.

### T-4.2 Selected delta-sigma ADCs (Table 13.9, p.935) — subset of columns
OCR of this table is heavily garbled; only columns that could be aligned with confidence are given (bits, max conversion rate, typ power, qty-25 price 2015). Supply-range and DC-error columns omitted (not reliably alignable). conf=medium.

| part | bits | max rate (ksps) | typ power (mW) | notable (comments column) | price qty25 ($) |
|---|---|---|---|---|---|
| ADS1158 | 16 | 125 | 42 | 16 SE or 8 diff; MUX out/ADC in pins | 11.77 |
| ADS1100 | 16 | 0.128 | 0.2 | I2C; internal clk; self-cal | 4.80 |
| ADS1115 | 16 | 0.86 | 0.5 (at 3.3 V) | I2C; 4 SE or 2 diff; PGA 1-16 | 5.53 |
| AD73360 | 16 (6 ADCs) | 4 | 86 | PGA 1-80 | 9.24 |
| MAX11208B | 20 | 0.12 | 0.8 | internal clock | 2.18 |
| CS5513 | 20 | 0.33 | 1.9 | CS5510/11 = 16-bit | 4.96 |
| MCP3551 | 22 | 0.014 | 0.3 (at 3.3 V) | 2.5 uVrms; auto-shutdown | 3.31 |
| LTC2412 | 24 | 0.008 | 0.2 | no latency; 0.8 uVrms; "a favorite" | 6.34 |
| AD7730 | 24 | 0.2 | 65 | bridge subsystem, offset DAC, ac excitation | 16.10 |
| AD7794 | 24 | 0.47 | 1 (0.4 unbuffered) | 6 ch, INA PGA 1-128, 2 current sources, int ref 4 ppm/degC | 10.80 |
| MAX11210 | 24 | 0.48 | 0.25 | PGA 1-16 | 3.32 |
| ADS1246 | 24 | 2 | 1.4 (at 3.3 V) | PGA 1-128; ADS1247/48 int 10 ppm/degC ref | 8.38 |
| CS5532-BS | 24 | 3.84 | 70 | PGA 1-64; 6 nV/rtHz; industrial workhorse | 12.80 |
| AD7190 | 24 | 4.8 | 1 | PGA 1-128; low noise | 10.89 |
| ADS1259 | 24 | 14 | 13 | off-scale detectors; 2 ppm ref | 12.15 |
| AD7734 | 24 | 15 | 85 | 4 ch, +-10 V inputs; chopper mode | 15.84 |
| ADS1210 | 24 | 19.5 | 26 | PGA 1-16 | 22.84 |
| ADS1258 | 24 | 23.7 | 42 | 16 ch; low noise | 18.80 |
| ADS1298 | 24 (8 ADCs) | 32 | 10 | biopotential (EKG/EEG); PGA 1-12 | 40.40 |
| ADS1278 | 24 (8 ADCs) | 144 | 530 | ADS1274 = quad | 39.57 |
| AD7764 | 24 | 312 | 300 | diff input buffer | 16.94 |
| ADS1672 | 24 | 625 | 350 | LVDS/CMOS serial | 22.06 |
| AD7760 | 24 | 2500 | 960 | diff input buffer; parallel | 42.49 |
| ADS1675 | 24 | 4000 | 575 | pin-programmed, LVDS or CMOS serial | 35.88 |
| ADS1281 | 32 | 4 | 12 | no missing codes to 31 bits | 49.68 |

Named-part facts in prose: MAX11208B: 20-bit at 13.75 sps, 0.7 uVrms, 80 dB rejection of 50 and 60 Hz with internal clock, $3.75 single; -A suffix 120 sps (deep 120 Hz rejection). CS5532-BS: en = 6.4 nV/rtHz at 0.1 Hz (G = 64), in = 1 pA/rtHz, dVos = 15 nV/degC (G = 64), FS drift 2 ppm/degC typ, +-0.0015% max INL, 6.25 sps to 3.8 ksps, noise-free resolution 20 bits (G = 64) to 23 bits (G <= 8), ~$16 (p.936). AD7190: 8.5 nV/rtHz (fn.94).

### T-4.3 Selected audio delta-sigma ADCs (Table 13.10, p.937)
SNR (A-weighted, measured with -60 dB input) and THD+N at max sample rate, 1 kHz, -1 dB signal. conf=medium (OCR).

| part | ch | bits | fsamp max (kHz) | SNR (dBA) | THD+N (dB) | Vcc (V) | Pdiss (mW) | notes |
|---|---|---|---|---|---|---|---|---|
| PCM1870A | 2 | 16 | 50 | 90 | -81 | 3 | 13 | mic preamp |
| CS4243x (OCR "CS43432") | 4 | 24 | 96 | 105 | -98 | 5 | 600 | codec 4 in + 6 out |
| PCM2906 | 2 | 16 | 48 | 89 | -80 | 5 | 280 | codec, USB, S/PDIF |
| AK5384 | 2 | 24 | 96 | 107 (at 48 kHz) | -94 | 5 | 275 | diff |
| AK5388 | 4 | 24 | 192 | 120 | -107 | 5 | 590 | diff |
| AK5394A | 2 | 24 | 192 | 123 | -94 (-110 at 96 kHz) | 5 | 705 | diff; popular |
| CS5381 | 2 | 24 | 192 | 120 | -110 | 5 | 260 | diff; preferred |
| AD1974 | 4 | 24 | 192 | 105 | -96 | 3.3 | 430 | diff, PLL |
| PCM4204 | 4 | 24 | 216 | 117 | -103 | 4 | 615 | diff |
| PCM4222 | 2 | 24 | 216 | 123 | -108 | 4 | 340 | diff; configurable |

Delta-sigma family capability anchors (p.923, p.924): audio DAC six 24-bit 192 ksps channels with 114 dB effective DR ~$10; ADCs from 24-bit dc-accurate to 24-bit 96 ksps to 16-bit 20 Msps; monotonic to 31 bits or more; HCPL-7800A delta-sigma isolation amplifier 0.004% nonlinearity typ, 3 ppm/degC gain change typ, kV isolation, 100 kHz BW.
### T-4.4 SAR vs delta-sigma "shootout" (p.939) — Analog Devices, both introduced 2006
| parameter | units | SAR AD7641 | delta-sigma AD7760 |
|---|---|---|---|
| price | US$ | 47 | 53 |
| conversion rate | Msps | 2.0 | 2.5 |
| sampling frequency | MHz | 2 | 40 |
| alias above | MHz | 1 | 20 |
| resolution | bits | 18 | 24 |
| zero error | ppm max | 60 | 200 |
| zero tempco | ppm/degC typ | 0.5 | 0.1 |
| gain error | max/typ | 0.25% | 0.016% |
| gain tempco | ppm/degC typ | 1 | 2 |
| SNR | dB typ | 93 | 100 |
| THD | dB typ | -101 | -103 |
| INL | ppm typ | +-7.6 | +-7.6 |
| data delay | us | 0.5 | 12 |
| reference | - | internal | external |
| supplies | count | 1 | 3 |
| power | mW | 75 | 960 |
(OCR column alignment reconstructed; ratios in prose — 25x latency, 13x power, 15x gain error — confirm alignment. conf=medium)

### T-4.5 Specialty A-to-D converters (Table 13.12, p.942) — conf=medium (OCR)
| part | bits | max rate (ksps) | channels | ADCs | function |
|---|---|---|---|---|---|
| AMC1203 | 1 | 10M (bitstream) | 1 | 1 | delta-sigma modulator, ac motor current |
| AD7873 | 12 | 125 | 6 | 1 | resistive X,Y touchscreen |
| AD7490 | 12 | 1000 | 16 | 1 | flexible sequencer |
| AFE5401 | 12 | 25M | 4 | 4 | automotive-radar AFE |
| AFE5804 | 12 | 40M | 8 | 8 | 8-ch ultrasound, 0.9 nV/rtHz |
| AD6620 | 12 | 67M | 2 | 1 | FIR filter + prog RAM, to FPGA |
| AD9869 | 12 | 80M | 1 | 1 | transceiver, 200 Msps DAC |
| AD6655 | 14 | 150M | 2 | 2 | IF diversity receiver, 32-bit NCO |
| LMP90080 | 16 | 0.21 | 8 | 1 | sensor AFE, many interfaces |
| ADE7753 | 16 | 14 kHz RMS BW | 2 | 2 | ac power monitor, single phase |
| DDC316 | 16 | 100 | 16 | 16 | 16 current inputs, 3 to 12 pC |
| AD7147 | 16 | 250 | 13 | 1 | 13 capacitance inputs, touch |
| AD7609 | 18 | 200 (all ch simultaneous) | 8 | 1 | simultaneous-sampling, differential |
| DDC232 | 20 | 6 | 32 | 32 | 32 current inputs, 3 to 12 pC |
| 78M6631 | 22 | 2.5 | 6 | 1 | 3-phase power, with 8051 CPU |
| AD7746 | 24 | 0.09 | 2 | 1 | precision capacitance, +-4 pF FS |
| ISL26102 | 24 | 4 | 2 | 1 | quiet, 7 nV/rtHz, 2 ppm linearity |
| LDC1000 | 24 (L), 16 (Rp) | fastest = 192 LC cycles (10 ksps at 2 MHz) | 2 | 2 | inductance, loss resistance |
| ADS1298 | 24 | 32 | 8 | 8 | standard 12-lead ECG |
| TPA5050 | 24 | 192 | 2 | 2 | audio, lip-sync delay to 120 ms |

### T-4.6 PLL phase-detector comparison (p.958)
| parameter | type I (exclusive-OR / multiplier) | type II (edge-triggered, "charge pump", PFD) |
|---|---|---|
| input duty cycle | 50% optimum | irrelevant |
| lock on harmonic? | yes | no |
| rejection of noise | good | poor |
| residual ripple at 2 f_in | high | low |
| lock range L | full VCO range | full VCO range |
| capture range | < L, set by loop-filter time constant | L |
| output frequency when out of lock | f_center | f_min |

### T-4.7 Analog-switch trade for DAQ signal routing (p.946-948, fn.112)
| switch | Ron | Cs(on) | charge injection | swing | note |
|---|---|---|---|---|---|
| MPC506 (MUX) | 1.5 kOhm | - | - | +-15 V rails, +20 V beyond rails OK | break-before-make, 0.3 us switching, make delay 80 ns; 2 nA typ leakage |
| IH5043 / DG403 | 80 Ohm max | 22 pF | low | +-15 V | chosen: low leakage, capacitance, injection |
| ADG884 | 0.4 Ohm max | 295 pF | - | 5 Vpp max | low-voltage part |
| ADG1413 | 1.5 Ohm | - | +-300 pC (5-10x DG403) | +-15 V | |

### T-4.8 16-channel DAQ error budget worked example (PGA202 + LTC1609, p.948-950)
| quantity | G = 1 | G = 10 | G = 100 |
|---|---|---|---|
| full-scale input | +-10 V | +-1 V | +-0.1 V |
| ADC LSB referred to input (LSB_RTI) | 300 uV | 30 uV | 3 uV |
| PGA offset RTI = (0.5 + 5/G) mV | 5.5 mV (18 LSB) | 1 mV (33 LSB) | 0.55 mV (180 LSB) |
| PGA offset drift RTI = (3 + 50/G) uV/degC | 53 uV/degC | 8 uV/degC | 3.5 uV/degC (~1 LSB/degC) |
| PGA gain TC | 3 ppm/degC | 3 ppm/degC | 40 ppm/degC (~1 LSB/degC; LSB = 30 ppm) |
| noise 0.1 Hz-10 kHz RTI | ~3 uV (negligible) | ~3 uV | ~3 uV (~1 LSB) |
Derived drift column values computed from printed formula (conf=medium); others printed (high).
### T-4.9 Two-tap maximal-length LFSRs (Table 13.14, p.976)
Feedback = XOR of bit n and bit m (last); m - n also valid. length = 2^m - 1 clock cycles.

| m | n | length | m | n | length | m | n | length |
|---|---|---|---|---|---|---|---|---|
| 3 | 2 | 7 | 49 | 40 | 5.6e14 | 108 | 77 | 3.2e32 |
| 4 | 3 | 15 | 52 | 49 | 4.5e15 | 111 | 101 | 2.6e33 |
| 5 | 3 | 31 | 55 | 31 | 3.6e16 | 113 | 104 | 1.0e34 |
| 6 | 5 | 63 | 57 | 50 | 1.4e17 | 118 | 85 | 3.3e35 |
| 7 | 6 | 127 | 58 | 39 | 2.9e17 | 119 | 111 | 6.6e35 |
| 9 | 5 | 511 | 60 | 59 | 1.2e18 | 121 | 103 | 2.7e36 |
| 10 | 7 | 1023 | 63 | 62 | 9.2e18 | 123 | 121 | 1.1e37 |
| 11 | 9 | 2047 | 65 | 47 | 3.7e19 | 124 | 87 | 2.1e37 |
| 15 | 14 | 32767 | 68 | 59 | 3.0e20 | 127 | 126 | 1.7e38 |
| 17 | 14 | 1.3e5 | 71 | 65 | 2.4e21 | 129 | 124 | 6.8e38 |
| 18 | 11 | 2.6e5 | 73 | 48 | 9.4e21 | 130 | 127 | 1.4e39 |
| 20 | 17 | 1.0e6 | 79 | 70 | 6.0e23 | 132 | 103 | 5.4e39 |
| 21 | 19 | 2.1e6 | 81 | 77 | 2.4e24 | 134 | 77 | 2.2e40 |
| 22 | 21 | 4.2e6 | 84 | 71 | 1.9e25 | 135 | 124 | 4.4e40 |
| 23 | 18 | 8.4e6 | 87 | 74 | 1.5e26 | 137 | 116 | 1.7e41 |
| 25 | 22 | 3.4e7 | 89 | 51 | 6.2e26 | 140 | 111 | 1.4e42 |
| 28 | 25 | 2.7e8 | 93 | 91 | 9.9e27 | 142 | 121 | 5.6e42 |
| 29 | 27 | 5.3e8 | 94 | 73 | 2.0e28 | 145 | 93 | 4.5e43 |
| 31 | 28 | 2.1e9 | 95 | 84 | 4.0e28 | 148 | 121 | 3.6e44 |
| 33 | 20 | 8.6e9 | 97 | 91 | 1.6e29 | 150 | 97 | 1.4e45 |
| 35 | 33 | 3.4e10 | 98 | 87 | 3.2e29 | 151 | 148 | 2.9e45 |
| 36 | 25 | 6.9e10 | 100 | 63 | 1.3e30 | 153 | 152 | 1.1e46 |
| 39 | 35 | 5.5e11 | 103 | 94 | 1.0e31 | 159 | 128 | 7.3e47 |
| 41 | 38 | 2.2e12 | 105 | 89 | 4.1e31 | 161 | 143 | 2.9e48 |
| 47 | 42 | 1.4e14 | 106 | 91 | 8.1e31 | 167 | 161 | 1.9e50 |
Column pairing reconstructed from OCR run-on lists (25 entries per column verified against lengths = 2^m - 1). conf=high for lengths; tap pairing conf=medium.
Fig. 13.119 example uses a 32-bit register with feedback from stages 31 and 18 (2^31 states).

### T-4.10 Multiple-of-8 maximal-length LFSRs (Table 13.15, p.976) — taps XORed with bit m
| m | taps | length | m | taps | length |
|---|---|---|---|---|---|
| 8 | 4, 5, 6 | 255 | 96 | 47, 49, 94 | 7.9e28 |
| 16 | 4, 13, 15 | 64K | 104 | 93, 94, 103 | 2.0e31 |
| 24 | 17, 22, 23 | 16M | 112 | 67, 69, 110 | 5.2e33 |
| 32 | 1, 2, 22 | 4G | 120 | 2, 9, 113 | 1.3e36 |
| 40 | 19, 21, 38 | 1.1e12 | 128 | 99, 101, 126 | 3.4e38 |
| 48 | 20, 21, 47 | 2.8e14 | 136 | 10, 11, 135 | 8.7e40 |
| 56 | 34, 35, 55 | 7.2e16 | 144 | 74, 75, 143 | 2.2e43 |
| 64 | 60, 61, 63 | 1.8e19 | 152 | 86, 87, 151 | 5.7e45 |
| 72 | 19, 25, 66 | 4.7e21 | 160 | 141, 142, 159 | 1.5e48 |
| 80 | 42, 43, 79 | 1.2e24 | 168 | 151, 153, 166 | 3.7e50 |
| 88 | 16, 17, 87 | 3.1e26 | | | |

### T-4.11 PRBS spectrum anchors (p.977-979)
| quantity | value |
|---|---|
| spectral line spacing | f_clk/K (K = 2^m - 1) |
| flatness | within +-0.1 dB up to 0.12 f_clk |
| noise density droop | -0.6 dB at 0.2 f_clk |
| -3 dB point | 0.44 f_clk |
| nulls | at f_clk and harmonics (envelope (sin x/x)^2) |
| low-frequency density | e_n = a*sqrt(2/f_clk) V/rtHz (f < 0.2 f_clk), a = half-swing |
| recommended LPF cutoff | 5-10% f_clk (RC: < 1% f_clk) |
| useful band | f_clk/K to ~0.2 f_clk |
### T-4.12 PC104/ISA 8-bit bus signals (Table 14.2, p.1013)
Drive: 2S = two-state active pull-up, 3S = three-state, OC = open collector, PS = power.
| signal | qty | active | drive | direction | pins | function |
|---|---|---|---|---|---|---|
| A[19..0] | 20 | H | 2S | CPU->I/O | A12..A31 | address (A15..0 for I/O) |
| D[7..0] | 8 | H | 3S | bidirectional | A2..A9 | data |
| IOR# | 1 | L | 2S | CPU->I/O | B14 | I/O read strobe |
| IOW# | 1 | L | 2S | CPU->I/O | B13 | I/O write strobe |
| MEMR# | 1 | L | 2S | CPU->I/O | B12 | memory read strobe |
| MEMW# | 1 | L | 2S | CPU->I/O | B11 | memory write strobe |
| AEN | 1 | H | 2S | CPU->I/O | A11 | DMA address signal |
| IRQ[7..2] | 6 | H (rising edge) | 2S | I/O->CPU | B21..B25, B4 | interrupt request |
| RESET | 1 | H | 2S | CPU->I/O | B2 | power-on reset |
| DRQ[3..1] | 3 | H | 2S | I/O->CPU | B16, B6, B18 | DMA request |
| DACK[3..0]# | 4 | L | 2S | CPU->I/O | B15, B26, B17, B19 | DMA acknowledge |
| ALE | 1 | H | 2S | CPU->I/O | B28 | address latch enable |
| CLK | 1 | - | 2S | CPU->I/O | B20 | CPU clock (1/3 HIGH, 2/3 LOW; 4.77 MHz original) |
| IOCHCK# | 1 | L | OC | I/O->CPU | A1 | I/O error -> NMI |
| IOCHRDY | 1 | H | OC | I/O->CPU | A10 | pull LOW for wait states |
| OSC | 1 | - | 2S | CPU->I/O | B30 | 14.31818 MHz |
| TC | 1 | H | 2S | CPU->I/O | B27 | DMA terminal count |
| GND | 4 | - | PS | - | A32; B1, B31, B32 | signal & power ground |
| +5 V | 2 | - | PS | - | B3, B29 | +5 V supply |
| +12 V | 1 | - | PS | - | B9 | +12 V |
| -5 V | 1 | - | PS | - | B5 | -5 V |
| -12 V | 1 | - | PS | - | B7 | -12 V |
PC104 connector: 2 x 32 pins (8-bit bus) + 2 x 20 pins (16-bit extension) = 104 pins; 53 signal lines + 8 power/ground on 8-bit bus (p.997). conf=medium (pin mapping from OCR table).

### T-4.13 Common buses and data links (Table 14.3, p.1029)
Par/Ser: P = parallel (width), S = serial. PP = point-to-point, MD = multidrop. Mb/s assumes no overhead.
| bus | par/ser | PP/MD | max Mb/s | devices per channel | address bits | max length (m) | hot swap | use / comment |
|---|---|---|---|---|---|---|---|---|
| PC104/ISA | P8,16 | MD | - | - | 20, 24 | - | N | peripheral cards; original IBM PC/XT |
| PCI | P32,64 | MD | 1000, 2000 | - | 32 | - | N | peripheral cards; obsolescent |
| PCIe | P1,2,4,8,16 lanes | PP | 4000 per lane | 1 | - | - | N | graphics & peripherals; serial unidirectional lanes |
| IDE/PATA | P16 | MD | 1000 | 2 | - | 0.45 | N | disks/optical; obsolescent |
| SATA | S | PP | 1500, 3000, 6000 | 1 | - | 1 | Y | HDD, SSD, optical; also eSATA |
| SCSI | P8/16 | MD | 320, 2500 | 8/16 | - | 12 | Y (SCA-2) | disk and tape; ultra2/ultra-320 |
| SAS | S | PP | 3000, 6000 | 4 | - | 8 | Y | serial attached SCSI |
| 4-20 mA | S | PP | 110 baud | few | - | 10k | Y | legacy slow devices; current loop, robust in noisy environments |
| RS-232C | S | PP | 0.1 | 1 | - | ~30 | Y | instruments, COM ports |
| RS-485 | S | MD | 0.1, 10 | 32 | - | 1000, 10k (see Ch.12 rate-vs-length graph) | Y | process control |
| parallel printer | P8 | PP | 2.5 | 1 | - | 10 | Y | obsolete |
| GPIB (IEEE-488) | P8 | MD | 8 | 15 | - | 20 | Y | test/measurement instruments; fat cable, 24-pin stackable connector |
| eSATA | S | PP | 3000 | 1 | - | 2 | Y | external disks |
| FireWire (IEEE-1394) | S | MD | 480, 800, (3200) | 63 | 64 | 10 | Y | disk, live video; full duplex, repeater topology |
| USB 1.1 | S | PP | 12 | 127 | 11 | 5 | Y | peripherals; half duplex, tiered star |
| USB 2.0 | S | PP | 480 (printed "400") | 127 | 12 | 5 | Y | incl. hard drives |
| USB 3.0 | S | PP | 4800 | 127 | - | 3 | Y | incl. SSDs; full duplex on SuperSpeed pairs |
| Ethernet | S | PP | 10, 100, 1000 | 1 | 48 | 100 (100base-Tx) | Y | networks (original coax was multidrop) |
| WiFi 802.11a/g/n | S | PP | 6 to 54, to 600 | 1 | 48 | 180 | Y | 600 Mb/s = four 64-QAM spatial streams, 40 MHz channel |
| Bluetooth | S | PP | 1, 2, 3 | 8 | 48 | 10 | Y | range 1 m at 1 mW to 100 m at 100 mW |
| Zigbee 802.15.4 | S | MD | 0.045, 0.25 | 240 (to 65534) | 64 | 30 | Y | 15-hop mesh |
| CAN | S | MD | 1.0, 0.01 | 64 | (DeviceNet) | 40 (1 Mb/s), 1k (10 kb/s) | Y | auto, factory, lab; 8-byte payload per packet |
| LIN | S | MD | 0.02 | 16 | (master-initiated) | 40 | Y | automotive one-wire sub-network under CAN |
| generic parallel chip bus | P4,8,16 | MD | to 3000 | NA | - | - | - | general purpose, fast |
| LVDS | S | PP | to 6000 | NA | - | - | - | IC to IC, backplane |
| I2C / SMBus | S | MD | 0.01, 0.1, 0.41, 3.4 | 112 | 7 | - | - | 2-wire bidirectional, handshake, addressed |
| SPI | S | MD | > 20 (chip dependent) | 1 per SS' | - | - | - | 4-wire full duplex, no handshake, no address |
| JTAG (IEEE 1149.1) | S | PP | ~100 | many | - | - | Y | diagnostics, program loading |
| 1-wire (Dallas) | S | MD | 0.1 | many | 64 | 100 | Y | sensors; power and data on one line |
USB 2.0 rate printed as "400" in OCR; USB 2.0 high speed is 480 Mb/s (book text elsewhere) — verify. conf=medium for the whole table (OCR column reassembly).

### T-4.14 Memory technology comparison (p.1015-1027)
| type | volatile | speed | endurance | notes |
|---|---|---|---|---|
| async SRAM | yes | ~50 ns std; ~8-10 ns fast | unlimited | zero quiescent (micropower ~1 uA standby), up to 16 Mb |
| sync SRAM | yes | 100-400 MHz, DDR | unlimited | 1-72 Mb, x9/18/36/72 |
| PSRAM | yes | ~50 ns (~20 ns page) | unlimited | to 128 Mb, ~100 uA standby |
| SDRAM (DDR2/3/4) | yes | 400-1600 MT/s (DDR3), 1600-3200 (DDR4) | unlimited | refresh: 8192 rows / 64 ms (1 Gb) |
| EEPROM | no | read ~100 ns, write ~10 ms | 10^5-10^6 | byte rewritable, 128 b-1 Mb serial |
| NOR flash | no | SRAM-like read | 10^5-10^6 (sector erase 4-64 kB) | 1 Mb-1 Gb, execute in place |
| NAND flash | no | serial/cmd interface | 10^5-10^6; MLC/TLC less | to 1 Tb/IC, needs controller (wear leveling, bad blocks) |
| FRAM | no | < 50 ns (150 ns cycle MB85RE4M2T) | 10^13-10^14 | to 2 Mb serial, 4 Mb parallel; 10 y at 85 degC |
| MRAM | no | 35 ns (MR2A16A) | "unlimited" | 4-16 Mb, 20-year retention |
### T-4.15 RS-232 signals (Table 14.4, p.1039) — direction as seen by DTE
| name | 25-pin | 9-pin | direction (DTE <-> DCE) | function | pair |
|---|---|---|---|---|---|
| TD | 2 | 3 | -> | transmitted data | data pair |
| RD | 3 | 2 | <- | received data | data pair |
| RTS | 4 | 7 | -> | request to send (= DTE ready) | handshake pair |
| CTS | 5 | 8 | <- | clear to send (= DCE ready) | handshake pair |
| DTR | 20 | 4 | -> | data terminal ready | handshake pair |
| DSR | 6 | 6 | <- | data set ready | handshake pair |
| DCD | 8 | 1 | <- | data carrier detect | enable DTE input |
| RI | 22 | 9 | <- | ring indicator | enable DTE input |
| FG | 1 | - | - | frame ground (= chassis) | |
| SG | 7 | 5 | - | signal ground | |
Levels: logic 1 (mark) = -5 to -15 V; logic 0 (space) = +5 to +15 V (Fig. 14.44). Waveforms captured at 8N1, 14.4 kbaud into 2.2 nF (Fig. 14.45).

### T-4.16 Serial line codes (p.1040-1042)
| code | transitions / run length | overhead | dc balance | used in |
|---|---|---|---|---|
| NRZ (NRZ-L) | unbounded runs | 0 | no | simple links |
| NRZI (NRZ-M) | changes on 0, runs of 1s unbounded | 0 | no | USB (with bit stuffing) |
| NRZI + bit stuffing | 0 inserted after six 1s -> max run 6 | worst 16%, < 1% random | no | USB |
| Manchester (biphase-level) | transition every mid-cell | 100% | yes | 10Base-T |
| biphase-mark (Aiken, F2F) | transition every cell start; mid-cell = 1 | 100% | yes, polarity-insensitive | AES3, S/PDIF, Toslink, magstripe |
| 4b/5b | bounded | 25% | - | 100 Mb/s Ethernet (3-level) |
| 8b/10b | max 5 identical; disparity <= 2 per >= 20 bits | 25% | yes | FireWire, SATA/SAS, GbE, DVI/HDMI, PCIe v1/v2 |
| EFM (8-to-14) | 2 <= RL <= 10 | 75% | shaped | CD |
| EFMPlus (8-to-16) | 2 <= RL <= 10, spectrum shaped | 100% | shaped | DVD |
(overhead for EFM/EFMPlus computed from bit ratios; conf=medium for those two cells)

### T-4.17 USB / FireWire / CAN / Ethernet physical limits (p.1042-1046)
| bus | rate | per-link length | system reach | nodes | power available |
|---|---|---|---|---|---|
| USB 1.x | 1.5 / 12 Mb/s | 5 m | ~20 m via hubs (<= 5 hub tiers) | 127 | 5 V, 100 mA (low) / 500 mA (high, negotiated) |
| USB 2.0 | 480 Mb/s | 5 m | ~20 m | 127 | as above |
| USB 3.0 | 4.8 Gb/s, full duplex | 3 m (Table 14.3) | - | 127 | 900 mA |
| USB 3.1 | 10 Gb/s | - | - | - | 5 V at 2 A; 5 A at 12 V or 20 V (10 W at 5 V, 100 W at 20 V) |
| FireWire 400 / 800 | 400 / 800 Mb/s (3.2 Gb/s planned) | 4.5 m | 72 m via repeaters | 63 | up to 45 W, 30 V |
| CAN | 1 Mb/s at <= 40 m; 10 kb/s at 1000 m | - | 1000 m | 30 | cable power pair (optional) |
| single-wire CAN / LIN | <= 40 kb/s / <= 20 kb/s | - | 40 m (LIN) | 16 (LIN) | LIN pull-up to +12 V battery |
| Ethernet UTP | 10/100/1000 Mb/s | ~100 m | - | switch ports | PoE ~48 V |
| Ethernet fiber | - | ~1 km multimode; tens of km single-mode | - | - | - |

### T-4.18 Number formats (Fig. 14.51, p.1047)
| format | bits (s/e/f) | exponent bias | range |
|---|---|---|---|
| int8 / int16 / int32 | 2's complement | - | -128..127 / -32768..32767 / -2147483648..2147483647 |
| int64 | 2's complement | - | printed "1.7e38" (OCR; int64 is -2^63..2^63-1 ~ +-9.2e18 — verify) |
| half (binary16) | 1/5/10 | 15 | +-6.1e-5 to +-6.6e4 (max 65504) |
| single (binary32) | 1/8/23 | 127 | +-1.2e-38 to +-3.4e38 (denormal to 1.4e-45) |
| double (binary64) | 1/11/52 | 1023 | +-2.2e-308 to +-1.8e308 |
| quad (binary128) | 1/15/112 | 16383 | +-3.4e-4932 to +-1.2e4932 |
### T-4.19 Standard resistor values (App. C.2, p.1104)
E24 ("5%") decade values (E12, used for 10% parts, = bold subset in book: 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82):
10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91 (then 100).

E96 ("1%") decade values:
100, 102, 105, 107, 110, 113, 115, 118, 121, 124, 127, 130, 133, 137, 140, 143, 147, 150, 154, 158, 162, 165, 169, 174, 178, 182, 187, 191, 196, 200, 205, 210, 215, 221, 226, 232, 237, 243, 249, 255, 261, 267, 274, 280, 287, 294, 301, 309, 316, 324, 332, 340, 348, 357, 365, 374, 383, 392, 402, 412, 422, 432, 442, 453, 464, 475, 487, 499, 511, 523, 536, 549, 562, 576, 590, 604, 619, 634, 649, 665, 681, 698, 715, 732, 750, 768, 787, 806, 825, 845, 866, 887, 909, 931, 953, 976.
E48 (2% or reduced 1% set) = bold subset in book (bold not recoverable from OCR; E48 = every second E96 value starting at 100 — derived, conf=medium). E192 superset for 0.1% parts; non-EIA round values (250, 300, 400, 500) sometimes available in precision parts.
Note: the book's E12 bold subset listed above is the standard E12 series; bolding not visible in OCR (conf=medium for the subset).

### T-4.20 Resistor color code and tolerance letters (Fig. C.1, p.1105)
| color | digit | multiplier | tolerance |
|---|---|---|---|
| black | 0 | 1 | - |
| brown | 1 | 10 | 1% |
| red | 2 | 100 | 2% |
| orange | 3 | 1k | - |
| yellow | 4 | 10k | - |
| green | 5 | 100k | 0.5% |
| blue | 6 | 1M | 0.25% |
| violet | 7 | 10M | 0.1% |
| gray | 8 | - | 0.05% |
| white | 9 | - | - |
| gold | - | 0.1 | 5% |
| silver | - | 0.01 | 10% |
| (none) | - | - | 20% |
Tolerance letter suffixes (printed-value parts): F 1%, G 2%, D 0.5%, C 0.25%, B 0.1%, A or W 0.05%, J 5%, K 10%, M 20%, N/Q/P 0.02% (as printed), T or L 0.01%, V 0.005%, X 0.0025%, U 0.002%, S 0.001%. Blank color-tolerance cells reconstructed from standard layout (OCR dropped empty cells) — conf=medium.

### T-4.21 Selected resistor types (Table C.1, p.1106) — partial (OCR alignment uncertain except where noted)
| parameter | carbon comp axial (RC-07) | thick film SMT-0603 (Vishay CRCW) | thin film SMT-0603 (KOA RN73) | metal film axial (RN-55D) | metal foil SMT (Vishay VSMP) |
|---|---|---|---|---|---|
| tolerances | 5%, 10% | 1%, 5% | 0.05%-1% | 0.1%-1% | 0.01%-1% |
| temp coef (ppm/degC) | -1000 | 100, 200 | 5, 10, 25, 50, 100 | 50, 100 | 0.05 (typ) |
| load life dR/R | 10% | 2% | (0.25-0.5%) | (0.25-0.5%) | 0.01% |
| moisture dR/R | 10% | 2% | ~ | ~ | 0.02% |
| thermal cycle dR/R | 2% | 2% | ~ | ~ | 0.01% |
| low temp dR/R | 3% | 0.5% | ~ | ~ | 0.01% |
| overload dR/R | 2% | 0.5% | ~ | ~ | 0.01% |
| soldering dR/R | 3% | - | ~ | ~ | 0.01% |
| vibration dR/R | 2% | - | ~ | ~ | - |
| voltage coef (ppm/V) | - | - | - | 5 (prose: 5 ppm/V -> 0.1% over 200 V) | 0.1 |
| self-heating | - | - | - | - | 5 ppm |
| price (approx, qty 100) | $0.35 (5%) | $0.025 (1%, TC 200) | $0.32 (0.1%, TC 25) | $0.05 (1%, TC 100) | $10 |
"~" = values 0.1-0.5% printed but column alignment unrecoverable. Book favorite: Vishay CMF-55 metal film (industrial RN-55D). conf=medium.
### T-4.22 Butterworth LC lowpass prototypes (Table E.1, p.1110)
Normalized to 1 Ohm load and -3 dB cutoff at 1 rad/s. Row "Rs = 1": equal source and load (pi: C1, L2, C3, ...; T: L1, C2, L3, ...). Row "Rs = inf": one termination much larger than the other; element 1 is at the non-resistive (ideal voltage- or current-source) end — verified by the book's Examples II-IV and by hand for n = 3 (La*C*Lb = 1, La*C = 2, La + Lb = 2 with La = 1.5).

| n | Rs | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 1 | 1.4142 | 1.4142 | | | | | | |
| 2 | inf | 1.4142 | 0.7071 | | | | | | |
| 3 | 1 | 1.0000 | 2.0000 | 1.0000 | | | | | |
| 3 | inf | 1.5000 | 1.3333 | 0.5000 | | | | | |
| 4 | 1 | 0.7654 | 1.8478 | 1.8478 | 0.7654 | | | | |
| 4 | inf | 1.5307 | 1.5772 | 1.0824 | 0.3827 | | | | |
| 5 | 1 | 0.6180 | 1.6180 | 2.0000 | 1.6180 | 0.6180 | | | |
| 5 | inf | 1.5451 | 1.6944 | 1.3820 | 0.8944 | 0.3090 | | | |
| 6 | 1 | 0.5176 | 1.4142 | 1.9319 | 1.9319 | 1.4142 | 0.5176 | | |
| 6 | inf | 1.5529 | 1.7593 | 1.5529 | 1.2016 | 0.7579 | 0.2588 | | |
| 7 | 1 | 0.4450 | 1.2470 | 1.8019 | 2.0000 | 1.8019 | 1.2470 | 0.4450 | |
| 7 | inf | 1.5576 | 1.7988 | 1.6588 | 1.3972 | 1.0550 | 0.6560 | 0.2225 | |
| 8 | 1 | 0.3902 | 1.1111 | 1.6629 | 1.9616 | 1.9616 | 1.6629 | 1.1111 | 0.3902 |
| 8 | inf | 1.5607 | 1.8246 | 1.7287 | 1.5283 | 1.2588 | 0.9371 | 0.5776 | 0.1951 |
Scaling (lowpass): L = R_L*L_n/omega, C = C_n/(omega*R_L). Highpass: swap element types; C = 1/(R_L*omega*L_n), L = R_L/(omega*C_n).

### T-4.23 50 Ohm matched T and Pi attenuators (Table H.1, p.1124)
| atten (dB) | Pi Rp (Ohm) | Pi Rs (Ohm) | T Rp (Ohm) | T Rs (Ohm) |
|---|---|---|---|---|
| 0 | inf | 0 | inf | 0 |
| 0.25 | 3.47k | 1.44 | 1.74k | 0.72 |
| 0.50 | 1.74k | 2.88 | 868 | 1.44 |
| 0.75 | 1.16k | 4.32 | 578 | 2.16 |
| 1.00 | 870 | 5.77 | 433 | 2.88 |
| 1.25 | 696 | 7.22 | 346 | 3.59 |
| 1.50 | 581 | 8.68 | 288 | 4.31 |
| 1.75 | 498 | 10.1 | 247 | 5.02 |
| 2.0 | 436 | 11.6 | 215 | 5.73 |
| 2.5 | 350 | 14.6 | 171 | 7.15 |
| 3 | 292 | 17.6 | 142 | 8.55 |
| 4 | 221 | 23.9 | 105 | 11.3 |
| 5 | 178 | 30.4 | 82.2 | 14.0 |
| 6 | 150 | 37.4 | 66.9 | 16.6 |
| 7 | 131 | 44.8 | 55.8 | 19.1 |
| 8 | 116 | 52.8 | 47.3 | 21.5 |
| 9 | 105 | 61.6 | 40.6 | 23.8 |
| 10 | 96.3 | 71.1 | 35.1 | 26.0 |
| 15 | 71.6 | 136 | 18.4 | 34.9 |
| 20 | 61.1 | 248 | 10.1 | 40.9 |
| 25 | 56.0 | 443 | 5.64 | 44.7 |
| 30 | 53.3 | 790 | 3.17 | 46.9 |
| 35 | 51.8 | 1.41k | 1.78 | 48.3 |
| 40 | 51.0 | 2.50k | 1.00 | 49.0 |
| 45 | 50.6 | 4.45k | 0.56 | 49.4 |
| 50 | 50.3 | 7.91k | 0.32 | 49.7 |
| 55 | 50.2 | 14.1k | 0.18 | 49.8 |
| 60 | 50.1 | 25.0k | 0.10 | 49.9 |
Scale linearly for other equal input/output impedances. Spot-checked against the formulas of AOE-4270 at 3 dB (all four values agree).

### T-4.24 Transmission-line reference data (App. H, p.1116-1122)
| item | value |
|---|---|
| coax capacitance (low-frequency view) | ~30 pF/ft |
| RG-58 | 50 Ohm (a = 0.81 mm, b = 2.95 mm, er = 2.3 -> 51 Ohm by formula) |
| RG-8 | 52 Ohm, VF 0.66, 29.5 pF/ft specified |
| RG-59 | 75 Ohm (video) |
| RG-62 | 93 Ohm (pulse) |
| UTP/STP (Cat-3, Cat-5, 5e, 6) | 100 Ohm nominal |
| velocity factor | 0.66 solid polyethylene; 0.80 polyethylene foam; 0.78 RG-8/U foam (measured example); 1.0 air |
| PCB traces | typically 50-100 Ohm (microstrip, grounded coplanar waveguide, stripline) |
| skin depth, Cu | 6.6/sqrt(f) cm; ~1 cm at 60 Hz; ~10 um at 40 MHz |
| scope helical delay cable (Tek 2213) | 12 ns/ft; 2.5 m for 100 ns |
| Tek 545A lumped delay | 200 ns with 50 inductor pairs + 50 trimmer capacitors (30 MHz scope) |

## 3. Mechanizable checks

Each check: inputs (units) -> formula -> pass criterion -> margin -> source rules.
`CHECK-nplc-integration`: inputs (t_int_s, f_line_Hz in {50,60}) -> N = t_int_s*f_line_Hz -> pass if N is an integer >= 1 (tolerance on N set by the required rejection; line-locked clock per AOE-4076 gives exact integers) -> margin = expected NMR from T-4.1 (1 PLC 60 dB, 10 PLC 95 dB, 100 PLC 105 dB) minus required rejection (dB) -> AOE-4001.

`CHECK-chargebal-integrator`: inputs (I_fs_A, Vcc_V, R_ohm, C_F, f_clk_Hz, T_meas_s, counter_bits) -> (1) R < Vcc/I_fs; (2) dV = Vcc/(R*C*f_clk) < Vcc/2 (or < Vcc/5 for the coulomb-counter variant); (3) f_clk*T_meas <= 2^counter_bits -> pass if all true -> margin = min(Vcc/I_fs/R - 1, (Vcc/2)/dV - 1, 2^bits/(f_clk*T_meas) - 1) -> AOE-4010, AOE-4023.

`CHECK-chargebal-dynamic-range`: inputs (Vos_max_V, R_ohm, I_fs_A, DR_required) -> I_err = Vos/R; DR = I_fs/I_err -> pass if DR >= DR_required -> margin = DR/DR_required - 1 -> AOE-4011, AOE-4023.

`CHECK-dsm-enob`: inputs (OSR, order_m, quantizer_bits, ENOB_required) -> ENOB = log2(OSR)*(m+0.5)*(2 if quantizer_bits==2 else 1) -> pass if ENOB >= ENOB_required (flag if m > 2: formula approximate) -> margin = ENOB - ENOB_required (bits) -> AOE-4014.

`CHECK-dsm-order-audio`: inputs (application, modulator_order) -> pass if application != "audio" or order >= 3 -> AOE-4017, AOE-4015.

`CHECK-adc-noise-resolution`: inputs (V_span_V, V_noise_rms_V, bits_required, use_noise_free bool) -> ENOB = log2(V_span/V_noise_rms); NFR = ENOB - 2.7 -> pass if (NFR if use_noise_free else ENOB) >= bits_required -> margin = difference in bits -> AOE-4026.

`CHECK-adc-latency`: inputs (arch in {dsm, pipeline, sar, flash}, f_out_Hz, k_latency_samples from datasheet (book ranges: delta-sigma "tens of" output samples, audio ADCs 12-63, pipelined ~10 up to 20 clocks, SAR ~0), loop_budget_s) -> t_lat = k/f_out -> pass if t_lat <= loop_budget_s -> AOE-4019.

`CHECK-coulomb-zero-error`: inputs (Vos_max_V, R_sense_ohm, I_sleep_A, ratio_max (default = book example 1 uA : 45 uA ~ 0.022, judged "completely negligible")) -> I_zero = Vos/R_sense -> pass if I_zero <= ratio_max*I_sleep -> margin = ratio_max*I_sleep/I_zero - 1 -> AOE-4024.

`CHECK-sleep-wake-interval`: inputs (C_int_F, I_sleep_A, dV_allow_V, t_wake_s) -> t_max = dV_allow*C_int/I_sleep -> pass if t_wake <= t_max -> AOE-4025.
`CHECK-adc-rti-error-budget`: inputs per channel/gain (V_span_V, N_bits, G, Vos_RTI_V, Vos_trimmed bool, drift_RTI_V_per_C, dT_C, gainTC_ppm_per_C, en_V_per_rtHz, BW_Hz, max_err_LSB) -> LSB_RTI = V_span/2^N/G; err_offset = 0 if trimmed else Vos_RTI; err_drift = drift_RTI*dT; err_gain = gainTC*1e-6*dT*(V_span/2/G); err_noise = en*sqrt(BW)*6.6 (p-p) -> total_LSB = (sum)/LSB_RTI -> pass if total_LSB <= max_err_LSB -> margin = max_err_LSB - total_LSB -> AOE-4054..AOE-4057, AOE-4060.

`CHECK-rto-to-rti`: inputs (spec_value, spec_referred in {RTI,RTO}, G) -> RTI = spec/G if RTO else spec -> report; flag if G < 1 and spec_referred == RTO (error grows) -> AOE-4060.

`CHECK-pga-settling`: inputs (t_settle_s at required accuracy, f_scan_Hz or ADC acquisition t_acq_s, mux t_switch_s) -> pass if t_switch + t_settle <= 1/f_scan (and <= t_acq when PGA drives ADC directly) -> AOE-4050, AOE-4053.

`CHECK-mux-overvoltage`: inputs (V_fault_max_V, V_rail_V, beyond_rail_rating_V, I_limit_A, R_series_ohm) -> I_fault = (V_fault - V_rail - V_clamp)/R_series -> pass if V_fault - V_rail <= beyond_rail_rating or I_fault <= I_limit (20 mA MPC506/MAX11046) -> AOE-4049, AOE-4066.

`CHECK-isolator-spi-timing`: inputs (f_SCK_Hz, t_pd_iso_s, t_skew_s, t_setup_host_s, echo_clock bool) -> if not echo_clock: pass if 2*t_pd_iso + t_setup_host <= 0.5/f_SCK; if echo_clock: pass if t_skew + t_setup_host <= 0.5/f_SCK -> AOE-4064.

`CHECK-i2c-address-plan`: inputs (list of devices with available address sets, bus count) -> assign unique 7-bit addresses per bus (backtracking) -> pass if assignment exists -> AOE-4068.

`CHECK-line-rejection-clock`: inputs (clock_tolerance_pct, notch_type in {single, wide}, required_NMR_dB) -> estimated NMR: internal RC clock (+-10..20%) -> 30 dB; wide notch 47-63 Hz -> 80 dB min; +-0.5% clock with staggered-zero sinc -> 85 dB; single deep notch with accurate clock -> 120 dB -> pass if estimate >= required -> AOE-4069.

`CHECK-sclk-power`: inputs (C_pin_F, V_V, f_SCK_Hz, active_fraction, P_budget_W) -> P = C*V^2*f*active_fraction -> pass if P <= P_budget -> AOE-4041.

`CHECK-pll-loop`: inputs (VDD_V, f_min_Hz, f_max_Hz, V_ctrl_span_V, n, R3, R4, C2, fc_target_Hz) -> Kp = VDD/(4*pi); Kvco = 2*pi*(f_max - f_min)/V_ctrl_span; f1 = 1/(2*pi*R4*C2); abs(G(f)) computed; find f_unity -> pass if f_unity is at the intended fc (user tolerance) and f_unity/f1 >= 3 (book: zero lower by a factor of at least 3-5) with -6 dB/octave slope through unity -> margin = f_unity/f1 - 3 -> AOE-4080, AOE-4081.

`CHECK-pll-jitter-cap`: inputs (C2, C3, placement) -> pass if C3 present with C3 ~= C2/20 (book value) and placed at the VCO control pin; re-check loop stability with C3 included -> AOE-4083.

`CHECK-vco-margin`: inputs (f_center_Hz, f_min_Hz, f_max_Hz) -> pass if f_center/f_min >= 3 and f_max/f_center >= 3 (book: 3x safety margin) or bench-validated flag -> AOE-4085.

`CHECK-pll-lock-time`: inputs (pd_type, df_Hz, BW_Hz, t_lock_budget_s) -> t = (df^2)/(BW^3) if type I (book); for type II the book gives only "a time constant characteristic of the loop bandwidth" -> simulate the capture transient -> pass if t <= budget else require sweep-acquisition -> AOE-4087.
`CHECK-intn-synth`: inputs (f_ref_Hz, r, n, m, f_vco_max_Hz, step_req_Hz, f_comp_min_Hz) -> f_comp = f_ref/r; f_vco = n*f_comp; f_out = f_vco/m; step = f_comp/m -> pass if step <= step_req and f_vco <= f_vco_max and f_comp >= f_comp_min (f_comp bounds the usable loop bandwidth and places reference spurs at +-f_comp) -> AOE-4090.

`CHECK-rafs-search`: inputs (f_target_Hz, f_master_Hz, pull_ppm (default 100), r_max) -> for r in 1..r_max: n = round(f_target*r/f_master); err_ppm = (n*f_master/r/f_target - 1)*1e6; accept first |err_ppm| <= pull_ppm -> report r, n, reference offset = -err_ppm, f_phi = f_master/r -> pass if found -> AOE-4092 (book example: 1234.56789 MHz from 100 MHz -> r = 26, n = 321, -38.469 ppm).

`CHECK-lfsr-maximal`: inputs (m, taps list, feedback in {XOR, XNOR}) -> simulate or look up T-4.9/T-4.10; period == 2^m - 1 -> pass; also require reset/initialization that avoids lock-up state (all-0 for XOR, all-1 for XNOR) -> AOE-4100.

`CHECK-prbs-noise-level`: inputs (a_V, f_clk_Hz, f_3dB_Hz, filter_type in {RC, sharp}, V_rms_required) -> e_n = a*sqrt(2/f_clk); NBW = (pi/2)*f_3dB for RC else f_3dB (approx) -> V_rms = e_n*sqrt(NBW) -> pass if f_3dB <= 0.01*f_clk (RC) or <= 0.1*f_clk (sharp) and |V_rms/V_rms_required - 1| <= tolerance -> AOE-4103, AOE-4104.

`CHECK-prbs-repeat`: inputs (m, f_clk_Hz, T_test_s) -> T_rep = (2^m - 1)/f_clk -> pass if T_rep >= T_test (sequence must not repeat within a test/measurement) -> AOE-4102.

`CHECK-enob-sinad`: inputs (SINAD_dB, ENOB_required) -> ENOB = (SINAD - 1.76)/6.02 -> pass if ENOB >= required -> AOE-4109.

`CHECK-dac-monotonic-in-loop`: inputs (DAC_type, monotonic_guaranteed bool, used_in_digital_control_loop bool) -> pass if not in loop or DAC_type == resistor-string or monotonic_guaranteed -> AOE-4110.
`CHECK-bus-strobe-timing`: inputs (t_data_setup_avail_ns, t_data_hold_avail_ns, device_t_su_ns, device_t_h_ns, latch_edge in {leading, trailing}) -> pass if latch_edge == trailing and avail_setup >= t_su and avail_hold >= t_h -> margin = min(avail_setup - t_su, avail_hold - t_h) -> AOE-4115 (ISA: 474 ns setup, 25 ns hold available).

`CHECK-read-access`: inputs (strobe_width_ns, bus_setup_required_ns, device_access_ns incl. decode + buffer delays) -> pass if device_access <= strobe_width - bus_setup (ISA: 530 - 26 = 504 ns) -> AOE-4116.

`CHECK-shared-net-drivers`: inputs (netlist: nets with >1 driver pin, pin driver types) -> pass if every multi-driver net has only 3-state or open-collector/open-drain drivers and (for OC/OD) exactly one pull-up -> AOE-4121, AOE-4125.

`CHECK-irq-sharing`: inputs (IRQ line, trigger type, number of sources, per-source mask bit) -> pass if sources == 1 or (trigger == level-low and driver == OC and every source maskable) -> AOE-4125.

`CHECK-dram-refresh`: inputs (rows, t_retention_ms, refresh_interval_us) -> required = t_retention/rows -> pass if refresh_interval <= required (1 Gb: 64 ms/8192 = 7.8 us) -> AOE-4131.

`CHECK-nvm-endurance`: inputs (writes_per_day per block/cell, lifetime_years, endurance_cycles, wear_leveling_factor (blocks spread)) -> N = writes_per_day*365*years/wear_leveling_factor -> pass if N <= endurance (EEPROM/flash 1e5-1e6; FRAM 1e13) -> margin = endurance/N - 1 -> AOE-4139, AOE-4142.

`CHECK-backup-retention`: inputs (battery_mAh, I_retention_uA, t_hold_required_h, V_batt_end, V_retention_min) -> t = battery_mAh*1000/I_ret -> pass if t >= t_hold and V_batt_end >= V_retention_min -> AOE-4138.

`CHECK-scope-bw-eye`: inputs (f_clock_Hz (link clock), scope_BW_Hz) -> pass if scope_BW >= 3*f_clock (prefer 5x, book: "3rd (or even the 5th) harmonic of the clock frequency") -> AOE-4144.

`CHECK-parallel-vs-serial`: inputs (bit_rate_per_line_bps, max_skew_s, line_length_m, n_drops) -> electrical length = line_length/(0.2 m/ns); pass for parallel only if skew is small relative to the bit period (user threshold; book gives no number) and (n_drops == 1 or stub delay << rise time) else recommend point-to-point serial with clock recovery -> AOE-4143.

`CHECK-bus-selection`: inputs (rate_Mbps, length_m, nodes, hot_swap) -> filter T-4.13 rows with max rate >= rate, length >= length, devices >= nodes -> pass if selected bus in candidate list -> AOE-4149.
`CHECK-spi-compat`: inputs per slave (mode 0-3, f_SCLK_min_Hz, f_SCLK_max_Hz, bits_per_frame), bus f_SCLK_Hz -> pass if all slaves share a mode (or firmware switches mode per SS') and max(f_min) <= f_SCLK <= min(f_max) -> AOE-4150.

`CHECK-i2c-bus`: inputs (devices with 7-bit addresses, pullup_R_ohm on SCL and SDA present bool, bus speed class in {0.01, 0.1, 0.4, 3.4 Mb/s}) -> pass if addresses unique, both pull-ups present -> AOE-4152, AOE-4068.

`CHECK-onewire-length`: inputs (network_length_m, driver_type in {simple, enhanced}) -> pass if length <= 30 m (simple) or <= 500 m (enhanced per AN244) -> AOE-4154.

`CHECK-uart-clock-tolerance`: inputs (baud, tx_clock_ppm, rx_clock_ppm, bits_per_frame (10 for 8N1), sample_point_fraction 0.5) -> cumulative error at last stop-bit sample = (|tx_ppm| + |rx_ppm|)*1e-6*(bits_per_frame - 0.5) -> pass if <= 0.5 - margin (book: "a few percent" total) -> AOE-4160.

`CHECK-uart-throughput`: inputs (baud, data_bits, parity_bits, stop_bits, required_bytes_per_s) -> bytes/s = baud/(1 + data_bits + parity_bits + stop_bits) -> pass if >= required (8N1 9600 -> 960 B/s) -> AOE-4160.

`CHECK-usb-power`: inputs (I_enumeration_mA, I_operating_mA, usb_version, negotiated_high_power bool) -> pass if I_enumeration <= 100 and I_operating <= (500 if v2 and negotiated, 900 if v3, 100 otherwise) -> AOE-4166.

`CHECK-usb-cable`: inputs (cable_lengths_m, hub_tiers, usb_version) -> pass if each <= 5 m (<= 3 m USB 3.0), hub_tiers <= 5, total <= ~20 m -> AOE-4167.

`CHECK-can-bus`: inputs (length_m, bit_rate_bps, nodes, terminations list (ohm, location), Z0_ohm) -> pass if nodes <= 30 and exactly 2 terminations at the ends with R ~= Z0 (~120 Ohm) and bit_rate <= rate_limit(length) (1 Mb/s at 40 m ... 10 kb/s at 1000 m; interpolate per transceiver datasheet) -> AOE-4169.

`CHECK-can-cm-range`: inputs (expected ground offset V_gnd_offset_V, transceiver CM range (min, max)) -> pass if 2.5 V +/- V_gnd_offset stays within CM range (standard minimum -2..+7 V); else require isolation -> AOE-4170.

`CHECK-ethernet-length`: inputs (medium in {UTP, MMF, SMF}, length_m) -> pass if UTP <= 100, MMF <= ~1000, SMF <= tens of km -> AOE-4173.

`CHECK-line-code-runlength`: inputs (code, max_run_allowed_by_CDR) -> max run from T-4.16 -> pass if <= allowed -> AOE-4163, AOE-4164.

`CHECK-pcie-routing-count`: inputs (slots with lane widths) -> pairs = sum(2*lanes) -> report wires = 2*pairs; flag if layer count < 6 or trace width budget < 0.12 mm (book reference design) -> AOE-4158.
`CHECK-leakage-at-temp`: inputs (I_leak_25C_A, T_max_C, I_signal_min_A, ratio_required (default 0.01 = book example: 10 nA worst-case switch leakage vs ~1 uA photocurrent "does the job nicely")) -> I_leak_T = I_leak_25C*2**((T_max - 25)/10) -> pass if I_leak_T <= ratio_required*I_signal_min -> margin = ratio_required*I_signal_min/I_leak_T - 1 -> AOE-4182, AOE-4183.

`CHECK-uart-clock-source`: inputs (clock_tolerance_pct (MCU), peer_tolerance_pct, framing bits=10) -> total = tolerance + peer -> pass if total <= "a few percent" (book: 7% fails, 0.5% resonator passes; compute the exact limit with CHECK-uart-clock-tolerance) -> AOE-4186.

`CHECK-opto-input-holdup`: inputs (I_pullup_A (max), t_gap_s, V_IL_max_V (margin, e.g. 0.4), C_F) -> dV = I_pullup*t_gap/C -> pass if dV <= V_IL_max -> required C = I_pullup*t_gap/V_IL_max -> AOE-4196.

`CHECK-ssr-thermal`: inputs (I_load_A, V_drop_SSR_V (~1 V), R_th_heatsink_C_per_W, T_amb_C, T_case_max_C) -> P = I*V_drop -> T_case = T_amb + P*R_th -> pass if T_case <= T_case_max -> AOE-4192.

`CHECK-ssr-leakage`: inputs (I_leak_max_A, load_min_current_to_actuate_A, indicator present) -> pass if I_leak_max << load threshold or bleeder resistor present -> AOE-4194.

`CHECK-dds-filter`: inputs (f_ref_Hz, f_out_max_Hz, filter_fc_Hz, filter_stop_atten_dB at f_ref - f_out_max, required_spur_dBc) -> pass if f_out_max < filter_fc < f_ref - f_out_max and attenuation >= required -> AOE-4201.

`CHECK-keypad-pins`: inputs (rows, cols, simultaneous_keys_needed) -> pins = rows + cols -> flag ghosting if simultaneous_keys_needed >= 3 without per-key diodes -> AOE-4204.

`CHECK-rtd-selfheat`: inputs (I_bias_A, R_max_ohm, P_selfheat_max_W, dissipation constant mW/degC if known) -> P = I^2*R_max -> pass if P <= P_selfheat_max (book: 0.6 mW at 2 mA, 160 Ohm) -> AOE-4206.

`CHECK-pwm-resolution`: inputs (f_clk_Hz, f_pwm_Hz, bits_required) -> steps = f_clk/f_pwm -> bits = log2(steps) -> pass if bits >= required (12.58 MHz/10 kHz -> 1258 steps ~10.3 bits) -> AOE-4210.

`CHECK-mosfet-pwm-loss`: inputs (I_load_A, V_bus_V, Ron_ohm (at Tj), D, f_sw_Hz, Q_gd_C, I_gate_A, L_out_H (if unclamped), R_thJA_C_per_W, T_amb_C, Tj_max_C) -> P_cond = I^2*Ron*D; t_ramp = Q_gd/I_gate; P_sw = 2*(V_bus*I*t_ramp/6)*f_sw; P_av = 0.5*L_out*I^2*f_sw; Tj = T_amb + (P_cond + P_sw + P_av)*R_thJA -> pass if Tj <= Tj_max - margin -> AOE-4212, AOE-4215.

`CHECK-avalanche-energy`: inputs (L_H, I_A, E_AS_rating_J) -> E = 0.5*L*I^2 -> pass if E*20 <= E_AS_rating else require transient-thermal check -> AOE-4213.

`CHECK-pid-sample-rate`: inputs (loop_period_s, plant_dominant_time_constant_s) -> ratio = tau/loop_period -> pass if ratio >= 25 (derived from the book's example: 10 ms loop period for thermal time constants of order 250 ms; conf medium) -> AOE-4216.

`CHECK-realtime-capture`: inputs (t_clk_high_s, t_data_hold_s, instr_per_loop, f_cpu_Hz, cycles_per_instr) -> t_loop = instr*cycles/f_cpu; worst-case read time = t_loop (loopback) + t_read -> margin = t_clk_high + t_hold - worst -> pass if margin exceeds the user threshold (book: 5 ns remaining at 30 MHz judged "a close call") else add capture FF (+~35 ns) -> AOE-4230.

`CHECK-i2c-capacitance`: inputs (sum of pin capacitances + trace capacitance (pF)) -> pass if <= 400 pF -> AOE-4223.

`CHECK-watchdog`: inputs (watchdog_enabled, kick_location in {main_loop, ISR, timer}, timeout_s, worst_loop_s) -> pass if enabled and kicked from the main loop and worst-case loop time < timeout -> AOE-4199.
`CHECK-butterworth-lc`: inputs (n, f_c_Hz, R_s_ohm, R_L_ohm, type in {LP, HP}) -> choose table row (Rs = 1 if R_s ~= R_L else inf) and topology (pi if R_L << R_s or equal; T if R_L >> R_s) -> element values by T-4.22 scaling -> pass if designed values match within tolerance of the netlist; regression cases AOE-4252 -> AOE-4250..4252.

`CHECK-tline-needed`: inputs (length_m, velocity_factor, t_rise_s or f_max_Hz) -> t_pd = length/(VF*3e8); pass (lumped OK) if 2*t_pd < 0.2*t_rise and length < lambda_min/20 (lambda = VF*3e8/f_max); else require termination -> AOE-4256.

`CHECK-series-termination`: inputs (Z0_ohm, R_driver_out_ohm (min/max), R_series_ohm, far_end_termination) -> R_total = R_out + R_series -> pass if far_end is open/high-Z and abs(R_total - Z0) <= tol*Z0 (user tol; book example 15 + 33 = 48 Ohm on a 50 Ohm line); flag overshoot if R_total <= Z0/2 (33% at far end) -> AOE-4260, AOE-4261.

`CHECK-reflection`: inputs (R_term_ohm, Z0_ohm, rho_max) -> rho = (R - Z0)/(R + Z0) -> pass if |rho| <= rho_max; VSWR = (1 + |rho|)/(1 - |rho|) -> AOE-4259, AOE-4265.

`CHECK-coax-z0`: inputs (a_m, b_m, er, Z0_target) -> Z0 = 138/sqrt(er)*log10(b/a) -> pass if within tolerance; C = sqrt(er)/(3e8*Z0) F/m -> AOE-4257.

`CHECK-quarterwave-stub`: inputs (cable_length_m, VF, f_band_Hz list, load in {open, high-Z}) -> f_n = (2k+1)*VF*3e8/(4*L) -> flag if any f_n in band and far end unterminated -> AOE-4264.

`CHECK-cable-loss-scaling`: inputs (loss_dB_per_100ft at f1, f2, length_ft) -> loss = loss1*sqrt(f2/f1)*length/100 -> pass if <= budget -> AOE-4266.

`CHECK-skin-depth`: inputs (f_Hz, conductor_thickness_m) -> delta = 0.066/sqrt(f) m (Cu) -> report ratio thickness/delta (book: copper thicker than the skin depth reduces ac loss little, e.g. ~1 cm at 60 Hz; user sets flag threshold) -> AOE-4267.

`CHECK-L-pad`: inputs (r_ohm (smaller), R_ohm (larger)) -> X = R/r; Rp = r*sqrt(X/(X - 1)); Rs = r*sqrt(X*(X - 1)); loss = 20*log10(sqrt(X) + sqrt(X - 1)) -> compare against schematic values and loss budget -> AOE-4269 (50 -> 75: 86.6, 43.3, 5.72 dB).

`CHECK-attenuator`: inputs (dB, Z0, topology, R values) -> compute ideal per AOE-4270 -> pass if each resistor within E96 rounding (~1%) -> AOE-4270.

`CHECK-L-match`: inputs (R_high, R_low, f0, L_or_C choice, component values) -> Q_EL = sqrt(R_high/R_low - 1); X_par = R_high/Q_EL; X_ser = Q_EL*R_low -> pass if components within the design tolerance and the parallel element sits across the R_high port -> AOE-4273.

`CHECK-lumped-delay`: inputs (N, L_H, C_F, t_rise_required_s) -> T_i = sqrt(LC); Z0 = sqrt(L/C); t_p = N*T_i -> pass if T_i <= t_rise_required and Z0 matches load -> AOE-4275.

## 4. Verification procedures & plots
- **Delta-sigma noise shaping (Figs. 13.54, 13.58, p.927-930)**: simulate modulator (behavioral/ngspice or Python) with band-limited input; plot power spectrum of input, bitstream and error on log-frequency axis from f_nyq/1000 to f_clk/2. Good: error spectrum rises ~linearly (1st order), quadratically (2nd order) from zero; in-band error well below signal. Corner: dc inputs such as 0.625 of FS to expose idle tones (Figs. 13.61-13.62). Pass: in-band tone/noise below required SNR (ENOB*6.02+1.76 dB). Book reference point: 8x OSR 1st-order -> ~+-6% p-p error, SNR ~16:1 (24 dB).
- **Time-domain ADC accuracy (Fig. 13.57, p.929)**: overlay analog input, decimated digital output points and error on common time axis; eyeball peak-to-peak error as fraction of FS.
- **Integrating-ADC line rejection (Table 13.8)**: inject line-frequency sine (50/60 Hz, plus +-1% frequency offset) at the input; plot reading error vs integration time in PLC; pass if NMR >= Table T-4.1 value for selected NPLC.
- **Charge-balance integrator headroom (Fig. 13.49)**: transient sim at I_in = 0 and I_in = I_fs; plot integrator output vs clock; pass if excursion per clock < Vcc/2 (or design limit) and no saturation.
- **Coulomb counter**: sweep load current from sleep level (~45 uA) to max (25 mA); plot count rate vs I_load and zero-current count; pass if slope linear and zero error <= 1 uA equivalent.
- **ADC noise-free resolution**: short input (or tie to mid-reference), capture >= 1000 conversions, compute Vrms and p-p code spread; ENOB = log2(span/Vrms), NFR = log2(span/Vpp); compare to datasheet (p-p ~6.6 x rms).
- **Averaging-window response (Fig. 13.69, p.940)**: plot |sin(pi f T)/(pi f T)| vs normalized frequency f*T from 0 to 3, overlaid with RC lowpass at f_3dB = 1/(2T); good: nulls at integer f*T. Use to choose integration time vs interferer frequencies.
- **Micropower ADC energy per reading (p.941-942)**: for candidate ADCs compute/measure average supply current vs sample rate (log-log, 1 sps to f_max); include SCLK drive power and sensor excitation; pass: average power at required rate within budget and noise (after any averaging) within spec.
- **Multiplexed DAQ settling (p.946-949)**: step between adjacent channels at max and min input (+FS to -FS); scope PGA output and ADC acquisition window; pass: settled to 0.01% (or 1/2 LSB) before acquisition ends, at every gain.
- **DAQ error budget vs temperature (p.949-950)**: shorted-input and reference-input readings at each gain across the temperature range (e.g. +-10 degC around cal); plot offset (LSB) and gain error (ppm) vs T; pass: <= 1 LSB/degC or per requirement.
- **Line-rejection measurement (Fig. 13.83, p.955)**: inject differential 50 Hz and 60 Hz (and +-2 Hz) sinusoids of known amplitude, compute NMR = 20 log(V_in/V_err); plot NMR vs frequency 40-70 Hz; pass: NMR >= spec at both line frequencies; test also with clock at tolerance extremes.
- **PLL loop Bode plot (Figs. 13.98, 13.100, p.961-963)**: plot |G(f)| (dB) and phase of Kp*Kf*Kvco/(j w n) from fc/100 to 100 fc; good: -6 dB/octave through unity gain, zero at <= fc/3..fc/5 ("comfortable phase margin" per book; record the phase margin value); repeat at Kvco min/max (nonlinear VCO).
- **PLL capture transient (Fig. 13.101, p.965)**: record VCO control voltage vs time from power-up / reference step; good: monotonic approach (PFD) or asymmetric beat then settle (type I) with modest overshoot; measure lock time vs budget.
- **PLL bench validation (p.964)**: measure VCO f_min, f_max vs R1, R2, C1 on the chosen manufacturer's parts; pass: design center within 3x safety margin at supply/temperature extremes.
- **PRBS generator period and spectrum (§13.14, Figs. 13.115-13.117)**: simulate or capture the LFSR output for >= 2 full periods; verify period = 2^m - 1 clocks and ones-count = zeros-count + 1 per period; FFT the +-a bipolar output and plot PSD (dB) vs f/f_clk from 0 to 2: good = (sin x/x)^2 envelope, nulls at multiples of f_clk, flat +-0.1 dB to 0.12 f_clk.
- **Filtered-noise level (Fig. 13.118, p.979)**: measure rms of the filtered output with a true-rms meter or scope statistics; compare with e_n*sqrt(NBW) (560 mV for the book example); histogram should be Gaussian-like but with bounded crest factor (4.34 for the 32-tap design).
- **True-RNG quality (§13.14.7)**: collect >= 1e8-1e9 bits; measure 1s/0s bias (expect few parts in 1e4, trim), autocorrelation at small lags and spectrum at 50/60 Hz and harmonics (should show none), run a statistical battery (book: Marsaglia Diehard passes).
- **PLL phase-noise / jitter transfer (§13.13.7)**: measure output phase noise (or TIE jitter) with clean vs noisy reference and vary loop bandwidth; good: reference noise suppressed above loop BW, VCO noise suppressed inside loop BW.
- **Serial-link eye diagram (Fig. 14.33, p.1028)**: drive the link with a PRBS (2^7-1 for quick look, 2^23-1 / 2^31-1 for BER, AOE-4101) at the operating rate; capture persistent differential waveform at the receiver, triggered by the (recovered) clock; x-axis one or two unit intervals, y-axis differential volts; scope BW >= 3rd-5th harmonic of the clock. Good: open eye with margin at the sampling point; compare with and without transmit equalization. Pass: eye height/width above receiver requirements; BER test error-free for the required bit count.
- **I2C bus waveform check**: scope SCL/SDA rise times with all devices attached (bus capacitance <= 400 pF, AOE-4223), verify ACK after each byte, repeated-START on register reads, clock stretching tolerated by master.
- **SPI mode check**: scope SCLK, MOSI, MISO, SS' per slave; confirm the sampling edge and idle polarity match each slave's datasheet mode and SCLK within min/max (AOE-4150).
- **UART framing check (Figs. 14.44-14.45)**: capture bytes at the configured baud into the real cable load (book used 14.4 kbaud 8N1 into 2.2 nF); verify START/STOP, bit time error from both clock sources < a few %, RS-232 levels +-5..15 V.
- **CAN physical layer (Fig. 14.49)**: measure termination (~60 Ohm between CANH and CANL with power off = two 120 Ohm ends), recessive ~2.5 V both lines, dominant CANH ~3.5 V / CANL ~1.5 V; inject ground offset to confirm common-mode range.
- **USB power**: measure device current during enumeration (<= 100 mA) and after configuration (<= 500 mA USB 2.0); hot-plug inrush with the host's current-limited switch.
- **Interrupt/DMA timing**: toggle a spare GPIO at ISR entry/exit and scope it against the interrupt source to measure latency and ISR duration; verify worst case under load.
- **DRAM/NVM**: verify refresh interval setting (<= 7.8 us average per row for 64 ms/8192 rows); run an endurance/cycle-count estimate from logged write rates.
- **Cable frequency response (Fig. H.1, p.1116)**: sweep a sinewave source (1 V open-circuit, 50 Ohm) into 10 ft of RG-58, measure amplitude at the source connector vs frequency (0-100 MHz) with far end open and with far end terminated in 50 Ohm. Good: terminated case flat at half the open-circuit amplitude; open case shows dips at odd multiples of the lambda/4 frequency. Use to verify every generator-to-DUT cabling setup.
- **TDR-style step test (Figs. H.2-H.7, p.1117-1120)**: drive the line with a fast step from a 50 Ohm (series-terminated) and a low-Z source; probe input, mid-point and far end with a high-impedance probe; horizontal ~40-100 ns/div for 8-70 ft cables. Good: series-terminated far end = single clean step to V_oc; input shows V_oc/2 plateau lasting one round-trip. Bad: far-end 2x overshoot and ringing (low-Z drive). Use the plateau length to measure electrical length / velocity factor, and the reflected step amplitude to compute rho.
- **Filter response check (App. E)**: simulate (ngspice .ac) the LC filter from source to load resistor, plot |H| in dB vs log f from f_c/10 to 10 f_c; good: -3 dB at f_c (plus the 6 dB flat-band loss for equal terminations), n x 20 dB/decade rolloff, maximally flat passband; corners: component tolerance +-5% Monte Carlo.
- **VSWR / return loss (App. H.1.3)**: with a directional power meter measure Pf and Pr, compute VSWR; or with a network analyzer plot |rho| vs frequency across band; pass per requirement (e.g. VSWR <= 1.5).
- **Attenuator/pad verification (App. H.2)**: measure insertion loss and input impedance of pads with both ends terminated in Z0; pass if loss within 0.1-0.2 dB of design and input match within spec.
- **Reactive L-match (Fig. H.14)**: simulate S11 or input impedance vs frequency; good: perfect match at f0 with half-power bandwidth ~ f0/Q (Q ~ Q_EL/2).
- **Probe compensation (App. O.1.5, p.1160)**: connect 10x probe to the scope's ~1 kHz calibrator square wave; adjust the probe trimmer for flat tops with no overshoot or rounding; repeat whenever the probe moves to a different input (input capacitance not standardized).
- **Ground-reference sanity check (App. O.1.6, p.1161)**: with the short ground lead attached at the circuit ground next to the node, touch the probe tip to that same ground; the trace must be flat (no signal) at the sensitivity used; otherwise ground-loop/pickup is corrupting the measurement.
- **Alias check (App. O.2.2A, p.1164)**: change sweep speed by 10x and switch to peak-detect; a real waveform scales consistently, an alias changes shape/frequency or becomes unstable.
- **Probe deskew (p.1164)**: feed one fast edge to all probes (passive, active, current via a loop) and align channel delays before any multichannel timing measurement (errors of tens of ns otherwise).
- **Rare-event capture (p.1164)**: set glitch/runt/width or setup-hold violation triggers and run for a time T such that expected event count >= 3; report live fraction (sweep x update rate) if using ordinary triggering.
- **Current-probe choice**: verify probe response includes dc if the waveform has a dc component (Hall types, e.g. A622 dc-100 kHz, TCP312A dc-100 MHz) and that the probe bandwidth covers the waveform's significant harmonics (by analogy with the 3rd-5th harmonic guidance for scope bandwidth, AOE-4144).
- **MCU firmware bring-up (§15.2.2D, p.1059)**: connect pod via header, power board, verify device ID, program fuses (clock source, brownout, watchdog, debug/JTAG/SPI enables), download HEX (+EEPROM), reset and observe; confirm programming port still enabled afterwards.
- **PID loop tuning (§15.6.2, p.1074)**: step the setpoint; with I and D off raise P to onset of oscillation then back off; add D to critical damping; add I for minimum settling; plot controlled variable and actuator (PWM) vs time for each step (as Figs. 15.15-15.16); pass: no sustained oscillation, overshoot and settling within spec.
- **MOSFET PWM stage (Fig. 15.13, p.1073)**: scope drain voltage and inductor current at turn-off; confirm avalanche clamp duration/energy (E = 1/2 L I^2) and measure case temperature rise at max duty; pass: Tj estimate within rating with margin.
- **Coulomb counter / leakage at temperature (§15.2.2F)**: measure zero-light (or zero-load) count rate at 25 degC and at the 85 degC design maximum; pass: leakage-induced count << minimum signal count.

## 5. Pitfalls, failure modes, review checklist
- Integrating-ADC integration time not an integer number of line cycles -> poor 50/60 Hz rejection (p.921, Table 13.8).
- Reference-steering switches that are make-before-break momentarily ground the integrator summing junction (acts like an input equal to Vos) (p.920).
- Calibration cannot detect drift of the primary voltage reference; an external known source is required (p.921).
- First-order delta-sigma modulator used in audio -> idle tones ~25 dB below FS (p.932).
- Delta-sigma ADC latency (tens of samples) placed inside a fast control loop (p.931).
- Delta-sigma DAC chosen for low-noise dc work without checking noise density (~1000 nV/rtHz vs ~10 nV/rtHz ladder) (p.938).
- Software-timed charge pulses in an MCU-based delta-sigma integrator (unstable ON-time degrades accuracy) (p.933).
- Coulomb counter sense resistor placed so that it misses regulator/MCU/op-amp quiescent current (p.934).
- Audio ADC used with coupling caps bypassed for dc: internal ~1 Hz digital HPF removes dc unless dc mode is enabled (p.937, fn.96).
- "Effective resolution" (rms-based) quoted where noise-free (p-p) resolution is required; they differ by ~2.7 bits (p.935-936).
- Thermocouple digitizer without cold-junction compensation (p.937).
- Datasheet micropower figure (e.g. 1.8 uW) quoted for 12-bit mode at 1 sps used for a 16-bit design (p.942).
- External-clock ADC requiring a 50 MHz SCLK whose drive power exceeds the ADC's own dissipation (p.942, fn.105).
- Startup delay from sleep ignored in an intermittently powered converter (p.942).
- MUX that clamps inputs when unpowered, or cannot tolerate beyond-rail inputs, on a +-10 V DAQ (p.946).
- Anti-alias filter placed after the MUX (limits scan speed) (p.947).
- Lowest-Ron analog switch chosen without checking Cs(on) and charge injection (p.948, fn.112).
- Amplifier offset/drift specified RTO treated as RTI (factor 1/G error; x5 for a G = 0.2 driver) (p.950).
- PGA offset at gain 100 exceeding 100 LSB without trim/nulling (p.949).
- Parallel-interface ADC chosen where galvanic isolation is required (21 isolator channels, bidirectional lines) (p.952).
- I2C parts with pre-assigned addresses: 8 different part numbers needed and stocking problems (p.953).
- Datasheet 105 dB CMR at 50/60 Hz mistaken for normal-mode rejection (~30 dB) (p.953, fn.116).
- Delta-sigma ADC with internal RC clock (+-10..20%) expected to reject line frequency (p.953).
- Externally referenced ADC whose full-scale is still only +-10% (CS5512: VFS = 2.5 Vref +-10%) (p.954).
- 74HC4046 VCO timing components copied from a datasheet graph without bench validation, or second-sourced from another manufacturer (+160%/-60% frequency deviations) (p.964).
- Type-II PFD driven from a noisy line-derived reference (false triggering) (p.963).
- Loop-filter damping resistor passing raw PD pulses to the VCO without a ~C2/20 shunt cap (jitter) (p.964).
- Type-I PLL with narrow loop bandwidth and no sweep-acquisition aid (lock may take minutes) (p.965).
- Integer-n PLL with a very low comparison frequency (1 Hz steps via r = 10^7): slow lock, VCO noise uncorrected, close-in reference spurs (p.966-967).
- Fractional-n part chosen without examining datasheet fractional spurs (p.968).
- Plain PLL used to recover a BPSK carrier (no spectral line at carrier) (p.970).
- LFSR with XOR feedback powered up in the all-zeros state (stuck forever) (p.975); use XNOR feedback so reset-to-zero is a legal start (p.981).
- Non-maximal tap choice (e.g. 4-bit register with taps 2 and 4) (p.976, Exercise 13.8).
- PRBS filtered with an RC whose corner is not << f_clk (spectrum not flat; sin x/x droop) (p.979).
- PRBS noise generator gains set from rms without checking finite-tap peak (clipping; crest factor 4.34 for the 32-tap design) (p.981).
- Pseudorandom sequence relied on for true randomness (it is predictable; use a physical noise source) (p.982).
- Current-output DAC converted to voltage with an external feedback resistor instead of the matched internal one (poor accuracy and stability) (p.985).
- MDAC used at small codes without checking capacitive feedthrough (bandwidth collapse) (p.985).
- Pipelined ADC latency (up to 20 clocks) ignored in a control loop (p.986).
- Clocking bus data on the leading edge of the write strobe (data not yet valid) (p.998-999).
- ISA/PC104 I/O decode not qualified by AEN (spurious responses during DMA) (p.1012).
- Lazy decoding producing aliases that collide with another peripheral (p.1000).
- Multi-byte DAC loaded byte by byte without double buffering (transient false outputs) (p.999).
- Bidirectional bus line driven by an active-pullup output ("Never!") (p.1003).
- Status-polling loop that loses keyboard/serial data while the main program is busy (p.1005).
- Long interrupt handler with interrupts disabled (lost data from other devices) (p.1008).
- Edge-triggered IRQ lines shared by several devices (ISA design flaw) (p.1008, p.1010).
- Interrupt flag not cleared by RESET (spurious interrupt at power-up) (p.1005).
- DMA terminal count used without qualifying by the channel's DACK' (p.1013).
- Wired links from lightning-exposed sites (use fiber) (p.1013).
- Battery-backed settings lost because of out-of-spec retention leakage (p.1022, fn.34).
- Frequently written data in EEPROM/flash without endurance budgeting or wear leveling (p.1024-1025).
- Deep power-down of PSRAM used where data retention was expected (refresh stops, data lost) (p.1018).
- Multidrop parallel bus at Gb/s rates (stub reflections, skew) (p.1027).
- Eye diagram viewed on a scope without 3rd-5th harmonic bandwidth (misleading closed/open eye) (p.1028).
- SPI slaves with different modes or minimum clock rates sharing one bus without per-device configuration (p.1033).
- SPI write to an absent/unpowered slave goes unnoticed (no handshake) — read back an ID/status (p.1033).
- I2C bus with missing pull-ups or duplicate device addresses (p.1034-1035).
- 1-wire network run beyond 30 m with a simple driver (p.1036).
- JTAG header assumed standard across vendors (it is not) (p.1036).
- Continuous back-to-back UART bytes (e.g. 55h 'U') — receiver may lock onto the wrong START edge (p.1038).
- RS-232 DTE/DCE and gender mismatches; USB-to-RS-232 adapters make it worse (p.1038-1039).
- Manchester-coded link polarity inverted by transformer wiring (use biphase-mark if polarity is uncertain) (p.1041).
- NRZ/NRZI data with long runs through transformer coupling (baseline wander, lost clock) (p.1041).
- USB device drawing > 100 mA before configuration / > 500 mA without negotiation (p.1042, fn.62).
- USB cable longer than 5 m without an active hub (p.1042).
- CAN bus terminated at only one end, mid-bus, or not at all (p.1044).
- Long CAN runs with non-isolated transceivers (ground loops, CM range exceeded) (p.1044-1045).
- Ethernet hubs (collisions) used instead of switches (p.1046, fn.72).
- Multi-byte values sent over SPI/I2C without agreed endianness (p.1048).
- MCU 3-state pin used as the discharge switch for a uA-level integrator (+-1 uA worst-case leakage) (p.1055).
- Leakage evaluated only at 25 degC for equipment that sits in the sun (85 degC design temperature; 64x increase) (p.1059).
- Pot/divider biased continuously from the battery to overcome 1 uA ADC leakage (p.1055).
- MCU internal RC oscillator (+-7..10%) used for 8N1 UART (p.1063).
- Relay/heater outputs enabled before their port bits are driven to the safe state at power-up (p.1064).
- Memory-mapped register variable not declared volatile (compiler removes re-reads) (p.1057).
- Watchdog kicked from an interrupt (hides a hung main loop) — kick from main loop (p.1064).
- ISR waiting on a slow peripheral (serial port) and missing switch events (p.1065).
- SSR off-state leakage (up to 10 mA) lighting indicators or holding light loads on (p.1062).
- SSR without heat sink at 10 A (~10 W dissipation) (p.1063).
- Opto ac-detect input on MCU internal pull-up (up to 0.4 mA) with too small a holding cap (p.1064).
- DDS output without reconstruction filter (spur at f_ref - f_out) (p.1068).
- Matrix keypad expected to register three or more simultaneous keys (ghosting) (p.1068).
- RTD read 2-wire (lead resistance error) or over-excited (self-heating) (p.1070).
- MOSFET PWM switch gate driven straight from an MCU pin (switching loss dominates) (p.1073-1074).
- Output LC filter added without accounting for the avalanche energy it dumps into the MOSFET at each turn-off (p.1073).
- Heater loop without independent thermal cutout (p.1071).
- Programming port disabled or wrong clock-source fuse set (bricked MCU) (p.1091).
- Bit-banged serial capture with only a few ns of worst-case margin (p.1089).
- Crash-prone product with no watchdog/reset supervisor (desk phone that must be unplugged) (p.1086).
- Designing from load lines on typical transistor curves (5x spread hidden) (p.1113).
- BNC cable from a generator to a high-impedance circuit without termination: amplitude varies wildly with frequency (lambda/4 shorts) (p.1116).
- Low-impedance logic driver into an unterminated coax (2x overshoot at far end, damaging receivers) (p.1119-1120).
- Driver impedance ~Z0/2 into unterminated trace: 33% overshoot, false clocking (p.1119).
- Front-panel logic input with no series resistor, pull-down or rail-overdrive protection (lab pulse generators set to -pulses or 20 V) (p.1120).
- Amplifier driving a sharp filter directly (stopband reflection can make it oscillate) — insert a matched attenuator (p.1123).
- Instruments with separately grounded chassis linked by coax where grounds differ by volts of 60 Hz — use an isolation transformer (p.1125).
- Resistive charging of large capacitor banks (wastes 50% of energy) where resonant charging is feasible (p.1126).
- Lumped delay line with too few sections for the required rise-time fidelity (p.1126).
- Using conductor thickness far beyond the skin depth for ac current capacity (little benefit) (p.1122).
- Schematic with four-way junctions, unlabeled parts, or missing revision/title blocks (p.1101-1103).
- Scope vernier (VARIABLE) left out of CAL during voltage/time measurements (p.1158).
- AC coupling used on low-frequency or dc-bearing signals (0.1 s time constant distorts them) (p.1158).
- 1x probe on a sensitive or fast node (~100 pF load; ~160 Ohm at 10 MHz; may oscillate) (p.1160).
- 10x probe not compensated after moving to another scope/input (p.1158, p.1160).
- Probe ground clip connected to a non-ground node, or to a line-powered "hot" circuit (short circuit/shock hazard) (p.1161).
- Floating the scope by lifting the power-cord ground (p.1161).
- Long probe ground lead on weak/HF signals (pickup; verify by probing ground) (p.1161).
- Digital scope aliasing at slow sweep in sample mode mistaken for a real signal (p.1164).
- Rare glitches missed because the scope is live only 0.1% of the time (p.1164).
- Leftover probe-skew, bandwidth-limit, averaging or single-sweep settings silently corrupting measurements (p.1165).
- Current probe without dc response used on a waveform with dc content (p.1161).
- SPICE value "1M" intended as 1 megohm (SPICE reads milli; use "meg") (p.1146).
- Transient simulation without a maximum time step (coarse, jagged, misleading waveforms) (p.1148).
- HDMI cable relied on for mechanical retention (no latch in the connector standard) (p.1144).

## 6. Standards referenced
| standard | edition/year | clause/table | governs | page |
|---|---|---|---|---|
| S/PDIF, AES3, IEC 60958, CPR-1205 | - | - | digital audio interface formats handled by CDR receivers (DIR9001, 28-108 ksps) | p.971 |
| I2S, TDM | - | - | audio PCM data-output interfaces of audio ADCs | p.937 |
| IEEE 802.11a/g/n (WiFi) | - | Table 14.3 | wireless Ethernet, 6-54 Mb/s, to 600 Mb/s (4 x 64-QAM streams, 40 MHz) | p.1029 |
| IEEE 802.15.4 (Zigbee) | - | Table 14.3 | low-rate mesh networking, 0.045/0.25 Mb/s, 15-hop | p.1029 |
| IEEE 1394 (FireWire) | - | Table 14.3 | serial bus 480/800/(3200) Mb/s, 63 devices | p.1029 |
| IEEE 1149.1 (JTAG) | - | Table 14.3 | boundary-scan test and program loading | p.1029 |
| IEEE 488 (GPIB) | - | §14.6.4C | instrument bus, 24-pin stackable connector, 20 m | p.1031 |
| IEEE 1284 (ECP, EPP) | - | §14.6.4D | bidirectional extensions of the PC parallel port | p.1031 |
| PC104 / ISA | - | Table 14.2 | 8/16-bit stack-through embedded PC bus | p.1013 |
| PCI, PCIe v1/v2/v3 | - | Table 14.3, §14.6.3 | computer peripheral buses; PCIe lanes 2.5/5/8 Gb/s | p.1029-1030 |
| PATA (ATA/IDE), SATA, eSATA, SCSI (ultra2/ultra-320), SAS | - | Table 14.3 | storage interfaces | p.1029-1031 |
| RS-232C, RS-485, 4-20 mA current loop | - | Table 14.3 | serial instrument/process links | p.1029 |
| USB 1.1 / 2.0 / 3.0 | - | Table 14.3 | peripheral serial bus | p.1029 |
| Ethernet 10/100/1000 (100base-Tx) | - | Table 14.3 | networks, 100 m segments | p.1029 |
| Bluetooth | - | Table 14.3 | wireless peripherals, 1 m at 1 mW to 100 m at 100 mW | p.1029 |
| CAN (with DeviceNet layer), LIN | - | Table 14.3 | automotive/industrial multidrop buses | p.1029 |
| I2C / SMBus, SPI, 1-wire, LVDS | - | Table 14.3 | inter-chip links | p.1029 |
| SD card specification | - | §14.4.5C | SD cards must support native SD and SPI protocols | p.1025 |
| DDR, DDR2, DDR3 ("DDR3-1600"), DDR4 SDRAM standards | - | §14.4.4B | synchronous DRAM generations and transfer rates | p.1021 |
| ISO 11898 (CAN) | - | §14.7.15 | Controller Area Network physical/data link; 1 Mb/s to 40 m, 10 kb/s at 1000 m, 30 nodes, 120 Ohm termination both ends | p.1043-1044 |
| ISO 7637 | - | §14.7.15 | automotive transient immunity test (trains of +-150 V ns-scale pulses) that CAN transceivers must survive | p.1044 |
| DeviceNet | - | §14.7.15 | protocol layer over CAN used on factory floors | p.1043 |
| LIN, single-wire CAN | - | §14.7.15 | simplified automotive sub-buses, <= 20 kb/s and <= 40 kb/s | p.1045 |
| IEEE 802.3 (Ethernet) | - | §14.7.16 | minimum packet length (printed 74 bytes), coax (10Base5/10Base2) and twisted-pair (10Base-T, 100Base-TX, 1000Base-T) physical layers | p.1045-1046 |
| Power over Ethernet (PoE) | - | fn.73 | ~48 V dc phantom power on Ethernet pairs | p.1046 |
| IEEE 1588 (PTP) | - | fn.74 | precision time protocol, ~100 ns synchronization over Ethernet | p.1046 |
| LXI (LAN eXtensions for Instrumentation) | - | §14.7.16 | LAN-based instrument control | p.1046 |
| SCPI | - | fn.22 | standard command syntax for programmable instruments | p.1065 |
| IEEE 754-2008 | 2008 | §14.8.2 | floating-point formats (binary16/32/64/128) | p.1047-1048 |
| ASCII (7-bit); ISO-8859 extended character sets | - | Table 14.5, fn.59 | character encoding for serial text links | p.1039-1040 |
| RS-232 ("Recommended Standard 232"), RS-422, RS-485 | - | §14.7.8, Table 14.4 | asynchronous serial electrical levels, pinout (DB-25/DE-9) | p.1038-1039 |
| AES3, S/PDIF, Toslink | - | §14.7.10 | biphase-mark coded digital audio links | p.1041 |
| USB 1.1/2.0/3.0/3.1 (type-C) | - | §14.7.13 | data rates 1.5/12/480 Mb/s, 4.8/10 Gb/s; bus power 100/500/900 mA, up to 100 W at 20 V (3.1) | p.1042 |
| I2C-Bus Specification v2.1 | Jan 2000 (NXP) | fn.40 | inter-IC bus; max bus capacitance 400 pF | p.1081 |
| SMBus | - | fn.52 | tighter protocol/electrical variant of I2C | p.1034 |
| SD card specs (SanDisk OEM Product Manual Table 3-2; Physical Layer Simplified Spec v2.00 ch.7) | v2.00 | fn.43 | SD/miniSD/microSD cards incl. SPI mode | p.1082 |
| DMX512 (superseded by DALI) | - | §15.8.1 item 24 | theater lighting control over RS-485, 250 kbaud, 5-pin XLR, 120 Ohm cable, to 1200 m | p.1081 |
| IEEE 1149.1 (JTAG boundary scan) | - | §14.7.4 | TCK/TMS bused, TDI/TDO daisy chain, 1-100 Mb/s | p.1036 |
| ATSC A/53, A/54 (MPEG-2); ATSC 2.0; MPEG-4 / H.264 (AVC) | - | App. I fn.25 | digital TV compression and transport (188-byte packets) | p.1137-1138 |
| NTSC, 8-VSB, 256-QAM | - | App. I | analog TV (480i, 3.58 MHz chroma) and digital broadcast/cable modulation | p.1133-1138 |
| HDMI (v1.4, v2.0), DVI (-D, -A, -I; single/dual link), DisplayPort, VGA; HDCP, DPCP (128-bit AES) | - | App. I.11 | video interfaces and content protection | p.1143-1145 |
| EIA standard decades E12/E24/E48/E96/E192 | - | App. C.2 | preferred resistor values | p.1104 |
| MIL RN-55D (metal-film resistor; Vishay CMF-55 industrial version) | - | Table C.1 | resistor type reference | p.1106 |
| Category 3 / 5 / 5e / 6 twisted-pair cable | - | App. H.1.1A | 100 Ohm UTP/STP for 10/100/1000 Mb/s Ethernet | p.1117 |
| FCC TV channel allocation (Channels 2-51, 54-698 MHz); AM 520-1710 kHz; FM 88-108 MHz | - | App. I.2 | US broadcast spectrum | p.1134 |

## 7. Process / lifecycle guidance
The book is a circuit-design text, not a product-lifecycle text; the following process guidance appears in this range.

| stage | activity | deliverable | exit criterion | source |
|---|---|---|---|---|
| Architecture | Decide MCU vs PLD/FPGA vs ASSP; pick MCU family the team already has tools for; start from the premium family member | architecture note | MCU used where displays, configurable chips, comms, computation, calibration, sequencing or upgrades exist; FPGA where hard timing/parallelism (AOE-4235, AOE-4236) | p.1093-1094 |
| Architecture | Select ADC/DAC architecture from rate/resolution/latency table | converter selection record | latency and noise budget met (AOE-4033, AOE-4111) | p.938, p.985-987 |
| Detailed design | Error budget referred to input (offset, drift, gain TC, noise vs LSB) per channel and gain | RTI error budget table | every term <= allowed LSBs at max gain and temperature (AOE-4054..4058) | p.948-950 |
| Detailed design | Choose one manufacturer (no substitutes) for mixed-signal functions in logic ICs (VCOs, Schmitt triggers, monostables, comparators, phase detectors) | AVL note "no substitutes" | single source recorded on BOM (AOE-4085) | p.964 |
| Prototype | Replace paper values (VCO R/C, timing) with bench-measured values on the chosen maker's parts; keep >= 3x frequency margin | bench measurement log | measured center within margin (AOE-4085) | p.964 |
| Prototype / firmware | Program MCU via pod: connect header, power, verify device ID, set fuses, download HEX/EEPROM, reset | programming procedure | device runs; programming port still reachable (AOE-4233) | p.1059, p.1091 |
| Design review | Full design review including environment (e.g. 85 degC for sun-exposed products, leakage x64) and a human-interface review against spec | review minutes | open items closed; HI tester sign-off (AOE-4191) | p.1059 |
| Calibration | Factory/user calibration stored in non-volatile memory (offset, full scale, amplitude vs frequency) | cal procedure + NVM map | cal constants verified after power cycle (AOE-4059, AOE-4203) | p.949-950, p.1067 |
| Documentation | Schematic per App. B rules with title and revision blocks | released schematic | checklist AOE-4238..4241 passes | p.1101-1103 |
| Sourcing | Check lifecycle/availability via locators; plan obsolete-part sources | BOM availability report | no unplanned single-source/obsolete risk (AOE-4284) | p.1078, p.1150-1151 |
| Production test | Digital-scope mask/limit (go/no-go) testing of waveforms and jitter | test limits file | yield within target (AOE-4294) | p.1164 |

## 8. Coverage log

**Lines read (Read tool, sequential, <= 700-line chunks, no truncation reported):**
- Orientation: 1-800 (front matter, TOC ch.1-4), 2150-3019 (TOC ch.10-15, appendices, list of tables).
- Assigned range, in order: 56850-57449, 57449-58148, 58148-58847, 58847-59546, 59546-60245, 60245-60944, 60944-61543, 61543-62242, 62242-62941, 62941-63640, 63640-64339, 64339-65038, 65038-65737, 65737-66436, 66436-67135, 67135-67834, 67834-68533, 68533-69232, 69232-69931, 69931-70630, 70630-71329, 71329-72028, 72028-72727, 72727-73146, 73146-73845, 73845-74059.
- Started at 56850 (start of §13.8.6 Multislope, the section boundary nearest line 57000) — small overlap with part 3 intentionally kept so no section is split.

**Skipped / not extracted (with reason):**
- Index, lines 74018-75879: skipped per brief (index pages).
- Exercises 13.5-13.11, 14.1-14.3, 15.1-15.4: not extracted as exercises (Exercise 15.4's stated answers - 580 mW vs 320 mW, 115 mW avalanche, 86 mJ rating, 40 degC/W - were used because the text states them).
- §14.2 x86 instruction set, addressing and assembly-language program listings (Programs 14.1-14.5), Program 15.1 C listing: read; only hardware-relevant rules extracted (volatile, ISR structure, endianness), not the instruction set itself.
- Appendix A (math review) and the proofs in Appendix D: pure math, read; only the Thevenin/Norton/Millman working formulas extracted.
- Appendices K (vendors), M (catalogs), N (further reading), P (acronyms): read; no design rules beyond part-locator/obsolescence guidance (AOE-4284).
- Appendix I (television tutorial): read; only data-rate/interface rules extracted (AOE-4277..4281); historical and consumer narrative skipped.
- Historical anecdotes (e.g. Armstrong, Efratom story details, calendar/leap-year analogy for fractional-n) skipped except for embedded numbers.

**Tables:**
- Reproduced: Table 13.8 (T-4.1), Table 13.9 subset (T-4.2), Table 13.10 (T-4.3), AD7641 vs AD7760 shootout (T-4.4), Table 13.12 (T-4.5), PD comparison (T-4.6), Tables 13.14 and 13.15 (T-4.9, T-4.10), Table 14.2 (T-4.12), Table 14.3 (T-4.13), Table 14.4 (T-4.15), E-series values and color code (T-4.19, T-4.20), Table C.1 partial (T-4.21), Table E.1 (T-4.22), Table H.1 (T-4.23), plus derived summary tables T-4.7, T-4.8, T-4.11, T-4.14, T-4.16-T-4.18, T-4.24.
- NOT reproduced (OCR too garbled to align reliably): Table 13.11 (audio DACs, p.939), Table 13.13 (selected PLLs, p.972), Table 14.1 (x86 instruction subset - software), Table 14.5 (ASCII code chart - standard, only noted), most DC-error/supply columns of Table 13.9 and middle columns of Table C.1.

**Extraction limitations:**
- OCR interleaves two-column pages line by line; sentences were re-assembled by hand. Several table layouts had to be reconstructed; confidence marked medium where alignment was inferred (checked against internal consistency, e.g. clocks/375 kHz = duration in Table 13.8, 2^m - 1 lengths in Table 13.14, 3 dB row of Table H.1 recomputed from formulas).
- Some formula glyphs were lost in OCR and were reconstructed and verified against the book's worked examples: L-pad loss (5.72 dB for 50->75 Ohm), L-match Q_EL (4.36, 3.65 uH, 73 pF for 1 kOhm->50 Ohm at 10 MHz), PRBS noise density (14.14 mV/rtHz), ADC ENOB/noise-free relations, RG-8 capacitance (printed as 91.1 pF/m in OCR; 97.1 pF/m matches the stated 29.6 pF/ft).
- Inconsistency flagged, not resolved: PLL design example (AOE-4081) — printed Kp/Kvco values give |G| ~0.5 at 2 Hz with R3 = 4.3 MOhm whereas the text claims 1.0; box header says VDD = +10 V while the VCO range is quoted for V2 = 0-5 V.
- USB 2.0 rate printed "400" in Table 14.3 and the review, but "480 Mb/s" in §14.7.13; USB 3.0 "4.8 Gb/s" in text vs "3.2 Gbps" in the review — both noted in T-4.13.
- Figures are not in the text: graph-dependent content (Fig. 13.56 ENOB vs OSR, Fig. 13.69 averaging-window response, Fig. H.9 cable attenuation vs frequency, Fig. H.10 skin depth vs frequency, Figs. 15.15-15.16 control simulations) captured only via captions and numeric anchors in prose.
- Prices and part availability are 2015 snapshots from the book; treat as relative guidance.
