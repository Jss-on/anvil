# Microwave Engineering (4th ed.), Part 2 — Anvil rulebook

## 0. Citation

D. M. Pozar, *Microwave Engineering*, 4th ed. Hoboken, NJ: John Wiley & Sons, 2012. ISBN 978-0-470-63155-3.

Chapters covered by THIS extraction (text lines 32,500–65,005, printed pp. ≈329–732): the rest of Ch.7 Power Dividers and Directional Couplers, from the even/odd analysis of §7.3 Wilkinson onward (§7.3–7.9, point of interest "The Reflectometer"); Ch.8 Microwave Filters (§8.1–8.8); Ch.9 Theory and Design of Ferrimagnetic Components (§9.1–9.6); Ch.10 Noise and Nonlinear Distortion (§10.1–10.4); Ch.11 Active RF and Microwave Devices (§11.1–11.5); Ch.12 Microwave Amplifier Design (§12.1–12.5); Ch.13 Oscillators and Mixers (§13.1–13.5); Ch.14 Introduction to Microwave Systems (§14.1–14.6); Appendices A–J (prefixes, math, physical constants, conductivities, dielectrics, ferrites, standard waveguide, standard coax); Answers to Selected Problems (used as test vectors); Index; end-matter "Useful Results".

Chapters NOT read in this extraction: front matter beyond the TOC, Ch.1 Electromagnetic Theory, Ch.2 Transmission Line Theory, Ch.3 Transmission Lines and Waveguides, Ch.4 Microwave Network Analysis, Ch.5 Impedance Matching and Tuning, Ch.6 Microwave Resonators, and §7.1–early §7.3 (text lines 1–32,500) — reason: assigned to the part-1 agent (rules POZAR-0xx/1xx). Lines 1–700 (TOC) were read here for orientation only.

Id block: POZAR-201 … POZAR-482 (282 rules). Tables: T2.1–T2.30. Checks: 25. All formulas used in §3 were re-computed against the book's worked examples (scratch script reproduced every anchor value listed as a "test vector").

Symbols (used throughout): Z0 reference impedance; f0/w0 design frequency; Delta fractional bandwidth; g_k low-pass prototype element values; Gamma reflection coefficient; K, Delta(S), mu stability factors; F noise factor (linear), NF (dB); Te noise temperature; T0 = 290 K; k = 1.380e-23 J/K; OIP3/IIP3 output/input third-order intercept; P1dB 1 dB compression; L(fm) SSB phase noise (dBc/Hz); Eb/n0 energy per bit to noise density.

## 1. Design rules

Conventions: Z0 = system/reference impedance (ohm); f0 = design (center) frequency; lambda = wavelength in the line (lambda_g for waveguide); beta = phase constant (rad/m); all dB quantities are 10*log10 of power ratios unless noted. "Figure" data (graphs) are marked conf=medium.

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| POZAR-201 | rf | Equal-split Wilkinson divider element values | quarter-wave arms Z = sqrt(2)*Z0 (70.7 ohm for Z0=50); isolation resistor R = 2*Z0 (100 ohm for Z0=50); arms lambda/4 at f0 | Z0, f0 | 3-port, equal (-3 dB) split, TEM/quasi-TEM planar; narrowband about f0 | calc | §7.3, Ex.7.2, p.331 | high |
| POZAR-202 | rf | Ideal equal-split Wilkinson S-parameters at f0 (all ports matched, outputs isolated) | S11 = S22 = S33 = 0; S21 = S31 = -j/sqrt(2) (-3.01 dB each); S23 = S32 = 0 | — | at f0 with matched terminations; response vs frequency 0.5f0–1.5f0 in Fig.7.12 (graph) | sim | §7.3 p.330–331, Fig.7.12 | high |
| POZAR-203 | rf | Wilkinson divider is lossless when outputs are matched; the isolation resistor dissipates only power reflected from ports 2/3 (so its power rating is set by worst-case output mismatch/imbalance) | P_R = 0 when ports 2,3 matched | output VSWR, drive power | divider or combiner use; rating statement is a derived design consequence | review | §7.3 p.331 | high (dissipation) / low (rating note) |
| POZAR-204 | rf | Unequal-split Wilkinson design equations with power ratio K^2 = P3/P2 | Z03 = Z0*sqrt((1+K^2)/K^3); Z02 = K^2*Z03 = Z0*sqrt(K*(1+K^2)); R = Z0*(K + 1/K); output ports are then matched to R2 = Z0*K and R3 = Z0/K (add lambda/4 transformers to reach Z0) | K, Z0 | reduces to equal split at K = 1 | calc | §7.3 eq.(7.37a–c), Fig.7.13, p.332 | high |
| POZAR-205 | rf | N-way equal-split Wilkinson: N lambda/4 arms of sqrt(N)*Z0 with a Z0 resistor from each output to a common node; matched at all ports with isolation between all ports; needs resistor crossovers for N >= 3 (hard in planar form); multi-section (stepped) versions give more bandwidth | Z_arm = sqrt(N)*Z0; R = Z0 | N, Z0 | planar crossovers are the practical limit for N>=3 | review | §7.3 Fig.7.14, p.332–333 | medium (figure) |
| POZAR-206 | rf | Directional coupler directivity | D(dB) = I(dB) - C(dB); ideal coupler: lossless, matched, I and D infinite (only C defines it) | C, I (dB) | 4-port coupler; port 1 input, 2 through, 3 coupled, 4 isolated | measure | §7.4 p.333–334 | high |
| POZAR-207 | rf | Hybrid junction definition | 3 dB coupling; output phase difference 90 deg (quadrature/branch-line) or 180 deg (magic-T, rat-race) | — | classification for part/topology selection | review | §7.4 p.334 | high |
| POZAR-208 | rf | Bethe-hole coupler (parallel waveguides, round hole): aperture offset s that cancels the isolated-port wave | sin(pi*s/a) = lambda0 / sqrt(2*(lambda0^2 - a^2)); round-hole polarizabilities alpha_e = 2*r0^3/3, alpha_m = 4*r0^3/3; C = 20*log10\|A/A10-\| dB; D = 20*log10\|A10-/A10+\| dB | a (m), lambda0 (m), r0 (m) | single small aperture in common broad wall, TE10; narrowband | calc | §7.4 eq.(7.41),(7.42a,b), p.335–336 | high |
| POZAR-209 | rf | Skewed Bethe-hole coupler (hole at s = a/2): skew angle and coupling | cos(theta) = k0^2/(2*beta^2); C = -20*log10(4*k0^2*r0^3/(3*a*b*beta)) dB | k0, beta (1/m), a, b, r0 (m) | awkward angular geometry; correct only at design frequency | calc | §7.4 eq.(7.44),(7.45), p.336 | high |
| POZAR-210 | rf | Worked Bethe-hole design (anchor): WR-90 X-band at 9 GHz, C = 20 dB | a = 0.02286 m, b = 0.01016 m, lambda0 = 0.0333 m, k0 = 188.5 1/m, beta = 129.0 1/m, Z10 = 550.9 ohm, P10 = 4.22e-7 m^2/ohm; s = 0.424a = 9.69 mm; r0 = 4.15 mm | — | coupling varies < 1 dB over 7–11 GHz; directivity > 60 dB at 9 GHz falling to 15–20 dB at band edges | calc | §7.4 Ex.7.3, Fig.7.17, p.337–338 | high |
| POZAR-211 | rf | Single-aperture (and any cancellation-based) coupler: directivity is far more frequency-sensitive than coupling, because it depends on cancellation of two wave components; specify/verify directivity across the whole band, not only at f0 | D(f) must be checked at band edges | band | all couplers that rely on cancellation (holes, branch-line) | sim | §7.4 p.337–338 | high |
| POZAR-212 | rf | Two-hole coupler principle: holes spaced lambda_g/4; waves add in phase at the coupled port and cancel (lambda_g/2 path difference) at the isolated port | d = lambda_g/4 at f0 | lambda_g | also realizable in microstrip/stripline | calc | §7.4 Fig.7.18, p.338 | high |
| POZAR-213 | rf | Weak-coupling approximation for multi-aperture couplers: for a 20 dB coupler, through power 0.99, field drop sqrt(0.99)=0.995 (0.5%) so equal amplitude at every aperture is a good assumption | coupling power factor = 10^(-C/10) | C (dB) | valid for weak coupling (e.g. >= 20 dB) | calc | §7.4 p.339 | high |
| POZAR-214 | rf | Multihole coupler coupling and directivity (N+1 holes, spacing d, forward/backward hole coefficients Fn, Bn) | C = -20*log10\|sum_n Fn\| dB; D = -C - 20*log10\|sum_n Bn*exp(-2j*beta*n*d)\| dB; round holes: Fn = Kf*rn^3, Bn = Kb*rn^3 | Fn, Bn, beta, d, rn | synthesize the directivity response; coupling stays nearly constant with frequency | calc | §7.4 eq.(7.46)–(7.52), p.339–340 | high |
| POZAR-215 | rf | Binomial (maximally flat directivity) multihole coupler | rn^3 = k*C(N,n) (binomial coefficient); C = -20log\|Kf\| - 20log k - 20log(sum_n C(N,n)) dB; spacing d = lambda_g/4 at center frequency | N, Kf, C | N+1 holes | calc | §7.4 eq.(7.54),(7.55), p.340–341 | high |
| POZAR-216 | rf | Chebyshev (equal-ripple directivity) multihole coupler | S = k*\|T_N(sec(theta_m)*cos(theta))\|, theta = beta*d; D_min = 20*log10(T_N(sec(theta_m))) dB; C = -20log\|Kf\| - 20log k - 20log\|T_N(sec theta_m)\| dB; T_N(x) = cosh(N*acosh(x)) for \|x\|>1 | N, D_min, C, Kf | symmetric coupler; N even -> odd number of holes (eq.7.56), N odd -> even number of holes (eq.7.60); D not exactly Chebyshev since Kf/Kb varies with f (small error) | calc | §7.4 eq.(7.56)–(7.60), p.341 | high |
| POZAR-217 | rf | Worked 4-hole Chebyshev coupler (anchor): WR-90, s = a/4, f0 = 9 GHz, C = 20 dB, D_min = 40 dB | \|Kf\| = 3.953e5, \|Kb\| = 3.454e5; T3(sec theta_m) = 100 -> sec theta_m = 3.01, theta_m = 70.6 deg and 109.4 deg at band edges; k = 2.53e-9; r0 = r3 = 3.26 mm, r1 = r2 = 4.51 mm | — | directivity bandwidth much wider than single Bethe hole (Fig.7.20) | calc | §7.5 Ex.7.4, Fig.7.20, p.341–343 | high |
| POZAR-218 | rf | Branch-line (quadrature) hybrid element values | series (through) arms Z0/sqrt(2) (35.4 ohm for Z0=50); shunt arms Z0; all four arms lambda/4 at f0 | Z0, f0 | microstrip/stripline; single section | calc | §7.5 Fig.7.21, Ex.7.5, p.343, 346 | high |
| POZAR-219 | rf | Branch-line hybrid S-matrix: port 1 input -> port 2 at -90 deg, port 3 at -180 deg, each half power; port 4 isolated; any port can be input (outputs are on the opposite side, isolated port on the same side) | [S] = (-1/sqrt(2)) * [[0,j,1,0],[j,0,0,1],[1,0,0,j],[0,1,j,0]] | — | at f0 | sim | §7.5 eq.(7.61),(7.67), p.343–345 | high |
| POZAR-220 | rf | Branch-line hybrid bandwidth is limited to 10%–20% by the quarter-wave arms; cascading multiple sections extends it to a decade or more | BW_1section ≈ 10–20 % | BW required | single section; return loss, isolation, and split all degrade quickly away from f0 (Fig.7.25) | sim | §7.5 p.346 | high |
| POZAR-221 | rf | Branch-line junction discontinuities may require the shunt arms to be lengthened by 10–20 deg (electrical) | shunt arm length = 90 deg + (10..20 deg) | layout | microstrip/stripline T-junction parasitics; confirm with EM sim | sim | §7.5 p.346 | high |
| POZAR-222 | rf | Coupled-line even/odd mode capacitances and impedances (symmetric TEM pair; C11 = C22 to ground, C12 between strips) | Ce = C11; Co = C11 + 2*C12; Z0e = 1/(vp*Ce); Z0o = 1/(vp*Co); vp = c/sqrt(er) | C11, C12 (F/m), er | TEM (coax, stripline) exact; microstrip/CPW/slotline only approximately TEM | calc | §7.6 eq.(7.68)–(7.71), p.348–349 | high |
| POZAR-223 | rf | Edge-coupled stripline design data scale with dielectric constant (TEM): read W/b and S/b from normalized curves of sqrt(er)*Z0e vs sqrt(er)*Z0o | use Fig.7.29 with sqrt(er)*Z0e, sqrt(er)*Z0o | Z0e, Z0o, er, b | symmetric edge-coupled stripline | calc | §7.6 Fig.7.29, p.349–350 | medium (graph) |
| POZAR-224 | rf | Coupled microstrip data do NOT scale with er (need a chart per er; Fig.7.30 is er = 10), and even/odd phase velocities differ, which degrades coupler directivity | v_pe != v_po for microstrip | er, geometry | coupled microstrip couplers/filters; prefer stripline when directivity matters | review | §7.6 Fig.7.30, p.350 | high |
| POZAR-225 | rf | Broadside-coupled stripline (W >> S, W >> b, fringing ignored) even/odd impedances | C11 = 2*er*e0*W/(b-S); C12 = er*e0*W/S; Z0e = eta0*(b-S)/(2*W*sqrt(er)); Z0o = eta0/(2*W*sqrt(er)*(1/(b-S) + 1/S)); eta0 = 377 ohm | W, S, b (m), er | parallel-plate approximation, no fringing | calc | §7.6 Ex.7.6, p.350–351 | high |
| POZAR-226 | rf | Single-section coupled-line coupler match condition: all ports matched and port 4 perfectly isolated at ANY frequency when Z0 equals the geometric mean of the mode impedances (equal mode velocities assumed) | Z0 = sqrt(Z0e*Z0o) | Z0e, Z0o | TEM (equal even/odd phase velocity) | calc | §7.6 eq.(7.77),(7.78), p.354 | high |
| POZAR-227 | rf | Coupled-line coupler midband voltage coupling factor | C = (Z0e - Z0o)/(Z0e + Z0o) (voltage ratio V3/V0 at theta = pi/2); C_dB = -20*log10(C) | Z0e, Z0o | single lambda/4 section | calc | §7.6 eq.(7.81),(7.85), p.354 | high |
| POZAR-228 | rf | Coupled-line coupler design equations from Z0 and voltage coupling C | Z0e = Z0*sqrt((1+C)/(1-C)); Z0o = Z0*sqrt((1-C)/(1+C)) | Z0, C (= 10^(-C_dB/20)) | TEM; best for weak coupling (tight coupling needs impractically close lines or non-realizable Z0e/Z0o) | calc | §7.6 eq.(7.87a,b), p.355 | high |
| POZAR-229 | rf | Coupled-line coupler frequency response (single section, electrical length theta) | V3/V0 = j*C*tan(theta)/(sqrt(1-C^2) + j*tan(theta)); V2/V0 = sqrt(1-C^2)/(sqrt(1-C^2)*cos(theta) + j*sin(theta)); V4 = 0; at theta = pi/2: V3/V0 = C, V2/V0 = -j*sqrt(1-C^2) (outputs in quadrature) | C, theta | coupling maxima at theta = pi/2, 3pi/2, ...; operate at first maximum (lambda/4) for small size, minimum line loss | calc | §7.6 eq.(7.82)–(7.86), Fig.7.33, p.354 | high |
| POZAR-230 | rf | Coupled-microstrip couplers have unequal even/odd phase velocities (even mode has less fringing field in air -> higher e_eff, lower v_p) giving poor directivity; compensate with dielectric overlays or anisotropic substrates, or use stripline | v_pe < v_po in microstrip | medium | microstrip, other non-TEM lines | sim | §7.6 p.355 | high |
| POZAR-231 | rf | Worked 20 dB single-section stripline coupler (anchor) | b = 0.32 cm, er = 2.2, Z0 = 50 ohm, f0 = 3 GHz: C = 0.1; Z0e = 55.28 ohm, Z0o = 45.23 ohm; sqrt(er)*Z0e = 82.0, sqrt(er)*Z0o = 67.1; W/b = 0.809, S/b = 0.306; W = 0.259 cm, S = 0.098 cm | — | with tan_delta = 0.05 and 2 mil copper, losses reduce directivity, which is typically > 70 dB without loss (Fig.7.34) | calc | §7.6 Ex.7.7, Fig.7.34, p.355–356 | high |
| POZAR-232 | rf | Multisection coupled-line coupler: use an odd number N of lambda/4 sections (better phase), weak coupling (C >= 10 dB); the section voltage couplings Cn form a Fourier series of the coupling response (synthesize COUPLING, not directivity) | V3/V1 = 2j*sin(theta)*exp(-j*N*theta)*[C1*cos((N-1)theta) + C2*cos((N-3)theta) + ... + CM/2], M = (N+1)/2; symmetric C1 = CN, C2 = CN-1 | Cn, N | decade bandwidths possible only at low coupling levels; even/odd velocity equality more critical than single section -> stripline preferred | calc | §7.6 eq.(7.88)–(7.91), p.356–357 | high |
| POZAR-233 | rf | Worked 3-section binomial (maximally flat) 20 dB coupled-line coupler (anchor) | conditions: C0 = C2 - 2*C1 = 0.1 and 10*C1 - C2 = 0 -> C1 = C3 = 0.0125, C2 = 0.125; Z0e1 = Z0e3 = 50.63, Z0o1 = Z0o3 = 49.38, Z0e2 = 56.69, Z0o2 = 44.10 ohm (Z0 = 50 ohm, f0 = 3 GHz) | — | ideal directivity D > 100 dB (Fig.7.37) | calc | §7.6 Ex.7.8, Fig.7.37, p.358–359 | high |
| POZAR-234 | rf | Directivity of coupled-line couplers is degraded by mismatched mode phase velocities, junction discontinuities, load mismatches, and fabrication tolerances | — | layout, tolerance | multisection especially | sim | §7.6 p.357 | high |
| POZAR-235 | rf | Lange (interdigitated, 4-finger) coupler: use when 3 dB or 6 dB coupling is needed (edge-coupled pair too loose); gives 3 dB with an octave or more bandwidth, 90 deg outputs (quadrature), partially compensates unequal mode velocities; drawback: very narrow, closely spaced lines and bond wires | C = 3 dB .. 6 dB; BW >= octave | C | microstrip MIC/MMIC | review | §7.7 p.359 | high |
| POZAR-236 | rf | Lange coupler: 4-wire mode impedances from adjacent-pair Z0e, Z0o | Ze4 = Z0e*(Z0o+Z0e)/(3*Z0o+Z0e); Zo4 = Z0o*(Z0o+Z0e)/(3*Z0e+Z0o); Z0 = sqrt(Ze4*Zo4) = sqrt(Z0e*Z0o*(Z0o+Z0e)^2/((3*Z0o+Z0e)*(3*Z0e+Z0o))); C = 3*(Z0e^2 - Z0o^2)/(3*(Z0e^2 + Z0o^2) + 2*Z0e*Z0o) | Z0e, Z0o (adjacent pair) | nearest-neighbour coupling only, equal mode velocities (approximate but usually sufficient) | calc | §7.7 eq.(7.97)–(7.99), p.362 | high |
| POZAR-237 | rf | Lange coupler design (invert for adjacent-pair impedances) | Z0e = Z0*(4C - 3 + sqrt(9 - 8C^2))/(2C*sqrt((1-C)/(1+C))); Z0o = Z0*(4C + 3 - sqrt(9 - 8C^2))/(2C*sqrt((1+C)/(1-C))) | Z0, C (voltage) | e.g. C = 0.7071 (3 dB), Z0 = 50: Z0e ≈ 176 ohm, Z0o ≈ 52.6 ohm (computed from the formula, conf medium) | calc | §7.7 eq.(7.100a,b), p.362 | high |
| POZAR-238 | rf | Ideal 3 dB 180-deg hybrid S-matrix (port 1 = sum, port 4 = difference): port 1 splits in phase to 2,3 with 4 isolated; port 4 splits 180 deg out of phase with 1 isolated; as combiner, sum at 1, difference at 4 | [S] = (-j/sqrt(2))*[[0,1,1,0],[1,0,0,-1],[1,0,0,1],[0,-1,1,0]] | — | unitary, symmetric | sim | §7.8 eq.(7.101), p.362–363 | high |
| POZAR-239 | rf | Ring hybrid (rat-race) element values: ring impedance sqrt(2)*Z0 (70.7 ohm for 50), feedlines Z0; port spacings lambda/4, lambda/4, lambda/4 and 3lambda/4 (ring circumference 1.5 lambda) | Z_ring = sqrt(2)*Z0; circumference = 3*lambda/2 | Z0, f0 | planar or waveguide; bandwidth 20%–30%, extend with extra sections or symmetric ring | calc | §7.8 Fig.7.42a, Ex.7.9, p.363, 367 | high |
| POZAR-240 | rf | Tapered coupled-line 180-deg hybrid: arbitrary power division with decade-or-more bandwidth | Z0e(0) = Z0o(0) = Z0; Z0e(L) = Z0/k, Z0o(L) = k*Z0, Z0e(z)*Z0o(z) = Z0^2 for all z (Klopfenstein taper); voltage coupling 4->3: beta = 2*sqrt(k)/(k+1); 4->2: alpha = (1-k)/(1+k); alpha^2 + beta^2 = 1; uncoupled Z0 phase-compensation section of the same electrical length theta = beta*L; both sections electrically long for a good match | k (0..1), Z0 | asymmetric tapered coupler | calc | §7.8 eq.(7.110)–(7.118), Fig.7.47, p.367–371 | high |
| POZAR-241 | rf | Magic-T tuning posts or irises used for matching must be placed symmetrically to preserve hybrid operation (sum/difference isolation) | symmetric placement | mech drawing | waveguide magic-T | inspect | §7.8 p.371 | high |
| POZAR-242 | rf | Riblet short-slot coupler: interaction-region width must be small enough that TE30 does not propagate (only TE10/TE20) | width < TE30 cutoff width | waveguide width | waveguide; usually smaller than other waveguide couplers | calc | §7.9 p.373 | high |
| POZAR-243 | rf | Schwinger reversed-phase coupler: directivity essentially frequency-independent but coupling very frequency sensitive (opposite of multihole coupler) | slot spacing lambda_g/4 | — | waveguide | review | §7.9 p.372–373 | high |
| POZAR-244 | test | Reflectometer / SWR measurement error from finite coupler directivity: measurement uncertainty ≈ ±1/D (numeric); use a coupler with directivity preferably > 40 dB | \|Vr/Vi\|max,min = (\|Gamma\| ± 1/D)/(1 ∓ \|Gamma\|/D); D = 10^(D_dB/20) | Gamma, D_dB | loose coupling (1 - C^2 ≈ 1), matched coupler | calc | §7 Point of Interest "The Reflectometer", p.374–375 | high |
| POZAR-245 | rf | Coupler port powers from datasheet parameters (all ports matched) | P_coupled = P_in - C; P_isolated = P_in - C - D = P_in - I; P_through = P_in - L (all dB/dBm); C = -20log\|S13\|, D = 20log(\|S13\|/\|S14\|), I = -20log\|S14\|, L = -20log\|S12\| | P_in (dBm), C, D, L (dB) | definitions of eq.(7.20) (in §7.1) as used in Problems 7.1–7.3 | calc | §7.1 eq.(7.20) (ref.), Problems 7.1–7.3, p.376 | medium |
| POZAR-246 | filter | Periodically loaded line (shunt normalized susceptance b every d) dispersion: passband where \|RHS\| <= 1, stopband (reflective, not dissipative) where \|RHS\| > 1 | cos(beta*d) = cos(theta) - (b/2)*sin(theta), theta = k*d; stopband: cosh(alpha*d) = \|cos(theta) - (b/2)*sin(theta)\| >= 1 | b, k, d | lossless loaded line; infinitely many passbands, narrowing as k*d increases | calc | §8.1 eq.(8.9a,b), p.383 | high |
| POZAR-247 | filter | Bloch impedance of a symmetric unit cell (A = D); real in passband, imaginary in stopband; terminate with ZL = ZB (or add lambda/4 transformer) to avoid reflections | ZB = ± B*Z0/sqrt(A^2 - 1); Gamma = (ZL - ZB)/(ZL + ZB) | A, B (normalized ABCD), Z0, ZL | periodic structures, slow-wave lines | calc | §8.1 eq.(8.12),(8.18), p.384–385 | high |
| POZAR-248 | transmission-line | Phase and group velocity from the k-beta (Brillouin) diagram | vp = omega/beta = c*k/beta (slope of line from origin); vg = d(omega)/d(beta) = c*dk/d(beta) (slope of curve); waveguide mode: vp -> infinity and vg -> 0 at cutoff | k, beta | dispersive structures | calc | §8.1 eq.(8.19)–(8.21), p.385–386 | high |
| POZAR-249 | filter | Worked capacitively loaded line (anchor) | Z0 = 50 ohm, d = 1.0 cm, C0 = 2.666 pF, f = 3.0 GHz: C0*Z0*c/(2d) = 2.0; first passband 0 <= k0d <= 0.96; k0d = 0.6283 (36 deg) -> beta*d = 1.5, beta = 150 rad/m; vp = 0.42c (slow wave); b = 1.256, A = 0.0707, B = j0.3479; ZB = 17.4 ohm | — | — | calc | §8.1 Ex.8.1, p.386–388 | high |
| POZAR-250 | filter | Image impedances and propagation factor of a reciprocal two-port | Zi1 = sqrt(A*B/(C*D)); Zi2 = sqrt(B*D/(A*C)); Zi2 = D*Zi1/A; e^(-gamma) = sqrt(A*D) - sqrt(B*C); cosh(gamma) = sqrt(A*D) | ABCD | symmetric network: Zi1 = Zi2 | calc | §8.2 eq.(8.27),(8.30),(8.31), p.389–390 | high |
| POZAR-251 | filter | Constant-k low-pass section: cutoff, nominal impedance and image impedance; stopband roll-off 40 dB/decade; attenuation low near cutoff | wc = 2/sqrt(L*C); R0 = sqrt(L/C); ZiT = R0*sqrt(1 - (w/wc)^2) | L, C | valid only when terminated in its (frequency-dependent) image impedance — the method's main weakness | calc | §8.2 eq.(8.32)–(8.36), p.390–392 | high |
| POZAR-252 | filter | Constant-k high-pass section | R0 = sqrt(L/C); wc = 1/(2*sqrt(L*C)) | L, C | image-parameter design | calc | §8.2 eq.(8.37),(8.38), p.392 | high |
| POZAR-253 | filter | m-derived section: attenuation pole beyond cutoff set by m; attenuation falls again above w_inf, so cascade with a constant-k section | Z1' = m*Z1; Z2' = Z2/m + (1-m^2)*Z1/(4m); LPF pole w_inf = wc/sqrt(1 - m^2) (series-LC resonance in shunt arm); 0 < m < 1 | m, wc | m = 1 reduces to constant-k | calc | §8.2 eq.(8.39)–(8.44), p.393–394 | high |
| POZAR-254 | filter | m-derived pi (bisected) matching end sections: m = 0.6 gives the flattest image impedance over the passband | Zipi = R0*(1 - (1-m^2)*(w/wc)^2)/sqrt(1 - (w/wc)^2); use m = 0.6 | m | use at both ends of a composite filter | calc | §8.2 eq.(8.46), Fig.8.16, p.395 | high |
| POZAR-255 | filter | Composite image-parameter filter structure: bisected-pi m = 0.6 matching section + constant-k T (deep stopband) + sharp-cutoff m-derived T (m < 0.6, pole near cutoff) + bisected-pi m = 0.6 matching section | LPF m_sharp = sqrt(1 - (fc/f_inf)^2); HPF m_sharp = sqrt(1 - (f_inf/fc)^2) | fc, f_inf, R0 | see Table 8.2 (§2 T2.6) | calc | §8.2 Fig.8.18, Table 8.2, p.396–397 | high |
| POZAR-256 | filter | Worked composite LPF (anchor): fc = 2 MHz, R0 = 75 ohm, f_inf = 2.05 MHz | constant-k: L = 11.94 uH, C = 2.122 nF; sharp section m = 0.2195: mL/2 = 1.310 uH, mC = 465.8 pF, (1-m^2)L/(4m) = 12.94 uH; m = 0.6 matching: mL/2 = 3.582 uH, mC/2 = 636.5 pF, (1-m^2)L/(2m) = 6.368 uH; series inductors between sections combined (5.97 uH) | — | \|S12\| dips at 2.05 MHz (m = 0.2195) and a pole at 2.50 MHz (m = 0.6 sections) (Fig.8.20) | sim | §8.2 Ex.8.2, Figs.8.19–8.20, p.398–399 | high |
| POZAR-257 | filter | Insertion-loss method: define response by the power loss ratio; realizable only if PLR has the form 1 + M(w^2)/N(w^2) | PLR = P_inc/P_load = 1/(1 - \|Gamma(w)\|^2) (= 1/\|S21\|^2 with matched source and load); IL(dB) = 10*log10(PLR) | Gamma(w) | lossless filter | calc | §8.3 eq.(8.49)–(8.52), p.399–400 | high |
| POZAR-258 | filter | Response-type selection: minimum passband insertion loss / flattest -> binomial (Butterworth); sharpest cutoff -> Chebyshev; minimum-attenuation stopband spec with best cutoff -> elliptic; phase linearity (e.g. multiplexers) -> linear-phase (worse attenuation). Performance improves with higher order N | — | spec priorities | lumped prototypes; N = number of reactive elements | review | §8.3 p.399, 401 | high |
| POZAR-259 | filter | Maximally flat (Butterworth) low-pass response; -3 dB at wc for k = 1; stopband roll-off 20N dB/decade; first (2N-1) derivatives zero at w = 0 | PLR = 1 + k^2*(w/wc)^(2N); k = 1 | N, wc | low-pass prototype | calc | §8.3 eq.(8.53), Fig.8.21, p.400 | high |
| POZAR-260 | filter | Equal-ripple (Chebyshev) low-pass response; passband ripple 1 + k^2; for w >> wc, PLR ≈ (k^2/4)*(2w/wc)^(2N): also 20N dB/decade, but (2^(2N))/4 times more loss than Butterworth of the same N | PLR = 1 + k^2*T_N^2(w/wc); k^2 = 10^(ripple_dB/10) - 1; T_N(x) = cos(N*acos x) for \|x\|<=1, cosh(N*acosh x) for \|x\|>1 | N, ripple, wc | low-pass prototype; PLR(0) = 1 for N odd, 1 + k^2 for N even | calc | §8.3 eq.(8.54),(8.61), p.400–401, 404 | high |
| POZAR-261 | filter | Elliptic-function filters: equal ripple in passband and stopband; specify A_max (passband) and A_min (stopband); best cutoff rate but difficult to synthesize (see ref [3]) | A_max, A_min | spec | when a minimum stopband attenuation suffices | review | §8.3 Fig.8.22, p.401 | high |
| POZAR-262 | filter | Linear-phase (maximally flat group delay) response | phi(w) = A*w*(1 + p*(w/wc)^(2N)); tau_d = d(phi)/d(w) = A*(1 + p*(2N+1)*(w/wc)^(2N)); prototype (Table 8.5) delay tau_d = 1/wc | N, A, p | sharp cutoff incompatible with good phase response | calc | §8.3 eq.(8.55),(8.56), Table 8.5, p.401, 408 | high |
| POZAR-263 | filter | N = 2 maximally flat prototype check value (1 ohm source, wc = 1 rad/s) | L = C = sqrt(2) = 1.4142, R = 1 | — | agrees with Table 8.3 | calc | §8.3 p.402–403 | high |
| POZAR-264 | filter | Chebyshev prototype with EVEN N has non-unity load resistance -> mismatch to a unity (Z0) load; correct with a lambda/4 transformer or add one element to make N odd (odd N gives R = 1) | R = 1 + 2k^2 ± 2k*sqrt(1 + k^2) (N even) | k^2, N | Table 8.4: g_{N+1} = 1.9841 (0.5 dB), 5.8095 (3.0 dB) for even N | calc | §8.3 eq.(8.63), p.405–406 | high |
| POZAR-265 | filter | Determine filter order from the required insertion loss at a stopband frequency using attenuation-vs-normalized-frequency curves (\|w/wc\| - 1); if N > 10 is required, cascade two lower-order designs | Figs.8.26 (maximally flat), 8.27a (0.5 dB ripple), 8.27b (3.0 dB ripple); or compute from POZAR-259/260 | IL_req (dB), w/wc | low-pass prototype domain (map BPF/HPF via transformations) | calc | §8.3 p.404, 406, Figs.8.26–8.27 | high |
| POZAR-266 | filter | Impedance scaling of a prototype to source resistance R0 | L' = R0*L; C' = C/R0; Rs' = R0; RL' = R0*RL | R0, prototype L, C, RL | all prototypes | calc | §8.4 eq.(8.64a–d), p.408 | high |
| POZAR-267 | filter | Low-pass frequency scaling of a prototype (with impedance scaling) | w <- w/wc; Lk' = R0*Lk/wc; Ck' = Ck/(R0*wc) | R0, wc, gk | prototype wc = 1 rad/s | calc | §8.4 eq.(8.65)–(8.67), p.409 | high |
| POZAR-268 | filter | Low-pass to high-pass transformation: each series L becomes a series C, each shunt C becomes a shunt L | w <- -wc/w; Ck' = 1/(R0*wc*Lk); Lk' = R0/(wc*Ck) | R0, wc, gk | ladder prototypes | calc | §8.4 eq.(8.68)–(8.70), p.410 | high |
| POZAR-269 | filter | Low-pass to bandpass transformation (geometric-mean center frequency) | w <- (1/Delta)*(w/w0 - w0/w); Delta = (w2 - w1)/w0; w0 = sqrt(w1*w2); series Lk -> series LC: L' = Lk/(w0*Delta), C' = Delta/(w0*Lk); shunt Ck -> parallel LC: L' = Delta/(w0*Ck), C' = Ck/(w0*Delta) (multiply L by R0, divide C by R0 for impedance scaling) | w1, w2, gk, R0 | all resonators tuned to w0 | calc | §8.4 eq.(8.71)–(8.74), Table 8.6, p.411–414 | high |
| POZAR-270 | filter | Low-pass to bandstop transformation | w <- -Delta*(w/w0 - w0/w)^(-1); series Lk -> parallel LC: L' = Lk*Delta/w0, C' = 1/(w0*Delta*Lk); shunt Ck -> series LC: L' = 1/(w0*Delta*Ck), C' = Ck*Delta/w0 | w1, w2, gk | Delta, w0 as for bandpass | calc | §8.4 eq.(8.75),(8.76), Table 8.6, p.413–414 | high |
| POZAR-271 | filter | Map any stopband frequency to the prototype (normalized low-pass) domain before choosing order N from the prototype attenuation curves | bandpass: w_n = (1/Delta)*\|w/w0 - w0/w\|; use \|w_n\| - 1 on the Fig.8.26/8.27 x-axis; high-pass: w_n = wc/w | f, f0, Delta | all transformed designs | calc | §8.4, Ex.8.7, 8.9, 8.10, p.435–436, 442, 446–447 | high |
| POZAR-272 | filter | Worked maximally flat LPF (anchor): fc = 2 GHz, 50 ohm, >= 15 dB at 3 GHz -> \|w/wc\| - 1 = 0.5 -> N = 5 (Fig.8.26) | g = 0.618, 1.618, 2.000, 1.618, 0.618; C1 = 0.984 pF, L2 = 6.438 nH, C3 = 3.183 pF, L4 = 6.438 nH, C5 = 0.984 pF | — | trade-off (Fig.8.30): equal-ripple sharpest cutoff but worst group delay; maximally flat flatter passband, slightly lower cutoff rate; linear phase worst cutoff, very good group delay | sim | §8.4 Ex.8.3, Figs.8.29–8.30, p.410–412 | high |
| POZAR-273 | filter | Worked lumped bandpass (anchor): 0.5 dB ripple, N = 3, f0 = 1 GHz, 10% BW, 50 ohm (Fig.8.25b ladder, series L first) | L1' = L3' = 127.0 nH, C1' = C3' = 0.199 pF (series resonators); L2' = 0.726 nH, C2' = 34.91 pF (shunt resonator) | — | note the extreme element spread (0.199 pF vs 34.91 pF) typical of narrow lumped BPFs | calc | §8.4 Ex.8.4, Figs.8.32–8.33, p.414–415 | high |
| POZAR-274 | filter | Richards' transformation: lumped L -> short-circuited stub of Z0 = L; lumped C -> open-circuited stub of Z0 = 1/C (normalized); all stubs lambda/8 at wc (commensurate lines) | Omega = tan(beta*l) = tan(w*l/vp); l = lambda/8 at wc; attenuation pole at 2wc (stubs lambda/4); response periodic, repeating every 4wc | gk, wc | distributed low-pass/bandstop; response departs from prototype away from wc | calc | §8.5 eq.(8.77),(8.78), Fig.8.34, p.416 | high |
| POZAR-275 | filter | Kuroda identities use redundant unit elements (UE, lambda/8 at wc) to separate stubs, convert series stubs to shunt stubs (and vice versa), and change impractical impedances | n^2 = 1 + Z2/Z1. (a) shunt OC stub Z2 then UE Z1 == UE Z2/n^2 then series SC stub Z1/n^2. (b) UE Z2 then series SC stub Z1 == shunt OC stub n^2*Z1 then UE n^2*Z2 (as applied in Ex.8.5). (c),(d) are the transformer (1:n^2, n^2:1) forms in Table 8.7 (element labels garbled in OCR) | Z1, Z2 | UEs added at a matched port do not change the response; Kuroda identities are NOT useful for high-pass or bandpass filters (use for low-pass/bandstop) | calc | §8.5 Table 8.7, Fig.8.35, eq.(8.79)–(8.80), p.416–421 | high (a,b) / low (c,d) |
| POZAR-276 | filter | Worked stub LPF (anchor): 4 GHz, 50 ohm, N = 3, 3 dB equal ripple, microstrip, all lines lambda/8 at 4 GHz | prototype g = 3.3487, 0.7117, 3.3487, 1.0000; Richards: series stubs Z = 3.3487, shunt stub Z = 1.405; Kuroda (b) with n^2 = 1 + 1/3.3487 = 1.299 -> final: shunt OC stub 217.5 ohm, UE 64.9 ohm, shunt OC stub 70.3 ohm, UE 64.9 ohm, shunt OC stub 217.5 ohm | — | distributed version: similar passband up to 4 GHz, sharper cutoff than lumped, response repeats every 16 GHz (Fig.8.37) | sim | §8.5 Ex.8.5, Figs.8.36–8.37, p.419–421 | high |
| POZAR-277 | filter | Impedance (K) and admittance (J) inverters: convert series elements to shunt (and vice versa); especially useful for narrow (< 10%) bandpass/bandstop filters | Zin = K^2/ZL; Yin = J^2/YL; lambda/4 line of Z0 = K (or Y0 = J); line+reactance form: K = Z0*tan\|theta/2\|, X = K/(1 - (K/Z0)^2), theta = -atan(2X/Z0); J = Y0*tan\|theta/2\|, B = J/(1 - (J/Y0)^2), theta = -atan(2B/Y0); capacitor pi/T networks: K = 1/(w*C), J = w*C (with -C elements) | K or J | negative line lengths are absorbed into adjacent lines | calc | §8.5 Fig.8.38, p.421–422 | high |
| POZAR-278 | filter | Stepped-impedance (hi-Z/lo-Z) LPF: series L -> short high-impedance line, shunt C -> short low-impedance line; make Zh/Zl as large as practical (highest/lowest fabricable impedances); evaluate lengths at wc | beta*l = L*R0/Zh (inductor); beta*l = C*Zl/R0 (capacitor); L, C = prototype gk; valid for short lines (beta*l < pi/4); exact T-model: X/2 = Z0*tan(beta*l/2), B = sin(beta*l)/Z0 | gk, R0, Zh, Zl | compact but electrically inferior: use where a sharp cutoff is not required (e.g. rejecting out-of-band mixer products); lines not commensurate -> spurious passbands not exactly periodic | calc | §8.6 eq.(8.81)–(8.86), p.422–424 | high |
| POZAR-279 | filter | Worked stepped-impedance LPF (anchor): maximally flat, fc = 2.5 GHz, > 20 dB at 4 GHz (\|w/wc\| - 1 = 0.6 -> N = 6 from Fig.8.26), R0 = 50, Zh = 120, Zl = 20 ohm, microstrip d = 0.158 cm, er = 4.2, tan_delta = 0.02, 0.5 mil Cu | sections (Z, beta*l deg, W mm, l mm): 1 (20, 11.8, 11.3, 2.05); 2 (120, 33.8, 0.428, 6.63); 3 (20, 44.3, 11.3, 7.69); 4 (120, 46.1, 0.428, 9.04); 5 (20, 32.4, 11.3, 5.63); 6 (120, 12.3, 0.428, 2.41) | — | losses raise passband attenuation to about 1 dB at 2 GHz; lumped version gives more attenuation at high frequency (Fig.8.41) | sim | §8.6 Ex.8.6, Figs.8.40–8.41, p.424–426 | high |
| POZAR-280 | filter | Parallel coupled-line bandpass/bandstop filters are easy in microstrip/stripline for bandwidths below about 20%; wider bandwidths need very tightly coupled lines that are difficult to fabricate | BW_frac < ~0.20 | Delta | coupled-line filters | review | §8.7 p.426 | high |
| POZAR-281 | filter | Open-circuit Z-matrix of a coupled-line section (length theta) | Z11 = Z22 = Z33 = Z44 = -(j/2)*(Z0e + Z0o)*cot(theta); Z12 = Z21 = Z34 = Z43 = -(j/2)*(Z0e - Z0o)*cot(theta); Z13 = Z31 = Z24 = Z42 = -(j/2)*(Z0e - Z0o)*csc(theta); Z14 = Z41 = Z23 = Z32 = -(j/2)*(Z0e + Z0o)*csc(theta) | Z0e, Z0o, theta | 10 canonical 2-port terminations (Table 8.8) give low-pass, bandpass, all-pass, all-stop responses; OC-terminated bandpass form preferred in microstrip (open circuits easier than shorts) | calc | §8.7 eq.(8.99), Table 8.8, p.428–429 | high |
| POZAR-282 | filter | Bandpass coupled-line section (ports 2,4 open) image impedance and passband edges | Zi = 0.5*sqrt((Z0e - Z0o)^2*csc^2(theta) - (Z0e + Z0o)^2*cot^2(theta)); at theta = pi/2: Zi = (Z0e - Z0o)/2; passband theta1 < theta < pi - theta1 with cos(theta1) = (Z0e - Z0o)/(Z0e + Z0o); cos(beta) = ((Z0e + Z0o)/(Z0e - Z0o))*cos(theta) | Z0e, Z0o | single lambda/4 section | calc | §8.7 eq.(8.101)–(8.103), Fig.8.43, p.430 | high |
| POZAR-283 | filter | Coupled-line section as admittance inverter J between two theta-long Z0 lines: even/odd impedances from J | Z0e = Z0*(1 + J*Z0 + (J*Z0)^2); Z0o = Z0*(1 - J*Z0 + (J*Z0)^2) | J, Z0 | near theta = pi/2 (sin theta ≈ 1) | calc | §8.7 eq.(8.108a,b), p.431 | high |
| POZAR-284 | filter | Coupled-line bandpass filter (N+1 sections, lambda/4 each at f0) inverter constants from prototype g-values | Z0*J1 = sqrt(pi*Delta/(2*g1)); Z0*Jn = pi*Delta/(2*sqrt(g(n-1)*g(n))) for n = 2..N; Z0*J(N+1) = sqrt(pi*Delta/(2*gN*g(N+1))); then Z0e, Z0o per POZAR-283 | gk, Delta, Z0 | narrowband; valid also for g(N+1) != 1 (even-N Chebyshev); spurious passbands at 3f0, 5f0, ... | calc | §8.7 eq.(8.121a–c), p.435 | high |
| POZAR-285 | filter | lambda/2 line between inverters behaves as a shunt parallel LC resonator near f0 | L = 2*Z0/(pi*w0); C = pi/(2*Z0*w0) | Z0, w0 | narrowband equivalence | calc | §8.7 eq.(8.114a,b), p.433 | high |
| POZAR-286 | filter | Worked coupled-line BPF (anchor): N = 3, 0.5 dB ripple, f0 = 2.0 GHz, 10% BW, Z0 = 50 | n: g, Z0*J, Z0e, Z0o = 1: 1.5963, 0.3137, 70.61, 39.24; 2: 1.0967, 0.1187, 56.64, 44.77; 3: 1.5963, 0.1187, 56.64, 44.77; 4: 1.0000, 0.3137, 70.61, 39.24 ohm; attenuation at 1.8 GHz ≈ 20 dB (normalized -2.11, \|w\|-1 = 1.11) | — | symmetric about midpoint; passbands also at 6, 10 GHz ... (Fig.8.46) | sim | §8.7 Ex.8.7, Fig.8.46, p.435–436 | high |
| POZAR-287 | filter | Interdigitated filter = coupled-line filter folded at the line midpoints (compact) | — | — | see Matthaei [1], Malherbe [3] | review | §8.7 p.436 | high |
| POZAR-288 | filter | Quarter-wave shunt-stub filters: lambda/4 OC stubs -> bandstop, lambda/4 SC stubs -> bandpass, spaced by lambda/4 Z0 lines (inverters); N stubs ≈ (N+1)-section coupled-line filter for narrow BW; more compact but may require impedances hard to realize | bandstop (OC stubs): Z0n = 4*Z0/(pi*gn*Delta); bandpass (SC stubs): Z0n = pi*Z0*Delta/(4*gn) | gn, Delta, Z0 | input/output impedance Z0 only -> NOT for even-N equal-ripple designs; making interconnecting-line impedances variable gives an exact correspondence with coupled-line filters (ref.[1]) | calc | §8.8 eq.(8.130),(8.131), Fig.8.47, p.437–440 | high |
| POZAR-289 | filter | Worked stub bandstop (anchor): 3 OC stubs, f0 = 2.0 GHz, 15% BW, 50 ohm, 0.5 dB ripple | Z01 = Z03 = 265.9 ohm, Z02 = 387.0 ohm; stubs and lines lambda/4 at 2.0 GHz | — | realized passband ripple somewhat > 0.5 dB due to design approximations (Fig.8.49); note 387 ohm is not realizable in ordinary microstrip | sim | §8.8 Ex.8.8, Fig.8.49, p.440 | high |
| POZAR-290 | filter | Capacitive-gap coupled series-resonator BPF: N resonators ≈ lambda/2 at f0 with N+1 series gap capacitors | Ji from POZAR-284; Bi = Ji/(1 - (Z0*Ji)^2); Ci = Bi/w0; phi_i = -atan(2*Z0*Bi); resonator length theta_i = pi - 0.5*(atan(2*Z0*Bi) + atan(2*Z0*B(i+1))) rad | gk, Delta, Z0, w0 | gap capacitance vs geometry from ref.[1] graphs | calc | §8.8 eq.(8.132)–(8.135), p.441–442 | high |
| POZAR-291 | filter | Worked gap-coupled BPF (anchor): 0.5 dB ripple, f0 = 2.0 GHz, 10% BW, 50 ohm, >= 20 dB at 2.2 GHz (normalized 1.91, \|w\|-1 = 0.91 -> N = 3 per Fig.8.27a) | n: Z0*J, B (S), C (pF), theta (deg) = 1: 0.3137, 6.96e-3, 0.554, 155.8; 2: 0.1187, 2.41e-3, 0.192, 166.5; 3: 0.1187, 2.41e-3, 0.192, 155.8; 4: 0.3137, 6.96e-3, 0.554, — | — | response identical to the coupled-line filter near the passband (Fig.8.51 vs 8.46); CAUTION: exact Chebyshev formula gives only 17.8 dB at normalized 1.91 for N = 3 (computed, see CHECK-FILTER-ORDER) | sim | §8.8 Ex.8.9, Fig.8.51, p.442–443 | high (values) / medium (caution) |
| POZAR-292 | filter | Capacitively coupled shunt SC-stub (ceramic/combline-type) BPF inverter constants and coupling capacitors | Z0*J01 = sqrt(pi*Delta/(4*g1)); Z0*J(n,n+1) = pi*Delta/(4*sqrt(gn*g(n+1))); Z0*J(N,N+1) = sqrt(pi*Delta/(4*gN*g(N+1))); C01 = J01/(w0*sqrt(1 - (Z0*J01)^2)); C(n,n+1) = J(n,n+1)/w0; C(N,N+1) = J(N,N+1)/(w0*sqrt(1 - (Z0*J(N,N+1))^2)) | gk, Delta, Z0, w0 | end capacitors treated differently from internal ones | calc | §8.8 eq.(8.136),(8.137), p.444 | high |
| POZAR-293 | filter | Shunt-stub resonators are shortened below lambda/4 by the negative inverter capacitances | dC_n = -C(n-1,n) - C(n,n+1); dl = Z0*w0*dC*lambda/(2*pi); l_n = lambda/4 + Z0*w0*dC_n*lambda/(2*pi); stub impedance Z0 | C couplings, Z0, w0 | beta*dl << 1 | calc | §8.8 eq.(8.138)–(8.141), p.444–446 | high |
| POZAR-294 | filter | Worked shunt-stub BPF (anchor): N = 3, 0.5 dB, f0 = 2.5 GHz, 10% BW, 50 ohm | Z0*J01 = Z0*J34 = 0.2218 (C = 0.2896 pF); Z0*J12 = Z0*J23 = 0.0594 (C = 0.0756 pF); dC1 = dC3 = -0.3652 pF (dl = -0.04565 lambda, l = 73.6 deg); dC2 = -0.1512 pF (dl = -0.0189 lambda, l = 83.2 deg) | — | canonical lumped estimate 35 dB at 3.0 GHz (normalized 3.667) but realized ≈ 30 dB: high-side roll-off of this topology is weaker than low-side (Fig.8.54) | sim | §8.8 Ex.8.10, Fig.8.54, p.446–447 | high |
| POZAR-295 | materials | Ceramic resonator filter dielectric requirements: high er (miniaturization), low loss (high Q -> low passband IL, deep stopband), and low temperature coefficient of er (no passband drift). Example: zinc/strontium titanate er = 36, Q = 10,000 at 4 GHz, TC(er) = -7 ppm/degC | er, Q, TC(er) | material selection | UHF–microwave wireless BPFs (cellular, GPS use two or more) | review | §8.8 p.443–446 | high |
| POZAR-296 | filter | Anchor for high-order distributed LPF feasibility: 21-pole microstrip stub LPF, fc = 5.4 GHz, > 75 dB rejection from 5.8 to 9.0 GHz (commercial downconverter) | N = 21; rejection 75 dB at 1.07–1.67 fc | — | industrial example | review | §8.8 Fig.8.55, p.448 | high |
| POZAR-297 | magnetics | Ferrite gyromagnetic (Larmor) frequency and magnetization frequency in practical CGS units | f0 = (2.8 MHz/Oe)*H0 (Oe); fm = (2.8 MHz/Oe)*(4*pi*Ms in G); 1 G = 1e-4 Wb/m^2; 4*pi*1e-3 Oe = 1 A/m; mu0*Ms (Wb/m^2) = 1e-4*(4*pi*Ms in G) | H0, 4piMs | saturated ferrite, g ≈ 2 (microwave ferrites g = 1.98–2.01) | calc | §9.1 p.452, 457–458 | high |
| POZAR-298 | magnetics | Operate microwave ferrites magnetically saturated: below saturation they are very lossy and RF interaction is reduced; Ms falls with temperature (zero at Curie temperature Tc) | 4*pi*Ms typically 300–5000 G | temperature range | isolators, circulators, phase shifters | review | §9.1 p.455 | high |
| POZAR-299 | magnetics | Saturated ferrite permeability tensor (z bias) and circular-polarization permeabilities; reversing bias flips the sign of kappa (nonreciprocity) | mu = mu0*(1 + w0*wm/(w0^2 - w^2)); kappa = mu0*w*wm/(w0^2 - w^2); mu_RHCP = mu + kappa = mu0*(1 + wm/(w0 - w)); mu_LHCP = mu - kappa = mu0*(1 + wm/(w0 + w)); w0 = mu0*gamma*H0, wm = mu0*gamma*Ms, gamma = 1.759e11 C/kg | H0, Ms, f | small-signal, lossless; RHCP stopband for w0 < w < w0 + wm | calc | §9.1 eq.(9.25),(9.30),(9.35), p.457–459 | high |
| POZAR-300 | magnetics | Ferrite magnetic loss via linewidth; include loss by w0 -> w0 + j*alpha*w | dH = 2*alpha*w/(mu0*gamma); typical dH < 100 Oe (YIG), 100–500 Oe (ferrites), as low as 0.3 Oe (single-crystal YIG); in CGS: f0 -> f0 + j*(2.8 MHz/Oe)*dH/2 | dH | separate from the material's dielectric loss | calc | §9.1 eq.(9.37),(9.40), p.460–462; Ex.9.1 p.468 | high |
| POZAR-301 | magnetics | Internal bias field differs from applied field by demagnetization; resonance of a finite sample from Kittel's equation | H_int = H_applied - N*M; Nx + Ny + Nz = 1; thin disk/plate (z normal): N = (0, 0, 1); thin rod along z: N = (1/2, 1/2, 0); sphere: (1/3, 1/3, 1/3); normal-biased thin plate: H0 = Ha - Ms; tangential: H0 = Ha; w_r = mu0*gamma*sqrt((Ha + (Nx - Nz)*Ms)*(Ha + (Ny - Nz)*Ms)) | Ha, Ms, shape | ferrite parts in magnetic circuits (YIG tuners, isolators) | calc | §9.1 eq.(9.41),(9.46), Table 9.1, p.462–464 | high |
| POZAR-302 | magnetics | Faraday rotation of a linearly polarized wave along the bias direction (nonreciprocal: does not unwind on the return trip; round trip gives 2*phi) | phi = -(beta+ - beta-)*z/2; beta± = w*sqrt(eps*(mu ± kappa)) | beta±, z | propagation along bias | calc | §9.2 eq.(9.52),(9.57), p.466–467 | high |
| POZAR-303 | magnetics | Transverse bias (birefringence): ordinary wave unaffected; extraordinary wave uses mu_e, which is negative (cutoff, total reflection) over some bias range | beta_o = w*sqrt(mu0*eps); beta_e = w*sqrt(mu_e*eps); mu_e = (mu^2 - kappa^2)/mu | mu, kappa | graph Fig.9.8 of mu_e vs H0 | calc | §9.2 eq.(9.61)–(9.67), Fig.9.8, p.469–471 | high |
| POZAR-304 | components | Ideal isolator S = [[0,0],[1,0]]: matched, non-unitary (must be lossy), nonreciprocal; placed between a high-power source and load to protect the source, it absorbs (rather than re-reflects) power reflected by the load -> its internal load must be rated for the reflected power | P_absorbed = \|Gamma_L\|^2 * P_fwd | P_fwd, Gamma_L | source protection; not a substitute for a matching network if efficiency matters | review | §9.4 eq.(9.85), p.475–476 | high (rating note low) |
| POZAR-305 | components | Resonance isolator: E-plane full-height slab has no truly circularly polarized position -> nonzero forward loss, bandwidth set by ferrite linewidth dH (narrow), poor heat removal (Ms drifts with temperature) -> not for high power; H-plane slab on the wall at the circular-polarization point has better thermal behaviour | CP point of empty guide: tan(kc*x) = ± kc/beta0; E-plane slab resonance w = sqrt(w0*(w0 + wm)) | dH, geometry | waveguide ferrite isolators | review | §9.4 eq.(9.86),(9.87), p.476–479 | high |
| POZAR-306 | components | Worked E-plane resonance isolator (anchor): 10 GHz, WR-90, 0.5 mm slab, 4piMs = 1700 G, dH = 200 Oe, er = 13 | H0 ≈ 2820 Oe from (9.87), 2840 Oe numerically; min forward loss at c/a = 0.125 with alpha- = 12.4 dB/cm; 30 dB isolation -> L = 2.4 cm; >= 27 dB isolation bandwidth < 2% | — | wider BW needs a larger-linewidth ferrite, costing a longer/thicker slab and higher forward loss | calc | §9.4 Ex.9.2, Fig.9.12, p.478–479 | high |
| POZAR-307 | components | Field-displacement isolator: ~10% bandwidth, compact, needs a much smaller bias field (operates well below resonance, requires mu_e < 0); slab t ≈ a/10; resistive sheet ≈ 75 ohm/square typical at the forward-wave field null | ka+ = pi/d; beta+ < k0 < beta-; anchor 11 GHz, 4piMs = 3000 G, er = 13, H0 = 1200 Oe, t = 0.25 cm, c/a = 0.028, beta+ = 0.724k0, beta- = 1.607k0 | — | waveguide | calc | §9.4 eq.(9.88), Ex.9.3, Fig.9.14, p.479–482 | high |
| POZAR-308 | components | Latching (remanent) ferrite phase shifter: digital states ±Mr, bias current only pulsed, switching speed a few microseconds; binary sections 180, 90, 45 deg ...; differential phase proportional to kappa (≈ Mr) up to kappa/mu0 ≈ 0.5; figure of merit = phase shift / insertion loss (deg/dB) | remanent state: mu = mu0, kappa = -mu0*wm/w; anchor: 10 GHz, 4piMr = 1786 G, er = 13, slab spacing 1 mm: kappa/mu0 = ±0.5, t/a = 0.12 (t = 2.74 mm), (beta+ - beta-) = 0.4k0 = 0.836 rad/cm = 48 deg/cm -> 180 deg: 3.75 cm, 90 deg: 1.88 cm | Mr, f | phased arrays | calc | §9.5 eq.(9.89), Ex.9.4, Fig.9.17, p.482–485 | high |
| POZAR-309 | components | Perturbation formula for ferrite differential phase shift is accurate only for very small ferrite fill | (beta+ - beta-) ≈ 2*kc*(kappa/mu)*(dS/S)*sin(2*kc*c); valid for dS/S < 0.01 | dS/S | small strips/rods | calc | §9.3 eq.(9.80), p.474 | high |
| POZAR-310 | components | Circulator facts: ideal S = [[0,0,1],[1,0,0],[0,1,0]]; reverse circulation by reversing bias; one port terminated in a matched load makes an isolator; electromagnet-biased latching circulator = SPDT switch | — | — | stripline/microstrip junction circulators | review | §9.6 eq.(9.91), p.487 | high |
| POZAR-311 | components | Mismatched lossless circulator: isolation and transmission both degrade with port mismatch — isolation magnitude ≈ port reflection magnitude | \|S_isolation\| ≈ \|Gamma\|; \|S_transmission\| ≈ sqrt(1 - \|Gamma\|^2) -> Isolation(dB) ≈ Return loss(dB) | Gamma (or RL) | small imperfection, circularly symmetric, lossless | calc | §9.6 eq.(9.92)–(9.94), p.488 (cf. Problem 9.20) | high |
| POZAR-312 | components | Stripline junction circulator: operating frequency = unbiased disk resonance; bias splits it into w± straddling w0; narrowband unless dielectric-loaded | w0 = 1.841/(a*sqrt(mu0*eps)) (disk radius a); w± ≈ w0*(1 ± 0.418*kappa/mu); port wave impedance Zw ≈ mu*sin(psi)/(kappa*Y), tuned by bias (kappa/mu) | a, eps, kappa/mu | ferrite disks in stripline | calc | §9.6 eq.(9.101)–(9.110), p.490–492 | high |
| POZAR-313 | noise | Available thermal noise power of a resistor (Rayleigh–Jeans) and its validity | Pn = k*T*B; Vn(rms) = sqrt(4*k*T*B*R); k = 1.380e-23 J/K; valid when h*f << k*T (e.g. 100 GHz, 100 K: hf = 6.6e-23 J << kT = 1.4e-21 J); otherwise Vn = sqrt(4*h*f*B*R/(exp(h*f/(k*T)) - 1)), h = 6.626e-34 J*s | T (K), B (Hz), R | white noise; independent noise powers add | calc | §10.1 eq.(10.1)–(10.3), p.498–499 | high |
| POZAR-314 | noise | Equivalent noise temperature of a white noise source / amplifier | Te = No/(k*B) (source); amplifier: Te = No/(G*k*B) with 0 K source, i.e. No = G*k*Te*B | No, G, B | noise flat over the bandwidth | calc | §10.1 eq.(10.4),(10.5), p.500 | high |
| POZAR-315 | test | Noise source excess noise ratio; solid-state noise generators typically ENR = 20–40 dB | ENR(dB) = 10*log10((Tg - T0)/T0), T0 = 290 K | Tg | noise-figure measurement | calc | §10.1 eq.(10.6), p.501 | high |
| POZAR-316 | test | Y-factor noise-temperature measurement; hot and cold loads must be well separated (Y close to 1 loses accuracy); cold = liquid N2 (77 K) or He (4 K), hot = active noise source, one load usually at 290 K | Y = N1/N2 = (T1 + Te)/(T2 + Te) > 1; Te = (T1 - Y*T2)/(Y - 1) | T1 > T2, measured N1, N2 | matched loads | measure | §10.1 eq.(10.7)–(10.9), p.501–502 | high |
| POZAR-317 | test | Worked Y-factor (anchor): X-band amp G = 20 dB, B = 1 GHz, N1 = -62.0 dBm at 290 K, N2 = -64.7 dBm at 77 K | Y = 2.7 dB = 1.86; Te = 170 K; with a 450 K source: No = G*k*B*(Ts + Te) = 8.56e-10 W = -60.7 dBm | — | — | calc | §10.1 Ex.10.1, p.502 | high |
| POZAR-318 | noise | Noise figure definition and conversion to noise temperature; defined for a MATCHED source at T0 = 290 K | F = (Si/Ni)/(So/No) >= 1 with Ni = k*T0*B; F = 1 + Te/T0; Te = (F - 1)*T0; NF(dB) = 10*log10(F) | Te or F | interchangeable characterizations | calc | §10.2 eq.(10.10)–(10.12), p.502–503 | high |
| POZAR-319 | noise | Matched lossy line / attenuator at physical temperature T: noise temperature and noise figure; at T0 the noise figure equals the loss (6 dB pad -> 6 dB NF) | Te = (L - 1)*T; F = 1 + (L - 1)*T/T0; F = L at T = T0; L = 1/G | L, T | matched | calc | §10.2 eq.(10.13)–(10.16), p.503–504 | high |
| POZAR-320 | noise | Cascade (Friis) noise formula: system noise is dominated by the first stage, so the first stage needs low NF and at least moderate gain; spend effort there | Tcas = Te1 + Te2/G1 + Te3/(G1*G2) + ...; Fcas = F1 + (F2 - 1)/G1 + (F3 - 1)/(G1*G2) + ... (linear ratios, not dB) | Fi (or Tei), Gi | matched stages | calc | §10.2 eq.(10.20)–(10.23), p.504–505 | high |
| POZAR-321 | noise | Worked receiver front-end (anchor): LNA G = 10 dB, F = 2 dB; BPF L = 1 dB; mixer Lc = 3 dB, F = 4 dB; T0 system, 50 ohm, B = 10 MHz, TA = 150 K | Fcas = 1.80 (2.55 dB); Te = 232 K; G = 3.95; No = k*(TA + Te)*B*G = 2.08e-13 W = -96.8 dBm; SNR_out = 20 dB -> Si = 5.27e-12 W = -82.8 dBm -> 16.2 uV rms at the input | — | — | calc | §10.2 Ex.10.2, Fig.10.10, p.505–506 | high |
| POZAR-322 | noise | When the source (antenna) temperature TA != T0, compute absolute output noise with temperatures, No = k*(TA + Te)*B*G — NOT No = k*TA*B*F*G (common error; gives 1.47e-13 W instead of 2.08e-13 W in Ex.10.2) | No = k*(TA + Te)*B*G | TA, Te, B, G | receiver sensitivity calcs | calc | §10.2 Ex.10.2 note, p.506 | high |
| POZAR-323 | noise | Noise temperature / figure of a general passive two-port (possibly mismatched) at physical temperature T uses the AVAILABLE gain | G21 = \|S21\|^2*(1 - \|Gs\|^2)/(\|1 - S11*Gs\|^2*(1 - \|Gout\|^2)); Gout = S22 + S12*S21*Gs/(1 - S11*Gs); Te = (1 - G21)*T/G21; F = 1 + (1 - G21)*T/(G21*T0) | S-params, Gs, T | passive networks only (no diodes/transistors) | calc | §10.2 eq.(10.24)–(10.29), p.506–508 | high |
| POZAR-324 | noise | Mismatched lossy line: input mismatch raises noise temperature above (L-1)T; impedance matching minimizes noise | G21 = L*(1 - \|Gs\|^2)/(L^2 - \|Gs\|^2); Te = (L - 1)*(L + \|Gs\|^2)*T/(L*(1 - \|Gs\|^2)) | L, Gs, T | reduces to (L-1)T for Gs = 0; 0 for L = 1 | calc | §10.2 eq.(10.30)–(10.33), p.508–509 | high |
| POZAR-325 | noise | Wilkinson divider used as a 2-port (one output matched-terminated): the isolation resistor adds noise | F = 1 + (2L - 1)*T/T0; = 2L at T0; lossless at room temperature: F = 2 (3 dB) | L (dissipative loss, excluding the 3 dB split), T | matched | calc | §10.2 Ex.10.3, p.509–510 | high |
| POZAR-326 | noise | Input mismatch degrades amplifier noise figure; good NF requires good input match | Fm = 1 + (F - 1)/(1 - \|Gamma\|^2) | F (matched), Gamma_in | output matched; more complex if output also mismatched and amp not unilateral | calc | §10.2 eq.(10.34)–(10.36), p.510–511 | high |
| POZAR-327 | noise | Practical receiver/component noise floors are -80 to -140 dBm over the system bandwidth (lowest with cooled components); dynamic range is bounded below by the noise floor and above by compression/failure | noise floor -80..-140 dBm | B, NF | orientation value | review | §10.1 Fig.10.1, p.497 | high |
| POZAR-328 | rf | Weakly nonlinear model and gain compression: a3 typically opposes a1 so gain drops with drive | vo = a0 + a1*vi + a2*vi^2 + a3*vi^3; Gv(w0) = a1 + (3/4)*a3*V0^2 | a1, a3, V0 | memoryless polynomial model | calc | §10.3 eq.(10.37)–(10.41), p.512 | high |
| POZAR-329 | rf | 1 dB compression point: output 1 dB below the linear extrapolation; amplifiers specify OP1dB (output), mixers IP1dB (input) | OP1dB = IP1dB + G - 1 dB | IP1dB or OP1dB, G | same reference plane conversions | calc | §10.3 Fig.10.15, p.513 | high |
| POZAR-330 | rf | Two-tone intermodulation products and their placement: products at m*w1 + n*w2, order \|m\|+\|n\|; 2nd-order and 3w, 2w1+w2 etc. fall far away (filterable); 2w1 - w2 and 2w2 - w1 fall in-band next to the tones (cannot be filtered) | f_IM3 = 2f1 - f2, 2f2 - f1; 2nd harmonic power 6 dB below the sum/difference products; 3rd harmonic power 9.54 dB below the IM3 products (single-device polynomial) | f1, f2 | closely spaced tones | calc | §10.3 eq.(10.43),(10.44), Fig.10.16, p.513–515 | high |
| POZAR-331 | rf | Third-order intercept: IM3 output rises 3 dB per 1 dB of input; OIP3 = G*IIP3; amplifiers usually specify OIP3, mixers IIP3; rule of thumb IP3 ≈ P1dB + 10..15 dB (same reference) | P_IM3 = P_fund^3/OIP3^2 (W), i.e. P_IM3(dBm) = 3*P_fund(dBm) - 2*OIP3(dBm); V_IP = sqrt(4*a1/(3*a3)); OIP3 = 2*a1^3/(3*a3) | P_fund, OIP3 | extrapolated from low-level data | calc | §10.3 eq.(10.45)–(10.49), Fig.10.17, p.515–517 | high |
| POZAR-332 | rf | Cascade third-order intercept (output-referred); coherent (worst case, in-phase voltage addition) and non-coherent (power addition) forms; the cascade IP3 is below the smallest individual IP3 | coherent: 1/OIP3 = 1/(G2*OIP3_1) + 1/OIP3_2; non-coherent: OIP3 = (1/(G2*OIP3_1)^2 + 1/OIP3_2^2)^(-1/2) (linear W) | OIP3_i, G2 | extend stage by stage; use coherent for design margin | calc | §10.3 eq.(10.50)–(10.54), p.516–518 | high |
| POZAR-333 | rf | Worked cascade IP3 (anchor): LNA G = 20 dB, OIP3 = 22 dBm (158 mW); mixer conversion loss 6 dB, IIP3 = 13 dBm -> OIP3 = 7 dBm (5 mW), G2 = 0.25 | coherent OIP3 = 4.4 mW = 6.4 dBm; non-coherent 4.96 mW = 6.9 dBm | — | — | calc | §10.3 Ex.10.4, p.518 | high |
| POZAR-334 | rf | Passive intermodulation (PIM) from metal-to-metal contacts: poor mechanical contact, oxidized ferrous junctions, contaminated RF surfaces, nonlinear materials (carbon-fibre composites, ferromagnetics), thermal effects at high power; cannot be predicted — measure it; matters in transmitters (base stations 30–40 dBm), not receivers | typical target PIM < -125 dBm with two 40 dBm carriers | Tx power, connectors, cables, antenna hardware | outdoor hardware needs maintenance (oxidation, vibration, sunlight) | measure | §10.3 p.519 | high |
| POZAR-335 | rf | Linear dynamic range (noise floor to compression) and spurious-free dynamic range (noise floor to IM3 = noise) | LDR(dB) = OP1dB - No; SFDR(dB) = (2/3)*(OIP3 - No); with a required output SNR: SFDR(dB) = (2/3)*(OIP3 - No) - SNR (all dBm/dB, output-referred) | OP1dB, OIP3, No, SNR | components or receivers | calc | §10.4 eq.(10.55)–(10.60), Fig.10.20, p.519–520 | high |
| POZAR-336 | rf | Worked dynamic range (anchor): F = 7 dB, OP1dB = 25 dBm, G = 40 dB, OIP3 = 35 dBm, TA = 150 K, SNR = 10 dB, B = 100 MHz | No = G*k*B*(TA + (F-1)*T0) = 1.8e-8 W = -47.4 dBm; LDR = 72.4 dB; SFDR = 44.9 dB (SFDR << LDR) | — | — | calc | §10.4 Ex.10.5, p.521 | high |
| POZAR-337 | test | Extracting IP3 from a two-tone spectrum: with dP = P_fund - P_IM3 (dB) at the output | OIP3 = P_fund + dP/2 (dBm); also (OIP3 - P_fund,out) = (IIP3 - P_fund,in) and (OIP3 - P_IM3,out) = 3*(IIP3 - P_IM3,in) in dB | measured P_fund, P_IM3 | measure well below IP3 (slope-1/slope-3 region) | measure | §10 Problems 10.12–10.13 (stated relations), p.523 | medium |
| POZAR-338 | components | Junction (Schottky) diode small-signal model: I = Is*(exp(alpha*V) - 1), alpha = q/(n*k*T) ≈ 1/(25 mV) at 290 K; Is typically 1e-6 to 1e-15 A; ideality n ≈ 1.05 (Schottky) to ≈ 2.0 (point-contact Si); junction resistance from bias current | Gd = 1/Rj = alpha*(I0 + Is); Gd' = alpha*Gd; i = v*Gd + (v^2/2)*Gd' | I0, Is, n, T | small-signal; package adds Ls, Cp; Rs, Cj bias dependent (Fig.11.3) | calc | §11.1 eq.(11.1)–(11.6), p.525–527 | high |
| POZAR-339 | components | Diode detector current and voltage sensitivity; typical RF detector voltage sensitivity 400–1500 mV/mW | beta_i = Gd'/(2*Gd) = alpha/2 (A/W); beta_v = beta_i*Rj (V/W) | alpha, I0 (sets Rj) | small signal, open-circuit output; zero-bias raises Rj (and beta_v) | calc | §11.1 eq.(11.9),(11.10), p.528 | high |
| POZAR-340 | components | Diode detectors are square law (output ∝ input power) only over a restricted input range: noise floor at the bottom, saturation (then linear, then constant) at the top; power-indicating uses (SWR meters, level indicators) must stay in the square-law region; DC bias can optimize sensitivity | v_out ∝ P_in in square-law region (Fig.11.5 spans roughly -40..+40 dBm axis; graph) | P_in range | AM detection output at wm has amplitude m*v0^2*Gd'/2 | measure | §11.1 Fig.11.5, Table 11.2, p.528–529 | medium (graph) |
| POZAR-341 | components | PIN diode switch bias and speed: forward bias 10–30 mA (low-Z state), reverse bias 10–60 V (high-Z, Cj), parasitic Li < 1 nH; bias through RF chokes (or high-Z lambda/4 lines) and DC blocks; switching 1–10 us typical, ~20 ns with careful driver design | I_F = 10–30 mA; V_R = 10–60 V | diode datasheet | series switch ON when forward biased; shunt switch ON when reverse biased; OFF state reflects the input power | review | §11.1 p.530–531 | high |
| POZAR-342 | components | PIN SPST switch insertion loss (ON and OFF states) | series: IL = -20*log10\|2*Z0/(2*Z0 + Zd)\|; shunt: IL = -20*log10\|2*Zd/(2*Zd + Z0)\|; Zr = Rr + j*(w*Li - 1/(w*Cj)) (reverse), Zf = Rf + j*w*Li (forward) | Rf, Rr, Cj, Li, Z0, f | lumped model Fig.11.6; external series/parallel reactance can resonate out diode reactance (narrows bandwidth) | calc | §11.1 eq.(11.13)–(11.15), p.531–532 | high |
| POZAR-343 | components | Worked PIN switch (anchor): 1.8 GHz, UM9605 (Cj = 0.5 pF, Rf = 1.5 ohm), Li = 0.5 nH, Rr = 2.0 ohm, Z0 = 50 | Zr = 2.0 - j171.2 ohm, Zf = 1.5 + j5.6 ohm; series: IL_on = 0.14 dB, IL_off = 6.0 dB; shunt: IL_on = 0.11 dB, IL_off = 13.3 dB -> shunt gives the best on/off ratio and lowest on loss | — | — | calc | §11.1 Ex.11.1, p.532–534 | high |
| POZAR-344 | components | Shunt-type SPDT PIN switch uses lambda/4 lines that limit its bandwidth; series SPDT has no such lines | BW limited by lambda/4 | topology | multi-throw switches | review | §11.1 Fig.11.9, p.532 | high |
| POZAR-345 | rf | Switched-line phase shifter: true time delay (phase linear in f for TEM/quasi-TEM), reciprocal; insertion loss = 2 SPDT losses + line loss; avoid OFF-path lengths near multiples of lambda/2 (resonance, shifted by diode Cj) | dphi = beta*(l2 - l1) | l1, l2, beta | binary bits 180/90/45 ... | calc | §11.1 eq.(11.16), Fig.11.11, p.534–535 | high |
| POZAR-346 | rf | Loaded-line phase shifter (small shifts, <= 45 deg): single shunt b; use two identical loads lambda/4 apart to cancel reflections | single load: Gamma = -jb/(2 + jb), T = 2/(2 + jb), dphi = atan(b/2); pair lambda/4 apart: cos(theta_e) = -b, Ze = Z0/sqrt(1 - b^2); small b: theta_e ≈ pi/2 + b, Ze ≈ Z0*(1 + b^2/2) | b = B*Z0 | insertion loss grows with b | calc | §11.1 eq.(11.17)–(11.21), Fig.11.12, p.535–536 | high |
| POZAR-347 | rf | Reflection phase shifter (quadrature hybrid + two switched terminations): widest bandwidth when the two states' reflection coefficients are phase conjugates (e.g. for dphi = 90 deg choose phi = 45 deg); input match requires well-matched (identical) diodes; loss set by hybrid loss and diode Rf, Rr | Gamma_on = exp(-j(phi + pi)), Gamma_off = exp(-j(phi + dphi)) | dphi | — | calc | §11.1 Fig.11.13, p.536–537 | high |
| POZAR-348 | components | PIN diode phase shifters need continuous bias current (higher DC power) whereas latching ferrite shifters need only pulsed current; diode shifters are smaller, planar and faster | — | power budget | phased arrays | review | §11.1 p.534 | high |
| POZAR-349 | components | Varactor C-V law | Cj(V) = C0/(1 - V/V0)^gamma (V negative = reverse); V0 = 0.5 V (Si), 1.3 V (GaAs); gamma = 0.5 "ideal hyperabrupt" (as printed), ≈ 0.47 many practical diodes, up to 1.5–2.0 some diodes; Rs a few ohms; typical GaAs: C0 = 0.5–2.0 pF, Cj ≈ 0.1–2.0 pF for V = -20..0 V | C0, V0, gamma | include package parasitics in real designs | calc | §11.1 eq.(11.22), Fig.11.14, p.537 | high |
| POZAR-350 | components | Negative-resistance diode sources (orientation values): Gunn — up to several hundred mW CW, 1–200 GHz, eta 5–15%, bias tuning <= 1% (use varactor for more); IMPATT — 70–100 V bias, 10–300 GHz, eta up to 15%, noisier (high AM noise) but more power, better temperature stability; Si IMPATT 10 W @ 10 GHz to 1 W @ 94 GHz (eta < 10%), GaAs IMPATT 20 W @ 10 GHz to 5 mW @ 130 GHz; BARITT — low AM noise LO up to 94 GHz | see statement | f, P | mm-wave sources; thermal limits for IMPATT | review | §11.1 p.538–539 | high |
| POZAR-351 | rf | Power combining of coherent, in-phase sources is limited in practice to a multiplication factor of about 10–20 dB (higher-order modes, combiner loss) | N_combine gain ≈ 10–20 dB max | N sources | device-, circuit- (N-way Wilkinson, cavity) or spatial combining | review | §11.1 p.539–540 | high |
| POZAR-352 | components | Transistor unity current-gain frequency from the hybrid-pi / FET small-signal model | BJT: fT = gm/(2*pi*C_pi); FET: fT = gm/(2*pi*Cgs); e.g. MESFET typical gm = 40 mS, Cgs = 0.3 pF -> fT ≈ 21 GHz (computed) | gm, C_pi or Cgs | unilateral model (Cc or Cgd neglected, S12 = 0) | calc | §11.2 eq.(11.23), §11.3 eq.(11.24), p.541–545 | high |
| POZAR-353 | components | Si BJT application range: amplifiers to 2–10 GHz, oscillators to ~20 GHz; very low 1/f noise (good for low phase-noise oscillators); preferred below ~2–4 GHz (gain, cost, single supply); shot + thermal noise -> NF worse than FETs; low collector current for best NF, higher current for best gain | f limits as stated | f, NF, supply | RF BJT (npn) | review | §11.2 p.540–542 | high |
| POZAR-354 | components | GaAs MESFET: gate length 0.2–0.6 um gives upper frequency limits of about 100 to 50 GHz; typical small-signal values Ri = 7 ohm, Rds = 400 ohm, Cgs = 0.3 pF, Cds = 0.12 pF, Cgd = 0.01 pF, gm = 40 mS; low-noise bias at I_D ≈ 15% of Idss; needs dual-polarity supply (negative gate) with RF chokes and DC blocks | I_D(LNA) ≈ 0.15*Idss | Idss | common source | review | §11.3 p.544–546 | high |
| POZAR-355 | components | Transistor technology selection anchors: LDMOS for high-power base stations (900/1900 MHz); GaN HEMT drain 20–40 V, up to 100 W at low microwave; GaAs HEMT > 100 GHz, lowest NF; SiGe HBT for low-cost mm-wave (60 GHz+); CMOS for integrated low-cost/low-power | see Table 11.6 (§2) | f, P, NF, cost, supply polarity | 2012-era device data | review | §11.2–11.3, Table 11.6, p.542–547 | high |
| POZAR-356 | fab | Hybrid MIC substrate choice: alumina er ≈ 9–10 (rigid, small circuits at lower f; at high f thin substrates make lines too narrow); quartz er ≈ 4 (rigid, > 20 GHz); PTFE-type soft substrates er 2–10 (large area, low cost, poor rigidity/thermal); conductors Cu or Au; tuning/trim stubs raise yield but add skilled labour cost | er as stated | f, size, thermal | hybrid MICs | review | §11.4 p.548 | high |
| POZAR-357 | fab | MMIC process/design constraints: Au conductors several skin depths thick over Cr or Ti adhesion layers; dielectrics SiO, SiO2, silicon nitride, Ta2O5; resistors NiCr, Ta, Ti, doped GaAs; post-fab trimming impractical, so design must include tolerances, discontinuities, bias networks, spurious coupling, package resonances; vias give grounds and heat paths | t_metal >= several delta_s | f | GaAs/Si/SiC/InP MMIC | review | §11.4 p.549–550 | high |
| POZAR-358 | cost | MMIC economics/limits: waste expensive substrate on lines/hybrids, critical processing -> low yields, expensive in small quantities (< several hundred), limited heat dissipation (moderate power only), high-Q resonators/filters difficult; advantages: extra FETs almost free, low parasitics -> broader bandwidth, very reproducible (same wafer) | qty threshold ~ several hundred | volume, power, Q | make-vs-buy / technology choice | review | §11.4 p.550 | high |
| POZAR-359 | components | RF switch technology comparison over 10–20 GHz (use for part selection): PIN IL 0.1–0.8 dB, isolation 25–45 dB, 1–5 mW, 1–10 V, 1–5 ns; FET 0.5–1.0 dB, 20–50 dB, 1–5 mW, 1–10 V, 2–10 ns; MEMS 0.1–1.0 dB, 25–60 dB, 1 uW, 10–20 V, > 30 us (mechanical: slow, lifetime-limited, but virtually no IMD) | see table §2 T2.10 | IL, isolation, speed, power | 2012-era values | review | §11.4 POI "RF MEMS", p.551–552 | high |
| POZAR-360 | components | Tubes vs solid state: solid state preferred when it meets power/frequency; tubes for very high power (>= 10 kW) and/or >= 100 GHz; radar Tx 1–10 kW, EW 100 W–1 kW (wide tuning), microwave oven ≈ 700 W | P, f per Fig.11.28 (graph) | P, f | source selection | review | §11.5 p.552–553, Fig.11.28 | medium (graph) |
| POZAR-361 | rf | Two-port gain definitions: power gain G = PL/Pin (independent of ZS), available gain GA = Pavn/Pavs (depends on ZS, not ZL), transducer gain GT = PL/Pavs (depends on both); with both ports conjugately matched G = GA = GT; GT is the most useful for amplifier design | see POZAR-363 | S, Gs, GL | linear two-port | calc | §12.1 p.559, 562 | high |
| POZAR-362 | rf | Terminated two-port input/output reflection coefficients | Gin = S11 + S12*S21*GL/(1 - S22*GL); Gout = S22 + S12*S21*GS/(1 - S11*GS); GS = (ZS - Z0)/(ZS + Z0); GL = (ZL - Z0)/(ZL + Z0) | S-params, ZS, ZL | Z0 = S-parameter reference | calc | §12.1 eq.(12.1),(12.3), p.559–560 | high |
| POZAR-363 | rf | Power, available and transducer gains in S-parameters | G = \|S21\|^2*(1 - \|GL\|^2)/((1 - \|Gin\|^2)*\|1 - S22*GL\|^2); GA = \|S21\|^2*(1 - \|GS\|^2)/(\|1 - S11*GS\|^2*(1 - \|Gout\|^2)); GT = \|S21\|^2*(1 - \|GS\|^2)*(1 - \|GL\|^2)/(\|1 - GS*Gin\|^2*\|1 - S22*GL\|^2); GS = GL = 0 -> GT = \|S21\|^2; unilateral (S12 = 0): GTU = \|S21\|^2*(1 - \|GS\|^2)*(1 - \|GL\|^2)/(\|1 - S11*GS\|^2*\|1 - S22*GL\|^2) | S, GS, GL | — | calc | §12.1 eq.(12.8)–(12.15), p.560–561 | high |
| POZAR-364 | rf | Worked gain comparison (anchor): Si BJT at 1 GHz, S11 = 0.38∠-158, S12 = 0.11∠54, S21 = 3.50∠80, S22 = 0.40∠-43, ZS = 25 ohm, ZL = 40 ohm | GS = -0.333, GL = -0.111; Gin = 0.365∠-152, Gout = 0.545∠-43; G = 13.1, GA = 19.8, GT = 12.6 (linear) | — | — | calc | §12.1 Ex.12.1, p.561–562 | high |
| POZAR-365 | rf | Transducer gain factorization into input-network, device and output-network terms; matching-network "gains" can exceed 1 because they recover the device's mismatch loss | GT = GS*G0*GL; GS = (1 - \|GS\|^2)/\|1 - Gin*GS\|^2, G0 = \|S21\|^2, GL = (1 - \|GL\|^2)/\|1 - S22*GL\|^2; unilateral: GS = (1 - \|GS\|^2)/\|1 - S11*GS\|^2 | S, GS, GL | lossless matching networks | calc | §12.1 eq.(12.16),(12.17), p.562–563 | high |
| POZAR-366 | rf | Conjugately matched unilateral FET gain falls 6 dB/octave | GTU = gm^2*Rds/(4*w^2*Ri*Cgs^2) = (Rds/(4*Ri))*(fT/f)^2 | gm, Rds, Ri, Cgs, f | simplified FET model (Cgd = 0) | calc | §12.1 eq.(12.18), p.563 | high |
| POZAR-367 | rf | Amplifier stability: unconditional if \|Gin\| < 1 and \|Gout\| < 1 for ALL passive \|GS\|, \|GL\| < 1, otherwise conditional (potentially unstable); stability depends on frequency AND bias, so check it over the whole band where the device has gain, not just at f0; valid when S-params are measurable (pole-free) | \|Gin\| < 1, \|Gout\| < 1 | S(f), bias | two-port amplifiers | sim | §12.2 p.564, 567 | high |
| POZAR-368 | rf | Output and input stability circles (loci of \|Gin\| = 1 in the GL plane and \|Gout\| = 1 in the GS plane) | Delta = S11*S22 - S12*S21; CL = conj(S22 - Delta*conj(S11))/(\|S22\|^2 - \|Delta\|^2), RL = \|S12*S21/(\|S22\|^2 - \|Delta\|^2)\|; CS = conj(S11 - Delta*conj(S22))/(\|S11\|^2 - \|Delta\|^2), RS = \|S12*S21/(\|S11\|^2 - \|Delta\|^2)\|; if \|S11\| < 1 the chart centre (GL = 0) is stable, so the region on the centre's side of the output circle is stable (if \|S11\| > 1 the opposite); same for input circle with S22 | S-params | choose GS, GL inside stable regions for conditionally stable devices | calc | §12.2 eq.(12.21)–(12.26), Fig.12.5, p.565–566 | high |
| POZAR-369 | rf | Unconditional stability via circles; a device with \|S11\| > 1 or \|S22\| > 1 can never be unconditionally stable; resistive loading can make a device unconditionally stable at the cost of gain | \|\|CL\| - RL\| > 1 (for \|S11\| < 1) and \|\|CS\| - RS\| > 1 (for \|S22\| < 1) | CL, RL, CS, RS | — | calc | §12.2 eq.(12.27), p.566–567 | high |
| POZAR-370 | rf | Rollet K–Delta test for unconditional stability (necessary and sufficient, both conditions) | K = (1 - \|S11\|^2 - \|S22\|^2 + \|Delta\|^2)/(2*\|S12*S21\|) > 1 AND \|Delta\| = \|S11*S22 - S12*S21\| < 1 | S-params | cannot rank relative stability of devices | calc | §12.2 eq.(12.28),(12.29), p.567 | high |
| POZAR-371 | rf | Edwards–Sinsky mu test: single-parameter unconditional stability; larger mu = more stable (allows device ranking) | mu = (1 - \|S11\|^2)/(\|S22 - Delta*conj(S11)\| + \|S12*S21\|) > 1; mirror form mu' = (1 - \|S22\|^2)/(\|S11 - Delta*conj(S22)\| + \|S12*S21\|) (by S11<->S22 interchange, stated for input side) | S-params | — | calc | §12.2 eq.(12.30)–(12.35), p.567–569 | high (mu) / medium (mu') |
| POZAR-372 | rf | Worked stability check (anchor): Triquint T1G6000528 GaN HEMT at 1.9 GHz, S11 = 0.869∠-159, S12 = 0.031∠-9, S21 = 4.250∠61, S22 = 0.507∠-117 | \|Delta\| = 0.336, K = 0.383, mu = 0.678 -> potentially unstable; CL = 1.59∠132, RL = 0.915; CS = 1.09∠162, RS = 0.205; chart centre stable since \|S11\|, \|S22\| < 1 | — | — | calc | §12.2 Ex.12.2, Fig.12.6, p.569–570 | high |
| POZAR-373 | rf | Simultaneous conjugate match for maximum gain (bilateral device): exists only if K > 1 (with \|Delta\| < 1); take the root with \|G\| < 1; narrowband because \|S11\|, \|S22\| are large | GS = (B1 ± sqrt(B1^2 - 4\|C1\|^2))/(2*C1); GL = (B2 ± sqrt(B2^2 - 4\|C2\|^2))/(2*C2); B1 = 1 + \|S11\|^2 - \|S22\|^2 - \|Delta\|^2; B2 = 1 + \|S22\|^2 - \|S11\|^2 - \|Delta\|^2; C1 = S11 - Delta*conj(S22); C2 = S22 - Delta*conj(S11); Gin = conj(GS), Gout = conj(GL) | S-params | lossless matching networks; ports then matched to Z0 | calc | §12.3 eq.(12.36)–(12.41), p.571–572 | high |
| POZAR-374 | rf | Maximum gains: unilateral max transducer gain, bilateral matched gain (K > 1), and maximum stable gain (figure of merit for conditionally stable devices) | GTUmax = \|S21\|^2/((1 - \|S11\|^2)*(1 - \|S22\|^2)); GTmax = (\|S21\|/\|S12\|)*(K - sqrt(K^2 - 1)) for K > 1; MSG = \|S21\|/\|S12\| (GTmax at K = 1) | S-params, K | GTmax meaningless for K < 1 | calc | §12.3 eq.(12.42)–(12.44), p.572 | high |
| POZAR-375 | rf | Worked conjugate-matched amplifier (anchor): GaAs MESFET, 4 GHz, S at 3/4/5 GHz: S11 = 0.80∠-89 / 0.72∠-116 / 0.66∠-142; S12 = 0.03∠56 / 0.03∠57 / 0.03∠62; S21 = 2.86∠99 / 2.60∠76 / 2.39∠54; S22 = 0.76∠-41 / 0.73∠-54 / 0.72∠-68 | K = 0.77 / 1.19 / 1.53, \|Delta\| = 0.592 / 0.487 / 0.418 (conditionally stable at 3 GHz); at 4 GHz GS = 0.872∠123, GL = 0.876∠61; GS = 6.20 dB, G0 = 8.30 dB, GL = 2.22 dB, GTmax = 16.7 dB; single-stub networks: input line 0.120λ + OC stub 0.206λ, output line 0.206λ + stub 0.206λ; 1 dB gain bandwidth ≈ 2.5% | — | verify out-of-band (3 GHz) that the realized GS, GL lie in stable regions (CAD showed stable 3–5 GHz) | sim | §12.3 Ex.12.3, Fig.12.7, p.573–575 | high |
| POZAR-376 | rf | Unilateral-approximation error bound: treat the device as unilateral only if the bound is a few tenths of a dB or less | U = \|S12\|\|S21\|\|S11\|\|S22\|/((1 - \|S11\|^2)*(1 - \|S22\|^2)); 1/(1 + U)^2 < GT/GTU < 1/(1 - U)^2 | S-params | — | calc | §12.3 eq.(12.45),(12.46), p.576 | high |
| POZAR-377 | rf | Constant-gain circles (unilateral) for specified-gain design: 0 dB circles pass through the chart centre; pick GS, GL on the required circles as close to the chart centre as possible (least mismatch, widest bandwidth) | GSmax = 1/(1 - \|S11\|^2); gS = GS/GSmax = (1 - \|GS\|^2)*(1 - \|S11\|^2)/\|1 - S11*GS\|^2; CS = gS*conj(S11)/(1 - (1 - gS)*\|S11\|^2); RS = sqrt(1 - gS)*(1 - \|S11\|^2)/(1 - (1 - gS)*\|S11\|^2); output circles identical with S22, gL | S11, S22, target GS, GL | centres lie on the conj(S11), conj(S22) radial lines | calc | §12.3 eq.(12.47)–(12.52), p.576–577 | high |
| POZAR-378 | rf | Worked specified-gain amplifier (anchor): unilateral device at 4 GHz S11 = 0.75∠-120, S21 = 2.5∠80, S22 = 0.60∠-70, target 11 dB | GSmax = 2.29 (3.6 dB), GLmax = 1.56 (1.9 dB), G0 = 6.25 (8.0 dB), GTUmax = 13.5 dB; circles GS = 3 dB: gS = 0.875, C = 0.706∠120, R = 0.166; GS = 2 dB: 0.691, 0.627∠120, 0.294; GL = 1 dB: 0.806, 0.520∠70, 0.303; GL = 0 dB: 0.640, 0.440∠70, 0.440; chosen GS = 0.33∠120, GL = 0.22∠70 -> 11 dB; ±1 dB gain bandwidth ≈ 25% (vs 2.5% for conjugate match) but input return loss only ≈ 5 dB | — | trade: flat gain vs port match (fix with balanced topology) | sim | §12.3 Ex.12.4, Fig.12.8, p.577–579 | high |
| POZAR-379 | noise | Two-port noise figure versus source termination (noise parameters Fmin, Gopt/Yopt, RN from datasheet or measurement) | F = Fmin + (RN/GS_re)*\|YS - Yopt\|^2 = Fmin + 4*(RN/Z0)*\|GS - Gopt\|^2/((1 - \|GS\|^2)*\|1 + Gopt\|^2); F = Fmin only when GS = Gopt | Fmin, Gopt, RN, GS | minimum NF and maximum gain generally need different GS -> compromise | calc | §12.3 eq.(12.53)–(12.57), p.580 | high |
| POZAR-380 | noise | Constant noise-figure circles in the GS plane | N = \|GS - Gopt\|^2/(1 - \|GS\|^2) = (F - Fmin)*\|1 + Gopt\|^2/(4*RN/Z0); CF = Gopt/(N + 1); RF = sqrt(N*(N + 1 - \|Gopt\|^2))/(N + 1) | F target (linear), Fmin, Gopt, RN, Z0 | overlay with gain circles to trade NF vs gain | calc | §12.3 eq.(12.58)–(12.60), p.580–581 | high |
| POZAR-381 | noise | Worked LNA (anchor): GaAs MESFET at 4 GHz, S11 = 0.6∠-60, S12 = 0.05∠26, S21 = 1.9∠81, S22 = 0.5∠-60, Fmin = 1.6 dB, Gopt = 0.62∠100, RN = 20 ohm, target F = 2.0 dB | K = 2.78, \|Delta\| = 0.37; U = 0.059 -> -0.50 < GT - GTU < 0.53 dB; N = 0.0986, CF = 0.56∠100, RF = 0.24; gain circles GS = 1.0/1.5/1.7 dB: gS = 0.805/0.904/0.946, CS = 0.52/0.56/0.58∠60, RS = 0.300/0.205/0.150; choose GS = 0.53∠75 (GS = 1.7 dB, F = 2.0 dB), GL = conj(S22) = 0.5∠60 (GL = 1.25 dB), G0 = 5.58 dB -> GTU = 8.53 dB (CAD 8.36 dB) | — | — | sim | §12.3 Ex.12.5, Fig.12.9, p.581–582 | high |
| POZAR-382 | rf | Inductive source degeneration creates a noiseless real input resistance for MOSFET (or other FET) LNAs; series gate inductor cancels the remaining capacitive reactance; the input forms a series RLC whose Q sets bandwidth | Zin = gm*Ls/Cgs + j*(w*Ls - 1/(w*Cgs)); Ls = Z0*Cgs/gm; Lg = -X/w; Q = w*Lg*Cgs/(gm*Ls) (as printed) | gm, Cgs, Z0, f | unilateral simplified model (Ri, Rds, Cds neglected) | calc | §12.3 eq.(12.61)–(12.63), p.582–584 | high |
| POZAR-383 | rf | Worked degenerated MOSFET LNA (anchor): Infineon BF1005, Cgs = 2.1 pF, gm = 24 mS, 900 MHz, Z0 = 50 ohm | Ls = 4.37 nH; residual X = -59.5 ohm -> Lg = 10.5 nH; Q = 1.2 -> bandwidth "as high as 80%" (optimistic given model approximations) | — | — | calc | §12.3 Ex.12.6, p.584–585 | high |
| POZAR-384 | rf | Broadband amplifier techniques (each trades gain, complexity, NF or DC power for bandwidth): compensated matching (worse port match); resistive matching (good match, lower gain, higher NF); negative feedback (flattens gain, improves match and stability, > decade bandwidth possible, costs gain and NF); balanced (good match over an octave or more, gain of one stage, 2x devices and DC power); distributed (decade+, good match/NF, large, less gain than a cascade); differential (~2x fT, ~2x voltage swing, common-mode rejection) | — | BW target | microwave transistors are poorly matched to 50 ohm and \|S21\| falls 6 dB/octave; Bode–Fano limits match bandwidth | review | §12.4 p.585 | high |
| POZAR-385 | rf | Balanced amplifier (two identical stages between 90-deg hybrids): reflections go to coupler terminations -> good port match and improved stability; stages can be optimized for flatness or NF alone; one stage failing costs 6 dB; bandwidth set by the couplers (octave+; Lange couplers in MMIC, or branch-line / Wilkinson + 90 deg line) | S21 = -j*(GA + GB)/2; S11 = (GammaA - GammaB)/2 (0 for identical stages); S22 = (GammaA,out - GammaB,out)/2; F = (FA + FB)/2 | GA, GB, Gammas, FA, FB | ideal hybrids | calc | §12.4 eq.(12.64)–(12.68), Fig.12.11, p.586–587; Problem 12.19 (S22) | high |
| POZAR-386 | rf | Worked balanced amplifier (anchor): Example 12.4 stages between 4 GHz quadrature hybrids, 3–5 GHz: return loss improves dramatically (best at 4 GHz); CAD optimization to flat 10 dB changed stub/line lengths: input stub 0.100λ -> 0.109λ, input line 0.179λ -> 0.113λ, output line 0.045λ -> 0.134λ, output stub 0.432λ -> 0.461λ | — | — | — | sim | §12.4 Ex.12.7, Fig.12.12, p.587–588 | high |
| POZAR-387 | rf | Distributed (traveling-wave) amplifier line design: FET Cgs, Cds absorbed into artificial gate/drain lines; gate and drain phase velocities must be synchronized; line terminations absorb reverse waves | Zg = sqrt(Lg/(Cg + Cgs/lg)); alpha_g*lg ≈ w^2*Ri*Cgs^2*Zg/2; Zd = sqrt(Ld/(Cd + Cds/ld)); alpha_d*ld ≈ Zd/(2*Rds); synchronization beta_g*lg = beta_d*ld | FET Ri, Cgs, Rds, Cds, line L, C | small-loss, electrically short unit cells, unilateral FET (w*Ri*Cgs << 1) | calc | §12.4 eq.(12.69)–(12.75), p.588–591 | high |
| POZAR-388 | rf | Distributed amplifier gain and optimum number of stages: lossless gain grows as N^2 (not G0^N) but with loss the gain -> 0 as N -> infinity, so there is an optimum N | G = (gm^2*Zd*Zg/4)*(exp(-N*ag*lg) - exp(-N*ad*ld))^2/(exp(-ag*lg) - exp(-ad*ld))^2; lossless: G = gm^2*Zd*Zg*N^2/4; N_opt = ln(ag*lg/(ad*ld))/(ag*lg - ad*ld) | gm, Zd, Zg, alphas | matched ports | calc | §12.4 eq.(12.76)–(12.80), p.591–592 | high |
| POZAR-389 | rf | Worked distributed amplifier (anchor): Zd = Zg = 50 ohm, Ri = 5 ohm, Rds = 250 ohm, Cgs = 0.30 pF, gm = 30 mS, N = 2, 4, 8, 16 over 1–18 GHz | at 16 GHz ag*lg = 0.100, ad*ld = 0.114 -> N_opt = 9.4 (≈ 9 stages); w*Ri*Cgs = 0.17 at 18 GHz; larger N rolls off faster (N = 16 below smaller N at high f) | — | Fig.12.16 (graph) | calc | §12.4 Ex.12.8, Fig.12.16, p.592–593 | high |
| POZAR-390 | rf | Differential amplifiers: reject common-mode interference (important in dense RFICs), ~2x output voltage swing; cost ~2x devices and more bias power; pseudo-differential = two single-ended amps between 180-deg hybrids; baluns: transformer (low f), 180-deg hybrid (difference port = unbalanced), Marchand coupled-line balun | — | topology | RFIC receivers | review | §12.4 Figs.12.17–12.18, p.593–594 | high |
| POZAR-391 | rf | Differential-pair (FET) differential gain, common-mode gain and CMRR: tail (source) resistance Rs (or current source) sets common-mode rejection; Rs = 0 -> CMRR = 1 (none), Rs -> infinity (ideal current source) -> CMRR -> infinity | Ad = -gm*RD*Rds/((1 + j*w*Ri*Cgs)*(RD + Rds)); Ac = -gm*Rds*RD/((1 + j*w*Cgs*(Ri + 2Rs))*(Rds + RD + 2Rs)); CMRR = Ad/Ac = (1 + 2Rs/(Rds + RD))*(1 + j*w*Cgs*(Ri + 2Rs))/(1 + j*w*Cgs*Ri) | gm, RD, Rds, Ri, Cgs, Rs | unilateral FET model | calc | §12.4 eq.(12.81)–(12.87), p.595–596 | high (Ad printed with Cds in eq.12.83, Cgs per derivation) |
| POZAR-392 | rf | Power amplifier output-power orientation: 100–500 mW (mobile voice/data), 1–100 W (radar, fixed point radio); single transistors 10–100 W at UHF, generally < 10 W at higher frequencies (combine devices for more) | P_out ranges | application | 2012-era | review | §12.5 p.596–597 | high |
| POZAR-393 | power | PA efficiency definitions: drain/collector efficiency overrates low-gain amplifiers; use power-added efficiency. Si BJT PAs at 800–900 MHz reach PAE ≈ 80%, falling quickly with frequency | eta = Pout/PDC; PAE = (Pout - Pin)/PDC = (1 - 1/G)*eta | Pout, Pin, PDC, G | PA is the main DC consumer in handhelds | calc | §12.5 eq.(12.88),(12.89), p.597 | high |
| POZAR-394 | rf | Compressed gain at the 1 dB point | G1(dB) = G0(dB) - 1 | G0 | — | calc | §12.5 eq.(12.90), p.597 | high |
| POZAR-395 | rf | Amplifier class theoretical maximum efficiencies and use: class A (linear, full-cycle conduction) 50%; class B (half cycle, push-pull) 78%; class C near 100% but constant-envelope modulation only; D/E/F/S switch-mode higher; UHF+ communication transmitters mostly use A, AB or B for low distortion; linearity critical for non-constant-envelope modulation (ASK, QAM) and multicarrier (adjacent-channel spurs) | eta_max: A 50%, B 78%, C ≈ 100% | modulation type | — | review | §12.5 p.597–598 | high |
| POZAR-396 | rf | Large-signal characterization: above ≈ IP1dB S-parameters depend on drive, load, bias, temperature and are not unique; still use small-signal S for stability checks; characterize by optimum large-signal GSP, GLP (max gain at a given Pout, often OP1dB) or load-pull constant-Pout contours (not perfect circles); dominant FET nonlinear elements Cgs, gm, Cgd, Rds (temperature dependent) | — | load-pull data | PA design | measure | §12.5 Table 12.1, Fig.12.21, p.598 | high |
| POZAR-397 | rf | Class A PA design practice: check stability first with small-signal S (high-power oscillation can destroy devices); select a transistor with about 20% more power capacity than required; heat-sink any stage above a few tenths of a watt; conjugate-match the input, match the output to GLP for maximum power (not the small-signal conjugate); use low-loss output matching (highest currents); internally matched devices reduce package-parasitic effects | P_device ≈ 1.2 x P_required | P_out, device data | — | review | §12.5 p.599–600 | high |
| POZAR-398 | rf | Worked 10 W class A PA (anchor): Nitronex NPT25100 GaN HEMT at 2.3 GHz, VDS = 28 V, ID = 600 mA; S11 = 0.593∠178, S12 = 0.009∠-127, S21 = 1.77∠-106, S22 = 0.958∠175; ZSP = 10 - j3 ohm, ZLP = 2.5 - j2.3 ohm; G = 16.4 dB and drain efficiency 26% at 10 W | \|Delta\| = 0.579, K = 2.08 (unconditionally stable); GSP = 0.668∠187, GLP = 0.905∠-175 (vs small-signal conjugate GS = 0.508∠166, GL = 0.954∠-176); Pin = 40 - 16.4 = 23.6 dBm (229 mW); PDC = 38.5 W; ID = 1.37 A; PAE = 25% | — | — | calc | §12.5 Ex.12.9, Fig.12.23, p.600–601 | high |
| POZAR-399 | rf | A lossless reciprocal network that matches ZL (port 2) to Z0 (port 1) presents conj(ZL) at port 2 when port 1 is terminated in Z0 — so Chapter 5 load-matching techniques can design amplifier output (and input) networks | Z_port2 = conj(ZL) | network | lossless, reciprocal | calc | §12 Problem 12.10 (stated relation), p.603 | medium |
| POZAR-400 | rf | Oscillator specification set and typical requirements: tuning range (MHz/V for VCOs), frequency stability (ppm/degC; typical requirement 2 to 0.5 ppm/degC), AM/FM (phase) noise (dBc/Hz at an offset; typical -80 to -110 dBc/Hz at 10 kHz offset), harmonics (dBc) | stability 0.5–2 ppm/degC; L(10 kHz) = -80..-110 dBc/Hz | requirements | RF/microwave LOs and sources | review | §13 intro p.604–605 | high |
| POZAR-401 | rf | Tunable source choice: varactor-tuned VCOs tune about an octave (fast); YIG-tuned oscillators tune a decade or more but slower; transistor oscillators are more controllable (bias, terminations, temperature stability, noise, locking, modulation) than diode sources but lower power | VCO ≈ 1 octave; YTO ≥ 1 decade | tuning range, speed | — | review | §13 intro p.605 | high |
| POZAR-402 | rf | Feedback (Barkhausen/Nyquist) oscillation condition | Vo/Vi = A/(1 - A*H(w)); oscillation where A*H(w) = 1 | A, H(w) | oscillator design needs an unstable circuit (opposite of amplifier design) | calc | §13.1 eq.(13.1),(13.2), p.605–606 | high |
| POZAR-403 | rf | Three-reactance transistor oscillator conditions (unilateral device, lossless feedback): X1 and X2 same type, X3 opposite; Colpitts = C1, C2 with L3; Hartley = L1, L2 with C3 | X1 + X2 + X3 = 0; common emitter: X1 = (gm/Gi)*X2; Colpitts: w0 = sqrt((C1 + C2)/(L3*C1*C2)), CE: C2/C1 = gm/Gi, CG (FET): C1/C2 = gm/Go; Hartley: w0 = 1/sqrt(C3*(L1 + L2)), CE: L1/L2 = gm/Gi, CG: L2/L1 = gm/Go | gm, Gi or Go, L, C | idealized; real design must include port reactances, temperature variation, bias/decoupling, inductor loss (use CAD) | calc | §13.1 eq.(13.6)–(13.19), p.607–610 | high |
| POZAR-404 | rf | Common-emitter Colpitts with lossy inductor (series R): frequency and maximum R (minimum inductor Q) for sustained oscillation; keep R well below the maximum | w0 = sqrt((1/L3)*(1/C1' + 1/C2)), C1' = C1/(1 + R*Gi); oscillation requires R/Gi < (1 + gm/Gi)/(w0^2*C1*C2) - L3/C1, i.e. R_max = Gi*((1 + beta)/(w0^2*C1*C2) - L3/C1); Q_min = w0*L3/R_max | L3, Q0, C1, C2, gm, Gi | small-signal; margin needed for start-up | calc | §13.1 eq.(13.20)–(13.22), p.610–611 | high |
| POZAR-405 | rf | Worked Colpitts (anchor): 50 MHz, CE BJT beta = gm/Gi = 30, Ri = 1200 ohm, L3 = 0.10 uH with Q0 = 100 | series C = 100 pF -> C1 = C2 = 200 pF; R = 0.31 ohm; C1' ≈ 200 pF; condition 372 < 7852 - 500 = 7352 (satisfied); R_max = 6.13 ohm -> Q_min = 5.1 | — | — | calc | §13.1 Ex.13.1, p.611–612 | high |
| POZAR-406 | components | Crystal oscillators: LC resonators below a few hundred MHz seldom exceed Q of a few hundred, quartz reaches Q ≈ 100,000 with drift < 0.001%/degC (oven control improves further); crystal operated in its inductive region between series and parallel resonance (replaces the inductor in Colpitts/Pierce) | ws = 1/sqrt(L*C); wp = 1/sqrt(L*C*C0/(C0 + C)); inductive for ws < w < wp | crystal L, C, C0 | fundamental mode | calc | §13.1 eq.(13.23), Figs.13.4–13.5, p.612–613 | high |
| POZAR-407 | rf | One-port negative-resistance oscillator: start-up needs net negative resistance; steady state when resistances and reactances cancel; the load reflection coefficient is the reciprocal of the device's | start-up: Rin(I,w) + RL < 0; steady state: RL + Rin = 0, XL + Xin = 0; GL = 1/Gin | Zin(I,w), ZL | Rin becomes less negative as amplitude grows; final frequency differs from start-up frequency | calc | §13.2 eq.(13.24)–(13.26), p.613–614 | high |
| POZAR-408 | rf | Kurokawa stability condition for the oscillation point; with dRin/dI > 0 it is met by a steep reactance slope, so a high-Q resonator (cavity, dielectric) maximizes oscillator stability | (dRT/dI)*(dXT/dw) - (dXT/dI)*(dRT/dw) > 0; passive load: (dRin/dI)*d(XL + Xin)/dw - (dXin/dI)*(dRin/dw) > 0 | Z(I,w) data | — | calc | §13.2 eq.(13.27)–(13.30), p.614 | high |
| POZAR-409 | rf | Worked negative-resistance oscillator (anchor): diode Gin = 1.25∠40 (Z0 = 50) at 6 GHz | Zin = -44 + j123 ohm -> ZL = 44 - j123 ohm realized with shunt stub + series line (0.254λ, 0.308λ) | — | — | calc | §13.2 Ex.13.2, Fig.13.7, p.615 | high |
| POZAR-410 | rf | Two-port transistor oscillator design: use a highly unstable configuration (common gate/base, positive feedback e.g. gate inductor); choose GL (inside the unstable region) for large \|Gin\|; then set the terminating impedance with margin for start-up; oscillation at the input implies oscillation at the output (GL*Gout = 1); prefer large-signal S | RS = -Rin/3; XS = -Xin (and analogously ZL = -Rout/3 - j*Xout when designing from the output side) | S (large-signal preferred) | steady-state frequency will differ from design value (nonlinearity) | calc | §13.2 eq.(13.31)–(13.34), p.615–616 | high |
| POZAR-411 | rf | Worked FET oscillator (anchor): 4 GHz GaAs MESFET, common gate + 5 nH gate inductor; common-source S11 = 0.72∠-116, S12 = 0.03∠57, S21 = 2.60∠76, S22 = 0.73∠-54 -> CG+L: S11' = 2.18∠-35, S12' = 1.26∠18, S21' = 2.75∠96, S22' = 0.52∠155 | output stability circle CL = 1.08∠33, RL = 0.665 (stable region inside since \|S11'\| > 1); GL = 0.59∠-104 (ZL = 20 - j35 ohm); Gin = 3.96∠-2.4 (Zin = -84 - j1.9 ohm); ZS = 28 + j1.9 ohm (90 ohm load + short line) | — | — | calc | §13.2 Ex.13.3, Fig.13.9, p.616–617 | high |
| POZAR-412 | rf | Dielectric resonator oscillators: lumped/microstrip resonator Q limited to a few hundred; metal cavities reach 1e4 but are bulky and drift with thermal expansion; dielectric resonators (TE01δ) give Q up to several thousand, compact, temperature stable; coupled magnetically to a microstrip line (spacing d sets coupling); parallel-feedback DROs tune wider, series-feedback simpler | Z_series = N^2*R/(1 + j*2*Q0*dw/w0); coupling g = Q0/Qe = N^2*R/(2*Z0) (×2 if line ends in an open stub lambda/4 beyond the DR); Gamma(resonance) = N^2*R/(2*Z0 + N^2*R) = g/(1 + g) -> g = Gamma/(1 - Gamma) from measurement | Q0, N^2*R, Z0 | only N^2*R is determinable | calc | §13.2 eq.(13.35)–(13.37), Figs.13.10–13.11, p.617–620 | high |
| POZAR-413 | rf | Worked series-feedback DRO (anchor): 2.4 GHz WLAN LO, BJT S11 = 1.8∠130, S12 = 0.4∠45, S21 = 3.8∠36, S22 = 0.7∠-63, resonator Q0 = 1000 | choose GS = 0.6∠-130 -> Gout = 10.7∠132 (Zout = -43.7 + j6.1 ohm) -> ZL = 5.5 - j6.1 ohm (match: line 0.481λ, OC stub 0.307λ); lr = 0.431λ puts GS' = 0.6∠180 -> resonator ZS' = 12.5 ohm, coupling g = 0.25 (open-stub termination); \|Gout\| collapses within a few hundredths of a percent of f0 (Fig.13.12b) | — | — | calc | §13.2 Ex.13.4, Fig.13.12, p.620–622 | high |
| POZAR-414 | rf | Phase noise definition and relations: SSB noise power in 1 Hz at offset fm relative to carrier (dBc/Hz); e.g. cellular spec -110 dBc/Hz at 25 kHz; small-angle modulation relations | L(fm) = Pn(1 Hz SSB)/Pc = theta_p^2/4 = theta_rms^2/2; two-sided S_theta(fm) = 2*L(fm) = theta_rms^2; white additive noise: S_theta = k*T0*F/Pc | theta_p, F, Pc | theta_p << 1 | calc | §13.3 eq.(13.38)–(13.44), p.622–624 | high |
| POZAR-415 | rf | Leeson oscillator phase-noise model (resonator loaded Q0, 1/f corner f_alpha, amplifier NF F, oscillator power P0); SSB L(fm) = S_phi/2 | S_phi(dw) = (k*T0*F/P0)*[K*w_alpha*wh^2/dw^3 + wh^2/dw^2 + K*w_alpha/dw + 1], wh = w0/(2*Q0) (resonator half-power bandwidth); close-in 1/f^3 (-18 dB/octave), then 1/f^2 (-12 dB/oct) if fh > f_alpha (low Q) or 1/f (-6 dB/oct) if fh < f_alpha (high Q); floor k*T0*F (k*T0 = -174 dBm/Hz); close-in noise ∝ 1/Q0^2 | Q0, f0, F, P0, f_alpha, K | feedback oscillator with high-Q resonator | calc | §13.3 eq.(13.45)–(13.49), Fig.13.17, p.624–626 | high |
| POZAR-416 | components | 1/f (flicker) noise corner frequencies by device (drives close-in phase noise): Si JFET 50–100 Hz; Si BJT 5–50 kHz; GaAs MESFET 2–10 MHz or higher -> prefer BJT/JFET for low close-in phase noise | f_alpha as stated | device type | — | review | §13.3 p.625 | high |
| POZAR-417 | rf | Reciprocal mixing: LO phase noise down-converts adjacent interferers; maximum LO phase noise for adjacent-channel rejection S | L(fm) (dBc/Hz) = C(dBm) - S(dB) - I(dBm) - 10*log10(B_IF in Hz), fm = interferer offset | C, I, S, B | selectivity usually the most severe phase-noise impact | calc | §13.3 eq.(13.50), Fig.13.18, p.626–627 | high |
| POZAR-418 | rf | Worked GSM LO phase-noise requirement (anchor): C = -99 dBm, S = 9 dB, B = 200 kHz; interferers -23 dBm @ 3 MHz, -33 dBm @ 1.6 MHz, -43 dBm @ 0.6 MHz | L = -138, -128, -118 dBc/Hz respectively -> requires a phase-locked synthesizer; GSM bit errors dominated by reciprocal mixing, not thermal noise | — | — | calc | §13.3 Ex.13.5, p.627 | high |
| POZAR-419 | rf | Frequency multiplication multiplies phase noise | noise increase = 20*log10(n) dB (doubler >= 6 dB, tripler >= 9.5 dB); reactive (varactor/SRD) multipliers add little noise, resistive multipliers can add significant noise | n | — | calc | §13.4 p.628 | high |
| POZAR-420 | rf | Multiplier type selection and efficiency limits: reactive (varactor, step-recovery) ideally 100% (Manley–Rowe), varactors for n = 2–4, SRDs for higher n; practical varactor doublers/triplers 50–80% at 50 GHz, varactor fc can exceed 1000 GHz but need n*f0 << fc; resistive (Schottky) efficiency <= 1/m^2 but wider bandwidth and more stable; transistor multipliers give conversion gain, better bandwidth, less DC/input power, limited by fT; antiparallel diode pair rejects all even harmonics | Manley–Rowe single source: sum_{n>=2} Pn0 = -P10 -> Pn0/P10 = 1 (ideal reactive); resistive: Pm/P1 <= 1/m^2 | n, device | idler terminations needed (e.g. varactor tripler needs 2f0 idler current path) | calc | §13.4 eq.(13.59)–(13.69), p.628–633 | high |
| POZAR-421 | rf | Class-B-biased FET frequency multiplier: harmonic drain current from a half-cosine pulse of width tau; optimum tau/T = 0.35 (n = 2), 0.22 (n = 3), practical tau/T usually larger; limited to doublers/triplers; output typically < 10 dBm up to 60–100 GHz | I0 = 2*tau*Imax/(pi*T); In = (4*tau*Imax/(pi*T))*cos(n*pi*tau/T)/(1 - (2*n*tau/T)^2); cos(pi*tau/T) = (2Vt - Vgmax - Vgmin)/(Vgmax - Vgmin); Vgg = (Vgmax + Vgmin)/2 (book prints "-" but evaluates the mean); Vg = Vgmax - Vgg; Pin = \|Vg\|^2*Ri/(2*\|Ri - j/(w0*Cgs)\|^2); RL = (Vdmax - Vdmin)/(2*In); Pn = \|In\|^2*RL/2; Gc = Pn/Pavail | device V/I limits | drain tank resonates Cds at n*w0, shorts other harmonics | calc | §13.4 eq.(13.70)–(13.80), p.633–635 | high |
| POZAR-422 | rf | Worked FET doubler (anchor): 12 -> 24 GHz, GaAs MESFET Vt = -2.0 V, Ri = 10 ohm, Cgs = 0.20 pF, Cds = 0.15 pF, Rds = 40 ohm; Vgmax = 0.2 V, Vgmin = -6.0 V, Vdmax = 5.0 V, Vdmin = 1.0 V, Imax = 80 mA | Vgg = -2.9 V, Vg = 3.1 V; Pin = 10.7 mW; cos(pi*tau/T) = 0.29 -> tau/T = 0.406; I2 = 0.262*Imax = 21.0 mA; RL = 95.2 ohm; P2 = 21.0 mW; Gc = 2.9 dB; XL = 1/(2*w0*Cds) = 44.2 ohm (0.293 nH) | — | — | calc | §13.4 Ex.13.6, p.636 | high |
| POZAR-423 | rf | Mixer frequency plan: up-conversion fRF = fLO ± fIF (USB/LSB); down-conversion fIF = fRF - fLO; image at fIM = fLO - fIF, separated from the wanted RF by 2*fIF and indistinguishable at IF unless pre-selected (filtered) at RF; two LO choices fLO = fRF ± fIF; most receivers use high-side LO (smaller LO tuning ratio) | f_image = f_RF ± 2*f_IF (opposite side of LO) | fRF band, fIF, LO side | — | calc | §13.5 eq.(13.81)–(13.89), p.637–639 | high |
| POZAR-424 | rf | Worked image check (anchor): IS-54 receive 869–894 MHz, IF 87 MHz, 30 kHz channels | LO = 956–981 MHz (high side) or 782–807 MHz (low side); with high-side LO the image is 1043–1068 MHz, well outside the receive band | — | — | calc | §13.5 Ex.13.7, p.641 | high |
| POZAR-425 | rf | Mixer conversion loss and typical values: diode mixers 4–7 dB (1–10 GHz); transistor mixers lower loss or a few dB conversion gain; minimum loss typically for LO drive 0–10 dBm (nonlinear analysis needed) | Lc = 10*log10(P_RF,avail/P_IF,avail) >= 0 dB | LO power | receivers: minimize Lc (front-end NF) | measure | §13.5 eq.(13.90), p.639 | high |
| POZAR-426 | noise | Mixer noise figure: practical 1–5 dB (diode mixers generally lower than transistor mixers); SSB noise figure is twice (3 dB above) the DSB value because noise from both sidebands converts to IF | F_SSB = 2*F_DSB (T_SSB = 2*T_DSB) | F_DSB | equal conversion gain for signal and image | calc | §13.5 eq.(13.91)–(13.97), p.640–641; Problem 13.19 | high |
| POZAR-427 | rf | Mixer linearity and isolation typicals: IIP3 15–30 dBm; LO-to-RF isolation 20–40 dB (depends on diplexing coupler); LO leakage out of the RF port is radiated by the antenna and is regulated -> put a bandpass filter between antenna and mixer or an LNA ahead of the mixer | IIP3 15–30 dBm; isolation 20–40 dB | mixer datasheet | receivers driving RF port from antenna | review | §13.5 p.641 | high |
| POZAR-428 | rf | Single-ended diode mixer: diplexer combines RF and LO; DC blocks and RF choke for bias; LPF selects IF; IF current from the square-law term | i_IF = (Gd'/2)*V_RF*V_LO*cos(w_IF*t) | Gd', V_RF, V_LO | small-signal; also usable as up-converter | calc | §13.5 eq.(13.98)–(13.101), Fig.13.25, p.642–643 | high |
| POZAR-429 | rf | Single-ended FET mixer: bias gate near pinch-off so the LO pumps gm (strongest nonlinearity); g1 (fundamental Fourier coefficient of gm(t)) measured, typically ≈ 10 mS; drain bypass returns LO; maximum (conjugately matched) conversion gain | Gc = g1^2*Rd/(4*w_RF^2*Cgs^2*Ri) (Rg = Ri, Xg = 1/(w_RF*Cgs), RL = Rd, XL = 0) | g1, Rd, Ri, Cgs, f_RF | excludes matching-network losses | calc | §13.5 eq.(13.102)–(13.108), p.643–645 | high |
| POZAR-430 | rf | Worked FET mixer gain (anchor): 2.4 GHz WLAN, Rd = 300 ohm, Ri = 10 ohm, Cgs = 0.3 pF, g1 = 10 mS | Gc = 36.6 (15.6 dB) maximum, before matching losses | — | — | calc | §13.5 Ex.13.8, p.646 | high |
| POZAR-431 | rf | Balanced mixers: 90-deg hybrid version gives an ideal RF input match over a wide band (diode reflections cancel at the RF port, appear at the LO port) but RF–LO isolation depends on diode matching; 180-deg hybrid version gives ideal RF–LO isolation over a wide band; both reject all even-order intermodulation products | 90 deg: V_RF,refl = 0; V_LO,refl = j*Gamma*V_RF | diode match | — | calc | §13.5 eq.(13.109)–(13.116), Fig.13.29, p.646–649 | high |
| POZAR-432 | rf | Image-reject mixer (RF 90-deg hybrid, two mixers, IF 90-deg hybrid): LSB and USB appear at separate IF ports (also works as SSB modulator); no loss beyond normal conversion loss, but a good hybrid at the (low) IF is hard, and losses/NF are usually higher than a simple mixer | v_LSB = (K*V_LO*V_L/2)*cos(w_IF*t); v_USB = (K*V_LO*V_U/2)*sin(w_IF*t) | — | — | calc | §13.5 eq.(13.117)–(13.122), Fig.13.31, p.649–650 | high |
| POZAR-433 | rf | Singly balanced differential FET mixer and Gilbert cell: LO-switched upper pair (biased slightly above pinch-off) commutates the RF current of the lower transconductor; RF and LO cancel at the IF without filtering; IF circuit must return LO to ground; tail current source or inductive degeneration; Gilbert cell = double-balanced, fully differential RF/LO/IF, common in CMOS RFICs | g(t) = 1/2 + (2/pi)*cos(w_LO*t) - (2/(3*pi))*cos(3*w_LO*t) + ...; v_IF(after LPF) = -(2/pi)*gm*V_RF*RD*cos(w_IF*t) | gm, RD | ideal switching | calc | §13.5 eq.(13.123)–(13.127), Figs.13.32–13.33, p.650–652 | high |
| POZAR-434 | rf | Double-balanced (4-diode, two hybrids/transformers) mixer: good isolation between all ports, rejects all even harmonics of RF and LO, very good conversion loss, highest IP3, but less-than-ideal RF input match; antiparallel-diode subharmonic mixer: LO at half frequency (w_LO = (w_RF - w_IF)/2), suppresses the fundamental mixing product (mm-wave) | see Table 13.1 (§2 T2.18) | topology | — | review | §13.5 Figs.13.34–13.35, Table 13.1, p.652–653 | high |
| POZAR-435 | rf | Phase detector from a single-balanced mixer: 90-deg hybrid version outputs i = k*v0^2*sin(theta); 180-deg hybrid version outputs i = k*v0^2*cos(theta) | as stated | theta | stated in Problem 13.21 | calc | §13 Problem 13.21, p.657 | medium |
| POZAR-436 | rf | Manley–Rowe bound for a reactive up-converter (f3 = f1 + f2, others open-circuited): maximum conversion gain | G_max = 1 + w2/w1 (= f3/f1 for LO f2) | f1 (RF), f2 (LO) | lossless nonlinear reactance; stated in Problem 13.13 | calc | §13 Problem 13.13, p.656 | medium |
| POZAR-437 | antenna | Antenna types by band/gain: wire (dipole, monopole, loop, Yagi) low gain, HF–UHF, light/cheap/simple; aperture (horns, reflectors, lenses, reflectarrays) moderate–high gain at microwave/mm-wave; printed (patch, printed dipole/slot) photolithographic with feed on the same substrate, easily arrayed; arrays/phased arrays steer beam and set sidelobes via element amplitude/phase | — | f, gain need | selection | review | §14.1 p.659–660 | high |
| POZAR-438 | antenna | Far-field (Fraunhofer) distance for measurement/coupling analysis: spherical-wave phase error < pi/8 (22.5 deg) across the aperture; use at least 2λ for electrically small antennas | R_ff = 2*D^2/λ (D = largest antenna dimension); R_ff >= 2λ | D, f | anchor: 18 in (0.457 m) DBS dish at 12.4 GHz (λ = 2.42 cm) -> R_ff = 17.3 m | calc | §14.1 eq.(14.5), Ex.14.1, p.661 | high |
| POZAR-439 | antenna | Far-field relations: E-field ∝ exp(-j*k0*r)/r, H = E/eta0 (eta0 = 377 ohm); radiation intensity and total radiated power | U(theta,phi) = (\|F_theta\|^2 + \|F_phi\|^2)/(2*eta0) (W/sr); P_rad = ∫∫ U*sin(theta) dtheta dphi | pattern F | far zone | calc | §14.1 eq.(14.1)–(14.7), p.660–662 | high |
| POZAR-440 | antenna | Directivity and typical values: isotropic D = 1 (0 dBi); wire dipole 2.2 dB; microstrip patch 7.0 dB; waveguide horn 23 dB; parabolic reflector 35 dB; short dipole D = 1.5 (1.76 dB), HPBW 90 deg | D = 4*pi*U_max/P_rad | pattern | — | calc | §14.1 eq.(14.8), Ex.14.2, p.663–664 | high |
| POZAR-441 | antenna | Pencil-beam directivity from orthogonal-plane half-power beamwidths (approximate; not for omnidirectional patterns); beamwidth and directivity are not uniquely related (sidelobes matter) | D ≈ 32,400/(theta1*theta2), theta in degrees | HPBWs | pencil beams | calc | §14.1 eq.(14.9), p.663 | high |
| POZAR-442 | antenna | Radiation efficiency and gain: G <= D; mismatch and polarization losses are external to the antenna (realized gain includes mismatch) | eta_rad = P_rad/P_in = 1 - P_loss/P_in; G = eta_rad*D | P_loss, D | — | calc | §14.1 eq.(14.10),(14.11), p.664–665 | high |
| POZAR-443 | antenna | Aperture antennas: maximum directivity of an electrically large aperture and aperture efficiency (taper, blockage, spillover); receive effective area | D_max = 4*pi*A/λ^2 (e.g. 2λ x 3λ horn -> 24pi ≈ 19 dB); D = eta_ap*4*pi*A/λ^2; Pr = Ae*S_avg; Ae = D*λ^2/(4*pi) (use G for lossy antennas) | A, λ, eta_ap | Ae ≈ physical area only for large apertures | calc | §14.1 eq.(14.12)–(14.15), p.665–666 | high |
| POZAR-444 | noise | Background (sky/ground) noise temperatures at low microwave frequencies: sky toward zenith 3–5 K, sky toward horizon 50–100 K, ground 290–300 K; atmospheric absorption peaks at 22 GHz (H2O) and 60 GHz (O2) raise sky temperature (at 60 GHz a high-gain antenna through the atmosphere looks like a 290 K load) | T_B values as stated; Fig.14.6 (sea level, 15 degC, 7.5 g/m^3 water vapour; graph) | elevation, f | receiver sensitivity budgets | calc | §14.1 Figs.14.5–14.6, p.667–668 | high (values) / medium (graph) |
| POZAR-445 | noise | Antenna brightness temperature (pattern-weighted background) and antenna noise temperature including ohmic loss | Tb = ∫∫ TB(theta,phi)*D(theta,phi)*sin(theta) / ∫∫ D*sin(theta); TA = eta_rad*Tb + (1 - eta_rad)*Tp | TB distribution, D pattern, eta_rad, Tp | TA referenced at antenna terminals; aperture efficiency adds no noise (radiation efficiency does) | calc | §14.1 eq.(14.17),(14.18), p.668–669, 671 | high |
| POZAR-446 | noise | Sidelobes can dominate antenna noise: idealized high-gain pattern (sidelobes -20 dB) facing a 10x/0.1x/1x background gives Tb = 86.4 K with most noise from the sidelobe region — do not assume main-beam-only noise when sidelobes see hot ground | Tb per POZAR-445 | pattern, scene | — | calc | §14.1 Ex.14.3, Fig.14.7, p.669–670 | high |
| POZAR-447 | noise | System noise temperature at the receiver input for antenna -> lossy line (loss L, temperature Tp) -> receiver, with antenna mismatch Gamma | TS = ((1 - \|Gamma\|^2)/L)*(eta_rad*Tb + (1 - eta_rad)*Tp) + ((L - 1)/L)*(1 + \|Gamma\|^2/L)*Tp; matched: TS = (1/L)*(eta_rad*Tb + (1 - eta_rad)*Tp) + ((L - 1)/L)*Tp | Tb, eta_rad, Tp, L, Gamma | reference at receiver input | calc | §14.1 eq.(14.19),(14.20), p.670–671 | high |
| POZAR-448 | antenna | Receive figure of merit G/T: input SNR ∝ G/TA; raise it with antenna gain (also reduces hot low-elevation pickup) unless omni coverage is required | G/T(dB/K) = 10*log10(G/T_sys) | G, TA (or system T) | — | calc | §14.1 eq.(14.21), p.671 | high |
| POZAR-449 | requirements | Wireless system classification: point-to-point (high-gain fixed antennas: satellite, utility data, cellular backhaul), point-to-multipoint (broadcast), multipoint-to-multipoint (cellular, WLAN); simplex / half-duplex / full-duplex (FDD separate bands or TDD time slots) | — | — | requirements framing | review | §14.2 p.671–672 | high |
| POZAR-450 | requirements | Satellite orbits: GEO ≈ 36,000 km, 24 h period (fixed over equator; long delay, weak signal for handhelds); LEO 500–2000 km, visible from a point for a few minutes to ~20 min (needs large constellations) | — | — | — | review | §14.2 p.672 | high |
| POZAR-451 | rf | Friis free-space link equation (maximum possible received power; reduce for mismatch, polarization, propagation, multipath) and EIRP | S_avg = Gt*Pt/(4*pi*R^2); Pr = Gt*Gr*λ^2*Pt/(4*pi*R)^2; EIRP = Pt*Gt | Pt, Gt, Gr, λ, R | far field, matched, co-polarized | calc | §14.2 eq.(14.22)–(14.25), p.673–674 | high |
| POZAR-452 | rf | Radio path loss falls only as 1/R^2 vs the exponential e^(-2*alpha*z) of any cable/waveguide/fiber, so long unrepeated links favour radio | L0 vs alpha*z | R, alpha | unless repeaters are possible | review | §14.2 p.674 | high |
| POZAR-453 | rf | Link budget in dB with path loss, line losses, atmospheric attenuation, mismatch and polarization terms | L0(dB) = 20*log10(4*pi*R/λ); Pr(dBm) = Pt - Lt + Gt - L0 - LA + Gr - Lr; mismatch loss L_imp = -10*log10(1 - \|Gamma\|^2); polarization: V->H zero, V->circular half power (3 dB) | all terms | — | calc | §14.2 eq.(14.26)–(14.28), p.674–675 | high |
| POZAR-454 | requirements | Link margin must be positive; typical 3–20 dB; fade margin for satellite links above 10 GHz often 20 dB or more (heavy rain); avoid excessive margin (cost) | LM(dB) = Pr - Pr(min) > 0 | Pr, Pr(min) from required CNR/SNR | — | calc | §14.2 eq.(14.29), p.675 | high |
| POZAR-455 | rf | Worked DBS downlink (anchor): 12.2–12.7 GHz (use 12.45 GHz, λ = 0.0241 m), Pt = 120 W (50.8 dBm), Gt = 34 dB, R = 39,000 km (30 deg slant), Gr = 33.5 dB (18 in dish), Tb = 50 K, LNB NF = 0.7 dB, B = 20 MHz, CNR_min = 15 dB | L0 = 206.2 dB; Pr = -87.9 dBm (1.63e-12 W); Te = Tb + (F - 1)*T0 = 100.8 K; G/T = 13.5 dB/K; CNR = 58.6 (17.7 dB); link margin 2.7 dB | — | — | calc | §14.2 Ex.14.4, Fig.14.10, p.675–676 | high |
| POZAR-456 | rf | Receiver gain distribution: total gain ≈ 100–120 dB for -100 to -120 dBm inputs; avoid more than about 50–60 dB of gain in any one frequency band (instability/oscillation); spread gain over RF, IF and baseband (also cheaper at lower f); obtain selectivity with sharp IF filters and a tuned LO, not narrow tunable RF filters | G_band <= 50–60 dB | gain plan | — | review | §14.2 p.677 | high |
| POZAR-457 | rf | Receiver architecture trade-offs: TRF (all gain at RF, poor selectivity, obsolete); direct conversion/homodyne (zero IF, no image, simple/cheap, but LO must be very precise/stable; Doppler radars); superheterodyne (IF between RF and baseband, sharp IF filters and IF gain, LO tuning, most common); dual-conversion superhet at microwave/mm-wave for LO stability | — | architecture choice | — | review | §14.2 Figs.14.11–14.13, p.677–678 | high |
| POZAR-458 | noise | Receiver system noise temperature and SNR with antenna, lossy line and RF amp / mixer / IF chain; use temperatures, not noise figure, when TA != T0 | T_REC = T_RF + T_M/G_RF + T_IF*L_M/G_RF; T_TL = (L_T - 1)*Tp; T_SYS = eta_rad*Tb + (1 - eta_rad)*Tp + (L_T - 1)*Tp + L_T*T_REC; Ni = k*B*TA; So/No = Si/(k*B*T_SYS) | component G, F (T = (F-1)T0), losses | noise of later stages usually negligible | calc | §14.2 eq.(14.27)–(14.34) (book reuses numbers 14.27–14.29), p.679–680 | high |
| POZAR-459 | noise | Worked receiver SNR (anchor): f = 4.0 GHz, B = 1 MHz, GA = 26 dB, eta_rad = 0.90, Tp = 300 K, Tb = 200 K, LT = 1.5 dB, G_RF = 20 dB, F_RF = 3.0 dB, L_M = 6.0 dB, F_M = 7.0 dB, G_IF = 30 dB, F_IF = 1.1 dB, Si = -80 dBm | T_M = 1163 K, T_RF = 289 K, T_IF = 84 K; T_REC = 304 K; T_TL = 123 K; TA = 210 K; Ni = -115 dBm -> Si/Ni = 35 dB; T_SYS = 762 K; k*B*T_SYS = -110 dBm -> So/No = 30 dB | — | — | calc | §14.2 Ex.14.5, p.680–681 | high |
| POZAR-460 | rf | Digital-link energy per bit relations; for a fixed SNR the Eb/n0 falls (BER rises) as bit rate rises; receiver bandwidth is 1 to several times the bit rate | Eb = S*Tb = S/Rb; Eb/n0 = S/(n0*Rb) = (S/N)*(B/Rb); n0 = k*T_sys | S, Rb, B, T_sys | coherent detection | calc | §14.2 eq.(14.35)–(14.37), p.682–683 | high |
| POZAR-461 | rf | Required Eb/n0 for Pb = 1e-5 and bandwidth efficiency by modulation: ASK 15.6 dB (1 bps/Hz), FSK 12.6 (1), BPSK 9.6 (1), QPSK 9.6 (2), 8-PSK 13.0 (3), 16-PSK 18.7 (4), 16-QAM 13.4 (4), 64-QAM 17.8 (6); BER vs Eb/n0 curves in Fig.14.16 (coherent, Gray-coded QPSK) | see Table 14.1 (§2 T2.20) | modulation, BER target | — | calc | §14.2 Table 14.1, Fig.14.16, p.683–684 | high |
| POZAR-462 | rf | Worked LEO downlink data-rate limit (anchor): R = 940 km, λ = 1.875 cm, QPSK, Pt = 80 W (49 dBm), Gt = 20 dB, Gr = 1 dB, T_sys = 750 K, LA = 2 dB, LM = 10 dB, Pb = 0.01 (Eb/n0 ≈ 5 dB = 3.16 from Fig.14.16) | L0 = 176.0 dB; Pr = -108 dBm; Smin = -118 dBm (1.58e-15 W); Rb = Smin/(k*T_sys*(Eb/n0)) = 48 kbps | — | — | calc | §14.2 Ex.14.6, p.683–684 | high |
| POZAR-463 | requirements | GPS signal facts for receiver design: L1 = 1575.42 MHz (C/A civil, also P), L2 = 1227.60 MHz (P, military); 24 MEO satellites at 20,200 km, 12 h orbits; needs >= 4 satellites (3 if altitude known); received level ≈ -130 dBm with a 0 dBi antenna (below noise; spread-spectrum gain recovers it); L1 accuracy ≈ 100 ft; differential GPS ≈ 1 cm; dominant error is atmospheric/ionospheric delay | as stated | — | 2012-era | review | §14.2 p.687–688 | high |
| POZAR-464 | requirements | Short-range radio orientation: IEEE 802.11 Wi-Fi at 2.4 / 5.7 GHz ISM, a/b/g up to 54 Mbps, n up to 150 Mbps (MIMO), indoor range < a few hundred feet; Bluetooth 2.4 GHz, 1–100 mW for 1–100 m, 1–24 Mbps; 60 GHz WLAN demo 59–62 GHz at 2.8 Gbps | as stated | — | 2012-era | review | §14.2 p.688–689 | high |
| POZAR-465 | requirements | Other system orientation: DBS 10–12 GHz, QPSK, ≈ 40 Mbps, 120 W per channel, opposite circular polarizations for co-located satellites (DBS-1/-2 at 101.2/100.8 deg); point-to-point backhaul at 18, 24, 38 GHz, > 50 Mbps with high-gain antennas; passive RFID tags rectify the interrogation signal to power CMOS logic; IMT-2000 3G 2 Mbps fixed / 144 kbps mobile, LTE goal 100/50 Mbps | as stated | — | 2012-era | review | §14.2 p.686–689 | high |
| POZAR-466 | rf | Radar equation (monostatic) and maximum range; received power ∝ 1/R^4; pulse integration of N pulses improves detectability by ≈ N | Pr = Pt*G^2*λ^2*sigma/((4*pi)^3*R^4); R_max = (Pt*G^2*sigma*λ^2/((4*pi)^3*P_min))^(1/4); sigma = Ps/St (m^2) | Pt, G, λ, sigma, P_min | ideal; propagation, statistics, interference reduce range | calc | §14.3 eq.(14.38)–(14.42), p.691–692 | high |
| POZAR-467 | rf | Worked radar range (anchor): 10 GHz pulse radar, G = 28 dB (631), Pt = 2 kW, sigma = 12 m^2, P_min = -90 dBm (1e-12 W), λ = 0.03 m | R_max = 8114 m | — | — | calc | §14.3 Ex.14.7, p.693 | high |
| POZAR-468 | rf | Pulse radar timing: pulse widths 100 ms (as printed) to 50 ns — shorter gives better range resolution, longer better post-processing SNR; PRF 100 Hz–100 kHz — higher PRF more pulses per unit time, lower PRF avoids range ambiguity (ambiguous when R > c*Tr/2); share one LO for Tx up-conversion and Rx down-conversion to avoid drift | R_unamb = c/(2*f_r) | tau, f_r | — | calc | §14.3 p.693; Problem 14.16 | high |
| POZAR-469 | rf | Pulse-radar T/R isolation must be 80–100 dB (transmitter leakage would mask the return or damage the receiver); circulators give only 20–30 dB, so use high-isolation T/R switches (more in series if needed); CW Doppler radars can use a circulator because the IF filter rejects DC | isolation >= 80–100 dB (pulse) | Pt, Rx damage level | — | review | §14.3 p.693–694 | high |
| POZAR-470 | rf | Doppler shift and CW Doppler radar filter: pass the expected Doppler band, reject zero frequency (clutter, leakage, 1/f noise); sign (approach/recede) needs an SSB (I/Q) mixer; pulse-Doppler separates moving targets from clutter | fd = 2*v*f0/c (approaching +, receding -) | v range, f0 | e.g. 12 GHz, 1–20 m/s -> 80–1600 Hz (Problem 14.17 answer) | calc | §14.3 eq.(14.43), Fig.14.22, p.694–695 | high |
| POZAR-471 | rf | Radar cross section behaviour of a sphere of radius a: Rayleigh region (a << λ) sigma ∝ (a/λ)^4; optical region (a >> λ) sigma = pi*a^2; resonance region oscillates and can be large; typical RCS values in Table 14.3 (§2 T2.21); reduce RCS with radar-absorbing (lossy) materials | sigma per region | a/λ | monostatic | calc | §14.3 Fig.14.23, Table 14.3, p.695–696 | high |
| POZAR-472 | test | Radiometry: emissivity and brightness temperature (a body never looks hotter than its physical temperature) | e = P/(k*T*B), 0 <= e <= 1; TB = e*T | e, T | passive remote sensing | calc | §14.4 eq.(14.44),(14.45), p.697 | high |
| POZAR-473 | test | Total-power radiometer errors: noise-fluctuation error falls with bandwidth x integration time, but gain drift usually dominates -> use Dicke switching (10–1000 Hz, faster than gain drift > 1 s) against a reference noise source | Vo = G*(TB + TR)*k*B; dT_N = (TB + TR)/sqrt(B*tau); dT_G = (TB + TR)*dG/G; example 10 GHz, B = 100 MHz, TR = 500 K, tau = 0.01 s, dG/G = 0.01, TB = 300 K -> dT_N = 0.8 K, dT_G = 8 K | TB, TR, B, tau, dG/G | typical TB range 50–300 K | calc | §14.4 eq.(14.46)–(14.48), p.699–700 | high |
| POZAR-474 | rf | Atmospheric refractivity, radio horizon and ducting: permittivity decreases with height and bends waves toward Earth (use effective Earth radius kR, k = 4/3 average); temperature inversions cause ducting (duct heights 50–500 ft) | er = 1 + 1e-6*(79*P/T - 11*V/T + 3.8e5*V/T^2) (P, V in mbar; T in K); horizon d = sqrt(2*R*h) (use k*R) | P, T, V, h | statistical; radar elevation errors near horizon | calc | §14.5 eq.(14.49),(14.50), p.701–702 | high |
| POZAR-475 | rf | Atmospheric attenuation: negligible below 10 GHz; peaks at 22.2 and 183.3 GHz (H2O) and 60 and 120 GHz (O2); windows near 35, 94 and 135 GHz; rain/snow/fog add loss at higher f; sensing radiometers operate near 20 or 55 GHz; 60 GHz used for spacecraft crosslinks (Earth jamming/eavesdropping suppressed) | Fig.14.29 dB/km vs f (sea level and 9150 m; graph) | f, path | include LA in Friis/radar budgets | calc | §14.5 Fig.14.29, p.702–703 | medium (graph) |
| POZAR-476 | rf | Ground effects: direct + ground-reflected wave interfere (fading = long-term, scintillation = short-term); diversity (frequency, polarization or space, whose fades are nearly independent) reduces fading; diffraction slightly extends range beyond the horizon (small at microwave; larger with obstacles); clutter echoes from terrain/sea mask targets | — | geometry | — | review | §14.5 Fig.14.30, p.703–704 | high |
| POZAR-477 | rf | Plasma propagation: waves propagate only above the plasma frequency; ionosphere average f_p ≈ 8 MHz (lower frequencies reflect -> beyond-horizon HF); dense re-entry plasma causes communication blackout and antenna mismatch | eps_e = eps0*(1 - wp^2/w^2); wp = sqrt(N*q^2/(m*eps0)) | N (electrons/m^3) | isotropic plasma (no B field) | calc | §14.5 eq.(14.51),(14.52), p.704 | high |
| POZAR-478 | compliance | Microwave oven design facts: magnetron at 2.45 GHz (915 MHz for deeper penetration), 500–1500 W; mode stirrer and turntable against standing-wave hot spots; heat-to-input efficiency < 50%; door needs close tolerances, RF absorber and a lambda/4 choke flange; US leakage limit: power density at 5 cm from any point <= 1 mW/cm^2 | leakage <= 1 mW/cm^2 at 5 cm | — | US regulation as cited | measure | §14.6 p.705, 707 | high |
| POZAR-479 | compliance | RF exposure: IEEE C95.1-2005 power-density limits (100 MHz–100 GHz) for general population (30 min average) and controlled/occupational environments (6 min average), lower limits at lower frequency (deeper penetration); handheld devices in the US: SAR <= 1.6 W/kg averaged over 1 g (partial body); EU: SAR < 2 W/kg over 10 g; US microwave ovens: <= 1 mW/cm^2 at 5 cm | SAR = sigma*\|E\|^2/(2*rho) (W/kg); limits as stated; Fig.14.32 gives power-density limit vs frequency (graph) | E in tissue, sigma, rho; power density | as cited 2012 | calc | §14.6 eq.(14.53), Fig.14.32, p.706–707 | high (SAR) / medium (graph) |
| POZAR-480 | compliance | Exposure power density near a transmitting antenna; evaluate main beam and worst-case sidelobe | S = Pt*Gt/(4*pi*R^2); anchor: 18 GHz link, Gt = 36 dB (4000), Pt = 10 W, R = 20 m -> 8 W/m^2 (main beam), 0.8 W/m^2 (-10 dB sidelobe), below the general-population limit | Pt, Gt, R | far field assumed | calc | §14.6 Ex.14.8, p.707–708 | high |
| POZAR-481 | power | Wireless power transfer orientation: solar power satellite concept (5 x 10 km array, 1 km antenna, ≈ 5 GW) doubtful on cost/safety; beamed power to small drones demonstrated; RFID powering feasible because CMOS DC needs are tiny; ambient RF harvesting generally not feasible when other sources exist | — | — | — | review | §14.6 p.705–706 | high |
| POZAR-482 | transmission-line | Reflection/return-loss/SWR/insertion-loss and skin-depth reference formulas | RL = -20*log10\|Gamma\|; IL = -20*log10\|T\|; SWR = (1 + \|Gamma\|)/(1 - \|Gamma\|); 1 neper = 8.686 dB; Rs = sqrt(w*mu/(2*sigma)); delta_s = sqrt(2/(w*mu*sigma)) | Gamma, T, sigma, f | — | calc | "Useful Results" end matter, p.(back) | high |
## 2. Formulas & tables (numbers)

### T2.1 Maximally flat (Butterworth) low-pass prototype element values (g0 = 1, wc = 1 rad/s, N = 1 to 10) — Table 8.3, p.404 (source: Matthaei, Young, Jones)

| N | g1 | g2 | g3 | g4 | g5 | g6 | g7 | g8 | g9 | g10 | g11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2.0000 | 1.0000 | | | | | | | | | |
| 2 | 1.4142 | 1.4142 | 1.0000 | | | | | | | | |
| 3 | 1.0000 | 2.0000 | 1.0000 | 1.0000 | | | | | | | |
| 4 | 0.7654 | 1.8478 | 1.8478 | 0.7654 | 1.0000 | | | | | | |
| 5 | 0.6180 | 1.6180 | 2.0000 | 1.6180 | 0.6180 | 1.0000 | | | | | |
| 6 | 0.5176 | 1.4142 | 1.9318 | 1.9318 | 1.4142 | 0.5176 | 1.0000 | | | | |
| 7 | 0.4450 | 1.2470 | 1.8019 | 2.0000 | 1.8019 | 1.2470 | 0.4450 | 1.0000 | | | |
| 8 | 0.3902 | 1.1111 | 1.6629 | 1.9615 | 1.9615 | 1.6629 | 1.1111 | 0.3902 | 1.0000 | | |
| 9 | 0.3473 | 1.0000 | 1.5321 | 1.8794 | 2.0000 | 1.8794 | 1.5321 | 1.0000 | 0.3473 | 1.0000 | |
| 10 | 0.3129 | 0.9080 | 1.4142 | 1.7820 | 1.9754 | 1.9754 | 1.7820 | 1.4142 | 0.9080 | 0.3129 | 1.0000 |

(Cross-check, not from text: these equal g_k = 2*sin((2k-1)*pi/(2N)), g_{N+1} = 1.)

### T2.2 Equal-ripple (Chebyshev) low-pass prototype element values, 0.5 dB ripple (g0 = 1, wc = 1, N = 1 to 10) — Table 8.4, p.406

| N | g1 | g2 | g3 | g4 | g5 | g6 | g7 | g8 | g9 | g10 | g11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.6986 | 1.0000 | | | | | | | | | |
| 2 | 1.4029 | 0.7071 | 1.9841 | | | | | | | | |
| 3 | 1.5963 | 1.0967 | 1.5963 | 1.0000 | | | | | | | |
| 4 | 1.6703 | 1.1926 | 2.3661 | 0.8419 | 1.9841 | | | | | | |
| 5 | 1.7058 | 1.2296 | 2.5408 | 1.2296 | 1.7058 | 1.0000 | | | | | |
| 6 | 1.7254 | 1.2479 | 2.6064 | 1.3137 | 2.4758 | 0.8696 | 1.9841 | | | | |
| 7 | 1.7372 | 1.2583 | 2.6381 | 1.3444 | 2.6381 | 1.2583 | 1.7372 | 1.0000 | | | |
| 8 | 1.7451 | 1.2647 | 2.6564 | 1.3590 | 2.6964 | 1.3389 | 2.5093 | 0.8796 | 1.9841 | | |
| 9 | 1.7504 | 1.2690 | 2.6678 | 1.3673 | 2.7239 | 1.3673 | 2.6678 | 1.2690 | 1.7504 | 1.0000 | |
| 10 | 1.7543 | 1.2721 | 2.6754 | 1.3725 | 2.7392 | 1.3806 | 2.7231 | 1.3485 | 2.5239 | 0.8842 | 1.9841 |

### T2.3 Equal-ripple (Chebyshev) low-pass prototype element values, 3.0 dB ripple (g0 = 1, wc = 1, N = 1 to 10) — Table 8.4, p.406

| N | g1 | g2 | g3 | g4 | g5 | g6 | g7 | g8 | g9 | g10 | g11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 1.9953 | 1.0000 | | | | | | | | | |
| 2 | 3.1013 | 0.5339 | 5.8095 | | | | | | | | |
| 3 | 3.3487 | 0.7117 | 3.3487 | 1.0000 | | | | | | | |
| 4 | 3.4389 | 0.7483 | 4.3471 | 0.5920 | 5.8095 | | | | | | |
| 5 | 3.4817 | 0.7618 | 4.5381 | 0.7618 | 3.4817 | 1.0000 | | | | | |
| 6 | 3.5045 | 0.7685 | 4.6061 | 0.7929 | 4.4641 | 0.6033 | 5.8095 | | | | |
| 7 | 3.5182 | 0.7723 | 4.6386 | 0.8039 | 4.6386 | 0.7723 | 3.5182 | 1.0000 | | | |
| 8 | 3.5277 | 0.7745 | 4.6575 | 0.8089 | 4.6990 | 0.8018 | 4.4990 | 0.6073 | 5.8095 | | |
| 9 | 3.5340 | 0.7760 | 4.6692 | 0.8118 | 4.7272 | 0.8118 | 4.6692 | 0.7760 | 3.5340 | 1.0000 | |
| 10 | 3.5384 | 0.7771 | 4.6768 | 0.8136 | 4.7425 | 0.8164 | 4.7260 | 0.8051 | 4.5142 | 0.6091 | 5.8095 |

Note (p.406): for even N the load g_{N+1} != 1 (1.9841 at 0.5 dB, 5.8095 at 3.0 dB) -> mismatch to a unity load; fix with a lambda/4 transformer or make N odd.

### T2.4 Maximally flat time delay (linear-phase / Bessel-type) low-pass prototype element values (g0 = 1, wc = 1, N = 1 to 10) — Table 8.5, p.408; passband group delay tau_d = 1/wc = 1 s (normalized)

| N | g1 | g2 | g3 | g4 | g5 | g6 | g7 | g8 | g9 | g10 | g11 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2.0000 | 1.0000 | | | | | | | | | |
| 2 | 1.5774 | 0.4226 | 1.0000 | | | | | | | | |
| 3 | 1.2550 | 0.5528 | 0.1922 | 1.0000 | | | | | | | |
| 4 | 1.0598 | 0.5116 | 0.3181 | 0.1104 | 1.0000 | | | | | | |
| 5 | 0.9303 | 0.4577 | 0.3312 | 0.2090 | 0.0718 | 1.0000 | | | | | |
| 6 | 0.8377 | 0.4116 | 0.3158 | 0.2364 | 0.1480 | 0.0505 | 1.0000 | | | | |
| 7 | 0.7677 | 0.3744 | 0.2944 | 0.2378 | 0.1778 | 0.1104 | 0.0375 | 1.0000 | | | |
| 8 | 0.7125 | 0.3446 | 0.2735 | 0.2297 | 0.1867 | 0.1387 | 0.0855 | 0.0289 | 1.0000 | | |
| 9 | 0.6678 | 0.3203 | 0.2547 | 0.2184 | 0.1859 | 0.1506 | 0.1111 | 0.0682 | 0.0230 | 1.0000 | |
| 10 | 0.6305 | 0.3002 | 0.2384 | 0.2066 | 0.1808 | 0.1539 | 0.1240 | 0.0911 | 0.0557 | 0.0187 | 1.0000 |

g-value definitions (Fig.8.25, p.403–404): g0 = generator resistance (ladder starting with shunt C, Fig.8.25a) or generator conductance (ladder starting with series L, Fig.8.25b); gk (k = 1..N) = inductance of series inductors / capacitance of shunt capacitors; g_{N+1} = load resistance if gN is a shunt capacitor, load conductance if gN is a series inductor. The two ladders are duals and give the same response. Filter order N = number of reactive elements.

### T2.5 Image-parameter T- and pi-network parameters — Table 8.1, p.391

| quantity | T-network (series Z1/2, shunt Z2, series Z1/2) | pi-network (shunt 2Z2, series Z1, shunt 2Z2) |
|---|---|---|
| A | 1 + Z1/(2*Z2) | 1 + Z1/(2*Z2) |
| B | Z1 + Z1^2/(4*Z2) | Z1 |
| C | 1/Z2 | 1/Z2 + Z1/(4*Z2^2) |
| D | 1 + Z1/(2*Z2) | 1 + Z1/(2*Z2) |
| Z / Y params | Z11 = Z22 = Z2 + Z1/2; Z12 = Z21 = Z2 | Y11 = Y22 = 1/Z1 + 1/(2*Z2); Y12 = Y21 = -1/Z1 (minus sign lost in OCR; standard) |
| image impedance | ZiT = sqrt(Z1*Z2)*sqrt(1 + Z1/(4*Z2)) | Zipi = sqrt(Z1*Z2)/sqrt(1 + Z1/(4*Z2)) = Z1*Z2/ZiT |
| propagation | e^gamma = 1 + Z1/(2*Z2) + sqrt(Z1/Z2 + Z1^2/(4*Z2^2)) | same as T |

### T2.6 Composite (image-parameter) filter design summary — Table 8.2, p.397

| section | low-pass | high-pass |
|---|---|---|
| constant-k T | series L/2, L/2; shunt C; R0 = sqrt(L/C), wc = 2/sqrt(L*C); L = 2*R0/wc, C = 2/(wc*R0) | series 2C, 2C; shunt L; R0 = sqrt(L/C), wc = 1/(2*sqrt(L*C)); L = R0/(2*wc), C = 1/(2*wc*R0) |
| m-derived T (sharp cutoff) | series mL/2, mL/2; shunt mC in series with (1-m^2)L/(4m); m = sqrt(1 - (fc/f_inf)^2) | series 2C/m, 2C/m; shunt L/m in series with 4m*C/(1-m^2); m = sqrt(1 - (f_inf/fc)^2) |
| bisected-pi matching end section | m = 0.6; series mL/2; shunt mC/2 in series with (1-m^2)L/(2m); faces R0 on the outside, ZiT inside | m = 0.6; series 2C/m; shunt 2L/m in series with 2m*C/(1-m^2) |

L, C of m-derived sections are the same as the constant-k section. Only one free parameter (m of the sharp-cutoff section) remains once fc and R0 are fixed.

### T2.7 Prototype-to-final element transformations (no impedance scaling; multiply L by R0 and divide C by R0 afterward) — Table 8.6, p.414 (Delta = (w2 - w1)/w0, w0 = sqrt(w1*w2))

| prototype element | low-pass (wc) | high-pass (wc) | bandpass | bandstop |
|---|---|---|---|---|
| series L | series L/wc | series C = 1/(wc*L) | series L' = L/(w0*Delta) with series C' = Delta/(w0*L) | parallel L' = L*Delta/w0 with C' = 1/(w0*L*Delta) |
| shunt C | shunt C/wc | shunt L = 1/(wc*C) | parallel L' = Delta/(w0*C) with C' = C/(w0*Delta) | series L' = 1/(w0*C*Delta) with C' = C*Delta/w0 |

### T2.8 Ten canonical coupled-line two-port circuits (image impedance, response) — Table 8.8, p.429 (graphics not in text; image-impedance formulas as recoverable)

| response | image impedance (theta = beta*l) |
|---|---|
| low-pass | Zi1 = 2*Z0e*Z0o*cos(theta)/sqrt((Z0e + Z0o)^2*cos^2(theta) - (Z0e - Z0o)^2); Zi2 = Z0e*Z0o/Zi1 |
| bandpass (both ends open on alternate sides, Fig.8.42c) | Zi = 0.5*sqrt((Z0e - Z0o)^2*csc^2(theta) - (Z0e + Z0o)^2*cot^2(theta)) (eq. 8.101) |
| bandpass | Zi1 = 2*Z0e*Z0o*sin(theta)/sqrt((Z0e - Z0o)^2 - (Z0e + Z0o)^2*cos^2(theta)) |
| bandpass | Zi1 = sqrt((Z0e - Z0o)^2 - (Z0e + Z0o)^2*cos^2(theta))/(2*sin(theta)) |
| bandpass | Zi1 = Z0e*Z0o*sqrt((Z0e - Z0o)^2 - (Z0e + Z0o)^2*cos^2(theta))/((Z0e + Z0o)*sin(theta)); Zi2 = Z0e*Z0o/Zi1 |
| all pass (x3) | Zi1 = (Z0e + Z0o)/2; Zi1 = 2*Z0e*Z0o/(Z0e + Z0o); Zi1 = sqrt(Z0e*Z0o) |
| all stop (x3) | Zi1 = -j*(2*Z0e*Z0o/(Z0e + Z0o))*cot(theta) (Zi2 = Z0e*Z0o/Zi1); Zi1 = j*sqrt(Z0e*Z0o)*tan(theta); Zi1 = -j*sqrt(Z0e*Z0o)*cot(theta) |

### T2.9 Permanent magnet materials — POI "Permanent Magnets", p.465 (units as printed: "Br (Oe)" and "Hc (G)"; conventionally Br is in G and Hc in Oe)

| material | composition | Br | Hc | (BH)max (G-Oe x 1e6) |
|---|---|---|---|---|
| ALNICO 5 | Al, Ni, Co, Cu | 12,000 | 720 | 5.0 |
| ALNICO 8 | Al, Ni, Co, Cu, Ti | 7100 | 2000 | 5.5 |
| ALNICO 9 | Al, Ni, Co, Cu, Ti | 10,400 | 1600 | 8.5 |
| Remalloy | Mo, Co, Fe | 10,500 | 250 | 1.1 |
| Platinum cobalt | Pt, Co | 6450 | 4300 | 9.5 |
| Ceramic | BaO6Fe2O3 | 3950 | 2400 | 3.5 |
| Cobalt samarium | Co, Sm | 8400 | 7000 | 16.0 |

Demagnetization factors (Table 9.1, p.463): thin disk/plate normal to z: Nx = 0, Ny = 0, Nz = 1; thin rod along z: Nx = 1/2, Ny = 1/2, Nz = 0; sphere: 1/3, 1/3, 1/3.

### T2.10 Commercial Schottky diode parameters — Table 11.1, p.527

| diode | Is (A) | Rs (ohm) | Cj (pF) | Ls (nH) | Cp (pF) |
|---|---|---|---|---|---|
| Skyworks SMS1546 | 3e-7 | 4 | 0.38 | 1.0 | 0.07 |
| Skyworks SMS7630 | 5e-6 | 20 | 0.14 | 0.05 | 0.005 |
| Avago HSMS2800 | 3e-8 | 30 | 1.6 | — | — |
| Macom MA4E2054 | 3e-8 | 11 | 0.1 | — | 0.11 |

### T2.11 Square-law detector output components for an AM input v = v0*(1 + m*cos(wm*t))*cos(w0*t) — Table 11.2, p.529 (relative amplitudes of terms multiplying v0^2*Gd'/4)

| frequency | relative amplitude |
|---|---|
| 0 (DC) | 1 + m^2/2 |
| wm | 2m |
| 2wm | m^2/2 |
| 2w0 | 1 + m^2/2 |
| 2w0 ± wm | m |
| 2(w0 ± wm) | m^2/4 |

### T2.12 Commercial PIN diode parameters — Table 11.3, p.531

| diode | Rf (ohm) | Cj (pF) |
|---|---|---|
| ASI 8001 | 3.0 | 0.03 |
| Skyworks DSG9500 | 4.0 | 0.025 |
| Infineon BA592 | 0.36 | 1.4 |
| Microsemi UM9605 | 1.5 | 0.5 |

### T2.13 Transistor S-parameters (magnitude angle-deg) — Tables 11.4, 11.5, 11.7, 11.8, p.541–547

NEC NE58219 Si BJT, Vce = 5.0 V, Ic = 5.0 mA, common emitter (Table 11.4):

| f (GHz) | S11 | S12 | S21 | S22 |
|---|---|---|---|---|
| 0.1 | 0.78 -33 | 0.03 71 | 12.7 155 | 0.93 -17 |
| 0.5 | 0.46 -113 | 0.08 52 | 6.3 104 | 0.53 -38 |
| 1.0 | 0.38 -158 | 0.11 54 | 3.5 80 | 0.40 -43 |
| 2.0 | 0.40 157 | 0.19 56 | 1.9 52 | 0.33 -63 |
| 4.0 | 0.52 117 | 0.38 45 | 1.1 14 | 0.33 -127 |

Infineon BFP640F SiGe HBT, Vce = 2.0 V, Ic = 1.2 mA, common emitter (Table 11.5):

| f (GHz) | S11 | S12 | S21 | S22 |
|---|---|---|---|---|
| 1.0 | 0.91 -44 | 0.06 68 | 3.92 149 | 0.93 -17 |
| 2.0 | 0.75 -86 | 0.10 46 | 3.39 120 | 0.79 -31 |
| 4.0 | 0.59 -144 | 0.11 29 | 2.18 82 | 0.64 -43 |
| 6.0 | 0.54 176 | 0.11 34 | 1.64 57 | 0.58 -53 |

NEC NE76184A GaAs MESFET, VDS = 3.0 V, ID = 10.0 mA, common source (Table 11.7):

| f (GHz) | S11 | S12 | S21 | S22 |
|---|---|---|---|---|
| 1.0 | 0.97 -28 | 0.04 72 | 3.82 154 | 0.70 -19 |
| 2.0 | 0.90 -55 | 0.08 54 | 3.56 129 | 0.65 -37 |
| 4.0 | 0.72 -103 | 0.12 28 | 2.91 86 | 0.53 -68 |
| 8.0 | 0.52 179 | 0.14 -1 | 2.0 20 | 0.42 -129 |
| 12.0 | 0.49 103 | 0.17 -19 | 1.5 -38 | 0.44 170 |

Cree CGH21120 GaN HEMT, VDD = 28 V (OCR prints "328 V"), ID = 500 mA, common source (Table 11.8):

| f (GHz) | S11 | S12 | S21 | S22 |
|---|---|---|---|---|
| 0.5 | 0.96 180 | 0.007 -16 | 3.67 68 | 0.72 -174 |
| 1.0 | 0.95 172 | 0.008 -35 | 2.03 44 | 0.78 -172 |
| 2.0 | 0.78 153 | 0.014 -83 | 2.09 -17 | 0.91 -174 |
| 4.0 | 0.88 -51 | 0.008 79 | 0.84 88 | 0.88 171 |

### T2.14 Performance characteristics of microwave transistors — Table 11.6, p.543

| device | semiconductor | frequency range (GHz) | typical gain (dB) | NF dB (at GHz) | power capacity | cost | single-polarity supply |
|---|---|---|---|---|---|---|---|
| BJT | Si | 10 | 10–15 | 2.0 (2) | High | Low | Yes |
| HBT | SiGe | 30 | 10–15 | 0.6 (8) | Medium | Medium | Yes |
| CMOS | Si | 20 | 10–20 | 1.0 (4) | Low | Low | Yes |
| MESFET | GaAs | 60 | 5–20 | 1.0 (10) | Medium | Medium | No |
| HEMT | GaAs | 100 | 10–20 | 0.5 (12) | Medium | High | No |
| HEMT | GaN | 10 | 10–15 | 1.6 (6) | High | Medium | No |

### T2.15 RF switch technologies, 10–20 GHz band — POI "RF MEMS Switch Technology", p.552

| technology | insertion loss (dB) | isolation (dB) | switching power | DC voltage (V) | switching speed |
|---|---|---|---|---|---|
| PIN diode | 0.1–0.8 | 25–45 | 1–5 mW | 1–10 | 1–5 ns |
| FET | 0.5–1.0 | 20–50 | 1–5 mW | 1–10 | 2–10 ns |
| MEMS | 0.1–1.0 | 25–60 | 1 uW | 10–20 | > 30 us |

### T2.16 Microwave tube characteristics (orientation) — §11.5, p.553–555

| tube | type | key numbers |
|---|---|---|
| klystron amplifier | linear beam | 2 cavities ≈ 20 dB gain; 4 cavities (practical limit) 80–90 dB; peak powers in MW range; efficiency 30–50%; narrow bandwidth; very low AM/FM noise |
| reflex klystron | linear beam oscillator | mechanically tuned single cavity |
| TWT | linear beam amplifier | bandwidth 30–120% (widest of tubes); several hundred W (kW with coupled cavities, less BW); efficiency 20–40% |
| BWO | linear beam oscillator | voltage tunable over an octave or more; < 1 W typically |
| EIO | linear beam oscillator | narrow tuning, moderate efficiency, high power to several hundred GHz |
| magnetron | crossed field oscillator | several kW, efficiency >= 80%; noisy, not coherent pulse-to-pulse; mainly microwave ovens |
| CFA | crossed field amplifier | efficiency up to 80%; gain 10–15 dB; bandwidth up to 40%; noisier than klystron/TWT |
| gyrotron | crossed field | 10–100 kW at mm-wave; frequency set by bias field and electron velocity |

### T2.17 Small-signal S-parameters and large-signal optimum reflection coefficients, Si BJT power transistor — Table 12.1, p.598 (mag angle-deg)

Note: the OCR column order is S11, S12, S21, S22; the printed values (4.10∠76 in the "S12" position, 0.065∠49 in the "S21" position) indicate the S12/S21 columns are transposed in the extraction — physically |S21| = 4.10, 3.42, 3.08 and |S12| = 0.065, 0.073, 0.079.

| f (MHz) | S11 | S21 (as physically interpreted) | S12 (as physically interpreted) | S22 | GammaSP | GammaLP | G (dB) |
|---|---|---|---|---|---|---|---|
| 800 | 0.76 176 | 4.10 76 | 0.065 49 | 0.35 -163 | 0.856 -167 | 0.455 129 | 13.5 |
| 900 | 0.76 172 | 3.42 72 | 0.073 52 | 0.35 -167 | 0.747 -177 | 0.478 161 | 12.0 |
| 1000 | 0.76 169 | 3.08 69 | 0.079 53 | 0.36 -169 | 0.797 -187 | 0.491 185 | 10.0 |

### T2.18 Mixer characteristics — Table 13.1, p.653

| mixer type | number of diodes | RF input match | RF-LO isolation | conversion loss | third-order intercept |
|---|---|---|---|---|---|
| single ended | 1 | Poor | Fair | Good | Fair |
| balanced (90 deg) | 2 | Good | Poor | Good | Fair |
| balanced (180 deg) | 2 | Fair | Excellent | Good | Fair |
| double balanced | 4 | Poor | Excellent | Excellent | Excellent |
| image reject | 2 or 4 | Good | Good | Good | Good |

Typical mixer numbers (§13.5, p.639–641): diode conversion loss 4–7 dB (1–10 GHz); LO drive for minimum loss 0–10 dBm; NF 1–5 dB; IIP3 15–30 dBm; LO-RF isolation 20–40 dB. Anchor MMIC: SiGe subharmonic down-converter 43.5–45.5 GHz, NF < 6 dB (Fig.13.36, p.654).

### T2.19 Oscillator / phase-noise orientation numbers — §13, p.604–627

| quantity | value |
|---|---|
| typical frequency-stability requirement | 2 to 0.5 ppm/degC |
| typical phase-noise requirement | -80 to -110 dBc/Hz at 10 kHz offset |
| cellular-radio phase-noise example | -110 dBc/Hz at 25 kHz |
| varactor VCO tuning range | ≈ 1 octave |
| YIG-tuned oscillator tuning range | decade or more (slower) |
| quartz crystal Q | up to 100,000; drift < 0.001%/degC |
| LC resonator Q (below a few hundred MHz) | seldom > a few hundred |
| dielectric resonator Q | up to several thousand (cavities 1e4+) |
| 1/f corner: Si JFET / Si BJT / GaAs MESFET | 50–100 Hz / 5–50 kHz / 2–10 MHz or higher |
| thermal floor k*T0 | -174 dBm/Hz |
| multiplier noise penalty | 20*log10(n) dB |
| varactor multiplier efficiency (doubler/tripler, 50 GHz) | 50–80% |
| FET multiplier optimum tau/T | 0.35 (n = 2), 0.22 (n = 3) |

### T2.20 Digital modulation performance — Table 14.1, p.684

| modulation | Eb/n0 (dB) for Pb = 1e-5 | bandwidth efficiency (bps/Hz) |
|---|---|---|
| binary ASK | 15.6 | 1 |
| binary FSK | 12.6 | 1 |
| binary PSK | 9.6 | 1 |
| QPSK | 9.6 | 2 |
| 8-PSK | 13.0 | 3 |
| 16-PSK | 18.7 | 4 |
| 16-QAM | 13.4 | 4 |
| 64-QAM | 17.8 | 6 |

(Fig.14.16 curve reading used in Ex.14.6: QPSK Pb = 0.01 at Eb/n0 ≈ 5 dB.)

### T2.21 Typical radar cross sections — Table 14.3, p.696

| target | sigma (m^2) |
|---|---|
| bird | 0.01 |
| missile | 0.5 |
| person | 1 |
| small plane | 1–2 |
| bicycle | 2 |
| small boat | 2 |
| fighter plane | 3–8 |
| bomber | 30–40 |
| large airliner | 100 |
| truck | 200 |

### T2.22 Wireless system frequencies — Table 14.2, p.685 (U = uplink mobile-to-base, D = downlink)

| system | frequency |
|---|---|
| AMPS (US, obsolete) | U 824–849 MHz; D 869–894 MHz |
| GSM 850 (Americas) | U 824–849 MHz; D 869–894 MHz |
| GSM 900 (worldwide) | U 890–915 MHz; D 935–960 MHz |
| GSM 1800 (worldwide) | U 1710–1785 MHz; D 1805–1880 MHz |
| GSM 1900 (Americas) | U 1850–1910 MHz; D 1930–1990 MHz |
| UMTS band 1 | U 1920–1980 MHz; D 2110–2170 MHz |
| UMTS band 2 | U 1850–1910 MHz; D 1930–1990 MHz |
| UMTS band 8 | U 880–916 MHz (as printed); D 925–960 MHz |
| WLAN (Wi-Fi) | 902–928 MHz; 2.400–2.484 GHz; 5.725–5.850 GHz |
| GPS | L1 1575.42 MHz; L2 1227.60 MHz |
| DBS | Europe/Russia 10.7–12.75 GHz; Americas 12.2–12.7 GHz; Asia/Australia 11.7–12.2 GHz |
| ISM (most countries) | 902–928 MHz; 2.400–2.484 GHz; 5.725–5.850 GHz |

### T2.23 Physical constants — Appendix E, p.718

| constant | value |
|---|---|
| eps0 | 8.854e-12 F/m |
| mu0 | 4*pi*1e-7 H/m |
| eta0 | 376.7 ohm |
| c | 2.998e8 m/s |
| electron charge q | 1.602e-19 C |
| electron mass m | 9.107e-31 kg |
| Boltzmann k | 1.380e-23 J/K |
| Planck h | 6.626e-34 J*s |
| gyromagnetic ratio gamma (g = 2) | 1.759e11 C/kg |

### T2.24 Conductivities at 20 degC — Appendix F, p.719 (S/m)

| material | sigma | material | sigma |
|---|---|---|---|
| aluminum | 3.816e7 | nichrome | 1.0e6 |
| brass | 2.564e7 | nickel | 1.449e7 |
| bronze | 1.00e7 | platinum | 9.52e6 |
| chromium | 3.846e7 | sea water | 3–5 |
| copper | 5.813e7 | silicon | 4.4e-4 |
| distilled water | 2e-4 | silver | 6.173e7 |
| germanium | 2.2e6 (as printed) | steel (silicon) | 2e6 |
| gold | 4.098e7 | steel (stainless) | 1.1e6 |
| graphite | 7.0e4 | solder | 7.0e6 |
| iron | 1.03e7 | tungsten | 1.825e7 |
| mercury | 1.04e6 | zinc | 1.67e7 |
| lead | 4.56e6 | | |

### T2.25 Dielectric constants and loss tangents (tan_delta at 25 degC) — Appendix G, p.719

| material | frequency | er | tan_delta |
|---|---|---|---|
| alumina (99.5%) | 10 GHz | 9.5–10. | 0.0003 |
| barium tetratitanate | 6 GHz | 37 ± 5% | 0.0005 |
| beeswax | 10 GHz | 2.35 | 0.005 |
| beryllia | 10 GHz | 6.4 | 0.0003 |
| ceramic (A-35) | 3 GHz | 5.60 | 0.0041 |
| fused quartz | 10 GHz | 3.78 | 0.0001 |
| gallium arsenide | 10 GHz | 13.0 | 0.006 |
| glass (pyrex) | 3 GHz | 4.82 | 0.0054 |
| glazed ceramic | 10 GHz | 7.2 | 0.008 |
| lucite | 10 GHz | 2.56 | 0.005 |
| nylon (610) | 3 GHz | 2.84 | 0.012 |
| paraffin | 10 GHz | 2.24 | 0.0002 |
| plexiglass | 3 GHz | 2.60 | 0.0057 |
| polyethylene | 10 GHz | 2.25 | 0.0004 |
| polystyrene | 10 GHz | 2.54 | 0.00033 |
| porcelain (dry process) | 100 MHz | 5.04 | 0.0078 |
| Rexolite (1422) | 3 GHz | 2.54 | 0.00048 |
| silicon | 10 GHz | 11.9 | 0.004 |
| Styrofoam (103.7) | 3 GHz | 1.03 | 0.0001 |
| Teflon | 10 GHz | 2.08 | 0.0004 |
| titania (D-100) | 6 GHz | 96 ± 5% | 0.001 |
| Vaseline | 10 GHz | 2.16 | 0.001 |
| water (distilled) | 3 GHz | 76.7 | 0.157 |

Note (§8.8, p.446): zinc/strontium titanate resonator ceramic er = 36, Q = 10,000 at 4 GHz, TC(er) = -7 ppm/degC. FR4-type example values used in Ch.7–8 problems/examples: er = 4.2, tan_delta = 0.02 (0.01 in Problem 8.18), thickness 0.158 cm or 0.079 cm, 0.5 mil copper.

### T2.26 Microwave ferrite materials (Trans-Tech) — Appendix H, p.720

| material | Trans-Tech no. | 4*pi*Ms (G) | dH (Oe) | er | tan_delta | Tc (degC) | 4*pi*Mr (G) |
|---|---|---|---|---|---|---|---|
| magnesium ferrite | TT1-105 | 1750 | 225 | 12.2 | 0.00025 | 225 | 1220 |
| magnesium ferrite | TT1-390 | 2150 | 540 | 12.7 | 0.00025 | 320 | 1288 |
| magnesium ferrite | TT1-3000 | 3000 | 190 | 12.9 | 0.0005 | 240 | 2000 |
| nickel ferrite | TT2-101 | 3000 | 350 | 12.8 | 0.0025 | 585 | 1853 |
| nickel ferrite | TT2-113 | 500 | 150 | 9.0 | 0.0008 | 120 | 140 |
| nickel ferrite | TT2-125 | 2100 | 460 | 12.6 | 0.001 | 560 | 1426 |
| lithium ferrite | TT73-1700 | 1700 | < 400 | 16.1 | 0.0025 | 460 | 1139 |
| lithium ferrite | TT73-2200 | 2200 | < 450 | 15.8 | 0.0025 | 520 | 1474 |
| yttrium garnet | G-113 | 1780 | 45 | 15.0 | 0.0002 | 280 | 1277 |
| aluminum garnet | G-610 | 680 | 40 | 14.5 | 0.0002 | 185 | 515 |

(Column alignment reconstructed from sequential OCR lists of equal length; conf medium for alignment.)

### T2.27 Standard rectangular waveguide data — Appendix I, p.720 (letters in parentheses = alternative band designations)

| band | EIA | recommended range (GHz) | TE10 cutoff (GHz) | inside dims, in (cm) | outside dims, in (cm) |
|---|---|---|---|---|---|
| L | WR-650 | 1.12–1.70 | 0.908 | 6.500 x 3.250 (16.51 x 8.255) | 6.660 x 3.410 (16.916 x 8.661) |
| R | WR-430 | 1.70–2.60 | 1.372 | 4.300 x 2.150 (10.922 x 5.461) | 4.460 x 2.310 (11.328 x 5.867) |
| S | WR-284 | 2.60–3.95 | 2.078 | 2.840 x 1.340 (7.214 x 3.404) | 3.000 x 1.500 (7.620 x 3.810) |
| H (G) | WR-187 | 3.95–5.85 | 3.152 | 1.872 x 0.872 (4.755 x 2.215) | 2.000 x 1.000 (5.080 x 2.540) |
| C (J) | WR-137 | 5.85–8.20 | 4.301 | 1.372 x 0.622 (3.485 x 1.580) | 1.500 x 0.750 (3.810 x 1.905) |
| W (H) | WR-112 | 7.05–10.0 | 5.259 | 1.122 x 0.497 (2.850 x 1.262) | 1.250 x 0.625 (3.175 x 1.587) |
| X | WR-90 | 8.20–12.4 | 6.557 | 0.900 x 0.400 (2.286 x 1.016) | 1.000 x 0.500 (2.540 x 1.270) |
| Ku (P) | WR-62 | 12.4–18.0 | 9.486 | 0.622 x 0.311 (1.580 x 0.790) | 0.702 x 0.391 (1.783 x 0.993) |
| K | WR-42 | 18.0–26.5 | 14.047 | 0.420 x 0.170 (1.07 x 0.43) | 0.500 x 0.250 (1.27 x 0.635) |
| Ka (R) | WR-28 | 26.5–40.0 | 21.081 | 0.280 x 0.140 (0.711 x 0.356) | 0.360 x 0.220 (0.914 x 0.559) |
| Q | WR-22 | 33.0–50.5 | 26.342 | 0.224 x 0.112 (0.57 x 0.28) | 0.304 x 0.192 (0.772 x 0.488) |
| U | WR-19 | 40.0–60.0 | 31.357 | 0.188 x 0.094 (0.48 x 0.24) | 0.268 x 0.174 (0.681 x 0.442) |
| V | WR-15 | 50.0–75.0 | 39.863 | 0.148 x 0.074 (0.38 x 0.19) | 0.228 x 0.154 (0.579 x 0.391) |
| E | WR-12 | 60.0–90.0 | 48.350 | 0.122 x 0.061 (0.31 x 0.015 as printed; 0.155 expected) | 0.202 x 0.141 (0.513 x 0.356) |
| W | WR-10 | 75.0–110.0 | 59.010 | 0.100 x 0.050 (0.254 x 0.127) | 0.180 x 0.130 (0.458 x 0.330) |
| F | WR-8 | 90.0–140.0 | 73.840 | 0.080 x 0.040 (0.203 x 0.102) | 0.160 x 0.120 (0.406 x 0.305) |
| D | WR-6 | 110.0–170.0 | 90.854 | 0.065 x 0.0325 (0.170 x 0.083) | 0.145 x 0.1125 (0.368 x 0.2858) |
| G | WR-5 | 140.0–220.0 | 115.750 | 0.051 x 0.0255 (0.130 x 0.0648) | 0.131 x 0.1055 (0.333 x 0.2680) |

### T2.28 Standard coaxial cable data — Appendix J, p.721 (dielectric P / T; conventionally P = polyethylene, T = PTFE/Teflon — legend not in extracted text)

| RG/U type | Z0 (ohm) | inner cond. diam (in) | dielectric | dielectric diam (in) | cable type | overall diam (in) | C (pF/ft) | max oper. voltage (V) | loss at 1 GHz (dB/100 ft) |
|---|---|---|---|---|---|---|---|---|---|
| RG-8A/U | 52 | 0.0855 | P | 0.285 | braided | 0.405 | 29.5 | 5000 | 9.0 |
| RG-9B/U | 50 | 0.0855 | P | 0.280 | braided | 0.420 | 30.8 | 5000 | 9.0 |
| RG-55B/U | 54 | 0.0320 | P | 0.116 | braided | 0.200 | 28.5 | 1900 | 16.5 |
| RG-58B/U | 54 | 0.0320 | P | 0.116 | braided | 0.195 | 28.5 | 1900 | 17.5 |
| RG-59B/U | 75 | 0.0230 | P | 0.146 | braided | 0.242 | 20.6 | 2300 | 11.5 |
| RG-141A/U | 50 | 0.0390 | T | 0.116 | braided | 0.190 | 29.4 | 1900 | 13.0 |
| RG-142A/U | 50 | 0.0390 | T | 0.116 | braided | 0.195 | 29.4 | 1900 | 13.0 |
| RG-174/U | 50 | 0.0189 | P | 0.060 | braided | 0.100 | 30.8 | 1500 | 31.0 |
| RG-178B/U | 50 | 0.0120 | T | 0.034 | braided | 0.072 | 29.4 | 1000 | 45.0 |
| RG-179B/U | 75 | 0.0120 | T | 0.063 | braided | 0.100 | 19.5 | 1200 | 25.0 |
| RG-180B/U | 95 | 0.0120 | T | 0.102 | braided | 0.140 | 15.4 | 1500 | 16.5 |
| RG-187/U | 75 | 0.0120 | T | 0.060 | braided | 0.105 | 19.5 | 1200 | 25.0 |
| RG-188/U | 50 | 0.0201 | T | 0.060 | braided | 0.105 | 29.4 | 1200 | 30.0 |
| RG-195/U | 95 | 0.0120 | T | 0.102 | braided | 0.145 | 15.4 | 1500 | 16.5 |
| RG-213/U | 50 | 0.0888 | P | 0.285 | braided | 0.405 | 30.8 | 5000 | 9.0 |
| RG-214/U | 50 | 0.0888 | P | 0.285 | braided | 0.425 | 30.8 | 5000 | 9.0 |
| RG-223/U | 50 | 0.0350 | P | 0.116 | braided | 0.211 | 30.8 | 1900 | 16.5 |
| RG-316/U | 50 | 0.0201 | T | 0.060 | braided | 0.102 | 29.4 | 1200 | 30.0 |
| RG-401/U | 50 | 0.0645 | T | 0.215 | semi-rigid | 0.250 | 29.3 | 3000 | — |
| RG-402/U | 50 | 0.0360 | T | 0.119 | semi-rigid | 0.141 | 29.3 | 2500 | 13.0 |
| RG-405/U | 50 | 0.0201 | T | 0.066 | semi-rigid | 0.0865 | 29.4 | 1500 | — |

### T2.29 Reflection coefficient / SWR / return loss conversions — "Useful Results" end matter

| abs(Gamma) | SWR | RL (dB) |
|---|---|---|
| 0.024 | 1.05 | 32.3 |
| 0.032 | 1.07 | 30.0 |
| 0.048 | 1.10 | 26.4 |
| 0.050 | 1.11 | 26.0 |
| 0.056 | 1.12 | 25.0 |
| 0.10 | 1.22 | 20.0 |
| 0.178 | 1.43 | 15.0 |
| 0.200 | 1.50 | 14.0 |
| 0.316 | 1.92 | 10.0 |
| 0.33 | 2.00 | 9.6 |

ABCD of basic two-ports (end matter): series Z: A = 1, B = Z, C = 0, D = 1; shunt Y: A = 1, B = 0, C = Y, D = 1; line (Z0, beta*l): A = cos(beta*l), B = j*Z0*sin(beta*l), C = j*Y0*sin(beta*l), D = cos(beta*l); ideal transformer N:1: A = N, B = 0, C = 0, D = 1/N; pi (Y1 shunt, Y3 series, Y2 shunt): A = 1 + Y2/Y3, B = 1/Y3, C = Y1 + Y2 + Y1*Y2/Y3, D = 1 + Y1/Y3; T (Z1 series, Z3 shunt, Z2 series): A = 1 + Z1/Z3, B = Z1 + Z2 + Z1*Z2/Z3, C = 1/Z3, D = 1 + Z2/Z3.

### T2.30 Answer-key test vectors (from "Answers to Selected Problems", p.722–724) usable to unit-test the checks in §3

| problem | inputs (from problem statement) | book answer |
|---|---|---|
| 7.3 | coupler S-matrix | RL = 20 dB, C = 15 dB, D = 30 dB, L = 0.5 dB |
| 8.7 | maximally flat LPF 0–2 GHz, >= 20 dB at 3.4 GHz | N = 5 |
| 10.4 | amp G = 12 dB, F = 4 dB, then receiver Te = 900 K | Fcas = 4.3 dB |
| 10.15 | Ex.10.4 with mixer first, then amp | OIP3 = 20.8 dBm (coherent) |
| 10.17 | B = 1 GHz, G = 15 dB, Te = 250 K, OP1dB = 5 dBm | LDR = 74.5 dB |
| 10.18 | F = 6 dB, OP1dB = 21 dBm, G = 30 dB, OIP3 = 33 dBm, Ni = -105 dBm, SNR = 8 dB, B = 20 MHz | LDR = 86.7 dB, SFDR = 57.8 dB |
| 12.13 | S11 = 0.880∠-115, S12 = 0.029∠31, S21 = 9.40∠110, S22 = 0.328∠-67 | -2.9 dB < GT - GTU < 4.3 dB |
| 12.21 | Ri = 5, Rds = 200, Cgs = 0.3 pF, gm = 40 mS, Z0 = 50, 16 GHz | N_opt = 8.4 |
| 13.9 | F = 6 dB, Q = 500, f0 = 100 MHz, P = 10 dBm, f_alpha = 50 kHz, K = 1 | L(1 MHz) = -181 dBc/Hz, L(10 kHz) = -153 dBc/Hz |
| 13.12 | 860 MHz, 80 dB rejection, equal-level interferer, IF 12 kHz | L = -121 dBc/Hz |
| 14.4 | 18 in dish, 12.4 GHz, eta_ap = 65% | D = 33.6 dB |
| 14.6 | uniform 5 K sky, TA = 105 K, Tp = 290 K | eta_rad = 65% |
| 14.17 | 12 GHz, 1–20 m/s | Doppler passband 80–1600 Hz |

## 3. Mechanizable checks

Conventions for all checks: powers in dBm (or W where stated), gains/losses in dB, noise figure F in dB (linear f = 10^(F/10)), temperatures in K, T0 = 290 K, k = 1.380e-23 J/K, frequencies in Hz, impedances in ohm. Linear gains g = 10^(G/10). "margin" is (allowed − actual) in dB unless stated; a check passes when margin >= 0 (or >= a stated guard band). All formulas below were re-run against the book's worked examples (vectors listed per check; scratch script reproduced every one).

**CHECK-RF-CASCADE-NF** — noise figure / temperature of a receive chain (POZAR-318…326)
- Inputs (one row per stage, in signal order): `stage`, `G_dB` (negative for loss), `NF_dB` *or* `Te_K`; for passive/lossy stages optionally `L_dB`, `T_phys_K`, `mismatch_Gamma` (then Te = (L−1)·T_phys, or Te from POZAR-324 when mismatched); chain-level `TA_K` (antenna/source temperature), `B_Hz`, `NF_spec_dB`.
- Formula: Te_i = (f_i − 1)·T0; T_cas = Te_1 + Te_2/g_1 + Te_3/(g_1 g_2) + …; F_cas = 1 + T_cas/T0; g_tot = Π g_i. Output noise N_o = k·(TA + T_cas)·B·g_tot (never k·TA·B·F·g_tot when TA ≠ T0 — POZAR-322). Input-mismatched amplifier: f_m = 1 + (f − 1)/(1 − |Γ|²) (POZAR-326).
- Pass: NF_cas_dB <= NF_spec_dB. Margin = NF_spec_dB − NF_cas_dB. Report each stage's contribution Te_i/Π(g before i) to show first-stage dominance.
- Test vectors: Ex.10.2 (LNA 10 dB/2 dB, BPF −1 dB/1 dB, mixer −3 dB/4 dB) → F_cas = 1.80 (2.55 dB), T_cas = 232 K, N_o = −96.8 dBm at TA = 150 K, B = 10 MHz; Problem 10.4 (12 dB/4 dB amp → 900 K receiver) → 4.3 dB.

**CHECK-RF-SENSITIVITY** — minimum detectable signal / required input for a target SNR (POZAR-321, 458, 460)
- Inputs: `T_sys_K` (from CHECK-RF-CASCADE-NF plus antenna/line, POZAR-447/458), `B_Hz`, `SNR_min_dB` or (`EbN0_req_dB`, `Rb_bps`), `P_signal_dBm` (expected).
- Formula: N_in = k·T_sys·B; S_min = N_in·10^(SNR_min/10); digital: S_min = k·T_sys·Rb·10^(EbN0_req/10); input voltage V = sqrt(Z0·S).
- Pass: P_signal_dBm − S_min_dBm >= 0. Margin = that difference.
- Test vectors: Ex.10.2 → S_i = 5.27e-12 W (−82.8 dBm, 16.2 µV in 50 Ω) for 20 dB SNR; Ex.14.5 → T_SYS = 762 K, kBT_SYS = −110 dBm, So/No = 30 dB at Si = −80 dBm.

**CHECK-RF-CASCADE-IP3** — third-order intercept of a chain (POZAR-329…333)
- Inputs (per stage): `G_dB`, `OIP3_dBm` (convert IIP3 with OIP3 = IIP3 + G); chain `IIP3_spec_dBm` or `OIP3_spec_dBm`.
- Formula (output-referred, linear mW, stage by stage): coherent (worst case) 1/OIP3_{1..k} = 1/(g_k·OIP3_{1..k−1}) + 1/OIP3_k; non-coherent OIP3_{1..k} = [1/(g_k·OIP3_{1..k−1})² + 1/OIP3_k²]^(−1/2). IIP3_cas = OIP3_cas − G_tot. IM3 product level: P_IM3 = 3·P_fund − 2·OIP3 (dBm, output).
- Pass: IIP3_cas_dBm (coherent) >= IIP3_spec_dBm. Margin = IIP3_cas − IIP3_spec. Flag if IP3 − P1dB of any stage is outside 10–15 dB (datasheet sanity, POZAR-331).
- Test vectors: Ex.10.4 (LNA G 20 dB, OIP3 22 dBm → mixer −6 dB, IIP3 13 dBm) → 6.4 dBm coherent, 6.9 dBm non-coherent; Problem 10.15 (order reversed) → 20.8 dBm coherent.

**CHECK-RF-DYNAMIC-RANGE** — LDR and SFDR (POZAR-335/336)
- Inputs: `OP1dB_dBm`, `OIP3_dBm`, `G_dB`, `NF_dB` (or `Te_K`), `TA_K`, `B_Hz`, `SNR_req_dB`, `LDR_spec_dB`, `SFDR_spec_dB`.
- Formula: N_o = g·k·B·(TA + (f − 1)·T0) (dBm); LDR = OP1dB − N_o; SFDR = (2/3)(OIP3 − N_o) − SNR_req.
- Pass: LDR >= LDR_spec and SFDR >= SFDR_spec. Margins = differences.
- Test vectors: Ex.10.5 → N_o = −47.4 dBm, LDR = 72.4 dB, SFDR = 44.9 dB; Problem 10.18 → LDR 86.7 dB, SFDR 57.8 dB; Problem 10.17 → LDR 74.5 dB.

**CHECK-LINK-BUDGET-MARGIN** — Friis link budget and margin (POZAR-451…455)
- Inputs: `f_Hz`, `R_m`, `Pt_dBm`, `Lt_dB`, `Gt_dBi`, `LA_dB` (atmospheric/rain, Fig.14.29), `Gr_dBi`, `Lr_dB`, `Gamma_t`, `Gamma_r` (mismatch), `L_pol_dB` (0; 3 for linear↔circular; ∞ for crossed linear), receiver `T_sys_K` (antenna TA + LNB, POZAR-445/447), `B_Hz`, `CNR_min_dB`, `LM_req_dB`.
- Formula: λ = c/f; L0 = 20·log10(4πR/λ); L_imp = −10·log10(1 − |Γ|²) per mismatched end; Pr = Pt − Lt + Gt − L0 − LA + Gr − Lr − L_imp,t − L_imp,r − L_pol; N = 10·log10(k·T_sys·B/1 mW); CNR = Pr − N; LM = CNR − CNR_min (equivalently Pr − Pr_min); G/T = Gr − 10·log10(T_sys).
- Pass: LM >= LM_req (book typical 3–20 dB; ≥ 20 dB fade margin for satellite links above 10 GHz in heavy rain). Margin = LM − LM_req.
- Test vector: Ex.14.4 DBS → L0 = 206.2 dB, Pr = −87.9 dBm, T_e = 100.8 K, G/T = 13.5 dB/K, CNR = 17.7 dB, LM = 2.7 dB.

**CHECK-LINK-MAX-DATA-RATE** — digital link capacity at a BER (POZAR-460…462, Table T2.20)
- Inputs: `Pr_dBm` (from CHECK-LINK-BUDGET-MARGIN), `LM_req_dB`, `T_sys_K`, `modulation`, `BER_target`, `EbN0_req_dB` (Table 14.1 for 1e-5 or Fig.14.16 reading), `Rb_req_bps`.
- Formula: S_min = Pr − LM_req (dBm → W); Rb_max = S_min/(k·T_sys·10^(EbN0_req/10)); occupied bandwidth ≈ Rb/η_bw (η_bw from Table 14.1).
- Pass: Rb_max >= Rb_req. Margin = 10·log10(Rb_max/Rb_req) dB.
- Test vector: Ex.14.6 LEO QPSK (L0 = 176.0 dB, Pr = −108 dBm, S_min = −118 dBm, Eb/n0 = 5 dB, T_sys = 750 K) → 48 kbps.

**CHECK-FILTER-ORDER** — minimum prototype order for a stopband rejection (POZAR-259, 260, 264, 265, 271; Tables T2.1–T2.4)
- Inputs: `type` ∈ {LPF, HPF, BPF, BSF}, `response` ∈ {butterworth, chebyshev}, `ripple_dB` (Chebyshev), `fc_Hz` (LPF/HPF) or `f1_Hz`,`f2_Hz` (BPF/BSF edges), `f_stop_Hz`, `A_stop_dB` (required insertion loss), optional `N_max` (default 10).
- Formula: normalized frequency x — LPF: f_s/fc; HPF: fc/f_s; BPF: |f_s/f0 − f0/f_s|/Δ with f0 = sqrt(f1 f2), Δ = (f2 − f1)/f0; BSF: Δ/|f_s/f0 − f0/f_s|. Prototype loss: Butterworth IL = 10·log10(1 + x^(2N)); Chebyshev IL = 10·log10(1 + ε²·T_N(x)²), ε² = 10^(ripple/10) − 1, T_N(x) = cosh(N·acosh x) for x > 1. N_min = smallest N with IL(x, N) >= A_stop.
- Pass: N_min exists and N_min <= N_max (if N > 10, cascade two lower-order designs, POZAR-265). Margin = IL(x, N_chosen) − A_stop (dB). Flags: Chebyshev with even N → load g_{N+1} ≠ 1 (1.9841 at 0.5 dB, 5.8095 at 3 dB) → requires λ/4 transformer or N+1 (POZAR-264); BPF/BSF from stubs/couplers are only accurate for narrow Δ (coupled-line < ~20 %, inverter-based < ~10 %; POZAR-277, 280); distributed designs add spurious passbands (Richards: repeats every 4fc; coupled-line BPF: 3f0, 5f0 …).
- Test vectors: Ex.8.3 (fc 2 GHz, ≥15 dB at 3 GHz, Butterworth) → N = 5; Problem 8.7 (≥20 dB at 3.4 GHz, fc 2 GHz) → N = 5; Ex.8.7 (0.5 dB, N = 3, f0 2 GHz, Δ 10 %, 1.8 GHz) → x = 2.11, IL = 20.8 dB (book "about 20 dB"); Ex.8.9 (2.2 GHz, x = 1.91, N = 3) → only 17.8 dB by formula, so a strict ≥20 dB spec needs N = 4 (28.7 dB) — the book's graph reading was optimistic (see §5).

**CHECK-FILTER-REALIZABILITY** — element / line-impedance feasibility of a distributed filter (POZAR-274…279, 284, 288…294)
- Inputs: synthesized list of line/stub impedances `Z_i_ohm` and electrical lengths `theta_i_deg` (from the design formulas), fabrication window `Z_min_ohm`, `Z_max_ohm` (from the stackup's minimum/maximum manufacturable trace widths), coupled-line `Z0e`, `Z0o` with minimum gap `S_min`.
- Formula: stepped-impedance: βl_L = g·R0/Zh, βl_C = g·Zl/R0 (require βl < 45° for the lumped approximation, POZAR-278); stub BSF Z0n = 4Z0/(π·gn·Δ), stub BPF Z0n = π·Z0·Δ/(4gn); coupled-line Z0e,o = Z0(1 ± JZ0 + (JZ0)²); Kuroda n² = 1 + Z2/Z1.
- Pass: every Z_i within [Z_min, Z_max]; stepped sections βl < 45° (or flagged); coupled sections achievable within S_min (map Z0e/Z0o through a field solver or Fig.7.29/7.30). Margin = min over i of (Z_max − Z_i, Z_i − Z_min) in ohm.
- Test vectors: Ex.8.8 stub BSF → 265.9 / 387.0 / 265.9 Ω (fails an ordinary microstrip window); Ex.8.6 → one section at 46.1° (> 45°, flagged but acceptable per book); Ex.8.7 → Z0e/Z0o = 70.61/39.24, 56.64/44.77 Ω.

**CHECK-AMP-STABILITY** — unconditional stability over the whole S-parameter band (POZAR-367…372)
- Inputs: S-parameter table `f_Hz, S11, S12, S21, S22` (complex) over the full band where the device has gain (not only the design band), per bias point; optionally realized terminations `GammaS(f)`, `GammaL(f)` from the matching networks.
- Formula: Δ = S11S22 − S12S21; K = (1 − |S11|² − |S22|² + |Δ|²)/(2|S12S21|); µ = (1 − |S11|²)/(|S22 − ΔS11*| + |S12S21|); if terminations given: |Γin| = |S11 + S12S21ΓL/(1 − S22ΓL)|, |Γout| = |S22 + S12S21ΓS/(1 − S11ΓS)|; stability circles CL, RL, CS, RS per POZAR-368.
- Pass: for every frequency either (K > 1 and |Δ| < 1, equivalently µ > 1) or, for conditionally stable points, |Γin| < 1 and |Γout| < 1 with the actual ΓS(f), ΓL(f). Margin = min_f(µ − 1) (unconditional) or min_f(1 − max(|Γin|, |Γout|)) (conditional).
- Test vectors: Ex.12.2 GaN at 1.9 GHz → |Δ| = 0.336, K = 0.383, µ = 0.678 (fail), CL = 1.59∠132°, RL = 0.915, CS = 1.09∠162°, RS = 0.205; Ex.12.3 → K = 0.77/1.19/1.53 at 3/4/5 GHz (conditional at 3 GHz); Ex.12.9 → K = 2.08, |Δ| = 0.579 (pass).

**CHECK-AMP-GAIN-FEASIBILITY** — can the device meet the gain spec, and is a unilateral design valid (POZAR-373…378)
- Inputs: S-parameters at the design frequency, `G_req_dB`, `unilateral_error_max_dB` (default 0.3 = "a few tenths").
- Formula: K > 1 → GT_max = |S21/S12|·(K − sqrt(K² − 1)) with ΓS, ΓL from (12.40); K < 1 → MSG = |S21|/|S12|; unilateral: GTU_max = |S21|²/((1 − |S11|²)(1 − |S22|²)); U = |S12S21S11S22|/((1 − |S11|²)(1 − |S22|²)), error band 20·log10(1/(1 ± U)).
- Pass: G_req <= GT_max (or MSG) and, if a unilateral design is used, max(|20log10(1/(1−U))|, |20log10(1/(1+U))|) <= unilateral_error_max_dB. Margin = GT_max − G_req (dB).
- Test vectors: Ex.12.3 → ΓS = 0.872∠123°, ΓL = 0.876∠61°, GT_max = 16.7 dB; Ex.12.4 → GTU_max = 13.5 dB; Ex.12.5 → U = 0.059, −0.50…+0.53 dB; Problem 12.13 → −2.9…+4.3 dB (unilateral assumption invalid).

**CHECK-LNA-NOISE-MATCH** — noise figure at the chosen source termination (POZAR-379…381)
- Inputs: `Fmin_dB`, `Gamma_opt` (complex), `RN_ohm`, `Z0`, chosen `GammaS`, `NF_spec_dB`.
- Formula: F = Fmin + 4(RN/Z0)|ΓS − Γopt|²/((1 − |ΓS|²)|1 + Γopt|²) (linear); noise circle for the spec: N = (F_spec − Fmin)|1 + Γopt|²/(4RN/Z0), CF = Γopt/(N+1), RF = sqrt(N(N + 1 − |Γopt|²))/(N+1).
- Pass: F(ΓS) <= F_spec (i.e. |ΓS − CF| <= RF). Margin = NF_spec − NF(ΓS) dB.
- Test vector: Ex.12.5 → N = 0.0986, CF = 0.56∠100°, RF = 0.24; ΓS = 0.53∠75° gives F = 2.0 dB.

**CHECK-PA-BUDGET** — power-amplifier drive, DC and efficiency (POZAR-392…398)
- Inputs: `Pout_dBm`, `G_dB` (large-signal at Pout), `eta_drain`, `V_DD`, `P_device_rated_W`, `class`, `PAE_spec`.
- Formula: Pin = Pout − G; P_DC = Pout/η; I_D = P_DC/V_DD; PAE = (Pout − Pin)/P_DC = (1 − 1/g)·η; class ceiling η_max: A 0.50, B 0.78, C ≈ 1.
- Pass: P_device_rated >= 1.2·Pout (POZAR-397); η <= η_max(class); PAE >= PAE_spec; heatsink required if Pout > "a few tenths of a watt". Margins: P_device_rated/(1.2·Pout) − 1; PAE − PAE_spec.
- Test vector: Ex.12.9 (10 W, 16.4 dB, 26 %, 28 V) → Pin = 23.6 dBm (229 mW), P_DC = 38.5 W, I_D = 1.37 A, PAE = 25 %.

**CHECK-LO-PHASE-NOISE** — LO phase-noise requirement from reciprocal mixing, and Leeson estimate (POZAR-414…419)
- Inputs: per interferer row `offset_Hz`, `I_dBm`; `C_dBm` (wanted signal), `S_dB` (required rejection), `B_IF_Hz`; LO data: either datasheet `L_dBcHz(offset)` or Leeson inputs `f0_Hz`, `Q_loaded`, `F_dB`, `P0_dBm`, `f_alpha_Hz`, `K` (default 1); multiplication factor `n` if the LO is multiplied.
- Formula: L_req(fm) = C − S − I − 10·log10(B_IF); Leeson SSB: L(fm) = −174 + F − P0 + 10·log10(K·fα·fh²/fm³ + fh²/fm² + K·fα/fm + 1) − 3.01, fh = f0/(2Q); multiplied LO: L + 20·log10(n).
- Pass: L_LO(fm) + 20log10(n) <= L_req(fm) at every interferer offset. Margin = L_req − L_LO (dB), minimum over offsets.
- Test vectors: Ex.13.5 GSM → −138 / −128 / −118 dBc/Hz at 3 / 1.6 / 0.6 MHz; Problem 13.12 → −121 dBc/Hz; Problem 13.9 (Leeson) → −181 dBc/Hz at 1 MHz, −153 dBc/Hz at 10 kHz.

**CHECK-MIXER-FREQUENCY-PLAN** — image and in-band IM3 products (POZAR-330, 423…427)
- Inputs: `RF_band` [f_lo, f_hi], `f_IF`, `LO_side` ∈ {high, low}, preselector response (for CHECK-FILTER-ORDER), `image_rejection_req_dB`, two strongest in-band carriers `f1`, `f2`, `P_dBm`, `OIP3_dBm`.
- Formula: f_LO = f_RF ± f_IF; image f_IM = f_LO ± f_IF on the opposite side (= f_RF ± 2f_IF); IM3 at 2f1 − f2, 2f2 − f1 with P_IM3 = 3P − 2·OIP3; mixer SSB NF = DSB NF + 3 dB.
- Pass: image band entirely outside RF band and preselector IL(f_IM) >= image_rejection_req; IM3 products either out of channel or below the noise/sensitivity floor. Margins: preselector IL(f_IM) − requirement; floor − P_IM3.
- Test vector: Ex.13.7 IS-54 (869–894 MHz, IF 87 MHz) → high-side LO 956–981 MHz, image 1043–1068 MHz (outside band).

**CHECK-RECEIVER-GAIN-PLAN** — gain per frequency band (POZAR-456)
- Inputs: chain table with `stage`, `band` ∈ {RF, IF1, IF2, BB}, `G_dB`.
- Formula: G_band = Σ G_dB within each band.
- Pass: every G_band <= 60 dB (warn above 50 dB). Margin = 60 − max(G_band).

**CHECK-RADAR-RANGE** — maximum range, unambiguous range, T/R isolation (POZAR-466…470)
- Inputs: `Pt_W`, `G_dBi`, `f_Hz`, `sigma_m2` (Table T2.21), `P_min_W` (or from T_sys, B, SNR), `N_pulses_integrated`, `PRF_Hz`, `R_req_m`, `isolation_TR_dB`.
- Formula: R_max = (Pt·G²·σ·λ²/((4π)³·P_min/N))^(1/4) (≈N integration gain); R_unamb = c/(2·PRF); Doppler band fd = 2v f0/c.
- Pass: R_max >= R_req; R_unamb >= R_req; pulse radar isolation_TR >= 80 dB (book 80–100 dB). Margins: 40·log10(R_max/R_req) dB (link-equivalent), R_unamb − R_req.
- Test vectors: Ex.14.7 → 8114 m; Problem 14.17 → Doppler 80–1600 Hz for 1–20 m/s at 12 GHz.

**CHECK-RF-EXPOSURE** — power density near a transmitter and SAR (POZAR-479, 480)
- Inputs: `Pt_W`, `Gt_dBi`, `R_m` (evaluation distance, main beam and worst sidelobe level `SLL_dB`), `S_limit_Wm2` (from IEEE C95.1-2005 curve at f, general or controlled), handheld `SAR_Wkg` (measured/simulated).
- Formula: S = Pt·Gt/(4πR²) (far field); sidelobe S·10^(SLL/10); SAR = σ|E|²/(2ρ).
- Pass: S <= S_limit; SAR <= 1.6 W/kg over 1 g (US) / 2 W/kg over 10 g (EU); microwave ovens <= 1 mW/cm² at 5 cm. Margin = 10·log10(S_limit/S) dB.
- Test vector: Ex.14.8 → 8 W/m² main beam, 0.8 W/m² sidelobe at 20 m (10 W, 36 dBi, 18 GHz).

**CHECK-ANTENNA-NOISE-GT** — antenna temperature, system temperature, G/T (POZAR-444…448)
- Inputs: `Tb_K` (sky/ground, Fig.14.6 / 3–5 K zenith, 50–100 K horizon, 290–300 K ground), `eta_rad`, `Tp_K`, feed-line `L_dB`, `Gamma_ant`, receiver `T_rec_K`, `G_dBi`, `GT_spec_dBK`.
- Formula: TA = η·Tb + (1 − η)Tp; TS = ((1 − |Γ|²)/L)·TA + ((L − 1)/L)(1 + |Γ|²/L)·Tp; T_sys = TS + T_rec (at receiver input); G/T = G − 10log10(T_sys) with G referred to the same plane.
- Pass: G/T >= GT_spec. Margin = G/T − GT_spec.
- Test vectors: Ex.14.4 → G/T = 13.5 dB/K; Problem 14.6 → η_rad = 65 % from TA = 105 K; Ex.14.5 → TA = 210 K, T_SYS = 762 K.

**CHECK-ANTENNA-FAR-FIELD-DISTANCE** — test range / coupling distance (POZAR-438, 443)
- Inputs: `D_m` (max dimension), `f_Hz`, `R_m` (test or separation distance); for apertures `A_m2`, `eta_ap`.
- Formula: R_ff = max(2D²/λ, 2λ); D_dir = η_ap·4πA/λ²; Ae = G·λ²/(4π).
- Pass: R >= R_ff. Margin = R/R_ff.
- Test vectors: Ex.14.1 → 17.3 m (0.457 m, 12.4 GHz); Problem 14.4 → D = 33.6 dB (η_ap = 0.65).

**CHECK-COUPLER-HYBRID-DESIGN** — coupled-line / Lange / Wilkinson element feasibility (POZAR-201, 204, 226…237, 244)
- Inputs: `topology` ∈ {coupled_line, lange, wilkinson_equal, wilkinson_unequal, branch_line, rat_race}, `Z0`, `C_dB` or power ratio `K2 = P3/P2`, fabrication window `Z_min`, `Z_max`, required directivity `D_req_dB` (e.g. for reflectometers).
- Formula: coupled line C = 10^(−C_dB/20), Z0e,o = Z0·sqrt((1 ± C)/(1 ∓ C)); Lange per POZAR-237; Wilkinson equal Z = √2·Z0, R = 2Z0; unequal Z03 = Z0·sqrt((1+K²)/K³), Z02 = K²Z03, R = Z0(K + 1/K); branch-line Z0/√2 and Z0; rat-race √2·Z0; reflectometer uncertainty ±1/10^(D/20).
- Pass: all impedances within [Z_min, Z_max]; single-section edge coupling only for weak coupling (use Lange for 3–6 dB); if D_req is high (a reflectometer "preferably > 40 dB"), flag plain coupled microstrip (unequal mode velocities, POZAR-230) and prefer stripline or velocity-compensated lines — confirm by EM simulation; reflectometer: 10^(−D/20) <= allowed |Γ| error. Margin = min impedance headroom (ohm).
- Test vectors: Ex.7.2 → 70.7 Ω / 100 Ω; Ex.7.7 → 55.28 / 45.23 Ω; Ex.7.8 → 50.63/49.38, 56.69/44.10 Ω; Lange 3 dB, Z0 = 50 → Z0e ≈ 176 Ω, Z0o ≈ 52.6 Ω (computed).

**CHECK-CIRCULATOR-ISOLATOR** — isolation implied by port match and load rating (POZAR-304, 311)
- Inputs: port return loss `RL_dB` (worst port), load `Gamma_L`, forward power `P_fwd_W`, isolator/termination rating `P_rated_W`, `Iso_spec_dB`.
- Formula: Isolation ≈ RL (|S_iso| ≈ |Γ|); transmission loss ≈ −10log10(1 − |Γ|²); P_absorbed = |Γ_L|²·P_fwd.
- Pass: RL >= Iso_spec (necessary); P_rated >= P_absorbed (with the worst-case |Γ_L| = 1 for an open/short load when the load can fail). Margins: RL − Iso_spec; P_rated − P_absorbed.

**CHECK-PIN-SWITCH** — ON/OFF insertion loss from diode parameters (POZAR-341…343)
- Inputs: `topology` ∈ {series, shunt}, `f_Hz`, `Rf`, `Rr`, `Cj`, `Li`, `Z0`, `IL_on_max_dB`, `Iso_min_dB`.
- Formula: Zr = Rr + j(ωLi − 1/(ωCj)); Zf = Rf + jωLi; series IL = −20log10|2Z0/(2Z0 + Zd)|; shunt IL = −20log10|2Zd/(2Zd + Z0)| (ON uses Zf for series / Zr for shunt; OFF the opposite).
- Pass: IL_on <= IL_on_max and IL_off >= Iso_min. Margins = differences.
- Test vector: Ex.11.1 (UM9605 at 1.8 GHz) → series 0.14/6.0 dB, shunt 0.11/13.3 dB.

**CHECK-OSCILLATOR-STARTUP** — negative-resistance start-up margin and feedback-oscillator Q (POZAR-403…410)
- Inputs: small-signal `Z_in` of the active port at the design frequency, chosen termination `Z_S`; or Colpitts `L3`, `Q0`, `C1`, `C2`, `gm`, `Gi`.
- Formula: start-up requires Re(Z_S) + Re(Z_in) < 0 with Re(Z_S) ≈ −Re(Z_in)/3 and Im(Z_S) = −Im(Z_in); Colpitts R_max = Gi·((1 + gm/Gi)/(ω0²C1C2) − L3/C1), Q_min = ω0L3/R_max.
- Pass: Re(Z_S)/|Re(Z_in)| <= 1/3 (book practice) and Q0 >= 2·Q_min (margin factor is a design choice; book only requires Q0 > Q_min). Margin = Q0/Q_min.
- Test vectors: Ex.13.3 → Zin = −84 − j1.9 Ω, Z_S = 28 + j1.9 Ω; Ex.13.1 → R_max = 6.13 Ω, Q_min = 5.1 (Q0 = 100).

**CHECK-MULTIPLIER-NOISE-AND-EFFICIENCY** — multiplier output estimate (POZAR-419…422)
- Inputs: `n`, `type` ∈ {varactor, SRD, resistive, FET}, `P_in_dBm`, `L_in_dBcHz`.
- Formula: phase noise out = L_in + 20log10(n); resistive efficiency <= 1/n²; FET doubler I_n per POZAR-421.
- Pass: output phase noise meets the LO requirement (CHECK-LO-PHASE-NOISE); expected P_out = P_in + 10log10(η) meets need. Margin = requirement − predicted.
- Test vector: Ex.13.6 FET doubler → τ/T = 0.406, I2 = 21.0 mA, P2 = 21.0 mW, Gc = 2.9 dB.

**CHECK-RADIOMETER-RESOLUTION** — total-power radiometer error budget (POZAR-473)
- Inputs: `TB_K`, `TR_K`, `B_Hz`, `tau_s`, `dG_over_G`, `dT_spec_K`.
- Formula: ΔT_N = (TB + TR)/sqrt(B·τ); ΔT_G = (TB + TR)·ΔG/G.
- Pass: sqrt(ΔT_N² + ΔT_G²) <= dT_spec (root-sum-square combination is an Anvil convention, not from the book); if ΔT_G dominates, require Dicke switching (10–1000 Hz). Margin = dT_spec − combined error.
- Test vector: 10 GHz example → ΔT_N = 0.8 K, ΔT_G = 8 K.

## 4. Verification procedures & plots

Each item: property → plot (x / y) → sweep/corners → what good looks like (book) → pass criterion → setup notes. Pass limits come from the design spec unless the book states one.

| # | property | plot (x → y) | sweep / corners | what good looks like (per book) | pass criterion | setup / notes | source |
|---|---|---|---|---|---|---|---|
| V1 | Power divider / hybrid response | f/f0 (0.5–1.5) → \|S11\|, \|S21\|, \|S31\|, \|S23\| (or \|S14\|) in dB | ideal and with conductor + dielectric loss (tanδ, Cu thickness) | Wilkinson, branch-line, rat-race: perfect match/split/isolation at f0, degrading quickly away (branch-line BW 10–20 %, ring 20–30 %) | split, RL, isolation meet spec across the band | CAD S-parameter sweep; Figs.7.12, 7.25, 7.46 | POZAR-202, 220, 239 |
| V2 | Coupler coupling & directivity | f (GHz) → C (dB), D (dB) | ±20–30 % around f0; lossless vs lossy; microstrip vs stripline | C nearly flat; D peaks at f0 (> 60–70 dB ideal) and falls to 15–20 dB at band edges for single-aperture designs; losses reduce D | C within ±x dB, D >= D_req over band | Figs.7.17, 7.20, 7.34, 7.37 | POZAR-210, 217, 231, 233 |
| V3 | Periodic / slow-wave line passbands | βd (rad) → k0d (dispersion, Brillouin diagram) | k0d from 0 to ~4 | passbands where \|cos k0d − (b/2) sin k0d\| <= 1; vp = c·k0/β | stopband edges where required | Fig.8.6 | POZAR-246, 249 |
| V4 | Filter amplitude response | f → insertion loss (dB) (and return loss) | lumped prototype vs distributed; lossless vs lossy (tanδ, conductor); wide sweep to 4–5 × fc to expose spurious passbands | Butterworth monotone; Chebyshev equal ripple; distributed LPF sharper cutoff but repeats (Richards: every 4fc; stepped-impedance: non-periodic spurious bands); coupled-line BPF repeats at 3f0, 5f0 | passband IL/ripple and stopband rejection at f_stop meet spec (CHECK-FILTER-ORDER) | Figs.8.20, 8.30a, 8.33, 8.37, 8.41, 8.46, 8.49, 8.51, 8.54 | POZAR-256, 272, 276, 279, 286, 289, 291, 294 |
| V5 | Filter group delay | f → τ_d (ns) | same filters, same N | linear-phase flattest delay, equal-ripple worst (delay peaks at band edge) | delay variation within spec | Fig.8.30b | POZAR-262, 272 |
| V6 | Noise temperature / noise figure measurement | f → Te (K) or NF (dB) | hot/cold loads (e.g. 290 K and 77 K, or noise source ENR 20–40 dB) | Y well above 1 for accuracy | NF <= spec | Y = N1/N2, Te = (T1 − Y·T2)/(Y − 1); matched source; Ex.10.1 | POZAR-315, 316, 317 |
| V7 | Compression and intercept | Pin (dBm) → Pout (dBm) for fundamental (slope 1) and IM3 (slope 3), two-tone | tones closely spaced, equal level; well below P1dB for extrapolation | P1dB where fundamental is 1 dB below linear; IP3 at the slope-1/slope-3 intersection, typically 10–15 dB above P1dB | OP1dB, OIP3 >= spec (CHECK-RF-CASCADE-IP3) | spectrum analyzer; OIP3 = P_fund + ΔP/2; Figs.10.15, 10.17 | POZAR-329, 331, 337 |
| V8 | Detector law | Pin (dBm) → log V_out | from noise floor to saturation | square-law region (V_out ∝ Pin) over a limited range; linear/saturated above | operating range inside square-law region when power is inferred | Fig.11.5 | POZAR-340 |
| V9 | Amplifier stability | f → K, \|Δ\|, µ; Smith-chart stability circles at several f | full S-parameter band (not just design band), each bias point, with realized ΓS(f), ΓL(f) | µ > 1 (or K > 1 and \|Δ\| < 1) everywhere; otherwise terminations inside stable regions | CHECK-AMP-STABILITY margin >= 0 at all f | Fig.12.6; also transient/CAD check for oscillation | POZAR-367–372, 375 |
| V10 | Amplifier gain and match | f → GT (dB) and −RL (dB) | design band ± ~25 % | conjugate match: max gain, ~2.5 % 1-dB BW, good RL; specified-gain: ±1 dB over ~25 % but RL ≈ 5 dB; balanced: good RL over the coupler bandwidth | gain flatness, RL meet spec | Figs.12.7c, 12.8c, 12.12 | POZAR-375, 378, 386 |
| V11 | Gain / noise circles | Smith chart (ΓS plane) → constant GS circles and constant-F circles | several GS, F values | choose ΓS at tangency of the highest-gain circle with the F_spec circle | F(ΓS) <= spec, GT >= spec | Figs.12.8a, 12.9a | POZAR-377, 380, 381 |
| V12 | Power-amplifier large-signal behaviour | ΓL (Smith chart) → constant-Pout (load-pull) contours; Pin → Pout, PAE | drive up to/above OP1dB; temperature | max-Pout load differs from small-signal conjugate; PAE peak near compression | Pout, PAE, gain at rated Pout meet spec | automated load-pull tuners; Fig.12.21 | POZAR-396–398 |
| V13 | Distributed amplifier gain | f → gain (dB) for N = 2, 4, 8, 16 | 1–18 GHz | larger N rolls off faster; optimum N at the top frequency | gain at f_max maximal at N_opt | Fig.12.16 | POZAR-388, 389 |
| V14 | Oscillator start-up / stability | f → Re, Im of Z_in + Z_L (or \|Γ_out\| vs Δf/f0) | small-signal and large-signal; temperature | net negative resistance at start-up; steep reactance slope (high Q); DRO \|Γ_out\| collapses within a few 0.01 % of f0 | Kurokawa condition satisfied; start-up margin RS ≈ −Rin/3 | Fig.13.12b; POZAR-408 | POZAR-407–413 |
| V15 | Phase noise | log offset fm → L(fm) (dBc/Hz) | 10 Hz–10 MHz offsets | 1/f³ close-in (−18 dB/oct), then 1/f² (−12 dB/oct) or 1/f (−6 dB/oct), then flat floor at kT0F/P0 | L(fm) <= reciprocal-mixing requirement at each interferer offset | spectrum analyzer / phase-noise set; Fig.13.17 | POZAR-414–418 |
| V16 | Mixer conversion and spurs | LO power (dBm) → conversion loss; RF sweep → IF output spectrum | LO 0–10 dBm; image frequency; two-tone | minimum loss at 0–10 dBm LO; image suppressed by preselector or image-reject topology; LO leakage at RF port 20–40 dB down | Lc, image rejection, LO leakage meet spec | Table 13.1 topology choice | POZAR-423–434 |
| V17 | Antenna pattern | angle θ (deg) → normalized pattern (dB, 20log\|F\|) polar or rectangular | E- and H-planes | main beam, HPBW, sidelobe levels (e.g. −13 dB first sidelobe for the horn example) | HPBW, SLL, D (≈ 32,400/(θ1θ2)) meet spec | Fig.14.3 | POZAR-440, 441 |
| V18 | Link budget | stages → cumulative level (dBm) (waterfall); range → CNR | worst-case slant range, rain/atmospheric loss | positive link margin (3–20 dB typical; ≥ 20 dB fade margin above 10 GHz satellite) | CHECK-LINK-BUDGET-MARGIN | Ex.14.4 | POZAR-451–455 |
| V19 | Digital link BER | Eb/n0 (dB) → Pb (log) | modulation type | Table 14.1 thresholds for Pb = 1e-5 | Pb <= target at the budgeted Eb/n0 | Fig.14.16 | POZAR-460–462 |
| V20 | Sky noise / atmospheric loss | f (GHz) → T_B (K) or dB/km | elevation angles; sea level vs altitude | low sky T at zenith, peaks at 22 and 60 GHz; windows 35/94/135 GHz | T_sys / LA assumptions in budgets | Figs.14.6, 14.29 | POZAR-444, 475 |
| V21 | RF exposure | distance R (m) → power density (W/m²) main beam and sidelobe | Pt, G, frequency | falls as 1/R² in the far field | below IEEE C95.1-2005 curve (Fig.14.32) at the accessible distance; SAR <= 1.6 W/kg (1 g) for handhelds | Ex.14.8 | POZAR-479, 480 |
| V22 | Radiometer calibration | time → output voltage with two calibrated noise loads | integration τ, gain drift | calibration gives G·k·B and G·TR·k·B; Dicke switching removes gain drift | ΔT within spec | total-power vs Dicke | POZAR-473 |

## 5. Pitfalls, failure modes, review checklist

- [ ] Computing absolute output noise as k·TA·B·F·G when the source is not at 290 K — use noise temperatures, No = k(TA + Te)BG (Ex.10.2 note, p.506).
- [ ] Noise figure is only defined for a matched source at T0 = 290 K; do not use a "system NF" when the antenna temperature differs from T0 (§14.2 p.680).
- [ ] First stage sets the cascade NF: put the low-NF, moderate-gain stage first; any loss ahead of the LNA (filter, cable, switch) adds its loss in dB directly to NF at 290 K (§10.2 p.504–505).
- [ ] Input mismatch raises amplifier NF: Fm = 1 + (F − 1)/(1 − |Γ|²) (§10.2 eq.10.36).
- [ ] A Wilkinson (or any divider) used as a 2-port adds noise: F = 2L (3 dB lossless) at room temperature (Ex.10.3).
- [ ] Stability checked only at the design frequency — check K/µ over the device's entire gain bandwidth and every bias point (§12.2 p.564, 567).
- [ ] Conditionally stable design: verify out-of-band that the realized frequency-dependent ΓS, ΓL stay inside the stable regions (Ex.12.3 at 3 GHz).
- [ ] Simultaneous conjugate match attempted with K < 1 — not solvable; use MSG and deliberate mismatch/resistive loading (§12.3 p.572).
- [ ] Conjugate-matched amplifier is narrowband (≈ 2.5 % 1-dB BW in Ex.12.3); specified-gain design widens BW (≈ 25 %) but degrades return loss (≈ 5 dB) — fix with a balanced topology (Ex.12.4, 12.7).
- [ ] Unilateral design used where U-error exceeds a few tenths of a dB (Problem 12.13: −2.9 to +4.3 dB) (§12.3 eq.12.45).
- [ ] Large-signal S-parameters treated as unique/linear — they depend on drive, load, bias, temperature; use small-signal S for stability, load-pull/ΓLP for power matching (§12.5 p.598).
- [ ] PA without stability margin — high-power oscillation can destroy the device; heatsink anything above a few tenths of a watt; pick a device with ~20 % power headroom (§12.5 p.599).
- [ ] More than ~50–60 dB of gain in one frequency band of a receiver → instability/oscillation (§14.2 p.677).
- [ ] Filter order read off attenuation graphs can be optimistic: Ex.8.9 chose N = 3 for ≥ 20 dB at normalized 1.91, but the Chebyshev formula gives 17.8 dB — compute IL exactly (CHECK-FILTER-ORDER).
- [ ] Even-order Chebyshev prototype drives a non-unity load (g_{N+1} = 1.9841 at 0.5 dB, 5.8095 at 3 dB) — add a λ/4 transformer or use odd N (§8.3 p.405–406).
- [ ] Stub / inverter filter formulas assume Z0 terminations — not valid for even-N equal-ripple designs (§8.8 p.440).
- [ ] Stub filters can demand unrealizable impedances (Ex.8.8: 387 Ω) — check against the fabrication impedance window before layout.
- [ ] Kuroda identities are not useful for high-pass or bandpass filters (§8.5 p.421).
- [ ] Richards-transformed filters repeat every 4fc and have a pole at 2fc — check spurious passbands against system spectrum (§8.5 p.416, Ex.8.5).
- [ ] Stepped-impedance LPFs: lines are not commensurate, lumped approximation fails above cutoff (less high-f rejection than lumped, spurious bands), sections should stay < 45° (§8.6 p.424–426).
- [ ] Coupled-line BPFs only practical below about 20 % bandwidth; inverter-based designs for < 10 % (§8.5 p.421, §8.7 p.426).
- [ ] Losses (tanδ, thin copper) raise passband loss (≈ 1 dB at 2 GHz on FR4 in Ex.8.6) and cut coupler directivity — always simulate with loss (§7.6 Ex.7.7, §8.6 Ex.8.6).
- [ ] Coupled microstrip couplers/filters: unequal even/odd phase velocities → poor directivity; multisection couplers are more sensitive — prefer stripline or compensation (§7.6 p.355, 357).
- [ ] Single-section coupled-line couplers cannot realize tight (3–6 dB) coupling — use Lange/interdigitated (§7.6 p.355, §7.7 p.359).
- [ ] Branch-line hybrid: shunt arms may need +10–20° for junction parasitics; bandwidth only 10–20 % (§7.5 p.346).
- [ ] Wilkinson isolation resistor dissipates all power reflected from the outputs (and imbalance when combining) — rate it for the worst-case output mismatch (§7.3 p.331).
- [ ] Reflectometer/VSWR monitor with a low-directivity coupler gives ±1/D error — use ≥ 40 dB directivity (§7 POI p.374–375).
- [ ] Circulator isolation is only as good as its port match (isolation ≈ return loss) (§9.6 eq.9.94).
- [ ] Isolator protecting a source absorbs all reflected power — its load must be rated for the worst reflection (§9.4 p.476).
- [ ] Ferrites below saturation are lossy; Ms drops with temperature (Curie) — thermal design of high-power ferrite parts (§9.1 p.455, §9.4 p.478).
- [ ] Magic-T tuning posts/irises placed asymmetrically destroy sum/difference isolation (§7.8 p.371).
- [ ] Diode detector used outside its square-law range gives wrong power readings (§11.1 p.528–529).
- [ ] PIN switch OFF state reflects (not absorbs) the incident power; shunt SPDT with λ/4 lines is band-limited (§11.1 p.531–532).
- [ ] Switched-line phase shifter OFF line near nλ/2 resonates (shifted by diode Cj) (§11.1 p.535).
- [ ] MMIC: no post-fab trimming — tolerances, discontinuities, bias networks, coupling and package resonances must be in the design; expensive in small volumes; limited power and Q (§11.4 p.549–550).
- [ ] Oscillator designed exactly at Rin + RS = 0 may not start (Rin shrinks as amplitude grows) — use RS ≈ −Rin/3; expect the running frequency to differ from the design value (§13.2 p.614–617).
- [ ] Oscillator with low-Q tank has poor frequency stability and close-in phase noise ∝ 1/Q² (§13.2 eq.13.30, §13.3 p.626).
- [ ] GaAs MESFET 1/f corner (2–10 MHz) → worse close-in phase noise than Si BJT (5–50 kHz) or JFET (50–100 Hz) oscillators (§13.3 p.625).
- [ ] Frequency multipliers raise phase noise by 20·log n (6 dB doubler, 9.5 dB tripler) (§13.4 p.628).
- [ ] Varactor triplers need an idler (2f0) current path (§13.4 p.630).
- [ ] Mixer image not pre-selected → image-band signals are indistinguishable at IF (§13.5 p.639).
- [ ] SSB mixer noise figure is 3 dB worse than the DSB value quoted on some datasheets (§13.5 eq.13.97).
- [ ] LO leakage out of the mixer RF port is radiated by the antenna (regulated) — add a preselector or LNA (§13.5 p.641).
- [ ] 90° balanced mixer: RF–LO isolation depends on diode matching; use a 180° hybrid when isolation matters (§13.5 p.646–649).
- [ ] Reciprocal mixing (LO phase noise) usually limits receiver selectivity more than SNR — derive LO L(fm) from adjacent-channel blocking levels (§13.3 p.626–627).
- [ ] Passive intermodulation from connectors, oxidized ferrous joints, contamination, carbon-fibre or ferromagnetic hardware in high-power transmit paths (base stations 30–40 dBm; target < −125 dBm) — specify PIM-rated parts and maintenance (§10.3 p.519).
- [ ] Antenna noise from sidelobes seeing hot ground can dominate (Ex.14.3: most of 86.4 K from sidelobes) (§14.1 p.669–670).
- [ ] Antenna mismatch and feed-line loss both reduce received signal and add line noise (TS formula) (§14.1 eq.14.19).
- [ ] Polarization mismatch: linear-to-circular costs 3 dB, crossed linear → no power (§14.2 p.675).
- [ ] Link budget with no fade margin: satellite links above 10 GHz often need ≥ 20 dB rain margin (§14.2 p.675).
- [ ] Pulse radar with only a circulator for T/R isolation (20–30 dB vs 80–100 dB needed) (§14.3 p.693).
- [ ] CW Doppler filter must reject DC (clutter, leakage, 1/f) (§14.3 p.694).
- [ ] 22 GHz (H2O) and 60 GHz (O2) absorption lines — do not place terrestrial links there unless short range/security is intended (§14.5 p.702).
- [ ] RF exposure: check main-beam and sidelobe power density at accessible distances against IEEE C95.1-2005; handheld SAR ≤ 1.6 W/kg (1 g, US) / 2 W/kg (10 g, EU) (§14.6 p.706–707).
- [ ] Microwave oven door: λ/4 choke flange + absorber, leakage ≤ 1 mW/cm² at 5 cm (§14.6 p.705–707).
- [ ] Source-text errata noticed during extraction (verify before reuse): eq.(13.74) printed Vgg = (Vgmax − Vgmin)/2 but Ex.13.6 evaluates the mean (Vgmax + Vgmin)/2; eq.(12.83) prints Cds where the derivation gives Cgs; Ex.13.3 cites "(11.25)" for the stability circle (should be 12.25); Table 12.1 S12/S21 column labels appear transposed in the extraction; Appendix I WR-12 inside height printed 0.015 cm (0.155 expected); Table 11.8 VDD printed "328 V" (28 V expected); Appendix F lists germanium σ = 2.2e6 S/m (as printed); pulse widths quoted "100 ms to 50 ns" (as printed).

## 6. Standards referenced

| standard / regulation | edition / year | clause / table | what it governs (as used in the text) | page |
|---|---|---|---|---|
| IEEE Std C95.1 | 2005 | Fig.14.32 (power-density limits vs frequency) | Human exposure to RF/microwave fields, 100 MHz–100 GHz: general population (30 min average) and controlled/occupational (6 min average) limits; separate E/H limits below 100 MHz | p.706–707 |
| FCC exposure rule for hand-held wireless devices (US) | as of 2012 | SAR limit | SAR ≤ 1.6 W/kg averaged over 1 g of tissue (partial-body: head/hand) for all devices sold in the US | p.707 |
| European Union hand-held SAR requirement | as of 2012 | SAR limit | SAR < 2 W/kg averaged over 10 g of tissue | p.707 |
| US microwave-oven emission standard | as of 2012 | leakage limit | ≤ 1 mW/cm² at 5 cm from any point on the oven | p.707 |
| IEEE 802.11 (a, b, g, n) "Wi-Fi" | — | — | WLAN at 2.4 / 5.7 GHz ISM, FHSS/DSSS; up to 54 Mbps (a/b/g), 150 Mbps (n, multi-antenna) | p.688 |
| Bluetooth | — | — | 2.4 GHz short-range networking; 1–100 mW for 1–100 m; 1–24 Mbps | p.688 |
| GSM (850/900/1800/1900) | — | Table 14.2; Ex.13.5 blocking levels | Cellular bands; receiver must reject −23 / −33 / −43 dBm interferers at 3 / 1.6 / 0.6 MHz by ≥ 9 dB for a −99 dBm carrier, 200 kHz channels | p.627, 685 |
| IS-54 digital cellular | — | Ex.13.7 | Receive band 869–894 MHz, first IF 87 MHz, 30 kHz channels | p.641 |
| AMPS | 1983 (obsolete) | Table 14.2 | U 824–849 / D 869–894 MHz analog FM cellular | p.685 |
| ITU IMT-2000 (3G); 3GPP / UMTS; 3GPP2 (CDMA2000, W-CDMA); LTE | as of 2012 | — | 3G: 2 Mbps fixed / 144 kbps mobile; LTE goal 100 / 50 Mbps; UMTS band allocations in Table 14.2 | p.685–686 |
| GPS (NAVSTAR) signal structure | — | L1 C/A and P codes; L2 P code | L1 1575.42 MHz, L2 1227.60 MHz, BPSK spread spectrum; ≈ −130 dBm received with 0 dBi antenna | p.687–688 |
| DBS (direct broadcast satellite) allocations | — | Table 14.2 | 10.7–12.75 GHz (Europe/Russia), 12.2–12.7 GHz (Americas), 11.7–12.2 GHz (Asia/Australia) | p.685, 689 |
| ISM bands | — | Table 14.2 | 902–928 MHz, 2.400–2.484 GHz, 5.725–5.850 GHz | p.685 |
| EIA rectangular waveguide designations (WR-xx) | — | Appendix I | Standard waveguide sizes, recommended ranges, TE10 cutoff | p.720 |
| RG/U coaxial cable designations | — | Appendix J | Standard coax impedance, dimensions, capacitance, voltage rating, 1 GHz loss | p.721 |
| Trans-Tech ferrite part numbers (manufacturer catalogue) | — | Appendix H | Microwave ferrite/garnet material properties | p.720 |

Note: standards cited only in the other half of the book (e.g. IEEE Std 211-1997 terminology, Ch.1) are covered by the part-1 extraction.

## 7. Process / lifecycle guidance

Pozar is a design-theory text, not a product-development book, so this section is limited to the design flows the text prescribes (useful as Anvil gate sequences for RF blocks).

| stage | activity | deliverable | exit criterion | source |
|---|---|---|---|---|
| Filter: specification | Fix response type (Butterworth / Chebyshev / elliptic / linear-phase), passband edges, ripple, stopband rejection, impedance | filter spec | spec complete; response type chosen by priority (min IL, sharpest cutoff, phase) | §8.3 p.399, 401 (POZAR-258) |
| Filter: prototype | Pick order N from IL(x, N) and g-values from Tables 8.3–8.5 | prototype ladder | CHECK-FILTER-ORDER passes | Fig.8.23, §8.3 |
| Filter: scaling & transformation | Impedance/frequency scale; LP→HP/BP/BS transform | lumped design | element values computed | §8.4 (POZAR-266–270) |
| Filter: implementation | Richards + Kuroda, stepped impedance, coupled lines, coupled resonators; verify realizability | distributed layout | CHECK-FILTER-REALIZABILITY passes; lossy EM/CAD sweep meets spec (V4, V5) | §8.5–8.8 |
| Amplifier: device & stability | Select transistor; check K/µ over full band and bias | stability report | CHECK-AMP-STABILITY passes (or stable-region terminations defined) | §12.2 |
| Amplifier: matching | Conjugate / specified-gain / noise-circle design; bias and decoupling networks | RF circuit + bias network | gain, NF, RL meet spec in CAD (V10, V11) | §12.3 |
| Amplifier: broadband/power | Balanced, distributed, feedback, or large-signal (load-pull) design | final amplifier | V12/V13 plots meet spec; thermal path defined | §12.4–12.5 |
| Oscillator | Choose unstable configuration, termination with start-up margin, high-Q resonator; phase-noise estimate | oscillator design | CHECK-OSCILLATOR-STARTUP and CHECK-LO-PHASE-NOISE pass | §13.1–13.3 |
| MIC/MMIC fabrication | CAD design & mask → photoresist/etch (hybrid) or implant/epi, ohmic contacts, gates, metal 1, resistors, dielectrics, metal 2, backside lap + vias (MMIC) → test | fabricated circuit | tests meet spec; MMIC designs must not rely on trimming | §11.4 p.548–550 |
| System: link & receiver | Link budget, receiver architecture, noise/gain plan, modulation choice | system budget | CHECK-LINK-BUDGET-MARGIN, CHECK-RF-CASCADE-NF, CHECK-RECEIVER-GAIN-PLAN pass | §14.2 |

## 8. Coverage log

Source file: `refs-text/Pozar_David_M_Microwave_engineering_2012_Wiley_libgen_li.txt` (65,005 lines). Assigned range: lines 32,500–65,005 (end). The other agent covers lines 1–32,500.

Read in order with the Read tool (offset / lines read), no chunk skipped:

| chunk | lines | content |
|---|---|---|
| orientation | 1–700 | front matter, preface, full TOC, start of Ch.1 (orientation only) |
| 1 | 32,500–33,299 | §7.3 Wilkinson even/odd analysis, Ex.7.2, unequal & N-way Wilkinson; §7.4 Bethe-hole coupler, Ex.7.3 start |
| 2 | 33,300–34,499 | Ex.7.3 end; multihole binomial/Chebyshev couplers, Ex.7.4; §7.5 quadrature hybrid, Ex.7.5; §7.6 coupled-line theory, Figs.7.29–7.30, Ex.7.6 |
| 3 | 34,500–35,799 | coupled-line coupler design eqs, Ex.7.7, multisection couplers, Ex.7.8; §7.7 Lange coupler; §7.8 180° hybrid start |
| 4 | 35,800–37,099 | ring hybrid, Ex.7.9; tapered coupled-line hybrid; magic-T; §7.9 other couplers; reflectometer POI; Ch.7 references and problems |
| 5 | 37,100–38,499 | Ch.7 problems end; Ch.8 intro; §8.1 periodic structures, Ex.8.1; §8.2 image-parameter method, Table 8.1, constant-k |
| 6 | 38,500–39,899 | m-derived and composite filters, Table 8.2, Ex.8.2; §8.3 insertion-loss method, Tables 8.3–8.5, Figs.8.26–8.27 |
| 7 | 39,900–41,299 | §8.4 transformations, Ex.8.3–8.4, Table 8.6; §8.5 Richards, Kuroda (Table 8.7), Ex.8.5, inverters; §8.6 stepped impedance, Ex.8.6 |
| 8 | 41,300–42,699 | Ex.8.6 end; §8.7 coupled-line filters, Table 8.8, design eqs, Ex.8.7 |
| 9 | 42,700–44,099 | §8.8 coupled-resonator filters, Ex.8.8–8.10, ceramic resonators; Ch.8 problems; Ch.9 intro, §9.1 start |
| 10 | 44,100–45,599 | permeability tensor, circular polarization, loss/linewidth, demagnetization (Table 9.1), Kittel, permanent magnets POI; §9.2 Faraday rotation, birefringence, Ex.9.1; §9.3 start |
| 11 | 45,600–47,099 | ferrite-loaded guide (eqs 9.73–9.84), §9.4 isolators, Ex.9.2–9.3; §9.5 phase shifters, Ex.9.4, gyrator; §9.6 circulators |
| 12 | 47,100–48,599 | junction circulator end; Ch.9 problems; Ch.10 §10.1 noise, Y-factor, Ex.10.1; §10.2 noise figure, cascade, Ex.10.2, passive/mismatched networks |
| 13 | 48,600–50,099 | Ex.10.3; mismatched amplifier; §10.3 nonlinear distortion, P1dB, IM products, IP3, cascade IP3, Ex.10.4, PIM; §10.4 dynamic range, Ex.10.5; problems; Ch.11 §11.1 Schottky diodes, Table 11.1 |
| 14 | 50,100–51,099 | detector (Table 11.2), spectrum analyzer POI, PIN diodes (Table 11.3), switches, Ex.11.1, phase shifters, varactors, Gunn/IMPATT/BARITT, power combining; §11.2 BJT/HBT (Tables 11.4–11.5); §11.3 FETs (Tables 11.6–11.8); §11.4 MIC/MMIC |
| 15 | 51,100–52,099 | MMIC process, RF MEMS POI; §11.5 tubes; Ch.11 problems; Ch.12 §12.1 gains, Ex.12.1 |
| 16 | 52,100–53,099 | eq.12.18; §12.2 stability circles, K–Δ and µ tests, Ex.12.2; §12.3 conjugate matching start |
| 17 | 53,100–54,099 | simultaneous match eqs, GTmax, MSG, Ex.12.3; unilateral figure of merit; constant-gain circles; Ex.12.4 start |
| 18 | 54,100–55,099 | Ex.12.4 end; low-noise design, noise circles, Ex.12.5 |
| 19 | 55,100–56,199 | inductive degeneration, Ex.12.6; §12.4 broadband, balanced (Ex.12.7), distributed amplifiers, Ex.12.8 start |
| 20 | 56,200–57,299 | Ex.12.8 end; differential amplifiers, CMRR; §12.5 power amplifiers, Table 12.1, Ex.12.9; Ch.12 problems; Ch.13 intro, §13.1 RF oscillators, Colpitts/Hartley, Ex.13.1, crystal start |
| 21 | 57,300–58,299 | crystal resonator; §13.2 negative-resistance oscillators, Kurokawa, Ex.13.2–13.3, DRO, Ex.13.4 start |
| 22 | 58,300–59,399 | Ex.13.4 end; §13.3 phase noise, Leeson, reciprocal mixing, Ex.13.5; §13.4 multipliers, Manley–Rowe, resistive and FET multipliers |
| 23 | 59,400–60,499 | FET multiplier, Ex.13.6; §13.5 mixers: image, conversion loss, NF (SSB/DSB), Ex.13.7, diode/FET mixers, Ex.13.8, balanced and image-reject mixers |
| 24 | 60,500–61,599 | differential/Gilbert mixers, double-balanced, subharmonic, Table 13.1; Ch.13 problems; Ch.14 §14.1 antennas, far field, directivity, gain, apertures, background/brightness temperature |
| 25 | 61,600–62,399 | eq.14.20, G/T; §14.2 wireless: Friis, link budget/margin, Ex.14.4, receiver architectures and noise, Ex.14.5, modulation/BER (Table 14.1), Ex.14.6, Table 14.2, systems; §14.3 radar start |
| 26 | 62,400–63,299 | radar equation, Ex.14.7, pulse and Doppler radar, RCS (Table 14.3); §14.4 radiometry; §14.5 propagation; §14.6 heating, power transfer, safety, Ex.14.8; Ch.14 problems; Appendices A–B start |
| 27 | 63,300–64,199 | Appendix B–D (math), E constants, F conductivities, G dielectrics, H ferrites (first half) |
| 28 | 64,200–65,005 | Appendix H end, I waveguides, J coax, answers to selected problems, index, end-matter useful results / ABCD table / vector formulas |

Two Read requests exceeded the tool's per-read token cap and were re-issued with smaller limits (50,100 → 1,000 lines; 61,600 → 800 lines); no lines were skipped. No Read result reported truncation of individual lines.

Skipped or not transcribed (read, then deliberately not turned into rules):
- Homework problem statements (kept only explicit "show that / derive" relations and the answer key, tagged conf=medium; answers used as test vectors in T2.30).
- Long derivations (kept only final design equations): even/odd derivations (Ch.7), ABCD manipulations (Ch.8), ferrite equations of motion and the slab-loaded-waveguide transcendental equations (9.73–9.84, numerical-solution only), Manley–Rowe derivation, distributed-amplifier summation algebra, differential-amplifier node analysis.
- Historical/descriptive prose (filter history, tube history, cellular history, Iridium business history) except numeric facts.
- Appendix B (vector identities), C (Bessel series/zeros; only p11' = 1.841 used for the circulator), D (integrals/Taylor series), and the Index — not design data.

Extraction limitations:
- OCR dropped or scrambled Greek letters and operators (Γ, Δ, ε, ℓ, √, fraction bars); equations were rebuilt from context and verified numerically against the worked examples (all reproduced; see §3 test vectors).
- Figures are absent; graph-dependent values (attenuation-vs-normalized-frequency curves Figs.8.26–8.27, coupled-line design charts Figs.7.29–7.30, µe vs H0 Fig.9.8, sky noise Fig.14.6, atmospheric loss Fig.14.29, exposure limits Fig.14.32, load-pull Fig.12.21) are marked conf=medium or referenced as "graph"; Smith-chart figure text was OCR noise and ignored.
- Table column alignment was reconstructed from sequential equal-length OCR lists for Appendices G, H, J and Table 12.1 (S12/S21 labels appear transposed in the extraction) — conf medium on alignment.
- Kuroda identities (c) and (d) of Table 8.7 could not be recovered reliably (transformer forms) and are marked low; (a) and (b) were verified from Fig.8.35 and Ex.8.5.
- Suspected source errata are listed at the end of §5 (eq.13.74 sign, eq.12.83 Cds/Cgs, Ex.13.3 equation reference, WR-12 dimension, Table 11.8 VDD, germanium conductivity, pulse-width range).
