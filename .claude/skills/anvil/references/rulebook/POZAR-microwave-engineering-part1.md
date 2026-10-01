# Microwave Engineering (4th ed.) — Anvil rulebook (Part 1: Ch. 1–6 and Ch. 7 §7.1–7.3 opening)

## 0. Citation

D. M. Pozar, *Microwave Engineering*, 4th ed. Hoboken, NJ, USA: John Wiley & Sons, 2012 (copyright 2012, 2005, 1998). ISBN 978-0-470-63155-3 (hardback). LCCN 2011033196; LC call no. TK7876.P69 2011.

Chapters covered by THIS extraction (source text file lines 1–32549; assigned range 1–32500): front matter and table of contents (orientation); Ch. 1 Electromagnetic Theory (§1.1–1.9, design-usable results only); Ch. 2 Transmission Line Theory (§2.1–2.8); Ch. 3 Transmission Lines and Waveguides (§3.1–3.11, incl. stripline and microstrip design formulas); Ch. 4 Microwave Network Analysis (§4.1–4.8); Ch. 5 Impedance Matching and Tuning (§5.1–5.9); Ch. 6 Microwave Resonators (§6.1–6.7); Ch. 7 Power Dividers and Directional Couplers §7.1 (basic properties of three-/four-port networks, coupler metrics), §7.2 (T-junction and resistive dividers) and the opening of §7.3 (Wilkinson definition and equal-split element values, p.328; file line 32500 falls inside the §7.3 even–odd analysis).

Chapters NOT read by this extraction (assigned to the part-2 agent, file lines 32500–65005): rest of Ch. 7 (§7.3 Wilkinson analysis onward: waveguide couplers, quadrature and 180° hybrids, coupled-line and Lange couplers); Ch. 8 Microwave Filters; Ch. 9 Ferrimagnetic Components; Ch. 10 Noise and Nonlinear Distortion; Ch. 11 Active Devices; Ch. 12 Amplifier Design; Ch. 13 Oscillators and Mixers; Ch. 14 Microwave Systems; Appendices A–J (incl. App. E physical constants, App. F conductivities, App. G dielectric constants and loss tangents, App. I standard rectangular waveguide data, App. J standard coax data). End-of-chapter problems were skipped except where a problem statement gives a numeric design result (marked "Problem x.y", conf medium).

Notes on the source text: printed page numbers are present as running headers and are cited as p.NNN. The PDF-to-text extraction drops most Greek epsilon symbols, the script-l used for line length, square-root radicals and many subscripts; every formula here was reconstructed from context and, wherever the book gives a worked example, re-evaluated numerically to confirm the transcription (Examples 1.1–1.4, 2.2–2.9, 3.1–3.8, 4.2, 4.4, 4.5, 5.1–5.8, 6.1–6.6 and the full Table 4.2 conversion set were reproduced). Rule ids use POZAR-1001 … POZAR-1248 (1xxx block, sequential, no gaps reused) to avoid collisions with the part-2 file.

## 1. Design rules

### Ch. 1 Electromagnetic theory (design-usable results)

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| POZAR-1001 | rf | RF/microwave frequency range definitions: RF/microwave engineering covers 100 MHz to 1000 GHz; VHF = 30–300 MHz; UHF = 300–3000 MHz; "microwave" = 3–300 GHz (λ = c/f = 10 cm to 1 mm); mm-wave = wavelengths on the order of millimeters | λ = c/f; 3 GHz ↔ 10 cm; 300 GHz ↔ 1 mm | f | Band naming for requirements/HRS; band letters in Table 2-1 of this rulebook (Fig. 1.1) | review | p.1, Fig. 1.1 | high |
| POZAR-1002 | transmission-line | Lumped circuit theory is invalid when component dimensions are on the order of the electrical wavelength: phase of V and I changes significantly over the device; treat as distributed element (transmission line) | Flag distributed treatment when physical length l is a "considerable fraction" of λ (no numeric threshold given in §1.1/§2.1; Pozar's numeric criterion for lumped MIC elements is l < λ/10, POZAR-1176) | l, f, εeff | Any interconnect/component at RF | calc | p.1, p.48 (§2.1) | low |
| POZAR-1003 | materials | Complex permittivity and loss tangent. Loss from dielectric damping (ωε'') is indistinguishable from conduction loss (σ); total effective conductivity = ωε'' + σ | ε = ε' − jε'' = ε'(1 − j tanδ) = ε0·εr·(1 − j tanδ);  tanδ = (ωε'' + σ)/(ωε') | ε', ε'', σ, ω | Isotropic linear dielectric; εr and tanδ are specified "at a certain frequency" (App. G) | calc | p.10–11, eq. (1.18), (1.20), (1.21) | high |
| POZAR-1004 | materials | Loss is introduced into a lossless solution by replacing real ε with complex ε | ε → ε0·εr·(1 − j tanδ) | εr, tanδ | Post-processing a lossless analysis | calc | p.11 | high |
| POZAR-1005 | transmission-line | Wave parameters in a lossless medium | k = ω·sqrt(µε) (1/m); vp = ω/k = 1/sqrt(µε) = c/sqrt(µr·εr); λ = 2π/k = vp/f = λ0/sqrt(µr·εr); η = sqrt(µ/ε) = η0·sqrt(µr/εr) (Ω) | f, εr, µr | Plane wave / TEM wave, lossless homogeneous medium | calc | p.16–17, eq. (1.47)–(1.49), (1.106)–(1.109) | high |
| POZAR-1006 | transmission-line | Free-space constants used throughout | µ0 = 4π×10^-7 H/m; ε0 = 8.854×10^-12 F/m; c = 1/sqrt(µ0ε0) = 2.998×10^8 m/s; η0 = sqrt(µ0/ε0) = 377 Ω | — | MKS units throughout the book; cosine-based peak phasors, e^{jωt} suppressed | calc | p.7, eq. (1.2); p.16–17 | high |
| POZAR-1007 | transmission-line | Worked check (Example 1.1): 5.0 GHz plane wave with λ = 3.0 cm in a lossless dielectric | k = 2π/0.03 = 209.4 m^-1; vp = λf = 1.5×10^8 m/s; εr = (c/vp)^2 = 4.0; η = 377/sqrt(4.0) = 188.5 Ω | f, λ | Regression test for a propagation calculator | calc | p.17, Example 1.1 | high |
| POZAR-1008 | materials | Good-conductor criterion and propagation constant: conduction current >> displacement current | Good conductor if σ >> ωε (equivalently ε'' >> ε'); γ = α + jβ ≈ (1 + j)·sqrt(ωµσ/2) = (1 + j)/δs | σ, f, µ | "Most metals" at microwave frequencies | calc | p.19, eq. (1.59); (1.113) | high |
| POZAR-1009 | materials | Skin depth: field amplitude decays to 1/e (36.8%) after one skin depth; most current flows in an extremely thin surface layer | δs = 1/α = sqrt(2/(ωµσ)) = 1/sqrt(π·f·µ0·σ) (m) | f (Hz), σ (S/m), µ | Good conductor, µ = µ0 for the closed form | calc | p.19, eq. (1.60) | high |
| POZAR-1010 | materials | Skin depth at 10 GHz shortcut (non-magnetic metals) | δs(10 GHz) = 5.03×10^-3 / sqrt(σ) (m, σ in S/m); scale ∝ 1/sqrt(f) | σ | µ = µ0; values: Al 0.814 µm, Cu 0.660 µm, Au 0.786 µm, Ag 0.640 µm (Table 2-2) | calc | p.19, Example 1.2 | high |
| POZAR-1011 | fab | Only a thin plating of a good conductor (e.g. silver or gold) is needed for low-loss microwave components, because fields and power decay to a negligible value "within a few skin depths" | Plating thickness t_plate ≥ a few δs at the lowest operating frequency (Pozar gives no multiplier; "a few" quantified by user, e.g. 3–5 δs → conf low) | t_plate, f_min, σ_plating | Plated conductors, cavities, waveguides, RF traces with surface finish | calc | p.19; p.32 | low |
| POZAR-1012 | materials | Intrinsic impedance of a good conductor has a 45° phase; lossless material has 0°, arbitrary lossy medium between 0° and 45° | η = (1 + j)·sqrt(ωµ/(2σ)) = (1 + j)/(σ·δs) (Ω) | σ, f | Good conductor | calc | p.20, eq. (1.61), (1.114) | high |
| POZAR-1013 | materials | Surface resistance of a conductor | Rs = Re{η} = sqrt(ωµ/(2σ)) = 1/(σ·δs) (Ω per square); Rs ∝ sqrt(f) | f, σ, µ | Good conductor, thickness >> δs | calc | p.28, eq. (1.98), (1.125) | high |
| POZAR-1014 | materials | Conductor power loss via surface resistance: compute the surface current as if the metal were a perfect conductor (Js = n × H), then dissipate it in Rs | P_loss = (Rs/2)·∫S abs(Js)^2 ds = (Rs/2)·∫S abs(Ht)^2 ds (W; peak phasors) | Rs, Ht or Js over the surface | Valid for arbitrary conductor shape as long as bends/corners have radii on the order of a skin depth or larger; approximation abs(η) << η0 (Cu at 1 GHz abs(η) = 0.012 Ω) | calc | p.28, eq. (1.97); p.34, eq. (1.131) | high |
| POZAR-1015 | transmission-line | Normal-incidence reflection/transmission at a media interface | Γ = (η − η0)/(η + η0);  T = 1 + Γ = 2η/(η + η0) | η of both media | Plane wave, normal incidence, arbitrary (lossy) medium 2 | calc | p.29, eq. (1.105) | high |
| POZAR-1016 | materials | Worked check (Example 1.4): copper half-space at 1 GHz (σ = 5.813×10^7 S/m) behaves practically as an ideal short | δs = 2.088×10^-6 m; γ = (4.789 + j4.789)×10^5 m^-1; η = (8.239 + j8.239)×10^-3 Ω; Γ = 1.0∠179.99°; T = 6.181×10^-5∠45° | f, σ | Regression test for conductor calculator | calc | p.34–35, Example 1.4 | high |
| POZAR-1017 | rf | Brewster angle (zero reflection) exists only for parallel polarization at a dielectric interface; none exists for perpendicular polarization | sin θb = 1/sqrt(1 + ε1/ε2) | ε1, ε2 | Lossless dielectric media, µ = µ0 | calc | p.37, eq. (1.138); p.38 | high |
| POZAR-1018 | rf | Total internal reflection beyond the critical angle; abs(Γ) = 1 and the transmitted field is a surface wave that decays exponentially away from the interface (no real power transmitted into region 2) | sin θc = sqrt(ε2/ε1) for ε1 > ε2; decay α = sqrt(k1^2 sin^2θi − k2^2) | ε1, ε2, θi | Wave incident from denser dielectric | calc | p.38–40, eq. (1.145), (1.149) | high |
| POZAR-1019 | rf | Worked check (Example 1.5): free space onto εr = 2.55 | η2 = 377/sqrt(2.55) = 236 Ω; reflection vs angle plotted in Fig. 1.14 (parallel pol. dips to 0 at Brewster angle) | εr | — | calc | p.38, Example 1.5, Fig. 1.14 (graph) | medium |
| POZAR-1020 | rf | Pozar uses cosine-based PEAK phasors: time-average power carries a factor 1/2 and rms = peak/sqrt(2); decomposition of Poynting vector into incident + reflected parts is only valid for time-average (real) power in a lossless region | abs(E)rms = abs(E)/sqrt(2); Pavg = (1/2)·Re{E × H*}; Pavg = (1/2)·Re{V·I*} | phasors | All power computations in this rulebook | review | p.8–9, eq. (1.13); p.31 | high |

### Ch. 2 Transmission line theory

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| POZAR-1021 | transmission-line | Distributed RLGC model of a TEM line (per-unit-length, both conductors). R = conductor loss, G = dielectric loss | R (Ω/m), L (H/m), G (S/m), C (F/m); telegrapher: dV/dz = −(R + jωL)I, dI/dz = −(G + jωC)V | line geometry, materials | Any two-conductor TEM line; finite line = cascade of Δz sections | calc | p.48–49, Fig. 2.1, eq. (2.3) | high |
| POZAR-1022 | transmission-line | Complex propagation constant and characteristic impedance of a general (lossy) line | γ = α + jβ = sqrt((R + jωL)(G + jωC)) (1/m); Z0 = sqrt((R + jωL)/(G + jωC)) (Ω); λ = 2π/β; vp = ω/β = λf | R, L, G, C, f | Exact; α in Np/m (×8.686 → dB/m) | calc | p.50–51, eq. (2.5), (2.7), (2.10), (2.11) | high |
| POZAR-1023 | transmission-line | Lossless line | β = ω·sqrt(LC); Z0 = sqrt(L/C) (real); λ = 2π/(ω·sqrt(LC)); vp = 1/sqrt(LC); α = 0 | L, C | R = G = 0 | calc | p.51, eq. (2.12)–(2.16) | high |
| POZAR-1024 | transmission-line | Line parameters from the lossless-line fields (energy/power equivalence) | L = (µ/abs(Io)^2)∫S H·H* ds; C = (ε'/abs(Vo)^2)∫S E·E* ds; R = (Rs/abs(Io)^2)∮(C1+C2) H·H* dl; G = (ωε''/abs(Vo)^2)∫S E·E* ds | field solution, Rs, ε', ε'' | Useful for simple lines only; complex lines use field-theory Z0/γ directly | calc | p.51–52, eq. (2.17)–(2.20) | high |
| POZAR-1025 | transmission-line | Coaxial line RLGC (inner radius a, outer radius b) | L = (µ/2π)·ln(b/a); C = 2πε'/ln(b/a); R = (Rs/2π)·(1/a + 1/b); G = 2πωε''/ln(b/a) | a, b, µ, ε', ε'', Rs | TEM mode | calc | p.53–54, Example 2.1, Table 2.1 | high |
| POZAR-1026 | transmission-line | Two-wire line RLGC (wire radius a, center spacing D) | L = (µ/π)·acosh(D/2a); C = πε'/acosh(D/2a); R = Rs/(πa); G = πωε''/acosh(D/2a) | a, D | TEM mode | calc | p.54, Table 2.1 | high |
| POZAR-1027 | transmission-line | Parallel-plate line RLGC (width w, separation d) | L = µd/w; C = ε'w/d; R = 2Rs/w; G = ωε''w/d; Z0 = ηd/W | w, d | w >> d (fringing ignored) | calc | p.54, Table 2.1; p.104, eq. (3.39) | high |
| POZAR-1028 | transmission-line | Characteristic impedance of coax | Z0 = (η/2π)·ln(b/a) = (sqrt(µ/ε)/2π)·ln(b/a); for µr = 1: Z0 ≈ (60/sqrt(εr))·ln(b/a) (η0/2π = 59.96 Ω) | a, b, εr | TEM; the 60 Ω constant is derived from η0 = 377 Ω | calc | p.56, eq. (2.32) | high |
| POZAR-1029 | transmission-line | Every TEM line: β = ω·sqrt(µε) (same as a plane wave in the filling medium) and wave impedance Zw = E/H = η; power flows only in the fields between conductors | β = k = ω·sqrt(µε); Z_TEM = η; P = (1/2)·Vo·Io* | medium εr, µr | TEM lines with homogeneous fill; do not confuse Zw with Z0 | calc | p.56, eq. (2.30), (2.31), (2.33); p.99, eq. (3.17) | high |
| POZAR-1030 | matching | Load reflection coefficient; load is "matched" only when ZL = Z0 | Γ = Vo−/Vo+ = (ZL − Z0)/(ZL + Z0); Γ = 0 ⇔ ZL = Z0 | ZL, Z0 | Lossless line; Z0 real | calc | p.57, eq. (2.35) | high |
| POZAR-1031 | matching | Power delivered to a mismatched load from a matched generator = incident − reflected | Pavg = (abs(Vo+)^2/(2Z0))·(1 − abs(Γ)^2) (W, peak phasors) | Vo+, Γ, Z0 | Generator matched (no re-reflection); lossless line | calc | p.57–58, eq. (2.37) | high |
| POZAR-1032 | matching | Return loss (dB); non-negative for any passive network; matched = ∞ dB; total reflection = 0 dB | RL = −20·log10abs(Γ) (dB) ≥ 0 | abs(Γ) | Passive reflection | calc | p.58, eq. (2.38) | high |
| POZAR-1033 | matching | Standing wave ratio; VSWR = SWR | SWR = Vmax/Vmin = (1 + abs(Γ))/(1 − abs(Γ)), 1 ≤ SWR ≤ ∞; Vmax = abs(Vo+)(1 + abs(Γ)), Vmin = abs(Vo+)(1 − abs(Γ)) | abs(Γ) | Lossless line | calc | p.58, eq. (2.40), (2.41) | high |
| POZAR-1034 | transmission-line | Standing-wave geometry: successive maxima (or minima) λ/2 apart; maximum-to-minimum λ/4 | Δl(max→max) = λ/2; Δl(max→min) = λ/4, λ = guide wavelength on the line | λ | Lossless line | calc | p.58 | high |
| POZAR-1035 | transmission-line | Reflection coefficient transforms along a lossless line with constant magnitude | Γ(l) = Γ(0)·e^{−2jβl} (l = distance from load toward generator) | Γ(0), β, l | Lossless; for lossy use POZAR-1059 | calc | p.58, eq. (2.42) | high |
| POZAR-1036 | transmission-line | Transmission-line impedance equation (input impedance of a terminated lossless line) | Zin = Z0·(ZL + jZ0·tan βl)/(Z0 + jZL·tan βl) = Z0·(1 + Γe^{−2jβl})/(1 − Γe^{−2jβl}) | Z0, ZL, βl | Lossless line | calc | p.59, eq. (2.43), (2.44) | high |
| POZAR-1037 | transmission-line | Short- and open-circuited stubs are pure reactances; short stub of λ/4 looks open; impedance periodic in λ/2 | Short: Zin = jZ0·tan βl (Γ = −1); Open: Zin = −jZ0·cot βl (Γ = +1); SWR = ∞ | Z0, βl | Lossless ideal terminations | calc | p.59–61, eq. (2.45c), (2.46c), Fig. 2.6, 2.8 | high |
| POZAR-1038 | transmission-line | Half-wave line does not transform the load, regardless of its Z0 | Zin = ZL for l = nλ/2 | l | Single frequency (exact only at nλ/2) | calc | p.61, eq. (2.47) | high |
| POZAR-1039 | matching | Quarter-wave line inverts the load impedance | Zin = Z0^2/ZL for l = λ/4 + nλ/2 | Z0, ZL | Single frequency | calc | p.61, eq. (2.48) | high |
| POZAR-1040 | transmission-line | Junction of two lines (feed Z0 into matched line Z1): reflection, transmission, insertion loss | Γ = (Z1 − Z0)/(Z1 + Z0); T = 1 + Γ = 2Z1/(Z1 + Z0); IL = −20·log10abs(T) (dB) | Z0, Z1 | Z1 line matched or infinite | calc | p.62, eq. (2.49), (2.51), (2.52) | high |
| POZAR-1041 | rf | Decibel/neper conventions: dB only for power ratios; with unequal load resistances the voltage-ratio dB needs a resistance term; 1 Np (voltage ratio e) = 8.686 dB; dBm referenced to 1 mW; cascaded gains/losses add in dB | dB = 10·log10(P1/P2) = 20·log10(V1/V2) + 10·log10(R2/R1); Np = ln(V1/V2) = (1/2)ln(P1/P2); 1 Np = 8.686 dB; 0 dBm = 1 mW, 30 dBm = 1 W; 2× = 3 dB, 0.1× = −10 dB; 23 dB amp after 6 dB pad = 17 dB | P, V, R | All budgets | calc | p.62–63, Point of Interest "Decibels and Nepers" | high |
| POZAR-1042 | matching | Smith chart mapping and rotation: moving toward the generator rotates Γ clockwise by 2βl; one full revolution = λ/2; a λ/4 rotation (180°) converts normalized impedance to normalized admittance | Γ = (zL − 1)/(zL + 1); zL = (1 + Γ)/(1 − Γ); z = Z/Z0; rotation angle = −2βl | zL, l/λ | Lossless line (abs(Γ) constant on the SWR circle) | calc | p.64–67, eq. (2.53), (2.54), (2.57) | high |
| POZAR-1043 | matching | Smith chart circle families: resistance circles centered on the real axis through Γ = 1; reactance circles centered on Γr = 1 line; circles are orthogonal | r-circle: (Γr − r/(1+r))^2 + Γi^2 = (1/(1+r))^2; x-circle: (Γr − 1)^2 + (Γi − 1/x)^2 = (1/x)^2 | r, x | r = 1 circle: center 0.5, radius 0.5 | calc | p.65, eq. (2.56) | high |
| POZAR-1044 | matching | Worked check (Example 2.2): ZL = 40 + j70 Ω on a 100 Ω line, l = 0.3λ | abs(Γ) = 0.59; SWR = 3.87; RL = 4.6 dB; ∠ΓL = 104°; WTG 0.106λ → 0.406λ; zin = 0.365 − j0.611; Zin = 36.5 − j61.1 Ω; ∠Γin = 248° | ZL, Z0, l | Smith-chart read accuracy (2–3 digits) | calc | p.66–67, Example 2.2, Fig. 2.11 | high |
| POZAR-1045 | matching | Worked check (Example 2.3): ZL = 100 + j50 Ω on a 50 Ω line, l = 0.15λ | zL = 2 + j1; yL = 0.40 − j0.20; YL = 0.0080 − j0.0040 S; WTG 0.214λ → 0.364λ; y = 0.61 + j0.66; Yin = 0.0122 + j0.0132 S | ZL, Z0, l | Chart-read accuracy | calc | p.67–68, Example 2.3, Fig. 2.12 | high |
| POZAR-1046 | test | Load impedance from a standing-wave (slotted-line) measurement: measure SWR and distance lmin from load to first voltage minimum; calibrate the load reference plane with a short (minima repeat every λ/2); use minima, not maxima (minima are sharper → better accuracy) | abs(Γ) = (SWR − 1)/(SWR + 1); θ = π + 2β·lmin; ZL = Z0·(1 + Γ)/(1 − Γ) | SWR, lmin, λ | Two independent quantities needed for a complex load | measure | p.68–72, eq. (2.58)–(2.60) | high |
| POZAR-1047 | test | Worked check (Example 2.4): 50 Ω slotted line, short-circuit minima at 0.2/2.2/4.2 cm (λ = 4.0 cm); load SWR = 1.5, minima at 0.72/2.72/4.72 cm | lmin = 4.2 − 2.72 = 1.48 cm = 0.37λ; abs(Γ) = 0.2; θ = 86.4°; Γ = 0.0126 + j0.1996; ZL = 47.3 + j19.7 Ω (Smith chart: 47.5 + j20 Ω) | measured data | — | calc | p.70–72, Example 2.4, Fig. 2.14–2.15 | high |
| POZAR-1048 | test | Slotted lines are largely superseded by the vector network analyzer (accuracy, versatility); still useful at high mm-wave frequencies or to avoid connector mismatch by connecting the unknown load directly | Prefer VNA for impedance measurement unless f is high mm-wave or connector transitions dominate error | f, fixture | — | review | p.69 | high |
| POZAR-1049 | matching | Quarter-wave transformer design: section impedance is the geometric mean; exact match only where l = λ/4 (or odd multiples) — mismatch at other frequencies; standing waves exist on the λ/4 section; only real loads (complex loads first rotated to real by a length of line, single frequency) | Z1 = sqrt(Z0·RL); l = λ/4 at fo; βl = (π/2)(f/fo) | Z0, RL, fo | Lossless; narrowband | calc | p.72–74, eq. (2.61)–(2.63) | high |
| POZAR-1050 | matching | Worked check (Example 2.5): RL = 100 Ω to 50 Ω line | Z1 = sqrt(50·100) = 70.71 Ω; abs(Γ) vs f/fo from Zin(2.44) with βl = πf/(2fo); zero at f/fo = 1, 3, …; Fig. 2.17 peaks ≈ 0.33 (graph, 0–4 f/fo) | RL, Z0 | — | sim | p.73, Example 2.5, Fig. 2.17 | medium |
| POZAR-1051 | matching | Multiple-reflection view of the λ/4 transformer: partial reflections sum to zero only if Z1^2 = Z0·RL | numerator of Γ ∝ 2(Z1^2 − Z0·RL)/((Z1 + Z0)(RL + Z1)); Γ1 = (Z1 − Z0)/(Z1 + Z0), Γ2 = −Γ1, Γ3 = (RL − Z1)/(RL + Z1), T1 = 2Z1/(Z1 + Z0), T2 = 2Z0/(Z1 + Z0) | Z0, Z1, RL | Lossless; steady state | calc | p.74–75, eq. (2.64)–(2.66) | high |
| POZAR-1052 | matching | Forward-wave amplitude with both generator and load mismatched | Vo+ = Vg·(Z0/(Z0 + Zg))·e^{−jβl}/(1 − Γl·Γg·e^{−2jβl}); Γg = (Zg − Z0)/(Zg + Z0); SWR from Γl only | Vg, Zg, Z0, ZL, βl | Lossless line | calc | p.76–77, eq. (2.71)–(2.73) | high |
| POZAR-1053 | matching | Power delivered to the load (general) | P = (1/2)abs(Vg)^2 · Rin/((Rin + Rg)^2 + (Xin + Xg)^2), Zin = Rin + jXin, Zg = Rg + jXg | Vg (peak), Zg, Zin | Lossless line (P into Zin = P into load) | calc | p.77, eq. (2.74), (2.75) | high |
| POZAR-1054 | matching | Three matching cases for fixed Zg: (a) load matched to line (ZL = Z0); (b) generator matched to loaded line (Zin = Zg, may still have standing waves); (c) conjugate match Zin = Zg* gives maximum power = available power | (a) P = (1/2)abs(Vg)^2·Z0/((Z0 + Rg)^2 + Xg^2); (b) P = (1/2)abs(Vg)^2·Rg/(4(Rg^2 + Xg^2)); (c) Pmax = (1/2)abs(Vg)^2/(4Rg) = abs(Vg)^2/(8Rg) | Vg, Zg | If Xg = 0, (b) and (c) coincide; in (c) Γ, Γg, Γl may be nonzero | calc | p.77–78, eq. (2.76)–(2.81) | high |
| POZAR-1055 | matching | Neither Z0 matching nor conjugate matching maximizes efficiency: with Zg = ZL = Z0 only 50% of generated power reaches the load; efficiency improves only by making Zg small | η_tx = 50% when Zg = ZL = Z0 | Zg | Power-transfer vs efficiency trade (e.g. PA output design) | review | p.78 | high |
| POZAR-1056 | transmission-line | High-frequency low-loss approximations: β and Z0 ≈ lossless values; α split into conductor and dielectric parts | If R << ωL and G << ωC: α ≈ (1/2)(R/Z0 + G·Z0) (Np/m); β ≈ ω·sqrt(LC); Z0 ≈ sqrt(L/C) | R, L, G, C | "Most practical" RF lines | calc | p.79, eq. (2.85), (2.86) | high |
| POZAR-1057 | transmission-line | Coax attenuation (conductor + dielectric) | α = (Rs/(2η·ln(b/a)))·(1/a + 1/b) + ωε''η/2 (Np/m); dielectric term = k·tanδ/2; αc = (Rs/(4π·Z0))(1/a + 1/b) | a, b, Rs, ε', tanδ, f | Low loss; TEM | calc | p.80, Example 2.6; p.83, Example 2.7; p.85, Example 2.8 | high |
| POZAR-1058 | transmission-line | Distortionless (Heaviside) line: linear phase and frequency-independent attenuation; otherwise lossy lines are dispersive (vp varies with f → pulse distortion, significant on very long lines) | R/L = G/C ⇒ α = R·sqrt(C/L), β = ω·sqrt(LC); typically needs added L (periodic series loading coils) | R, L, G, C | R is a weak function of f in practice | calc | p.80–81, eq. (2.87), (2.88) | high |
| POZAR-1059 | transmission-line | Terminated lossy line | Γ(l) = Γ·e^{−2jβl}·e^{−2αl} = Γ·e^{−2γl}; Zin = Z0·(ZL + Z0·tanh γl)/(Z0 + ZL·tanh γl) | Z0 (≈ real), γ, ZL, l | Small loss (Z0 approx. real) | calc | p.81, eq. (2.90), (2.91) | high |
| POZAR-1060 | transmission-line | Power budget on a terminated lossy line: both incident and reflected waves are attenuated | Pin = (abs(Vo+)^2/(2Z0))·(e^{2αl} − abs(Γ)^2·e^{−2αl}); PL = (abs(Vo+)^2/(2Z0))(1 − abs(Γ)^2); Ploss = (abs(Vo+)^2/(2Z0))·[(e^{2αl} − 1) + abs(Γ)^2(1 − e^{−2αl})] | Vo+ (at load), α, l, Γ | Low-loss line | calc | p.81–82, eq. (2.92)–(2.94) | high |
| POZAR-1061 | transmission-line | Perturbation method for attenuation: compute loss per unit length from the LOSSLESS fields and divide by twice the carried power | α = P'l/(2·Po) (Np/m); P(z) = Po·e^{−2αz}; P'l = conductor loss (Rs/2)∮abs(Ht)^2 dl + dielectric loss (ωε''/2)∫abs(E)^2 ds; α = αc + αd | field solution, Rs, ε'' | Low loss (fields not greatly perturbed) | calc | p.82, eq. (2.95), (2.96); p.101 | high |
| POZAR-1062 | transmission-line | Wheeler incremental inductance rule for conductor loss of TEM/quasi-TEM lines: αc from the change in Z0 when all conductor walls recede by δs/2 | αc = ωΔL/(2Z0) = β·ΔZ0/(2Z0) = (β·δs/(4Z0))·dZ0/dl = (Rs/(2·Z0·η))·dZ0/dl (Np/m); l = distance into each conductor wall | Z0(geometry), Rs, η of dielectric | TEM or quasi-TEM; good conductors | calc | p.83–85, eq. (2.102), (2.104), (2.106), Example 2.8 | high |
| POZAR-1063 | transmission-line | Measured conductor attenuation exceeds smooth-conductor theory because of surface roughness; quasi-empirical correction (max factor 2) | α'c = αc·[1 + (2/π)·atan(1.4·(Δ/δs)^2)], Δ = rms surface roughness, δs = skin depth | αc, Δ (m), δs (m) | Any TL conductor; factor → 2 when Δ >> δs | calc | p.85, eq. (2.107), ref [7] (Edwards) | high |
| POZAR-1064 | timing | Transient launch on a line: until the first reflection returns (t < 2l/vp) the line input looks like Z0, so the launched step is a divider of Zg and Z0; each end reflects by its Γ; steady state equals the DC circuit solution | v+ = V0·Z0/(Z0 + Zg); reflections ×ΓL at load, ×Γg at source; t_round-trip = 2l/vp; V_final = V0·RL/(Rg + RL) | V0, Zg, Z0, ZL, l, vp | Lossless line, resistive terminations | calc | p.85–87, Fig. 2.21–2.23 | high |
| POZAR-1065 | timing | Shorted line with matched source generates a short rectangular pulse: at position z the pulse has amplitude V0/2 over z/vp < t < (2l − z)/vp | pulse width at z = 2(l − z)/vp; open-circuit end doubles to V0 | l, vp | Matched source (Zg = Z0) | calc | p.87, Fig. 2.22 | high |
| POZAR-1066 | timing | Worked check (Example 2.9) bounce diagram: 12 V step, Rg = 50 Ω, Z0 = 100 Ω, RL = 200 Ω | v+ = 8.0 V; Γg = −1/3; ΓL = +1/3; waves 8 V, 8/3 V, −8/9 V, −8/27 V; (derived) V_final = 12·200/250 = 9.6 V | V0, Rg, Z0, RL | — | calc | p.88–89, Example 2.9, Fig. 2.26 | high |
| POZAR-1067 | cables | Reference data point (Problem 2.3): RG-402U semirigid coax — inner conductor diameter 0.91 mm, dielectric (PTFE) diameter 3.02 mm, copper conductors; manufacturer spec 50 Ω and 0.43 dB/m at 1 GHz | (derived) Z0 = (60/sqrt(2.08))·ln(3.02/0.91) = 49.9 Ω | — | Data stated in a problem statement (not a worked example) | calc | p.90, Problem 2.3 | medium |
| POZAR-1068 | cables | Coax geometry that minimizes conductor attenuation (fixed outer size): x·ln x = 1 + x with x = b/a | x = b/a = 3.591 → Z0 = 77 Ω for εr = 1 (Z0 = 60·ln 3.591 = 76.7 Ω; divide by sqrt(εr) for filled line) | b/a, εr | Result stated in Problem 2.27 ("show that … 77 Ω"); root computed | calc | p.93, Problem 2.27 | medium |

### Ch. 3 Transmission lines and waveguides

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| POZAR-1069 | transmission-line | Mode classes: TEM needs ≥ 2 conductors (Ez = Hz = 0, kc = 0, β = k); a single closed conductor (hollow waveguide) cannot carry TEM; TE/TM modes have kc ≠ 0 and a cutoff frequency | TEM: β = k = ω·sqrt(µε), Z_TEM = η; TE: Z_TE = kη/β; TM: Z_TM = βη/k; kc^2 = k^2 − β^2 | geometry | Uniform guide, homogeneous fill | review | p.96–101, eq. (3.6), (3.8), (3.17), (3.22), (3.26) | high |
| POZAR-1070 | materials | Dielectric attenuation of any mode in a guide/line COMPLETELY filled with a homogeneous low-loss dielectric | TE/TM: αd = k^2·tanδ/(2β) (Np/m); TEM: αd = k·tanδ/2 (Np/m), k = ω·sqrt(µ0ε0εr) | f, εr, tanδ, β | tanδ << 1; homogeneous fill only (partially filled lines e.g. microstrip use a filling factor, POZAR-1102) | calc | p.101–102, eq. (3.29), (3.30) | high |
| POZAR-1071 | transmission-line | Parallel-plate guide higher-order modes: TMn and TEn share a cutoff; TM0 = TEM (no cutoff); there is no TE0 mode; below cutoff the mode is evanescent (guide acts as high-pass) | fc = n/(2d·sqrt(µε)) = n·c/(2d·sqrt(εr)); λc = 2d/n | d, εr | W >> d; useful for modelling higher-order modes in stripline / plane pairs | calc | p.104–108, eq. (3.49), (3.53), (3.69) | high |
| POZAR-1072 | transmission-line | Waveguide-mode phase velocity exceeds the speed of light in the medium and guide wavelength exceeds the medium wavelength; defined only above cutoff | vp = ω/β > 1/sqrt(µε); λg = 2π/β > λ | β | TE/TM modes above cutoff | calc | p.105, eq. (3.51), (3.52); p.113 | high |
| POZAR-1073 | transmission-line | Parallel-plate conductor attenuation (TEM and higher modes); αc → ∞ as a TE/TM mode approaches cutoff | TEM: αc = Rs/(η·d) (Np/m); TMn: αc = 2kRs/(βηd); TEn: αc = 2kc^2·Rs/(kβηd) | Rs, d, η, k, β | Two lossy plates; Fig. 3.4 (graph) | calc | p.107–109, eq. (3.60)–(3.61), (3.72), Fig. 3.4, Table 3.1 | high |
| POZAR-1074 | transmission-line | Rectangular waveguide (a > b) cutoff frequencies; TE10 is the overall dominant mode; lowest TM is TM11; no TE00, TM00, TM01, TM10 | fc,mn = (1/(2π·sqrt(µε)))·sqrt((mπ/a)^2 + (nπ/b)^2) = (c/(2·sqrt(εr)))·sqrt((m/a)^2 + (n/b)^2); fc10 = 1/(2a·sqrt(µε)) | a, b, εr | Homogeneous fill | calc | p.113, eq. (3.84), (3.85); p.116, eq. (3.103) | high |
| POZAR-1075 | transmission-line | Operate rectangular waveguide single-mode (only TE10 propagates); a guide with more than one propagating mode is "overmoded" | fc10 < f < min(fc20, fc01) (a, b chosen so the next mode is above the band) | f, a, b | "Vast majority of waveguide applications" | calc | p.113 | high |
| POZAR-1076 | transmission-line | TE10 mode relations | kc = π/a; β = sqrt(k^2 − (π/a)^2); Z_TE = kη/β; P10 = ωµa^3·abs(A10)^2·b·Re(β)/(4π^2) | a, b, f | Propagating (β real) | calc | p.113–114, eq. (3.86), (3.90)–(3.92) | high |
| POZAR-1077 | transmission-line | TE10 conductor attenuation | αc = Rs·(2bπ^2 + a^3k^2)/(a^3·b·β·k·η) (Np/m) | Rs, a, b, k, β, η | Perturbation method; Fig. 3.8 shows brass guide a = 2.0 cm (graph) | calc | p.115, eq. (3.96), Fig. 3.8 | high |
| POZAR-1078 | transmission-line | Worked check (Example 3.1): Teflon-filled (εr = 2.08, tanδ = 0.0004) copper K-band guide a = 1.07 cm, b = 0.43 cm | fc: TE10 9.72, TE20 19.44, TE01 24.19, TE11/TM11 26.07, TE21/TM21 31.03 GHz; at 15 GHz: k = 453.1 m^-1, β = 345.1 m^-1, αd = 0.119 Np/m = 1.03 dB/m; Rs(Cu, σ = 5.8×10^7) = 0.032 Ω; αc = 0.050 Np/m = 0.434 dB/m | a, b, εr, tanδ, σ, f | — | calc | p.116–119, Example 3.1 | high |
| POZAR-1079 | components | Rectangular waveguide components exist for standard bands 1–220 GHz; waveguide is still preferred for high power, mm-wave, satellite systems and some precision test; planar lines preferred otherwise (miniaturization/integration) | Band coverage 1–220 GHz (standard guides, App. I) | f, power | Medium selection | review | p.110 | high |
| POZAR-1080 | connectors | Waveguide flange joints: cover-to-cover joint needs smooth, clean, square contact surfaces (RF current crosses the joint); SWR typically < 1.03; imperfect junctions can break down at high power. Cover-to-choke joint uses two λg/4 sections to put the contact resistance in series with a very high impedance → no voltage drop, avoids breakdown; SWR typically < 1.05 and more frequency dependent | SWR(cover–cover) < 1.03; SWR(cover–choke) < 1.05; choke depth ≈ λg/4 + λg/4 | power level, band | Use choke flanges for high power | inspect | p.120–121, Point of Interest "Waveguide Flanges" | high |
| POZAR-1081 | transmission-line | Circular waveguide (radius a) cutoff: TEnm uses roots p'nm of Jn'(x); TMnm uses roots pnm of Jn(x). TE11 is dominant (p'11 = 1.841); next is TM01 (p01 = 2.405); no TE10/TM10 | fc,nm = p·c/(2π·a·sqrt(εr)); λc = 2π/kc, kc = p/a | a, εr | Values in Table 2-9 | calc | p.123–126, eq. (3.125), (3.127), (3.140), Tables 3.3–3.4 | high |
| POZAR-1082 | transmission-line | Circular TE11 conductor attenuation; TE01 attenuation falls with frequency (attractive for long low-loss runs) but TE01 is not dominant, so power converts to lower propagating modes | αc(TE11) = (Rs/(a·k·η·β))·(kc^2 + k^2/(p'11^2 − 1)) (Np/m) | Rs, a, k, β | Fig. 3.12: copper, a = 2.54 cm (graph) | calc | p.125–127, eq. (3.133), Fig. 3.12, 3.13 | high |
| POZAR-1083 | transmission-line | Worked check (Example 3.2): Teflon-filled (εr = 2.08, tanδ = 0.0004) gold-plated (σ = 4.1×10^7) circular guide a = 0.5 cm, 30 cm long at 14 GHz | fc(TE11) = 12.19 GHz; fc(TM01) = 15.92 GHz (only TE11 propagates at 14 GHz); k = 422.9 m^-1; β = 208.0 m^-1; αd = 0.172 Np/m = 1.49 dB/m; Rs = 0.0367 Ω; αc = 0.0672 Np/m = 0.583 dB/m; α = 2.07 dB/m; loss = 0.62 dB | geometry, materials, f | — | calc | p.127–130, Example 3.2 | high |
| POZAR-1084 | transmission-line | Coax higher-order modes: dominant waveguide-type mode is TE11; avoiding its propagation sets an upper limit on coax size (or on frequency for a given cable) and thereby on power capacity; multiple propagating modes with different β cause undesirable effects | kc(TE11) ≈ 2/(a + b) (approximate; exact from Jn'(kca)Yn'(kcb) = Jn'(kcb)Yn'(kca), Fig. 3.16); fc = c·kc/(2π·sqrt(εr)) | a, b, εr | Approximation vs graph: b/a = 3.33 → kca = 0.462 approx vs 0.45 exact | calc | p.131–133, eq. (3.159), Fig. 3.16 | high |
| POZAR-1085 | derating | Coax usable frequency limit: apply a 5% safety margin below the TE11 cutoff | f_max = 0.95·fc(TE11) | fc(TE11) | "In practice, a 5% safety margin is usually recommended" | calc | p.133, Example 3.3 | high |
| POZAR-1086 | cables | Worked check (Example 3.3): RG-401U semirigid coax, inner/outer conductor diameters 0.0645 in / 0.215 in, Teflon εr = 2.2 | b/a = 3.33; kca = 0.45 (Fig. 3.16); kc = 549.4 m^-1; fc(TE11) = 17.7 GHz; f_max = 16.8 GHz | diameters, εr | — | calc | p.132–133, Example 3.3 | high |
| POZAR-1087 | connectors | 50 Ω is a compromise impedance: air coax has minimum attenuation near 77 Ω and maximum power capacity near 30 Ω; 75 Ω is used for television systems | Z_min-loss ≈ 77 Ω; Z_max-power ≈ 30 Ω; standard 50 Ω / 75 Ω (TV) | — | Air-filled coax | review | p.134, Point of Interest "Coaxial Connectors" | high |
| POZAR-1088 | connectors | Connector upper-frequency limits (Pozar): Type-N (female OD ≈ 0.625 in) 11–18 GHz depending on cable size; TNC (threaded BNC) below 1 GHz; SMA (female OD ≈ 0.25 in) 18–25 GHz, most common microwave connector; APC-7 precision, sexless, SWR < 1.04 up to 18 GHz (measurement use); 2.4 mm (SMA-family, mm-wave) to about 50 GHz | f_op ≤ connector limit: N 11–18 GHz; TNC < 1 GHz; SMA 18–25 GHz; APC-7 18 GHz (SWR < 1.04); 2.4 mm ≈ 50 GHz | f_max, connector type | Connector selection; also require low SWR, higher-order-mode-free operation, repeatability after connect/disconnect, mechanical strength | review | p.134–135, Point of Interest "Coaxial Connectors" | high |
| POZAR-1089 | rf | Surface waves on a grounded dielectric sheet (thickness d): TM0 has ZERO cutoff (always present for any εr > 1, d > 0); mode order TM0, TE1, TM1, TE2, TM2, …; surface waves can be excited on microstrip and slotline | TMn: fc = n·c/(2d·sqrt(εr − 1)), n = 0, 1, 2, …; TEn: fc = (2n − 1)·c/(4d·sqrt(εr − 1)), n = 1, 2, …; first TE (TE1) cutoff = c/(4d·sqrt(εr − 1)) | d, εr | Infinite grounded slab; field decays as e^{−h(x−d)} above slab | calc | p.135–139, eq. (3.167), (3.174) | high |
| POZAR-1090 | transmission-line | Stripline (strip width W centred between ground planes spaced b, homogeneous εr) is a true TEM line; usually built by etching the strip on a grounded substrate of thickness b/2 and covering with a second grounded substrate; air dielectric is used when loss must be minimized | vp = c/sqrt(εr); β = sqrt(εr)·k0; Z0 = 1/(vp·C) (c = 3×10^8 m/s) | εr | Symmetric, homogeneous stripline | calc | p.141–142, eq. (3.176)–(3.178) | high |
| POZAR-1091 | stackup | Suppress stripline higher-order (parallel-plate/waveguide) modes: keep BOTH the ground-plane spacing and the sidewall width below half a wavelength in the dielectric; use shorting vias between the ground planes to enforce the sidewall-width condition; add shorting vias wherever an asymmetry between the ground planes is introduced (e.g. surface-mounted coaxial transition) | b < λd/2 and w_sidewall (via-wall to via-wall across the line) < λd/2, λd = c/(f_max·sqrt(εr)) | b, via-fence spacing, εr, f_max | Stripline circuits; applies at the highest frequency of interest | calc | p.141 | high |
| POZAR-1092 | transmission-line | Stripline characteristic impedance (analysis; curve fit to exact conformal-mapping solution) — Z0 falls as W increases | Z0 = (30π/sqrt(εr))·b/(We + 0.441b); We/b = W/b for W/b > 0.35; We/b = W/b − (0.35 − W/b)^2 for W/b < 0.35 | W, b, εr | Zero-thickness strip; accurate to about 1% of exact | calc | p.142–143, eq. (3.179) | high |
| POZAR-1093 | transmission-line | Stripline width synthesis (inverse of POZAR-1092) | x = 30π/(sqrt(εr)·Z0) − 0.441; W/b = x for sqrt(εr)·Z0 < 120; W/b = 0.85 − sqrt(0.6 − x) for sqrt(εr)·Z0 > 120 | Z0, b, εr | Zero-thickness strip | calc | p.143, eq. (3.180) | high |
| POZAR-1094 | transmission-line | Stripline conductor attenuation (approximate; perturbation/Wheeler) | sqrt(εr)Z0 < 120: αc = 2.7×10^-3·Rs·εr·Z0·A/(30π(b − t)); sqrt(εr)Z0 > 120: αc = 0.16·Rs·B/(Z0·b) (Np/m); A = 1 + 2W/(b − t) + (1/π)·((b + t)/(b − t))·ln((2b − t)/t); B = 1 + (b/(0.5W + 0.7t))·(0.5 + 0.414t/W + (1/2π)·ln(4πW/t)) | W, b, t (strip thickness), Rs, εr, Z0 | SI units (m, Ω) | calc | p.143, eq. (3.181) | high |
| POZAR-1095 | transmission-line | Stripline dielectric attenuation is the TEM result | αd = k·tanδ/2 = π·f·sqrt(εr)·tanδ/c (Np/m) | f, εr, tanδ | Homogeneous fill | calc | p.143, eq. (3.30) | high |
| POZAR-1096 | transmission-line | Worked check (Example 3.5): 50 Ω copper stripline, b = 0.32 cm, εr = 2.20, tanδ = 0.001, t = 0.01 mm, 10 GHz | sqrt(εr)Z0 = 74.2; x = 0.830; W = 0.266 cm; k = 310.6 m^-1; αd = 0.155 Np/m; Rs = 0.026 Ω; A = 4.74; αc = 0.122 Np/m; α = 0.277 Np/m = 2.41 dB/m; λ = 2.02 cm; 0.049 dB/λ | geometry, materials | — | calc | p.143–144, Example 3.5 | high |
| POZAR-1097 | transmission-line | Stripline closed-form Z0 accuracy (Example 3.6, εr = 2.55): formula (3.179) is within ~2% of commercial CAD for 0.25 ≤ W/b ≤ 2 but ~9% low at W/b = 5; a uniform-charge numerical estimate (3.192) runs 4–7% high for narrow strips | See Table 2-12 (W/b = 0.25…5.0) | W/b | Validation of calculator vs CAD | review | p.146–147, Example 3.6 | high |
| POZAR-1098 | transmission-line | Microstrip is not a pure TEM line (hybrid TM–TE; phase matching at the air–dielectric interface impossible); for electrically thin substrates (d << λ) the fields are quasi-TEM and quasi-static formulas apply; effective permittivity lies between 1 and εr and depends on εr, d, W and frequency | vp = c/sqrt(εe); β = k0·sqrt(εe); 1 < εe < εr | εr, d, W, f | d << λ (quasi-static) | review | p.147–148, eq. (3.193), (3.194) | high |
| POZAR-1099 | transmission-line | Microstrip effective dielectric constant (quasi-static curve fit) | εe = (εr + 1)/2 + ((εr − 1)/2)·1/sqrt(1 + 12d/W) | εr, d, W | Quasi-static (DC); zero strip thickness implied | calc | p.148, eq. (3.195) | high |
| POZAR-1100 | transmission-line | Microstrip characteristic impedance (analysis) | W/d ≤ 1: Z0 = (60/sqrt(εe))·ln(8d/W + W/(4d)); W/d ≥ 1: Z0 = 120π/(sqrt(εe)·[W/d + 1.393 + 0.667·ln(W/d + 1.444)]) (Ω) | W, d, εe | Quasi-static; curve fits to rigorous quasi-static solutions (Bahl & Trivedi; Gupta, Garg & Bahl) | calc | p.148, eq. (3.196) | high |
| POZAR-1101 | transmission-line | Microstrip width synthesis for a target Z0 | W/d < 2: W/d = 8e^A/(e^{2A} − 2); W/d > 2: W/d = (2/π)·[B − 1 − ln(2B − 1) + ((εr − 1)/(2εr))·(ln(B − 1) + 0.39 − 0.61/εr)]; A = (Z0/60)·sqrt((εr + 1)/2) + ((εr − 1)/(εr + 1))·(0.23 + 0.11/εr); B = 377π/(2·Z0·sqrt(εr)) | Z0, εr | Guess W/d < 2 first, verify, else use the W/d > 2 branch | calc | p.148–149, eq. (3.197) | high |
| POZAR-1102 | transmission-line | Microstrip dielectric attenuation = TEM result × filling factor (fields partly in lossless air) | αd = k0·εr·(εe − 1)·tanδ/(2·sqrt(εe)·(εr − 1)) (Np/m); filling factor q = εr(εe − 1)/(εe(εr − 1)) | f, εr, εe, tanδ | Quasi-TEM | calc | p.149, eq. (3.198) | high |
| POZAR-1103 | transmission-line | Microstrip conductor attenuation (approximate) | αc = Rs/(Z0·W) (Np/m), Rs = sqrt(ωµ0/(2σ)) | Rs, Z0, W | Approximate; overestimates vs CAD (Example 3.7: 0.094 vs 0.054 dB/cm) | calc | p.149, eq. (3.199) | high |
| POZAR-1104 | transmission-line | For most microstrip substrates conductor loss is more significant than dielectric loss; exceptions may occur with some semiconductor substrates | Expect αc > αd (check both; do not drop αc) | αc, αd | Low-loss laminates / ceramics | calc | p.149 | high |
| POZAR-1105 | transmission-line | Worked check (Example 3.7): 50 Ω microstrip on 0.5 mm alumina (εr = 9.9, tanδ = 0.001), copper, 270° at 10 GHz | A = 2.142; W/d = 0.9654; W = 0.483 mm; εe = 6.665; k0 = 209.4 m^-1; l = 8.72 mm; αd = 0.255 Np/m = 0.022 dB/cm; Rs = 0.026 Ω; αc = 0.0108 Np/cm = 0.094 dB/cm; total loss 0.101 dB. CAD: W = 0.478 mm, εe = 6.83, l = 8.61 mm, αd = 0.022 dB/cm, αc = 0.054 dB/cm | geometry, materials | Formulas within a few % of CAD except αc (largest discrepancy) | calc | p.149–150, Example 3.7 | high |
| POZAR-1106 | transmission-line | Microstrip dispersion: εe rises from εe(0) toward εr with frequency (current distribution across the strip also varies; strip thickness mainly affects conductor loss) | εe(f) = εr − (εr − εe(0))/(1 + G(f)); G(f) = g·(f/fp)^2; g = 0.6 + 0.009·Z0; fp = Z0/(8π·d) (Z0 in Ω, f and fp in GHz, d in cm) | εr, εe(0), Z0, d, f | Approximate model [Bahl & Trivedi]; Example 3.8: reasonable to ~10 GHz, overestimates above | calc | p.150–151, eq. (3.200) | high |
| POZAR-1107 | transmission-line | Use εe at the operating frequency for phase-critical lines: frequency variation of εe matters more than that of Z0 (phase delay of long lines; dispersion of broadband signals), while a small Z0 change only adds a small mismatch | Worked check (Example 3.8): 25 Ω line, εr = 10.0, d = 0.65 mm → W = 2.00 mm, εe(0) = 7.53; 1.093 cm line: 360° using εe(0) vs ≈374° using εe(10 GHz) = 8.12 (CAD) → ≈14° phase error | f, l, εe(f) | Phase-matched lines, couplers, filters | calc | p.150–153, Example 3.8, Fig. 3.27 (graph) | medium |
| POZAR-1108 | process | Closed-form microstrip/stripline approximations are valid only over limited frequency/parameter ranges; modern CAD (numerical/EM) tools give accurate results over wide ranges and are usually preferred | Use closed forms for synthesis/first cut, then verify in CAD/EM solver | — | Design flow | review | p.150–151 | high |
| POZAR-1109 | rf | Microstrip TM0 surface-wave coupling threshold (TM0 has zero cutoff but little coupling until this frequency): excess loss and coupling to adjacent elements above it | fT1 = (c/(2π·d))·sqrt(2/(εr − 1))·atan(εr); equals 35%–66% of the TM1 surface-wave cutoff for εr = 1…10 | d, εr | Microstrip on grounded substrate | calc | p.151, eq. (3.201) | high |
| POZAR-1110 | rf | Microstrip TE1 surface-wave threshold: transverse currents at discontinuities (bends, junctions, width steps — i.e. most practical circuits) couple to TE surface waves above this frequency | fT2 = c/(4d·sqrt(εr − 1)) | d, εr | Circuits with transverse discontinuities | calc | p.151, eq. (3.202) | high |
| POZAR-1111 | rf | Wide-microstrip transverse resonance: strip edges act roughly as magnetic walls; resonance when effective width W + d/2 ≈ λ/2 in the dielectric (rare in practice) | fT3 = c/(sqrt(εr)·(2W + d)) | W, d, εr | Wide lines | calc | p.151, eq. (3.203) | high |
| POZAR-1112 | rf | Wide-microstrip parallel-plate mode when strip–ground spacing approaches λ/2 in the dielectric; for thinner strips fringing lowers this threshold by as much as 50% | fT4 = c/(2d·sqrt(εr)) (wide lines); narrow lines: down to ≈ 0.5·fT4 | d, εr, W | Wide microstrip | calc | p.151–152, eq. (3.204) | high |
| POZAR-1113 | rf | The surface-wave and higher-order-mode thresholds together impose an upper frequency limit of operation for a given microstrip geometry (function of substrate thickness, εr and strip width) | f_max,op < min(fT1, fT2, fT3, fT4) (fT4 derated to 0.5·fT4 for narrow strips) | d, εr, W | Combination via min() is the rulebook's mechanization of Pozar's statement | calc | p.152 | medium |
| POZAR-1114 | transmission-line | Transverse resonance technique for cutoff frequencies of layered guides: at cutoff the transverse equivalent line is resonant, so the input impedances looking either way sum to zero at any point; gives only the cutoff (not fields or conductor loss) | Z_in,right(x) + Z_in,left(x) = 0 for all x; TE line impedance Z = kη/ky | layer thicknesses, εr | Guides with dielectric layers (e.g. partially filled guide: ky_a·tan(ky_d·t) + ky_d·tan(ky_a(b − t)) = 0) | calc | p.153–154, eq. (3.206)–(3.209) | high |
| POZAR-1115 | timing | Group velocity is the speed of a narrowband signal envelope; a lossless TEM line (β = ω/c·sqrt(εr)) is dispersionless; a lossy TEM line can still distort if α varies with f; in a waveguide vg < c < vp | vg = (dβ/dω)^-1 at ω0; air waveguide: vg = c·β/k0, vp = c·k0/β | β(ω) | Narrow bandwidth or mild dispersion (Taylor linearization of β) | calc | p.154–157, eq. (3.222), Example 3.9 | high |
| POZAR-1116 | transmission-line | Medium selection guide (Table 3.6): coax — TEM, no dispersion, high BW, medium loss, medium power, large, hard to integrate; waveguide — TE10, medium dispersion, low BW, low loss, high power, large; stripline — TEM, no dispersion, high BW, high loss, low power, medium size, easy fab, fair integration; microstrip — quasi-TEM, low dispersion, high BW, high loss, low power, small, easy fab and integration | See Table 2-13 | application needs | "General guidelines only" | review | p.158, Table 3.6 | high |
| POZAR-1117 | transmission-line | Rectangular-waveguide practical bandwidth is slightly less than an octave because TE20 starts at 2× the TE10 cutoff; ridge loading lowers the dominant cutoff → wider bandwidth and more constant impedance (often tapered for matching) but reduces power-handling capacity | BW_single-mode < 2:1 (fc20 = 2·fc10); ridge: lower fc10, lower P_max | a, ridge geometry | Waveguide selection | review | p.158–159, Fig. 3.31 | high |
| POZAR-1118 | transmission-line | Other planar/guided lines: dielectric waveguide (εr2 ridge > εr1 substrate) suits mm-wave to optical but is very lossy at bends/junctions; slotline Z0 is set by slot width (quasi-TEM); coplanar waveguide supports even and odd quasi-TEM modes and is convenient for active circuits (centre conductor with nearby grounds) | Qualitative | — | Medium selection | review | p.159–160, Fig. 3.32–3.34 | high |
| POZAR-1119 | mechanical | Covered (shielded) microstrip: the metal cover is usually placed several substrate thicknesses above the circuit, and it can still perturb circuit operation enough that it must be included in the design (EM model with lid) | Cover height h_cover ≥ "several" d; include lid in EM simulation | cover height, d | Shielded modules/housings | sim | p.159, Fig. 3.35 | medium |
| POZAR-1120 | derating | Air-filled line/guide power capacity is usually limited by voltage breakdown (thermal limits for some lines): room-temperature sea-level air breaks down at about Ed = 3×10^6 V/m; limits are PEAK values (arcing is a fast transient), average capacity is lower | Ed(air) ≈ 3×10^6 V/m (3 kV/mm) | E_peak in structure | Room temperature, sea-level pressure; pressurizing or dielectric fill raises Ed but dielectric heating may then limit | calc | p.160–161, Point of Interest "Power Capacity of Transmission Lines" | high |
| POZAR-1121 | derating | Coax peak power capacity; E is maximum at the inner conductor; for a line free of higher-order modes at f_max there is an absolute ceiling | Vmax = Ed·a·ln(b/a); Pmax = Vmax^2/(2Z0) = (π·a^2·Ed^2/η0)·ln(b/a); with no higher-order modes: Pmax = (0.025/η0)·(c·Ed/f_max)^2 = 5.8×10^12·(Ed/f_max)^2 W → ≈ 520 kW at 10 GHz | a, b, Ed, f_max | Air coax; peak power (text labels Vmax "peak-to-peak") | calc | p.160 | high |
| POZAR-1122 | derating | Rectangular waveguide (TE10) peak power capacity; E maximum at guide centre x = a/2; with a < c/f_max to avoid TE20 (standard guides a ≈ 2b) | Pmax = a·b·Ed^2/(4·Zw); ceiling Pmax = (0.11/η0)·(c·Ed/f_max)^2 = 2.6×10^13·(Ed/f_max)^2 W → ≈ 2300 kW at 10 GHz (vs ≈ 520 kW for coax) | a, b, Zw, Ed, f_max | Air-filled TE10 | calc | p.160–161 | high |
| POZAR-1123 | derating | Power-capacity derating: apply a safety factor of at least two (limit to about half the breakdown value); reflections reduce capacity further — abs(Γ) = 1 doubles peak voltage and cuts capacity by 4 | P_allowed ≤ Pmax/2; with mismatch: P_allowed ≤ Pmax/(2·(1 + abs(Γ))^2) (general (1 + abs(Γ))^2 form derived from Vmax = (1 + abs(Γ))V+; text states the abs(Γ) = 1 → ÷4 case) | Pmax, abs(Γ) | Peak power | calc | p.161 | medium |

### Ch. 4 Microwave network analysis

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| POZAR-1124 | rf | Network (circuit) analysis replaces field analysis once each port has defined V, I (or wave amplitudes); a transition between line types or a line discontinuity generally cannot be treated as a simple junction of two lines — it needs an equivalent circuit for the reactance (stored energy) at the junction; know when circuit analysis is an oversimplification and a field (EM) solution is required | Model every transition/discontinuity as a two-port (equivalent circuit or S-block), not as an ideal junction | layout discontinuities | All RF circuit models | review | p.165–166 | high |
| POZAR-1125 | transmission-line | Equivalent voltage/current for non-TEM (waveguide) modes are not unique; define per mode with V ∝ transverse E, I ∝ transverse H, (1/2)V·I* = mode power, and V+/I+ = Z0 chosen equal to the wave impedance (ZTE/ZTM) or normalized to 1 | C1·C2* = ∫S e × h*·z ds; C1/C2 = Z0 (= Zw or 1). TE10 with Z0 = ZTE: C1 = sqrt(ab/2), C2 = (1/ZTE)·sqrt(ab/2) | mode fields | Waveguide ports | calc | p.166–170, eq. (4.6)–(4.12), Example 4.1 | high |
| POZAR-1126 | transmission-line | Three distinct impedances: η = sqrt(µ/ε) (medium only; = wave impedance of a plane wave); Zw = Et/Ht (wave type: ZTEM, ZTE, ZTM; may depend on line, material, frequency); Z0 = V+/I+ (unique only for TEM lines) | η, Zw, Z0 — do not interchange | — | — | review | p.170–171 | high |
| POZAR-1127 | transmission-line | Worked check (Example 4.2): X-band guide a = 2.286 cm, b = 1.016 cm, air (z < 0) to Rexolite εr = 2.54 (z > 0), 10 GHz, TE10 via equivalent line Z0 = k0η0/β | k0 = 209.4 m^-1; βa = 158.0 m^-1; βd = 304.1 m^-1; Z0a = 500.0 Ω; Z0d = 259.6 Ω; Γ = −0.316 | a, εr, f | Only TE10 propagates in both regions | calc | p.171–172, Example 4.2 | high |
| POZAR-1128 | rf | One-port impedance from power and stored energy: Re part = dissipation, Im part = net stored energy; lossless one-port is a pure reactance, inductive if Wm > We | Zin = (P + 2jω(Wm − We))/((1/2)abs(I)^2); lossless: X = 4ω(Wm − We)/abs(I)^2 | P, Wm, We, I | Any one-port | calc | p.172–173, eq. (4.17), (4.18) | high |
| POZAR-1129 | rf | Even/odd symmetry of network functions (real time signals): R(ω) even, X(ω) odd; Γ(−ω) = Γ*(ω); abs(Γ(ω)) and abs(Γ(ω))^2 are even — fit abs(Γ) models only with even series a + bω^2 + cω^4 + … | R(−ω) = R(ω); X(−ω) = −X(ω); abs(Γ(−ω)) = abs(Γ(ω)) | Z(ω) | Linear networks | calc | p.173, eq. (4.20)–(4.23) | high |
| POZAR-1130 | rf | Impedance and admittance matrices: Zij = Vi/Ij with all other ports OPEN (Ik = 0, k ≠ j); Yij = Ii/Vj with all other ports SHORTED; [Y] = [Z]^-1; an N-port has 2N^2 real degrees of freedom in general | [V] = [Z][I]; [I] = [Y][V] | port V, I | Terminal planes define phase reference | calc | p.174–175, eq. (4.25)–(4.29) | high |
| POZAR-1131 | rf | Reciprocity: a network with no active devices and no nonreciprocal media (ferrites, plasmas) is reciprocal | Zij = Zji; Yij = Yji; [S] = [S]^t | network contents | — | calc | p.175–176, eq. (4.36); p.182, eq. (4.48) | high |
| POZAR-1132 | rf | Lossless network: all impedance and admittance matrix elements are purely imaginary | Re{Zmn} = 0 (and Re{Ymn} = 0) for all m, n | [Z] | Reciprocal lossless N-port | calc | p.177, eq. (4.38), (4.39) | high |
| POZAR-1133 | rf | Worked check (Example 4.3): T-network (series ZA, series ZB, shunt ZC) | Z11 = ZA + ZC; Z12 = Z21 = ZC; Z22 = ZB + ZC | ZA, ZB, ZC | — | calc | p.177–178, Example 4.3 | high |
| POZAR-1134 | rf | Scattering matrix: Sij = Vi−/Vj+ with all other incident waves zero, i.e. all other ports terminated in MATCHED loads; Sii = reflection coefficient at port i, Sij = transmission coefficient j → i; measured directly with a VNA | [V−] = [S][V+]; Sij = Vi−/Vj+ at Vk+ = 0 (k ≠ j) | port waves | Linear network; equal port reference impedances unless generalized | measure | p.178–179, eq. (4.40), (4.41) | high |
| POZAR-1135 | rf | The reflection seen at port n equals Snn ONLY if all other ports are matched (likewise transmission = Smn only if others matched); S-parameters are properties of the network alone and do not change with terminations/excitation | Γport,n = Snn iff all other ports matched; otherwise use POZAR-1153 | terminations | Linear networks | review | p.183–184 | high |
| POZAR-1136 | components | Worked check (Example 4.4): matched 3 dB, 50 Ω T attenuator — series 8.56 Ω, shunt 141.8 Ω, series 8.56 Ω | Zin = 8.56 + 141.8‖(8.56 + 50) = 50 Ω → S11 = S22 = 0; S21 = S12 = (41.44/(41.44 + 8.56))·(50/(50 + 8.56)) = 0.707; Pout = Pin/2 (−3 dB) | resistor values | — | calc | p.179–180, Example 4.4, Fig. 4.8 | high |
| POZAR-1137 | rf | S ↔ Z (normalized; all port impedances equal, set to 1) | [S] = ([Z] + [U])^-1([Z] − [U]) = ([Z] − [U])([Z] + [U])^-1; [Z] = ([U] + [S])([U] − [S])^-1; one-port: S11 = (z11 − 1)/(z11 + 1) | [Z] or [S] | Equal real port impedances; else use generalized S (POZAR-1142) | calc | p.180–181, eq. (4.44), (4.45), (4.47) | high |
| POZAR-1138 | rf | Lossless network ⇔ unitary S: each column (and row) has unit norm and different columns are orthogonal | [S]^t[S]* = [U]; Σk abs(Ski)^2 = 1; Σk Ski·Skj* = 0 (i ≠ j) | [S] | Equal port impedances | calc | p.182–183, eq. (4.51)–(4.53) | high |
| POZAR-1139 | rf | Worked check (Example 4.5): [S] = [[0.15∠0°, 0.85∠−45°], [0.85∠45°, 0.2∠0°]] | Not reciprocal (S12 ≠ S21); not lossless (abs(S11)^2 + abs(S21)^2 = 0.745 ≠ 1); port 2 matched: RL = −20 log 0.15 = 16.5 dB; port 2 shorted (ΓL = −1): Γ = S11 − S12S21/(1 + S22) = −0.452 → RL = 6.9 dB | [S] | — | calc | p.183, Example 4.5 | high |
| POZAR-1140 | test | Reference-plane shift (de-embedding of line lengths): moving port n's plane outward by electrical length θn = βn·ln | [S'] = diag(e^{−jθn})·[S]·diag(e^{−jθn}); S'nn = e^{−2jθn}·Snn; S'mn = e^{−j(θm + θn)}·Smn | [S], θn | Lossless feed lines | calc | p.184–185, eq. (4.56) | high |
| POZAR-1141 | rf | Power waves (valid for complex reference impedance ZR = RR + jXR, lossy lines, or circuits with no line): delivered power is abs(a)^2/2 − abs(b)^2/2 for ANY ZR; choosing ZR = ZL* makes b = 0 but does NOT imply a conjugate match or maximum power. The voltage-wave form PL = (abs(V0+)^2 − abs(V0−)^2)/(2Z0) is valid only for real Z0 | a = (V + ZR·I)/(2·sqrt(RR)); b = (V − ZR*·I)/(2·sqrt(RR)); Γp = b/a = (ZL − ZR*)/(ZL + ZR); PL = (abs(a)^2 − abs(b)^2)/2 | V, I, ZR | Complex source/load impedances | calc | p.185–187, eq. (4.58)–(4.64) | high |
| POZAR-1142 | rf | Generalized (power-wave) S-matrix with per-port reference impedances ZRi; diagonal elements can be zeroed by proper choice of ZRi | [Sp] = [F]([Z] − [ZR]*)([Z] + [ZR])^-1[F]^-1, [F] = diag(1/(2·sqrt(Re ZRi))), [ZR] = diag(ZRi) | [Z], ZRi | Convert ordinary S → Z (eq. 4.45) → Sp | calc | p.187–188, eq. (4.67), (4.68) | high |
| POZAR-1143 | rf | Generator–load power without a line | V = V0·ZL/(ZL + Zg); I = V0/(ZL + Zg); PL = (abs(V0)^2/2)·RL/abs(ZL + Zg)^2; conjugate match (Zg = ZL*): PL = abs(V0)^2/(8RL) | V0 (peak), Zg, ZL | — | calc | p.187, eq. (4.65), (4.66) | high |
| POZAR-1144 | test | Vector network analyzer: 2- or 4-channel receiver measuring magnitude and phase of incident, reflected and transmitted waves; accuracy relies on error correction with a 12-term error model and calibration (corrects coupler mismatch, imperfect directivity, loss, frequency-response variation); time-domain response via inverse Fourier transform of the swept data | Calibrate (12-term) before S-parameter acceptance measurements; example instrument range 10 MHz–67 GHz (Agilent N5247A) | f range | — | measure | p.179, Fig. 4.7; p.188, Point of Interest "The Vector Network Analyzer" | high |
| POZAR-1145 | rf | ABCD (transmission) matrix: defined with I2 flowing OUT of port 2 so cascades chain; the ABCD of a cascade is the ordered product (matrix multiplication is not commutative) | [V1; I1] = [A B; C D]·[V2; I2]; [ABCD]total = [ABCD]1·[ABCD]2·… (in physical order) | element ABCDs | Two-port cascades | calc | p.188–190, eq. (4.69)–(4.71) | high |
| POZAR-1146 | rf | ABCD building blocks (Table 4.1) | Series Z: [1, Z; 0, 1]; shunt Y: [1, 0; Y, 1]; line (Z0, βl): [cos βl, jZ0 sin βl; jY0 sin βl, cos βl]; ideal transformer N:1: [N, 0; 0, 1/N]; π (shunt Y1, series Y3, shunt Y2): A = 1 + Y2/Y3, B = 1/Y3, C = Y1 + Y2 + Y1Y2/Y3, D = 1 + Y1/Y3; T (series Z1, shunt Z3, series Z2): A = 1 + Z1/Z3, B = Z1 + Z2 + Z1Z2/Z3, C = 1/Z3, D = 1 + Z2/Z3 | element values | Lossless line entry; lossy: replace jβl → γl (cosh/sinh) (derived) | calc | p.190, Table 4.1, Example 4.6 | high |
| POZAR-1147 | rf | Z → ABCD, and reciprocity test on ABCD | A = Z11/Z21; B = (Z11Z22 − Z12Z21)/Z21; C = 1/Z21; D = Z22/Z21; reciprocal ⇒ AD − BC = 1 | [Z] | I2 sign per ABCD convention | calc | p.191, eq. (4.72), (4.73) | high |
| POZAR-1148 | rf | Two-port parameter conversions S/Z/Y/ABCD (Table 4.2, all ports Z0 real) | Full set in Table 2-17 of this rulebook | any 2-port set, Z0 | Equal real Z0 at both ports | calc | p.192, Table 4.2 | high |
| POZAR-1149 | rf | Two-port equivalent circuits: reciprocal two-port → T or π equivalent with 6 real degrees of freedom; lossless → 3 degrees of freedom and a purely reactive T/π; a nonreciprocal network cannot be represented by a passive equivalent circuit of reciprocal elements | T: series (Z11 − Z12), (Z22 − Z12), shunt Z12; π: shunt (Y11 + Y12), (Y22 + Y12), series −Y12 (element values derived from Example 4.3 and duality; Fig. 4.13 labels not in extracted text) | [Z] or [Y] | Reciprocal networks | calc | p.193–194, Fig. 4.13; p.177, Example 4.3 | medium |
| POZAR-1150 | connectors | Line-type transitions (e.g. coax-to-microstrip) store electric/magnetic energy at the junction → reactive parasitics; characterize by measurement or numerical analysis and represent as a two-port (black box S-block) or a lumped equivalent (e.g. series L with shunt C1, C2) | Include transition model (L, C1, C2 or measured S) in every launch/connector simulation | transition geometry | Coax/microstrip, other line transitions, steps, bends | sim | p.191–193, Fig. 4.12 | high |
| POZAR-1151 | rf | Signal-flow-graph reduction rules: series branches multiply; parallel branches add; a self-loop S on a node divides incoming branches by (1 − S); a node may be split if each input/output combination is kept once (equivalent to Mason's rule) | series: S21·S32; parallel: Sa + Sb; self-loop: S21/(1 − S22) | flow graph | Linear networks | calc | p.194–197, Fig. 4.16, eq. (4.75)–(4.79) | high |
| POZAR-1152 | matching | Input/output reflection of a two-port terminated in arbitrary load/source | Γin = S11 + S12S21ΓL/(1 − S22ΓL); Γout = S22 + S12S21Γs/(1 − S11Γs) | [S], ΓL, Γs | Linear two-port | calc | p.197, Example 4.7 | high |
| POZAR-1153 | test | VNA calibration choice: calibration with known loads (short/open/match) is limited by the imperfection of the standards — errors grow at higher frequencies and as system quality improves; TRL needs no perfect standards: Thru (direct connection), Reflect (any large, unknown ΓL such as a nominal open or short; its sign must be known to within 180°), Line (matched line of unknown length and loss) | Use TRL (or equivalent) when standards are uncertain / at high frequency; solve eq. (4.84), (4.86)–(4.90) (Section 4 procedure) | T, R, L measurements | Error boxes assumed reciprocal, identical, symmetric (text derivation) | measure | p.197–202, Fig. 4.20–4.21 | high |
| POZAR-1154 | process | CAD role and limits: physics-based (EM solvers) vs circuit-based (equivalent-circuit) tools; flow = spec → initial design from experience → CAD model incl. loss and discontinuities → optimize → tolerance/error study → prototype → measure → iterate; essential for MMICs (cannot be tuned after fabrication); models cannot fully capture fabrication tolerances, surface roughness, spurious coupling, higher-order modes, junction discontinuities, thermal effects | Gate: tolerance analysis in CAD before prototype; measured prototype must meet spec or iterate | — | RF/microwave circuit development | review | p.202, Point of Interest "Computer-Aided Design for Microwave Circuits" | high |
| POZAR-1155 | rf | Waveguide discontinuity equivalent circuits: thin diaphragms (irises) give shunt inductance (inductive diaphragm), shunt capacitance (capacitive diaphragm) or a resonant combination (resonant iris); height change ≈ shunt C, width change ≈ shunt L with impedance step; component values depend on geometry and frequency, sometimes with reference-plane shifts | Qualitative (values from Marcuvitz, Waveguide Handbook [8]) | geometry | Rectangular/circular guide | review | p.203–204, Fig. 4.22 | high |
| POZAR-1156 | transmission-line | Microstrip discontinuities and their equivalent circuits: open end → shunt capacitance Cp; gap → series Cg with shunt Cp; width step → series L with shunt C; T-junction → L1, L2, L3 with shunt C; coax-to-microstrip → series L with shunts C1, C2; many printed-line discontinuities require numerical (EM) modeling | Include discontinuity models (or EM-extracted S) for every open end, gap, step, T and launch | layout | Microstrip (similar for stripline, slotline, CPW, covered microstrip) | sim | p.203–205, Fig. 4.23 | high |
| POZAR-1157 | rf | H-plane (width) step in rectangular waveguide behaves as a shunt inductance; modal-analysis solution converges quickly (evanescent modes decay fast) — two modes already close to Marcuvitz data | X = −jZ1a·(1 + A1)/(1 − A1), A1 = TE10 reflection from [Q][A] = [P] (eq. 4.106–4.108); Fig. 4.25: normalized inductance X·λg/(2a·Z1a) vs c/a for λ = 1.4a (graph) | a, c, λ | TE10 only propagating | calc | p.203–209, eq. (4.105)–(4.110), Fig. 4.25 | medium |
| POZAR-1158 | dfm | Microstrip bend compensation: a plain right-angle bend adds parasitic excess capacitance (extra conductor area at the corner); either use a swept bend with radius r ≥ 3W (costs area) or miter the corner; a miter length a = 1.8W is often used in practice (optimum depends on Z0 and bend angle); mitering also compensates steps and T-junctions | Swept bend: r ≥ 3W; mitered 90° bend: a ≈ 1.8W (a = miter dimension per Pozar figure, W = strip width) | W, bend geometry | Microstrip; applies to arbitrary bend angles | inspect | p.209–210, Point of Interest "Microstrip Discontinuity Compensation" (Edwards) | high |
| POZAR-1159 | rf | Uncompensated discontinuities (bends, width steps, junctions) introduce parasitic reactances → phase and amplitude errors, input/output mismatch, possibly spurious coupling or radiation; compensate either by including the discontinuity model and adjusting line lengths/impedances/stubs, or by chamfering/mitering the conductor | Every discontinuity either compensated (miter/chamfer) or modeled and compensated in the design | layout | Planar circuits | review | p.209 | high |
| POZAR-1160 | rf | Mode excitation: a correctly shaped current sheet excites a single waveguide mode, but practical probes/loops excite many modes, most of them evanescent (stored reactive energy near the feed); TEM/quasi-TEM lines usually have one propagating mode but the feed still adds reactance | Model feed reactance; ensure only the intended mode propagates | feed geometry | Waveguide and planar feeds | review | p.210–212 | high |
| POZAR-1161 | rf | Probe-fed rectangular waveguide (Example 4.8): thin current probe spanning the full height b at x = a/2 in an infinite guide, TE10 the only propagating mode | A1± = −Z1·I0/a; Rin = b·Z1/a, Z1 = k0η0/β1 (TE10 wave impedance); real for propagating TE10 | a, b, f | Infinitesimal probe diameter; guide open (matched) both ways | calc | p.214–215, Example 4.8 | high |
| POZAR-1162 | rf | Small-aperture coupling: an aperture in a conducting wall is equivalent to an electric dipole driven by the normal E (polarizability αe) and a magnetic dipole driven by the tangential H (polarizability αm); theory is approximate — valid for apertures small relative to wavelength and not too close to edges/corners | Pe = ε0·αe·n·En·δ(…); Pm = −αm·Ht·δ(…); equivalent J = jωPe, M = jωµ0Pm; round hole (radius r0): αe = 2r0^3/3, αm = 4r0^3/3; rectangular slot (length l, width d, H across slot): αe = αm = π·l·d^2/16 | aperture shape/size | Small apertures; slot length symbol l restored (script-l dropped by OCR) | calc | p.215–218, eq. (4.130), (4.131), (4.134), Table 4.3 | medium |
| POZAR-1163 | rf | Small round aperture centred in a transverse waveguide wall ≈ normalized shunt inductive susceptance; small-hole theory gives abs(Γ) slightly > 1 (artifact of the approximation) | B = −a·b/(2β·αm); Γ ≈ 4jβαm/(ab) − 1; T = 4jβαm/(ab), αm = 4r0^3/3 | a, b, β, r0 | TE10 incident, aperture small | calc | p.218–220, eq. (4.141), Fig. 4.32 | high |
| POZAR-1164 | rf | Broad-wall small-aperture coupling between two parallel guides (aperture centred at x = a/2): the electric dipole excites equal fields in both directions, the magnetic dipole excites opposite-sign fields — the basis of directional (Bethe-hole) coupling | Forward: A+ = (−jωA/P10)·(ε0αe − µ0αm/Z10^2); backward: A− = (−jωA/P10)·(ε0αe + µ0αm/Z10^2); P10 = ab/Z10 | αe, αm, a, b, Z10 | TE10 incident; off-centre aperture also couples Hz | calc | p.220–221, eq. (4.142)–(4.147) | high |
| POZAR-1165 | rf | Single series or shunt element between equal-Z0 ports: transmission follows from reflection (result stated in Problem 4.11) | Series Z: S12 = S21 = 1 − S11; shunt Z: S12 = S21 = 1 + S11 | Z, Z0 | Problem statement ("show that"); consistent with Table 2-17 | calc | p.223, Problem 4.11 | medium |
| POZAR-1166 | rf | Cascade of two two-ports A then B (result stated in Problem 4.12) — multiple reflections between the blocks reduce/alter transmission | S21 = S21A·S21B/(1 − S22A·S11B) | [SA], [SB] | Equal port impedances | calc | p.223, Problem 4.12 | medium |
| POZAR-1167 | rf | Lossless two-port limits (Problem 4.13): reciprocal → abs(S21)^2 = 1 − abs(S11)^2; a lossless nonreciprocal two-port cannot be unidirectional (S12 = 0 with S21 ≠ 0 impossible); a lossless, reciprocal three-port cannot be matched at all ports (Problem 4.15; proven in §7.1, see POZAR-1237) | abs(S21)^2 + abs(S11)^2 = 1 | [S] | Problem statements | review | p.223–224, Problems 4.13, 4.15 | medium |
| POZAR-1168 | transmission-line | Open-end microstrip fringing: the end capacitance Cf can be replaced by an extra line length Δl; Hammerstad–Bekkadal approximation (quoted in Problem 4.30) — shorten open stubs by Δl | Δl = 0.412·d·((εe + 0.3)/(εe − 0.258))·((w + 0.262d)/(w + 0.813d)); equivalence Δl = Cf·Z0·c/sqrt(εe) (derived). Data: 50 Ω, d = 0.158 cm, εr = 2.2 → w = 0.487 cm, εe = 1.894, Cf = 0.075 pF; (computed) H–B Δl ≈ 0.075 cm | w, d, εe | Microstrip open ends / open stubs | calc | p.226, Problem 4.30 | medium |

### Ch. 5 Impedance matching and tuning

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| POZAR-1169 | matching | Why match: maximum power is delivered when the load is matched to the line (generator matched) and feed-line loss is minimized; matching sensitive receive components (antenna, LNA) may improve SNR; matching in power-distribution networks (array feeds) reduces amplitude and phase errors | Match target: Zin(match network + load) = Z0 | — | Lossless matching network placed between line and load | review | p.228, Fig. 5.1 | high |
| POZAR-1170 | matching | Any load with a positive real part can be matched; a general match needs at least two degrees of freedom; choose the network by: complexity (simplest that meets spec — cheaper, smaller, more reliable, less lossy), bandwidth (any network matches perfectly at one frequency; broadband needs more complexity), implementation (e.g. tuning stubs are easier than multisection λ/4 transformers in waveguide), adjustability (variable loads) | Re{ZL} > 0 ⇒ matchable; ≥ 2 independent reactive parameters | ZL, band, medium | — | review | p.228–229, p.231 | high |
| POZAR-1171 | matching | L-section topology choice: if zL is inside the r = 1 circle (RL > Z0) put the shunt element next to the load and the series element toward the line (Fig. 5.2a); if outside (RL < Z0) put the series element next to the load and the shunt element toward the line (Fig. 5.2b); each element may be L or C → 8 circuits | RL > Z0 → shunt-at-load; RL < Z0 → series-at-load | RL, XL, Z0 | Lumped L networks | calc | p.229, Fig. 5.2 | high |
| POZAR-1172 | matching | L-section design equations, case RL > Z0 (shunt B at load, series X toward line); two solutions | B = [XL ± sqrt(RL/Z0)·sqrt(RL^2 + XL^2 − Z0·RL)]/(RL^2 + XL^2); X = 1/B + XL·Z0/RL − Z0/(B·RL) | RL, XL, Z0 | RL > Z0 guarantees real roots | calc | p.230, eq. (5.3a), (5.3b) | high |
| POZAR-1173 | matching | L-section design equations, case RL < Z0 (series X at load, shunt B toward line); two solutions | X = ± sqrt(RL(Z0 − RL)) − XL; B = ± sqrt((Z0 − RL)/RL)/Z0 | RL, XL, Z0 | RL < Z0 | calc | p.231, eq. (5.6a), (5.6b) | high |
| POZAR-1174 | matching | Element realization and sign convention: X > 0 → inductor, X < 0 → capacitor; B > 0 → capacitor, B < 0 → inductor; pick between the two solutions for smaller component values, better bandwidth, or lower SWR between network and load | L = X/(2πf); C_series = −1/(2πf·X); C_shunt = B/(2πf); L_shunt = −1/(2πf·B) (with b, x normalized: C = b/(2πf·Z0), L = x·Z0/(2πf)) | X, B, f | — | calc | p.230, p.232 | high |
| POZAR-1175 | matching | Worked check (Example 5.1): ZL = 200 − j100 Ω (200 Ω + 3.18 pF series) to 100 Ω at 500 MHz | zL = 2 − j1 (inside r = 1 circle); solution 1: b = 0.29 (chart 0.3), x = 1.22 → C = 0.92 pF shunt, L = 38.8 nH series; solution 2: b = −0.69, x = −1.22 → C = 2.61 pF series, L = 46.1 nH shunt; bandwidths similar (Fig. 5.3c) | ZL, Z0, f | — | calc | p.231–233, Example 5.1 | high |
| POZAR-1176 | components | Lumped-element matching is feasible up to about 1 GHz with discrete parts (higher in MICs); in hybrid/monolithic MICs lumped R, L, C work up to 60 GHz or higher only if the element length l < λ/10, and parasitic C/L, spurious resonances, fringing, loss and ground-plane effects must be included via CAD models | l_element < λ/10 at f_max (λ in the medium); discrete lumped L-sections ≲ 1 GHz | element length, f | MIC lumped elements | calc | p.229; p.233, Point of Interest "Lumped Elements for Microwave Integrated Circuits" | high |
| POZAR-1177 | components | MIC lumped-element value ranges: resistors from thin lossy films (nichrome, tantalum nitride, doped semiconductor) or chip resistors — low resistances are hard; small inductance from a short line or loop, up to about 10 nH with a spiral (larger L → more loss and shunt C → self-resonance limits f_max); shunt capacitance 0–0.1 pF from a short stub; series capacitance up to about 0.5 pF from a gap or interdigital gap; up to about 25 pF from MIM (monolithic or chip) | Spiral L ≤ ≈10 nH; stub C ≤ 0.1 pF; gap/interdigital C ≤ ≈0.5 pF; MIM C ≤ ≈25 pF | required values | Hybrid/monolithic MIC | review | p.234, Point of Interest (cont.) | high |
| POZAR-1178 | matching | Single-stub tuner medium choice: shunt stubs for microstrip/stripline; series stubs for slotline/CPW; open- and short-circuited stubs for the same susceptance differ in length by λ/4; open stubs are easier in microstrip/stripline (no via); short stubs are preferred in coax/waveguide because an open end may radiate (no longer purely reactive) | l_short = l_open ± λ/4 (same reactance) | line type | — | review | p.234–235 | high |
| POZAR-1179 | matching | Keep the matching stub as close as possible to the load (shortest d and l): improves match bandwidth and reduces loss from a high SWR on the line between stub and load | Prefer the solution with minimum d (and stub length) | d, l | Stub tuners (Example 5.2: shorter solution has significantly better bandwidth) | sim | p.236–237, Example 5.2, Fig. 5.5c | high |
| POZAR-1180 | matching | Shunt-stub tuner design equations (t = tan βd) | t = [XL ± sqrt(RL·((Z0 − RL)^2 + XL^2)/Z0)]/(RL − Z0) (RL ≠ Z0); t = −XL/(2Z0) if RL = Z0; d/λ = atan(t)/(2π) (t ≥ 0) or (π + atan t)/(2π) (t < 0); B = [RL^2·t − (Z0 − XL·t)(XL + Z0·t)]/(Z0·[RL^2 + (XL + Z0·t)^2]); open stub: lo/λ = −atan(B/Y0)/(2π); short stub: ls/λ = atan(Y0/B)/(2π); add λ/2 if negative | RL, XL, Z0 | Lossless lines | calc | p.238, eq. (5.7)–(5.11) | high |
| POZAR-1181 | matching | Worked check (Example 5.2): ZL = 60 − j80 Ω (60 Ω + 0.995 pF) to 50 Ω at 2 GHz, short-circuited shunt stubs | zL = 1.2 − j1.6; d1 = 0.110λ (y1 = 1 + j1.47), l1 = 0.095λ; d2 = 0.260λ (y2 = 1 − j1.47), l2 = 0.405λ; solution 1 has significantly better bandwidth (1–3 GHz sweep, Fig. 5.5c) | ZL, Z0 | — | calc | p.235–237, Example 5.2 | high |
| POZAR-1182 | matching | Series-stub tuner design equations (YL = GL + jBL, t = tan βd) | t = [BL ± sqrt(GL·((Y0 − GL)^2 + BL^2)/Y0)]/(GL − Y0) (GL ≠ Y0); t = −BL/(2Y0) if GL = Y0; d/λ as for shunt; X = [GL^2·t − (Y0 − t·BL)(BL + t·Y0)]/(Y0·[GL^2 + (BL + Y0·t)^2]); short stub: ls/λ = −atan(X/Z0)/(2π); open stub: lo/λ = atan(Z0/X)/(2π); add λ/2 if negative | GL, BL, Y0 | Lossless lines | calc | p.241, eq. (5.12)–(5.16) | high |
| POZAR-1183 | matching | Worked check (Example 5.3): ZL = 100 + j80 Ω (100 Ω + 6.37 nH) to 50 Ω at 2 GHz, open-circuited series stubs | zL = 2 + j1.6; d1 = 0.120λ (z1 = 1 − j1.33), l1 = 0.397λ; d2 = 0.463λ (z2 = 1 + j1.33), l2 = 0.103λ | ZL, Z0 | — | calc | p.238–240, Example 5.3 | high |
| POZAR-1184 | matching | Double-stub tuner (stubs at fixed positions, e.g. adjustable coax tuners) cannot match every load: loads in the forbidden region cannot reach the rotated 1 + jb circle; shrinking the stub spacing d shrinks the forbidden region but d must remain fabricable, and spacings near 0 or λ/2 are very frequency-sensitive — use λ/8 or 3λ/8 in practice; an adjustable load-to-first-stub line can always move the load out of the forbidden region | Matchable iff 0 ≤ GL ≤ Y0·(1 + t^2)/t^2 = Y0/sin^2(βd), t = tan βd (GL referred to the first stub) | GL, d | Shunt double-stub tuner | calc | p.241–243, eq. (5.21), Fig. 5.8 | high |
| POZAR-1185 | matching | Double-stub tuner design equations (load referred to first stub, spacing d, t = tan βd) | B1 = −BL + [Y0 ± sqrt((1 + t^2)·GL·Y0 − GL^2·t^2)]/t; B2 = [±Y0·sqrt(Y0·GL·(1 + t^2) − GL^2·t^2) + GL·Y0]/(GL·t) (same sign choice); open stub lo/λ = atan(B/Y0)/(2π); short stub ls/λ = −atan(Y0/B)/(2π) (add λ/2 if negative) | GL, BL, Y0, d | Lossless | calc | p.245–246, eq. (5.17)–(5.24) | high |
| POZAR-1186 | matching | Worked check (Example 5.4): ZL = 60 − j80 Ω to 50 Ω, open stubs spaced λ/8, 2 GHz | yL = 0.3 + j0.4; solution 1: b1 = 1.314, y2 = 1 − j3.38, b2 = 3.38, l1 = 0.146λ, l2 = 0.204λ; solution 2: b1' = −0.114, y2' = 1 + j1.38, b2' = −1.38, l1' = 0.482λ, l2' = 0.350λ; solution 1 has much narrower bandwidth (Fig. 5.9c; recomputed sweep: 48 MHz vs 92 MHz at abs(Γ) ≤ 0.2 — note the text attributes this to longer stubs, but as printed solution 1 has the shorter stubs and the larger susceptances) | ZL, Z0, d | — | sim | p.243–245, Example 5.4 | medium |
| POZAR-1187 | matching | Quarter-wave transformer matches only real loads; a complex load can be made real with a length of line or a series/shunt reactance, which usually alters the load's frequency dependence and reduces the match bandwidth; the discontinuity reactance at an impedance step is compensated by a small adjustment of the section length | Z1 = sqrt(Z0·ZL); l = λ0/4 at f0 | Z0, ZL | Single section | calc | p.246–249, eq. (5.25) | high |
| POZAR-1188 | matching | Single-section λ/4 transformer mismatch vs frequency | abs(Γ) = 1/sqrt(1 + [4Z0ZL/(ZL − Z0)^2]·sec^2θ), θ = βl = (π/2)(f/f0) (TEM); near f0: abs(Γ) ≈ abs(ZL − Z0)·abs(cos θ)/(2·sqrt(Z0·ZL)) | Z0, ZL, f/f0 | TEM lines; non-TEM adds dispersion and frequency-dependent wave impedance (usually minor for small bandwidths) | calc | p.247–248, eq. (5.29), (5.30), Fig. 5.11, 5.12 | high |
| POZAR-1189 | matching | Single-section λ/4 transformer fractional bandwidth for a maximum tolerable abs(Γ) = Γm; bandwidth grows as ZL approaches Z0 | Δf/f0 = 2 − (4/π)·acos[(Γm/sqrt(1 − Γm^2))·2·sqrt(Z0·ZL)/abs(ZL − Z0)]; cos θm per eq. (5.32); band edges θm and π − θm | Z0, ZL, Γm | TEM lines | calc | p.248, eq. (5.31)–(5.33) | high |
| POZAR-1190 | matching | Worked check (Example 5.5): 10 Ω load to 50 Ω line at 3 GHz, SWR ≤ 1.5 | Z1 = 22.36 Ω; Γm = 0.2; Δf/f0 = 0.29 (29%) | ZL, Z0, SWR | — | calc | p.249, Example 5.5 | high |
| POZAR-1191 | matching | Theory of small reflections: the total reflection is dominated by the first-order partial reflections; for N commensurate sections with monotonic Zn and real ZL, Γ is a finite Fourier (cosine) series — any smooth passband response can be synthesized with enough sections | Single section: Γ ≈ Γ1 + Γ3·e^{−2jθ}; N sections: Γ(θ) ≈ Γ0 + Γ1e^{−2jθ} + … + ΓN·e^{−2jNθ}, Γn = (Zn+1 − Zn)/(Zn+1 + Zn); symmetric design (Γ0 = ΓN, …) → Γ = 2e^{−jNθ}[Γ0 cos Nθ + Γ1 cos(N − 2)θ + …] | Zn | abs(Γ1Γ3) << 1 (small steps) | calc | p.250–252, eq. (5.42)–(5.46) | high |
| POZAR-1192 | matching | Binomial (maximally flat) multisection transformer: first N − 1 derivatives of abs(Γ) vanish at f0 | Γ(θ) = A(1 + e^{−2jθ})^N; abs(Γ) = 2^N·abs(A)·abs(cos θ)^N; A = 2^−N·(ZL − Z0)/(ZL + Z0) ≈ 2^−(N+1)·ln(ZL/Z0); Γn = A·C(N, n), C(N, n) = N!/((N − n)!·n!) | Z0, ZL, N | Commensurate λ/4 sections | calc | p.252–253, eq. (5.47)–(5.52) | high |
| POZAR-1193 | matching | Binomial transformer impedances (approximate, self-consistent) — exact values in Table 2-21 (Pozar Table 5.1); for ZL/Z0 < 1 use Z0/ZL and number Z1 from the LOAD end (symmetric/reversible) | ln(Zn+1/Zn) ≈ 2^−N·C(N, n)·ln(ZL/Z0), n = 0 … N − 1 (ends at ZN+1 = ZL) | Z0, ZL, N | Small steps | calc | p.253–255, eq. (5.53), Table 5.1 | high |
| POZAR-1194 | matching | Binomial transformer fractional bandwidth | Δf/f0 = 2 − (4/π)·acos[(1/2)·(Γm/abs(A))^(1/N)]; θm = acos[(1/2)(Γm/abs(A))^(1/N)] | A, Γm, N | TEM | calc | p.255, eq. (5.54), (5.55) | high |
| POZAR-1195 | matching | Worked check (Example 5.6): 3-section binomial, 50 Ω load to 100 Ω line, Γm = 0.05 | A = −0.0433; Δf/f0 = 0.70 (70%); Z1 = 91.7 Ω, Z2 = 70.7 Ω, Z3 = 54.5 Ω (approximate = exact to 3 significant digits; Table 5.1 with ZL/Z0 = 2 reversed); more sections → more bandwidth (Fig. 5.15) | ZL, Z0, N, Γm | — | calc | p.255–256, Example 5.6 | high |
| POZAR-1196 | filter | Chebyshev polynomials and properties used for equal-ripple designs (transformers, couplers, filters): abs(Tn) ≤ 1 and oscillates between ±1 for abs(x) ≤ 1 (equal ripple → passband); abs(Tn) > 1 for abs(x) > 1 and grows faster with n | T1 = x; T2 = 2x^2 − 1; T3 = 4x^3 − 3x; T4 = 8x^4 − 8x^2 + 1; Tn = 2x·Tn−1 − Tn−2; Tn(x) = cos(n·acos x) (abs(x) < 1), cosh(n·acosh x) (x > 1); map x = sec θm·cos θ; T1(sec θm cos θ) = sec θm cos θ; T2 = sec^2θm(1 + cos 2θ) − 1; T3 = sec^3θm(cos 3θ + 3cos θ) − 3sec θm cos θ; T4 = sec^4θm(cos 4θ + 4cos 2θ + 3) − 4sec^2θm(cos 2θ + 1) + 1 | x, θm | — | calc | p.257–258, eq. (5.56)–(5.60) | high |
| POZAR-1197 | matching | Chebyshev (equal-ripple) multisection transformer design: trades passband ripple for bandwidth (substantially wider than binomial for the same N) | Γ(θ) = A·e^{−jNθ}·TN(sec θm cos θ), A = Γm; sec θm = cosh[(1/N)·acosh((1/Γm)abs((ZL − Z0)/(ZL + Z0)))] ≈ cosh[(1/N)·acosh(abs(ln(ZL/Z0))/(2Γm))]; Δf/f0 = 2 − 4θm/π; Γn from equating cos(N − 2n)θ terms; ln(Zn+1/Zn) ≈ 2Γn | Z0, ZL, Γm, N | Small-reflection approximation; exact values Table 2-22 (Pozar Table 5.2) | calc | p.258–259, eq. (5.61)–(5.64) | high |
| POZAR-1198 | matching | Worked check (Example 5.7): 3-section Chebyshev, 100 Ω load to 50 Ω line, Γm = 0.05 | sec θm = 1.408, θm = 44.7°; Γ0 = Γ3 = 0.0698, Γ1 = Γ2 = 0.1037; Z1 = 57.5, Z2 = 70.7, Z3 = 87.0 Ω (exact 57.37, 70.71, 87.15 Ω); Δf/f0 = 1.01 (101%) vs 70% for the binomial of Example 5.6 | ZL, Z0, N, Γm | — | calc | p.259–261, Example 5.7, Fig. 5.17 | high |
| POZAR-1199 | matching | Continuously tapered line response from small-reflection theory | Γ(θ) = (1/2)·∫0^L e^{−2jβz}·(d/dz) ln(Z(z)/Z0) dz | Z(z), β | β independent of z (TEM) | calc | p.261–262, eq. (5.65)–(5.67) | high |
| POZAR-1200 | matching | Exponential taper: make it longer than λ/2 (βL > π) to limit low-frequency mismatch; response lobes fall with length; first null at βL = π | Z(z) = Z0·e^{az}, a = (1/L)·ln(ZL/Z0); abs(Γ) = (abs(ln(ZL/Z0))/2)·abs(sin βL/(βL)) | Z0, ZL, L, β | TEM | calc | p.262–263, eq. (5.68)–(5.70), Fig. 5.19 | high |
| POZAR-1201 | matching | Triangular taper (triangular d ln Z/dz): lower lobes than the exponential taper for βL > 2π, but its first null is at βL = 2π (vs π) | Z(z) = Z0·e^{2(z/L)^2 ln(ZL/Z0)} (0 ≤ z ≤ L/2); Z0·e^{(4z/L − 2z^2/L^2 − 1) ln(ZL/Z0)} (L/2 ≤ z ≤ L); abs(Γ) = (1/2)abs(ln(ZL/Z0))·[sin(βL/2)/(βL/2)]^2 | Z0, ZL, L | TEM | calc | p.263–264, eq. (5.71)–(5.73), Fig. 5.20 | high |
| POZAR-1202 | matching | Klopfenstein taper is optimum: minimum in-band reflection for a given length, or shortest length for a given Γm; equal-ripple passband βL ≥ A; the impedance has small steps at both ends | ln Z(z) = (1/2)ln(Z0·ZL) + (Γ0/cosh A)·A^2·φ(2z/L − 1, A); φ(x, A) = ∫0^x I1(A·sqrt(1 − y^2))/(A·sqrt(1 − y^2)) dy, φ(0, A) = 0, φ(x, 0) = x/2, φ(1, A) = (cosh A − 1)/A^2; Γ(θ) = Γ0·e^{−jβL}·cos(sqrt((βL)^2 − A^2))/cosh A (βL > A; cosh(sqrt(A^2 − (βL)^2)) for βL < A); Γ0 = (ZL − Z0)/(ZL + Z0) ≈ (1/2)ln(ZL/Z0); Γm = Γ0/cosh A | Z0, ZL, Γm | Derived from stepped Chebyshev as N → ∞; φ computed numerically (Grossberg method) | calc | p.264–265, eq. (5.74)–(5.78) | high |
| POZAR-1203 | matching | Worked check (Example 5.8): 50 Ω load to 100 Ω line, tapers compared; Klopfenstein with Γm = 0.02 | Γ0 = 0.346; A = acosh(0.346/0.02) = 3.543; passband βL ≥ 3.543 = 1.13π (shorter than exponential or triangular for abs(Γ) ≤ 0.02); exponential a = 0.693/L in magnitude (a = ln(0.5)/L) | ZL, Z0, Γm | Fig. 5.21 (graph) | calc | p.265–267, Example 5.8 | high |
| POZAR-1204 | matching | Bode–Fano limits on broadband matching with a lossless network (Fig. 5.22) | Parallel RC: ∫0^∞ ln(1/abs(Γ(ω))) dω ≤ π/(RC); series RC: ∫0^∞ (1/ω^2)·ln(1/abs(Γ)) dω ≤ π·R·C; parallel RL: ∫0^∞ (1/ω^2)·ln(1/abs(Γ)) dω ≤ π·L/R; series RL: ∫0^∞ ln(1/abs(Γ)) dω ≤ π·R/L | R, L, C, band | Lossless passive matching network | calc | p.267–268, eq. (5.79), Fig. 5.22 | high |
| POZAR-1205 | matching | Bode–Fano consequences: with an ideal square response (abs(Γ) = Γm over Δω, 1 elsewhere) broader bandwidth costs higher in-band reflection; Γm = 0 only if Δω = 0 (perfect match only at discrete frequencies); higher R and/or C (higher-Q loads) are intrinsically harder to match; the area between the return-loss curve and RL = 0 dB is bounded; the square response needs infinitely many elements, a Chebyshev design approximates it | Parallel RC, square response: Δω·ln(1/Γm) ≤ π/(RC) → Γm ≥ exp(−π/(RC·Δω)) | R, C, Δω | Upper performance bound for any matching design | calc | p.268–269, eq. (5.80), Fig. 5.23 | high |
| POZAR-1206 | antenna | Worked bound (computed from Problem 5.24 data): UWB transmitter 3.1–10.6 GHz into a parallel RC load R = 75 Ω, C = 0.6 pF — best achievable return loss with an optimum lossless match | Δω = 2π·7.5 GHz; Γm ≥ exp(−π/(RC·Δω)) = 0.227 → RL ≤ 12.9 dB | R, C, band | Square-response ideal (upper bound) | calc | p.271, Problem 5.24 (computed) | medium |

### Ch. 6 Microwave resonators

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| POZAR-1207 | filter | Series RLC resonator (models many microwave resonators near resonance): resonance when Wm = We; Q = ω·(Wm + We)/Ploss; half-power fractional bandwidth = 1/Q0 | ω0 = 1/sqrt(LC); Q0 = ω0L/R = 1/(ω0RC); Zin ≈ R + j2L·Δω = R + j2RQ0·Δω/ω0; BW = Δf3dB/f0 = 1/Q0 | R, L, C | Near resonance (Δω small) | calc | p.272–275, eq. (6.6)–(6.11), Fig. 6.1 | high |
| POZAR-1208 | filter | Parallel RLC resonator (antiresonance); Q increases with R | ω0 = 1/sqrt(LC); Q0 = R/(ω0L) = ω0RC; Zin ≈ R/(1 + 2jQ0·Δω/ω0); BW = 1/Q0 (abs(Zin)^2 = R^2/2 edges) | R, L, C | Near resonance | calc | p.275–277, eq. (6.12)–(6.21), Fig. 6.2 | high |
| POZAR-1209 | filter | Add loss to a lossless resonator solution by using a complex resonant frequency (perturbation approach) | ω0 → ω0·(1 + j/(2Q0)) | ω0, Q0 | High-Q (small loss) resonators | calc | p.274–275, eq. (6.10), (6.20) | high |
| POZAR-1210 | filter | Loaded Q: unloaded Q0 covers conductor, dielectric and radiation loss of the resonator; the external circuit adds loss (external Q) and lowers the loaded Q | Qe = ω0L/RL (series) or RL/(ω0L) (parallel); 1/QL = 1/Qe + 1/Q0 | Q0, RL | — | calc | p.274, p.277–278, eq. (6.22), (6.23), Table 6.1 | high |
| POZAR-1211 | filter | Short-circuited λ/2 line resonator ≈ series RLC (resonances at l = nλ/2) | R = Z0·α·l; L = Z0·π/(2ω0); C = 1/(ω0^2·L); Q0 = π/(2αl) = β/(2α); Zin(res) = Z0αl | Z0, α, β | Low-loss TEM line (αl << 1) | calc | p.278–280, eq. (6.24)–(6.27), Fig. 6.4 | high |
| POZAR-1212 | filter | Short-circuited λ/4 line resonator ≈ parallel RLC | R = Z0/(αl); C = π/(4ω0·Z0); L = 1/(ω0^2·C); Q0 = π/(4αl) = β/(2α); Zin(res) = Z0/(αl) | Z0, α, β | Low-loss TEM | calc | p.281–282, eq. (6.28)–(6.31) | high |
| POZAR-1213 | filter | Open-circuited λ/2 line resonator (common in microstrip) ≈ parallel RLC at l = nλ/2 | R = Z0/(αl); C = π/(2ω0·Z0); L = 1/(ω0^2·C); Q0 = π/(2αl) = β/(2α) | Z0, α, β | Low-loss TEM; ignores end fringing | calc | p.282–283, eq. (6.32)–(6.35), Fig. 6.5 | high |
| POZAR-1214 | filter | Transmission-line resonator Q is set by the line's attenuation: Q0 = β/(2α) for λ/2 (short or open) and λ/4 (short) resonators; Q falls as attenuation rises — air dielectric or silver plating raises Q | Q0 = β/(2α) (α = αc + αd, Np/m) | α, β | TEM / quasi-TEM | calc | p.280–283 | high |
| POZAR-1215 | filter | Worked check (Example 6.1): λ/2 copper coax resonator, a = 1 mm, b = 4 mm, 5 GHz | Rs = 1.84×10^-2 Ω; air: αc = 0.022 Np/m, Q0 = 104.7/(2·0.022) = 2380; Teflon (εr = 2.08, tanδ = 0.0004): αc = 0.032 Np/m, αd = 0.030 Np/m, Q0 = 1218 (air ≈ 2× Teflon) | a, b, materials, f | — | calc | p.280–281, Example 6.1 | high |
| POZAR-1216 | filter | Worked check (Example 6.2): λ/2 open-circuited 50 Ω microstrip resonator on Teflon (εr = 2.08, tanδ = 0.0004), h = 0.159 cm, copper, 5 GHz | W = 0.508 cm; εe = 1.80; l = 2.24 cm; β = 151.0 rad/m; αc = 0.0724 Np/m; αd = 0.024 Np/m; Q0 = 783 | substrate, f | Fringing ignored | calc | p.283–284, Example 6.2 | high |
| POZAR-1217 | filter | Waveguide resonators are shorted at both ends (closed cavity) because an open-ended guide radiates significantly; power is dissipated in the walls and any dielectric fill; couple by small aperture, probe or loop | Closed cavity; coupling via aperture/probe/loop | — | Cavity resonators | review | p.284 | high |
| POZAR-1218 | filter | Rectangular cavity (a × b × d) resonances: cavity length = integer multiple of λg/2; if b < a < d the dominant mode is TE101 (like a shorted λg/2 section); dominant TM mode is TM110 | f_mnl = (c/(2π·sqrt(µr·εr)))·sqrt((mπ/a)^2 + (nπ/b)^2 + (lπ/d)^2); β_mn·d = lπ | a, b, d, εr | Lossless walls for frequency | calc | p.284–285, eq. (6.38)–(6.40), Fig. 6.6 | high |
| POZAR-1219 | filter | Rectangular cavity TE10l conductor Q | Qc = ((k·a·d)^3·b·η/(2π^2·Rs))·1/(2l^2·a^3·b + 2b·d^3 + l^2·a^3·d + a·d^3) | a, b, d, l, Rs, k, η | Lossless dielectric | calc | p.286–287, eq. (6.46) | high |
| POZAR-1220 | filter | Dielectric-loss Q of ANY fully filled cavity mode depends only on the loss tangent; total unloaded Q combines reciprocally | Qd = 1/tanδ; 1/Q0 = 1/Qc + 1/Qd | tanδ, Qc | Homogeneous fill; perfectly conducting walls for Qd | calc | p.287, eq. (6.48), (6.49); p.292, eq. (6.59) | high |
| POZAR-1221 | filter | Worked check (Example 6.3): copper WR-187 cavity (a = 4.755 cm, b = 2.215 cm) filled with polyethylene (εr = 2.25, tanδ = 0.0004) at 5 GHz — dielectric loss dominates Q (use air fill for higher Q) | k = 157.08 m^-1; d = 2.20 cm (l = 1), 4.40 cm (l = 2); Rs = 1.84×10^-2 Ω; η = 251.3 Ω; Qc = 8,403 (l = 1), 11,898 (l = 2); Qd = 2500; Q0 = 1927 (l = 1), 2065 (l = 2) | geometry, materials | — | calc | p.287–288, Example 6.3 | high |
| POZAR-1222 | filter | Circular cavity (radius a, length d) resonances: dominant TE mode TE111, dominant TM mode TM010; use the mode chart ((2af)^2 vs (2a/d)^2, Fig. 6.9) to see which modes can be excited in a band for a given cavity shape | TE_nml: f = (c/(2π·sqrt(µrεr)))·sqrt((p'nm/a)^2 + (lπ/d)^2); TM_nml: f = (c/(2π·sqrt(µrεr)))·sqrt((pnm/a)^2 + (lπ/d)^2) | a, d, εr | Roots in Table 2-9 | calc | p.289–290, eq. (6.52), (6.53), Fig. 6.9 | high |
| POZAR-1223 | filter | Circular-cavity TE011 has a much higher unloaded Q than TE111, TM010 or TM111; frequency meters use TE011 with loose (small-aperture) coupling and a movable wall for tuning (resolution set by Q); for fixed shape and mode Qc ∝ 1/sqrt(f) | Normalized Q·Rs/(πη) = Q·δs/λ0 vs 2a/d (Fig. 6.10, graph, 0–1.0 scale; TE011/TE012 curves lie well above TE111, TM010, TM111; no numeric values in text) | mode, 2a/d | Air-filled copper cavity (figure) | review | p.288–292, Fig. 6.7, 6.10 | medium |
| POZAR-1224 | filter | Circular cavity TEnml conductor Q | Qc = ((ka)^3·η·a·d/(4(p'nm)^2·Rs))·(1 − (n/p'nm)^2)/{(ad/2)[1 + (βan/(p'nm)^2)^2] + (βa^2/p'nm)^2·(1 − n^2/(p'nm)^2)} | a, d, n, m, l, Rs | Lossless dielectric | calc | p.291, eq. (6.57) | high |
| POZAR-1225 | filter | Worked check (Example 6.4): TE011 copper cavity, d = 2a, Teflon-filled (εr = 2.08, tanδ = 0.0004), 5.0 GHz | k = 151.0 m^-1; a = sqrt(3.832^2 + (π/2)^2)/k = 2.74 cm; d = 5.48 cm; Rs = 0.0184 Ω; Qc = kaη/(2Rs) = 29,390; Qd = 2500; Q0 = 2300; air-filled Q0 = 42,400 | geometry, materials | — | calc | p.292–293, Example 6.4 | high |
| POZAR-1226 | filter | Dielectric resonators (DRs): εr ≈ 10–100 (e.g. barium tetratitanate, titanium dioxide), low loss; no conductor loss but fringing gives some radiation loss; dielectric loss usually rises with εr; Q up to several thousand; smaller, cheaper and lighter than metal cavities, easily coupled to planar lines in MICs; mechanically tunable with an adjustable metal plate above the puck; TE01δ is the mode most used (analogous to TE011) — key components of integrated filters and oscillators | εr 10–100; Q ≈ 1/tanδ when radiation is small | εr, tanδ | Cylindrical DR on/near microstrip | review | p.293–294, p.297 | high |
| POZAR-1227 | filter | DR TE01δ closed-form (magnetic-wall) model is only ≈10% accurate — not accurate enough for design; use EM/refined models. Worked check (Example 6.5): titania εr = 95, tanδ = 0.001, a = 0.413 cm, L = 0.8255 cm | Transcendental: tan(βL/2) = α/β, β = sqrt(εr·k0^2 − (2.405/a)^2), α = sqrt((2.405/a)^2 − k0^2); root bracket f1 = c·2.405/(2π·sqrt(εr)·a) = 2.853 GHz to f2 = c·2.405/(2πa) = 27.804 GHz; result 3.152 GHz vs measured ≈ 3.4 GHz (≈10% low); Qd = 1000 | εr, a, L | Approximate | calc | p.294–297, eq. (6.60)–(6.70), Example 6.5 | high |
| POZAR-1228 | filter | Resonator coupling level depends on the application: loose coupling for frequency meters (keeps high Q and accuracy); tight coupling for oscillators and tuned amplifiers (maximum power transfer); critical coupling = resonator matched to the feed at resonance | Series: critical when R = Z0 (Qe = Q0, QL = Q0/2) | application | — | review | p.298–299, eq. (6.73)–(6.75) | high |
| POZAR-1229 | filter | Coupling coefficient classifies coupling | g = Q0/Qe; series resonator: g = Z0/R; parallel: g = R/Z0; g < 1 undercoupled, g = 1 critically coupled, g > 1 overcoupled (Smith-chart loci Fig. 6.15) | Q0, Qe, R, Z0 | Resonator on a line of Z0 | calc | p.299, eq. (6.76), Fig. 6.15 | high |
| POZAR-1230 | filter | Gap-coupled λ/2 open microstrip resonator: the series gap capacitance inverts the resonator so it looks like a SERIES RLC near resonance; coupling lowers the resonant frequency | Resonance: tan βl + bc = 0, bc = Z0·ω·C; z ≈ π/(2Q0·bc^2) + jπ(ω − ω1)/(ω1·bc^2); R = Z0·π/(2Q0·bc^2); critical: bc = sqrt(π/(2Q0)); g = 2Q0·bc^2/π (bc < sqrt(π/2Q0) under, > over) | Q0, C, Z0 | bc << 1 | calc | p.299–301, eq. (6.77)–(6.83) | high |
| POZAR-1231 | filter | Worked check (Example 6.6): 50 Ω open microstrip resonator, l = 2.175 cm, εe = 1.9, α = 0.01 dB/cm, gap-coupled to a 50 Ω line | f0 (uncoupled) = 5.00 GHz; Q0 = π/(2αl) = 628; bc = 0.05; C = 0.032 pF for critical coupling; loaded resonance 4.918 GHz (1.6% low); Fig. 6.18: C = 0.06 pF over-, 0.033 pF critically, 0.02 pF under-coupled | l, εe, α | — | calc | p.302–303, Example 6.6 | high |
| POZAR-1232 | filter | Aperture-coupled waveguide cavity: a small transverse-wall aperture acts as a shunt inductance; first resonance near βl = π (slightly shifted); the next mode (exactly λg/2, field null at the aperture) is negligibly coupled | Antiresonance: tan βl + xL = 0, xL = ωL/Z0; critical coupling: XL = Z0·sqrt(π·k0·ω1/(2Q0·β^2·c)); then size aperture from XL (POZAR-1163) | Q0, k0, β, ω1 | xL << 1 | calc | p.302–304, eq. (6.84)–(6.89), Fig. 6.19–6.20 | high |
| POZAR-1233 | test | Unloaded Q from a two-port transmission measurement (series resonator in series with a Z0 line, or EM-simulated S21): loaded Q from the −3 dB bandwidth of abs(S21) relative to its resonance value; coupling from the resonance transmission; Q0 = (1 + g)·QL. For a resonator that appears as a parallel RLC, invert g | QL = f0/BW3dB; g = S21(ω0)/(1 − S21(ω0)) (series; g = 2Z0/R, S21(ω0) = g/(1 + g)); parallel: g → 1/g; Q0 = (1 + g)·QL | f0, BW3dB, S21(ω0) (real, planes at resonator) | Direct Q0 measurement is not possible because of loading | measure | p.305–306, eq. (6.90)–(6.94), Fig. 6.21–6.22 | high |
| POZAR-1234 | test | Cavity material perturbation: any increase of ε or µ anywhere in the cavity lowers the resonant frequency; basis of dielectric-constant measurement by frequency shift. Thin slab (thickness t, εr) on the bottom wall of a TE101 cavity of height b | Δω/ω0 ≈ −∫(Δεabs(E0)^2 + Δµabs(H0)^2)dv / ∫(εabs(E0)^2 + µabs(H0)^2)dv; slab: Δω/ω0 = −(εr − 1)·t/(2b) | Δε, Δµ, t, b | Small perturbations (fields ≈ unperturbed) | calc | p.306–309, eq. (6.100), Example 6.7 | high |
| POZAR-1235 | filter | Cavity shape perturbation (tuning screws, movable walls): frequency may rise or fall depending on whether the change removes volume where magnetic or electric energy dominates; a thin screw (radius r0, depth l) at the centre of the broad wall of a TE101 cavity (E maximum) lowers the frequency | Δω/ω0 ≈ (ΔWm − ΔWe)/(Wm + We) = ∫ΔV(µabs(H0)^2 − εabs(E0)^2)dv / ∫V0(µabs(H0)^2 + εabs(E0)^2)dv; centred screw: Δω/ω0 = −2πr0^2·l/(abd) = −2ΔV/V0 | r0, l, a, b, d | Small perturbations | calc | p.309–312, eq. (6.107), (6.108), Example 6.8 | high |
| POZAR-1236 | antenna | Circular microstrip disk resonator (radius a), magnetic-wall approximation, fringing neglected — dominant mode (result stated in Problem 6.17) | f110 = 1.841·c/(2π·a·sqrt(εr)) | a, εr | Fringing ignored (effective radius larger in practice) | calc | p.314, Problem 6.17 | medium |

### Ch. 7 Power dividers and couplers (§7.1–7.3 opening)

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| POZAR-1237 | components | Three-port theorem: no three-port can be simultaneously lossless, reciprocal and matched at all ports; relaxing any one condition makes a realizable device | Lossless + reciprocal + S11 = S22 = S33 = 0 ⇒ contradiction (unitarity of eq. 7.2) | requirements | Passive networks without anisotropic media are reciprocal | review | p.318, eq. (7.1)–(7.3) | high |
| POZAR-1238 | components | A matched, lossless three-port must be nonreciprocal — a circulator (usually ferrite-based): power flows 1→2→3→1 (or the reverse) | [S] = [[0,0,1],[1,0,0],[0,1,0]] (clockwise, S21 = S32 = S13 = 1) or [[0,1,0],[0,0,1],[1,0,0]] (counter-clockwise); phase references arbitrary | — | Ideal circulator | review | p.318–319, eq. (7.4)–(7.6), Fig. 7.2 | high |
| POZAR-1239 | components | Relaxed three-port options: lossless + reciprocal can be matched at only two ports, and then degenerates into a matched two-port plus a totally mismatched one-port; a LOSSY three-port can be reciprocal and matched at all ports (resistive divider) and can also isolate its output ports (Wilkinson) | Lossless reciprocal, S11 = S22 = 0 ⇒ S13 = S23 = 0, abs(S12) = abs(S33) = 1 | requirements | — | review | p.319–320, eq. (7.7), (7.8), Fig. 7.3 | high |
| POZAR-1240 | components | Any reciprocal, lossless, matched four-port is a directional coupler: S14 = S23 = 0, abs(S13) = abs(S24), abs(S12) = abs(S34), and α^2 + β^2 = 1 (one degree of freedom apart from phase); symmetric coupler: S13 = S24 = jβ; antisymmetric coupler: S13 = β, S24 = −β | [S] = [[0, α, jβ, 0], [α, 0, 0, jβ], [jβ, 0, 0, α], [0, jβ, α, 0]] (symmetric) or [[0, α, β, 0], [α, 0, 0, −β], [β, 0, 0, α], [0, −β, α, 0]] (antisymmetric); θ + φ = π | α, β | Port 1 input, 2 through, 3 coupled, 4 isolated (Fig. 7.4) | calc | p.320–322, eq. (7.9)–(7.19) | high |
| POZAR-1241 | components | Directional-coupler figures of merit (dB) and their relation | Coupling C = 10 log(P1/P3) = −20 log β; Directivity D = 10 log(P3/P4) = 20 log(β/abs(S14)); Isolation I = 10 log(P1/P4) = −20 logabs(S14); Insertion loss L = 10 log(P1/P2) = −20 logabs(S12); I = D + C (dB); ideal coupler D = I = ∞ | S12, S13, S14 | Port convention of Fig. 7.4 | calc | p.322–323, eq. (7.20), (7.21) | high |
| POZAR-1242 | components | Hybrid couplers are 3 dB couplers (α = β = 1/sqrt 2): quadrature hybrid (90° between ports 2 and 3 when fed at 1) and magic-T / rat-race (180° between ports 2 and 3 when fed at 4) | Quadrature: [S] = (1/sqrt 2)·[[0, 1, j, 0], [1, 0, 0, j], [j, 0, 0, 1], [0, j, 1, 0]]; 180°: [S] = (1/sqrt 2)·[[0, 1, 1, 0], [1, 0, 0, −1], [1, 0, 0, 1], [0, −1, 1, 0]] | — | Ideal hybrids | calc | p.323, eq. (7.22), (7.23) | high |
| POZAR-1243 | test | Coupler directivity requirement and masking: applications often require directivity of 35 dB or more; poor directivity limits reflectometer accuracy and makes the coupled level vary with even small through-line mismatch; directivity cannot be measured directly when the load's reflected-and-coupled signal (RL + C below input) exceeds the directivity leakage (D + C below input) | D ≥ 35 dB (typical application requirement); example C = 20 dB, D = 35 dB, RL = 30 dB → leakage at −55 dB masked by reflection at −50 dB | C, D, RL | Reflectometers, power monitors | measure | p.323, Point of Interest "Measuring Coupler Directivity" | high |
| POZAR-1244 | test | Sliding-load directivity measurement: measure coupled power Pc with a matched load; reverse the coupler, terminate the through line with a sliding load and record Pmax, Pmin over slide positions | Numerical C = 10^(−C_dB/20), D = 10^(D_dB/20) ≥ 1; M = Pc/Pmax = (D/(1 + abs(Γ)D))^2; m = Pmax/Pmin = ((1 + abs(Γ)D)/(1 − abs(Γ)D))^2; D = sqrt(M)·2·sqrt(m)/(sqrt(m) + 1) (radicals restored — OCR drops sqrt signs; consistent with M, m definitions); valid only if abs(Γ) < 1/D (load RL > D in dB) | Pc, Pmax, Pmin | Sliding matched load | measure | p.323–324 | medium |
| POZAR-1245 | components | Lossless T-junction divider (E/H-plane waveguide T, microstrip/stripline T): matched input requires the output line admittances to sum to the input admittance; junction susceptance B (fringing, higher-order modes) is cancelled by discontinuity compensation or a reactive tuner (narrowband); outputs are not isolated and are mismatched looking back in | Yin = jB + 1/Z1 + 1/Z2 = 1/Z0; B = 0: 1/Z1 + 1/Z2 = 1/Z0; power split P1/P2 = Z2/Z1; 3 dB from 50 Ω: two 100 Ω lines (λ/4 transformers can restore 50 Ω) | Z0, split ratio | Lossless lines | calc | p.324–326, eq. (7.24), (7.25), Fig. 7.5–7.6 | high |
| POZAR-1246 | components | Worked check (Example 7.1): lossless T, 50 Ω source, 2:1 output power ratio | Z1 = 3Z0 = 150 Ω (1/3 Pin), Z2 = 3Z0/2 = 75 Ω (2/3 Pin); Zin = 75 ∥ 150 = 50 Ω (matched); looking back: 150 Ω port sees 50 ∥ 75 = 30 Ω (Γ = −0.666), 75 Ω port sees 50 ∥ 150 = 37.5 Ω (Γ = −0.333) | Z0, ratio | — | calc | p.326, Example 7.1 | high |
| POZAR-1247 | components | Resistive (star) power divider: three Z0/3 resistors; matched at all ports, reciprocal, but lossy (half the input power is dissipated) and with no isolation between outputs; each output is 6 dB below the input | Zin = Z0/3 + (4Z0/3)/2 = Z0; S = (1/2)·[[0, 1, 1], [1, 0, 1], [1, 1, 0]] (not unitary); P2 = P3 = Pin/4 | Z0 | Equal split; unequal ratios possible | calc | p.326–328, eq. (7.26)–(7.32), Fig. 7.7 | high |
| POZAR-1248 | components | Wilkinson divider: a lossy three-port matched at all ports WITH isolation between the outputs, and lossless when the outputs are matched (only power reflected from the outputs is dissipated); arbitrary split possible; equal-split (3 dB) element values: two λ/4 lines of sqrt(2)·Z0 and a 2Z0 resistor between the output ports; usually microstrip/stripline | Equal split: Z_λ/4 = sqrt(2)·Z0 (70.7 Ω for 50 Ω), R = 2Z0 (100 Ω for 50 Ω); analysis by even–odd modes | Z0 | Detailed S-matrix/bandwidth in §7.3 (part 2 of this book extraction) | calc | p.328, Fig. 7.8 | high |

## 2. Formulas & tables (numbers)

### Table 2-1. Band designations and typical allocations (Pozar Fig. 1.1, p.2)

Approximate band designations:

| Band | Frequency range |
|---|---|
| Medium frequency (MF) | 300 kHz–3 MHz |
| High frequency (HF) | 3–30 MHz |
| Very high frequency (VHF) | 30–300 MHz |
| Ultra high frequency (UHF) | 300 MHz–3 GHz |
| L band | 1–2 GHz |
| S band | 2–4 GHz |
| C band | 4–8 GHz |
| X band | 8–12 GHz |
| Ku band | 12–18 GHz |
| K band | 18–26 GHz |
| Ka band | 26–40 GHz |
| U band | 40–60 GHz |
| V band | 50–75 GHz |
| E band | 60–90 GHz |
| W band | 75–110 GHz |
| F band | 90–140 GHz |

Typical frequencies (same figure):

| Service | Frequency |
|---|---|
| AM broadcast band | 535–1605 kHz |
| Short wave radio band | 3–30 MHz |
| FM broadcast band | 88–108 MHz |
| VHF TV (2–4) | 54–72 MHz |
| VHF TV (5–6) | 76–88 MHz |
| UHF TV (7–13) | 174–216 MHz |
| UHF TV (14–83) | 470–890 MHz |
| US cellular telephone | 824–849 MHz, 869–894 MHz |
| European GSM cellular | 880–915 MHz, 925–960 MHz |
| GPS | 1575.42 MHz, 1227.60 MHz |
| Microwave ovens | 2.45 GHz |
| US DBS | 11.7–12.5 GHz |
| US ISM bands | 902–928 MHz, 2.400–2.484 GHz, 5.725–5.850 GHz |
| US UWB radio | 3.1–10.6 GHz |

### Table 2-2. Skin depth of common metals at 10 GHz (Pozar Example 1.2, p.19; conductivities from App. F)

| Metal | σ (S/m) | δs at 10 GHz (m) | δs (µm) |
|---|---|---|---|
| Aluminum | 3.816×10^7 | 8.14×10^-7 | 0.814 |
| Copper | 5.813×10^7 | 6.60×10^-7 | 0.660 |
| Gold | 4.098×10^7 | 7.86×10^-7 | 0.786 |
| Silver | 6.173×10^7 | 6.40×10^-7 | 0.640 |

Formula: δs = 1/sqrt(π f µ0 σ) = 5.03×10^-3/sqrt(σ) m at f = 10 GHz. Scale to other f by sqrt(10 GHz / f). Copper at 1 GHz: δs = 2.088 µm (Example 1.4, p.35). Rs = 1/(σ δs).

### Table 2-2b. Skin depth and surface resistance vs frequency (computed from δs = 1/sqrt(πfµ0σ), Rs = sqrt(πfµ0/σ) with the Example 1.2 conductivities — conf medium, derived; spot-checked against Pozar's quoted values: Cu δs(1 GHz) = 2.088 µm, Cu Rs(5 GHz) = 1.84×10^-2 Ω, Cu Rs(10 GHz) = 0.026 Ω, Au Rs(14 GHz) = 0.0367 Ω)

| Metal | σ (S/m) | δs 1 GHz (µm) | δs 2.4 GHz | δs 5 GHz | δs 10 GHz | δs 28 GHz | Rs 1 GHz (mΩ) | Rs 2.4 GHz | Rs 5 GHz | Rs 10 GHz | Rs 28 GHz |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Aluminum | 3.816×10^7 | 2.576 | 1.663 | 1.152 | 0.815 | 0.487 | 10.17 | 15.76 | 22.74 | 32.16 | 53.82 |
| Copper | 5.813×10^7 | 2.087 | 1.347 | 0.934 | 0.660 | 0.394 | 8.24 | 12.77 | 18.43 | 26.06 | 43.61 |
| Gold | 4.098×10^7 | 2.486 | 1.605 | 1.112 | 0.786 | 0.470 | 9.82 | 15.21 | 21.95 | 31.04 | 51.94 |
| Silver | 6.173×10^7 | 2.026 | 1.308 | 0.906 | 0.641 | 0.383 | 8.00 | 12.39 | 17.88 | 25.29 | 42.32 |

(Pozar's full conductivity table is Appendix F and dielectric table Appendix G — outside this part's line range; see the part-2 rulebook.)

### Table 2-3. Plane-wave propagation summary (Pozar Table 1.1, p.20)

| Quantity | Lossless (ε'' = σ = 0) | General lossy | Good conductor (ε'' >> ε' or σ >> ωε') |
|---|---|---|---|
| Complex propagation constant | γ = jω sqrt(µε) | γ = jω sqrt(µε) = jω sqrt(µε')·sqrt(1 − jσ/(ωε')) | γ = (1 + j) sqrt(ωµσ/2) |
| Phase constant (wave number) | β = k = ω sqrt(µε) | β = Im{γ} | β = Im{γ} = sqrt(ωµσ/2) |
| Attenuation constant | α = 0 | α = Re{γ} | α = Re{γ} = sqrt(ωµσ/2) |
| Impedance | η = sqrt(µ/ε) = ωµ/k | η = jωµ/γ | η = (1 + j) sqrt(ωµ/(2σ)) |
| Skin depth | δs = ∞ | δs = 1/α | δs = sqrt(2/(ωµσ)) |
| Wavelength | λ = 2π/β | λ = 2π/β | λ = 2π/β |
| Phase velocity | vp = ω/β | vp = ω/β | vp = ω/β |

### Table 2-4. Physical constants as used in the text (p.7, p.16–17, p.22)

| Constant | Value | Units |
|---|---|---|
| µ0 (permeability of free space) | 4π×10^-7 | H/m |
| ε0 (permittivity of free space) | 8.854×10^-12 | F/m |
| c (speed of light) | 2.998×10^8 | m/s |
| η0 = sqrt(µ0/ε0) (intrinsic impedance of free space) | 377 | Ω |

### Table 2-5. Transmission line parameters for common lines (Pozar Table 2.1, p.54)

| Parameter | Coax (radii a < b) | Two-wire (radius a, spacing D) | Parallel plate (width w, gap d) |
|---|---|---|---|
| L (H/m) | (µ/2π)·ln(b/a) | (µ/π)·acosh(D/2a) | µd/w |
| C (F/m) | 2πε'/ln(b/a) | πε'/acosh(D/2a) | ε'w/d |
| R (Ω/m) | (Rs/2π)·(1/a + 1/b) | Rs/(πa) | 2Rs/w |
| G (S/m) | 2πωε''/ln(b/a) | πωε''/acosh(D/2a) | ωε''w/d |
| Z0 (Ω) | (η/2π)·ln(b/a) (eq. 2.32) | sqrt(L/C) = (η/π)·acosh(D/2a) (derived) | ηd/w (eq. 3.39) |

Rs = 1/(σδs) = sqrt(ωµ0/(2σ)); ε = ε' − jε'' = ε'(1 − j tanδ). Parallel-plate formulas assume w >> d.

### Table 2-6. Reflection coefficient ↔ SWR ↔ return loss ↔ mismatch loss (computed from Pozar eq. 2.38, 2.41; Problem 2.15 lists these rows blank)

Formulas: abs(Γ) = (SWR − 1)/(SWR + 1); SWR = (1 + abs(Γ))/(1 − abs(Γ)); RL = −20·log10abs(Γ) dB; mismatch loss ML = −10·log10(1 − abs(Γ)^2) dB (from eq. 2.37: PL/Pinc = 1 − abs(Γ)^2); reflected power % = 100·abs(Γ)^2. Rows marked * are the Problem 2.15 rows; values are computed (conf medium: derived from stated relations).

| SWR | abs(Γ) | RL (dB) | Mismatch loss (dB) | Reflected power (%) |
|---|---|---|---|---|
| 1.000 * | 0.0000 | ∞ | 0.0000 | 0.000 |
| 1.010 * | 0.0050 | 46.06 | 0.0001 | 0.002 |
| 1.020 * | 0.0100 | 40.00 | 0.0004 | 0.010 |
| 1.050 * | 0.0244 | 32.26 | 0.0026 | 0.059 |
| 1.065 * | 0.0316 | 30.00 | 0.0043 | 0.100 |
| 1.100 * | 0.0476 | 26.44 | 0.0099 | 0.227 |
| 1.119 | 0.0562 | 25.00 | 0.0138 | 0.316 |
| 1.200 * | 0.0909 | 20.83 | 0.0360 | 0.826 |
| 1.222 * | 0.1000 | 20.00 | 0.0436 | 1.000 |
| 1.250 | 0.1111 | 19.08 | 0.0540 | 1.235 |
| 1.300 | 0.1304 | 17.69 | 0.0745 | 1.701 |
| 1.433 | 0.1778 | 15.00 | 0.1396 | 3.162 |
| 1.500 * | 0.2000 | 13.98 | 0.1773 | 4.000 |
| 1.925 * | 0.3162 | 10.00 | 0.4576 | 10.000 |
| 2.000 * | 0.3333 | 9.54 | 0.5115 | 11.111 |
| 2.500 * | 0.4286 | 7.36 | 0.8814 | 18.367 |
| 3.000 | 0.5000 | 6.02 | 1.2494 | 25.000 |
| 5.000 | 0.6667 | 3.52 | 2.5527 | 44.444 |
| 10.000 | 0.8182 | 1.74 | 4.8073 | 66.942 |
| ∞ | 1.0000 | 0.00 | ∞ | 100.000 |

### Table 2-7. Special terminations and lengths (Pozar §2.3, p.59–62)

| Case | Γ at load | SWR | Zin |
|---|---|---|---|
| Matched ZL = Z0 | 0 | 1 | Z0 (line "flat") |
| Short ZL = 0 | −1 | ∞ | jZ0·tan βl (l = λ/4 → open) |
| Open ZL = ∞ | +1 | ∞ | −jZ0·cot βl (l = λ/4 → short) |
| Pure reactance ZL = jX | abs = 1 | ∞ | reactive |
| l = nλ/2, any ZL | Γ | — | ZL (no transformation) |
| l = λ/4 + nλ/2 | Γ | — | Z0^2/ZL (impedance inverter) |

### Table 2-8. Parallel-plate waveguide summary (Pozar Table 3.1, p.109) — design quantities only

| Quantity | TEM | TMn | TEn |
|---|---|---|---|
| kc | 0 | nπ/d | nπ/d |
| β | k = ω sqrt(µε) | sqrt(k^2 − kc^2) | sqrt(k^2 − kc^2) |
| λc | ∞ | 2d/n | 2d/n |
| αd | k·tanδ/2 | k^2·tanδ/(2β) | k^2·tanδ/(2β) |
| αc | Rs/(ηd) | 2kRs/(βηd) | 2kc^2·Rs/(kβηd) |
| Z (wave) | Z_TEM = ηd/W (as Z0) | Z_TM = βη/k | Z_TE = kη/β |

### Table 2-9. Bessel-root values for circular waveguide cutoff (Pozar Tables 3.3–3.4, p.123, 126); fc = p·c/(2πa·sqrt(εr))

| n | TE: p'n1 | p'n2 | p'n3 | TM: pn1 | pn2 | pn3 |
|---|---|---|---|---|---|---|
| 0 | 3.832 | 7.016 | 10.174 | 2.405 | 5.520 | 8.654 |
| 1 | 1.841 | 5.331 | 8.536 | 3.832 | 7.016 | 10.174 |
| 2 | 3.054 | 6.706 | 9.970 | 5.135 | 8.417 | 11.620 |

Mode order relative to fc(TE11) (derived from the table; Fig. 3.13): TE11 1.000, TM01 1.306, TE21 1.659, TE01/TM11 2.081, TM21 2.789, TE12 2.896 (TE31, TE41, TM02 appear in Fig. 3.13 but their roots are not tabulated).

### Table 2-10. Example mode cutoffs — Teflon-filled K-band rectangular guide a = 1.07 cm, b = 0.43 cm (Pozar Example 3.1, p.117)

| Mode | m | n | fc (GHz) |
|---|---|---|---|
| TE | 1 | 0 | 9.72 |
| TE | 2 | 0 | 19.44 |
| TE | 0 | 1 | 24.19 |
| TE, TM | 1 | 1 | 26.07 |
| TE, TM | 2 | 1 | 31.03 |

### Table 2-11. Coaxial connectors (Pozar Point of Interest, p.134–135)

| Connector | Size note | Upper frequency (Pozar) | Notes |
|---|---|---|---|
| Type-N | female OD ≈ 0.625 in | 11–18 GHz (depends on cable size) | 1942, P. Neil (Bell Labs); rugged, large, older equipment |
| TNC | threaded BNC | < 1 GHz | — |
| SMA | female OD ≈ 0.25 in | 18–25 GHz | 1960s; "probably the most commonly used microwave connector" |
| APC-7 | precision, sexless, butt contact | 18 GHz with SWR < 1.04 (repeatable) | Measurement/instrumentation |
| 2.4 mm | SMA-sized | ≈ 50 GHz | mm-wave SMA variant |

Impedance standards: 50 Ω (compromise: air coax minimum loss ≈ 77 Ω, maximum power ≈ 30 Ω); 75 Ω television.

### Table 2-12. Stripline Z0 comparison, εr = 2.55, a = 100b (Pozar Example 3.6, p.146)

| W/b | Z0 numerical eq. (3.192) (Ω) | Z0 formula eq. (3.179) (Ω) | Z0 commercial CAD (Ω) |
|---|---|---|---|
| 0.25 | 90.9 | 86.6 | 85.3 |
| 0.50 | 66.4 | 62.7 | 61.7 |
| 1.0 | 43.6 | 41.0 | 40.2 |
| 2.0 | 25.5 | 24.2 | 24.4 |
| 5.0 | 11.1 | 10.8 | 11.9 |

### Table 2-13. Comparison of common transmission lines and waveguides (Pozar Table 3.6, p.158)

| Characteristic | Coax | Waveguide | Stripline | Microstrip |
|---|---|---|---|---|
| Preferred mode | TEM | TE10 | TEM | Quasi-TEM |
| Other modes | TM, TE | TM, TE | TM, TE | Hybrid TM, TE |
| Dispersion | None | Medium | None | Low |
| Bandwidth | High | Low | High | High |
| Loss | Medium | Low | High | High |
| Power capacity | Medium | High | Low | Low |
| Physical size | Large | Large | Medium | Small |
| Ease of fabrication | Medium | Medium | Easy | Easy |
| Integration with other components | Hard | Hard | Fair | Easy |

### Table 2-14. Microstrip higher-order-mode / surface-wave threshold frequencies (Pozar §3.8, p.151–152; c = 3×10^8 m/s)

| Threshold | Mechanism | Formula | Notes |
|---|---|---|---|
| fT1 | Coupling to TM0 surface wave | (c/(2πd))·sqrt(2/(εr − 1))·atan(εr) | 35%–66% of TM1 cutoff for εr 1–10 |
| fT2 | TE1 surface wave excited at transverse discontinuities | c/(4d·sqrt(εr − 1)) | Bends, junctions, width steps |
| fT3 | Transverse resonance of wide strip (W + d/2 ≈ λ/2) | c/(sqrt(εr)(2W + d)) | Rare in practice |
| fT4 | Parallel-plate mode (strip–ground ≈ λ/2) | c/(2d·sqrt(εr)) | Narrow strips: up to 50% lower |

Surface-wave cutoffs of the grounded slab (eq. 3.167, 3.174): TMn fc = n·c/(2d·sqrt(εr − 1)); TEn fc = (2n − 1)·c/(4d·sqrt(εr − 1)). Illustration (computed, not from the book): εr = 4.4, d = 1.6 mm, W = 3 mm → fT1 = 30.8 GHz, fT2 = 25.4 GHz, fT3 = 18.8 GHz, fT4 = 44.7 GHz.

### Table 2-15. Transmission-line power capacity (Pozar Point of Interest, p.160–161)

| Item | Value |
|---|---|
| Air breakdown field Ed (room temp, sea level) | ≈ 3×10^6 V/m |
| Coax Pmax (given a, b) | (π a^2 Ed^2/η0)·ln(b/a) |
| Coax Pmax ceiling for mode-free f_max | 5.8×10^12·(Ed/f_max)^2 W → ≈ 520 kW at 10 GHz |
| Rect. waveguide TE10 Pmax | a·b·Ed^2/(4Zw) |
| Rect. waveguide ceiling | 2.6×10^13·(Ed/f_max)^2 W → ≈ 2300 kW at 10 GHz |
| Safety factor | ≥ 2 (use ≈ half the above) |
| Worst-case mismatch abs(Γ) = 1 | capacity ÷ 4 |

### Table 2-16. Material and conductor values used in Ch. 3 examples (quoted from App. F/G by the text)

| Material | Property | Value | Source |
|---|---|---|---|
| Teflon (PTFE) | εr, tanδ | 2.08, 0.0004 | Example 3.1 (p.117), Example 3.2 |
| Teflon (RG-401U fill) | εr | 2.2 | Example 3.3 (p.132) |
| Alumina | εr, tanδ | 9.9, 0.001 | Example 3.7 (p.149) |
| Copper | σ | 5.8×10^7 S/m (App. F: 5.813×10^7) | Example 3.1 |
| Copper | Rs at 15 GHz / 10 GHz | 0.032 Ω / 0.026 Ω | Examples 3.1, 3.5, 3.7 |
| Gold | σ; Rs at 14 GHz | 4.1×10^7 S/m; 0.0367 Ω | Example 3.2 (p.128) |

### Table 2-17. Two-port parameter conversions (Pozar Table 4.2, p.192) — all formulas verified numerically by round-trip (Z0 real, equal at both ports; Y0 = 1/Z0)

Determinants: det(Z) = Z11Z22 − Z12Z21; det(Y) = Y11Y22 − Y12Y21; ΔZ = (Z11 + Z0)(Z22 + Z0) − Z12Z21; ΔY = (Y11 + Y0)(Y22 + Y0) − Y12Y21; Δ_S = (1 − S11)(1 − S22) − S12S21; Σ_S = (1 + S11)(1 + S22) − S12S21; D_A = A + B/Z0 + C·Z0 + D.

| To \ From | S | Z | Y | ABCD |
|---|---|---|---|---|
| S11 | S11 | ((Z11 − Z0)(Z22 + Z0) − Z12Z21)/ΔZ | ((Y0 − Y11)(Y0 + Y22) + Y12Y21)/ΔY | (A + B/Z0 − C·Z0 − D)/D_A |
| S12 | S12 | 2·Z12·Z0/ΔZ | −2·Y12·Y0/ΔY | 2(AD − BC)/D_A |
| S21 | S21 | 2·Z21·Z0/ΔZ | −2·Y21·Y0/ΔY | 2/D_A |
| S22 | S22 | ((Z11 + Z0)(Z22 − Z0) − Z12Z21)/ΔZ | ((Y0 + Y11)(Y0 − Y22) + Y12Y21)/ΔY | (−A + B/Z0 − C·Z0 + D)/D_A |
| Z11 | Z0·((1 + S11)(1 − S22) + S12S21)/Δ_S | Z11 | Y22/det(Y) | A/C |
| Z12 | Z0·2S12/Δ_S | Z12 | −Y12/det(Y) | (AD − BC)/C |
| Z21 | Z0·2S21/Δ_S | Z21 | −Y21/det(Y) | 1/C |
| Z22 | Z0·((1 − S11)(1 + S22) + S12S21)/Δ_S | Z22 | Y11/det(Y) | D/C |
| Y11 | Y0·((1 − S11)(1 + S22) + S12S21)/Σ_S | Z22/det(Z) | Y11 | D/B |
| Y12 | Y0·(−2S12)/Σ_S | −Z12/det(Z) | Y12 | (BC − AD)/B |
| Y21 | Y0·(−2S21)/Σ_S | −Z21/det(Z) | Y21 | −1/B |
| Y22 | Y0·((1 + S11)(1 − S22) + S12S21)/Σ_S | Z11/det(Z) | Y22 | A/B |
| A | ((1 + S11)(1 − S22) + S12S21)/(2S21) | Z11/Z21 | −Y22/Y21 | A |
| B | Z0·((1 + S11)(1 + S22) − S12S21)/(2S21) | det(Z)/Z21 | −1/Y21 | B |
| C | (1/Z0)·((1 − S11)(1 − S22) − S12S21)/(2S21) | 1/Z21 | −det(Y)/Y21 | C |
| D | ((1 − S11)(1 + S22) + S12S21)/(2S21) | Z22/Z21 | −Y11/Y21 | D |

N-port matrix forms (normalized to Z0 = 1): [S] = ([Z] − [U])([Z] + [U])^-1; [Z] = ([U] + [S])([U] − [S])^-1; [Y] = [Z]^-1.

### Table 2-18. ABCD parameters of useful two-ports (Pozar Table 4.1, p.190)

| Circuit | A | B | C | D |
|---|---|---|---|---|
| Series impedance Z | 1 | Z | 0 | 1 |
| Shunt admittance Y | 1 | 0 | Y | 1 |
| Transmission line (Z0, Y0 = 1/Z0, length l) | cos βl | jZ0·sin βl | jY0·sin βl | cos βl |
| Ideal transformer N:1 | N | 0 | 0 | 1/N |
| π network: shunt Y1 (port 1), series Y3, shunt Y2 (port 2) | 1 + Y2/Y3 | 1/Y3 | Y1 + Y2 + Y1Y2/Y3 | 1 + Y1/Y3 |
| T network: series Z1 (port 1), shunt Z3, series Z2 (port 2) | 1 + Z1/Z3 | Z1 + Z2 + Z1Z2/Z3 | 1/Z3 | 1 + Z2/Z3 |

Conventions: [V1; I1] = [A B; C D][V2; I2] with I2 flowing out of port 2; cascade = product in physical order; reciprocal ⇒ AD − BC = 1.

### Table 2-19. Small-aperture polarizabilities (Pozar Table 4.3, p.217)

| Aperture | αe | αm |
|---|---|---|
| Round hole, radius r0 | 2r0^3/3 | 4r0^3/3 |
| Rectangular slot, length l, width d (H across slot) | π·l·d^2/16 | π·l·d^2/16 |

(Slot-length symbol l restored — the extraction drops script-l throughout; conf medium for the slot row.)

### Table 2-20. Worked network examples (Pozar Ch. 4)

| Example | Inputs | Results |
|---|---|---|
| 4.2 (p.171) | X-band a = 2.286 cm, b = 1.016 cm, air → Rexolite εr = 2.54, 10 GHz | βa = 158.0, βd = 304.1 m^-1; Z0a = 500.0 Ω, Z0d = 259.6 Ω; Γ = −0.316 |
| 4.4 (p.179) | T pad 8.56 / 141.8 / 8.56 Ω, Z0 = 50 Ω | S11 = S22 = 0, S21 = S12 = 0.707 (3 dB) |
| 4.5 (p.183) | S11 = 0.15∠0°, S12 = 0.85∠−45°, S21 = 0.85∠45°, S22 = 0.2∠0° | not reciprocal, not lossless (0.745); RL = 16.5 dB (matched), 6.9 dB (port 2 shorted, Γ = −0.452) |
| 4.8 (p.214) | centred full-height probe, TE10 only | Rin = b·Z1/a |

### Table 2-21. Binomial transformer design — exact normalized impedances (Pozar Table 5.1, p.254). For ZL/Z0 < 1 use Z0/ZL and start Z1 at the load end.

| ZL/Z0 | N=2: Z1 | Z2 | N=3: Z1 | Z2 | Z3 | N=4: Z1 | Z2 | Z3 | Z4 |
|---|---|---|---|---|---|---|---|---|---|
| 1.0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| 1.5 | 1.1067 | 1.3554 | 1.0520 | 1.2247 | 1.4259 | 1.0257 | 1.1351 | 1.3215 | 1.4624 |
| 2.0 | 1.1892 | 1.6818 | 1.0907 | 1.4142 | 1.8337 | 1.0444 | 1.2421 | 1.6102 | 1.9150 |
| 3.0 | 1.3161 | 2.2795 | 1.1479 | 1.7321 | 2.6135 | 1.0718 | 1.4105 | 2.1269 | 2.7990 |
| 4.0 | 1.4142 | 2.8285 | 1.1907 | 2.0000 | 3.3594 | 1.0919 | 1.5442 | 2.5903 | 3.6633 |
| 6.0 | 1.5651 | 3.8336 | 1.2544 | 2.4495 | 4.7832 | 1.1215 | 1.7553 | 3.4182 | 5.3500 |
| 8.0 | 1.6818 | 4.7568 | 1.3022 | 2.8284 | 6.1434 | 1.1436 | 1.9232 | 4.1597 | 6.9955 |
| 10.0 | 1.7783 | 5.6233 | 1.3409 | 3.1623 | 7.4577 | 1.1613 | 2.0651 | 4.8424 | 8.6110 |

| ZL/Z0 | N=5: Z1 | Z2 | Z3 | Z4 | Z5 | N=6: Z1 | Z2 | Z3 | Z4 | Z5 | Z6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| 1.5 | 1.0128 | 1.0790 | 1.2247 | 1.3902 | 1.4810 | 1.0064 | 1.0454 | 1.1496 | 1.3048 | 1.4349 | 1.4905 |
| 2.0 | 1.0220 | 1.1391 | 1.4142 | 1.7558 | 1.9569 | 1.0110 | 1.0790 | 1.2693 | 1.5757 | 1.8536 | 1.9782 |
| 3.0 | 1.0354 | 1.2300 | 1.7321 | 2.4390 | 2.8974 | 1.0176 | 1.1288 | 1.4599 | 2.0549 | 2.6577 | 2.9481 |
| 4.0 | 1.0452 | 1.2995 | 2.0000 | 3.0781 | 3.8270 | 1.0225 | 1.1661 | 1.6129 | 2.4800 | 3.4302 | 3.9120 |
| 6.0 | 1.0596 | 1.4055 | 2.4495 | 4.2689 | 5.6625 | 1.0296 | 1.2219 | 1.8573 | 3.2305 | 4.9104 | 5.8275 |
| 8.0 | 1.0703 | 1.4870 | 2.8284 | 5.3800 | 7.4745 | 1.0349 | 1.2640 | 2.0539 | 3.8950 | 6.3291 | 7.7302 |
| 10.0 | 1.0789 | 1.5541 | 3.1623 | 6.4346 | 9.2687 | 1.0392 | 1.2982 | 2.2215 | 4.5015 | 7.7030 | 9.6228 |

Consistency check (performed): Zn·Z(N+1−n) = ZL/Z0 for every row (e.g. N=6, ZL/Z0 = 10: 1.0392 × 9.6228 = 10.000); N=5, ZL/Z0 = 4 gives abs(Γ(f0)) = 0 by exact cascade.

### Table 2-22. Chebyshev transformer design — exact normalized impedances (Pozar Table 5.2, p.260)

| ZL/Z0 | N=2 Γm=0.05: Z1 | Z2 | N=2 Γm=0.20: Z1 | Z2 | N=3 Γm=0.05: Z1 | Z2 | Z3 | N=3 Γm=0.20: Z1 | Z2 | Z3 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1.0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| 1.5 | 1.1347 | 1.3219 | 1.2247 | 1.2247 | 1.1029 | 1.2247 | 1.3601 | 1.2247 | 1.2247 | 1.2247 |
| 2.0 | 1.2193 | 1.6402 | 1.3161 | 1.5197 | 1.1475 | 1.4142 | 1.7429 | 1.2855 | 1.4142 | 1.5558 |
| 3.0 | 1.3494 | 2.2232 | 1.4565 | 2.0598 | 1.2171 | 1.7321 | 2.4649 | 1.3743 | 1.7321 | 2.1829 |
| 4.0 | 1.4500 | 2.7585 | 1.5651 | 2.5558 | 1.2662 | 2.0000 | 3.1591 | 1.4333 | 2.0000 | 2.7908 |
| 6.0 | 1.6047 | 3.7389 | 1.7321 | 3.4641 | 1.3383 | 2.4495 | 4.4833 | 1.5193 | 2.4495 | 3.9492 |
| 8.0 | 1.7244 | 4.6393 | 1.8612 | 4.2983 | 1.3944 | 2.8284 | 5.7372 | 1.5766 | 2.8284 | 5.0742 |
| 10.0 | 1.8233 | 5.4845 | 1.9680 | 5.0813 | 1.4385 | 3.1623 | 6.9517 | 1.6415 | 3.1623 | 6.0920 |

| ZL/Z0 | N=4 Γm=0.05: Z1 | Z2 | Z3 | Z4 | N=4 Γm=0.20: Z1 | Z2 | Z3 | Z4 |
|---|---|---|---|---|---|---|---|---|
| 1.0 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| 1.5 | 1.0892 | 1.1742 | 1.2775 | 1.3772 | 1.2247 | 1.2247 | 1.2247 | 1.2247 |
| 2.0 | 1.1201 | 1.2979 | 1.5409 | 1.7855 | 1.2727 | 1.3634 | 1.4669 | 1.5715 |
| 3.0 | 1.1586 | 1.4876 | 2.0167 | 2.5893 | 1.4879 † | 1.5819 | 1.8965 | 2.0163 † |
| 4.0 | 1.1906 | 1.6414 | 2.4369 | 3.3597 | 1.3692 | 1.7490 | 2.2870 | 2.9214 |
| 6.0 | 1.2290 | 1.8773 | 3.1961 | 4.8820 | 1.4415 | 2.0231 | 2.9657 | 4.1623 |
| 8.0 | 1.2583 | 2.0657 | 3.8728 | 6.3578 | 1.4914 | 2.2428 | 3.5670 | 5.3641 |
| 10.0 | 1.2832 | 2.2268 | 4.4907 | 7.7930 | 1.5163 | 2.4210 | 4.1305 | 6.5950 |

† Suspected misprint (conf low): as printed, the N=4, Γm=0.20, ZL/Z0=3.0 row is non-monotonic vs its neighbours and an exact cascade of those values gives max abs(Γ) ≈ 0.40 over the design band (neighbouring rows give ≈ 0.21–0.22). Small-reflection theory (computed) gives Z1 ≈ 1.32, Z2 ≈ 1.58, Z3 ≈ 1.90, Z4 ≈ 2.26 — verify by simulation before use. Rows with ZL/Z0 = 1.5 at Γm = 0.20 collapse to a single-section value sqrt(1.5) = 1.2247.

### Table 2-23. Matching-network worked examples (Pozar Ch. 5)

| Example | Problem | Key results |
|---|---|---|
| 5.1 L-section (p.231) | 200 − j100 Ω → 100 Ω, 500 MHz | b = 0.29, x = 1.22 (0.92 pF ∥, 38.8 nH series) or b = −0.69, x = −1.22 (2.61 pF series, 46.1 nH ∥) |
| 5.2 shunt stub (p.235) | 60 − j80 Ω → 50 Ω, 2 GHz, shorted | d = 0.110λ, l = 0.095λ or d = 0.260λ, l = 0.405λ |
| 5.3 series stub (p.238) | 100 + j80 Ω → 50 Ω, 2 GHz, open | d = 0.120λ, l = 0.397λ or d = 0.463λ, l = 0.103λ |
| 5.4 double stub (p.243) | 60 − j80 Ω → 50 Ω, open stubs, λ/8 spacing | l1 = 0.146λ, l2 = 0.204λ or l1 = 0.482λ, l2 = 0.350λ |
| 5.5 λ/4 (p.249) | 10 Ω → 50 Ω, 3 GHz, SWR ≤ 1.5 | Z1 = 22.36 Ω, BW = 29% |
| 5.6 binomial N=3 (p.255) | 50 Ω → 100 Ω, Γm = 0.05 | 91.7 / 70.7 / 54.5 Ω, BW = 70% |
| 5.7 Chebyshev N=3 (p.259) | 100 Ω → 50 Ω, Γm = 0.05 | 57.5 / 70.7 / 87.0 Ω (exact 57.37 / 70.71 / 87.15), BW = 101% |
| 5.8 Klopfenstein (p.265) | 50 Ω → 100 Ω, Γm = 0.02 | Γ0 = 0.346, A = 3.543, passband βL ≥ 1.13π |

### Table 2-24. Bode–Fano limits (Pozar Fig. 5.22, p.268)

| Load | Limit |
|---|---|
| Parallel RC | ∫0^∞ ln(1/abs(Γ(ω))) dω ≤ π/(RC) |
| Series RC | ∫0^∞ ω^-2·ln(1/abs(Γ(ω))) dω ≤ πRC |
| Parallel RL | ∫0^∞ ω^-2·ln(1/abs(Γ(ω))) dω ≤ πL/R |
| Series RL | ∫0^∞ ln(1/abs(Γ(ω))) dω ≤ πR/L |

Square-response corollary (parallel RC): Δω·ln(1/Γm) ≤ π/(RC).

### Table 2-25. Series and parallel resonators (Pozar Table 6.1, p.278)

| Quantity | Series resonator | Parallel resonator |
|---|---|---|
| Input impedance / admittance | Zin = R + jωL − j/(ωC) ≈ R + j2RQ0·Δω/ω0 | Yin = 1/R + jωC − j/(ωL) ≈ 1/R + j2Q0·Δω/(R·ω0) |
| Power loss | Ploss = (1/2)abs(I)^2·R | Ploss = (1/2)abs(V)^2/R |
| Stored magnetic energy | Wm = (1/4)abs(I)^2·L | Wm = (1/4)abs(V)^2/(ω^2·L) |
| Stored electric energy | We = (1/4)abs(I)^2/(ω^2·C) | We = (1/4)abs(V)^2·C |
| Resonant frequency | ω0 = 1/sqrt(LC) | ω0 = 1/sqrt(LC) |
| Unloaded Q | Q0 = ω0L/R = 1/(ω0RC) | Q0 = ω0RC = R/(ω0L) |
| External Q | Qe = ω0L/RL | Qe = RL/(ω0L) |

1/QL = 1/Qe + 1/Q0; half-power fractional bandwidth = 1/Q.

### Table 2-26. Transmission-line resonators (Pozar §6.2, p.278–284)

| Resonator | Equivalent | R | L or C | Q0 |
|---|---|---|---|---|
| Short-circuited λ/2 | Series RLC | Z0·α·l | L = πZ0/(2ω0) | β/(2α) = π/(2αl) |
| Short-circuited λ/4 | Parallel RLC | Z0/(α·l) | C = π/(4ω0·Z0) | β/(2α) = π/(4αl) |
| Open-circuited λ/2 | Parallel RLC | Z0/(α·l) | C = π/(2ω0·Z0) | β/(2α) = π/(2αl) |

### Table 2-27. Resonator worked examples (Pozar Ch. 6)

| Example | Structure | Q results |
|---|---|---|
| 6.1 (p.280) | λ/2 Cu coax a = 1 mm, b = 4 mm, 5 GHz | air Q0 = 2380; Teflon Q0 = 1218 (αc 0.032 + αd 0.030 Np/m) |
| 6.2 (p.283) | λ/2 open 50 Ω microstrip, Teflon 0.159 cm, 5 GHz | l = 2.24 cm, β = 151.0 rad/m, αc = 0.0724, αd = 0.024 Np/m, Q0 = 783 |
| 6.3 (p.287) | Cu WR-187 cavity, polyethylene, 5 GHz | TE101: d = 2.20 cm, Qc = 8403, Qd = 2500, Q0 = 1927; TE102: d = 4.40 cm, Qc = 11,898, Q0 = 2065 |
| 6.4 (p.292) | Cu TE011 circular cavity d = 2a, Teflon, 5 GHz | a = 2.74 cm, d = 5.48 cm, Qc = 29,390, Qd = 2500, Q0 = 2300 (air 42,400) |
| 6.5 (p.297) | Titania DR εr = 95, tanδ = 0.001, a = 0.413 cm, L = 0.8255 cm | f ≈ 3.152 GHz (measured ≈ 3.4 GHz), Qd = 1000 |
| 6.6 (p.302) | Gap-coupled λ/2 microstrip, εe = 1.9, 0.01 dB/cm | Q0 = 628, bc = 0.05, C = 0.032 pF (critical), f = 4.918 GHz |

Copper Rs at 5 GHz = 1.84×10^-2 Ω (Example 6.1).

### Table 2-28. Three- and four-port network properties (Pozar §7.1, p.317–323)

| Network | Lossless | Reciprocal | All ports matched | Output isolation | Realization |
|---|---|---|---|---|---|
| Lossless T-junction | yes | yes | no (outputs mismatched) | no | E/H-plane T, microstrip T |
| Circulator | yes | no | yes | (directional) | ferrite junction |
| Resistive divider | no (½ power lost) | yes | yes | no | Z0/3 star, −6 dB per output |
| Wilkinson divider | lossless when outputs matched | yes | yes | yes | λ/4 lines sqrt(2)Z0 + 2Z0 resistor |
| Directional coupler (4-port) | yes | yes | yes | S14 = S23 = 0 | coupled lines, branch-line, etc. |

Coupler metrics: C = −20 log β; D = 20 log(β/abs(S14)); I = −20 logabs(S14); L = −20 logabs(S12); I = D + C.

## 3. Mechanizable checks

### Transmission-line basics (Ch. 1–2)

`CHECK-match-gamma` (match table → Γ, VSWR, RL, mismatch loss)
- inputs: per row `ZL_re` (Ω), `ZL_im` (Ω), `Z0` (Ω, real), `RL_min_dB` (spec) or `VSWR_max` (spec)
- formula: Γ = (ZL − Z0)/(ZL + Z0) (complex); abs(Γ); VSWR = (1 + abs(Γ))/(1 − abs(Γ)); RL = −20·log10abs(Γ); ML = −10·log10(1 − abs(Γ)^2); ∠Γ (deg)
- pass: RL ≥ RL_min_dB (equivalently VSWR ≤ VSWR_max); passive sanity abs(Γ) ≤ 1 (RL ≥ 0)
- margin: RL − RL_min_dB (dB) (or VSWR_max − VSWR)
- source rows: POZAR-1030, POZAR-1032, POZAR-1033, POZAR-1031; Table 2-6

`CHECK-zin-line` (input impedance through a line section)
- inputs: `Z0` (Ω), `ZL` (complex Ω), `length_m`, `f_Hz`, `eps_eff` (or `vp`), optional `alpha_Np_per_m`
- formula: β = 2πf·sqrt(eps_eff)/c; lossless Zin = Z0(ZL + jZ0 tan βl)/(Z0 + jZL tan βl); lossy Zin = Z0(ZL + Z0 tanh γl)/(Z0 + ZL tanh γl), γ = α + jβ; Γin = (Zin − Zref)/(Zin + Zref)
- pass: abs(Γin) ≤ Γ_spec at every frequency point of the band
- margin: Γ_spec − max_f abs(Γin) (or RL margin in dB)
- source rows: POZAR-1036, POZAR-1059, POZAR-1035

`CHECK-quarter-wave-band` (λ/4 transformer bandwidth)
- inputs: `Z0` (Ω), `RL` (Ω, real), `f0`, `f_lo`, `f_hi`, `Gamma_max`
- formula: Z1 = sqrt(Z0·RL); βl = (π/2)(f/f0); Zin(f) from TL equation with Z1, RL; abs(Γ(f)) = abs((Zin − Z0)/(Zin + Z0))
- pass: max over [f_lo, f_hi] of abs(Γ(f)) ≤ Gamma_max; RL must be real (else flag: rotate to real first)
- margin: Gamma_max − maxabs(Γ)
- source rows: POZAR-1049, POZAR-1050; see also CHECK-multisection-transformer (closed-form bandwidth)

`CHECK-power-delivery` (generator/load mismatch power)
- inputs: `Vg_peak` (V), `Rg`, `Xg` (Ω), `Zin` (complex Ω; from CHECK-zin-line)
- formula: P = (1/2)abs(Vg)^2·Rin/((Rin + Rg)^2 + (Xin + Xg)^2); P_avail = abs(Vg)^2/(8Rg); ML_gen = 10·log10(P_avail/P)
- pass: ML_gen ≤ allowed mismatch loss (dB); conjugate-match optimum is Zin = Zg*
- margin: allowed − ML_gen (dB)
- source rows: POZAR-1053, POZAR-1054, POZAR-1055

`CHECK-lossy-line-power` (line loss with reflection)
- inputs: `alpha_dB_per_m` (convert: α_Np = α_dB/8.686), `length_m`, `abs(Γ_L)`, `Z0`, `Vo_plus`
- formula: PL/Pin = (1 − abs(Γ)^2)/(e^{2αl} − abs(Γ)^2 e^{−2αl}); Ploss per eq. (2.94)
- pass: 10·log10(Pin/PL) ≤ loss budget (dB)
- margin: budget − computed loss (dB)
- source rows: POZAR-1060, POZAR-1041

`CHECK-skin-depth-plating`
- inputs: `f_min_Hz`, `sigma_S_per_m` (Table 2-2 / App. F), `t_conductor_m` (plating or copper thickness), `k_min` (user rule multiplier, e.g. 3)
- formula: δs = 1/sqrt(π f µ0 σ); ratio = t/δs; Rs = 1/(σ δs)
- pass: t/δs ≥ k_min (Pozar only says fields decay to negligible within "a few" skin depths → k_min is a user choice; conf low)
- margin: t/δs − k_min
- source rows: POZAR-1009, POZAR-1011, POZAR-1013

`CHECK-roughness-factor`
- inputs: `Delta_rms_m` (rms surface roughness), `f_Hz`, `sigma`
- formula: δs = 1/sqrt(π f µ0 σ); K = 1 + (2/π)·atan(1.4·(Δ/δs)^2); αc,rough = K·αc
- pass: αc,rough·l within loss budget (use K in every loss check); informational: K ≤ 2 always
- margin: loss budget − K·αc·l
- source rows: POZAR-1063

`CHECK-coax-geometry`
- inputs: `a_m` (inner radius), `b_m` (outer conductor inner radius), `eps_r`, `tan_d`, `sigma`, `f_Hz`, `Z0_target`
- formula: Z0 = (η0/(2π·sqrt(εr)))·ln(b/a); αc = Rs(1/a + 1/b)/(2η ln(b/a)); αd = k·tanδ/2, k = 2πf·sqrt(εr)/c
- pass: abs(Z0 − Z0_target)/Z0_target ≤ tolerance; α_total (dB/m) ≤ spec
- margin: tolerance − relative error; spec − α
- source rows: POZAR-1025, POZAR-1028, POZAR-1057, POZAR-1068

`CHECK-bounce-settling` (step response on a resistively terminated line)
- inputs: `V0`, `Rg`, `Z0`, `RL`, `length_m`, `vp`, `settle_pct`
- formula: v1 = V0·Z0/(Z0 + Rg); ΓL = (RL − Z0)/(RL + Z0); Γg = (Rg − Z0)/(Rg + Z0); load voltage after n round trips V_L(n) = v1(1 + ΓL)·Σ_{k=0..n}(ΓL·Γg)^k; V_final = V0·RL/(Rg + RL); t_n = (2n + 1)·l/vp
- pass: abs(V_L(n) − V_final) ≤ settle_pct·V_final by the required time; overshoot/ringing sign given by sign(ΓL·Γg)
- margin: allowed time − settling time
- source rows: POZAR-1064, POZAR-1066

### Planar lines, waveguides, coax, power capacity (Ch. 3)

`CHECK-microstrip-trace` (trace-geometry table → Z0, εeff, loss at f) — primary check for Anvil trace tables
- inputs per row: `W_m` (strip width), `d_m` (substrate height to reference plane), `eps_r`, `tan_d`, `sigma_S_per_m` (default Cu 5.813×10^7), `f_Hz`, `length_m`, `Z0_target_ohm`, `Z0_tol_pct`, `loss_budget_dB`, optional `rough_rms_m`
- formula:
  - εe = (εr + 1)/2 + ((εr − 1)/2)/sqrt(1 + 12d/W)  [POZAR-1099]
  - u = W/d; Z0 = (60/sqrt εe)·ln(8/u + u/4) if u ≤ 1, else 120π/(sqrt εe·(u + 1.393 + 0.667·ln(u + 1.444)))  [POZAR-1100]
  - dispersion: fp[GHz] = Z0/(8π·d[cm]); g = 0.6 + 0.009·Z0; εe(f) = εr − (εr − εe)/(1 + g(f/fp)^2)  [POZAR-1106]
  - k0 = 2πf/c; β = k0·sqrt(εe(f)); phase = β·length (deg); delay = length·sqrt(εe(f))/c
  - αd = k0·εr(εe − 1)·tanδ/(2·sqrt(εe)(εr − 1))  [POZAR-1102]
  - Rs = sqrt(πfµ0/σ); αc = Rs/(Z0·W)  [POZAR-1103]; optional K = 1 + (2/π)atan(1.4(Δ/δs)^2), αc ← K·αc  [POZAR-1063]
  - loss_dB = 8.686·(αc + αd)·length
  - thresholds fT1…fT4 (Table 2-14); f_limit = min(fT1, fT2, fT3, 0.5·fT4)  [POZAR-1109–1113]
- pass: abs(Z0 − Z0_target) ≤ Z0_tol_pct·Z0_target/100 AND loss_dB ≤ loss_budget_dB AND f_Hz < f_limit AND d << λ (quasi-static validity; flag if d > λ/10 as a heuristic, conf low)
- margin: Z0_tol − abs(ΔZ0) (Ω); loss_budget − loss_dB (dB); (f_limit − f)/f_limit (%)
- source rows: POZAR-1098–1106, 1109–1113, 1063. Note: closed-form αc overestimates CAD (Example 3.7: 0.094 vs 0.054 dB/cm) — treat as conservative.
- self-test: W = 0.483 mm, d = 0.5 mm, εr = 9.9, tanδ = 0.001, 10 GHz → εe = 6.665, Z0 ≈ 50 Ω, αd = 0.255 Np/m, αc = 1.08 Np/m, l(270°) = 8.72 mm (Example 3.7).

`CHECK-microstrip-width-synthesis`
- inputs: `Z0_target`, `eps_r`, `d_m`
- formula: A, B per POZAR-1101; W/d = 8e^A/(e^{2A} − 2) (valid if result < 2) else the B-branch
- pass: re-analysis with CHECK-microstrip-trace returns Z0 within 1% of target (closed-form round-trip consistency)
- margin: 1% − abs(Z0(W) − Z0_target)/Z0_target
- source rows: POZAR-1101, POZAR-1100; self-test Example 3.7 (A = 2.142, W/d = 0.9654)

`CHECK-stripline-trace`
- inputs: `W_m`, `b_m` (ground-to-ground spacing), `t_m` (strip thickness), `eps_r`, `tan_d`, `sigma`, `f_Hz`, `f_max_Hz`, `via_fence_spacing_m` (sidewall width across line), `length_m`, `Z0_target`, `Z0_tol_pct`
- formula: We per POZAR-1092; Z0 = (30π/sqrt εr)·b/(We + 0.441b); αd = πf·sqrt(εr)·tanδ/c; αc per POZAR-1094 (A-branch if sqrt(εr)Z0 < 120, else B-branch); λd = c/(f_max·sqrt εr)
- pass: Z0 within tolerance; b < λd/2; via_fence_spacing < λd/2; loss within budget
- margin: λd/2 − b; λd/2 − via_fence_spacing; tolerance margin
- source rows: POZAR-1090–1096; self-test Example 3.5 (W = 0.266 cm, αc = 0.122 Np/m, α = 2.41 dB/m)

`CHECK-coax-mode-limit`
- inputs: `a_m`, `b_m`, `eps_r`, `f_max_Hz`
- formula: kc ≈ 2/(a + b) (or exact from Fig. 3.16 / eq. 3.159); fc = c·kc/(2π·sqrt εr)
- pass: f_max ≤ 0.95·fc(TE11)
- margin: 0.95·fc − f_max (Hz)
- source rows: POZAR-1084–1086; self-test RG-401U: b/a = 3.33, εr = 2.2 → fc = 17.7 GHz (exact kca = 0.45), f_max = 16.8 GHz

`CHECK-waveguide-single-mode`
- inputs: `a_m`, `b_m` (a > b), `eps_r`, `f_lo_Hz`, `f_hi_Hz`
- formula: fc,mn = (c/(2 sqrt εr))·sqrt((m/a)^2 + (n/b)^2); next = min(fc20, fc01)
- pass: fc10 < f_lo and f_hi < next (only TE10 propagates)
- margin: (f_lo − fc10)/fc10 and (next − f_hi)/next (%) — attenuation rises steeply near cutoff (POZAR-1073), so keep f_lo well above fc10 (no numeric margin given in the text for waveguide)
- source rows: POZAR-1074, 1075, 1078

`CHECK-peak-power-capacity`
- inputs: line type, geometry (`a`, `b`), `Ed_V_per_m` (default 3×10^6 air), `P_peak_W`, `abs(Γ)`
- formula: coax Pmax = (π a^2 Ed^2/η0)·ln(b/a); waveguide Pmax = a·b·Ed^2/(4Zw); P_allowed = Pmax/(2·(1 + abs(Γ))^2)
- pass: P_peak ≤ P_allowed
- margin: 10·log10(P_allowed/P_peak) (dB)
- source rows: POZAR-1120–1123

`CHECK-connector-frequency`
- inputs: `connector_type`, `f_max_Hz`
- formula: lookup Table 2-11 (N 11–18 GHz, TNC < 1 GHz, SMA 18–25 GHz, APC-7 18 GHz, 2.4 mm ≈ 50 GHz)
- pass: f_max ≤ lower bound of the connector's quoted range (conservative)
- margin: limit − f_max
- source rows: POZAR-1088

`CHECK-surface-wave-threshold` (substrate choice for a microstrip design)
- inputs: `d_m`, `eps_r`, `f_max_Hz`, `has_discontinuities` (bool)
- formula: fT1, fT2 (Table 2-14)
- pass: f_max < fT1; and f_max < fT2 if the layout has bends/junctions/steps
- margin: (fT − f_max)/fT
- source rows: POZAR-1089, 1109, 1110

### Networks and matching (Ch. 4–5)

`CHECK-sparam-properties` (S-matrix table → reciprocity / losslessness / passivity)
- inputs: N×N complex S-matrix per frequency (`Sij_re`, `Sij_im`), common real `Z0`, tolerance `tol`
- formula: reciprocity error e_r = maxabs(Sij − Sji); column power p_i = Σk abs(Ski)^2; orthogonality o_ij = abs(Σk Ski·Skj*) (i ≠ j); (derived) passivity: eigenvalues of [U] − [S]^H[S] ≥ 0 (necessary condition: p_i ≤ 1)
- pass: passive device → p_i ≤ 1 + tol and eig ≥ −tol; claimed reciprocal → e_r ≤ tol; claimed lossless → abs(p_i − 1) ≤ tol and o_ij ≤ tol
- margin: tol − e_r; 1 − max p_i (dissipated fraction)
- source rows: POZAR-1131, 1132, 1134, 1138, 1139 (self-test Example 4.5: Σ = 0.745 → not lossless; S12 ≠ S21 → not reciprocal)

`CHECK-terminated-twoport` (match table → Γin/Γout of a two-port with arbitrary terminations)
- inputs: two-port S (complex), `Gamma_L`, `Gamma_S`, `RL_min_dB`
- formula: Γin = S11 + S12S21ΓL/(1 − S22ΓL); Γout = S22 + S12S21ΓS/(1 − S11ΓS); RL = −20 logabs(Γin)
- pass: RL ≥ RL_min_dB (never assume Γin = S11 unless ΓL = 0)
- margin: RL − RL_min_dB
- source rows: POZAR-1135, 1152; self-test Example 4.5 shorted port 2: Γ = −0.452, RL = 6.9 dB

`CHECK-abcd-cascade` (element list → S of a ladder/cascade)
- inputs: ordered list of blocks {series Z / shunt Y / line (Z0, βl or γl) / transformer N}, reference `Z0`, `f`
- formula: [ABCD] = Π blocks (Table 2-18, physical order); S from Table 2-17; IL = −20 logabs(S21); RL = −20 logabs(S11); reciprocity sanity AD − BC = 1
- pass: IL ≤ IL_max and RL ≥ RL_min across the band; abs(AD − BC − 1) ≤ 1e-9 for passive reciprocal blocks
- margin: IL_max − IL; RL − RL_min
- source rows: POZAR-1145–1148, 1166; self-test Example 4.4 T pad 8.56/141.8/8.56 Ω → S11 = 0, abs(S21) = 0.707

`CHECK-deembed-reference-plane`
- inputs: measured S at planes zn = 0, feed-line electrical lengths θn (= βn·ln) to move each plane outward (or −θn inward)
- formula: S'mn = Smn·e^{−j(θm + θn)}
- pass: de-embedded abs(Smn) unchanged (lossless feeds) and phase consistent with the model within tolerance
- margin: phase error allowance − abs(Δφ)
- source rows: POZAR-1140

`CHECK-microstrip-bend-miter` (layout inspection table)
- inputs per bend: `W`, bend angle, bend type {plain, mitered, swept}, miter length `a` or radius `r`, `f_max`
- formula: swept: r/W; mitered 90°: a/W
- pass: plain right-angle bends flagged at microwave frequencies; swept r ≥ 3W; mitered a ≈ 1.8W (Pozar's practical value; optimum depends on Z0 and angle → tolerance user-set)
- margin: r/W − 3; abs(a/W − 1.8) within tolerance
- source rows: POZAR-1158, 1159

`CHECK-open-end-length` (open stubs / open line ends)
- inputs: `w`, `d`, `eps_eff`, drawn stub length `l_drawn`, target electrical length
- formula: Δl = 0.412·d·(εe + 0.3)/(εe − 0.258)·(w + 0.262d)/(w + 0.813d); l_eff = l_drawn + Δl
- pass: abs(l_eff − l_target) ≤ tolerance
- margin: tolerance − abs(error)
- source rows: POZAR-1168 (Problem 4.30 data: d = 0.158 cm, εe = 1.894, w = 0.487 cm → Δl ≈ 0.075 cm)

`CHECK-L-section` (match table → lumped L network)
- inputs: `RL`, `XL` (Ω), `Z0`, `f0`, optional load model for sweep, `Gamma_max`, band
- formula: topology by RL vs Z0 (POZAR-1171); B, X by POZAR-1172/1173; element values by POZAR-1174; verify Zin(f0) = Z0; sweep abs(Γ(f)) with frequency-dependent element reactances and load model
- pass: abs(Γ(f0)) < 1e-6 (construction check); max abs(Γ) ≤ Gamma_max over band; element realizable (discrete L-sections ≲ 1 GHz; MIC element length < λ/10)
- margin: Gamma_max − maxabs(Γ)
- source rows: POZAR-1171–1176; self-test Example 5.1 (b = 0.29, x = 1.22; 0.92 pF, 38.8 nH)

`CHECK-stub-tuner` (single shunt/series stub)
- inputs: `RL`, `XL`, `Z0`, stub type {shunt / series}, termination {open / short}, `f0`, band, `Gamma_max`
- formula: t, d, B (or X), l per POZAR-1180 / 1182; choose the solution with the smallest d (then l); sweep abs(Γ(f)) with lengths scaled by f/f0
- pass: max abs(Γ) ≤ Gamma_max over band
- margin: Gamma_max − maxabs(Γ)
- source rows: POZAR-1178–1183; self-tests Examples 5.2 (d = 0.110λ, l = 0.095λ) and 5.3 (d = 0.120λ, l = 0.397λ)

`CHECK-double-stub-range`
- inputs: `YL` referred to the first stub (G, B), spacing `d` (in λ), `Y0`
- formula: t = tan(2πd/λ); G_max = Y0·(1 + t^2)/t^2 = Y0/sin^2(βd)
- pass: 0 ≤ G ≤ G_max (else load is in the forbidden region → change d or add a load-side line length); flag d/λ near 0 or 0.5 (frequency-sensitive); prefer λ/8 or 3λ/8
- margin: G_max − G
- source rows: POZAR-1184–1186

`CHECK-multisection-transformer` (λ/4 stepped transformer sizing)
- inputs: `Z0`, `ZL` (real), `Gamma_max`, required fractional bandwidth `BW_req`, type {single / binomial / chebyshev}
- formula: single: BW = 2 − (4/π)acos[(Γm/sqrt(1 − Γm^2))·2sqrt(Z0ZL)/abs(ZL − Z0)]; binomial: A = 2^−(N+1) ln(ZL/Z0), BW = 2 − (4/π)acos[(1/2)(Γm/abs(A))^(1/N)]; Chebyshev: sec θm = cosh[(1/N)acosh(abs(ln(ZL/Z0))/(2Γm))], BW = 2 − 4θm/π; section impedances from Tables 2-21/2-22 or ln(Zn+1/Zn) rules
- pass: BW(N) ≥ BW_req for the chosen minimum N; exact cascade of the chosen impedances gives maxabs(Γ) ≤ Γm over the band
- margin: BW(N) − BW_req
- source rows: POZAR-1189, 1192–1198; self-tests Examples 5.5 (29%), 5.6 (70%), 5.7 (101%)

`CHECK-bode-fano-feasibility` (is the matching spec physically possible?)
- inputs: load model {parallel RC / series RC / parallel RL / series RL} with R, C or L; band [f1, f2]; spec `Gamma_max`
- formula (ideal square response over Δω = 2π(f2 − f1), centre ω0): parallel RC Γmin = exp(−π/(RC·Δω)); series RL Γmin = exp(−πR/(L·Δω)); series RC and parallel RL use the 1/ω^2-weighted integrals (approximate with ω ≈ ω0: series RC Γmin ≈ exp(−π·R·C·ω0^2/Δω); parallel RL Γmin ≈ exp(−π·(L/R)·ω0^2/Δω) — ω0 approximation derived, conf medium)
- pass: Gamma_max ≥ Γmin (else no lossless network can meet the spec — relax band, accept loss, or change the load)
- margin: 20·log10(Gamma_max/Γmin) (dB of RL headroom)
- source rows: POZAR-1204–1206; self-test UWB 3.1–10.6 GHz, 75 Ω ∥ 0.6 pF → Γmin = 0.227 (RL ≤ 12.9 dB)

### Resonators, dividers, couplers (Ch. 6–7)

`CHECK-resonator-Q-from-S21` (measured or simulated two-port resonator data)
- inputs: `f0_Hz`, `f_lo_3dB_Hz`, `f_hi_3dB_Hz` (−3 dB relative to abs(S21(f0))), `S21_f0_lin` (real, planes at resonator), `topology` {series-in-series / parallel-appearing}
- formula: QL = f0/(f_hi − f_lo); g = S21/(1 − S21) (series) or its inverse (parallel); Q0 = (1 + g)·QL; Qe = Q0/g
- pass: Q0 ≥ Q0_required; coupling class as intended (g < 1 loose / g ≈ 1 critical / g > 1 tight)
- margin: Q0 − Q0_required
- source rows: POZAR-1229, POZAR-1233

`CHECK-line-resonator-Q` (resonator from a trace-geometry row)
- inputs: line row from CHECK-microstrip-trace (β, αc, αd at f0), resonator type {λ/2 open / λ/2 short / λ/4 short}
- formula: Q0 = β/(2(αc + αd)); equivalent R, L, C per Table 2-26
- pass: Q0 ≥ required (filter insertion-loss / oscillator phase-noise budgets use this Q0)
- margin: Q0 − required
- source rows: POZAR-1211–1216; self-test Example 6.2 (Q0 = 783)

`CHECK-cavity-Q`
- inputs: cavity type/mode, dimensions, `sigma`, `eps_r`, `tan_d`, `f0`
- formula: Rs = sqrt(πf0µ0/σ); Qc per POZAR-1219 (rectangular TE10l) or POZAR-1224 (circular TEnml; TE011 with d = 2a: Qc = kaη/(2Rs)); Qd = 1/tanδ; Q0 = (1/Qc + 1/Qd)^-1
- pass: Q0 ≥ required; and mode-chart check: no other mode within the tuning range (Fig. 6.9)
- margin: Q0 − required
- source rows: POZAR-1218–1225; self-tests Examples 6.3 (Q0 = 1927 / 2065) and 6.4 (Q0 = 2300)

`CHECK-gap-coupling` (critical coupling of a gap-coupled λ/2 microstrip resonator)
- inputs: `Q0`, `Z0`, `f0`
- formula: bc = sqrt(π/(2Q0)); C = bc/(2πf0·Z0); loaded resonance from tan βl + bc = 0 (expect a few % below f0)
- pass: realized gap capacitance within ± tolerance of C; resonance shift accounted for in resonator length
- margin: abs(C_realized − C)/C vs tolerance
- source rows: POZAR-1230, 1231 (self-test: Q0 = 628 → bc = 0.05, C = 0.032 pF, f = 4.918 GHz)

`CHECK-cavity-perturbation` (tuning range / material measurement)
- inputs: TE101 cavity a, b, d; slab thickness t and εr; or screw radius r0 and depth l
- formula: slab: Δf/f0 = −(εr − 1)·t/(2b); centred screw: Δf/f0 = −2πr0^2·l/(abd)
- pass: required tuning range achievable while abs(Δf/f0) stays small (perturbation valid)
- margin: tuning range − required
- source rows: POZAR-1234, 1235

`CHECK-coupler-metrics` (4-port S table → coupler figures of merit)
- inputs: abs(S12), abs(S13), abs(S14) (dB or linear) with port 1 input, 2 through, 3 coupled, 4 isolated; spec C_target ± tol, D_min (e.g. 35 dB)
- formula: C = −20 logabs(S13); D = 20 log(abs(S13)/abs(S14)); I = −20 logabs(S14); L = −20 logabs(S12); check I − (D + C) = 0
- pass: abs(C − C_target) ≤ tol and D ≥ D_min
- margin: D − D_min (dB)
- source rows: POZAR-1240–1243

`CHECK-divider-topology` (requirement consistency, three-port theorem)
- inputs: booleans lossless_req, reciprocal (true unless ferrite/active), all_ports_matched_req, output_isolation_req
- formula: if lossless ∧ reciprocal ∧ all-matched → infeasible (POZAR-1237); matched ∧ lossless → circulator only; all-matched ∧ isolation ∧ reciprocal → lossy (Wilkinson-type)
- pass: requested combination is realizable
- margin: n/a (boolean)
- source rows: POZAR-1237–1239, 1245–1248

`CHECK-T-junction-split`
- inputs: `Z0`, power ratio k = P2/P1 (output 2 vs output 1)
- formula: Z1 = Z0·(1 + k), Z2 = Z0·(1 + k)/k (lossless T, B = 0); output-port reflections Γ1 = ((Z0∥Z2) − Z1)/((Z0∥Z2) + Z1), Γ2 = ((Z0∥Z1) − Z2)/((Z0∥Z1) + Z2)
- pass: input matched (Z1∥Z2 = Z0); output mismatch acceptable to the loads' tolerance (no isolation)
- margin: output RL vs requirement
- source rows: POZAR-1245, 1246 (self-test 2:1 → 150 Ω / 75 Ω, Γ = −0.666 / −0.333)

## 4. Verification procedures & plots

### Ch. 2

- **Quarter-wave transformer response** (Fig. 2.17, p.73): x = f/fo (0 to 4), y = abs(Γ) (linear, 0–0.3) or RL (dB). Good: nulls at f/fo = 1, 3, …; pass band where abs(Γ) ≤ Γm. Sweep: dense (≥ 200 pts). Corners: Z1 tolerance, εeff tolerance (shifts fo). Source POZAR-1049/1050.
- **Standing-wave pattern** (Fig. 2.6, 2.8; eq. 2.39, p.58): x = distance from load (in λ, 0 to −λ), y = abs(V(z))/abs(Vo+). Good: flat line (SWR = 1). Read SWR = Vmax/Vmin, minima spacing λ/2. Source POZAR-1033/1034.
- **Smith chart trajectory** (Fig. 2.10–2.12, p.64–68): plot Γ(f) or zin(f) of the matched structure; good = trajectory clustered inside the abs(Γ) = Γm circle over the band. Clockwise rotation = toward generator. Source POZAR-1042/1043.
- **Slotted-line / standing-wave impedance measurement** (Example 2.4, p.70): step 1 short at load plane → record minima (gives λ/2 and reference plane); step 2 unknown load → record SWR and nearest minimum toward generator; compute Γ, ZL. Use minima (sharper). Modern substitute: VNA S11 with calibration (see Ch. 4 TRL). Source POZAR-1046/1047/1048.
- **Bounce (lattice) diagram** (Fig. 2.24, 2.26, p.88–89): x = position z (0 to l), y = time (0 to ≥ 4l/vp); label each ray with wave amplitude; total V(z,t) = sum of rays crossed by a vertical line at z up to t. Companion plot: V(load) vs t (staircase). Pass: settles to DC value V0·RL/(Rg + RL) within spec. Source POZAR-1064–1066.
- **Line attenuation vs frequency** (Problem 2.4 asks for this plot; formula from Example 2.6/2.7): x = f (log, 1 MHz–100 GHz), y = α (dB/m, log). Expected shape: conductor term ∝ sqrt(f) (Rs ∝ sqrt f), dielectric term ∝ f; crossover where αd = αc. Include roughness factor K(f) (eq. 2.107). Source POZAR-1057/1063 (shape derived → medium).

### Ch. 3

- **Microstrip εe(f) dispersion plot** (Fig. 3.27, p.152): x = frequency (0–20 GHz), y = εe. Overlay closed-form model (3.200) and CAD/EM. Good: model and EM agree within a few % up to the band edge; Example 3.8 model tracks CAD to ≈10 GHz then overestimates. Use εe(f_op) for phase-critical lines. Source POZAR-1106/1107.
- **Line attenuation vs frequency per mode** (Fig. 3.4 parallel plate, Fig. 3.8 rectangular brass a = 2.0 cm, Fig. 3.12 circular Cu a = 2.54 cm): x = frequency (or k/kc), y = αc (dB/m). Good: operating band sits well above the TE10/TE11 cutoff (αc → ∞ at cutoff) and below the next mode's cutoff. Source POZAR-1073/1077/1082.
- **Mode-cutoff bar chart** (Fig. 3.13 circular; Example 3.1 table rectangular): x = fc/fc(dominant), markers per mode; overlay the operating band. Pass: only the dominant mode inside the band. Source POZAR-1074/1081.
- **Surface-wave dispersion β/k0 vs d/λ0** (Fig. 3.21, εr = 2.55, d/λ0 = 0–1.2): curves for TM0, TE1, TM1, TE2, TM2, TE3 between 1 and sqrt(εr). Use to show which surface modes exist at f_max for a given substrate. Source POZAR-1089.
- **Microstrip Z0/εe vs W/d sweep** (eq. 3.195–3.196): x = W/d (log, 0.1–10), y1 = Z0 (Ω), y2 = εe; corners εr ± tolerance, d ± tolerance; mark target Z0 and its tolerance band; the width tolerance window is where Z0 stays in band. Source POZAR-1099/1100 (plot type derived → medium).
- **Stripline formula vs numerical vs CAD** (Example 3.6 table): x = W/b, y = Z0; use as regression plot for the calculator. Source POZAR-1097.
- **Threshold-frequency ladder** (Table 2-14): horizontal bars fT1…fT4 for the chosen substrate/width with the operating band overlaid; pass when the band ends below min(fT). Source POZAR-1113.
- **Peak-power capacity vs f_max** (Point of Interest p.160): x = f_max (log), y = Pmax (W, log) for coax (5.8×10^12 (Ed/f)^2) and waveguide (2.6×10^13 (Ed/f)^2); overlay required peak power × 2 × (1 + abs(Γ))^2. Source POZAR-1121–1123.

### Ch. 4–5

- **VNA S-parameter measurement** (Point of Interest p.188, Fig. 4.7): calibrate first (12-term error model; corrects coupler mismatch, imperfect directivity, loss, frequency response); sweep the band; display abs(S11)/RL, abs(S21)/IL, phase, group delay; optionally time-domain (inverse FFT) to locate discontinuities. Pass: calibration verified with a known check standard before DUT data are accepted. Source POZAR-1144.
- **TRL calibration** (§4.5, p.197–202): measure Thru [T], Reflect [R] (unknown large ΓL, nominal open/short) and Line [L] (matched line, unknown length/loss) at the measurement planes. Solve: e^{γl} = [L12^2 + T12^2 − (T11 − L11)^2 ± sqrt((L12^2 + T12^2 − (T11 − L11)^2)^2 − 4L12^2·T12^2)]/(2L12·T12) (sign: Re γ > 0, Im γ > 0 or known phase of ΓL); S22 = (T11 − L11)/(T12 − L12·e^{−γl}); S11 = T11 − S22·T12; S12^2 = T12(1 − S22^2); ΓL = (R11 − S11)/(S12^2 + S22(R11 − S11)) (eq. 4.89, consistent with R11 = S11 + S12^2·ΓL/(1 − S22·ΓL), eq. 4.81); convert error boxes to ABCD and de-embed: [ABCD]DUT = [ABCD]err^-1·[ABCD]meas·[D B; C A]err^-1 (port-2 box reversed). Assumes identical, reciprocal, symmetric error boxes. Source POZAR-1153 (eq. 4.80–4.90).
- **Reference-plane shift / de-embedding** (eq. 4.56): rotate Snn by e^{−2jθn}; plot S11 phase vs f before/after — good: after de-embedding, phase slope matches the DUT model. Source POZAR-1140.
- **Discontinuity characterization** (§4.6): EM-simulate or measure each transition/discontinuity (coax launch, open end, gap, step, T, bend); extract an equivalent circuit (Fig. 4.23) or S-block; plot abs(S11) of launch vs f — good: below the RL budget of the interconnect. Source POZAR-1150, 1156.
- **Matching-network response plots** (Figs. 5.3c, 5.5c, 5.6c, 5.9c, 5.12, 5.15, 5.17, 5.21): x = f (GHz) or f/f0 (0–2), y = abs(Γ) (0–1, linear) or RL (dB). Include the real frequency dependence of the load (e.g. series RC 60 Ω + 0.995 pF) and of all stubs/lines. Pass: abs(Γ) ≤ Γm across the required band. Compare candidate solutions on one plot (shorter d/l usually wider band). Source POZAR-1175–1206.
- **Multisection transformer comparison** (Figs. 5.15, 5.17): overlay N = 1…5 binomial and Chebyshev designs for the same ZL/Z0; y = abs(Γ), x = f/f0 (1/3 to 5/3). Good: Chebyshev equal ripple at Γm with wider band; binomial monotone. Source POZAR-1192–1198.
- **Taper response vs βL** (Figs. 5.19–5.21): x = βL (0–6π), y = abs(Γ); overlay exponential, triangular, Klopfenstein; mark Γm and the Klopfenstein passband edge βL = A. Source POZAR-1199–1203.
- **Return-loss area vs Bode–Fano bound** (Fig. 5.23): integrate ln(1/abs(Γ)) over ω for the designed network and compare with π/(RC) (or the relevant load bound); good = close to the bound with abs(Γ) ≈ Γm in-band and ≈ 1 out of band. Source POZAR-1204/1205.

### Ch. 6–7

- **Resonator transmission response** (Fig. 6.22, p.305): x = ω/ω0 (0.985–1.015), y = abs(S21) (dB, 0 to −30); measure f0, the −3 dB bandwidth relative to the resonance value, and abs(S21(f0)); derive QL, g, Q0 (CHECK-resonator-Q-from-S21). Curves for Q0 = 1000 with g = 0.5 and g = 4.0 illustrate under/over-coupling. Source POZAR-1233.
- **Coupling locus on the Smith chart** (Fig. 6.15, 6.18): plot Zin(f) of the coupled resonator; the resonance circle passes left of centre (overcoupled), through centre (critical), or right of centre (undercoupled). Example 6.6 overlays C = 0.06, 0.033, 0.02 pF. Source POZAR-1229–1231.
- **Cavity mode chart** (Fig. 6.9): x = (2a/d)^2, y = (2af)^2 (MHz·cm)^2; draw the operating line for the chosen shape and tuning range; pass when only the intended mode (e.g. TE011) lies in the tuning window. Source POZAR-1222.
- **Normalized cavity Q vs 2a/d** (Fig. 6.10): y = Q·δs/λ0 for TE011, TE012, TE111, TM010, TM111; pick shape near the TE011 optimum. Source POZAR-1223.
- **Cavity-perturbation dielectric measurement** (Example 6.7): measure f0 empty and f with a thin slab (thickness t) on the broad wall; εr = 1 + 2b·(f0 − f)/(f0·t) (inverted from POZAR-1234; derived). Source POZAR-1234.
- **Directional-coupler directivity by sliding load** (p.323–324): step 1 matched load → Pc; step 2 coupler reversed, sliding load on through arm → Pmax, Pmin (use a precision variable attenuator to read ratios); compute D. Requires load RL > D. Source POZAR-1244.
- **Divider S-parameter verification**: measure all Sii (match), S21/S31 (split), S23 (isolation) with the unused port terminated; compare with Table 2-28 expectations (T: no isolation, outputs mismatched; resistive: −6 dB, no isolation; Wilkinson: isolated). Source POZAR-1245–1248.

## 5. Pitfalls, failure modes, review checklist

- [ ] Skin depth at 10 GHz is < 1 µm for Al, Cu, Au, Ag (0.64–0.81 µm) — surface finish, plating and roughness dominate conductor loss at microwave frequencies (p.19).
- [ ] A conductor is "good" only if σ >> ωε; semiconductors/lossy substrates may violate this and cannot use Rs = 1/(σδs) (p.19).
- [ ] Brewster-angle (zero-reflection) behaviour exists only for parallel polarization; do not assume it for perpendicular polarization (p.38).

- [ ] Wave impedance (Zw = η for TEM, ZTE, ZTM) is not the characteristic impedance Z0 of the line; Z0 depends on geometry, Zw only on the medium (p.99, §3.1).
- [ ] Pozar's phasors are PEAK amplitudes: Pavg = abs(V)^2/(2R). A source quoted in V rms (e.g. Problem 2.16: 15 V rms) must be converted (×sqrt 2) before using book formulas, or the power is off by 2× (p.8–9, p.92).
- [ ] Return loss is a non-negative number for a passive network (RL = −20 logabs(Γ)); a negative "RL" in a report is a sign-convention error (p.58).
- [ ] Reflectionless match (ZL = Z0) ≠ conjugate match (Zin = Zg*); conjugate match maximizes delivered power, but neither maximizes efficiency (50% when Zg = ZL = Z0) (p.77–78).
- [ ] A quarter-wave transformer matches only a real load and only at fo (and odd multiples); a complex load must first be rotated to a real impedance by a series line length (single frequency) (p.73–74).
- [ ] Surface-impedance loss calculation (P = Rs/2 ∫abs(Js)^2) is invalid where conductor bends/corners have radii smaller than about a skin depth (p.34).
- [ ] Calculated conductor attenuation assumes smooth metal; measured attenuation is usually higher — always apply the roughness factor (up to 2×) (p.85, eq. 2.107).
- [ ] Splitting the complex Poynting vector into "incident" and "reflected" parts is meaningless; only time-average real power splits, and only in a lossless region (p.31–32).
- [ ] When measuring standing waves, locate voltage minima rather than maxima (minima are more sharply defined) (p.72).
- [ ] Standard circuit (lumped) analysis is invalid when component dimensions approach the wavelength — the phase varies across the device (p.1, p.48).
- [ ] A lossy line is dispersive (β not linear in ω) unless R/L = G/C; the effect accumulates on very long lines (p.80).
- [ ] Transient launch amplitude is set by Zg and Z0 (not ZL) until the first round trip 2l/vp has elapsed (p.86).

- [ ] Microstrip dielectric loss must use the filling factor q = εr(εe − 1)/(εe(εr − 1)); using the homogeneous TEM formula k·tanδ/2 with εr overstates αd (p.149).
- [ ] Do not neglect conductor loss in microstrip — for most substrates it exceeds dielectric loss (p.149).
- [ ] The simple microstrip αc = Rs/(Z0W) is approximate and runs high vs CAD (Example 3.7: 0.094 vs 0.054 dB/cm) (p.150).
- [ ] Phase-critical microstrip lengths computed with the DC εe(0) can be off by ≈14° per 360° at 10 GHz on εr = 10 substrate (Example 3.8) — use εe(f) (p.152–153).
- [ ] Every microstrip layout with bends/junctions/width steps can launch TE1 surface waves above fT2 = c/(4d·sqrt(εr − 1)); thick, high-εr substrates lower this limit (p.151).
- [ ] Narrow microstrip lines reach the parallel-plate-mode threshold up to 50% below c/(2d·sqrt εr) because fringing lengthens the path (p.152).
- [ ] Stripline: place ground-stitching (shorting) vias so the sidewall width stays < λd/2, and add vias at every ground-plane asymmetry such as a surface-mount coax launch (p.141).
- [ ] Stripline closed-form Z0 (3.179) assumes zero strip thickness and is ≈1% accurate vs exact; up to ≈9% off vs CAD for very wide strips (W/b = 5) (p.143, p.146).
- [ ] A metal lid/cover over microstrip perturbs the circuit even several substrate thicknesses away — include it in the EM model (p.159).
- [ ] Coax used above 0.95·fc(TE11) risks propagating the first waveguide mode; two modes with different β cause undesirable effects (p.132–133).
- [ ] Rectangular waveguide cannot be used over more than ≈ an octave (TE20 at 2·fc10); ridge guide widens band but lowers power capacity (p.158–159).
- [ ] Circular TE01 has falling loss with frequency but is not the dominant mode — mode conversion to lower modes wastes power (p.127).
- [ ] Waveguide cover-flange joints must be smooth, clean and square; imperfect joints cause reflection, resistive loss, and breakdown at high power (p.120).
- [ ] Power-capacity numbers are peak values; average capacity is lower; derate by ≥ 2× and by (1 + abs(Γ))^2 for reflections (÷4 at abs(Γ) = 1) (p.161).
- [ ] Phase velocity of a waveguide mode exceeds c; use group velocity vg = (dβ/dω)^-1 (< c) for signal delay (p.157).

- [ ] Γ at port n equals Snn only when every other port is matched; with real terminations use Γin = S11 + S12S21ΓL/(1 − S22ΓL) (p.183–184, p.197).
- [ ] Table 4.2 conversions assume the same real Z0 at both ports; for complex or unequal reference impedances use power-wave (generalized) S-parameters (p.185–188).
- [ ] Choosing the power-wave reference ZR = ZL* zeroes the reflected wave b but does NOT mean conjugate match or maximum power (p.187).
- [ ] ABCD uses I2 flowing OUT of port 2; cascade multiplication must follow the physical order; a reversed two-port has ABCD [D B; C A] (p.189, Problem 4.25).
- [ ] Raw VNA data include connectors, cables and transitions — calibrate/de-embed to the DUT reference planes; known-standard calibrations degrade at high frequency because the standards are imperfect (use TRL) (p.197–198).
- [ ] A nonreciprocal network cannot be represented by a passive equivalent circuit of reciprocal elements (p.194).
- [ ] The one-mode impedance viewpoint can give wrong answers (Problem 4.1: an E-plane height step analysed as a junction of two TE10 lines gives Γ = 0) — use modal/EM analysis for waveguide steps (p.222).
- [ ] Small-aperture coupling theory is approximate (valid for electrically small apertures away from edges/corners; can even give abs(Γ) > 1) (p.218, p.220).
- [ ] Plain right-angle microstrip bends add excess capacitance — miter (a ≈ 1.8W) or sweep (r ≥ 3W) them (p.209).
- [ ] CAD results are approximations — they miss fabrication tolerances, roughness, spurious coupling, higher-order modes, junction effects, thermal effects; run tolerance analysis and verify by measurement (p.202).
- [ ] A double-stub tuner cannot match loads in its forbidden region (G > Y0/sin^2 βd); stub spacings near 0 or λ/2 are very frequency sensitive (p.242–246).
- [ ] Place single stubs as close to the load as possible; long lines between stub and a high-SWR load narrow the bandwidth and add loss (p.236–237).
- [ ] In coax/waveguide an open-circuited stub may radiate (not purely reactive) — use shorted stubs there (p.235).
- [ ] A quarter-wave transformer matches only real loads; pre-rotating a complex load with a line or reactance usually shrinks bandwidth (p.246).
- [ ] Lumped MIC elements must be < λ/10 and modelled with parasitics; spiral inductors self-resonate (larger L → more shunt C) (p.233–234).
- [ ] No lossless network gives a perfect broadband match (Bode–Fano); high-Q (large R·C or L/R) loads are intrinsically narrowband (p.268).
- [ ] Binomial Table 5.1 lists only ZL/Z0 > 1 — for ZL/Z0 < 1 invert and number sections from the load (p.255).
- [ ] Pozar Table 5.2, N = 4, Γm = 0.20, ZL/Z0 = 3.0 row appears misprinted (as printed gives abs(Γ) ≈ 0.40 in band) — verify before use (Table 2-22 note).
- [ ] An exponential taper shorter than λ/2 (βL < π) leaves a large low-frequency mismatch; the Klopfenstein taper has impedance steps at both ends (p.263, p.265).

- [ ] A measured resonator Q is the LOADED Q; convert with Q0 = (1 + g)·QL using the coupling at resonance (p.305–306).
- [ ] Tight coupling lowers loaded Q; resonators used as frequency references/meters must be loosely coupled (p.298).
- [ ] Gap (capacitive) coupling lowers the resonant frequency (≈1.6% in Example 6.6) — cut the resonator for the loaded frequency (p.301–302).
- [ ] In dielectric-filled cavities the dielectric (Qd = 1/tanδ) usually dominates Q; air fill raises Q dramatically (Example 6.4: 2300 → 42,400) (p.288, p.293).
- [ ] Closed-form dielectric-resonator frequency (magnetic-wall model) is only ≈10% accurate — do not use it for final design (p.297).
- [ ] A tuning screw at the E-field maximum lowers the frequency; screws/walls in H-field regions can raise it — check location before relying on tuning direction (p.311).
- [ ] Do not specify a three-port that is lossless, reciprocal and matched at all ports — it is impossible (p.318).
- [ ] A lossless T-junction has unmatched, unisolated output ports; junction susceptance must be compensated (p.324–326).
- [ ] The resistive divider costs 6 dB per output (half the power dissipated) and gives no isolation (p.327–328).
- [ ] Coupler directivity below ≈35 dB degrades reflectometer accuracy; directivity cannot be read directly when a load mismatch masks it (p.323).
- [ ] Open-ended waveguide sections radiate — close cavities at both ends (p.284).

## 6. Standards referenced

| Standard / designation | Edition / year | Clause / table | What it governs (as used in the text) | Page |
|---|---|---|---|---|
| IEEE Std 211 — Standard Definitions of Terms for Radio Wave Propagation | 1997 | — | Terminology: "electric field"/"magnetic field" (not "field intensity"); recommends "relative permittivity" over "dielectric constant" | p.6 (fn. 1), p.11 (fn. 2) |
| IEEE Std 145 — Standard Definitions of Terms for Antennas | 1993 | — | Still recognizes the term "dielectric constant" | p.11 (fn. 2) |
| EIA "WR-" rectangular waveguide designations (standard waveguide bands 1–220 GHz; data in App. I) | — | App. I (not in this part) | WR-28 (Ka-band) components; WR-187 (H-band, a = 4.755 cm, b = 2.215 cm) cavity example | p.110–111 (Fig. 3.6), p.287 |
| RG-xxxU coaxial cable designations | — | — | RG-402U (0.91 mm / 3.02 mm, PTFE, 50 Ω, 0.43 dB/m at 1 GHz); RG-401U (0.0645 in / 0.215 in, PTFE εr = 2.2) | p.90, p.132 |
| Coaxial connector families (no standard numbers given) | — | — | Type-N, BNC/TNC, SMA, APC-7, 2.4 mm — frequency limits in Table 2-11 | p.134–135 |
| Waveguide flange types (cover, choke) — reference Montgomery, Dicke & Purcell, *Principles of Microwave Circuits* (1948) | — | — | Cover-to-cover SWR < 1.03; cover-to-choke SWR < 1.05 | p.120–121 |
| US frequency allocations (Fig. 1.1; issuing body not named) | — | Fig. 1.1 | ISM 902–928 MHz, 2.400–2.484 GHz, 5.725–5.850 GHz; UWB 3.1–10.6 GHz; GPS 1575.42/1227.60 MHz; cellular/GSM bands (Table 2-1) | p.2 |

## 7. Process / lifecycle guidance

Pozar is a design textbook rather than a product-development text; only the explicit design-flow guidance is captured.

| Stage | Activity | Deliverable | Exit criterion | Source |
|---|---|---|---|---|
| Specification | Define design goals (bandwidth, Γm/SWR, loss, power, size) | Spec table | Spec is physically achievable (e.g. Bode–Fano bound for matching, three-port theorem for dividers) | p.202; p.267–269; p.318 |
| Initial design | Engineer's initial topology and layout from experience; closed-form synthesis (Ch. 2–7 formulas) | Schematic + first-cut dimensions | Closed-form round-trip checks pass (CHECK-* in §3) | p.202 |
| CAD modelling | Circuit- and/or physics-based (EM) model including loss and discontinuities (bends, steps, T-junctions, launches) | Simulated S-parameters | Meets spec in simulation | p.202; p.150–151 |
| Optimization & tolerance study | Adjust parameters; study component/fabrication tolerances and errors (robustness) | Optimized, tolerance-checked design | Spec met across tolerance corners | p.202 |
| Prototype & measurement | Build prototype; calibrate VNA (12-term / TRL) and measure; derive Q, coupling, directivity etc. | Measured data vs model | Measured results satisfy spec, else revise and iterate (MMICs cannot be tuned after fabrication — rely on CAD before fab) | p.188, p.197–202, p.305 |

## 8. Coverage log

**Line ranges read (sequential Read chunks, all ≤ 2000 lines, no truncation reported):** 1–800 (front matter, preface, full TOC), 801–2800, 2801–4800, 4801–6800, 6801–8800, 8801–10200, 10201–12200, 12201–14200, 14201–16200, 16201–18200, 18201–20200, 20201–22200, 22200–23799, 23800–25599, 25600–27299, 27300–28999, 29000–30799, 30800–32549. Assigned range 1–32500 fully read; reading stopped at line 32549 (Pozar p.329, start of the Wilkinson even–odd analysis) — the remainder of §7.3 onward belongs to part 2.

**Chapter ↔ file-line map used:** Ch. 1 ≈ 419–4532; Ch. 2 ≈ 4533–9402; Ch. 3 ≈ 9403–16224; Ch. 4 ≈ 16225–22685; Ch. 5 ≈ 22686–27043; Ch. 6 ≈ 27044–31559; Ch. 7 from ≈ 31560 (§7.1 p.317, §7.2 p.324, §7.3 p.328 at ≈ 32471).

**Skipped within the range (and why):**
- Pure derivations with no design output: Maxwell's equations/boundary conditions (§1.2–1.3), general plane-wave and circular-polarization derivations (§1.5), Poynting theorem derivation (§1.6), reciprocity/image-theory proofs (§1.9), telegrapher-equation field derivation for coax (§2.2), TE/TM field-component derivations for parallel-plate, rectangular and circular guides (§3.2–3.4), coax Laplace solution (§3.5), stripline numerical (Fourier-series) capacitance method (§3.7 — only its comparison table kept), transverse-resonance and group-velocity derivations (§3.9–3.10), waveguide-excitation formalism (§4.7) and H-plane-step modal equations (§4.6) — results only, TRL algebra kept as a procedure, cavity-perturbation derivations (§6.7) — results only.
- Historical material (§1.1 history, waveguide history in Ch. 3 intro, microwave network theory history), photographs and figure-only content.
- Smith-chart figures (Figs. 2.10–2.15, 5.3, 5.5, 5.6, 5.9) extract as scattered scale numbers — ignored; the worked-example numbers read from the charts in the prose were kept.
- End-of-chapter problems (Ch. 1–6): skipped except those stating numeric design results — Problems 2.3 (RG-402U data), 2.27 (77 Ω min-loss coax), 3.28 (30 Ω max-power coax, consistent with POZAR-1087), 4.11–4.13, 4.15, 4.30 (open-end Δl formula), 5.24 (Bode–Fano bound, computed), 6.17 (disk resonator). The blank SWR/abs(Γ)/RL table of Problem 2.15 was filled by computation (Table 2-6, derived).

**Extraction limitations and corrections:**
- OCR drops ε (epsilon), script-l (length), radicals and many subscripts; formulas were reconstructed and numerically validated against the book's worked examples (all listed examples reproduced to the printed precision; Table 4.2 verified by S↔Z↔Y↔ABCD round-trip; Table 5.1 verified by Zn·Z(N+1−n) = ZL and exact cascade).
- Table 5.2 (Chebyshev), N = 4, Γm = 0.20, ZL/Z0 = 3.0 row: suspected misprint (exact cascade of the printed values gives abs(Γ) ≈ 0.40 in-band) — flagged in Table 2-22 and §5.
- Example 5.4: the text says solution 1 has the narrower bandwidth because its stubs are longer; as printed solution 1 has the shorter stubs. A recomputed sweep confirms solution 1 is narrower (48 MHz vs 92 MHz at abs(Γ) ≤ 0.2); POZAR-1186 records this.
- Example 3.8: phase value at 10 GHz is garbled in the extraction; recorded as ≈374° (recomputed 373.7° with εe = 8.12), error ≈14° as stated.
- Table 4.3 rectangular-slot polarizabilities and the coupler-directivity formula (p.324) had lost symbols (slot length l; square roots) — restored and marked conf medium.
- Figures are not in the text: rules depending on graphs (Figs. 1.14, 2.17, 3.4, 3.8, 3.12, 3.16, 3.21, 3.27, 4.25, 5.12, 5.15, 5.17, 5.21, 6.9, 6.10, 6.18, 6.22) give caption/anchor values only and are marked "graph" / conf medium.
- Values derived rather than stated are labelled "(derived)" or "(computed)" with conf medium: Table 2-2b (δs/Rs vs f), Table 2-6 (SWR/RL/mismatch loss), coax 60/sqrt(εr) constant, Bode–Fano ω0 approximations, general (1 + abs(Γ))^2 power derating, surface-wave threshold illustration for εr = 4.4, d = 1.6 mm, Wilkinson/T-junction split formulas for general ratios.
- Appendix tables requested in the assignment (App. E constants, App. F conductivities, App. G εr/tanδ) lie outside this line range; this part supplies the constants and material values quoted inside Ch. 1–7 (Tables 2-2, 2-2b, 2-4, 2-16) and defers the full appendix tables to part 2.

**Output statistics (validated at assembly):** 248 design rules (POZAR-1001 … POZAR-1248; no duplicate ids, no gaps, no dangling cross-references; confidence: 226 high, 20 medium, 2 low), 29 tables (Tables 2-1 … 2-28 plus 2-2b), 36 mechanizable checks (no duplicate or dangling CHECK names), verification/plot procedures for Ch. 2–7, pitfall checklist for Ch. 1–7. Absolute values are written abs(x) and Pozar's two-port determinants det(Z), det(Y) so that no table cell contains a raw pipe.
