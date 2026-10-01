# Introduction to Electromagnetic Compatibility (3rd ed.) — Anvil rulebook (part 1 of 2)

## 0. Citation

C. R. Paul, R. C. Scully, and M. A. Steffka, *Introduction to Electromagnetic Compatibility*, 3rd ed. Hoboken, NJ, USA: John Wiley & Sons, 2023 (copyright page: "This edition first published 2023 © 2023"; preface dated December 2021; assignment listed 2022). Hardback ISBN 9781119404347. Edition history: 2nd ed. 2006, 1st ed. 1992 (Wiley).

BOOKTAG: PAUL. Rule ids in this part: PAUL-1001 .. PAUL-1188 (the "1" prefix block, widened to four digits so that more than 100 rules fit without colliding with part 2's PAUL-2xx ids).

Source file: `refs-text/Introduction_to_Electromagnetic_Compatibility_Clayton_R_Paul.txt`, lines 1-17000 of 34101 (this extraction). Page citations `p.NNN` are the printed page numbers.

Chapters covered by THIS extraction (lines 1-17000):
- Front matter, table of contents, preface (lines 1-1248).
- Ch.1 Introduction to EMC: electrical dimensions, wavelength, dB units, signal-source specification (full).
- Ch.2 EMC Requirements for Electronic Systems: FCC Part 15 A/B, CISPR 32, MIL-STD-461G, measurement (OATS/SAC, LISN), aircraft/vehicle standards, design constraints (full).
- Ch.3 Signal Spectra: Fourier series, trapezoidal spectral bounds, bandwidth, duty cycle, ringing, spectrum analyzers (RBW, peak/QP/AV), nonperiodic and random signals (full; problems skimmed for answer anchors).
- Ch.4 Transmission Lines and Signal Integrity: per-unit-length parameters (wires, coax, stripline, microstrip, coplanar, broadside), time-domain reflections, terminations, discontinuities, phasor solution, losses, lumped models (full).
- Ch.5 Nonideal Behavior of Components: wires, PCB lands, leads, R/L/C models, ferromagnetics, ferrite beads, CM chokes, motors, digital devices, variability, switch arcing and contact protection (full).
- Ch.6 Conducted Emissions and Susceptibility: LISN, CM/DM, power-line filters, CM/DM diagnosis, linear/SMPS supplies, transformers, placement (full).
- Ch.7 Antennas: §7.1-§7.6.3 through p.380 (Hertzian and loop dipoles, half-wave dipole/monopole, arrays, directivity/gain, effective aperture, antenna factor, baluns, pads, Friis, images, plane-wave reflection, start of multipath) — partial, stops at line 17000.

Chapters NOT read here (reason: assigned to the part-2 agent, lines 17001-34101): remainder of Ch.7 (§7.6.3 vertical-polarization factor onward, §7.7 biconical/log-periodic antennas, §7.8 antenna modeling), Ch.8 Radiated Emissions and Susceptibility (printed DM/CM emission models, current probes, susceptibility, transfer impedance), Ch.9 Crosstalk, Ch.10 Shielding, Ch.11 System Design for EMC, Appendices A-E, index. Note: the requested DM/CM cable emission formulas are printed in Ch.8 (part 2); this part gives the same forms derived from Ch.7's elemental-antenna equations (PAUL-1185/1186, conf medium).

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| PAUL-1001 | emc | Treat a circuit/structure as lumped (Kirchhoff valid) only when its largest dimension is electrically small. | electrically small if L_max < lambda/10; lambda = v/f (m) | L_max (m), f (Hz), v (m/s) | "Typically" criterion; v0 = 2.99792458e8 m/s (~3e8) in air | calc | p.9 §1.2 | high |
| PAUL-1002 | timing | Propagation delay of an interconnect. | TD = L/v (s); free space ~3 ns/m (~1 ns/ft) | L (m), v (m/s) | air: v0~3e8 m/s; FR-4 PCB land: v ~1.8e8 m/s -> 6-in land ~850 ps | calc | p.10 eq.(1.1) | high |
| PAUL-1003 | emc | Fast rise/fall times are the primary source of high-frequency spectral content; slow (increase) rise/fall times as much as the logic tolerates as first line of defense. | - | t_r, t_f (s) | limited by point at which digital circuitry malfunctions | review | p.3 §1.1 | low |
| PAUL-1004 | emc | Wavelength in a medium; scale from "1 m = 1 lambda at 300 MHz" in air. | lambda = v/f = v0/(f*sqrt(er*ur)) (m); v = v0/sqrt(er*ur); lambda_air(m) = 300/f(MHz) | f (Hz), er, ur | nonconductive media; dielectrics er 2..12 give v = 0.7..0.29 v0 | calc | p.12-16 eq.(1.8),(1.11) | high |
| PAUL-1005 | emc | Electrical dimension K of a structure = physical length over wavelength at the highest frequency of interest; electrically large (L > 0.1 lambda) requires distributed/Maxwell treatment. | K = L/lambda; small if K < 0.1 | L (m), f_max (Hz), er | phase shift 36 deg at 0.1 lambda, 18 deg at 0.05 lambda, 3.6 deg at 0.01 lambda; "for some situations the phase shift must be smaller" | calc | p.13,16 eq.(1.12) | high |
| PAUL-1006 | materials | Free-space constants for all field/line calculations. | eps0 = 1/(36*pi) * 1e-9 F/m (approx); mu0 = 4*pi*1e-7 H/m (exact); v0 = 1/sqrt(mu0*eps0) ~ 3e8 m/s | - | - | calc | p.14 eq.(1.10) | high |
| PAUL-1007 | materials | Permeability of ferrous materials is field-strength and frequency dependent and generally decreases rapidly from the quoted dc value; do not use dc ur at RF. | sheet steel ur = 2000 (dc); ur(f, H) < ur_dc | ur_dc, f | ferrous/magnetic materials | review | p.14 §1.2 | medium |
| PAUL-1008 | emc | dB definitions: power ratios use 10log10, voltage/current (and E, H field) ratios use 20log10. | dB = 10log10(P2/P1); dB = 20log10(V2/V1) = 20log10(I2/I1) | ratio | voltage-gain dB equals power-gain dB only when RL = Rin | calc | p.18-19 eq.(1.23)-(1.25) | high |
| PAUL-1009 | emc | Absolute EMC units. | dBuV = 20log10(V/1uV); dBmV = 20log10(V/1mV); dBuA = 20log10(A/1uA); dBmA = 20log10(A/1mA); dBuW = 10log10(W/1uW); dBm = 10log10(W/1mW); dBuV/m = 20log10((V/m)/(1uV/m)); dBuA/m = 20log10((A/m)/(1uA/m)) | value | 1 V = 120 dBuV; 1 mV = 60 dBuV; 100 uV/m = 40 dBuV/m | calc | p.19-20 eq.(1.26)-(1.33) | high |
| PAUL-1010 | emc | Inverse conversion from dB to absolute. | V = 10^(dBuV/20)*1e-6; V = 10^(dBmV/20)*1e-3; W = 10^(dBuW/10)*1e-6; W = 10^(dBm/10)*1e-3 | dB value | fields treated like voltage/current (20log) | calc | p.21 eq.(1.36)-(1.39) | high |
| PAUL-1011 | emc | Convert dBm (power into 50 ohm) to RMS voltage in dBuV. | dBuV(RMS) = 107 + dBm | dBm | only valid across 50 ohm | calc | p.28 eq.(1.72) | high |
| PAUL-1012 | emc | Test/measurement equipment is calibrated in RMS; no 1/2 factor in power when RMS used. | P_av = V_RMS^2/R = V_peak^2/(2R); V_RMS = V_peak/sqrt(2) | V, R | sinusoid; 120 V RMS = 170 V peak | calc | p.17 §1.3 | high |
| PAUL-1013 | emc | A 50 ohm source meter reading (dBm) is power into a matched 50 ohm load; for a mismatched load compute VOC first, then divide. | VOC_dBuV = 6 dB + Vout_dBuV(RL=50); Vout = RL/(RS+RL)*VOC | meter dBm, RS=50, RL | e.g. -26 dBm into 150 ohm -> 84.5 dBuV | calc | p.26-28 eq.(1.69)-(1.71) | high |
| PAUL-1014 | cables | Matched-cable loss in dB subtracts directly from source level (power or voltage) only when source, cable and load are all 50 ohm matched. | Prec_dBm = (loss_dB/100ft)*len + Psrc_dBm; Vrec_dBuV = cable_gain_dB + Vsrc_dBuV | loss (dB/100 ft), length (ft) | RG58U: 4.5 dB/100 ft at 100 MHz | calc | p.29-30 eq.(1.73)-(1.75) | high |
| PAUL-1015 | test | Know the input model of the instrument: spectrum analyzers and many scope plug-ins are 50 ohm; scope high-Z plug-in is Cin || Rin. | spectrum analyzer: Cin = 0, Rin = 50 ohm; scope high-Z: Cin = 47 pF, Rin = 1 Mohm | instrument | typical values | inspect | p.25 §1.3.1 | high |
| PAUL-1016 | compliance | FCC Part 15 "digital device": unintentional radiator using timing pulses > 9000 pulses/s; product with digital circuitry and clock > 9 kHz is covered (limited exemptions). | f_clock > 9 kHz -> Part 15 Subpart B applies | f_clock | USA; RF defined 9 kHz..3000 GHz | review | p.36 §2.1.1 | high |
| PAUL-1017 | compliance | FCC class election: Class A = commercial/industrial/business environment; Class B = marketed for residential use (more stringent); PCs and peripherals are Class B and require certification with test data. | Class B limits < Class A limits | market | if a product could be bought for home use, test as Class B | review | p.37 §2.1.1; Prob.2.1.2 | high |
| PAUL-1018 | compliance | FCC/CISPR 32 conducted-emission band and method. | 150 kHz - 30 MHz, measured via 50 ohm LISN on phase and neutral separately; QP and AV limits both apply | EUT ac power cord | FCC harmonized with CISPR 32 conducted limits | measure | p.37 §2.1.1, Table 2.1-2.2 | high |
| PAUL-1019 | compliance | FCC Class B conducted limits (QP / AV). | 0.15 MHz: 66/56 dBuV; 0.5 MHz: 56/46; 0.5-5 MHz: 56/46; 5-30 MHz: 60/50 dBuV | f (MHz), V_LISN (dBuV) | CISPR 32 identical; 0.15-0.5 MHz slope per Fig. 2.1 graph | measure | p.38 Table 2.1 | high |
| PAUL-1020 | compliance | FCC Class A conducted limits (QP / AV). | 0.15-0.5 MHz: 79/66 dBuV; 0.5-30 MHz: 73/60 dBuV | f (MHz), V_LISN (dBuV) | CISPR 32 identical | measure | p.38 Table 2.2 | high |
| PAUL-1021 | compliance | FCC radiated-emission upper measurement frequency depends on the highest frequency generated/used in the device. | f_hi < 1.705 MHz -> 30 MHz; 1.705-108 -> 1000 MHz; 108-500 -> 2000 MHz; 500-1000 -> 5000 MHz; > 1000 MHz -> min(5*f_hi, 40 GHz) | f_hi (MHz) | e.g. 3 GHz clock -> measure to 15 GHz | calc | p.40 Table 2.3 | high |
| PAUL-1022 | compliance | FCC Class B radiated limits at 3 m (QP). | 30-88 MHz: 40 dBuV/m (100 uV/m); 88-216: 43.5 (150); 216-960: 46 (200); >960: 54 (500); >1 GHz: 54 AV and 74 peak | f, E (dBuV/m) | both antenna polarizations; antenna height scanned 1-4 m, max recorded | measure | p.38,40 Table 2.4 | high |
| PAUL-1023 | compliance | FCC Class A radiated limits at 10 m (QP). | 30-88 MHz: 39 dBuV/m (90 uV/m); 88-216: 43.5 (150); 216-960: 46.4 (210); >960: 49.5 (300); >1 GHz: 49.5 AV and 69.5 peak | f, E (dBuV/m) | both polarizations; 1-4 m height scan | measure | p.38,40 Table 2.5 | high |
| PAUL-1024 | compliance | CISPR 32 Class B radiated limits at 10 m (QP), OATS/SAC. | 30-230 MHz: 30 dBuV/m (31.6 uV/m); 230-1000 MHz: 37 dBuV/m (70.8 uV/m) | f, E | ITE/MME | measure | p.42 Table 2.6 | high |
| PAUL-1025 | compliance | CISPR 32 Class A radiated limits at 10 m (QP), OATS/SAC. | 30-230 MHz: 40 dBuV/m (100 uV/m); 230-1000 MHz: 47 dBuV/m (224 uV/m) | f, E | ITE/MME | measure | p.42 Table 2.7 | high |
| PAUL-1026 | compliance | Distance extrapolation (inverse-distance rule): field assumed proportional to 1/d. | E2_dB = E1_dB + 20log10(d1/d2); 3 m <-> 10 m: 20log10(10/3) = 10.46 dB | E1, d1, d2 | valid only in far field of emitter (approx. d > 3 lambda); at 30 MHz boundary ~30 m, at 1 GHz ~90 cm, so 3 m at 30 MHz is near field | calc | p.38-39 §2.1.1 | high |
| PAUL-1027 | compliance | CISPR 32 vs FCC (scaled to 10 m) Class B: CISPR more restrictive 88-216 MHz by 3 dB and 216-230 MHz by 5.5 dB; FCC more restrictive 230-960 MHz by ~1.5 dB. Class A: CISPR more restrictive 88-216 MHz by ~4 dB and 216-230 MHz by 6 dB; less restrictive 230-960 MHz by ~1 dB. | design to the envelope min(FCC, CISPR) per band | market list | QP detector | calc | p.44 §2.1.2, Fig.2.4 | high |
| PAUL-1028 | compliance | EU EMC Directive 2014/30/EU requires immunity (susceptibility) testing (IEC/EN 61000-4-x: ESD, radiated field, EFT/burst, surge, power-frequency H-field, pulsed H-field, damped oscillatory, dips/interruptions, harmonics, conducted CM 0 Hz-150 kHz); FCC does not. | test list | market | CE mark on compliance | review | p.44 §2.1.2 | high |
| PAUL-1029 | compliance | MIL-STD-461G core requirements applying to all systems: CE102 (power leads 10 kHz-10 MHz), RE102 (E-field 10 kHz-18 GHz), CS101 (power leads 30 Hz-150 kHz), CS114 (bulk cable injection 10 kHz-200 MHz), RS103 (E-field 2 MHz-40 GHz). | peak detector for all emissions; radiated measured at 1 m | platform | requirements can be waived/tailored by procuring activity | review | p.45 §2.1.3, Table 2.8-2.9 | high |
| PAUL-1030 | compliance | MIL-STD-461G RS103 field levels the EUT must withstand (see Table 2.10 in section 2). | 200 V/m aircraft external/safety-critical and ships above deck; 10 V/m metallic ships below deck; 20 V/m space; ground 10-50 V/m | platform, service, band | per Table 2.10 | measure | p.47 Table 2.10 | high |
| PAUL-1031 | compliance | Measurement procedures: FCC per ANSI C63.4-2014; CISPR 32 references CISPR 16; MIL-STD-461G self-contained. | - | - | - | review | p.48 §2.1.4 | high |
| PAUL-1032 | test | Commercial radiated-emission setup: OATS (preferred) or semianechoic chamber; EUT 1 m above ground plane; antenna height scanned 1-4 m; H and V polarization; biconical 30-200 MHz, log-periodic 200 MHz-1 GHz. | FCC B 3 m; FCC A 10 m; CISPR 32 A/B 10 m | - | QP detector (FCC/CISPR) | measure | p.50-51 §2.1.4.1 | high |
| PAUL-1033 | test | MIL-STD-461G radiated-emission setup: shielded absorber-lined room, 1 m distance, peak detector, no height scan (antenna at 120 cm); 104-cm rod 10 kHz-30 MHz, biconical 30-200 MHz, double-ridge horn > 200 MHz; H and V above 30 MHz. | - | - | - | measure | p.51 §2.1.4.1 | high |
| PAUL-1034 | compliance | LISN measured voltage maps directly to noise current out of phase/neutral through 50 ohm. | I_P = V_P/50; I_N = V_N/50; dBuA = dBuV - 34 (20log10(50) = 33.98) | V_P, V_N | 150 kHz-30 MHz; e.g. Class B 46 dBuV AV (0.5-5 MHz) = 12 dBuA = 4 uA | calc | p.54 §2.1.4.2; Prob.2.1.3 | high |
| PAUL-1035 | compliance | FCC/CISPR LISN element values (one side). | L1 = 50 uH (47..9425 ohm over 150 kHz-30 MHz; 0.019 ohm at 60 Hz); C2 = 1 uF (1.06..0.005 ohm; 2653 ohm at 60 Hz); C1 = 0.1 uF (10.6..0.05 ohm, dc block); R1 = 1 kohm (C1 discharge); 50 ohm receiver/dummy load | - | presents ~50 ohm phase-green and neutral-green, constant over band and site-to-site | inspect | p.53-54 §2.1.4.2, Fig.2.10-2.11 | high |
| PAUL-1036 | power | Choose SMPS switching frequency so the first harmonics fall below the 150 kHz conducted-emission start (unregulated). | n*f_sw < 150 kHz for the harmonics to exempt; example f_sw = 45 kHz puts 3rd harmonic at 135 kHz (50 kHz would put it at 150 kHz) | f_sw | FCC/CISPR 32 conducted; only marginal efficiency impact | calc | p.55 §2.1.5 | high |
| PAUL-1037 | emc | Even a trivial un-designed PCB fails: two 7 in parallel 15-mil lands 180 mils apart driven by a 10 MHz oscillator/74LS04 exceeded FCC Class B by up to 30 dB (horizontal) and ~15 dB (vertical) at 3 m. Plan EMC from the start. | margin deficit up to 30 dB | - | battery powered, no ac cord | review | p.60 §2.1.6, Fig.2.14-2.15 | high |
| PAUL-1038 | esd | Design for ESD from human/furniture discharge. | static voltage can approach 25 kV | - | EU requires ESD test; FCC and MIL-STD-461G do not | review | p.63 §2.2.3 | high |
| PAUL-1039 | compliance | Commercial aircraft: RTCA DO-160G (susceptibility, conducted/radiated emissions, ESD, lightning). Vehicles: CISPR 12 (off-board receivers), CISPR 25 (on-board receivers), SAE J551 (vehicle), SAE J1113 (component). | - | market | - | review | p.63 §2.2.4-2.2.5 | high |
| PAUL-1040 | dfm | Provide unpopulated optional EMC suppression footprints: capacitor pads at clock output and a series-resistor footprint in the clock land populated with 0 ohm; fix later by BOM change, not relayout. | footprint present on every clock net | clock nets | early design | inspect | p.65 §2.4 | high |
| PAUL-1041 | emc | Keep clock oscillators away from cable connectors on the PCB (oscillator adjacent to a connector couples to cable and radiates). | - | placement | cost-free only before layout | inspect | p.65 §2.4 | low |
| PAUL-1042 | process | Test the first prototype, however crude, for EMC; include an experienced EMC engineer from concept; enclosure/package shape fixes PCB and cable exit locations early. | - | - | - | review | p.65-66 §2.4 | low |
| PAUL-1043 | emc | Rectangular (zero-rise) pulse train spectrum: harmonics at n/T on a sin(x)/x envelope with nulls at multiples of 1/tau; one-sided magnitude = 2|cn|. | |cn| = (A*tau/T)*|sin(n*pi*tau/T)/(n*pi*tau/T)|; c0 = A*tau/T; 50% duty: c_n+ = 2A/(n*pi) odd n, 0 even n, c0 = A/2 | A (V), tau (s), T (s) | periodic | calc | p.77-79 eq.(3.23)-(3.27) | high |
| PAUL-1044 | emc | Trapezoidal clock/data one-sided harmonic magnitudes (equal rise/fall). | |c_n+| = 2*A*D*|sin(n*pi*D)/(n*pi*D)|*|sin(n*pi*tr*f0)/(n*pi*tr*f0)|, n>=1; c0 = A*D; D = tau/T; f0 = 1/T | A (V), D, tr (s, 0-100%), f0 (Hz) | only valid for tr = tf; replacing tr by (tr+tf)/2 when tr != tf "is not correct" (approximation only) | calc | p.95 eq.(3.48b-c), p.108 eq.(3.58) | high |
| PAUL-1045 | emc | Rise-time definitions: book uses 0-100% transition time; industry 10-90%. | tr(10-90%) = 0.8 * tr(0-100%) | tr | linear ramp | calc | p.93 §3.2.1 | high |
| PAUL-1046 | emc | Trapezoidal spectral bound (upper bound, worst case): flat at 2AD to f1, -20 dB/decade to f2, -40 dB/decade above. | f1 = 1/(pi*tau) = f0/(pi*D); f2 = 1/(pi*tr); L(f) = 20log10(2AD) for f<=f1; -20log10(f/f1) for f1<f<=f2; -20log10(f2/f1) - 40log10(f/f2) for f>f2 | A, D, f0, tr, f | tr = tf; tau >= tr; approximate bound | calc | p.96-98 eq.(3.49)-(3.54), Fig.3.19 | high |
| PAUL-1047 | emc | High-frequency spectral content of clocks/data is set by rise/fall time; increase tr/tf as much as timing allows to cut emissions. | example 1 V, 10 MHz, 50%: tr 20 ns -> 5 ns raises bound at 110 MHz from 78.45 to 90.5 dBuV (exact 73.8 -> 90.4 dBuV); measured 11th harmonic 68.0 -> 86.1 dBuV (+18 dB) | tr | trapezoid | calc | p.98-103 Ex.3.5, Fig.3.21 | high |
| PAUL-1048 | emc | Lowering the repetition rate (same D, same tr) lowers the HF envelope. | 1 V 50% tr = 20 ns: 10 MHz -> 1 MHz reduces bound at 110 MHz from 78.45 to 58.4 dBuV (-20 dB); f1 moves from 6.37 MHz to 637 kHz | f0 | clock frequency usually fixed by design | calc | p.104 Ex.3.5 | high |
| PAUL-1049 | emc | Reducing duty cycle (pulse width) lowers low-frequency content only; high-frequency content unchanged. | start level 2AD falls, f1 = f0/(pi*D) rises; new f1 lies on old -20 dB/dec segment | D | trapezoid | calc | p.108-109 §3.2.2.3, Fig.3.25 | high |
| PAUL-1050 | emc | Even harmonics vanish only at exactly 50% duty; small duty deviations change even-harmonic levels widely (odd stable) -> poor day-to-day repeatability of emissions at even clock harmonics. | even-harmonic magnitude ~ |sin(n*pi*D)| sensitive near D = 0.5 | D | clocks near 50% | review | p.96 §3.2.1 | high |
| PAUL-1051 | timing | Digital-waveform bandwidth estimate (guide, not hard): BW = 1/tr (~3x the second breakpoint 1/(pi*tr)); alternative 0.5/tr reproduces edges less well. | BW = 1/tr (Hz); first null of true spectrum at f = 1/tr; bound is 19.89 dB (=40log10(pi)) below the f2 level at 1/tr | tr (s) | 5 V 100 MHz tr = 1 ns: BW = 1 GHz, 10 harmonics reconstruct well | calc | p.105-107 eq.(3.55), RevEx.3.3 | high |
| PAUL-1052 | emc | Average power of 50% duty trapezoid; power is not a bandwidth criterion (96% of power in dc + fundamental). | Pav = V^2*[1/2 - tr/(3T)] (W, 1 ohm); example V = 5 V, tr = 1 ns, T = 10 ns -> 11.667 W; 10 harmonics hold 99.97%, 5 harmonics 99.84% | V, tr, T | tr = tf, D = 0.5 | calc | p.107-108 eq.(3.56) | high |
| PAUL-1053 | emc | Ringing (overshoot/undershoot) enhances the spectrum in a band around the ringing frequency; damp with series resistor, ferrite bead, or line matching. | enhancement centered at w = sqrt(alpha^2 + wr^2) ~ wr; ringing Ke^(-alpha t) sin(wr t) | K, alpha, fr | e.g. 1 MHz 5 V square wave + K = 0.5 V, fr = 30 MHz, alpha = 1e7: +5.76 dB | sim | p.109-111 eq.(3.59), RevEx.3.4 | high |
| PAUL-1054 | emc | Output spectrum bound of a linear system = input spectral bound + transfer-function Bode magnitude (dB add). For an RC lowpass, choose RC >> tau to cut HF substantially; RC << tau only rounds edges above 1/(pi*tau). | |Y|dB = |H|dB + |X|dB; RC corner 1/(2*pi*RC) vs 1/(pi*tau) | H(f), X(f) | linear system | calc | p.111-113 eq.(3.62), Fig.3.27 | high |
| PAUL-1055 | test | Spectrum analyzers display RMS; convert computed peak harmonic amplitude to RMS before comparing. | RMS_dB = peak_dB - 3.01 dB | c_n+ (peak) | sinusoidal harmonic | calc | p.103 §3.2.2.1 | high |
| PAUL-1056 | compliance | Minimum measurement (6 dB) bandwidths: FCC radiated 30 MHz-1 GHz 120 kHz, >1 GHz 1 MHz, conducted 150 kHz-30 MHz 9 kHz; CISPR 32 radiated 30 MHz-1 GHz 120 kHz, conducted 9 kHz. | RBW_min per band | band | using wider RBW only raises readings | measure | p.116 Tables 3.1-3.2 | high |
| PAUL-1057 | emc | Choose clock/data repetition rates so no harmonics of different signals fall within one measurement bandwidth of each other (they add in the receiver). | |n*f_a - m*f_b| > RBW (120 kHz radiated) for all harmonics in band; equal coincident levels add +6.02 dB | f_a, f_b, RBW | e.g. 10 MHz and 15 MHz clocks coincide at 90 MHz | calc | p.116 §3.3.1 | high |
| PAUL-1058 | emc | In-phase addition of two unequal harmonics within the RBW: increase over the larger. | dL = 20log10(1 + 10^(-Delta/20)); Delta 10 dB -> +2.39 dB; 18.3 dB -> +1.0 dB | Delta (dB) | upper bound (in phase) | calc | p.116-117 Table 3.3 | high |
| PAUL-1059 | test | Diagnose harmonic addition by narrowing the analyzer RBW (e.g. 103 kHz -> 30 kHz, below regulatory minimum for diagnostics only); no change => no addition. | - | - | diagnostic only | measure | p.117 §3.3.1 | high |
| PAUL-1060 | test | Detector hierarchy: QP <= peak; if QP exceeds the limit, peak surely does; peak screening that passes guarantees QP pass. Average detector ~1 Hz lowpass after envelope detector reveals narrowband clock harmonics hidden under broadband noise (e.g. motor arcing). | AV <= QP <= Peak | detector | FCC/CISPR use QP (+AV conducted); MIL uses peak | measure | p.117-118 §3.3.2 | high |
| PAUL-1061 | emc | Random NRZ data spectrum: PSD has nulls at multiples of the bit rate; treat data like clocks (increase rise/fall times). | Gx(f) = (X0^2/4)*delta(f) + (X0^2*T/4)*sin^2(pi*f*T)/(pi*f*T)^2 W/Hz | X0 (V), T (bit period s) | PCM-NRZ, equiprobable, zero rise time | calc | p.124 eq.(3.75), Fig.3.33 | high |
| PAUL-1062 | emc | Single (nonperiodic) pulse has a continuous spectrum; periodic-train coefficients from the pulse Fourier transform. | cn = X(j*n*w0)/T; rectangular pulse |X| = A*tau*|sin(w*tau/2)/(w*tau/2)| | X(jw), T | - | calc | p.119-121 eq.(3.65)-(3.67) | high |
| PAUL-1063 | timing | Per-unit-length delay by medium. | free space 3.33 ns/m = 85 ps/in; Teflon coax (er 2.1, v = 2.07e8) 4.8 ns/m = 122.7 ps/in; FR-4 stripline (er 4.7) 7.2 ns/m = 183.6 ps/in; microstrip/outer PCB estimate er' = (1+4.7)/2 = 2.85, v = 1.777e8 -> 5.6 ns/m = 143 ps/in | medium | 6-in stripline land = 1.1 ns | calc | p.135-136 §4 intro | high |
| PAUL-1064 | timing | Clock skew: route clock lands so every receiving module sees equal total path delay. | TD_path_i equal for all loads | route lengths | - | inspect | p.170 §4.4, Fig.4.21 | high |
| PAUL-1065 | transmission-line | Homogeneous medium relations: only one of l or c needed. | l*c = mu*eps; v = 1/sqrt(lc) = v0/sqrt(er); l = 1/(c v^2); c = 1/(l v^2); inhomogeneous: use er' with l*c = mu0*eps0*er' | l, c, er | TEM; static (dc) field solutions give c, l | calc | p.140 eq.(4.6)-(4.9) | high |
| PAUL-1066 | transmission-line | Two-wire line (equal radii) per-unit-length parameters. | exact: l = (mu0/pi)*acosh(s/(2rw)); c = pi*eps0/acosh(s/(2rw)); wide-sep: l = 0.4*ln(s/rw) uH/m = 10.16*ln(s/rw) nH/in; c = 27.78/ln(s/rw) pF/m = 0.706/ln(s/rw) pF/in | s (center-center), rw | wide-separation form within ~3% for s/rw > 5 (2.7% at 5); 5% high at s/rw = 4 | calc | p.146-148 eq.(4.18)-(4.25) | high |
| PAUL-1067 | transmission-line | One wire at height h above a ground plane (method of images). | exact: c = 2*pi*eps0/acosh(h/rw); l = (mu0/(2*pi))*acosh(h/rw); h >> rw: c = 2*pi*eps0/ln(2h/rw); l = (mu0/(2*pi))*ln(2h/rw) | h, rw | example 20 AWG (rw 16 mil), h = 1 cm: 14.26 pF/m, 0.779 uH/m, Zc 234 ohm | calc | p.148-149 eq.(4.26)-(4.29) | high |
| PAUL-1068 | transmission-line | Coaxial cable per-unit-length parameters (exact, no proximity effect). | l = (mu0/(2*pi))*ln(rs/rw) = 0.2*ln(rs/rw) uH/m = 5.08*ln(rs/rw) nH/in; c = 2*pi*eps/ln(rs/rw) = 55.56*er/ln(rs/rw) pF/m = 1.4*er/ln(rs/rw) pF/in | rw, rs (shield inner radius), er | RG58U (rw 16 mil, rs 58 mil, PE er 2.3): 0.2576 uH/m, 99.2 pF/m, v = 66% c, Zc ~51 ohm | calc | p.149-151 eq.(4.32)-(4.35) | high |
| PAUL-1069 | transmission-line | PCB line parameters from Zc and v. | Zc = sqrt(l/c); v = 1/sqrt(lc) = v0/sqrt(er'); l = Zc/v; c = 1/(v*Zc) | Zc, er' | - | calc | p.151-153 eq.(4.37)-(4.39) | high |
| PAUL-1070 | transmission-line | Stripline (centered strip, zero thickness) characteristic impedance. | Zc = (30*pi/sqrt(er)) / (we/s + 0.441); we/s = w/s for w/s >= 0.35; we/s = w/s - (0.35 - w/s)^2 for w/s <= 0.35 | s = plane-to-plane separation, w, er | t = 0; example s = 20 mil, w = 5 mil, er 4.7: 63.8 ohm, 113.2 pF/m, 0.461 uH/m, v 1.38e8 | calc | p.153 eq.(4.40) | high |
| PAUL-1071 | transmission-line | Microstrip characteristic impedance and effective permittivity (Wheeler/Hammerstad form). | w/h <= 1: Zc = (60/sqrt(er'))*ln(8h/w + w/(4h)); w/h >= 1: Zc = (120*pi/sqrt(er'))/(w/h + 1.393 + 0.667*ln(w/h + 1.444)); er' = (er+1)/2 + ((er-1)/2)/sqrt(1 + 10h/w) | h, w, er | t = 0; limits er' -> er (h << w), (er+1)/2 (h >> w); example h = 50, w = 5 mil, er 4.7: 151 ohm, er' 3.034, 38.46 pF/m, 0.877 uH/m | calc | p.153-154 eq.(4.41a-c) | high |
| PAUL-1072 | transmission-line | Simplified microstrip impedance (IPC-style). | Zc = (87/sqrt(er + 1.41))*ln(5.98h/(0.8w + t)) | h, w, t, er | valid 0.1 <= t/w <= 0.8; 1 oz Cu t = 1.38 mil -> 1.725 <= w <= 13.8 mil; example gives 151.8 ohm vs 151 exact | calc | p.154 eq.(4.41d) | high |
| PAUL-1073 | transmission-line | Coplanar strips on one side of a board (PCB I). | k = s/(s+2w); k' = sqrt(1-k^2); 1/sqrt2 <= k <= 1: Zc = (120/sqrt(er'))*ln(2(1+sqrt k)/(1-sqrt k)); 0 <= k <= 1/sqrt2: Zc = (377*pi/sqrt(er'))/ln(2(1+sqrt k')/(1-sqrt k')); er' = ((er+1)/2)*{tanh[0.775*ln(h/w) + 1.75] + (k*w/h)*[0.04 - 0.7k + 0.01(1 - 0.1er)(0.25 + k)]} | s (edge-edge), w, h, er | t = 0; example s = w = 15 mil, h = 62 mil, er 4.7: 144.45 ohm, v 1.8e8, 38.53 pF/m, 0.804 uH/m | calc | p.154-155 eq.(4.42) | high |
| PAUL-1074 | transmission-line | Strips on opposite sides of a board (PCB II / broadside). | w/h > 1: Zc = (377/sqrt(er)) / {w/h + 0.441 + ((er+1)/(2*pi*er))*[ln(w/h + 0.94) + 1.451] + 0.082*(er-1)/er^2}; w/h < 1: Zc = (377*sqrt2/(pi*sqrt(er+1)))*[ln(4h/w) + (1/8)(w/h)^2 - (1/2)((er-1)/(er+1))(0.452 + 0.242/er)] | w, h, er | t = 0; example w = 200 mil, h = 62 mil FR-4: 41.05 ohm (vs 155.7 ohm coplanar with s = 62 mil) | calc | p.155 eq.(4.43) | high |
| PAUL-1075 | pdn | Use wide lands on opposite sides of a substrate (low Zc = low l, high c) for dc power distribution to reduce L*di/dt drops. | Zc(opposite-side 200 mil) = 41 ohm << 155.7 ohm same-side | geometry | power distribution | calc | p.155 §4.2.2 | high |
| PAUL-1076 | termination | Reflection coefficients and initial launched wave. | GammaL = (RL - Zc)/(RL + Zc); GammaS = (RS - Zc)/(RS + Zc); current reflection = -Gamma; V_init = Zc/(RS + Zc)*VS; line looks like Zc for 0 <= t <= 2TD | RS, RL, Zc | lossless line | calc | p.157-158 eq.(4.47)-(4.52) | high |
| PAUL-1077 | termination | Load voltage lattice series. | V(L,t) = Zc/(RS+Zc)*(1+GammaL)*[VS(t-TD) + GammaS*GammaL*VS(t-3TD) + (GammaS*GammaL)^2*VS(t-5TD) + ...] | RS, RL, Zc, TD, VS(t) | resistive terminations | sim | p.167,172 eq.(4.53b),(4.62) | high |
| PAUL-1078 | termination | Ringing occurs whenever GammaS and GammaL have opposite signs (typical CMOS: RS < Zc, RL > Zc); monotonic settling when same sign. | ring if GammaS*GammaL < 0 | RS, RL, Zc | e.g. RS = 10 ohm, Zc = 50, open load, 5 V: V_init 4.17 V, load rings 8.33 / 2.78 V | calc | p.171-174 Table 4.1 | high |
| PAUL-1079 | components | Typical CMOS gate models for SI analysis. | output resistance 10-30 ohm (nonlinear); input capacitance 5-15 pF | - | typical | review | p.170-171 §4.4.1 | high |
| PAUL-1080 | termination | Capacitive load on a source-matched line adds delay (50% point) and rise time. | VL(t) = V0*(1 - exp(-(t-TD)/TC))u(t-TD); TC = Zc*C; td = 0.693*Zc*C | Zc, C | RS = Zc; e.g. 50 ohm, 5 pF -> 0.173 ns | calc | p.174-176 eq.(4.64)-(4.68) | high |
| PAUL-1081 | termination | Inductive load on a source-matched line gives decaying spike. | VL(t) = V0*exp(-(t-TD)/TL)u(t-TD); TL = L/Zc | L, Zc | RS = Zc | calc | p.176-177 eq.(4.72) | high |
| PAUL-1082 | termination | Series (source) match: add R so that RS + R = Zc; with open/CMOS load the half-amplitude wave doubles to V0 at the load; no dc power in R. | R = Zc - RS | RS, Zc | load ~ open circuit; point-to-point | calc | p.177-178 §4.4.2 | high |
| PAUL-1083 | termination | Parallel (load) match: R || RL = Zc; no reflection but load level = Zc/(RS+Zc)*V0 (< V0) and R dissipates power in the high state. | R*RL/(R+RL) = Zc; e.g. RS 25, Zc 50, V0 5 V -> 3.33 V | RS, RL, Zc | - | calc | p.178-179 §4.4.2 | high |
| PAUL-1084 | termination | The line "does not matter" (no matching required) when rise time exceeds ~10 one-way delays; rule of thumb for FR-4 outer-layer lands: tr(ns) > L(in) (uses tr > 7 TD, 0.1429 ns/in). | tr > 10*TD (L < v/(10*f_max), f_max = 1/tr); tr(ns) > L(in) | tr, L, v | example RS 20 ohm, Zc 50, 5 pF, TD 0.2 ns: overshoot 7 V (tr = TD), ~6 V (5TD), 5.3 V (10TD), 5.2 V (20TD) on 5 V | calc | p.179-180 eq.(4.73)-(4.76), Fig.4.28 | high |
| PAUL-1085 | transmission-line | Impedance discontinuity (width/layer/via change): reflection and transmission. | Gamma12 = (Zc2 - Zc1)/(Zc2 + Zc1); T12 = 1 + Gamma12 = 2Zc2/(Zc2 + Zc1) | Zc1, Zc2 | incident from line 1 | calc | p.180-185 eq.(4.77)-(4.78) | high |
| PAUL-1086 | termination | With an impedance discontinuity, eliminating reflections requires BOTH series match at source and parallel match at load; source match alone leaves multiple reflections. | series R at source AND R || RL = Zc2 at load | Zc1, Zc2 | e.g. 50 -> 100 ohm, open load: load overshoots to 6.667 V on 5 V | review | p.185-188 Ex.4.5-4.6 | high |
| PAUL-1087 | termination | Daisy-chain (series) distribution: series match at the source eliminates reflections if all segments have equal Zc. Do NOT parallel-terminate at the midpoint junction (gives Gamma = -1/3, T = 2/3 and multiple reflections). | R_mid = Zc at junction -> Gamma12 = Gamma21 = -1/3 | topology | CMOS loads ~open | review | p.189-190 Fig.4.32-4.33 | high |
| PAUL-1088 | termination | Star (parallel) distribution from one driver is less desirable: junction reflections persist unless loads are parallel-matched (costly current). | Gamma12 = Gamma21 = -Zc/(2RS + Zc); T = 2RS/(2RS + Zc); RS = Zc -> -1/3; RS = Zc/2 -> -1/2 | RS, Zc | equal delays only special case | calc | p.190-192 eq.(4.80) | high |
| PAUL-1089 | transmission-line | Sinusoidal steady state: input impedance, VSWR and power. | Zin = Zc*(ZL + j*Zc*tan(beta*L))/(Zc + j*ZL*tan(beta*L)); VSWR = (1+|GammaL|)/(1-|GammaL|); Pav = (|V+|^2/(2Zc))*(1-|GammaL|^2); P_refl/P_inc = |GammaL|^2 | ZL, Zc, beta = 2*pi/lambda, L | Zin repeats every lambda/2; lambda/4 short <-> open | calc | p.195-199 eq.(4.99)-(4.104) | high |
| PAUL-1090 | materials | Skin depth of a conductor. | delta = 1/sqrt(pi*f*mu0*sigma) (m); sigma_Cu = 5.8e7 S/m; mu0 = 4*pi*1e-7 | f, sigma | nonmagnetic conductor | calc | p.202 eq.(4.112) | high |
| PAUL-1091 | current-carrying | Wire resistance per unit length: dc and skin-effect. | rdc = 1/(sigma*pi*rw^2) ohm/m; rhf = 1/(sigma*2*pi*rw*delta) ohm/m for rw >> delta; rhf rises as sqrt(f) (10 dB/decade) | rw, sigma, f | - | calc | p.202-203 eq.(4.111) | high |
| PAUL-1092 | current-carrying | PCB land resistance per unit length: dc and skin-effect; asymptotes join where delta = wt/(2(w+t)) ~ t/2 (w >> t). | rdc = 1/(sigma*w*t); rhf = 1/(2*sigma*delta*(w+t)) ohm/m | w, t, sigma, f | ignores corner crowding; 1 oz Cu t = 1.38 mil | calc | p.203 eq.(4.113) | high |
| PAUL-1093 | materials | Dielectric loss: complex permittivity and loss tangent; conductance per unit length rises as f (20 dB/decade). | eps_c = er' - j*er''; tan(delta) = er''/er'; g = w*c*tan(delta) = w*tan(delta)/(v*Zc) | c, tan(delta), f | FR-4 tan(delta) ~ 0.02, fairly constant at HF (goes to 0 at dc); strictly homogeneous media only | calc | p.204-205,210 eq.(4.114)-(4.118),(4.127) | high |
| PAUL-1094 | transmission-line | Low-loss line (r << wl, g << wc): Zc and v as lossless; attenuation and loss. | alpha ~ (1/2)*(r/Zc + g*Zc) Np/m; beta ~ w*sqrt(lc); Loss_dB = 8.686*alpha*L; Loss_r = 4.343*(r/Zc)*L; Loss_g = 4.343*g*Zc*L = 4.343*w*sqrt(er)*tan(delta)*L/v0 dB | r, g, Zc, L | matched line; Loss_g formula homogeneous only (independent of cross-section) | calc | p.206-210 eq.(4.120)-(4.128) | high |
| PAUL-1095 | transmission-line | Stripline loss anchor (s = 20 mil, w = 5 mil, FR-4, tan = 0.02): low-loss above ~5 MHz; rhf dominates above 23 MHz; at 1 GHz r = 25.46 ohm/m, g = 1.423e-2 S/m, alpha = 0.653, Loss_r = 1.73 dB/m, Loss_g = 3.94 dB/m; 6 in -> 0.86 dB. Above 1 GHz dielectric loss dominates. | g = 14.2e-12*f S/m; r = 8.05e-4*sqrt(f) ohm/m; alpha(100 MHz) = 0.1085 | f, L | this geometry | calc | p.206-210 §4.5.4 | high |
| PAUL-1096 | transmission-line | Losses cause dispersion (frequency-dependent v and alpha): HF attenuated more, pulse bandwidth reduced, rise/fall times increased. | v = w/beta(f) | r(f), g(f) | - | sim | p.205-206 §4.5.4 | high |
| PAUL-1097 | transmission-line | Lumped-pi/T line models are valid only while the line is electrically short at the highest source frequency; cascading many sections gives little extension; lumped r, g cannot represent frequency-dependent loss in time domain. | L < 0.1*lambda(f_max) | L, f_max | SPICE modeling | review | p.210-211 §4.6 | high |
| PAUL-1098 | components | Primary frequencies of interest for suppression components are the regulatory bands (FCC: 150 kHz-30 MHz conducted, 30 MHz-40 GHz radiated); verify component impedance by measurement at the target frequency. | - | f_target | out-of-band emissions still cause field interference | measure | p.221 §5 intro | high |
| PAUL-1099 | current-carrying | Copper wire skin depth (quick form) and skin-effect onset. | delta = 6.6e-2/sqrt(f) m = 2.6e3/sqrt(f) mils (Cu); resistance starts rising where rw = 2*delta | f (Hz), rw | Cu sigma 5.8e7; e.g. 20 AWG onset 105.8 kHz | calc | p.225-227 eq.(5.2),(5.3); Prob.5.1.3 | high |
| PAUL-1100 | current-carrying | Wire resistance (dc and HF) for a total length L. | R = L/(sigma*pi*rw^2); rhf ~ 1/(2*pi*sigma*rw*delta) = rdc*rw/(2*delta) = (1/(2rw))*sqrt(mu0/(pi*sigma))*sqrt(f) ohm/m | L, rw, f | rw >> delta for rhf; e.g. 20 AWG, 2 in, 200 MHz: 1.44 ohm/m, 73.4 mohm | calc | p.223-228 eq.(5.1),(5.3), Ex.5.1 | high |
| PAUL-1101 | components | Stranded wire: R and internal L ~ single-strand value / number of strands S; external L and C ~ solid wire of equivalent radius. | R_str = R_strand/S; L_int,str = L_int,strand/S | S, rws | approximation | calc | p.222 §5.1 | high |
| PAUL-1102 | components | Wire internal inductance (dc and skin-effect). | li,dc = mu0/(8*pi) = 50 nH/m = 1.27 nH/in (rw << delta); li,hf = (2*delta/rw)*li,dc = (1/(4*pi*rw))*sqrt(mu0/(pi*sigma))/sqrt(f) (falls -10 dB/decade) | rw, f | e.g. 20 AWG 200 MHz: 1.15 nH/m | calc | p.227-228 eq.(5.4) | high |
| PAUL-1103 | components | Loop inductance of a wire pair; external inductance dominates internal (~10x for 20 AWG at 50 mil) so internal L may be neglected. | L_loop = 2*li*L + le*L; le = 0.4*ln(s/rw) uH/m = 10.16*ln(s/rw) nH/in | s, rw, L | s/rw > 5; e.g. 20 AWG @ 50 mil: le 0.456 uH/m vs li,dc 0.05 uH/m | calc | p.229-232 eq.(5.5) | high |
| PAUL-1104 | components | Wire-pair capacitance and Zc; insulation does not change le; c formula only approximates insulated (inhomogeneous) wires (no closed form). | c = 27.78/ln(s/rw) pF/m = 0.706/ln(s/rw) pF/in; Zc = 120*ln(s/rw) ohm (air) | s, rw | s/rw > 5; e.g. two 20 AWG at 1/4 in: 27.9 nH/in, 0.257 pF/in | calc | p.230-232 eq.(5.6)-(5.7) | high |
| PAUL-1105 | components | Choose the lumped model by load impedance: low-impedance load (<< Zc) -> lumped-T or lumped-Gamma; high-impedance load -> lumped-Pi or backward-Gamma. | ZL << Zc vs ZL >> Zc | ZL, Zc | electrically short (L << lambda) | review | p.230-231 §5.1.3, Fig.5.4 | high |
| PAUL-1106 | fab | PCB cladding thickness and board data used for land calculations. | 1 oz Cu = 1.38 mil; 2 oz = 2.76 mil; FR-4 er ~ 4.7; board thickness 47-62 mil typical; v = 11.8/sqrt(er') in/ns | - | - | calc | p.232-234 §5.2, eq.(5.9b) | high |
| PAUL-1107 | components | Component lead loop model: two 0.5-in leads 0.25 in apart (20 AWG) ~ 14 nH loop inductance and ~0.128 pF lead capacitance; lump L in either lead. | L_lead = le*l_lead; C_lead = c*l_lead | lead length, spacing, rw | electrically short leads | calc | p.235 §5.3 | high |
| PAUL-1108 | components | Resistor HF model: R || Cpar, in series with Llead; Cpar (lead + leakage) typ. 1-2 pF; high-value resistors dominated by Cpar. | f1 = 1/(2*pi*R*Cpar); f0 = 1/(2*pi*sqrt(Llead*Cpar)); e.g. 1 kohm, 1 pF -> XC = R at ~159 MHz, SRF ~1.3 GHz | R, Cpar, Llead | measured 1 kohm 1/8 W carbon, 0.5 in leads: f1 ~ 120 MHz; fit R 1.05 kohm, Cpar 1.2 pF, Llead 14 nH | calc | p.238-243 eq.(5.12)-(5.13), Fig.5.12 | high |
| PAUL-1109 | components | Avoid wire-wound resistors where di/dt is high (e.g. SMPS current-sense ~1 ohm): inductance differentiates the current, creating fast spikes at the switching rate; carbon tolerance 5-10%. | v = R*i + L*di/dt | resistor type | - | review | p.238 §5.4 | high |
| PAUL-1110 | decoupling | Capacitor HF model: series C + Llead + ESR; self-resonant frequency. Above SRF the capacitor is inductive. Use only below SRF for shunting. | f0 = 1/(2*pi*sqrt(Llead*C)); |Z(f0)| = ESR; with 14 nH: 470 pF -> 62 MHz; 0.1 uF -> 4.25 MHz | C, Llead, ESR | ESR several ohms (electrolytic, f-dependent), negligible for ceramic in regulatory band | calc | p.243-245 eq.(5.17)-(5.18) | high |
| PAUL-1111 | decoupling | Capacitor families: tantalum electrolytic 1-1000 uF for conducted band and bulk storage; ceramic 5 pF-1 uF stays ideal to much higher frequency for radiated-band suppression. | - | band | - | review | p.243-244 §5.5 | high |
| PAUL-1112 | decoupling | Increasing a shunt capacitor value can INCREASE emissions above its SRF (lower SRF, inductive). Measured at 100 MHz with 0.5-in leads: 100 pF = 8 ohm, 10,000 pF = 12 ohm. | choose C with SRF > f_noise | C, f_noise | lead length fixed | measure | p.247-250 §5.5 | high |
| PAUL-1113 | emc | Shunt capacitor diversion by current division: effective only if Z_CAP << Z_LOAD; parallel capacitors work best in high-impedance circuits. | I_C = Z_LOAD/(Z_CAP + Z_LOAD)*I_NOISE | Z_CAP(f), Z_LOAD(f) | e.g. 90% of 100 MHz into 1 kohm load needs 3.3 pF | calc | p.250-251 eq.(5.19), RevEx.5.6 | high |
| PAUL-1114 | emc | Series inductor/ferrite blocking effective only if its impedance >> the series path impedance Z_LOAD; series inductors work best in low-impedance circuits. Use on slow lines (reset, green wire); can cause ringing on fast signals. | |Z_L| >> |Z_LOAD| | Z_L(f), Z_LOAD(f) | e.g. 20 dB reduction of 100 MHz across 50 ohm needs ~0.8 uH (Prob.5.6.2) | calc | p.253 §5.6 | high |
| PAUL-1115 | components | Inductor HF model: (Rpar + L) || Cpar; inductive above Rpar/L, capacitive above SRF; larger L lowers SRF. | f0 = 1/(2*pi*sqrt(L*Cpar)); measured 1.2 uH: SRF ~110 MHz, Cpar ~1.7 pF; 10 uH: SRF ~40 MHz, Cpar ~1.6 pF | L, Cpar, Rpar | layered windings raise Cpar | calc | p.251-253 eq.(5.21)-(5.22), Fig.5.23 | high |
| PAUL-1116 | emc | RC filter at a connector (RC pack): break frequency 1/(2*pi*RC) must stay above the functional signal spectrum or waveform distorts; too high gives little filtering. A shunt C at a cable may ring with cable inductance. | f_RC = 1/(2*pi*R*C) vs signal BW (1/tr) | R, C, tr | - | calc | p.250 §5.5 | high |
| PAUL-1117 | magnetics | Toroid inductance and saturation: permeability (and L) falls with dc/low-frequency current as the core saturates. | L = ur*mu0*N^2*A/l; mu = dB/dH | ur, N, A, l, I | ur values quoted at low current, <= 1 kHz | calc | p.255-256 eq.(5.23) | high |
| PAUL-1118 | magnetics | Flux split between core and leakage path by reluctance (magnetic current divider). | R = l/(mu*A); NI = R*psi; psi_core = R_air/(R_air + R_core)*psi | l, mu, A | high-mu core keeps flux (e.g. steel ur 1000) | calc | p.256 eq.(5.24)-(5.26) | high |
| PAUL-1119 | magnetics | Pick ferrite material for the band: MnZn = high initial ur but falls fast with f (conducted band); NiZn = lower initial ur but better above ~tens of MHz (radiated band). A core with ur 2000 at 1 kHz may be < 100 in the regulatory range. | 5-turn toroid: MnZn ~500 ohm @1 MHz, 380 ohm @60 MHz; NiZn ~80 ohm @1 MHz, 1200 ohm @60 MHz | f band | catalog cores by type (color-code) | measure | p.257-258 §5.7, Fig.5.26-5.27 | high |
| PAUL-1120 | emc | Ferrite bead = frequency-dependent R(f) in series with L(f) from complex permeability; ~100 ohm above ~100 MHz typical; multi-hole/multi-turn beads raise Z. Limited to a few hundred ohm -> use in low-impedance circuits (power supplies), bead + shunt C = 2-pole lossy lowpass, damps ringing. | Z = w*ur''*mu0*K + j*w*ur'*mu0*K | ur'(f), ur''(f) | saturates with high-level low-frequency current (e.g. 1-10 A at 60 Hz) | measure | p.258-260 eq.(5.27)-(5.28) | high |
| PAUL-1121 | emc | Common-mode vs differential-mode decomposition of a conductor pair. | I_D = (I1 - I2)/2; I_C = (I1 + I2)/2; I1 = I_C + I_D; I2 = I_C - I_D | I1, I2 | uA of CM radiate like tens of mA of DM | calc | p.261-262 eq.(5.29)-(5.30) | high |
| PAUL-1122 | emc | Common-mode choke: CM sees L + M per line, DM sees L - M (leakage, ~0 if L = M); DM (functional) flux cancels so the core does not saturate; ferrite adds R(f) for CM. | Z_CM = jw(L+M); Z_DM = jw(L-M); k = M/sqrt(L1*L2) ~ 1 | L, M | symmetric windings | calc | p.262-264 eq.(5.31)-(5.33), p.299-300 eq.(6.14)-(6.16) | high |
| PAUL-1123 | emc | CM choke construction: wind all conductors of the group together around the core; keep input and output leads separated on the core (input-output parasitic C shunts the choke). | - | winding | - | inspect | p.263-264 Fig.5.35 | high |
| PAUL-1124 | emc | DC motor brush arcing radiates (typically 200 MHz-1 GHz depending on motor); suppress with R/C disks across commutator segments, small series inductors in dc leads, and a CM choke in driver leads (motor frame capacitance to product frame forms a large CM loop). | measured CM impedance nulls (wires tied to frame): dc motor ~1 ohm near 100 MHz; stepper ~3 ohm near 70 MHz; solenoid ~8 ohm near 150 MHz | motor type | frame bonded for cooling | measure | p.265-268 §5.10 | high |
| PAUL-1125 | emc | Downstream buffers "square up" edges slowed by an upstream filter: place edge-rate control after the last driver; filter at the source. | - | net topology | - | review | p.269 §5.11 | medium |
| PAUL-1126 | emc | Treat every conductor as potentially carrying HF (e.g. microprocessor reset line, -12 V lead of an RS-232 driver): route "rare-event" lines short. | - | nets | - | review | p.269-270 §5.11-5.12 | low |
| PAUL-1127 | reliability | EMC margin must cover part-to-part and vendor-to-vendor variation: vendors guarantee max rise time (functional) but not min rise time (EMC); re-qualify EMC on any vendor change. | EMC analysis uses tr_min | tr_min, vendor | RS-232 driver example 10-210 MHz variability | review | p.270 §5.12 | high |
| PAUL-1128 | protection | Contact arcing thresholds in air. | VB (min breakdown) ~ 320 V at d_min = 0.3 mil (0.00762 mm); glow VG ~ 280 V; arc VA ~ 12 V (11-16 V, material dependent); IG ~ 1-100 mA; IA ~ 0.1-1 A; short-arc field EB ~ 1e9 V/m; VB,glow = 320 + 7e6*d; VG = 280 + 1000*d (d units not printed; SI metres inferred) | d, contact material | atmospheric pressure; Paschen VB = K1*p*d/(K2 + ln(p*d)) | calc | p.271-274 eq.(5.34)-(5.36) | high |
| PAUL-1129 | protection | Inductive-load contact protection criteria (prevent arc initiation). | (a) EB*v > Vdc/(RL*C) (initial dV/dt = I0/C below ~1 V/us for EB = 1e8 V/m, v = 0.01 m/s); (b) (Vdc/RL)*sqrt(L/C) < VB,gas ~ 320 V; non-oscillatory if sqrt(L/C) < RL/2 | Vdc, RL, L, C, v | I0 = Vdc/RL | calc | p.275-276 §5.13.3 | high |
| PAUL-1130 | protection | RC snubber across contacts: size C and R. | C >= (I0/320)^2*L; C >= I0*1e-6 (F, I0 in A); Vdc/IA,min < R < RL; with diode across R: R >= Vdc/IA,min | Vdc, RL, L, IA,min | e.g. Vdc 50 V, RL 500 ohm, L 10 mH, IA 0.25 A -> C > 0.1 uF, 200 < R < 500 ohm | calc | p.276-278 eq.(5.37)-(5.38); Prob.5.13.1 | high |
| PAUL-1131 | protection | Free-wheeling diode across an inductive load clamps the switch (transistor collector to +VCC); place the diode very close to the inductor to minimize the radiating loop of the circulating current. Resistive loads drawing < IA,min need no contact protection. | - | layout | - | inspect | p.278 §5.13.3, Fig.5.44 | high |
| PAUL-1132 | compliance | A product failing conducted emissions will likely fail radiated too; give conducted-emission control equal priority (single path: the power cord). | - | - | - | review | p.287 §6 intro | medium |
| PAUL-1133 | compliance | LISN element impedances over the conducted band (sanity values for the measurement model). | 50 uH: 47.1 ohm @150 kHz, 9424.8 ohm @30 MHz; 0.1 uF: 10.61 / 0.053 ohm; 1 uF: 1.06 / 0.0053 ohm; at 60 Hz: 50 uH 18.8 mohm, 0.1 uF 26.5 kohm, 1 uF 2.7 kohm | f | 1 kohm bleeders; 50 ohm receiver + 50 ohm dummy load | calc | p.289-290 Table 6.1 | high |
| PAUL-1134 | emc | Conducted emissions: LISN voltages from CM/DM currents; unlike radiated emissions, CM current can equal or exceed DM current in conducted emissions. DM here is the noise (not the 60 Hz) current. | V_P = 50*(I_C + I_D); V_N = 50*(I_C - I_D); I_D = (I_P - I_N)/2; I_C = (I_P + I_N)/2; if one dominates, V_P ~ V_N ~ 50*I_dom | I_P, I_N | 150 kHz-30 MHz, LISN ideal | calc | p.291-292 eq.(6.1)-(6.6) | high |
| PAUL-1135 | emc | Clock harmonics coupled onto the ac cord fall in the conducted band (e.g. 10 MHz clock -> 10, 20, 30 MHz) and are measured by the LISN. | n*f_clk <= 30 MHz counts | f_clk | - | review | p.291 §6.1.1 | high |
| PAUL-1136 | emc | Green-wire (safety ground) CM inductor: wind several turns of the green wire on a ferrite toroid (never solder an inductor into the safety path). | typical 0.5 mH -> ~471 ohm at 150 kHz; HF effectiveness degraded by winding capacitance | L_GW | safety: fault path preserved | inspect | p.292-293 §6.1.2, Fig.6.5a | high |
| PAUL-1137 | emc | Two-wire (no green wire) products still have CM conducted emissions via stray capacitance chassis-to-test-site and transformer primary-secondary capacitance; do not assume CM = 0. Use a 60 Hz transformer at the power entry for shock safety. | - | construction | LISN bonded to test ground plane | review | p.293-294 Fig.6.5b | high |
| PAUL-1138 | filter | Filter insertion loss definition; IL depends on source and load impedances. Datasheet IL (50 ohm/50 ohm, separate CM and DM tests) may not predict in-product performance. | IL_dB = 20log10(|V_L,without|/|V_L,with|); series-L lowpass: IL = 10log10(1 + (w*tau)^2), tau = L/(RS + RL) | RS, RL, L | CM test: phase+neutral tied vs green; DM test: phase vs neutral, green open | calc | p.294-297 eq.(6.7)-(6.12), Fig.6.8 | high |
| PAUL-1139 | filter | Generic ac power-line filter topology (Pi-like): green-wire inductor L_GW, line-to-line X-caps C_DL/C_DR (DM), line-to-ground Y-caps C_CL/C_CR (CM), CM choke (L, M). Y-caps must be safety-approved; value limited by allowed 60 Hz leakage current. | C_Y,max = I_leak/(2*pi*f_line*V_line); e.g. 150 uA -> 3316 pF (120 V, 60 Hz) | I_leak, V, f | UL-type leakage limits | calc | p.298 §6.2.3, RevEx.6.1 | high |
| PAUL-1140 | filter | Typical filter values and effectiveness thresholds: CD ~ 0.047 uF (X), CC ~ 2200 pF (Y); left-side Y-caps parallel the 50 ohm LISN so they only divert CM where |Z_C| << 50 ohm (2200 pF = 50 ohm at 1.45 MHz). CM choke L ~ 10 mH -> w(L+M) = 18,850 ohm @150 kHz, 3.77 Mohm @30 MHz (ideal; parasitic C limits). | f(|Z_CY| = 50 ohm) = 1/(2*pi*50*C_Y) | C_Y, L | ideal values | calc | p.298-300 §6.2.3 | high |
| PAUL-1141 | filter | Green-wire inductor only helps if left line-to-ground caps C_CL exist: without them 2*L_GW (e.g. 2 mH) is in series with the choke L + M (e.g. 55 mH) and has little effect. | I_LISN/I_choke = 1/(1 - w^2*2*L_GW*C_CL + j*w*50*C_CL) | L_GW, C_CL | symmetric filter | calc | p.300-301 Fig.6.11 | high |
| PAUL-1142 | filter | With both L_GW and LISN-side Y-caps C_CL, CM current into the LISN rolls off -40 dB/decade above f0; without L_GW only -20 dB/decade above f1. | f0 = 1/(2*pi*sqrt(2*L_GW*C_CL)) (1 mH, 3300 pF -> 62 kHz); f1 = 1/(2*pi*50*C_CL) (3300 pF -> 965 kHz) | L_GW, C_CL | symmetric filter, ideal LISN | calc | p.301-302 §6.2.3 | high |
| PAUL-1143 | filter | DM equivalent circuit: X-caps appear doubled (2*C_D); Y-caps also load DM when no X-cap parallels them; an ideal CM choke (L = M) is transparent to DM. | DM corner where |Z(2*C_D + C_C)| = 50 ohm (0.203 uF -> 15.7 kHz) | C_D, C_C | - | calc | p.302-303,308 Fig.6.12 | high |
| PAUL-1144 | emc | Dominant-effect rule for conducted emissions: at a failing frequency only reducing the dominant component (CM or DM) lowers the total; change the filter element that acts on that component (X-caps/DM inductors for DM; Y-caps/CM choke/green-wire L for CM). | I_total = I_C +/- I_D ~ max(|I_C|, |I_D|) when one dominates | I_C(f), I_D(f) | dominance may switch across the band | measure | p.303-304 eq.(6.17), Fig.6.13 | high |
| PAUL-1145 | test | Separate CM and DM conducted emissions with a balun combiner on the LISN outputs. | V_P + V_N = 2*V_C; V_P - V_N = 2*V_D | V_P, V_N phasors | wideband transformers; switchable polarity | measure | p.304-305 eq.(6.18), Fig.6.14 | high |
| PAUL-1146 | filter | CM-choke leakage inductance L(1-k) provides useful DM attenuation; use small air-core inductors (not individual ferrite-core inductors, which saturate on 60 Hz current) for extra DM filtering in phase and neutral. | L_leak = L - M = L*(1 - k); 28 mH, k = 0.98 -> 560 uH; k = 0.95 -> 1.4 mH | L, k | measured: adding 28 mH choke drastically cut DM | calc | p.309 §6.2.4; Prob.6.2.6 | high |
| PAUL-1147 | filter | Unfiltered product example: conducted emissions exceeded FCC Class B by > 30 dB with CM and DM of the same order; each filter element then reduced only its own mode (Y-caps both modes above ~2 MHz; 0.1 uF X-cap DM; 1 mH green-wire L CM; 28 mH CM choke DM via leakage). | - | - | switching-supply digital product | measure | p.306-309 Figs.6.16-6.20 | high |
| PAUL-1148 | filter | Green-wire inductor self-resonance limits HF blocking. | 1 mH with 10 pF parasitic: SRF 1.6 MHz; only 532 ohm at 30 MHz | L, Cpar | - | calc | Prob.6.2.2 p.322 | high |
| PAUL-1149 | power | Power-supply type trade-off: linear supplies are quietest (efficiency 20-40%); SMPS 60-90% efficient, switching 20-100 kHz (some to 1 MHz) but inherently noisier. | - | topology | - | review | p.312 §6.3.1-6.3.2 | high |
| PAUL-1150 | power | Buck converter average output and duty cycle; chopped node is a trapezoid for spectral estimation. | V_av = D*Vdc; D = tau/T; e.g. 100 V -> 5 V at 50 kHz: D = 0.05; 25th harmonic (1.25 MHz) bound 128.1 dBuV, exact 125.1 dBuV | Vdc, Vout, fs | ideal chopper | calc | p.313 eq.(6.20); Prob.6.3.1 | high |
| PAUL-1151 | power | SMPS switch gate resistor RG slows switch edges (lower conducted/radiated spectrum) at the cost of switch dissipation/efficiency. | tr up -> HF spectrum down (Ch.3 bound); P_switch up | RG | thermal limit | sim | p.314-315 §6.3.2 | high |
| PAUL-1152 | power | Switch-to-heatsink capacitance (insulating washer) couples switching noise; if the heatsink is bonded to the green wire it creates a CM conducted path. | - | mechanical | - | review | p.315-316 §6.3.2 | high |
| PAUL-1153 | power | Primary-side (flyback, off-line) switchers feed switching harmonics straight to the line cord through the bridge (no 60 Hz transformer filtering) -> larger power-line filter burden. | - | topology | - | review | p.315 §6.3.2 | high |
| PAUL-1154 | power | Rectifier diode reverse recovery generates HF spectrum: prefer soft-recovery diodes; place an RC snubber across the diode with short leads, very close, to minimize the loop. | - | diode type | fast/hard recovery favored for efficiency | inspect | p.315-316 Fig.6.24 | high |
| PAUL-1155 | magnetics | Gapped ferrite (E-core) SMPS transformers radiate low-frequency magnetic fields at the switching frequency and harmonics from the air gap. | - | core type | gap used to prevent saturation | review | p.317-318 §6.3.3 | high |
| PAUL-1156 | magnetics | Lap-wound transformer primary-secondary capacitance couples secondary-side HF noise (e.g. >10 MHz clocks) to the line side; insert a Faraday shield between windings and connect it to the PRIMARY ground so the noise current circulates without passing through the LISN. | shield to primary side; wrong (secondary) connection sends current through line cord | winding construction | same principle for signal transformers: ground shield at receiver input side | inspect | p.318-319 Fig.6.26 | high |
| PAUL-1157 | emc | Ferrite beads are effective in power supplies because circuit impedances there are low (below bead impedance of a few hundred ohm). | Z_bead >> Z_path | Z_path | - | calc | p.319 §6.3.3 | high |
| PAUL-1158 | emc | Place the power-line filter directly at the power-cord exit and the power supply close to the filter; internal noise (20 kHz to > 500 MHz) coupled onto cord wiring bypasses the filter; filters designed for 150 kHz-30 MHz will not stop a 50 MHz clock or its harmonics. | filter-to-cord-exit distance ~ 0 | layout | - | inspect | p.319-320 §6.4, Fig.6.27 | high |
| PAUL-1159 | emc | Do not route digital data/clock wiring near the power-supply output or input wires (couples to the cord). | - | routing | - | inspect | p.310 §6.3 | high |
| PAUL-1160 | compliance | Design and test ac-input conducted susceptibility (lightning-induced surges, momentary interruptions) by direct injection; the emission filter may be insufficient for surge levels. | - | - | manufacturer tests | measure | p.321 §6.5 | medium |
| PAUL-1161 | antenna | Hertzian (short electric) dipole far field, broadside maximum; basis of wire/CM emission estimates. | |E_theta| = eta0*beta0*I*dl*sin(theta)/(4*pi*r) = f*mu0*I*dl*sin(theta)/(2r) (V/m, I peak); |H| = |E|/eta0; eta0 = 120*pi ~ 377 ohm; numerically |E| = 6.283e-7*f*I*dl*sin(theta)/r | f (Hz), I (A), dl (m), r (m) | electrically short element, uniform current; far field; e.g. 1 cm, 1 A, 100 MHz, 1000 m: 6.28e-4 V/m, H 1.67e-6 A/m | calc | p.327-328 eq.(7.2),(7.3c), Ex.7.1 | high |
| PAUL-1162 | antenna | Near/far-field boundary: Hertzian dipole terms cross at r = lambda0/(2*pi) ~ lambda0/6, but use the larger of 3*lambda0 (wire antennas) or 2*D^2/lambda0 (surface antennas) as the practical far-field criterion; EMC measurements (esp. FCC Class B at 3 m, low frequency) are often in the near field. | r_ff = max(3*lambda0, 2*D^2/lambda0) | f, D | 2D^2/lambda0 -> phase error <= lambda0/16; 3*lambda0 -> wave impedance ~ free space | calc | p.327 §7.1.1; p.366 §7.5 | high |
| PAUL-1163 | antenna | Inverse-distance scaling |E_D2| = (D1/D2)*|E_D1| is valid only when both distances are in the far field. | E2 = E1*D1/D2 | D1, D2, f | far field only | calc | p.328 §7.1.1, RevEx.7.1 | high |
| PAUL-1164 | antenna | Hertzian dipole radiated power and radiation resistance: a very inefficient radiator. | Prad = 80*pi^2*(dl/lambda0)^2*|I|^2/2 W (I peak); Rrad = 80*pi^2*(dl/lambda0)^2 ohm; 1 cm @300 MHz: 79 mohm (1 W needs 3.6 A RMS); @3 MHz: 7.9 mohm (356 A) | dl, lambda0 | - | calc | p.329 eq.(7.5)-(7.6) | high |
| PAUL-1165 | antenna | Small loop (magnetic dipole) far field: shape irrelevant if electrically small; field max in the plane of the loop. | m = I*A (A = pi*b^2); |E_phi| = eta0*beta0^2*m*sin(theta)/(4*pi*r) = (pi^2*mu0/v0)*f^2*I*b^2*sin(theta)/r => |E| = 1.316e-14*f^2*I*A*sin(theta)/r (V/m; f Hz, I A peak, A m^2, r m) | f, I, A, r | loop circumference < lambda0/10; far field; numeric constant evaluated from eq.(7.9a) (reproduces Ex.7.2: 109.6 uV/m) | calc | p.330-331 eq.(7.7)-(7.9) | medium |
| PAUL-1166 | emc | A small PCB current loop easily fails Class B: 1 x 1 cm loop (equiv. radius 5.64 mm), 100 mA at 50 MHz gives 109.6 uV/m = 40.8 dBuV/m at 3 m > 40 dBuV/m FCC Class B (30-88 MHz). Minimize loop area x current x f^2. | E proportional to f^2*I*A | loop area, I, f | in-plane maximum, free space | calc | p.331 Ex.7.2 | high |
| PAUL-1167 | antenna | Loop radiation resistance. | Rrad = 31,170*(A/lambda0^2)^2 ohm; 1 cm radius @300 MHz: 3.08 mohm (1 W needs 18 A RMS) | A, lambda0 | electrically small | calc | p.331 eq.(7.10) | high |
| PAUL-1168 | antenna | Long (center-fed) dipole far field and pattern. | E_theta = j*60*I_m*exp(-j*beta0*r)*F(theta)/r; F(theta) = [cos(pi*l*cos(theta)/lambda0) - cos(pi*l/lambda0)]/sin(theta); half-wave: F = cos((pi/2)cos(theta))/sin(theta), |E|max = 60*|I_m|/r broadside | I_m (peak input current for half-wave), l, r | sinusoidal current distribution; far field | calc | p.333-335 eq.(7.16)-(7.20) | high |
| PAUL-1169 | antenna | Half-wave dipole / quarter-wave monopole input impedance and radiated power. | half-wave dipole: Rrad = 73 ohm, Xin = 42.5 ohm; Prad = 73*|I_RMS|^2; quarter-wave monopole: Rrad = 36.5 ohm, Xin = 21.25 ohm; Sav = 4.77*|I_m|^2*F^2/r^2 W/m^2 (eta0/(8*pi^2) = 4.77) | I | monopole over perfect ground radiates half the dipole power | calc | p.337-338 eq.(7.21)-(7.25) | high |
| PAUL-1170 | antenna | Electrically short antennas: small Rrad, large capacitive reactance -> little radiated power unless loaded; monopoles are cut slightly shorter than lambda/4 for zero reactance. | lambda0/8 dipole: Rrad ~ 1.5 ohm, Xin ~ -600 ohm; 100 V peak 50 ohm source at 150 MHz: 20.7 mW (vs 21.36 W for half-wave); +0.637 uH loading -> 2.81 W | l/lambda0 | Fig.7.6 graph (Jordan & Balmain) | calc | p.338-342 Ex.7.3, Fig.7.6 | high |
| PAUL-1171 | antenna | Antenna conductor loss from skin effect. | Rloss = rwire*l/2 for a dipole of total length l; rwire = 1/(2*pi*rw*delta*sigma); 20 AWG @150 MHz: delta = 5.4e-6 m (0.212 mil), r = 1.25 ohm/m, Rloss = 0.63 ohm; Ploss = |I|^2*Rloss/2 (184 mW of 21.36 W radiated) | rw, f, l | sinusoidal current | calc | p.339-341 Ex.7.3 | high |
| PAUL-1172 | antenna | Two-element array factor (equal amplitudes, phase delta, spacing d): emissions from multiple points add or cancel by path phase. | |E| proportional to |cos(pi*d*cos(phi)/lambda0 + delta/2)|; nulls where pi*d*cos(phi)/lambda0 + delta/2 = +/- pi/2; d = lambda/2 in-phase -> endfire nulls; d = lambda/2 anti-phase -> broadside nulls; d = lambda/4, 90 deg -> single null | d, delta, lambda0 | far field, parallel-ray approximation | calc | p.342-348 eq.(7.28)-(7.33) | high |
| PAUL-1173 | antenna | Directivity, gain, efficiency and isotropic reference. | U = r^2*Sav; D = 4*pi*U/Prad; G = e*D, e = Prad/Papp; isotropic: Sav = PT/(4*pi*d^2), |E| = sqrt(60*PT)/d; Sav = G*Papp/(4*pi*r^2) | PT, G, d | far field; eta0 = 120*pi | calc | p.349-351 eq.(7.34)-(7.48) | high |
| PAUL-1174 | antenna | Reference gains. | Hertzian dipole G = 1.5 (1.76 dB); half-wave dipole 1.64 (2.15 dBi); quarter-wave monopole 3.28 (5.17 dB); gain over half-wave dipole = 10log10(G/1.64) | antenna type | lossless | calc | p.352-353 Ex.7.7-7.8, eq.(7.49)-(7.51) | high |
| PAUL-1175 | antenna | Reciprocity: transmit and receive patterns are identical; the transmit input impedance equals the Thevenin impedance of the receiving antenna. | Z_rx,Thevenin = Z_in,tx | - | linear, same terminations | review | p.354 §7.4.1 | high |
| PAUL-1176 | antenna | Effective aperture and gain. | Ae = PR/Sav; Aem = lambda0^2*G/(4*pi); half-wave dipole @150 MHz: 0.522 m^2; Hertzian: Aem = 1.5*lambda0^2/(4*pi) | G, lambda0 | matched load and polarization | calc | p.354-356 eq.(7.52)-(7.59), RevEx.7.4 | high |
| PAUL-1177 | test | Antenna factor converts analyzer voltage to incident field; add cable loss (AF is referenced to the antenna terminals). | AF = |E_inc|/|V_rec| (1/m); E(dBuV/m) = AF(dB) + V_SA(dBuV) + cable_loss(dB); he = 1/AF | AF(f), V_SA, cable loss | valid only with the calibration termination (normally 50 ohm) and matched polarization; e.g. 60 dBuV/m, 30 ft RG58U (1.35 dB @100 MHz), 40 dBuV reading -> AF = 18.65 dB | calc | p.356-359 eq.(7.60)-(7.62), Ex.7.10 | high |
| PAUL-1178 | test | Measurement antennas must be balanced: CM current on the outside of a coax feed distorts the pattern and can make a failing product appear compliant. Use baluns: bazooka (quarter-wave sleeve, narrowband) or ferrite sleeves/toroid (wideband, ~3:1). | ferrite balun bandwidth ~3:1 | feed | swept measurements need broadband baluns | inspect | p.359-362 §7.4.4, Figs.7.19-7.20 | high |
| PAUL-1179 | test | Resistive matching pad keeps the cable matched (antenna sees 50 ohm) for any receiver load at the cost of insertion loss. | X = 10^(IL/20); R1 = R3 = RL*(1+X)/((RL/Zc)*X - 1); R2 = (R3 || RL)*(X - 1); IL = 20log10(1 + R2/(R3 || RL)); 50 ohm 6 dB Pi: R1 = R3 = 150.48, R2 = 37.35 ohm (Rin 29.92..83.55 ohm, VSWR <= 1.67); 50 ohm 20 dB: 61.11 / 247.50 ohm (VSWR 1.02); 75 ohm 10 dB: 144.37 / 106.73 ohm | IL, Zc, RL | acceptable VSWR usually < 1.2 | calc | p.362-365 eq.(7.63)-(7.65), RevEx.7.5 | high |
| PAUL-1180 | antenna | Friis transmission equation (antenna-to-antenna coupling, worst case if mismatched). | PR/PT = GT*GR*(lambda0/(4*pi*d))^2; dB: 10log10(PR/PT) = GT,dB + GR,dB - 20log10(f) - 20log10(d) + 147.56 (f Hz, d m); |E| = sqrt(60*PT*GT)/d | PT, GT, GR, f, d | far field (d > max(3*lambda0, 2D^2/lambda0)); matched load/polarization else upper bound; e.g. two half-wave dipoles, 150 MHz, 1000 m, 21.36 W: E = 45.85 mV/m, PR = 1.459 uW, -71.66 dB | calc | p.365-368 eq.(7.66)-(7.72), Ex.7.11 | high |
| PAUL-1181 | antenna | Method of images over a perfect ground plane: horizontal current image is reversed; vertical current image has the same direction; oblique currents decompose into components. | image at depth h below plane | geometry | infinite perfect conductor | calc | p.368-369 §7.6.1, Fig.7.23 | high |
| PAUL-1182 | shielding | Normal-incidence plane wave at a material boundary. | Gamma = (eta2 - eta1)/(eta2 + eta1); T = 2*eta2/(eta2 + eta1); 1 + Gamma = T; |Gamma| <= 1; eta = sqrt(j*w*mu/(sigma + j*w*eps)); perfect conductor: Gamma = -1 | eta1, eta2 | copper @1 MHz: eta = 3.69e-4 at 45 deg ohm, T = 1.96e-6 at 45 deg; 10 V/m on 2 m^2 dissipates 0.637 uW in one skin depth (66.1 um) | calc | p.368-376 eq.(7.73)-(7.80), Ex.7.12 | high |
| PAUL-1183 | antenna | Standing wave in front of a conductor: E is zero at multiples of lambda/2 from the surface and maximum (2Em) at lambda/4, 3lambda/4; H maxima at the conductor. | |E1| = 2*Em*|sin(2*pi*z/lambda)|; |H1| = (2*Em/eta1)*|cos(2*pi*z/lambda)| | z, lambda | normal incidence on perfect conductor | calc | p.372-374 eq.(7.81)-(7.83), Fig.7.25 | high |
| PAUL-1184 | test | Ground-plane (OATS/SAC) multipath: received field = direct wave x F; reflected path via image; both polarizations have Gamma = -1 over a perfect ground plane (vertical-case field vector sense per Fig.7.27b). | d = sqrt(D^2 + (hR - hT)^2); dr = sqrt(D^2 + (hR + hT)^2); F = 1 + (patterns)*Gamma*(d/dr)*exp(-j*beta0*(dr - d)); horizontal (omni): F_H = 1 - (d/dr)*exp(-j*2*pi*(dr - d)/lambda0); |F| <= 1 + d/dr (< 2, i.e. < 6 dB) | D, hT, hR, f | FCC B example: D = 3 m, hT = 1 m, hR = 1 m: d = 3, dr = sqrt13; hR = 4 m: d = sqrt18, dr = sqrt34; |F| bound derived (medium) | calc | p.376-380 eq.(7.84)-(7.89), Fig.7.28 | high |
| PAUL-1185 | emc | Differential-mode (loop) emission estimate for a pair of conductors of length L and spacing s carrying I_D: treat as a small loop of area A = L*s. | E_DM,max ~ 1.316e-14*f^2*I_D*L*s/d (V/m; f Hz, I_D A peak, L, s, d m) | f, I_D, L, s, d | electrically small loop, far field, free space, in-plane maximum; derived here from eq.(7.9a) — the printed Ch.8 model (§8.1.2) lies in the part-2 range | calc | p.331 eq.(7.9a) (derived) | medium |
| PAUL-1186 | emc | Common-mode emission estimate for an electrically short cable of length L whose two conductors each carry I_C (total 2*I_C): treat as a Hertzian dipole. | E_CM,max ~ mu0*f*(2*I_C)*L/(2d) = 1.257e-6*f*I_C*L/d (V/m) | f, I_C, L, d | L electrically short, uniform current, far field, free space, broadside; derived here from eq.(7.3c) — printed Ch.8 model (§8.1.3) in part-2 range | calc | p.328 eq.(7.3c) (derived) | medium |
| PAUL-1187 | emc | Common-mode currents dominate radiated emissions: microamperes of CM current radiate as much as tens of milliamperes of DM current; control CM (chokes, cable filtering, return-path design). | I_C/I_D (equal field) = 1.316e-14*f*s/1.257e-6 = 1.047e-8*f*s (derived from PAUL-1185/1186) | f, s | e.g. f = 100 MHz, s = 1.27 mm -> ratio 1.3e-3 | calc | p.261-262 §5.9 (statement); ratio derived | medium |
| PAUL-1188 | test | Over a ground plane the measured field can exceed the free-space value by the reflection factor |F| <= 1 + d/dr (< 6 dB); height scanning 1-4 m seeks the constructive maximum. | 20log10|F| <= 20log10(1 + d/dr) | geometry, f | perfect ground plane, far field | calc | p.376-380 eq.(7.88) (bound derived) | medium |

## 2. Formulas & tables (numbers)

### 2.1 Unit conversions (p.8 §1.1)
| quantity | value |
|---|---|
| 1 in. | 2.54 cm |
| 1 mil | 0.001 in. |
| 1 ft | 12 in. |
| 1 mile | 5280 ft |
| speed of light in free space v0 | 2.99792458e8 m/s (~3e8 m/s) |
| PCB land (FR-4) propagation velocity | ~1.8e8 m/s (p.10) |

### 2.2 Free-space wavelength (Table 1.1, p.13)
| f | 60 Hz | 3 kHz | 30 kHz | 300 kHz | 3 MHz | 30 MHz | 300 MHz | 3 GHz | 30 GHz | 300 GHz |
|---|---|---|---|---|---|---|---|---|---|---|
| lambda | 3107 mi (5000 km) | 100 km | 10 km | 1 km | 100 m | 10 m | 1 m | 10 cm | 1 cm | 1 mm |

### 2.3 Relative permittivity of dielectrics (Table 1.3, p.15)
| material | er | material | er |
|---|---|---|---|
| Styrofoam | 1.03 | Epoxy resin | 3.6 |
| Polyethylene foam | 1.6 | Quartz (fused) | 3.8 |
| Cellular polyethylene | 1.8 | Epoxy glass (PCB substrate) | 4.7 |
| Teflon | 2.1 | Bakelite | 4.9 |
| Polyethylene | 2.3 | Glass (pyrex) | 5.0 |
| Polystyrene | 2.5 | Mylar | 4.0 |
| Nylon | 3.5 | Porcelain | 6.0 |
| Silicon rubber | 3.1 | Neoprene | 6.7 |
| Polyvinyl chloride (PVC) | 3.5 | Polyurethane | 7.0 |
| | | Silicon | 12.0 |
Nonmagnetic dielectrics: ur = 1. Teflon v = 0.69 v0 (p.14).

### 2.4 Metals: conductivity relative to copper (sr) and relative permeability (ur) (Table 1.4, p.15)
| metal | sr | ur | metal | sr | ur |
|---|---|---|---|---|---|
| Silver | 1.05 | 1 | Steel (SAE 1045) | 0.10 | 1000 |
| Copper, annealed | 1.00 | 1 | Lead | 0.08 | 1 |
| Gold | 0.70 | 1 | Monel | 0.04 | 1 |
| Aluminum | 0.61 | 1 | Stainless steel (430) | 0.02 | 500 |
| Brass | 0.26 | 1 | Zinc | 0.32 | 1 |
| Nickel | 0.20 | 600 | Iron | 0.17 | 1000 |
| Bronze | 0.18 | 1 | Beryllium | 0.10 | 1 |
| Tin | 0.15 | 1 | Mumetal (at 1 kHz) | 0.03 | 30,000 |
| | | | Permalloy (at 1 kHz) | 0.03 | 80,000 |
Sheet steel: ur = 2000, er = 1.0 (p.14). Copper sigma_Cu = 5.8e7 S/m (p.202 §4.5.4).

### 2.5 Ratio to dB (Table 1.5, p.22)
| ratio | 1e6 | 1e5 | 1e4 | 1e3 | 1e2 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0.1 | 0.01 | 0.001 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V or I (dB) | 120 | 100 | 80 | 60 | 40 | 20 | 19.08 | 18.06 | 16.9 | 15.56 | 13.98 | 12.04 | 9.54 | 6.02 | 0 | -20 | -40 | -60 |
| P (dB) | 60 | 50 | 40 | 30 | 20 | 10 | 9.54 | 9.03 | 8.45 | 7.78 | 6.99 | 6.02 | 4.77 | 3.01 | 0 | -10 | -20 | -30 |
Quick-estimate rule: x2 = 6 dB (V) / 3 dB (P); x3 = 10 dB (V) / 5 dB (P).

### 2.6 FCC / CISPR 32 conducted-emission limits, 150 kHz-30 MHz, 50 ohm LISN (Tables 2.1-2.2, p.38; current equivalents Prob.2.1.3-2.1.4, p.66)
| class | f (MHz) | QP uV | AV uV | QP dBuV | AV dBuV | QP dBuA | AV dBuA | QP uA | AV uA |
|---|---|---|---|---|---|---|---|---|---|
| B | 0.15 | 1995 | 631 | 66 | 56 | 32 | 22 | 39.9 | 12.6 |
| B | 0.5 | 631 | 199.5 | 56 | 46 | 22 | 12 | 12.6 | 4 |
| B | 0.5-5 | 631 | 199.5 | 56 | 46 | 22 | 12 | 12.6 | 4 |
| B | 5-30 | 1000 | 316 | 60 | 50 | 26 | 16 | 20 | 6.3 |
| A | 0.15-0.5 | 8912.5 | 1995 | 79 | 66 | 45 | 32 | 178.25 | 39.9 |
| A | 0.5-30 | 4467 | 1000 | 73 | 60 | 39 | 26 | 89 | 20 |
Class B between 0.15 and 0.5 MHz the limit falls from 66 to 56 dBuV QP (56 to 46 AV) per graph Fig. 2.1 (standard convention: linear in log f — not stated in text; conf medium).

### 2.7 FCC radiated-emission limits (Tables 2.4-2.5, p.40; >1 GHz values p.38)
| f (MHz) | Class B @3 m uV/m | Class B dBuV/m | Class A @10 m uV/m | Class A dBuV/m |
|---|---|---|---|---|
| 30-88 | 100 | 40 | 90 | 39 |
| 88-216 | 150 | 43.5 | 150 | 43.5 |
| 216-960 | 200 | 46 | 210 | 46.4 |
| >960 | 500 | 54 | 300 | 49.5 |
| >1 GHz (AV) | 500 | 54 | 300 | 49.5 |
| >1 GHz (peak) | - | 74 | - | 69.5 |
QP detector below 1 GHz. FCC Class B scaled to 5 m (Prob.2.1.5): 35.56 / 39 / 41.56 / 49.56 dBuV/m. FCC Class A scaled to 5 m (Prob.2.1.6): 45 / 49.5 / 52 / 55.5 dBuV/m.

### 2.8 FCC upper measurement frequency (Table 2.3, p.40)
| highest frequency generated/used (MHz) | upper frequency of measurement (MHz) |
|---|---|
| < 1.705 | 30 |
| 1.705-108 | 1000 |
| 108-500 | 2000 |
| 500-1000 | 5000 |
| > 1000 | 5th harmonic of highest frequency or 40 GHz, whichever is lower |

### 2.9 CISPR 32 radiated-emission limits, 10 m, OATS/SAC, QP (Tables 2.6-2.7, p.42)
| f (MHz) | Class B uV/m | Class B dBuV/m | Class A uV/m | Class A dBuV/m |
|---|---|---|---|---|
| 30-230 | 31.6 | 30 | 100 | 40 |
| 230-1000 | 70.8 | 37 | 224 | 47 |

### 2.10 MIL-STD-461G RS103 radiated-susceptibility levels, V/m (Table 2.10, p.47)
Columns: AcExt = Aircraft (external or safety-critical); AcInt = Aircraft internal; ShipAbv = all ships above decks and submarines external; ShipMetBlw = ships (metallic) below decks; ShipNonMetBlw = ships (nonmetallic) below decks; SubInt = submarines internal; Gnd = ground; Spc = space. A = Army, N = Navy, AF = Air Force.
| band | svc | AcExt | AcInt | ShipAbv | ShipMetBlw | ShipNonMetBlw | SubInt | Gnd | Spc |
|---|---|---|---|---|---|---|---|---|---|
| 2-30 MHz | A | 200 | 200 | 200 | 10 | 50 | 5 | 50 | 20 |
| 2-30 MHz | N | 200 | 200 | 200 | 10 | 50 | 5 | 10 | 20 |
| 2-30 MHz | AF | 200 | 20 | - | - | - | - | 10 | 20 |
| 30 MHz-1 GHz | A | 200 | 200 | 200 | 10 | 10 | 10 | 50 | 20 |
| 30 MHz-1 GHz | N | 200 | 200 | 200 | 10 | 10 | 10 | 10 | 20 |
| 30 MHz-1 GHz | AF | 200 | 20 | - | - | - | - | 10 | 20 |
| 1-18 GHz | A | 200 | 200 | 200 | 10 | 10 | 10 | 50 | 20 |
| 1-18 GHz | N | 200 | 200 | 200 | 10 | 10 | 10 | 50 | 20 |
| 1-18 GHz | AF | 200 | 60 | - | - | - | - | 50 | 20 |
| 18-40 GHz | A | 200 | 200 | 200 | 10 | 10 | 10 | 50 | 20 |
| 18-40 GHz | N | 200 | 60 | 200 | 10 | 10 | 10 | 50 | 20 |
| 18-40 GHz | AF | 200 | 60 | - | - | - | - | 50 | 20 |
Equipment external to a submarine pressure hull but within the superstructure: use Ships (metallic) below decks. (Column assignment of the flattened OCR block to SubInt/Gnd/Spc is by position; conf medium.)

### 2.11 MIL-STD-461G emission-limit anchors (figures not reproduced in text)
| item | value | source | conf |
|---|---|---|---|
| CE102 band | 10 kHz-10 MHz, power leads ac and dc, all applications | p.45, Fig.2.5 | high |
| CE102 vs FCC/CISPR Class A QP (115-V equipment) | 3 dB more stringent at 150 kHz, 13 dB at 500 kHz (=> ~60 dBuV at 500 kHz) | Prob.2.1.14 answer | medium |
| RE102 band | 10 kHz-18 GHz; separate aircraft/space (Fig.2.6a) and ground (Fig.2.6b) limits; 1 m | p.45, Fig.2.6 | high |
| RE102 ground (USAF) vs FCC Class A (unscaled) | 15 dB more restrictive at 30 MHz, 5.5 dB at 1 GHz (=> ~24 dBuV/m @30 MHz, ~44 dBuV/m @1 GHz); peak vs QP detectors so not strictly comparable | Prob.2.1.15 answer | medium |

### 2.12 MIL-STD-461G requirement list (Table 2.8, p.45)
CE101 CE audio-frequency currents, power leads; CE102 CE RF potentials, power leads; CE106 CE antenna port; CS101 CS power leads; CS103 CS antenna port intermodulation; CS104 CS antenna port rejection of undesired signals; CS105 CS antenna port cross-modulation; CS109 CS structure current; CS114 CS bulk cable injection; CS115 CS bulk cable injection impulse excitation; CS116 CS damped sinusoidal transients, cables and power leads; CS117 CS lightning induced transients; CS118 CS personnel-borne ESD; RE101 RE magnetic field; RE102 RE electric field; RE103 RE antenna spurious and harmonic outputs; RS101 RS magnetic field; RS103 RS electric field; RS105 RS transient electromagnetic field.

### 2.13 Trapezoidal-spectrum formulas (Ch.3, p.95-108)
```
Pulse: amplitude A, period T (f0 = 1/T), width tau (50% points), rise tr = fall tf (0-100%), D = tau/T
Exact one-sided:  |c_n+| = 2 A D |sin(n pi D)/(n pi D)| |sin(n pi tr f0)/(n pi tr f0)|   (n >= 1)
                  c0 = A D ;  angle c_n = -n pi (tau + tr)/T (+/- 180 deg sign flips)
Bound breakpoints: f1 = 1/(pi tau) = f0/(pi D) ;  f2 = 1/(pi tr)
Bound level (dB):  L = 20log10(2 A D)                                   f <= f1
                   L = 20log10(2 A D) - 20log10(f/f1)                    f1 < f <= f2
                   L = 20log10(2 A D) - 20log10(f2/f1) - 40log10(f/f2)   f > f2
Log-log interpolation: log10(Y2) = log10(Y1) + (M/20) log10(f2/f1), M in dB/decade (eq.3.52)
Bandwidth guide: BW = 1/tr (alt 0.5/tr); true-spectrum first null at 1/tr (second sinc)
```

### 2.14 Worked spectral anchors (verification data)
| waveform | f | bound (dBuV) | exact (dBuV) | measured (dBuV, RMS) | source |
|---|---|---|---|---|---|
| 1 V, 10 MHz, 50%, tr = 20 ns (f1 = 6.37 MHz, f2 = 15.9 MHz) | 110 MHz ("11th harmonic (98 MHz)" in text) | 78.45 | 73.8 (70.8 RMS) | 68.0 | p.101-103 Ex.3.5 |
| 1 V, 10 MHz, 50%, tr = 5 ns (f2 = 63.66 MHz) | 110 MHz | 90.5 | 90.4 (87.4 RMS) | 86.1 | p.103 Ex.3.5 |
| 1 V, 1 MHz, 50%, tr = 20 ns (f1 = 637 kHz) | 110 MHz | 58.4 | - | - | p.104 |
| 5 V, 100 MHz, 50%, tr = 1 ns | 15th harmonic | 93.07 (interp.) | 93.07 | - | RevEx.3.2 p.105 |
| 5 V, 100 MHz, 50%, tr = 1 ns | c0 = 2.5 V; c1+ = 3.131; c3+ = 0.9108; c5+ = 0.4053; c7+ = 0.1673; c9+ = 0.03865 V | - | - | - | p.107 |
| 5 V, 100 MHz, 50%, tr = 1 ns | c0 = 112.16 dBuV (other harmonics printed garbled: c3+ = 119.19 dBuV) | - | - | - | RevEx.3.1 p.96 |
| 1 V, 1 MHz, 50%, tr = 12.5 ns (10 ns 10-90%) | nulls at 1/tau = 2 MHz and 1/tr = 80 MHz; 15th harmonic (15 MHz) | - | 92 | 87 (+3 dB = 90 peak) | p.113 Fig.3.28c |

### 2.15 Spectrum-analyzer minimum 6 dB bandwidths (Tables 3.1-3.2, p.116)
| regulation | radiated 30 MHz-1 GHz | radiated > 1 GHz | conducted 150 kHz-30 MHz |
|---|---|---|---|
| FCC | 120 kHz | 1 MHz | 9 kHz |
| CISPR 32 | 120 kHz | - | 9 kHz |

### 2.16 Addition of two in-phase signals within the RBW (Table 3.3, p.117)
| level difference (dB) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 18.3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| increase over the larger (dB) | 6.02 | 5.53 | 5.08 | 4.65 | 4.25 | 3.88 | 3.53 | 3.21 | 2.91 | 2.64 | 2.39 | 1.0 |

### 2.17 Propagation delay by medium (p.135-136)
| medium | er (eff.) | v (m/s) | ns/m | ps/cm | ps/in | ns/ft |
|---|---|---|---|---|---|---|
| free space / air | 1 | 3e8 | 3.33 | 33.3 | 85 | 1 |
| Teflon coax | 2.1 | 2.07e8 | 4.8 | 48.3 | 122.7 | 1.47 |
| FR-4 stripline | 4.7 | ~1.38e8 | 7.2 | 72.3 | 183.6 | 2.2 |
| microstrip / 2-layer PCB (estimate er' = 2.85) | 2.85 | 1.777e8 | 5.6 | 56.3 | 143 | 1.7 |

### 2.18 Transmission-line parameter verification anchors (Review Exercises 4.1-4.8 and Problems 4.2.x answers)
| structure | dimensions | l | c | Zc | v (m/s) | source |
|---|---|---|---|---|---|---|
| two-wire ribbon, 28 AWG 7x36 | rw = 7.5 mil, s = 50 mil (s/rw 6.7) | 0.75 uH/m exact (0.759 approx) | 14.82 pF/m exact (14.64 approx) | 225 ohm | 3e8 | RevEx 4.1, 4.7 |
| wire over ground, 20 AWG solid | rw = 16 mil, h = 1 cm (2h/rw 49) | 0.779 uH/m | 14.26 pF/m | 234 ohm | 3e8 | RevEx 4.2, 4.7 |
| RG58U coax | rw = 16 mil, rs = 58 mil, er 2.3 | 0.2576 uH/m | 99.2 pF/m | 51 ohm | 1.98e8 (66%) | RevEx 4.3, 4.7 |
| stripline FR-4 | s = 20 mil, w = 5 mil, er 4.7 | 0.461 uH/m | 113.2 pF/m | 63.8 ohm | 1.38e8 | RevEx 4.4, 4.8 |
| microstrip FR-4 | h = 50 mil, w = 5 mil, er 4.7 (er' 3.034) | 0.877 uH/m | 38.46 pF/m | 151 ohm | 1.72e8 | RevEx 4.5, 4.8 |
| coplanar strips (PCB I) | s = w = 15 mil, h = 62 mil, er 4.7 | 0.804 uH/m | 38.53 pF/m | 144.45 ohm | 1.8e8 | RevEx 4.6, 4.8 |
| two bare 20 AWG wires | rw = 16 mil, s = 50 mil | 0.4065 uH/m exact (0.4558 approx) | 27.33 pF/m exact (24.38 approx) | 122 ohm | 3e8 | Prob 4.2.1, 4.2.7 |
| 12 AWG over ground | rw = 40 mil, h = 80 mil | 0.2634 uH/m exact (0.2773 approx) | 42.18 pF/m exact (40.07 approx) | 79 ohm | 3e8 | Prob 4.2.2, 4.2.8 |
| RG6U coax | rw = 20.15 mil, rs = 90 mil, foamed PE er 1.45 | 0.3 uH/m | 53.83 pF/m | 75 ohm | 2.5e8 (0.83) | Prob 4.2.3, 4.2.9 |
| stripline FR-4 | s = 10 mil, w = 5 mil | 0.334 uH/m | 156.4 pF/m | 46 ohm | 1.38e8 | Prob 4.2.4, 4.2.10 |
| microstrip FR-4 | h = 64 mil, w = 10 mil (er' 3.079) | 0.7873 uH/m | 43.46 pF/m | 135 ohm | 1.71e8 | Prob 4.2.5, 4.2.11 |
| coplanar FR-4 | w = 5, s = 5, h = 47 mil (er' 2.825) | 0.8038 uH/m | 39.06 pF/m | 143 ohm | 1.79e8 | Prob 4.2.6, 4.2.12 |
| PCB II (opposite sides) | w = 200 mil, h = 62 mil FR-4 | - | - | 41.05 ohm | - | p.155 |
| coplanar | w = 200 mil, s = 62 mil, h = 62 mil | - | - | 155.7 ohm | - | p.155 |

### 2.19 Reflection-sign table (Table 4.1, p.174)
| GammaS | GammaL | load-voltage waveform |
|---|---|---|
| - (RS < Zc) | + (RL > Zc) | rings (oscillates about final value) |
| + (RS > Zc) | - (RL < Zc) | rings |
| + (RS > Zc) | + (RL > Zc) | monotonic build-up |
| - (RS < Zc) | - (RL < Zc) | monotonic build-up |

### 2.20 Loss anchors, FR-4 stripline s = 20 mil, w = 5 mil (p.206-210)
| quantity | value |
|---|---|
| g | 14.2e-12*f S/m (tan delta 0.02) |
| r (f > 23 MHz) | 8.05e-4*sqrt(f) ohm/m |
| r < wl above | 1.34 MHz |
| low-loss region (Zc, v ~ lossless) | above ~5 MHz |
| alpha @100 MHz | 1.085e-1 Np/m |
| @1 GHz: r / g / alpha | 25.46 ohm/m / 1.423e-2 S/m / 0.653 Np/m |
| @1 GHz: conductor / dielectric loss | 1.73 dB/m / 3.94 dB/m (6 in total 0.86 dB) |

### 2.21 AWG wire diameters, mils (Table 5.2, p.224) — solid; stranded (strands x gauge)
| AWG | solid | stranded options |
|---|---|---|
| 4/0 | 460.1 | 522.0 (427x23); 522.0 (259x21) |
| 3/0 | 409.6 | 464.0 (427x24); 464.0 (259x23) |
| 2/0 | 364.8 | 414.0 (259x23); 414.0 (133x20) |
| 1/0 | 324.9 | 368.0 (259x24); 368.0 (133x21) |
| 1 | 289.3 | 328.0 (2109x34); 328.0 (817x30) |
| 2 | 257.6 | 292.0 (2646x36); 292.0 (665x30) |
| 4 | 204.3 | 232.0 (1666x36) |
| 6 | 162.0 | 184.0 (1050x36); 184.0 (259x30) |
| 8 | 128.5 | 147.0 (655x36) |
| 10 | 101.9 | 116.0 (105x30); 115.0 (37x26) |
| 12 | 80.0 | 95.0 (165x34); 96.0 (7x20) |
| 14 | 64.1 | 73.0 (105x30); 73.0 (41x30); 73.0 (7x22) |
| 16 | 50.8 | 59.0 (105x36); 59.0 (26x30); 60.0 (7x24) |
| 18 | 40.3 | 47.0 (65x36); 49.0 (19x30); 47.0 (16x30); 48.0 (7x26) |
| 20 | 32.0 | 36.0 (41x36); 36.0 (26x34); 37.0 (19x32); 35.0 (10x30) |
| 22 | 25.3 | 30.0 (26x36); 31.0 (19x34); 30.0 (7x30) |
| 24 | 20.1 | 23.0 (41x40); 24.0 (19x36); 23.0 (10x34); 24.0 (7x32) |
| 26 | 15.9 | 19.0 (7x34); 20.0 (19x38); 21.0 (10x36) |
| 28 | 12.6 | 16.0 (19x40); 15.0 (7x36) |
| 30 | 10.0 | 12.0 (7x38) |
| 32 | 8.0 | 8.0 (7x40) |
| 34 | 6.3 | 7.5 (7x42) |
| 36 | 5.0 | 6.0 (7x44) |
| 38 | 4.0 | - |
Radius conversion: mils x 2.54e-5 = m (20 AWG solid rw = 16 mil = 0.4064 mm) (p.223).

### 2.22 Relative permittivity of wire-insulation dielectrics (Table 5.3, p.224)
| material | er | material | er |
|---|---|---|---|
| Air | 1.0005 | Epoxy resin | 3.6 |
| Styrofoam | 1.03 | Quartz (fused) | 3.8 |
| Polyethylene foam | 1.6 | Glass (pyrex) | 4.0 |
| Cellular polyethylene | 1.8 | Epoxy glass (PCB substrate) | 4.7 |
| Teflon | 2.1 | Bakelite | 4.9 |
| Polyethylene | 2.3 | Mylar | 5.0 |
| Polystyrene | 2.5 | Porcelain | 6.0 |
| Silicone rubber | 3.1 | Neoprene | 6.7 |
| Nylon | 3.5 | Polyurethane | 7.0 |
| PVC | 3.5 | Silicon | 12.0 |
Note: Table 1.3 (p.15) prints Glass (pyrex) 5.0 and Mylar 4.0 — the two tables disagree for these two entries (as printed).

### 2.23 Skin depth of copper (Table 5.4, p.226; sigma 5.8e7 S/m)
| f | 60 Hz | 1 kHz | 10 kHz | 100 kHz | 1 MHz | 10 MHz | 100 MHz | 1 GHz |
|---|---|---|---|---|---|---|---|---|
| delta | 8.5 mm | 2.09 mm | 0.66 mm | 0.21 mm | 2.6 mils | 0.82 mils | 0.26 mils | 0.0823 mils |
Steel SAE 1045 (Prob.5.1.2): 0.26 mils @1 MHz, 0.026 mils @100 MHz, 0.00823 mils @1 GHz.

### 2.24 Component parasitic anchors (Ch.5)
| item | value | source |
|---|---|---|
| 20 AWG lead pair, 0.5 in long, 0.25 in apart | L_loop ~ 14 nH; C ~ 0.128 pF | p.235 |
| resistor Cpar (lead + body leakage) | 1-2 pF typical | p.239 |
| 1 kohm 1/8 W carbon, 0.5 in leads (measured, 1-500 MHz) | f1 ~ 120 MHz; fit R 1.05 kohm, Cpar 1.2 pF, Llead 14 nH | p.243 Fig.5.12 |
| 470 pF ceramic, 1/2 in leads | SRF ~ 62 MHz (short leads: L ~ 4.775 nH, Prob.5.5.1) | p.245 Fig.5.16-5.17 |
| 0.1 uF with 14 nH | SRF 4.25 MHz | p.245 |
| 0.15 uF tantalum, 1/2 in leads | 10 ohm inductive at 100 MHz -> 15.9 nH | RevEx.5.4 |
| 100 pF vs 10,000 pF ceramic, 0.5 in leads, at 100 MHz | 8 ohm vs 12 ohm | p.250 |
| 10,000 pF ceramic, 20 AWG 0.5 in leads, 50 MHz | 4.08 ohm at +90 deg (inductive) | RevEx.5.5 |
| 1.2 uH inductor | SRF ~110 MHz, Cpar ~1.7 pF; ~30 ohm at 4 MHz | p.253 |
| 10 uH inductor | SRF ~40 MHz, Cpar ~1.6 pF | p.253 |
| 5-turn MnZn toroid | ~500 ohm @1 MHz, 380 ohm @60 MHz | p.258 |
| 5-turn NiZn toroid | ~80 ohm @1 MHz, 1200 ohm @60 MHz (fit L 8 uH, R 1200 ohm, Cpar 1.6 pF, Prob.5.7.1) | p.258 |
| ferrite bead | ~100 ohm above ~100 MHz; up to several hundred ohm | p.259 |
| CM impedance null, wires-to-frame | dc motor ~1 ohm @~100 MHz; stepper ~3 ohm @~70 MHz; solenoid ~8 ohm @~150 MHz | p.267-268 |

### 2.25 Wire/land resistance and inductance anchors (Ch.5 examples/problems)
| case | result | source |
|---|---|---|
| 20 AWG solid, 2 in, 200 MHz (delta 0.184 mil) | rhf 1.44 ohm/m = 36.7 mohm/in; R 73.4 mohm; li,hf 1.15 nH/m; Li 58.4 pH | Ex.5.1 p.227-229 |
| 20 AWG pair at 50 mil | li,dc 0.05 uH/m = 1.27 nH/in; le 0.456 uH/m = 11.58 nH/in | p.232 |
| 28 AWG solid pair, 5 in, 50 mil, 10 MHz | 0.209 ohm; Li 3.32 nH; Le 105 nH; C 1.7 pF | RevEx.5.2 |
| PCB I, 5 in, s = w = 15 mil, h = 62 mil, t = 1.38 mil, 100 MHz | 796 mohm, 102 nH, 4.89 pF | RevEx.5.3 |
| dc resistance #6 solid / 259x30; #20 solid / 19x32; #28 solid / 7x36; #30 solid / 7x38 | 1.3 / 1.31; 33.2 / 28; 214.3 / 194.4; 340.3 / 303.8 mohm/m | Prob.5.1.1 |
| 20 AWG solid at 100 MHz | 1.022 ohm/m; skin onset 105.8 kHz | Prob.5.1.3 |
| 32 AWG internal L | starts falling at 1.7 MHz; 6.5 nH/m at 100 MHz | Prob.5.1.4 |
| ribbon 2x 28 AWG (7x36), 2 m, 50 mil, 100 MHz | 3.74 ohm, 5.95 nH, 1.518 uH, 29.28 pF, Zc 227.7 ohm | Prob.5.1.5 |
| 6 in land, w = 5 mil | 0.59 ohm @1 MHz; 0.776 ohm @40 MHz | Prob.5.1.6 |
| microstrip h = 47 mil, w = 100 mil, 1 oz | er' 3.625, 45.3 ohm, 7.3 nH/in, 3.56 pF/in | Prob.5.2.1 |
| coplanar h = 47, w = 100, s = 100 mil | er' 1.96, 172.2 ohm, 20.4 nH/in, 0.688 pF/in | Prob.5.2.2 |
| opposite-side lands w = 100 mil, h = 47 mil | 56.48 ohm | Prob.5.2.3 |

### 2.26 Contact-arc parameters in air (p.271-276)
| parameter | value |
|---|---|
| minimum breakdown VB,min | ~320 V at d = 0.3 mil (0.00762 mm) |
| glow voltage VG | ~280 V (VG = 280 + 1000 d) |
| arc voltage VA | ~12 V (11-16 V, contact material) |
| glow sustaining current IG | ~1-100 mA |
| arc sustaining current IA | ~0.1-1 A (tens of mA to 1 A) |
| short-arc field EB | ~1e9 V/m (1e8 V/m used for design) |
| gas breakdown for d > dmin | VB,glow = 320 + 7e6 d |
| typical contact velocity | 0.01 m/s -> EB*v ~ 1 V/us (with EB = 1e8) |

### 2.27 LISN element impedances (Table 6.1, p.289; 60 Hz values p.290)
| element | 150 kHz | 30 MHz | 60 Hz |
|---|---|---|---|
| 50 uH | 47.1 ohm | 9424.8 ohm | 18.8 mohm |
| 0.1 uF | 10.61 ohm | 0.053 ohm | 26.5 kohm |
| 1 uF | 1.06 ohm | 0.0053 ohm | 2.7 kohm |
LISN one-side input impedance (Prob.6.1.1, SPICE): power-net short: 38.31 ohm @150 kHz, 47.62 ohm @30 MHz; power-net open: 37.85 / 47.62 ohm.

### 2.28 Power-line filter typical values and anchors (§6.2, p.298-309; Problems 6.2.x)
| element | typical value | note |
|---|---|---|
| line-to-line X-cap C_D | ~0.047 uF (0.1 uF in experiment) | DM; appears as 2*C_D to DM |
| line-to-ground Y-cap C_C | ~2200 pF (3300 pF in experiment) | CM; 2200 pF = 50 ohm at 1.45 MHz; leakage-current limited (150 uA -> 3316 pF) |
| green-wire inductor L_GW | 0.5-1 mH | 0.5 mH = 471 ohm @150 kHz; 1 mH + 10 pF -> SRF 1.6 MHz, 532 ohm @30 MHz |
| CM choke L (each winding) | ~10 mH (28 mH in experiment); L + M ~ 55 mH example | 10 mH: 18,850 ohm @150 kHz, 3.77 Mohm @30 MHz ideal; leakage L(1-k) |
| DM/CM insertion-loss example (Prob.6.2.1) | DM 41.7 dB @150 kHz, 179.75 dB @30 MHz; CM 49.2 / 166.18 dB | ideal SPICE, 50 ohm terminations |
| CM/DM impedance example (Prob.6.2.7: L_GW 1 mH, L 28 mH, k 0.98, C_C 3300 pF, C_D 0.1 uF) | Z_CM -24 dBohm @150 kHz, -210 dBohm @30 MHz; Z_DM -25.6 / -164 dBohm | - |

### 2.29 Elemental antenna and radiated-field formulas (Ch.7, p.325-338) — as printed plus evaluated constants
```
Free space: eta0 = 120*pi ~ 377 ohm; beta0 = 2*pi/lambda0; lambda0 = v0/f, v0 = 3e8 m/s
Hertzian dipole (dl, uniform I, peak):  E_theta = j*eta0*beta0*I*dl*sin(theta)*exp(-j*beta0*r)/(4*pi*r)
                                        = j*(f*mu0/2)*I*dl*sin(theta)*exp(-j*2*pi*r/lambda0)/r         (7.2a)
                                        |E| = 6.283e-7 * f * I * dl * sin(theta) / r   [constant = mu0/2]
   H_phi = E_theta/eta0; near/far crossover r = lambda0/(2*pi)
   Prad = 80*pi^2*(dl/lambda0)^2*|I|^2/2 ; Rrad = 80*pi^2*(dl/lambda0)^2                              (7.5-7.6)
Magnetic dipole (loop area A = pi*b^2, m = I*A):
   E_phi = eta0*beta0^2*m*sin(theta)*exp(-j*beta0*r)/(4*pi*r) = (pi^2*f^2*mu0*I*b^2/v0)*sin(theta)*exp(..)/r   (7.9a)
   |E| = 1.316e-14 * f^2 * I * A * sin(theta) / r   [constant = pi*mu0/v0 = 4*pi^2*1e-7/3e8]
   Rrad = 31,170*(A/lambda0^2)^2                                                                      (7.10)
Long dipole: E_theta = j*60*I_m*exp(-j*beta0*r)*F(theta)/r ; F = [cos(pi*l*cos(theta)/lambda0) - cos(pi*l/lambda0)]/sin(theta)
Half-wave dipole: F = cos((pi/2)cos(theta))/sin(theta); |E|max = 60*|I_m|/r; Rrad = 73 ohm; X = 42.5 ohm; G = 1.64
Quarter-wave monopole: Rrad = 36.5 ohm; X = 21.25 ohm; G = 3.28
Isotropic: Sav = PT/(4*pi*d^2); |E| = sqrt(60*PT)/d ; with gain: |E| = sqrt(60*PT*GT)/d
Effective aperture: Aem = lambda0^2*G/(4*pi); Friis: PR/PT = GT*GR*(lambda0/(4*pi*d))^2
   dB: 10log10(PR/PT) = GT,dB + GR,dB - 20log10 f(Hz) - 20log10 d(m) + 147.56
Antenna factor: E(dBuV/m) = V(dBuV) + AF(dB) + cable loss(dB)
Far-field criterion: d > max(3*lambda0 (wire antennas), 2*D^2/lambda0 (surface antennas))
```

### 2.30 Antenna reference values (Ch.7)
| antenna | G (abs) | G (dB) | Rrad | X_in | source |
|---|---|---|---|---|---|
| isotropic | 1 | 0 | - | - | p.351 |
| Hertzian dipole | 1.5 | 1.76 | 80*pi^2*(dl/lambda0)^2 (1 cm @300 MHz: 79 mohm) | - | p.329, 352 |
| small loop | - | - | 31,170*(A/lambda0^2)^2 (r = 1 cm @300 MHz: 3.08 mohm) | - | p.331 |
| half-wave dipole | 1.64 | 2.15 | 73 ohm | +42.5 ohm | p.337-338, 353 |
| quarter-wave monopole | 3.28 | 5.17 | 36.5 ohm | +21.25 ohm | p.338, 353 |
| lambda0/8 dipole (Fig.7.6) | - | - | ~1.5 ohm | ~-600 ohm | p.342 |
| half-wave dipole Aem @150 MHz | - | - | 0.522 m^2 | - | RevEx.7.4 |

### 2.31 Worked radiated-field anchors (Ch.7)
| case | result | source |
|---|---|---|
| 1 cm Hertzian dipole, 1 A, 100 MHz, 1000 m broadside | 6.28e-4 V/m; 1.67e-6 A/m | Ex.7.1 |
| 1 x 1 cm loop, 100 mA, 50 MHz, 3 m, in-plane | 109.6 uV/m = 40.8 dBuV/m (fails FCC B 40 dBuV/m) | Ex.7.2 |
| 1 cm dipole, 100 mA peak, 10 MHz | Prad 0.44 uW | RevEx.7.2 |
| half-wave dipole, 100 mA RMS, 100 MHz | Prad 0.73 W; 95.4 nW/m^2 at 1000 m | RevEx.7.3 |
| half-wave dipole, 100 V peak 50 ohm source, 150 MHz, 20 AWG | I = 0.765 A at -18.97 deg; Prad 21.36 W; Ploss 184 mW | Ex.7.3 |
| same source, lambda0/8 dipole | I = 0.166 A at 85.1 deg; Prad 20.7 mW; with 0.637 uH loading 2.81 W | p.342 |
| two half-wave dipoles, 150 MHz, 1000 m, 21.36 W | E 45.85 mV/m (45.90 from 60 I/r); Sav 2.794 uW/m^2; PR 1.459 uW (-28.36 dBm); PR/PT -71.66 dB | Ex.7.11 |
| antenna calibration: 60 dBuV/m incident, SA 40 dBuV, 30 ft RG58U @100 MHz (1.35 dB) | AF = 18.65 dB | Ex.7.10 |
| 10 V/m, 1 MHz plane wave on copper, 2 m^2, one skin depth (66.1 um) | 0.637 uW dissipated | Ex.7.12 |
| 100 V/m, 1 MHz on seawater (sigma 4 S/m), 10 m^2, one skin depth | 1.2 W | RevEx.7.6 |

### 2.32 Resistive pad values (p.363-365)
| pad | R1 = R3 (ohm) | R2 (ohm) | input R range (load open..short) | worst VSWR |
|---|---|---|---|---|
| 50 ohm, 6 dB (Pi) | 150.48 | 37.35 | 83.55 .. 29.92 | 1.67 (|Gamma| 0.25) |
| 50 ohm, 20 dB | 61.11 | 247.50 | 51.01 .. 49.01 | 1.02 |
| 75 ohm, 10 dB | 144.37 | 106.73 | - | - |

## 3. Mechanizable checks

`CHECK-electrically-small`: inputs (L_max m, f_max Hz, er, ur) -> lambda = 3e8/(f_max*sqrt(er*ur)); K = L_max/lambda -> pass if K < 0.1 (lumped model valid) -> margin = 0.1 - K (or 20log10(0.1/K) dB) -> PAUL-1001, PAUL-1005.

`CHECK-conducted-emission-limit`: inputs (f MHz, V_meas dBuV QP, V_meas dBuV AV, class A|B, market FCC|CISPR32) -> limit from Table 2.1/2.2 (Class B 0.15-0.5 MHz: interpolate 66->56 QP, 56->46 AV vs log10 f) -> pass if V_meas <= limit for QP and AV, both phase and neutral -> margin_dB = limit - V_meas -> PAUL-1019, PAUL-1020.

`CHECK-conducted-current-at-limit`: inputs (I_noise A per line, f) -> V_LISN_dBuV = 20log10(I*50/1e-6) -> compare as above -> margin -> PAUL-1034.

`CHECK-radiated-emission-limit`: inputs (f MHz, E_meas dBuV/m, d_meas m, class, market) -> limit L(f, class, market) at its standard distance d_std (FCC B 3 m, FCC A 10 m, CISPR 32 10 m); E_at_std = E_meas + 20log10(d_meas/d_std) -> pass if E_at_std <= L -> margin = L - E_at_std; flag "near-field extrapolation" if min(d_meas,d_std) < 3*lambda -> PAUL-1022..1026.

`CHECK-emission-scan-range`: inputs (f_highest MHz) -> f_upper from Table 2.3 -> pass if test plan upper frequency >= f_upper -> PAUL-1021.

`CHECK-smps-harmonics-below-band`: inputs (f_sw Hz, n_exempt) -> pass if n_exempt*f_sw < 150e3 -> margin = 150e3 - n*f_sw -> PAUL-1036.

`CHECK-dBm-to-dBuV-50ohm`: inputs (P dBm) -> V dBuV = P + 107 -> used by other checks -> PAUL-1011.

`CHECK-trapezoid-harmonic-envelope`: inputs (net, A V, f0 Hz, D, tr s (0-100%; if only 10-90% given, tr = t10_90/0.8), f Hz) -> f1 = f0/(pi*D), f2 = 1/(pi*tr); L_dBuV = 120 + 20log10(2*A*D) - (f>f1)*20log10(min(f,f2)/f1) - (f>f2)*40log10(f/f2) -> output envelope level (peak); subtract 3.01 dB for RMS comparison with SA readings -> used as source term for radiation checks -> PAUL-1044, PAUL-1046, PAUL-1055.

`CHECK-trapezoid-harmonic-exact`: inputs (A, f0, D, tr, n) -> c_n+ = 2*A*D*|sinc(n*D)|*|sinc(n*tr*f0)| (sinc(x)=sin(pi x)/(pi x)) -> dBuV = 20log10(c_n+/1e-6) -> compare to envelope (exact <= bound) -> PAUL-1044.

`CHECK-edge-rate-bandwidth`: inputs (tr s, f_required Hz) -> BW = 1/tr -> flag if interconnect/filter/probe bandwidth < BW (signal-integrity) or if BW > regulatory upper frequency of concern (EMC) -> PAUL-1051.

`CHECK-clock-harmonic-collision`: inputs (list of clock frequencies f_i Hz, band [30 MHz, f_upper], RBW = 120 kHz) -> for each pair (i,j) and harmonics n*f_i, m*f_j in band: flag if |n*f_i - m*f_j| < RBW -> worst-case increase = 20log10(1 + 10^(-Delta/20)) dB with Delta = level difference -> pass if no collisions or increase keeps margin >= 0 -> PAUL-1057, PAUL-1058.

`CHECK-even-harmonic-sensitivity`: inputs (D nominal, D tolerance) -> ratio of 2nd-harmonic magnitude at D_min/D_max vs D = 0.5 -> flag if emission margin at even harmonics < swing -> PAUL-1050.

`CHECK-line-needs-termination`: inputs (net, L in or m, er_eff or v, tr s) -> TD = L/v; pass (termination not required) if tr > 10*TD (strict) — quick form for FR-4 outer layers tr(ns) > L(in) -> margin = tr/(10*TD) (>1 good) -> if fail require series or parallel match -> PAUL-1084.

`CHECK-ringing-sign`: inputs (RS ohm driver, RL ohm (CMOS ~ open), Zc ohm) -> GammaS, GammaL -> flag "ringing" if GammaS*GammaL < 0 and line not "short" per CHECK-line-needs-termination; worst overshoot estimate V_L,max = Zc/(RS+Zc)*(1+GammaL)*V0 for step -> PAUL-1076..1078.

`CHECK-series-termination-value`: inputs (RS driver ohm, Zc ohm, R_series ohm) -> err = |RS + R_series - Zc|/Zc -> pass if err <= tolerance (design choice, e.g. 10%; book gives ideal equality) -> PAUL-1082.

`CHECK-parallel-termination-level`: inputs (RS, Zc, R, RL, V0, V_IH min) -> V_load = Zc/(RS+Zc)*V0 when R||RL = Zc -> pass if V_load >= V_IH; P_R = V_load^2/R in high state reported -> PAUL-1083.

`CHECK-cap-load-delay`: inputs (Zc, C_load) -> td = 0.693*Zc*C -> add to timing budget -> PAUL-1080.

`CHECK-discontinuity-reflection`: inputs (Zc of each segment in order) -> Gamma at each junction -> flag |Gamma| > threshold (design choice) and require both-end termination when any junction |Gamma| > 0 and load unmatched -> PAUL-1085, PAUL-1086.

`CHECK-trace-impedance`: inputs (geometry type {stripline, microstrip, coplanar, broadside}, w, h/s, t, er) -> Zc from PAUL-1070..1074 (microstrip: eq.4.41a, cross-check eq.4.41d when 0.1 <= t/w <= 0.8) -> pass if |Zc - Zc_target|/Zc_target <= tol -> PAUL-1070..1074.

`CHECK-line-loss`: inputs (geometry -> l, c, Zc; w, t; tan delta; L; f) -> r = max(rdc, rhf), g = 2*pi*f*c*tan delta, alpha = (r/Zc + g*Zc)/2, Loss_dB = 8.686*alpha*L -> pass if Loss_dB <= budget at f = 1/tr (or Nyquist) -> PAUL-1090..1095.

`CHECK-skin-depth`: inputs (f, sigma, conductor thickness t or radius rw) -> delta -> flag skin-effect regime when t > 2*delta (land) or rw >> delta (wire) -> PAUL-1090..1092.

`CHECK-cap-srf-vs-target`: inputs (refdes, C F, L_esl H (lead/pad/via loop; 14 nH for 0.5-in leads), ESR ohm, f_target Hz) -> f0 = 1/(2*pi*sqrt(L*C)); |Z(f)| = sqrt(ESR^2 + (2*pi*f*L - 1/(2*pi*f*C))^2) -> pass if f_target < f0 (capacitive) and |Z(f_target)| <= Z_required -> margin = f0/f_target -> PAUL-1110, PAUL-1112.

`CHECK-shunt-cap-diversion`: inputs (C, L_esl, ESR, Z_load(f) complex, f, required fraction x) -> I_C/I_noise = Z_load/(Z_cap + Z_load) -> pass if |ratio| >= x (e.g. 0.9) -> attenuation dB = 20log10|1/(1 - ratio)| of current reaching load -> PAUL-1113.

`CHECK-series-block-effectiveness`: inputs (Z_series(f) of inductor/bead/CM-choke leg, Z_loop(f) existing series impedance, required dB) -> IL = 20log10(|Z_loop + Z_series|/|Z_loop|) -> pass if IL >= required -> PAUL-1114, PAUL-1120.

`CHECK-inductor-srf`: inputs (L, Cpar, f_target) -> f0 = 1/(2*pi*sqrt(L*Cpar)) -> pass if f_target < f0 -> PAUL-1115.

`CHECK-ferrite-dc-bias`: inputs (bead/choke rated current I_sat or datasheet Z-vs-I curve, I_dc or I_60Hz through it, DM or CM path) -> fail if single-line bead carries I_dc > I_rated (CM choke with DM current exempt: flux cancels) -> PAUL-1117, PAUL-1120, PAUL-1122.

`CHECK-contact-protection`: inputs (Vdc V, RL ohm, L H, C F, IA_min A, v m/s (default 0.01), EB (default 1e8 V/m)) -> I0 = Vdc/RL; (a) I0/C < EB*v; (b) I0*sqrt(L/C) < 320 V; (c) Vdc/IA_min < R < RL for RC snubber; C >= max((I0/320)^2*L, I0*1e-6) -> pass if all -> PAUL-1129, PAUL-1130.

`CHECK-y-cap-leakage`: inputs (sum of line-to-ground C per line F, V_line RMS, f_line Hz, I_leak_max A) -> I_leak = 2*pi*f_line*V_line*C_Y -> pass if I_leak <= I_leak_max -> margin = I_leak_max/I_leak -> PAUL-1139.

`CHECK-y-cap-effective-band`: inputs (C_Y, band start 150 kHz) -> f_eff = 1/(2*pi*50*C_Y) -> report: Y-caps divert CM only above f_eff; if a CM failure lies below f_eff require L_GW or CM choke -> PAUL-1140, PAUL-1142.

`CHECK-cm-choke-leakage`: inputs (L H, k) -> L_CM = L*(1+k) (= L + M), L_DM = L*(1-k) -> report CM/DM impedances at 150 kHz and 30 MHz -> PAUL-1122, PAUL-1146.

`CHECK-conducted-mode-dominance`: inputs (V_P(f), V_N(f) complex or measured CM/DM separator outputs) -> V_C = (V_P + V_N)/2, V_D = (V_P - V_N)/2 -> label dominant mode per failing frequency -> recommend element class (X-cap/DM L vs Y-cap/CM choke/L_GW) -> PAUL-1144, PAUL-1145.

`CHECK-smps-edge-spectrum`: inputs (Vdc, fs, D, tr of switch node) -> bound per CHECK-trapezoid-harmonic-envelope in dBuV at conducted-band frequencies -> required filter attenuation = bound + coupling estimate - limit -> PAUL-1150, PAUL-1151.

`CHECK-loop-radiation-vs-limit`: inputs (net/loop id, loop area A m^2 (trace length x height/spacing to return), harmonic current I_n A peak at f_n (from CHECK-trapezoid-harmonic-envelope / load or line impedance), measurement distance d m (3 or 10), class/market) -> E = 1.316e-14*f_n^2*I_n*A/d (V/m, in-plane max, free space); E_dBuV/m = 20log10(E/1e-6); optional ground-plane allowance +20log10(1 + d/dr) (<= 6 dB) -> pass if E_dBuV/m - 3.01 (peak->RMS) <= limit(f_n) - design_margin -> margin_dB = limit - (E_dBuV/m - 3.01) -> valid only if loop circumference < lambda/10 and d in far field (d > 3*lambda) else flag "estimate only" -> PAUL-1165, PAUL-1166, PAUL-1185, PAUL-1022..1025, PAUL-1055, PAUL-1188. Verification: A = 1e-4 m^2, I = 0.1 A, f = 50 MHz, d = 3 m -> 109.6 uV/m (40.8 dBuV/m) (Ex.7.2).

`CHECK-dm-current-allowed-at-limit`: inputs (L m, s m, f Hz, limit E_lim V/m at distance d) -> I_D,max = E_lim*d/(1.316e-14*f^2*L*s) (peak; x sqrt2 if the limit is read as RMS) -> pass if design I_D(f) <= I_D,max -> margin_dB = 20log10(I_D,max/I_D) -> PAUL-1185.

`CHECK-cm-current-allowed-at-limit`: inputs (cable length L m (electrically short, L < lambda/10 advisable), f Hz, limit E_lim V/m at distance d, measured/estimated CM current I_C per conductor (current-probe reading = total 2*I_C)) -> I_C,max = E_lim*d/(1.257e-6*f*L) -> pass if I_C <= I_C,max -> margin_dB = 20log10(I_C,max/I_C) -> PAUL-1186, PAUL-1187. Worked (derived, medium): FCC Class B 100 uV/m at 3 m, f = 30 MHz, L = 1 m -> I_C,max ~ 8 uA.

`CHECK-far-field-validity`: inputs (f, d, D_max antenna/product dimension) -> lambda = 3e8/f; far if d > max(3*lambda, 2*D^2/lambda) -> if not, flag inverse-distance extrapolation and far-field formulas as approximate -> PAUL-1026, PAUL-1162, PAUL-1163.

`CHECK-antenna-factor-conversion`: inputs (V_SA dBuV, AF(f) dB, cable loss dB/100 ft (or dB), cable length, pad IL if any) -> E(dBuV/m) = V_SA + AF + cable_loss (+ pad IL) -> compare to limit -> PAUL-1177, PAUL-1014.

`CHECK-transmitter-field-at-product` (immunity planning): inputs (PT W, GT (abs), d m) -> E = sqrt(60*PT*GT)/d (V/m peak) -> pass if E <= product immunity level (e.g. RS103/IEC test level of the target market) -> PAUL-1173, PAUL-1180, PAUL-1030.

`CHECK-friis-coupling`: inputs (PT dBm, GT dBi, GR dBi, f Hz, d m) -> PR dBm = PT + GT + GR - 20log10 f - 20log10 d + 147.56 -> upper bound if mismatched; valid in far field -> PAUL-1180.

`CHECK-pad-design`: inputs (IL dB, Zc, RL) -> X = 10^(IL/20); R1 = R3 = RL(1+X)/((RL/Zc)X - 1); R2 = (R3||RL)(X-1) -> worst-case VSWR for RL in {0, inf} -> pass if VSWR <= 1.2 (book "acceptable") -> PAUL-1179.

## 4. Verification procedures & plots

### VP-1 Radiated-emission compliance scan (FCC/CISPR 32) (p.38-51, §2.1.1, §2.1.4.1)
- Setup: OATS or semianechoic chamber (absorber on walls/ceiling, reflective ground-plane floor); EUT 1 m above floor; antenna at 3 m (FCC B) or 10 m (FCC A, CISPR 32 A/B); biconical 30-200 MHz, log-periodic 200 MHz-1 GHz; height scan 1-4 m; horizontal and vertical polarization; QP detector (<1 GHz), AV and peak above 1 GHz (FCC).
- Plot: x = frequency (log, 30 MHz to Table 2.3 upper limit), y = E in dBuV/m; overlay limit line(s) of the target market(s) at the test distance (scale with 20log10(d1/d2) for other distances, far field only); separate traces for H and V.
- Pass: every QP point below limit in both polarizations; report margin = limit - measured (dB) per emission.
- Note: emission spectra show resonant "accentuated" regions from cable tuning rather than a smooth harmonic envelope (p.54, Fig. 2.12).

### VP-2 Conducted-emission compliance scan (p.37, 52-54, §2.1.4.2)
- Setup: 50 uH / 50 ohm LISN in series with ac cord; measure phase-to-green (V_P) and neutral-to-green (V_N) with 50 ohm receiver, other port in 50 ohm dummy load.
- Plot: x = frequency (log, 150 kHz-30 MHz), y = dBuV; QP and AV traces vs QP and AV limits (Table 2.1/2.2); both phase and neutral.
- Pass: both V_P and V_N under both QP and AV limits over the band. Current = V/50 ohm.
- Diagnostic: identify SMPS harmonics (e.g. 45/90/135 kHz peaks) and clock harmonics at the high end (p.54-55, Fig. 2.13).

### VP-3 MIL-STD-461G emissions (p.45-51, §2.1.3)
- CE102: LISN (MIL-STD-461G version, Fig. 2.11b) on power leads, 10 kHz-10 MHz, peak detector. RE102: 1 m, shielded absorber-lined room, antennas 104-cm rod (10 kHz-30 MHz), biconical (30-200 MHz), double-ridge horn (>200 MHz), fixed 120 cm height, H and V above 30 MHz, 10 kHz-18 GHz.

### VP-4 Clock/data spectral envelope plot (p.96-104, §3.2.2, Figs. 3.19-3.23)
- Plot: x = log frequency (f0 .. >= 1/tr, extend to regulatory upper frequency), y = dBuV (or dBuA for currents); overlay (a) exact discrete harmonics |c_n+| from eq.(3.48b), (b) three-segment bound (0 / -20 / -40 dB/decade, breakpoints 1/(pi*tau) and 1/(pi*tr)).
- Sweep/corners: tr min/max (driver datasheet, series-R options), duty-cycle tolerance (even harmonics), clock frequency options.
- Good: exact harmonics lie under the bound; bound at the frequencies of regulatory concern reduced by slowing tr (book example: 5 ns -> 20 ns at 110 MHz lowers bound 12 dB, measured 18 dB).
- Measurement correlation: spectrum analyzer displays RMS: expect measured ~= exact - 3 dB (within 1-2 dB in book's experiments).

### VP-5 Receiver/analyzer settings for pre-compliance (p.115-118, §3.3)
- RBW = regulatory minimum (120 kHz radiated 30 MHz-1 GHz, 1 MHz > 1 GHz FCC, 9 kHz conducted). Peak detector for fast screening; re-measure QP (and AV for conducted) at frequencies within a few dB of the limit.
- Harmonic-addition test: reduce RBW (e.g. 103 -> 30 kHz); unchanged display => no two harmonics adding.
- Average detector used to uncover narrowband harmonics under broadband (arcing) noise.

### VP-6 Signal-integrity transient simulation of a point-to-point net (p.170-180, §4.4, Fig. 4.23, 4.28)
- Model: Thevenin driver (RS 10-30 ohm CMOS, ramp tr), lossless TL (Zc, TD) (SPICE T element / Branin model, Fig. 4.20), load C 5-15 pF or open.
- Plot: y = V(L,t) and V(0,t) (V), x = time 0 .. >= 10 TD; overlay V_IH / V_IL thresholds and final value.
- Sweep: tr/TD in {1, 5, 10, 20}; termination {none, series R = Zc - RS, parallel R = Zc}; RS corners.
- Good: overshoot within logic/abs-max limits and no re-crossing of thresholds (book: 5.3 V at tr = 10 TD vs 7 V at tr = TD for 5 V).
### VP-7 Lattice/bounce diagram hand check (p.167, Fig. 4.19)
- Tabulate successive waves at z = 0 and z = L using GammaS, GammaL, T12/Gamma12 at discontinuities; totals must converge to dc steady state (RL/(RS+RL)*VS).
### VP-8 TDR measurement of a line (Prob.4.3.6, p.215)
- 50 ohm TDR source into line; round-trip time 2TD gives length L = v*t/2; reflected step gives GammaL -> RL = Zc(1+Gamma)/(1-Gamma).
### VP-9 Frequency-domain line loss (p.206-210, Figs. 4.41-4.42)
- Plot |Zc| and angle vs f (10 kHz-1 GHz), alpha(f), v(f); good: Zc and v flat (lossless values) above ~5 MHz; loss budget checked at 1/tr.

### VP-10 Component impedance characterization (§5, Figs. 5.12-5.31)
- Instrument: impedance analyzer / VNA, 1-500 MHz (book range), part mounted with the production lead length/pad geometry.
- Plot: |Z| (dBohm or ohm, log) and phase vs log f; overlay ideal R, 1/(wC), wL lines.
- Extract: SRF (phase crosses 0), ESL = |Z|/(2*pi*f) above SRF, Cpar from inductor SRF, ESR at SRF.
- Good: target noise band lies below capacitor SRF / below inductor SRF; bead/ferrite |Z| >> circuit impedance in band.
### VP-11 Power-line filter insertion loss (p.294-297, Fig. 6.8)
- DM test: phase vs neutral (green open), 50 ohm source/load; CM test: phase+neutral tied vs green, 50 ohm. Plot IL (dB) vs log f, 150 kHz-30 MHz (extend to 100+ MHz to see parasitic roll-back). Note: in-product IL differs because source impedance is unknown.
### VP-12 CM/DM diagnostic sequence (p.303-309, Figs. 6.13-6.20)
- Measure V_P, V_N with LISN; separate into V_C and V_D with balun combiner; overlay limit.
- At each failing frequency identify dominant mode; change only elements acting on that mode; re-measure; iterate (add Y-caps, X-caps, L_GW, CM choke one at a time).
### VP-13 Contact-arc / snubber verification (§5.13)
- Scope switch voltage at opening with inductive load; good: no showering-arc bursts, initial dv/dt < ~1 V/us, peak < 320 V; verify closure current < IA,min through snubber R.

### VP-14 Antenna-factor calibration and field computation (p.356-359, Ex.7.10)
- Known incident field (calibrated site, e.g. NIST) -> read SA voltage through 50 ohm cable; add cable loss to get antenna-terminal voltage; AF(dB) = E(dBuV/m) - V_terminal(dBuV). Plot AF (dB) vs log f over the antenna's band.
- In use: E = V_SA + AF + cable loss (+ pad loss). Termination must equal calibration termination (50 ohm); keep cable matched (pad if receiver not 50 ohm).
### VP-15 Radiated-emission prediction plot for a design (derived from Ch.3 + Ch.7)
- For each clock/data net: compute harmonic currents (trapezoid envelope / load impedance), loop area, CM current estimate; plot predicted E (dBuV/m, at 3 m and 10 m) vs log f with FCC/CISPR limit lines; mark estimate validity (far field, electrically small).
- Good: every predicted harmonic below limit by the project margin (book shows unmanaged boards miss by up to 30 dB, Fig.2.15).
### VP-16 Ground-plane (multipath) sensitivity (p.376-380, Fig.7.28)
- Plot |F| (dB) vs receive-antenna height 1-4 m at each frequency for H and V polarization (D = 3 m or 10 m, EUT at 1 m): shows why height scanning finds up to ~6 dB enhancement; use to interpret site-to-site differences.
### VP-17 Antenna-pattern / array check (p.342-348)
- For two coherent emitters (e.g. two cable exits, two clock loops) with spacing d and phase delta: plot array factor |cos(pi d cos(phi)/lambda + delta/2)| vs phi; identify directions of constructive addition (measurement turntable maximum).

## 5. Pitfalls, failure modes, review checklist

- [ ] Lumped-circuit (Kirchhoff/SPICE-lumped) model used only where largest dimension < 0.1 lambda at the highest frequency of interest (p.13).
- [ ] ac power cord treated as an RF antenna (typ. >= 1 m) — it carries high-frequency noise, not only 50/60 Hz (p.4).
- [ ] Signal-source meter reading (dBm) re-computed when the load is not 50 ohm (meter assumes matched 50 ohm) (p.27).
- [ ] Cable-loss-in-dB shortcut applied only with matched 50 ohm source/cable/load (p.29).
- [ ] FCC Class A vs B: if the product could plausibly be purchased for home use, test to Class B (Prob.2.1.2, p.66).
- [ ] Compliance of one sample is not enough — FCC random-samples production units; recalls are the real cost (p.37).
- [ ] Radiated test covers both antenna polarizations and 1-4 m height scan; product must pass both (p.38).
- [ ] Inverse-distance (20 dB/decade) extrapolation not trusted inside ~3 lambda (near field): 30 m at 30 MHz (p.39).
- [ ] FCC radiated scan extends to the Table 2.3 upper frequency (5th harmonic of highest clock up to 40 GHz above 1 GHz) (p.40).
- [ ] MIL-STD-461 (peak, 1 m) and FCC/CISPR (QP, 3/10 m) limits not compared without accounting for detector and distance (Prob.2.1.15, p.68).
- [ ] SMPS fundamental and low harmonics placed below 150 kHz where possible (45 kHz example) (p.55).
- [ ] Clock harmonics coupling onto the ac cord also drive radiated emissions above 30 MHz (p.55).
- [ ] Clock oscillator not adjacent to a cable connector (p.65).
- [ ] Optional EMC footprints (clock shunt-C pads, series-R/0 ohm) placed before layout freeze (p.65).
- [ ] Product enclosure shape reviewed by EMC engineer before it freezes PCB/cable-exit locations (p.66).
- [ ] Openings/cable penetrations assumed to defeat a metal enclosure's shielding (p.63).
- [ ] Rise/fall times quoted 10-90% converted to 0-100% (divide by 0.8) before using the book's spectral formulas (p.93).
- [ ] Averaged rise/fall (tr+tf)/2 used in the product-of-sinc formula only as an approximation (book: "not correct") (p.95).
- [ ] Emissions at even clock harmonics expected to vary day-to-day with duty-cycle drift (p.96).
- [ ] Computed peak harmonic levels reduced by 3.01 dB before comparing with spectrum-analyzer (RMS) readings (p.103).
- [ ] Multiple clocks with the same frequency, or harmonic coincidences within 120 kHz (e.g. 10 MHz x9 = 15 MHz x6 = 90 MHz), avoided (p.116).
- [ ] Ringing on clock lines damped (series R / ferrite / matching) — ringing produces narrowband "resonant" emission humps (p.109-111).
- [ ] Pre-compliance measured with RBW no wider than the regulatory minimum; a wider RBW sums neighbouring harmonics and over-reads (p.116).
- [ ] Interconnect delay included in timing budget (6-in stripline = 1.1 ns) (p.136).
- [ ] Wide-separation wire formulas (ln(s/rw)) not used below s/rw ~ 5 (use acosh) (p.146-147).
- [ ] Series-terminated nets with an impedance discontinuity (width change, via, connector) also need load termination to be reflection-free (p.188).
- [ ] No parallel termination placed at the midpoint/junction of a daisy chain (p.189).
- [ ] Star (parallel) fan-out from one driver avoided or each branch parallel-terminated (p.192).
- [ ] Parallel terminations checked for dc power and reduced high level Zc/(RS+Zc)*V0 (p.179).
- [ ] Loss tangent 0.02 for FR-4 applied only at high frequency (it -> 0 at dc) (p.206).
- [ ] Lumped-pi SPICE models of lines not trusted above the frequency where the line is ~0.1 lambda (p.211).
- [ ] Shunt capacitor SRF above the noise frequency (a "bigger" cap can make 100 MHz emissions worse: 10 nF 12 ohm vs 100 pF 8 ohm) (p.250).
- [ ] Shunt capacitors not used to divert noise in low-impedance circuits; series inductors/beads not used in high-impedance circuits (p.251, 253).
- [ ] Series inductors not placed on fast signal lines where they cause ringing (use on reset lines, green wire) (p.253).
- [ ] Ferrite material matched to band (MnZn conducted, NiZn radiated); cores catalogued/colour-coded (p.258).
- [ ] Single-line ferrite beads/inductors not saturated by dc/60 Hz load current (p.260, 309).
- [ ] CM choke input and output leads kept apart on the core (p.263).
- [ ] Motors/solenoids bonded to chassis for cooling have CM chokes or filtering on driver leads (p.266-268).
- [ ] Wire-wound resistors not used as SMPS current-sense resistors (p.238).
- [ ] EMC re-verified after any second-source/vendor change of fast logic parts (min rise time not guaranteed) (p.270).
- [ ] Free-wheeling/snubber diodes placed tight to the inductive load (p.278).
- [ ] Green-wire inductor made by winding the green wire on a toroid — never a soldered inductor in the safety path (p.292).
- [ ] Two-wire (no-ground) products still analysed for CM via stray capacitance (p.294).
- [ ] Filter vendor insertion-loss curves (50/50 ohm) not assumed to hold in product (p.296).
- [ ] Y-cap total within leakage-current limit (e.g. 150 uA -> 3316 pF at 120 V/60 Hz) (p.298).
- [ ] Green-wire inductor paired with LISN-side Y-caps (otherwise no effect) (p.301).
- [ ] Filter changes target the dominant mode at the failing frequency (p.304).
- [ ] Transformer Faraday shield tied to primary side (p.319).
- [ ] Power-line filter at the cord exit; supply adjacent to filter; no digital wiring near power wiring (p.310, 319).
- [ ] Far-field formulas and 1/r scaling applied only for d > max(3 lambda, 2D^2/lambda); FCC Class B at 3 m below ~100 MHz is near field (p.327, 366).
- [ ] PCB current loops sized: a 1 cm^2 loop with 100 mA at 50 MHz already fails Class B at 3 m (p.331).
- [ ] Antenna factor used with the same 50 ohm termination and polarization as calibrated; cable loss added (not subtracted) (p.358-359).
- [ ] Measurement antenna feed balanced (balun) — unbalanced feed can make a failing product look compliant (p.362).
- [ ] Receiver that is not 50 ohm padded so the cable stays matched (VSWR < 1.2) (p.362-364).
- [ ] Friis results treated as upper bound when load/polarization are not matched; only in far field (p.366).
- [ ] Ground-plane reflection (up to ~6 dB) considered when correlating free-space predictions with OATS/SAC data (p.376-380).
- [ ] Short (< lambda/2) antennas/cables: large capacitive reactance; do not assume resonant-dipole efficiency (p.338-342).

## 6. Standards referenced

| standard | edition/year | clause/table | governs | page |
|---|---|---|---|---|
| FCC 47 CFR Part 15, Subpart B (Unintentional Radiators) | 2022 (ref.) | Tables 2.1-2.5 of book | US conducted (150 kHz-30 MHz) and radiated (30 MHz-40 GHz) emission limits for digital devices, Class A/B | p.36-40 |
| CISPR 32 | ed. 2.1 consolidated, 2019 | Tables 2.1, 2.2, 2.6, 2.7 of book | Emission requirements for multimedia equipment (MME/ITE), Class A/B; conducted limits identical to FCC | p.40-44 |
| CISPR 22 | (superseded by CISPR 32) | Fig. 2.4, 2.12 labels | older ITE limit; same as CISPR 32 radiated limit shown | p.42, 54 |
| CISPR 16 | - | - | measurement apparatus/methods referenced by CISPR 32 | p.48 |
| European EMC Directive 2014/30/EU | Feb 26 2014, revised by Regulation (EU) 2018/1139 (July 4 2018) | - | EEA market access, CE mark, requires immunity tests | p.41 |
| IEC 61000-4-x / EN 61000-4-x | - | - | immunity: ESD, radiated field, EFT/burst, surge, power-frequency H, pulsed H, damped oscillatory H, dips/interruptions, harmonics/interharmonics, conducted CM 0 Hz-150 kHz, power quality | p.44 |
| MIL-STD-461G | Dec 11 2015 | Tables 2.8-2.10; CE102 Fig.2.5; RE102 Fig.2.6 | US DoD EMI control: CE/CS/RE/RS; peak detector, 1 m | p.44-49 |
| ANSI C63.4-2014 | 2014 | - | FCC measurement methods, 9 kHz-40 GHz | p.48 |
| RTCA DO-160G | 2010 | - | commercial airborne equipment environment incl. EMC, ESD, lightning | p.63 |
| CISPR 12 | 2021 | - | vehicles/boats/ICE: protection of off-board receivers | p.63 |
| CISPR 25 | - | - | vehicles/boats/ICE: protection of on-board receivers | p.63 |
| SAE J551 | 2012 (ref.) | - | whole-vehicle EMC testing | p.63 |
| SAE J1113 | 2012 (ref.) | - | vehicle component EMC testing | p.63 |
| German VDE (GOP) limits | older | Fig. 2.12 | historical radiated limits plotted with typical product data | p.54 |
| UL (Underwriters Laboratories) safety requirements | - | - | maximum 60 Hz leakage current through line-to-ground (Y) capacitors; X/Y capacitor safety approval | p.298 |
| NIST (formerly NBS), Boulder CO calibrated sites | - | - | source of known fields for antenna-factor calibration | p.357 |

## 7. Process / lifecycle guidance

| stage | activity | deliverable | exit criterion | source |
|---|---|---|---|---|
| Market/requirements | Identify every target market and its EMC regime (FCC Part 15 Class A/B, CISPR 32 + EU immunity (EN 61000-4-x), MIL-STD-461G with tailoring, RTCA DO-160G, CISPR 12/25, SAE J551/J1113); elect Class B if home use is plausible | Compliance matrix: limits, detectors, distances, frequency ranges (incl. FCC Table 2.3 upper frequency) | Every limit line and immunity level assigned to the product | p.35-44, 63; Prob.2.1.2 |
| Concept / architecture | Include an experienced EMC engineer from the start; review enclosure/package shape (fixes PCB placement, cable exits, internal cable routes) | EMC design review record | Enclosure, cable-exit and PCB-placement decisions reviewed for EMC before they freeze | p.64-66 §2.3-2.4 |
| Concept / architecture | Choose clock frequencies to avoid coincident harmonics (> RBW apart) and SMPS switching frequency so low harmonics fall below 150 kHz; prefer slow edges | Frequency plan | CHECK-clock-harmonic-collision and CHECK-smps-harmonics-below-band pass | p.55, 116 |
| Schematic | Provide optional suppression footprints (clock shunt-C pads, series-R/0-ohm, filter positions at connectors); power-line filter at cord entry | Schematic with DNP EMC options | Options exist on every clock and I/O net | p.65, 319 |
| Layout | Place oscillators away from connectors; minimize loop areas; filter and supply at power-cord exit; terminations per SI checks | Layout review vs Section 5 checklist | Section 5 items closed | p.65, 319-320 |
| Prototype | Test the first prototype, however crude, for radiated and conducted emissions; locate dominant source/radiator | Pre-compliance report | Trouble spots identified early | p.66 §2.4 |
| Debug / fix | Diagnose the dominant mechanism before changing parts (CM vs DM for conducted; dominant radiator for radiated); change only elements acting on the dominant component | Diagnostic log | Emissions below limit with margin; fix is manufacturable and low cost | p.64, 303-304 |
| Production | Verify EMC margin across part-to-part and vendor variation (min rise times); re-test on any vendor change; FCC samples production units | Production EMC audit / vendor-change re-test | Margin holds over sample; recall risk controlled | p.37, 270 |
| Design constraints | Balance suppression against product cost, marketability (appearance/usability), manufacturability (automated assembly of suppression parts) and development schedule | Trade record | Suppression parts auto-insertable; schedule held | p.63-64 §2.3 |

## 8. Coverage log

Line ranges read in order with the Read tool (offset/limit <= 900 lines per call):
- 1-1500: front matter, full table of contents (orientation for the whole book), preface, Ch.1 start.
- 1499-2712: Ch.1 (electrical dimensions, Tables 1.1-1.5, dB units, signal sources, problems skimmed).
- 2713-3369: Ch.2 (FCC/CISPR/MIL-STD-461G tables, measurement, LISN, typical emissions, design constraints; problems read for answer anchors).
- 3370-7001: Ch.3 (Fourier series, trapezoid spectra, bounds, bandwidth, duty cycle, ringing, spectrum analyzers, Fourier transform, random signals; problems skimmed).
- 7002-11138: Ch.4 (TL equations, per-unit-length parameters, time-domain solution, SI terminations, discontinuities, phasor solution, losses, lumped models; problems read for answer anchors).
- 11139-12986: Ch.5 (wires, lands, leads, R, C, L, ferromagnetics, beads, CM chokes, motors, digital devices, variability, switches; problems read for answer anchors).
- 12987-13690: Ch.6 (LISN, CM/DM, filters, CM/DM separation experiment, power supplies, transformers, placement, susceptibility; problems read for answer anchors).
- 13691-17000: Ch.7 §7.1 through §7.6.3 (p.325-380), stopping mid-way through the multipath vertical-polarization factor (end of assigned range).

Skipped or only skimmed: exercise/problem statements (answers used only as numeric verification anchors, labelled "Prob."/"RevEx."), long pure derivations (Fourier coefficient algebra §3.1.1-3.1.3, TL equation derivations §4.1, Branin model algebra §4.3.2, phasor derivations §4.5.1, plane-wave field algebra §7.6.2), historical remarks (Ch.1 introduction, Bell Labs 50 ohm anecdote), reference lists.

Extraction limitations:
- OCR replaced most Greek letters with "������" and scrambled many display equations; formulas were reconstructed from the surviving structure and verified against the book's own worked examples where possible (stripline 63.8 ohm, microstrip 151 ohm / er' 3.034, coplanar 144.45 ohm, broadside 41.05 ohm, pad resistor values, loop-field constant vs Ex.7.2, Pav of a trapezoid vs 11.667 W, Y-cap 3316 pF). Unverifiable reconstructions are marked medium/low.
- Figures are not in the text: FCC/CISPR limit plots (Figs.2.1-2.4), MIL-STD-461G CE102/RE102 limit curves (Figs.2.5-2.6), measured spectra and impedance plots. Where only a figure holds the value, the caption and prose anchors are given and marked "graph"/medium; CE102/RE102 numeric levels are available only as problem-answer anchors (Table 2.11).
- MIL-STD-461G Table 2.9 (requirement applicability matrix) is too scrambled in the OCR to reconstruct reliably and is omitted (only "CE102, RE102, CS101, CS114, RS103 apply to all" is stated in prose and captured). Table 2.10 (RS103) column assignment of the flattened Submarine/Ground/Space block is positional (medium).
- Table 1.3 and Table 5.3 disagree on Glass (pyrex) vs Mylar permittivity (5.0/4.0 vs 4.0/5.0); both recorded as printed.
- Review Exercise 3.1 harmonic answers are garbled; only c0 = 112.16 dBuV and c3+ = 119.19 dBuV were legible.
- Ex.3.5 text calls the evaluated frequency "98 MHz (11th harmonic)" while the computation uses 110 MHz; recorded as printed.
- Contact-arc formulas VB,glow = 320 + 7e6 d and VG = 280 + 1000 d print no length unit (SI metres inferred, flagged).
- DM/CM cable emission formulas (E_DM = 1.316e-14 f^2 I L s/d, E_CM = 1.257e-6 f I L/d) are printed in Ch.8 (part-2 range); here they are derived from Ch.7 elemental-antenna equations and marked medium (PAUL-1185/1186).

Counts: 188 design rules (PAUL-1001..PAUL-1188); 32 formula/table blocks; 40 mechanizable checks; 17 verification procedures; 57 pitfall/checklist items; 16 standards/authorities.

