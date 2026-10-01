# Introduction to Electromagnetic Compatibility (3rd ed.) — Anvil rulebook (Part 2: §7.6.3 end – Ch.11, Appendices A–E)

## 0. Citation

C. R. Paul, R. C. Scully, and M. A. Steffka, *Introduction to Electromagnetic Compatibility*, 3rd ed. Hoboken, NJ, USA: John Wiley & Sons, 2023 (copyright page: "This edition first published 2023 © 2023"; earlier editions 1992, 2006). Hardback ISBN 978-1-119-40434-7.

Chapters covered by THIS extraction (file lines 17000–34101): end of §7.6.3 and §7.7–7.8 (broadband measurement antennas, antenna modeling); Ch.8 Radiated Emissions and Susceptibility; Ch.9 Crosstalk; Ch.10 Shielding; Ch.11 System Design for EMC (grounding, PCB design, decoupling, system configuration, ESD, diagnostics, dominant effect); Appendix A (phasor method), Appendix B (EM field equations and waves), Appendix C (PUL-parameter codes), Appendix D (SPICE/LTSPICE, exact and lumped MTL models, Fourier analysis), Appendix E (history), index.

Chapters NOT read by this extraction: Ch.1 Introduction, Ch.2 EMC Requirements, Ch.3 Signal Spectra, Ch.4 Transmission Lines and Signal Integrity, Ch.5 Nonideal Behavior of Components, Ch.6 Conducted Emissions and Susceptibility, Ch.7 Antennas up to mid-§7.6.3 — assigned to the Part-1 agent (file lines 1–17000). Conducted-emission content in this file is limited to what Ch.11 restates (LISN 50 ohm legs, CM/DM dominant-effect filtering).

Rule ids PAUL-2001…PAUL-2204 (Part-2 block, four digits, to avoid collision with Part-1 ids). Page numbers are the printed book pages. Problem-set answers were not mined as rules except where they give clean numeric anchors (cited as "Prob.").

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| PAUL-2001 | emc | Radiated-emission measurement antenna selection by band for compliance testing | biconical 30–200 MHz; log-periodic 200 MHz–1 GHz; horn antennas > 1 GHz | f (MHz) | Regulatory radiated-emission (RE) testing, 30 MHz to >1 GHz | review | §7.7 p.381 | high |
| PAUL-2002 | antenna | A tuned half-wave dipole is impractical at the low end of the RE band: at 30 MHz it is lambda0/2 = 5 m (~15 ft) long, so it cannot be height-scanned 1–4 m in vertical polarization | L_dipole = lambda0/2 = 150/f_MHz (m) | f (MHz) | FCC-preferred tuned dipole vs broadband antennas | calc | §7.7 p.381 | high |
| PAUL-2003 | antenna | Infinite biconical antenna input impedance (purely resistive, = radiation resistance); choose cone half-angle to match feedline, use a balun at the input | Zin = Rrad = 120*ln(cot(theta_h/2)) (ohm); theta_h = cone half-angle; Zin = 50 ohm -> theta_h = 66.8 deg | theta_h (deg) | Infinite cones (truncated real cones add reactance/standing waves); discone Rrad = 1/2 of biconical | calc | §7.7.1 Eq.(7.94) p.383; Review Ex.7.7 p.384 | high |
| PAUL-2004 | antenna | Log-periodic dipole array bandwidth: highest frequency where shortest element = lambda/2, lowest frequency where longest element = lambda/2; element ratio constant tau = l_n/l_(n+1) = R_n/R_(n+1) | l_max = 150/f_low_MHz (m); l_min = 150/f_high_MHz (m); e.g. 500 MHz–10 GHz -> 30 cm and 1.5 cm; 200 MHz–1 GHz -> 75 cm and 15 cm | f_low, f_high (MHz) | Feed with crisscrossed (180 deg alternating) feed from the rear (coax through boom); parallel apex feed does not work well | calc | §7.7.2 Eq.(7.98) p.385–387; Review Ex.7.8; Prob.7.7.3 | high |
| PAUL-2005 | antenna | Log-periodic dipole array input impedance is roughly resistive and frequency-independent, 50–100 ohm; VSWR can be kept below 2.0 over 200 MHz–1 GHz | Zin = 50…100 ohm; VSWR < 2.0 | f | LPDA used for RE compliance 200 MHz–1 GHz | measure | §7.7.2 p.387 | high |
| PAUL-2006 | emc | Near/far-field status of the RE test: 30 MHz is one wavelength at 10 m, 1 GHz is one wavelength at 30 cm; the product is in the near field at the low end, so the inverse-distance (1/d) translation of limits between distances is valid only in the far field | lambda0 = 300/f_MHz (m); 1/d scaling only for d >> lambda0 | f, d | FCC: 3 m (Class B), 10 m (Class A); CISPR 22 (EN55022): 10 m for Class A and B | review | Ch.8 intro p.397 | high |
| PAUL-2007 | emc | Decompose two-conductor currents into differential-mode (functional) and common-mode (antenna-mode, undesired) parts before any emission estimate | I_D = (I1 − I2)/2; I_C = (I1 + I2)/2; I1 = I_C + I_D, I2 = I_C − I_D | I1, I2 (phasor A) | Any pair of wires/PCB lands; transmission-line models predict only I_D | calc | §8.1.1 Eq.(8.1),(8.2) p.398 | high |
| PAUL-2008 | emc | A tiny common-mode current radiates as much as a large differential-mode current: for a 1 m ribbon cable, 50 mil spacing, 30 MHz, d = 3 m, the FCC Class B limit (40 dBuV/m = 100 uV/m, 30–88 MHz) is reached by I_D = 20 mA but by only I_C = 8 uA (ratio 2500 ≈ 68 dB) — never dismiss CM current because it is small | I_D,limit = 19.95 mA; I_C,limit = 7.96 uA | L = 1 m, s = 1.27 mm, f = 30 MHz, d = 3 m | Far-field, electrically short line | calc | §8.1.1 p.399; Ex.8.1 p.403; Ex.8.2 p.408 | high |
| PAUL-2009 | emc | Hertzian-dipole field coefficient used for short current segments (constant current along the segment) | M = j*2*pi*1e-7*f*L; F(theta) = sin(theta); far field E_theta = M*I*e^(-j*beta0*r)/r * F(theta) | f (Hz), L (m) | Segment electrically short | calc | §8.1.1 Eq.(8.4),(8.5) p.401 | high |
| PAUL-2010 | emc | Half-wave-dipole field coefficient for resonant (lambda0/2) current segments with sinusoidal distribution | M = j60; F(theta) = cos((pi/2)*cos(theta))/sin(theta) | L = lambda0/2 | Resonant-length conductors | calc | §8.1.1 Eq.(8.6) p.401 | high |
| PAUL-2011 | emc | Maximum far-field emission of differential-mode current on a two-conductor line (in the plane of the wires, broadside) | abs(E_D,max) = 1.316e-14 * abs(I_D) * f^2 * L * s / d (V/m); I_D (A), f (Hz), L length (m), s separation (m), d distance (m) | I_D, f, L, s, d | L electrically short (constant current), s electrically small, d in far field; at d = 3 m, L somewhat < 1 m; 1 m cable ≈ lambda0/3 at 100 MHz; 30 cm land ≈ lambda0/10 at 100 MHz (OK below ~200 MHz) | calc | §8.1.2 Eq.(8.12) p.403 | high |
| PAUL-2012 | emc | DM radiation transfer function rises +40 dB/decade and scales with loop area A = L*s | abs(E_D,max/I_D) = K*f^2*A; K = 1.316e-14/d = 4.39e-15 at d = 3 m (FCC Class B) | f, A = L*s (m^2), d | Far field | calc | §8.1.2 Eq.(8.13) p.403 | high |
| PAUL-2013 | emc | DM radiated spectrum of a trapezoidal signal: +40 dB/dec up to 1/(pi*tau), +20 dB/dec up to 1/(pi*tr), flat above; therefore DM emission problems concentrate at the upper part of the RE band, typically above 200 MHz | breakpoints f1 = 1/(pi*tau), f2 = 1/(pi*tr); e.g. 100 MHz, 50 % duty, tr = 1 ns -> 63.7 MHz, 318.3 MHz | tau pulse width (s), tr rise time (s) | Trapezoidal clock/data driving a two-wire line | calc | §8.1.2 p.403; Fig.8.4 | high |
| PAUL-2014 | emc | DM emission is maximum in the plane of the wires and cancels at points equidistant from both wires, so DM emissions are sensitive to cable rotation | pattern max at phi = 0/180 deg (in-plane); null broadside to the plane | cable orientation | Two-wire line, far field | measure | §8.1.2 p.403–405; Fig.8.5 | high |
| PAUL-2015 | emc | To cut DM emission at a given frequency: (1) reduce current — slow rise/fall times and/or lower repetition rate to move 1/(pi*tau) and 1/(pi*tr) down; (2) reduce loop area early in design (more a PCB problem than a harness problem) | E_D ∝ I_D * f^2 * L * s | tr, f0, loop area | Design phase | review | §8.1.2 p.405 | high |
| PAUL-2016 | emc | Place the clock oscillator close to the ASIC/microprocessor it drives to avoid large clock-land loop areas created by routing-driven layout | minimize clock trace length and loop area | oscillator-to-load distance | PCB clock routing | inspect | §8.1.2 p.405; Fig.8.6a; §8.1.3 p.408 | high |
| PAUL-2017 | connectors | Assign connector/ribbon-cable pins so each signal is adjacent to its return; a phase loop spanning three wire separations radiates 3x (~10 dB) more DM emission than one spanning a single separation | E_D ∝ s; 3 separations -> 1 separation = −9.5 dB | pin map, pitch | Ribbon cables (e.g. stepper-motor phase wiring) | inspect | §8.1.2 p.405; Fig.8.6b,c | high |
| PAUL-2018 | emc | Maximum far-field emission of common-mode current on a two-conductor line (each wire carries I_C); pattern virtually omnidirectional about the cable | abs(E_C,max) = 1.257e-6 * abs(I_C) * f * L / d (V/m); with probe (net) current I_probe = 2*I_C: abs(E_C,max) = 6.283e-7 * abs(I_probe) * f * L / d | I_C or I_probe (A), f (Hz), L (m), d (m) | s electrically small (typical s <= lambda0/100: in-plane factor 0.9995 vs 1.000 perpendicular); far field; constant current | calc | §8.1.3 Eq.(8.16a,b) p.407 | high |
| PAUL-2019 | emc | CM radiation transfer function rises +20 dB/decade and scales with line length L (not loop area) | abs(E_C,max/I_C) = K*f*L; K = 1.257e-6/d = 4.19e-7 at d = 3 m | f, L, d | Far field | calc | §8.1.3 Eq.(8.17) p.408 | high |
| PAUL-2020 | emc | CM radiated spectrum of a trapezoidal signal: +20 dB/dec up to 1/(pi*tau), flat up to 1/(pi*tr), −20 dB/dec above; CM emission problems concentrate in the lower part of the RE band, typically below 300 MHz | same breakpoints as DM (63.7 MHz, 318.3 MHz for 100 MHz/50 %/1 ns) | tau, tr | Assumes CM waveform shape = DM waveform shape | calc | §8.1.3 p.408; Fig.8.8 | high |
| PAUL-2021 | emc | CM emission is essentially independent of cable rotation (omnidirectional); a rotation-insensitive emission points to CM, rotation-sensitive to DM | — | cable orientation vs emission | Diagnostic heuristic from the two models | measure | §8.1.3 p.408; §8.1.2 p.405 | medium |
| PAUL-2022 | cables | To cut CM emission: reduce CM current (slower edges, lower rep rate), shorten conductors (harnesses and long PCB lands), keep oscillator/crystal next to the module it feeds; where cable length is fixed by the system, block CM current with a ferrite toroid/CM choke | E_C ∝ I_C * f * L | L, I_C | Peripheral/harness cables | review | §8.1.3 p.408–410 | high |
| PAUL-2023 | test | Current-probe transfer impedance defines conversion from measured voltage to current; calibration valid only when terminated in the calibration load (usually 50 ohm) | Z_T = V/I (ohm); abs(Z_T)dBohm = abs(V)dBuV − abs(I)dBuA; typical probe ≈ 12 dBohm flat 10–100 MHz; probe in book's tests 15 dBohm 10–200 MHz | V_SA (dBuV), Z_T (dBohm) | Probe measures net (CM) current of all enclosed wires; DM fluxes cancel in the core | measure | §8.1.4 Eq.(8.19),(8.20) p.410–411 | high |
| PAUL-2024 | emc | Net common-mode current on a cable that just reaches a radiated limit (one lumped wire of length L) | abs(E_C)max = 6.28e-7 * abs(I_C,net) * f * L / d; FCC Class B, L = 1 m, 30 MHz, d = 3 m -> I_C,net = 15.92 uA = 24 dBuA; with Z_T = 15 dBohm -> V_SA = 39 dBuV (89 uV) | L, f, d, E_limit | Far field, cable electrically short | calc | §8.1.4 Eq.(8.21),(8.22) Ex.8.3 p.411–413 | high |
| PAUL-2025 | test | Bench current-probe screening limit for each peripheral cable (no chamber needed); scale for cable length by subtracting 20log10(L) | V_SA,max(dBuV) = E_limit(dBuV/m) + Z_T(dBohm) + 20log10(d) − 20log10(f_MHz) − 20log10(L) + 4.041 | E_limit, Z_T, d (m), f (MHz), L (m) | Probe usable only within its flat Z_T band (example probe ≈ up to 100 MHz); use before/after a fix (e.g. toroid) | calc | §8.1.4 Eq.(8.24) Ex.8.4 p.413–414; Fig.8.11 | high |
| PAUL-2026 | test | Convert probe reading to current including the probe-to-analyzer cable loss (add cable loss to the analyzer reading) | I_probe(dBuA) = V_SA(dBuV) + cable_loss(dB) − Z_T(dBohm) | V_SA, cable loss, Z_T | Measure cable loss at each frequency | calc | §8.1.5 Eq.(8.25) p.416 | high |
| PAUL-2027 | emc | Predicted CM field at 3 m for a 1 m cable from probe reading, including ground-plane reflection correction F_GP | E_C(dBuV/m) = V_SA(dBuV) + cable_loss(dB) − Z_T(dBohm) + 20log10(f_MHz) + abs(F_GP)dB − 13.58 | V_SA, Z_T, f, F_GP | L = 1 m, d = 3 m, semi-anechoic chamber (ground-plane correction per Table 7.1) | calc | §8.1.5 Eq.(8.26),(8.27) p.416 | high |
| PAUL-2028 | emc | The constant-current (electrically short) CM emission model remains usable up to about L = lambda0/3: measured CM current on a 1 m cable at 100 MHz varied only 34.0–45.1 dBuA along its length (max 45.1 dBuA = 180 uA at 40 cm) and predictions from probe current were within 3 dB (except 50, 80, 130 MHz) | L <= ~lambda0/3 for the lumped CM model | L, f | 1 m ribbon, 30–200 MHz, 3 m, semi-anechoic chamber | measure | §8.1.5 p.418; Table 8.1; Fig.8.15 | high |
| PAUL-2029 | test | Coax loss between current probe and analyzer must be added to the reading; RG55U ≈ 2.5 dB/100 ft at 100 MHz (40 ft ≈ 1 dB); ground-plane correction at 100 MHz (horizontal pol., 1 m height) = 0.78 dB, at 180 MHz = 4.4 dB | loss(dB) = 2.5 dB/100 ft × length(ft) at 100 MHz | cable length, f | Book's RE test geometry (antenna and cable 1 m above floor, 3 m apart) | calc | §8.1.5 Ex.8.5 p.418; Review Ex.8.1 | high |
| PAUL-2030 | emc | Diagnostic for dominant mechanism: remove the far-end load (DM current collapses) — if radiated emission is essentially unchanged, CM current is the dominant radiator | Δemission(load removed) ≈ 0 dB -> CM dominant | emission with/without load | Wires and PCB lands; DM not zero with open load (displacement current) | measure | §8.1.5 p.418–420; Figs.8.16, 8.20 | high |
| PAUL-2031 | emc | Diagnostic for dominant mechanism: rotate the board/cable so the conductor plane is perpendicular to the antenna direction (DM fields cancel) — if emission is unchanged, CM is dominant | Δemission(on edge) ≈ 0 dB -> CM dominant | emission vs orientation | Two parallel lands/wires | measure | §8.1.5 p.420 | high |
| PAUL-2032 | emc | A ferrite toroid (4 turns of the cable through a NiZn toroid) reduced cable CM radiated emission by over 20 dB at some frequencies; verify any CM fix by measuring CM current with a probe before and after | ΔE ≈ ΔI_C (dB); >20 dB observed | I_C before/after | 30–200 MHz, 1 m ribbon cable | measure | §8.1.5 p.418; Fig.8.17 | high |
| PAUL-2033 | emc | CM current can dominate even on short, compact, symmetric PCB lands with no mains connection: 6 in. lands (1 oz, 25 mil wide, 380 mil c-c, 62 mil FR4, Zc = 342 ohm, 330 ohm matched load, 10 MHz, tr ≈ 4 ns, tf ≈ 2 ns) — DM model predicted emissions ≈ 20 dB below measured; CM model from probe current matched | DM prediction − measured ≈ −20 dB | — | Do not assume CM ≈ 0 because the layout is small/symmetric | measure | §8.1.5 p.419–420; Figs.8.18–8.20 | high |
| PAUL-2034 | emc | Image (ground) plane placed beneath a PCB reduces radiated emissions from both DM and CM currents on PCB lands (image theory) | — | presence/height of image plane | Per German, Ott, Paul [19] | review | Prob.8.2.9 p.443; Ref.[19] | medium |
| PAUL-2035 | emc | Incident far field from a distant transmitter (Friis form) for susceptibility estimates | abs(E_i) = sqrt(60*P_T*G)/d (V/m); abs(H_i) = abs(E_i)/eta0, eta0 = 120*pi ≈ 377 ohm; e.g. half-wave dipole G = 1.64 (2.15 dB), 1 kW, 100 MHz, 3000 m -> E = 0.105 V/m, H = 0.277 mA/m | P_T (W), G (abs), d (m) | Far field of transmitter; uniform plane wave | calc | §8.2 Eq.(8.32) Ex.8.6 p.426 | high |
| PAUL-2036 | emc | Per-unit-length L and C of a two-wire line (wide separation) used in pickup/crosstalk models | l = (mu0/pi)*ln(s/rw) (H/m); c = pi*eps0*eps_r/ln(s/rw) (F/m); Zc = 120*ln(s/rw) (ohm, eps_r = 1); e.g. 28 AWG 7x36 (rw = 7.5 mil), s = 50 mil -> Zc = 228 ohm, c = 14.64 pF/m | s, rw (m), eps_r | s >> rw, homogeneous non-ferromagnetic medium | calc | §8.2 Eq.(8.28) p.424; Ex.8.7, 8.8 p.427–430 | high |
| PAUL-2037 | emc | Lumped plane-wave pickup sources for an electrically short two-conductor line: H normal to the loop induces a series voltage source; E transverse to the line induces a shunt current source | V_s = j*omega*mu0*H_ni*A; I_s = j*omega*c*E_ti*A; A = s*L (m^2) | f, H_ni (A/m), E_ti (V/m), s, L, c | L << lambda0, s electrically small | calc | §8.2 Eq.(8.35),(8.36) p.427 | high |
| PAUL-2038 | emc | Terminal voltages of an electrically short line illuminated by a plane wave (superposition of inductive and capacitive pickup) | V_S = RS/(RS+RL)*j*omega*mu0*L*s*H_ni − RS*RL/(RS+RL)*j*omega*c*L*s*E_ti; V_L = −RL/(RS+RL)*j*omega*mu0*L*s*H_ni − RS*RL/(RS+RL)*j*omega*c*L*s*E_ti (V); sign of V-source term follows H direction (Lenz) | RS, RL (ohm), L, s, c, H_ni, E_ti, f | Neglects line l, c: valid for electrically short lines and terminations not extreme (not near short/open) / not far from Zc; e.g. 1 m, 50 mil ribbon, 50/150 ohm, 10 V/m 100 MHz broadside -> V_S = j6.65 mV, V_L = −j19.95 mV; endfire -> V_S = −j11.03 mV, V_L = j15.57 mV | calc | §8.2 Eq.(8.37) p.427; Ex.8.7, 8.8 p.427–430 | high |
| PAUL-2039 | emc | Simple pickup model accuracy: within 1 dB up to ≈ 40 MHz for a 1.5 m, 300 ohm twin lead (lambda0/10 at 20 MHz); induced voltage rises 20 dB/decade until standing waves appear | V ∝ f (+20 dB/dec) while L << lambda0 | L, f | Terminations near Zc; beyond that use full transmission-line model | measure | §8.2.1 p.433–434; Fig.8.29 | high |
| PAUL-2040 | emc | Orient the line so no incident H component is normal to the loop and no incident E component is transverse to the line: then both induced sources vanish (propagation along the line with E perpendicular to the loop plane induces nothing) | H_ni = 0 and E_ti = 0 -> V_ind = I_ind = 0 | wave direction and polarization vs line | Plane-wave or ESD-table fields | review | §8.2 p.430; Fig.8.26 | high |
| PAUL-2041 | esd | ESD table-discharge fields: at the metal table surface E is perpendicular and H parallel to the table; a PCB mounted vertically puts its land pairs transverse to E (current-source pickup, lock-ups). Mount the PCB flat on the product bottom so E is perpendicular to the circuit loops and H is not normal to them | board plane parallel to table -> E_ti ≈ 0, H_ni ≈ 0 | board orientation | Product placed on metal ESD table, gun discharged to table (indirect discharge) | inspect | §8.2 Ex.8.9 p.431–432; Fig.8.27 | high |
| PAUL-2042 | esd | Late-program ESD fix: place a conductive metal plate parallel and very close behind a vertically mounted PCB; boundary conditions bend E normal to the plate, i.e. perpendicular to the PCB loops, nulling the induced current source | plate spacing << board dimensions | plate presence/spacing | When PCB cannot be relocated | inspect | §8.2 Ex.8.10 p.432; Fig.8.28 | high |
| PAUL-2043 | cables | Shielded-cable shield must be peripherally (360 deg) bonded to the enclosures at both ends through connectors; pigtails are breaks in the shield and should be avoided if full shielding effectiveness is to be realized | pigtail length = 0 (goal) | shield termination method | Coax/shielded cables | inspect | §8.2.2 p.435 | high |
| PAUL-2044 | cables | Solid-shield surface transfer impedance (diffusion) | Z_T = (1/(sigma*2*pi*r_sh*t_sh)) * gamma*t_sh/sinh(gamma*t_sh) (ohm/m); gamma = (1+j)/delta; delta = 1/sqrt(pi*f*mu0*sigma); dc value r_dc = 1/(sigma*2*pi*r_sh*t_sh) for t_sh << delta; abs(Z_T) falls below r_dc once t_sh > delta | sigma (S/m), r_sh inner radius (m), t_sh thickness (m), f | Shield without pigtails/breaks; graph Fig.8.31 (Z_T/r_dc vs t_sh/delta) | calc | §8.2.2 Eq.(8.39),(8.40) p.435–436; Fig.8.31 | high |
| PAUL-2045 | cables | Braided-shield surface transfer impedance = braid diffusion term + aperture (hole) mutual-inductance term | Z_T = r_dc * gamma*2*r_bw/sinh(gamma*2*r_bw) + j*omega*m12 (ohm/m); r_dc = r_b/(B*W*cos(theta_w)); r_b = 1/(sigma*pi*r_bw^2) for r_bw << delta; B = belts, W = wires/belt, theta_w = weave angle, r_bw = braid wire radius; e.g. B = 16, W = 4, r_bw = 2.5 mil, theta_w = 30 deg -> r_dc = 24.6 mohm (1 m), abs(Z_T(1 MHz)) = 19 mohm | B, W, theta_w, r_bw, sigma, m12, f | Surface transfer admittance Y_T (hole capacitance c12) negligible except for very large terminations | calc | §8.2.2 Eq.(8.41)–(8.43),(8.46),(8.47) p.436–438; Prob.8.2.8 | high |
| PAUL-2046 | cables | Voltages induced in the terminations of an electrically short shielded cable by exterior shield current | V_S = RS/(RS+RL)*Z_T*I_SH*L; V_L = −RL/(RS+RL)*Z_T*I_SH*L (V); e.g. 300/50 ohm, I_SH = 31.5 mA, 1 m, 1 MHz braid above -> 513 uV, 85.5 uV | Z_T (ohm/m), I_SH (A), L (m), RS, RL | Cable electrically short; I_SH computed assuming perfect shield | calc | §8.2.2 Eq.(8.45) p.438; Prob.8.2.8 | high |
| PAUL-2047 | crosstalk | Crosstalk needs >= 3 conductors (generator, receptor, reference); it is near-field (intrasystem) coupling. Internal crosstalk onto a peripheral cable or the power cord can cause radiated or conducted emission failures and can bring external disturbances inside | — | conductor topology | Wires in cables, lands on PCBs | review | Ch.9 intro p.445 | high |
| PAUL-2048 | transmission-line | Propagation velocity in a homogeneous medium; glass-epoxy PCB (stripline) eps_r ≈ 4.7 gives v = 1.38e8 m/s = 5.45 in/ns; microstrip and single-sided PCB (partly air) have two propagation velocities, neither equal to c | v = v0/sqrt(eps_r), v0 ≈ 3e8 m/s | eps_r | Homogeneous: stripline, bare wires, wires in a dielectric-filled shield | calc | §9.1 Eq.(9.1) p.447–448 | high |
| PAUL-2049 | transmission-line | Quasi-TEM assumption (per-unit-length L, C from static methods) is adequate for good conductors, typical cross sections and frequencies up to the lower GHz range; lossless-medium assumption usually reasonable below the low GHz range | f <~ low GHz | f | MTL crosstalk analysis | review | §9.2 p.450; §9.4.1.1 p.481 | high |
| PAUL-2050 | crosstalk | Three-conductor per-unit-length matrices: L = [[lG, lm],[lm, lR]]; C = [[cG+cm, −cm],[−cm, cR+cm]]. Homogeneous medium: L*C = mu*eps*I, so C = (1/v^2)*L^-1; inhomogeneous (PCB): L = mu0*eps0*C0^-1 with C0 = capacitance with dielectric removed | cm = lm/(v^2*(lG*lR − lm^2)); cG+cm = lR/(v^2*(lG*lR − lm^2)); cR+cm = lG/(v^2*(lG*lR − lm^2)) | lG, lR, lm, v | Lossless uniform line | calc | §9.2 Eq.(9.5) p.451; §9.3.1 Eq.(9.8)–(9.12) p.452–453 | high |
| PAUL-2051 | crosstalk | Three-wire (one wire as reference) wide-separation inductances | lG = (mu0/2pi)*ln(dG^2/(rwG*rw0)); lR = (mu0/2pi)*ln(dR^2/(rwR*rw0)); lm = (mu0/2pi)*ln(dG*dR/(dGR*rw0)) (H/m); dG, dR = distances from reference wire, dGR = generator–receptor distance, rw = radii | geometry (m) | Separation/radius >= ~5:1; bare wires (insulation does not change L) | calc | §9.3.2 Eq.(9.18)–(9.20) p.456–457 | high |
| PAUL-2052 | crosstalk | Ribbon cable with center wire as reference (28 AWG 7x36, rw = 7.5 mil, 50 mil pitch): lG = lR = (mu0/pi)ln(d/rw) = 0.759 uH/m (19.3 nH/in); lm = (mu0/2pi)ln(d/(2rw)) = 0.24 uH/m (6.1 nH/in); cG = cR = 11.1 pF/m (0.28 pF/in); cm = 5.17 pF/m (0.13 pF/in); Zc isolated 227.7 ohm, in presence of other circuit 216 ohm | as stated | d, rw | Bare wires (wide-separation) | calc | §9.3.2 Ex.9.1 p.459–460 | high |
| PAUL-2053 | crosstalk | Two wires above an infinite ground plane (image method) | lG = (mu0/2pi)*ln(2hG/rwG); lR = (mu0/2pi)*ln(2hR/rwR); lm = (mu0/4pi)*ln(1 + 4*hG*hR/s^2) (H/m); e.g. 20 AWG (rw = 16 mil), h = 2 cm, s = 2 cm -> lG = lR = 0.918 uH/m, lm = 0.161 uH/m, cG = cR = 10.3 pF/m, cm = 2.19 pF/m, Zc = 275.4 ohm (271 ohm coupled) | hG, hR, s, rw | Wide separation, bare wires | calc | §9.3.2 Eq.(9.31)–(9.35) Ex.9.2 p.460–461 | high |
| PAUL-2054 | crosstalk | Two wires inside an overall cylindrical shield (shield = reference) | lG = (mu0/2pi)*ln((rSH^2 − dG^2)/(rSH*rwG)); lR = (mu0/2pi)*ln((rSH^2 − dR^2)/(rSH*rwR)); lm = (mu0/2pi)*ln{(dR/rSH)*sqrt[((dG*dR)^2 + rSH^4 − 2*dG*dR*rSH^2*cos(thGR))/((dG*dR)^2 + dR^4 − 2*dG*dR^3*cos(thGR))]}; e.g. 28 AWG, dG = dR = 2rw, rSH = 4rw, thGR = 180 deg -> lG = lR = 220 nH/m, lm = 44.6 nH/m, cG = cR = 42 pF/m, cm = 10.7 pF/m, Zc = 65.9 ohm (64.5 coupled) | rSH, dG, dR, thGR, rw | Homogeneous dielectric inside shield | calc | §9.3.2 Eq.(9.36)–(9.38) Ex.9.3 p.462–463 | high |
| PAUL-2055 | crosstalk | Wide-separation (uniform charge) formulas are accurate only when separation/radius >= ~5:1 (proximity effect): at s/rw = 5 exact 17.7 pF/m vs approx 17.3 pF/m (< 3 %); at s/rw = 2.1 exact 88.2 vs approx 37.4 pF/m (236 % error) | c_exact = pi*eps0/ln(s/(2rw) + sqrt((s/(2rw))^2 − 1)); c_approx = pi*eps0/ln(s/rw) | s, rw | Closely spaced wires require exact/numerical methods | calc | §9.3.3 Eq.(9.39) p.463 | high |
| PAUL-2056 | materials | Wire dielectric insulation cannot be ignored for capacitance (ribbon cable: effective eps_r' 1.507–1.664) although it does not affect inductance; wide-separation inductance error only 1.4–2.0 % | eps_r' = C/C0 per entry | insulation eps_r, thickness | Ribbon cable, PVC-type insulation (Table 9.1/9.2) | calc | §9.3.3.1 Tables 9.1, 9.2 p.471–472 | high |
| PAUL-2057 | crosstalk | Parallel-plate capacitance C = eps*A/d neglects fringing; accurate only for d/w << 1 (use MoM for d ≈ w) | C = eps*A/d | A, d, w | Plate width w >> separation d | calc | §9.3.3 Eq.(9.40) p.465; Fig.9.15 | high |
| PAUL-2058 | crosstalk | Weak-coupling, electrically-short inductive–capacitive crosstalk model: generator treated as isolated line with dc-like current and voltage; receptor driven by total mutual inductance and capacitance | I_Gdc = VS/(RS+RL); V_Gdc = RL*VS/(RS+RL); Lm = lm*L; Cm = cm*L | RS, RL, lm, cm, L | Weak coupling (one-way), L << lambda = v/f | calc | §9.4 Eq.(9.64) p.478–479 | high |
| PAUL-2059 | crosstalk | Frequency-domain near-end and far-end crosstalk (inductive + capacitive) | V_NE/VS = j*omega*[RNE/(RNE+RFE) * Lm/(RS+RL) + RNE*RFE/(RNE+RFE) * RL*Cm/(RS+RL)]; V_FE/VS = j*omega*[−RFE/(RNE+RFE) * Lm/(RS+RL) + RNE*RFE/(RNE+RFE) * RL*Cm/(RS+RL)] | RS, RL, RNE, RFE (ohm), Lm (H), Cm (F), f | Weakly coupled, electrically short; crosstalk rises +20 dB/decade | calc | §9.4.1 Eq.(9.66)–(9.69) p.480–481 | high |
| PAUL-2060 | crosstalk | Inductive (magnetic) coupling dominates for low-impedance terminations, capacitive (electric) coupling for high-impedance terminations, relative to the circuit characteristic impedances | NE: inductive dominates if Lm/Cm > RFE*RL (homogeneous: RFE*RL/(ZCG*ZCR) < 1); FE: inductive dominates if Lm/Cm > RNE*RL (RNE*RL/(ZCG*ZCR) < 1); ZCG = sqrt(lG/(cG+cm)), ZCR = sqrt(lR/(cR+cm)) | terminations, ZCG, ZCR | Homogeneous medium for the Z form | calc | §9.4.1 Eq.(9.70),(9.71) p.481 | high |
| PAUL-2061 | crosstalk | Common-impedance coupling through the reference-conductor resistance sets a frequency-independent crosstalk floor at low frequency | V0 = R0*VS/(RS+RL), R0 = r0*L; M_NE_CI = RNE/(RNE+RFE) * R0/(RS+RL); M_FE_CI = −RFE/(RNE+RFE) * R0/(RS+RL); total V/VS = j*omega*(M_IND + M_CAP) + M_CI | r0 (ohm/m), L, terminations | Electrically short; dominant below the frequency where omega*M = M_CI | calc | §9.4.1.1 Eq.(9.72)–(9.75) p.483–484; Fig.9.28 | high |
| PAUL-2062 | crosstalk | Ribbon cable crosstalk benchmark (4.737 m, 28 AWG, 50 mil, PVC eps_r = 3.5, center reference, RS = 0, R = 50 ohm): V_NE/VS = j7.61e-8*f + 9.21e-3 -> floor −40.7 dB, −22.4 dB at 1 MHz (measured ≈ −23 dB); R = 1 kohm: j9.69e-8*f + 4.61e-4 -> floor −66.7 dB, −20.3 dB at 1 MHz; within 3 dB up to 10 MHz (L ≈ lambda0/6) | MoM PUL: lG = lR = 0.749 uH/m, lm = 0.24 uH/m, cG = cR = 18 pF/m, cm = 6.27 pF/m, ZC = 173 ohm, r0 = 0.194 ohm/m (R0 = 0.921 ohm) | — | Line is 1 lambda at 63.3 MHz, electrically short below ≈ 6 MHz | measure | §9.4.1.2 p.484–487; Fig.9.30 | high |
| PAUL-2063 | crosstalk | Choose the conductor between generator and receptor (the middle wire) as the reference/return: using an outer wire as reference raised NEXT at 1 MHz from −22.4 to −15.65 dB (50 ohm) and from −20.3 to −10.87 dB (1 kohm) | ΔNEXT ≈ +6.8 dB (50 ohm), +9.4 dB (1 kohm) with outer reference | reference wire assignment | 3-wire ribbon cable | calc | §9.4.1.2 Review Ex.9.2, 9.3 p.487 | high |
| PAUL-2064 | crosstalk | Coupled microstrip benchmark: two 1 oz lands 100 mil wide, 100 mil edge gap, 62 mil FR4 (eps_r = 4.7) over ground, 20 cm: lm = 37.15 nH/m, cm = 4.93 pF/m, lG = lR = 0.335 uH/m, cG = cR = 110.6 pF/m, eps_eff ≈ 3.5, ZC = 53.85 ohm; measured M_NE = 1.06e-10 (50 ohm) and 6.37e-10 (1 kohm); MTL model within 1 dB to 250 MHz (50 ohm), 3 dB to 100 MHz (1 kohm) | abs(V_NE/VS) = omega*(Lm/(2R) + R*Cm/2) = 2*pi*f*M_NE for RS = 0, RL = RNE = RFE = R | — | Lands lambda/10 at ≈ 80 MHz; 1 kohm-in-BNC loads add ≈ 10 pF | measure | §9.4.1.2 Eq.(9.76) p.487–490; Fig.9.32 | high |
| PAUL-2065 | test | Extract total mutual inductance and capacitance from two NEXT measurements in the +20 dB/decade region using two load values | M_NE = abs(V_NE/VS)(f0)/(2*pi*f0); solve M_NE(R1), M_NE(R2) for Lm, Cm via M_NE = Lm/(2R) + R*Cm/2 | measured NEXT at f0, R1, R2 | RS = 0, equal loads R | measure | §9.4.1.2 Eq.(9.76) p.488 | high |
| PAUL-2066 | crosstalk | Time-domain crosstalk of an electrically short line = crosstalk coefficient × source slew rate (+ common-impedance replica) | V_NE(t) = (M_NE_IND + M_NE_CAP)*dVS/dt + M_NE_CI*VS(t); V_FE(t) = (M_FE_IND + M_FE_CAP)*dVS/dt + M_FE_CI*VS(t); peak ≈ M*ΔV/tr | M coefficients (s), ΔV (V), tr (s) | M_NE always > 0; M_FE > 0 if capacitive dominates, < 0 if inductive dominates | calc | §9.4.2 Eq.(9.80),(9.85) p.491–494 | high |
| PAUL-2067 | crosstalk | Validity of the lumped crosstalk model for pulses: rise/fall time must exceed ten one-way line delays | tr, tf > 10*TD; TD = L/v; (from fu = 1/tr and L < lambda/10 at fu) | tr, L, v | Approximate criterion; e.g. 4.737 m ribbon TD = 15.8 ns -> tr > ~150 ns; 20 cm microstrip (eps_eff' ≈ (1+4.7)/2 = 2.85) TD = 1.125 ns -> tr >~ 12 ns | calc | §9.4.2 Eq.(9.81)–(9.84) p.493–494 | high |
| PAUL-2068 | crosstalk | Time-domain benchmark: RS-232-like 2.5 V, 20 kHz, tr = 400 ns (6.25e6 V/s) on the 4.737 m ribbon -> NEXT peak 75 mV (50 ohm) with 23 mV common-impedance offset; 96.4 mV (1 kohm) with 1.15 mV offset; FEXT −66 mV / −89 mV. 2.5 V, 1 MHz, tr = 50 ns (5e7 V/s) on the 20 cm microstrip -> NEXT 5.3 mV predicted/5.5 mV measured (50 ohm), 31.9 mV predicted/24 mV measured (1 kohm); FEXT −2.14 mV / 31.5 mV | V = M*dV/dt | — | Model validity from tr > 10*TD | measure | §9.4.2.2 p.495–499; Review Ex.9.5, 9.6 | high |
| PAUL-2069 | crosstalk | PCB coplanar three-land reference case (w = s = 15 mil, h = 47 mil, eps_r = 4.7, outer land reference): L = [[1.105, 0.691],[0.691, 1.381]] uH/m, C = [[40.6, −20.3],[−20.3, 29.7]] pF/m; with middle land as generator, 20 cm, RS = 50, RL = 100, RNE = 500, RFE = 200 ohm, 10 MHz -> FEXT = −42.2 dB | as stated | — | Lands on surface of a board with no ground plane; PCB.FOR, 30 subsections/land | calc | §9.3.3.2 Fig.9.23 p.476; Review Ex.9.4 p.490 | high |
| PAUL-2070 | crosstalk | With equal terminations RS = RL = RNE = R the inductive and capacitive crosstalk contributions are equal when R = sqrt(Lm/Cm); at that R the far-end inductive and capacitive terms cancel (FEXT ≈ 0) | R_eq = sqrt(Lm/Cm); e.g. Lm = 1 uH, Cm = 250 pF -> 63.25 ohm, VFE,max = 0 | Lm, Cm | Weakly coupled, electrically short | calc | Prob.9.4.3, 9.4.10 p.552 | medium |
| PAUL-2071 | cables | Shield per-unit-length resistance: braid rS = rb/(B*W*cos(theta_w)); solid (flatpack/coax) shield rS = 1/(sigma*2*pi*rsh*tsh) (current taken uniform over wall) | rS (ohm/m); rb = braid-wire resistance per m | B, W, theta_w, rb, sigma, rsh, tsh | Crosstalk to shielded wires | calc | §9.5.1 Eq.(9.87),(9.88) p.500–501 | high |
| PAUL-2072 | cables | Shield-over-ground inductances: self-inductance of shield circuit equals shield–receptor mutual inductance (lRS = lS); this identity is what lets a both-ends-grounded shield cancel inductive coupling | lS = (mu0/2pi)*ln(2hR/(rsh+tsh)); lR = (mu0/2pi)*ln(2hR/rwR); lGS = lGR = (mu0/4pi)*ln(1 + 4hG*hR/s^2); cRS = 2*pi*eps0*eps_r/ln(rsh/rwR) | hG, hR, s, rsh, tsh, rwR, eps_r | Ground plane reference, wide separation | calc | §9.5.1 Eq.(9.89)–(9.95) p.501–503 | high |
| PAUL-2073 | cables | A shield acts as a Faraday cage for the enclosed wire: generator-to-receptor mutual capacitance cGR = 0 and receptor self-capacitance cR = 0; ungrounded shield leaves capacitive coupling ≈ unchanged because CRS >> CGS (CRS ∥ CGS ≈ CGS ≈ CGR) | V_CAP = j*omega*(RNE*RFE/(RNE+RFE))*(CRS*CGS/(CRS+CGS))*V_Gdc (shield floating) | CRS, CGS | Electrically short line | calc | §9.5.1 p.503; §9.5.2 Eq.(9.97)–(9.99) p.504–505 | high |
| PAUL-2074 | cables | Grounding a shield at either end removes capacitive (electric-field) coupling for electrically short lines; for electrically long lines ground the shield at multiple points spaced about lambda/10 | V_CAP = 0 if shield grounded at >= 1 end; spacing <= lambda/10 for long lines | L/lambda | Low-impedance ground connection | inspect | §9.5.2 Eq.(9.100) p.505 | high |
| PAUL-2075 | cables | A shield must be grounded at BOTH ends to reduce inductive (magnetic) coupling, and only above the shield break frequency, where the generator return current transfers from the ground plane to the shield; above fSH the inductive crosstalk becomes flat with frequency | SF = RSH/(RSH + j*omega*LSH) = 1/(1 + j*f/fSH); fSH = RSH/(2*pi*LSH); SF ≈ 1 (f < fSH), ≈ RSH/(j*omega*LSH) (f > fSH); V_NE_IND(f > fSH) = RNE/(RNE+RFE) * LGR/(RS+RL) * RSH/LSH * VS | RSH = rS*L (ohm), LSH = lS*L (H) | Single-point (one-end) shield grounding gives no magnetic shielding | calc | §9.5.2 Eq.(9.101)–(9.111) p.505–509 | high |
| PAUL-2076 | cables | Shield grounding benchmark (3.6576 m over ground at 1.5 cm; 20 AWG generator; shielded 22 AWG, Teflon eps_r = 2.1, rsh = 35 mil, braid 36 AWG r = 2.5 mil, theta_w = 30 deg, B = 16, W = 4, tsh ≈ 5 mil): RSH = 89.8 mohm, LSH = 2.48 uH, LGR = LGS = 1.98 uH, CRS = 503.6 pF, CGS = 76.3 pF, CGR = 48.2 pF, fSH = 5.8 kHz. At 100 kHz NEXT: R = 50 ohm OO 1.348e-2, OS/SO 1.24e-2, SS 7.17e-4; R = 1 kohm OO 2.144e-2, OS/SO 6.22e-4, SS 3.59e-5 | as stated | — | RS = 0, RL = RNE = RFE = R | measure | §9.5.3 p.510–518; Fig.9.50; Review Ex.9.7, 9.8 | high |
| PAUL-2077 | cables | Shield effectiveness depends on which coupling dominates: for low-impedance (inductive-dominant) circuits a one-end-grounded shield gives no reduction; for high-impedance (capacitive-dominant) circuits one-end grounding already removes the dominant term | classify via RFE*RL vs ZCG*ZCR (PAUL-2060) | terminations, Zc | Choose grounding (one end vs both ends) from the dominant mechanism | review | §9.5.3 p.516–517; Fig.9.51 | high |
| PAUL-2078 | cables | Even when L ≈ lambda0/400 (3.66 m at 200 kHz) the end at which a single-end-grounded shield is bonded matters for high-impedance circuits: grounding only the far end left the near-end shield voltage non-zero and NEXT rose above ≈ 200 kHz | ground the shield at the end where the victim is sensitive, or both ends | L/lambda0 | R = 1 kohm case | measure | §9.5.3 p.518 | high |
| PAUL-2079 | cables | Pigtails (shield brought out through a connector pin by a wire) expose the inner conductor and add unshielded coupling that rises +20 dB/decade; 8 cm pigtails (4.4 % of a 3.66 m line) raised NEXT by up to ≈ 30 dB above 1 MHz vs 0.5 cm pigtails (R = 50 ohm) and dominated above ≈ 100 kHz; pigtails > 5 in. are common in practice | V_NE = V_left_pigtail + V_shielded + V_right_pigtail (superpose inductive + capacitive per section) | pigtail length | Use 360 deg peripheral bonding; keep pigtails as short as possible (0.5 cm ~ minimum without peripheral bond) | inspect | §9.5.4 Eq.(9.112) p.518–519; Figs.9.52–9.56 | high |
| PAUL-2080 | cables | Shielding both generator and receptor wires (each grounded at both ends) multiplies two shield factors: crosstalk rolls off at −20 dB/decade above the second break frequency (until pigtail coupling takes over) | V/VS = (V_IND/VS)_unshielded * RSHG/(RSHG + j*omega*LSHG) * RSHR/(RSHR + j*omega*LSHR); fSHG = RSHG/(2*pi*LSHG), fSHR = RSHR/(2*pi*LSHR) | shield R, L | Example: identical shields fSH ≈ 6 kHz, −20 dB/dec to 100 kHz, then +20 dB/dec from 8 cm pigtails | calc | §9.5.5 Eq.(9.113),(9.114) p.519–521; Fig.9.57, 9.59 | high |
| PAUL-2081 | crosstalk | A twisted pair is the dual of a shield: twisting inherently reduces inductive coupling (net emf ≈ one half-twist for odd N, ≈ 0 for even N) but reduces capacitive coupling only if both ends are balanced to the reference | V_NE/VS = RNE/(RNE+RFE)*j*omega*(lm1 − lm2)*L_HT/(RS+RL) + RNE*RFE/(RNE+RFE)*j*omega*cm*L*RL/(RS+RL); lm1,2 = (mu0/4pi)*ln[1 + 4h(h ± Δh)/(d^2 + Δh^2)] | lm1, lm2, L_HT, cm, L, terminations | Unbalanced termination (one pair wire grounded at near end), weakly coupled, electrically short | calc | §9.6.1, 9.6.2 Eq.(9.115)–(9.120) p.529–536 | high |
| PAUL-2082 | crosstalk | For unbalanced terminations, twisting reduces total crosstalk only in low-impedance (inductive-dominant) circuits; in high-impedance circuits the capacitive floor dominates and twisting gives no reduction — twisted pairs are typically effective for power-distribution (low-impedance) circuits | measured (4.705 m, 20 AWG, 2 cm spacing/height, N = 225, L_HT = 2.09 cm ≈ 7 twists/ft): R = 1 kohm little change; R = 50 ohm SWP −20 dB, TWP another −10 dB; R = 1 ohm SWP −26 dB, TWP another ≈ −80 dB | R vs Zc | RS = 0, RL = RNE = RFE = R | measure | §9.6.2, 9.6.3 p.536–546; Fig.9.76, 9.77 | high |
| PAUL-2083 | crosstalk | Twisted-pair benchmark values (d = 2 cm, h = 2 cm, 20 AWG rw = 16 mil, Δh = 33 mil): lm1 = 1.641e-7, lm2 = 1.574e-7 (difference 6.706e-9), lG = 9.179e-7, lR1 = 9.261e-7, lR2 = 9.093e-7, lR1R2 = 6.344e-7 H/m; cm1 = 1.411, cm2 = 1.190 pF/m. abs(V_NE/VS) = f*(4.403e-13 + 1.922e-8) at R = 1 kohm; f*(8.81e-12 + 0.96e-9) at 50 ohm; f*(4.40e-10 + 1.92e-11) at 1 ohm | abs(V_NE/VS) = 2*pi*f*[(lm1 − lm2)*L_HT/(2R) + (R/2)*cm*L] | — | cm = (cm1 + cm2)/2 | calc | §9.6.1 p.532–533; §9.6.3 Eq.(9.121) p.541–545 | high |
| PAUL-2084 | crosstalk | For very low-impedance loads (R = 1–3 ohm) twisted-pair crosstalk is extremely sensitive to odd/even number of half-twists (up to 40 dB); precise prediction is not feasible — design with margin | sensitivity up to 40 dB | R, twist count | Unbalanced (R = 1, 3 ohm) and balanced pairs over a wide range of R | measure | §9.6.3 p.546; Fig.9.78 | high |
| PAUL-2085 | crosstalk | Balanced terminations (center-tapped transformer or balanced drivers/receivers) eliminate the capacitive contribution to a twisted pair; the remaining crosstalk is the inductive coupling of one half-twist, making balanced twisted pairs sensitive to line twist over a wide range of terminations | V/VS = inductive term of SWP with length L_HT only | balance of terminations | Balanced pair | calc | §9.6.4 Eq.(9.122) p.546–548; Fig.9.80 | high |
| PAUL-2086 | emc | Any wire penetrating a shielded enclosure without treatment virtually eliminates the enclosure's shielding: filter the cable at the entry/exit point or use a shielded cable whose shield is peripherally (360 deg) bonded to the enclosure at the entry point; a wire/pigtail from cable shield to enclosure conducts shield current inside | treated penetrations: filter or 360 deg bond | each penetration | Metallic product enclosures | inspect | Ch.10 intro p.557–558; Fig.10.2a,b | high |
| PAUL-2087 | cables | A cable shield connected (by pigtail) to a noisy point such as logic ground becomes a monopole antenna; removing such a shield can reduce emissions. Terminate cable shields to a zero-potential (chassis) point, peripherally | shield resonates when L_cable ≈ lambda0/4; 1.5 m cable -> 50 MHz; CM resonances frequently seen 50–100 MHz | cable length (m) | Peripheral cables (printer cables ≈ 1.5 m) | calc | Ch.10 intro p.558–559; Fig.10.2c | high |
| PAUL-2088 | emc | Babinet's principle: a slot in a shield radiates like a dipole of the same length (E and H interchanged); a lambda0/2 slot is an efficient radiator no matter how narrow ("if you can't see light through it, it still radiates") — short out lid/door seams with conductive gaskets or beryllium finger stock | slot resonant at L = lambda0/2 = 150/f_MHz (m) | slot length | Seams around lids, doors, panels | inspect | Ch.10 intro Eq.(10.1) p.559–561; Fig.10.3 | high |
| PAUL-2089 | emc | Do not rely on shielding to fix emissions; apply the same EMC design principles whether or not the product is shielded (plastic-enclosure products can comply) | — | — | Product architecture | review | Ch.10 intro p.561 | high |
| PAUL-2090 | emc | Shielding effectiveness definition (electric field; magnetic-field form identical only for plane waves with same medium both sides) | SE = 20*log10(abs(E_i)/abs(E_t)) dB (or 20*log10(abs(H_i)/abs(H_t))); 100 dB = 1e5, 120 dB = 1e6 reduction; SE_dB = R_dB + A_dB + M_dB (M <= 0) | E_i, E_t | E-field definition used as standard for near and far fields | calc | §10.1 Eq.(10.2)–(10.4) p.561–563 | high |
| PAUL-2091 | emc | Far-field (plane-wave) shielding effectiveness of a solid good-conductor barrier (exact result reduced for eta << eta0, t >> delta) | abs(E_i/E_t) ≈ abs(eta0/(4*eta)) * e^(t/delta); SE_dB = R_dB + A_dB + M_dB; eta = sqrt(omega*mu/sigma)∠45 deg; eta0 = 120*pi ohm | sigma, mu, t, f | Normal incidence, same medium (air) both sides, sigma >> omega*eps | calc | §10.2.1 Eq.(10.11)–(10.16) p.566–567; §10.2.2.4 Eq.(10.32) p.573 | high |
| PAUL-2092 | emc | Plane-wave reflection loss of a metal barrier: largest at low frequency and for high-conductivity metals, degraded by permeability; falls −10 dB/decade | R_dB = 168 + 10*log10(sigma_r/(mu_r*f)); f in Hz; sigma_r = sigma/sigma_Cu, sigma_Cu = 5.8e7 S/m; copper: 138 dB at 1 kHz, 98 dB at 10 MHz; sheet steel (mu_r = 1000, sigma_r = 0.1): 98 dB at 1 kHz, 58 dB at 10 MHz; at 1 MHz: Al 106 dB, brass 102 dB, stainless 64 dB | sigma_r, mu_r, f | Far-field source, good conductor | calc | §10.2.2.4 Eq.(10.34),(10.35) p.573; Review Ex.10.1 p.575 | high |
| PAUL-2093 | materials | Skin depth of a metal | delta = 1/sqrt(pi*f*mu*sigma) = 0.06609/sqrt(f*mu_r*sigma_r) m = 2.6/sqrt(f*mu_r*sigma_r) in. = 2602/sqrt(f*mu_r*sigma_r) mils; at 1 MHz: Al 3.33 mil, brass 5.1 mil, stainless 0.82 mil; steel SAE 1045: 0.048 mil (30 MHz), 0.026 mil (100 MHz), 0.0082 mil (1 GHz) | f (Hz), mu_r, sigma_r | Good conductor | calc | §10.2.2.4 Eq.(10.36) p.573; Review Ex.10.2 p.575; Prob.10.2.1 p.589 | high |
| PAUL-2094 | emc | Absorption loss grows as sqrt(f) on a dB scale (i.e. very fast) and with mu_r*sigma_r; ≈ 8.7 dB per skin depth of thickness | A_dB = 8.686*t/delta = 131.4*t*sqrt(f*mu_r*sigma_r) (t in m) = 3.338*t*sqrt(f*mu_r*sigma_r) (t in in.); 8.7 dB at t = delta, 17.4 dB at t = 2*delta; 125 mil at 1 MHz: Al 326 dB, brass 213 dB, stainless 1320 dB | t, f, mu_r, sigma_r | Same for far-field and near-field sources | calc | §10.2.2.2 Eq.(10.25); §10.2.2.4 Eq.(10.37),(10.38) p.574; Review Ex.10.3 | high |
| PAUL-2095 | emc | Multiple-reflection correction is negligible for t >> delta but negative (reduces SE) for thin barriers | M_dB = 20*log10abs(1 − ((eta0 − eta)/(eta0 + eta))^2 * e^(−2*gamma*t)) ≈ 20*log10abs(1 − e^(−2t/delta)*e^(−j2t/delta)); t/delta = 0.1 -> M = −11.8 dB | t/delta | Good conductor; more significant for magnetic fields | calc | §10.2.1 Eq.(10.16b) p.567; §10.2.2.3 Eq.(10.31) p.572 | high |
| PAUL-2096 | emc | Electric fields are mainly "shorted out" at the first surface (primary E transmission occurs at the second surface) so thin shields work for E fields; magnetic fields transmit mainly at the first surface so absorption (thickness, mu*sigma) matters most for H-field shielding | E: thin conductive shield sufficient; H: need t/delta large | source type | Far-field analysis; carries to near field | review | §10.2.2.1 p.569–570 | high |
| PAUL-2097 | emc | Reflection loss dominates at low frequencies and absorption at high frequencies: 20 mil copper -> absorption dominant above ≈ 2 MHz; 20 mil steel (SAE 1045) -> reflection dominant only below ≈ 20 kHz | crossover where R_dB = A_dB | material, t | Plane-wave source (graphs Fig.10.8, 10.9) | calc | §10.2.2.4 p.575; Figs.10.8, 10.9 | medium |
| PAUL-2098 | emc | Near/far-field boundary: 1/r terms equal 1/r^2, 1/r^3 terms at r = lambda0/(2*pi) (≈ lambda0/6); plane-wave properties (E ⊥ H, E/H = eta0) hold only beyond ≈ 3*lambda0 | r_boundary = lambda0/(2*pi) = 47.7/f_MHz (m) | f, r | Electric (Hertzian) and magnetic (loop) dipoles | calc | §10.3.1 p.576–577; Fig.10.10 | high |
| PAUL-2099 | emc | Near-field wave impedance: an electric (short-wire) source is high-impedance (Zw > eta0), a magnetic (loop/transformer) source is low-impedance (Zw < eta0); use Zw in place of eta0 for near-field reflection loss | abs(Zw)e = 1/(2*pi*f*eps0*r) = 60*lambda0/r; abs(Zw)m = 2*pi*f*mu0*r = 2369*r/lambda0 (ohm); e.g. 100 kHz, 15 cm: 1.2e6 ohm (short wire), 0.118 ohm (transformer loop) | f, r (m), lambda0 (m) | beta0*r << 1; electric near field E ∝ 1/r^3, H ∝ 1/r^2; magnetic near field H ∝ 1/r^3, E ∝ 1/r^2 | calc | §10.3.1 Eq.(10.40)–(10.48) p.577–579; Review Ex.10.4, 10.5 | high |
| PAUL-2100 | emc | Classify near-field sources: transformers/inductors ≈ magnetic (loop) sources; spark gaps, arcing contacts, dc-motor brushes ≈ electric sources | — | source type | Choose shielding method by source type | review | §10.3.1 p.579 | high |
| PAUL-2101 | emc | Near-field electric-source reflection loss (higher than plane-wave; rises as the source nears the shield; falls −30 dB/decade) | R_e,dB = 322 + 10*log10(sigma_r/(mu_r*f^3*r^2)); f Hz, r m; e.g. Al, 100 kHz, 15 cm -> 186 dB; 20 mil steel, 5 cm -> 188.02/158.02/128.02 dB at 10 k/100 k/1 MHz | sigma_r, mu_r, f, r | Approximation: eta0 replaced by Zw; absorption term unchanged | calc | §10.3.2 Eq.(10.49),(10.50) p.580; Fig.10.11; Review Ex.10.6; Prob.10.3.1 | high |
| PAUL-2102 | emc | Near-field magnetic-source reflection loss (lower than plane wave, small at low frequency); for accuracy replace r by r/2 (Olsen et al.); if the formula gives a negative value use R = 0 | R_m,dB = 14.57 + 10*log10(f*r^2*sigma_r/mu_r); e.g. stainless, 100 kHz, 15 cm -> 4 dB; 20 mil steel, 5 cm: −11.45 dB (use 0) at 10 kHz, −1.45 dB (use 0) at 100 kHz, 8.55 dB at 1 MHz | f, r, sigma_r, mu_r | Low-frequency magnetic sources: reflection and absorption both small -> use flux diversion or shorted turns | calc | §10.3.3 Eq.(10.51) p.580; Review Ex.10.7; Prob.10.3.2 | high |
| PAUL-2103 | emc | Low-frequency magnetic shielding methods: (1) divert flux with a high-permeability (low-reluctance) path; (2) shorted turn (conductive loop whose induced current opposes the field) | — | f, field level | Near-field magnetic sources at low frequency | review | §10.4 p.581–582; Fig.10.12 | high |
| PAUL-2104 | materials | Permeability of ferromagnetic shields falls with frequency and with field strength (saturation); vendors quote initial mu_r at ≈ 1 kHz and low field. Mumetal mu_r > 10,000 from dc to ≈ 1 kHz, falls sharply above 1 kHz and above ≈ 20 kHz is no better than cold-rolled steel | use mu_r(f, H), not catalogue mu_r | f, H | Graph Fig.10.13 | review | §10.4 p.582; Fig.10.13 | high |
| PAUL-2105 | emc | Shield switching-power-supply magnetic fields with steel, not Mumetal: steel is cheaper and as effective at the switcher fundamental (20–100 kHz) and harmonics; Mumetal is better only below a few tens of kHz (e.g. 60 Hz) if not saturated | f_sw >= 20 kHz -> steel | f_sw | SMPS enclosures | review | §10.4 p.582–583 | high |
| PAUL-2106 | emc | Against saturation (e.g. high-current 60 Hz fields) use a two-layer magnetic shield: first layer low mu_r / hard to saturate (reduces field, gives some E-field reflection), second layer high mu_r | layer 1 low mu_r, layer 2 high mu_r | H level | High-level LF magnetic fields | review | §10.4 p.583; Fig.10.14 | high |
| PAUL-2107 | magnetics | Shorted-turn band (contiguous copper tape) around a switching transformer reduces radiated leakage flux; orient the band's loop area perpendicular to the flux to cancel; gapped cores may need a second, orthogonal band | band loop normal ∥ leakage flux | core gap location, band orientation | Effective for LF magnetic-field emission limits (loop antenna, < 30 MHz) and nearby monitors | inspect | §10.4 p.584; Fig.10.15 | high |
| PAUL-2108 | emc | Ventilation apertures: use many small holes rather than one long slot; a slot interrupting induced shield current degrades SE regardless of its width; a slot parallel to the current has much less effect | hole count/size vs one slot of equal area | aperture geometry | Current direction usually unknown -> use hole arrays | inspect | §10.5 p.585–586; Fig.10.16 | high |
| PAUL-2109 | emc | Seam/lid gaps: gap length matters more than gap thickness; break lid seams with many closely spaced screws and/or metallic gaskets (wire-knit mesh, BeCu finger stock) placed INSIDE the securing screws (outside placement leaves the screw holes unprotected) | seam segment length << lambda0/2 at the highest frequency of concern | screw pitch, gasket position | Shielded enclosure lids, doors | inspect | §10.5 p.586–587; Fig.10.17 | high |
| PAUL-2110 | emc | Waveguide-below-cutoff ventilation (honeycomb): square cell side d, depth l | fc,mn = v0*sqrt(m^2 + n^2)/(2d); fc,10 = 1.5e8/d (d in m) = 5.9e9/d (d in in.); alpha10 = pi/d (f << fc); SE_dB = 27.3*l/d; e.g. 100 dB with 100 x 100 mil cells -> l = 9.3 mm, attenuates dc to 59 GHz | d, l (same units), f | f << fc,10 | calc | §10.5 Eq.(10.52)–(10.57) p.587–588; Prob.10.5.1 | high |
| PAUL-2111 | emc | A cable shield connected to a 1 mV, 37.5 MHz shield-attachment-point voltage on a 2 m printer cable (monopole over the computer chassis) gives ≈ 53.5 dBuV/m at 3 m — far above Class B | E ≈ 53.5 dBuV/m for 1 mV | V_attach, L | Estimate via monopole model | calc | Prob.10.1.2 p.589 | medium |
| PAUL-2112 | process | Involve an experienced EMC engineer from product conceptual development: enclosure/packaging, PCB orientation and cable-routing decisions made first remove most EMC options; late fixes (spacers, steel cages) can negate automated-assembly cost savings | EMC review at concept gate | design stage | All products | review | Ch.11 intro p.593–595; Figs.11.1, 11.2 | high |
| PAUL-2113 | pcb | "Plan B" provisions in first layout: series 0 ohm SMT resistor in clock lands plus unpopulated capacitor pads across them (RC low-pass to slow edges later by BOM change only); pads for alternative connection points of a switching transformer's Faraday shield (ac-input side vs electronics side) | R_series = 0 ohm initially; C pads unpopulated | clock nets, transformer shield | Avoids re-layout after EMC pre-scan | inspect | Ch.11 intro p.596; Fig.11.3 | high |
| PAUL-2114 | emc | Frequency bands of concern for EMC component behavior: conducted emissions 150 kHz–30 MHz; radiated emissions 30 MHz to > 1 GHz — evaluate every component (wires, lands, R, C, L, ferrites, ICs) for non-ideal behavior there | CE 0.15–30 MHz; RE 30–1000+ MHz | f | Commercial limits | review | §11.1 p.597 | high |
| PAUL-2115 | components | A suppression capacitor above its self-resonant frequency behaves as an inductor and can make noise diversion worse; motors have large parasitic capacitance from windings to frame that puts driver noise on the product frame as CM current | f_noise < SRF of the capacitor; account for motor lead-to-frame capacitance | SRF, f | Suppression capacitors, motors bonded to frame for heat sinking | review | §11.1.1 p.597 | high |
| PAUL-2116 | current-carrying | Wire resistance and internal inductance vs skin depth (copper) | r = 1/(sigma*pi*rw^2) for rw < 2*delta; r = 1/(sigma*2*pi*rw*delta) for rw > 2*delta (ohm/m); li = mu0/(8*pi) = 50 nH/m = 1.27 nH/in (rw < 2*delta), li = (1/(4*pi*rw))*sqrt(mu0/(pi*sigma))/sqrt(f) (rw > 2*delta); delta = 6.6e-2/sqrt(f) m = 2.6/sqrt(f) in.; 20 AWG solid (rw = 16 mil) = 2*delta at 106 kHz: 33 mohm/m (0.84 mohm/in) below, 1.02 ohm/m (26 mohm/in) at 100 MHz | rw, f, sigma = 5.8e7 S/m | Internal inductance is negligible vs external (partial) inductance 15–30 nH/in | calc | §11.1.1 Eq.(11.1) p.598–599 | high |
| PAUL-2117 | current-carrying | Wires and PCB lands are inductors at RE frequencies: partial inductance ≈ 15–30 nH/in dominates resistance; a 1 ft 20 AWG "connection" is 113–226 ohm at 100 MHz — parts joined by a long wire are not connected at high frequency | z = r + j*2*pi*f*(15…30 nH/in) per inch; 20 AWG at 100 MHz: 26e-3 + j(9.42…18.8) ohm/in | length, f | 30 MHz–1 GHz | calc | §11.1.1 p.599 | high |
| PAUL-2118 | current-carrying | PCB land resistance vs skin depth | r = 1/(sigma*w*t) for t < 2*delta; r = 1/(2*sigma*delta*(w + t)) for t > 2*delta (ohm/m); 1 oz (1.38 mil) x 5 mil land: 3.9 ohm/m (98.4 mohm/in) below ≈ 14.2 MHz, then ∝ sqrt(f); 10 mil x 1.38 mil x 3 in at 100 MHz with 15 nH/in: Z = 0.344 + j28.27 ohm | w, t, sigma, f | Partial inductance still dominates | calc | §11.1.1 Eq.(11.2) p.599; Review Ex.11.1 p.600 | high |
| PAUL-2119 | cables | View cable lengths in wavelengths: cables radiate efficiently at lambda/4 to lambda/2; a 1.5 m printer cable is lambda/4–lambda/2 between 50 and 100 MHz (classic ≈ 75 MHz CM emission problem, fixed with a ferrite toroid at the cable exit) | lambda/4 <= L <= lambda/2 -> high radiation risk; f = 75/L … 150/L (MHz, L in m) | L | Peripheral cables | calc | §11.1.1 p.600 | high |
| PAUL-2120 | filter | Keep the power-entry filter's input and output lands/wires physically separated; looping output lands back past the input lands couples around the filter (parasitic capacitance) and bypasses it; long phase-wire runs (e.g. to a remote on/off switch) pick up internal noise and carry it out the cord | no input/output land proximity; switch at power entry (mechanical linkage to front) | layout of filter I/O | AC power entry | inspect | §11.1.1 p.600–601; Fig.11.5; §11.4.2 p.656–657; Fig.11.52 | high |
| PAUL-2121 | return-path | "Electrons do not read schematics": return current takes the lowest-impedance path, which at high frequency is the lowest-inductance (smallest-loop) path and differs per frequency component; returns may flow on the +5 V plane or on "60 Hz only" power cords (e.g. 132 MHz = 11th harmonic of 12 MHz found on the power cord with a current probe) | identify return path for every high-speed net | net topology | Low MHz to GHz | review | §11.1.2 p.601–603; Fig.11.6 | high |
| PAUL-2122 | test | Probe every ASIC/microprocessor pin (high-frequency FET probe + spectrum analyzer, relative levels) — "quiet" pins such as reset can carry clock harmonics coupled via bond wires and must not be routed as long lands (add series inductor if needed) | — | pin spectra | Pre-layout and debug | measure | §11.1.2 p.603; §11.3.2 p.638–639; Fig.11.36 | high |
| PAUL-2123 | emc | Conductive-coated or carbon-filled plastic enclosures do not necessarily shield as well as a contiguous metal enclosure; a single untreated penetration can destroy any enclosure's shielding; do not rely on a shield to cure bad PCB layout | treat every penetration (filter/360 deg bond/honeycomb) | enclosure type | Products with access openings (printers) are far from ideal shields | review | §11.1.3 p.603–604; Fig.11.7 | high |
| PAUL-2124 | cables | A braided printer-cable shield pigtailed to a noisy "ground" raised emissions; removing the shield dropped RE > 10 dB. Production fix: route all cable wires and the shield pigtail through a ferrite toroid | ΔRE > 10 dB | shield termination | Centronics-type cables | measure | §11.1.3 p.604–605; Fig.11.8 | high |
| PAUL-2125 | grounding | Common-impedance coupling: subsystems sharing a return impedance ZG impress each other's signals on their ground references (V_G1 = ZG1*(I1 + I2)); ground impedance at RE frequencies is inductive, not the dc resistance: 28 AWG 5.4e-3 ohm/in dc, 65.9e-3 ohm/in at 100 MHz; 20 AWG 8.44e-4 / 25.9e-3 ohm/in; but ≈ 15 nH/in -> 9.43 ohm/in at 100 MHz — thicker wire barely helps | Z_gnd ≈ j*2*pi*f*L_partial | ZG, currents | 30 MHz–1 GHz | calc | §11.2 p.605–606; Fig.11.9 | high |
| PAUL-2126 | pdn | Ground bounce / power-rail collapse: V = L*dI/dt across supply and return partial inductances; e.g. C_LOAD = 10 pF, 3 V in 5 ns -> 6 mA (edges ≈ 1 ns) through 5 in x 15 nH/in = 75 nH -> 0.45 V; 2 in land (30–60 nH), 0→10 mA in 10 ns -> 30–60 mV, in 1 ns -> 300–600 mV, in 500 ps -> 0.6–1.2 V (approaches logic noise margin); TTL crossover current ≈ 50 mA | V_GND = L_GND*dI/dt = C_LOAD*L_GND*d2V/dt2 | L (nH), ΔI, tr | Reduce L (parallel conductors, planes/grids) or its effect (local decoupling) | calc | §11.2 p.606–607; Fig.11.10; §11.2.3 p.612–613 | high |
| PAUL-2127 | grounding | Supply/return currents of switching logic contain pulses at twice the clock rate (e.g. 20 MHz for a 10 MHz clock) with sub-5 ns edges — even small loops of these currents radiate | f_pulse = 2*f_clk | f_clk | Digital boards | review | §11.2 p.608 | high |
| PAUL-2128 | grounding | Safety (chassis/green-wire) ground carries current only during faults (and ESD diversion); signal ground is the return path for signal currents, not an equipotential. Two-wire (no green wire) products still have a CM path via displacement current to the LISN frame and through peripheral-cable grounds: they may lessen but do not eliminate conducted CM emissions | — | product class (2-wire/3-wire) | US 120 V/60 Hz, Europe 240 V/50 Hz mains | review | §11.2.1 p.608–610; §11.2.2 p.610–611 | high |
| PAUL-2129 | return-path | Provide a signal return path immediately adjacent to each "going-down" path; the loop area of go + return sets DM radiation and the loop inductance sets ground-drop; also minimize both path lengths (CM radiation) | minimize loop area A and lengths | route geometry | All signal nets | inspect | §11.2.2 p.611–612; Fig.11.13 | high |
| PAUL-2130 | return-path | Self-partial inductance of a round wire of length l, radius rw | Lp = (mu0*l/(2*pi))*[ln(2l/rw) − 3/4] H (dc); Lp = (mu0*l/(2*pi))*[ln(2l/rw) − 1] H (f -> inf); e.g. 20 AWG, 3 in: 78.9 nH (26.3 nH/in) | l, rw (m) | l >> rw | calc | §11.2.3.1 Eq.(11.11) p.615–616; Review Ex.11.3 p.617 | high |
| PAUL-2131 | return-path | Mutual partial inductance of two parallel filaments (length l, separation d) | Mp = (mu0*l/(2*pi))*[ln(l/d + sqrt(1 + l^2/d^2)) − sqrt(1 + d^2/l^2) + d/l] H; d << l: Mp ≈ (mu0*l/(2*pi))*[ln(2l/d) − 1]; e.g. 3 in, 1/4 in: 34.44 nH exact (11.48 nH/in), 33.19 nH approx | l, d | Mutual partial inductance of orthogonal segments = 0 | calc | §11.2.3.1 Eq.(11.12) p.616–617; Review Ex.11.3 | high |
| PAUL-2132 | return-path | Loop inductance and ground bounce of a go/return pair from partial inductances: moving the return closer raises Mp and lowers both loop inductance and return-conductor voltage drop | Lloop = 2*(Lp − Mp) = (mu0*l/pi)*[ln(d/rw) + 1/4]; V_return = (Lp − Mp)*dI/dt; e.g. 20 AWG, 3 in, 1/4 in apart (Lp − Mp ≈ 14.82 nH/in), 100 mA in 10 ns -> 445 mV | l, d, rw, dI/dt | d << l; increasing d increases ground bounce | calc | §11.2.3.1 Eq.(11.13)–(11.15) p.618; Review Ex.11.4, 11.5 p.618–620 | high |
| PAUL-2133 | return-path | Self-partial inductance of a zero-thickness PCB land (width w, length l, u = l/w) | Lp = (mu0*l/(6*pi))*[3*ln(u + sqrt(u^2 + 1)) + u^2 + 1/u + 3*u*ln(1/u + sqrt(1/u^2 + 1)) − (u^2 + 1)^(3/2)/u] H; u = 10 -> 705.7 nH/m (17.93 nH/in); u = 1000 -> 1.62 uH/m (41.15 nH/in) | l, w | Accurate for u > 10; typical lands w = 5–15 mil, l = 1–5 in (67 < u < 1000) | calc | §11.2.3.2 Eq.(11.16) p.620; Review Ex.11.6 | high |
| PAUL-2134 | return-path | Mutual partial inductance of rectangular bars: treat as filaments (Eq.11.12) unless separation ≈ bar thickness; otherwise subdivide into sub-bar filaments and average | Mp = (1/(B1*B2))*ΣΣ Mp_ij (d = center distance of sub-bars) | B1, B2 subdivisions | Parallel aligned bars | calc | §11.2.3.2 Eq.(11.17) p.620 | high |
| PAUL-2135 | return-path | Return current on a ground plane under a trace/wire at height h concentrates directly beneath it | Js(x) = I*h/(pi*(h^2 + x^2)) A/m; Js(0) = I/(pi*h); fraction within ±d: I(d)/I = (2/pi)*atan(d/h) -> 50 % at d = h, 71 % at 2h, 88 % at 5h, 94 % at 10h | h, d | Electrically small distances; closer trace -> tighter concentration | calc | §11.2.4 Eq.(11.21)–(11.23) p.623–625; Table 11.1 | high |
| PAUL-2136 | return-path | Do not cut slots/splits in ground planes under signal traces: the return detours around the slot, creating a large loop (more radiation) | no signal crossing a plane slot/split | plane cutouts vs routes | Innerplane PCBs | inspect | §11.2.4 p.625; Fig.11.22 | high |
| PAUL-2137 | cables | Route internal cables and wires very close to large conducting planes (chassis): parasitic capacitance gives a displacement-current return path whose loop area shrinks with height | minimize cable height above chassis | routing | Internal cables | inspect | §11.2.4 p.625; §11.2.5 p.628 | high |
| PAUL-2138 | connectors | Connector/ribbon/backplane pin assignment: place returns directly adjacent to signals (GSG or GSSG); clock lines get returns on both sides; several low-rate signals may share returns between ground lands; do not let non-EMC personnel assign pins | adjacent return per signal (GSG/GSSG) | pinout | Connectors, flat cables, edge connectors, backplanes | inspect | §11.2.5 p.626–628; Fig.11.24; §11.4.3 p.658 | high |
| PAUL-2139 | connectors | GSG symmetric returns split the return current equally and cancel the radiated field — the two ground conductors must be connected together at both ends | returns bonded at both ends | GSG topology | Symmetric placement close to signal | inspect | §11.2.5 p.628; Fig.11.25 | high |
| PAUL-2140 | cables | An image plane (metal foil strip under a ribbon/flat cable terminated to the PCB grounds) lets each signal's return flow directly beneath it and reduces radiated emissions | foil under cable bonded to grounds | — | Ribbon/flat cables | inspect | §11.2.5 p.628; Ref.[14] | high |
| PAUL-2141 | grounding | Single-point grounding: use for low frequencies (kHz range and below), low-level analog subsystems, and to keep high-level (motor-driver) return currents out of shared nets; avoid daisy-chain (series) single-point connection (common-impedance coupling); parallel single-point with long leads fails at high frequency (lead impedance, inter-lead coupling) | f <~ kHz range -> single point | f, signal level | Analog / high-level subsystems | review | §11.2.6 p.629–631; Fig.11.26 | high |
| PAUL-2142 | grounding | Multipoint grounding: use for digital subsystems (susceptible to internal common-impedance noise) via a ground plane or grid; valid only if impedance between connection points is small at the frequency of interest (a long narrow land is really a daisy chain); keep high-current (e.g. +38 V motor) returns out of the shared plane | Z between ground points small at f | plane/grid presence | Digital, high frequency | review | §11.2.6 p.630–631; Fig.11.27 | high |
| PAUL-2143 | grounding | Hybrid grounding: capacitors to ground give single-point at LF and multipoint at HF; inductors give the reverse (green-wire safety connection at LF, single-point at HF). Shield grounded directly at one end and via capacitor at the other: single-end at LF, both ends at HF; abs(Zc) < 1 ohm above 100 MHz needs C >= 1.6 nF (large C typical); coaxial double shield (inner grounded one end, outer the other) does the same via inter-shield capacitance | C >= 1/(2*pi*f*abs(Z)max) | f, abs(Z) | Avoid LF ground loops while keeping HF shielding | calc | §11.2.6 p.631–632; Figs.11.28, 11.29; Review Ex.11.7 | high |
| PAUL-2144 | grounding | Segregate three ground systems with dedicated returns to the board connector/power entry: signal ground (low-level; analog single-point, digital multipoint), noisy ground (motor drivers, relays, high-level), hardware/chassis ground (frames, racks; carries current only for faults/ESD). Do not connect hardware ground to signal ground inside the board | 3 separate return trees joined only at the entry point | ground topology | Mixed digital/analog/motor boards | inspect | §11.2.6 p.633–634; Fig.11.30 | high |
| PAUL-2145 | grounding | Ground-loop common-mode currents driven by a ground-voltage difference V_G between subsystems: break with a common-mode choke in the signal+return pair, an optical coupler (large ground offsets, e.g. PWM input of an SMPS), or balanced drivers/receivers (V_out = 2*V_S, V_G cancels) with twisted pairs | — | V_G, interface type | Interconnected subsystems; parasitic capacitance can close the loop (motors) | review | §11.2.7 p.634–636; Figs.11.31–11.33 | high |
| PAUL-2146 | pcb | Rank every part by "signal speed" in a layout-priority spreadsheet; place and route the fastest parts manually first (no autoplace/autoroute for them); digital bandwidth ≈ 1/tr (500 ps -> 2 GHz) | speed ≈ f0*I0/tr; BW = 1/tr | f0 (Hz), I0 (A), tr (s) | Initial layout | review | §11.3.1 Eq.(11.24) p.637 | high |
| PAUL-2147 | pcb | Clock routing: clock source very close to its load, ground (return) lands on both sides of clock lands, RC "plan B" pads | guard/return lands both sides of clock | clock nets | Two-layer and multilayer | inspect | §11.3.1 p.637 | high |
| PAUL-2148 | pcb | Keep the highest-speed components and their lands far from off-board connectors (clock next to an edge connector coupled onto the backplane and failed RE); place high-frequency circuitry at board center, connectors at the edge, to exploit parasitic filtering | max distance(clock/CPU, connectors) | placement | All boards | inspect | §11.3.2 p.637–638; Fig.11.34; §11.4.4 p.658–659 | high |
| PAUL-2149 | pcb | Downstream gates/buffers restore fast edges and undo upstream RC filtering; filter at the point where the signal leaves the board, after the last active stage | filter after last driver | signal chain | Slowed/filtered nets | review | §11.3.2 p.638; Fig.11.35 | high |
| PAUL-2150 | pcb | Place all I/O cable connectors on one edge of the PCB (prevents board-ground voltage differences from driving cables on opposite edges as a dipole) and create a "quiet ground" at that edge: a metal area joined to the noisy logic ground only through a narrow neck, bonded to chassis, for cable-shield termination and ESD diversion; provide pads for DIP toroids (CM) and RC packs (DM only) on every I/O line | connectors on 1 edge; quiet-ground island + chassis bond | connector placement | Off-board cables | inspect | §11.3.3 p.639–640; Figs.11.37, 11.38; §11.4.4 p.659 | high |
| PAUL-2151 | pcb | On two-layer (no-plane) boards use a gridded ground (stitched ground lands on both sides, "screen door"); finer mesh approaches a plane; use vias so the grid does not block orthogonal wiring channels | grid pitch as fine as practical | ground-grid presence/pitch | Low-cost double-sided boards | inspect | §11.3.4 p.641; Fig.11.39 | high |
| PAUL-2152 | pdn | Treat power/return as a transmission line and minimize its characteristic impedance (low l, high c): wide lands on opposite board faces beat side-by-side lands (w = 200 mil, h = 62 mil: 41.05 ohm vs 155.7 ohm with s = 62 mil); power/ground planes 5 mil apart with ≈ 25 mil current spread give ≈ 28.6 ohm | Zc = sqrt(l/c) -> minimize | land geometry | 2S2P and double-sided boards | calc | §11.3.5 Eq.(11.25) p.641–643; Fig.11.40 | high |
| PAUL-2153 | pdn | Inter-plane capacitance of power/ground planes | C = eps_r*eps0*A/d; eps_r = 4.7, A = 100 in^2, d = 5 mil -> ≈ 0.02 uF | A, d, eps_r | Parallel-plate approximation; only part of the area is effective for a given current path | calc | §11.3.5 p.643 | high |
| PAUL-2154 | decoupling | Decoupling capacitor at every module between power and ground pins, as close as possible; lead inductance = entire conductor length from capacitor body to module pins (including PCB land), not just visible leads; best: SMT capacitor directly beneath the module on the opposite side, or distributed (parallel-plate) capacitors under the package; connect the ground side to the ground grid/plane | minimize total cap-to-pin loop length | cap placement | DIP pins at diagonal corners are the worst case | inspect | §11.3.5 p.644–646; Figs.11.41–11.44 | high |
| PAUL-2155 | decoupling | A decoupling capacitor is effective only below its lead-inductance resonance; switching current spectrum extends to 1/tr, so keep f0 above it; for fixed lead length use as small a capacitance as the charge requirement allows | f0 = 1/(2*pi*sqrt(Llead*C)) >= 1/tr (target) | Llead (H), C (F), tr | Above f0 the capacitor is an inductor | calc | §11.3.5 Eq.(11.26) p.646; Fig.11.45 | high |
| PAUL-2156 | decoupling | Paralleling a small capacitor with a large one (same lead inductance L) improves the high-frequency impedance only by 2x (6 dB) — equivalent to halving the large capacitor's lead length — and creates an anti-resonance; worthwhile mainly when the large part is tantalum/electrolytic with large internal inductance | zeros f1 = 1/(2*pi*sqrt(L*C1)), f3 = 1/(2*pi*sqrt(L*C2)); anti-resonance f2 = f3/sqrt(2) = 1/(2*pi*sqrt(2*L*C2)) (C1 >> C2; text prints C1 in f2 but states f3 = sqrt(2)*f2); measured 0.01 uF ∥ 100 pF, 0.25 in 22 AWG leads (L = 11.48 nH, M = 2.046 nH, k = 0.178): resonance ≈ 100 MHz, ≈ 6 dB gain only above ≈ 150 MHz | L, M, C1, C2 | Bode asymptotes, M = 0 | sim | §11.3.5 Eq.(11.27) p.646–648; Figs.11.46, 11.47 | medium |
| PAUL-2157 | decoupling | Minimum local decoupling capacitance from allowed supply droop during an edge | C = I*dt/dV; C = tr/(R*ln(V0/(V0 − ΔV))) ≈ V0*tr/(R*ΔV); e.g. 50 mA, ΔV = 0.1 V, tr = 1 ns -> 500 pF (495 pF with V0 = 5 V, R ≈ 100 ohm) | I (A), tr (s), ΔV (V), V0, R | First-order; verify with SPICE including parasitics | calc | §11.3.5 Eq.(11.28)–(11.32) p.649–651; Fig.11.48 | high |
| PAUL-2158 | pcb | Inspect power-distribution and signal-return loop areas by printing only the +5 V and ground nets (and each critical net) from the layout tool; fix large loops before prototypes | minimize loop area per net | net plots | All boards | inspect | §11.3.6 p.651–652; Figs.11.49, 11.50 | high |
| PAUL-2159 | pcb | Mixed-signal partitioning: place digital, low-level analog and high-level noisy (motor) circuits in separate geographic sections; split the POWER plane into separate islands (e.g. +5 V digital, ±12 V analog, +38 V motor) but do NOT split the ground plane — return currents stay under their traces; if planes are split, traces crossing the split create large loops and the two halves form a dipole (connect them directly beneath any crossing trace) | contiguous ground; power islands; no trace over a split | plane layout | Two-layer boards: use a ground grid | inspect | §11.3.7 p.652–655; Fig.11.51 | high |
| PAUL-2160 | pcb | Prefer a single system PCB to several boards interconnected by cables (cable impedance between board grounds drives CM currents); where boards must be separated, use short low-impedance motherboard/backplane lands with interspersed grounds; avoid passing clocks between boards (use asynchronous links) | 1 board preferred | board count | System architecture | review | §11.4.3 p.657–658; Fig.11.53 | high |
| PAUL-2161 | pcb | Buffer high-speed signals where they enter a PCB, not at the driving board: fan-out of 4 at the receiving board cuts interconnect current (and its emission) by 4x | I_cable reduced by fan-out factor | fan-out | Board-to-board signals | review | §11.4.3 p.658 | high |
| PAUL-2162 | emc | Metallic enclosures: close seams (metallic fingers on door edges, knitted-wire gaskets), treat every exiting cable (RC packs per wire or CM choke through which all wires incl. shield pigtail pass); provide through-hole pads bridged by 0 ohm SMT resistors for an RC pack or DIP toroid at every cable exit, reserving board space; plastic enclosures need nickel paint, flame/arc spray, vacuum metallization, electroless plating, foil, or conductive fillers — penetrations still need treatment; vents: many small holes; display windows: laminated wire mesh | provisions reserved in first layout | enclosure, exits | Product enclosures | inspect | §11.4.1 p.655–656 | high |
| PAUL-2163 | filter | Mount the power-line filter directly at the ac power entry point (integral power-socket/filter modules are most effective); a filter on the power-supply PCB away from the entry lets internal noise couple onto the cord ahead of it | filter at entry, no unfiltered internal cord run | filter location | AC-powered products | inspect | §11.4.2 p.656–657; Fig.11.52 | high |
| PAUL-2164 | cables | Route internal cables away from noisy components (e.g. flat cable lying on a clock module coupled via parasitic capacitance and failed RE); do not place two PCBs vertically close together (board-to-board coupling defeats careful layout); packaging and board designers must agree before configuration freeze | cable-to-noise-source clearance | routing, board placement | System configuration | inspect | §11.4.4 p.659; §11.4.5 p.659; Figs.11.1, 11.2 | high |
| PAUL-2165 | emc | Keep a switching transformer (small magnetic loop, near field ∝ 1/r^3) physically away from sensitive boards: modest separation reduces coupling dramatically and avoids steel cages | H ∝ 1/r^3 (doubling r -> −18 dB) | r | 50 kHz SMPS example | calc | Ch.11 intro p.595; Fig.11.2 | medium |
| PAUL-2166 | filter | Subsystem decoupling: ferrite CM chokes (available in DIP packages for auto-insertion) block CM currents between subsystems without affecting DM signals; RC packs/ferrite beads filter DM too and can affect functional signals — use with care; local decoupling capacitors keep switching currents off the inter-subsystem power distribution | — | interface | Board-to-board, board-to-cable | review | §11.4.6 p.659–660 | high |
| PAUL-2167 | components | Motor noise: dc/stepper/ac motors have large winding-to-frame capacitance (measured small dc motor leads-to-frame impedance minimum ≈ 1 ohm near 100 MHz) — drive-circuit noise goes straight onto the product frame; put a CM choke in motor drive wires; suppress commutator arcing with resistive or RC disks on the commutator | abs(Z_leads-frame) ≈ 1 ohm at ≈ 100 MHz | motor type | H-bridge and stepper drivers | measure | §11.4.7 p.660 | high |
| PAUL-2168 | esd | Charge separation by contact/rubbing of insulators follows the triboelectric series only roughly (Table 11.2: positive end air, human skin, glass, nylon, wool ...; negative end polyethylene, polypropylene, PVC, silicon, Teflon); surface smoothness, cleanliness, contact area, pressure, degree of rubbing and separation speed matter more; like materials also charge (opening a plastic bag) | — | materials in contact | Charged insulators cannot discharge; the hazard is induction onto conductors that then arc | review | §11.4.8 p.661–662; Table 11.2 | high |
| PAUL-2169 | esd | Air breakdown ≈ 3e6 V/m = 3 kV/mm (30 kV/cm): only a small voltage between conductors ~1 mm apart (finger to keyboard) arcs; ESD below ≈ 3500 V cannot be felt or seen by humans yet can upset or destroy electronics | E_bd(air) ≈ 3 kV/mm; human perception threshold ≈ 3.5 kV | gap (mm), V | Air at normal conditions | calc | §11.4.8 p.662–663 | high |
| PAUL-2170 | esd | ESD current waveform: charged C at V0 discharging through body/object R and path inductance L (single-discharge RLC model); personnel discharge (higher R) overdamped, furniture discharge (lower R) underdamped; rise times ≈ 200 ps–70 ns, total duration ≈ 100 ns–2 us, peak currents approach tens of amperes at 10 kV; spectrum extends well into the GHz range; multiple discharges per event occur; faster approach -> shorter arc gap -> faster, higher current | tr = 0.2–70 ns; duration 0.1–2 us; I_pk ~ tens of A at 10 kV | V0, R, L, C | Simplistic model (see Boxleitner [22] for detail) | sim | §11.4.8 p.663–664; Fig.11.55 | high |
| PAUL-2171 | esd | Human-body charge is lower in humid environments (reverse charge flow through shoe–carpet contact resistance) and with antistatic carpet sprays, but products must not rely on humidity: design for ESD regardless of installation | human body charge up to ≈ 25 kV max | environment | All products | review | §11.4.8 p.664; p.666 | high |
| PAUL-2172 | esd | ESD damage/upset mechanisms: pre-arc electrostatic field overstresses dielectrics; arc current acts via direct conduction, secondary arcs, capacitive coupling (dominant into high-impedance circuits) and inductive coupling (dominant into low-impedance circuits); conduction causes upset and damage, near-field radiation mostly upset; fields coupling to cables then conducted inside combine both | — | circuit impedance level | Classify each victim net | review | §11.4.8 p.664–665 | high |
| PAUL-2173 | esd | Enclosure potential during ESD: grounded metal enclosure rises to several thousand volts across the green-wire inductance; ungrounded enclosure can rise to the source potential (at most ≈ 25 kV). A penetration-free metal box would keep internal circuits at the same potential (no upset) — every penetration (cables, cord, vents) is an ESD entry point | V_enclosure(grounded) ~ kV; V(ungrounded) <= 25 kV | green-wire inductance, penetrations | — | review | §11.4.8 p.665; Fig.11.56 | high |
| PAUL-2174 | esd | Three ESD strategies: prevent the event (e.g. wire brushes or passive ionizers on paper paths; antistatic packaging), hardware immunity (block/divert coupling), software immunity; antistatic pink polyethylene ≈ 1e9 ohm/square redistributes charge; ordinary insulators > 1e14 ohm/square do not | rho_s(antistatic) ≈ 1e9 ohm/sq vs > 1e14 ohm/sq insulators | surface resistivity | Packaging, paper-handling products | review | §11.4.8 p.665–666 | high |
| PAUL-2175 | esd | Prevent secondary arcs: bond every exposed metal enclosure part (decals, nameplates) to chassis ground; keep interior electronics >= 1 cm (air) from ungrounded metal parts and >= 1 mm from grounded parts; otherwise lengthen the discharge path (overlapping joints), add a secondary shield to circuit ground, or a grounded spark arrestor behind plastic knobs | d_min = V/E_bd: 25 kV/(30 kV/cm) ≈ 1 cm (ungrounded, body up to 25 kV); ≈ 1500 V/(30 kV/cm) -> ≈ 1 mm (grounded part, green-wire drop ≈ 1500 V) | V_part, dielectric | Air insulation; Mylar etc. permits smaller spacing | calc | §11.4.8 p.666–667; Fig.11.57 | high |
| PAUL-2176 | esd | First priority: keep ESD current out of sensitive circuitry by blocking (insulation) or diverting (metal enclosure carries it to ground); treat apertures like shielding apertures (many small holes; break long slots with close screws/gaskets — coupling depends on maximum dimension, not area) and keep sensitive circuitry away from all apertures even when treated | — | apertures, circuit placement | Metallic enclosures | inspect | §11.4.8 p.667–668 | high |
| PAUL-2177 | esd | Cables are the main ESD entry once apertures are treated (diagnose by removing all cables except the power cord during ESD test). Shielded cables help only if 360 deg bonded to the enclosure; a pigtail (≈ 15 nH/in) develops large shield-to-enclosure voltage during the discharge | V_pigtail = L_pigtail*dI/dt, L ≈ 15 nH/in | shield termination | Peripheral cables incl. power cord | measure | §11.4.8 p.668; Fig.11.58 | high |
| PAUL-2178 | esd | Block ESD-induced CM currents on cables with a common-mode choke (also cuts RE), optical couplers, or series impedances in every wire incl. grounds; route ALL conductors (including ground wires and the shield pigtail) through the CM choke — bypassing it with the shield connection defeats it; DIP chokes mount at the cable entry | all conductors through choke | choke wiring | Cable entries | inspect | §11.4.8 p.668–669; Fig.11.59 | high |
| PAUL-2179 | esd | Divert ESD currents at the cable entry with capacitors to the enclosure ground located right at the entry (line-to-line for DM, line-to-ground for CM; Tee/Pi if needed), effective only if the ESD spectrum is above the signal spectrum; a distant ground connection forces the discharge through PCB ground — another reason to put all connectors on one edge | cap-to-chassis loop minimal at entry | cap location, ground distance | Signal and power entries | inspect | §11.4.8 p.669; Fig.11.60 | high |
| PAUL-2180 | esd | Match protection element to input impedance: shunt capacitors work across high-impedance inputs; across low-impedance inputs they are ineffective (current division) — use a series impedance (ferrite bead) instead | Z_shunt << Z_input for diversion; Z_series >> Z_input for blocking | Z_input | Circuit inputs at connectors | review | §11.4.8 p.670 | high |
| PAUL-2181 | esd | Transient suppressors (zener/TVS): response time is inversely related to current capability — pair a fast low-current device with a slow high-current device; clamp diodes to +5 V and ground keep inputs in range; lead inductance of TVS and capacitors must be minimal because ESD energy extends into the GHz range | minimize TVS/capacitor lead and loop inductance | device placement | Inputs exposed to ESD | inspect | §11.4.8 p.670; Fig.11.61 | high |
| PAUL-2182 | esd | Plastic-enclosure products: add a large metal plane under the product bonded to all metal parts and the green wire; connect the electronic grounds of all peripheral connectors to this plane where the connector enters the PCB; mount all PCBs horizontally, close and parallel to this plane (E normal, H parallel to circuit loops); keep loop areas and conductor lengths small, use ground grids and GSG/GSSG routing | PCB-to-plane spacing minimal; horizontal mounting | board orientation, bonding | Products tested on a metal ESD table | inspect | §11.4.8 p.670–671; Figs.11.62, 11.63 | high |
| PAUL-2183 | firmware | Software ESD immunity: no unlimited wait states (lock-up risk); watchdog routines verifying program flow and initiating recovery; parity bits, checksums, error-correcting codes with frequent checks; tie all unused inputs to ground or +5 V; avoid edge-triggered inputs — latch and strobe all inputs | watchdog present; no unbounded waits; unused inputs tied | firmware/HW review | All microprocessor products | review | §11.4.8 p.671–672 | high |
| PAUL-2184 | test | Pre-compliance diagnostic kit: small E-field probe (≈ 1 in. of RG58 shield removed, inner insulation kept), small H-field loop probe (subminiature coax, inner conductor tied to shield), high-impedance high-frequency FET probe to a spectrum analyzer, near-field PCB scanner, high-frequency current probe, and systematic "detective work" (disconnect cables one at a time) | — | — | Near-field levels show where, not whether, a product fails (poor correlation to regulatory far field) | measure | §11.5 p.672–674; Fig.11.64 | high |
| PAUL-2185 | cables | Development-lab CM-current target: a CM current of ≈ 5 uA on a 1 m cable can fail FCC Class B / CISPR 22 Class B — measure every cable with a current probe and drive CM current below 5 uA before booking the semi-anechoic chamber; keep a log of fixes tried and outcomes | I_CM < 5 uA per 1 m cable | I_CM per cable | Radiated emissions pre-scan | measure | §11.5 p.674 | high |
| PAUL-2186 | test | Dominant-effect principle: if E = E1 + E2 with E1 >> E2, reducing E2 changes nothing — identify the dominant contributor before choosing a fix (e.g. separate conducted emissions into CM and DM with a CM/DM separator network) | fix must reduce the dominant term | component levels | CE, RE, crosstalk | measure | §11.5.1 Eq.(11.33) p.674–675; §11.5 p.674 | high |
| PAUL-2187 | filter | Conducted-emission dominance: DM noise usually dominates at the lower frequencies of the CE band -> change line-to-line (X) capacitors; CM dominates at higher frequencies -> change line-to-ground (Y) capacitors and/or the CM choke, or add an inductor in the green wire to block the CM return; CM-choke leakage inductance also blocks some DM | fix element chosen by dominant mode vs f | CE split into CM/DM | LISN 50 ohm phase–green and neutral–green | measure | §11.5.1 p.675–677; Fig.11.65 | high |
| PAUL-2188 | emc | Radiated-emission fix by dominant mode: DM-dominant cable emission -> shunt capacitor between the wires; CM-dominant -> CM choke on the wires; a bypass capacitor does nothing to CM-dominant emission | — | DM/CM identification (PAUL-2030/2031) | Cable emissions | measure | §11.5.1 p.677–678; Figs.11.66–11.68 | high |
| PAUL-2189 | crosstalk | Crosstalk fix by dominant mechanism: low-impedance circuits (inductive dominant, e.g. power supplies) -> twisted pair (or shield grounded both ends above fSH); high-impedance circuits (capacitive dominant) -> shield grounded at one or both ends (or balanced twisted pair) | classify by load impedance vs Zc | loads, Zc | Wire-type cables | review | §11.5.1 p.678–680; Figs.11.69–11.71 | high |
| PAUL-2190 | test | In a time-varying magnetic field the routing of voltmeter/probe leads changes the reading (the lead loop encloses flux and adds a Faraday source): same two points read 40t V with leads outside the flux and −20t V with leads enclosing it. Keep probe lead loops minimal and route leads to avoid enclosing flux | V_meas = V_true ± dPhi_leads/dt | probe loop area, dB/dt | Any measurement near transformers/switching loops | measure | App.B §B.2.1 Ex.B.6 p.705–706 | high |
| PAUL-2191 | materials | Classify a material at frequency f by loss tangent sigma/(omega*eps): >> 1 good conductor, << 1 good dielectric; copper at 1 GHz: 1.04e9; seawater (eps_r 80, sigma 4 S/m) at 1 kHz: 9e5; dry soil (eps_r 4, sigma 1e-5 S/m): displacement current dominates above ≈ 45 kHz | sigma/(2*pi*f*eps0*eps_r) | sigma, eps_r, f | Complex permittivity eps_hat = eps*(1 − j*sigma/(omega*eps)) | calc | App.B §B.2.2 Ex.B.9 p.714; §B.6.4 Eq.(B.80) p.738–739; Prob.B.2.12 | high |
| PAUL-2192 | materials | Good-conductor wave parameters | alpha = beta = 1/delta = sqrt(pi*f*mu*sigma); eta = sqrt(omega*mu/sigma)∠45 deg = (1 + j)/(sigma*delta); v = omega/beta; copper at 1 MHz: alpha = beta = 1.51e4 m^-1, eta = 3.69e-4 ∠45 deg ohm, v = 416 m/s, lambda = 4.16e-4 m; seawater (4 S/m, eps_r 81) at 1 MHz: alpha = 3.97, beta = 3.98, eta = 1.4∠45 deg | sigma, mu, f | sigma/(omega*eps) >> 1 | calc | App.B §B.6.2 Ex.B.13–B.15 p.734–737; §B.6.4 Eq.(B.83)–(B.86) p.739–740 | high |
| PAUL-2193 | current-carrying | Current in a conductor is confined to a few skin depths at the surface facing the field (copper: 8.5 mm at 60 Hz, 0.21 mm at 100 kHz, 2.6 mil at 1 MHz, 0.26 mil = 6.6 um at 100 MHz, 0.0823 mil at 1 GHz; see Table B.1) — use surface area, not cross-section, for RF resistance | delta = 1/sqrt(pi*f*mu*sigma); amplitude falls to 1/e (37 %) per delta | f, material | Good conductors | calc | App.B §B.6.5 Eq.(B.89) Table B.1 p.740–741 | high |
| PAUL-2194 | transmission-line | Wave parameters in a lossless dielectric scale from free space: v = v0/sqrt(eps_r*mu_r), lambda = lambda0/sqrt(eps_r*mu_r), beta = beta0*sqrt(eps_r*mu_r), eta = eta0*sqrt(mu_r/eps_r); lambda0 = 1 m at 300 MHz, 1 cm at 30 GHz; FR4 (eps_r 4.7) at 1 GHz: eta = 173.9 ohm, beta = 45.41 rad/m, v = 1.38e8 m/s, lambda = 13.8 cm; silicon (12): 109 ohm, 72.55 rad/m, 8.66e7 m/s, 8.66 cm | v0 ≈ 3e8 m/s, eta0 = 120*pi ≈ 377 ohm | eps_r, mu_r, f | Uniform plane waves / TEM lines in homogeneous media | calc | App.B §B.6.1 Eq.(B.72) Ex.B.11 p.731–733 | high |
| PAUL-2195 | requirements | Lumped-circuit (Kirchhoff) modeling is acceptable only when the largest circuit dimension is electrically small: < lambda/10 (36 deg phase shift; lambda/100 -> 3.6 deg); lambda = 5000 km at 60 Hz, 300 m at 1 MHz; at CE/RE frequencies products, cables and cords may be electrically large -> use transmission-line/field models | L_max < lambda/10 = v/(10*f) | L_max, f, eps_eff | Model-selection gate for every simulation | calc | App.B intro p.693; §B.7.1.1 p.742–743 | high |
| PAUL-2196 | emc | Average power density with peak-value phasors carries a 1/2 factor; with RMS phasors it does not | S_av = (1/2)*Re{E x H*} (peak); S_av = Re{E x H*} (RMS); plane wave in lossy medium S_av = (Em^2/(2abs(eta)))*e^(−2*alpha*z)*cos(theta_eta) | E, H, units convention | Field/power budget calculations | calc | App.B §B.5 Eq.(B.53) p.726; §B.6.3 Eq.(B.77) p.737 | high |
| PAUL-2197 | sim | SPICE netlist hygiene: no zero-valued elements (short = 1e-8 ohm, open = 1e8 ohm), no floating nodes, every node needs a dc path to ground; suffix F = femto (a 3 F capacitor is not "3F"), M = milli, MEG = mega; current-controlled sources sense through a 0 V source; for transmission lines set the .TRAN step ceiling (default max step = end_time/50) | — | netlist | SPICE2/PSPICE/LTSPICE | review | App.D §D.1.1–D.1.2 p.767–772 | high |
| PAUL-2198 | sim | SPICE .FOUR analyzes only the last period (end_time − 1/f0 … end_time) and reports dc + first 9 harmonics; run several periods (e.g. > 5 time constants) so the waveform is in steady state; .FOUR phases are on a sine basis (add 90 deg to cosine-basis hand results) | end_time >= transient settling + 1/f0 | f0, circuit time constants | .TRAN only | review | App.D §D.1.3 p.773; §D.5 p.805–806 | high |
| PAUL-2199 | crosstalk | Exact lossless multiconductor-line SPICE model: decouple with V = TV*Vm, I = TI*Im so TV^-1*L*TI and TI^-1*C*TV are diagonal; each mode is a two-conductor lossless line; implement terminals with controlled sources. Coupling changes each line's propagation: two 20 AWG wires 2 cm over ground (4.674 m) -> mode Z0 = 323.4 and 226.9 ohm (isolated wire 275.35 ohm), equal delays 15.59 ns (homogeneous); PCB 3 lands (15 mil, 45 mil gap, 47 mil FR4, 25.4 cm) -> 265.9 and 109.6 ohm, delays 1.321 and 1.411 ns (inhomogeneous: two velocities); the lone land pair would be 204.5 ohm, eps_r' 2.6159, 1.369 ns | Z_Cm = sqrt(l_m/c_m); v_m = 1/sqrt(l_m*c_m) | L, C matrices, length | Lossless lines; losses (common-impedance coupling) not modeled | sim | App.D §D.4 Eq.(D.4)–(D.17) p.788–801 | high |
| PAUL-2200 | crosstalk | SPICE MTL benchmarks vs inductive–capacitive model: wires over ground (4.674 m, 50 ohm loads) V_NE/V_S = j4.89e-8*f (M_IND 7.52e-9 + M_CAP 2.56e-10): −86.22 dB at 1 kHz (SPICE −86), −26.22 dB at 1 MHz (SPICE ≈ −27); PCB (25.4 cm) j1.18e-8*f (1.76e-9 + 1.29e-10): −78.5 dB at 10 kHz (SPICE −79), −18.53 dB at 10 MHz (SPICE ≈ −20); PCB time domain (1 V, 10 MHz, tr = 6.25 ns): NEXT peak 95 mV predicted vs 94 mV measured | V_NE/V_S = j*2*pi*f*(M_IND + M_CAP) | — | Lossless SPICE model misses common-impedance coupling that dominated the PCB below ≈ 100 kHz; 1–2 lumped-Pi sections match the TL model while the line is electrically short (< 100 MHz for 25.4 cm) | sim | App.D §D.4.1, D.4.2 p.792–803; Figs.D.29–D.33 | high |
| PAUL-2201 | crosstalk | Time-domain lumped-model validity examples: tr = 12.5 ns vs TD = 15.6 ns -> not valid; tr = 6.25 ns vs modal TD 1.32/1.41 ns (≈ 4x) -> "marginally sufficient"; for inhomogeneous lines test against the longer modal delay | tr/TD_max (target >= 10, >= 4 marginal) | tr, modal TDs | Complements PAUL-2067 | calc | App.D Review Ex.D.1, D.2 p.795, 801 | high |
| PAUL-2202 | emc | Trapezoid harmonic anchors (one-sided amplitudes): 100 MHz, 5 V, 50 %, tr = tf = 1 ns: dc 2.5 V, 1st 3.131, 3rd 0.9108, 5th 0.4053, 7th 0.1673, 9th 0.03865 V, evens ≈ 0; dc + 9 harmonics reconstruct the pulse well because BW = 1/tr = 1 GHz. 50 MHz, 5 V, 50 %, 5 ns edges: dc 2.5, 1st 2.866, 3rd 0.3184, 5th 0.1146, 7th 0.05849, 9th 0.03538 V | as tabulated | f0, A, duty, tr, tf | Verification data for spectrum calculators | sim | App.D §D.5 Ex.D.9, D.10, D.11 Tables D.5, D.6 p.809–813 | high |
| PAUL-2203 | emc | Unequal rise and fall times (even at 50 % duty) create even harmonics and shift individual odd harmonics substantially: 50 MHz, 5 V: tr = 6 ns/tf = 5 ns -> 2nd harmonic 0.1759 V (6.3 % of fundamental), odd-harmonic ratios vs equal edges 1.027/1.498/0.993/2.233/1.346 (n = 1…9); tr = 7 ns -> 2nd 0.320 V (11.9 %), ratios 1.066/2.182/1.627/1.106/1.386. Equal-edge spectral bounds are not guaranteed per harmonic — simulate actual edge shapes | even harmonics = 0 only for 50 % duty AND tr = tf | tr, tf, duty | Clock/data spectra | sim | App.D §D.5 Ex.D.11 Tables D.6–D.8 p.813–815 | high |
| PAUL-2204 | transmission-line | Lumped-Pi model validity anchor: 2 m, three wires r = 10 mil on a 100 mil equilateral triangle, eps_r 2.1: LG = LR = 1.84 uH, Lm = 0.921 uH, CG = CR = Cm = 16.9 pF; valid below 10.35 MHz (L = lambda/10) and for pulses with tr >= 96.6 ns (10*TD) | f_max = v/(10*L); tr_min = 10*L/v | L, eps_r | Single-section lumped Pi | calc | App.D Prob.D.6.1 p.818 | high |

## 2. Formulas & tables (numbers)

### 2.1 Radiated-emission prediction constants (Ch.8)

| quantity | expression | constant | units / conditions | source |
|---|---|---|---|---|
| DM max field | abs(E_D) = K_D * I_D * f^2 * L * s / d | K_D = 1.316e-14 | V/m; I_D A, f Hz, L/s/d m; far field, electrically short/small | Eq.(8.12) p.403 |
| DM transfer at 3 m | abs(E_D/I_D) = K * f^2 * A | K = 4.39e-15 | A = L*s m^2; d = 3 m | Eq.(8.13) p.403 |
| CM max field (I_C per wire, 2 wires) | abs(E_C) = K_C * I_C * f * L / d | K_C = 1.257e-6 | V/m | Eq.(8.16a) p.407 |
| CM max field (net/probe current) | abs(E_C) = 6.283e-7 * I_probe * f * L / d | 6.283e-7 (= 4*pi*1e-7/2) | I_probe = 2*I_C | Eq.(8.16b),(8.21) p.407, 411 |
| CM transfer at 3 m | abs(E_C/I_C) = K * f * L | K = 4.19e-7 | d = 3 m | Eq.(8.17) p.408 |
| Probe screening voltage | V_SA = E_lim + Z_T + 20log d − 20log f_MHz − 20log L + 4.041 | 4.041 dB | dBuV, dBuV/m, dBohm | Eq.(8.24) p.413 |
| CM field from probe (L = 1 m, d = 3 m) | E = V_SA + loss − Z_T + 20log f_MHz + F_GP − 13.58 | −13.58 dB | dBuV/m | Eq.(8.27) p.416 |
| Hertzian dipole coefficient | M = j*2*pi*1e-7*f*L | 2*pi*1e-7 | F(theta) = sin(theta) | Eq.(8.5) p.401 |
| Half-wave dipole coefficient | M = j60 | 60 | F(theta) = cos((pi/2)cos theta)/sin theta | Eq.(8.6) p.401 |

### 2.2 Worked limit currents (FCC Class B, 3 m, 30 MHz, 100 uV/m = 40 dBuV/m)

| case | geometry | current just reaching limit | source |
|---|---|---|---|
| DM, ribbon cable | L = 1 m, s = 50 mil (1.27 mm), 28 AWG | I_D = 19.95 mA | Ex.8.1 p.403 |
| CM, same cable (each wire I_C) | same | I_C = 7.96 uA | Ex.8.2 p.408 |
| CM net (probe) current | L = 1 m | 15.92 uA = 24 dBuA -> 39 dBuV (89 uV) on a 15 dBohm probe | Ex.8.3, 8.4 p.413–414 |

### 2.3 FCC Class B radiated limits quoted in Ch.8 (d = 3 m)

| band (MHz) | limit (dBuV/m) | source |
|---|---|---|
| 30–88 | 40 (100 uV/m) | §8.1.4 p.414 |
| 88–216 | 43.5 | §8.1.4 p.414 |
| 216–960 | 46 | §8.1.4 p.414 |

Measurement distances quoted: FCC Class B 3 m, FCC Class A 10 m; CISPR 22 (EN 55022) 10 m for Class A and Class B (Ch.8 intro p.397).

### 2.4 Table 8.1 — CM current (I_probe, dBuA) vs probe position on a 1 m ribbon cable, f = 100 MHz (10th harmonic of 10 MHz)

| position from oscillator end (cm) | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60 | 65 | 70 | 75 | 80 | 85 | 90 | 95 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| I_probe (dBuA) | 38.7 | 40.7 | 41.9 | 42.6 | 43.4 | 44.3 | 44.7 | 45.1 | 44.7 | 44.4 | 43.9 | 43.2 | 41.9 | 41.1 | 40.2 | 39.5 | 38.4 | 35.5 | 34.0 |

Source: Table 8.1 p.418 (max 45.1 dBuA = 180 uA at 40 cm).

### 2.5 Measurement-antenna data (Ch.7 tail)

| antenna | band | impedance | notes | source |
|---|---|---|---|---|
| Tuned half-wave dipole | 30 MHz upward | (see §7.2, Part 1) | 5 m long at 30 MHz; cannot height-scan vertical | §7.7 p.381 |
| Biconical | 30–200 MHz | Zin = 120 ln(cot(theta_h/2)); 50 ohm at theta_h = 66.8 deg | truncated/wire-cage cones add reactance; discone Rrad = 1/2 | §7.7.1 p.383–384 |
| Log-periodic dipole array | 200 MHz–1 GHz | 50–100 ohm, VSWR < 2.0 | element length = lambda/2 at band edges | §7.7.2 p.385–387 |
| Horn | > 1 GHz | — | — | §7.7 p.381 |

### 2.6 Cable/probe data quoted

| item | value | source |
|---|---|---|
| RG55U loss | ≈ 2.5 dB/100 ft at 100 MHz | Ex.8.5 p.418 |
| Belden 8285 twin lead | Zc ≈ 300 ohm, c = 11.8 pF/m | §8.2.1 p.433 |
| 28 AWG (7x36) ribbon, 50 mil pitch | rw = 7.5 mil, Zc = 228 ohm (air), c = 14.64 pF/m | Ex.8.7, 8.8 p.427–430 |
| Typical current probe | Z_T ≈ 12 dBohm flat 10–100 MHz; book's probe 15 dBohm 10–200 MHz | §8.1.4 p.411 |
| Braid example | 16 belts x 4 wires, r_bw = 2.5 mil, 30 deg weave, r_sh = 35 mil -> r_dc = 24.6 mohm/m, Z_T(1 MHz) = 19 mohm ∠−64.3 deg | Prob.8.2.8 p.443 |
### 2.7 Table 9.1 — three-wire ribbon cable capacitances (outer wire = reference; 28 AWG 7x36, 50 mil pitch, 10 mil insulation eps_r = 3.5)

| entry | with dielectric (pF/m) | without dielectric (pF/m) | effective eps_r' |
|---|---|---|---|
| cG + cm | 37.432 | 22.494 | 1.664 |
| −cm | −18.716 | −11.247 | 1.664 |
| cR + cm | 24.982 | 16.581 | 1.507 |

Source: Table 9.1 p.471.

### 2.8 Table 9.2 — same cable, inductances exact vs wide-separation approximation

| entry | exact (uH/m) | wide-separation (uH/m) | error (%) |
|---|---|---|---|
| lG | 0.74850 | 0.75885 | 1.38 |
| lm | 0.50770 | 0.51805 | 2.04 |
| lR | 1.0154 | 1.0361 | 2.04 |

Source: Table 9.2 p.472.

### 2.9 Per-unit-length parameter reference cases (Ch.9) — use as solver regression anchors

| structure | dimensions | lG / lR | lm | cG / cR | cm | Zc | source |
|---|---|---|---|---|---|---|---|
| 3-wire ribbon, center reference (bare) | 28 AWG rw = 7.5 mil, 50 mil pitch | 0.759 uH/m (19.3 nH/in) | 0.24 uH/m (6.1 nH/in) | 11.1 pF/m (0.28 pF/in) | 5.17 pF/m (0.13 pF/in) | 227.7 ohm isolated; 216 ohm coupled | Ex.9.1 p.460 |
| same, MoM with PVC (eps_r 3.5, 10 mil) | as above | 0.749 uH/m | 0.24 uH/m | 18 pF/m | 6.27 pF/m | 173 ohm | §9.4.1.2 p.484 |
| 2 wires over ground | 20 AWG solid rw = 16 mil, h = 2 cm, s = 2 cm | 0.918 uH/m (23.3 nH/in) | 0.161 uH/m (4.09 nH/in) | 10.3 pF/m | 2.19 pF/m | 275.4 ohm; 271 ohm coupled | Ex.9.2 p.461 |
| 2 wires in shield | 28 AWG, dG = dR = 2rw, rSH = 4rw, 180 deg | 220 nH/m (5.58 nH/in) | 44.6 nH/m (1.13 nH/in) | 42 pF/m (1.07 pF/in) | 10.7 pF/m (0.272 pF/in) | 65.9 ohm; 64.5 ohm coupled | Ex.9.3 p.463 |
| 3 coplanar lands on board (no plane), outer reference | w = s = 15 mil, h = 47 mil, eps_r 4.7 | L11 = 1.105, L22 = 1.381 uH/m | 0.691 uH/m | C11 = 40.6, C22 = 29.7 pF/m (matrix) | 20.3 pF/m | — | §9.3.3.2 p.476 |
| coupled microstrip | 1 oz, w = 100 mil, gap 100 mil, h = 62 mil, eps_r 4.7, L = 20 cm | 0.335 uH/m | 37.15 nH/m (meas 37.2) | 110.6 pF/m | 4.93 pF/m (meas 6.33) | 53.85 ohm; eps_eff ≈ 3.5 | §9.4.1.2 p.488–490 |
| single stripline | w = 5 mil, plane spacing 20 mil, eps_r 4.7 | 0.4666 uH/m (formula 0.461) | — | 112.07 pF/m (formula 113.2) | — | — | Prob.9.3.6 p.550 |
| single microstrip | w = 5 mil, h = 50 mil, eps_r 4.7 | 0.8788 uH/m (formula 0.877) | — | 39.03 pF/m (formula 38.46) | — | — | Prob.9.3.7 p.550 |
| two lands on board (no plane) | w = 15 mil, gap 15 mil, h = 62 mil, eps_r 4.7 | 0.8092 uH/m (formula 0.804) | — | 38.62 pF/m (formula 38.53) | — | — | Prob.9.3.8 p.551 |
| twisted pair over ground | d = 2 cm, h = 2 cm, 20 AWG, Δh = 33 mil | lG 0.9179, lR1 0.9261, lR2 0.9093 uH/m | lm1 0.1641, lm2 0.1574 uH/m; lR1R2 0.6344 | — | cm1 1.411, cm2 1.190 pF/m | — | §9.6.1 p.532–533 |
| 2 wires in PVC-filled shield | 20 AWG, rSH = 250 mil, d = 100 mil, eps_r = 4 | 0.515 uH/m | 74.3 nH/m | 75.4 pF/m | 12.72 pF/m | — | Prob.9.3.5 p.550 |

### 2.10 Proximity-effect check (two bare wires)

| s/rw | exact c (pF/m) | wide-sep c (pF/m) | error |
|---|---|---|---|
| 5 | 17.7 | 17.3 | < 3 % |
| 2.1 | 88.2 | 37.4 | 236 % |

Source: §9.3.3 p.463, Fig.9.11.

### 2.11 Shielded-wire crosstalk benchmark (Fig.9.49, L = 3.6576 m, h = 1.5 cm)

| quantity | value |
|---|---|
| RSH | 89.8 mohm |
| LG, LR, LSH | 3.15 uH, 3.19 uH, 2.48 uH |
| LGR = LGS | 1.98 uH |
| CRS, CGS, CGR (shield removed) | 503.6 pF, 76.3 pF, 48.2 pF |
| fSH | 5.8 kHz |
| ZCG, ZCR (isolated) | 258 ohm, 262 ohm |
| NEXT plateau, SS, f > fSH | 7.17e-4 (R = 50 ohm); 3.59e-5 (R = 1 kohm) |

Source: §9.5.3 p.510–518.

### 2.12 Crosstalk coefficient benchmarks (RS = 0, RL = RNE = RFE = R)

| line | R | M_NE_IND | M_NE_CAP | M_NE_CI | NEXT at 1 MHz | source |
|---|---|---|---|---|---|---|
| 4.737 m ribbon | 50 ohm | 1.14e-8 s | 7.43e-10 s | 9.21e-3 (−40.7 dB) | −22.4 dB | §9.4.1.2 p.485 |
| 4.737 m ribbon | 1 kohm | 5.7e-10 s | 1.49e-8 s | 4.61e-4 (−66.7 dB) | −20.3 dB | §9.4.1.2 p.485–487 |
| 20 cm microstrip | 50 ohm | M_NE = 1.06e-10 s total | | ≈ 0 | — | §9.4.1.2 p.488 |
| 20 cm microstrip | 1 kohm | M_NE = 6.37e-10 s total | | ≈ 0 | — | §9.4.1.2 p.488 |
### 2.13 Table 10.1 — relative conductivity and permeability of shield materials, with absorption (∝ mu_r*sigma_r) and reflection (∝ sigma_r/mu_r) factors

sigma_r = sigma/sigma_Cu, sigma_Cu = 5.8e7 S/m.

| material | sigma_r | mu_r | A ∝ mu_r*sigma_r | R ∝ sigma_r/mu_r |
|---|---|---|---|---|
| Silver | 1.05 | 1 | 1.05 | 1.05 |
| Copper | 1 | 1 | 1 | 1 |
| Gold | 0.7 | 1 | 0.7 | 0.7 |
| Aluminum | 0.61 | 1 | 0.61 | 0.61 |
| Brass | 0.26 | 1 | 0.26 | 0.26 |
| Bronze | 0.18 | 1 | 0.18 | 0.18 |
| Tin | 0.15 | 1 | 0.15 | 0.15 |
| Lead | 0.08 | 1 | 0.08 | 0.08 |
| Nickel | 0.2 | 600 | 120 | 3.3e-4 |
| Stainless steel (430) | 0.02 | 500 | 10 | 4e-5 |
| Steel (SAE 1045) | 0.1 | 1000 | 100 | 1e-4 |
| Mumetal (at 1 kHz) | 0.03 | 30,000 | 900 | 1e-6 |
| Superpermalloy (at 1 kHz) | 0.03 | 100,000 | 3000 | 3e-7 |

Source: Table 10.1 p.574. Note: mu_r of Mumetal/Superpermalloy is the 1 kHz, low-field value; falls sharply above ~1 kHz and with field strength (§10.4, Fig.10.13).

### 2.14 Shielding formula constants (Ch.10)

| quantity | formula | units | source |
|---|---|---|---|
| skin depth | delta = 0.06609/sqrt(f*mu_r*sigma_r) | m (f Hz) | Eq.(10.36) |
| skin depth | delta = 2602/sqrt(f*mu_r*sigma_r) | mils | Eq.(10.36) |
| absorption | A = 131.4*t*sqrt(f*mu_r*sigma_r) | dB, t in m | Eq.(10.37) |
| absorption | A = 3.338*t*sqrt(f*mu_r*sigma_r) | dB, t in in. | Eq.(10.37) |
| absorption per skin depth | A = 8.686*t/delta | dB | Eq.(10.37) |
| reflection, plane wave | R = 168 + 10log10(sigma_r/(mu_r*f)) | dB | Eq.(10.35) |
| reflection, near-field electric | R_e = 322 + 10log10(sigma_r/(mu_r*f^3*r^2)) | dB, r in m | Eq.(10.50) |
| reflection, near-field magnetic | R_m = 14.57 + 10log10(f*r^2*sigma_r/mu_r) (use r/2 per Olsen; floor at 0) | dB | Eq.(10.51) |
| multiple reflection | M = 20log10abs(1 − e^(−2t/delta)*e^(−j2t/delta)) | dB (≤ 0) | Eq.(10.16b) |
| wave impedance, E source | abs(Zw) = 60*lambda0/r | ohm | Eq.(10.43) |
| wave impedance, H source | abs(Zw) = 2369*r/lambda0 | ohm | Eq.(10.48) |
| waveguide cutoff | fc,10 = 1.5e8/d (m) = 5.9e9/d (in.) | Hz | Eq.(10.53) |
| waveguide attenuation | SE = 27.3*l/d | dB | Eq.(10.57) |

### 2.15 Worked shielding anchors (for regression tests of CHECK-SE-*)

| case | R (dB) | A (dB) | source |
|---|---|---|---|
| copper, plane wave, 1 kHz / 10 MHz | 138 / 98 | — | p.573 |
| sheet steel (mu_r 1000, sigma_r 0.1), 1 kHz / 10 MHz | 98 / 58 | — | p.573 |
| Al / brass / stainless, 1 MHz, plane wave | 106 / 102 / 64 | 125 mil: 326 / 213 / 1320 | Review Ex.10.1, 10.3 p.575 |
| 20 mil steel SAE 1045, plane wave, 30 MHz / 100 MHz / 1 GHz | 53.23 / 48 / 38 | 3656.6 / 6676.0 / 21,111 | Prob.10.2.4 p.590 |
| 20 mil steel, electric source 5 cm, 10 kHz / 100 kHz / 1 MHz | 188.02 / 158.02 / 128.02 | 66.76 / 211.11 / 667.6 | Prob.10.3.1 p.590 |
| 20 mil steel, magnetic source 5 cm, 10 kHz / 100 kHz / 1 MHz | −11.45→0 / −1.45→0 / 8.55 | 66.76 / 211.11 / 667.6 | Prob.10.3.2 p.590 |
| Al, electric source, 100 kHz, 15 cm | 186 | — | Review Ex.10.6 p.581 |
| stainless, magnetic source, 100 kHz, 15 cm | 4 | — | Review Ex.10.7 p.581 |
| steel SAE 1045 intrinsic impedance 30 MHz / 100 MHz / 1 GHz | 0.202 / 0.369 / 1.17 ohm ∠45 deg | — | Prob.10.2.2 p.589 |
| brass intrinsic impedance 30 MHz / 100 MHz / 1 GHz | 3.96e-3 / 7.24e-3 / 2.29e-2 ohm ∠45 deg | — | Prob.10.2.2 p.589 |
| skin depth nickel 30 MHz / 100 MHz / 1 GHz | 0.0434 / 0.0238 / 0.0075 mil | — | Prob.10.2.1 p.589 |
| skin depth brass 30 MHz / 100 MHz / 1 GHz | 0.93 / 0.51 / 0.16 mil | — | Prob.10.2.1 p.589 |
| waveguide 100 x 100 mil, 100 dB | l = 9.3 mm; cutoff 59 GHz | — | Prob.10.5.1 p.590 |
### 2.16 Table 11.1 — fraction of ground-plane return current within ±d of the point beneath a conductor at height h

I(d)/I = (2/pi)*atan(d/h)  (Eq.11.23)

| d/h | I(d)/I | % |
|---|---|---|
| 1 | 0.5 | 50 |
| 2 | 0.705 | 71 |
| 5 | 0.874 | 88 |
| 10 | 0.94 (formula gives 0.937; printed "0.9") | 94 |

Source: Table 11.1 p.625.

### 2.17 Table 11.2 — triboelectric series (top = positive / gives up electrons; bottom = negative)

| rank | material | rank | material |
|---|---|---|---|
| 1 | Air | 18 | Hard rubber |
| 2 | Human skin | 19 | Mylar |
| 3 | Asbestos | 20 | Epoxy–glass |
| 4 | Glass | 21 | Nickel, copper |
| 5 | Mica | 22 | Brass, silver |
| 6 | Human hair | 23 | Gold, platinum |
| 7 | Nylon | 24 | Polystyrene foam |
| 8 | Wool | 25 | Acrylic |
| 9 | Fur | 26 | Polyester |
| 10 | Lead | 27 | Celluloid |
| 11 | Silk | 28 | Orlon |
| 12 | Aluminum | 29 | Polyurethane foam |
| 13 | Paper | 30 | Polyethylene |
| 14 | Cotton | 31 | Polypropylene |
| 15 | Wood | 32 | Polyvinyl chloride (PVC) |
| 16 | Steel | 33 | Silicon |
| 17 | Sealing wax | 34 | Teflon |

Source: Table 11.2 p.661. Rough indicator only (surface, pressure, speed dominate).

### 2.18 ESD numbers (§11.4.8)

| quantity | value | source |
|---|---|---|
| Air breakdown field | ≈ 3e6 V/m = 3 kV/mm = 30 kV/cm | p.662, p.666 |
| Human perception threshold | ESD < 3500 V not felt or seen | p.663 |
| Max human-body charge voltage | ≈ 25 kV | p.665–666 |
| Grounded enclosure / part rise during ESD | several kV (enclosure); ≈ 1500 V used for part spacing | p.665–666 |
| Rise time | ≈ 200 ps to 70 ns | p.663 |
| Total duration | ≈ 100 ns to 2 us | p.663 |
| Peak current | approaches tens of A for 10 kV | p.663 |
| Clearance, ungrounded metal part to electronics | ≈ 1 cm (air) | p.666 |
| Clearance, grounded metal part to electronics | ≈ 1 mm (air) | p.666 |
| Pigtail inductance | ≈ 15 nH/in. | p.668 |
| Antistatic (pink polyethylene) surface resistivity | ≈ 1e9 ohm/square | p.666 |
| Insulator surface resistivity | > 1e14 ohm/square | p.666 |

### 2.19 Conductor impedance numbers (§11.1–11.2)

| item | value | source |
|---|---|---|
| partial inductance, wires and lands (rule of thumb) | 15–30 nH/in. | p.598–599, p.612 |
| internal inductance, round wire (low f) | mu0/(8*pi) = 50 nH/m = 1.27 nH/in. | Eq.(11.1c) |
| copper skin depth | 6.6e-2/sqrt(f) m = 2.6/sqrt(f) in. | Eq.(11.1e) |
| 20 AWG solid (rw = 16 mil) | = 2*delta at 106 kHz; 33 mohm/m below; 1.02 ohm/m at 100 MHz | p.599 |
| 28 AWG solid (rw = 6.3 mil) | 5.4e-3 ohm/in dc; 65.9e-3 ohm/in at 100 MHz | p.606 |
| 20 AWG solid | 8.44e-4 ohm/in dc; 25.9e-3 ohm/in at 100 MHz | p.606 |
| 1 oz (1.38 mil) x 5 mil land | 3.9 ohm/m (98.4 mohm/in) below ≈ 14.2 MHz | p.599 |
| land partial self-inductance u = l/w = 10 / 1000 | 705.7 nH/m (17.93 nH/in) / 1.62 uH/m (41.15 nH/in) | Review Ex.11.6 p.620 |
| 20 AWG, 3 in, 1/4 in apart: Lp / Mp / Lp − Mp | 78.9 nH / 34.44 nH / ≈ 14.82 nH/in | Review Ex.11.3, 11.4 |
| power lands 200 mil wide, opposite faces of 62 mil board | Zc = 41.05 ohm | p.643 |
| power lands 200 mil wide, same face, 62 mil apart | Zc = 155.7 ohm | p.643 |
| planes 5 mil apart, 25 mil effective current width | Zc = 28.6 ohm | p.643 |
| plane pair 100 in^2, 5 mil, eps_r 4.7 | ≈ 0.02 uF | p.643 |
| small dc motor, leads-to-frame impedance minimum | ≈ 1 ohm near 100 MHz | p.660 |
| decoupling example | 50 mA, 0.1 V droop, 1 ns -> 500 pF (495 pF exact form, R ≈ 100 ohm) | p.649–651 |
| parallel-cap experiment | 0.01 uF ∥ 100 pF, 0.25 in 22 AWG leads 0.25 in apart, loops 1/8 in apart: Llead = 11.48 nH, M = 2.046 nH, k = 0.178 | p.647 |
### 2.20 Table B.1 — skin depth of copper (sigma = 5.8e7 S/m)

| f | 60 Hz | 1 kHz | 10 kHz | 100 kHz | 1 MHz | 10 MHz | 100 MHz | 1 GHz |
|---|---|---|---|---|---|---|---|---|
| delta | 8.5 mm | 2.09 mm | 0.66 mm | 0.21 mm | 2.6 mils | 0.82 mils | 0.26 mils | 0.0823 mils |

Source: Table B.1 p.741 (1 mil = 2.54e-5 m; 100 MHz = 6.6 um).

### 2.21 Lossless-dielectric wave parameters (mu_r = 1)

| material | eps_r | eta (ohm) | v (m/s) | lambda | source |
|---|---|---|---|---|---|
| free space | 1 | 120*pi ≈ 377 | ≈ 3e8 | 1 m at 300 MHz; 1 cm at 30 GHz; 3107 mi at 60 Hz | §B.6.1 p.731 |
| glass-epoxy (FR4) | 4.7 | 173.9 | 1.38e8 | 13.8 cm at 1 GHz (beta = 45.41 rad/m) | Ex.B.11 p.732 |
| silicon | 12 | ≈ 109 | 8.66e7 | 8.66 cm at 1 GHz (beta = 72.55 rad/m) | Ex.B.11 p.732–733 |
| Teflon | 2.1 | 260 | 2.07e8 | 414 m at 500 kHz; 20.7 m at 10 MHz | Review Ex.B.12; Prob.B.6.1 |
| PVC | 3.5 | 202 | 1.6e8 | 16 m at 10 MHz | Prob.B.6.1 p.750 |
| Mylar | 5 | 169 | 1.34e8 | 13.4 m at 10 MHz | Prob.B.6.1 |
| polyurethane | 7 | 142 | 1.13e8 | 11.3 m at 10 MHz | Prob.B.6.1 |

Physical constants used throughout: eps0 ≅ (1/(36*pi))e-9 F/m, mu0 = 4*pi*1e-7 H/m, v0 ≅ 3e8 m/s (SPICEMTL.FOR uses 2.997925e8 m/s) — Eq.(B.41) p.720; p.795.

### 2.22 Conductor/dielectric parameters quoted in App.B

| medium | sigma (S/m) | eps_r | sigma/(omega*eps) | note | source |
|---|---|---|---|---|---|
| copper | 5.8e7 | 1 | 1.04e9 at 1 GHz | alpha = beta = 1.51e4 /m, eta = 3.69e-4∠45 deg ohm at 1 MHz | Ex.B.9, B.13, B.14 |
| seawater | 4 | 80–81 | 9e5 at 1 kHz | eta = 1.4∠45 deg ohm, alpha = 3.97 at 1 MHz | Review Ex.B.8, B.13, B.14 |
| dry soil | 1e-5 | 4 | = 1 at ≈ 45 kHz | displacement dominates above | Prob.B.2.12 |
| wet marshy soil | 1e-2 | 15 | — | eta = 28.05∠42.62 deg at 1 MHz | Prob.B.6.8 |

### 2.23 Appendix C field-solver outputs (per-unit-length matrices; regression anchors)

| program / case | L11 | L12 | L22 | C11 | C12 | C22 | C0 (no dielectric) | source |
|---|---|---|---|---|---|---|---|---|
| WIDESEP: 3-wire ribbon, bare, 28 AWG r = 7.5 mil, 50 mil pitch, center ref | 7.58848e-7 | 2.40795e-7 | 7.58848e-7 | 1.63040e-11 | −5.17352e-12 | 1.63040e-11 | — | §C.1 p.756 |
| WIDESEP: 2 wires over ground, r = 16 mil, h = 2 cm, s = 2 cm | 9.17859e-7 | 1.60944e-7 | 9.17859e-7 | 1.25068e-11 | −2.19302e-12 | 1.25068e-11 | — | §C.1 p.757 |
| WIDESEP: 2 wires r = 7.5 mil at 15 mil radius in 30 mil shield, 0/180 deg | 2.19722e-7 | 4.46287e-8 | 2.19722e-7 | 5.28179e-11 | −1.07281e-11 | 5.28179e-11 | — | §C.1 p.758 |
| RIBBON: 3-wire, r = 7.5 mil, 10 mil insulation eps_r 3.5, 50 mil pitch, center ref, 20 Fourier terms | 7.48501e-7 | 2.40801e-7 | 7.48501e-7 | 2.49819e-11 | −6.26613e-12 | 2.49819e-11 | 1.65812e-11 / −5.33434e-12 | §C.2 p.759–760 |
| PCB: 3 lands w = 15 mil, 45 mil edge gap, h = 47 mil, eps_r 4.7, outer land ref, 30 subsections | 1.38315e-6 | 6.91573e-7 | 1.10707e-6 | 2.96949e-11 | −2.02619e-11 | 4.05238e-11 | 1.16982e-11 / −7.30774e-12 / 1.46155e-11 | §C.3 p.760–761; §D.4.2 |
| STRPLINE: 2 lands w = 5 mil, 5 mil gap, planes 20 mil apart, eps_r 4.7 | 4.63055e-7 | 9.21843e-8 | 4.63054e-7 | 1.17594e-10 | −2.34105e-11 | 1.17594e-10 | 2.50201e-11 / −4.98097e-12 | §C.5 p.762–763 |
| MSTRP: 2 lands w = 100 mil, 100 mil gap, h = 62 mil, eps_r 4.7 | 3.35327e-7 | 3.71527e-8 | 3.35327e-7 | cG+cm = 115.511e-12 | cm = 4.92724e-12 | — | — | Prob.9.3.10 p.551 (the §C.4 listing reprints the STRPLINE output — book error) |

All in H/m and F/m (C12 entries are the negative mutual term). Note: the same PCB matrices are attributed in §9.3.3.2 and Review Ex.9.4 to w = s = 15 mil, but PCB.IN (§C.3) and §D.4.2 state a 45 mil edge-to-edge gap — treat the 45 mil geometry as the one that generated the numbers.

### 2.24 SPICE modal-model data (App.D)

| case | mode Z0 (ohm) | mode TD | reference | source |
|---|---|---|---|---|
| 2 wires over ground, 4.674 m (homogeneous) | 323.4158 / 226.9176 | 15.59 ns both | isolated wire Zc = 275.3516 ohm | §D.4.1 p.795 |
| 3 PCB lands, 25.4 cm (inhomogeneous) | 265.8983 / 109.6490 | 1.321285 / 1.410790 ns | two lands alone: Zc = 204.525 ohm, eps_r' = 2.6159, TD = 1.369 ns | §D.4.2 p.801 |
| lumped-Pi (SPICELPI) of the PCB case, 25.4 cm | L101 = 3.51320e-7 H, L102 = 2.81196e-7 H, K101 = 0.558877; per-end shunt C101 = C201 = 1.19799e-12 F, C102 = C202 = 2.57326e-12 F; mutual CM101 = CM201 = 2.57326e-12 F (each end carries half the total line capacitance) | — | element = per-unit-length value × 0.254 m (C split half per end) | §D.7 p.817–818 |

### 2.25 Tables D.5–D.8 — trapezoid Fourier magnitudes (one-sided, V) from SPICE .FOUR

| n | 100 MHz, 5 V, 50 %, tr = tf = 1 ns (D.5) | 50 MHz, 5 V, 50 %, tr = tf = 5 ns (D.6) | tr = 6 ns, tf = 5 ns (D.7) | tr = 7 ns, tf = 5 ns (D.8) |
|---|---|---|---|---|
| dc | 2.500006 | 2.500000 | 2.375000 | 2.250000 |
| 1 | 3.131 | 2.866 | 2.790 | 2.689 |
| 2 | 1.149e-5 | 5.594e-10 | 0.1759 | 0.3200 |
| 3 | 0.9108 | 0.3184 | 0.2107 | 0.1459 |
| 4 | 9.224e-6 | 5.550e-10 | 0.06204 | 0.08604 |
| 5 | 0.4053 | 0.1146 | 0.1154 | 0.07044 |
| 6 | 6.035e-6 | 1.191e-9 | 0.04587 | 0.05377 |
| 7 | 0.1673 | 0.05849 | 0.02619 | 0.05205 |
| 8 | 2.633e-6 | 8.294e-10 | 0.02510 | 0.01329 |
| 9 | 0.03865 | 0.03538 | 0.02628 | 0.02553 |

Source: Tables D.5–D.8 p.810–815. (The text labels Table D.7's case as "tr = 7 ns" once, but its PWL source and the example statement give tr = 6 ns.) Other .FOUR anchors: Table D.2 (0.25 Hz triangle-step example, dc 1.499969, c1 0.7547 ...), Tables D.3/D.4 (0.5 Hz square wave into RC, dc 0.5, c1 0.6366 → output c1 0.1930).

## 3. Mechanizable checks

Units: SI unless stated; dBuV/m = 20log10(E/1e-6 V/m); limits and margins in dB. "margin" is always the designer-supplied required headroom (the book gives no universal value). Every constant below was re-computed against the book's worked answers (53 anchors reproduced, see §8).

**CHECK-RE-DM** — differential-mode radiated emission of a go/return pair, per harmonic
- inputs: net, f (Hz), I_D (A, DM current amplitude at f), L (m, run length), s (m, go–return spacing), d (m, 3 or 10), E_lim (dBuV/m at f), margin (dB), eps_eff.
- formula: E = 1.316e-14 * I_D * f^2 * L * s / d (V/m); E_dB = 20log10(E/1e-6).
- pass: E_dB <= E_lim − margin for every harmonic. margin_actual = E_lim − E_dB.
- validity flags (report, do not pass silently): L > lambda0/3 (constant-current model stretched; PAUL-2028), s > lambda0/100, d < lambda0/(2*pi) (measurement in near field; PAUL-2098).
- note: DM emission risk concentrates above 1/(pi*tr) (upper RE band, > 200 MHz typical).
- source rows: PAUL-2011, 2012, 2013, 2014, 2028, 2098.

**CHECK-RE-CM** — common-mode radiated emission of a cable/land bundle, per harmonic
- inputs: f (Hz), I_net (A, total CM current as a clamp probe measures it) or I_C per wire, L (m), d (m), E_lim, margin.
- formula: E = 6.283e-7 * I_net * f * L / d (V/m) [= 1.257e-6 * I_C * f * L / d with I_C per wire of a pair].
- pass: E_dB <= E_lim − margin; equivalently I_net <= I_max = E_lim(V/m) * d / (6.283e-7 * f * L).
- shortcut: FCC/CISPR Class B, 1 m cable -> keep I_net < 5 uA (PAUL-2185); 30 MHz, 3 m -> 15.92 uA is exactly at 40 dBuV/m.
- note: CM risk concentrates between 1/(pi*tau) and 1/(pi*tr) (lower RE band, < 300 MHz typical); cable resonance flag if lambda/4 <= L <= lambda/2 at any clock harmonic (PAUL-2119).
- source rows: PAUL-2018, 2019, 2020, 2024, 2119, 2185.

**CHECK-CABLE-PROBE** — bench current-probe screen of each cable
- inputs: cable_id, L (m), f (MHz), Z_T (dBohm, flat band only), cable_loss (dB, probe-to-analyzer coax at f), V_SA (dBuV, analyzer reading), E_lim (dBuV/m), d (m), margin (dB).
- formula: V_max = E_lim + Z_T + 20log10(d) − 20log10(f_MHz) − 20log10(L) + 4.041 (dBuV at the probe terminals); V_probe = V_SA + cable_loss.
- pass: V_probe <= V_max − margin; margin_actual = V_max − V_probe. Reject the data point if f is outside the probe's flat-Z_T band or the probe is not 50 ohm terminated.
- source rows: PAUL-2023, 2025, 2026, 2029.

**CHECK-FIELD-PICKUP** — plane-wave pickup at the terminations of an electrically short two-conductor line
- inputs: incident E_i (V/m) or (P_T (W), G (abs), r (m)); f; L, s (m); c (F/m, line capacitance); RS, RL (ohm); k_H, k_E ∈ [0, 1] (fractions of H normal to loop, E transverse to line; worst case 1, 1); V_th (V, victim threshold/noise margin); margin (dB).
- formula: E_i = sqrt(60*P_T*G)/r; H = E_i/(120*pi); V_S = RS/(RS+RL)*j*omega*mu0*L*s*k_H*H − RS*RL/(RS+RL)*j*omega*c*L*s*k_E*E_i; V_L = −RL/(RS+RL)*j*omega*mu0*L*s*k_H*H − RS*RL/(RS+RL)*j*omega*c*L*s*k_E*E_i; worst case take |first term| + |second term|.
- pass: max(|V_S|, |V_L|) <= V_th * 10^(−margin/20).
- validity: L <= lambda/10 at f (model within 1 dB up to ≈ lambda0/5 in the book's test); terminations not near short/open; else require transmission-line model.
- source rows: PAUL-2035, 2036, 2037, 2038, 2039, 2040.

**CHECK-SHIELDED-CABLE-PICKUP** — voltage induced inside a shield by exterior shield current
- inputs: I_SH (A), L (m), RS, RL (ohm), shield type; solid: sigma, r_sh, t_sh; braid: B, W, theta_w, r_bw, sigma, m12 (H/m, optional); f; V_th, margin.
- formula: delta = 1/sqrt(pi*f*mu0*sigma); gamma = (1+j)/delta; solid Z_T = (1/(sigma*2*pi*r_sh*t_sh)) * gamma*t_sh/sinh(gamma*t_sh); braid Z_T = (1/(sigma*pi*r_bw^2*B*W*cos(theta_w))) * gamma*2*r_bw/sinh(gamma*2*r_bw) + j*omega*m12; V_S = RS/(RS+RL)*Z_T*I_SH*L; V_L = RL/(RS+RL)*Z_T*I_SH*L (magnitudes).
- pass: max(|V_S|, |V_L|) <= V_th * 10^(−margin/20). Fail outright if any pigtail termination is present on a cable that relies on this check (PAUL-2043).
- anchor: B = 16, W = 4, r_bw = 2.5 mil, 30 deg, 1 m -> r_dc = 24.6 mohm; 300/50 ohm, I_SH = 31.5 mA, 1 MHz -> 513 uV / 85.5 uV.
- source rows: PAUL-2043, 2044, 2045, 2046.

**CHECK-XTALK-FD** — near/far-end crosstalk of an electrically short three-conductor line
- inputs: lm (H/m), cm (F/m), L (m), r0 (ohm/m, reference-conductor resistance), RS, RL, RNE, RFE (ohm), f (Hz), v (m/s), budget (dB, max allowed |V/VS|).
- formula: Lm = lm*L, Cm = cm*L, R0 = r0*L; a = RNE/(RNE+RFE), b = RFE/(RNE+RFE), p = RNE*RFE/(RNE+RFE), g = 1/(RS+RL); NE = j*omega*(a*Lm*g + p*RL*Cm*g) + a*R0*g; FE = j*omega*(−b*Lm*g + p*RL*Cm*g) − b*R0*g.
- pass: 20log10|NE| <= budget and 20log10|FE| <= budget.
- also report: dominant mechanism (inductive if Lm/Cm > RFE*RL for NE, > RNE*RL for FE; homogeneous form RFE*RL/(ZCG*ZCR) < 1) and the matching fix (twisted pair / shield both ends above fSH for inductive; shield grounded >= 1 end or balanced pair for capacitive).
- validity: L <= v/(10*f); weak coupling; else use exact MTL/SPICE model (PAUL-2199).
- anchors: 4.737 m ribbon, 50 ohm: j7.61e-8*f + 9.21e-3; 20 cm microstrip M_NE = 1.06e-10 s (50 ohm).
- source rows: PAUL-2058–2064, 2189, 2199.

**CHECK-XTALK-TD** — peak crosstalk for trapezoidal signals
- inputs: coefficients from CHECK-XTALK-FD (M_NE = a*Lm*g + p*RL*Cm*g, M_FE = −b*Lm*g + p*RL*Cm*g, M_NE_CI = a*R0*g, M_FE_CI = −b*R0*g), ΔV (V), tr, tf (s), V_high (V), L (m), v or modal delays (s), V_NM (V, victim noise margin), margin (dB).
- formula: V_NE,pk = |M_NE|*ΔV/min(tr, tf) + |M_NE_CI|*V_high; V_FE,pk likewise; TD = L/v (use the longest modal delay for inhomogeneous lines).
- pass: V_pk <= V_NM * 10^(−margin/20) AND tr, tf >= 10*TD (report "marginal" for 4 <= tr/TD < 10, "invalid, use SPICE MTL" below 4).
- anchors: RS-232-like 2.5 V/400 ns on 4.737 m ribbon -> 75 mV (50 ohm), 96.4 mV (1 kohm); 2.5 V/50 ns on 20 cm microstrip -> 5.3 mV.
- source rows: PAUL-2066, 2067, 2068, 2201.

**CHECK-SHIELD-GROUNDING** — effect of a receptor/generator shield on crosstalk
- inputs: RSH (ohm, = rS*L), LSH (H, = lS*L), grounding (none/one end/both ends), pigtail length (cm), f, unshielded M_IND, M_CAP (s), budget.
- formula: fSH = RSH/(2*pi*LSH); SF = 1/(1 + j*f/fSH) if both ends else 1; shielded = j*omega*M_IND*SF + (0 if grounded at >= 1 end else j*omega*M_CAP); for two shields multiply two SF terms.
- pass: 20log10|shielded| <= budget. Flags: inductive-dominant circuit with one-end grounding (no benefit); f < fSH; pigtail > 0.5 cm (book's minimum without 360 deg bond; 8 cm cost up to 30 dB) — severity rises with length.
- source rows: PAUL-2071–2080.

**CHECK-SE-FARFIELD** — solid sheet shield vs plane wave
- inputs: material (sigma_r, mu_r from Table 10.1), t (m), f (Hz), SE_req (dB), margin (dB).
- formula: delta = 0.06609/sqrt(f*mu_r*sigma_r) (m); R = 168 + 10log10(sigma_r/(mu_r*f)); A = 8.686*t/delta; M = 20log10|1 − exp(−2t/delta)*exp(−j2t/delta)|; SE = R + A + M.
- pass: SE >= SE_req + margin at every f of interest.
- guards: for Mumetal/Superpermalloy use Table 10.1 mu_r only at <= 1 kHz and low field; above ≈ 20 kHz treat as cold-rolled steel (the book gives no numeric mu_r(f) — flag for data); reject the result if the enclosure has any untreated penetration (PAUL-2086).
- anchors: Cu R = 138 dB (1 kHz), 98 dB (10 MHz); 125 mil Al at 1 MHz A = 326 dB.
- source rows: PAUL-2090–2097; Table 10.1.

**CHECK-SE-NEARFIELD** — solid shield vs near-field electric or magnetic source
- inputs: as CHECK-SE-FARFIELD plus source type (E or H) and source-to-shield distance r (m).
- formula: near field if r < lambda0/(2*pi); R_E = 322 + 10log10(sigma_r/(mu_r*f^3*r^2)); R_H = 14.57 + 10log10(f*(r/2)^2*sigma_r/mu_r) (Olsen r -> r/2), clamp R_H >= 0; A and M as far field; SE = R + A + M.
- pass: SE >= SE_req + margin. Flag: H source with SE shortfall at low f -> requires flux diversion (high-mu or steel) or a shorted turn (not computable from this book).
- anchors: 20 mil steel, 5 cm: R_E = 188.02/158.02/128.02 dB at 10 k/100 k/1 MHz; R_H = 0/0/8.55 dB (unclamped −11.45/−1.45/8.55 with r, not r/2).
- source rows: PAUL-2098–2107.

**CHECK-APERTURE** — ventilation honeycomb and seams
- inputs: (a) per honeycomb: cell side d (m), depth l (m), f_max (Hz), SE_req (dB); (b) per seam/slot: longest unbroken length L_slot (m) between fasteners/gasket contacts, f_max.
- formula (a): fc = v0/(2d) = 1.5e8/d; alpha(f) = (2*pi/v0)*sqrt(fc^2 − f^2) (Np/m, exact form of Eq.10.54); SE(f) = 8.686*alpha*l (≈ 27.3*l/d for f << fc).
- pass (a): f_max < fc AND SE(f_max) >= SE_req + margin.
- formula/pass (b): f_res = v0/(2*L_slot); require f_res > f_max (no half-wave slot resonance in band). The book gives no slot-SE formula (Babinet argument only) — report L_slot/(lambda_min/2) as a risk ratio, never a dB value.
- anchors: 100 x 100 mil cells, 100 dB -> l = 9.3 mm, fc = 59 GHz.
- source rows: PAUL-2088, 2108, 2109, 2110.

**CHECK-DECOUPLING** — local decoupling capacitor value and effective band per IC
- inputs: I_step (A), tr (s), ΔV (V, allowed droop), V0 (V), R (ohm, discharge-path resistance; book example ≈ 100 ohm), C (F), L_loop (H, total cap-body-to-pin loop incl. lands and vias).
- formula: C_min = I_step*tr/ΔV (or C_min = tr/(R*ln(V0/(V0 − ΔV)))); f0 = 1/(2*pi*sqrt(L_loop*C)); BW = 1/tr.
- pass: C >= C_min AND f0 >= BW (book criterion; conf medium). If f0 < BW is unavoidable, require plane/distributed capacitance per PAUL-2152–2154 and report. Adding a smaller capacitor in parallel with equal L credits at most 6 dB above resonance (PAUL-2156).
- anchor: 50 mA, 0.1 V, 1 ns -> 500 pF (495 pF exact form).
- source rows: PAUL-2154–2157.

**CHECK-GROUND-BOUNCE** — inductive drop along a return (or supply) path
- inputs: return geometry (wire: l, rw; land: l, w) and separation d to its signal conductor; ΔI (A); tr (s); V_NM (V); margin (dB).
- formula: wire Lp = (mu0*l/(2*pi))*[ln(2l/rw) − 3/4] (use −1 for HF); land Lp = (mu0*l/(6*pi))*[3 ln(u + sqrt(u^2+1)) + u^2 + 1/u + 3u ln(1/u + sqrt(1/u^2+1)) − (u^2+1)^1.5/u], u = l/w (u > 10); Mp = (mu0*l/(2*pi))*[ln(l/d + sqrt(1 + l^2/d^2)) − sqrt(1 + d^2/l^2) + d/l]; V = (Lp − Mp)*ΔI/tr. Fallback without geometry: L = (15…30 nH/in)*length (use 30 for worst case).
- pass: V <= V_NM * 10^(−margin/20).
- anchor: 20 AWG, 3 in, 1/4 in spacing, 100 mA/10 ns -> 445 mV.
- source rows: PAUL-2117, 2126, 2130–2133.

**CHECK-RETURN-CONFINEMENT** — plane voids near high-speed traces
- inputs: trace height h over its reference plane (m); distance d from trace centerline to the nearest plane void/slot/split edge (m); required contained fraction p (design choice); crosses_split (bool).
- formula: fraction = (2/pi)*atan(d/h) (50 % at d = h, 71 % 2h, 88 % 5h, 94 % 10h).
- pass: crosses_split == false AND fraction >= p. (Use of the fraction as a keep-out rule is derived — conf medium.)
- source rows: PAUL-2135, 2136, 2159.

**CHECK-ELECTRICAL-SIZE** — model-selection and resonance gate
- inputs: structure/cable length L (m), eps_eff, f_max (Hz) and/or tr (s), clock f0 and harmonic list.
- formula: lambda = v0/(sqrt(eps_eff)*f); lumped OK iff L < lambda(f_max)/10 and tr >= 10*L*sqrt(eps_eff)/v0; resonance-risk harmonics: n*f0 with lambda/4 <= L <= lambda/2.
- pass: model choice matches (lumped only when OK); list flagged harmonics for CHECK-RE-CM.
- anchors: 2 m, eps_r 2.1 -> 10.35 MHz, 96.6 ns; 1.5 m cable -> 50–100 MHz.
- source rows: PAUL-2067, 2119, 2195, 2204.

**CHECK-ESD-CLEARANCE** — secondary-arc spacing
- inputs: per exposed metal part: bonded_to_chassis (bool), clearance to nearest electronics (mm), insulation medium.
- formula: required (air) = 10 mm if not bonded (25 kV / 30 kV/cm ≈ 1 cm), 1 mm if bonded (≈ 1500 V / 30 kV/cm per book); other media may be smaller only with their datasheet breakdown.
- pass: clearance >= required; additionally every exposed metal part should be bonded (PAUL-2175).
- source rows: PAUL-2169, 2173, 2175.

**CHECK-HYBRID-GROUND-CAP** — capacitor that grounds a shield/subsystem only at high frequency
- inputs: f_min (Hz) above which |Z| must be low, |Z|max (ohm), C (F), L_lead (H).
- formula: C_min = 1/(2*pi*f_min*|Z|max); f_SRF = 1/(2*pi*sqrt(L_lead*C)).
- pass: C >= C_min AND f_SRF above the highest frequency needing the ground. anchor: 1 ohm above 100 MHz -> 1.6 nF.
- source rows: PAUL-2143, 2155.

**CHECK-CE-FILTER-MARGIN** — conducted-emission margin by mode (dominant-effect method)
- inputs: per f (150 kHz–30 MHz): CM and DM components of the unfiltered LISN voltage (dBuV, from a CM/DM separator or model), filter insertion losses IL_CM(f), IL_DM(f) (dB; vendor data or Part-1 Ch.6 formulas), limit (dBuV, QP/AV), margin (dB).
- formula: V_CM' = CM − IL_CM, V_DM' = DM − IL_DM; LISN phase/neutral voltage magnitude <= 20log10(10^(V_CM'/20) + 10^(V_DM'/20)) (phase = 50*(I_C + I_D), neutral = 50*(I_C − I_D) with 50 ohm LISN legs — worst-case in-phase sum; derived, conf medium).
- pass: worst-case <= limit − margin at every f. Output the dominant mode per f and the element class to change: DM -> line-to-line (X) capacitors; CM -> line-to-ground (Y) capacitors, CM choke, or green-wire inductor (PAUL-2187). Changing a non-dominant-mode element is reported as "no expected improvement".
- source rows: PAUL-2186, 2187; Part-1 rows for LISN/filter formulas (Ch.6).

**CHECK-PINOUT-RETURNS** — connector/ribbon pin assignment
- inputs: ordered pin list per connector with net class (clock / high-speed / low-rate signal / return / power) and pitch (m); cable length.
- formula: for each signal, n = pitches to nearest return; DM emission penalty = 20log10(n) dB relative to adjacent return (E_D ∝ s).
- pass: clocks have returns on both sides (GSG); every high-speed signal has an adjacent return (n = 1); low-rate signals may share returns (GSSG); GSG returns bonded at both ends.
- anchor: 3 pitches vs 1 -> ≈ 10 dB (9.5 dB).
- source rows: PAUL-2017, 2138, 2139.

**CHECK-TWISTED-PAIR-FIT** — will twisting (or balancing) help?
- inputs: receptor terminations, pair termination (balanced/unbalanced), Zc of the circuits, NE/FE inductive and capacitive terms from CHECK-XTALK-FD.
- rule: unbalanced pair -> new crosstalk = capacitive term of full length + inductive term of one half-twist (odd count) — effective only if inductive dominated; balanced pair -> capacitive term removed, inductive of one half-twist remains; R <= ~3 ohm -> add ±40 dB twist-sensitivity uncertainty.
- pass: predicted post-fix crosstalk <= budget including the uncertainty.
- source rows: PAUL-2081–2085, 2189.

## 4. Verification procedures & plots

### VP-RE-1 Cable common-mode current screen (bench, no chamber) — §8.1.4 p.413–414, Fig.8.11
- Setup: clamp-on current probe (known Z_T, flat band; e.g. 15 dBohm 10–200 MHz) around the whole cable (net CM current), 50 ohm spectrum analyzer, known coax loss. Measure at several positions along the cable (Table 8.1 shows the maximum is not at the ends).
- Plot: x = frequency (MHz, log, 30 MHz to probe upper limit), y = V_SA (dBuV) measured vs limit line V_SA,max(f) = E_lim(f) + Z_T + 20log d − 20log f_MHz − 20log L + 4.041.
- Good: every harmonic below the limit line with the design margin; line steps with the FCC Class B bands 40/43.5/46 dBuV/m.
- Use before/after every fix (toroid, grounding strap — straps may increase CM current).

### VP-RE-2 Predicted radiated field from probe current — Eq.(8.27) p.416, Figs.8.15–8.17
- Plot: x = f (MHz, harmonics of the clock), y = E (dBuV/m) predicted = V_SA + cable loss − Z_T + 20log f_MHz + F_GP − 13.58 (1 m cable, 3 m) overlaid with measured chamber data and the regulatory limit.
- Good: predicted within ≈ 3 dB of measured; margin to limit >= design margin.

### VP-RE-3 DM vs CM dominance tests — §8.1.5 p.418–420
- (a) Remove the far-end load: DM current collapses; unchanged emission -> CM dominant.
- (b) Rotate board/cable 90 deg so the conductor plane faces the antenna edge-on: DM cancels; unchanged emission -> CM dominant.
- (c) Add ferrite toroid/CM choke: large drop (> 20 dB seen) -> CM dominant.
- Plot: x = f, y = E (dBuV/m) for baseline / load removed / rotated / toroid, same axes.

### VP-RE-4 Emission-envelope Bode sketch — §8.1.2, §8.1.3; Figs.8.4, 8.8
- Plot: x = log f, y = dB; trapezoid spectrum envelope (flat, −20 dB/dec above 1/(pi*tau), −40 dB/dec above 1/(pi*tr)) plus transfer function (+40 dB/dec DM, +20 dB/dec CM) = predicted envelope.
- Good: DM envelope peaks above 1/(pi*tr) (upper band, > 200 MHz); CM envelope flat between breakpoints (lower band, < 300 MHz).

### VP-RS-1 Plane-wave pickup of a short two-conductor line — §8.2.1 p.433–434, Fig.8.29
- Setup: parallel-plate TEM cell/antenna held at 1 V/m by a field-probe feedback loop; line placed midway, wave along the line axis.
- Plot: x = f (log, 1 MHz upward), y = |V_term| (dBV); model line rises +20 dB/decade.
- Good: measured within 1 dB of model up to ≈ 40 MHz for a 1.5 m line (line is lambda0/10 at 20 MHz, lambda0/5 at 40 MHz); beyond, standing waves -> use transmission-line model.
### VP-XT-1 Frequency-domain crosstalk transfer ratio — §9.4.1, Figs.9.26–9.28, 9.30, 9.32
- Setup: drive generator circuit with swept sinusoid (tracking generator / VNA), measure |V_NE/VS| and |V_FE/VS|; data at 1, 1.5, 2, 2.5, 3, 4, 5, 6, 7, 8, 9 per decade.
- Plot: x = f (log), y = 20log10|V/VS| (dB). Overlay model: common-impedance floor (flat, M_CI), then +20 dB/decade line 2*pi*f*(M_IND + M_CAP), resonances where L > ~lambda/10.
- Sweep/corners: at least two load values (low R << Zc and high R >> Zc) to separate inductive and capacitive coupling (and extract Lm, Cm from Eq.(9.76)).
- Good: model within 3 dB up to L ≈ lambda0/6 (ribbon), within 1 dB to 250 MHz (microstrip, 50 ohm).

### VP-XT-2 Time-domain crosstalk — §9.4.2, Figs.9.34, 9.38–9.41
- Setup: trapezoidal pulse train with tr > 10*TD; scope at near and far end.
- Plot: x = time, y = V_NE(t), V_FE(t) overlaid on VS(t). Expect pulses during transitions of height M*ΔV/tr plus a common-impedance offset M_CI*VS during the flat top.
- Good: peak within the predicted value (e.g. 75 mV predicted vs measured, 5.3 vs 5.5 mV).

### VP-XT-3 Shield-grounding matrix — §9.5.3, Figs.9.50, 9.51
- Configurations: OO, SO, OS, SS (open/short at each end); loads R = 50 ohm and 1 kohm.
- Plot: x = f (log, 100 Hz–10 MHz), y = |V_NE/VS| (dB) for all four; mark fSH = RSH/(2*pi*LSH).
- Good: capacitive term vanishes for SO/OS/SS; SS flattens above fSH; rise above ~100 kHz flags pigtail coupling.

### VP-XT-4 Pigtail-length sweep — §9.5.4, Figs.9.54–9.56
- Same line with pigtails 0.5 / 3 / 8 cm at both ends, shield SS; plot NEXT vs f. Good: short pigtails keep the flat plateau; long pigtails show +20 dB/decade takeover (up to 30 dB worse > 1 MHz).

### VP-XT-5 Single wire vs straight pair vs twisted pair — §9.6.3, Figs.9.73–9.78
- Loads 1 kohm / 50 ohm / 1 ohm; plot NEXT vs f for the three receptor configurations; for low R also rotate the far end (odd/even half-twists) and plot min/max envelope.
- Good: TWP reduction only where inductive coupling dominated; expect up to 40 dB twist sensitivity for R = 1–3 ohm.
### VP-SH-1 Shielding effectiveness vs frequency — §10.2.2.4, Figs.10.8, 10.9, 10.11
- Plot: x = f (log, 10 Hz–1 GHz), y = dB; curves R (plane wave), R_e(r), R_m(r) for the design source distance, A, M, and total SE = R + A + M, with the required SE line.
- Corners: source type (plane wave / electric near field / magnetic near field), min and max source distance, material mu_r(f) derated above ~1 kHz for high-mu alloys.
- Good: total SE >= requirement at every frequency; note the low-frequency magnetic case where R_m ≈ 0 and A is small (needs flux diversion or shorted turn).

### VP-SH-2 Aperture / honeycomb check — §10.5
- Plot: x = f, y = SE_aperture (dB) for waveguide-below-cutoff cells (27.3*l/d, valid f << fc,10) and a vertical marker at every seam/slot resonance f = c/(2*L_slot).
- Good: no slot or seam half-wave resonance inside the RE band; honeycomb SE >= requirement.

### VP-GND-1 Ground bounce / return-path inductance — §11.2.3, Figs.11.10, 11.17
- Sim (SPICE): driver edge into C_LOAD with return path modeled by partial inductances (Lp − Mp); plot V_GND(t) and supply-pin voltage vs time.
- Good: ground bounce and rail droop below the logic noise-margin budget (book examples: 0.45 V for 75 nH, 6 mA/1 ns).

### VP-DEC-1 Decoupling impedance — §11.3.5, Figs.11.45–11.47
- Sim/measure: |Z(f)| of each decoupling network including total lead/land inductance and mutual inductance, 10–500 MHz (or to 1/tr).
- Plot: x = f (log), y = |Z| (ohm), mark self-resonance f0 = 1/(2*pi*sqrt(L*C)) and anti-resonances of parallel capacitors.
- Good: |Z| below target over the band up to 1/tr; no anti-resonance peak at clock harmonics; expect only ≈ 6 dB gain from adding a small capacitor in parallel.

### VP-ESD-1 ESD immunity pre-test — §8.2 Ex.8.9, §11.4.8
- Setup: product on metal table, indirect (table) and direct discharges, personnel and furniture waveforms; rerun with all cables except the power cord removed to locate entry points.
- Record: upset/lock-up/damage per discharge point and level; verify watchdog recovery.
- Good: no damage; upsets self-recover; board orientation and plane spacing per PAUL-2041/2182.

### VP-DIAG-1 Dominant-effect diagnosis — §11.5, §11.5.1
- CE: split LISN data into CM and DM with a separator; plot both vs f (150 kHz–30 MHz) with the limit; change X-caps where DM dominates, Y-caps/CM choke/green-wire inductor where CM dominates.
- RE: current-probe every cable (target < 5 uA CM on 1 m), E/H near-field probes and FET-probe pin spectra to localize; log each fix and its measured delta.
### VP-SIM-1 Exact multiconductor-line crosstalk in SPICE — App.D §D.4, Figs.D.25–D.33
- Flow: 2-D field solve for L, C (and C0) -> modal decomposition (TV, TI) -> subcircuit of lossless T-lines + controlled sources -> attach RS, RL, RNE, RFE.
- Plots: (a) x = time (0–200 ns), y = V_NE(t), V_FE(t) with the source pulse; (b) x = f (log, 1 kHz–1 GHz, 50 pts/decade), y = 20log10|V_NE/V_S| and |V_FE/V_S|.
- Good: matches measurement (book: 95 mV vs 94 mV peak); low-frequency +20 dB/decade region equals the inductive–capacitive model (−86.22 vs −86 dB at 1 kHz).
- Limitation: lossless model — add reference-conductor resistance (or use a lossy TL model) to capture the common-impedance floor below ≈ 100 kHz.

### VP-SIM-2 Lumped-Pi vs exact line — App.D §D.3, Figs.D.23, D.24, D.33
- Overlay 1-, 2- and 5-section lumped-Pi predictions on the exact model vs f; good = agreement wherever the line is electrically short (L < lambda/10); divergence marks where more sections or the exact model are needed.

### VP-SIM-3 Harmonic content of clock/data waveforms — App.D §D.5, Tables D.5–D.8
- Setup: .TRAN over several periods with a fine step ceiling, then .FOUR at f0 on the node of interest (steady state).
- Plot: x = harmonic number / f, y = amplitude (dBuV), overlaid with the equal-edge spectral bound; add cases tr ≠ tf.
- Good: equal-edge 50 % case shows no even harmonics; unequal edges show the even harmonics and odd-harmonic deviations listed in PAUL-2203 — feed the simulated amplitudes, not the bound, into CHECK-RE-DM/CM when edges are asymmetric.

### VP-MEAS-1 Probe-loop discipline — App.B Ex.B.6
- Before any low-level measurement near switching magnetics, rotate/reroute the probe ground lead and confirm the reading does not change; a change indicates flux pickup in the lead loop.

## 5. Pitfalls, failure modes, review checklist

- Assuming CM current is negligible because it is small: 8 uA CM radiates like 20 mA DM on a 1 m cable at 30 MHz (68 dB). — §8.1.1 p.399
- Assuming a compact, symmetric, battery-powered PCB has no CM current: 6 in. lands radiated ≈ 20 dB above the DM prediction. — §8.1.5 p.419–420
- Applying 1/d distance scaling of emissions in the near field (below ~30 MHz at 10 m, the product is not in the far field). — Ch.8 intro p.397
- Using the Hertzian/constant-current emission models for conductors longer than ~lambda0/3 or for near-field measurement points. — §8.1.2 p.402; §8.1.5 p.418
- Reading a current probe with a load other than its calibration load (usually 50 ohm) invalidates Z_T. — §8.1.4 p.411
- Forgetting coax loss between probe and analyzer (add it to the analyzer reading). — §8.1.5 p.416
- Using a current probe beyond its flat Z_T band (example probe usable only to ≈ 100 MHz). — §8.1.4 p.414
- Clock oscillator far from its load (long, large-area clock loop). — §8.1.2 p.405
- Connector pinout that separates a signal from its return by several pins (loop area x N). — §8.1.2 p.405, Fig.8.6
- Adding grounding straps as a "fix" without measuring: they may increase cable CM current. — §8.1.4 p.413
- Vertically mounted PCB at the rear of a product on an ESD table: E field transverse to land pairs -> lock-ups. — §8.2 Ex.8.9 p.431
- Pigtail shield terminations (breaks in the shield). — §8.2.2 p.435
- Using the simple pickup model with extreme (near-short/near-open) terminations or electrically long lines. — §8.2 p.427, §8.2.1 p.434
- Using an outer ribbon wire as the common return instead of the wire between generator and receptor (+7 to +9 dB NEXT). — §9.4.1.2 Review Ex.9.2/9.3 p.487
- Using wide-separation (uniform-charge) formulas for wires closer than ~5 radii (up to 236 % capacitance error). — §9.3.3 p.463
- Ignoring wire insulation when computing capacitance (eps_r' 1.5–1.7 for ribbon). — Table 9.1 p.471
- Applying the lumped inductive–capacitive crosstalk model to pulses with tr < 10*TD or lines longer than ~lambda/10. — §9.4.2 p.494
- Ignoring common-impedance (return-conductor resistance) coupling: sets a flat floor at low frequency (e.g. −40.7 dB with 0.92 ohm return and 50 ohm loads). — §9.4.1.1 p.483–485
- Grounding a shield at one end and expecting magnetic (inductive) crosstalk reduction. — §9.5.2 p.505–509
- Expecting any shield to reduce inductive coupling below fSH = RSH/(2*pi*LSH) (≈ 1–6 kHz typical). — §9.5.2, 9.5.3; Prob.9.5.2 (970 Hz)
- Long shield pigtails (> 5 in. common) — dominate crosstalk above ~100 kHz. — §9.5.4 p.518–519
- Expecting a twisted pair to cut crosstalk in high-impedance unbalanced circuits (capacitive floor unaffected). — §9.6.2 p.538
- Relying on a precise crosstalk prediction for very low-impedance twisted-pair circuits (±40 dB twist sensitivity). — §9.6.3 p.546
- Untreated cable penetration of a shielded enclosure. — Ch.10 intro p.557
- Cable shield pigtailed to logic ground (shield becomes a monopole, CM resonances 50–100 MHz for 1.5 m cables). — Ch.10 intro p.558
- Assuming a narrow seam/slot does not leak because little light passes. — Ch.10 intro p.561
- Expecting a thin copper shield to stop low-frequency magnetic fields (R_m and A both small; use steel/mu-metal diversion or shorted turns). — §10.3.3, §10.4 p.580–581
- Using catalogue mu_r of Mumetal above ~1 kHz or at high field (saturation); using Mumetal for 20–100 kHz SMPS shields (steel is as good and cheaper). — §10.4 p.582–583
- Single long ventilation slot instead of many small holes; gaskets placed outside the lid screws. — §10.5 p.585–587
- Suppression capacitor used above its self-resonant frequency. — §11.1.1 p.597
- Treating a long wire/land as a short circuit at RE frequencies (1 ft of 20 AWG ≈ 113–226 ohm at 100 MHz). — §11.1.1 p.599
- Power-entry filter with input and output lands looped close together, or phase wire run to a remote switch before the filter. — §11.1.1 p.600–601; §11.4.2 p.656
- Assuming the power cord carries only 60 Hz (clock harmonics found on it). — §11.1.2 p.603
- Treating reset or other "slow" pins as quiet and routing them long. — §11.1.2 p.603; §11.3.2 p.638
- Returns (grounds) grouped together on connector pins far from their signals. — §11.2.5 p.626–628
- Slots or splits in the ground plane under traces; split analog/digital ground planes with traces crossing the split. — §11.2.4 p.625; §11.3.7 p.653
- Daisy-chained single-point grounds; "multipoint" grounding to a long thin land. — §11.2.6 p.629–630
- Motor-driver return currents sharing the digital ground net. — §11.2.6 p.630–631
- Autoplacing/autorouting the highest-speed parts; clock or CPU next to an off-board connector. — §11.3.1, 11.3.2 p.637–638
- RC filter upstream of a buffer that restores the fast edges. — §11.3.2 p.638
- I/O connectors on more than one board edge. — §11.3.3 p.639; §11.4.4 p.659
- Decoupling capacitor with short leads but long connecting lands (total loop inductance counts). — §11.3.5 p.644–645
- Believing a small capacitor in parallel with a large one fixes lead inductance (≈ 6 dB only, plus anti-resonance). — §11.3.5 p.646–648
- Several PCBs connected by cables where one board would do; buffering a fanned-out signal on the sending board. — §11.4.3 p.657–658
- Two PCBs mounted vertically close together; internal flat cable laid over a clock module. — §11.4.4, 11.4.5 p.659; Figs.11.1, 11.2
- Isolated (unbonded) metal decals/nameplates near electronics (< 1 cm): secondary arcs. — §11.4.8 p.666
- CM choke bypassed by the cable-shield pigtail or ground wire. — §11.4.8 p.669
- ESD diversion capacitor grounded far from the cable entry; shunt capacitor across a low-impedance input. — §11.4.8 p.669–670
- Unbounded firmware wait states, no watchdog, floating unused inputs, edge-triggered inputs. — §11.4.8 p.671–672
- Changing a filter element that addresses the non-dominant mode and concluding "EMC is black magic". — §11.5.1 p.674–680
- Mixing peak and RMS phasors in power-density calculations (the 1/2 factor applies only to peak values). — App.B §B.5 p.726
- Using Kirchhoff/lumped models for structures longer than lambda/10 at the highest frequency of interest. — App.B §B.7.1.1 p.742
- Oscilloscope/voltmeter lead loops enclosing changing flux (reading depends on lead routing). — App.B Ex.B.6 p.705
- SPICE: zero-valued elements, floating nodes, no dc path to ground, writing "3F" for 3 farads (F = femto), default .TRAN step (end_time/50) on transmission-line circuits. — App.D §D.1 p.767–772
- Taking .FOUR results from a run that has not reached steady state. — App.D §D.5 p.805–806
- Assuming equal rise/fall times when bounding harmonics of real drivers (even harmonics appear; individual odd harmonics can change > 2x). — App.D Ex.D.11 p.813–815
- Trusting a lossless SPICE MTL model at low frequency (misses common-impedance coupling). — App.D §D.4.2 p.803
- Applying the lumped crosstalk model when tr is comparable to the line delay (12.5 ns vs 15.6 ns). — App.D Review Ex.D.1 p.795
- Reusing PCB.FOR matrices with the §9.3.3.2 geometry (s = 15 mil) — the solver input was a 45 mil gap. — App.C §C.3; App.D §D.4.2

## 6. Standards referenced

| standard / body | edition / year | clause / table | what it governs (as used in this range) | page |
|---|---|---|---|---|
| FCC rules for digital devices (Class A / Class B) | rule published 1979 | Class B RE limits 40 / 43.5 / 46 dBuV/m for 30–88 / 88–216 / 216–960 MHz at 3 m; Class A measured at 10 m | Radiated-emission compliance targets used in all Ch.8 examples and the current-probe screening chart | p.397, p.413–414; App.E p.824 |
| CISPR 22 (EN 55022) | — | Class A and Class B measured at 10 m | RE limits; ≈ 5 uA CM on a 1 m cable can fail Class B | p.397; p.674 |
| CISPR (IEC special committee) | formed 1933 (IEC, Paris); reconvened 1946 (London) | — | Origin of measurement-equipment and limit recommendations followed by FCC | App.E p.824 |
| MIL-STD-461 | in force from early 1960s | emissions and susceptibility requirements | Military EMI control incl. injected-signal susceptibility tests | App.E p.824 |
| "Industry standard" ESD susceptibility test | — | product on metal table, ESD gun discharged to the table | Indirect-discharge immunity (field coupling to PCB loops) | §8.2 Ex.8.9 p.431 |
| ESD immunity test with personnel and furniture discharges (Calcavecchio & Pratt, IEEE EMC Symp. 1986, ref. [23]) | 1986 | — | Personnel (overdamped) and furniture (underdamped) discharge simulation | §11.4.8 p.663 |
| Low-frequency radiated magnetic-field emission limits (agencies not named) | — | loop-antenna measurement below 30 MHz | Switching-transformer leakage flux emissions (shorted-turn bands) | §10.4 p.583–584 |
| Ground-plane reflection correction factors (book Table 7.1, Part 1) | — | horizontal polarization, 1 m height: 0.78 dB at 100 MHz, 4.4 dB at 180 MHz | Converting probe current to predicted field (Eq.8.27) | p.416–418 |
| Index-only mentions (content lies in Part 1): CISPR 12, CISPR 25, CISPR 32, MIL-STD-461E (CE102, RE102, CS101, CS114, RS103), RTCA DO-160G, SAE J551, SAE J1113, UL, ANSI | — | — | Not read in this range | Index p.827–833 |

## 7. Process / lifecycle guidance

| stage | activity | deliverable | exit criterion | source |
|---|---|---|---|---|
| Concept / packaging | Assign an experienced EMC engineer; decide enclosure (metal vs plastic, coatings), number/orientation/spacing of PCBs, power-entry and switch location, internal cable routes with packaging team | EMC configuration review (board placement, cable routes, filter at entry, enclosure treatment) | Packaging not frozen until EMC review signed; no PCBs vertical and close together; no cables over noisy modules; filter at power entry | Ch.11 intro p.593–596; §11.4.1–11.4.5 p.655–659 |
| Schematic / BOM | Rank every part by signal speed f0*I0/tr; add "plan B" provisions: 0 ohm series R + unpopulated C on clocks, alternative pads for transformer Faraday-shield ground, through-hole pads bridged by 0 ohm resistors for DIP toroids/RC packs at each cable exit; buffer inter-board signals at the receiving board | Speed-ranked parts spreadsheet; plan-B pad list | Every cable exit and clock has a BOM-only fix path | §11.3.1 p.637; Ch.11 intro p.596; §11.4.1 p.656; §11.4.3 p.658 |
| Layout | Manual placement of fastest parts first (no autoplace/autoroute for them); clock at its load, returns both sides; connectors on one edge with quiet ground to chassis; ground plane or grid, no split grounds; decoupling at every IC with minimal loop; GSG pinouts | Layout + per-net plots (+5 V/ground and each critical net) | Loop-area review of power and signal nets completed before prototypes | §11.3.1–11.3.7 p.637–655 |
| Prototype pre-compliance | Current-probe every cable (target < 5 uA CM on 1 m), FET-probe all ASIC/CPU pins, E/H near-field probes, CM/DM split of CE, ESD pre-test (with/without cables), log every fix and result | Diagnostic log; per-cable CM current table; CE CM/DM plot | All cables below CM-current target and dominant mechanisms identified before booking the chamber | §11.5 p.672–674; §11.5.1 p.674–680 |
| Compliance test | Semi-anechoic chamber RE, LISN CE, ESD immunity | Test report | Limits met with margin | §8.1.5 p.414–416; §11.5 p.674 |
| Fix / iterate | Apply fixes to the dominant contributor only (X- vs Y-cap vs CM choke; shunt cap vs CM choke; twisted pair vs shield grounding); prefer BOM-only plan-B changes | Updated BOM and log | Measured reduction of the dominant term; no re-layout | §11.5.1 p.674–680; Ch.11 intro p.596 |

## 8. Coverage log

Source file: `refs-text/Introduction_to_Electromagnetic_Compatibility_Clayton_R_Paul.txt` (34,101 lines). This extraction's range: lines 17000–34101.

| file lines | content | treatment |
|---|---|---|
| 1–1200 | front matter, TOC | read for orientation only |
| 17000–17077 | end of §7.6.3 multipath (ground-reflection factor algebra) | read; no design rule (algebra only) |
| 17078–17286 | §7.7 biconical and log-periodic antennas, §7.8 antenna modeling | read; rules PAUL-2001…2005 |
| 17287–17839 | Ch.7 problems | skipped (exercises); one answer used as an anchor (Prob.7.7.3) |
| 17840–17855 | Ch.7 references, Ch.8 intro | read |
| 17856–19594 | Ch.8 radiated emissions and susceptibility (§8.1–8.2.2) | read fully; PAUL-2006…2046 |
| 19595–19650 | Ch.8 problems, references | skimmed; answers used only as numeric anchors (Probs.8.2.8, 8.2.9) |
| 19651–24123 | Ch.9 crosstalk (§9.1–9.6.4) | read fully; MoM derivations (§9.3.3) read but not transcribed beyond usable results; PAUL-2047…2085 |
| 24124–24220 | Ch.9 problems, references | skimmed; answers used as anchors (Probs.9.3.5–9.3.11, 9.4.3, 9.4.10, 9.5.2) |
| 24221–25701 | Ch.10 shielding (§10.1–10.5) | read fully; PAUL-2086…2111 |
| 25702–25734 | Ch.10 problems, references | read; answers used as anchors (Probs.10.1.2, 10.2.1–10.2.4, 10.3.1–10.3.2, 10.5.1) |
| 25735–27196 | Ch.11 system design for EMC (§11.1–11.5.1) incl. ESD and diagnostics | read fully; PAUL-2112…2189 |
| 27197–27531 | App.A phasor method | read; pure circuit math — no rules |
| 27532–30923 | App.B EM field equations and waves | read; vector-calculus review (§B.1) and Maxwell derivations skimmed as pure math; engineering content extracted: PAUL-2190…2196, Tables 2.20–2.22 |
| 30924–31575 | App.C FORTRAN PUL codes | read; input formats not transcribed; outputs kept as solver regression anchors (Table 2.23) |
| 31576–33895 | App.D SPICE/LTSPICE tutorial, lumped and exact MTL models, Fourier analysis, SPICEMTL/SPICELPI | read; GUI click-steps not transcribed; PAUL-2197…2204, Tables 2.24–2.25 |
| 33896–33918 | App.D problems, references | read; Prob.D.6.1 used as anchor |
| 33919–33950 | App.E history of EMC and failure anecdotes | read; anecdotes skipped per brief; regulatory history in §6 |
| 33951–34101 | index | scanned for standards names only (§6) |

Totals: 204 design rules (PAUL-2001…PAUL-2204), 25 numeric tables/blocks (§2.1–2.25), 20 mechanizable checks (§3), 20 verification procedures (§4), 59 pitfall/checklist items (§5). Absolute-value bars inside table cells are written abs(x) so every table row keeps its column count.

Numeric verification: 53 transcribed formulas/constants were re-computed in a scratch script against the book's own worked answers (Ex.8.1–8.7, 9.1–9.3, §9.4.1.2, §9.5.3, Probs.8.2.8/9.4.3/10.2.4/10.3.1–2/10.5.1/D.6.1, Review Ex.10.1–10.6, 11.1, 11.3–11.7, Table 11.1, App.B examples) — all reproduced within 2 % (plane-capacitance example within 6 %, which the book itself calls "approximately").

Limitations and source defects found:
- Equations are OCR-garbled in the text layer; each formula here was reconstructed from the prose and confirmed against the book's numeric examples (list above). Rows marked `medium` are derived or graph-based.
- Figures are absent (captions only): Fig.8.11 probe chart, Fig.8.31 Z_T/r_dc vs t/delta, Figs.9.26–9.60 crosstalk plots, Figs.10.8–10.13 SE and permeability curves, Fig.11.21b current distribution, Figs.11.46–11.47 decoupling plots, Fig.D.23/D.24 lumped-Pi comparisons. Numbers quoted from them come only from prose.
- Eq.(11.27b) prints the anti-resonance as 1/(2*pi*sqrt(2*L*C1)) while stating f3 = sqrt(2)*f2; circuit analysis gives f2 = 1/(2*pi*sqrt(2*L*C2)) for C1 >> C2 (PAUL-2156 flags this, conf medium).
- Table 11.1 prints 0.9 for d/h = 10; the formula (2/pi)*atan(10) gives 0.937 (the printed "94 %" agrees with the formula).
- The same PCB.FOR matrices are attributed to w = s = 15 mil (§9.3.3.2, Review Ex.9.4) and to a 45 mil edge gap (§C.3 input, §D.4.2) — the solver input (45 mil) is taken as authoritative.
- §C.4 (MSTRP.FOR) output listing duplicates the STRPLINE output and a wrong geometry echo; MSTRP values were taken from Prob.9.3.10 instead.
- Table D.7's case is labelled "tr = 7 ns" once in the prose but the PWL source and example statement give tr = 6 ns.
- Braid parameters in §9.5.3 are OCR-scrambled; W = 4 wires/belt was confirmed by reproducing RSH = 89.8 mohm (and Prob.8.2.8's 24.6 mohm/m).
- The book gives no numeric slot/aperture shielding formula (Babinet argument only) and no universal design margins; the corresponding checks report risk ratios or require a user-supplied margin rather than inventing values.

Chapters NOT read in this extraction: Ch.1–6 and Ch.7 up to mid-§7.6.3 (file lines 1–17000) — assigned to the Part-1 agent (includes Ch.6 LISN, power-supply filter formulas and the CM/DM separator of §6.2.4 that CHECK-CE-FILTER-MARGIN references).
