# Balanis, Antenna Theory: Analysis and Design (4th ed.), part 2 — Anvil rulebook

## 0. Citation

C. A. Balanis, *Antenna Theory: Analysis and Design*, 4th ed. Hoboken, NJ, USA: John Wiley & Sons, 2016.
ISBN printed in the CIP block as "978-1-118-642060-1" (OCR/print artifact; the 13-digit form is 978-1-118-64206-1).
BOOKTAG `BALANIS`; this file holds ids BALANIS-200 and up (part 1, lines 1-37000, is a separate file).

Chapters covered by THIS extraction (source text lines 37000-73949, printed p.491-1072):
§9.2B-9.9 (broadband dipoles, matching), Ch 10 (traveling-wave/broadband: long wire, V, rhombic, helix, Yagi-Uda),
Ch 11 (frequency-independent, LPDA, Chu limit, miniaturization, fractals), Ch 12 (aperture antennas),
Ch 13 (horns), Ch 14 (microstrip, PIFA/IFA/slot, DRA — priority), Ch 15 (reflectors), Ch 16 (smart antennas),
Ch 17 (measurements — priority), Appendix IX (frequency allocations).

Not read here: Ch 1-8 and §9.1-9.2A (assigned to the part-1 extraction); Appendices I-VIII are mathematical
function tables/identities (Si/Ci, Fresnel, Bessel, vector identities, stationary phase) — compute with
scipy.special instead; index pages.

## 1. Design rules

### Ch 9 (tail) — Broadband dipoles, matching techniques

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BALANIS-200 | antenna | Printed bow-tie (TM10) first-cut resonant frequency uses the rectangular-patch equations with the mean width Wi; finalize by full-wave simulation (initial vs final differ because equations are approximate and ignore the balun). | f_r(TM10) = [c/(2*sqrt(eps_reff)*L)]*(1.152/R_t) ; R_t built from (W+2dL),(Wc+2dL),(S+2dL) per (9-15b) ; dL = 0.412*h*(eps_reff+0.3)*(Wi/h+0.264)/((eps_reff-0.258)*(Wi/h+0.813)) ; eps_reff = (er+1)/2 + (er-1)/2*(1+12*h/Wi)^-0.5 ; Wi = (W+Wc)/2 | W, Wc, S, L (m) per Fig 9.8(a); h (m); er | microstrip/coplanar bow-tie; eq. (9-15a)-(9-15e); OCR of (9-15a),(9-15b) is garbled — confirm exact R_t form against the printed page before automating | sim | p.494 eq.(9-15) | low |
| BALANIS-201 | antenna | The balun, not the radiator, sets the bandwidth of a balun-fed printed bow-tie: bandwidth at -15 dB return loss (VSWR<1.5) fell from 15% to 8.75% once the balun was included. | BW(-15 dB) 15% -> 8.75% with balun | S11 sweep with and without balun | flexible PEN-substrate bow-tie at 7.66 GHz | sim | p.495 | high |
| BALANIS-202 | matching | Microstrip-to-coplanar-strip balun: make the two microstrip branch lengths differ by one quarter guided wavelength at center frequency (180 deg phase difference); tune the coplanar-strip gap to optimize balun performance. | dL_branch = lambda_g/4 @ f0 | lambda_g at f0 (m) | printed dipole / bow-tie baluns | sim | p.495 | high |
| BALANIS-203 | antenna | A dipole printed over a ground plane behaves as a 2-element Yagi (ground plane = reflector); expect back lobes ~10 dB below the forward lobe. | front/back ~ 10 dB | pattern | bow-tie with ground plane, 7.66 GHz | measure | p.495 | medium |
| BALANIS-204 | antenna | Removing the low-current center of a bow-tie (outline bow-tie) lowers the resonance (electrically larger): 7.4 GHz vs 7.66 GHz for the solid version. | f_r(outline) < f_r(solid) (7.4 vs 7.66 GHz) | geometry | flexible bow-tie example | sim | p.496 | high |
| BALANIS-205 | antenna | Vivaldi (tapered-slot) antenna performance anchors: gains up to 17 dB as length L grows; Gibson's single element covered <2 GHz to >40 GHz with 10 dB gain and -20 dB side lobes; bandwidth up to 6:1, even 10:1 or greater for VSWR<2 (S11<-10 dB). | G <= 17 dB; BW up to 6:1 (10:1 @ VSWR<2) | L, Wmin, Wmax, p | end-fire traveling-wave slot on substrate | sim | p.497 | high |
| BALANIS-206 | antenna | Vivaldi arrays: main lobe ~ cos(theta) and is maintained for scan angles up to about 50-60 deg. | scan <= 50-60 deg | scan angle | Vivaldi phased arrays (AESA) | sim | p.497 | high |
| BALANIS-207 | antenna | Vivaldi exponential taper profile; larger taper rate p improves low-frequency resistance but increases R/X variation across band; increasing p widens E-plane beam, narrows H-plane beam, increases bandwidth. | y(x) = +/- A*exp(p*x), A = Wmin/2 | A (m), p (1/m), x (m) | exponential taper | sim | p.498 eq.(9-16) | high |
| BALANIS-208 | antenna | Vivaldi sizing: length L greater than one wavelength at the lowest frequency; opening width Wmin set by the highest frequency; aperture width Wmax between lambda0 (center-frequency wavelength) and lambda_min/2 (lowest-frequency wavelength). | L > lambda(f_min) ; lambda0 < Wmax < lambda_min/2 ; Example uses lambda = c/(f*sqrt(er)) | f0, f_min, er | parametric guideline [28] | calc | p.498 eq.(9-17),(9-18) | high |
| BALANIS-209 | antenna | Vivaldi feed transition: simplest broadband transition is a lambda_m/4 open microstrip stub crossing a uniform lambda_s/4 slot line (wavelengths at center frequency); CPW feed gives wider bandwidth; the microstrip-to-slot transition must not limit antenna bandwidth. | stub = lambda_m/4 ; slot = lambda_s/4 @ f0 | lambda_m, lambda_s | Knorr microstrip-to-slot transition | sim | p.497-498 | high |
| BALANIS-210 | antenna | Worked Vivaldi design (f0 = 10 GHz, er = 2.33, h = 0.508 mm, f_min = 4 GHz): Wmax range 19.65-24.57 mm, chosen Wmax = 25 mm, L = 27 mm, Wmin = 2A = 0.1 mm, p = 0.204; S11 < -10 dB from 8.6 to 23.9 GHz = 2.77:1. | Wmax1 = 3e8/(10e9*sqrt(2.33)) = 19.65 mm ; Wmax2 = 3e8/(2*4e9*sqrt(2.33)) = 24.57 mm | f0, f_min, er | Example 9.1 | sim | p.498-499 Ex.9.1, Fig 9.12 | high |
| BALANIS-211 | antenna | Thicker wire dipoles are broader-band: l/d ~ 5,000 gives ~3% acceptable bandwidth; same length with l/d ~ 260 gives ~30%. | BW ~3% @ l/d=5000 ; ~30% @ l/d=260 | l, d | cylindrical dipole | calc | p.501 §9.5.1 | high |
| BALANIS-212 | antenna | Cylindrical dipole resonant lengths and resistances (Kraus empirical, Table 9.1): 1st 0.48*lambda*F / 67 ohm; 2nd 0.96*lambda*F / Rn^2/67; 3rd 1.44*lambda*F / 95 ohm; 4th 1.92*lambda*F / Rn^2/95. | F = (l/2a)/(1+l/2a) ; Rn = 150*log10(l/2a) (ohm) | l, a (wire radius) | center-fed cylindrical dipole in free space | calc | p.503 Table 9.1 | high |
| BALANIS-213 | antenna | Cylindrical stub (monopole over ground) resonances (Table 9.2): 1st 0.24*lambda*F' / 34 ohm; 2nd 0.48*lambda*F' / Rn'^2/34; 3rd 0.72*lambda*F' / 48 ohm; 4th 0.96*lambda*F' / Rn'^2/48. | F' = (l/a)/(1+l/a) ; Rn' = 75*log10(l/a) (ohm) | l, a | monopole on ground plane | calc | p.503 Table 9.2 | high |
| BALANIS-214 | antenna | To cancel dipole reactance make l slightly LESS than n*lambda/2 (n odd) or slightly GREATER than n*lambda (n = 1,2,...); the length change grows with wire radius. | l_res < n*lambda/2 (n odd) ; l_res > n*lambda | l, a, lambda | linear dipole | calc | p.503 §9.5.3 | high |
| BALANIS-215 | antenna | Ground-plane simulation for monopoles: usually two crossed wires (four radials); more radials simulate better; wire-mesh ground planes use wire spacing <= lambda/10; radial wires ~lambda/4 or longer. | mesh spacing <= lambda/10 ; radial length >= ~lambda/4 | lambda | VHF/UHF monopoles, discones | inspect | p.503, p.513 | high |
| BALANIS-216 | antenna | Dipole input impedance vs thickness (9-19): l = lambda/2: 73+j42.5 (l/d=1e4), 85.8+j54.9 (l/d=50), 88.4+j27.5 (l/d=25); l = 3*lambda/2: 105.49+j45.54, 103.3+j9.2, 106.8+j4.9. | tabulated | l/d | Moment-method values; sinusoidal current for l/d=1e4 | sim | p.504 eq.(9-19) | high |
| BALANIS-217 | antenna | Pattern of a thick dipole is essentially that of the ideal sinusoidal-current dipole in regions of strong radiation; thickness mainly fills nulls and lowers minor lobes. | n/a | l/d | first-order pattern estimate | sim | p.503-504 | medium |
| BALANIS-218 | antenna | Non-circular conductors: replace by equivalent circular radius ae (Table 9.3): thin flat strip of width a: ae = 0.25a; rectangle a x b: ae ~ 0.2(a+b); square of side a: ae = 0.59a; ellipse semi-axes a,b: ae = (a+b)/2; two conductors: ln(ae) ~ [S1^2 ln a1 + S2^2 ln a2 + 2 S1 S2 ln s]/(S1+S2)^2. | see formula | a, b, S1, S2 (peripheries), s (spacing) | electrically small cross-section; shape labels from figure (missing in text) | calc | p.506 Table 9.3 | medium |
| BALANIS-219 | antenna | Single-wire element length for good pattern and 50/75-ohm matching: lambda/4 <= l < lambda; half-wave dipole Zin ~ 73 + j42.5 ohm, D0 ~ 1.643. | lambda/4 <= l < lambda | l | linear dipoles | calc | p.505 | high |
| BALANIS-220 | antenna | Folded dipole: spacing s < 0.05*lambda (s << lambda); at l = lambda/2 it steps the single-dipole impedance up by 4 (~300 ohm, matches 300-ohm twin-lead). | Zin = 4*Zd (l = lambda/2) | Zd (ohm), s | two equal-radius wires | calc | p.506-509 eq.(9-27),(9-30) | high |
| BALANIS-221 | antenna | Folded dipole general input impedance from transmission-line + antenna mode decomposition. | Zin = 4*Zt*Zd/(2*Zd + Zt) ; Zt = j*Z0*tan(k*l/2) | Z0 two-wire line (ohm), Zd dipole impedance using ae, k = 2*pi/lambda, l | s << lambda | calc | p.507-508 eq.(9-20),(9-26) | high |
| BALANIS-222 | transmission-line | Two-wire line characteristic impedance. | Z0 = (eta/pi)*acosh(s/(2a)) ~ (eta/pi)*ln(s/a) = 0.733*eta*log10(s/a) for s/2 >> a ; eta = 120*pi ohm in air | s center spacing (m), a wire radius (m) | folded dipole / twin-lead | calc | p.507 eq.(9-21),(9-21a) | high |
| BALANIS-223 | antenna | Use the equivalent radius ae = sqrt(a*s) for the antenna-mode dipole of a folded dipole (more accurate than a or s/2, essential at larger spacing). | ae = sqrt(a*s) | a, s | equal-radius two-wire folded dipole | calc | p.508 eq.(9-24a) | high |
| BALANIS-224 | antenna | N-element folded dipole with equal radii and close spacing: Zin ~ N^2 * Zr; 3 elements at l ~ lambda/2 give ~9x (~650 ohm). | Zin ~ N^2*Zr | N, Zr | s << lambda, equal diameters | calc | p.510 eq.(9-33a) | high |
| BALANIS-225 | antenna | Transmission-line model of folded dipole agrees with MoM for d = 0.001*lambda, s = 0.00613*lambda (Z0 = 300 ohm); accuracy degrades for s = 0.0213*lambda (450 ohm) and s = 0.0742*lambda (600 ohm) unless wires are thicker. | Z0 = 300/450/600 ohm at s = 0.00613/0.0213/0.0742 lambda (d = 0.001 lambda) | s, d | model validity | sim | p.510 | high |
| BALANIS-226 | antenna | Folded-dipole bandwidth equals that of a single dipole with an equivalent radius a < ae < s/2; its impedance changes when used in an array or with a reflector (e.g. Yagi feed). | a < ae < s/2 | a, s | folded dipole | review | p.511 | medium |
| BALANIS-227 | antenna | Discone/conical skirt monopole: vertical polarization, omni azimuth, high-pass behavior; at cutoff the cone slant height ~ lambda/4; inefficient below cutoff with severe feed-line standing waves. | slant height ~ lambda(f_cutoff)/4 | f_cutoff | VHF (30-300 MHz)/UHF (300 MHz-3 GHz) | calc | p.512 | high |
| BALANIS-228 | antenna | Discone reference designs (Table 9.4): 90 MHz: A = 45.72, B = 60.96, C = 50.80 cm; 200 MHz: A = 22.86, B = 31.75, C = 35.56 cm; a 200-MHz-cutoff discone kept its figure-eight elevation pattern 250-650 MHz. | tabulated | f | Kandoian [33]; dimension letters per Fig 9.24 | inspect | p.513 Table 9.4 | high |
| BALANIS-229 | matching | Stub matching: a single variable-length stub cannot match all loads; double stub matches more; triple stub always matches all loads; prefer short-circuited stubs; higher-order stubs are broader and less frequency sensitive but more complex (usual compromise: double stub). | n/a | Z_L | shunt stub matching | review | p.513-514 | high |
| BALANIS-230 | matching | Single-section quarter-wave transformer: if the antenna impedance is complex, insert line length s0 so the impedance becomes real (Rin), then Z1 = sqrt(Rin*Z0); best realized in microstrip (change strip width). | Z1 = sqrt(Rin*Z0) (ohm) | Rin, Z0 | narrowband match at f0 | calc | p.515 | high |
| BALANIS-231 | matching | Multi-section quarter-wave transformer small-reflection model: junction reflection coefficients rho_n = (Z_{n+1}-Z_n)/(Z_{n+1}+Z_n); theta = (pi/2)*(f/f0); valid when rho_n small (RL ~ Z0); use -rho_n if RL < Z0. | Gamma_in(f) ~ sum_{n=0..N} rho_n*exp(-j*2*n*theta) | Zn, f, f0 | real load | calc | p.515 eq.(9-34) | high |
| BALANIS-232 | matching | Binomial (maximally flat) N-section transformer design. | rho_n = 2^-N*(RL-Z0)/(RL+Z0)*C(N,n) ; C(N,n) = N!/((N-n)!n!) ; abs(Gamma_in) = abs((RL-Z0)/(RL+Z0))*abs(cos(theta))^N | RL, Z0, N | ripple-free passband | calc | p.516 eq.(9-36),(9-37) | high |
| BALANIS-233 | matching | Binomial transformer fractional bandwidth for a maximum tolerable reflection coefficient rho_m. | df/f0 = 2 - (4/pi)*acos[(rho_m/abs((RL-Z0)/(RL+Z0)))^(1/N)] | rho_m, RL, Z0, N | binomial design | calc | p.516 eq.(9-40) | high |
| BALANIS-234 | matching | Worked binomial example: 70+j37 ohm dipole on 50-ohm line; 50-ohm line length s0 = 0.062*lambda gives Rin = 100 ohm; N = 2 binomial: Z1 = 59.09 ohm, Z2 = 82.73 ohm; for df/f0 = 0.375 (theta_m = 1.276 rad = 73.12 deg): rho_m = 0.028, VSWR_m = 1.058; N = 2 Chebyshev gives rho_m = 0.0147. | as stated | - | Example 9.2 | calc | p.517-518 Ex.9.2, Fig 9.26 | high |
| BALANIS-235 | transmission-line | Microstrip characteristic impedance (Liao) for sizing transformer sections: vary strip width w at fixed er, h, t. | Zc = 87/sqrt(er+1.41)*ln(5.98*h/(0.8*w+t)) (ohm), for h < 0.8*w | er, h, w, t (same length unit) | quasi-static approximation | calc | p.518 eq.(9-41) | high |
| BALANIS-236 | matching | Chebyshev (equal-ripple) N-section transformer design equations. | rho_m = abs((RL-Z0)/(RL+Z0))/T_N(sec(theta_m)) ; sec(theta_m) = cosh[(1/N)*acosh(abs((RL-Z0)/(RL+Z0))/rho_m)] ; df/f0 = 2 - 4*theta_m/pi ; abs(Gamma_in) = rho_m*abs(T_N(sec(theta_m)*cos(theta))) | RL, Z0, N, rho_m | physical only if rho_m < abs((RL-Z0)/(RL+Z0)) | calc | p.518-520 eq.(9-42)-(9-47a) | high |
| BALANIS-237 | matching | Chebyshev vs binomial: for the same rho_m, the N-section Chebyshev gives larger bandwidth (or smaller rho_m for the same bandwidth); even N -> abs(Gamma) = rho_m at f0, odd N -> zero at f0; binomial abs(Gamma) decreases monotonically toward f0; more sections -> more bandwidth. | n/a | N | quarter-wave transformers | calc | p.520-521 | high |
| BALANIS-238 | matching | Balun options: bazooka (lambda/4 sleeve shorted at one end) chokes shield current; parallel lambda/4 auxiliary line cancels it; lambda/4 coaxial 4:1 balun needs a U-section lambda/2 long; all of these are narrowband. | sleeve = lambda/4 ; U-section = lambda/2 | lambda | coax-fed balanced antennas | inspect | p.521-522 | high |
| BALANIS-239 | matching | Ferrite-core baluns/transformers (1:1 or 4:1) give 8:1 or even 10:1 bandwidth with good design; coiled-coax baluns give 2:1 or 3:1. | BW 8-10:1 (ferrite) ; 2-3:1 (coiled coax) | - | broadband balun selection | review | p.523 | high |

### Ch 10 — Traveling-wave and broadband antennas

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BALANIS-240 | antenna | Classify traveling-wave structures by phase velocity: slow wave vp/c <= 1 (surface-wave antennas; radiate only at discontinuities/curvature, mostly end-fire); fast wave vp/c > 1 (most leaky-wave antennas). | vp = omega/k ; slow: vp/c <= 1 ; fast: vp/c > 1 | omega, k | traveling-wave antennas | review | p.534-535 | high |
| BALANIS-241 | antenna | Long-wire (traveling-wave, matched) lobe maxima and nulls; include the cot^2 envelope by using 2m+1 = 0.742, 2.93, 4.96, 6.97, 8.99, 11, 13 instead of 1,3,5,... | theta_m = acos[1 - lambda*(2m+1)/(2l)] ; theta_n = acos(1 - n*lambda/l), n = 1,2,... | l (m), lambda (m) | K = kz/k = 1 (vp = c); l from one to many wavelengths | calc | p.537-538 eq.(10-7),(10-8),(10-10) | high |
| BALANIS-242 | antenna | Radiation resistance of a matched long wire (traveling wave, K = 1). | Rr = (eta/(2*pi))*[1.415 + ln(k*l/pi) - Ci(2kl) + sin(2kl)/(2kl)] (ohm), eta/(2*pi) = 60 ohm | l, k = 2*pi/lambda | free space | calc | p.538 eq.(10-12) | high |
| BALANIS-243 | antenna | Directivity of a matched long wire. | D0 = 2*cot^2[0.5*acos(1 - 0.371*lambda/l)] / [1.415 + ln(2l/lambda) - Ci(2kl) + sin(2kl)/(2kl)] | l, lambda | l >> lambda | calc | p.538 eq.(10-13) | high |
| BALANIS-244 | antenna | Beverage (long wire over ground) matched termination resistor ~ characteristic impedance of wire over ground; adjust about this value (usually ~200-300 ohm) until no standing wave. | RL = 138*log10(4h/d) (ohm) | h height above ground, d wire diameter (same units) | h small vs lambda; mainly receiving (load absorbs power) | measure | p.541-542 eq.(10-14) | high |
| BALANIS-245 | antenna | Resonant long wire of odd half-wave multiples: radiation resistance, beam angle and directivity (Rr within 0.5 ohm; D0 within 0.5 dB of exact). | Rr = 73 + 69*log10(n) (ohm) ; theta_max = acos((n-1)/n) ; D0 = 120/(Rr*sin^2(theta_max)) | n (odd, l = n*lambda/2) | MF (300 kHz-3 MHz) / HF (3-30 MHz) wires | calc | p.542-543 eq.(10-16)-(10-18) | high |
| BALANIS-246 | antenna | Linear-dipole directivity begins to fall for lengths above ~1.25*lambda (sidelobes grow); use a V to recover directivity. | l_dipole <= ~1.25*lambda | l | center-fed dipoles | calc | p.543 | high |
| BALANIS-247 | antenna | V antenna: unterminated legs longer than ~5*lambda leak enough that termination is not needed; for one main lobe choose half-angle theta0 ~ 0.8*theta_m (theta_m = cone angle of one leg's maximum); then D(V) ~ 2*D(one leg). | l > 5*lambda (no termination) ; theta0 ~ 0.8*theta_m | l, theta_m | long-wire V antennas | calc | p.543-545 | high |
| BALANIS-248 | antenna | Optimum V-dipole included angle and directivity (Thiele & Ekelman polynomial fits to MoM data). | 2*theta0 (deg) = -149.3x^3 + 603.4x^2 - 809.5x + 443.6 for 0.5 <= x <= 1.5 ; 2*theta0 = 13.39x^2 - 78.27x + 169.77 for 1.5 <= x <= 3 ; D0 = 2.94x + 1.15 for 0.5 <= x <= 3 ; x = l/lambda (arm length) | l/lambda | symmetrical V dipole; V input impedance slightly smaller than straight dipole | calc | p.545 eq.(10-19a),(10-19b),(10-20) | high |
| BALANIS-249 | antenna | Bent monopole V over ground: included angle > 120 deg -> essentially vertical polarization, straight-dipole patterns; < ~120 deg adds horizontal component filling toward horizon (aircraft use). 90-deg bent wire: omni in its plane for h1 <= 0.1*lambda; for h1 > 0.1*lambda approaches vertical lambda/2 dipole. | 2*theta0 > 120 deg ; h1 <= 0.1*lambda | angle, h1 | wire antennas over ground plane | sim | p.546-547 | high |
| BALANIS-250 | antenna | Rhombic antenna: terminate one end with ~600-800 ohm (legs > ~5*lambda may not need it); design height, leg length and half-angle for a beam at elevation angle psi0. | h_m/lambda0 = m/(4*cos(90deg - psi0)), m = 1,3,5,... (m = 1 minimum) ; l/lambda0 = 0.371/(1 - sin(90deg - psi0)*cos(phi0)) ; phi0 = acos[sin(90deg - psi0)] | psi0 (beam elevation), lambda0 | rhombus parallel to PEC ground | calc | p.548-549 eq.(10-21)-(10-23) | high |
| BALANIS-251 | antenna | Helix geometry: pitch angle, turn length and total lengths. alpha = 0 -> loop; alpha = 90 deg -> straight wire. | alpha = atan(S/(pi*D)) = atan(S/C) ; L0 = sqrt(S^2 + C^2) ; L = N*S ; Ln = N*L0 | S spacing, D diameter, C = pi*D, N turns | helical antennas | calc | p.549 eq.(10-24) | high |
| BALANIS-252 | antenna | Helix ground plane: flat ground plane diameter at least 3*lambda/4 (general statement); for axial mode ground plane diameter at least lambda0/2; cupped (cavity) ground planes also used. | D_gp >= 3*lambda/4 (general) ; >= lambda0/2 (axial mode) | lambda | coax-fed helix | inspect | p.549, p.553 | high |
| BALANIS-253 | antenna | Normal-mode helix axial ratio; circular polarization when C = sqrt(2*S*lambda0); normal mode needs N*L0 << lambda0, is very narrowband and inefficient (seldom used). | AR = abs(Etheta)/abs(Ephi) = 4S/(pi*k*D^2) = 2*lambda*S/(pi*D)^2 ; CP: C = pi*D = sqrt(2*S*lambda0), tan(alpha) = pi*D/(2*lambda0) | S, D, lambda0 | Ln << lambda0 | calc | p.552-553 eq.(10-27)-(10-29) | high |
| BALANIS-254 | antenna | Axial-mode (end-fire) helix validity window: 3/4 < C/lambda0 < 4/3 (C/lambda0 = 1 near optimum), S ~ lambda0/4, pitch 12 <= alpha <= 14 deg, N > 3; CP bandwidth usually 2:1. | 0.75 < C/lambda0 < 1.333 ; 12 deg < alpha < 14 deg ; N > 3 | C, S, alpha, N | Kraus empirical formulas | calc | p.550, p.553-554 | high |
| BALANIS-255 | antenna | Axial-mode helix input resistance (+/-20%), beamwidths, directivity and axial ratio (Kraus empirical). | R ~ 140*(C/lambda0) ohm ; HPBW(deg) ~ 52*lambda0^1.5/(C*sqrt(N*S)) ; FNBW(deg) ~ 115*lambda0^1.5/(C*sqrt(N*S)) ; D0 ~ 15*N*C^2*S/lambda0^3 ; AR = (2N+1)/(2N) | C, S, N, lambda0 | 12-14 deg pitch, 3/4 < C/lambda0 < 4/3, N > 3 | calc | p.554 eq.(10-30)-(10-34) | high |
| BALANIS-256 | antenna | Relative wave velocity on helix wire for ordinary end-fire and Hansen-Woodyard end-fire phasing. | p_ord = (L0/lambda0)/(S/lambda0 + 1) ; p_HW = (L0/lambda0)/(S/lambda0 + (2N+1)/(2N)) | L0, S, N, lambda0 | axial mode | calc | p.554-556 eq.(10-35b),(10-35c) | high |
| BALANIS-257 | antenna | Worked axial helix (N = 10, C = lambda0, alpha = 13 deg): S = 0.231*lambda0, L0 = 1.0263*lambda0, p_ord = 0.8337, p_HW = 0.8012, HPBW = 34.2 deg, D0(formula) = 34.65 (15.397 dB); numerical D0 = 12.678 (11.03 dB) ordinary and 26.36 (14.21 dB) Hansen-Woodyard; AR = 1.05 (0.21 dB). | as stated | - | Example 10.1 — Kraus D0 formula overestimates ordinary end-fire | calc | p.556-558 Ex.10.1 | high |
| BALANIS-258 | matching | Axial-mode helix nominal impedance is 100-200 ohm; to reach 50 ohm flatten the first 1/4 turn into a strip of width w over a dielectric-covered ground plane and transition to round wire and design pitch within the first 1/4-1/2 turn. | h = w/(377/(sqrt(er)*Z0) - 2) | w strip width, er slab dielectric constant, Z0 line impedance | Kraus 50-ohm helix feed | calc | p.558 eq.(10-41) | high |
| BALANIS-259 | antenna | Lower-impedance helix feeds trade bandwidth: 50-ohm helix VSWR < 2 over 40% vs 70% for a 140-ohm helix; VSWR < 1.2 over 12% vs 20%. Example: 70-mm strip bonded near the feed of a 13-mm wire helix gave 50 ohm at 230.77 MHz. | BW(VSWR<2): 40% (50 ohm) vs 70% (140 ohm) ; BW(VSWR<1.2): 12% vs 20% | Z0 target | axial-mode helix | measure | p.558 | high |
| BALANIS-260 | antenna | Commercial cupped-ground helix reference: RHCP 100-160 MHz, gain ~6 dB @100 MHz to 12.8 dB @160 MHz, AR ~8 dB @100 MHz to 2 dB @160 MHz, VSWR <= 3:1 (50 ohm). | as stated | - | Seavey helix, Fig 10.17 | measure | p.558-559 | high |
| BALANIS-261 | antenna | Electric-magnetic dipole (loop + dipole, power split for equal fields) gives near-CP; experimental model VSWR < 2:1 over 1.15-1.32 GHz; useful against polarization-dependent fading. | VSWR < 2 over 1.15-1.32 GHz | - | Kandoian | measure | p.559 | high |
| BALANIS-262 | antenna | Yagi-Uda dimensions: driven element 0.45-0.49*lambda (resonant, slightly < lambda/2); directors 0.4-0.45*lambda; director spacing 0.3-0.4*lambda (not necessarily uniform); reflector longer than feed; reflector-feed spacing ~0.25*lambda (smaller than feed-first-director spacing). | l_drive = 0.45-0.49 lambda ; l_dir = 0.40-0.45 lambda ; s_dir = 0.3-0.4 lambda ; s_ref ~ 0.25 lambda | lambda | HF/VHF/UHF Yagi | calc | p.561 | high |
| BALANIS-263 | antenna | For a 6*lambda Yagi, gain is independent of director spacing up to ~0.3*lambda and drops 5-7 dB for larger spacings; gain independent of director radius up to ~0.024*lambda. | s_dir <= 0.3 lambda ; a_dir <= 0.024 lambda | s, a | 6-lambda-long Yagi (experimental) | measure | p.561 | high |
| BALANIS-264 | antenna | Use 1 (at most 2) reflectors; typical 6-12 directors (30-40 elements built); typical array length ~6*lambda; gain ~5-9 per wavelength of length -> overall 30-54 (14.8-17.3 dB). | G ~ (5..9)*L/lambda | L/lambda | Yagi-Uda | calc | p.562 | high |
| BALANIS-265 | antenna | Yagi input impedance is low and bandwidth narrow (~2%); front-to-back ~30 (~15 dB) achievable at wider-than-optimum spacing; use a folded-dipole feed (~4:1 step-up) to raise impedance without hurting other parameters. | BW ~ 2% ; F/B ~ 15 dB | - | Yagi-Uda | measure | p.562 | high |
| BALANIS-266 | antenna | Yagi sensitivity: reflector spacing/size -> negligible effect on forward gain, large effect on back lobe and Zin; feeder length/radius -> small effect on forward gain, large on back lobe and Zin (set for real Zin); director size/spacing -> large effect on forward gain, back lobe and Zin (most critical). Use an odd number of rows for stacked (curtain) Yagis. | n/a | - | design/tuning priority | review | p.562 | high |
| BALANIS-267 | antenna | 15-element Yagi reference (reflector 0.5*lambda, feeder 0.47*lambda, 13 directors 0.406*lambda, s_ref = 0.25*lambda, s_dir = 0.34*lambda, a = 0.003*lambda): HPBW_E = 26.98 deg, HPBW_H = 27.96 deg, D = 14.64 dB. Max F/B at reflector spacing ~0.23*lambda; D falls from ~15.2 dB (s_ref = 0.1*lambda) to ~10.4 dB (0.5*lambda). | as stated | - | Example 10.2 (MoM) | sim | p.569-570 Ex.10.2, Fig 10.23 | high |
| BALANIS-268 | antenna | Director spacing: directivity rises from ~12 dB (0.1*lambda) to ~15.3 dB (~0.45*lambda) then drops steeply; large directivity reductions for spacing > ~0.4*lambda; F/B swings 20-25 dB for ~0.05*lambda spacing changes in long Yagis. | s_dir <= ~0.4 lambda | s_dir | 15-element example; more pronounced for more elements | sim | p.570-571 Fig 10.24 | high |
| BALANIS-269 | antenna | Optimized Yagi bandwidth: directivity drops rapidly above f0 but stays nearly constant below; make dimensions slightly smaller than optimum to increase bandwidth (design at the top of the band). | design at f_high | f0 | six-element optimized array | sim | p.572 Fig 10.26 | high |
| BALANIS-270 | matching | Yagi input impedance vs reflector spacing (15-element, reflector 0.5*lambda, directors 0.406*lambda at 0.34*lambda): 0.25 -> 62 ohm; 0.18 -> 50; 0.15 -> 32; 0.13 -> 22; 0.10 -> 12 ohm. Typical 30-70 ohm: use Gamma match to ~78-ohm coax, folded-dipole (4:1) to 300-ohm twin-lead. | Table 10.5 | s21/lambda | resonant driven element | calc | p.572, p.575 Table 10.5 | high |
| BALANIS-271 | antenna | For maximum directivity with equal currents the total element-to-element phase delay along the Yagi should be ~180 deg (Hansen-Woodyard); Yagi phase velocity is between c and the H-W value and decreases as array length grows. | total phase ~ 180 deg | - | end-fire criterion | sim | p.575 | medium |
| BALANIS-272 | antenna | NBS (Viezbicke) Yagi design tables: overall lengths 0.4, 0.8, 1.2, 2.2, 3.2, 4.2*lambda give 7.1, 9.2, 10.2, 12.25, 13.4, 14.2 dB over a lambda/2 dipole; valid 0.001 <= d/lambda <= 0.04; reflector spacing 0.2*lambda in all designs; folded-dipole driver; measured at 400 MHz. | Table 10.6 | L/lambda, d/lambda | one reflector; uniform director spacing | calc | p.576 Table 10.6 | high |
| BALANIS-273 | antenna | Metal boom compensation: lengthen every parasitic element per Fig 10.28 (0.001 <= D/lambda <= 0.04); e.g. D/lambda = 0.00852 needs +0.005*lambda. Example (50.1 MHz, 9.2 dB, d = 2.54 cm, D = 5.1 cm): l3 = l5 = 0.447*lambda, l4 = 0.443*lambda, l1 = 0.490*lambda, spacing 0.2*lambda, length 0.8*lambda. | dl = f(D/lambda) (graph) | D/lambda, d/lambda | NBS data on Plexiglas boom 3*lambda above ground | calc | p.576-578 Ex.10.3, Fig 10.27, 10.28 | medium |
| BALANIS-274 | antenna | Do not use wooden booms for Yagi reference builds (moisture changes gain); nonconducting (Plexiglas) booms behave as air; metal booms are repeatable only with element-length compensation. | n/a | boom material | NBS measurements | inspect | p.578 | high |
| BALANIS-275 | antenna | Commercial VHF TV Yagi (ch 2-13): gain over dipole 4.4 dB (ch 2) to 7.3 dB (ch 13), 300 ohm. | as stated | - | Winegard example | measure | p.579 | high |
| BALANIS-276 | antenna | Loop Yagi optimum (2-10 directors): feeder circumference ~1.1*lambda, reflector ~1.05*lambda, feeder-reflector spacing ~0.1*lambda, director circumference ~0.7*lambda, director spacing ~0.25*lambda, wire radius from Omega = 2*ln(2*pi*b2/a) = 11. Two-element loop array has 1.8 dB more gain than two dipoles; quad sides lambda/4 (perimeter lambda). | C_feed ~1.1 lambda ; C_ref ~1.05 lambda ; C_dir ~0.7 lambda ; s_ref ~0.1 lambda ; s_dir ~0.25 lambda | lambda | coaxial Yagi of circular loops | calc | p.579-580 | high |

### Ch 11 — Frequency-independent antennas, small-antenna limits, miniaturization, fractals

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BALANIS-280 | antenna | Frequency-independent (angle-specified, current-decaying) antennas: practical bandwidths ~40:1 (1000:1 possible but unnecessary); lower cutoff where current at truncation is negligible; upper cutoff where the feed region stops looking like a point, ~lambda2/8 (lambda2 = wavelength at highest frequency). | BW ~ 40:1 ; feed size <= lambda_high/8 | f_low, f_high, feed size | spirals, log-periodics; 10-10,000 MHz typical | calc | p.591-592 | high |
| BALANIS-281 | antenna | Scale-model invariance: impedance, pattern and polarization are unchanged if all dimensions are scaled by 1/K and frequency by K (electrical size constant). | f_model = K*f ; dims_model = dims/K | K | scale-model measurements (see §17.10) | calc | p.591 | high |
| BALANIS-282 | antenna | Equiangular (log) spiral arm length. | L = (rho1 - rho0)*sqrt(1 + 1/a^2) | rho0 inner radius, rho1 outer radius, 1/a expansion rate | planar equiangular spiral | calc | p.595 eq.(11-14) | high |
| BALANIS-283 | antenna | Self-complementary planar structure (spiral with delta = pi/2) ideally has Zin = eta/2 = 188.5 ~ 60*pi ohm (infinite structure); measured spiral mean input impedance only ~164 ohm (finite arms, plate thickness, feed). | Zs = Zc = 188.5 ohm (ideal) ; ~164 ohm measured | - | Babinet self-complementary | measure | p.596-597 | high |
| BALANIS-284 | antenna | Spiral slot design: 1/2 to 3 turns usable; optimum 1.25-1.5 turns with total arm length >= one wavelength; expansion rate <= ~10 per turn; lower cutoff chosen where on-axis axial ratio <= 2:1, typically at arm length ~ one wavelength; beamwidth varies ~10 deg with frequency (pattern rotates). | turns 1.25-1.5 ; L_arm >= lambda_low ; expansion <= 10/turn ; AR <= 2 at f_low | turns, L_arm, a | planar spiral slot, bidirectional broadside, CP on axis | calc | p.597 | high |
| BALANIS-285 | antenna | Spiral feed must be electrically and geometrically balanced: embed coax in one arm with a dummy cable in the other; an unbalanced feed needs a balun, which limits bandwidth; feed construction precision directly sets the high-frequency limit. | n/a | feed | spiral antennas | inspect | p.597 | high |
| BALANIS-286 | antenna | Measured spiral slot 700-2,500 MHz: Zin ~75-100 ohm, VSWR < 2 on 50-ohm line; free-space (no cavity/dielectric) spiral slot efficiency ~98% for arm length >= 1 wavelength, dropping rapidly for shorter arms. | Zin 75-100 ohm ; eta ~98% @ L_arm >= lambda | L_arm | Dyson spiral | measure | p.598 | high |
| BALANIS-287 | antenna | Conical spiral: unidirectional beam toward apex, CP, near-constant impedance over large bandwidth; flush mounting on a ground plane reduces bandwidth. | n/a | theta0 (cone half-angle) | conical equiangular spiral | review | p.598 | high |
| BALANIS-288 | antenna | Log-periodic period definitions; one operating period spans f1 to f2 = f1/tau; impedance (not pattern) sometimes repeats at half this period. | tau = R_n/R_{n+1} = f1/f2 (f2 > f1) ; eps = r_n/R_{n+1} ; Delta = ln(f2) - ln(f1) = ln(1/tau) | R_n, r_n | log-periodic structures (linearly polarized) | calc | p.602, p.605 eq.(11-23)-(11-27) | high |
| BALANIS-289 | antenna | LPDA scaling and spacing factor: all lengths, spacings, diameters and gaps scale by 1/tau per element; spacing factor sigma; apex half-angle alpha. | 1/tau = l_{n+1}/l_n = R_{n+1}/R_n = d_{n+1}/d_n = s_{n+1}/s_n ; sigma = (R_{n+1}-R_n)/(2*l_{n+1}) ; alpha = atan[(1-tau)/(4*sigma)] | tau, sigma | Isbell/Carrel LPDA | calc | p.602-603, p.608 eq.(11-26),(11-26a),(11-28) | high |
| BALANIS-290 | antenna | LPDA directivity is 7-12 dB (slightly below Yagi) but held over wide bandwidth; typical designs 10 <= alpha <= 45 deg and 0.7 <= tau <= 0.95; larger tau / smaller alpha -> more elements, smoother impedance, higher gain. | D = 7-12 dB ; alpha 10-45 deg ; tau 0.7-0.95 | tau, alpha | LPDA | calc | p.602, p.605-607 | high |
| BALANIS-291 | antenna | LPDA feed must be transposed (crisscross) between adjacent elements so the beam fires toward the short end; coax routed inside one feeder boom (center conductor to the other boom) gives a built-in broadband balun; feed at the short end. | n/a | feed topology | LPDA | inspect | p.604 | high |
| BALANIS-292 | antenna | LPDA cutoffs: lower cutoff ~ where longest element = lambda/2; upper cutoff lies beyond where shortest element = lambda/2 because the active region spans several elements; active region ~4-5 elements; transmission-region phase velocity ~0.6*c. | l_max = lambda_max/2 ; active region 4-5 elements ; vp ~ 0.6*v0 | tau, sigma | example tau = 0.95, sigma = 0.0564, N = 13, l/d = 177 | calc | p.604-605 | high |
| BALANIS-293 | antenna | LPDA phase center moves with frequency (active region migrates), so LPDAs are poor reflector feeds. | n/a | - | reflector feed selection | review | p.604 | high |
| BALANIS-294 | antenna | Carrel LPDA design equations: active-region bandwidth, designed bandwidth, boom length, element count, mean element impedance, feeder spacing. | B_ar = 1.1 + 7.7*(1-tau)^2*cot(alpha) ; Bs = B*B_ar ; L = (lambda_max/4)*(1 - 1/Bs)*cot(alpha) ; lambda_max = 2*l_max = v/f_min ; N = 1 + ln(Bs)/ln(1/tau) ; Za = 120*[ln(l_n/d_n) - 2.25] (ohm) ; sigma' = sigma/sqrt(tau) ; s = d*cosh(Z0/120) | B = f_max/f_min, tau, sigma, l/d, Rin, Z0 from Fig 11.14 | use 1-3 diameter groups (three typical) | calc | p.609-610 eq.(11-29)-(11-34) | high |
| BALANIS-295 | antenna | Carrel directivity contours (Fig 11.13) as originally published are 1-2 dB optimistic; use curves reduced by ~1 dB (Butson & Thompson correction). | D_true ~ D_Carrel(original) - 1 dB | tau, sigma | LPDA directivity estimate | review | p.609 Fig 11.13 | high |
| BALANIS-296 | antenna | LPDA worked design (54-216 MHz, D0 = 8 dB, Rin = 50 ohm): sigma = 0.157, tau = 0.865, alpha = 12.13 deg, B_ar = 1.753, Bs = 7.01, lambda_max = 5.556 m, L = 5.541 m, N = 14.43 (14 or 15), sigma' = 0.169, l_max/d_max = 145.816, Za = 327.88 ohm, Za/Rin = 6.558, Z0 ~ 1.2*Rin = 60 ohm, s = 0.846 in (d = 3/4 in). | as stated | - | Example 11.1 (elements 3/4 in largest, 3/16 in smallest; equal l/d) | calc | p.611-612 Ex.11.1 | high |
| BALANIS-297 | antenna | Commercial LPDA references: 21-element, 100-1,100 MHz, ~6 dBi, VSWR <= 2:1 (50 ohm), F/B ~20 dB, HPBW E ~75 deg / H ~120 deg; cavity-backed LP slot: VSWR 2:1, 70 deg E/H beamwidths, cavity 6.1 cm dia x 4.445 cm deep, 0.14 kg. | as stated | - | catalog data | measure | p.602, p.613 | high |
| BALANIS-298 | antenna | LPDA termination: add a terminating transmission line and load beyond the longest element to absorb energy passing the active region; otherwise it reflects back into the active region and degrades the pattern. | n/a | Z_term | LPDA feeder | sim | p.614 | high |
| BALANIS-299 | antenna | Chu-McLean fundamental limit on radiation Q of an antenna enclosed in a sphere of radius a (lowest TM10 mode); halve Q if both TE and TM modes are excited equally; independent of shape; approached but never reached in practice. | Q = [1 + 2(ka)^2]/{(ka)^3*[1+(ka)^2]} ~ 1/(ka)^3 ; or Q = 1/(ka)^3 + 1/(ka) ; k = 2*pi/lambda | a (m) radius of enclosing sphere (largest dimension = 2a), lambda | ka < 1 electrically small, 100% efficient | calc | p.616 eq.(11-35a),(11-35b) | high |
| BALANIS-300 | antenna | Fractional bandwidth from Q for a fixed-value resonant equivalent circuit; valid for Q >> 1, inaccurate for Q < 2. | FBW = df/f0 = 1/Q | Q | small antennas | calc | p.616 eq.(11-36) | high |
| BALANIS-301 | antenna | Small linear dipole impedance and Q (dipole of length l, wire radius b). | Zin ~ 20*pi^2*(l/lambda)^2 - j*120*[ln(l/2b) - 1]/tan(pi*l/lambda) (ohm) ; Q = X/R ~ 6*[ln(l/2b) - 1]/[(pi*l/lambda)^2*tan(pi*l/lambda)] | l, b, lambda | l << lambda; Q form derived as X/R from (11-37) (printed (11-38) OCR-garbled) | calc | p.617 eq.(11-37),(11-38) | medium |
| BALANIS-302 | antenna | Bandwidth of a size-limited antenna improves only by using the enclosing volume efficiently: dipole (1-D) is far above the Chu limit; Goubau and folded spherical helices approach it; lowering Q further at fixed volume costs efficiency. | n/a | geometry | small-antenna design | review | p.617-619 Fig 11.17 | high |
| BALANIS-303 | antenna | Four-arm folded spherical helix can be ka < 0.5, self-resonant, high efficiency, Q within 1.5x the fundamental limit, radiation resistance near 50 ohm at resonance; more arms (same sphere) -> lower Q. | Q <= 1.5*Q_Chu ; ka < 0.5 | turns, arms | Best 2004 | sim | p.618-619 Table 11.2 | high |
| BALANIS-304 | antenna | "Miniaturized" antenna definition: reduced in size while preserving fidelity of at least one performance characteristic, and performing better than the original antenna simply shrunk by the same factor; judge by Zin, return loss, impedance/fractional bandwidth, match, radiation efficiency, directivity, gain, realized gain, resonant Q. | n/a | - | miniaturization claims | review | p.619-620 | high |
| BALANIS-305 | antenna | Realized gain as the figure of merit for any shortened/loaded antenna. | G_re = 10*log10[e_cd*(1-abs(Gamma)^2)*D0] (dB) | e_cd, Gamma, D0 | all antennas | calc | p.621 Ex.11.2 | high |
| BALANIS-306 | antenna | Inductive (coil) loading trades length for gain: lambda0/(10*pi) monopole (a = 2.229e-4*lambda0) with Q = 300 mid-coil: Rr = 20.15 ohm, e_cd = 19.85%, S11 = -7.422 dB, G_re = -3.119 dB; lossless coil Rr = 2.37 ohm, G_re = -2.853 dB; vs lambda0/4 monopole Rr = 36.5 ohm, G_re = 4.664 dB (D0 = 3): 7.85x shorter costs ~7.5-7.8 dB. | as stated | Q_coil | Harrison monopole, 50-ohm line | calc | p.620-622 Ex.11.2 | high |
| BALANIS-307 | antenna | High-er dielectric loading shortens by sqrt(er) but can wreck efficiency: water sleeve (er = 73, tan d = 0.02) monopole 23 mm at 381 MHz: 8.544x shorter, 118x volume, Rr = 0.4 ohm, e = 12.6%, S11 = -0.139 dB, G_re = -18.85 dB (~24 dB below a lambda/4 monopole). Thinner-loading case (160 mm at 253 MHz, 1.85x shorter): e_cd = 96.6%, Rr = 8.5 ohm, G_re = 1.978 dB. | shortening = sqrt(er) | er, tan d | James & Henderson | calc | p.622-624 Ex.11.3 | high |
| BALANIS-308 | antenna | Meander-line monopole (lambda/4 monopole: 135 mm, 545 MHz, 36.5 ohm, e_cd 99.1%, FBW 9.5% at S11 = -10 dB): N = 2 meander in 2.7 x 45 mm -> 922 MHz, 1.8x shorter, 6.75x wider, Rr = 13 ohm, S11 = -4.62 dB, e = 96.7%, FBW 3%, G_re = 3.18 dB (-2 dB); N = 14 -> 1.33x shorter, e = 98%, FBW 8%, Rr = 23.5 ohm, S11 = -8.86 dB, G_re = 4.47 dB (-0.6 dB). | as stated | N folds | Rashed & Tai | measure | p.624-625 | high |
| BALANIS-309 | antenna | Rectangular meander (opposing horizontal currents) resonates higher than a helical meander of the same height/wire length (reinforcing currents): 10 cm tall, 30 cm wire, 1 mm wire, 3.3 cm diameter -> 361 MHz vs 312.6 MHz. | f_res(rect meander) > f_res(helical) | geometry | normal-mode helix vs meander | sim | p.625-626 | high |
| BALANIS-310 | antenna | Shorting pin/wall at a patch null halves the patch length (~lambda/4 instead of lambda/2); basis of PIFA/IFA. | L ~ lambda/4 (shorted) vs lambda/2 | - | microstrip miniaturization | calc | p.626 | high |
| BALANIS-311 | antenna | Fractal/space-filling elements raise small-loop resistance: circular loop ~1.33 ohm at 0.265*lambda circumference vs Koch loop of equal radius (~0.04218*lambda) ~35 ohm (both below resonance); fractal dipoles lower resonance with iteration (3-D fractal tree ~40% reduction after 5 iterations) with most benefit in the first 5 iterations; Koch dipole Q falls with iteration. | as stated | iteration count | Gianvittorio & Rahmat-Samii | sim | p.630-632 | high |

### Ch 12 — Aperture antennas

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BALANIS-320 | antenna | Aperture analysis by field equivalence: pick a closed surface where tangential fields are known (usually the infinite plane of the aperture); for an aperture in an infinite flat PEC ground plane use Ms = -2 n x Ea over the opening only (Js = 0) radiating in free space; without a ground plane approximate Js = n x Ha and Ms = -n x Ea over the opening, zero elsewhere. | Ms = -2*n x Ea (on PEC plane) | Ea over aperture | Love/image equivalents | review | p.640-645, p.660-661 | high |
| BALANIS-321 | antenna | Uniform rectangular aperture (a x b) on an infinite ground plane: H-plane pattern vanishes along the ground plane; E-plane pattern generally does not (unless b is a multiple of lambda); one E-plane sidelobe appears on each side when lambda < b <= 2*lambda; H-plane first sidelobes when lambda < a <= 2*lambda, second when 2*lambda < a <= 3*lambda. | n/a | a, b, lambda | uniform aperture | sim | p.652-654 | high |
| BALANIS-322 | antenna | Uniform-aperture principal-plane nulls and first-null beamwidth (E-plane with dimension b; H-plane approx. with a). | theta_n = asin(n*lambda/b) ; FNBW = 2*asin(lambda/b) ~ 114.6*(lambda/b) deg (b >> lambda) | b (or a), lambda | uniform distribution | calc | p.654-655 eq.(12-26a),(12-27) | high |
| BALANIS-323 | antenna | Uniform-aperture half-power beamwidth (from sin(x)/x = 0.707 at x = 1.391). | HPBW = 2*asin(0.443*lambda/b) ~ 0.886*lambda/b rad = 50.8*lambda/b deg (b >> 0.443*lambda) | b, lambda | uniform distribution | calc | p.655-656 eq.(12-28)-(12-29a) | high |
| BALANIS-324 | antenna | Uniform-aperture first sidelobe: at asin(1.43*lambda/b) (x = 4.494), level 0.217 = -13.26 dB (approximation -13.47 dB); beamwidth between first sidelobes ~163.8*lambda/b deg. | SLL = -13.26 dB ; theta_s = asin(1.43*lambda/b) | b, lambda | uniform distribution | calc | p.656 eq.(12-30)-(12-33) | high |
| BALANIS-325 | antenna | Uniform aperture directivity equals 4*pi*physical area/lambda^2 (maximum effective area = physical area). | D0 = 4*pi*a*b/lambda^2 = 4*pi*Ap/lambda^2 | a, b, lambda | uniform, large aperture (Ha = Ea/eta assumed) | calc | p.657 eq.(12-37) | high |
| BALANIS-326 | antenna | Worked uniform aperture (a = 3*lambda, b = 2*lambda): E-plane FNBW 60 deg, HPBW 25.6 deg, FSLBW 91.3 deg, SLL -13.26 dB; D0 = 75.4 (18.77 dB) by (12-37) vs 80.4 (19.05 dB) numerically (on ground plane), 81.16 (19.09 dB) without ground plane. | as stated | - | Examples 12.2-12.3 | calc | p.660-662 | high |
| BALANIS-327 | antenna | Aperture fields without an infinite ground plane equal the ground-plane result multiplied by (1 + cos(theta))/2 (z normal to aperture); main-lobe patterns and directivity nearly identical, extra minor lobes appear. | E_free = E_gp*(1 + cos th)/2 | theta | rectangular/circular apertures | calc | p.661, p.664, p.674 | high |
| BALANIS-342 | antenna | TE10 waveguide aperture on ground plane: E-plane same as uniform (50.8*lambda/b HPBW, 114.6*lambda/b FNBW, -13.26 dB); H-plane HPBW 68.8*lambda/a deg, FNBW 171.9*lambda/a deg, first sidelobe -23 dB; aperture efficiency 8/pi^2. | D0 = (8/pi^2)*(4*pi*a*b/lambda^2) = 0.81*(4*pi*a*b/lambda^2) | a, b, lambda | a >> lambda for beamwidth formulas | calc | p.659 Table 12.1, p.665 eq.(12-39c) | high |
| BALANIS-328 | antenna | Aperture efficiency definition and typical ranges: aperture antennas ~30-90%; horns 35-80% (optimum-gain horns ~50%); circular reflectors 50-80%. Reflector aperture efficiency is driven by spillover, amplitude taper, phase distribution, polarization uniformity, blockage and random surface errors. | Aem = eps_ap*Ap, 0 <= eps_ap <= 1 ; D0 = eps_ap*4*pi*Ap/lambda^2 | Ap, eps_ap | aperture antennas | calc | p.665 eq.(12-40) | high |
| BALANIS-329 | antenna | Beam efficiency (main-lobe discrimination): uniform square aperture 20 lambda x 20 lambda keeps ~94% of power within a 10-deg half-cone; a 3 lambda square (u = (ka/2) sin(theta1) = 1.64) only ~58%; uniform distribution has the poorest main-lobe/minor-lobe discrimination (Fig 12.15, graph). | BE(10 deg) ~94% (20 lambda) ; ~58% (3 lambda) | a/lambda, theta1 | apertures not on ground plane | calc | p.666-667 Ex.12.4 | medium |
| BALANIS-330 | antenna | Uniform circular aperture (radius a) on ground plane: HPBW 29.2*lambda/a deg, FNBW 69.9*lambda/a deg (both planes), first sidelobe -17.6 dB. | D0 = (2*pi*a/lambda)^2 = (C/lambda)^2 | a, lambda | a >> lambda | calc | p.671-673 eq.(12-56), Table 12.2 | high |
| BALANIS-331 | antenna | TE11 circular waveguide aperture on ground plane: HPBW E 29.2*lambda/a, H 37.0*lambda/a deg; FNBW E 69.9*lambda/a, H 98.0*lambda/a deg; first sidelobe E -17.6 dB, H -26.2 dB. | D0 = 0.836*(2*pi*a/lambda)^2 = 10.5*pi*(a/lambda)^2 | a, lambda | chi'11 = 1.841 | calc | p.673 Table 12.2 | high |
| BALANIS-332 | antenna | Aperture taper trade-off: smoother taper toward the edge -> lower sidelobes and wider HPBW; uniform illumination -> narrowest beam but highest sidelobes (~-13.5 dB); use an intermediate (e.g. Chebyshev-type) taper to balance. | SLL(uniform) ~ -13.5 dB | taper | apertures and continuous sources | review | p.675-676 | high |
| BALANIS-333 | antenna | Edge-of-coverage (EOC) optimum uniform rectangular aperture: size each side to maximize directivity at the coverage edge angle in that plane. | b = lambda/(2*sin(theta_ce)) ; a = lambda/(2*sin(theta_ch)) ; D0 = (4*pi/lambda^2)*a*b | theta_ce, theta_ch | satellite footprint design | calc | p.677 eq.(12-58a)-(12-59) | high |
| BALANIS-334 | antenna | EOC optimum uniform circular aperture: maximum at the edge when k*a*sin(theta_c) = 1.841; EOC directivity is -3.985 dB below peak. | a = 1.841*lambda/(2*pi*sin(theta_c)) = lambda/(3.413*sin(theta_c)) ; D0 = 1.079*pi/sin^2(theta_c) (Table 12.3 lists 1.086*pi) | theta_c | uniform circular | calc | p.678 eq.(12-61a)-(12-65) | high |
| BALANIS-335 | antenna | EOC designs (Table 12.3): square uniform side lambda/(2 sin theta_c), D = pi/sin^2 theta_c, EOC -3.920 dB; circular uniform radius lambda/(3.413 sin theta_c), 1.086*pi/sin^2, -3.985 dB; parabolic taper lambda/(2.732 sin theta_c), 1.263*pi/sin^2, -4.069 dB; parabolic taper on -10 dB pedestal lambda/(3.064 sin theta_c), 1.227*pi/sin^2, -4.034 dB. | see table | theta_c | Praba 1994 | calc | p.679 Table 12.3 | high |
| BALANIS-336 | antenna | Worked EOC (uniform, theta_c = 30 deg): square a = b = lambda, D0 = 12.5664 (10.992 dB), 7.072 dB at 30 deg; circular a = 0.586*lambda, D0 = 13.559 (11.32 dB), 7.365 dB at 30 deg. | as stated | - | Example 12.5 | calc | p.679 Ex.12.5 | high |
| BALANIS-337 | antenna | Babinet/Booker: a slot in a thin PEC screen and its complementary strip dipole satisfy Zs*Zc = eta^2/4; slot fields equal the dipole fields with E and H interchanged (vertical slot on vertical screen -> horizontal polarization); thin half-wave slot Zs ~ 362.95 - j211.31 ohm from Zc = 73 + j42.5. | Zs*Zc = eta^2/4 ; E_theta,s = H_theta,c ; H_theta,s = -E_theta,c/eta0^2 | Zc or Zs | infinite thin screen (approximated by screens large vs lambda and slot) | calc | p.680-683 eq.(12-67),(12-68), Ex.12.6 | high |
| BALANIS-338 | antenna | Slot on a finite screen: impedance is less affected than the pattern by finite screen size; slot radiates both sides; cavity backing makes it unidirectional with cavity depth an odd multiple of lambda_g/4. | depth = (2m+1)*lambda_g/4 | lambda_g | cavity-backed slot (covert/law-enforcement uses) | calc | p.682, p.684 | high |
| BALANIS-339 | antenna | Dielectric-covered aperture on a ground plane: the cover forces the E-plane field to zero along the surface; H-plane nearly unchanged; with increasing cover thickness both planes broaden near grazing and narrow elsewhere (TE10 guide, er = 2.1, h = 0.125-0.5*lambda0). | n/a | h, er | spectral-domain analysis (surface waves excluded) | sim | p.694-695 Fig 12.27 | high |
| BALANIS-340 | antenna | Aperture admittance via spectral domain: visible region (kx^2 + ky^2 <= k^2) gives conductance, invisible region gives susceptance; narrow slot (parallel-plate) admittance per unit length is always capacitive. | Ya = 2P*/abs(V)^2 ; small slot (b/lambda < 1/10): Ga ~ (pi/(eta*lambda))*[1 - (kb)^2/24], Ba ~ (pi/(eta*lambda))*[1 - 0.636*ln(kb)] ; large (b/lambda > 1): Ga ~ 1/(eta*b) | b, lambda, eta | parallel-plate guide on ground plane | calc | p.695-702 eq.(12-116), Ex.12.8 | high |
| BALANIS-341 | antenna | Finite ground planes: edge diffractions alter patterns mainly in low-intensity regions; model with GTD (large objects, high frequency) or MoM (small objects); a circular ground plane's rim produces stronger minor lobes near the axis than a square plane of similar size (lambda/4 monopole measurements). | n/a | ground plane size/shape | monopoles and apertures on finite grounds | sim | p.702-707 Figs 12.33-12.35 | high |

### Ch 13 — Horn antennas

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BALANIS-360 | antenna | Horns serve as reflector/lens feeds, phased-array elements and the universal standard for gain calibration of other high-gain antennas. | n/a | - | microwave horns | review | p.719 | high |
| BALANIS-361 | antenna | Horn aperture phase: quadratic approximation of the path difference from the virtual apex; maximum phase deviation at the aperture edge sets flare for a given length. | delta(y') ~ y'^2/(2*rho1) ; dphi_max = k*(b1/2)^2/(2*rho1) ; 2*psi_e = 2*atan(b1/(2*rho1)) | b1, rho1, lambda | E-plane sectoral horn (H-plane analog with a1, rho2) | calc | p.721-722 eq.(13-2b), Ex.13.1 | high |
| BALANIS-362 | antenna | Worked flare (a = 0.5*lambda, b = 0.25*lambda, b1 = 2.75*lambda): 56.72 deg maximum phase deviation -> rho1 = 6*lambda, total flare 2*psi_e = 25.81 deg. | as stated | - | Example 13.1 | calc | p.722 Ex.13.1 | high |
| BALANIS-363 | antenna | Quadratic- vs spherical-phase directivity: identical for apertures > 50*lambda or peak phase error S = rho_e - rho1 (or T = rho_h - rho2) < 0.2*lambda; spherical phase gives up to a few tenths dB (up to 0.6 dB for pyramidal) more for 5-8*lambda apertures or 0.2-0.6*lambda phase errors; can be lower for S, T > 0.6*lambda (especially E-plane horns). | S, T < 0.2*lambda -> quadratic model exact enough | a1, b1, S, T | horn directivity models | calc | p.722, p.756 | high |
| BALANIS-364 | antenna | Horn flare trade-off: for fixed length, beam narrows and directivity rises with flare up to an optimum, then the quadratic phase error broadens/flattens the beam and the maximum can leave the axis (e.g. rho1 = 15*lambda at 2*psi_e = 35 deg; pyramidal rho1 = rho2 = 6*lambda, a1 = 12*lambda, b1 = 6*lambda); a lens at the aperture removes the phase error. | n/a | flare, length | sectoral/pyramidal/conical horns | sim | p.726-728, p.738, p.746-748 | high |
| BALANIS-365 | antenna | E-plane sectoral horn directivity (Fresnel integrals C, S with argument q = b1/sqrt(2*lambda*rho1)). | D_E = (64*a*rho1/(pi*lambda*b1))*[C^2(q) + S^2(q)] | a, b1, rho1, lambda | quadratic phase, TE10 feed | calc | p.730 eq.(13-18) | high |
| BALANIS-366 | antenna | E-plane horn optimum (maximum directivity for a given length): aperture b1 ~ sqrt(2*lambda*rho1), i.e. peak phase deviation s = b1^2/(8*lambda*rho1) = 1/4 wavelength. | b1_opt = sqrt(2*lambda*rho1) ; s_op = 1/4 | rho1, lambda | E-plane sectoral horn | calc | p.731 eq.(13-18a),(13-18b) | high |
| BALANIS-367 | antenna | More accurate on-axis E-plane horn directivity (open-ended parallel-plate analysis) including the feed guide wavelength; agrees better with measurement than (13-18). | D_E(max) = [16*a*b1/(lambda^2*(1 + lambda_g/lambda))]*[(C^2(q) + S^2(q))/q^2]*exp[(pi*a/lambda)*(1 - lambda/lambda_g)], q = b1/sqrt(2*lambda*rho1) | a, b1, rho1, lambda, lambda_g | optimum-length E-plane horn; OCR-garbled, structure per [12],[13] | calc | p.731 eq.(13-18c) | medium |
| BALANIS-368 | antenna | Braun graphical E-plane directivity: B = (b1/lambda)*sqrt(50/(rho_e/lambda)); G_E from Fig 13.8, or G_E = (32/pi)*B if B < 2; D_E = (a/lambda)*G_E/sqrt(50/(rho_e/lambda)). | as stated | b1, a, rho_e, lambda | Braun data | calc | p.732 eq.(13-19a)-(13-19c) | high |
| BALANIS-369 | antenna | Worked E-plane horn (a = 0.5, b1 = 2.75, rho1 = 6 lambda): q = 0.794, C = 0.72, S = 0.24 -> D_E = 12.79 (11.07 dB); rho_e = 6.1555*lambda, sqrt(50/rho_e) = 2.85, B = 7.84, G_E = 73.5 -> D_E = 12.89 (11.10 dB). | as stated | - | Example 13.2 | calc | p.732-733 Ex.13.2 | high |
| BALANIS-370 | antenna | H-plane sectoral horn directivity. | D_H = (4*pi*b*rho2/(a1*lambda))*{[C(u)-C(v)]^2 + [S(u)-S(v)]^2} ; u = (1/sqrt2)*(sqrt(lambda*rho2)/a1 + a1/sqrt(lambda*rho2)) ; v = (1/sqrt2)*(sqrt(lambda*rho2)/a1 - a1/sqrt(lambda*rho2)) | a1, b, rho2, lambda | quadratic phase | calc | p.740 eq.(13-39) | high |
| BALANIS-371 | antenna | H-plane horn optimum: a1 ~ sqrt(3*lambda*rho2), i.e. peak phase deviation t = a1^2/(8*lambda*rho2) = 3/8 wavelength. | a1_opt = sqrt(3*lambda*rho2) ; t_op = 3/8 | rho2, lambda | H-plane sectoral horn | calc | p.740 eq.(13-39c),(13-39d) | high |
| BALANIS-372 | antenna | Braun graphical H-plane directivity: A = (a1/lambda)*sqrt(50/(rho_h/lambda)); G_H from Fig 13.15, or G_H = (32/pi)*A if A < 2; D_H = (b/lambda)*G_H/sqrt(50/(rho_h/lambda)). | as stated | a1, b, rho_h | Braun data | calc | p.741 eq.(13-40a)-(13-40c) | high |
| BALANIS-373 | antenna | Worked H-plane horn (a1 = 5.5, b = 0.25, rho2 = 6 lambda): u = 1.9, v = -1.273 -> D_H = 7.52 (8.763 dB); rho_h = 6.6*lambda, A = 15.14, G_H = 91.8 -> D_H = 8.338 (9.21 dB). | as stated | - | Example 13.3 | calc | p.743 Ex.13.3 | high |
| BALANIS-374 | antenna | Pyramidal horn physical realizability: the two slant lengths from the feed guide must be equal (pe = ph); principal-plane patterns equal those of the corresponding sectoral horns. | pe = (b1 - b)*sqrt((rho_e/b1)^2 - 1/4) ; ph = (a1 - a)*sqrt((rho_h/a1)^2 - 1/4) ; require pe = ph | a, b, a1, b1, rho_e, rho_h | pyramidal horn | calc | p.746-747 eq.(13-47a),(13-47b) | high |
| BALANIS-375 | antenna | Horn cross-polarization of good designs should be >= 30 dB below the co-polarized field (nonsymmetry, construction defects and higher-order modes create cross-pol). | X-pol <= -30 dB | pattern | horns | measure | p.748 | high |
| BALANIS-376 | antenna | Aperture-field (Fresnel) horn models are accurate near the main lobe and first sidelobes only; use edge diffraction (GTD) or full-wave MoM/FDTD for minor/back lobes (MoM matched measured 20-dB standard-gain horn patterns at 10 GHz including back lobes). | n/a | - | horn pattern prediction | sim | p.747-749 Fig 13.20 | high |
| BALANIS-377 | antenna | Pyramidal horn directivity from the sectoral-horn directivities. | D_p = (pi*lambda^2/(32*a*b))*D_E*D_H ; (= 8*pi*rho1*rho2/(a1*b1)*{[C(u)-C(v)]^2+[S(u)-S(v)]^2}*[C^2(q)+S^2(q)]) | D_E, D_H, a, b | pyramidal horn | calc | p.750 eq.(13-50),(13-50a) | high |
| BALANIS-378 | antenna | Pyramidal horn directivity from aperture area and phase-error loss figures (Fig 13.21 gives L_e(s), L_h(t)). | D_p(dB) = 10*[1.008 + log10(a1*b1/lambda^2)] - (L_e + L_h) ; s = b1^2/(8*lambda*rho1) ; t = a1^2/(8*lambda*rho2) | a1, b1, rho1, rho2, lambda | graph for L_e, L_h | calc | p.750-751 eq.(13-51), Fig 13.21 | medium |
| BALANIS-379 | antenna | Braun graphical pyramidal directivity (accurate to within 0.01 dB for rho_e = rho_h = 50*lambda). | D_p = G_E*G_H/[(32/pi)*sqrt(50/(rho_e/lambda))*sqrt(50/(rho_h/lambda))] = G_E*G_H/[10.1859*sqrt(50/(rho_e/lambda))*sqrt(50/(rho_h/lambda))] | G_E, G_H, rho_e, rho_h | Braun data | calc | p.750-751 eq.(13-52a)-(13-52e) | high |
| BALANIS-380 | antenna | Worked pyramidal horn (rho1 = rho2 = 6, a1 = 5.5, b1 = 2.75, a = 0.5, b = 0.25 lambda): pe = ph = 5.454*lambda (realizable); D_p = 75.54 (18.78 dB) by (13-50a); 84.41 (19.26 dB) by (13-52e); s = 0.1575, t = 0.63 -> L_e = 0.20 dB, L_h = 2.75 dB -> 18.93 dB by (13-51). | as stated | - | Example 13.4 | calc | p.753 Ex.13.4 | high |
| BALANIS-381 | antenna | Standard-gain pyramidal horn references: commercial X-band (8.2-12.4 GHz) exponential-taper horn, HPBW ~28 deg in E and H planes, sidelobes ~13 dB (E) and ~20 dB (H) down, VSWR < 1.1; 20-dB standard gain horn at 10 GHz: a1 = 4.87 in, b1 = 3.62 in, pe = ph = 10.06 in, WR-90 feed a = 0.9 in, b = 0.4 in. | as stated | - | NARDA horn data | measure | p.748-752, p.768 | high |
| BALANIS-382 | antenna | Optimum-gain pyramidal horn design: overall (antenna x aperture) efficiency ~50%, both planes at optimum (b1 = sqrt(2*lambda*rho_e), a1 = sqrt(3*lambda*rho_h)); solve the horn design equation for chi = rho_e/lambda starting from chi1 = G0/(2*pi*sqrt(2*pi)). | G0 = 0.5*(4*pi/lambda^2)*a1*b1 ; (sqrt(2*chi) - b/lambda)^2*(2*chi - 1) = (G0/(2*pi)*sqrt(3/(2*pi*chi)) - a/lambda)^2*(G0^2/(6*pi^3*chi) - 1) ; rho_h/lambda = G0^2/(8*pi^3*chi) ; a1 = (G0/(2*pi))*sqrt(3/(2*pi*chi))*lambda ; b1 = sqrt(2*chi)*lambda | G0 (linear), a, b, lambda | standard-gain horn design; then check pe = ph | calc | p.754-755 eq.(13-53)-(13-56b) | high |
| BALANIS-383 | antenna | Worked optimum horn (22.6 dB at 11 GHz, WR-90 a = 2.286 cm, b = 1.016 cm): G0 = 181.97, lambda = 2.7273 cm, chi1 = 11.5539 -> chi = 11.1157; rho_e = 30.316 cm, rho_h = 32.753 cm, a1 = 6.002*lambda = 16.370 cm, b1 = 4.715*lambda = 12.859 cm, pe = ph = 27.286 cm; checks give 22.1-22.5 dB. | as stated | - | Example 13.5 | calc | p.755-756 Ex.13.5 | high |
| BALANIS-384 | antenna | Optimum conical horn curve fits (length L, aperture diameter d_m). | (Dc)opt ~ 15.9749*(L/lambda) + 1.7209 ; (Dc)opt ~ 5.1572*(d_m/lambda)^2 - 0.6451*(d_m/lambda) + 1.3645 ; L/lambda ~ 0.3232*(d_m/lambda)^2 - 0.0475*(d_m/lambda) + 0.0052 | L, d_m, lambda | dimensionless directivity; spherical-phase-based fits [23] | calc | p.757 eq.(13-57a)-(13-57c) | high |
| BALANIS-385 | antenna | Conical horn directivity with phase-error loss figure (s = maximum aperture phase deviation in wavelengths). | Dc(dB) = 10*log10[(C/lambda)^2] - L(s), C = pi*d_m ; L(s) = -10*log10(eps_ap) ~ 0.5030 + 5.1123s - 7.1138s^2 + 23.1401s^3 (L <= 3*lambda) ; 0.7853 - 0.3976s + 13.112s^2 + 3.901s^3 (L > 3*lambda) ; s = d_m^2/(8*lambda*l) | d_m, l (slant length), L (axial length), lambda | conical horn | calc | p.758-759 eq.(13-58)-(13-58d) | high |
| BALANIS-386 | antenna | Conical horn optimum: d_m ~ sqrt(3*l*lambda) (s = 3/8), loss figure ~2.9 dB (aperture efficiency ~51%). | d_m,opt = sqrt(3*l*lambda) | l, lambda | conical horn | calc | p.759 eq.(13-59) | high |
| BALANIS-387 | antenna | Commercial X-band conical horn (L = 7.147*lambda, 2*psi_c = 35 deg) patterns at 10.5 GHz over a 0-60 dB range agree with GTD/UTD, simulation and measurement including back lobes. | as stated | - | Figs 13.25, 13.28 | measure | p.757-760 | high |
| BALANIS-388 | antenna | Corrugated horns raise reflector-feed aperture efficiency from ~50-60% (conventional feeds) to ~75-80%, equalize E/H beamwidths (near rotational symmetry), and cut edge diffraction (lower minor and back lobes). | eps_ap: 50-60% -> 75-80% | - | reflector feeds, radiometry | review | p.761-762 | high |
| BALANIS-389 | antenna | Corrugation geometry: >= 10 slots per wavelength; slot width w < lambda0/10; tooth thickness t <= w/10; slot depth lambda0/4 < d < lambda0/2 (generally (2n+1)*lambda0/4 < d < (n+1)*lambda0/2) so the surface is capacitive (no surface waves, E-plane edges not illuminated). | X = (w/(w+t))*sqrt(mu0/eps0)*tan(k0*d) ; w < lambda0/10 ; t <= w/10 ; lambda0/4 < d < lambda0/2 | w, t, d, lambda0 | corrugated horn walls | calc | p.763-764 eq.(13-60) | high |
| BALANIS-390 | antenna | Corrugated-horn practice: start corrugations a small distance from the waveguide-horn junction for low VSWR over a broad band; the cosine E-plane distribution is established by the 5th corrugation and the spherical phase front by the 15th (45-corrugation horn); a large corrugated horn handled 20 kW peak at 10 GHz without breakdown. | n/a | - | corrugated horns | inspect | p.764, p.766 | high |
| BALANIS-391 | antenna | Conical corrugated (scalar) horn slots: machine perpendicular to the axis for flare half-angles below ~20-25 deg (easier), perpendicular to the wall for larger flares. | psi_c < 20-25 deg -> axial-perpendicular slots | psi_c | scalar horns (Cassegrain feeds) | inspect | p.766 | high |
| BALANIS-392 | antenna | Corrugated vs conventional horn (2.96*lambda square, 50 deg flare, 10 GHz): much lower minor/back lobes, wider 3-dB but narrower 10-dB beamwidth, E- and H-plane patterns nearly identical 8-14 GHz; for an 8.2*lambda horn the corrugated beam is narrower and removes the on-axis saddle of the thick-edged control horn. | n/a | - | Fig 13.32 | measure | p.764-766 | high |
| BALANIS-393 | antenna | Aperture-matched horn: blend convex curved sections onto the aperture edges (radii 1.69*lambda to 8.47*lambda tested; circular cylinders with 2.5*lambda <= a <= 5*lambda work well) to replace edge by curved-surface diffraction: smoother patterns, much lower back lobes, 2:1 bandwidth; add a curved throat transition to cut throat reflections; corrugated aperture-matched horns reach cross-pol < -45 dB. | 2.5*lambda <= R <= 5*lambda ; BW 2:1 ; X-pol < -45 dB | R | reference/frequency-reuse horns | inspect | p.766-769 Fig 13.34 | high |
| BALANIS-394 | antenna | Diagonal horn (TE10 + TE01 in square guide): nearly equal 3-, 10-, 30-dB beamwidths in principal and 45/135-deg planes; principal-plane sidelobes theoretically -31.5 dB (>= 30 dB down observed), 45-deg-plane sidelobes -19.2 dB theory (-23 to -27 dB observed) but cross-pol lobes only 16 dB down in the +/-45-deg planes. A conventional square pyramidal horn has ~35% wider H-plane than E-plane beamwidth and E-plane sidelobes only 12-13 dB down. | as stated | - | multimode horns | review | p.769-770 | high |
| BALANIS-395 | antenna | Dual-mode (TE11 + TM11) conical horn gives equal beamwidths, suppressed sidelobes, low cross-pol and coincident E/H phase centers at the cost of axial gain (ideal Cassegrain feed); multimode feeds (adding TE12, TE13, TM12) raise paraboloid aperture efficiency to ~90% vs ~76% with dominant-mode feeds. | eps_ap: ~76% -> ~90% | modes | reflector feeds | review | p.770-771 | high |
| BALANIS-396 | antenna | Single-horn monopulse modes: sum TE10 + TE30 (cancels second minor lobe), E-plane difference TE11 + TM11, H-plane difference TE20. | n/a | - | multimode pyramidal monopulse horn | review | p.771 | high |
| BALANIS-397 | antenna | Dielectric loading of horn H-plane walls (dominant LSE mode) raises aperture efficiency to ~92-96% vs ~81% unloaded; Dielguides between feed and reflector act like shaped lenses. | eps_ap 92-96% | - | loaded horns | review | p.771 | high |
| BALANIS-398 | antenna | Feed phase center must sit at the reflector focus (defocus costs gain). Horn phase center lies between the virtual apex and the aperture: near the apex for large flare, toward the aperture for small flare; E- and H-plane phase centers coincide for small flares, otherwise use their average for a pyramidal horn. | n/a | flare angles | reflector feeds | measure | p.773-774 Fig 13.37 | high |

### Ch 14 — Microstrip and mobile communications antennas (priority)

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BALANIS-400 | antenna | Microstrip patch baseline limitations: low efficiency, low power, high Q (sometimes > 100), poor polarization purity and scan performance, spurious feed radiation, bandwidth typically a fraction of a percent to a few percent; thicker substrates raise efficiency (up to ~90% excluding surface waves) and bandwidth (up to ~35%) but excite surface waves. | Q > 100 possible ; BW ~0.x-few % ; thick: eta <= ~90%, BW <= ~35% | h, er | patch antennas | review | p.783 | high |
| BALANIS-401 | antenna | Patch substrate height window and conductor thickness. | 0.003*lambda0 <= h <= 0.05*lambda0 ; t << lambda0 | h, t, lambda0 | microstrip antennas | calc | p.784-785 | high |
| BALANIS-402 | antenna | Rectangular patch length window (dominant mode). | lambda0/3 < L < lambda0/2 | L, lambda0 | rectangular patch | calc | p.785 | high |
| BALANIS-403 | materials | Patch substrate selection: usual 2.2 <= er <= 12; thick, low-er substrates give better efficiency, larger bandwidth and loosely bound fields (larger element); thin, high-er substrates suit microwave circuitry (tightly bound fields, less radiation/coupling, smaller) but are lossier and narrower-band as antennas; compromise when integrating with circuits. | 2.2 <= er <= 12 | er, h | antenna vs circuit substrate | review | p.785 | high |
| BALANIS-404 | materials | Typical antenna substrates (Table 14.1): Duroid 5880 er 2.20 tan d 0.0009 (0-40 GHz); RO3003 3.00/0.0010; RO3010 10.2/0.0022; RO4350 3.48/0.0037; FR4 4.70 (tan d not given); DuPont HK 04J 3.50/0.005; Isola IS 410 5.40/0.035; Arlon DiClad 870 2.33/0.0013; Polyflon Polyguide 2.32/0.0005; Neltec NH 9320 3.20/0.0024; Taconic RF-60A 6.15/0.0038. | see Table 14.1 | substrate | nominal catalog values; column alignment reconstructed from OCR | inspect | p.784 Table 14.1 | medium |
| BALANIS-405 | antenna | Microstrip-line (inset) feed: easy to fabricate and match (inset position), simple to model; as h increases, surface waves and spurious feed radiation grow and practically limit bandwidth to ~2-5%. | BW ~ 2-5% | h | edge/inset microstrip feed | review | p.785-786 | high |
| BALANIS-406 | antenna | Coaxial probe feed: easy to fabricate and match, low spurious radiation, narrow bandwidth; difficult to model for thick substrates (h > 0.02*lambda0). Line and probe feeds are asymmetric and excite higher-order modes that produce cross-polarization. | h > 0.02*lambda0 -> use full-wave model | h | probe-fed patches | sim | p.786 | high |
| BALANIS-407 | antenna | Aperture-coupled feed: most difficult to fabricate, narrow bandwidth, moderate spurious radiation, feed isolated from radiator by the ground plane; use high-er bottom (feed) substrate and thick low-er top substrate; match with feed-line width and slot length; center the slot under the patch (magnetic coupling dominates) for polarization purity with no principal-plane cross-pol. | slot centered under patch | slot length, feed width, er1, er2 | two-substrate stack | sim | p.787 | high |
| BALANIS-408 | antenna | Proximity-coupled feed has the largest bandwidth of the four common feeds (as high as 13%), low spurious radiation, moderate modeling difficulty, harder fabrication; match with feeding-stub length and patch width-to-line ratio. | BW <= ~13% | stub length, W/w_line | two-layer feed | sim | p.787 | high |
| BALANIS-409 | antenna | Analysis model choice: transmission-line model is easiest but least accurate and poor for coupling; cavity model more accurate with good insight; full-wave (integral equation/MoM) most accurate and handles finite/infinite arrays, stacked and arbitrary shapes and coupling. TL and cavity models are most accurate for thin substrates. | n/a | - | design flow: TL/cavity first cut -> full-wave sign-off | review | p.787-788 | high |
| BALANIS-410 | transmission-line | Static effective dielectric constant of microstrip/patch (valid W/h > 1); eps_reff rises with frequency toward er (Fig 14.6). | eps_reff = (er+1)/2 + (er-1)/2*(1 + 12*h/W)^(-1/2) | er, h, W | W/h > 1; low-frequency (static) value | calc | p.789 eq.(14-1) | high |
| BALANIS-411 | antenna | Fringing length extension of a rectangular patch (Hammerstad). | dL = 0.412*h*(eps_reff+0.3)*(W/h+0.264)/((eps_reff-0.258)*(W/h+0.8)) | h, W, eps_reff | dominant TM010 | calc | p.790 eq.(14-2) | high |
| BALANIS-412 | antenna | Effective length and resonant frequency with fringing; fringing lowers the resonance by typically 2-6% vs the no-fringing value. | Leff = L + 2*dL ; f_r(no fringing) = v0/(2*L*sqrt(er)) ; f_rc = v0/(2*Leff*sqrt(eps_reff)) = q*v0/(2*L*sqrt(er)) ; q = f_rc/f_r | L, dL, eps_reff, v0 = 2.998e8 m/s | TM010, L > W | calc | p.790-791 eq.(14-3)-(14-5a) | high |
| BALANIS-413 | antenna | Patch width for good radiation efficiency (design step 1). | W = (v0/(2*f_r))*sqrt(2/(er+1)) | f_r, er | rectangular patch design | calc | p.791 eq.(14-6) | high |
| BALANIS-414 | antenna | Patch physical length (design step 4) after computing eps_reff (14-1) with W and dL (14-2). | L = v0/(2*f_r*sqrt(eps_reff)) - 2*dL | f_r, eps_reff, dL | rectangular patch design | calc | p.791 eq.(14-7) | high |
| BALANIS-415 | antenna | Typical patch length is 0.47-0.49 of the dielectric wavelength; lower er -> more fringing -> relatively shorter patch; higher er -> closer to lambda_d/2. | L ~ (0.47-0.49)*lambda0/sqrt(er) | lambda0, er | rectangular patch | calc | p.791 eq.(14-7a) | high |
| BALANIS-416 | antenna | Worked rectangular patch (er = 2.2 RT/duroid 5880, h = 0.1588 cm, 10 GHz): W = 1.186 cm, eps_reff = 1.972, dL = 0.081 cm, L = 0.906 cm, Le = 1.068 cm; the built probe-fed prototype's patterns are shown at 9.8 GHz (10 x 10 cm ground plane). | as stated | - | Example 14.1, Fig 14.8(a), 14.21 | calc | p.792, p.809 | high |
| BALANIS-417 | antenna | Radiating-slot admittance (transmission-line model, infinitely wide slot approximation). | G1 = W/(120*lambda0)*[1 - (k0*h)^2/24] (S) ; B1 = W/(120*lambda0)*[1 - 0.636*ln(k0*h)] (S) | W, h, lambda0, k0 = 2*pi/lambda0 | h/lambda0 < 1/10 | calc | p.793 eq.(14-8a),(14-8b) | high |
| BALANIS-418 | antenna | Radiating-slot conductance from the cavity-model field (preferred over 14-8a, which overestimated by ~2x in Example 14.2: 0.00157 vs 0.00328 S). | G1 = I1/(120*pi^2) ; I1 = -2 + cos(X) + X*Si(X) + sin(X)/X ; X = k0*W | W, lambda0 | k0*h << 1 | calc | p.793-794 eq.(14-12),(14-12a),(14-12b) | high |
| BALANIS-419 | antenna | Slot conductance asymptotes. | G1 = (1/90)*(W/lambda0)^2 for W << lambda0 ; G1 = (1/120)*(W/lambda0) for W >> lambda0 | W/lambda0 | single slot | calc | p.794 eq.(14-13) | high |
| BALANIS-420 | antenna | Resonant edge input resistance, without and with mutual conductance; use + for the dominant TM010 (odd/antisymmetric voltage) mode, - for even modes. | Rin = 1/(2*G1) ; Rin = 1/(2*(G1 +/- G12)) | G1, G12 (S) | edge-fed rectangular patch at resonance | calc | p.794-795 eq.(14-16),(14-17) | high |
| BALANIS-421 | antenna | Mutual conductance between the two radiating slots (usually small vs G1). | G12 = (1/(120*pi^2))*Integral_0^pi [sin((k0*W/2)*cos(th))/cos(th)]^2 * J0(k0*L*sin(th)) * sin^3(th) dth | W, L, lambda0 | cavity-model far field | calc | p.795 eq.(14-18a) | high |
| BALANIS-422 | antenna | Alternate closed-form resonant edge resistance for thin substrates (h << lambda0). | Rin = 90*(er^2/(er-1))*(L/W)^2 (ohm) | er, L, W | thin grounded substrate; squared exponent restored (OCR dropped it) — gives 212 ohm for Example 14.2 vs 228 ohm from (14-17) | calc | p.796 eq.(14-18b) | medium |
| BALANIS-423 | antenna | Edge input resistance is only weakly dependent on substrate height (independent of h for k0*h << 1); lower it by widening the patch but keep W/L <= 2 (single-patch aperture efficiency drops beyond 2). | W/L <= 2 | W, L | rectangular patch | calc | p.796 | high |
| BALANIS-424 | transmission-line | Microstrip feed-line characteristic impedance (Hammerstad). | Zc = (60/sqrt(eps_reff))*ln(8h/W0 + W0/(4h)) for W0/h <= 1 ; Zc = 120*pi/(sqrt(eps_reff)*[W0/h + 1.393 + 0.667*ln(W0/h + 1.444)]) for W0/h > 1 | W0 line width, h, eps_reff (14-1 with W = W0) | quasi-static | calc | p.797 eq.(14-19a),(14-19b) | high |
| BALANIS-425 | matching | Inset (recessed) feed input resistance, full form. | Rin(y0) = [1/(2*(G1 +/- G12))]*[cos^2(pi*y0/L) + ((G1^2+B1^2)/Yc^2)*sin^2(pi*y0/L) - (B1/Yc)*sin(2*pi*y0/L)] ; Yc = 1/Zc | G1, B1, G12, Zc, L, y0 | modal expansion | calc | p.797 eq.(14-20) | high |
| BALANIS-426 | matching | Inset-feed rule (G1/Yc << 1, B1/Yc << 1): resistance falls as cos^2 of the inset depth, from Rin(0) at the edge to zero at the center. | Rin(y0) = Rin(0)*cos^2(pi*y0/L) ; y0 = (L/pi)*acos(sqrt(Z0/Rin(0))) | Rin(0), L, Z0 | rectangular patch, dominant mode | calc | p.797 eq.(14-20a) | high |
| BALANIS-427 | matching | Edge resistance is typically 150-300 ohm; inset notch adds a junction capacitance that shifts resonance by ~1%; near the patch center cos^2 varies fast, so feed position needs tight tolerance. | Rin(0) ~ 150-300 ohm ; df_r ~ 1% from notch | y0 tolerance | inset-fed patch | measure | p.797 | high |
| BALANIS-428 | matching | Alternative patch matching: coupled (gap) recessed microstrip or a lambda/4 transformer at the radiating edge, which requires the edge input impedance to be real (at resonance). | Z1 = sqrt(Zc*Rin) | Zc, Rin | Fig 14.12 | calc | p.797-798 | high |
| BALANIS-429 | matching | Worked inset example (L = 0.906 cm, W = 1.186 cm, h = 0.1588 cm, er = 2.2, 10 GHz): G1 = 0.00157 S (cavity) vs 0.00328 S (TL formula), G12 = 6.1683e-4 S, Rin(edge) = 228.3508 ohm, inset for 50 ohm y0 = 0.3126 cm. | as stated | - | Example 14.2 | calc | p.797-798 Ex.14.2 | high |
| BALANIS-430 | antenna | Cavity-model interpretation: the patch is a "voltage radiator" (fringing fields at the two radiating edges add in phase); lower er -> more fringing -> more efficient radiation; high er is used for lines to suppress radiation; model losses with effective loss tangent delta_eff = 1/Q. | delta_eff = 1/Q | er, Q | cavity model | review | p.799-800 | high |
| BALANIS-431 | antenna | Rectangular cavity resonances (TMx, x normal to patch, y along L, z along W). | f_mnp = [1/(2*pi*sqrt(mu*eps))]*sqrt((m*pi/h)^2 + (n*pi/L)^2 + (p*pi/W)^2), m = n = p != 0 | h, L, W, er | cavity model, no fringing | calc | p.802 eq.(14-31) | high |
| BALANIS-432 | antenna | Mode ordering: L > W > h -> dominant TM010 at v0/(2L*sqrt(er)); if L > W > L/2 > h the second mode is TM001 at v0/(2W*sqrt(er)); if L > L/2 > W > h the second mode is TM020 at v0/(L*sqrt(er)). | f010 = v0/(2L sqrt(er)) ; f001 = v0/(2W sqrt(er)) ; f020 = v0/(L sqrt(er)) | L, W, er | no fringing | calc | p.803 eq.(14-33)-(14-35) | high |
| BALANIS-433 | antenna | Only the two slots separated by L radiate significantly (same magnitude and phase -> broadside); the two slots along L cancel in the principal planes (non-radiating slots). Principal E-plane contains the patch normal and L; H-plane contains the normal and W. | n/a | - | TM010 | review | p.805-811 | high |
| BALANIS-434 | antenna | Patch far-field (k0h << 1) in principal planes: E-plane Ephi ~ [sin((k0h/2)cos phi)/((k0h/2)cos phi)]*cos((k0Le/2)sin phi); H-plane Ephi ~ sin(th)*[sin((k0h/2)sin th)/((k0h/2)sin th)]*[sin((k0W/2)cos th)/((k0W/2)cos th)]. Array factor of the two slots: AF = 2*cos((k0*Le/2)*sin th*sin phi). | see formula | h, W, Le, k0 | cavity model | sim | p.807-808 eq.(14-42),(14-45),(14-46) | high |
| BALANIS-435 | antenna | Off-center (probe) feed along the E-plane makes measured/simulated E-plane patterns asymmetric; the cavity model ignores it. Finite ground-plane edge effects need diffraction (GTD) or full-wave. | n/a | feed position, ground size | 10 x 10 cm ground plane in measurements | measure | p.809 | high |
| BALANIS-436 | antenna | Dielectric-covered ground plane: E-plane (vertical-polarization) pattern is forced to a null at grazing; H-plane pattern essentially unaltered. | E-plane null at th = 90 deg (grazing) | - | impedance-surface ground | sim | p.809-810 | high |
| BALANIS-437 | antenna | Single radiating slot directivity and asymptotes; weakly dependent on h while h is electrically small. | D0 = (2*pi*W/lambda0)^2/I1 ; D0 -> 3.3 (5.2 dB) for W << lambda0 ; D0 -> 4*(W/lambda0) for W >> lambda0 | W, lambda0 (I1 per 14-12a) | k0h << 1 | calc | p.811-812 eq.(14-53),(14-54) | high |
| BALANIS-438 | antenna | Patch (two-slot) directivity: exact-form and array-factor form; the (14-55) form is the more accurate (~0.5 dB above the array-factor estimate in Example 14.3). | D2 = (2*pi*W/lambda0)^2*pi/I2 = (2/(15*Grad))*(W/lambda0)^2 ; I2 = Int_0^pi Int_0^pi [sin((k0W/2)cos th)/cos th]^2 sin^3 th cos^2((k0*Le/2) sin th sin phi) dth dphi ; D2 = D0*2/(1+g12), g12 = G12/G1 | W, Le, lambda0, G1, G12 | k0h << 1 | calc | p.812-813 eq.(14-55),(14-55a),(14-56) | high |
| BALANIS-439 | antenna | Patch directivity asymptotes: ~2 dB above a single slot; not a strong function of h while h is electrically small. | D2 -> 6.6 (8.2 dB) for W << lambda0 ; D2 -> 8*(W/lambda0) for W >> lambda0 | W/lambda0 | two-slot model | calc | p.813 eq.(14-57) | high |
| BALANIS-440 | antenna | Approximate patch beamwidths (guideline only; E-plane beam is very wide so Kraus/Tai-Pereira directivity from them is inaccurate). | Theta_E ~ 2*asin(sqrt(7.03*lambda0^2/(4*(3*Le^2 + h^2)*pi^2))) ; Theta_H ~ 2*asin(sqrt(1/(2 + k0*W))) | Le, h, W, lambda0 | rectangular patch | calc | p.813 eq.(14-58),(14-59) | high |
| BALANIS-441 | antenna | Square-patch directivity vs substrate height at fixed resonance: the er = 2.55 curve lies above the er = 10.2 curve over h/lambda0 = 0-0.05 (graph; low-er substrates give higher directivity). | graph (Fig 14.23) | h/lambda0, er | square patch (Pozar data) | sim | p.814 Fig 14.23 | medium |
| BALANIS-442 | antenna | Worked directivity (Examples 14.1-14.3 patch): g12 = 0.3921, D_AF = 1.4367 (1.5736 dB), I1 = 1.863, D0 = 3.312 (5.201 dB), D2 = 4.7584 (6.7746 dB) by (14-56); I2 = 3.59801, D2 = 5.3873 (7.314 dB) by (14-55). | as stated | - | Example 14.3 | calc | p.814-815 Ex.14.3 | high |
| BALANIS-443 | antenna | Circular patch: TMz modes; only the radius is free, so mode order cannot be changed (only absolute frequencies); first four modes TM110, TM210, TM010, TM310 from zeros of J'm: chi'11 = 1.8412, chi'21 = 3.0542, chi'01 = 3.8318, chi'31 = 4.2012. | f_mn0 = chi'_mn/(2*pi*a*sqrt(mu*eps)) | a, er | h < 0.05*lambda0 (p = 0) | calc | p.815-817 eq.(14-64),(14-65) | high |
| BALANIS-444 | antenna | Circular patch dominant TM110 resonance, fringing-corrected effective radius, and design radius. | f110 = 1.8412*v0/(2*pi*a*sqrt(er)) ; ae = a*{1 + (2h/(pi*a*er))*[ln(pi*a/(2h)) + 1.7726]}^(1/2) ; f_rc = 1.8412*v0/(2*pi*ae*sqrt(er)) = 8.791e9/(ae*sqrt(er)) (ae in cm) ; a = F/{1 + (2h/(pi*er*F))*[ln(pi*F/(2h)) + 1.7726]}^(1/2), F = 8.791e9/(f_r*sqrt(er)) | f_r (Hz), er, h (cm) | h in cm in (14-69) | calc | p.817-818 eq.(14-66)-(14-69a) | high |
| BALANIS-445 | antenna | Worked circular patch (er = 2.2, h = 0.1588 cm, 10 GHz): F = 0.593, a = 0.525 cm (0.207 in), ae = 0.598 cm; built probe-fed at rho_f = 0.2 cm, 10 x 10 cm ground plane; good agreement cavity/sim/measurement. | as stated | - | Example 14.4, Fig 14.25 | calc | p.818-819 | high |
| BALANIS-446 | antenna | Circular patch conductances: radiation, conductor and dielectric; total conductance sets edge resistance. | Grad = ((k0*ae)^2/480)*Int_0^(pi/2) [J02p^2 + cos^2(th)*J02^2] sin th dth ; J02p = J0(k0 ae sin th) - J2(k0 ae sin th), J02 = J0(.) + J2(.) ; Gc = eps_m0*pi*(pi*mu0*f_r)^(-3/2)/(4*h^2*sqrt(sigma))*[(k*ae)^2 - m^2] ; Gd = eps_m0*tan(d)/(4*mu0*h*f_r)*[(k*ae)^2 - m^2] ; eps_m0 = 2 (m = 0), 1 (m != 0) ; Gt = Grad + Gc + Gd | ae, h, sigma, tan d, f_r, m | TMmn0 modes (m = n = 1 dominant) | calc | p.821-822 eq.(14-76)-(14-79) | high |
| BALANIS-447 | antenna | Circular patch directivity; tends to 3 (4.8 dB) for very small radius (slot over ground). | D0 = (k0*ae)^2/(120*Grad) | ae, Grad | TM110 | calc | p.822 eq.(14-80), Fig 14.28 | high |
| BALANIS-448 | matching | Circular patch input resistance vs probe radius (feed position along the radius sets the match; independent of azimuth). | Rin(rho0) = (1/Gt)*J1^2(k*rho0)/J1^2(k*ae) ; Rin(ae) = 1/Gt | rho0, ae, k = k0*sqrt(er), Gt | TM11 mode | calc | p.822-823 eq.(14-81),(14-82) | high |
| BALANIS-449 | antenna | Patch total Q combines radiation, conductor, dielectric and surface-wave Q; surface-wave loss negligible only for very thin substrates (eliminate with cavities). | 1/Qt = 1/Qrad + 1/Qc + 1/Qd + 1/Qsw | Q components | patch | calc | p.823-824 eq.(14-83) | high |
| BALANIS-450 | antenna | Thin-substrate Q approximations; Qrad is inversely proportional to h and usually dominant for thin substrates. | Qc = h*sqrt(pi*f*mu*sigma) ; Qd = 1/tan(d) ; Qrad = 2*omega*er*K/(h*Gt/l) ; K = Int(abs(E)^2 dA) / Loop(abs(E)^2 dl) ; rectangular TM010: K = L/4, Gt/l = Grad/W | h, f, sigma, tan d, er, Grad, L, W | h << lambda0 | calc | p.824 eq.(14-84)-(14-87b) | high |
| BALANIS-451 | antenna | Patch fractional bandwidth from Q, and the matched-VSWR form (use this one for specs). | df/f0 = 1/Qt ; df/f0 = (VSWR - 1)/(Qt*sqrt(VSWR)) | Qt, VSWR | VSWR = 1 at design frequency | calc | p.824-825 eq.(14-88),(14-88a) | high |
| BALANIS-452 | antenna | Bandwidth scales with volume; at constant resonant frequency BW ~ 1/sqrt(er) and increases with h. | BW ~ L*W*h ~ 1/sqrt(er) | er, h | rectangular patch | calc | p.825 eq.(14-89) | high |
| BALANIS-453 | antenna | Empirical patch bandwidth for VSWR <= 2 (abs(Gamma) <= 1/3), valid h << lambda0 with surface-wave power << space-wave power. | BW = (16/(3*sqrt(2)))*((er-1)/er^2)*(h/lambda0)*(W/L) = 3.771*((er-1)/er^2)*(h/lambda0)*(W/L) | er, h, lambda0, W, L | thin grounded substrate (Sommerfeld-based) | calc | p.825 eq.(14-89a) | high |
| BALANIS-454 | antenna | Patch radiation (space-wave) efficiency from Q; efficiency falls and bandwidth rises with h/lambda0, efficiency drop faster for er = 10 than er = 2.2 (surface waves; Fig 14.29, h/lambda0 0-0.1). | e_cdsw = (1/Qrad)/(1/Qt) = Qt/Qrad | Qt, Qrad | rectangular patch; graph trends | calc | p.825-826 eq.(14-90), Fig 14.29 | high |
| BALANIS-455 | antenna | Patch impedance vs frequency: R and X roughly symmetric about resonance; resonant reactance equals the feed reactance xf = (Xmin + Xmax)/2; feed reactance is small for thin substrates but must be included for thick ones (matching and loaded resonance). | xf = (Xmin + Xmax)/2 | Z(f) | probe-fed patch | measure | p.826 Fig 14.30 | high |
| BALANIS-456 | antenna | Probe feed reactance: ~2x larger with the probe at an edge and ~4x at a corner vs an interior point (image argument; overestimates at the very edge). Approximate probe reactance (no images). | xf ~ -(eta*k*h/(2*pi))*[ln(k*d/4) + 0.577] (ohm) | h, d probe diameter, k and eta of substrate (eta*k = eta0*k0) | coax probe | calc | p.827 eq.(14-91) | medium |
| BALANIS-457 | antenna | Patch mutual coupling vs arrangement: for edge-to-edge spacing s < ~0.10*lambda0 the E-plane (collinear along E) arrangement couples less; for s > ~0.10*lambda0 the H-plane arrangement couples less, because the dominant TM0 surface wave (zero cutoff, 1/sqrt(rho) decay) propagates along the E-plane. Crossover depends on geometry/substrate. | crossover s ~ 0.10*lambda0 | s, arrangement | coax-fed patches (W = 10.57 cm, L = 6.55 cm, h = 0.1588 cm, er = 2.55, 1,410 MHz example) | sim | p.827-828 Fig 14.32 | high |
| BALANIS-458 | antenna | Mutual conductance between patches: H-plane arrangement decays with distance faster than E-plane; E-plane mutual conductance is higher for wider elements, H-plane lower for wider elements. | G12 per (14-92) E-plane, (14-93) H-plane | W, L, spacing | cavity model | calc | p.829-830 eq.(14-92),(14-93) | high |
| BALANIS-459 | antenna | Dual-feed CP patch: feed a square patch at two adjacent edges (TM010 and TM001) with 90 deg phase via a 90-deg hybrid or a power divider plus a lambda/4 line; circular patch: two probes 90 deg apart (each at the other's field null, low coupling) with a 90-deg hybrid; a center shorting pin suppresses phi-invariant modes and can improve CP. | feed phase quadrature 90 deg | - | Fig 14.34 | inspect | p.830 | high |
| BALANIS-460 | antenna | Probe angular spacing for CP on higher-order circular-patch modes (Table 14.2): TM110 90 deg; TM210 45 or 135 deg; TM310 30 or 90 deg; TM410 22.5 or 67.5 deg; TM510 18, 54 or 90 deg; TM610 15, 45 or 75 deg. For thicker substrates add two diametrically opposite probes (four total) to suppress adjacent modes. | alpha = (2k+1)*90deg/m (pattern of table) | mode m | after Huang [89]; table reconstructed from OCR | calc | p.830, p.832 Table 14.2 | medium |
| BALANIS-461 | antenna | Single-feed CP (nearly square patch, diagonal feed): the two orthogonal resonances bracket f0; side ratio from Qt; diagonal lower-left to upper-right gives LHCP, opposite diagonal RHCP; varactors can move the effective feed point electrically. | f1 = f0/sqrt(1 + 1/Qt) ; f2 = f0*sqrt(1 + 1/Qt) ; L/W = 1 + 1/Qt | f0, Qt | rectangular patch | calc | p.831 eq.(14-94a),(14-94b) | high |
| BALANIS-462 | antenna | Worked single-feed CP: 10 GHz, er = 2.2, h = 0.1588 cm, 5% BW at VSWR 2 -> Qt = 14.14, f1 = 9.664 GHz, f2 = 10.348 GHz, L/W = 1.07. | as stated | - | Example 14.5 | calc | p.831 Ex.14.5 | high |
| BALANIS-463 | antenna | Other near-CP perturbations: thin diagonal slot pair in a square patch with c = L/2.72 = W/2.72 and d = c/10 = L/27.2; trimmed opposite corners (feed at point 1 or 3); slightly elliptical circular patch or added tabs. | c = L/2.72 ; d = L/27.2 | L = W | square patch | calc | p.831-832 eq.(14-95a),(14-95b) | high |
| BALANIS-464 | antenna | Array feed choice: series feed (photolithographic, fixed beam or frequency scanning; any element change affects others; account for coupling/internal reflections); corporate feed (2^n splits, per-element amplitude/phase control, suits phased/multibeam/shaped arrays). | corporate splits 2^n | - | microstrip arrays | review | p.832-834 | high |
| BALANIS-465 | matching | Corporate feed matching of 100-ohm patches to a 50-ohm input with tapered lines or quarter-wave transformers (~70-ohm sections between 50- and 100-ohm lines, Fig 14.39). | Z_T = sqrt(50*100) = 70.7 ohm | Z1, Z2 | Munson feed network | calc | p.834-835 Fig 14.39 | medium |
| BALANIS-466 | antenna | Feed-line radiation (series or corporate) seriously limits array cross-polarization and sidelobe level; isolate the feed from the radiating face with probe feeds or aperture coupling. | n/a | feed topology | microstrip arrays | review | p.834 | high |
| BALANIS-467 | antenna | Microstrip array scan blindness from mutual coupling/surface (leaky) waves limits scan volume; conventional infinite array of circular patches (h = 0.08*lambda0, er = 2.5, dx = dy = 0.5*lambda0) goes blind in the E-plane near 72.5 deg; cavity backing strongly extends E-plane scan (at 2:1 VSWR), H-plane only for abs(Gamma) > ~0.6; both planes blind at grazing (90 deg). | E-plane blindness ~72.5 deg (conventional) | h, er, spacing | a = 0.156, b = 0.195, c = 0.25 lambda0, r0 = 0.004 lambda0 | sim | p.834-837 Fig 14.42 | high |
| BALANIS-468 | antenna | Scan performance metric: broadside-matched active reflection coefficient. | Gamma(th,phi) = [Zin(th,phi) - Zin(0,0)]/[Zin(th,phi) + Zin*(0,0)] | Zin(th,phi) | phased arrays | sim | p.836 eq.(14-96) | high |
| BALANIS-469 | antenna | EBG (high-impedance textured) substrate suppresses surface waves and removed scan blindness (~50 deg on the conventional substrate) for a printed-dipole array: dipole 9.766 mm in 4x4 cells (w = l = 1.22 mm, g = 1.66 mm), er = 2.2, h = 4.771 mm, band gap 9.7-15.1 GHz, at 13 GHz. | as stated | - | [92] design | sim | p.837 Fig 14.44 | high |
| BALANIS-470 | antenna | Shorted (lambda/4) patch: a shorting sheet or pin at the zero-voltage plane halves the patch length with radiation similar to the lambda/2 patch, at the cost of reduced bandwidth and gain. | L ~ lambda/4 | - | microstrip or probe fed | calc | p.837-839 Fig 14.45 | high |
| BALANIS-471 | antenna | PIFA advantages for handsets: low backward radiation (lower SAR), receives both polarizations, easy integration, light, conformal, low cost, reliable; drawbacks vs lambda/2 patch: lower bandwidth and gain. | n/a | - | mobile devices | review | p.838-839 | high |
| BALANIS-472 | antenna | PIFA resonance design equation (lambda = wavelength in the dielectric); full-width shorting sheet -> L = lambda/4 + h; pin-only short -> L ~ -W + lambda/4 + h. | L + W - ws = lambda/4 + h ; f = v0/(4*(L + W - ws - h)*sqrt(er)) | L, W, ws shorting width, h, er | planar inverted-F | calc | p.839-840 eq.(14-97)-(14-98) | high |
| BALANIS-473 | matching | PIFA/IFA feed placement: abs(Zin) decreases as the feed moves toward the short; for 50 ohm put the feed closer to the shorting sheet/pin than to the open end (y0 < L/2). | y0 < L/2 | y0 | PIFA, IFA | sim | p.840, p.843 | high |
| BALANIS-474 | antenna | Worked PIFA (air, er = 1, h = 0.448 cm, 1.8 GHz, W = 0.773L, ws = 0.428W = 0.331L): L = (lambda/4 + h)/1.442 = 3.2 cm = 0.192*lambda, W = 2.474 cm = 0.1484*lambda, ws = 1.059 cm = 0.0636*lambda, feed y0 = 0.57 cm. | as stated | - | Example 14.6, Figs 14.47-14.48 | sim | p.840-841 Ex.14.6 | high |
| BALANIS-475 | antenna | Slot antenna: length L ~ lambda/2, width W <= (0.05-0.1)*lambda, center-fed (voltage max at center); bidirectional unless cavity-backed (CBS); halving it with an open end gives an IFA. | L ~ lambda/2 ; W <= 0.05-0.1 lambda | L, W | ground-plane slot | calc | p.841-843 | high |
| BALANIS-476 | antenna | Babinet: complementary dipole and slot impedances; half-wave slot (W = lambda/10) predicted Zs ~ 362.95 - j211.31 ohm from Zd = 73 + j42.5; full-wave on a 5x5 lambda ground gave 339.38 - j78.85 ohm (reactance approaches the analytic value as W shrinks). | Zd*Zs = eta0^2/4 | Zd or Zs | free-space slot in PEC | calc | p.842-843 eq.(14-99), Ex.14.7 | high |
| BALANIS-477 | antenna | Planar IFA: arm ~ lambda/4 (lambda in dielectric), shorting-pin width W << lambda (usually <= (0.05-0.1)*lambda); pin inductance and open-end capacitance cancel at resonance; behaves like half a slot with a nearly omnidirectional pattern. | L ~ lambda/4 = c/(4*f*sqrt(er)) | f, er | printed IFA | calc | p.843-845 | high |
| BALANIS-478 | antenna | Worked IFA: RT/duroid 5870 (er = 2.33), h = 0.1524 cm, 1.8 GHz -> L = 2.73 cm, pin width W = 0.06*lambda = 0.655 cm. | as stated | - | Example 14.8, Fig 14.52-14.53 | sim | p.844 Ex.14.8 | high |
| BALANIS-479 | antenna | Multiband U-slot patch: each U-slot is about lambda/2 in total length at its band; keep slots separated from each other and from the patch edges to avoid coupling; first band from the patch itself. Two-band example: GSM 874-958 MHz (84 MHz, ~9%) and DCS 1,711-1,943 MHz (232 MHz, ~13%). | slot length ~ lambda/2 | band centers | handset multiband | sim | p.846-847 | high |
| BALANIS-480 | antenna | Dielectric resonator physics: dielectric-air reflection approaches +1 (PMC wall) for large er; resonators (energy storage) need er ~ 50 or greater; radiating DRAs use moderate er ~ 5-30 so energy leaks out. | Gamma = (sqrt(er) - 1)/(sqrt(er) + 1) | er | DR vs DRA | calc | p.847 eq.(14-100) | high |
| BALANIS-481 | antenna | DRA characteristics: efficient (no surface waves, radiate from all open faces); bandwidth typically ~10% (some geometries 50% or more; single digits when Q is very high); high power capability; heights as low as 0.05*lambda; usable ~1-60 GHz and above; low loss at mm-wave; feed by probe, microstrip, slot or CPW; probe position tunes the 50-ohm match. | BW ~ 10% typ ; h >= ~0.05 lambda | er, geometry | DRAs | review | p.848 | high |
| BALANIS-482 | antenna | Cavity (PMC-wall) model of DRAs is accurate for high er for resonant frequency and patterns, not necessarily for input impedance; refine with hybrid-mode formulas or full-wave. | n/a | - | DRA analysis | review | p.850 | high |
| BALANIS-483 | antenna | Rectangular DRA (a x b x c, c normal to ground) resonances; lowest mode: TMz101 for a > b > 2c and c > a > b; TMz011 for c > b > a. | f_TE/TM,mnp = [1/(2*pi*sqrt(mu_d*eps_d))]*sqrt((m*pi/a)^2 + (n*pi/b)^2 + [(2p-1)*pi/(2c)]^2) ; f_TM101 = [v0/(2*sqrt(er*mur))]*sqrt((1/a)^2 + (1/(2c))^2) ; f_TM011 = [v0/(2*sqrt(er*mur))]*sqrt((1/b)^2 + (1/(2c))^2) | a, b, c, er | cavity model | calc | p.850 eq.(14-101a)-(14-102b) | high |
| BALANIS-484 | antenna | Cylindrical DRA (radius a, height h) cavity-model resonances; lowest modes TEz010 and TMz110, the TMz110 being lowest. Bessel zeros chi_01 = 2.4049, chi_11 = 3.8318, chi_21 = 5.1357, chi_02 = 5.5201, chi_31 = 6.3802; chi'11 = 1.8412, chi'21 = 3.0542, chi'01 = 3.8318, chi'31 = 4.2012, 5.3175. | f_TE010 = [1/(2*pi*sqrt(mu_d*eps_d))]*sqrt((2.4049/a)^2 + (pi/(2h))^2) ; f_TM110 = [1/(2*pi*sqrt(mu_d*eps_d))]*sqrt((1.8412/a)^2 + (pi/(2h))^2) | a, h, er | cavity model | calc | p.851 eq.(14-103a)-(14-104b) | high |
| BALANIS-485 | antenna | Hemicylindrical DRA lowest mode: TEz010 for h/a < 2.031, TMz111 for h/a > 2.031. | f_TE010 = 2.4049/(2*pi*a*sqrt(mu_d*eps_d)) ; f_TM111 = [1/(2*pi*sqrt(mu_d*eps_d))]*sqrt((1.841/a)^2 + (pi/h)^2) | a, h, er | cavity model | calc | p.851-852 eq.(14-106a),(14-106b) | high |
| BALANIS-486 | antenna | Hemispherical DRA resonances from spherical-Bessel zeros (zeta11 = 4.493, zeta21 = 5.763, zeta31 = 6.988, zeta12 = 7.725, zeta41 = 8.183; zeta'11 = 2.744, zeta'21 = 3.870, zeta'31 = 4.973, zeta'41 = 6.062, zeta'12 = 6.117); lowest TM111 (degenerate). | f_TE = zeta_np/(2*pi*a*sqrt(mu_d*eps_d)) ; f_TM = zeta'_np/(2*pi*a*sqrt(mu_d*eps_d)) ; f_TE111 = 4.493/(...) ; f_TM111 = 2.744/(...) | a, er | cavity model | calc | p.852 eq.(14-107a)-(14-107d) | high |
| BALANIS-487 | antenna | Cylindrical DRA TE01d mode curve-fit resonance and radiation Q (z = a/h). | f_r = [v0/(2*pi*a)]*[2.327/sqrt(er + 1)]*[1 + 0.2123*z - 0.00898*z^2] (0.125 <= z <= 5) ; Q = 0.078192*er^1.27*[1 + 17.31/z - 21.57/z^2 + 10.86/z^3 - 1.98/z^4] (0.5 <= z <= 5; powers of h/a) | a, h, er | [121],[124]; validated vs Table 14.3 | calc | p.853 eq.(14-108a),(14-108b) | high |
| BALANIS-488 | antenna | Cylindrical DRA TM01d mode curve-fit (z = a/h). | f_r = [v0/(2*pi*a)]*[1/sqrt(er + 2)]*sqrt(3.83^2 + (pi*z/2)^2) ; Q = 0.008721*er^0.888413*exp(0.0397475*er)*[1 - (0.3 - 0.2*z)*((38 - er)/28)]*[9.498186*z + 2058.33*z^4.322261*exp(-3.50099*z)] (0.125 <= z <= 5) | a, h, er | printed coefficients truncated (0.00872, 0.888, 0.03975, 9.498, 4.3226, 3.501); full-precision values reproduce Table 14.3 | calc | p.853 eq.(14-109a),(14-109b) | medium |
| BALANIS-489 | antenna | Cylindrical DRA HE11d (broadside) mode curve-fit (z = a/h). | f_r = [v0/(2*pi*a)]*[6.324/sqrt(er + 2)]*[0.27 + 0.18*z + 0.005*z^2] (0.125 <= z <= 5) ; Q = 0.01007*er^1.3*z*{1 + 100*exp(-2.05*(0.5*z - 0.0125*z^2))} (0.5 <= z <= 5) | a, h, er | printed Q coefficient "0.01"; 0.01007 reproduces Table 14.3 (31.24) | calc | p.853 eq.(14-110a),(14-110b) | medium |
| BALANIS-490 | antenna | Hybrid-mode DRA formulas predict resonance within ~3% of measurement; Q within 10% except TM01d at er = 38 (35.7%). | abs(df_r) < 3% ; abs(dQ) < 10% (typ.) | - | Table 14.3 (er = 38, 79) | measure | p.854 Table 14.3 | high |
| BALANIS-491 | antenna | DRA mode patterns: HE11d ~ horizontal magnetic dipole (broadside, max along z for large h/a; a null forms along z for small h/a); TM01d ~ short vertical electric monopole (null at zenith); hemicylindrical TE01d ~ short horizontal magnetic dipole. | n/a | h/a | cylindrical/hemicylindrical DRA | sim | p.855-856 Figs 14.62-14.63 | high |
| BALANIS-492 | antenna | Cylindrical DRA design procedure: (1) Q from required BW and VSWR via (14-88a); (2) choose er inside the range for which the chosen mode's Q formula can hit that Q within its a/h window (TE01d, HE11d: 0.5 <= a/h <= 5; TM01d: 0.125 <= a/h <= 5), else the spec is infeasible; (3) solve f_r and Q equations simultaneously for a and h. | Q = (VSWR-1)/(BW*sqrt(VSWR)) | mode, BW, VSWR, f_r | DRA Analysis Design procedure | calc | p.854-855 | high |
| BALANIS-493 | antenna | Worked DRA analysis (a = 0.5 cm, h = 0.3 cm, probe l = 0.38 cm, d = 0.05 cm, rho0 = 0.36 cm, er = 8.9): simulated resonance 10.69 GHz with -10 dB BW 7.02%; cavity model TE010 11.38 / TM110 10.24 GHz (er = 89: 3.60/3.24 GHz); hybrid TE01d 9.385, TM01d 13.419 GHz (er = 89: 3.113, 4.644); Q: TE01d 7.17, TM01d 6.325, HE11d 5.8864 (er = 89: 133.512, 1,071.95, 117.45). | as stated | - | Example 14.9 (printed HE11d f_r = 8.564 GHz conflicts with eq.14-110a, which gives ~10.68 GHz = simulated dip) | sim | p.856-858 Ex.14.9 | high |
| BALANIS-494 | antenna | Worked DRA design (TE01d, BW 2.887%, VSWR 3, 10 GHz): Q = 40, feasible 34 < er < 48.65, chosen er = 38 -> a = 0.2653 cm, h = 0.1020 cm (re-analysis gives f_r = 10 GHz, Q = 40). | as stated | - | Example 14.10 | calc | p.858 Ex.14.10 | high |

### Ch 15 — Reflector antennas

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BALANIS-520 | antenna | 90-deg corner reflector is a retro-reflector (returns radar energy back toward the source) — avoid sharp corners on low-observable platforms; corner reflectors are common TV receiving antennas. | included angle 90 deg | - | radar targets/signatures | review | p.876 | high |
| BALANIS-521 | antenna | Corner-reflector proportions: aperture lambda < Da < 2*lambda; side length l ~ 2*s for 90 deg (longer for smaller angles); feed-to-vertex lambda/3 < s < 2*lambda/3; height 1.2-1.5 x the feed length; wire-grid sides with spacing g <= lambda/10 (wires parallel to the dipole reflect like solid sheet). Too small s -> radiation resistance approaches loss resistance (inefficient); too large -> multiple lobes. Longer sides raise bandwidth and radiation resistance, not beamwidth/directivity. Cylindrical or biconical feed dipoles widen bandwidth. | lambda < Da < 2 lambda ; lambda/3 < s < 2 lambda/3 ; l ~ 2s ; h = 1.2-1.5 x feed length ; g <= lambda/10 | Da, s, l, h, g | dipole-fed corner reflector | calc | p.876-877 | high |
| BALANIS-522 | antenna | 90-deg corner reflector array factor (images); single main lobe for small s, multiple lobes for s > 0.7*lambda, on-axis null at s = lambda; on-axis abs(E/E0) first peaks at s = 0.5*lambda with value 4 and is periodic in s with period lambda. | AF = 2*[cos(k s sin th cos phi) - cos(k s sin th sin phi)] ; number of images N = 360/alpha - 1 = 2n - 1 | s, lambda | infinite plates | calc | p.878-881 eq.(15-5), Fig 15.6 | high |
| BALANIS-523 | antenna | Other corner angles: multiple lobes appear at s ~ 0.95*lambda (60 deg), 1.2*lambda (45 deg), 2.5*lambda (30 deg); maximum abs(E/E0) ~5.2, 8, 9; first on-axis peak at s ~ 0.65, 0.85, 1.20*lambda; 60-deg response periodic with 2*lambda, 45/30-deg only pseudo-periodic (~16.69*lambda, ~30*lambda). | as stated | alpha, s | corner reflectors alpha = 180/n | calc | p.881-884 | high |
| BALANIS-524 | antenna | Reflector configuration trade-offs: front-fed needs long feed lines (loss/noise) or heavy equipment at the focus (blockage); Cassegrain puts equipment behind the dish and achieves 65-80% efficiency, ~10% better than front-fed; offset reflectors cut blockage and VSWR and allow larger f/d, but LP feeds then create cross-pol and CP feeds squint the beam. | eta_Cass = 65-80% | - | reflector systems | review | p.884-886 | high |
| BALANIS-525 | antenna | Parabolic cylinder vs paraboloid: amplitude taper ~1/rho vs 1/r^2, line vs point focus, parabolic cylinder with feed polarized along its axis produces no cross-pol (paraboloid does); cylinders are simpler but block more. | n/a | - | reflector selection | review | p.887 | high |
| BALANIS-526 | antenna | Paraboloid geometry and f/d vs half subtended angle theta0. | r' = 2f/(1 + cos th') = f*sec^2(th'/2) ; x'^2 + y'^2 = 4f(f - z') ; theta0 = atan[(0.5*(f/d))/((f/d)^2 - 1/16)] ; f/d = 0.25*cot(theta0/2) | f, d | paraboloidal reflector | calc | p.887-890 eq.(15-14a)-(15-25) | high |
| BALANIS-527 | antenna | Physical-optics current Js = 2 n x H_i is valid when reflector transverse dimensions, surface radius of curvature and incident-wave curvature radius are all large vs lambda; aperture- and current-distribution methods agree near the main beam; rim diffraction (GTD) is needed for far sidelobes. | Js = 2 n x Hi | - | reflector analysis | review | p.890-892 | high |
| BALANIS-528 | antenna | Paraboloid cross-polarization: an LP feed produces cross-pol off the principal planes (symmetric lobes 180 deg out of phase), vanishing on axis; a Huygens source (crossed electric and magnetic dipoles with moment ratio sqrt(mu/eps)) induces parallel surface currents and cancels cross-pol. | p_e/m ratio = sqrt(mu/eps) | feed | front-fed paraboloid | sim | p.896-897 | high |
| BALANIS-529 | antenna | Paraboloid directivity and aperture efficiency from the feed power pattern Gf(th') (symmetric, zero beyond 90 deg); all paraboloids with the same f/d have the same aperture efficiency for a given feed. | D0 = (pi*d/lambda)^2*eps_ap ; eps_ap = cot^2(theta0/2)*abs(Int_0^theta0 sqrt(Gf(th'))*tan(th'/2) dth')^2 | Gf, theta0, d, lambda | front-fed | calc | p.901-902 eq.(15-54),(15-55) | high |
| BALANIS-530 | antenna | cos^n feed family: Gf = 2(n+1)*cos^n(th') for th' <= 90 deg; for each n there is one optimum f/d; maximum aperture efficiency ~82-83% for all n; more directive feeds (larger n) need smaller subtended angles (larger f/d). | G0(n) = 2*(n+1) ; eps_ap,max ~ 0.82-0.83 | n, theta0 | Silver feed model | calc | p.902-903 eq.(15-56)-(15-59d) | high |
| BALANIS-531 | antenna | Aperture efficiency factors; spillover and taper dominate for symmetric, phase-aligned, cross-pol-free, unblocked, smooth reflectors; feed-line attenuation reduces gain further. | eps_ap = eps_s*eps_t*eps_p*eps_x*eps_b*eps_r ; eps_s = Int_0^theta0 Gf sin th' dth' / Int_0^pi Gf sin th' dth' ; eps_t = 2*cot^2(theta0/2)*abs(Int_0^theta0 sqrt(Gf) tan(th'/2) dth')^2 / Int_0^theta0 Gf sin th' dth' | Gf, theta0 | symmetric feeds | calc | p.903-905 eq.(15-60)-(15-62a) | high |
| BALANIS-532 | antenna | Uniform aperture illumination requires compensating the path taper: a point feed at the focus gives power taper (f/r')^2 = cos^4(th'/2), so the ideal feed pattern is Gf = G0*sec^4(th'/2) within theta0 (zero outside) with G0 = cot^2(theta0/2), giving eps_ap = 1 (impractical ideal). | Gf = cot^2(theta0/2)*sec^4(th'/2), th' <= theta0 | theta0 | ideal feed | calc | p.905-908 Ex.15.1-15.2, eq.(15-63) | high |
| BALANIS-533 | antenna | Feed edge taper for maximum aperture efficiency: cos^n feeds are 8 dB down at the rim for n = 2 and 8-10.5 dB for n = 2-10; use 9-10 dB feed edge taper for practical feeds; including the space (path) loss the rim illumination is ~11 dB below the vertex. | feed edge taper 9-10 dB ; total edge illumination ~ -11 dB | n, f/d | front-fed paraboloid | calc | p.908-909 Fig 15.23, Table 15.1 | high |
| BALANIS-534 | antenna | Practical reflector aperture efficiencies are 65-80%; 8x8-lambda square corrugated-horn feeds give maximum 74-79%, and the product of taper and spillover efficiencies approximates the total. | eps_ap(practical) = 0.65-0.80 | - | Figs 15.24-15.25 | calc | p.909-910 | high |
| BALANIS-535 | antenna | Worked reflector (d = 10 m, f/d = 0.5, 3 GHz, Gf = 6*cos^2 th'): theta0 = 53.13 deg, eps_ap = 0.75, D = 74,022.03 (48.69 dB), eps_s = 0.784, eps_t = 0.9566 (product 0.75); with maximum phase error pi/8: D >= 0.8517*D0 (-0.69 dB) = 48.0 dB. | as stated | - | Example 15.3 | calc | p.911-913 Ex.15.3 | high |
| BALANIS-536 | antenna | Aperture phase error bound (small errors; no need to know exact distributions): with maximum deviation m (rad) from the average phase. | D/D0 >= (1 - m^2/2)^2 ; dD/D0 <= m^2*(1 - m^2/4) | m (rad) | defocus, surface error, non-spherical feed fronts | calc | p.910-911 eq.(15-64)-(15-66) | high |
| BALANIS-537 | antenna | Place the feed phase center at the focal point (defocus -> phase error -> gain loss); horn phase centers lie between aperture and apex. | n/a | feed position | reflector feeds | measure | p.910-911 | high |
| BALANIS-538 | antenna | Ruze surface-roughness limit: for rms surface deviation sigma (Gaussian, correlation interval >> lambda) directivity peaks at lambda_max = 4*pi*sigma. | D = (pi*d/lambda)^2*eps_ap*exp(-(4*pi*sigma/lambda)^2) ; lambda_max = 4*pi*sigma ; Dmax = 10^(2q)*eps_ap*e^-1/16 ; Dmax(dB) = 20q - 16.38 + 10*log10(eps_ap), d/sigma = 10^q | d, sigma, lambda, eps_ap | reflectors | calc | p.913 eq.(15-67)-(15-71) | high |
| BALANIS-539 | antenna | Focal-region fields for microwave reflectors (f/d 0.25-0.5) are hybrid TE/TM modes (the scalar Airy [2J1(u)/u]^2 picture is valid only for large optical f/d); lambda/4-deep annular slots make a hollow pipe support both — the basis of hybrid-mode/corrugated feeds; "scalar" horns have >= 180 deg aperture phase error. | slot depth lambda/4 | f/d | feed design | review | p.913-914 | high |
| BALANIS-540 | antenna | Cassegrain benefits: convenient feed location, less spillover and minor-lobe radiation, equivalent focal length much larger than physical, beam scanning/broadening by moving a surface; the subreflector must be at least a few wavelengths across, and its blockage makes Cassegrains attractive mainly for gains of 40 dB or more. | G >= 40 dB typical ; D_sub >= few lambda | - | dual reflectors | review | p.915-916 | high |
| BALANIS-541 | antenna | Shaped dual reflectors (high magnification): subreflector curvature mainly controls aperture amplitude, main-reflector curvature mainly controls phase — reshape each accordingly (e.g. csc^4(th/2) subreflector field -> near-uniform amplitude, plane phase). | n/a | - | shaped Cassegrain/Gregorian | review | p.916-917 Fig 15.29 | high |
| BALANIS-542 | antenna | Cassegrain virtual-feed concept (real feed + convex subreflector = broader-beam virtual feed at the main focus) and equivalent-parabola concept (focal length = vertex-to-real-focus distance) give quick performance estimates, accurate for subreflectors a few wavelengths across; Gregorian (concave ellipse subreflector) needs a shorter main focal length than a Cassegrain of the same size and feed beamwidth. | n/a | - | dual reflectors | review | p.917-920 | high |
| BALANIS-543 | antenna | Spherical reflector: wide-angle scanning by moving the feed but spherical aberration (line focus from paraxial focus R/2 to the vertex); Ashmead-Pippard point-feed placement gives maximum path error ~d^4/(2000*f0^3) (within lambda/8 of a paraboloid) at the cost of large f/d; Li optimum focal length minimizes total phase error. | Dmax ~ d^4/(2000*f0^3) ; f_op = 0.25*(R + sqrt(R^2 - a^2)) (R = 2a -> 0.4665R, total error 0.02643*(R/lambda) rad) ; (a/R)^4_max = 14.7*(Delta/lambda)_total/(R/lambda) | R, a, lambda, allowed error | spherical reflectors (Arecibo) | calc | p.920-922 eq.(15-72)-(15-74) | high |
| BALANIS-544 | antenna | Worked spherical reflector: 10-ft diameter (R = 5 ft), 11.2 GHz (lambda = 0.08788 ft), allowed total phase error lambda/16 -> (a/R)^4 = 0.01615, a = 1.78 ft; line-source or multi-element feeds along the axis near the paraxial focus reduce aberration. | as stated | - | Example 15.4 | calc | p.922 Ex.15.4 | high |
| BALANIS-545 | antenna | Worked front-fed reflector: 35 GHz, f/d ~ 0.82 (f = 20.48 cm, d = 24.99 cm), dual-mode conical horn feed with identical E/H patterns -> identical E/H reflector patterns with no principal-plane cross-pol; aperture-plane field within 0-15 dB. | as stated | - | Figs 15.14-15.15 | sim | p.894-896 | high |

### Ch 16 — Smart antennas

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BALANIS-560 | rf | Cellular capacity techniques: cell splitting shrinks R at constant D/R (costs base stations and handoffs); 3 x 120-deg sectoring cuts cochannel interferers from six to two (improves S/I and reuse) but adds antennas and lowers trunking efficiency; smart antennas extend sectoring with multiple/adaptive beams. | sectors: 3 x 120 deg ; interferers 6 -> 2 | - | cellular base stations | review | p.933-936 | high |
| BALANIS-561 | rf | Switched-beam vs adaptive arrays: switched beams choose among fixed patterns (user may be off beam peak, an interferer near beam center is enhanced); adaptive arrays steer maxima to the SOI and nulls to SNOIs in real time but need a full RF chain and real-time calibration per element and heavy DSP; SDMA runs N parallel beamformers for intracell frequency reuse. | n/a | - | smart-antenna architecture | review | p.936-939, p.943 | high |
| BALANIS-562 | rf | Dense mobile systems are interference-limited (SIR << SNR); smart antennas raise SIR (signal up, interference down), extend range (base stations farther apart), add link security (eavesdropper must be at the same bearing) and enable location services. | SIR << SNR (interference-limited) | - | system benefits | review | p.942-943 | high |
| BALANIS-563 | antenna | Array size trade-off for adaptive systems: larger arrays resolve SOIs/SNOIs better but cost more and slow adaptive-algorithm convergence (consuming bandwidth); planar arrays are needed for 3-D (theta, phi) scanning; separable planar excitations need only M + N weights vs M x N. | weights: M + N (separable) vs M*N | M, N | smart-antenna arrays | review | p.943-946 | high |
| BALANIS-564 | antenna | Planar-array DOA time delay of element (m, n) relative to the origin element. | tau_mn = (m*dx*sin(th)*cos(phi) + n*dy*sin(th)*sin(phi))/v0 ; two elements: cos(theta) = v0*dt/d | dx, dy, theta, phi, v0 | rectangular grid array | calc | p.947-950 eq.(16-9), Ex.16.1 | high |
| BALANIS-565 | rf | DOA algorithm selection: delay-and-sum = poor resolution; Capon improves resolution but fails for SNOIs correlated with the SOI; MUSIC needs precise calibration, fails for highly correlated (multipath) signals unless spatially smoothed, and is compute-heavy; ESPRIT needs less computation and storage, no exhaustive search and no array calibration (algorithm of choice); maximum likelihood beats subspace methods at low SNR/correlated signals but is compute-heavy; integrated ILSP-CMA + subspace resolves up to 2M^2/3 DOAs vs M for conventional DOA. | DOAs resolvable: M (conventional) ; 2M^2/3 (ILSP-CMA integrated) | M elements | smart-antenna DSP | review | p.948-949 | high |
| BALANIS-566 | rf | Two-element null-steering weights (lambda/2 spacing, SOI at 0 deg, SNOI at 30 deg): w1 = 1/2 - j/2, w2 = 1/2 + j/2 (unity SOI response, zero SNOI). | as stated | - | Example 16.2 | calc | p.950-952 Ex.16.2 | high |
| BALANIS-567 | rf | Mutual coupling shifts and fills pattern nulls and biases DOA and beamforming unless compensated, worse at smaller spacing; example with c11 = c22 = 2.37 + j0.340, c12 = c21 = -0.130 - j0.0517: the intended null at 30 deg moved to 32.5 deg at only ~-35 dB. | coupling-corrected weights w~ = f(c_ij, w) | c_ij | adaptive arrays | sim | p.953-955 Ex.16.3 | high |
| BALANIS-568 | rf | Optimum (MMSE/Wiener) weights and the LMS iteration; LMS converges only for 0 < mu < 1/lambda_max (largest eigenvalue of Rxx) and converges slowly in noise. | w_opt = Rxx^-1 * r_xd ; w_{k+1} = w_k + 2*mu*x_k*(d_k - x_k^T*w_k) ; 0 < mu < 1/lambda_max | Rxx, r_xd, mu | adaptive beamforming | calc | p.955-957 eq.(16-14),(16-17),(16-18) | high |
| BALANIS-569 | rf | LMS beamforming anchors (8-element, 0.5*lambda, mu = 0.01): SOI only at 20 deg -> uniform amplitudes and -61.56 deg progressive phase after 55 iterations (same as classical scanning); SOI 20 deg + SNOI 45 deg after 81 iterations -> symmetric amplitudes 1.0000, 0.8982, 1.1384, 1.3760, 1.3760, 1.1384, 0.8982, 1.0000 (phases -11.62 ... -419.37 deg). | as stated | - | Examples 16.4-16.5, Tables 16.1-16.2 | sim | p.957-959 | high |
| BALANIS-570 | antenna | Smart-antenna element spacing: >= lambda/2 for (near) independent fading across elements in rich scattering (space diversity), < lambda to avoid grating lobes, <= lambda/2 (Nyquist) to avoid aliasing and misplaced nulls -> use lambda/2. | d = lambda/2 | lambda | adaptive arrays | calc | p.967-968, p.973 | high |
| BALANIS-571 | antenna | 20-GHz silicon patch (er = 11.7, tan d = 0.04, h = 0.300 mm, 50 ohm): cavity-model W = 2.976 mm, L = 2.129 mm, feed (y0, x0) = (1.488, 1.256) mm vs full-wave optimized W = 2.247 mm, L = 2.062 mm, (1.164, 0.794) mm; resonance at 20 GHz with -21.5 dB return loss, -3 dB bandwidth 0.74 GHz, -10 dB bandwidth 0.25 GHz; cavity model misses probe location and assumes truncated substrate (E-plane peak at 5 deg and null at 90 deg in full-wave). | as stated | - | Fig 16.37-16.39 | sim | p.965-967 | high |
| BALANIS-572 | matching | Use a stricter-than -10 dB impedance-bandwidth criterion when the antenna drives a power amplifier: PAs reduce output or become unstable at high VSWR. | S11 spec tighter than -10 dB (PA-driven) | S11 | transmit antennas on PAs | measure | p.965-966 | high |
| BALANIS-573 | rf | Network results (55-node MANET, 1,000 x 600 m, four 90-deg planar subarrays per node, 1,024-bit payloads): 8x8 arrays beat 4x4 in throughput; Chebyshev (-26 dB) patterns slightly beat uniform; an LMS-adapted pattern put 48 dB less gain toward the SNOI than the -26 dB Chebyshev pattern and gave higher throughput. | as stated | - | OPNET simulations, 802.11-based RTS/CTS/training MAC | sim | p.961-971 | high |
| BALANIS-574 | rf | Beamforming/training overhead limit: when the training sequence exceeds ~20% of the payload, network throughput and delay degrade to those of omnidirectional antennas. | training <= ~20% of payload (6-10% studied) | training length | smart-antenna MANET MAC | sim | p.970-972 | high |
| BALANIS-575 | rf | Link-level results (8x8 LMS array, SOI 0 deg, equal-power SNOI 45 deg, 60 training + 940 data symbols = 6% overhead, 100 Hz symbols): one interferer suppressed without loss on AWGN; 8-state TCM QPSK ~1.5 dB better than uncoded BPSK at BER 1e-5; Rayleigh fading fm = 0.1 Hz (fmT = 0.001) costs ~4 dB with one interferer and fm = 0.2 Hz another ~4 dB at BER 1e-4 with an error floor above ~18 dB SNR — LMS convergence must track the fading rate. | as stated | fm*T | BER studies | sim | p.972-975 | high |
| BALANIS-576 | antenna | Uniform circular arrays have no edge elements, so azimuthal electronic scanning keeps the beam shape. | n/a | - | UCA/UPCA | review | p.975-976 | high |

### Ch 17 — Antenna measurements (priority)

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BALANIS-600 | test | Far-field range length: separate source and test antenna by at least 2D^2/lambda (inner boundary of the far field); at exactly 2D^2/lambda the incident phase error at the aperture edges is ~22.5 deg (pi/8). Reflections from ground and nearby objects are the other main illumination error. | R >= 2*D^2/lambda ; phase error = pi*D^2/(4*lambda*R) = 22.5 deg at R = 2D^2/lambda | D largest aperture dimension (m), lambda (m), R (m) | pattern and gain measurements | calc | p.981-982 Fig 17.1 | high |
| BALANIS-601 | test | Measure reciprocal antennas in the receiving mode (patterns, gain identical to transmit); the ideal illumination is a uniform plane wave. | n/a | - | reciprocal antennas | review | p.981, p.1001 | high |
| BALANIS-602 | test | Use IEEE Std 149-1979 (Standard Test Procedures for Antennas) as the governing procedure reference for pattern, gain, directivity, efficiency, impedance, current and polarization measurements. | n/a | - | antenna test plans | review | p.982 | high |
| BALANIS-603 | test | Ground-reflection ranges create a constructive-interference "quiet zone" from direct plus specular ground ray; adjust transmit-antenna height (receive height fixed) for a small, symmetric amplitude taper; used for moderately broad antennas from UHF up to ~16 GHz. | UHF-16 GHz | h_t, h_r, R | outdoor reflection range | measure | p.983 | high |
| BALANIS-604 | test | Elevated-range reflection control: choose source directivity/sidelobe level, clear the line of sight, redirect or absorb energy reflected from the range surface and obstacles, and use signal processing (modulation tagging, short pulses); locate specular points from terrain profiles on irregular ground. | n/a | - | outdoor elevated ranges | inspect | p.983-984 | high |
| BALANIS-605 | test | Slant range: test antenna on a nonconducting tower, source near the ground with its free-space pattern maximum aimed at the test antenna center and its first null toward the ground specular point; needs less land than an elevated range (example geometry 30 m tower at 45 deg). | first null -> specular point | geometry | slant range | inspect | p.984 Fig 17.3(b) | high |
| BALANIS-606 | test | Anechoic chamber absorbers: -40 dB reflection at normal incidence is achievable down to ~100 MHz; absorber thickness must grow as frequency falls; an absorber meeting the low-frequency spec performs better at higher frequencies; significant specular reflections remain at large incidence angles. | Gamma_absorber <= -40 dB (normal) ; f >= ~100 MHz | f_min, absorber depth | rectangular/tapered chambers | measure | p.985 | high |
| BALANIS-607 | test | Tapered chamber operation: at the low end place the source near the apex so wall reflections occur near the source (small phase difference, smooth taper); at higher frequencies use a high-gain source and move it toward the end of the taper (behaves like a rectangular chamber). | n/a | f | tapered anechoic chamber | review | p.985-986 | high |
| BALANIS-608 | test | Compact antenna test range (CATR) generates near-plane waves in ~10-20 m instead of 2D^2/lambda; quiet zone is typically ~50-60% of the main reflector dimensions. | L_range ~ 10-20 m ; QZ ~ 0.5-0.6 x reflector size | reflector size | CATR | calc | p.986-987 | high |
| BALANIS-609 | test | CATR quiet-zone acceptance for most applications: phase deviation < 10 deg, peak-to-peak amplitude ripple < 1 dB, amplitude taper < 1 dB over the specified test zone (tighter for low-sidelobe antennas and low-observable targets). | dphi < 10 deg ; ripple < 1 dB p-p ; taper < 1 dB | QZ probe scan | CATR quiet zone | measure | p.987 | high |
| BALANIS-610 | test | CATR amplitude taper sources: the feed pattern maps directly into the quiet zone (feed 3-dB beamwidth ~60% of the angle subtended by the reflector edges -> ~3 dB taper; low-gain feeds are designed to add only a few tenths of a dB); 1/r^2 space attenuation adds an asymmetric taper in the feed-offset plane. | feed HPBW ~ 0.6*subtended angle -> 3 dB taper | feed pattern | CATR feed design | calc | p.987 | high |
| BALANIS-611 | test | CATR ripple comes mainly from reflector edge diffraction; mitigate with serrated edges (curved serrations help at high frequency), blended rolled edges, tapered illumination (array feed with nulls at the edges) or resistive/lossy edge terminations; offset feed eliminates blockage; long focal length reduces direct radiation, diffraction and depolarization. | n/a | edge treatment | CATR | inspect | p.987-989 | high |
| BALANIS-612 | test | CATR frequency limits: low-frequency limit when the reflector is ~25-30 wavelengths across (ripple grows); surface must deviate < ~0.007*lambda from the true paraboloid at the highest frequency; dual-reflector systems need twice the surface precision; typical CATRs operate 1-100 GHz. | D_refl >= 25-30*lambda_max ; surface error < 0.007*lambda_min (single) ; < 0.0035*lambda_min (dual, derived) | D_refl, surface error, f range | CATR design | calc | p.989 | high |
| BALANIS-613 | test | CATR types: single offset paraboloid ("virtual vertex") has fewest edges and low feed spillover but costly doubly curved surface and more depolarization (low f/d); dual parabolic-cylinder gives low cross-pol (long focal length), feed spillover controlled by range gating; dual shaped (Cassegrain-like) gives very high illumination efficiency (less clutter, more sensitivity); single parabolic-cylinder (SPCR) collimates in one plane. | n/a | - | range selection | review | p.989-991 | high |
| BALANIS-614 | test | Single-plane collimating range (SPCR): quiet zone ~50-60% of reflector vertically and ~100% horizontally; cost ~60% of a conventional CATR; needs only a 1-D NF/FF transform (one-to-one per azimuth cut) but illuminates more of the chamber (clutter) and loses some sensitivity. | QZ_h ~ 100% ; cost ~60% of CATR | - | ASU EMAC SPCR | review | p.991-992 | high |
| BALANIS-615 | test | NF/FF scan surface selection: planar for high-gain antennas and planar phased arrays with low back lobes (least computation, antenna stationary, limited angular span); cylindrical for fan beams/vertical dipoles (often least expensive equipment); spherical for low-gain and omnidirectional antennas (complete pattern; most expensive computation and positioning). | n/a | antenna type | near-field ranges | review | p.993-995 | high |
| BALANIS-616 | test | Planar near-field sampling rules: grid spacing <= lambda/2 (Nyquist), probe plane >= 2-3 wavelengths from the antenna (out of the reactive near field), extend the scan until edge levels are ~45 dB below the peak, measure both tangential polarizations, apply probe compensation; probe must not be circularly polarized nor have nulls over the angular region of interest. | dx = dy <= lambda/2 ; z0 >= 2-3*lambda ; edge <= -45 dB ; M = a/dx + 1, N = b/dy + 1 | scan size a x b, lambda | planar NF/FF | calc | p.993-998 eq.(17-10),(17-11) | high |
| BALANIS-617 | test | Cylindrical and spherical near-field sample spacing (a = radius of smallest enclosing cylinder/sphere). | cylindrical: dphi = lambda/(2*(a+lambda)), dz = lambda/2 ; spherical: dtheta = dphi = lambda/(2*(a+lambda)) (rad) | a, lambda | NF scanning | calc | p.994-995 eq.(17-1)-(17-4) | high |
| BALANIS-618 | test | Planar NF/FF transform via FFT costs time proportional to (ka)^2*log2(ka) (a = radius of smallest inscribing circle); sampling finer than lambda/2 adds no resolution (only evanescent spectrum); zero-padding the near-field data increases far-field pattern resolution. | T ~ (ka)^2 log2(ka) | a, lambda | planar NF/FF | calc | p.994, p.998 | high |
| BALANIS-619 | test | Planar NF/FF procedure: (1) measure Ex, Ey on the plane; (2) compute plane-wave spectrum fx, fy by 2-D Fourier transform; (3) far field E_theta ~ j*k*exp(-jkr)/(2*pi*r)*(fx cos phi + fy sin phi), E_phi ~ j*k*exp(-jkr)/(2*pi*r)*cos(theta)*(-fx sin phi + fy cos phi). | see formula | near-field samples | planar NF/FF | sim | p.996-997 eq.(17-7)-(17-9b) | high |
| BALANIS-620 | test | Near-field measurements match far-field ranges (4-ft reflector, ~30 dB gain, sum and difference patterns) and can pinpoint causes of pattern defects (e.g. defective array elements). | n/a | - | validation/diagnostics | measure | p.999-1000 | high |
| BALANIS-621 | test | Pattern documentation: at least the two orthogonal principal (E- and H-plane) cuts; elevation (great-circle) cuts at fixed phi, azimuth (conical) cuts at fixed theta; recorder dynamic range 0-60 dB, with 40 dB usually adequate to resolve the main and minor lobes; polar plots preferred for visualization. | dynamic range >= 40 dB | - | pattern measurements | measure | p.1000-1002 | high |
| BALANIS-622 | test | Range source antennas: log-periodic below 1 GHz, parabolas with broadband feeds above 400 MHz, large horns; source must allow polarization control (polarization positioner or crossed LPDA for CP); RF source needs frequency control, stability, spectral purity, adequate power and modulation. | LPDA < 1 GHz ; dish > 400 MHz | f | range instrumentation (five subsystems: source, receiver, positioner, recorder, data processing) | inspect | p.1001-1002 | high |
| BALANIS-623 | test | Measure in situ (e.g. airborne source flown around the test antenna in its far field) when moving the antenna to a range would change its operating environment; continuous (not point-by-point) recording preferred. | n/a | - | installed antennas | measure | p.1003 | high |
| BALANIS-624 | test | Phase patterns need a reference: couple a reference from the transmit line at short range, or use a fixed reference antenna receiving simultaneously at long range, with a dual-channel (phase-locked heterodyne) receiver. | n/a | - | phase-pattern measurement | measure | p.1003 | high |
| BALANIS-625 | test | Gain-measurement venue by frequency: free-space ranges above 1 GHz; ground-reflection ranges 0.1-1 GHz (or scale models with efficiency measured separately, G = D*e); below 0.1 GHz measure in situ; below 1 MHz measure ground-wave field strength instead of gain. | >1 GHz free space ; 0.1-1 GHz ground reflection ; <0.1 GHz in situ ; <1 MHz field strength | f | gain measurements | review | p.1003-1005 | high |
| BALANIS-626 | test | Gain standards: resonant lambda/2 dipole (~2.1 dB; very pure polarization but broad pattern, sensitive to environment) and pyramidal horn (12-25 dB; slightly elliptical, axial ratio ~40 dB to infinite; directive, less affected by environment). | G_dipole ~ 2.1 dB ; G_horn 12-25 dB | - | gain-transfer standards | review | p.1006 | high |
| BALANIS-627 | test | Two-antenna gain method (Friis, polarization-matched, boresight-aligned, far-field separation); for identical antennas each gain is half the sum. | (G0t)dB + (G0r)dB = 20*log10(4*pi*R/lambda) + 10*log10(Pr/Pt) ; identical: G = 0.5*[20 log10(4 pi R/lambda) + 10 log10(Pr/Pt)] | R (m), lambda (m), Pr/Pt | realized-gain calibration | calc | p.1006 eq.(17-14),(17-15) | high |
| BALANIS-628 | test | Three-antenna gain method: measure all three pairs and solve the three simultaneous dB equations for Ga, Gb, Gc (no prior gain knowledge). | Ga + Gb = 20 log10(4 pi R/lambda) + 10 log10(Prb/Pta) ; Ga + Gc = ... + 10 log10(Prc/Pta) ; Gb + Gc = ... + 10 log10(Prc/Ptb) | R, lambda, three power ratios | absolute gain | calc | p.1007-1008 eq.(17-16a)-(17-16c) | high |
| BALANIS-629 | test | Gain-measurement error controls: frequency-stable system, far-field separation (>= 2D^2/lambda), boresight alignment, impedance and polarization matching (correct with measured complex reflection coefficients and polarizations), minimal proximity/multipath (absorbers); cyclic gain variation vs separation indicates antenna-to-antenna multiple reflections. | R >= 2D^2/lambda | - | two/three-antenna methods | measure | p.1008 | high |
| BALANIS-630 | test | Extrapolation (three-antenna) method rigorously removes proximity/multipath errors; yields gains and polarizations of all three if none is CP, only the CP antenna's if exactly one is CP, and fails if two or more are CP; gains need amplitude only, polarization needs amplitude and phase. | CP antennas <= 1 | - | NIST-style gain/polarization calibration | measure | p.1008 | high |
| BALANIS-631 | test | Ground-reflection-range gain method (below ~1 GHz, moderately broad-beam linear antennas): mount linear antennas horizontally (smoother earth reflection for horizontal polarization), exclude CP/EP antennas, keep h_r << R0, set transmit height so the receive antenna sits at the first field maximum nearest the ground, then repeat at a field minimum to extract the range factor r. | (Ga)dB + (Gb)dB = 20 log10(4 pi R_D/lambda) + 10 log10(Pr/Pt) - 20 log10(sqrt(DA*DB) + r*R_D/R_R) | R_D, R_R, DA, DB, Pr/Pt, r from (17-18) | Hemming & Heaton | measure | p.1008-1009 eq.(17-17),(17-18) | high |
| BALANIS-632 | test | Gain-transfer (comparison) method: same geometry and input power, swap test and standard antennas; mount both back-to-back on an azimuth positioner (precise 180 deg swap) through a common switch; least sensitive to proximity/multipath when test and standard are similar. | (GT)dB = (GS)dB + 10*log10(PT/PS) | PT, PS (matched loads), GS | most common gain method | calc | p.1009-1010 eq.(17-19) | high |
| BALANIS-633 | test | Gain of CP/EP antennas with linear standards: measure partial gains with the standard vertical and then horizontal (rotate 90 deg) and sum powers; requires good linear polarization purity of source and standard. | (GT)dB = 10*log10(GTV + GTH) | GTV, GTH (linear power gains) | CP antennas | calc | p.1010 eq.(17-20) | high |
| BALANIS-634 | test | Free-space/ground-reflection/extrapolation gain techniques have a ~50 MHz low-frequency limit; below 50 MHz ground dominates and full-scale in-situ measurement is required. | f >= 50 MHz | f | HF antennas | review | p.1010 | high |
| BALANIS-635 | test | Directivity from patterns: rough estimate from E/H HPBW (Kraus or Tai-Pereira) when there is one major lobe and negligible minor lobes; better: integrate the measured pattern numerically (sample spacing must shrink as directivity rises); with two polarizations sum partial directivities. | D0 = D_theta + D_phi ; D_theta = 4*pi*U_theta/(Prad_theta + Prad_phi) ; D_phi = 4*pi*U_phi/(Prad_theta + Prad_phi) | pattern data | directivity measurement | calc | p.1010-1011 eq.(17-21) | high |
| BALANIS-636 | test | Cross-polarization of good antenna designs is usually below -40 dB relative to the primary polarization. | X-pol <= -40 dB | pattern (co/cross) | linearly polarized designs | measure | p.1012 | high |
| BALANIS-637 | test | Radiation efficiency from measured gain and directivity (same direction, max); for small antennas modeled as series R networks, R_loss = R_in - R_rad (not valid for lossy-dielectric-coated antennas or antennas over lossy ground). Mismatch and polarization do not enter radiation efficiency. | e = G/D ; R_loss = R_in - R_rad | G, D, R_in, R_rad | efficiency measurement | calc | p.1012 eq.(17-22) | high |
| BALANIS-638 | matching | Power lost to mismatch between antenna and connected circuit (non-conjugate match). | P_lost/P_avail = abs((Z_ant - Z_cct*)/(Z_ant + Z_cct))^2 | Z_ant, Z_cct (ohm) | antenna-circuit interface | calc | p.1013 eq.(17-23) | high |
| BALANIS-639 | matching | Reflected power vs VSWR at the antenna terminals. | P_refl/P_inc = abs(Gamma)^2 = abs(Z_ant - Zc)^2/abs(Z_ant + Zc)^2 = ((VSWR-1)/(VSWR+1))^2 | Z_ant, Zc or VSWR | line-fed antenna | calc | p.1013 eq.(17-24) | high |
| BALANIS-640 | test | Slotted-line impedance: abs(Gamma) from VSWR, phase from the n-th voltage minimum (use minima, first minimum unless too close to the terminals), then Z_ant. | psi = (4*pi/lambda_g)*x_n +/- (2n-1)*pi ; Z_ant = Zc*(1+Gamma)/(1-Gamma) | VSWR, x_n, lambda_g (twice the min-to-min spacing), Zc | slotted line (VNA equivalent) | calc | p.1013-1014 eq.(17-25),(17-26) | high |
| BALANIS-641 | matching | Match at (near) the antenna terminals to minimize line loss and voltage peaks and maximize bandwidth; conjugate match is not always optimal (some low-noise receivers want antenna impedance below the load; some transmitters want it above). | n/a | - | system matching | review | p.1012-1013 | high |
| BALANIS-642 | test | Measure input impedance in situ (it depends on geometry, excitation and nearby objects) unless the antenna is very narrow-beam; characterize mutual impedance through measured scattering (S_mn) coefficients converted to impedances. | n/a | - | impedance measurement | measure | p.1014 | high |
| BALANIS-643 | test | Current-distribution probe: small sampling loop near the radiator; run its leads to the detector wound as a helical choke on a dielectric rod with turn diameter and spacing ~lambda/50; bypass capacitor on the loop to avoid a dc short of the crystal rectifier. | choke turn dia = spacing ~ lambda/50 | lambda | current measurement | inspect | p.1014 | high |
| BALANIS-644 | test | Polarization description needs axial ratio, sense (RH/LH) and tilt angle; for a receiving antenna the matched incident-wave tilt tau_m and the transmitted-wave tilt tau_t relate as below (single coordinate system and view direction); use the polarization loss factor for mismatch. | tau_t = 180 deg - tau_m | tau_m | polarization characterization | calc | p.1015 eq.(17-27) | high |
| BALANIS-645 | test | Polarization-pattern method: spin a linear (dipole) probe; LP test antenna -> figure-eight, EP -> dumbbell with filled nulls, CP -> circle; axial ratio (dB) = outer minus inner envelope; does not give sense: get sense by comparing CW and CCW CP antennas (larger response) or with a dual-polarized probe measuring amplitude and relative phase; absolute three-antenna polarization method needs two non-CP antennas. | AR_dB = 20*log10(AR) = outer - inner envelope | probe response | polarization measurement | measure | p.1016-1019 | high |
| BALANIS-646 | test | Axial-ratio pattern example: nearly CP within 1 dB (AR < 1.122) near boresight, degrading monotonically to ~7 dB (AR ~2.24) at wide angles. | AR(1 dB) = 1.122 ; AR(7 dB) = 2.24 | - | CP test antenna, Fig 17.26 | measure | p.1017-1018 | high |
| BALANIS-647 | test | Geometrical scale model by factor n: lengths, time, wavelength, capacitance, inductance scale as 1/n; RCS as 1/n^2; frequency and conductivity as n; permittivity, permeability, velocity, impedance and antenna gain unchanged. Conductivity is the hardest to scale (use cleaner, polished, better conductors); get gain as directivity x efficiency when conductivity cannot be scaled. | l' = l/n ; f' = n*f ; sigma' = n*sigma ; RCS' = RCS/n^2 ; G' = G | n | scale-model measurements | calc | p.1019 Table 17.1 | high |
| BALANIS-648 | test | Scale-model validation: 1/10-scale helicopter measured at 7 GHz matched full-scale simulation at 700 MHz for a belly-mounted lambda/4 monopole (max gain ~6 dB); unscaled good conductivity (~5e7 S/m) did not affect results within measurement accuracy. | n = 10 | - | pattern scaling | measure | p.1020-1024 | high |
| BALANIS-649 | test | Flat-plate maximum monostatic RCS (normal incidence, either polarization, physical optics): 30 x 30 cm at 5 GHz -> 28.274 m^2 = 14.51 dBsm (sim 14.6); 10 x 10 cm at 15 GHz -> 3.142 m^2 = 4.97 dBsm (sim 5.10); scale factor n^2 = 9 -> 9.54 dB. | RCS_max = 4*pi*(A/lambda)^2 | A plate area (m^2), lambda | RCS range calibration | calc | p.1021-1023 eq.(17-28) | high |

### Appendices

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| BALANIS-680 | requirements | TV channel plan: every VHF and UHF channel is 6 MHz wide; video carrier = lower channel edge + 1.25 MHz; audio carrier = upper edge - 0.25 MHz (e.g. ch 2: 55.25/59.75 MHz; ch 14: 471.25/475.75 MHz); VHF ch 2-6 = 54-88 MHz (with gap 72-76 MHz), ch 7-13 = 174-216 MHz; UHF ch 14-83 = 470-890 MHz; land mobile allowed in 470-512 MHz in the top ten US urban areas. | f_video = f_low + 1.25 MHz ; f_audio = f_high - 0.25 MHz | channel number | US TV allocations as printed (pre-repack) | calc | p.1061 App.IX.1 | high |
| BALANIS-681 | requirements | Broadcast radio bands: AM 535-1605 kHz, 107 channels at 10 kHz spacing; FM 88-108 MHz, 100 channels at 200 kHz spacing. | as stated | - | US broadcast | inspect | p.1062 App.IX.2 | high |
| BALANIS-682 | requirements | Cellular bands (uplink MS->BS / downlink BS->MS): CDMA IS-95 824-849/869-894 MHz; GSM 890-915/935-960; E-GSM 880-915/925-960; DCS 1800 1710-1785/1805-1880; US PCS 1900 1850-1910/1930-1990; WCDMA 1920-1980/2110-2170 MHz; cordless: US 46-49 MHz, DECT 1.880-1.990 GHz. | Table App.IX.4 | - | as printed (2016) | inspect | p.1062 App.IX.4 | high |
| BALANIS-683 | requirements | IEEE radar band letters: HF 3-30 MHz, VHF 30-300 MHz, UHF 300-1,000 MHz, L 1-2 GHz, S 2-4, C 4-8, X 8-12, Ku 12-18, K 18-27, Ka 27-40, millimeter wave 40-300 GHz. | Table App.IX.5 | f | band naming in requirements | inspect | p.1063 App.IX.5 | high |


## 2. Formulas & tables (numbers)

### Ch 9 (tail) — Broadband dipoles, matching techniques

### Table 9.1 / 9.2 — Cylindrical dipole and stub resonances (Kraus) — p.503
| Resonance | Dipole length | Dipole R (ohm) | Stub length | Stub R (ohm) |
|---|---|---|---|---|
| 1st | 0.48*lambda*F | 67 | 0.24*lambda*F' | 34 |
| 2nd | 0.96*lambda*F | Rn^2/67 | 0.48*lambda*F' | (Rn')^2/34 |
| 3rd | 1.44*lambda*F | 95 | 0.72*lambda*F' | 48 |
| 4th | 1.92*lambda*F | Rn^2/95 | 0.96*lambda*F' | (Rn')^2/48 |
F = (l/2a)/(1+l/2a), Rn = 150*log10(l/2a); F' = (l/a)/(1+l/a), Rn' = 75*log10(l/a). Rn = "natural resistance" (geometric mean of an odd and next even resonance resistance).

### Eq. (9-19) — Dipole input impedance vs l/d (MoM) — p.504
| l | l/d = 1e4 (Omega = 19.81) | l/d = 50 (Omega = 9.21) | l/d = 25 |
|---|---|---|---|
| lambda/2 | 73 + j42.5 | 85.8 + j54.9 | 88.4 + j27.5 |
| 3*lambda/2 | 105.49 + j45.54 | 103.3 + j9.2 | 106.8 + j4.9 |
Omega = 2*ln(2l/d).

### Table 9.3 — Equivalent circular radius of non-circular conductors — p.506
| Cross-section (figure missing; labels per standard Table 9.3) | ae |
|---|---|
| thin flat strip, width a | 0.25*a |
| rectangle a x b | ~0.2*(a+b) |
| square, side a | 0.59*a |
| ellipse, semi-axes a, b | (a+b)/2 |
| two conductors C1, C2 (peripheries S1, S2; equivalent radii a1, a2; spacing s) | ln(ae) ~ [S1^2*ln(a1) + S2^2*ln(a2) + 2*S1*S2*ln(s)]/(S1+S2)^2 |

### Table 9.4 — Discone designs — p.513
| f (MHz) | A (cm) | B (cm) | C (cm) |
|---|---|---|---|
| 90 | 45.72 | 60.96 | 50.80 |
| 200 | 22.86 | 31.75 | 35.56 |

### Folded dipole two-wire line anchors (Thiele et al.) — p.510
| d (lambda) | s (lambda) | Z0 (ohm) | TL-model accuracy vs MoM |
|---|---|---|---|
| 0.001 | 0.00613 | 300 | excellent |
| 0.001 | 0.0213 | 450 | degrading |
| 0.001 | 0.0742 | 600 | poor unless thicker wires / equivalent radius |

### Ch 10 — Traveling-wave and broadband antennas

### Long-wire lobe constants (cot^2 envelope included) — p.538 eq.(10-8)
| Lobe | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th |
|---|---|---|---|---|---|---|---|
| 2m+1 (exact) | 0.742 | 2.93 | 4.96 | 6.97 | 8.99 | 11 | 13 |
| 2m+1 (approx.) | 1 | 3 | 5 | 7 | 9 | 11 | 13 |

### Table 10.1 — Six-element Yagi, director-spacing perturbation (l1 = 0.51, l2 = 0.50, l3..l6 = 0.43 lambda, a = 0.003369 lambda) — p.572
| Array | s21 | s32 | s43 | s54 | s65 (lambda) | D (dB) |
|---|---|---|---|---|---|---|
| Initial | 0.250 | 0.310 | 0.310 | 0.310 | 0.310 | 11.21 |
| Optimized | 0.250 | 0.336 | 0.398 | 0.310 | 0.407 | 12.87 |

### Table 10.2 — Six-element Yagi, all-spacing perturbation (same lengths) — p.572
| Array | s21 | s32 | s43 | s54 | s65 (lambda) | D (dB) |
|---|---|---|---|---|---|---|
| Initial | 0.280 | 0.310 | 0.310 | 0.310 | 0.310 | 10.92 |
| Optimized | 0.250 | 0.352 | 0.355 | 0.354 | 0.373 | 12.89 |

### Table 10.3 — Six-element Yagi, length perturbation (s21 = 0.250, others 0.310 lambda, a = 0.003369 lambda) — p.573
| Array | l1 | l2 | l3 | l4 | l5 | l6 (lambda) | D (dB) |
|---|---|---|---|---|---|---|---|
| Initial | 0.510 | 0.490 | 0.430 | 0.430 | 0.430 | 0.430 | 10.93 |
| Length-perturbed | 0.472 | 0.456 | 0.438 | 0.444 | 0.432 | 0.404 | 12.16 |

### Table 10.4 — Six-element Yagi, spacing then length perturbation (a = 0.003369 lambda) — p.573
| Array | l1 | l2 | l3 | l4 | l5 | l6 | s21 | s32 | s43 | s54 | s65 | D (dB) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Initial | 0.510 | 0.490 | 0.430 | 0.430 | 0.430 | 0.430 | 0.250 | 0.310 | 0.310 | 0.310 | 0.310 | 10.93 |
| After spacing perturbation | 0.510 | 0.490 | 0.430 | 0.430 | 0.430 | 0.430 | 0.250 | 0.289 | 0.406 | 0.323 | 0.422 | 12.83 |
| Optimum (spacing + length) | 0.472 | 0.452 | 0.436 | 0.430 | 0.434 | 0.430 | 0.250 | 0.289 | 0.406 | 0.323 | 0.422 | 13.41 |

### Table 10.5 — Yagi input impedance vs reflector spacing (reflector 0.5 lambda, directors 0.406 lambda @ 0.34 lambda) — p.575
| s21/lambda | 0.25 | 0.18 | 0.15 | 0.13 | 0.10 |
|---|---|---|---|---|---|
| Zin (ohm) | 62 | 50 | 32 | 22 | 12 |
(Table title says 15-element; text on p.572 says 13-element array, as printed.)

### Table 10.6 — NBS optimized uncompensated Yagi lengths, d/lambda = 0.0085, reflector spacing s12 = 0.2 lambda — p.576 (Viezbicke, NBS TN 688)
| Yagi length (lambda) | 0.4 | 0.8 | 1.20 | 2.2 | 3.2 | 4.2 |
|---|---|---|---|---|---|---|
| Reflector l1/lambda | 0.482 | 0.482 | 0.482 | 0.482 | 0.482 | 0.475 |
| Directors l3.. (lambda) | 0.442 | 0.428, 0.424, 0.428 | 0.428, 0.420, 0.420, 0.428 | 0.432, 0.415, 0.407, 0.398, 0.390, 0.390, 0.390, 0.390, 0.398, 0.407 | 0.428, 0.420, 0.407, 0.398, 0.394, 0.390, 0.386 x9 | 0.424, 0.424, 0.420, 0.407, 0.403, 0.398, 0.394, 0.390 x6 |
| Director spacing (lambda) | 0.20 | 0.20 | 0.25 | 0.20 | 0.20 | 0.308 |
| D over lambda/2 dipole (dB) | 7.1 | 9.2 | 10.2 | 12.25 | 13.4 | 14.2 |
| Design curve (Fig 10.27) | A | B | B | C | B | D |
(Director counts reconstructed from the OCR column order and consistent with length = 0.2 + n*spacing.)

### Fig 10.27 anchors — uncompensated element length vs d/lambda — p.577 (graph)
| Point | Value |
|---|---|
| Reflector at d/lambda = 0.00424 (curve B) | l1' = 0.485 lambda (vs l1'' = 0.482 lambda at 0.0085) |
| Directors curve B at 0.00424 | l3' = l5' = 0.442 lambda, l4' = 0.438 lambda (vs 0.428/0.424 at 0.0085) |
| Boom D/lambda = 0.00852 (Fig 10.28) | +0.005 lambda on every parasitic element |

### Ch 11 — Frequency-independent antennas, small-antenna limits, miniaturization, fractals

### Table 11.1 — LPDA input resistance Rin (ohm) and directivity D0 (dBi) vs apex half-angle alpha (Isbell) — p.607
| alpha (deg) | tau=0.81 Rin | tau=0.81 D0 | tau=0.89 Rin | tau=0.89 D0 | tau=0.95 Rin | tau=0.95 D0 |
|---|---|---|---|---|---|---|
| 10 | 98 | — | 82 | 9.8 | 77.5 | 10.7 |
| 12.5 | — | — | 77 | — | — | — |
| 15 | — | 7.2 | — | — | — | — |
| 17.5 | — | — | 76 | 7.7 | 62 | 8.8 |
| 20 | — | — | 74 | — | — | — |
| 25 | — | — | 63 | 7.2 | — | 8.0 |
| 30 | 80 | — | 64 | — | 54 | — |
| 35 | — | — | 56 | 6.5 | — | — |
| 45 | 65 | 5.2 | 59 | 6.2 | — | — |

### Table 11.2 — Four-arm folded spherical helix resonances (Best 2004) — p.618
| Turns | Arm length (cm) | f_R (MHz) | R_A (ohm) | Efficiency (%) | Q |
|---|---|---|---|---|---|
| 1/2 | 17 | 515.8 | 87.6 | 99.6 | 5.6 |
| 1 | 30.9 | 300.3 | 43.1 | 98.6 | 32 |
| 1 1/2 | 45.07 | 210 | 23.62 | 97.6 | 88 |

### Miniaturization trade-off data (50-ohm line) — p.620-625
| Case | Shortening | Rr (ohm) | e (%) | S11 (dB) | FBW | G_re (dB) |
|---|---|---|---|---|---|---|
| lambda0/4 monopole (reference) | 1 | 36.5 | 100 (99.1 meas.) | -16.1 (abs(G) = 0.1561) | 9.5% | 4.664 (D0=3) / 5.06 (D0=3.286) / 5.02 |
| Coil-loaded lambda0/(10pi), coil Q = 300 | 7.85 | 20.15 | 19.85 | -7.422 | — | -3.119 |
| Coil-loaded, lossless coil | 7.85 | 2.37 | 100 | -0.83 (abs(G) = 0.9095) | — | -2.853 |
| Water-loaded 23 mm @ 381 MHz | 8.544 (vol x118) | 0.4 | 12.6 | -0.139 | — | -18.85 |
| Water-loaded 160 mm @ 253 MHz | 1.85 (vol x199) | 8.5 | 96.6 | -2.98 | — | 1.978 |
| Meander N = 2 | 1.8 | 13 | 96.7 | -4.62 | 3% | 3.18 |
| Meander N = 14 | 1.33 | 23.5 | 98 | -8.86 | 8% | 4.47 |
(S11 of the reference and lossless-coil rows computed from the printed abs(Gamma): 20*log10(0.1561) = -16.1 dB, 20*log10(0.9095) = -0.82 dB — conf medium.)

### Ch 12 — Aperture antennas

### Table 12.1 — Rectangular apertures (a along H-plane x, b along E-plane y) — p.658-659
| Quantity | Uniform on ground plane | Uniform in free space | TE10 on ground plane |
|---|---|---|---|
| HPBW E-plane (deg), b >> lambda | 50.8/(b/lambda) | 50.8/(b/lambda) | 50.8/(b/lambda) |
| HPBW H-plane (deg), a >> lambda | 50.8/(a/lambda) | 50.8/(a/lambda) | 68.8/(a/lambda) |
| FNBW E-plane (deg) | 114.6/(b/lambda) | 114.6/(b/lambda) | 114.6/(b/lambda) |
| FNBW H-plane (deg) | 114.6/(a/lambda) | 114.6/(a/lambda) | 171.9/(a/lambda) |
| First sidelobe E / H (dB) | -13.26 / -13.26 | -13.26 / -13.26 | -13.26 / -23 |
| Directivity D0 | 4*pi*ab/lambda^2 | 4*pi*ab/lambda^2 | (8/pi^2)*4*pi*ab/lambda^2 = 0.81*4*pi*ab/lambda^2 |
Far-field: X = (ka/2) sin th cos phi, Y = (kb/2) sin th sin phi; free-space columns carry the (1+cos th)/2 factor.

### Table 12.2 — Circular apertures (radius a) — p.672-673
| Quantity | Uniform on ground plane | TE11 on ground plane |
|---|---|---|
| HPBW E-plane (deg), a >> lambda | 29.2/(a/lambda) | 29.2/(a/lambda) |
| HPBW H-plane (deg) | 29.2/(a/lambda) | 37.0/(a/lambda) |
| FNBW E-plane (deg) | 69.9/(a/lambda) | 69.9/(a/lambda) |
| FNBW H-plane (deg) | 69.9/(a/lambda) | 98.0/(a/lambda) |
| First sidelobe E / H (dB) | -17.6 / -17.6 | -17.6 / -26.2 |
| Directivity D0 | (2*pi*a/lambda)^2 | 0.836*(2*pi*a/lambda)^2 = 10.5*pi*(a/lambda)^2 |

### sin(x)/x pattern constants (uniform line/aperture) — p.655-656
| Point | x = (kb/2) sin th | Angle | Value |
|---|---|---|---|
| Half power | 1.391 | asin(0.443 lambda/b) | 0.707 |
| First null | pi | asin(lambda/b) | 0 |
| First sidelobe max | 4.494 | asin(1.43 lambda/b) | 0.217 (-13.26 dB) |

### Table 12.3 — Edge-of-coverage (EOC) optimum apertures — p.679
| Aperture | Distribution | Size | Directivity | EOC rel. to peak |
|---|---|---|---|---|
| Square | Uniform | side = lambda/(2 sin theta_c) | pi/sin^2(theta_c) | -3.920 dB |
| Circular | Uniform | radius = lambda/(3.413 sin theta_c) | 1.086*pi/sin^2(theta_c) (text eq.12-65: 1.079*pi) | -3.985 dB |
| Circular | Parabolic taper | radius = lambda/(2.732 sin theta_c) | 1.263*pi/sin^2(theta_c) | -4.069 dB |
| Circular | Parabolic taper, -10 dB pedestal | radius = lambda/(3.064 sin theta_c) | 1.227*pi/sin^2(theta_c) | -4.034 dB |

### Typical aperture efficiencies — p.665
| Antenna | eps_ap |
|---|---|
| Aperture antennas (general) | 0.30-0.90 |
| Horns | 0.35-0.80 (optimum-gain horn ~0.50) |
| Circular reflectors | 0.50-0.80 |
| TE10 rectangular aperture | 8/pi^2 = 0.81 |
| TE11 circular aperture | 0.836 |

### Ch 13 — Horn antennas

### Table 13.1 — Horn directivity formulas — p.761
| Horn | Formula | Eq. |
|---|---|---|
| E-plane | D_E = (64*a*rho1/(pi*lambda*b1))*[C^2(q) + S^2(q)], q = b1/sqrt(2*lambda*rho1) | 13-18 |
| E-plane (Braun) | D_E = (a/lambda)*G_E/sqrt(50/(rho_e/lambda)), B = (b1/lambda)*sqrt(50/(rho_e/lambda)); G_E = 32B/pi if B < 2 else Fig 13.8 | 13-19 |
| H-plane | D_H = (4*pi*b*rho2/(a1*lambda))*{[C(u)-C(v)]^2 + [S(u)-S(v)]^2} | 13-39 |
| H-plane (Braun) | D_H = (b/lambda)*G_H/sqrt(50/(rho_h/lambda)), A = (a1/lambda)*sqrt(50/(rho_h/lambda)); G_H = 32A/pi if A < 2 else Fig 13.15 | 13-40 |
| Pyramidal | D_p = (pi*lambda^2/(32*a*b))*D_E*D_H | 13-50a |
| Pyramidal (alternate) | D_p(dB) = 10*[1.008 + log10(a1*b1/lambda^2)] - (L_e + L_h) (Fig 13.21) | 13-51 |
| Pyramidal (Braun) | D_p = G_E*G_H/[(32/pi)*sqrt(50/(rho_e/lambda))*sqrt(50/(rho_h/lambda))] | 13-52e |
| Conical | Dc(dB) = 10*log10[(C/lambda)^2] - L(s); L(s) cubic fits; s = d_m^2/(8*lambda*l); d_m,opt = sqrt(3*l*lambda) | 13-58, 13-59 |

### Horn optimum/design constants — p.731-759
| Horn | Optimum relation | Peak phase error | Efficiency note |
|---|---|---|---|
| E-plane sectoral | b1 = sqrt(2*lambda*rho1) | s = 1/4 lambda | — |
| H-plane sectoral | a1 = sqrt(3*lambda*rho2) | t = 3/8 lambda | — |
| Pyramidal (optimum gain) | both of the above, pe = ph | — | overall ~50% (G0 = 0.5*4*pi*a1*b1/lambda^2) |
| Conical | d_m = sqrt(3*l*lambda) | s = 3/8 lambda | loss ~2.9 dB (eps_ap ~51%) |

### Fresnel-integral values used in the worked examples (Appendix IV) — p.733, p.743
| x | C(x) | S(x) |
|---|---|---|
| 0.794 | 0.72 | 0.24 |
| 1.273 | 0.659 | 0.669 |
| 1.9 | 0.394 | 0.373 |

### Worked horn anchors — p.722-756
| Case | Inputs | Results |
|---|---|---|
| Ex.13.1 E-plane flare | a = 0.5, b = 0.25, b1 = 2.75 lambda, 56.72 deg | rho1 = 6 lambda, 2*psi_e = 25.81 deg |
| Ex.13.2 E-plane | + rho1 = 6 lambda | D_E = 12.79 (11.07 dB); Braun 12.89 (11.10 dB) |
| Ex.13.3 H-plane | a1 = 5.5, b = 0.25, rho2 = 6 lambda | D_H = 7.52 (8.763 dB); Braun 8.338 (9.21 dB) |
| Ex.13.4 pyramidal | rho1 = rho2 = 6, a1 = 5.5, b1 = 2.75 lambda | pe = ph = 5.454 lambda; 18.78 / 19.26 / 18.93 dB |
| Ex.13.5 design | 22.6 dB @ 11 GHz, WR-90 | a1 = 16.370 cm, b1 = 12.859 cm, rho_e = 30.316 cm, rho_h = 32.753 cm, pe = ph = 27.286 cm |

### Ch 14 — Microstrip and mobile communications antennas (priority)

### Table 14.1 — Typical microstrip antenna substrates — p.784 (columns realigned from OCR; conf medium)
| Company | Substrate | Thickness (mm) | Frequency (GHz) | er | tan d |
|---|---|---|---|---|---|
| Rogers | Duroid 5880 | 0.127, 1.575, 3.175 | 0-40 | 2.20 | 0.0009 |
| Rogers | RO 3003 | 0.168 | 0-40 | 3.00 | 0.0010 |
| Rogers | RO 3010 | 0.508 | 0-10 | 10.2 | 0.0022 |
| Rogers | RO 4350 | 1.524 | 0-10 | 3.48 | 0.0037 |
| — | FR4 | 0.05-100 | 0.001 | 4.70 | — |
| DuPont | HK 04J | 0.025 | 0.001 | 3.50 | 0.005 |
| Isola | IS 410 | 0.05-3.2 | 0.1 | 5.40 | 0.035 |
| Arlon | DiClad 870 | 0.091 | 0-10 | 2.33 | 0.0013 |
| Polyflon | Polyguide | 0.102 | 0-10 | 2.32 | 0.0005 |
| Neltec | NH 9320 | 3.175 | 0-10 | 3.20 | 0.0024 |
| Taconic | RF-60A | 0.102 | 0-10 | 6.15 | 0.0038 |

### Patch feed comparison (from §14.1.2 text) — p.785-787
| Feed | Fabrication | Match | Spurious radiation | Bandwidth | Modeling |
|---|---|---|---|---|---|
| Microstrip line (inset) | easy | inset position | grows with h | ~2-5% (practical) | simple |
| Coax probe | easy | probe position | low | narrow | hard for h > 0.02 lambda0 |
| Aperture coupled | most difficult | feed width, slot length | moderate | narrow | somewhat easier |
| Proximity coupled | somewhat difficult | stub length, W/line ratio | low | largest (up to ~13%) | somewhat easy |

### Rectangular patch worked-example anchors (er = 2.2, h = 0.1588 cm, f = 10 GHz) — p.792-798, p.814-815, p.831
| Quantity | Value | Eq. |
|---|---|---|
| W | 1.186 cm (0.467 in) | 14-6 |
| eps_reff | 1.972 | 14-1 |
| dL | 0.081 cm (0.032 in) | 14-2 |
| L | 0.906 cm (0.357 in) | 14-7 |
| Le | 1.068 cm (0.421 in) = lambda_eff/2 | 14-3 |
| G1 (cavity) / G1 (TL 14-8a) | 0.00157 S / 0.00328 S | 14-12 / 14-8a |
| G12 | 6.1683e-4 S (g12 = 0.3921) | 14-18a |
| Rin at edge | 228.3508 ohm | 14-17 (+) |
| Inset y0 for 50 ohm | 0.3126 cm (0.123 in) | 14-20a |
| I1, D0 (one slot) | 1.863, 3.312 (5.201 dB) | 14-53 |
| D_AF, D2 (14-56) | 1.4367 (1.5736 dB), 4.7584 (6.7746 dB) | 14-56 |
| I2, D2 (14-55) | 3.59801, 5.3873 (7.314 dB) | 14-55 |
| CP single feed (5% BW @ VSWR 2) | Qt = 14.14, f1 = 9.664 GHz, f2 = 10.348 GHz, L/W = 1.07 | 14-88a, 14-94 |
| Derived: BW (14-89a) | 3.771*(1.2/4.84)*(0.1588/3)*(1.186/0.906) = 6.48% (VSWR 2) | derived, conf medium |
| Derived: Rin (14-18b) | 90*(4.84/1.2)*(0.906/1.186)^2 = 211.8 ohm | derived, conf medium |

### Circular patch anchors (er = 2.2, h = 0.1588 cm, 10 GHz) — p.818-819
| F | a | ae | probe rho_f |
|---|---|---|---|
| 0.593 | 0.525 cm (0.207 in) | 0.598 cm | 0.2 cm |

### Bessel-function zeros used for patches and DRAs — p.817, p.851-852
| Set | Values |
|---|---|
| J'm zeros chi'_mn (circular patch TMmn0; cylindrical DRA TM) | chi'11 = 1.8412, chi'21 = 3.0542, chi'01 = 3.8318, chi'31 = 4.2012, (5.3175, printed as chi'31; = chi'41) |
| Jm zeros chi_mn (cylindrical DRA TE) | chi01 = 2.4049, chi11 = 3.8318, chi21 = 5.1357, chi02 = 5.5201, chi31 = 6.3802 |
| Spherical Jn zeros zeta_np (hemispherical DRA TE) | zeta11 = 4.493, zeta21 = 5.763, zeta31 = 6.988, zeta12 = 7.725, zeta41 = 8.183 |
| Spherical J'n zeros zeta'_np (hemispherical DRA TM) | zeta'11 = 2.744, zeta'21 = 3.870, zeta'31 = 4.973, zeta'41 = 6.062, zeta'12 = 6.117 |

### Table 14.2 — Probe angular spacing for CP, circular patch — p.832 (layout reconstructed)
| Mode | TM110 | TM210 | TM310 | TM410 | TM510 | TM610 |
|---|---|---|---|---|---|---|
| alpha | 90 deg | 45 or 135 deg | 30 or 90 deg | 22.5 or 67.5 deg | 18, 54 or 90 deg | 15, 45 or 75 deg |

### Table 14.3 — Cylindrical DRA predicted vs measured resonance and Q — p.854
| er, a, h | Mode | f_meas (GHz) | f_theory (GHz) | diff | Q_meas | Q_theory | diff |
|---|---|---|---|---|---|---|---|
| 38, 0.6415 cm, 0.2810 cm | TE01d | 3.97 | 3.988 | 0.45% | 46.2 | 41.92 | 9.3% |
| | TM01d | 6.13 | 6.175 | 0.73% | 72.1 | 46.34 | 35.7% |
| | HE11d | 5.18 | 5.262 | 1.58% | 30.2 | 31.24 | 3.4% |
| 79, 0.5145 cm, 0.2255 cm | TE01d | 3.48 | 3.47 | 2.9% (as printed; 0.29% by arithmetic) | 114.7 | 106.21 | 7.4% |
| | TM01d | 5.41 | 5.41 | 0.0% | 336.7 | 349.61 | 3.8% |
| | HE11d | 4.56 | 4.61 | 1.1% | 76.4 | 80.94 | 5.9% |

### DRA Example 14.9 anchors (a = 0.5 cm, h = 0.3 cm, a/h = 1.67) — p.856-858
| Quantity | er = 8.9 | er = 89 |
|---|---|---|
| Cavity TE010 / TM110 (GHz) | 11.38 / 10.24 | 3.60 / 3.24 |
| Hybrid TE01d / TM01d / HE11d (GHz) | 9.385 / 13.419 / 8.564 (printed; eq.14-110a gives ~10.68) | 3.113 / 4.644 / 2.964 (printed; eq. gives ~3.70) |
| Q TE01d / TM01d / HE11d | 7.17 / 6.325 / 5.8864 | 133.512 / 1,071.95 / 117.45 |
| Simulated S11 minimum, -10 dB BW | 10.69 GHz, 7.02% | — |

### Handset antenna anchors — p.840-847
| Antenna | Substrate | f | Dimensions |
|---|---|---|---|
| PIFA (Ex.14.6) | air, h = 0.448 cm | 1.8 GHz | L = 3.2 cm (0.192 lambda), W = 2.474 cm (0.1484 lambda), ws = 1.059 cm (0.0636 lambda), y0 = 0.57 cm |
| Slot (Ex.14.7) | free space, 5x5 lambda PEC | — | L = lambda/2, W = lambda/10: Zs = 362.95 - j211.31 (Babinet) vs 339.38 - j78.85 (sim) |
| IFA (Ex.14.8) | RT/duroid 5870, er = 2.33, h = 0.1524 cm | 1.8 GHz | L = 2.73 cm (lambda/4), pin W = 0.655 cm (0.06 lambda) |
| U-slot 2-band | — | GSM 874-958 MHz; DCS 1,711-1,943 MHz | BW 84 MHz (~9%); 232 MHz (~13%) |

### Ch 15 — Reflector antennas

### Table 15.1 — Optimum-efficiency reflectors for cos^n feeds (edge values relative to vertex) — p.909
| n | eps_ap | theta0 (deg) | f/d | Feed 10log[G(theta0)] (dB) | Path 10log(f/r')^2 (dB) | Total (dB) |
|---|---|---|---|---|---|---|
| 2 | 0.829 | 66 | 0.385 | -7.8137 | -3.056 | -10.87 |
| 4 | 0.8196 | 53.6 | 0.496 | -8.8215 | -1.959 | -10.942 |
| 6 | 0.8171 | 46.2 | 0.5861 | -9.4937 | -1.439 | -10.93 |
| 8 | 0.8161 | 41.2 | 0.6651 | -9.7776 | -1.137 | -10.914 |
(n = 4 row: printed Feed + Path = -10.78 dB, not the printed total -10.942 — transcribed as printed; path sign for n = 8 restored from OCR.)

### cos^n feed aperture efficiency closed forms — p.902 eq.(15-59)
| n | eps_ap(theta0) |
|---|---|
| 2 | 24*{sin^2(theta0/2) + ln[cos(theta0/2)]}^2*cot^2(theta0/2) |
| 4 | 40*{sin^4(theta0/2) + ln[cos(theta0/2)]}^2*cot^2(theta0/2) |
| 6 | 14*{2 ln[cos(theta0/2)] + [1 - cos(theta0)]^3/3 + (1/2) sin^2(theta0)}^2*cot^2(theta0/2) |
| 8 | 18*{(1 - cos^4(theta0))/4 - 2 ln[cos(theta0/2)] - [1 - cos(theta0)]^3/3 - (1/2) sin^2(theta0)}^2*cot^2(theta0/2) |

### Corner reflector characteristic spacings — p.880-884
| alpha | Multiple lobes when s > | Max abs(E/E0) | First on-axis peak s | Period of on-axis field |
|---|---|---|---|---|
| 90 deg | 0.7 lambda (null on axis at s = lambda) | 4 (at 0.5 lambda) | 0.5 lambda | lambda |
| 60 deg | ~0.95 lambda | ~5.2 | ~0.65 lambda | 2 lambda |
| 45 deg | ~1.2 lambda | ~8 | ~0.85 lambda | pseudo (~16.69 lambda) |
| 30 deg | ~2.5 lambda | ~9 | ~1.20 lambda | pseudo (~30 lambda) |

### Reflector efficiency budget terms — p.903-905
| Term | Loss meaning |
|---|---|
| eps_s spillover | feed power missing the reflector |
| eps_t taper | nonuniform aperture amplitude |
| eps_p phase | aperture phase not uniform (defocus, surface, feed wavefront) |
| eps_x polarization | cross-polarized aperture fields |
| eps_b blockage | feed, struts, subreflector shadow |
| eps_r random surface error | Ruze exp(-(4 pi sigma/lambda)^2) |
Loss (%) of each = 100*(1 - eps); plus feed-line attenuation.

### Ch 16 — Smart antennas

### Table 16.1 — Eight-element array, SOI 20 deg (d = 0.5 lambda, mu = 0.01, 55 iterations) — p.958
| Element | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Classical w | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Classical phase (deg) | 0 | -61.56 | -123.12 | -184.69 | -246.25 | -307.82 | -369.38 | -430.95 |
| LMS phase (deg) | 0 | -61.56 | -123.13 | -184.69 | -246.25 | -307.82 | -369.38 | -430.95 |

### Table 16.2 — Eight-element LMS, SOI 20 deg + SNOI 45 deg (81 iterations) — p.959
| Element | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| w | 1.0000 | 0.8982 | 1.1384 | 1.3760 | 1.3760 | 1.1384 | 0.8982 | 1.0000 |
| phase (deg) | -11.62 | -57.05 | -109.98 | -178.77 | -252.21 | -321.01 | -373.94 | -419.37 |

### Fig 16.37 — 20 GHz Si patch: cavity model vs optimized full-wave — p.966
| Parameter | Cavity model | Optimized (Ensemble) |
|---|---|---|
| W | 2.976 mm | 2.247 mm |
| L | 2.129 mm | 2.062 mm |
| y0 | 1.488 mm | 1.164 mm |
| x0 | 1.256 mm | 0.794 mm |
| h | 0.300 mm | 0.300 mm |
| er, tan d | 11.7 (Si), 0.04 | 11.7 (Si), 0.04 |
| 8x8 array spacing | dx = dy = 7.500 mm (lambda/2 at 20 GHz) | Dx = 54.562 mm, Dy = 54.747 mm |

### Ch 17 — Antenna measurements (priority)

### Table 17.1 — Geometrical scale model (factor n) — p.1019
| Scaled parameter | Relation | Unchanged parameter | Relation |
|---|---|---|---|
| Length | l' = l/n | Permittivity | eps' = eps |
| Time | t' = t/n | Permeability | mu' = mu |
| Wavelength | lambda' = lambda/n | Velocity | v' = v |
| Capacitance | C' = C/n | Impedance | Z' = Z |
| Inductance | L' = L/n | Antenna gain | G0' = G0 |
| Echo area (RCS) | Ae' = Ae/n^2 | | |
| Frequency | f' = n*f | | |
| Conductivity | sigma' = n*sigma | | |

### Measurement acceptance / setup numbers (Chapter 17)
| Item | Value | Page |
|---|---|---|
| Far-field distance | R >= 2D^2/lambda (edge phase error 22.5 deg) | p.981-982 |
| Absorber reflectivity | -40 dB at normal incidence down to ~100 MHz | p.985 |
| CATR length | ~10-20 m | p.986 |
| CATR quiet zone | 50-60% of reflector; phase < 10 deg; ripple < 1 dB p-p; taper < 1 dB | p.987 |
| CATR reflector | >= 25-30 lambda across (low limit); surface error < 0.007 lambda; dual reflector 2x precision; 1-100 GHz typical | p.989 |
| SPCR | QZ ~100% horizontal, 50-60% vertical; ~60% cost of CATR | p.992 |
| Planar NF sampling | <= lambda/2; z0 >= 2-3 lambda; edge <= -45 dB | p.993-998 |
| Cyl./sph. NF sampling | dphi = dtheta = lambda/(2(a+lambda)); dz = lambda/2 | p.994-995 |
| Pattern dynamic range | 0-60 dB recorders; 40 dB usually adequate | p.1002 |
| Gain venues | >1 GHz free space; 0.1-1 GHz ground reflection; <0.1 GHz in situ; <1 MHz field strength; gain transfer >= 50 MHz | p.1005-1010 |
| Gain standards | lambda/2 dipole ~2.1 dB; pyramidal horn 12-25 dB (AR ~40 dB-inf) | p.1006 |
| Cross-pol (good design) | <= -40 dB | p.1012 |
| Current probe choke | turn diameter and pitch ~lambda/50 | p.1014 |

### VSWR / return-loss / mismatch-loss reference (derived from eq.17-24; conf medium) — p.1013
| VSWR | abs(Gamma) | Return loss (dB) | Mismatch loss (dB) | Reflected power (%) | Where the book uses it |
|---|---|---|---|---|---|
| 1.058 | 0.0282 | 31.0 | 0.003 | 0.08 | binomial transformer example (p.517) |
| 1.1 | 0.0476 | 26.44 | 0.010 | 0.23 | horn VSWR (p.768) |
| 1.2 | 0.0909 | 20.83 | 0.036 | 0.83 | 50-ohm helix narrow band (p.558) |
| 1.5 | 0.2000 | 13.98 | 0.177 | 4.0 | bow-tie criterion quoted as "-15 dB" (p.495) |
| 2 | 0.3333 | 9.54 | 0.512 | 11.1 | usual antenna bandwidth criterion S11 = -10 dB (p.499, p.625, p.825) |
| 3 | 0.5000 | 6.02 | 1.249 | 25.0 | commercial helix limit, DRA design example (p.559, p.858) |

### Example RCS / scale anchors — p.1021-1023
| Plate | f | RCS_max (formula) | Simulated |
|---|---|---|---|
| 30 x 30 cm | 5 GHz | 28.274 m^2 = 14.51 dBsm | 14.6 dBsm |
| 10 x 10 cm | 15 GHz | 3.142 m^2 = 4.97 dBsm | 5.10 dBsm |

### Appendices

### Appendix IX.1 — US television channels — p.1061
| Band | Channels | Frequency (MHz) | Channel width |
|---|---|---|---|
| VHF low | 2, 3, 4 | 54-60, 60-66, 66-72 | 6 MHz |
| VHF low | 5, 6 | 76-82, 82-88 | 6 MHz |
| VHF high | 7-13 | 174-216 (174, 180, 186, 192, 198, 204, 210, 216 edges) | 6 MHz |
| UHF | 14-83 | 470-890 (470, 476, 482, ... 878, 884, 890) | 6 MHz |

### Appendix IX.3 — Amateur bands — p.1062
| Band | MHz | Band | MHz |
|---|---|---|---|
| 160 m | 1.8-2.0 | 2 m | 144.0-148.0 |
| 80 m | 3.5-4.0 | — | 220-225 |
| 40 m | 7.0-7.3 | — | 420-450 |
| 20 m | 14.0-14.35 | — | 1215-1300 |
| 15 m | 21.0-21.45 | — | 2300-2450 |
| 10 m | 28.0-29.7 | — | 3300-3500 |
| 6 m | 50.0-54.0 | — | 5650-5925 |

### Appendix IX.4 — Cellular telephone bands — p.1062
| System | Uplink MS->BS (MHz) | Downlink BS->MS (MHz) | Areas |
|---|---|---|---|
| CDMA IS-95 | 824-849 | 869-894 | North America, Korea, China |
| GSM | 890-915 | 935-960 | North America, Europe, China, Japan |
| Extended-GSM | 880-915 | 925-960 | North America, Europe, China, Japan |
| DCS 1800 | 1710-1785 | 1805-1880 | Europe |
| US PCS 1900 | 1850-1910 | 1930-1990 | North America |
| WCDMA | 1920-1980 | 2110-2170 | Everywhere |
| CDMA2000 | all existing CDMA frequencies | — | Everywhere |
Cordless: USA 46-49 MHz; DECT 1.880-1.990 GHz.

### Appendix IX.5 — IEEE radar band designations — p.1063
| Band | Range |
|---|---|
| HF | 3-30 MHz |
| VHF | 30-300 MHz |
| UHF | 300-1,000 MHz |
| L | 1-2 GHz |
| S | 2-4 GHz |
| C | 4-8 GHz |
| X | 8-12 GHz |
| Ku | 12-18 GHz |
| K | 18-27 GHz |
| Ka | 27-40 GHz |
| Millimeter wave | 40-300 GHz |


## 3. Mechanizable checks

### Ch 9 (tail) — Broadband dipoles, matching techniques

- `CHECK-qw-transformer`: inputs Rin (ohm, real impedance at the insertion point), Z0 (ohm), Z1_design (ohm) -> Z1 = sqrt(Rin*Z0) -> pass if abs(Z1_design - Z1)/Z1 <= tol (e.g. 2%) -> margin = 1 - abs(err)/tol. Source BALANIS-230.
- `CHECK-binomial-transformer`: inputs RL, Z0 (ohm), N, rho_m -> rho_n = 2^-N*(RL-Z0)/(RL+Z0)*C(N,n); Z_{n+1} = Z_n*(1+rho_n)/(1-rho_n); df/f0 = 2-(4/pi)*acos[(rho_m/abs(rhoL))^(1/N)] -> pass if df/f0 >= required fractional BW -> margin = (df/f0)/BW_req - 1. Regression anchor: RL=100, Z0=50, N=2, rho_m=0.028 -> Z1=59.09, Z2=82.73, df/f0=0.375. Source BALANIS-232..234.
- `CHECK-chebyshev-transformer`: inputs RL, Z0, N, rho_m -> sec(theta_m) = cosh[(1/N)*acosh(abs(rhoL)/rho_m)], df/f0 = 2 - 4*theta_m/pi -> pass if df/f0 >= BW_req and rho_m < abs(rhoL) -> margin as above. Source BALANIS-236.
- `CHECK-vivaldi-envelope`: inputs f0, f_min (Hz), er, L, Wmax (m) -> lam0 = c/(f0*sqrt(er)), lam_min = c/(f_min*sqrt(er)) -> pass if lam0 < Wmax < lam_min/2 and L > c/f_min (free-space, conservative; use lam_min if substrate wavelength intended) -> margin = min(Wmax/lam0-1, (lam_min/2)/Wmax-1). Anchor: 10 GHz/4 GHz/2.33 -> 19.65..24.57 mm. Source BALANIS-208, -210.
- `CHECK-dipole-resonance-kraus`: inputs l (m), a (m), f (Hz) -> F = (l/2a)/(1+l/2a); l_res1 = 0.48*lambda*F -> pass if abs(l - l_res1)/l_res1 <= tol; predicted R = 67 ohm; VSWR vs Z0 = max(R/Z0, Z0/R). Source BALANIS-212/213.
- `CHECK-folded-dipole-Zin`: inputs Zd (ohm, complex, computed with ae = sqrt(a*s)), s, a, l, lambda -> Z0 = (377/pi)*acosh(s/(2a)); Zt = j*Z0*tan(pi*l/lambda); Zin = 4*Zt*Zd/(2*Zd+Zt) -> pass if VSWR(Zin, Z_line) <= spec. Source BALANIS-221..223.
- `CHECK-microstrip-Z-liao`: inputs er, h, w, t -> Zc = 87/sqrt(er+1.41)*ln(5.98h/(0.8w+t)) -> valid only if h < 0.8w; pass if abs(Zc - Z_target)/Z_target <= tol. Source BALANIS-235.

### Ch 10 — Traveling-wave and broadband antennas

- `CHECK-helix-axial-window`: inputs C (m), S (m), N, f (Hz) -> lambda0 = c/f; alpha = atan(S/C) -> pass if 0.75 < C/lambda0 < 4/3 and 12 <= alpha(deg) <= 14 and N > 3 -> margin = min distance to window edges (normalized). Source BALANIS-254.
- `CHECK-helix-kraus`: inputs C, S, N, lambda0, Z_line -> R = 140*C/lambda0; HPBW = 52*lambda0^1.5/(C*sqrt(N*S)); D0 = 15*N*C^2*S/lambda0^3; AR = (2N+1)/(2N) -> pass if D0_dB >= spec, AR_dB <= spec, VSWR(R, Z_line) <= spec (or a 50-ohm feed transition per (10-41) is present) -> margins in dB. Note Kraus D0 overestimates ordinary end-fire (Example 10.1: 15.4 dB formula vs 11.03 dB computed). Source BALANIS-255..258.
- `CHECK-yagi-geometry`: inputs lambda, element lengths/spacings, diameters -> pass if driven 0.45-0.49 lambda, directors 0.40-0.45 lambda, director spacing <= 0.4 lambda (warn > 0.3 lambda for long arrays), reflector spacing 0.15-0.25 lambda, reflector count <= 2 -> report violations. Source BALANIS-262..268.
- `CHECK-yagi-gain-estimate`: inputs boom length L/lambda -> G_lin = (5..9)*L/lambda and NBS table interpolation D(L) over dipole (0.4->7.1, 0.8->9.2, 1.2->10.2, 2.2->12.25, 3.2->13.4, 4.2->14.2 dB) -> pass if spec gain <= table value at the chosen length. Source BALANIS-264, -272.
- `CHECK-vee-optimum`: inputs arm length l/lambda (0.5..3), included angle (deg) -> 2*theta0_opt from (10-19); D0 = 2.94*l/lambda + 1.15 -> pass if abs(angle - opt) <= 5 deg -> margin in deg. Source BALANIS-248.
- `CHECK-beverage-termination`: inputs h, d -> RL = 138*log10(4h/d) -> pass if chosen resistor within +/-10% of RL (tune on the wire for no standing wave). Source BALANIS-244.
- `CHECK-resonant-longwire`: inputs n (odd) -> Rr = 73 + 69*log10(n); theta_max = acos((n-1)/n); D0 = 120/(Rr*sin^2(theta_max)). Regression: n = 1 -> 73 ohm, 90 deg, D0 = 1.644. Source BALANIS-245.

### Ch 11 — Frequency-independent antennas, small-antenna limits, miniaturization, fractals

- `CHECK-chu-limit`: inputs a (m, radius of the sphere enclosing antenna incl. ground/feed that radiates), f (Hz), required FBW, efficiency e -> ka = 2*pi*f*a/c; Q_min = 1/(ka)^3 + 1/(ka) (single mode) -> FBW_max ~ 1/Q_min (lossless; loss raises achievable FBW at efficiency cost) -> pass if FBW_req <= FBW_max (practical target: FBW_req <= FBW_max/1.5) -> margin = FBW_max/FBW_req - 1. Source BALANIS-299..303.
- `CHECK-realized-gain`: inputs Rr or Zin (ohm), Z0 (ohm), e_cd, D0 -> Gamma = (Zin-Z0)/(Zin+Z0); G_re = 10*log10[e_cd*(1-abs(Gamma)^2)*D0] -> pass if G_re >= spec -> margin (dB). Regression anchors: Rr = 20.15, e = 0.1985, D0 = 3 -> -3.119 dB; Rr = 36.5, e = 1, D0 = 3 -> 4.664 dB. Source BALANIS-305/306.
- `CHECK-lpda-carrel`: inputs f_min, f_max, D0 target (-> tau, sigma from Fig 11.13 optimum line), Rin, l/d -> alpha = atan((1-tau)/(4 sigma)); B_ar, Bs, L, N, Za, s per (11-28)-(11-34) -> pass if boom length L <= mechanical limit and N integer >= computed N -> report geometry. Regression: 54-216 MHz, sigma = 0.157, tau = 0.865 -> alpha = 12.13 deg, Bs = 7.01, L = 5.541 m, N = 14.43. Source BALANIS-294/296.
- `CHECK-spiral-low-cutoff`: inputs arm length L_arm (m), f_min -> pass if L_arm >= c/f_min (AR <= 2 on axis expected) -> margin = L_arm*f_min/c - 1. Source BALANIS-284.
- `CHECK-fi-feed-size`: inputs feed-region dimension g (m), f_max -> pass if g <= c/(8*f_max). Source BALANIS-280.

### Ch 12 — Aperture antennas

- `CHECK-aperture-gain`: inputs aperture area Ap (m^2) or a x b / radius, distribution {uniform, TE10, TE11, measured eps_ap}, f, radiation efficiency e -> D0 = eps_ap*4*pi*Ap/lambda^2 (eps_ap = 1, 0.81, 0.836 or given); G = e*D0 -> pass if G_dBi >= spec -> margin (dB). Regression: 3 lambda x 2 lambda uniform -> 75.4 (18.77 dB). Source BALANIS-325, -328, -330, -331, -342.
- `CHECK-aperture-beamwidth`: inputs dims/lambda, distribution -> HPBW from Tables 12.1/12.2 (e.g. 50.8*lambda/b, 68.8*lambda/a TE10 H-plane, 29.2*lambda/a circular) -> pass if within spec +/- tolerance; valid only for dimension >> lambda (else use exact asin forms). Source BALANIS-322..324, -330, -331.
- `CHECK-eoc-aperture`: inputs theta_c (coverage edge), shape, distribution -> optimum size and D0 per Table 12.3 -> compare design size; pass if within +/-5% of optimum or D(theta_c) meets spec; regression theta_c = 30 deg: square side = lambda, D0 = 10.99 dB; circular a = 0.586 lambda, 11.32 dB. Source BALANIS-333..336.
- `CHECK-babinet-slot`: inputs Z_dipole (complement) -> Zs = eta0^2/(4*Zd) with eta0 = 376.7 ohm -> regression 73 + j42.5 -> 362.95 - j211.31 ohm. Source BALANIS-337.
- `CHECK-sidelobe-taper`: inputs required SLL (dB) -> reject uniform illumination if SLL_req < -13.26 dB (rectangular) or < -17.6 dB (circular). Source BALANIS-324, -330, -332.

### Ch 13 — Horn antennas

- `CHECK-horn-sectoral-optimum`: inputs a1, b1, rho1, rho2 (or rho_e, rho_h), lambda -> s = b1^2/(8*lambda*rho1), t = a1^2/(8*lambda*rho2) -> pass (optimum) if abs(s - 0.25) <= 0.05 and abs(t - 0.375) <= 0.05; flag if s or t > 0.6 (phase-error regime where main beam may split/leave axis). Source BALANIS-363, -366, -371.
- `CHECK-horn-realizable`: inputs a, b, a1, b1, rho_e, rho_h -> pe, ph per (13-47) -> pass if abs(pe - ph)/pe <= 1% -> margin. Regression: Ex.13.4 -> 5.454 lambda both. Source BALANIS-374.
- `CHECK-horn-directivity`: inputs a, b, a1, b1, rho1, rho2, lambda -> D_E (13-18) and D_H (13-39) via Fresnel integrals (scipy.special.fresnel returns S, C with the same pi*t^2/2 kernel), D_p = pi*lambda^2/(32ab)*D_E*D_H -> pass if D_p(dBi) - losses >= G_spec -> margin. Regression: Ex.13.4 -> 18.78 dB. Source BALANIS-365, -370, -377.
- `CHECK-horn-design-optimum`: inputs G0 (dBi), a, b, f -> solve (13-54) for chi (Newton/bisection from chi1 = G0/(2*pi*sqrt(2*pi))) -> rho_e, rho_h, a1, b1, pe, ph -> report; regression Ex.13.5 (22.6 dB, 11 GHz, WR-90) -> chi = 11.1157, a1 = 16.370 cm, b1 = 12.859 cm, pe = ph = 27.286 cm. Source BALANIS-382, -383.
- `CHECK-conical-horn`: inputs d_m, l, L, lambda, D_spec -> s = d_m^2/(8*lambda*l); L(s) per (13-58b/c); Dc = 20*log10(pi*d_m/lambda) - L(s) -> pass if Dc >= D_spec; optimum if d_m ~ sqrt(3*l*lambda). Source BALANIS-384..386.
- `CHECK-corrugations`: inputs w, t, d, pitch, lambda0 (over the band) -> pass if slots/lambda >= 10, w < lambda0/10, t <= w/10, lambda0/4 < d < lambda0/2 at every band frequency (the depth window in which the book states the surface is capacitive) -> report the sub-band where the depth condition holds. Source BALANIS-389.

### Ch 14 — Microstrip and mobile communications antennas (priority)

Patch spec table columns assumed: er, tan_d, h (m), sigma (S/m), f_r (Hz), W (m), L (m), y0 (m), Z0 (ohm), W0 feed width (m), BW_req (fraction), VSWR_max, D_req (dBi), e_req.
- `CHECK-patch-substrate-window`: inputs er, h, f_r -> lambda0 = c/f_r -> pass if 2.2 <= er <= 12 and 0.003 <= h/lambda0 <= 0.05; warn if probe-fed and h/lambda0 > 0.02 (needs full-wave), warn if h/lambda0 near 0.05 (surface waves) -> margin = min(h/lambda0 - 0.003, 0.05 - h/lambda0)/0.05. Source BALANIS-401, -403, -406.
- `CHECK-patch-rect-dimensions`: inputs er, h, f_r, W, L -> W_d = c/(2 f_r)*sqrt(2/(er+1)); eps_reff (14-1) with W; dL (14-2); L_d = c/(2 f_r sqrt(eps_reff)) - 2 dL -> pass if abs(L - L_d)/L_d <= 1% and W/L <= 2 and lambda0/3 < L < lambda0/2 (expect L ~ 0.47-0.49*lambda0/sqrt(er)) -> margin = 1 - abs(L - L_d)/(0.01 L_d). Regression: (2.2, 0.1588 cm, 10 GHz) -> W = 1.186 cm, eps_reff = 1.972, dL = 0.081 cm, L = 0.906 cm. Source BALANIS-410..416.
- `CHECK-patch-resonance`: inputs W, L, h, er, f_target -> f_rc = c/(2*(L + 2 dL)*sqrt(eps_reff)) -> pass if abs(f_rc - f_target)/f_target <= tol (<= 1%; budget an extra ~1% for inset notch capacitance and ~2% observed prototype shift) -> margin = 1 - err/tol. Also report f_TM001 = c/(2W sqrt(er)) (or f_TM020 = c/(L sqrt(er)) if W < L/2) and require f_next/f_r - 1 > BW_req. Source BALANIS-412, -427, -432.
- `CHECK-patch-edge-resistance`: inputs W, L, f_r -> X = k0 W; I1 = -2 + cos X + X Si(X) + sin X/X; G1 = I1/(120 pi^2); G12 by numerical integral (14-18a); Rin0 = 1/(2(G1+G12)); cross-check Rin_alt = 90*er^2/(er-1)*(L/W)^2 -> pass if Rin0 >= Z0 (inset feasible) and abs(Rin0 - Rin_alt)/Rin0 <= 25% (model agreement flag) -> margin = Rin0/Z0 - 1. Regression: Example 14.2 -> G1 = 0.00157 S, G12 = 6.1683e-4 S, Rin0 = 228.35 ohm. Source BALANIS-418..422.
- `CHECK-patch-inset-50ohm`: inputs Rin0, L, Z0, y0_design, fab_tol (m) -> y0 = (L/pi)*acos(sqrt(Z0/Rin0)) -> pass if abs(y0_design - y0) <= fab_tol and 0 < y0 < L/2; sensitivity dR/dy0 = -Rin0*(pi/L)*sin(2 pi y0/L); report Rin(y0 +/- fab_tol) and resulting abs(Gamma) -> margin = 1 - abs(Gamma_worst)/Gamma_max. Regression: 228.3508 ohm, L = 0.906 cm, 50 ohm -> y0 = 0.3126 cm. Source BALANIS-426, -427, -429.
- `CHECK-feedline-width`: inputs er, h, Z_target -> solve (14-19a/b) for W0 (bisection on W0/h, eps_reff from 14-1 with W0) -> pass if abs(Zc(W0_design) - Z_target) <= 2% -> margin. Source BALANIS-424.
- `CHECK-patch-bandwidth`: inputs er, h, W, L, f_r, VSWR_max, BW_req -> BW2 = 3.771*((er-1)/er^2)*(h/lambda0)*(W/L) (VSWR 2); for other VSWR use Qt = 1/(BW2*sqrt(2)) then BW = (VSWR-1)/(Qt*sqrt(VSWR)) -> pass if BW >= BW_req -> margin = BW/BW_req - 1. Derived anchor: Example 14.1 patch -> 6.48% (book quotes ~5% for this substrate). Source BALANIS-451..453.
- `CHECK-patch-efficiency-Q`: inputs h, f_r, sigma, tan_d, er, W, L, Grad -> Qc = h*sqrt(pi f mu0 sigma); Qd = 1/tan_d; Qrad = 2*omega*er*(L/4)/(h*Grad/W) (per 14-86; confirm units in the original before trusting absolute values); 1/Qt = sum; e = Qt/Qrad -> pass if e >= e_req and 1/Qt consistent with BW check. Source BALANIS-449, -450, -454.
- `CHECK-patch-directivity`: inputs W, L, h, f_r -> D0 = (2 pi W/lambda0)^2/I1; g12 = G12/G1; D2 = D0*2/(1+g12) (fast) or (14-55) double integral (preferred, ~0.5 dB higher) -> pass if D2(dBi) >= D_req -> margin (dB). Asymptotic sanity: 6.6 (8.2 dB) for W << lambda0. Regression: Example 14.3 -> 6.7746 dB (14-56), 7.314 dB (14-55). Source BALANIS-437..442.
- `CHECK-circular-patch`: inputs er, h (cm), f_r, a -> F = 8.791e9/(f_r sqrt(er)); a_d = F/sqrt(1 + (2h/(pi er F))*(ln(pi F/(2h)) + 1.7726)); ae per (14-67) -> pass if abs(a - a_d)/a_d <= 1% -> margin. Probe radius for Z0: solve J1^2(k rho0)/J1^2(k ae) = Z0*Gt. Regression: (2.2, 0.1588 cm, 10 GHz) -> a = 0.525 cm, ae = 0.598 cm. Source BALANIS-444..448.
- `CHECK-cp-nearly-square`: inputs f0, BW, VSWR (or Qt), L, W -> Qt = (VSWR-1)/(BW sqrt(VSWR)); ratio_req = 1 + 1/Qt -> pass if abs(L/W - ratio_req) <= 0.5% -> f1 = f0/sqrt(1+1/Qt), f2 = f0*sqrt(1+1/Qt). Regression: 5%, VSWR 2 -> Qt = 14.14, L/W = 1.07, 9.664/10.348 GHz. Source BALANIS-461, -462.
- `CHECK-pifa`: inputs L, W, ws, h, er, f_target, y0 -> f = c/(4*(L + W - ws - h)*sqrt(er)) -> pass if abs(f - f_target)/f_target <= 3% (first-cut; finish in full-wave) and y0 < L/2 -> margin. Regression: L = 3.2, W = 2.474, ws = 1.059, h = 0.448 cm, er = 1 -> ~1.8 GHz. Source BALANIS-472..474.
- `CHECK-ifa-slot-length`: inputs f, er, arm length L (IFA) or slot length -> L_IFA = c/(4 f sqrt(er)); L_slot = lambda/2; slot width <= 0.1 lambda -> pass within 3%. Regression: 1.8 GHz, er = 2.33 -> 2.73 cm. Source BALANIS-475, -477, -478.
- `CHECK-dra-cylindrical`: inputs mode, a, h, er, f_target, BW_req, VSWR -> z = a/h within window; f_r, Q by (14-108)-(14-110); BW = (VSWR-1)/(Q sqrt(VSWR)) -> pass if abs(f_r - f_target)/f_target <= 3% and BW >= BW_req -> margins. Regression: Table 14.3 (er = 38, a = 0.6415, h = 0.2810 cm) -> TE01d 3.988 GHz Q 41.92; TM01d 6.175 GHz Q 46.34; HE11d 5.262 GHz Q 31.24; Example 14.10 -> a = 0.2653, h = 0.1020 cm, er = 38 gives 10 GHz, Q = 40. Source BALANIS-487..494.
- `CHECK-patch-array-coupling`: inputs edge spacing s/lambda0, arrangement (E or H plane) -> flag if E-plane arrangement with s > 0.10 lambda0 (surface-wave coupling dominant) or H-plane with s < 0.10 lambda0; require full-wave S12 when abs(S12) spec is tight. Source BALANIS-457.
- `CHECK-corporate-qw`: inputs Z_in_side, Z_out_side -> Z_T = sqrt(Z1*Z2) (e.g. 50 <-> 100 ohm -> 70.7 ohm), section length lambda_g/4 at f0. Source BALANIS-465.

### Ch 15 — Reflector antennas

- `CHECK-reflector-geometry`: inputs f, d -> theta0 = 2*atan(1/(4 f/d)) (equivalently eq.15-24); report subtended angle; regression f/d = 0.5 -> 53.13 deg; f/d = 0.385 -> 66 deg. Source BALANIS-526.
- `CHECK-reflector-efficiency`: inputs feed pattern Gf(th') (symmetric; or cos^n with G0 = 2(n+1)), f/d -> eps_s, eps_t, eps_ap by numerical integration (15-55, 15-61, 15-62) -> pass if eps_ap >= spec (practical 0.65-0.80) and feed edge taper within 9-10 dB (total rim ~ -11 dB) -> margins. Regression: Ex.15.3 (6 cos^2, f/d 0.5) -> eps_ap = 0.75, eps_s = 0.784, eps_t = 0.9566. Source BALANIS-529..535.
- `CHECK-reflector-gain`: inputs d, f, eps_ap, surface rms sigma, max phase error m, other eps (blockage, x-pol, line loss) -> D = (pi d/lambda)^2*eps_ap*exp(-(4 pi sigma/lambda)^2)*(1 - m^2/2)^2 -> pass if G_dBi >= spec; also flag if lambda < 4*pi*sigma*1.5 (near/below Ruze optimum wavelength) -> margin (dB). Regression: Ex.15.3 -> 48.69 dB; with m = pi/8 -> 48.0 dB. Source BALANIS-536, -538.
- `CHECK-ruze-max`: inputs d, sigma, eps_ap -> q = log10(d/sigma); Dmax(dB) = 20q - 16.38 + 10 log10(eps_ap) at lambda = 4*pi*sigma -> report usable upper frequency. Source BALANIS-538.
- `CHECK-corner-reflector`: inputs alpha, s, Da, h, feed length, grid spacing g, lambda -> pass if lambda < Da < 2 lambda, lambda/3 < s < 2 lambda/3 (90 deg), h in 1.2-1.5 x feed length, g <= lambda/10, and s below the multi-lobe threshold for alpha (0.7/0.95/1.2/2.5 lambda). Source BALANIS-521..523.
- `CHECK-spherical-aperture`: inputs R, lambda, allowed total phase error (wavelengths) -> a_max = R*(14.7*(Delta/lambda)/(R/lambda))^(1/4); regression Ex.15.4 -> 1.78 ft. Source BALANIS-543, -544.

### Ch 16 — Smart antennas

- `CHECK-array-spacing-smart`: inputs d (m), f_max, scan range -> pass if d <= lambda_min/2 (Nyquist/aliasing and grating-lobe free) and, when diversity is required, d >= lambda/2 at the band of interest -> margin = lambda_min/(2d) - 1. Source BALANIS-570.
- `CHECK-lms-stepsize`: inputs covariance estimate Rxx (or max input power) and mu -> lambda_max = max eig(Rxx) -> pass if 0 < mu < 1/lambda_max (use a margin, e.g. mu <= 0.1/lambda_max, for noise) -> margin = 1/(mu*lambda_max) - 1. Source BALANIS-568.
- `CHECK-training-overhead`: inputs training length, payload length -> ratio -> pass if <= 0.2 (book: >= 20% erases the smart-antenna throughput gain) -> margin = 0.2/ratio - 1. Source BALANIS-574.
- `CHECK-null-depth-coupling`: inputs designed null angle/depth, embedded (coupled) element patterns or coupling matrix C -> recompute AF with coupling -> flag if null shifts > tolerance (example: 30 -> 32.5 deg, depth only -35 dB). Source BALANIS-567.

### Ch 17 — Antenna measurements (priority)

- `CHECK-farfield-range`: inputs D (m), f (Hz), R (m) -> lambda = c/f; R_ff = 2*D^2/lambda; phase_err_deg = 180*D^2/(4*lambda*R) (derived from path difference D^2/(8R)) -> pass if R >= R_ff (phase_err <= 22.5 deg); margin = R/R_ff - 1. Source BALANIS-600.
- `CHECK-vswr-return-loss`: inputs S11 (complex or dB) or VSWR, Z0 -> abs(G) = (VSWR-1)/(VSWR+1); RL = -20*log10(abs(G)); mismatch loss = -10*log10(1-abs(G)^2); P_refl/P_inc = abs(G)^2 -> pass if VSWR <= VSWR_max (book's usual antenna bandwidth criteria: S11 <= -10 dB / VSWR <= 2, abs(G) <= 1/3, and VSWR <= 1.5 when quoted at "-15 dB") across the band -> margin = RL - RL_min (dB). Source BALANIS-639, -201, -453.
- `CHECK-impedance-from-slotted-line`: inputs VSWR, x_n (m), n, lambda_g, Zc -> abs(G) from VSWR; psi = 4*pi*x_n/lambda_g - (2n-1)*pi (choose sign per convention); Z_ant = Zc*(1+G)/(1-G) -> report Z_ant and compare to model. Source BALANIS-640.
- `CHECK-mismatch-loss-circuit`: inputs Z_ant, Z_cct -> P_lost/P_avail = abs((Z_ant - conj(Z_cct))/(Z_ant + Z_cct))^2 -> pass if <= budget (e.g. 0.5 dB). Source BALANIS-638.
- `CHECK-two-antenna-gain`: inputs R, f, Pr/Pt (dB), identical flag -> G_sum = 20*log10(4*pi*R/lambda) + 10*log10(Pr/Pt); G = G_sum/2 if identical -> pass if G within spec +/- measurement tolerance and R >= 2D^2/lambda. Source BALANIS-627, -629.
- `CHECK-three-antenna-gain`: inputs R, f, P_ab, P_ac, P_bc (dB ratios) -> S = 20 log10(4 pi R/lambda); Ga = (Sab + Sac - Sbc)/2 where Sxy = S + Pxy; similarly Gb, Gc -> report. Source BALANIS-628.
- `CHECK-gain-transfer`: inputs GS (dB), PT, PS (dBm) -> GT = GS + PT - PS; CP: GT = 10*log10(10^(GTV/10) + 10^(GTH/10)). Source BALANIS-632, -633.
- `CHECK-radiation-efficiency`: inputs G_meas (dBi), D_meas (dBi) -> e = 10^((G-D)/10) -> pass if e >= e_req. Source BALANIS-637.
- `CHECK-nearfield-sampling`: inputs f, dx, dy (planar) or a (m), dphi, dz, dtheta; z0; scan extent and edge level (dB) -> pass if dx, dy <= lambda/2; z0 >= 2*lambda (prefer 3*lambda); edge level <= -45 dB; cylindrical dphi <= lambda/(2(a+lambda)), dz <= lambda/2; spherical dtheta, dphi <= lambda/(2(a+lambda)) -> margin = min(limit/actual - 1). Also M = a/dx + 1, N = b/dy + 1. Source BALANIS-616, -617.
- `CHECK-catr-quietzone`: inputs QZ scan phase p-p (deg), amplitude ripple p-p (dB), taper (dB), reflector size (m), surface error rms (m), f_min, f_max, dual flag -> pass if phase < 10 deg, ripple < 1 dB, taper < 1 dB, size >= 25*c/f_min, surface error < 0.007*c/f_max (/2 if dual) -> margins. Source BALANIS-609..612.
- `CHECK-pattern-dynamic-range`: inputs measured noise floor vs peak (dB), cross-pol level -> pass if dynamic range >= 40 dB and cross-pol <= -40 dB (good design). Source BALANIS-621, -636.
- `CHECK-scale-model`: inputs n, full-scale f, dims, sigma -> model f' = n*f, dims/n, sigma' = n*sigma (flag if not achievable; then G = D*e via separate efficiency), RCS_full = n^2 * RCS_model -> regression: n = 3 -> 9.54 dB. Source BALANIS-647..649.
- `CHECK-rcs-flat-plate`: inputs A (m^2), f -> RCS_max = 4*pi*A^2/lambda^2 -> regression 0.09 m^2 @ 5 GHz -> 28.274 m^2 (14.51 dBsm). Source BALANIS-649.
- `CHECK-axial-ratio-db`: inputs AR (linear) or envelopes (dB) -> AR_dB = 20*log10(AR) -> regression 1.122 -> 1.0 dB, 2.24 -> 7.0 dB; pass if AR_dB <= spec (e.g. 3 dB). Source BALANIS-645, -646.

### Appendices

- `CHECK-band-letter`: input f (Hz) -> IEEE radar letter per App.IX.5 table -> use to label requirements/test plans consistently. Source BALANIS-683.


## 4. Verification procedures & plots

### Ch 9 (tail) — Broadband dipoles, matching techniques

- Quarter-wave / multi-section transformer: plot abs(Gamma_in) (linear) vs f/f0 over 0..2 for single-section, N-section binomial and N-section Chebyshev (Fig 9.26 style); good = abs(Gamma_in) <= rho_m across df/f0; binomial monotone, Chebyshev equal-ripple with N ripple extrema. Source p.518 Fig 9.26.
- Vivaldi: S11 (dB) vs frequency 0-25 GHz; bandwidth read at S11 = -10 dB (Example: 8.6-23.9 GHz, 2.77:1); E- and H-plane cuts at f0 should be symmetric end-fire beams. Source p.499 Fig 9.12, 9.14.
- Printed bow-tie with balun: S11 vs f with and without balun at -15 dB threshold (VSWR 1.5); expect balun-limited bandwidth. Patterns in principal E (y-z), secondary E (x-z) and H (x-y) planes, simulated vs measured. Source p.495.
- Dipole thickness study: Rin and Xin vs l/lambda (0-1.6) for l/d = 25, 50, 1e4; good = flatter curves for smaller l/d. Source p.502 Fig 9.17.

### Ch 10 — Traveling-wave and broadband antennas

- Yagi: E- and H-plane patterns (dB, polar); element-center current magnitude vs element number; directivity and F/B (dB) vs reflector spacing 0.1-0.5 lambda and vs director spacing 0.1-0.5 lambda (Fig 10.23/10.24). Good = F/B peak near 0.23 lambda reflector spacing with smooth directivity; director spacing kept below the steep drop (~0.4-0.45 lambda). Directivity vs f/f0 (Fig 10.26) shows the high-side roll-off; set f0 at the top band edge. F/B definition: 20*log10(abs(E(90,90)/E(90,270))). Source p.569-574.
- Helix: 3-D power pattern for ordinary vs Hansen-Woodyard phasing; directivity by numerical integration (not only Kraus formula); VSWR vs frequency of the feed transition (VSWR<2 bandwidth). Source p.557-558.
- Long wire: maxima and null angles vs length 0.5-10 lambda (Fig 10.7) for designing beam direction. Source p.541.

### Ch 11 — Frequency-independent antennas, small-antenna limits, miniaturization, fractals

- Small-antenna Q: plot Q vs ka (0.1-1.5) with the Chu/McLean curve and efficiency-scaled curves (e = 100, 50, 10, 5%); overlay the design's simulated Q (from input impedance: Q ~ X/R at resonance or from FBW). Good = design point within ~1.5x of the limit. Source p.617 Fig 11.17.
- LPDA: input impedance (R, X) vs log(frequency) should be periodic with period ln(1/tau) and small ripple; gain, VSWR, E/H HPBW vs frequency over the band (Fig 11.12); voltage/current along the feeder (transmission region vs active region). Source p.605-608.
- Spiral: on-axis axial ratio vs frequency; lower cutoff at AR = 2:1 (Fig 11.3). Source p.597.
- Miniaturized antenna: report realized gain, radiation efficiency, S11 (dB) and FBW at S11 = -10 dB side by side with the unminiaturized reference. Source p.619-625.

### Ch 12 — Aperture antennas

- Aperture antennas: principal E- and H-plane amplitude patterns (dB) vs theta for ground-plane-mounted and free-space versions; 3-D field pattern; E-plane of finite ground plane compared with GTD (edge diffraction) and measurement. p.652-654, p.704-706.
- Beam efficiency vs half-cone angle (Figs 12.15, 12.21) for candidate distributions to judge main-lobe capture. p.666, p.677.
- Dielectric-covered aperture E/H-plane patterns for several cover thicknesses (Fig 12.27). p.696.
- Narrow slot lambda*Ga and lambda*Ba vs b/lambda (0-1) (Fig 12.30). p.702.

### Ch 13 — Horn antennas

- Horn pattern verification: E- and H-plane amplitude patterns (dB, 0-60 dB range) aperture-model vs MoM/GTD vs measured (Fig 13.20, 13.28); good = main lobe and first sidelobes match the Fresnel model, back lobes match MoM/measurement. p.748-760.
- Horn design sweeps: HPBW vs flare angle for several lengths (Figs 13.6, 13.13) and normalized directivity vs aperture size (Figs 13.7, 13.14) — pick the optimum-directivity point. p.730-742.
- Standard-gain horn: gain vs frequency (measured vs computed vs manufacturer, Fig 13.23, 8-12 GHz); VSWR vs frequency (< 1.1; aperture-matched lower, Fig 13.34). p.752, p.768.
- Corrugated/aperture-matched comparisons: E-plane back-lobe level and HPBW vs frequency 7-16 GHz (Fig 13.32c,d). p.765.
- Phase center: phase-center position vs flare angle for E- and H-plane (Fig 13.37); verify the feed phase center at the reflector focus. p.774-775.

### Ch 14 — Microstrip and mobile communications antennas (priority)

- Patch S11 (dB) vs frequency, simulated and measured on the same axes (Fig 14.21b, 14.25b): good = minimum at f_r (within ~1-2%), depth < -10 dB (VSWR 2) across BW_req. Instrument: VNA, SOLT to the connector plane; ground plane size recorded (10 x 10 cm in the book). p.809, p.819.
- Input impedance R and X vs frequency (Fig 14.30): peak R at resonance; X symmetric; X at resonance = feed reactance (Xmin+Xmax)/2 — large offset flags thick-substrate probe inductance. p.826.
- Normalized Rin(y0)/Rin(0) vs y0/L (0..1) cos^2 curve (Fig 14.11b); overlay achievable fab tolerance band. p.796.
- Principal-plane patterns: E-plane (plane of L) and H-plane (plane of W), 2-D polar in dB, simulated vs measured vs cavity model; expect E-plane asymmetry toward the feed side; E-plane null at grazing with dielectric-covered ground. p.809, p.819.
- Directivity of one and two slots vs W/lambda0 (0.25-0.75) for h = 0.01 and 0.05 lambda0 (Fig 14.22); directivity vs h/lambda0 for er = 2.55 and 10.2 (Fig 14.23). p.812-814.
- Efficiency e_cdsw and percent bandwidth vs h/lambda0 (0-0.1) for er = 2.2 and 10 at constant f_r (Fig 14.29): pick h where BW meets spec before efficiency collapses. p.825.
- Circular patch Grad and D0 vs ae/lambda0 (0-1) (Figs 14.27, 14.28); D0 -> 4.8 dB at small ae. p.822-823.
- Mutual coupling abs(S12)^2 (dB) vs s/lambda0 (0-1.25) for E-plane and H-plane arrangements (Fig 14.32); G12 vs s/lambda0 (0-3) (Fig 14.33). p.828-829.
- Phased-array scan: abs(Gamma(theta0)) broadside-matched vs scan angle 0-90 deg for E- and H-planes with 2:1 VSWR line (abs(Gamma) = 1/3); scan blindness shows as abs(Gamma) -> 1 (Fig 14.42, 14.44). p.836-838.
- CP patch: axial ratio vs frequency on boresight; f1/f2 split per (14-94). p.831.
- PIFA/IFA: S11 vs frequency (1.74-1.86 GHz in examples), 3-D and E/H-plane patterns (Figs 14.47-14.48, 14.52-14.53). p.841-845.
- DRA: S11 and R/X vs frequency with -10 dB bandwidth marked (Fig 14.64: 10.69 GHz, 7.02%); E- and H-plane patterns. p.857.

### Ch 15 — Reflector antennas

- Reflector design curves: aperture efficiency and taper/spillover efficiencies vs half-angle theta0 (or f/d) for candidate feed patterns (Figs 15.20, 15.24, 15.25); good = operating f/d at the efficiency peak (~82% ideal, 74-79% corrugated horns). p.903-910.
- Directivity vs d/lambda with Ruze roughness for several smoothness indices q (Fig 15.27): shows the maximum-gain wavelength lambda_max = 4 pi sigma. p.914.
- Principal E/H secondary patterns and aperture-plane amplitude contours (Figs 15.14-15.15); co- vs cross-pol cuts in the 45-deg planes (Fig 15.16). p.894-896.
- Corner reflector: normalized azimuth patterns vs feed spacing (Fig 15.5) and on-axis abs(E/E0) vs s/lambda 0-10 (Figs 15.6, 15.7). p.881-883.

### Ch 16 — Smart antennas

- Beamformer verification: array factor (dB) vs angle with SOI/SNOI markers, with and without mutual coupling (Fig 16.27, 16.30, 16.31, 16.43); good = maximum at SOI, null depth at SNOI meeting spec (e.g. >= 40-48 dB below Chebyshev response). p.952-970.
- Element design check: abs(S11) (dB) vs frequency with -3 dB and -10 dB bandwidth markers (Fig 16.38); E/H patterns cavity model vs full-wave (Fig 16.39). p.966-967.
- System: throughput vs load and delay vs load for array sizes, tapers and training lengths (Figs 16.42, 16.44-16.46); BER vs SNR for uncoded/TCM, AWGN/Rayleigh, with/without interferer (Figs 16.47-16.49). p.969-974.

### Ch 17 — Antenna measurements (priority)

- Range qualification (before any pattern/gain run): compute 2D^2/lambda for the largest test aperture; for a CATR or chamber, scan the quiet zone with a probe: plot amplitude (dB) and phase (deg) vs transverse position; good = phase within 10 deg, ripple < 1 dB p-p, taper < 1 dB over the stated QZ (Fig 17.8 style). Absorber reflectivity <= -40 dB at the lowest frequency. p.982-989.
- Radiation patterns: principal E- and H-plane cuts (co- and cross-polarized), polar plot in dB with >= 40 dB dynamic range; elevation (great-circle) and azimuth (conical) cuts as needed; receiving mode for reciprocal antennas; record positioner angle synchronously. Good = sidelobes and cross-pol meet spec; cross-pol <= -40 dB for good linear designs. p.1000-1003, p.1012.
- Near-field range: planar grid <= lambda/2 spacing, z0 >= 2-3 lambda, scan until edges <= -45 dB, both polarizations, probe-compensated; transform by FFT; validate against a far-field range cut (Fig 17.15: sum and difference patterns overlay within a few dB down to -40 dB). p.993-999.
- Gain: choose venue by frequency (above 1 GHz free-space; 0.1-1 GHz ground reflection; below 50-100 MHz in situ). Use gain transfer against a lambda/2 dipole (~2.1 dB) or standard-gain pyramidal horn (12-25 dB) with back-to-back mounting; absolute calibration by two-/three-antenna or extrapolation methods; correct for impedance and polarization mismatch from measured Gamma and polarization. Plot gain vs frequency (swept-frequency setup, Fig 17.22b). p.1003-1010.
- Directivity: numerically integrate measured 3-D pattern (both polarizations) -> D0 = D_theta + D_phi; HPBW formulas only for rough estimates. p.1010-1012.
- Radiation efficiency: e = G/D from the same measurement campaign; for small series-R antennas: R_loss = R_in - R_rad. p.1012.
- Impedance: VNA S11 (magnitude dB and Smith chart) at the antenna terminals, measured in situ; acceptance by VSWR/return-loss limit across band (book examples use S11 <= -10 dB / VSWR 2, and -15 dB ~ VSWR 1.5); mutual coupling as abs(S21) between ports. p.1012-1014.
- Polarization: spinning-linear-probe axial-ratio pattern vs angle (dB envelopes; AR_dB = outer - inner); sense by CW/CCW CP reference or dual-pol amplitude+phase. p.1016-1019.
- Scale-model campaigns: scale f by n, dimensions by 1/n, verify with a canonical target (flat plate RCS offset of 20*log10(n) dB, i.e. n^2 in power). p.1019-1024.


## 5. Pitfalls, failure modes, review checklist

### Ch 9 (tail) — Broadband dipoles, matching techniques

- Balun-fed printed antenna bandwidth quoted without the balun is optimistic (15% -> 8.75% example). [p.495]
- Bow-tie design equations are patch-derived first cuts; expect a shift vs full-wave; always finish with simulation. [p.494-495]
- Vivaldi bandwidth is also limited by the microstrip-to-slot transition, Wmin and Wmax; check the transition separately. [p.497]
- Folded-dipole transmission-line model is inaccurate at larger spacing unless the equivalent radius ae = sqrt(a*s) is used. [p.510]
- Folded dipole isolated impedance (~300 ohm) changes when placed in an array or near a reflector (Yagi feed). [p.510-511]
- Discone below cutoff (slant height < lambda/4) is inefficient and produces severe standing waves on the feed. [p.512]
- Coax feeding a balanced dipole without a balun puts current on the outside of the shield (I3); fit a balun. [p.521]
- Single-stub match cannot match every load; use double/triple stub or re-position. [p.513]
- Multi-section transformer small-reflection formulas assume small rho_n (RL ~ Z0). [p.515]

### Ch 10 — Traveling-wave and broadband antennas

- Kraus helix directivity formula overestimates: example 15.4 dB (formula) vs 11.03 dB (ordinary end-fire numerical) and 14.21 dB (Hansen-Woodyard). [p.557-558]
- Normal-mode helix is very narrowband with very low radiation efficiency; do not rely on it without verifying efficiency. [p.553]
- Beverage antenna wastes power in its termination load: use primarily for receive. [p.542]
- Yagi director spacing beyond ~0.4 lambda collapses directivity; F/B is hypersensitive to spacing in long Yagis (20-25 dB over 0.05 lambda). [p.571]
- Yagi designed exactly at band center loses gain above f0; design at the top band edge. [p.572]
- Yagi input impedance drops steeply as the reflector moves closer (12 ohm at 0.10 lambda). [p.575]
- Metal boom without element-length compensation detunes NBS designs; wooden booms change with moisture. [p.578]
- A dipole longer than ~1.25 lambda loses directivity to sidelobes. [p.543]

### Ch 11 — Frequency-independent antennas, small-antenna limits, miniaturization, fractals

- Claimed small-antenna bandwidth beyond the Chu limit implies loss (low efficiency) — check efficiency, not just S11. [p.616-619]
- A shortened antenna with S11 near 0 dB (Rr << Z0) is not matched; realized gain collapses (e.g. -18.85 dB water-loaded monopole). [p.623]
- Dielectric loading that shortens by sqrt(er) can multiply volume (x118-x199) — compare volume, not length. [p.623-624]
- Metamaterial miniaturization results are mostly simulation-only; require measured data. [p.619-620, p.627]
- LPDA without termination reflects residual energy into the active region. [p.614]
- LPDA directivity from original Carrel curves is 1-2 dB too high. [p.609]
- Spiral with an unbalanced feed needs a balun that limits bandwidth; feed precision sets upper frequency. [p.597]
- Self-complementary spiral measured impedance (~164 ohm) is below the ideal 188.5 ohm. [p.597]

### Ch 12 — Aperture antennas

- Directivity 4*pi*ab/lambda^2 assumes Ha = Ea/eta over the aperture; numerical far-field integration gives ~0.3 dB more for a 3x2 lambda aperture. [p.660]
- Uniform illumination cannot meet sidelobe specs tighter than -13.26 dB (rectangular) or -17.6 dB (circular). [p.656, p.673]
- Simple HPBW formulas (50.8 lambda/b etc.) require dimensions >> lambda. [p.656, Table 12.1]
- Finite ground planes change low-level pattern regions (back and near-grazing) — include edge diffraction. [p.702-707]
- Circular ground planes create axial minor lobes from rim diffraction (ring source). [p.707]
- Slot antennas radiate on both sides unless cavity-backed. [p.682]
- EOC Table 12.3 lists 1.086*pi for the uniform circular aperture while eq.(12-65)/Example 12.5 use 1.079*pi (13.559 at 30 deg). [p.678-679]

### Ch 13 — Horn antennas

- Over-flared horn: main maximum can leave boresight; check s, t before trusting on-axis gain. [p.726-748]
- Simple Fresnel-model patterns are wrong in the back-lobe region — use MoM/GTD for low-level specs. [p.747-748]
- Pyramidal horn with pe != ph cannot be built on the given feed waveguide. [p.747]
- Conventional square pyramidal horn: H-plane beam ~35% wider than E-plane, E-plane sidelobes only 12-13 dB down — not a symmetric-pattern feed. [p.770]
- Diagonal horns have -16 dB cross-pol lobes in the 45-deg planes — avoid where polarization purity matters. [p.770]
- Corrugations starting right at the waveguide-horn junction degrade VSWR — start them a short distance into the flare. [p.766]
- Narrow corrugation slots (w < lambda0/10) raise breakdown/corona concerns at high power (20 kW at 10 GHz shown OK). [p.766]
- Feed phase center off the reflector focus causes significant gain loss. [p.774]
- Dual-mode horns trade on-axis gain for symmetry and low sidelobes. [p.770]

### Ch 14 — Microstrip and mobile communications antennas (priority)

- Transmission-line slot conductance (14-8a) is ~2x the cavity value (0.00328 vs 0.00157 S) -> edge resistance and inset depth wrong; use (14-12). [p.798]
- Inset notch adds junction capacitance: resonance shifts ~1%; re-tune length after inset. [p.797]
- Inset near the patch center is hypersensitive to position (cos^2 slope); check fab tolerance. [p.797]
- Built patch resonated ~2% low (9.8 vs 10 GHz design) — budget for fringing-model error. [p.792, p.809]
- W/L > 2 lowers aperture efficiency. [p.796]
- Thick substrates (h > ~0.02 lambda0 probe; toward 0.05 lambda0) excite surface waves: lower efficiency, pattern/polarization degradation at dielectric/ground truncation. [p.783, p.786, p.824]
- Probe/line feeds are asymmetric -> cross-polarization from higher-order modes. [p.786]
- Probe feed reactance grows ~2x at an edge and ~4x at a corner; significant for thick substrates. [p.827]
- Feed-network radiation limits array cross-pol and sidelobes; move feeds behind the ground (probe/aperture). [p.834]
- Patch arrays can go scan-blind (E-plane ~72.5 deg example) from surface/leaky waves. [p.837]
- E-plane-collinear patches couple more at spacing > ~0.1 lambda0 (surface waves). [p.827-828]
- Carrel-style simple beamwidth formulas for patches are guidance only (E-plane beam very wide). [p.813]
- PIFA/lambda/4 shorted patches trade bandwidth and gain for size. [p.839]
- Book errata spotted during extraction: Fig 14.47 caption h = 0.048 cm (text 0.448 cm); Fig 14.52 caption W = 0.006 lambda (text 0.06 lambda); Example 14.7 prints eta0 = 367.7 (should be ~376.7 to reproduce 362.95 - j211.31); PIFA frequency eq. printed as "(10-98)"; Example 14.9 HE11d f_r values inconsistent with eq.(14-110a); Table 14.3 TE01d (er = 79) "2.9%" is 0.29% by arithmetic. [p.840-858]
- DRA hybrid-mode Q formulas deviate most for TM01d (35.7% at er = 38). [p.854]
- Resonator-grade ceramics (er >= 50) do not radiate efficiently; radiating DRAs use er ~5-30. [p.847]

### Ch 15 — Reflector antennas

- Corner reflector feed too close to the vertex: radiation resistance approaches loss resistance (low efficiency); too far: multiple lobes / on-axis null (s = lambda for 90 deg). [p.877-880]
- Offset reflectors fed with LP feeds generate cross-pol; CP feeds squint the beam. [p.885]
- Feed phase center not at the focus -> gain loss (defocus phase error). [p.910-911]
- Operating near/above the Ruze frequency (lambda <= 4 pi sigma) collapses gain. [p.913]
- Cassegrain subreflector blockage makes it unattractive below ~40 dB gain. [p.916]
- Front-fed reflectors need long feed lines (loss/noise) or put heavy equipment at the focus (blockage). [p.884]
- Aperture-distribution/PO models ignore rim diffraction — far sidelobes need GTD. [p.892, p.899]
- Spherical reflectors have line focus/spherical aberration — a single point feed limits usable aperture. [p.920-922]
- Table 15.1 n = 4 row totals are internally inconsistent as printed (feed+path = -10.78 vs -10.942 dB). [p.909]

### Ch 16 — Smart antennas

- Ignoring mutual coupling shifts and fills adaptive nulls (30 -> 32.5 deg, -35 dB). [p.955]
- MUSIC-type DOA fails for coherent multipath without spatial smoothing and needs precise array calibration. [p.948-949]
- Training overhead >= ~20% of payload wipes out smart-antenna throughput gains. [p.971]
- LMS cannot track fast fading (error floor above ~18 dB SNR at fmT = 0.002). [p.974]
- Element spacing > lambda/2 risks aliasing/misplaced nulls; >= lambda creates grating lobes. [p.968]
- Cavity-model patch dimensions (W 2.976 vs 2.247 mm at 20 GHz on Si) can be far from full-wave optimum on high-er substrates — always finish in full-wave. [p.965-966]

### Ch 17 — Antenna measurements (priority)

- Test distance shorter than 2D^2/lambda puts > 22.5 deg phase taper on the aperture: nulls fill and gain reads low. [p.981-982]
- Cyclic variation of measured gain with range separation = multiple reflections between antennas; increase separation/absorbers. [p.1008]
- Dipole gain standard is polarization-pure but its broad pattern picks up environment reflections; horns are more robust. [p.1006]
- Probe for near-field scans must not be CP nor have nulls in the region of interest (probe-correction coefficients blow up). [p.997]
- Oversampling the near field below lambda/2 adds nothing; zero-padding is the way to increase far-field resolution. [p.998]
- Planar NF/FF gives only a limited angular span (one hemisphere at best) — not for low-gain/omni antennas. [p.994]
- LPDA sources/feeds have moving phase centers; parabolic CATR single-reflector depolarizes more (low f/d). [p.989]
- Radiation-efficiency series-resistance method fails for lossy-dielectric-coated antennas or antennas over lossy ground. [p.1012]
- Input impedance measured on a range may differ from installed impedance (environment dependence) — measure in situ. [p.1014]
- Gain-transfer with non-pure (finite AR) source or standard introduces error; techniques valid only above ~50 MHz. [p.1010]
- Extrapolation method fails with two or more CP antennas. [p.1008]
- Current probes disturb the field unless leads are choked (turns ~lambda/50). [p.1014]
- Scale models: conductivity not scaled (should be n x) — acceptable only for very good conductors (~1e7 S/m and above). [p.1024]


## 6. Standards referenced

| Standard | Edition/year | Clause/table | Governs | Page |
|---|---|---|---|---|
| IEEE Std 145-1983 | 1983 | definitions | IEEE Standard Definitions of Terms for Antennas (surface-wave and leaky-wave antenna definitions quoted) | p.535 |
| NBS Technical Note 688 (Viezbicke) | Dec 1976 (reference list says 1968) | Table 10.6, Figs 10.27-10.28 | Yagi antenna design data (element lengths, spacing, boom compensation) | p.576-578 |
| IEEE 802.11 (MAC) | — | MAC protocol (RTS/CTS/ACK) basis | channel access protocol adapted for smart-antenna MANET simulations | p.961-964 |
| IEEE Std 149-1979 | 1979 | whole standard (Figs 17.3, 17.14, 17.16-17.18, 17.20-17.21, 17.23 drawn from it) | Standard Test Procedures for Antennas: ranges, instrumentation, pattern, gain, polarization, impedance measurement | p.982-1019 |
| ANSI/IEEE Std 148-1959 (Reaff 1971) | 1959/1971 | reference [53] | impedance measurement (waveguide/transmission-line measurement methods) cited for impedance techniques | p.1014 |
| IEEE radar band designations (as tabulated) | — | App. IX.5 | Letter-band frequency ranges HF..mm-wave | p.1063 |

## 7. Process / lifecycle guidance

Not applicable: this is an analysis/design text, not a product-lifecycle book. Step-by-step design procedures (patch, circular patch, DRA, LPDA, Yagi, helix, horn, quarter-wave transformers) are captured as rules and checks; measurement sequences in §4.

## 8. Coverage log

- Assigned range: source text lines 37000-73949 (end of file), read in order within each chapter with the Read tool
  in chunks of <= 1,100 lines. Not read line by line (content confirmed by heading/text scan only): Ch 12 problems
  (lines 50440-51052), Ch 13 references/problems (55989-56224), Ch 14 references/problems (63171-63576), the
  pure-math Appendices III-VIII (70921-73542) and the index (73697-73949). Front matter/TOC lines 1-1000 read for
  orientation.
- Reading order: Ch 9-11 (lines 37000-44923), then — after a session restart, to secure the priority chapters —
  Ch 14 (56225-63577) and Ch 17 (69073-70876) plus Appendix IX, then Ch 12 (44924-51053), Ch 13 (51053-56225),
  Ch 15 (63577-67144), Ch 16 (67144-69072). No gaps remain.
- Skipped by rule: long derivations (summarized as procedures), problem sets, reference lists, historical notes, index.
- Limitations: PDF-to-text OCR garbles many equations (Greek letters mapped to replacement glyphs, fractions split
  across lines); formulas were rebuilt from the surviving structure and cross-checked against the worked examples
  where possible (patch Ex.14.1-14.5, DRA Table 14.3, horn Ex.13.1-13.5, reflector Ex.15.3, LPDA Ex.11.1, Yagi
  tables); rows whose structure could not be confirmed are marked conf=medium/low. Figures are absent: graph-only
  data are cited by caption with the numeric anchors stated in the prose. Page numbers are the printed ones.
- Id range: BALANIS-200 ... BALANIS-683 (not contiguous; grouped by chapter).
- Lines 37000-38943 (p.492-531): end of §9.2 biconical (finite cones, unipole), §9.3 bow-tie, §9.4 Vivaldi, §9.5 cylindrical dipole, §9.6 folded dipole, §9.7 discone, §9.8 matching, references, problems (skipped). Bow-tie eq.(9-15a)/(9-15b) OCR-garbled (R_t form uncertain). Table 9.3 shape drawings missing; labels taken from the standard table layout.
- Lines 38943-42470 (p.533-590): Chapter 10 read in full; skipped the Pocklington/MoM derivation details (§10.3.3A-B, eqs 10-42..10-65) beyond the formulation summary, references, and problems 10.1-10.46.
- Helix equations (10-31)-(10-35c) and rhombic (10-21)-(10-23) partly OCR-garbled; transcribed in the standard Kraus/Balanis form consistent with the worked Example 10.1 numbers (which check: S = 0.231, p = 0.8337/0.8012, HPBW 34.2 deg, D0 = 34.65).
- Lines 42471-44923 (p.591-637): Chapter 11 read; derivations of §11.2 (Rumsey) and spiral surface equations skimmed; references and problems skipped. Eq.(11-38) OCR-garbled; Q rebuilt as X/R of (11-37) (conf medium).
- Lines 44924-51053 (p.639-718): Chapter 12 read; equivalence-principle derivations, spectral-domain/stationary-phase derivations (§12.9.2-12.9.3) and aperture-admittance integrals skimmed; references and problems 12.1-12.x skipped. Tables 12.1-12.3 transcribed; Figs 12.13/12.14/12.19/12.20 (TE10/TE11 beamwidth curves) are graphs without numeric anchors.
- Lines 51053-56225 (p.719-782): Chapter 13 read; aperture-field/Fresnel derivations (13-3..13-17, 13-20..13-38, 13-41..13-49) skimmed; references and problems 13.1-13.x skipped (verified by heading scan). Graph-only data (Figs 13.6-13.8, 13.13-13.15, 13.21, 13.37) not digitized; eq.(13-18c) OCR-garbled (structure per cited refs, conf medium).
- Lines 56225-63577 (p.783-874): Chapter 14 read in full (priority chapter); cavity-model field derivations (eqs 14-21..14-32, 14-47..14-49, 14-60..14-63, 14-70..14-75) skimmed; references and problems 14.1-14.50 skipped (verified by heading scan).
- OCR issues: Table 14.1 columns realigned; Table 14.2 reconstructed; four-probe phase sentence (p.830) interleaved/garbled; eq.(14-18b) exponent lost (restored as (L/W)^2, conf medium); DRA Q formula coefficients printed truncated (full-precision values confirmed by reproducing Table 14.3).
- Lines 63577-67144 (p.875-930): Chapter 15 read; aperture/current-distribution derivations (15-26..15-50) skimmed; references and problems 15.1-15.30 skipped. Graph-only data (Figs 15.20, 15.23-15.28) not digitized except numeric anchors given in text.
- Lines 67144-69072 (p.931-980): Chapter 16 read; array-factor and MMSE derivations summarized; references and problems 16.1-16.16 skipped. Network/BER results are simulation anchors from the cited ASU studies (graphs; numeric anchors only where stated in text).
- Lines 69073-70876 (p.981-1026): Chapter 17 read in full (priority chapter); NF/FF modal-expansion equations transcribed only as procedure (17-5..17-13); references skipped.
- Lines 70877-73949 (p.1027-1072): Appendices I-II (sinc and array-factor plots), III (Si/Ci/Cin integrals, tables), IV (Fresnel integrals), V (Bessel functions), VI (identities), VII (vector analysis), VIII (method of stationary phase) confirmed by text scan to be pure mathematical function tables/identities — not transcribed (compute with scipy.special). Appendix IX (frequency allocations) transcribed. Index (p.1065-1072) skipped.
