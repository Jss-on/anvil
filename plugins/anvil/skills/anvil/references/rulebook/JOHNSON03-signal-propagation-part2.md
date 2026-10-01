# High-Speed Signal Propagation: Advanced Black Magic (Johnson & Graham) — Anvil rulebook (Part 2: Ch. 5.5.5.2 end–13, Appendices)

## 0. Citation

H. Johnson and M. Graham, *High-Speed Signal Propagation: Advanced Black Magic*. Upper Saddle River, NJ, USA: Prentice Hall PTR (Pearson Education), 2003. ISBN 0-13-084408-X. (LC TK5103.15 .J64 2002.)

Chapters covered by THIS extraction (text lines 15400–30722 of 30722; printed pp. 358–748):
- Ch. 5 tail: §5.5.5.2 Via Crosstalk (from eq. 5.39) and §5.6 The Future of On-Chip Interconnections (pp. 358–361).
- Ch. 6 Differential Signaling (pp. 363–438), incl. LVDS (§6.13).
- Ch. 7 Generic Building-Cabling Standards (pp. 439–455).
- Ch. 8 100-Ohm Balanced Twisted-Pair Cabling (pp. 457–503).
- Ch. 9 150-Ohm STP-A Cabling (pp. 505–512).
- Ch. 10 Coaxial Cabling (pp. 513–535).
- Ch. 11 Fiber-Optic Cabling (pp. 537–578; design-usable numbers only).
- Ch. 12 Clock Distribution (pp. 579–672).
- Ch. 13 Time-Domain Simulation Tools and Methods (pp. 673–701).
- Collected References (pp. 703–709; standards extracted), collected Points to Remember (pp. 710–730; cross-checked against in-chapter boxes), Appendices A–E (pp. 731–748).

Chapters NOT read here: Front matter beyond the TOC, Ch. 1–4 and Ch. 5 up to §5.5.5.2 eq. 5.38 (assigned to the Part-1 agent, lines 1–15400); the Index (pp. 749–766, skipped as an index).

ID range of this part: JOHNSON03-2001 … JOHNSON03-2338 (four-digit ids because the part exceeds 99 rules).

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| JOHNSON03-2001 | crosstalk | Via-to-via crosstalk through a shared stripline cavity: peak victim voltage for a step aggressor | V_peak,step = L_M * (dV/Zc)/t_r (V); L_M = mutual inductance (H), dV = aggressor step amplitude (V), Zc = aggressor line impedance (ohm), t_r = rise time (s) | L_M, dV, Zc, t_r | vias traversing a common cavity between two reference planes; inductive coupling only | calc | p.358 eq.5.39 | high |
| JOHNSON03-2002 | crosstalk | Via-to-via crosstalk, sinusoidal aggressor of amplitude a | V_peak,sin = a * 2*pi*f * L_M / Zc (V) | a (V), f (Hz), L_M (H), Zc (ohm) | as JOHNSON03-2001 | calc | p.358 eq.5.40 | high |
| JOHNSON03-2003 | via | Effective series inductance of a signal via with a single return via (English units) | Lv = h*5.08*2*ln(s/r) (nH); h = separation between reference planes (in.), s = signal-via to return-via separation (in.), r = via radius (in.) (OCR shows "(2-ln(s/r))"; the product form reproduces the book's worked value 0.539 nH) | h, s, r (in.) | nonmagnetic substrate; plan-view geometry of Fig.5.37 | calc | p.358 Fig.5.37 | high |
| JOHNSON03-2004 | via | Worked via-inductance regression case: 20-mil pad, 5-mil gap between pads, h = 0.025 in., r = 0.003 in., s = 0.025 in. | Lv = 0.539 nH (3.38 ohm at 1 GHz); L_MA = 0.357 nH (2.24 ohm); L_MB = 0.269 nH (1.69 ohm); L_MC = 0.181 nH (1.14 ohm at 1 GHz) | as stated | use to regression-test CHECK-via-mutual-inductance | calc | p.357-358 example | high |
| JOHNSON03-2005 | crosstalk | Mutual inductance between two signal vias with a nearby shared return via (case A) | L_MA = h*5.08*ln(2s/r) (nH), dims in inches | h, s, r (in.) | Fig.5.37 geometry | calc | p.358 Fig.5.37 | high |
| JOHNSON03-2006 | crosstalk | Mutual inductance, equidistant shared return via (case B) | L_MB = h*5.08*ln(s/r) (nH), dims in inches | h, s, r (in.) | Fig.5.38 geometry | calc | p.359 Fig.5.38 | high |
| JOHNSON03-2007 | crosstalk | Mutual inductance, shared return via placed between the two signals (case C) | L_MC = h*5.08*ln(s/(2r)) (nH), dims in inches (s1 = s3 = s, s2 = 2s in eq.5.38) | h, s, r (in.) | Fig.5.38 geometry | calc | p.359 Fig.5.38; p.357 eq.5.38 | high |
| JOHNSON03-2008 | crosstalk | Rule of thumb: a shared mutual impedance of 1 ohm between two 50-ohm circuits induces ~2 % crosstalk; in both-ends-terminated nets half the inductive crosstalk goes to each end; crosstalk from all aggressors sharing one return via aggregates | 2*pi*f*L_M = 1 ohm -> ~2 % (50-ohm circuits) | f, L_M | inductive via coupling | calc | p.359 | high |
| JOHNSON03-2009 | transmission-line | Simple CMOS totem-pole switching is adequate for pcb links up to ~1 GHz at 25 cm (10 in.); faster than 1 GHz or longer than 25 cm requires impedance control, terminations, crosstalk and loss management, multilevel signaling / adaptive equalization | f <= 1 GHz AND length <= 25 cm -> simple drivers OK | data rate/frequency, trace length | pcb traces, circa-2003 technology | review | p.361 §5.6 | high |
| JOHNSON03-2010 | power | Current to charge input capacitance on every edge (CMOS inputs are not zero-current) | I = C*dV/dt; 1 mA charges 1 pF by 1 V in 1 ns | C (F), dV (V), dt (s) | every electrical input | calc | p.364 fn.43 | high |
| JOHNSON03-2011 | grounding | Reference-pin noise on a single-ended IC is equivalent to the same noise on every receiver input and must be subtracted from the logic-family noise margin | V_noise,ref (e.g. 100 mV) adds directly to input noise; NM = min(VOL-VIL, VOH-VIH) must exceed total noise | VOL, VIL, VOH, VIH, reference noise (V) | single-ended receivers (TTL/CMOS ground-referenced; PECL Vcc-referenced) | calc | p.366, fn.45 | high |
| JOHNSON03-2012 | grounding | Single-ended signaling: limit voltage differences within the reference system to a small fraction of the signal amplitude; reference impedance must absorb all returning currents without objectionable drops | V_ref_diff << V_signal (fraction not numerically stated) | ground-shift budget, signal swing | single-ended links | review | p.366 | low |
| JOHNSON03-2013 | grounding | Know which rail each single-ended family uses as its reference: TTL and most high-speed CMOS = ground; ECL on ground/-5.2 V = ground; PECL (positive supply + ground) = positive supply | reference rail per family | logic family | noise budgeting | inspect | p.368 | high |
| JOHNSON03-2014 | return-path | Two-wire (and differential) signaling works only when stray returning signal current through parasitic couplings to chassis/planes is insignificant; differential signaling (complementary signal on the second wire) makes stray currents cancel | net stray current through z1 + z2 ~ 0 requires z1 = z2 and complementary drive | layout symmetry, drive balance | high-speed two-wire links | review | p.370-371 | medium |
| JOHNSON03-2015 | emc | Common-mode rejection in twisted-pair cable = weak coupling (thick jacket keeps objects away) + precise balance (tight twist); on pcb with solid planes CM rejection comes only from precise balance: equal trace height, width, thickness and length | equal h, w, t, length on both legs | pair geometry | pcb differential pairs over solid planes | inspect | p.372-373 | high |
| JOHNSON03-2016 | emc | Untwisting one wire of an active LAN pair and taping ~2 in. of it against chassis metal makes the product fail FCC/EN radiated limits -- keep pair untwist and wire-to-chassis asymmetry to a minimum at the connector/magnetics | untwist/asymmetric exposure of ~2 in. is enough to fail | untwist length at termination | UTP LAN ports | inspect | p.372 | high |
| JOHNSON03-2017 | crosstalk | Typical coupling ratio between the two traces of a pcb differential pair lies in 20 % to 50 %; tight coupling is NOT required for differential benefits -- any reasonable spacing works if drive is balanced and both traces have symmetric impedance to the planes | k_pair = 0.2 .. 0.5 (typical) | s, h, w | solid-plane pcb | review | p.373 | high |
| JOHNSON03-2018 | transmission-line | Differential / common-mode decomposition | d = a - b; c = (a + b)/2; a = c + d/2; b = c - d/2 (V or A) | a, b = wire voltages vs common reference | two-wire systems; same for currents | calc | p.374-375 eq.6.2-6.5 | high |
| JOHNSON03-2019 | transmission-line | Odd/even decomposition and its relation to differential/common | o = (a - b)/2; e = (a + b)/2; a = e + o; b = e - o; o = d/2; e = c; odd p-p range y -> differential p-p = 2y | a, b | two-wire systems | calc | p.375-376 eq.6.6-6.11 | high |
| JOHNSON03-2020 | emc | Limit the AC common-mode component of a differential signal; intercabinet cabling is extremely sensitive to high-frequency CM current (radiates efficiently from unshielded cable) | V_cm,ac << V_diff (qualitative) | CM amplitude | intercabinet links | measure | p.375 | low |
| JOHNSON03-2021 | transmission-line | Stripline (homogeneous dielectric): differential and common-mode velocities are equal; microstrip (inhomogeneous): slightly different -- impact small unless mode conversion occurs at both ends of a long line | v_odd = v_even (stripline); v_odd != v_even (microstrip) | configuration | long lines with double mode conversion | review | p.376-377 §6.5 | high |
| JOHNSON03-2022 | emc | Common-mode balance = CM (AC) amplitude / differential amplitude, in dB: 1 part in 10,000 (-80 dB) is exceptionally good; differential logic transmitters may achieve only -30 dB or even -20 dB; even/odd ratio is 6 dB lower than CM/diff ratio | balance_dB = 20*log10(V_cm,ac/V_diff); good <= -80 dB; logic parts ~ -30..-20 dB | V_cm,ac, V_diff | differential transmitters and channels | measure | p.377 §6.6 | high |
| JOHNSON03-2023 | components | Never violate a receiver's common-mode input range, not even briefly (behavior outside range may be normal, inverted, saturated with slow recovery, latched until power cycle, or permanent failure) | V_min,cm <= each input voltage <= V_max,cm at all times incl. transients | receiver CM range, worst-case ground shift + CM noise | all differential/digital receivers | calc | p.378 §6.7 | high |
| JOHNSON03-2024 | components | Convert power-supply or common-mode noise into equivalent differential input noise using CMRR; sum all equivalent input noise for SNR/jitter | V_eq,diff = V_noise * 10^(CMRR_dB/20); e.g. CMRR = -50 dB, 100 mV Vcc ripple -> 0.3 mV | CMRR (dB), noise (V) | linear amplifiers; digital receiver CM-range specs do not give this | calc | p.378 §6.7 | high |
| JOHNSON03-2025 | emc | Capacitive imbalance between the two legs of a differential output injects common-mode current; 2 pF imbalance with 10BASE-T (2 V p-p per wire, 25 ns switching) gives 160 uA, enough to violate emissions regulations on an exposed cable | i_cm,peak = dC * dV/dt; (2 pF)*(2 V/25 ns) = 160 uA | dC (F), dV (V), t_switch (s) | LAN transformer outputs; any balanced port | calc | p.379-380 eq.6.12 | high |
| JOHNSON03-2026 | transmission-line | Differential impedance of two matched, uncoupled lines is twice the single-line impedance; traces separated by more than 4x the trace height h are usually treated as uncoupled | Zdiff = 2*Z0 when s > 4*h | Z0, s, h | pcb traces | calc | p.380-381 eq.6.13, fn.48 | high |
| JOHNSON03-2027 | transmission-line | Even/odd/common/differential impedance relations (Fig.6.11 lumped model: Z1 = line-to-ground incl. neighbour, Z2 = coupling impedance) | Z_even = Z1; Z_odd = Z1 || (Z2/2); Z_common = Z_even/2; Z_diff = 2*Z_odd; always Z_odd < Z0_uncoupled < Z_even and Z_common > Z_diff/4 | Z1, Z2 or solver Z_odd/Z_even | coupled pair | calc | p.381-383 | high |
| JOHNSON03-2028 | transmission-line | Coupling between parallel pcb traces always decreases differential (odd-mode) impedance; when routing tightly coupled pairs, narrow the traces within the coupled region to hold Zdiff | Z_odd(coupled) < Z0(uncoupled) | s, w | coupled pcb pairs | calc | p.383 §6.9.1-6.9.2 | high |
| JOHNSON03-2029 | termination | Reflection coefficient formula applies to differential lines using differential impedances; e.g. 100-ohm cat-5 joined to 120-ohm cat-4 UTP gives r = 0.09 | r = (Z2 - Z1)/(Z2 + Z1) with Z = differential impedances | Z1, Z2 (ohm) | balanced lines; unbalance adds 4x4 mode-coupling matrix (frequency dependent) | calc | p.384 eq.6.14-6.15 | high |
| JOHNSON03-2030 | transmission-line | Requirements for a high-speed differential pair in a solid-plane pcb: (1) complementary voltages, (2) complementary currents (=> equal characteristic impedances), (3) equal impedance of each trace to the surrounding reference system (gnd/Vcc planes), (4) equal propagation delay | Z0(P) = Z0(N); Z_to_ref(P) = Z_to_ref(N); t_pd(P) = t_pd(N) | pair geometry, lengths | differential microstrip, edge-coupled stripline, broadside-coupled stripline | inspect | p.385 §6.10 | high |
| JOHNSON03-2031 | transmission-line | Compute differential trace impedance with a 2-D field solver (inputs: trace width, height, separation, thickness, configuration, dielectric constant, plus soldermask overlay); distrust closed-form calculators that are not field solvers | Zdiff = f(w, h, s, t, config, er, soldermask) via 2-D solver | stackup + geometry | all pcb differential structures | sim | p.385-386 §6.10, §6.10.1 | high |
| JOHNSON03-2032 | fab | Require the fab shop to place differential-impedance test coupons on every panel and test each one | coupon Zdiff within spec on each panel | fab notes | controlled-impedance differential boards | measure | p.389 §6.10.1 | high |
| JOHNSON03-2033 | transmission-line | Microstrip/stripline impedance monotonic rules: moving a trace closer to its reference plane or widening it lowers Z; moving away or narrowing raises Z; in offset stripline the nearest plane dominates (centered: both equal) | dZ/dh > 0; dZ/dw < 0 | h, w | single-ended and each leg of a pair | review | p.387 §6.10.1 | high |
| JOHNSON03-2034 | transmission-line | Differential impedance falls monotonically with decreasing edge-to-edge spacing; widely separated pair Zdiff = 2*Z_single; tightly spaced pair Zdiff < 2*Z_single; to hold Zdiff constant a reduction in spacing must be accompanied by a reduction in width (or increase in height) | dZdiff/ds > 0; Zdiff(s -> inf) = 2*Z0 | s, w, h | pcb pairs | review | p.387-388 §6.10.1 | high |
| JOHNSON03-2035 | transmission-line | Sanity screen for proposed 100-ohm diff microstrip: if the single-ended impedance of one trace is already < 50 ohm (e.g. 16-mil trace on 5-mil FR-4), no spacing can reach 100 ohm differential; reject such geometries | Z0_single < Zdiff_target/2 -> infeasible | Z0_single, Zdiff target | edge-coupled pairs | calc | p.388 §6.10.1 | high |
| JOHNSON03-2036 | transmission-line | 100-ohm differential edge-coupled microstrip candidate geometries on 5-mil FR-4 (er = 4.3 at 1 GHz, 1-oz finished Cu, 0.5-mil soldermask er = 3.3): h/w/s (mil) = 5/8/30, 5/7/11, 5/6/7, 5/5/5 | see Table 6.1 (R_AC, alpha_R, er_eff) | h, w, s | solver data accuracy ~ +/-2 % (resistance) | calc | p.389 Table 6.1 | high |
| JOHNSON03-2037 | transmission-line | Propagation velocity and delay from effective permittivity | v0 = 1/tp = c/sqrt(er_eff); c = 2.998e8 m/s | er_eff | quasi-TEM lines | calc | p.389 Table 6.1 note 3 | high |
| JOHNSON03-2038 | stackup | A thicker soldermask slightly reduces the finished propagation velocity (and the vendor will adjust width to hold Z) -- specify soldermask type/thickness in the impedance stackup | soldermask baseline in Table 6.1: 12.7 um (0.5 mil), er = 3.3 | soldermask spec | outer-layer microstrips | review | p.389 §6.10.1 | high |
| JOHNSON03-2039 | transmission-line | Edge-coupled stripline: below ~9 mil separation (b = 24, h = 6, t = 0.68 mil, er = 4.3) coupling is significant and Zdiff depends on both width and spacing; beyond ~4*h separation (24 mil here) traces hardly interact and Zdiff depends mostly on width | s < 9 mil -> coupled; s > 4*h -> uncoupled | s, h | Fig.6.13 stackup (graph) | calc | p.389-390 Fig.6.13 | medium |
| JOHNSON03-2040 | transmission-line | Author's default layout rule for edge-coupled stripline pairs: set separation ~4*h (Zdiff reduction < 6 %, ignorable) so all stripline traces share one width; allow the pair to separate locally around obstacles | s ~ 4*h -> dZdiff < 6 % | s, h | unless pressed for space | inspect | p.390 §6.10.2 | high |
| JOHNSON03-2041 | timing | Intrapair length match: equalize the two elements of a pair to within 1/20 of the rise time -> common-mode signal contributed by trace skew < 2.5 % of the single-ended amplitude | skew_intrapair <= t_r/20 -> V_cm/V_se < 2.5 % | t_r (s), intrapair delay (s) | pcb differential pairs | calc | p.390 §6.10.2 | high |
| JOHNSON03-2042 | transmission-line | Tight coupling forces narrower traces, which exacerbates skin-effect loss; trace width is the most important determiner of skin-effect loss (other factors secondary) | alpha_R ~ decreases with w (Tables 6.1-6.3) | w | 100-ohm pairs | review | p.390-391 §6.10.2 | high |
| JOHNSON03-2043 | transmission-line | Proximity factor of differential pcb traces: 100-150 ohm edge-coupled pairs kp typically 2.5-3.5 (example edge-coupled stripline kp = 3.08); broadside-coupled 75-135 ohm pairs kp 2.5-3.5 (example 2.73); kp = actual AC resistance / resistance of uniform current around the periphery of one signal conductor (skin depth accounted) | kp = 2.5 .. 3.5 | geometry | at 1 GHz, copper | calc | p.391 §6.10.2; p.402 fn.51 | high |
| JOHNSON03-2044 | transmission-line | Exact geometric scaling of a stripline pair: with k = b1/b2, multiply h, w, s and t by k -> Zdiff unchanged, skin-effect resistance and skin-effect attenuation (at 1 GHz) both divide by k; leaving t fixed gives small (second-order) error | Z(k*geom) = Z(geom); R_skin' = R_skin/k; alpha_R' = alpha_R/k | table row, b1 | any field-solver result | calc | p.392 §6.10.2 | high |
| JOHNSON03-2045 | transmission-line | Interpolate skin-loss tables linearly between rows to meet a loss budget; worked case b = 20, h = 7, w = 5, s = 7 mil -> 0.0929 dB/in vs budget 0.1 dB/in: fraction = (0.1-0.0929)/(0.1089-0.0929) = 58 % -> w = 4.42, s = 5.96 mil; or scale all dims by 0.0929/0.1 = 93 % -> b = 18.6, h = 6.51, w = 4.65, s = 6.51 mil; then tweak s in a 2-D solver for exact Z and choose interpair pitch for crosstalk | fraction = (budget - a1)/(a2 - a1); x = x1 + fraction*(x2 - x1) | table rows, loss budget (dB/in) | 1 GHz skin loss only | calc | p.393 eq.6.16-6.19 | high |
| JOHNSON03-2046 | transmission-line | Skin-effect attenuation of a 100-ohm differential pair from tabulated loop resistance (consistent with Tables 6.1-6.3) | alpha_R (dB/m) = 8.686 * R_AC(ohm/m) / (2 * 100 ohm) | R_AC (ohm/m, pair loop) | derived by checking table rows (e.g. 137.8 ohm/m -> 5.99 dB/m) | calc | p.389, 394 Tables 6.1-6.2 | medium |
| JOHNSON03-2047 | transmission-line | Tightly coupling two 50-ohm traces lowers Zdiff from 100 ohm to perhaps 70-90 ohm; separating a thinned, tightly coupled pair (e.g. around a via) reverts local Zdiff to 2*Z0 of the skinny traces (> 100 ohm) | Zdiff,coupled ~ 70..90 ohm (2 x 50-ohm traces) | Z0, s | edge-coupled pairs | calc | p.397 §6.10.3 | high |
| JOHNSON03-2048 | transmission-line | Do not place pair traces so close that the width required to hold Zdiff becomes unmanufacturable | w_required >= fab minimum | fab min width | tightly coupled pairs | inspect | p.397 fn.49 | high |
| JOHNSON03-2049 | transmission-line | Short mismatched section in a differential line (pair split around obstacle, BGA neck-down): reflection coefficient | r ~ (td/(2*tr)) * (Z2/Zdiff - Zdiff/Z2); e.g. Z2/Zdiff = 122/100 -> r ~ 0.200*td/tr; model: C2 ~ td/Z2, L2 ~ td*Z2, LN = Zdiff^2*C2, L_EXCESS = L2 - LN, r ~ L_EXCESS/(2*tr*Zdiff) | td = section delay (s), tr (s), Z2, Zdiff (ohm) | td << tr; same formula (negative r) when Z2 < Zdiff; nearby via-pad capacitance adds to C2 | calc | p.398-399 eq.6.20-6.24 | high |
| JOHNSON03-2050 | transmission-line | Accuracy limit of the short-discontinuity approximation eq.6.23: td/tr < 1/6 -> a couple of percent; td/tr = 1/3 -> ~20 %; td/tr = 1/2 -> totally erroneous (use a time-domain simulator) | valid if td/tr <= 1/6 | td, tr | lumped discontinuity models | calc | p.399 §6.10.3 | high |
| JOHNSON03-2051 | transmission-line | If a local pair split degrades the signal too much, thicken the traces in the separated region to match the impedance of the thinner, coupled traces elsewhere | Z(separated) = Zdiff target | local widths | pair splits | inspect | p.399 §6.10.3 | high |
| JOHNSON03-2052 | transmission-line | Broadside-coupled stripline: Zdiff is maximized, and least sensitive to width and height, when the trace height (to trace centerline) is 25 % of the interplane separation (6 mil for b = 24 mil); this point also maximizes width (minimum skin loss) but maximizes crosstalk between adjacent broadside pairs; avoid heights much different from 25 % | h_center = 0.25*b | b, h | b = 24 mil, t = 0.68 mil, er = 4.3 (Fig.6.18, graph) | calc | p.399-400 Fig.6.18 | high |
| JOHNSON03-2053 | return-path | Broadside pair entering/leaving inner layers: the trace whose return must hop planes (via a stitching via or bypass cap) gets extra delay; worked case stitching via 4 mm from signal via -> (4 mm)*2*(7 ps/mm) = 56 ps per transition, 112 ps if at both ends; place several plane-to-plane connections near every point where pairs dive into over/under configuration, change layers, and emerge | t_extra ~ 2*d_stitch*t_pd per transition | d_stitch (mm), t_pd (ps/mm) | also applies to through-hole vias (OCR prints '4 ps/mm'; the 56 ps result implies 7 ps/mm) | calc | p.401 Fig.6.19 example | medium |
| JOHNSON03-2054 | timing | If an intrapair skew near 100 ps matters, either place plane-stitching vias closer to the signal vias or do not use the broadside configuration | skew_budget ~ 100 ps threshold | skew budget | broadside pairs | review | p.402 §6.10.4 | high |
| JOHNSON03-2055 | pdn | Broadside pairs pick up any AC voltage difference between their two reference planes as differential noise: use the same supply voltage (preferably ground) on both planes and stitch them together with numerous vias on a tight grid | plane_top = plane_bottom (same net); dense stitching grid | stackup plane nets | broadside-coupled pairs (edge-coupled pairs are immune) | inspect | p.402 §6.10.4 | high |
| JOHNSON03-2056 | stackup | Broadside pairs are sensitive to dielectric thickness tolerance and layer-to-layer registration: e.g. 5-mil trace-to-plane separations with +/-1 mil tolerance can give 4 mil vs 6 mil, destroying symmetry; edge-coupled pairs (same layer, same etch) are inherently more symmetric | dielectric tol +/-1 mil on 5 mil -> 4/6 mil asymmetry | layer tolerances | broadside vs edge-coupled choice | review | p.402 §6.10.4 | high |
| JOHNSON03-2057 | dfm | Use broadside-coupled pairs only when routing density demands it (single-track routing between connector pins vs double-track for edge-coupled) | prefer edge-coupled | routing constraints | backplane pin fields | review | p.402 §6.10.4 | high |
| JOHNSON03-2058 | transmission-line | Tables 6.2/6.3 may be linearly interpolated along b for intermediate interplane spacings | linear interpolation in b | b | 100-ohm stripline pairs, 1 GHz | calc | p.403 §6.10.4 | high |
| JOHNSON03-2059 | connectors | Matching pcb traces to balanced cable: tightness of coupling is irrelevant, Zdiff must match the cable; use two 50-ohm traces for 100-ohm twisted pair (ISO 11801 cat 3/5/5e/6/7) and two 75-ohm traces for 150-ohm STP (IBM Type 1) | Zdiff,pcb = Zdiff,cable (100 or 150 ohm) | cable type | LAN/balanced-cable interfaces | calc | p.404 §6.11.1 | high |
| JOHNSON03-2060 | emc | LAN transmit interface: low-pass filter (L1-C1, L2-C2) to truncate power above signal bandwidth, transformer + common-mode choke to limit CM content; after the CM choke route the two traces symmetrically with equal impedance to all nearby grounded objects (tight coupling not required) | CM radiation from UTP is orders of magnitude more efficient than DM radiation | interface schematic, layout | 10/100BASE-T-type interfaces (Fig.6.21) | inspect | p.404-405 §6.11.1 | high |
| JOHNSON03-2061 | timing | Ground-bounce cancellation requires the two complementary signals to arrive at the receiver with equal delays from the driver (tight coupling not required) | intrapair skew ~ 0 | intrapair delay | differential receivers | calc | p.405 §6.11.2 | high |
| JOHNSON03-2062 | emc | Theoretical differential-mode far-field cancellation of a microstrip pair vs single-ended | a = 20*log10( abs( 1 - (r/(r+s))*exp(-j*2*pi*s/lambda) ) ) (dB); r = distance to receiver (m), s = trace separation (m), lambda = free-space wavelength of highest frequency (m); s = 0.5 mm at 1 GHz, r = 10 m -> ~ -40 dB | s, f_max, r | antenna in plane of board, broadside direction, r = 10 m (FCC class B) | calc | p.405-406 Fig.6.22 | high |
| JOHNSON03-2063 | emc | Total radiation improvement of a differential pair is capped by driver common-mode balance: imbalance of 1 part in 100 (1 % CM) -> <= 40 dB even at zero spacing; LVDS (balance no better than 1 part in 16) -> <= 24 dB (factor 16) | max_improvement_dB = -20*log10(CM_fraction) | driver CM balance | digital differential drivers | calc | p.406-407 §6.11.3 | high |
| JOHNSON03-2064 | emc | Ordinary differential digital traces need not be closer than 0.5 mm (0.020 in.) for any EMI purpose (common-mode radiation dominates) | s_EMI = 0.5 mm is sufficient | s | digital pcb pairs | inspect | p.407 §6.11.3 | high |
| JOHNSON03-2065 | connectors | Differential signaling cancels connector ground shift (within CMRR) and reduces connector crosstalk; the achievable cancellation depends on pin assignment within the connector, not on pcb trace coupling; an aggressor closer to one leg is not cancelled | pin-map review | connector pin assignment | mated-connector links | review | p.407 §6.11.4 | high |
| JOHNSON03-2066 | connectors | Open-pin-field connector pin assignment: put both elements of each pair in the same row (same pin length and bends); for isolation between asynchronous pairs/clocks ensure no wire of one pair is adjacent to a wire of another pair (=> at least as many grounds as signal pins); synchronous buses that can wait for crosstalk to settle may skip isolation | grounds >= signal pins for isolated pairs | pinout | high-density pin connectors | inspect | p.408 §6.11.4.1 | high |
| JOHNSON03-2067 | connectors | Connectors with solid ground shields between columns may give different pin lengths to the two elements of a pair; cancel any known connector intrapair skew elsewhere in the layout | skew_conn + skew_layout ~ 0 | connector skew data | shielded backplane connectors | calc | p.408 fn.52 | high |
| JOHNSON03-2068 | connectors | Measure connector differential impedance with a crude TDR: two RG-174 50-ohm coax driving a 100-ohm differential source through mated test boards (solid copper, drilled, no traces), far side terminated with 100 ohm (1/8-W axial resistor is fine); reference shot with the terminator directly across the coax; positive bump = connector Z too high, negative = too low; use the system's real risetime (not 35-ps edges) | bump polarity vs reference | TDR waveforms | open-pin-field connectors | measure | p.408-409 §6.11.4.1 | high |
| JOHNSON03-2069 | connectors | Connector impedance adjustment: more ground pins around the pair lowers Z, moving signal pins away from ground raises Z; added lumped capacitance (larger-than-normal via pads) lowers effective Z only when connector through-delay < 1/6 of signal risetime (connector acts as a lumped inductor) | big-pad fix valid if t_conn < t_r/6 | t_conn, t_r | connectors too high in impedance | calc | p.409 §6.11.4.1 | high |
| JOHNSON03-2070 | timing | Receiver switching-time uncertainty (clock skew contribution) from threshold window and input slew | t_UNCERTAINTY = (V_IH - V_IL)/(dv/dt); dv/dt ~ dV_swing/t_10-90 of driver; 5-V TTL example V_IL = 0.8 V, V_IH = 2.4 V (as printed) | V_IH, V_IL (V), dV (V), t_10-90 (s) | use driver risetime if driver/receiver similar technology and package not a significant impediment; receiver package slows the on-die edge | calc | p.409 eq.6.25, fn.53 | high |
| JOHNSON03-2071 | timing | Differential receiver threshold window: effective V_IH - V_IL spread = 2 x maximum input offset magnitude (offset polarity unpredictable); figure of merit = offset spread / p-p differential output swing (single-ended: (V_IH - V_IL)/p-p swing); p-p differential swing = 2 x p-p swing of either wire | window_diff = 2*abs(V_offset,max); FOM = window/V_pp,diff | V_offset,max (V), swing (V) | differential clock/data receivers | calc | p.410 §6.11.5, fn.55 | high |
| JOHNSON03-2072 | timing | Intrapair arrival difference effect: if the two halves arrive at t1 and t2 separated by a small fraction (~1/10) of the edge, the receiver switches near (t1 + t2)/2; if separation ~ one risetime, switching anywhere between t1 and t2; author matches pair delays within 1/20 of risetime; traces need equal delay, not the same path | t_switch ~ (t1 + t2)/2 when abs(t2 - t1) <= t_r/10; target abs(t2 - t1) <= t_r/20 | t1, t2, t_r | differential clocks | calc | p.410 §6.11.5 | high |
| JOHNSON03-2073 | timing | Clock skew contributed by a receiver depends on input risetime, switching thresholds and (differential) intrapair arrival similarity -- not on trace spacing or geometry other than delay | review items: t_r, thresholds, intrapair skew | — | clock receivers | review | p.410 §6.11.5 | high |
| JOHNSON03-2074 | crosstalk | Local crosstalk onto a pair is not balanced: an aggressor twice as close to one leg couples ~4:1 more strongly to it, and the receiver cannot cancel it; enforce net-class keep-out spacing around sensitive (clock) pairs, bigger than normal spacing between clock and data signals | coupling ratio ~ (d_far/d_near)^2 (4:1 at 2:1 distance, as stated) | d_near, d_far | pcb pairs over solid planes | inspect | p.411 Fig.6.24 | high |
| JOHNSON03-2075 | crosstalk | Tight intrapair coupling gives only modest NEXT improvement: converting a 50-ohm single-ended aggressor to a 100-ohm diff pair gives < 2 dB; reducing intrapair separation 8 -> 4 mil gives ~4 dB more; increasing aggressor distance x is far more effective | dNEXT: < 2 dB (SE -> diff aggressor), ~4 dB (8 -> 4 mil intrapair) | x, intrapair s | stripline, planes 24 mil apart, traces 6 mil above lower plane, 1/2-oz Cu, er = 4.3 (Fig.6.25, graph) | calc | p.411-412 Fig.6.25 | medium |
| JOHNSON03-2076 | crosstalk | Splitting a single-ended victim into a differential pair centred on the old trace helps only if the pair's traces are extremely close (< 1/3 of the original aggressor-victim centreline separation); otherwise the near leg picks up more crosstalk than balance cancels -- increasing separation is denser than differential distribution for local crosstalk | s_pair < d_orig/3 for any benefit | s_pair, d_orig | pcb over solid ground plane | calc | p.413-414 §6.11.8 | high |
| JOHNSON03-2077 | timing | Differential clock distribution keeps its ground-bounce and connector ground-shift cancellation in multidrop (daisy-chain) as well as point-to-point configurations; differential is rarely worth it for wide parallel buses (doubles wire count) | — | topology | clock nets | review | p.413-414 §6.11.8 | high |
| JOHNSON03-2078 | termination | A single resistor across a pair (e.g. 120 ohm) terminates only the differential mode; common mode is unterminated (open) at that end | Z_cm,term = open for single-resistor | termination topology | differential ECL/any pair | review | p.414 §6.11.9 | high |
| JOHNSON03-2079 | termination | Single-resistor termination with intrapair skew dt creates common-mode reflection: crosstalk and reflection coefficients each 1/2, residual CM f(t) = (1/2)*(x(t) - x(t - dt)); for dt < t_10-90 the peak CM ~ (1/2)*dV*(dt/t_10-90) | V_cm,peak ~ 0.5*dV*dt/t_10-90 | dV (V), dt (s), t_10-90 (s) | single-resistor end termination | calc | p.415-416 Fig.6.26 | high |
| JOHNSON03-2080 | termination | Common-mode resonance: with a low-impedance (e.g. ECL) driver and CM-open far end, CM noise bounces indefinitely; if the trace delay equals 1/4 of the clock period the CM artifacts of each edge add cycle after cycle (magnified CM noise and emissions) | avoid t_line ~ T_clk/4 when CM unterminated; better: terminate CM | t_line, T_clk | long differential links | calc | p.416 §6.11.9 | high |
| JOHNSON03-2081 | termination | Every long differential link needs (1) a good differential termination at one end and (2) a reasonable common-mode termination at one end; an ECL driver gives no CM termination at the source, so provide it at the load; a source-terminated driver works with a single-resistor load termination | DM term: Zdiff; CM term at one end | driver type, termination topology | long differential links | inspect | p.416 §6.11.9 | high |
| JOHNSON03-2082 | termination | Preferred two-resistor differential + CM terminator: R2 = R3 = Zdiff/2 in series across the pair, centre tap to a capacitor (to VT) sized only to hold its charge during the skew interval; four-resistor split termination (e.g. ECL 160 ohm to -5.2 V and 100 ohm to ground per line) also terminates both modes | R2 = R3 = Zdiff/2; C holds charge over dt | Zdiff, dt | ECL sources with pull-downs need no special VT on the capacitor | calc | p.414-416 Fig.6.26 | high |
| JOHNSON03-2083 | return-path | Differential pair crossing a reference-plane gap: return currents make a U-turn; the U-turn zone acts as a series inductor ~10 nH for 0.100 in. trace-to-trace separation and 0.100 in. plane gap -> in a 100-ohm diff system a low-pass time constant of 100 ps (unnoticeable for tr > 1 ns, harmful at ~100 ps risetimes) | tau = L_U/Zdiff; L_U ~ 10 nH at 0.1 in. x 0.1 in. | gap width, pair spacing, Zdiff, tr | pairs crossing split planes | calc | p.418 §6.11.10 | high |
| JOHNSON03-2084 | return-path | Counteract the U-turn by shrinking both the plane gap and the intrapair spacing, or provide continuous return paths (stitching) adjacent to each trace from plane to plane; if planes are at different DC voltages, a bypass capacitor next to each trace helps; U-turn crosstalk couples into every pair crossing the same gap and EMI/crosstalk scale with U-turn size | stitch via/cap adjacent to each trace at every plane transition | plane splits crossed by pairs | differential pairs over split planes | inspect | p.418 §6.11.10 | high |
| JOHNSON03-2085 | timing | Budget pair-turn skew only against driver skew: if driver intrapair skew is unspecified assume it is at least 10 % of the signal risetime (digital differential drivers are poorly balanced) | skew_driver >= 0.1*t_r (assumed) | t_r | digital differential drivers | calc | p.419 §6.11.11 | high |
| JOHNSON03-2086 | timing | Aggregate component+layout skew must stay below (CM balance ratio) x risetime to avoid amplifying CM: 100BASE-TX balanced to 1 part in 1000, t_r ~ 8 ns (~94 in. in air) -> skew budget ~ 0.094 in. ~ 0.1 in.; 2.5 Gb/s driver, t_r = 200 ps, output skew no better than ~20 ps -> budget ~20 ps | skew_budget = balance_ratio * t_r (100BASE-TX: 8 ns/1000) | balance ratio, t_r | cables, connectors, board layout | calc | p.419 §6.11.11 | high |
| JOHNSON03-2087 | timing | Extra length on the outside trace of an edge-coupled pair per 90 deg corner: square 2p, 45-deg chamfer 4*p*tan(22.5 deg) = 1.65p, round (pi/2)*p = 1.57p (p = centre-to-centre pitch); chamfering/rounding does not eliminate skew; e.g. p = 20 mil, 160 ps/in. -> 3.2 ps per p -> 5.0-6.4 ps per corner | dL_90 = 2p / 1.65p / 1.57p; skew = dL*t_pd | p (in.), t_pd (ps/in.), corner count & handedness | edge-coupled pairs | calc | p.419-420 Fig.6.28 | high |
| JOHNSON03-2088 | timing | Mitigate turn skew: reduce pair pitch p; orient ICs so the pair leaves the driver heading the same direction it enters the receiver (equal numbers of left/right turns, net zero skew unless spiral); a pair exiting east and entering west needs two extra same-handed turns | net_turns = n_left - n_right -> 0 | floorplan orientation | differential floorplanning | inspect | p.420-421 Fig.6.29 | high |
| JOHNSON03-2089 | timing | "Buy time" at BGA/pin-field entry: when ball pitch exceeds intrapair pitch, offset the pair centreline half a position on entry/exit to add delay to one leg; make skew adjustments near the end with the poorer termination | offset = 0.5*ball pitch (qualitative) | ball pitch, intrapair pitch | BGA, connector, via fields | inspect | p.421 §6.11.12 | medium |
| JOHNSON03-2090 | cables | Multi-pair twisted cable relies on different twist rates per pair to null interpair crosstalk (flip one pair -> crosstalk reverses; flip both -> same polarity); crosstalk specs give only worst-case pair-to-pair values, no pair hierarchy is standardized | — | cable spec | balanced cabling | review | p.422-423 §6.12 | high |
| JOHNSON03-2091 | cables | Quad cable: better interpair crosstalk inside the jacket (if well built) but worse coupling to outside objects; twisted pair is better for radiation and common-mode rejection; ribbon twisted-pair can use one twist pitch only because wires are varnished in a rigid geometry (coupling reverses every 90 deg) | — | cable type | intercabinet cabling | review | p.423-424 §6.12, §6.12.1 | high |
| JOHNSON03-2092 | grounding | Differential UTP links need no direct ground connection between ends provided the ground potential difference stays inside the receiver common-mode range; high-frequency single-ended intercabinet links need a low-inductance controlled-impedance ground (e.g. coax shield) -- the green-wire ground is inadequate | abs(V_gnd,A - V_gnd,B) + V_cm,signal within receiver CM range | ground shift estimate | intercabinet links | calc | p.424 §6.12.2 | high |
| JOHNSON03-2093 | compliance | Never introduce a metallic connection between frames powered by different AC power sources (ground-fault currents, GFI trips); if boxes must be connected, serve both from green-wire grounds at the same earth potential: same rack, daisy-chained power via convenience outlet, or same outlet/power strip; between rooms use differential, fiber or RF links | several volts can exist across a building; several amps may flow through an inter-domain bond | AC power domains of connected equipment | intercabinet metallic connections | review | p.425-426 §6.12.2 | high |
| JOHNSON03-2094 | emc | RF field absorbed by a cable becomes common-mode current; CM unterminated at both ends (plain transformer coupling) can resonate and amplify; imbalance in cable, connectors or circuitry converts CM to DM that the receiver takes as signal | i_common = sqrt(P/Z_common); P = received power (W), Z_common = CM impedance to earth incl. CM terminations (ohm) | P, Z_common | twisted-pair RFI | calc | p.426-427 §6.12.3 | high |
| JOHNSON03-2095 | emc | For best RF rejection: tightly twisted, well-balanced cable (twisted beats quad), connectors designed for the cable, well-balanced transmitter and receiver circuitry | — | BOM | balanced cabling | inspect | p.427 §6.12.3 | high |
| JOHNSON03-2096 | cables | Worked case: 15.2 m (50 ft) Belden RG-58 at 1000 Mbaud, single-ended 3.3-V 50-ohm driver, 250 ps rise/fall -> skin-effect distortion makes LVTTL thresholds (2.0 V / 0.8 V) miss a bit; LVDS thresholds still discriminate | eye closure vs threshold window | cable length/type, bit rate, thresholds | coax, 1 Gb/s | sim | p.427-428 Fig.6.33 | high |
| JOHNSON03-2097 | termination | Center the decision threshold under lossy-line distortion: use a differential receiver with its negative input tied to an accurate mid-level reference (e.g. 1.65 V for 3.3-V swing); tie an end termination to a voltage halfway between V_IH and V_IL (or a split terminator with Thevenin voltage there) so DC attenuation affects both levels symmetrically | V_T = (V_IH + V_IL)/2 | V_IH, V_IL | end-terminated single-ended cable links | calc | p.428 §6.12.4 | high |
| JOHNSON03-2098 | components | LVDS (IEEE 1596.3-1995 general-purpose) transmitter: Voh <= 1475 mV, Vol >= 925 mV, abs(Vod) 250-400 mV, Vos 1125-1275 mV, dVos <= 25 mV (AC CM), single-ended Ro 40-140 ohm, rise/fall (20-80 %) 300-500 ps -- all into Rload = 100 ohm +/-1 %; nominal wires 1.0 V / 1.4 V (1.2 +/- 0.2 V), diff p-p 800 mV nominal | see Table 6.5 | driver datasheet | 200-500 MHz source-synchronous links, up to 128 bits | inspect | p.429-430 Table 6.5 | high |
| JOHNSON03-2099 | components | LVDS receiver: input range 0-2400 mV (either input, abs(Vgpd) < 925 mV), differential threshold -100 to +100 mV, hysteresis >= 25 mV, Rin 90-110 ohm, Cin not specified (only "should not limit 250-MHz operation"); pcb skew allocation 50 ps worst case | see Table 6.5 | receiver datasheet | general-purpose LVDS | inspect | p.429-435 Table 6.5 | high |
| JOHNSON03-2100 | emc | LVDS CM/diff emission ratio can be as poor as 12.5 mV/250 mV = 5 %; relative to 400 mV p-p per wire, 25 mV p-p CM = 6.25 % -> radiated cancellation limited to -24 dB (= 20*log10(0.0625)), attained at all frequencies up to 1 GHz with pair separation <= 0.5 mm | CM ratio = (dVos/2)/abs(Vod,min) = 5 %; limit = 20*log10(dVos/V_pp,wire) | dVos, Vod, V_pp | LVDS traces | calc | p.430, 435 §6.13.2, §6.13.7 | high |
| JOHNSON03-2101 | grounding | LVDS tolerates a driver-to-receiver ground potential difference (Vgpd) of +/-925 mV (0-2400 mV input range vs 925-1475 mV output range); exceeding it voids all behavior guarantees | abs(Vgpd) <= 925 mV | ground shift | general-purpose LVDS | calc | p.430-431 §6.13.3 | high |
| JOHNSON03-2102 | components | Differential noise margin = minimum transmitter differential output - maximum receiver threshold offset: LVDS 250 - 100 = 150 mV (37 % of the 400 mV p-p per-wire swing) vs typical single-ended families 10-15 % | NM_diff = abs(Vod,min) - abs(V_th,max) | Vod,min, V_th,max | differential logic | calc | p.431 §6.13.4 | high |
| JOHNSON03-2103 | components | Always drive hysteresis receivers (LVDS) with fast-edged inputs; slowly moving inputs let crosstalk exceeding the hysteresis window cause glitches | edge rate fast vs hysteresis (25 mV) | input slew, noise | LVDS and hysteretic receivers | review | p.431-432 §6.13.5 | high |
| JOHNSON03-2104 | termination | Both-ends-terminated link residual reflections: r_src = (Ro - Z0)/(Ro + Z0), r_load = (Rin - Z0)/(Rin + Z0); second-incident amplitude = V * r_load * r_src; LVDS worst cases r_src = +0.167 / -0.428 (Ro = 140/40 ohm), r_load = +0.047 / -0.053 (Rin = 110/90 ohm) -> residual <= 2.25 % with a perfect 100-ohm line | V_2nd/V = abs(r_src*r_load) | Ro, Rin, Z0 | purely resistive terminations | calc | p.432-433 eq.6.26-6.29 | high |
| JOHNSON03-2105 | termination | LVDS line impedance tolerance (worst-case Ro and Rin, resistive): Z0 = 100 +/- 10 ohm -> initial residual reflection <= 5 % of incoming step; +/-20 ohm -> <= 7 %; reactances at Tx/Rx degrade further; time-domain simulation decides whether residual matters | residual(Z0) per Fig.6.34 (graph) | Z0 tolerance | both-ends-terminated LVDS | sim | p.433-434 Fig.6.34 | medium |
| JOHNSON03-2106 | termination | External LVDS termination: 100 ohm +/-10 % resistor in a low-inductance package (0805 or smaller) attached directly to the line at the receiver package input terminals, with very small pads (low parasitic capacitance) | R_T = 100 ohm +/-10 %, package <= 0805 | BOM, placement | receivers without internal termination | inspect | p.433 §6.13.6 | high |
| JOHNSON03-2107 | termination | Both-ends termination tolerates mid-line obstacles (vias etc.) better than single-end termination because every reflection path is damped at both ends | prefer source + end termination where power allows | termination scheme | long/obstacle-laden lines | review | p.434 box | high |
| JOHNSON03-2108 | timing | LVDS pcb skew allocation 50 ps (two pcbs + connectors + backplane architecture) ~ 1/4 in. of FR-4 length imbalance between any two signals of a link; with more than two connectors the per-connector budget shrinks; do not trust the autorouter -- inspect final artwork | abs(t_pd,i - t_pd,j) <= 50 ps (~0.25 in. FR-4) | per-net delays | LVDS source-synchronous links | calc | p.435-436 §6.13.10 | high |
| JOHNSON03-2109 | timing | Author's rule of thumb for intrapair skew of any differential signal: keep below 1/10 of the risetime (stricter layout target elsewhere: 1/20) | skew_pair < t_r/10 | t_r | LVDS and other differential pairs | calc | p.436 §6.13.10 | high |
| JOHNSON03-2110 | components | LVDS fail-safe (optional in the standard): internal bias forward-biases an open input by 50 mV (above actual +/-30 mV thresholds) and ~25 mV when a 100-ohm source is connected (thresholds shift to +55 / +5 mV, within +/-100 mV); external bias resistors (R4, R5) add margin for noisy cables, with compensating resistors (R6, R7) at the transmitter; all bias resistors appear in parallel with the termination -- include them when choosing R1 and trace impedance | V_bias,open = 50 mV (vendor example) | bias network values | mixing vendors: check fail-safe compatibility | calc | p.436-438 Fig.6.35-6.36 | high |
| JOHNSON03-2111 | cables | Room-to-room or building-to-building links should use generic building cabling (TIA/EIA 568-B.1-2001 / ISO/IEC 11801:2002): star topology, <= 100 m desktop-to-telecom-room, 100-ohm balanced cabling or fiber; design to the common ground of both standards (e.g. avoid category 7, ISO-only, unless bandwidth needs it) | L_horizontal <= 100 m | link length, cable type | building/campus data links | review | p.440-442 §7, §7.1 | high |
| JOHNSON03-2112 | cables | Horizontal connection: no more than 100 m of cable regardless of cable type, dedicated point-to-point (no bridges, taps or Y connections), two horizontal cables per work area; standard horizontal cabling is the best choice for interconnections of 3 m to 100 m | 3 m <= L <= 100 m; taps = 0 | topology | generic cabling | inspect | p.443 §7.1 | high |
| JOHNSON03-2113 | requirements | Specify cabling performance at the right level: cable (cable makers), permanent link (installers), channel (system makers: end of equipment cable to end of work-area cable); system designs must meet channel specs | channel spec compliance | spec level | generic cabling | review | p.444-445 Fig.7.3 | high |
| JOHNSON03-2114 | requirements | SNR budget for a cabled link: include attenuation and crosstalk of connectors, jumpers, work-area/equipment cables, chip packaging, board layout, receiver bandwidth, transmitter risetime, jitter, reflections from every juncture incl. structural return noise -- then add 2 dB margin (copper) or 3 dB power margin (fiber) | margin_copper >= 2 dB; margin_fiber >= 3 dB (after full budget) | budget line items (dB) | cabled links | calc | p.446 §7.2 | high |
| JOHNSON03-2115 | cables | Mixed categories in one link are guaranteed only to the lowest category (e.g. cat-3 connectors on cat-5e cable -> 16 MHz); cat-6/7 connectors' compensation may not interoperate with lower categories (cat-6 jack in cat-5e receptacle can fall below cat-5e); keep a building at one level | f_guaranteed = min over components | component categories | building cabling | review | p.450 §7.5 | high |
| JOHNSON03-2116 | requirements | Building data cabling life expectancy is 5 to 20 years; supporting category 3 vs requiring category 5e is a trade of transceiver design difficulty vs available market (20-100 Mb/s on cat 3 is challenging) | cabling life 5..20 yr | market | LAN product planning | review | p.450 §7.5 | high |
| JOHNSON03-2117 | connectors | UTP star LANs: hub and client use complementary pin assignments so copper wiring is straight-through (pin 1 to pin 1...); the required crossover belongs in the hub; for fiber label TX/RX and let the user cross them | crossover location = hub | pinout | 10BASE-T/100BASE-T-type links | inspect | p.451 §7.6 | high |
| JOHNSON03-2118 | connectors | A link needs an odd number of crossovers; multi-pair building cables are installed straight-through; any required external crossover (e.g. hub-to-hub) is a short, clearly visible, boldly labeled section of cabling; ports with internal crossover are marked "X" (both or neither marked -> external crossover may be needed) | n_crossovers odd | port types | UTP/STP star LANs | inspect | p.451-452 §7.6, fn.63; p.499 §8.4 | high |
| JOHNSON03-2119 | connectors | 100BASE-TX crossover for 100-ohm cable (RJ-45 pins): pair 3 (1/2) -> 3/6, pair 2 (3/6) -> 1/2, pair 1 (4/5) -> 7/8, pair 4 (7/8) -> 4/5 (pairs 1 and 4 unused by 100BASE-TX); 150-ohm STP-A crossover (DB-9 pins): pair 1 (5/9) -> 1/6, pair 2 (1/6) -> 5/9, pins 2,3,4,7,8 unused | see Tables 7.3-7.4 | pinout | crossover cords | inspect | p.452 Tables 7.3-7.4 | high |
| JOHNSON03-2120 | compliance | Plenum-return air systems forbid PVC-insulated cable in the plenum (toxic smoke distributed by the blower); plenum-rated cables are heavier, stiffer, somewhat more expensive | cable rating = plenum where the ceiling/attic returns air | building HVAC type | building cabling | inspect | p.452-453 §7.7 | high |
| JOHNSON03-2121 | derating | Do not use category 3 PVC cable above 40 C (104 F) (e.g. enclosed attic); use FEP, PTFE or PFA plenum-rated cable or cat 5e+; still de-rate cat 5e+ for copper resistance increase at temperature | T_max(cat 3 PVC) = 40 C | ambient temperature | building cabling | inspect | p.453 §7.8; p.462 §8.1.1 | high |
| JOHNSON03-2122 | connectors | T568A (standard) vs T568B (optional) swap pairs 2 and 3; on uncompensated cat-3 connectors worst crosstalk is between pairs 1 and 2 (T568A) or 1 and 3 (T568B); NCS TRP 109-1977 recognizes only T568A; cat 5e+ makes it moot | — | wiring style | RJ-45 terminations | review | p.453-454 §7.9 | high |
| JOHNSON03-2123 | cables | Do not use 25-pair horizontal cabling in the general case (TIA/EIA 568-B.1 Annex C) nor old telephone-grade quad (no controlled symmetry, terrible crosstalk); running two 2-pair systems in one 4-pair cable requires an explicit crosstalk budget | — | installed cable | legacy installations | review | p.454-455 §7.9 | high |
| JOHNSON03-2124 | cables | Screened 100-ohm cable (ScTP) shield: plastic/metal laminated tape with one or more tin-coated copper drain wires of 26 AWG equivalent or larger contacting the metal side; ScTP meets the same electrical specs as UTP (cat 3, 5e, 6) | drain wire >= 26 AWG | cable spec | TIA/EIA-568-B ScTP | inspect | p.458 §8 | high |
| JOHNSON03-2125 | cables | Table 8.1 values are cable (not channel) specs; channel performance (connectors, jumpers, work-area and equipment cables) is always worse; category 3 is specified only to 16 MHz, useful only to ~25 Mbaud | Baud_max(cat 3) ~ 25 Mbaud | cable category, baud | UTP links | calc | p.459 §8.1 | high |
| JOHNSON03-2126 | cables | DC resistance of a twisted pair (both conductors) | R_DC = 2*(1/(sigma*pi*(d/2)^2)) (ohm/m); AWG 24 (d = 0.508 mm), sigma = 5.80e7 S/m at 20 C -> 0.1701 ohm/m; worst-case spec 0.1876 ohm/m (conductors ~5 % below nominal diameter allowed) | sigma (S/m), d (m) | annealed Cu at 20 C; use datasheet value for stranded, plated or copper-clad-steel conductors | calc | p.460-461 eq.8.1 | high |
| JOHNSON03-2127 | derating | Copper resistance temperature coefficient for cable modeling: increase resistance by 0.39 % per deg C away from the 20 C specification temperature | R(T) = R20*(1 + 0.0039*(T - 20)) | T (C) | cable R_DC and R0 | calc | p.460 §8.1.1 | high |
| JOHNSON03-2128 | cables | Skin depth and skin-effect resistance of a twisted pair at w0 | delta = sqrt(2/(w*mu*sigma)) (m); R0 = kp/(pi*d*delta(w0)*sigma) = (kp/(pi*d))*sqrt(w0*mu/(2*sigma)) (ohm/m, both conductors via kp); cat 3, w0 = 2*pi*1e7, kp = 2.3, d = 0.508 mm -> 1.189 ohm/m nominal (worst-case best fit 1.452 ohm/m, +22 %) | w0 (rad/s), mu = 4*pi*1e-7 H/m, sigma, d, kp | 24-gauge cable: set w0 = 2*pi*10 MHz | calc | p.461-462 eq.8.2-8.4 | high |
| JOHNSON03-2129 | cables | Proximity factors for twisted-pair cables (include both conductors): cat 3, 5e, 6 kp = 2.3; 150-ohm STP-A kp = 2.06 | kp per Table 8.2 | cable type | at 10 MHz reference | calc | p.462 Table 8.2 | high |
| JOHNSON03-2130 | materials | PVC cable dielectric: below 40 C assume nominal effective loss angle theta0 = 0.02 (cat 3 worst-case best fit 0.01578); PVC is strongly temperature dependent above 40 C | theta0 = 0.02 (T < 40 C) | T | category 3 PVC | calc | p.462 §8.1.1 | high |
| JOHNSON03-2131 | cables | TIA/EIA 568-B worst-case delay at 10 MHz implies v0 = 0.6116c (rounded to 0.6c); t_p <= 5.45 ns/m at 10 MHz for cat 3/5e/6 and 150-ohm STP-A | v0 = 0.6c; t_p,max = 5.45 ns/m | — | worst-case cable models | calc | p.459-460 Table 8.1, fn.65 | high |
| JOHNSON03-2132 | cables | Fit a copper-cable model to worst-case specs by starting from eq.8.1/8.4 then tweaking R0 (scales loss above skin-effect onset) and theta0 (curvature at the top end); least-squares fit in dB gives <= 0.16 dB/100 m error (DC-inclusive) or <= 0.03 dB (>= 1 MHz only); TIA/EIA 1/sqrt(f) term near 1 MHz is physically unrealizable | parameters per Table 8.3 | spec attenuation points | time-domain-capable (phase-correct) cable models | sim | p.462-463 §8.1.2, Table 8.3 | high |
| JOHNSON03-2133 | cables | For system simulation add another 2 dB of fixed flat loss to the datasheet/standard attenuation, or extend the simulated maximum cable length by 10 % to 20 % (installers rarely calibrate testers; field cables may not quite meet spec) | L_sim = (1.1..1.2)*L_max or +2 dB flat | L_max, attenuation model | transceiver design verification | sim | p.464-465 §8.1.2 | high |
| JOHNSON03-2134 | cables | Step-response time of a skin-effect-limited cable scales generally with the square of cable length | t_step ~ L^2 | L | long copper cables | calc | p.465 §8.1.2 | high |
| JOHNSON03-2135 | cables | Worst-case cat-3 attenuation at 10 MHz (10BASE-T example, 20 C): 10 m ~1 dB, 50 m ~5 dB, 100 m ~10 dB, 150 m ~15 dB; transmit rise/fall 30 ns (common industry value; limits content above 30 MHz for FCC/EN) | A(10 MHz) ~ 0.1 dB/m cat 3 | L | Manchester 10 Mb/s | calc | p.465-466 Fig.8.4-8.5 | high |
| JOHNSON03-2136 | cables | Unequalized-link limit: when the attenuation difference between the maximum and minimum alternation frequencies of the code exceeds 3.5 dB, the eye suffers (100 m cat 3 at 5 vs 10 MHz: ~3.5 dB OK; 150 m: 5.2 dB too far) | A(f_max_alt) - A(f_min_alt) <= 3.5 dB | cable attenuation vs f, code | any coding without equalization | calc | p.466-467 §8.2 | high |
| JOHNSON03-2137 | cables | Minimum alternation frequency of a code: uncoded random binary = 0 (DC); DC-balanced code balanced over n baud intervals with baud period b ~ 1/(2*n*b); Manchester concentrates energy in 5-10 MHz at 10 Mb/s | f_min_alt ~ 1/(2*n*b) | n, b (s) | line-code selection | calc | p.467 fn.66; p.470 | high |
| JOHNSON03-2138 | cables | 10BASE-T style fixed transmit pre-emphasis: y = (3/4)*x(t) - (1/4)*x(t - b) (b = Manchester baud period): -6 dB below ~1 MHz, -2.5 dB at 5 MHz, 0 dB at 10 MHz; boosts maximum operational length of a two-level Manchester link by at least 50 %; adaptive equalization commonly >= 100 % | H(f) = 3/4 - (1/4)*exp(-j*2*pi*f*b) | b | two-level codes (overshoot harmless); multilevel codes need accurate (adaptive) equalization | calc | p.467-470 Fig.8.6-8.9 | high |
| JOHNSON03-2139 | cables | Principle of equalization: timing jitter is minimized when every received amplitude is independent of past data history | ISI -> 0 at decision point | eye pattern | all baseband links | sim | p.467 §8.2 | high |
| JOHNSON03-2140 | cables | UTP characteristic impedance is controlled within +/-15 % (cat 3) and +/-10 % (higher categories); transceiver input/output impedance can be held to about +/-5 % with hard work | Z0(cat 3) = 100 +/-15 %; Z0(cat 5e/6) = 100 +/-10 %; Z_xcvr +/-5 % | — | reflection budgets | calc | p.472 §8.3.1 | high |
| JOHNSON03-2141 | termination | End-of-cable reflection budget: +5 % transceiver vs -15 % cable ~20 % mismatch -> ~10 % reflection (105 vs 85 ohm: -0.105); with both ends terminated the round-trip reflection is only 10 % x 10 % = 1 % (plus two more passes of cable attenuation); cable-to-cable transitions in cat 3/5 reflect up to 15 % (85 vs 115 ohm) | r = (Zb - Za)/(Zb + Za) | Za, Zb | both-ends-terminated UTP links | calc | p.472 fn.68-69 | high |
| JOHNSON03-2142 | transmission-line | Length of cable needed to build a full-sized reflection; shorter sections reflect in proportion to their length | l_full = t_r*v/2 (m); e.g. 25 Mbaud, t_r ~ 40 ns, v = 0.6c -> 3.6 m (sections < 1 m reflect little) | t_r (10-90 %, s), v (m/s) | any mismatched section | calc | p.472-473 eq.8.5 | high |
| JOHNSON03-2143 | cables | Generic horizontal building wiring permits at most four major transition points per link; limit far-end reflections by limiting nominal impedance, impedance variation, and number of transitions | n_transitions <= 4 | link topology | horizontal cabling | inspect | p.473 §8.3.1 | high |
| JOHNSON03-2144 | cables | Worst-case far-end reflected noise by hand: sum the absolute magnitudes of all second-order reflection modes (reflection coefficients at each transition, zero attenuation between transitions); worst spacing between transitions ~ one-half data baud; include connector reflections; worked case (105/85/115/85/105 ohm, jumpers -1 dB, segment -10 dB) noise -42.2 dB vs signal -12 dB -> SNR 30.2 dB | N = sum over modes of product of abs(r_i) and path losses; SNR = S - N (dB) | r_i, segment losses | fast systems where reflections are > 1 symbol apart (sum of magnitudes is achievable) | calc | p.473-475 Fig.8.11, fn.71 | high |
| JOHNSON03-2145 | cables | Near-end (echo) reflections in bidirectional full-duplex links are first-order (one bounce) and far worse: same worked case gives total noise -17.1 dB vs signal -12 dB -> SNR 5.1 dB; unidirectional links are immune (not listening on the transmit pair) | SNR_near = S - N_first-order | r_i, losses | full-duplex on one pair (hybrids/echo cancel) | calc | p.475-477 Fig.8.13 | high |
| JOHNSON03-2146 | cables | Structural return noise (distributed impedance variation) grows with frequency as w^(3/4) (15 dB/decade) for long skin-effect-limited cables; e.g. a 39x data-rate increase (10 MHz vs 256 kHz) is 39^(3/4) = 15.6x worse | SRN ~ f^0.75 | f | bidirectional links | calc | p.477-478, p.481 §8.3.2.1-8.3.2.2 | high |
| JOHNSON03-2147 | cables | Cat 3 uses structural return loss + explicit mean-impedance limits; cat 5e/6 use a single return-loss spec measured into a 100-ohm load (covers mean and local variation); limits per Table 8.4 | RL >= Table 8.4 (dB) | f (MHz) | TIA/EIA-568-B.2 cables | measure | p.478-479 Table 8.4 | high |
| JOHNSON03-2148 | cables | Random structural-return (and NEXT) model for Monte-Carlo: SRL(w) = sum_{n=0..N} a_n * j*w * H(w, 2*n*dx), a_n Gaussian zero-mean with std sigma chosen to give nominal gain A0 at w0 (derived: sigma = A0/(w0*sqrt(sum_n abs(H(w0, 2*n*dx))^2))); magnitude is Rayleigh distributed -- de-rate A0 by 6-12 dB (8 dB used for Fig.8.21) so the worst case just touches the spec, or scale each trial to graze the limit | eq.8.6-8.7 | H(w,l), dx, A0, w0 | cable noise synthesis | sim | p.480-481 eq.8.6-8.7, Fig.8.21 | medium |
| JOHNSON03-2149 | cables | Hybrid (full-duplex on one channel): with Zs = Zc and Z_T = Zc, v(t) = (1/2)*x(t) + (1/2)*y(t)*h(t); subtract (1/2)*x(t); received gain <= 1/2 (6 dB loss); sensitivity to source or far-end impedance error ~1/2 (10 % error -> 5 % leakage = 26 dB hybrid return loss) | hybrid_RL(dB) ~ -20*log10(0.5*dZ/Z) | Zs, Z_T, Zc | LC or higher (low-loss) region | calc | p.481-483 eq.8.8 | high |
| JOHNSON03-2150 | cables | A resistively terminated hybrid works only above the RC-mode cutoff f = R/L (per-unit-length R and L) unless the line is short enough to be lumped; below it use higher-order terminating networks (normalized 2nd-order works to ~0.1 Hz, 3rd-order to ~0.02 Hz for R = L = C = 1; scale resistances by sqrt(L/C) and capacitances by sqrt(L*C)/R) or digital adaptive echo cancellation | f_min = R/L (Hz, as printed) | R (ohm/m), L (H/m), C (F/m) | dispersive (RC-region) lines | calc | p.483-485 Fig.8.16-8.18 | medium |
| JOHNSON03-2151 | cables | AC-couple the hybrid output (then restore DC if needed) because duty-cycle and supply differences at the two ends shift its DC operating point; balanced bridge hybrid with R >> Z0 yields (1/3)*y(t)*h(t) and is limited by transformer parasitic capacitance, resistor-ratio imbalance and cable impedance uncertainty | — | hybrid topology | balanced hybrids | review | p.486 Fig.8.19 | medium |
| JOHNSON03-2152 | crosstalk | UTP NEXT is a random residue of imperfect twisting: modeled like SRL, magnitude grows as f^(3/4) (15 dB/decade); include NEXT from all adjacent pairs in the SNR budget of any full-duplex system; limits per Table 8.5 | NEXT_loss(f) >= A - 15*log10(f/100) (dB, f in MHz) | f, cable category | TIA/EIA-568-B.2 cables >= 100 m | calc | p.487-489 Table 8.5 | high |
| JOHNSON03-2153 | crosstalk | Do not assume multi-disturber NEXT is less than N x worst-pair NEXT without solid statistics (IEEE 802.3 annex A method depends on NEXT statistics no standard guarantees) | conservative: sum of N disturbers | N pairs | multi-pair budgets | calc | p.489 §8.3.4 | high |
| JOHNSON03-2154 | bringup | Unplugged far end on a short double-end-terminated cable doubles transmit amplitude and doubles receiver susceptibility -> crosstalk into the receiver quadruples (+12 dB) and can trip carrier detect on self-crosstalk; implement a hardware signal-detect that disqualifies strange signals and reliably detects disconnected/powered-off far ends | NEXT_open = NEXT_nominal + 12 dB | NEXT budget, signal-detect threshold | full-duplex multi-pair links | calc | p.489 §8.3.4 | high |
| JOHNSON03-2155 | crosstalk | Alien crosstalk (other applications in the same jacket) cannot be cancelled; 10BASE-T design value: telephone ring-trip spike up to 264 mV differential on an adjacent pair (100-ohm receiver, bandwidth ~15 MHz, scales with bandwidth B); later standards require unused pairs to stay unused | V_alien = 264 mV * (B/15 MHz) | receiver bandwidth B | cat 3 shared-jacket installations | calc | p.490 §8.3.5 | high |
| JOHNSON03-2156 | crosstalk | FEXT/ELFEXT: single consolidated random source, grows 20 dB/decade (proportional to f) and roughly with sqrt(cable length); include in SNR budget of any system transmitting on multiple pairs in the same direction; cat-3 ELFEXT never standardized (100BASE-T2/T4 assumed ELFEXT loss >= 5.0 - 20*log10(f/100) dB, 2-16 MHz) | ELFEXT_loss >= Table 8.6 | f, L | multi-pair same-direction links | calc | p.490-492 Table 8.6 | high |
| JOHNSON03-2157 | timing | Multi-pair (parallel-lane) links: pair-to-pair skew drifts with cable temperature over a day -> continuously de-skew; choose fragment duration > worst-case skew to keep reassembly order unambiguous (at the cost of latency) | T_fragment > skew_max | skew_max, fragment size | striped links (1000BASE-T, 100BASE-T4 etc.) | calc | p.492 §8.3.6 | high |
| JOHNSON03-2158 | crosstalk | Power-sum NEXT/ELFEXT (4-pair cat 5e/6): aggregate power into any victim <= 3 dB worse than the worst single aggressor (vs 10*log10(3) = 4.77 dB for three equal uncorrelated sources); cat-6 power-sum NEXT exceeds pair-to-pair by only 2 dB | PS = worst_pair + 3 dB (cat 6 NEXT: +2 dB) | pair-to-pair values | TIA/EIA 568-B | calc | p.493 §8.3.7, fn.75 | high |
| JOHNSON03-2159 | emc | UTP RFI: design interoffice products for 3 V/m fields in the AM band (0.540-1.620 MHz) and Mobile/TV/FM band (27-200 MHz+); horizontally run 100 m cat 3 picks up < 40 mV (AM) and < 200 mV (Mobile/FM/TV) differential at 3 V/m; worst-case noise design limits 40 mV (AM) and 200 mV (Mobile/FM/TV) | V_RFI,design = 40 mV (AM), 200 mV (27-200 MHz) | band | cat-3 horizontal cabling, US | calc | p.494-495 Fig.8.23-8.24 | high |
| JOHNSON03-2160 | emc | Limit signal spectral content below 27 MHz and low-pass filter the receiver at 27 MHz to hold cat-3 RFI below ~40 mV in most commercial sites (no licensed high-power US sources 1.620-27.0 MHz); steel high-rises attenuate AM by 30-50 dB but FM/mobile hardly at all; cat 5e picks up ~12 dB and cat 6 ~17 dB less RFI than cat 3 | f_LPF = 27 MHz -> V_RFI < 40 mV | receiver filter | exceptions: next to high-power broadcast/military antennas or local transmitters within a few feet | calc | p.495-496 §8.3.8 | high |
| JOHNSON03-2161 | emc | Transformer- or CM-choke-coupled UTP transceivers give good CM balance (RFI and 60-Hz immunity) but require a DC-balanced line code (e.g. Manchester) or receiver DC restoration | code DC-balanced OR DC restore | line code | transformer-coupled links | review | p.493 §8.3.8, fn.76 | high |
| JOHNSON03-2162 | emc | Known-good FCC Class-A UTP systems (well-balanced coupling): 10BASE-T cat 3, 2 pairs, 20 Mbaud (10 MHz Manchester), max diff dV/dt 0.16 V/ns; 100BASE-TX cat 5, 2 pairs, 125 Mbaud MLT-3 scrambled, 0.33 V/ns; 1000BASE-T cat 5, 4 pairs, 125 Mbaud PAM-5 with pre-distortion scrambled, 0.33 V/ns -- review plans that exceed these rates or swings | dV/dt_diff <= 0.33 V/ns (known-good) | baud, dV/dt, pairs | UTP radiated emissions | review | p.496-497 Table 8.7 | high |
| JOHNSON03-2163 | emc | Scramble transmitted data (before coding, as in 1000BASE-T, not after 4B5B as in 100BASE-TX which destroys DC balance/run-length) to spread spectral density, decorrelate bits for adaptive equalizers and decorrelate TX/RX for NEXT/echo cancellers | — | coding chain | UTP transceivers | review | p.496-497 §8.3.9 | high |
| JOHNSON03-2164 | connectors | Category 5 IDC/punch-down UTP connectors suit data rates up to 125 Mbaud; work-area cables use RJ-45 (ISO 8877, IEC 603-7) at both equipment and wall outlet | Baud <= 125 Mbaud (cat 5 IDC) | connector category | UTP | review | p.497-499 Table 8.8 | high |
| JOHNSON03-2165 | connectors | RJ-45 pairs: pair 1 = pins 4,5; pair 2 = 3,6; pair 3 = 1,2; pair 4 = 7,8; 10BASE-T client (no internal crossover) TX+ 1, TX- 2, RX+ 3, RX- 6; hub (internal crossover) RX+ 1, RX- 2, TX+ 3, TX- 6; colored pairs may be consistently substituted, wires within a pair swapped only if polarity reversal is tolerated, but pairs must never be split (e.g. crossing BLU/WHT and ORG/WHT -> massive crosstalk) | pin map per Table 8.9 | wiring | RJ-45, North American color code | inspect | p.499-500 Table 8.9 | high |
| JOHNSON03-2166 | connectors | Support polarity reversal in the receiver to simplify installation (swapped wires within a pair are the most common installation error) | — | receiver design | UTP LANs | review | p.499-500 §8.4 | high |
| JOHNSON03-2167 | connectors | Connecting-hardware insertion loss limits (TIA/EIA-568-B.2): cat 3 <= 0.1*sqrt(f), cat 5e <= 0.04*sqrt(f), cat 6 <= 0.02*sqrt(f), 150-ohm STP-A <= 0.025*sqrt(f) dB (f in MHz) | IL_conn <= k*sqrt(f) | f, category | per mated connection | calc | p.500 Table 8.10 | high |
| JOHNSON03-2168 | connectors | Connecting-hardware NEXT/FEXT/RL limits (min loss): cat 5e NEXT 43.0, FEXT 35.1, RL 20.0 - 20*log10(f/100) (RL from 31.5 MHz; flat below); cat 6 NEXT 54.0, FEXT 43.1, RL 24.0 (from 50 MHz); STP-A NEXT 46.5, RL 20.1 (from 16 MHz); cat 3 NEXT only (OCR constant illegible); never extrapolate compensated-connector crosstalk beyond its specified band | L(f) >= K - 20*log10(f/100) dB | f, category | TIA/EIA-568-B.2 | calc | p.500-501 Table 8.11 | high |
| JOHNSON03-2169 | grounding | TIA/EIA 568-B.1 clause 4.6 requires ScTP drain wires to be terminated at both ends (telecom grounding busbar and equipment chassis) and AC voltage between cable ends <= 1 V rms before connection; the author does not recommend screened cables (field ground currents fluctuate, technicians will not check) | V_ac,ends <= 1 V rms | site ground measurements | screened building cable | measure | p.501-502 §8.5 | high |
| JOHNSON03-2170 | derating | Cable insertion-loss temperature de-rating (TIA/EIA 568-B): cat 5e and 6 +0.4 % of IL (dB) per deg C above 20 C; cat 3 +1.5 % per deg C (and not recommended in hot environments); ISO 8802.3 cl.14: above 40 C use less temperature-dependent (plenum-rated) cable; never use PVC cat 3 in an uncooled attic | IL(T) = IL20*(1 + k*(T - 20)), k = 0.004 (5e/6), 0.015 (3) | T (C), IL20 (dB) | horizontal cabling | calc | p.502-503 §8.6, Fig.8.27 | high |
| JOHNSON03-2171 | cables | 150-ohm STP-A (IBM Type 1): two 22-AWG pairs, per-pair foil + overall braid, jacket OD 0.43 in. (vs 0.25 in. for 4-pair UTP: 3x the cross-section for half the pairs); use only for quick first-release/beta transceivers or short jumpers, not general building wiring | OD = 0.43 in. | — | legacy/jumper applications | review | p.505-506 §9 | high |
| JOHNSON03-2172 | timing | 150-ohm STP-A intrapair skew: the two wires couple more to the shield than to each other (NEXT coupling only 3.7 %), so dielectric differences (e.g. colored insulation inks) create skew; 1000BASE-CX (800 ps baud) needs cable skew as tight as 150 ps in 25 m | skew <= 150 ps / 25 m (1000BASE-CX) | cable skew spec | shielded twinax pairs | measure | p.507-508 §9.3, fn.81-82 | high |
| JOHNSON03-2173 | grounding | Shielded twisted-pair shields must be grounded at both ends with very low impedance across the data spectrum -- conflicts with AC safety grounding, so restrict STP to short links within one closet/computer room between equipment intentionally tied to the same ground and state this in the spec; use fiber or UTP for longer links | ground both ends; same ground domain only | installation spec | STP / twinax | review | p.508 §9.4 | high |
| JOHNSON03-2174 | connectors | Gigabit Ethernet shield ground-transfer impedance <= 0.1 ohm at 625 MHz (=> effective series inductance < 25 pH): requires a 360-degree metallic shield-to-chassis connection around the pins; pigtails and discrete AC-coupling capacitors cannot meet it | Z_t <= 0.1 ohm @ 625 MHz; L_eff < 25 pH = 0.1/(2*pi*625e6) | connector design | 1000BASE-CX-class shielded links | calc | p.508-509 §9.4 | high |
| JOHNSON03-2175 | emc | UTP and STP can both give adequate immunity (IEC 801-4 EFT, Pritchard & Smith 1992): UTP immunity depends on symmetry and twist rate, STP on end-to-end shield integrity, which customers will not maintain | — | cable choice | general building wiring | review | p.509 §9.5 | high |
| JOHNSON03-2176 | connectors | 150-ohm STP-A connectors: avoid the IBM MIC (IEC 807-8, hermaphroditic, 9-part assembly); use shielded DB-9 (EIA/TIA 574:1990 Section 2) for jumpers (FDDI TP-PMD, 100BASE-TX, 1000BASE-CX); DB-9 contacts: no internal crossover 1 = RX+, 6 = RX-, 5 = TX+, 9 = TX-; with internal crossover 1 = TX+, 6 = TX-, 5 = RX+, 9 = RX-; shell = chassis | pin map per Table 9.2 | pinout | STP-A equipment ports | inspect | p.509-511 Tables 9.1-9.2 | medium |
| JOHNSON03-2177 | connectors | Straddle-mount connectors constrain total board thickness and assume a specific signal-layer-to-reference-plane spacing; if the stackup differs, the vendor pad width no longer holds impedance (noticeable above 1 Gb/s) | h_signal-ref = vendor assumption; t_board = vendor limit | stackup, connector drawing | straddle-mount DB-9 and similar | inspect | p.511 §9.6 | high |
| JOHNSON03-2178 | cables | Coax RG specifications (early-1960s US military) define mechanics but only loose electrical properties; modern cables in an RG class can outperform the class by up to 2x -- always use the specific vendor datasheet for loss/impedance | use vendor spec, not RG class | cable part number | coaxial cable selection | review | p.514 §10, fn.84 | high |
| JOHNSON03-2179 | fab | Coax field-applied connectors are unreliable (strip jacket, shield and dielectric in the field); prefer factory-made jumper assemblies made with good tools | factory-terminated assemblies | assembly method | coax links | review | p.513-514 §10 | high |
| JOHNSON03-2180 | cables | Coaxial characteristic impedance in the skin-effect region (current on facing surfaces only) | Z0 = (60/sqrt(er))*ln(d2/d1) (ohm); d2 = shield inside diameter (m), d1 = effective signal-conductor diameter (m), er = dielectric constant | d1, d2, er | above skin-effect onset (~100 kHz for RG-58-class cable); formula verified by book values 76.7 ohm (air) / 51.1 ohm (er = 2.25) at d2/d1 = 3.5911 | calc | p.515 eq.10.1; p.524-525 eq.10.9 | high |
| JOHNSON03-2181 | cables | Small, closely spaced, uniformly distributed geometric perturbations (e.g. braid roughness) raise coax skin-effect loss but not its impedance | — | — | perturbation scale << wavelength | review | p.515 §10.1 | high |
| JOHNSON03-2182 | cables | Standard coax impedances: 50 ohm (test equipment), 75 ohm (audio-visual, dipole-matched), 93 ohm (low capacitance per length); IEC Publication 78 (1967) preferred values 50, 75, 100 ohm | Z0 in {50, 75, 93} commonly available | application | coax selection | review | p.515, 524, 527 | high |
| JOHNSON03-2183 | cables | Coax DC loop resistance for the propagation model: sum of center-conductor and shield DC resistance (use only the inner shield of triax); for copper-plated-steel centers the plating thickness matters -- measure samples with an ohmmeter if not available | R_DC = DCR_center + DCR_shield (ohm/m) | datasheet DCRs | metallic-transmission model, w0 = 2*pi*10 MHz | calc | p.515-516 eq.10.2 | high |
| JOHNSON03-2184 | cables | Coax skin-effect resistance (no proximity correction: coax current distribution is circularly symmetric) | delta_n = sqrt(2/(w0*mu_n*sigma_n)); R0 = 1/(pi*d1*delta_1*sigma_1) + 1/(pi*d2*delta_2*sigma_2) (ohm/m); same material: R0 = (1/pi)*(1/d1 + 1/d2)*sqrt(w0*mu/(2*sigma)) | d1, d2 (m), sigma_n (S/m), mu_n (H/m), w0 | solid conductors; then fit to vendor data (stranding/plating corrections not worth modeling) | calc | p.516-517 eq.10.3-10.6 | high |
| JOHNSON03-2185 | cables | Composite copper-plated steel conductors: current is expelled from the steel at low frequency (tiny skin depth of high-mu steel, mu_r 100 to 10,000+), giving a low-frequency ramp in R_AC, a plateau (hollow copper tube) and then sqrt(f) rise once skin depth ~ plating thickness -- the skin-effect onset region broadens | — | plating thickness | copper-clad steel center conductors | review | p.516, 518 §10.1, Table 10.3 note | high |
| JOHNSON03-2186 | materials | Polyethylene coax dielectric loss tangent ranges 0.0002 to 0.002 (temperature and purity dependent); PTFE is similar but usable to higher temperature; TFE Teflon er ~2.1 vs polyethylene ~2.6 (as printed; elsewhere PE = 2.25-2.3) | tan_d(PE) = 0.0002..0.002 | T, material | coax dielectrics; investigate at temperature extremes | calc | p.518, 522 §10.1 | high |
| JOHNSON03-2187 | cables | Air in the dielectric (helical wrap, foamed/cellular) lowers er: faster propagation (e.g. solid PE v0 = 0.66c vs foamed PE v0 = 0.75c), lower loss tangent, and permits a larger center conductor at the same Z0 -> lower skin loss; foamed materials are less temperature sensitive | v0(foam) = 0.75c vs 0.66c (solid PE) | dielectric type | air vesicles small vs wavelength, uniformly distributed | review | p.518-519 Fig.10.2 | high |
| JOHNSON03-2188 | cables | Coax model fit: start from eq.10.2-10.6, then optimize three parameters to the vendor worst-case curve; add 2 dB fixed flat loss or 10-20 % extra length for rigorous system testing; step-response duration scales with the square of cable length | L_sim = (1.1..1.2)*L or +2 dB | vendor attenuation data | Table 10.4 parameters, 1-1000 MHz | sim | p.519-520 Table 10.4, Fig.10.3 | high |
| JOHNSON03-2189 | cables | Cable size dominates high-frequency loss: bigger conductor circumference -> lower skin loss (RG-174/RG-316 ~0.1 in. OD are about the smallest with standard crimp BNCs; RG-58/RG-303 ~0.2 in.; RG-8 0.405 in. best but hard to install) | loss ~ 1/diameter | OD | coax selection | review | p.520-521 §10.1 | high |
| JOHNSON03-2190 | cables | Coax lowest-order non-TEM (waveguide) mode cutoff; do not operate at or above it (bigger cable -> lower cutoff) | wc = 0.586*pi*c/(d2*sqrt(er)) (rad/s); fc = 0.293*c/(d2*sqrt(er)) (Hz); d2 = shield inside diameter (m); RG-58 (d2 = 2.95 mm, er = 2.3) -> fc = 19.7 GHz | d2, er | coaxial cables | calc | p.521 eq.10.7 | high |
| JOHNSON03-2191 | cables | Tinned and/or stranded center conductors increase attenuation (8259 vs 8240); silver plating (resistivity ~8 % below copper) and TFE dielectric (allows fatter center) reduce it; order sweep-tested cable when performance is critical (roots out periodic manufacturing defects that cause response lumps) | — | cable construction | coax selection | review | p.521-522 §10.1 | high |
| JOHNSON03-2192 | cables | Effective diameter of stranded center conductors (d = single-strand diameter): skin-effect 7-strand = 2.63*d, 19-strand = 4.23*d; DC-resistance effective diameter sqrt(7)*d and sqrt(19)*d | d_eff,AC = 2.63d (7) / 4.23d (19); d_eff,DC = sqrt(n)*d | n, d | 2-D MoM solver, 50-ohm solid PE cable, 120 segments; similar for other Z0/dielectrics | calc | p.522-523 Fig.10.5 | medium |
| JOHNSON03-2193 | transmission-line | Why ~50-ohm pcb traces: near-field EMI proportional to trace height, halving height cuts crosstalk ~4x, lower Z tolerates capacitive loading better; stop at ~50 ohm because most chips cannot drive less (exceptions: Rambus 27 ohm, BTL 17 ohm); slow NMOS-class parts favour high-Z lines (low power); in dense boards 70-ohm traces may be unmanufacturably narrow | Z0_pcb default ~ 50 ohm; crosstalk ~ h^2 (factor ~4 per halving) | driver strength, h, fab limits | pcb impedance selection | review | p.523 §10.1.2 | high |
| JOHNSON03-2194 | cables | Minimum skin-effect loss of a coax with fixed shield diameter occurs at d2/d1 = 3.5911, independent of er and absolute size: 76.7 ohm (air), 51.1 ohm (solid PE er = 2.25, v = 0.667c); minimum is broad (50 -> 75 ohm in solid PE raises skin loss only ~12 %) | alpha_R ~ (sqrt(er)/(60*d2))*(1 + d2/d1)/ln(d2/d1); optimum d2/d1 = 3.5911 | d2/d1, er | coax design | calc | p.524-525 eq.10.8-10.10, Fig.10.6 | high |
| JOHNSON03-2195 | cables | Coax impedance trivia quoted by readers (air dielectric): max power ~30 ohm, max voltage ~66 ohm, min insertion loss ~75-77 ohm; half-wave dipole ~73 ohm, quarter-wave over ground ~37 ohm (geometric compromise 51.97 ohm, SWR 1.404 either way); early rigid lines 51.5 ohm from standard copper-pipe sizes | quoted values | — | air-dielectric coax (reader correspondence, not derived) | review | p.526 §10.1.3 | medium |
| JOHNSON03-2196 | cables | 50-ohm coax tolerates the capacitive loading of multidrop transceiver taps better than 75 ohm (smaller reflection per tap -> more stations per segment; why 10BASE-5 chose 50 ohm); lower differential impedance than 150 ohm would have given STP-A less loss in the same jacket | — | tap capacitance | multidrop coax buses | review | p.527-528 §10.1.3 | high |
| JOHNSON03-2197 | cables | Coax crosstalk between adjacent cables is negligible for digital LAN work; remaining coax impairments are far-end reflections and RFI; RG-58 (50 +/-2 ohm) splice gives worst reflection 4 %, double reflection <= 0.0016 (ignorable) | r_max = 2/50 = 4 %; r^2 = 0.0016 | Z0 tolerance | unidirectional coax links | calc | p.528 §10.2-10.2.1 | high |
| JOHNSON03-2198 | emc | Coax susceptibility below ~30 MHz is set by shield DC/low-frequency resistance (use thicker braid or bigger cable); above that, field leaks through braid holes (use heavy braid + solid foil; foil slightly raises HF attenuation) | Z_t low; braid + foil for HF | shield construction | coax RFI/radiation | review | p.529 §10.2.2 | high |
| JOHNSON03-2199 | connectors | Fast digital coax: use connectors with 360-degree shell-to-chassis contact; no pigtails, pins or tabs connecting shield to chassis | 360-degree bond | connector type | coax/shielded cable entries | inspect | p.529 §10.2.2 | high |
| JOHNSON03-2200 | emc | Specify coax by transfer impedance (longitudinal shield voltage / internal signal current vs frequency) for EMC (ISO/IEEE 8802.3 (1996)); above 100 MHz scramble data so idle/repetitive patterns do not concentrate power at pattern harmonics | Z_t(f) spec; scrambling above 100 MHz | Z_t, coding | coax links | review | p.529 §10.2.3, fn.86 | high |
| JOHNSON03-2201 | grounding | Coax ground treatment follows the signal: direct-connected signal needs a low-impedance shield-to-chassis connection; if the signal path is blocked by an isolator (transformer, opto/GMR isolator, differential receiver) the shield may be isolated from chassis; unidirectional convention: direct-connect at transmitter, isolate at receiver | — | interface topology | intercabinet coax | review | p.530-531 Fig.10.7-10.8 | high |
| JOHNSON03-2202 | magnetics | Common-mode choke for blocking intercabinet ground current on coax: several henries (primary impedance of several thousand ohms at 60 Hz) with leakage inductance small enough to pass the digital signal | Z_CM(60 Hz) >= several kohm; L ~ several H | choke specs, signal bandwidth | coax/shielded links between AC domains | calc | p.531 Fig.10.9 | high |
| JOHNSON03-2203 | grounding | A DC-balanced signal (50 % clock, Manchester, 8B/10B) has negligible power below f_DC (10-MHz Manchester ~1 MHz) and passes through transformers/high-pass paths with cutoff < f_DC; the shield may then be grounded through a path that is low-Z at HF but high-Z at 60 Hz (e.g. a capacitor with low enough series inductance) | f_HP,cutoff < f_DC | code, f_DC | transformer/AC-coupled links | calc | p.531-532 box | high |
| JOHNSON03-2204 | connectors | Above 100 MHz always match the coax connector impedance (sqrt(L/C) of its parasitics) to the cable; at risetimes comparable to connector delay internal details matter -- demand vendor SWR/reflection data; threaded types outperform bayonet types; performance depends on cavity manufacturing uniformity | Z_conn = Z_cable for f > 100 MHz | connector data | coax connectors | review | p.532-533 §10.3 | high |
| JOHNSON03-2205 | connectors | Coax connector family ratings (recommended max frequency): C 4 GHz, N 10 GHz, BNC 4 GHz, TNC 10 GHz, SMB 4 GHz, SMA/SMC 10-30 GHz (cable OD .060-.425 in. standard/miniature, .060-.141 in. subminiature) | f_max per Table 10.5 | family | selection | inspect | p.533 Table 10.5 | medium |
| JOHNSON03-2206 | connectors | For a digital signal to pass a connector ~99 % intact, require return loss > 17 dB at all frequencies from DC to the logic knee frequency (0.5/t_r); connector distortions aggregate over every connector in the link | RL >= 17 dB for f <= 0.5/t_r (r <= 0.1413, transmission 0.990) | RL(f), t_r | connectors in high-speed links | calc | p.533 Table 10.6 | high |
| JOHNSON03-2207 | connectors | SWR / return loss / reflection conversions | r = 10^(-RL/20); SWR = (1 + r)/(1 - r); transmission = sqrt(1 - r^2) | RL (dB) or r | sine-wave excitation | calc | p.534 Table 10.6 | high |
| JOHNSON03-2208 | connectors | Coax connector practice: gold or stainless-steel mating surfaces for repeated insertion; threaded connectors on anything that moves (boat, car, plane); crimp for speed and no-AC-power sites (best dimensional/impedance control), solder where crimp tools/spares are unavailable (ships, spacecraft); avoid twist-on types; heat-treated beryllium-copper contact springs | — | BOM | coax connectors | inspect | p.533-535 §10.3 | high |
| JOHNSON03-2209 | cables | Fiber: bandwidth far exceeds copper but transceivers cost more and connectors must be kept clean and unscratched (copper IDCs wipe clean and tolerate dirty environments) | — | environment | medium selection | review | p.537 §11 | high |
| JOHNSON03-2210 | cables | Standard glass fiber geometry (TIA/EIA-568-B, ISO/IEC 11801) for any core < 85 um: cladding 125 um, coating 250 um; LAN multimode cores 50 and 62.5 um (also 85, 100, 140 um); single-mode core ~10 um; tight buffer 900 um for 50-62.5 um fiber | cladding = 125 um, coating = 250 um | core size | fiber specification | inspect | p.539-542 Fig.11.3 | high |
| JOHNSON03-2211 | cables | Larger fiber cores lower system cost (looser mechanical tolerances) but reduce bandwidth (more modes); plastic fiber for low-bandwidth short links only | — | core size | fiber selection | review | p.540 §11.2 | high |
| JOHNSON03-2212 | cables | Get fiber optical data from the core manufacturer, mechanical data from the cable plant; an unprotected fiber stretched by 1 part in 1,000 breaks; microbends greatly raise attenuation; tight buffer for horizontal in-building runs, loose buffer (optionally gel-filled) for tall vertical runs and outdoor stress | strain_max < 1e-3 | buffer type | fiber cable selection | review | p.541-543 §11.3 | high |
| JOHNSON03-2213 | cables | Glass fiber windows: 770-860 nm, 1270-1355 nm, 1500-1600 nm; Rayleigh scattering loss ~1/lambda^4 below ~700 nm; IR absorption precludes operation above ~1800 nm; OH absorption peaks near 950, 1240 and 1390 nm (OH < 1 part in 1e8 required) | lambda in {770-860, 1270-1355, 1500-1600} nm | wavelength | glass fiber links | review | p.543-544 Fig.11.7 | high |
| JOHNSON03-2214 | cables | Multimode modal dispersion: each mode has its own delay and attenuation; graded-index modal delays matched to better than 1 part in 1,000; dispersion that exceeds the source risetime visibly stretches edges and must be carried in the power budget | — | length, modal bandwidth | multimode links | calc | p.546-547 Fig.11.10 | high |
| JOHNSON03-2215 | cables | Modal bandwidth Bm is the 6-dB electrical (3-dB optical) bandwidth of 1 km of fiber (MHz-km); modal 10-90 % dispersion risetime estimated from Bm and length (eq.11.1; formula body not legible in OCR) | t_m = f(Bm, l) per eq.11.1 (ps; Bm in MHz-km, l in km) | Bm, l | overfilled (LED) launch | calc | p.548 eq.11.1 | low |
| JOHNSON03-2216 | cables | Chromatic dispersion 10-90 % risetime from dispersion constant, length and RMS source spectral width; use factor 2.56 for RMS width, 1.09 for FWHM width (eq.11.2); modal and chromatic dispersion combine per eq.11.3 | t_c = 2.56*D*l*lambda_RMS (ps) (reconstructed from the stated variables and constant; OCR lost the equation body) | D (ps/nm-km), l (km), lambda_RMS (nm) | LED ~150 nm spectral width; D ~85 ps/nm-km near 800 nm; null near 1300 nm | calc | p.548-550 eq.11.2-11.3 | medium |
| JOHNSON03-2217 | cables | LED sources (~150 nm spectral width) suffer heavy chromatic dispersion at 850 nm, much less at 1300 nm (natural dispersion null); lasers/VCSELs are narrow and less affected; improve chromatic dispersion with 1300 nm, narrow sources and short links | D(800 nm) ~ 85 ps/nm-km | wavelength, source | multimode LED links | review | p.549-550 Fig.11.11 | high |
| JOHNSON03-2218 | cables | Step-index multimode worst-case modal spread = delay*(n2/n1 - 1) (ratio of transit times); typical n2/n1 ~ 1.01 -> 100 m (400 ns) gives 4 ns; graded-index profiles improve modal dispersion by orders of magnitude | dt = t_delay*(n_ratio - 1) | t_delay, index ratio | step-index fiber (ray model) | calc | p.551 Fig.11.12 | high |
| JOHNSON03-2219 | cables | Specify multimode fiber per IEC 793-2 category A1a (50 um) or A1b (62.5 um); dual-window bandwidth written e.g. 62.5/125 um 160/500 MHz-km (850/1300 nm); safe installed-base design values (IEEE 802.3z, 1997 survey): 160/500 MHz-km for 62.5 um and 400/400 MHz-km for 50 um (ISO 11801: 200/500 for 62.5 um) | Bm_design(62.5) = 160/500; Bm_design(50) = 400/400 MHz-km | fiber type | building multimode fiber | inspect | p.552-553 Table 11.1 | high |
| JOHNSON03-2220 | cables | Numerical aperture ~ sqrt(n_core^2 - n_cladding^2) (already fixed by IEC 793-2 section A for standard graded-index fibers) | NA = sqrt(n1^2 - n2^2) | n1, n2 | multimode fiber | calc | p.553 §11.5.3 | high |
| JOHNSON03-2221 | cables | 50-um fiber has higher bandwidth and lower attenuation but a surface-emitting LED calibrated for 62.5 um loses ~2 to 5 dB when coupled into 50-um fiber (edge emitters: no penalty) | coupling penalty 2..5 dB (surface LED into 50 um) | source type | multimode power budgets | calc | p.554 Fig.11.13 | high |
| JOHNSON03-2222 | requirements | Every fiber link needs an accurate worst-case optical performance budget covering dispersion, attenuation and jitter (templates valid for glass multimode, 100 m - 1 km, 100-1000 Mb/s; re-check assumptions outside that range) -- customers use it to assign blame | budget items: dispersion, attenuation, jitter | link parameters | multimode fiber links | calc | p.555 §11.5.5 | high |
| JOHNSON03-2223 | cables | Optical link test points for budgets: TP1 electrical input to LED/laser driver; TP2 optical into cable plant (far side of TX connector, or end of first connection after a pigtail; Gigabit Ethernet: end of a specified patch cord); TP3 optical at receiver input; TP3b inside receiver after the low-pass filter, before the limiting amplifier; TP4 electrical after the limiter, before the sampling flip-flop | budget ISI at TP3b | — | fiber link specs | review | p.556-557 Fig.11.14 | high |
| JOHNSON03-2224 | timing | Gaussian risetime combination (variances add): valid only when source edge, fiber and filter step responses are monotonic and approximately Gaussian -- NOT for copper (skin-effect tails are non-Gaussian; convolve explicitly) | t_TP3b = sqrt(t_TP2^2 + t_fiber^2 + t_filter^2) (10-90 %); t_10-90 = 2.56*sigma | component 10-90 % risetimes | fiber-optic links | calc | p.558-559 eq.11.4, Fig.11.15 | high |
| JOHNSON03-2225 | cables | Multimode fiber 10-90 % risetime (modal + chromatic) | t_fiber = sqrt( (0.48*l*1e6/Bm)^2 + (D*l*2.56*lambda_RMS)^2 ) (ps); Bm = 6-dB electrical modal bandwidth (MHz-km), l (km), D (ps/nm-km), lambda_RMS (nm); constant 0.48 back-solved from the book's FDDI example (OCR illegible) | Bm, l, D, lambda_RMS | Gaussian fiber impulse assumption | calc | p.559-560 eq.11.5; p.566 example | medium |
| JOHNSON03-2226 | cables | Chromatic dispersion constant from zero-dispersion wavelength and slope (IEEE 802.3z 1998 formula; normal and dispersion-shifted fiber, 850 and 1300 nm windows, wide or narrow sources; not for dispersion-flattened SMF) | D = sqrt( ((S0/4)*(lambda_c - lambda_0^4/lambda_c^3))^2 + (0.7*S0*lambda_RMS)^2 ) (ps/nm-km); S0 (ps/nm^2-km), lambda (nm); worst case over lambda_0 and lambda_c ranges | S0, lambda_0, lambda_c, lambda_RMS | form verified numerically against the FDDI example (t_TP3b = 6119 ps) | calc | p.560 eq.11.6; p.566 | medium |
| JOHNSON03-2227 | cables | Source spectral width conversions: lambda_RMS = lambda_FWHM/2.35; 10-90 % risetime factor 2.56 x (RMS width) or 1.09 x (FWHM width) | lambda_RMS = lambda_FWHM/2.35 | spectral width | Gaussian spectra | calc | p.549, 565 | high |
| JOHNSON03-2228 | components | Receiver low-pass filter 10-90 % risetime (multipole, critically damped) and recommended cutoff | t_filter = 0.35/B_3dB (s, B in Hz) (ideal Gaussian 0.338/B_3dB); typical receivers set the LPF cutoff near 0.7/t_b (t_b = baud interval) | B_3dB, t_b | optical receivers | calc | p.560-561 eq.11.7, fn.106; p.570 §11.5.7 | high |
| JOHNSON03-2229 | timing | Worst-case ISI pattern for monotonic step responses is an isolated 1 in a long run of 0s (or complement); Gaussian system: h(t) = exp(-t^2/(2*sigma^2))/(sigma*sqrt(2*pi)), g(t) = erf2(t/sigma), H(w) = exp(-(w*sigma)^2/2), sigma = t_TP3b/2.56 | y_bad(t) = g(t - t0) - g(t - t0 - t_b) | t_TP3b, t_b | linear-phase Gaussian model (erf2 = cumulative normal) | sim | p.561-562 eq.11.8-11.12 | high |
| JOHNSON03-2230 | cables | Dispersion (ISI) power penalty for a unit eye sampled mid-baud with mid-level threshold | P_D = -10*log10( (erf2(1.28*t_b/t_TP3b) - erf2(-1.28*t_b/t_TP3b) - 1/2)/(1/2) ) (dB optical) = -10*log10(4*erf2(1.28*t_b/t_TP3b) - 3) | t_TP3b, t_b | Gaussian model | calc | p.562-563 eq.11.13-11.18, Fig.11.17 | high |
| JOHNSON03-2231 | cables | Limit the dispersion penalty to 2 dB or perhaps 3 dB (3 dB = eye half closed by ISI at top dead centre; beyond 3 dB performance becomes extremely sensitive); a dispersion-limited link is not fixed by more transmit power | P_D <= 2..3 dB | P_D | fiber links | calc | p.563 §11.5.5.1 | high |
| JOHNSON03-2232 | timing | Clock-window (sampling uncertainty) penalty with half-sinusoid eye assumption (pessimistic) | P_W = -10*log10(cos(pi*t_w/(2*t_b))) (dB optical); t_w = full width of clock uncertainty window centred in the baud | t_w, t_b | improve only with better clock recovery | calc | p.564 eq.11.19; p.566 (t_w = 2000 ps, t_b = 7500 ps -> 0.393 dB) | high |
| JOHNSON03-2233 | timing | Duty-cycle distortion: use the minimum ON/OFF duration as t_b in dispersion and clock-window penalties (FDDI: DCD <= 1.00 ns p-p -> t_b = 8.00 - 0.50 = 7.50 ns) | t_b,eff = t_b - DCD_pp/2 | DCD spec | optical transmitters | calc | p.564 §11.5.5.1 | high |
| JOHNSON03-2234 | cables | Worked FDDI dispersion regression case: t_s = 3500 ps, t_b = 7500 ps, t_w = 2000 ps, Bm = 500 MHz-km, L = 2 km, lambda_FWHM = 140 nm, lambda_0 = 1300-1350 nm, S0 = 0.11 ps/nm^2-km, lambda_c = 1320-1360 nm, B_LPF = 87.5 MHz -> t_LPF = 4000 ps, t_TP3b = 6119 ps, P_D = 1.154 dB, P_W = 0.393 dB | as stated | as stated | typical datasheet values, not FDDI worst case | calc | p.565-566 example | high |
| JOHNSON03-2235 | cables | Optical attenuation (power) budget: margin = (TX min power - guaranteed RX sensitivity) - (cable loss + connector/splice loss + dispersion penalty + clock-window penalty + extinction-ratio penalty + other penalties); glass cable loss typically 2-10 dB/km; allow several connectors (e.g. 4 x 0.5 dB) for patch panels and jumpers | margin_dB = (P_TX,min - S_RX) - sum(losses, penalties) | budget line items (dBm, dB) | multimode LED links (laser links add penalties) | calc | p.566-567 Table 11.3 | high |
| JOHNSON03-2236 | cables | Optical power margin: a 3-dB margin is highly desirable (robust in the field); insist on ~6 dB during initial product planning because the margin always erodes | margin >= 3 dB (final); >= 6 dB (planning) | budget | fiber links | calc | p.568 Table 11.3 notes, fn.107 | high |
| JOHNSON03-2237 | cables | Extinction-ratio penalty (E = zero-state power / one-state power): peak-to-peak power falls below twice the average when the transmitter does not go dark | P_ER = abs(10*log10((1 - E)/(1 + E))) (dB optical); often negligible for LEDs | E | fiber transmitters | calc | p.567-568 Table 11.3 notes | high |
| JOHNSON03-2238 | cables | RX sensitivity must be guaranteed at acceptable BER under worst case including self-crosstalk from the local transmitter in the same package and Vcc noise; if sensitivity is specified with a worst-case dispersion stress signal, the dispersion penalty may already be included | — | receiver datasheet | fiber receivers | review | p.567 Table 11.3 notes | high |
| JOHNSON03-2239 | timing | Jitter budget = bounded deterministic jitter (measured with a repeating mixed-run-length pattern, e.g. 10101111000011110000, averaged) + Gaussian random jitter; random jitter measured at 1e-6 is extrapolated to 1e-12 by 7/4.8 = 1.46 | TJ(1e-12) = DJ + 1.46*RJ(1e-6) (Gaussian extrapolation) | DJ, RJ | serial links | calc | p.568-569 Fig.11.19 | high |
| JOHNSON03-2240 | components | Fiber receiver with a dark input (fiber unplugged, far end off) runs its AGC to maximum gain and can lock onto crosstalk from the local transmitter; limit maximum receiver gain, add a minimum-signal-level (signal-detect) circuit that shuts the receiver off, or reduce crosstalk | signal-detect required | receiver design | duplex fiber transceivers | review | p.570 §11.5.7 | high |
| JOHNSON03-2241 | emc | Fiber does not radiate, but the optical transmitter near the cabinet opening can radiate strongly -- include it in the emissions plan | — | layout | fiber ports | review | p.570 §11.5.7 | high |
| JOHNSON03-2242 | compliance | Never look into the end of a fiber; single-mode systems fall under international laser-safety rules requiring labels/warnings on transmitters and fibers | provide laser-safety labels | product labeling | fiber equipment | inspect | p.571, 578 §11.5.8, §11.6.3 | high |
| JOHNSON03-2243 | cables | Laser diodes on multimode fiber depend on unspecified fiber properties: centre launches excite bad modes (excess modal dispersion/differential mode delay), plus modal noise, mode-partition noise and reflection-induced noise (test per ANSI X3.230-1994 annex A, A.5); if you must, copy the specification of a high-volume standard | — | launch conditions | 1-Gb/s class laser MMF links (to several hundred m) | review | p.571-573 §11.5.9 | high |
| JOHNSON03-2244 | connectors | Fiber connectors: duplex SC (ISO-preferred for new facilities, smallest footprint, only connector authorized for Gigabit Ethernet), ST (two per port), FDDI MIC (FDDI only); leave a service loop of fiber at each end for re-termination; single-mode connectors can join multimode fiber but not vice versa | duplex SC preferred | connector type | building fiber | inspect | p.575-578 Table 11.4 | high |
| JOHNSON03-2245 | cost | Optical backplanes are not yet cost-effective (transceiver pair vs one Euro-connector pin); use optics for intersystem links; check transceiver and connector pricing/availability before committing | — | cost model | backplane architecture | review | p.576 §11.5.11 | high |
| JOHNSON03-2246 | cables | Single-mode fiber (9-10 um core per ISO 11801, 1300 nm and longer only, never at 850 nm): no modal dispersion, DMD, modal or mode-partition noise; >20 km at 1 Gb/s attainable (10-100x multimode distance); budget as multimode with t_modal = 0; often hard-spliced to save attenuation; requires laser sources and precise (costly) connectors | t_m = 0; lambda >= 1300 nm | link length, rate | single-mode links | calc | p.576-578 §11.6 | high |
| JOHNSON03-2247 | timing | Clock signal requirements: monotonic and perfectly damped through the V_IL-V_IH region on both edges (no ringback into the transition region at any time), fast square edges (but no faster than the receivers can use), low jitter (reduce crosstalk, package ground bounce and supply noise into oscillator/repeaters), high fan-out, low skew | clock edge monotonic between V_IL and V_IH | waveforms at every clock load | all clock nets | sim | p.579-581 §12, Fig.12.1-12.3 | high |
| JOHNSON03-2248 | timing | Slow clock edges enlarge the receiver switching-time uncertainty and crosstalk susceptibility (fast edges are one SI need directly opposed to EMC) | t_unc = (V_IH - V_IL)/(dV/dt) | edge rate | clock receivers | calc | p.580-581 Fig.12.2 | high |
| JOHNSON03-2249 | timing | Intentional clock skew via DLL/PLL clock buffers (phase-detector feedback) produces arbitrary, precise delays where fixed chain-of-gates delays cannot be made accurate; delaying the capture clock helps setup (long-path) limits, advancing it helps hold (short-path) limits; gains vanish in loops whose feedback path delay is comparable to forward stage delays | — | timing report | pipelined synchronous designs | calc | p.582-584, 587-588 §12.1-12.2 | high |
| JOHNSON03-2250 | timing | Setup constraint with clock skew (Fig.12.7 circuit): data must arrive before the next capture clock minus setup | t_CLK > t_FF,MAX + t_G,MAX + t_SETUP + (t_C1,MAX - t_C2,MIN); t_SLOW = t_C1,MAX + t_FF,MAX + t_G,MAX; t_REQUIRED = t_CLK + t_C2,MIN - t_SETUP; require t_SLOW < t_REQUIRED | clock-path delays C1 (launch), C2 (capture), FF clock-to-Q, logic delay incl. trace, setup | only the difference in clock path delays matters, not absolute delay; a separate hold constraint also applies | calc | p.586-587 eq.12.1-12.4 | high |
| JOHNSON03-2251 | timing | Setup violations appear above a frequency (slowing the clock fixes them); hold violations are independent of clock period (slowing the clock does NOT fix them); max-delay analysis must maximize launch-clock delay and minimize capture-clock delay (or require setup margin > maximum absolute clock skew) | margin_setup > abs(skew_max) (alternative check) | timing paths | STA | calc | p.584-587 §12.2 | high |
| JOHNSON03-2252 | timing | Never operate near the setup-failure frequency: de-rate so every path keeps a positive setup margin of about one gate delay under all conditions (covers crosstalk edge shifts, delay miscounts, out-of-spec gates, later layout changes); offset a non-crystal oscillator so its shortest period still exceeds t_CLK | margin_setup >= 1 gate delay | path delays | synchronous designs | calc | p.585-588 §12.2 | high |
| JOHNSON03-2253 | timing | Worked 500-MHz budget (10EP31 flip-flops, two 10EP58 MUX stages, 10EP14 clock driver; ps): clk-to-Q 475 + setup 150 = 625; per logic section MUX 400 + 25 mm trace 180, x2 = 1160; clock skew 10EP14 max-min 50 + 2.5 mm trace skew 18 = 68; margin 147 (7.3 %); total 2000 | sum(terms) + margin = T_clk | budget table | bipolar ECL example; trace delay ~7.2 ps/mm | calc | p.588 example | high |
| JOHNSON03-2254 | timing | Clock skew costs cycle time exactly like any other propagation delay; in resource-constrained projects minimize clock skew rather than optimizing every data net | skew counted 1:1 in T_clk | skew budget | synchronous designs | review | p.588 §12.2 | high |
| JOHNSON03-2255 | termination | Clock repeaters: 4 to 20 low-skew outputs with low-impedance drivers intended for one accurately series-terminated line each (not multiple loads per output); always terminate clock lines regardless of length (predictable delay vs length) | one series-terminated line per output | repeater outputs, R_s | clock distribution | inspect | p.589-590 §12.3 | high |
| JOHNSON03-2256 | timing | Output-to-output skew is the repeater's worst skew across its own outputs; part-to-part (input-to-output) uncertainty matters only when repeaters are chained/tree'd; GaAs and bipolar repeaters have very low skew but are power hungry and non-TTL outputs lose their skew advantage through translators | tree skew = sum of input-to-output uncertainties of cascaded parts + output skew + trace skew | repeater datasheet | multi-level clock trees | calc | p.590-592 Table 12.1, Fig.12.11 | high |
| JOHNSON03-2257 | timing | One oscillator may drive several repeater inputs directly only if it can drive the load and the trace delay between repeater inputs is <= 1/6 of the clock risetime; otherwise use a tree | t_trace,between inputs <= t_r/6 | oscillator drive, trace delay, t_r | clock tree topology | calc | p.590 Fig.12.10 | high |
| JOHNSON03-2258 | timing | Worst-case skew of a two-level repeater tree (Fig.12.11) | skew = input-to-output uncertainty of A + output-to-output skew of B + input-to-output uncertainty of E + trace-length skew between C and D | datasheet uncertainties, trace skews | chained repeaters | calc | p.592 Fig.12.11 | high |
| JOHNSON03-2259 | pdn | Source clocks from an isolated clock-repeater package, not spare ASIC I/Os (package SSN/ground bounce corrupts clock outputs); keep clock parts physically separated from noisy signals | dedicated clock package | BOM/placement | clock sources | inspect | p.592 §12.3 | high |
| JOHNSON03-2260 | timing | Active (DLL) skew correction nulls output-to-output skew but does nothing for overall input-to-output delay uncertainty; actively compensated repeaters are highly sensitive to supply noise -- follow vendor supply-filtering guidance and provide a clean, jitter-free reference | — | repeater type, PSU filter | PLL/DLL clock buffers | review | p.593 §12.3.1 | high |
| JOHNSON03-2261 | timing | Zero-delay (PLL or DLL) clock buffers regulate outputs to the input edge and so control input-to-output uncertainty (the key parameter for big clock trees); choose parts on observable worst-case skew and RMS jitter, not on PLL-vs-DLL architecture claims | input-to-output offset ~ 0 (+/-50 ps shown in Fig.12.13, graph) | datasheet skew/jitter | multi-level clock trees | review | p.594-595 §12.3.2, Fig.12.13 | medium |
| JOHNSON03-2262 | timing | Skew that matters is at the points of use: repeater output skew only transfers if every branch has equal delay (not just equal length), the same termination and the same loading | branch delay, termination and load identical | per-branch delay, C_load | clock trees | calc | p.595, 599 §12.3.3, §12.5 | high |
| JOHNSON03-2263 | termination | On a perfectly source-terminated line the source node shows two half-height steps separated by one round-trip delay; the far-end transition occurs exactly midway between them (basis for line-length-sensing clock drivers) | t_far = (t_step1 + t_step2)/2 | source waveform | series-terminated lines (measurement/diagnosis) | measure | p.595-596 Fig.12.14 | high |
| JOHNSON03-2264 | timing | Stripline propagation velocity depends only on the dielectric (not geometry or impedance); microstrip is always faster: FR-4 examples 13 % to 17 % faster than stripline (er_eff 3.14-3.37 vs 4.30) | v = c/sqrt(er_eff); stripline er_eff = er | layer type, geometry | same dielectric on all layers (mixed-material stackups excepted; engineer their X-Y CTE mismatch) | calc | p.596-598 Table 12.2 | high |
| JOHNSON03-2265 | timing | Temperature skew between layers: FR-4 er can vary up to 10 % over 0-70 C (stripline delay ~5 %), 50-ohm FR-4 microstrip only ~3 %; length-matched microstrip vs stripline clocks still mismatch >= 1 % at temperature extremes (+/-20 ps on 30 cm) -- route all clocks of a skew group on the same layer type | dt_skew ~ (0.05 - 0.03)/2 * t_pd (approx, +/-1 %) | layer assignment, length | clock nets | calc | p.598-599 §12.4 | high |
| JOHNSON03-2266 | termination | Clock-line delay vs load: with series termination each 5 pF of load adds ~300 ps delay to the 75 % threshold (~R*C with R = 50 ohm), independent of line length (linear, predictable); unterminated short lines (10-ohm driver) show nonlinear, threshold-dependent delay (e.g. 5 pF, 1-in. line appears ~0 delay at 75 % but bulges at 25 %) -- always terminate clock lines | dt_load ~ Z0*C_L per load (series-terminated) | Z0, C_L | t_r = 1.00 ns, Z0 = 50 ohm, 180 ps/in. FR-4 stripline (Fig.12.18, graph) | sim | p.599-601 Fig.12.18-12.19 | high |
| JOHNSON03-2267 | timing | Low-skew clock tree recipe: same clock driver type everywhere, source-terminate every driver, same line length, impedance and loading on every trace (add dummy capacitors to balance), use input-to-output (not only output-to-output) delay specs, and verify with a high-quality probe and high-bandwidth scope | branch parameters identical | tree netlist, layout | clock distribution | inspect | p.601 §12.5 | high |
| JOHNSON03-2268 | timing | Include receiver threshold uncertainty in every clock skew budget | t_UNCERTAINTY = t_10-90 * (V_IH - V_IL)/dV | t_10-90, V_IH, V_IL, dV | single-ended clocks (differential receivers contribute little) | calc | p.601-602 Fig.12.20 | high |
| JOHNSON03-2269 | termination | Resistive loads scale amplitude (RL/(RL + Rs), e.g. 100 ohm on a 10-ohm driver -> 90 %) but do not change the 10-90 % risetime measured on the signal's own final value; they do shift threshold-crossing times (load to ground retards rising, advances falling edges); a split terminator (Thevenin voltage set by R1/R2) can trim timing slightly | V_final = V_oc*RL/(RL + Rs); t_10-90 unchanged | Rs, RL, threshold | resistive terminations | calc | p.602-604 Fig.12.21-12.23, fn.116 | high |
| JOHNSON03-2270 | timing | Use purposeful clock skew only with a good whole-circuit timing model; aim first to reduce clock arrival uncertainty, then apply fixed offsets; include each delay element's uncertainty in the timing margin | — | timing model | intentional skew | review | p.605, 610 §12.8 | high |
| JOHNSON03-2271 | timing | Fixed delay element ranges and accuracy: pcb trace (serpentine) 10-1000 ps, +/-10 %; ordinary logic gate 100-10,000 ps each, +/-50 % or more (minimum delay rarely specified); discrete RC circuit 1000-1,000,000 ps, +/-5 % to +/-20 % | see Table 12.3 | required delay, tolerance | board-level delays (on-chip gates much faster) | calc | p.605-606 Table 12.3 | high |
| JOHNSON03-2272 | timing | Trace delay-line sizing at er = 4.3: 1 ns requires 0.144 m (5.67 in.) of trace; at 300-um (11.8-mil) pitch each ns consumes ~0.43 cm^2 (0.067 in^2) | L_per_ns = c/sqrt(er)*1 ns; area = L*pitch | er, pitch | stripline serpentine delays | calc | p.606 §12.8.1 | high |
| JOHNSON03-2273 | materials | Measure laminate er temperature dependence with a copper-clad blank in an oven and a capacitance meter (calibrate out leads); trace velocity changes by half the percentage change in er | C = 8.854e-12*er*w*d/h (F); 0.3 x 0.3 m, h = 1.5 mm, er = 4.5 @1 MHz -> 2391 pF; dv/v = -0.5*d(er)/er | w, d, h (m), er | FR-4 delay-line qualification | measure | p.606 eq.12.5 | high |
| JOHNSON03-2274 | timing | Discrete RC delay between CMOS gates ~ RC (any R, even 1 Mohm, with CMOS); with bipolar/DC-input-current gates the I*R drop can prevent switching (use a bead/inductor); long delays make the slow node noise-sensitive: use a low-offset differential receiver or Schmitt feedback (~C/10), shield from crosstalk and give it a privately filtered supply | t_d ~ R*C | R, C, input current | discrete delays | calc | p.606-607 Fig.12.24 | high |
| JOHNSON03-2275 | test | Every production timing adjustment needs a written test procedure stating how to measure the clock delay at that point and the acceptable limits; prefer simple tap schemes (binary-weighted jumper delays breed mistakes); glue/clamp adjustable components (vibration) | procedure + limits per adjustment | adjustment list | adjustable delays | review | p.607-609 §12.8.2 | high |
| JOHNSON03-2276 | timing | Tapped delay lines work only if the tap-collection circuit is short compared with the edge length; shorting plugs (0.025-in. square posts on 0.100-in. centres) add ~1-3 nH and show side effects above 100 MHz; solder-blob jumpers (1 mm square pads, 150 um / 0.006 in. gap) are smaller and better at high frequency | L_plug = 1..3 nH (0.1-in. pins on 0.1-in. spacing) | f_clk, jumper type | adjustable delays | review | p.607-609 Fig.12.25-12.27, fn.117 | high |
| JOHNSON03-2277 | timing | Varactor-tuned delays need a reverse-bias supply of at least 12 V (preferably 24 V); DLL-calibrated dummy delays or supply-starved CMOS chains can track temperature/process; for an N-phase generator tune a delay chain (inverters hold 50 % duty better than buffers) with a phase detector to exactly one clock period | V_bias >= 12 V (24 V preferred) | delay technology | programmable delays | review | p.609-610 §12.8.3 | high |
| JOHNSON03-2278 | timing | Match all eight factors for clock delay balance: trace length, configuration (microstrip/stripline), width/impedance (HF loss), dielectric constant, loading, receiver thresholds, terminations, serpentine layout; clock distribution skew = slowest corner (longest, slowest layer, narrowest, highest er, most load, highest threshold, least overshoot) minus fastest corner | skew = t_slow,corner - t_fast,corner | tolerances on all 8 items | clock nets with delay matching | sim | p.610-611 §12.8.4 | high |
| JOHNSON03-2279 | crosstalk | Serpentine switchbacks: 50-ohm microstrip 8-mil traces/5-mil spaces, 5 mil above plane -> NEXT ~10 %; if a switchback's round-trip delay >= risetime, NEXT appears as ~10 % pre/post-cursor distortion (microstrip also shows FEXT pulses); if << risetime (<= ~1/3 t_r) coupling instead advances arrival: up to 2 x NEXT for one switchback, up to 4 x NEXT for a multi-section serpentine | t_rt,section <= t_r/3; delay reduction <= 4*NEXT | NEXT coefficient, section delay, t_r | pcb serpentine delay lines | sim | p.611-612 §12.8.4 | high |
| JOHNSON03-2280 | crosstalk | Maximum useful coupled-switchback section length ~1 in. (2 in. round trip) for 1-ns risetime on FR-4, ~0.1 in. for 100-ps risetime; for first-pass-accurate delay space serpentine traces far enough apart to eliminate coupling, for minimum area use short tightly packed sections and add sections to recover the lost delay | L_section,max ~ t_r*v/6 (1 ns -> ~1 in.) | t_r, v | serpentines | calc | p.611-612, 615-616 §12.8.4-12.8.5 | high |
| JOHNSON03-2281 | crosstalk | Switchback regression case (Fig.12.29-12.31): microstrip 200-130-200 um (8-5-8 mil), 330-um pitch, 130 um height, 50 ohm, er = 4.3, 300-ps 3.3-V CMOS driver; straight 300 mm = 1680 ps; single 2 x 150 mm switchback -> 300 mV NEXT pre- and post-cursors (each 1680 ps long) and a 500-mV FEXT pulse 1680 ps after the edge; 24 x 12.5 mm serpentine with ~10 % NEXT arrives ~25 % early; stripline serpentine shows the NEXT effect without FEXT | as stated | as stated | HyperLynx LineSim v5.01, lossless, perfectly terminated | sim | p.612-615 Fig.12.29-12.32 | high |
| JOHNSON03-2282 | termination | Source termination does not reduce peak driver current: initial input impedance 2*Z0 needs I_peak = Vcc/(2*Z0), the same as a split (mid-supply Thevenin) end termination; size the series resistor from the driver's guaranteed output voltage at I_peak | R_series = (V_out(I_peak) - Vcc/2)/I_peak; I_peak = Vcc/(2*Z0) | driver V-I curve, Z0, Vcc | series-terminated lines | calc | p.616-617 Fig.12.33 | high |
| JOHNSON03-2283 | termination | One driver can serve N source-terminated lines only if all lines are equal length and equally loaded, with each series resistor reduced to account for the shared driver impedance (negative self-reflection cancels positive cross-coupling); no solution if the result is negative; imbalance makes the net ring | R_t = Z0 - N*Rs (derived from the text's statements; OCR lost eq.12.6); launch = Vcc/2 on each line | Rs, Z0, N | multi-line source termination | calc | p.617-618 eq.12.6, Fig.12.34 | medium |
| JOHNSON03-2284 | termination | A tee net with all three branches long vs the edge cannot simultaneously give a crisp, full-size first incident wave with no residual reflections using good practice: slow driver (15 ns) too slow for 66 MHz; 50-ohm series + 50-ohm end terminations give 1/3 amplitude; 100-ohm weak end terminations only calm ringing; 50-ohm trunk with 100-ohm branches plus 40-ohm series (+10-ohm driver) works only with equal branches (0.75 vs 1.25 ns, i.e. t_r/2 imbalance, destroys it) -- prefer two low-skew drivers with point-to-point links | avoid tees unless CAD enforces the constraints | topology | 3.3-V CMOS, 10 ohm, 6 nH package, 1 ns edges, 150-mm branches, 3 pF loads (graph) | sim | p.619-624 Fig.12.35-12.43 | high |
| JOHNSON03-2285 | termination | Always simulate branched/"hairball" nets with one load at maximum input capacitance and line length and the other at minimum, using the fastest risetime expected over the product life | corner sims: (C_max, L_max) vs (C_min, L_min) | load and length ranges | tee, split-tee, H-trees | sim | p.622-623, 627 §12.9.1-12.9.2 | high |
| JOHNSON03-2286 | termination | Split-tee (source-terminated trunk feeding two short stubs): keep stub delay <= 1/6 of the risetime; every split-tee hides an unconstrained resonance between the two loads that the source terminator cannot damp -- imbalance (e.g. 6 pF vs 4 pF) excites it (example ~500 MHz = 3rd harmonic of a 166-MHz clock); small series resistors at each receiver (18 ohm in the example) kill it; test at the resonant frequency and at 1/3 and 1/5 of it | t_stub <= t_r/6 | stub delay, load imbalance | example: driver Rs = 11 ohm, t_10-90 = 500 ps, trunk 50 ohm 1000 ps, stubs 50 ohm 250 ps | sim | p.625-627 Fig.12.44-12.45 | high |
| JOHNSON03-2287 | termination | Daisy-chain tap reflection (isolated capacitive load on a line) and remedies | a ~ -dV*tau/t_r, tau = (1/2)*Z0*C; e.g. 2.5 V, 3 pF, 50 ohm, 500 ps -> 375 mV (15 % of swing, enough to double-clock many families); remedies: slower driver (just fast enough for the skew budget), less tap capacitance (include connector/stub C), lower Z0, isolate each CMOS receiver with a series R >= Z0, or narrow the trace near each tap | C, Z0, t_r, dV | loads spaced widely vs edge length | calc | p.627-629 eq.12.7 | high |
| JOHNSON03-2288 | termination | Lowest end-termination resistance a driver can drive while meeting VOH/VOL on every edge | R_T,min = (VOH - VOL)/(IOH - IOL) (datasheet spreads) | VOH, VOL, IOH, IOL | end-terminated lines | calc | p.628 §12.10 | high |
| JOHNSON03-2289 | termination | Effective impedance of a uniformly loaded line, and daisy-chain rules: space loads uniformly, with inter-tap delay small vs rise/fall time, and terminate at the loaded impedance (not the raw trace impedance) | Z_LOADED = Z0*sqrt(C_LINE/(C_LINE + C_LOAD)); C_LINE = t_PROP/Z0; example 25 cm at 1.44e8 m/s -> 1.73 ns, 34.6 pF + 5 x 3 pF -> 41.7 ohm (40-ohm termination removes 10 % overshoot) | Z0, t_PROP, C_LOAD | uniform spacing, tap delay << t_r | calc | p.629-632 eq.12.8, Fig.12.47-12.50 | high |
| JOHNSON03-2290 | termination | Faster edges on a loaded daisy chain: modulate trace width (e.g. 40-ohm main trace with an 11.6-mm 80-ohm section bracketing each 3-pF load, 5-cm spacing) to compensate tap capacitance -- supports ~2x faster edges (500 MHz+ clocking) | see example | Z_main, Z_comp, lengths | FR-4 stripline, 5 loads, 10-ohm driver | sim | p.632-633 Fig.12.51-12.52 | high |
| JOHNSON03-2291 | timing | Clock-reference quality terms: frequency offset (long-term; crystal-controlled systems ~a few hundred ppm, measured with a counter over many seconds; mainly affects PLL lock-in), wander (short-term variation the PLL must track within slew limits), jitter (variation too fast to track; directly becomes timing error) | comply with the PLL input offset/wander/jitter specs | reference specs | PLL clock multipliers/regenerators | review | p.634-635 §12.11 | high |
| JOHNSON03-2292 | pdn | PLL clock multipliers need a stable, low-jitter reference: noisy oscillator power (e.g. 100-kHz switching noise) can make the multiplied clock fail to lock, hunt, or shut off; get, test and meet the reference offset/wander/jitter specs | — | reference oscillator supply | clock multipliers incl. in-processor PLLs | measure | p.635-636 §12.11 | high |
| JOHNSON03-2293 | timing | Clock jitter matters mainly at boundaries between independently clocked domains; within one synchronous state machine only the minimum (and for poor designs maximum) clock period matters -- characterize with a clock-interval histogram (timing interval analyzer) | T_min >= required period | period histogram | synchronous logic | measure | p.636 §12.11.1.1 | high |
| JOHNSON03-2294 | timing | PLLs track input phase modulation below the loop bandwidth, filter it above, and may resonate (peak) in between; any peaking multiplies through chains (gain^N: 1.1^50 = 117; 0.5 dB x 256 token-ring stations = 128 dB) -- PLLs used in cascade/data comm must have a well-damped jitter transfer function with no peak | peak(jitter transfer) = 0 dB for cascaded PLLs | jitter transfer function | chained PLLs, repeaters, rings | measure | p.636-640, 652 §12.11.1.2, §12.11.2.1 | high |
| JOHNSON03-2295 | timing | Receiver phase-error budget: theoretical limit +/-1/2 data interval, practical limit more like +/-10 % to +/-20 % of a bit interval | abs(phase error) <= 0.1..0.2 UI | jitter budget | clock/data recovery | calc | p.640 fn.123 | high |
| JOHNSON03-2296 | timing | PLL tracking-error variance equals the reference phase-jitter power above the loop bandwidth | sigma_e^2 = (1/pi)*int_0^inf abs(1 - F(w))^2*abs(Y(w))^2 dw = 2*int_0^inf abs(1 - F(f))^2*abs(Y(f))^2 df; brick-wall cutoff B: (1/pi)*int_B^inf abs(Y(w))^2 dw; stochastic reference: (1/pi)*int_B^inf S(w) dw | F, Y or S, B | mind rad/s vs Hz integration constants | calc | p.640-643 eq.12.10-12.15 | high |
| JOHNSON03-2297 | timing | FIFO between two PLL-locked domains with a low-rate common reference: FIFO excursion follows accumulated phase (integral of frequency error) between reference edges -- 1e-4 frequency offset over 77,750 cycles (8 kHz ref, 622 MHz clocks) = 7.775 clocks; size FIFO = 2N with N = maximum cycle drift per packet/transaction (preload N words); prefer a higher reference frequency (e.g. 8 MHz) | N = df*T (cycles); FIFO depth >= 2N | df (Hz), T (s) | burst transfers between domains | calc | p.643-644 Fig.12.57, fn.126 | high |
| JOHNSON03-2298 | components | Oscillator/PLL jitter sources: crystal thermal noise, microphonics, amplifier self-noise (often larger), and power-supply noise (most troublesome; poor supply immunity is common); a PLL also passes reference jitter inside its tracking bandwidth | — | oscillator selection, supply filtering | clock sources | review | p.644-645 §12.11.1.5 | high |
| JOHNSON03-2299 | timing | Separate deterministic from random jitter: DJ measured by triggering at the pattern/reference repetition rate with averaging; random variance by subtraction; DJ has a peak/sigma ratio ~1 (two-valued), RJ peak/sigma set by BER (Table 12.4) -- a single sigma spec for mixed jitter is overly stringent | sigma_R^2 = sigma_T^2 - sigma_D^2 | measured variances | clock/data jitter specs | measure | p.645-647 eq.12.16 | high |
| JOHNSON03-2300 | timing | Jitter budget at a BER: peak allowance = DJ(worst case, not scaled) + k*sigma_RJ with k from Table 12.4 (k = 7.131 at 1e-12); e.g. 0.3 rad tolerance: all-Gaussian sigma <= 0.3/7.131 = 0.042 rad, or 0.1 rad DJ + sigma_RJ <= 0.028 rad | DJ + k(BER)*sigma_RJ <= tolerance | tolerance, DJ, BER | serial links, clock recovery | calc | p.647-648 Table 12.4 | high |
| JOHNSON03-2301 | timing | Phase-noise plot to jitter: under the narrowband PM assumption (phase deviation < 1 rad), phase variance (rad^2) = (integrated phase-noise power outside the PLL tracking bandwidth B) / (carrier power); p-p jitter at BER 1e-12 ~ 14.3 sigma; e.g. 0.1 UI p-p requires sigma < 0.1/14.3 UI = (0.1*2*pi)/14.3 rad (SMPTE 270 Mb/s example: 370 ps p-p at 27 MHz = +/-0.1 UI over 10 Hz to 1/10 serial clock) | sigma^2 = P_noise(|f - f0| > B)/P_carrier; J_pp(1e-12) = 14.3*sigma | phase-noise spectrum, B | VCO/PLL clock synthesis | calc | p.648-649, 654-656 §12.11.2, §12.11.2.2 | high |
| JOHNSON03-2302 | test | Jitter measurement methods: spectrum analysis (needs narrowband-PM and distribution assumptions for peak phase), direct phase vs ideal or "golden PLL" (divide by n to keep error < 1 UI: error/n), differential phase via delayed sweep (differential jitter up to 2x actual; with FM period T worst at T/2), BERT bathtub scan, timing interval analysis (easiest statistics), PLL loop test with loop BW << jitter band | — | instrument | clock jitter characterization | measure | p.648-650 §12.11.2 | high |
| JOHNSON03-2303 | test | Characterize a PLL by (A) jitter transfer (phase-modulate the reference at rate MR, scope delayed 0.5/MR), (B) supply sensitivity (AC-couple a swept sine onto each Vcc pin, removing PLL-side bypass caps if needed; at each F find the noise amplitude X giving a standard objectionable jitter, e.g. 0.1 clock period; watch for squelching), and (C) intrinsic jitter (timing-interval or spectrum analyzer with clean supply and reference) | tolerance curve X(F) vs measured supply noise spectrum -> required filter attenuation | test setup (Fig.12.58: 1-ohm/0.047-uF injection network, 50-ohm-terminated generator) | oscillators and PLLs | measure | p.651-654 Fig.12.58-12.59 | high |
| JOHNSON03-2304 | pdn | Design a PLL/oscillator supply filter from the measured supply-noise tolerance curve X(F) combined with the measured system supply-noise spectrum (the only rational method); dips in the tolerance curve indicate needed extra filtering | required attenuation(F) = V_noise,sys(F)/X(F) | tolerance curve, noise spectrum | clock sources, repeaters, PLLs | calc | p.653 §12.11.2.1 | high |
| JOHNSON03-2305 | pdn | Clock-source supply filter (Fig.12.60): L1 = 1 uH (0.1 ohm, 100 pF shunt) feeding two 0.047-uF capacitors (0.1 ohm, 0.5 nH each) with a 2.2-ohm damping resistor (1 nH, 1 pF): > 20 dB attenuation from 10 MHz to 1 GHz; cascading two sections roughly doubles attenuation (dB); without the damper L1 resonates with the capacitors at the cutoff | f_c = 1/(2*pi*sqrt(L*C)) (1 uH, 0.094 uF -> ~500 kHz); -20 dB/decade with damping (~20 dB one decade above f_c) | L, C, R | damping-resistor formula eq.12.20 illegible in OCR | calc | p.656-658 eq.12.19, Table 12.5, Fig.12.61 | medium |
| JOHNSON03-2306 | pdn | Single-stage LC filter stops working near the parasitic resonance of the inductor's shunt capacitance with the capacitors' series inductance; add a ~25-mm (~10 nH) trace downstream of L1 with input and output well separated to push past it | f_par ~ 1/(2*pi*sqrt(C_L,SHUNT*L_C,SERIES)) (100 pF, 0.25 nH -> ~1 GHz) | parasitics | wideband supply filters | calc | p.658 eq.12.21 | high |
| JOHNSON03-2307 | pdn | High-frequency filter layout: keep input and output well separated; connect every capacitor directly to a solid reference plane with large vias (>= 500 um / 20 mil diameter); keep incidental traces < 2.5 mm (0.1 in.); use the smallest practical SMT parts; wideband filters are cascades of sections each covering a higher band; measure component parasitics first | via dia >= 0.5 mm; stray trace < 2.5 mm | layout | supply filters for clocks/PLLs | inspect | p.659 §12.12 | high |
| JOHNSON03-2308 | bringup | Measure Vcc-to-ground noise on every new board: solder a 50-ohm coax directly to a removed bypass capacitor's pads (short exposed center conductor) into the scope's 50-ohm input (power-ground impedance < 1 ohm, no high-Z probe needed); measure at several locations (distributed at HF); AC-couple with a series 0.1-uF capacitor (0.1 uF x 50 ohm = 5 us, passes > 100 kHz) -- e.g. re-solder a board cap with its ground end on insulating tape, or an SMA black box good to ~1 GHz | tau = C_block*50 ohm = 5 us | test points | board bring-up | measure | p.659-661 Fig.12.62 | high |
| JOHNSON03-2309 | pdn | Very low measured supply noise is a cue to remove or shrink bypass capacitors (cost, space, weight); high noise flags PDN work | — | measured noise vs budget | bring-up / cost-down | measure | p.661 §12.12.1 | high |
| JOHNSON03-2310 | pdn | An LC supply filter (L1 series, C2 from AVCC to DGND) does not remove absolute noise; it makes AVCC track DGND at high frequency (differential noise across the analog load -> 0) -- adequate for oscillators, PLLs and fiber receivers; A/D converters referencing two grounds need the grounds joined at a point carrying no high-speed current | Z_L1 >> Z_load >> Z_C2 at noise frequencies | filter values, load impedance | quiet analog supplies | review | p.661-663 Fig.12.63 | high |
| JOHNSON03-2311 | emc | Clock spread-spectrum/dither lowers FCC/EN peaks only because those measure in 100-kHz bandwidths (new modes must be > 100 kHz apart); total radiated energy is unchanged and wideband victims (bandwidth > modulation bandwidth) see no improvement; really moving interference needs a frequency shift of 2-3x | mode spacing > 100 kHz for any peak reduction | modulation profile | EMC compliance strategy | review | p.663-666 §12.13-12.13.1 | high |
| JOHNSON03-2312 | timing | Never use an intentionally modulated (spread-spectrum/dithered) clock as the reference for data-communication transceivers (Ethernet, Fibre Channel, FDDI, ATM, SONET, ADSL), RF/direct-sequence-spread-spectrum references, or CPUs/PLL clock multipliers unless the vendor explicitly tolerates it; otherwise add a clean reference plus async FIFO | reference clock = unmodulated | clock tree netlist | mixed synchronous/async systems | inspect | p.664-665 §12.13 | high |
| JOHNSON03-2313 | emc | Preferred clock EMC measures instead of modulation: solid power and ground planes, minimum trace-to-plane spacing, thin packages (signals close to board), slower clock edges, differential clock transmission, lower-voltage clock drivers (LVDS, GTL) | — | stackup, driver choice | clock emissions | review | p.665 §12.13 | high |
| JOHNSON03-2314 | emc | Scrambled clock (edges on a fixed time grid with pseudorandom polarity) spreads emissions without adding jitter: a 256-bit PRBS splits the spectrum into 256 lines each ~1/256 of the energy (> 20 dB peak reduction); standardize the sequence, use a divide-by-N acquisition aid, high transition density and DC balance | peak reduction ~ 10*log10(N_seq) dB | sequence length | zero-delay PLL clock distribution | calc | p.667-668 Fig.12.64 | high |
| JOHNSON03-2315 | crosstalk | Reduced-voltage clock signaling (BTL, GTL, ECL, SSTL, LVDS) saves power and cuts EMI but is more noise-susceptible: enforce extra spacing between low-voltage traces and other logic families' traces | extra spacing to full-swing nets | net classes | reduced-swing clocks | inspect | p.668-669 §12.14 | high |
| JOHNSON03-2316 | crosstalk | Protect clocks with extra spacing or dedicated layers between solid reference planes (power or ground with low impedance between them), implemented through auto-router net-class spacing rules; attend the start of layout to ensure the constraints are applied | clock net class spacing > default | net-class rules | clock routing | inspect | p.669-670 §12.15 | high |
| JOHNSON03-2317 | emc | Choose terminations for minimum signal current, not just acceptable voltage: on a short source-terminated line the largest series resistor that still gives acceptable waveforms minimizes transmitted current and emissions (example 30.5 cm, 133 MHz clock, 10-39 ohm: larger values cut current harmonics 10-20 dB; 22-25 ohm showed current glitches); layer changes that divert return current magnify stray common-mode current | R_series = max acceptable value | simulated current waveforms | clock and fast nets | sim | p.670-672 Fig.12.65-12.66 | high |
| JOHNSON03-2318 | process | Ringing on pcb traces over a solid plane with known source/load impedances and risetime is deterministic and accurately simulatable: simulate every questionable net instead of rules of thumb (e.g. "3-inch stubs are okay"); simulators are weak on 3-D problems such as crosstalk across split planes | simulate before build | net list, models | SI sign-off | sim | p.673-674 §13.1 | high |
| JOHNSON03-2319 | process | SI model extraction: die I/O (SPICE or IBIS), package (L and C coupling matrices plus per-pin R; coupled-line models for large packages/extreme speeds), board (trace impedances, lengths, topologies, coupling, connectors); main errors are wrong modeling depth and data-entry mistakes -- have a second person double-check all model parameters; staffing ~1 SI specialist per 5 digital designers | second-person model review | model sources | SI process | review | p.674-676 §13.2 | high |
| JOHNSON03-2320 | process | Required modeling depth for boards <= 25 cm (10 in.): t_r ~ 3 ns (OCR prints "3 us") -> lossless lines, no package models; 1 ns -> add IC package models for fast signals (package resonance); 300 ps -> model packages, vias, all discontinuities, skin effect and dielectric loss; compare each added level with the previous result to see if it matters | model level by t_r | t_r, board size | SI simulation planning | sim | p.676 §13.2.1 | high |
| JOHNSON03-2321 | process | Post-route SI verification should flag nets violating overshoot %, ringback %, monotonicity, peak crosstalk and settling time, and list where terminations are needed or unnecessary; automated tools are only as good as their input -- double-check results | violation lists per criterion | post-route sim | SI sign-off | sim | p.676-677 §13.2.2-13.2.3 | high |
| JOHNSON03-2322 | process | SPICE transient practice: run twice with different (max) time steps -- results must not change; for very fast circuits with a minimum-step limit scale all C and L by 1000, slow inputs by 1000 and lengthen lossless lines by 1000 (rescale skin/dielectric loss to keep dB loss); set tolerance options for very small/large signals; cure non-convergence by shunting inductors with a small C or 1 Mohm, and smoothing piecewise-linear I-V curves | result(dt) = result(dt/2) | step size, tolerances | SPICE/SI engines | sim | p.680-682 §13.3.2 | high |
| JOHNSON03-2323 | process | SPICE evolves capacitor voltages and inductor currents explicitly each step (DC initial solution with C open, L short) and iterates node voltages (Newton-Raphson; needs smooth, monotonic I-V curves) | v_C(n+1) = v_C(n) + dt*i_C(n)/C; i_L(n+1) = i_L(n) + dt*v_L(n)/L | — | time-domain solvers | sim | p.678-680 §13.3-13.3.1 | high |
| JOHNSON03-2324 | transmission-line | Lossless transmission-line models suffice for t_r >= 1 ns on boards <= 25 cm (10 in.); if trace loss at the logic knee frequency exceeds 10 %, use a skin-effect + dielectric-loss (e.g. W-element) model (lossless models misstate step response and underestimate jitter); lossy-model run time ~ 1/dt^2 (halving the step quadruples time); smaller segments give better accuracy | loss(f_knee) > 10 % -> lossy model | loss at f_knee | SPICE TL modeling | sim | p.682-683 §13.3.3 | high |
| JOHNSON03-2325 | test | Correlate the simulator to the bench before trusting it: start with hand-calculable low-frequency circuits (e.g. 20 ft of 50-ohm coax driven by a 50-ohm generator paralleled with 50 ohm = 25-ohm source -> 33 % far-end overshoot, 10-100 ns risetimes); at >= 500 MHz (1 ns) use SMA connectors and a resistive-input probe with >= 3x the signal bandwidth | overshoot = (Z0 - Rs)/(Z0 + Rs) = 33 % for 25 ohm into 50 ohm; BW_probe >= 3*BW_signal | test setup | simulator validation | measure | p.684 §13.3.4 | high |
| JOHNSON03-2326 | process | Use IBIS behavioral models (I-V tables for high/low states plus switching waveforms/ramp) for board-level ringing and crosstalk: ~10-15x less computation than transistor-level SPICE and non-proprietary; limitations: controlled-risetime feedback drivers, driver interaction under ground bounce; request IBIS files (incl. minimum risetime) from every chip vendor | IBIS model per driver/receiver | vendor models | board-level SI | review | p.685-688 §13.3.5-13.4 | high |
| JOHNSON03-2327 | process | IBIS waveform data to request: CMOS totem-pole -- rising and falling waveforms with 50 ohm to ground and 50 ohm to Vcc (four total; if only one of each, use a symmetrically split end termination); emitter followers (ECL, PECL, some GaAs) -- one each into 50 ohm to V_T; open-drain (Rambus, GTL, BTL) -- one each into 25 ohm (or system value) to V_T; always specify behavior under conditions like the application (50-ohm loads, not 50-pF lumps, for fast parts) | waveform sets per driver type | IBIS file | model quality check | inspect | p.691-694 §13.6 | high |
| JOHNSON03-2328 | process | IBIS interpolation: die capacitance is de-embedded from measured waveforms, then i_TP(v,t) = a(t)*i_LOW(v) + b(t)*i_HIGH(v); with one waveform per edge the solver assumes a + b = 1, two waveforms (different loads) solve a, b independently and extrapolate better; wrong die capacitance -> errors grow away from the measurement load | eq.13.1 | I-V tables, waveforms, C_comp | IBIS simulators (method varies by vendor) | sim | p.692-694 eq.13.1 | high |
| JOHNSON03-2329 | grounding | SSO (ground-bounce) noise on the internal ground rail; linear summation of individual driver di/dt overestimates it (drivers slow each other through the shared rail) -- IBIS simulators do not compute SSO properly; request the full package pin self/mutual inductance matrix; gauge driver sensitivity by lowering Vcc and watching switching time | V_SSO = L_GROUND*d(i_GROUND)/dt | L_GROUND (effective, all ground pins), di/dt | package/IC selection | calc | p.695-697 eq.13.2 | high |
| JOHNSON03-2330 | emc | EMC is a serial hunt for the worst radiating mode (fixing any other changes nothing); a product 20 dB out of spec may need ~10 fixes of 2-3 dB each; rules: limit risetimes, doubling speed vs last design needs ~6 dB more protection, run a quick EMI scan as early as possible (software cannot predict the worst mode) | +6 dB margin per 2x speed | prior product data | EMC planning | measure | p.697-699 §13.8-13.8.1 | high |
| JOHNSON03-2331 | pdn | Power/ground planes act as a lumped capacitor only if cross-board delay is short vs edge rate (6 x 6 in. FR-4: ~1 ns across; fine for ~5 ns edges, distributed for 200-ps edges); if the round-trip delay across the board is close to the clock period expect plane resonance -- measure a mock-up (double-sided FR-4 core) with a network analyzer or use distributed plane simulators for decoupling placement | t_rt,board vs T_clk; lumped if t_cross << t_r | board size, er, t_r, T_clk | designs relying on plane capacitance | calc | p.699-701 §13.9, Fig.13.9 | high |
| JOHNSON03-2332 | process | Signal-integrity organization: an independent SI department with a clear mission ("maximize the performance and minimize the cost of interconnection technology used in high-speed digital designs"), led by a manager who can sell it; start as consultant (no mandates) and prove value on a pilot program; mature ratio ~1 SI specialist per 5 digital designers, with model/package/connector specialists in large groups | 1 SI : 5 designers | org plan | engineering organization | review | p.731-732 App.A | high |
| JOHNSON03-2333 | transmission-line | Loss slope of a channel = slope of log(attenuation in dB) vs log(f); attenuation proportional to f^eta has loss slope eta: skin-effect region 1/2, dielectric-loss region 1; the loss slope measures the severity of the distance-vs-speed tradeoff in dispersion-limited systems | eta = d(log a_dB)/d(log f) = log(a2/a1)/log(f2/f1) | a_dB at two frequencies | linear systems | calc | p.733-734 App.B eq.B.1-B.8 | high |
| JOHNSON03-2334 | transmission-line | Two-port transmission (ABCD) matrices for cascade analysis (cascade = matrix product): series Z = [[1, Z],[0, 1]]; shunt Z = [[1, 0],[1/Z, 1]]; line with one-way transfer H and impedance Zc = [[(1/H + H)/2, Zc*(1/H - H)/2],[(1/H - H)/(2*Zc), (1/H + H)/2]]; with output open: Zin = a00/a10, voltage gain v2/v1 = 1/a00; source-line-load gain v3/v1 = 1/[A_s*B_line*C_load]_00 | M_total = product of stage matrices | Z's, H(w), Zc(w) | linear time-invariant networks (drivers, bond wires, pads, BGA traces, via pi-models...) | calc | p.735-742 App.C eq.C.1-C.21, Fig.C.3 | high |
| JOHNSON03-2335 | transmission-line | Input impedance of a line of one-way transfer H: open-circuited far end Zin = Zc*(1/H + H)/(1/H - H); matched Zin = Zc; shorted Zin = Zc*(1/H - H)/(1/H + H); TDR response = (v3/v1)*[BC]_00 | as stated | Zc, H | TDR/impedance calculations | calc | p.739-741 eq.C.12-C.19 | high |
| JOHNSON03-2336 | transmission-line | Pi-model (lumped C/2 - L,R - C/2) accuracy vs a true line: error ~ ((l*gamma)^3/6)*(Zs/(2*Zc) + Zc/ZL) for abs(l*gamma) < 1/4 (< 1 % with the book's impedance-ratio limits); abs(l*gamma) < 1/2 -> no better than 1 part in 10; in the LC region abs(l*gamma) ~ 2*pi*0.35*t_d/t_r: t_d/t_r = 1/6 -> 0.366 -> ~3 % error, 1/3 -> ~25 %, > 1/2 -> no predictive value | use pi model only if t_d <= t_r/6 | t_d, t_r, Zs, Zc, ZL | lumped models of short lines/vias | calc | p.743-746 App.D eq.D.11-D.15 | medium |
| JOHNSON03-2337 | transmission-line | Spectral midpoint of an edge used for lumped-vs-distributed decisions | w_edge ~ 2*pi*0.35/t_r (rad/s) | t_r | LC-region lines | calc | p.745 eq.D.14 | high |
| JOHNSON03-2338 | process | Error-function conventions differ between texts/tools: erf(a) = 2*(erf2(a*sqrt(2)) - 1/2), erfc(a) = 2*(1 - erf2(a*sqrt(2))), erf2 = cumulative standard normal (= pnorm(x,0,1)), Q(a) = 1 - erf2(a); in MathCad versions before 2001 the built-in erf() is unrelated -- use pnorm | erf2(x) = 0.5*(1 + erf(x/sqrt(2))) | tool | BER/jitter/dispersion calculations | calc | p.747-748 App.E Table E.1 | high |

## 2. Formulas & tables (numbers)

### 2.0 Key formulas (quick reference; ids point to the rule rows)

| Quantity | Formula (units) | Rule |
|---|---|---|
| Differential / common / odd / even | d = a - b; c = (a + b)/2; o = d/2; e = c | JOHNSON03-2018, 2019 |
| Pair impedances | Z_diff = 2*Z_odd; Z_common = Z_even/2; uncoupled Z_diff = 2*Z0; Z_odd < Z0 < Z_even | 2026, 2027 |
| Pair skin loss from loop resistance | alpha_R (dB/m) = 8.686*R_AC/(2*Zdiff) | 2046 |
| Short mismatched section reflection | r ~ (t_d/(2*t_r))*(Z2/Zdiff - Zdiff/Z2), valid t_d <= t_r/6 | 2049, 2050 |
| Receiver switching uncertainty | t_unc = (V_IH - V_IL)/(dv/dt) = t_10-90*(V_IH - V_IL)/dV | 2070, 2268 |
| Differential radiation cancellation | a = 20*log10(abs(1 - (r/(r+s))*exp(-j*2*pi*s/lambda))) | 2062 |
| CM current from imbalance | i = dC*dV/dt | 2025 |
| Single-resistor CM residual | V_cm,peak ~ 0.5*dV*dt_skew/t_10-90 | 2079 |
| Both-ends residual | V_2nd/V = r_src*r_load | 2104 |
| Full-reflection length | l_full = t_r*v/2 | 2142 |
| Twisted-pair R_DC, R0 | R_DC = 2/(sigma*pi*(d/2)^2); R0 = (kp/(pi*d))*sqrt(w0*mu/(2*sigma)) | 2126, 2128 |
| Copper tempco | R(T) = R20*(1 + 0.0039*(T - 20)) | 2127 |
| Cable IL de-rating | IL(T) = IL20*(1 + k*(T - 20)), k = 0.004 (5e/6), 0.015 (3) | 2170 |
| 10BASE-T pre-emphasis | H(f) = 3/4 - (1/4)*exp(-j*2*pi*f*b) | 2138 |
| Hybrid output | v = x/2 + (y*h)/2 (Zs = Z_T = Zc) | 2149 |
| RFI CM current | i = sqrt(P/Z_common) | 2094 |
| Coax impedance | Z0 = (60/sqrt(er))*ln(d2/d1); min loss at d2/d1 = 3.5911 | 2180, 2194 |
| Coax skin resistance | R0 = 1/(pi*d1*delta1*sigma1) + 1/(pi*d2*delta2*sigma2) | 2184 |
| Coax non-TEM cutoff | fc = 0.293*c/(d2*sqrt(er)) | 2190 |
| Return loss conversions | r = 10^(-RL/20); SWR = (1 + r)/(1 - r); T = sqrt(1 - r^2) | 2207 |
| Fiber risetime chain | t_TP3b = sqrt(t_s^2 + t_fiber^2 + t_LPF^2); t_LPF = 0.35/B_3dB | 2224, 2228 |
| Fiber t_fiber and D | t_fiber = sqrt((0.48*l*1e6/Bm)^2 + (D*l*2.56*lambda_RMS)^2); D = sqrt(((S0/4)*(lc - l0^4/lc^3))^2 + (0.7*S0*lambda_RMS)^2) | 2225, 2226 |
| Dispersion / clock-window penalties | P_D = -10*log10(4*erf2(1.28*t_b/t_TP3b) - 3); P_W = -10*log10(cos(pi*t_w/(2*t_b))) | 2230, 2232 |
| Setup with skew | t_CLK > t_FF,MAX + t_G,MAX + t_SETUP + (t_C1,MAX - t_C2,MIN) | 2250 |
| Multiple source-terminated lines | R_t = Z0 - N*Rs | 2283 |
| Daisy-chain tap reflection / loaded Z | a = dV*(Z0*C/2)/t_r; Z_loaded = Z0*sqrt(C_line/(C_line + C_load)) | 2287, 2289 |
| PLL tracking-error variance | sigma^2 = (1/pi)*int_B^inf S(w) dw | 2296 |
| Jitter at BER | DJ + k(BER)*sigma_RJ <= tolerance (k = 7.131 at 1e-12); p-p = 14.3*sigma | 2300, 2301 |
| RJ/DJ separation | sigma_R^2 = sigma_T^2 - sigma_D^2 | 2299 |
| Clock filter | f_c = 1/(2*pi*sqrt(L*C)); f_par = 1/(2*pi*sqrt(C_L,shunt*L_C,series)) | 2305, 2306 |
| SSO | V_SSO = L_GROUND*d(i_GROUND)/dt | 2329 |
| Loss slope | eta = d(log a_dB)/d(log f): 1/2 skin, 1 dielectric | 2333 |
| Pi-model limit | abs(l*gamma) ~ 2*pi*0.35*t_d/t_r; valid t_d <= t_r/6 | 2336 |
| Via inductance (in., nH) | Lv = 5.08*h*2*ln(s/r); L_MA = 5.08*h*ln(2s/r); L_MB = 5.08*h*ln(s/r); L_MC = 5.08*h*ln(s/(2r)) | 2003-2007 |

### T-6.1 AC resistance and skin-effect loss (at 1 GHz) of selected 100-ohm differential edge-coupled microstrips (p.389, Table 6.1)

Conditions: FR-4 er = 4.3 at 1 GHz; copper 1/2-oz etch + 1/2-oz plating = 1-oz total, sigma = 5.98e7 S/m; conformal soldermask 12.7 um (0.5 mil), er = 3.3. AC parameters at 1 GHz. Method-of-moments magnetic-field simulator, 120 segments/trace, accuracy ~ +/-2 %. v0 = 1/tp = c/sqrt(er_eff), c = 2.998e8 m/s. h = trace height, w = finished plated width, s = finished plated edge-to-edge separation.

| h (mil) | w (mil) | s (mil) | kp | R_AC (ohm/in) | R_AC (ohm/m) | alpha_R (dB/in) | alpha_R (dB/m) | er_eff |
|---|---|---|---|---|---|---|---|---|
| 5 | 8 | 30 | 3.48 | 1.54 | 60.7 | 0.067 | 2.63 | 3.17 |
| 5 | 7 | 11 | 3.17 | 1.57 | 61.7 | 0.068 | 2.68 | 2.97 |
| 5 | 6 | 7 | 3.01 | 1.69 | 66.5 | 0.073 | 2.89 | 2.85 |
| 5 | 5 | 5 | 2.91 | 1.89 | 74.4 | 0.082 | 3.23 | 2.78 |

Other 100-ohm "recommendations" quoted by a reader for 5-mil FR-4 microstrip at 2.4 GHz (unverified; the author rules out 16/16 and flags the two LineCalc results as mutually inconsistent): 5/5, 4/8, 5/8, 6/6.5, 16/16 mil (w/s) (p.386).

### T-6.2 AC resistance and skin-effect loss (at 1 GHz) of selected 100-ohm differential edge-coupled striplines (p.394-396, Table 6.2)

Conditions: all b, h, w, s in mils (b = interplane separation, h = trace height per Fig.6.12, w = width, s = edge-to-edge separation); FR-4 er = 4.3; copper 1/2-oz, sigma = 5.98e7 S/m; values at 1 GHz. Scaling rule: multiply b, h, w, s, t by k -> same Zdiff, R and alpha divide by k (p.392).

| b | h | w | s | R_AC (ohm/in) | R_AC (ohm/m) | alpha_R (dB/in) | alpha_R (dB/m) | Zdiff (ohm) |
|---|---|---|---|---|---|---|---|---|
| 10 | 3 | 3 | 40.0 | 3.50 | 137.8 | 0.152 | 5.99 | 99.0 |
| 10 | 4 | 3 | 7.0 | 3.24 | 127.6 | 0.139 | 5.47 | 100.4 |
| 10 | 5 | 3 | 7.0 | 3.22 | 126.8 | 0.137 | 5.40 | 101.2 |
| 10 | 5 | 4 | 40.0 | 2.76 | 108.7 | 0.126 | 4.95 | 94.6 |
| 14 | 4 | 3 | 5.5 | 3.19 | 125.6 | 0.136 | 5.36 | 101.0 |
| 14 | 4 | 4 | 12.0 | 2.74 | 107.9 | 0.118 | 4.63 | 100.3 |
| 14 | 5 | 3 | 4.5 | 3.14 | 123.6 | 0.135 | 5.31 | 100.1 |
| 14 | 5 | 4 | 7.5 | 2.60 | 102.4 | 0.112 | 4.39 | 100.5 |
| 14 | 5 | 5 | 40.0 | 2.33 | 91.7 | 0.101 | 3.98 | 99.5 |
| 14 | 7 | 3 | 4.5 | 3.11 | 122.4 | 0.132 | 5.19 | 101.8 |
| 14 | 7 | 4 | 6.5 | 2.56 | 100.8 | 0.110 | 4.31 | 100.6 |
| 14 | 7 | 5 | 13.0 | 2.24 | 88.2 | 0.096 | 3.77 | 100.9 |
| 14 | 7 | 6 | 40.0 | 2.01 | 79.1 | 0.091 | 3.59 | 95.0 |
| 20 | 5 | 3 | 4.4 | 3.14 | 123.6 | 0.134 | 5.28 | 101.0 |
| 20 | 5 | 4 | 6.5 | 2.59 | 102.0 | 0.111 | 4.37 | 100.7 |
| 20 | 5 | 5 | 11.0 | 2.27 | 89.4 | 0.097 | 3.84 | 100.6 |
| 20 | 5 | 6 | 40.0 | 2.09 | 82.3 | 0.092 | 3.61 | 98.4 |
| 20 | 7 | 3 | 3.9 | 3.13 | 123.2 | 0.134 | 5.26 | 101.1 |
| 20 | 7 | 4 | 5.2 | 2.55 | 100.4 | 0.109 | 4.29 | 100.9 |
| 20 | 7 | 5 | 7.0 | 2.17 | 85.4 | 0.093 | 3.66 | 100.7 |
| 20 | 7 | 6 | 10.0 | 1.91 | 75.2 | 0.082 | 3.24 | 100.3 |
| 20 | 7 | 7 | 19.0 | 1.75 | 68.9 | 0.075 | 2.96 | 100.7 |
| 20 | 7 | 8 | 40.0 | 1.61 | 63.4 | 0.072 | 2.85 | 96.3 |
| 20 | 10 | 3 | 3.7 | 3.14 | 123.6 | 0.135 | 5.30 | 100.6 |
| 20 | 10 | 4 | 5.0 | 2.54 | 100.0 | 0.108 | 4.25 | 101.6 |
| 20 | 10 | 5 | 6.5 | 2.15 | 84.6 | 0.092 | 3.60 | 101.4 |
| 20 | 10 | 6 | 8.5 | 1.88 | 74.0 | 0.081 | 3.17 | 100.7 |
| 20 | 10 | 7 | 12.0 | 1.68 | 66.1 | 0.072 | 2.85 | 100.5 |
| 20 | 10 | 8 | 25.0 | 1.56 | 61.4 | 0.067 | 2.65 | 100.3 |
| 30 | 5 | 3 | 4.3 | 3.15 | 124.0 | 0.135 | 5.30 | 100.7 |
| 30 | 5 | 4 | 6.3 | 2.60 | 102.4 | 0.111 | 4.38 | 100.7 |
| 30 | 5 | 5 | 10.0 | 2.27 | 89.4 | 0.097 | 3.83 | 100.7 |
| 30 | 5 | 6 | 22.0 | 2.09 | 82.3 | 0.090 | 3.54 | 100.2 |
| 30 | 6 | 3 | 4.0 | 3.14 | 123.6 | 0.134 | 5.27 | 101.0 |
| 30 | 6 | 4 | 5.4 | 2.56 | 100.8 | 0.110 | 4.33 | 100.7 |
| 30 | 6 | 5 | 7.5 | 2.20 | 86.6 | 0.094 | 3.71 | 100.7 |
| 30 | 6 | 6 | 11.2 | 1.96 | 77.2 | 0.084 | 3.31 | 100.6 |
| 30 | 6 | 7 | 20.0 | 1.81 | 71.3 | 0.078 | 3.07 | 100.4 |
| 30 | 7 | 3 | 3.8 | 3.14 | 123.6 | 0.134 | 5.29 | 100.9 |
| 30 | 7 | 4 | 5.0 | 2.56 | 100.8 | 0.109 | 4.31 | 100.9 |
| 30 | 7 | 4.5 | 5.7 | 2.35 | 92.5 | 0.101 | 3.96 | 100.7 |
| 30 | 7 | 5 | 6.5 | 2.17 | 85.4 | 0.093 | 3.67 | 100.6 |
| 30 | 7 | 6 | 8.8 | 1.91 | 75.2 | 0.082 | 3.22 | 100.7 |
| 30 | 7 | 7 | 12.5 | 1.73 | 68.1 | 0.074 | 2.92 | 100.8 |
| 30 | 7 | 8 | 21.0 | 1.60 | 63.0 | 0.069 | 2.72 | 100.5 |
| 30 | 8 | 3 | 3.7 | 3.15 | 124.0 | 0.134 | 5.29 | 101.0 |
| 30 | 8 | 4 | 4.7 | 2.56 | 100.8 | 0.110 | 4.33 | 100.6 |
| 30 | 8 | 5 | 6.0 | 2.17 | 85.4 | 0.093 | 3.66 | 100.7 |
| 30 | 8 | 6 | 7.7 | 1.89 | 74.4 | 0.081 | 3.20 | 100.6 |
| 30 | 8 | 7 | 10.2 | 1.69 | 66.5 | 0.073 | 2.85 | 100.9 |
| 30 | 8 | 8 | 14.0 | 1.55 | 61.0 | 0.066 | 2.62 | 100.6 |
| 30 | 8 | 9 | 23.0 | 1.45 | 57.1 | 0.062 | 2.45 | 100.5 |
| 30 | 8 | 10 | 40.0 | 1.36 | 53.5 | 0.060 | 2.37 | 97.8 |
| 30 | 10 | 3 | 3.6 | 3.16 | 124.4 | 0.135 | 5.30 | 101.2 |
| 30 | 10 | 4 | 4.5 | 2.57 | 101.2 | 0.110 | 4.32 | 101.0 |
| 30 | 10 | 5 | 5.5 | 2.17 | 85.4 | 0.093 | 3.67 | 100.7 |
| 30 | 10 | 6 | 6.8 | 1.89 | 74.4 | 0.081 | 3.19 | 100.7 |
| 30 | 10 | 7 | 8.4 | 1.67 | 65.7 | 0.072 | 2.82 | 100.9 |
| 30 | 10 | 8 | 10.5 | 1.51 | 59.4 | 0.065 | 2.55 | 100.8 |
| 30 | 10 | 9 | 13.5 | 1.38 | 54.3 | 0.059 | 2.34 | 100.6 |
| 30 | 10 | 10 | 19.0 | 1.29 | 50.8 | 0.055 | 2.18 | 100.6 |
| 30 | 10 | 11 | 34.0 | 1.22 | 48.0 | 0.053 | 2.08 | 100.2 |
| 30 | 10 | 12 | 40.0 | 1.15 | 45.3 | 0.052 | 2.03 | 96.4 |
| 30 | 15 | 3 | 3.5 | 3.17 | 124.8 | 0.135 | 5.33 | 101.0 |
| 30 | 15 | 4 | 4.3 | 2.58 | 101.6 | 0.111 | 4.36 | 100.7 |
| 30 | 15 | 5 | 5.3 | 2.18 | 85.8 | 0.093 | 3.65 | 101.2 |
| 30 | 15 | 6 | 6.3 | 1.89 | 74.4 | 0.081 | 3.19 | 100.9 |
| 30 | 15 | 7 | 7.5 | 1.67 | 65.7 | 0.072 | 2.82 | 101.0 |
| 30 | 15 | 8 | 9.0 | 1.50 | 59.1 | 0.064 | 2.53 | 100.9 |
| 30 | 15 | 9 | 11.0 | 1.36 | 53.5 | 0.058 | 2.30 | 101.0 |
| 30 | 15 | 10 | 13.0 | 1.25 | 49.2 | 0.054 | 2.14 | 100.0 |
| 30 | 15 | 11 | 17.0 | 1.17 | 46.1 | 0.050 | 1.98 | 100.3 |
| 30 | 15 | 12 | 25.0 | 1.10 | 43.3 | 0.047 | 1.87 | 100.5 |

Notes: rows with s = 40.0 mil are effectively uncoupled (Zdiff falls below 100 ohm: 94.6-99.0). Consistency check (derived): alpha_R(dB/m) ~ 8.686*R_AC(ohm/m)/200.

### T-6.3 AC resistance and skin-effect loss (at 1 GHz) of selected 100-ohm differential broadside-coupled striplines (p.403, Table 6.3)

Conditions: b, h, w in mils; FR-4 er = 4.3; 1/2-oz copper, sigma = 5.98e7 S/m; 1 GHz. Linear interpolation along b is permitted.

| b (mil) | h (mil) | w (mil) | R_AC (ohm/in) | R_AC (ohm/m) | alpha_R (dB/in) | alpha_R (dB/m) |
|---|---|---|---|---|---|---|
| 14 | 4 | 1.9 | 4.04 | 159.1 | 0.175 | 6.89 |
| 20 | 5 | 3.5 | 2.71 | 106.5 | 0.117 | 4.61 |
| 30 | 7 | 5.3 | 2.01 | 78.9 | 0.087 | 3.43 |
| 45 | 10 | 9.1 | 1.32 | 52.0 | 0.057 | 2.24 |

Graph anchors: Fig.6.13 (edge-coupled stripline Zdiff vs width 2-7 mil and spacing, b = 24 mil, h = 6 mil, t = 0.68 mil, er = 4.3: strongly coupled below s ~ 9 mil, contours vertical beyond s ~ 24 mil = 4h) (p.390); Fig.6.18 (broadside Zdiff vs width and height, b = 24 mil, t = 0.68 mil, er = 4.3: maximum at h = 6 mil = 25 % of b) (p.400); Fig.6.22 (radiation improvement a vs separation 0.25-25 mm, a ~ -40 dB at 0.5 mm, 1 GHz) (p.406).

### T-6.5 LVDS general-purpose link specifications (p.429, Table 6.5, adapted from ANSI/IEEE P1596.3-1995)

| Side | Signal | Parameter | Conditions | Min | Max | Units |
|---|---|---|---|---|---|---|
| Tx | Voh | Output voltage high, either wire | Rload = 100 ohm +/-1 % | — | 1475 | mV |
| Tx | Vol | Output voltage low, either wire | Rload = 100 ohm +/-1 % | 925 | — | mV |
| Tx | abs(Vod) | Output differential voltage | Rload = 100 ohm +/-1 % | 250 | 400 | mV |
| Tx | Ro | Output impedance, single-ended | Vcm = 1.0 V and 1.4 V | 40 | 140 | ohm |
| Tx | Vos | Output offset voltage | — | 1125 | 1275 | mV |
| Tx | dVos | Change in Vos between 0 and 1 states (defines AC common-mode output voltage) | Rload = 100 ohm +/-1 % | — | 25 | mV |
| Tx | trise, tfall | Vod rise/fall time 20 % to 80 % | Rload = 100 ohm +/-1 % | 300 | 500 | ps |
| Rx | Vi | Input voltage range, either input | abs(Vgpd) < 925 mV | 0 | 2400 | mV |
| Rx | Vidth | Input differential threshold | abs(Vgpd) < 925 mV | -100 | +100 | mV |
| Rx | Vhyst | Input differential hysteresis (Vidthh - Vidthl) | — | 25 | — | mV |
| Rx | Rin | Receiver differential input impedance | — | 90 | 110 | ohm |
| Rx | Cin | Input capacitance | not specified | — | — | — |
| Impl. | — | Pcb skew allocation | worst case | — | 50 | ps |

Derived (p.430-436): nominal wire levels 1.0/1.4 V (CM 1.2 V, odd-mode +/-0.2 V, diff +/-0.4 V = 800 mV p-p); AC CM +/-12.5 mV; CM/diff ratio up to 5 %; CM tolerance +/-925 mV; diff noise margin 150 mV (37 %); worst reflection at Tx -0.428, at Rx -0.053; residual <= 2.25 %; Fig.6.34: Z0 = 100 +/-10 ohm -> <= 5 %, +/-20 ohm -> <= 7 % residual; 50 ps skew ~ 1/4 in. FR-4. National fail-safe example: actual thresholds +/-30 mV; open-input bias 50 mV; connected bias ~25 mV (thresholds +55/+5 mV).

### T-7.1 Popular cables recognized for use as horizontal cabling (p.445, Table 7.1)

| TIA/EIA 568-B.1-2001 cable type | Pairs or strands | ISO/IEC 11801:2002 cable type | Pairs or strands |
|---|---|---|---|
| 100-ohm category 5, 5e, or 6 balanced cabling | 4 | 100-ohm category 5, 5e, 6, or 7 balanced cabling | 2 or 4 |
| 62.5/125-um multimode fiber | 2 | 62.5/125-um multimode fiber | 2 |
| 50/125-um multimode fiber | 2 | 50/125-um multimode fiber | 2 |

Notes: (1) Category 3 still recognized by both but no longer widely available; cat 5/5e perform better and cost no more. (2) 150-ohm STP-A still recognized but no longer widely available; may be dropped. (3) Pairs of 100-ohm balanced cable or strands of fiber.

### T-7.2 Preferred horizontal cable combinations, TIA/EIA 568-B.1-2001 (p.449, Table 7.2)

| Outlet | Cable |
|---|---|
| First outlet | Four-pair, 100-ohm UTP, category 5e or better |
| Second outlet (any one of) | Four-pair 100-ohm UTP cat 5e or better; two-strand 62.5/125-um fiber; two-strand 50/125-um fiber |

Author's recommendation: category 5e four-pair 100-ohm balanced cabling to both outlets (p.449).

### T-7.3 Cable category glossary (p.446-448, §7.3)

| Category / class | Governing document (as cited) | Specified to | Notes |
|---|---|---|---|
| Cat 1, 2, DIW | not sanctioned | — | DIW = classic 24-AWG phone wire pre-1988; basis of cat 3; test each link if unsure |
| Cat 3 | TIA/EIA 568-B.2-2001; IEC 61156-2 (2001-09) | 16 MHz | four gently twisted pairs, PVC insulation; ISO class C |
| Cat 4 (120 ohm, France) | ISO/IEC 11801 (retracted in 11801-2002) | — | never adopted by TIA/EIA-568; somewhat lower attenuation than 100-ohm |
| Cat 5 | EIA/TIA 568-A-1995 | 100 MHz | superseded by cat 5e |
| Cat 5e | TIA/EIA 568-B.2-2001; IEC 61156-5 (2002-03) | 100 MHz | adds ELFEXT spec and return-loss form of impedance spec; ISO class D |
| Cat 6 | TIA/EIA 568-B.2-1-2002; IEC 61156-5 (2002-03) | 250 MHz | marginally better attenuation, much better noise; ISO class E |
| Cat 7 | IEC 61156-5 (2002-03) | 600 MHz | ISO/IEC 11801 only; ISO class F |
| Pairs per outlet | TIA/EIA: 4; ISO/IEC: 2 allowed | — | 4 preferred (Gigabit Ethernet needs all four) |
| Screen naming | ISO/IEC: S = braid, F = foil, SF = both (overall) / UTP or FTP (per element) | — | TIA/EIA: UTP (no screen), ScTP (overall screen) |

### T-8.1 TIA/EIA-568-B UTP and 150-ohm STP-A cable electrical specifications (p.459, Table 8.1)

Maximum allowable attenuation abs(H(w)) in dB per 100 m (328 ft) at 20 C (cable only, not channel).

| f (MHz) | Cat-3 | Cat-5e | Cat-6 | 150-ohm STP-A |
|---|---|---|---|---|
| 0.064 | 0.9 | — | — | — |
| 0.256 | 1.3 | — | — | — |
| 0.512 | 1.8 | — | — | — |
| 0.772 | 2.2 | 1.8 | 1.8 | — |
| 1.0 | 2.6 | 2.0 | 2.0 | — |
| 4.0 | 5.6 | 4.1 | 3.8 | 2.2 |
| 8.0 | 8.5 | 5.8 | 5.3 | 3.1 |
| 10.0 | 9.7 | 6.5 | 6.0 | 3.6 |
| 16.0 | 13.1 | 8.2 | 7.6 | 4.4 |
| 20.0 | — | 9.3 | 8.5 | 4.9 |
| 25.0 | — | 10.4 | 9.5 | 6.2 |
| 31.25 | — | 11.7 | 10.7 | 6.9 |
| 62.5 | — | 17.0 | 15.4 | 9.8 |
| 100.0 | — | 22.0 | 19.8 | 12.3 |
| 200 | — | — | 29.0 | — |
| 250 | — | — | 32.8 | — |
| 300.0 | — | — | — | 21.4 |
| Zc min (ohm) | 85 | 90 (1) | 90 (1) | 135 |
| Zc max (ohm) | 115 | 110 (1) | 110 (1) | 165 |
| t_p ~ 1/v0 max at 10 MHz (ns/m) | 5.45 | 5.45 | 5.45 | 5.45 |

(1) As implied by the return-loss specification. Zc measured on a 100 m length; group delay varies slightly with frequency. (STP-A column alignment reconstructed from OCR: values start at 4.0 MHz; 200/250 MHz blank.)

### T-8.2 Proximity factors for twisted-pair cabling (p.462, Table 8.2)

| Cable | cat-3 | cat-5e | cat-6 | 150-ohm STP-A |
|---|---|---|---|---|
| kp (both conductors) | 2.3 | 2.3 | 2.3 | 2.06 |

### T-8.3 Worst-case transmission-line model parameters for TIA/EIA-568-B cables (p.463, Table 8.3)

Parameters for the Chapter-3 metallic-transmission model (Z0, v0, R_DC, R0 at w0, loss angle theta0 at w0).

| Cable | Z0 (ohm) | v0/c | R_DC (ohm/m) | R0 (ohm/m) | theta0 (rad) | w0/2pi (MHz) | Useful range (MHz) | Max error (dB/100 m) |
|---|---|---|---|---|---|---|---|---|
| cat-3 (DC-inclusive fit) | 85 | 0.6 | 0.1876 | 1.452 | 0.01578 | 10 | 0-16 | 0.012 |
| cat-5e (DC-inclusive) | 85 | 0.6 | 0.1876 | 1.253 | 0.00115 | 10 | 0-100 | 0.032 |
| cat-6 (DC-inclusive) | 90 | 0.6 | 0.1876 | 1.257 | 0.00044 | 10 | 0-250 | 0.161 |
| 150-ohm STP-A (DC-inclusive) | 135 | 0.6 | 0.1142 | 1.134 | 0.00065 | 10 | 0-300 | 0.164 |
| cat-6 (fit from 1 MHz up) | 90 | 0.6 | 0.2902 | 1.208 | 0.00096 | 10 | 1-250 | 0.028 |
| 150-ohm STP-A (fit from 1 MHz up) | 135 | 0.6 | 0.2855 | 1.061 | 0.00113 | 10 | 1-300 | 0.013 |

Notes: the >= 1 MHz fits raise R_DC and lower R0 to mimic the TIA/EIA 1/sqrt(f) term near 1 MHz (sacrificing correct DC resistance). Nominal (not worst-case) cat-3 values: R_DC = 0.1701 ohm/m, R0 = 1.189 ohm/m (p.461-462).

### T-8.4 (Structural) return loss for UTP and 150-ohm STP-A, worst pair (p.479, Table 8.4; f in MHz; from TIA/EIA-568-B.2-2001 and -B.2-1)

| Cable | Frequency range (MHz) | Minimum (structural) return loss (dB) |
|---|---|---|
| cat-3 (structural return loss) | 1 <= f <= 10 | 12 |
| cat-3 | 10 <= f <= 16 | 12 - 10*log10(f/10) |
| cat-5e (return loss) | 1 <= f <= 10 | 20 + 5*log10(f) |
| cat-5e | 10 <= f <= 20 | 25 |
| cat-5e | 20 <= f <= 100 | 25 - 7*log10(f/20) |
| cat-6 (return loss) | 1 <= f <= 10 | 20 + 5*log10(f) |
| cat-6 | 10 <= f <= 20 | 25 |
| cat-6 | 20 <= f <= 250 | 25 - 7*log10(f/20) |
| 150-ohm STP-A | 0 <= f <= 20 | 24 |
| 150-ohm STP-A | 20 <= f | 24 - 10*log10(f/20) |

### T-8.5 NEXT for UTP and 150-ohm STP-A cabling, worst pair (p.488, Table 8.5; TIA/EIA-568-B.2-2001, cables > 100 m; f in MHz)

| Cable | Frequency range (MHz) | Min. allowed NEXT loss (dB) | At 10 MHz (dB) |
|---|---|---|---|
| cat-3 | 0.772-16 | 11.26 - 15*log10(f/100) (form modified to match others) | 26.3 |
| cat-5e | 0.772-100 | 35.3 - 15*log10(f/100) (3 dB tighter than EIA/TIA 568-A cat 5) | 50.3 |
| cat-6 | 0.772-250 | 44.3 - 15*log10(f/100) | 59.3 |
| 150-ohm STP-A | 1-300 | 38.5 - 15*log10(f/100) | 53.5 |

(The text says the last column is at 5 MHz; the printed values match 10 MHz.)

### T-8.6 ELFEXT limits (p.491, Table 8.6; f in MHz; cable only)

| Standard | Cable | Frequency range (MHz) | Min. allowed ELFEXT loss (dB) |
|---|---|---|---|
| EIA/TIA 568-B | cat-5e | 1-100 | 23.8 - 20*log10(f/100) |
| EIA/TIA 568-B | cat-6 | 1-250 | 27.8 - 20*log10(f/100) |
| (assumed by 100BASE-T2/T4, never standardized) | cat-3 | 2-16 | 5.0 - 20*log10(f/100) |

150-ohm STP-A: ELFEXT not applicable (one pair per direction). Power-sum NEXT/ELFEXT (cat 5e/6): <= 3 dB worse than worst pair (cat-6 NEXT: 2 dB) (p.493).

### T-8.7 Systems that pass FCC Class-A radiated emissions limits on UTP (p.497, Table 8.7)

| System | Cable | Active pairs | Data rate (Mb/s) | Baud rate per pair | Max. diff. dV/dt |
|---|---|---|---|---|---|
| IEEE 802.3 10BASE-T | Cat. 3 | 2 | 10 | 20 Mbaud (10 MHz Manchester) | 0.16 V/ns |
| IEEE 802.3 100BASE-TX | Cat. 5 | 2 | 100 | 125 Mbaud (3-level MLT-3), scrambled | 0.33 V/ns |
| IEEE 802.3 1000BASE-T | Cat. 5 | 4 | 1000 | 125 Mbaud (5-level PAM with pre-distortion), scrambled | 0.33 V/ns |

### T-8.9 10BASE-T North American RJ-45 contact assignments (p.499, Table 8.9)

| RJ-45 contact | No internal crossover | With internal crossover | UTP pair | Color |
|---|---|---|---|---|
| 1 | TX+ | RX+ | Pair 3 | GRN/WHT |
| 2 | TX- | RX- | Pair 3 | WHT/GRN |
| 3 | RX+ | TX+ | Pair 2 | ORG/WHT |
| 4 | — | — | Pair 1 | BLU/WHT |
| 5 | — | — | Pair 1 | WHT/BLU |
| 6 | RX- | TX- | Pair 2 | WHT/ORG |
| 7 | — | — | Pair 4 | BRN/WHT |
| 8 | — | — | Pair 4 | WHT/BRN |

### T-8.10 / 8.11 Connecting hardware limits (p.500-501, Tables 8.10-8.11; TIA/EIA-568-B.2; f in MHz)

| Connector | Range (MHz) | Max insertion loss (dB) | Min NEXT loss (dB) | Min FEXT loss (dB) | Min return loss (dB) |
|---|---|---|---|---|---|
| cat-3 | 1-16 | 0.1*sqrt(f) | [OCR: "2.1"] - 20*log10(f/100) (constant illegible; verify in standard) | not specified | not specified |
| cat-5e | 1-100 | 0.04*sqrt(f) | 43.0 - 20*log10(f/100) | 35.1 - 20*log10(f/100) | 20.0 - 20*log10(f/100) for 31.5-100 MHz (flat below) |
| cat-6 | 1-250 | 0.02*sqrt(f) | 54.0 - 20*log10(f/100) | 43.1 - 20*log10(f/100) | 24.0 - 20*log10(f/100) for 50-250 MHz (flat below) |
| 150-ohm STP-A | 1-300 | 0.025*sqrt(f) | 46.5 - 20*log10(f/100) | — | 20.1 - 20*log10(f/100) for 16-300 MHz (flat below) |

### T-9.2 Shielded DB-9 contact assignments, two-pair 150-ohm STP-A (p.511, Table 9.2; reconstructed from OCR)

| Contact | No internal crossover | With internal crossover | Wire color |
|---|---|---|---|
| 1 | Receive+ | Transmit+ | Orange |
| 5 | Transmit+ | Receive+ | Red |
| 6 | Receive- | Transmit- | Black |
| 9 | Transmit- | Receive- | Green |
| Shell | Chassis | Chassis | Cable sheath |

Pairs are [1,6] and [5,9]; contacts 2, 3, 4, 7, 8 unused. Shielded DB-9 = 9-pin D-subminiature shielded = EIA/TIA 574:1990 Section 2 (Molex housing example 82034-0010) (Table 9.1).

### T-10.1 Selected Belden coaxial cable types (p.514, Table 10.1)

| Belden type | Class | Jacket OD (in.) | Conductor stranding (AWG) | Conductor composition | Dielectric |
|---|---|---|---|---|---|
| 8216 | RG-174/U | 0.110 | 7 x 34 | Bare copper-plated steel | Polyethylene |
| 84316 | RG-316/U | 0.098 | 7 x 33(?) (OCR unclear) | Copper-plated steel with silver coating | TFE Teflon |
| 8259 | RG-58A/U | 0.193 | 19 x 32 | Tinned copper | Polyethylene |
| 8240 | RG-58/U | 0.193 | 20 solid | Bare copper | Polyethylene |
| 84303 | RG-303/U | 0.170 | 18 solid | Copper-plated steel with silver coating | TFE Teflon |
| 8237 | RG-8/U | 0.405 | 7 x 21 | Bare copper | Polyethylene |

### T-10.2 Electrical specifications for selected Belden coaxial cables (p.516, Table 10.2)

Attenuation in dB/100 m at 20 C (cable only, not channel).

| f (MHz) | 8216 | 84316 | 8259 | 8240 | 84303 | 8237 |
|---|---|---|---|---|---|---|
| 1 | 6.23 | 3.93 | 1.38 | 0.98 | 1.11 | 0.52 |
| 10 | 10.82 | 8.85 | 4.92 | 3.61 | 3.61 | 1.84 |
| 50 | 19.02 | 18.36 | 12.13 | 8.20 | 8.85 | 4.26 |
| 100 | 27.5 | 27.2 | 17.7 | 12.5 | 12.8 | 6.2 |
| 200 | 41.0 | 39.3 | 26.6 | 18.4 | 18.4 | 9.2 |
| 400 | 62.3 | 57.4 | 40.7 | 27.5 | 26.9 | 13.8 |
| 700 | 88.5 | 77.7 | 58.0 | 38.4 | 36.1 | 19.3 |
| 900 | 101.6 | 89.5 | 69.2 | 44.9 | 41.0 | 22.6 |
| Z0 min (ohm) | 48 | 48 | 48 | 49.5 | 48 | 48 |
| Z0 max (ohm) | 52 | 52 | 52 | 53.5 | 52 | 52 |
| v/c nominal | 0.66 | 0.695 | 0.66 | 0.66 | 0.695 | 0.66 |

(Column order inferred from Table 10.4, whose v0/c and Z0 entries match.)

### T-10.3 Conductivity of common conductor materials (p.518, Table 10.3)

| Material | Conductivity (S/m) |
|---|---|
| Annealed copper as prepared for ordinary wires | 5.80e7 |
| Aluminum as prepared for ordinary wires and foil shields | 3.54e7 |
| Solder-tinned copper (surface conductivity) | 1.54e7 |
| Silver (pure) | 6.29e7 |
| Steel, E.B.B. | 0.96e7 |
| Steel, B.B. | 0.84e7 |

Note: relative permeability of "ordinary" steel ranges 100 to 10,000 or more (large skin-depth variation).

### T-10.4 Worst-case transmission-line parameters for selected Belden coax (p.519, Table 10.4; optimized for 1-1000 MHz)

| Parameter | 8216 | 84316 | 8259 | 8240 | 84303 | 8237 |
|---|---|---|---|---|---|---|
| Z0 (ohm) | 50 | 50 | 50 | 51.5 | 50 | 50 |
| v0/c | 0.660 | 0.695 | 0.66 | 0.660 | 0.695 | 0.66 |
| R_DC (ohm/m) | 0.353 | 0.297 | 0.0488 | 0.0463 | 0.0676 | 0.0102 |
| R0 (ohm/m) | 0.932 | 0.948 | 0.533 | 0.395 | 0.418 | 0.206 |
| theta0 (rad) | 0.00205 | 0.00099 | 0.00210 | 0.00112 | 0.00066 | 0.00005 |
| w0 (rad/s) | 2*pi*1e7 | 2*pi*1e7 | 2*pi*1e7 | 2*pi*1e7 | 2*pi*1e7 | 2*pi*1e7 |

### T-10.5 Selected coaxial connector families (p.533, Table 10.5)

| Size | Nominal cable OD (in.) | Quick-disconnect (bayonet) | Max freq. | Threaded | Max freq. |
|---|---|---|---|---|---|
| Standard | .060 to .425 | C | 4 GHz | N | 10 GHz |
| Miniature | .060 to .425 | BNC | 4 GHz | TNC | 10 GHz |
| Subminiature | .060 to .141 | SMB | 4 GHz | SMA, SMC | 10 to 30 GHz |

### T-10.6 SWR and return-loss conversions for connectors (p.534, Table 10.6; sine-wave excitation)

SWR = (1 + r)/(1 - r); RL = -20*log10(r); transmission = sqrt(1 - r^2).

| RL (dB) | r | SWR | sqrt(1-r^2) | RL (dB) | r | SWR | sqrt(1-r^2) |
|---|---|---|---|---|---|---|---|
| 1 | 0.8913 | 17.39 | 0.4535 | 16 | 0.1585 | 1.377 | 0.9874 |
| 2 | 0.7943 | 8.724 | 0.6075 | 17 | 0.1413 | 1.329 | 0.9900 |
| 3 | 0.7079 | 5.848 | 0.7063 | 18 | 0.1259 | 1.288 | 0.9920 |
| 4 | 0.631 | 4.419 | 0.7758 | 19 | 0.1122 | 1.253 | 0.9937 |
| 5 | 0.5623 | 3.57 | 0.8269 | 20 | 0.1000 | 1.222 | 0.9950 |
| 6 | 0.5012 | 3.01 | 0.8653 | 21 | 0.0891 | 1.196 | 0.9960 |
| 7 | 0.4467 | 2.615 | 0.8947 | 22 | 0.0794 | 1.173 | 0.9968 |
| 8 | 0.3981 | 2.323 | 0.9173 | 23 | 0.0707 | 1.152 | 0.9975 |
| 9 | 0.3548 | 2.1 | 0.9349 | 24 | 0.0631 | 1.135 | 0.9980 |
| 10 | 0.3162 | 1.925 | 0.9487 | 25 | 0.0562 | 1.119 | 0.9984 |
| 11 | 0.2818 | 1.785 | 0.9595 | 26 | 0.0501 | 1.106 | 0.9987 |
| 12 | 0.2512 | 1.671 | 0.9679 | 27 | 0.0446 | 1.094 | 0.9990 |
| 13 | 0.2239 | 1.577 | 0.9746 | 28 | 0.0398 | 1.083 | 0.9992 |
| 14 | 0.1995 | 1.499 | 0.9799 | 29 | 0.0354 | 1.074 | 0.9994 |
| 15 | 0.1778 | 1.433 | 0.9841 | 30 | 0.0316 | 1.065 | 0.9995 |

### T-11.1 Standard attenuation and modal bandwidth specifications for dual-wavelength multimode fiber (p.553, Table 11.1, adapted from IEC 793-3 with additions)

Attenuation categories (max, dB/km):

| Category row | A1b 62.5/125 um @850 nm | A1b @1300 nm | A1a 50/125 um @850 nm | A1a @1300 nm |
|---|---|---|---|---|
| 1 | 3.5 | 1.5 | 2.7 | 1.0 |
| 2 | 3.2 | 0.9 | 2.5 | 0.8 |
| 3 | 3.0 | 0.7 | 2.4 | 0.6 |

Modal bandwidth categories (MHz-km, 850/1300 nm) -- OCR row alignment partly uncertain:

| A1b 62.5/125 um | A1a 50/125 um |
|---|---|
| 160/200 | 200/400 |
| **160/500** (IEEE 802.3z design value) | 200/600 |
| 200/200 | **400/400** (IEEE 802.3z design value) |
| 200/400 | 400/600 |
| 200/500 (1) | 400/800 |
| 200/600 | 400/1000 |
| 250/1000 (?) | 400/1200 |
| 300/800 (?) | 400/1500 |
| — | 500/500 (2) |
| — | 600/1000 |

(1) Specified in ISO/IEC 11801 but not part of IEC 793-3. (2) Common specification of the predominant 50/125-um manufacturer, not part of IEC 793-3. Future: 50/125-um fiber with 2500 MHz-km suggested for 10-Gigabit Ethernet (1999) (p.552).

### T-11.2 Parameters required for fiber dispersion calculations (p.556, Table 11.2)

| Name | Meaning | Units |
|---|---|---|
| t_s | Source rise/fall time (10-90 %) | ps |
| t_b | Source baud interval | ps |
| t_w | Clock window at receiver | ps |
| Bm | Fiber modal bandwidth | MHz-km |
| l | Fiber length | km |
| lambda_RMS | Source RMS spectral width | nm |
| D | Fiber chromatic dispersion constant | ps/nm-km |
| lambda_0 (if D unknown) | Zero-dispersion wavelength | nm |
| S0 (if D unknown) | Dispersion slope | ps/nm^2-km |
| lambda_c (if D unknown) | Source center wavelength | nm |

### T-11.2a FDDI dispersion-penalty worked example (p.565-566; typical datasheet values, not FDDI worst case)

| Quantity | Value |
|---|---|
| Source rise/fall t_s | 3500 ps (10-90 %) |
| Source baud interval (min) t_b | 7500 ps |
| Clock window t_w | 2000 ps |
| Fiber modal bandwidth Bm | 500 MHz-km |
| Fiber length L | 2 km |
| Source FWHM spectral width | 140 nm (lambda_RMS = 140/2.35 = 59.6 nm) |
| Zero-dispersion wavelength lambda_0 | 1300 (min) - 1350 (max) nm |
| Dispersion slope S0 | 0.11 ps/nm^2-km |
| Source center wavelength lambda_c | 1320 (min) - 1360 (max) nm |
| LPF bandwidth B_LPF | 87.5 MHz |
| LPF risetime t_LPF = 0.35e6/B_LPF | 4000 ps |
| Overall risetime t_TP3b | 6119 ps (10-90 %) |
| Dispersion penalty P_D | 1.154 dB optical |
| Clock window penalty P_W | 0.393 dB optical |

(Consistency check derived here: D_worst = 7.69 ps/nm-km at lambda_0 = 1300, lambda_c = 1360; chromatic 2347 ps; modal 1920 ps; fiber 3032 ps.)

### T-11.3 Multimode LED optical power budget (p.567, Table 11.3; typical FDDI datasheet values)

| Line | Item | Value | Units |
|---|---|---|---|
| 1 | TX power (min) | -20 | dBmW |
| 2 | Guaranteed RX sensitivity | -31 | dBmW |
| 3 | Power budget (line 1 less line 2) | 11 | dB |
| 4 | Cable losses (2 km at 2 dB/km) | 4.0 | dB |
| 5 | Connector and splice losses (4 x 0.5 dB) | 2.0 | dB |
| 6 | Dispersion penalty P_D | 1.2 | dB |
| 7 | Clock window penalty P_W | 0.4 | dB |
| 8 | Extinction ratio penalty | 0.0 | dB |
| 9 | Other penalties (laser links) | n/a | dB |
| 10 | Total losses and penalties | 7.6 | dB |
| 11 | Power margin | 3.4 | dB |

### T-11.4 Common fiber-optic connectors (p.575, Table 11.4)

| Connector | Standard designations | Notes |
|---|---|---|
| Duplex SC | duplex SCFOC/2.5; EIA/TIA 604-3; IEC 874-14 | ISO-preferred connector for future facilities designs; smallest footprint; only connector for Gigabit Ethernet |
| ST | BFOC/2.5; EIA/TIA 604-2 | separate connectors for TX and RX |
| FDDI fiber-MIC | ISO/IEC 9314-3 | unique to FDDI equipment |
| Emerging (2002) | 3M Volition VF-45 (ANSI/TIA/EIA 604-7); Siemens MT-RJ | RJ-45-sized |

### T-12.1 Specifications for selected clock repeaters (p.591, Table 12.1) -- LOW CONFIDENCE (column headers illegible in OCR)

Row values as parsed; first column assumed number of outputs, second output-to-output skew (ps), third part-to-part uncertainty (ps), last column assumed maximum frequency (MHz); fourth column unidentified.

| Part | Technology | Output drive | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 |
|---|---|---|---|---|---|---|---|
| Vitesse VSC6110 | GaAs | 50-ohm diff. | 4 | 50 | — | — | 1250 |
| AZ10E111 | 5V-ECL | 50-ohm diff. | 9 | 75 | 150 | 250 | 500 |
| Fairchild 100310 | 5V-ECL | 50-ohm diff. | 8 | 50 | 400 | 275 | 750 |
| AMCC S3LV308 | BiCMOS | 65-75 ohm | 20 | 350 | 500 | 1500 | 100 |
| IDT 5T907 | 2.5V CMOS | +/-8 mA, short lines only | 10 | 25 | 300 | — | 250 |
| IDT CSPT857A | 2.5V CMOS PLL | 60-ohm diff. | 10 | 75 | 100 | 1000 | 200 |
| Cypress CY2300 | CMOS zero-delay buffer | +/-8 mA, short lines only | 4 | 200 | 400 | — | 66 |

### T-12.2 Propagation delay of typical microstrip traces vs stripline (p.598, Table 12.2)

FR-4 er = 4.30 at 1 GHz; 1-oz copper (incl. plating), sigma = 5.98e7 S/m; conformal soldermask 12.7 um (0.5 mil), er = 3.3. v0 = 1/t_p = c/sqrt(er_eff), c = 2.998e8 m/s.

| Geometry | h (mil) | w (mil) | Impedance (ohm) | er_eff | Speed vs stripline (derived) |
|---|---|---|---|---|---|
| Microstrip | 3 | 3 | 59.6 | 3.14 | +17 % |
| Microstrip | 3 | 4 | 53.0 | 3.19 | +16 % |
| Microstrip | 3 | 5 | 47.8 | 3.24 | +15 % |
| Microstrip | 3 | 6 | 43.6 | 3.28 | +14 % |
| Microstrip | 3 | 7 | 37.1 | 3.37 | +13 % |
| Stripline | any | any | any | 4.30 | reference |

### T-12.3 Common fixed delay elements (p.605, Table 12.3)

| Element | Practical delay range (ps) | Approximate delay uncertainty |
|---|---|---|
| Pcb trace (serpentine delay) | 10-1000 | +/-10 % |
| Ordinary logic gate (each) | 100-10,000 | +/-50 % or more |
| Discrete circuit | 1000-1,000,000 | +/-5 % to +/-20 % depending on quality |

Note: on-chip gate delays are considerably less.

### T-12.4 Gaussian waveform probabilities: ratio of peak deviation to standard deviation vs BER (p.647, Table 12.4)

| BER | 1E-04 | 1E-05 | 1E-06 | 1E-07 | 1E-08 | 1E-09 | 1E-10 | 1E-11 | 1E-12 | 1E-13 | 1E-14 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Peak/sigma | 3.891 | 4.417 | 4.892 | 5.327 | 5.731 | 6.109 | 6.467 | 6.807 | 7.131 | 7.441 | 7.739 |

Peak-to-peak spread between 1E-12 tails = 2 x 7.131 ~ 14.3 sigma (p.656). Extrapolation of RJ measured at 1E-6 to 1E-12: x 1.46 (7/4.8 in Fig.11.19, p.569).

### T-12.5 Parasitic models for power-filter components (p.658, Table 12.5)

| Component | Resistance (ohm) | Inductance | Capacitance |
|---|---|---|---|
| L1 | 0.1 | 1 uH | 100 pF (shunt) |
| R2 (damping) | 2.2 | 1 nH | 1 pF |
| C3, C4 (each) | 0.1 | 0.5 nH | 0.047 uF |

Resulting behavior (Fig.12.61, graph): undamped resonance near 500 kHz; > 20 dB attenuation 10 MHz-1 GHz; parasitic resonance near 1 GHz removed by a 25-mm (~10 nH) trace in series with L1.

## 3. Mechanizable checks

All formulas below were re-computed against the book's worked numbers (FDDI dispersion example, loaded daisy-chain impedance, via inductances, radiation cancellation, UTP reflection budgets, clock-filter resonances) and reproduce them. erf2(x) denotes the cumulative standard normal, erf2(x) = 0.5*(1 + erf(x/sqrt(2))).

### 3.1 Differential pairs and differential impedance

`CHECK-diff-impedance-geometry`: inputs per pair (config {microstrip, edge-stripline, broadside}, h, w, s, t, b (mil), er, Z0_single (ohm, from solver), Zdiff_target (ohm)) -> (a) feasibility: Z0_single >= Zdiff_target/2 (otherwise no spacing works); (b) uncoupled estimate Zdiff ~ 2*Z0_single if s >= 4*h (coupling reduction < 6 %); (c) for 100-ohm targets on FR-4 (er = 4.3) look up/interpolate Tables T-6.1/T-6.2/T-6.3 after geometric scaling k = b_design/b_table (multiply h, w, s, t by k; Zdiff unchanged; R_AC and alpha divide by k); (d) if s < 4*h the width must be reduced vs the uncoupled width (Zdiff falls monotonically with s) -> pass if abs(Zdiff_est - Zdiff_target)/Zdiff_target <= tolerance (coupon-verified) -> margin = tolerance - error -> rows JOHNSON03-2026, 2027, 2028, 2034, 2035, 2036, 2039, 2040, 2044, 2045, 2058, 2032.

`CHECK-pair-skin-loss`: inputs (R_AC ohm/m at 1 GHz from table, length m, budget dB) -> alpha_R(dB/m) = 8.686*R_AC/(2*100); loss = alpha_R*L*sqrt(f/1 GHz) (skin region) -> pass if loss <= budget -> margin = budget - loss -> rows 2046, 2045, 2042.

`CHECK-intrapair-skew`: inputs (per pair: delay_P, delay_N (s) incl. connector skew, number of net left vs right 90-deg turns n_L - n_R, pitch p (in.), t_pd (s/in.), corner style {square 2p, chamfer 1.65p, round 1.57p}, t_r, driver skew (default 0.1*t_r), CM balance ratio (e.g. 1/1000 for 100BASE-TX)) -> skew = abs(delay_P - delay_N) + abs(n_L - n_R)*k_corner*p*t_pd -> pass if skew <= t_r/20 (layout target; <= t_r/10 hard limit) AND skew <= max(driver skew, balance_ratio*t_r) where applicable -> margin = t_r/20 - skew -> rows 2041, 2072, 2085, 2086, 2087, 2088, 2109, 2067.

`CHECK-pair-split-reflection`: inputs (Zdiff, Z2 of separated/necked section, section delay t_d, t_r) -> r = (t_d/(2*t_r))*(Z2/Zdiff - Zdiff/Z2) -> pass if abs(r) <= reflection budget AND t_d/t_r <= 1/6 (else simulate) -> margin = budget - abs(r) -> rows 2049, 2050, 2047.

`CHECK-diff-emission-cap`: inputs (s (m), f_max (Hz), driver CM/diff ratio x (e.g. 0.01, 1/16, 0.0625)) -> a_DM = 20*log10(abs(1 - (r/(r+s))*exp(-j*2*pi*s/lambda))), r = 10 m; achievable improvement = max(a_DM, 20*log10(x)) -> flag spacing tighter than 0.5 mm justified only for non-EMI reasons -> rows 2062, 2063, 2064, 2100.

`CHECK-common-mode-range`: inputs (receiver V_cm,min/max, driver Vol/Voh, worst ground shift V_gpd, CM noise) -> V_in,min = Vol - abs(V_gpd) - V_cmnoise, V_in,max = Voh + abs(V_gpd) + V_cmnoise -> pass if V_cm,min <= V_in,min and V_in,max <= V_cm,max (LVDS: abs(V_gpd) <= 925 mV) -> margin = min(V_in,min - V_cm,min, V_cm,max - V_in,max) -> rows 2023, 2101, 2092.

`CHECK-diff-noise-margin`: inputs (abs(Vod,min), abs(V_threshold,max), crosstalk/ringing budget) -> NM = abs(Vod,min) - abs(V_th,max) (LVDS 250 - 100 = 150 mV) -> pass if NM >= noise budget -> margin = NM - budget -> rows 2102, 2071.

`CHECK-cm-conversion`: inputs (capacitive imbalance dC, per-wire swing dV, transition time t_s; CMRR dB, supply ripple) -> i_cm = dC*dV/t_s; V_eq = V_ripple*10^(CMRR/20) -> flag i_cm >= ~100 uA on exposed cables (2 pF at 10BASE-T levels = 160 uA fails) -> rows 2025, 2024, 2016.

`CHECK-diff-termination-cm`: inputs (termination topology, driver CM output impedance, line delay t_line, clock period T, intrapair skew dt, t_10-90, dV) -> single-resistor DM-only termination requires a source with CM termination; V_cm,peak = 0.5*dV*dt/t_10-90; flag abs(t_line - T/4) small when CM unterminated at both ends -> rows 2078, 2079, 2080, 2081, 2082.

`CHECK-u-turn`: inputs (pairs crossing plane gaps: gap width, pair spacing, Zdiff, t_r, stitching present?) -> tau = L_U/Zdiff (L_U ~ 10 nH for 0.1 in. x 0.1 in.) -> pass if stitching/caps adjacent OR tau << t_r (e.g. tau <= t_r/10) -> rows 2083, 2084.

`CHECK-lvds-link`: inputs (Ro range, Rin range, Z0 and tolerance, external terminator value/tolerance/package, pcb skew between any two signals) -> r_src = (Ro - Z0)/(Ro + Z0), r_load = (Rin - Z0)/(Rin + Z0); residual = max abs(r_src*r_load) over corners -> pass if residual <= 5 % (Z0 = 100 +/- 10 ohm) and skew <= 50 ps and terminator 100 ohm +/- 10 %, <= 0805 -> rows 2098, 2099, 2104, 2105, 2106, 2108.

### 3.2 Cabling and link budgets

`CHECK-cable-loss-vs-sensitivity`: inputs (cable type (Table T-8.1 UTP / T-10.2 coax / T-11.1 fiber), length m, f_eval (MHz; e.g. max alternation frequency or Nyquist), temperature C, number of connectors n_c and their category, transmitter amplitude or power, receiver allowed loss / sensitivity, extra penalties) -> A_cable = A_table(f) (log-log interpolation; skin region ~ sqrt(f)) * L/100 m; A_T = A_cable*(1 + k*(T - 20)), k = 0.004 (cat 5e/6), 0.015 (cat 3); A_conn = n_c*k_c*sqrt(f) (0.1/0.04/0.02/0.025 for cat 3/5e/6/STP-A); A_total = A_T + A_conn + 2 dB model margin (or +10-20 % length) -> pass if A_total <= allowed loss and (unequalized) A(f_max_alt) - A(f_min_alt) <= 3.5 dB; for fiber: margin = (P_TX,min - S_RX) - (cable dB/km*L + connectors + P_D + P_W + P_ER + other) >= 3 dB -> margin in dB -> rows 2133, 2135, 2136, 2137, 2167, 2170, 2114, 2235, 2236, 2237, 2188 (coax model; data in T-10.2).

`CHECK-cable-reach`: inputs (application topology) -> pass if horizontal length <= 100 m, taps = 0, transition points <= 4, category mix -> min category, cat-3 baud <= ~25 Mbaud, no cat-3 PVC above 40 C -> rows 2111, 2112, 2143, 2115, 2125, 2121.

`CHECK-reflection-noise-budget`: inputs (segment impedance ranges, transceiver impedance tolerance, segment losses (dB), t_r, v) -> r_i = (Z_i+1 - Z_i)/(Z_i+1 + Z_i) at worst corners; sections shorter than l_full = t_r*v/2 scaled by length/l_full; far-end noise = sum of magnitudes of all second-order paths (each path = r_a*r_b*path losses); near-end (full duplex) = sum of first-order paths -> SNR = signal_loss - noise -> pass if SNR >= receiver requirement -> rows 2141, 2142, 2144, 2145, 2146, 2147. Regression: 105/85/115/85/105 ohm, J1 = J2 = -1 dB, S1 = -10 dB -> far-end -42.2 dB (SNR 30.2 dB), near-end -17.1 dB (SNR 5.1 dB).

`CHECK-crosstalk-budget-utp`: inputs (category, f (MHz), number of disturbers, alien devices?, receiver bandwidth B) -> NEXT_loss(f) = A_cat - 15*log10(f/100) (A = 11.26/35.3/44.3/38.5 for cat 3/5e/6/STP-A); ELFEXT_loss = 23.8 (5e) / 27.8 (6) - 20*log10(f/100); power sum = worst + 3 dB (cat 6 NEXT +2 dB); open-far-end case +12 dB; alien = 264 mV*(B/15 MHz) -> pass if total noise <= SNR budget -> rows 2152, 2153, 2154, 2155, 2156, 2158.

`CHECK-rfi-budget`: inputs (cable category, receiver LPF cutoff, environment) -> V_rfi = 40 mV if f_LPF <= 27 MHz else 200 mV (cat 3; 3 V/m); cat 5e -12 dB, cat 6 -17 dB -> pass if receiver noise margin >= V_rfi -> rows 2159, 2160.

`CHECK-coax-cutoff`: inputs (d2 m, er, f_max) -> fc = 0.293*c/(d2*sqrt(er)) -> pass if f_max < fc (with margin) -> margin = fc - f_max -> row 2190. Regression: RG-58, 2.95 mm, er 2.3 -> 19.7 GHz.

`CHECK-coax-impedance`: inputs (d1 (effective, stranded: 2.63d or 4.23d), d2, er) -> Z0 = (60/sqrt(er))*ln(d2/d1); skin-loss factor (1 + d2/d1)/ln(d2/d1) minimized at d2/d1 = 3.5911 -> rows 2180, 2192, 2194.

`CHECK-connector-rl`: inputs (connector RL(f) or SWR(f), t_r, number of connectors) -> r = 10^(-RL/20); SWR = (1 + r)/(1 - r) -> pass if RL >= 17 dB for all f <= 0.5/t_r and connectors impedance-matched above 100 MHz; frequency <= family max (C/BNC/SMB 4 GHz, N/TNC 10 GHz, SMA/SMC 10-30 GHz) -> rows 2204, 2205, 2206, 2207, 2168.

`CHECK-shield-transfer`: inputs (shield bond type, Z_t at f) -> pass if 360-degree bond and Z_t <= 0.1 ohm at 625 MHz (L_eff < 25 pH) for GbE-class links -> rows 2174, 2199.

### 3.3 Fiber

`CHECK-fiber-dispersion`: inputs (t_s, t_b, t_w, DCD_pp, Bm, L, lambda_FWHM or lambda_RMS, lambda_0 range, S0, lambda_c range, B_LPF) -> t_b,eff = t_b - DCD_pp/2; lambda_RMS = lambda_FWHM/2.35; D = max over corners sqrt(((S0/4)*(lambda_c - lambda_0^4/lambda_c^3))^2 + (0.7*S0*lambda_RMS)^2); t_fiber = sqrt((0.48*L*1e6/Bm)^2 + (D*L*2.56*lambda_RMS)^2); t_LPF = 0.35/B_LPF; t_TP3b = sqrt(t_s^2 + t_fiber^2 + t_LPF^2); P_D = -10*log10(4*erf2(1.28*t_b,eff/t_TP3b) - 3); P_W = -10*log10(cos(pi*t_w/(2*t_b,eff))) -> pass if P_D <= 2 dB (<= 3 dB absolute) -> margin = 2 - P_D -> rows 2224, 2225, 2226, 2227, 2228, 2230, 2231, 2232, 2233, 2234. Regression: FDDI example -> t_TP3b = 6119 ps, P_D = 1.154 dB, P_W = 0.393 dB.

`CHECK-fiber-selection`: inputs (wavelength, core, source type, fiber category) -> pass if lambda in a window (770-860, 1270-1355, 1500-1600 nm), SMF never at 850 nm, Bm >= design value (160/500 for 62.5 um; 400/400 for 50 um), surface LED into 50 um adds 2-5 dB -> rows 2213, 2219, 2221, 2246.

### 3.4 Clock distribution and timing

`CHECK-setup-skew-closure`: inputs per launch/capture pair (t_CLK min period incl. oscillator tolerance, t_FF,MAX, t_G,MAX incl. trace, t_SETUP, t_C1,MAX (launch clock path), t_C2,MIN (capture clock path), gate delay t_gate) -> slack = t_CLK + t_C2,MIN - t_SETUP - (t_C1,MAX + t_FF,MAX + t_G,MAX) -> pass if slack >= t_gate (one gate delay) -> margin = slack - t_gate; hold is checked separately (independent of t_CLK) -> rows 2250, 2251, 2252, 2253. Regression: 500-MHz ECL budget 625 + 1160 + 68 + 147 = 2000 ps.

`CHECK-clock-tree-skew`: inputs (tree levels: repeater output-to-output skew, input-to-output uncertainty per cascaded repeater, trace delays per branch (length x t_pd per layer), loads C_L per branch, termination per branch, receiver V_IH/V_IL/dV/t_10-90, layer type per branch) -> skew = sum(input-to-output uncertainty of cascaded parts) + output skew of last repeater + (max - min branch trace delay) + max over branches of Z0*abs(C_L - C_L,mean) (series-terminated) + t_10-90*(V_IH - V_IL)/dV (single-ended) + 0.01*t_pd,branch if microstrip and stripline branches mixed -> pass if skew <= skew budget -> margin = budget - skew; also require every branch terminated, oscillator-to-repeater input spread <= t_r/6 -> rows 2256, 2257, 2258, 2264, 2265, 2266, 2268, 2255, 2278.

`CHECK-source-term-multi`: inputs (Rs driver, Z0, N lines, branch lengths, loads) -> R_t = Z0 - N*Rs -> pass if R_t > 0 and all branch delays/loads equal (within simulation-verified tolerance) -> rows 2283, 2282.

`CHECK-stub-and-tee`: inputs (topology, stub delays, t_r, branch load imbalance) -> pass if split-tee stub delay <= t_r/6 and corner simulation (C_max/L_max vs C_min/L_min) monotonic; tees with long branches flagged for dual-driver redesign -> rows 2284, 2285, 2286.

`CHECK-daisy-chain`: inputs (Z0, raw line delay t_prop, tap C (incl. stub/connector), n taps, tap spacing delay t_tap, t_r, dV, termination R_T, driver VOH/VOL/IOH/IOL) -> a = dV*(0.5*Z0*C)/t_r per isolated tap; Z_loaded = Z0*sqrt(C_line/(C_line + n*C)), C_line = t_prop/Z0 -> pass if t_tap << t_r (uniform), abs(R_T - Z_loaded)/Z_loaded <= 10 %, R_T >= (VOH - VOL)/(IOH - IOL), and a <= allowed nonmonotonic margin -> rows 2287, 2288, 2289, 2290. Regression: 25 cm at 1.44e8 m/s, 5 x 3 pF -> 41.7 ohm; 2.5 V, 3 pF, 50 ohm, 500 ps -> 375 mV.

`CHECK-serpentine`: inputs (section length, pitch, NEXT coefficient k_NEXT from solver, t_r, v) -> t_rt,section = 2*section_length/v -> pass if t_rt,section <= t_r/3 (else distortion) and delay target corrected by up to -4*k_NEXT (multi-section) -> rows 2279, 2280, 2281.

`CHECK-delay-element`: inputs (element type, nominal delay) -> uncertainty = +/-10 % (trace), +/-50 % (gate), +/-5..20 % (RC) -> add to timing margin; trace length per ns = c/sqrt(er)*1e-9 (0.144 m at er 4.3) -> rows 2271, 2272.

`CHECK-jitter-ber`: inputs (tolerance (UI or rad), DJ (worst case), RJ sigma, target BER) -> k = Table T-12.4(BER) (7.131 at 1e-12); pass if DJ + k*sigma_RJ <= tolerance (p-p form: DJ + 2k*sigma) -> margin = tolerance - (DJ + k*sigma) ; RJ measured at 1e-6 scales x1.46 to 1e-12 -> rows 2299, 2300, 2239, 2295.

`CHECK-phase-noise-jitter`: inputs (phase-noise samples L(f) dBc/Hz, PLL tracking bandwidth B, f_clk, jitter spec) -> sigma^2 = 2*int_B^inf 10^(L(f)/10) df (rad^2); jitter_pp(1e-12) = 14.3*sigma/(2*pi) UI -> pass if <= spec (e.g. 0.1 UI p-p) -> rows 2301, 2296.

`CHECK-pll-cascade`: inputs (jitter-transfer peak G_peak (linear) per stage, N stages) -> accumulated = G_peak^N -> pass if G_peak <= 1 (no peaking) for any cascaded/ring application -> row 2294.

`CHECK-fifo-depth`: inputs (frequency offset/instability df/f, clock f, transaction duration T) -> N = (df/f)*f*T cycles -> pass if FIFO depth >= 2N (preload N) -> row 2297.

`CHECK-clock-supply-filter`: inputs (L, C_total, R_damp, C_L,shunt, L_C,series, noise-tolerance curve X(F), measured supply noise V(F)) -> f_c = 1/(2*pi*sqrt(L*C)); f_par = 1/(2*pi*sqrt(C_L,shunt*L_C,series)); required attenuation(F) = V(F)/X(F) -> pass if filter attenuation >= required over the band and a damping resistor or series trace handles f_c and f_par -> rows 2304, 2305, 2306, 2307.

`CHECK-emi-series-termination`: inputs (range of series R giving acceptable waveforms) -> pick R = max acceptable -> rows 2317.

### 3.5 Modeling and simulation validity

`CHECK-model-level`: inputs (t_r, board size, loss at f_knee = 0.5/t_r) -> lossless OK if t_r >= 1 ns and board <= 25 cm and loss(f_knee) <= 10 %; else lossy (skin + dielectric) model; package models required at t_r <= 1 ns; full via/discontinuity modeling at t_r <= 300 ps -> rows 2320, 2324.

`CHECK-lumped-valid`: inputs (element delay t_d, t_r) -> pass if t_d <= t_r/6 (pi/lumped model error ~3 %; 25 % at t_r/3) -> rows 2336, 2337, 2050, 2069.

`CHECK-plane-resonance`: inputs (board max dimension, er, clock period T_clk, t_r) -> t_cross = dim*sqrt(er)/c; flag if 2*t_cross is near T_clk (or its harmonics) or t_cross is not << t_r -> row 2331.

`CHECK-via-crosstalk`: inputs (h, s, r (in.), aggressor dV, Zc, t_r, f) -> Lv = 5.08*h*2*ln(s/r); L_MA = 5.08*h*ln(2s/r); L_MB = 5.08*h*ln(s/r); L_MC = 5.08*h*ln(s/(2r)) (nH); V = L_M*dV/(Zc*t_r) -> pass if V/dV <= crosstalk budget (aggregate all aggressors sharing a return via; half to each end if both-ends terminated) -> rows 2001-2008. Regression: h = s = 0.025, r = 0.003 -> 0.539/0.357/0.269/0.181 nH.

`CHECK-loss-slope`: inputs (attenuation dB at f1, f2) -> eta = log(a2/a1)/log(f2/f1) -> classify ~0.5 skin-effect-limited, ~1 dielectric-limited -> row 2333.

`CHECK-two-port-cascade`: inputs (ordered list of stages: series Z(w), shunt Z(w), lines (Zc(w), H(w))) -> multiply ABCD matrices; gain = 1/M00 (with source/load stages), Zin = M00/M10 (open output) -> use for frequency-domain channel models -> rows 2334, 2335.

## 4. Verification procedures & plots

| # | Property | Plot / procedure (x / y, sweep, corners) | What good looks like / pass criterion | Setup notes | Source |
|---|---|---|---|---|---|
| V1 | Differential impedance vs geometry | x = trace width (mil), y = Zdiff (ohm), family of curves vs edge spacing s (and vs trace height for broadside); 2-D field solver incl. soldermask | contours vertical beyond s ~ 4h (uncoupled); target Zdiff reached at a manufacturable width; broadside maximum near h = 0.25b | FR-4 er = 4.3 at 1 GHz, t = 0.68 mil, b = 24 mil reference stackup | p.390 Fig.6.13; p.400 Fig.6.18 |
| V2 | Impedance coupons | TDR of differential coupons on every panel | coupon Zdiff within the drawing tolerance | fab test | p.389 |
| V3 | Connector differential impedance | Crude TDR: two RG-174 50-ohm coax into mated test boards, far end 100 ohm (1/8-W axial); subtract reference shot with terminator directly on coax | no bump = matched; + bump = connector too high, - bump = too low; use system risetime (not 35 ps) | ground all pins grounded in application | p.408-409 |
| V4 | Intrapair skew / mode conversion | y = common-mode amplitude at receiver vs time; sweep intrapair skew 0..t_r | CM from skew <= 2.5 % of single-ended amplitude when skew <= t_r/20 | simulate or measure with differential probe; include corner turns (2p, 1.65p, 1.57p per 90 deg) | p.390, 419-420 |
| V5 | Differential radiation | x = trace separation s (0.25-25 mm, log), y = cancellation a (dB) at f_max, r = 10 m | ~-40 dB at 0.5 mm and 1 GHz; overall improvement capped at 20*log10(CM ratio) (-24 dB LVDS, -40 dB at 1 %) | theoretical far-field, antenna in board plane | p.406 Fig.6.22 |
| V6 | Local crosstalk onto pairs | x = separation x to nearest aggressor (mil), y = NEXT coefficient (dB), curves: SE aggressor->pair, pair->pair (8 mil and 4 mil intrapair) | crosstalk falls steeply with x; tight coupling buys only ~2-4 dB | stripline, planes 24 mil apart, traces 6 mil above lower plane, 1/2-oz Cu, er = 4.3 | p.412 Fig.6.25 |
| V7 | LVDS residual reflection | x = trace impedance (40-160 ohm), y = worst residual reflection after first incident wave (worst Ro 40/140 ohm, Rin 90/110 ohm) | <= 5 % for 100 +/- 10 ohm, <= 7 % for +/-20 ohm | resistive Tx/Rx; add reactances in time-domain sim | p.433-434 Fig.6.34 |
| V8 | Cable attenuation model fit | x = frequency (log, 1-1000 MHz), y = attenuation dB/100 m: model curve vs standard/vendor points | error <= 0.16 dB/100 m (DC-inclusive fit) or <= 0.03 dB (>= 1 MHz fit) | then add +2 dB flat or +10-20 % length for system sims | p.462-464 Fig.8.2; p.520 Fig.10.3 |
| V9 | Cable step response | x = time (ns), y = normalized step response for 100 m of each cable type | duration scales ~ L^2 (skin-effect limited) | worst-case model parameters (Tables T-8.3, T-10.4) | p.464 Fig.8.3; p.521 Fig.10.4 |
| V10 | Eye pattern vs cable length | eye diagrams at 10, 50, 100, 150 m (x = time in bit intervals, y = V); unequalized vs pre-emphasized | eye usable while A(f_max_alt) - A(f_min_alt) <= 3.5 dB; pre-emphasis extends reach >= 50 % | 10 Mb/s Manchester, 30-ns edges, worst-case cat 3 at 20 C; receiver LPF adds degradation | p.465-470 Fig.8.4-8.9 |
| V11 | Synthetic NEXT / SRL | x = frequency (MHz), y = NEXT loss (dB): Monte-Carlo random-segment model vs spec line | worst trial just grazes the spec (average set 6-12 dB, e.g. 8 dB, below limit) | eq.8.6-8.7 model | p.480-488 Fig.8.21 |
| V12 | Hybrid termination | x = frequency (log), y = Re/Im of Zin for lengths 0.5-5 units; 1st/2nd/3rd-order terminations | Zin tracks Zc down to ~1 Hz (R), 0.1 Hz (2nd), 0.02 Hz (3rd) normalized | normalized RC line R = L = C = 1 | p.483-485 Fig.8.16-8.18 |
| V13 | Fiber dispersion penalty | x = t_TP3b/t_b (UI), y = P_D (dB optical) | P_D <= 2 dB (3 dB = eye half closed) | Gaussian model eq.11.18 | p.563-564 Fig.11.17 |
| V14 | Fiber ISI waveforms | received isolated-1 pattern for t_TP3b/t_b = 0.2..1.0 | pulse amplitude above threshold at mid-baud | eq.11.12 | p.562 Fig.11.16 |
| V15 | Jitter extrapolation | x = relative random jitter magnitude (sigma units), y = complementary cumulative probability (log, 1e-1..1e-15) | RJ(1e-12) = 1.46 x RJ(1e-6); DJ added unscaled | measure DJ with averaged repeating mixed-run pattern | p.568-569 Fig.11.19 |
| V16 | Clock monotonicity | clock waveform at every receiver (2 ns/div) with V_IL/V_IH bands | no ringback or plateau inside V_IL..V_IH on either edge | HyperLynx-style SI sim; fastest corner driver | p.579-581 Fig.12.1-12.3 |
| V17 | Clock delay vs load/length | x = trace length (0-1 in.), y = delay to 75 % Vcc, curves C_L = 0-25 pF; series-terminated vs unterminated | series-terminated: linear, ~+300 ps per 5 pF, parallel curves; unterminated: nonlinear (reject) | t_r = 1 ns, 50 ohm, 180 ps/in., 10-ohm driver | p.600-601 Fig.12.18-12.19 |
| V18 | Tee / split-tee / hairball nets | step response + first 3 cycles of the real clock at each load, at load/length extremes (C_max/L_max vs C_min/L_min), fastest lifetime risetime | monotonic, full amplitude, no residual resonance; if a resonance appears, re-run at f_res, f_res/3, f_res/5 | example 3.3-V CMOS, 10 ohm, 6 nH package, 1 ns, 66/166 MHz | p.619-627 Fig.12.36-12.45 |
| V19 | Daisy-chain | step response at each tap (0-25 cm), driver 500 ps and 1000 ps, termination 50 vs 40 ohm, compensated 40/80-ohm trace | no lumps > nonmonotonic budget; no overshoot when termination = Z_loaded | FR-4 stripline, 5 cm spacing, 3 pF taps | p.629-633 Fig.12.47-12.52 |
| V20 | Serpentine delay | received edge: straight vs 2-section vs 24-section serpentine (500 ps/div) | no NEXT/FEXT plateaus (sections short); measured delay deficit <= 4 x NEXT, corrected in design | coupled-line simulator, lossless, perfect terminations | p.612-615 Fig.12.30-12.32 |
| V21 | PLL jitter transfer | x = modulation frequency (log), y = output/input phase deviation (log-log) | flat tracking region, roll-off above cutoff, no peak (> 0 dB) for cascaded use | phase-modulated reference (rate MR, amplitude MA), scope trigger on output, delay 0.5/MR, divide-by-N output if needed | p.651-652 §12.11.2.1 |
| V22 | PLL/oscillator supply-noise tolerance | x = injected sine frequency F (log, below loop BW to beyond output rate), y = amplitude X giving standard objectionable jitter (e.g. 0.1 period) | smooth curve without dips; overlay measured supply-noise spectrum -> required filtering; no squelch | AC-coupled injection (Fig.12.58: generator 50-ohm terminated, 1 ohm / 0.047 uF network), remove PLL-side bypass caps if needed, test each Vcc pin | p.652-654 Fig.12.58-12.59 |
| V23 | Intrinsic PLL jitter | timing interval analyzer histogram or phase-noise spectrum integrated beyond loop BW | sigma within spec; convert with Table T-12.4 | clean supply and low-jitter reference during test | p.654-656 |
| V24 | Clock supply filter | x = frequency (1e4-1e10 Hz), y = filter gain: undamped vs damped vs with 25-mm series trace | >= 20 dB attenuation 10 MHz-1 GHz, no peak at f_c or near 1 GHz | component parasitics per Table T-12.5 | p.656-658 Fig.12.61 |
| V25 | PDN noise on first boards | scope 50-ohm input via coax soldered to bypass-cap pads, AC-coupled (0.1 uF), several board locations | noise within budget; if tiny, candidate for bypass-cap reduction | < 1 ohm plane impedance allows direct 50-ohm connection | p.659-661 Fig.12.62 |
| V26 | EMI-driven termination choice | simulated transmitted current (mA) vs time for series R = 10..39 ohm, alongside received voltage | pick the largest R with acceptable voltage; current harmonics down 10-20 dB | 30.5-cm 133-MHz clock example | p.671-672 Fig.12.65-12.66 |
| V27 | Simulator correlation | bench vs sim: 20 ft 50-ohm coax, 25-ohm source (50-ohm generator + 50-ohm tee terminator), t_r 10-100 ns | 33 % far-end overshoot matches; then faster circuits with SMA and resistive probe BW >= 3x signal | SPICE step-size doubling test: results unchanged | p.681, 684 |
| V28 | Power-plane resonance | network-analyzer impedance between planes of a double-sided FR-4 mock-up, or distributed plane simulation (voltage map) | no resonance near clock harmonics; caps placed at noise maxima | compare board round-trip delay to clock period | p.699-701 Fig.13.9 |
| V29 | Via crosstalk | V_victim/dV vs aggressor via spacing using L_M formulas; sum aggressors sharing a return via | within crosstalk budget | inductive coupling, both-ends termination halves each end | p.358-359 Fig.5.37-5.38 |

## 5. Pitfalls, failure modes, review checklist

- [ ] Every via group sharing one return via: sum the inductive crosstalk from all aggressors (it aggregates) (p.359).
- [ ] Single-ended noise budget includes reference-pin (ground/Vcc) noise at full value (p.366).
- [ ] Differential legs have equal height, width, thickness, length and equal impedance to every nearby plane/grounded object (p.373, 385, 405).
- [ ] No untwisted/asymmetric wire segment against chassis near LAN magnetics/connector (2 in. fails FCC/EN) (p.372).
- [ ] Capacitive imbalance between legs of a balanced port (magnetics, connector, pads) kept well below 2 pF (2 pF at 10BASE-T levels -> 160 uA CM) (p.379-380).
- [ ] Receiver common-mode input range never exceeded, including transients and ground shift (p.378, 431).
- [ ] Pairs thinned for tight coupling are not split around obstacles without re-widening (split reverts to 2*Z0 of skinny traces) (p.397-399).
- [ ] Required width for tightly coupled pairs is manufacturable (p.397 fn.49).
- [ ] Broadside pairs: both reference planes same net (preferably GND), dense stitching grid, stitching vias near every layer change (p.401-402).
- [ ] Broadside pairs only where routing density requires; check dielectric thickness tolerance and layer registration symmetry (p.402).
- [ ] Differential-impedance test coupons on every panel (p.389).
- [ ] Differential trace spacing tighter than 0.5 mm is not justified for EMI alone (p.407, 435).
- [ ] Open-pin-field connector: both legs of each pair in the same row; isolated pairs separated by grounds (grounds >= signals) (p.408).
- [ ] Known connector intrapair skew compensated elsewhere in layout (p.408 fn.52).
- [ ] Clock pairs have a net-class keep-out from aggressive signals (near-leg coupling is not cancelled) (p.411).
- [ ] Single-resistor differential terminations checked for common-mode termination elsewhere (source-terminated driver or CM terminator); line delay near T_clk/4 with unterminated CM flagged (p.414-416).
- [ ] Pairs crossing plane gaps: gap and pair spacing minimized, return stitching vias or caps adjacent to each trace (p.418).
- [ ] Pair routing floorplan: driver exit direction = receiver entry direction where turn skew matters (p.420-421).
- [ ] Skew compensation placed near the end with the poorer termination (p.421).
- [ ] No metallic bond between chassis on different AC power domains; single-ended intercabinet links carry their own low-inductance ground (coax shield) (p.424-426).
- [ ] CM of a cable not left unterminated at both ends (transformer-coupled at both ends -> CM resonance) (p.427).
- [ ] Final artwork manually checked for skew compliance (e.g. LVDS 50 ps, ~1/4 in. FR-4); do not trust autorouter (p.436).
- [ ] LVDS external terminator: 100 ohm +/-10 %, 0805 or smaller, at receiver pins, small pads; fail-safe bias resistors included in termination value (p.433, 437).
- [ ] LVDS / hysteresis receivers driven by fast edges only (p.432).
- [ ] Mixed-vendor LVDS fail-safe compatibility verified (optional feature) (p.436).
- [ ] Horizontal cable run <= 100 m, no taps/bridges/Y; product works on standard channel spec (p.443).
- [ ] Mixed cabling categories: guaranteed performance = lowest category; no cat-6 jack into cat-5e receptacle (p.450).
- [ ] SNR budget has all impairments + 2 dB (copper) / 3 dB (fiber) margin (p.446).
- [ ] No PVC-insulated (non-plenum) cable in plenum-return air spaces; no cat-3 PVC above 40 C (attics) (p.452-453, 502).
- [ ] Cable loss de-rated for temperature (0.4 %/C cat 5e/6, 1.5 %/C cat 3 above 20 C) in the link budget (p.502).
- [ ] Simulation cable model carries +2 dB flat loss or +10-20 % length margin (p.465, 520).
- [ ] RJ-45 pairs never split across colored pairs; pair substitution consistent at both ends (p.500).
- [ ] External crossover present when both or neither port is marked "X" (p.499, 452).
- [ ] Alien devices on unused pairs of the same jacket either forbidden or budgeted (264 mV at 15 MHz bandwidth) (p.490).
- [ ] Hardware signal-detect rejects self-crosstalk with far end unplugged/powered off (+12 dB NEXT case) (p.489).
- [ ] Full-duplex designs budget near-end echoes (first-order reflections, structural return noise) and NEXT from all pairs (p.475-489).
- [ ] Multi-pair designs de-skew continuously (skew drifts with cable temperature) (p.492).
- [ ] Transformer-coupled links use a DC-balanced code or receiver DC restoration (p.493, 532).
- [ ] Data scrambled (before coding) on cable links above ~100 MHz to avoid radiating pattern harmonics (p.496-497, 529).
- [ ] Differential dV/dt on UTP not above known-good 0.33 V/ns without an emissions plan (p.497).
- [ ] Shielded cable/connector shields bonded 360 degrees to chassis; no pigtails or discrete AC-coupling caps at GHz (p.508-509, 529).
- [ ] STP/ScTP shields only between equipment on the same ground (no inter-domain shield bonds) (p.501, 508).
- [ ] Straddle-mount connector footprint matches stackup (board thickness, signal-to-plane spacing) (p.511).
- [ ] Connector crosstalk never extrapolated beyond its specified band (p.500).
- [ ] Coax connectors impedance-matched above 100 MHz and RL > 17 dB up to 0.5/t_r; count all connectors (p.532-533).
- [ ] Threaded coax connectors on vehicles/vibration; gold or stainless mating surfaces for repeated insertion; BeCu springs (p.533-535).
- [ ] Coax operated below its first non-TEM cutoff fc = 0.293*c/(d2*sqrt(er)) (p.521).
- [ ] Coax shield treatment consistent with signal isolation (direct-connect vs isolated end) (p.530-531).
- [ ] Surface-emitting LED into 50-um fiber: 2-5 dB coupling penalty budgeted (p.554).
- [ ] Fiber strain < 1 part in 1,000; no microbends; connectors kept clean/unscratched (p.537, 541).
- [ ] Fiber optical specs sourced from core manufacturer (not distributor) (p.541).
- [ ] Fiber link has a written worst-case budget (dispersion P_D, clock window P_W, extinction ratio, connectors, cable, laser penalties) with >= 3 dB final margin (>= 6 dB at planning) (p.555-568).
- [ ] Dispersion penalty <= 2-3 dB; if dispersion-limited, do not "fix" with more power (p.563).
- [ ] Duty-cycle distortion subtracted from t_b in dispersion/clock-window calculations (p.564).
- [ ] Gaussian risetime-addition shortcut not used for copper channels (convolve instead) (p.558).
- [ ] Fiber receivers have a signal-detect / max-gain limit so a dark input does not lock onto local crosstalk (p.570).
- [ ] Laser-on-multimode designs copy an existing high-volume standard's launch/noise specs (p.573).
- [ ] Laser-safety labels per IEC 60825-1 on single-mode/laser equipment (p.578).
- [ ] Clock edges monotonic through V_IL..V_IH at every load (no ringback) (p.579-580).
- [ ] Clock skew budget includes repeater output skew, input-to-output (part-to-part) uncertainty of every cascaded repeater, trace skew, receiver threshold uncertainty (p.586-592, 601).
- [ ] Clocks sourced from dedicated repeater packages, not spare ASIC outputs (p.592).
- [ ] PLL/DLL repeaters have vendor-specified supply filtering and a clean reference (p.593, 635).
- [ ] Skew-matched clocks all on stripline or all on microstrip (not mixed) (p.599).
- [ ] Every clock line terminated (series preferred), branches equal in length, impedance, termination and load (dummy caps if needed) (p.590, 599-601).
- [ ] One driver on multiple source-terminated lines only with equal lengths/loads and R_t = Z0 - N*Rs (p.617-618).
- [ ] Tees avoided (or simulated at load/length extremes); split-tee stubs <= t_r/6 and checked for the load-to-load resonance (p.619-627).
- [ ] Daisy-chained clocks: uniform tap spacing << t_r and termination at loaded impedance Z0*sqrt(C_line/(C_line + C_load)) (p.632).
- [ ] Serpentine sections short (round trip <= t_r/3) or spaced to avoid coupling; delay verified in a coupled-line simulator (p.611-616).
- [ ] Every delay adjustment has a written test procedure with limits; adjustable parts glued/clamped (p.607-609).
- [ ] PLLs in cascade (rings, repeaters, chained multipliers) have no jitter-transfer peaking (p.638, 652).
- [ ] Jitter specs split into DJ (worst-case) and RJ (sigma x Table 12.4 factor) (p.647).
- [ ] FIFO between PLL-derived domains sized >= 2N for worst drift N per transaction; reference frequency ratio kept low (p.643-644).
- [ ] PLL supply filter designed from measured noise-tolerance curve vs measured supply noise; no squelch frequencies (p.652-654).
- [ ] Clock-source filter damped at its LC cutoff; parasitic resonance near 1/(2*pi*sqrt(C_Lshunt*L_Cseries)) addressed (p.656-658).
- [ ] No spread-spectrum/modulated clock feeding data-comm transceivers, RF references or PLL CPUs without vendor approval (p.664).
- [ ] Reduced-swing (LVDS/GTL/SSTL) clock traces spaced away from full-swing families (p.669).
- [ ] Series-termination value chosen for minimum current (largest acceptable) on EMI-critical clocks (p.670-672).
- [ ] Vcc/GND noise measured on first boards at several locations (coax on bypass-cap pads) (p.659-661).
- [ ] SI simulator correlated to bench measurements before use; SPICE results stable vs time step (p.681, 684).
- [ ] Lossy line models used when loss at the knee frequency > 10 % (p.683).
- [ ] IBIS models include rising/falling waveforms under loads like the application; SSO not trusted from IBIS summation (p.692-697).
- [ ] Board plane round-trip delay compared with clock period (plane resonance risk) (p.700-701).
- [ ] Pi/lumped models only where t_d <= t_r/6 (p.745-746).

### 5.1 POINTS TO REMEMBER (verbatim boxed lists, by section, pp. 359–701)

OCR checkmark glyphs rendered as "-". The book's collected "Points to Remember" section (pp. 710–730) repeats these lists; entries for §5.5.5.2–§13.9 were cross-checked against it (wording differences noted: §12.9.1 collected version reads "A slow driver can damp the ringing on a hairball network, but it may need to be too slow for your circuit.").

**§5.5.5.2 Via Crosstalk (p.359)**
- Vias that traverse a common stripline cavity (i.e., the space between two reference planes) create crosstalk.
- The crosstalk voltage induced in a victim circuit equals the rate of change of current in the aggressor times the mutual inductance, LM, shared between the two circuits.

**§6.1 Single-Ended Circuits (p.368)**
- The big advantage of single-ended signaling is that it requires only one wire per signal.
- Single-ended signaling falls prey to disturbances in the reference voltage.
- Single-ended signaling is susceptible to ground bounce.
- Single-ended signaling requires a low-impedance common reference connection.

**§6.2 Two-Wire Circuits (p.370)**
- Two-wire signaling renders a system immune to disturbances in distribution of global reference voltages.
- Two-wire signaling counteracts any type of interfering noise that affects both wires equally.
- Two-wire signaling counteracts ground bounce (also called simultaneous switching noise) within a receiver.
- Two-wire signaling counteracts ground shifts in connectors.
- Two-wire signaling works when there is no significant stray returning signal current.

**§6.3 Differential Signaling (p.374)**
- Differential signaling delivers equal but opposite AC voltages and currents on two wires.
- Assuming the layout is symmetrical, any AC currents induced in the reference system by one wire are counteracted by equal and opposite signals induced by the complementary wire.
- Differential pcb traces need not be tightly coupled to be effective.
- Differential signaling markedly reduces radiated emissions.

**§6.4 Differential and Common-Mode Voltages and Currents (p.376)**
- Differential and common-mode signals are used to describe the voltages and currents on a two-wire transmission system.
- Odd-mode and even-mode signals are yet another way to describe the voltages and currents on a two-wire transmission system.
- Differential receivers cancel common-mode noise.

**§6.5 Differential and Common-Mode Velocity (p.377)**
- Microstrips support slightly different propagation velocities for the differential and common modes. The impact of this difference is not very great.

**§6.6 Common-Mode Balance (p.378)**
- Common-mode balance is the ratio of common-mode to differential-mode signal amplitudes.

**§6.7 Common-Mode Range (p.378)**
- Don't violate the common-mode input range specification for a receiver (not even briefly).

**§6.8 Differential to Common-Mode Conversion (p.380)**
- An imbalanced circuit can translate part of a perfectly good differential signal into a common-mode signal, or vice versa.

**§6.9 Differential Impedance (p.382-383)**
- Differential impedance is the impedance measured between two conductors when they are driven in the differential mode.
- Odd-mode impedance is the impedance measured on either of two conductors when they are driven with opposite signals in the differential mode.
- The value of differential-mode impedance is twice the value of odd-mode impedance.
- The differential impedance of two matched, uncoupled transmission lines is double the impedance of either line alone.
- The odd-mode impedance of two matched, uncoupled transmission lines equals the impedance of either line alone.
- Coupling between two parallel pcb traces decreases both differential and odd-mode impedances.
- Common-mode impedance is the impedance measured on two wires in parallel when they are driven together.
- Even-mode impedance is the impedance measured on either of two wires when they are driven with identical signals in the common mode.
- The value of common-mode impedance is half the value of even-mode impedance.

**§6.9.3 Differential Reflections (p.385)**
- Aside from the complications introduced by unbalanced modes, differential transmission lines behave pretty much like single-ended ones.

**§6.10.2 Edge-Coupled Stripline (p.394)**
- Differential traces can be pushed really, really close together. If you do so, compute a new trace width to compensate for the fact that the differential impedance goes down for closely spaced pairs.
- Widely spaced (i.e., loosely-coupled) pairs are not subject to picky, difficult-to-implement spacing and width requirements.
- The most important determiner of skin-effect loss is the trace width.
- An interpair trace separation of four times h yields about a 6% effect on impedance, a small enough value in many cases to simply ignore.
- Matching the elements of each pair to within 1/20 of a risetime limits the common-mode signal contributed by trace skew to less than 2.5% of the single-ended signal amplitude.

**§6.10.3 Breaking Up a Pair (p.399)**
- If you separate elements of a tightly-coupled pair the differential impedance reverts to twice the uncoupled value of Z0.

**§6.10.4 Broadside-Coupled Stripline (p.403)**
- Broadside differential trace impedance is maximized by a trace height equal to 25% of the interplane separation.
- The bottom trace of a broadside-coupled differential pair has some extra delay built in at the endpoints.
- Avoid broadside-coupled traces unless they are made necessary by routing considerations.

**§6.11.1 Matching to an External, Balanced Differential Transmission Medium (p.405)**
- Match the differential characteristic impedance of two pcb traces to the differential characteristic impedance of a balanced cable.
- Make the two pcb traces as symmetrical as possible, with equal impedances to ground.

**§6.11.2 Defeating Ground Bounce (p.405)**
- Differential signaling defeats ground bounce.

**§6.11.3 Reducing EMI with Differential Signaling (p.407)**
- You need not struggle to place ordinary differential digital traces any closer than 0.5 mm (0.020 in.) for any EMI purpose.

**§6.11.4 Punching Through a Noisy Connector (p.407)**
- Subject to the limits of common-mode rejection, ground shifts generated within a connector are totally cancelled within a differential receiver.

**§6.11.5 Reducing Clock Skew (p.411)**
- Differential receivers often have more accurately specified switching thresholds than single-ended receivers.
- Uncoupled differential traces need not follow the same path; they just need to have the same delay.

**§6.11.6 Reducing Local Crosstalk (p.412)**
- Tightly coupling a differential pair delivers only a modest improvement in crosstalk.

**§6.11.8 Differential Clocks (p.414)**
- The benefits of differential signaling apply to multidrop configurations.

**§6.11.9 Differential Termination (p.416)**
- Every long, differential link needs at least one good differential termination and also a reasonable common-mode termination to prevent severe common-mode resonance.

**§6.11.10 Differential U-Turn (p.418)**
- Visualize the propagation of a differential signal as a quad of four currents.

**§6.11.11 Your Layout Is Skewed (p.420)**
- Chamfering or rounding of differential corners does not eliminate skew.

**§6.11.12 Buying Time (p.422)**
- A pair that starts and ends going north has by definition equal numbers of right-hand and left-hand turns.

**§6.12 Intercabinet Applications (p.423)**
- The twisted-pair cable guarantees low crosstalk by virtue of having a different rate of twist on all the pairs within the same jacket.
- Quad cable guarantees low crosstalk by virtue of its unique geometrical alignment.

**§6.12.1 Ribbon-Style Twisted-Pair Cables (p.424)**
- Ribbon cables can use the same twist pitch on every pair because the wires are held in a rigid geometry.

**§6.12.2 Immunity to Large Ground Shifts (p.426)**
- Never introduce a metallic connection between any two frames powered by different AC power sources.
- If you must electrically connect two boxes, make sure that both boxes are served by green-wire grounds connected to the same Earth potential.
- Differential signaling with unshielded cables does not require a direct ground connection between the two ends of the link.

**§6.12.3 Rejection of External Radio-Frequency Interference (RFI) (p.427)**
To get the best RF-rejection performance from your cabling,
- Use a tightly twisted, well-balanced cable. Twisted cables work better than quad cables in this respect.
- Don't scrimp on connectors. Buy and use connectors designed to go with the cable.
- Use well-balanced circuitry for both transmitter and receiver.

**§6.12.4 Differential Receivers Have Superior Tolerance to Skin Effect (p.428)**
- Differential receivers have more accurate switching thresholds than ordinary single-ended logic.

**§6.13.1 LVDS Output Levels (p.430)**
- Normal operating voltages for LVDS logic are 1.2 ± 0.2 V on each wire.

**§6.13.2 Common-Mode Output (p.430)**
- LVDS, like most digital transceivers, is not extraordinarily well balanced.

**§6.13.3 Common-Mode Noise Tolerance (p.431)**
- The common-mode noise tolerance for general-purpose LVDS logic is ±925 mV.

**§6.13.4 Differential-Mode Noise Tolerance (p.431)**
- The high noise margin gives LVDS a built-in natural advantage in combating ringing, overshoot, and crosstalk from like devices.

**§6.13.5 Hysteresis (p.432)**
- Always provide fast-edged inputs to LVDS logic.

**§6.13.6 Impedance Control (p.435)**
- LVDS works best with 100-Ω transmission lines.

**§6.13.7 Trace Radiation (p.435)**
- You need not struggle to place ordinary differential digital traces any closer than 0.5 mm (0.020 in.) for any EMI purpose.

**§6.13.10 Skew (p.436)**
- Always double-check your final artwork to make sure you've met the specifications for skew.

**§6.13.11 Fail-Safe (p.437)**
- Fail-safe features are permitted by the LVDS standard, but not required.

**§7 Generic Building-Cabling Standards (p.442)**
- Any system that connects from room to room, or from building to building, should use generic building cabling.
- Building-cabling standards are evolving rapidly. If you want the latest information, order the latest standards.

**§7.1 Generic Cabling Architecture (p.445-446)**
- Horizontal cabling is the most widely deployed, highest-volume element of the building-cabling architecture.
- New buildings in North America provide two outlets in every work area, with four-pair, 100-Ω UTP, category 5 or better cabling to both outlets.
- Backbone cables are mostly a mix of category 5 cables, multimode fiber (62.5-µm or 50-µm), and some single-mode fiber.
- A weird backbone cabling requirement is a sales obstacle to be overcome. A weird horizontal cabling requirement is a wooden stake in the heart of your project.

**§7.2 SNR Budgeting (p.446)**
- Don't underestimate the complexity of proper SNR budgeting.

**§7.6 Crossover Wiring (p.452)**
- Multi-pair building cables should be installed straight-through with no crossing of the pairs.
- When necessary, an external crossover should be implemented in a short, clearly visible section of cabling and boldly labeled.

**§7.7 Plenum-Rated Cables (p.453)**
- The materials used to make fire-resistant plenum-rated cables are heavy, stiff, and somewhat more expensive than PVC.

**§7.8 Laying Cables in an Uncooled Attic Space (p.453)**
- Cable performance must be de-rated to account for operation at the elevated temperatures commonly found in building attics.

**§8 100-Ohm Balanced Twisted-Pair Cabling (p.458)**
- Cabling standards proliferate faster than bunnies.

**§8.1 UTP Signal Propagation (p.460)**
- Compared to category 3 cabling, categories 5e and 6 higher have progressively tighter twists and better plastic insulation with less dielectric loss at high frequencies. The resulting cables pick up less noise and have a superior frequency response.

**§8.1.2 Adapting the Metallic-Transmission Model (p.465)**
- The many possible combinations of surface plating, types of shielding, and dielectric make it difficult to accurately predict the performance of all twisted-pair cables from the basic information provided on a datasheet.
- The cable model you use for system simulation should either add another 2 dB of fixed, flat loss to the datasheet attenuation or extend the simulated maximum cable length by another 10% to 20%.

**§8.2 UTP Transmission Example: 10BASE-T (p.471)**
- Timing jitter is improved when all received amplitudes are independent of past history.
- Simple fixed pre-emphasis boosts the maximum operational cable length of a Manchester-coded link by at least 50%.
- A more sophisticated adaptive equalizer can extend operation to even greater distances.

**§8.3.1 UTP: Far-End Reflections (p.475)**
- A complete noise budget takes into account all reflections within a cabling system.
- Connectors generate reflections that superimpose on the reflections generated by changes in cable impedance.

**§8.3.2 UTP: Near-End Reflections (p.477)**
- Bidirectional links must tolerate near-end reflections.

**§8.3.2.1 UTP: (Structural) Return Loss (p.480)**
- A specification of structural return loss combined with a specification of the mean value of characteristic impedance is used for old category 3 cables.
- A single specification of cable return loss (as measured with the cable terminated in a 100-Ω load) simultaneously limits both the mean value and local perturbations in cable impedance.

**§8.3.2.2 Modeling Structural Return Loss (p.481)**
- Structural return noise is modeled as a summation of many noise sources with random amplitudes.
- Structural return noise grows at a rate of 15 dB per decade.

**§8.3.3 UTP: Hybrid Circuits (p.487)**
- A hybrid circuit makes possible bidirectional full-duplex transmission through a single channel.
- A sufficiently complex adaptive digital filter can compensate for cable roughness and also cable-transition reflections simultaneously. Such a filter is called an adaptive echo cancellation circuit.

**§8.3.4 UTP: Near-End Crosstalk (p.489)**
- NEXT is modeled as a summation of many noise sources with random amplitudes.
- NEXT grows at a rate of 15 dB per decade.

**§8.3.5 UTP: Alien Crosstalk (p.490)**
- Alien crosstalk comes from devices occupying unused pairs within your cable jacket.

**§8.3.6 UTP: Far-End Crosstalk (p.492)**
- FEXT is modeled as a single noise source with a random amplitude.
- FEXT grows at a rate of 20 dB per decade.

**§8.3.7 Power Sum NEXT and ELFEXT (p.493)**
- Within a single jacket there may be one combination of pairs that press up against the limit for pair-to-pair NEXT or ELFEXT, but not all combinations of pairs may do so.

**§8.3.8 UTP: Radio-Frequency Interference (p.496)**
- The best antidote for RFI is good signal balance.
- A 27-MHz low-pass filter applied to category-3 horizontal cabling should cut RFI to less than 40 mV in most commercial situations.
- Categories 5e and 6 cabling pick up less RFI.

**§8.3.9 UTP: Radiation (p.497)**
- The key to obtaining good radiated performance is good common-mode balance.
- Scrambling spreads the spectral power density of the transmitted signal, reducing the peak radiation.

**§8.4 UTP Connectors (p.500)**
- UTP connectors are cheap, and the performance is outstanding.
- Systems that tolerate polarity reversal greatly simplify installation.

**§8.5 Issues with Screening (p.502)**
- Even though screened cables are heavily favored in Europe, this author does not recommend their use.

**§8.6 Category-3 UTP at Elevated Temperature (p.502)**
- Never use PVC-insulated category 3 cables in an uncooled attic space.

**§9 150-Ohm STP-A Cabling (p.506)**
- Think about 150-Ω STP-A when you need a quick and dirty transceiver for a first product release (or beta-trial).

**§9.2 150-Ω STP-A Noise and Interference (p.507)**
- When 150-Ω STP-A is used in a unidirectional mode it is not subject to near-end reflections, alien crosstalk, or far-end crosstalk.

**§9.3 150-Ω STP-A: Skew (p.508)**
- Inside a 150-Ω STP-A cable, the signal on one wire of a pair might arrive ahead of the signal on the other wire.

**§9.4 150-Ω STP-A: Radiation and Safety (p.509)**
- Pigtail and AC-coupled shields work at audio frequencies, but not at a gigahertz.

**§9.5 150-Ω STP-A: Comparison with UTP (p.509)**
- Customers will not maintain the shields on an STP system.

**§9.6 150-Ω STP-A Connectors (p.512)**
- The equipment-end connector used with FDDI and Ethernet 150-Ω STP-A installations is the shielded DB-9.

**§10 Coaxial Cabling (p.514)**
- The electrical performance of coaxial cable is as good as anything else, but physically, coax is difficult to handle.
- Coaxial cable suffers from an overabundance of standards.

**§10.1 Coaxial Signal Propagation (p.522)**
- A good coaxial cable presents a nearly uniform impedance at all frequencies above the onset of the skin effect.
- Coaxial cables formed from foamed, cellular, or helically-wrapped dielectrics exhibit a faster propagation velocity and less high-frequency loss than their solid-dielectric counterparts.
- The step response duration for a coaxial cable scales roughly in proportion to the square of cable length.

**§10.1.2 Why 50 Ohms? (p.525)**
- A characteristic impedance of approximately 50 Ω minimizes the skin-effect losses in a solid-polyethylene coaxial cable.

**§10.1.3 50-Ohm Mailbag (p.528)**
- Wimpy drivers appreciate higher-impedance transmission lines.
- I consider IBM's selection of 150-Ω for STP-A a goof.
- 50-Ω coax is less sensitive than 75-Ω coax to reflections caused by transceiver taps.

**§10.2.1 Coax: Far-End Reflected Noise (p.528)**
- Coaxial cables are generally manufactured to much tighter impedance standards than UTP cables.

**§10.2.3 Coax: Radiation (p.530)**
- RF susceptibility and radiation in coaxial cables result from imperfections in the shield.

**§10.2.4 Coaxial Cable: Safety Issues (p.532)**
- If you block the direct path of signal current with an isolating device, such as a transformer, optical isolator, or differential receiver, then you are free, as far as signal integrity is concerned, to disconnect the coax ground from your equipment ground.
- A common-mode choke can also block the flow of intercabinet ground current.
- DC-balanced signals are perfectly suited for connection through transformers.

**§10.3 Coaxial Cable Connectors (p.535)**
- Above 100 MHz, you should always match the characteristic impedance of the connector to the cable.
- Contact plating serves to stave off corrosion and eventual failure of the contacts.
- If it goes on a boat, a car, a plane, or anything that moves, use threaded connectors.
- Crimp-style connectors generally superior to the other types for high-frequency work.
- Always specify heat-treated beryllium-copper for critical contact springs.

**§11 Fiber-Optic Cabling (p.538)**
- The bandwidth-carrying capacity of modern fiber-optic cabling greatly exceeds that of any form of copper cabling, an advantage counterbalanced by the high costs and practical difficulties associated with fiber.

**§11.1 Making Glass Fiber (p.539)**
- Glass optical fiber is drawn as one continuous thread from a single cylinder of purified glass called a preform.

**§11.2 Finished Core Specifications (p.541)**
- The key parameter that differentiates fiber in the marketplace is core diameter.

**§11.3 Cabling the Fiber (p.543)**
- The optical properties of the fiber are determined almost entirely by the coated glass core.
- The mechanical properties of the cable are determined almost entirely by the buffer and jacket construction.

**§11.4 Wavelengths of Operation (p.544)**
- The three most popular wavelength windows for glass fiber are (1) 770 nm to 860 nm, (2) 1270 nm to 1355 nm, and (3) 1500 nm to 1600 nm.

**§11.5 Multimode Glass Fiber-Optic Cabling (p.546)**
- The two most popular standard core diameters for multimode glass fiber are 50 µm and 62.5 µm.
- A graded-index multimode fiber higher bandwidth than a step-index multimode fiber of the same core diameter and quality.

**§11.5.1 Multimode Signal Propagation (p.550)**
- Within a multimode fiber, there exist hundreds of different pathways, or modes of propagation.
- The multiple modes cause a step input to gradually disperse in time as it travels down the fiber.
- Dispersion in a multimode fiber is divided into modal dispersion and chromatic dispersion.
- Modal bandwidth is a function of the refractive index profile of the fiber.
- Chromatic dispersion is a function of the material properties of the glass and also the refractive index profile of the fiber.

**§11.5.2 Why Is Graded-Index Fiber Better than Step-Index? (p.552)**
- Carefully grading the profile of the index of refraction greatly improves modal bandwidth.

**§11.5.3 Standards for Multimode Fiber (p.553)**
- Internationally recognized specifications for 50 and 62.5 µm multimode optical fibers are provided by IEC 793-2.

**§11.5.4 What Considerations Govern the Use of 50-micron Fiber? (p.555)**
- Fifty-micron multimode fiber has a generally higher bandwidth and less attenuation than 62.5-µm multimode fiber. These advantages are counterbalanced by the fact that some common LED sources can't couple efficiently into 50-µm core.

**§11.5.5.1 Multimode Dispersion Budget (p.566)**
- Dispersion calculations determine the extent of risetime degradation and estimate the impact that degradation will have on signal reception.

**§11.5.5.2 Multimode Attenuation Budget (p.568)**
- An attenuation budget allocates attenuation among the long continuous runs of fiber cabling, the short fiber jumpers, and the connectors in a typical installation.

**§11.5.6 Jitter (p.569)**
- Fiber-optic transmission systems commonly divide the jitter budget into deterministic jitter and random jitter.

**§11.5.7 Multimode Fiber-Optic Noise and Interference (p.571)**
- Fiber cabling may be immune to crosstalk and RFI, but your fiber-optic receiver is not.

**§11.5.8 Multimode Fiber Safety (p.571)**
- Never look into the end of a fiber.

**§11.5.9 Multimode Fiber with Laser Source (p.573)**
- The use of laser-diodes on multimode fiber depends on subtle, undocumented, and unspecified features of the multimode fiber.

**§11.5.10 VCSEL Diodes (p.574)**
- A VCSEL shines perpendicular to its top surface, just like a surface-emitting LED.

**§11.5.11 Multimode Fiber-Optic Connectors (p.576)**
- No one has yet designed a satisfactory, easy to install, inexpensive fiber-optic connector.
- Optics work well for intersystem connections, but I've not yet seen a cost-effective optical backplane.

**§11.6.1 Single-Mode Signal Propagation (p.578)**
- Single-mode fiber does not suffer from modal dispersion, differential mode delay, modal noise, or mode partition noise.
- The most important optical parameters for a single-mode fiber are the operating wavelength, the attenuation in dB/km, and the chromatic dispersion.

**§12 Clock Distribution (p.582)**
- Clock signals, because they are so fast, so heavily loaded, and so important for system timing, are subject to special requirements.

**§12.1 Extra Fries, Please (p.584)**
- DLL or PLL technology can produce arbitrary, precise, intentional clock skew where and when you need it.

**§12.2 Arithmetic of Clock Skew (p.589)**
- Timing margin measures the slack, or excess time, remaining in each clock cycle.
- Lowering the clock frequency fixes setup problems, but not hold problems.
- Clock skew affects operating speed as much as any other propagation delay.

**§12.3 Clock Repeaters (p.592)**
- The performance of a clock tree structure depends heavily on the input-to-output uncertainty of the clock repeaters.
- Keeping the clock repeater isolated in its own package is a good idea.

**§12.3.1 Active Skew Correction (p.593)**
- A skew-compensated clock repeater architecture does nothing to combat uncertainty in the overall input-to-output delay.
- Actively compensated clock repeaters are highly susceptible to power supply noise.

**§12.3.2 Zero-Delay Clock Repeaters (p.595)**
- A zero-delay clock buffer directly controls the input-to-output uncertainty.

**§12.3.3 Compensating for Line Length (p.596)**
- What you really want is low skew as defined at the points of usage.

**§12.4 Stripline vs. Microstrip Delay (p.599)**
- Given similar dielectrics, signals propagate faster on a microstrip layer than on a stripline layer. For best speed matching, don't mix the two types.

**§12.5 Importance of Terminating Clock Lines (p.601)**
- For low skew, use the same clock drivers everywhere, source-terminate every driver, and use the same length line with the same impedance and the same loading on every trace.

**§12.6 Effect of Clock Receiver Thresholds (p.602)**
- The spread between VIL and VIH creates an uncertainty in the exact moment at which a clock receiver will switch.

**§12.7 Effect of Split Termination (p.605)**
- Resistive loading attenuates the output of a digital driver, but does not change its rise (or fall) time.

**§12.8.3 Automatically Programmable Delays (p.610)**
- Delay elements are built from three basic building blocks: transmission lines, logic gates, and passive lumped circuits.
- A fixed delay cannot cancel variations in board fabrication or active component delay.
- An adjustable delay compensates for actual delays, not just nominal delays, elsewhere in the circuit.
- Whatever form of delay you choose, incorporate its uncertainty in delay into your timing margin calculations.

**§12.8.5 Switchback Coupling (p.616)**
- Avoid long, coupled switchbacks.

**§12.9 Driving Multiple Loads with Source Termination (p.618)**
- A single driver can service two or more source-terminated lines only under limited conditions.

**§12.9.1 To Tee or Not To Tee (p.625)**
- A slow driver can damp ringing, but it may need to be too slow for your circuit.
- Appropriately placed attenuating networks can damp all the oscillatory modes at the expense of shrinking the received signal.
- A weak termination can help reduce, but totally cure, overshoot and ringing.
- Test all combinations of maximum and minimum load capacitance and line length.
- Eventually, someone will inherit your hairball design and try to figure out what you did. Keep it simple.

**§12.9.2 Driving Two Loads (p.627)**
- Hidden within every split-tee network is an unconstrained resonance.

**§12.10 Daisy-Chain Clock Distribution (p.629)**
- Five things reduce the reflection from an isolated, lumped-element capacitive load: slow the risetime, lower the capacitance, lower the characteristic impedance of the trace, isolate the load with a big resistor, or compensate for the capacitance by modulating the trace width.

**§12.10.1 Case Study of Daisy-Chained Clock (p.634)**
- Rules for good daisy-chaining—Uniformly space the loads, with a spacing whose delay is small compared to the signal rise and fall time, and terminate the structure with a resistance that matches the effective impedance of the loaded structure you've built, not just the impedance of the raw trace you started with.

**§12.11 The Jitters (p.636)**
- PLL-based clock generators require a stable, low-jitter reference clock.

**§12.11.1.2 Clock Jitter Propagation (p.640)**
- Any sort of resonance in a PLL, even a tiny one, spells disaster for a highly cascaded system.

**§12.11.1.3 Variance of the Tracking Error (p.643)**
- The variance of the tracking error in a PLL circuit represents all the power in the input reference signal that falls above the tracking range of the PLL.

**§12.11.1.4 Clock Jitter in FIFO-Based Architectures (p.644)**
- A large ratio between the reference clock frequency and the PLL output frequency requires a very stable VCO.

**§12.11.1.5 What Causes Jitter (p.645)**
- Jitter in the output of a PLL comes from internal sources plus noise coupled from the power system and noise propagated from the reference input.

**§12.11.1.6 Random and Deterministic Jitter (p.648)**
- The point of separating jitter into random and deterministic components is to avoid overly stringent specifications for deterministic jitter.

**§12.11.2.1 Jitter Measurement (p.654)**
- The noise properties of a PLL are characterized by the intrinsic internal jitter, the power supply sensitivity, and a jitter transfer function.

**§12.11.2.2 Jitter and Phase Noise (p.656)**
- You can calculate the variance of jitter using a spectrum analyzer.

**§12.12 Power Supply Filtering for Clock Sources, Repeaters, and PLL Circuits (p.659)**
- Filters designed for wideband operation are built from a cascade of multiple sections, each section scaled to provide coverage in successively higher frequency bands.

**§12.12.1 Healthy Power (p.661)**
- Observing the noise between Vcc and ground always returns useful information.

**§12.12.2 Clean Power (p.663)**
- A power-supply filter does not eliminate noise—it merely copies junk from one circuit node to another, eliminating the difference between them.

**§12.13.1 Signal Integrity Mailbag (p.666)**
- A modulated clock can never be used as the reference clock input to any advanced data communication transceiver.

**§12.13.2 Jitter-Free Clocks (p.668)**
- A scrambled clock spreads the clock emissions without modulating the mean clock frequency.

**§12.14 Reduced-Voltage Signaling (p.669)**
- Reduced-voltage clock signaling saves power and cuts EMI at the expense of noise susceptibility.

**§12.15 Controlling Crosstalk on Clock Lines (p.670)**
- The physical means of providing extra crosstalk protection are simple; the logistical means are complex.

**§12.16 Reducing Emissions (p.672)**
- On a short line, if a range of series termination values will work, the biggest value minimizes the transmitted current and therefore the emissions.

**§13.1 Ringing in a New Era (p.674)**
- If by using a simulator you can save one design spin on one circuit board, the simulator pays for itself.

**§13.2.3 A Word of Caution (p.677-678)**
- Signal-integrity simulations may be performed in what-if mode or post-processing mode.
- Tool sets are highly differentiated according to their degree of software integration.
- Automated tools can be as dangerous as they are powerful and easy to use.

**§13.3.2 Pitfalls of SPICE-Like Algorithms (p.682)**
- All signal-integrity time-domain analysis tools use simulation techniques pioneered by SPICE.
- Especially on circuits containing inductive spikes or hard corners in the I-V curves, SPICE may fail to converge.
- Some versions of SPICE have a lower limit on the smallest permissible step size.
- Check your documentation to make sure TOL and REFTOL are set properly for your application.
- If your parameter extraction efforts fail to properly account for all the significant parasitic elements in a circuit, SPICE results will be incorrect.

**§13.3.3 Transmission Lines (p.683)**
- The SPICE lossless transmission-line model is computationally efficient.
- For typical pcb traces up to 25 cm (10 in.) long, at risetimes of 1 ns or slower, a lossless transmission-line model serves adequately well. Higher speeds and greater distances require the use of a transmission-line model that accounts for the skin effect and dielectric-loss.
- Lossy transmission-line models take a lot longer to run.

**§13.3.4 Interpreting Your Results (p.685)**
- When you first start working with any simulator, begin by setting up some simple, low-frequency test circuits for which you can predict the response by hand calculations.

**§13.4.5 What You Can Do to Help (p.688-689)**
- IBIS is an international standard for the electrical specification of chip drivers and receivers.
- IBIS specifies how to record the various parameters of a chip driver or receiver, but it does not specify what to do with them.
- IBIS is the best, most comprehensive, and genuinely useful piece of signal-integrity technology to come along in a great while.
- We need our chip vendors to provide IBIS model files for every part they make.
- At the time of publication, the IBIS committee maintained work-in-progress copies of its latest draft standards at the Electronic Design Automation (EDA) and Electronic Computer-Aided Design (ECAD) one-stop standards resource: http://www.eda.org/pub/ibis.

**§13.6 IBIS: Issues with Interpolation (p.695)**
- Specify circuit behavior under conditions similar to the actual conditions present in your application.

**§13.7 IBIS: Issues with SSO Noise (p.697)**
- IBIS simulators don't yet properly compute SSO noise.

**§13.8.1 EMC Simulation (p.699)**
- Real live EMI problems are much too complex for even the best software tools.

**§13.9 Power and Ground Resonance (p.701)**
- If your system design depends on the natural power-plane capacitance, compare the roundtrip delay across your board to your clock period—you could be headed for resonance problems.

## 6. Standards referenced

| Standard | Edition / year | Clause / table | What it governs (as used in the book) | Page |
|---|---|---|---|---|
| FCC / EN radiated-emission limits | — | — | Untwisting ~2 in. of one wire of a LAN pair against chassis fails them; 160 uA CM on exposed cable violates them | p.372, p.380 |
| FCC class B measurement conditions | — | antenna in board plane, r = 10 m | basis for the 40 dB differential-cancellation estimate at 0.5 mm, 1 GHz | p.406 |
| ISO/IEC 11801 (categories 3, 5, 5e, 6, 7) | 2002 | classes C/D/E/F = cat 3/5e/6/7 | 100-ohm balanced (twisted-pair) building cabling; cat 7 ISO-only; allows 2 pairs per outlet; cat 4 (120 ohm) retracted in 11801-2002 | p.404, 440-448 |
| IBM Type 1 (150-ohm STP-A) | early 1980s | — | 150-ohm shielded twisted pair; match with two 75-ohm traces; still recognized, may be dropped | p.404, 445, 448 |
| JEDEC LVTTL (3.3 V) | — | V_IH = 2.0 V, V_IL = 0.8 V | single-ended receiver thresholds used in the RG-58 eye example | p.427 |
| ANSI/IEEE P1596.3-1995 (LVDS) | 1995 | Table 6.5 (general-purpose link specs) | Voh/Vol/Vod/Vos/dVos/Ro/trise, receiver Vi/Vidth/Vhyst/Rin, 50 ps pcb skew allocation | p.429 |
| TIA/EIA 568-B.1-2001 | 2001 | Table 7.1, 7.2 | North American generic building cabling: star topology, <= 100 m horizontal, 4 pairs per outlet, preferred horizontal combinations | p.440-449 |
| TIA/EIA 568-B.2-2001 | 2001 | cat 3, cat 5e | balanced cable component specs (cat 3 to 16 MHz; cat 5e adds ELFEXT, return loss) | p.447 |
| TIA/EIA 568-B.2-1-2002 | 2002 | cat 6 | 250 MHz balanced cabling | p.447 |
| EIA/TIA 568-A-1995 | 1995 | cat 5 | 100 MHz four-pair cable (superseded by cat 5e) | p.447 |
| IEC 61156-2 | 2001-09 | cat 3 | multicore/symmetrical pair cable, cat 3 listing | p.447 |
| IEC 61156-5 | 2002-03 | cat 5e, 6, 7 | cable specs incl. cat 7 to 600 MHz | p.447-448 |
| IEEE 802.3 10BASE-T / 100BASE-TX / 1000BASE-T | — | — | LAN examples: 10BASE-T ~2 V p-p per wire, 25 ns switching; 100BASE-TX t_r ~ 8 ns, balance 1:1000; 1000BASE-T uses 4 pairs cat 5 + adaptive equalization | p.360, 379, 419 |
| NCS TRP 109-1977 (US Federal Government) | 1977 | — | recognizes only the T568A RJ-45 wiring style | p.453 |
| TIA/EIA 568-B.1 Annex C | 2001 | Annex C | 25-pair horizontal cabling "should not be used for the general case" | p.454 |
| TIA/EIA 568-B.1 clause 4.6 | 2001 | cl.4.6 | ScTP drain wire terminated at both ends; AC voltage between cable ends <= 1 V rms before connection | p.501 |
| TIA/EIA-568-B.2 / B.2-1 (cable + connecting hardware) | 2001 / 2002 | Tables 8.1, 8.4-8.6, 8.10-8.11 | cable attenuation, Zc, delay, (structural) return loss, NEXT, ELFEXT, power sum; connector IL/NEXT/FEXT/RL; de-rating 0.4 %/C (5e/6), 1.5 %/C (3) | p.459-502 |
| IEC 61156-5 | 2002-03 | foreword | "contents ... unchanged until 2004"; cat 5e/6/7 cable | p.458 |
| ISO 8802.3 clause 14 (10BASE-T) | — | cl.14 | PVC cable loss temperature dependence; above 40 C use less temperature-dependent (plenum) cable | p.502 |
| IEEE 802.3 Annex A "Example Crosstalk Computation for Multiple Disturbers" | — | Annex A | multi-disturber NEXT summation method (use with caution) | p.489 |
| ISO 8877; IEC 603-7 | — | — | RJ-45 8-way connector (IEC 603-7 adds mechanical characteristics) | p.499 |
| EIA/TIA 574:1990 Section 2 | 1990 | Sec.2 | shielded DB-9 (9-pin D-subminiature) connector | p.511 |
| IEC 807-8 | — | — | IBM Medium Interface Connector (MIC), hermaphroditic (not recommended) | p.509 |
| IEC 801-4 (EFT) | — | — | electrical fast transient immunity test used to compare UTP and STP | p.509 |
| IEC 801-3 (EN55024) | — | — | radiated RF immunity limits incl. mobile radio; basis of 3 V/m design field | p.494 |
| FCC Class A radiated emissions | — | — | Table 8.7 known-good UTP systems | p.496-497 |
| IEEE 802.3 1000BASE-CX; FDDI TP-PMD; 100BASE-T2/T4; 802.3z | — | — | STP-A skew 150 ps/25 m (CX); DB-9 connector (TP-PMD, 100BASE-TX, CX); ELFEXT assumption (T2/T4); fiber bandwidth design values (802.3z) | p.490, 507-510, 552 |
| US MIL RG coaxial specifications | early 1960s | — | coax mechanical classes (RG-58, RG-174 ...), loose electrical specs | p.514 |
| IEC Publication 78 | 1967 | — | preferred coaxial cable impedances 50, 75, 100 ohm | p.524, 527 |
| ISO/IEEE 8802.3 | 1996 | — | coax EMC performance determined largely by transfer impedance | p.529 |
| IEC 793-2 | 1992 | Section A; categories A1a (50 um), A1b (62.5 um) | graded-index multimode fiber dimensions, numerical aperture, bandwidth/attenuation categories | p.552-553 |
| IEC 793-3 | — | — | source of Table 11.1 attenuation/modal-bandwidth categories | p.553 |
| TIA/EIA-568-B; ISO/IEC 11801 (fiber) | 2001 / 2002 | — | cladding 125 um, coating 250 um for cores < 85 um; 62.5 um 200/500 MHz-km (ISO) | p.541, 552 |
| IEC 61156-1 / -3 / -4 / -6 | 2001-07 / 2001-09 / 2001-09 / 2002-03 | parts 1, 3, 4, 6 | multicore/symmetrical pair/quad cables: generic spec; work-area and riser cat 3; work-area cat 5e/6/7 to 600 MHz | p.707 refs [74]-[79] |
| IEEE 802.3z (Gigabit Ethernet) | 1998 | — | chromatic-dispersion formula (eq.11.6); installed-base fiber bandwidth design values 160/500 (62.5 um), 400/400 MHz-km (50 um); duplex SC only connector; mode-partition noise in power budget | p.552, 560, 573, 575 |
| ANSI X3.230-1994 (Fibre Channel) annex A, subclause A.5 | 1994 | Annex A, A.5 | laser susceptibility to reflections (RIN) test; for MMF omit the polarization rotator and replace SMF with MMF (802.3z note) | p.573 fn.110 |
| IEC 60825-1 | 1993 | Part 1 | safety of laser products: equipment classification, requirements, labels | p.578, p.708 ref [87] |
| IEC 793-2 / 793-3 | 1992 | — | optical fibre product specs; attenuation and bandwidth categories (Table 11.1) | p.552-553, ref [86] |
| EIA/TIA 604-3 / IEC 874-14; EIA/TIA 604-2; ISO/IEC 9314-3; ANSI/TIA/EIA 604-7 | — | — | duplex SC; ST (BFOC/2.5); FDDI fiber MIC; 3M Volition VF-45 | p.575-576 Table 11.4 |
| ISO/IEC 11801 (single-mode) | 2002 | — | 1300-nm SMF core 9-10 um | p.576 |
| FDDI (ANSI/ISO 9314) | — | — | transmitter duty-cycle distortion <= 1.00 ns p-p (8.00 ns baud) | p.564 |
| Fibre Channel "Methodologies for Jitter Specification" (ANSI NCITS draft TR) | Feb 8, 1998 | — | jitter/BER extrapolation (bathtub) | p.650, ref [97] |
| SMPTE SDI (259M class, as quoted) | — | — | parallel clock jitter 370 ps p-p at 27 MHz (+/-0.1 UI at 270 Mb/s), 10 Hz to 1/10 serial clock | p.654-655 |
| IEEE 802.5 Token Ring | — | — | up to 256 stations; PLL peaking accumulation example | p.652 |
| FCC / EN radiated-emission measurement | — | 100-kHz resolution bandwidth | basis of spread-spectrum peak reduction | p.664 |
| IBIS (I/O Buffer Information Specification): v1.0 June 1993; v1.1 Aug 1993; v2.0 June 1994; v2.1 = ANSI/EIA-656 (Dec 1995); v3.2 = ANSI/EIA-656-A (Sept 1999) = IEC 62014-1 (April 2001) | 1993-2001 | — | behavioral I/O models: I-V tables, ramp/waveforms, package data | p.686-690 |
| ICEM (Integrated Circuits Electromagnetic Model), IEC (pending at publication) | — | — | IC core-noise EMC modeling | p.691 |
| HP Product Note 11729C-2 | 1985 | — | phase-noise characterization of oscillators | ref [98] |

## 7. Process / lifecycle guidance

The book is a signal-propagation reference, not a product-development text; the items below are the process guidance it does give (SI simulation flow, cabling budgets, clock-adjustment test, SI organization).

| Stage | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| Architecture | Choose generic building cabling (TIA/EIA 568-B.1 / ISO/IEC 11801 common ground) for any room-to-room link; decide copper vs fiber vs coax | link architecture with channel specs | horizontal <= 100 m, point-to-point, supported categories listed | p.439-446 |
| Architecture | Full SNR / optical power budget (all attenuation, crosstalk, reflections, jitter, packaging, layout) | budget spreadsheet | +2 dB (copper) / +3 dB (fiber) margin after all known items; plan with ~6 dB optical margin | p.446, 555-568 |
| Architecture (SI what-if) | Early what-if simulations with schematic-capture SI tools for topologies, terminations, driver choice | waveform overlays per critical net | monotonic clocks, acceptable ringing/crosstalk at fastest corners | p.676 §13.2.2 |
| Model preparation | Parameter extraction for die (IBIS/SPICE), packages (L/C matrices, R), board (Z, lengths, topologies, coupling, connectors) | model library | second person has double-checked every parameter source; modeling depth matched to t_r | p.674-676 |
| Tool qualification | Correlate simulator against hand-calculable bench circuits, then faster ones | correlation report | measured vs simulated agree within instrument tolerance | p.684 |
| Post-route verification | Batch SI simulation of every net from the layout database | violation lists (overshoot, ringback, monotonicity, crosstalk, settling) + termination recommendations | zero open violations or waived with rationale | p.676-677 |
| Fabrication | Impedance coupons on every panel | coupon TDR data | within tolerance | p.389 |
| Bring-up | Measure Vcc/GND noise at several locations; check clock waveforms at loads | noise and waveform records | within budgets | p.659-661 |
| Production test | Written procedure for every timing adjustment (measurement point, method, limits) | test procedure | technicians can set and verify each adjustment | p.607 |
| EMC | Quick EMI scan as early as possible; iterate worst-mode-first | scan results, fix list | compliance with margin (expect +6 dB need per 2x speed) | p.697-699 |
| Organization | Independent SI department (consultant first, pilot program, then mainstream); ~1 SI specialist per 5 designers | charter/mission | measurable SI performance and cost results | p.731-732 App.A |

## 8. Coverage log

Line ranges read (Read tool, sequential, in order): 1–600 (front matter/TOC, orientation only); 15330–15401 (context for eq. 5.39); 15400–16199; 16200–17099; 17100–17999; 18000–18899; 18900–19599; 19600–20399; 20400–21199; 21200–21999; 22000–22799; 22800–23598; 23599–24397; 24398–25096; 25097–25895; 25896–26694; 26695–27493; 27494–28292; 28293–29091; 29092–29340; 29341–29539; 29540–29798; 29799–30127; 30128–30427 (Appendix E end + start of Index); 30680–30722 (tail check). A session restart/rate-limit interruption occurred after line 23598; work resumed from the saved scratch parts without gaps.

Skipped: Index (lines ~30394–30722, pp. 749–766) — index pages; historical anecdotes (e.g. telegraph/telephone history in §5.6, ENIAC, IBM MIC demonstration, token-ring market history) summarized only where they carry a number; reader-mailbag humor (clock-modulation "white van" etc.); pure derivations reproduced only as final formulas (App. C/D intermediate algebra). No exercises exist in this book.

Extraction limitations:
- OCR damage to equations: eq. 6.20–6.23 bodies (reconstructed from the text's definitions and verified against eq. 6.24's 0.200*t_d/t_r); eq. 10.1/10.9 (standard 60/sqrt(er)*ln(d2/d1), verified by the book's 76.7/51.1-ohm values); eq. 11.1 (modal risetime) body illegible — the modal constant 0.48 in eq. 11.5 was back-solved from the FDDI example (t_TP3b = 6119 ps), marked medium; eq. 11.6 form verified numerically against the same example; eq. 12.6 (multiple source-terminated lines) body lost — R_t = Z0 - N*Rs derived from the text's stated behaviour (N = 1 -> Rs + R_t = Z0; negative for large N) and checked to launch exactly Vcc/2; eq. 12.20 (clock-filter damping resistor) illegible — only the Table 12.5 value (2.2 ohm) is given; eq. D.11 impedance-ratio condition garbled ("each less than 3.8"), numeric anchors (< 1 % at l*gamma < 1/4; ~3 % at t_d/t_r = 1/6) kept.
- Figure 5.37 self-inductance printed as "(2-ln(s/r))" in OCR; corrected to 2*ln(s/r), which reproduces the book's 0.539-nH example.
- Broadside example delay "(4 mm)*2*(4 ps/mm) = 56 ps": arithmetic implies 7 ps/mm; recorded with note.
- Table 11.1 modal-bandwidth rows and Table 12.1 column headers partially illegible (marked medium/low); Table 9.2 and Table 8.9 pin maps reconstructed from interleaved OCR columns (medium).
- Table 8.11 cat-3 connector NEXT constant reads "2.1" in OCR (implausible; flagged, verify in TIA/EIA-568-B.2).
- §13.2.1 "3 us" risetime is OCR for (almost certainly) 3 ns; recorded with note.
- Table 8.5 text says its last column is at 5 MHz; printed values correspond to 10 MHz (noted).
- Figures are not in the text: graph-based rules carry figure captions/anchors and conf = medium.

Counts: 338 design rules (JOHNSON03-2001 … 2338); 33 reproduced tables (T-6.1–T-12.5 incl. derived example tables) plus a key-formula table; 41 mechanizable checks; 29 verification procedures; 83 checklist items; verbatim POINTS TO REMEMBER for every boxed list in §5.5.5.2–§13.9.
