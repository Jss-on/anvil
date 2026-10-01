# Printed Circuits Handbook (7th ed.) — Anvil rulebook, Part 2 (Chaps. 20.4–37.8)

## 0. Citation

C. F. Coombs, Jr. and H. T. Holden (Eds.), *Printed Circuits Handbook*, 7th ed. New York, NY, USA: McGraw-Hill Education, 2016. ISBN 978-0-07-183395-0 (print), 978-0-071-83396-7 (eBook).

Chapter authors cited in this extraction: B. Hargin & M. I. Montrose (Ch. 20), S. Webb (Ch. 21), M. Jouppi (Ch. 22, 23; Ch. 23 edited from D. Edwards, 6th ed.), V. Solberg (Ch. 24, orig. D. Fritz), H. T. Holden (Ch. 25, 26, 27), M. Stickel (Ch. 28, 29), G. Parry (Ch. 30, 37), C. D. Dupriest & H. T. Holden (Ch. 31), M. Carano (Ch. 32), G. Milad (Ch. 33, 35), H. Nakahara (Ch. 34), D. A. Vaughan (Ch. 36).

**Chapters covered by THIS extraction (text lines 4050–8100 of 16154):** Ch. 20 §20.4 (differential signaling, from mid-section) through §20.10; Ch. 21 (Basics of PCB Design); Ch. 22 (Current Carrying Capacity); Ch. 23 (PCB Design for Thermal Performance); Ch. 24 (Embedded Components); Ch. 25 (Intro to HDI); Ch. 26 (Advanced HDI); Ch. 27 (CAM Tooling); Ch. 28 (Drilling); Ch. 29 (Precision Interconnect & Laser Drilling); Ch. 30 (Imaging & AOI); Ch. 31 (Multilayer Materials & Processing); Ch. 32 (Preparing Boards for Plating); Ch. 33 (Electroplating); Ch. 34 (Direct Plating); Ch. 35 (Surface Finishes); Ch. 36 (Solder Mask); Ch. 37 §37.1–§37.8 (Etching, partial).

**Chapters NOT read (assigned to other agents):** Ch. 1–19 and Ch. 20 §20.1–20.3 (lines 1–4049); Ch. 37 §37.8 (remainder) through Ch. 71 and Appendix (lines 8101–16154).

Note on figures/equations: the source is an eBook text extraction in which most equations, all figures and most tables appear only as the placeholder "Images" or a bare caption. Where an equation is a placeholder, the rule transcribes only the numeric anchors stated in prose (tagged `medium`/`low`, "eq. not in text"); where the prose gives enough worked numbers to reconstruct the equation, the reconstruction is checked against those numbers and tagged `medium`. Printed page numbers are not preserved in this extraction; citations use §chapter.section and figure/table numbers.

## 1. Design rules

| id | domain | rule statement | formula / limit (units) | inputs | applicability & conditions | verify by | source | conf |
|---|---|---|---|---|---|---|---|---|
| COOMBS-2001 | transmission-line | Differential pairs target the impedance most component vendors recommend for noise cancellation | Zdiff = 100 Ω or 85 Ω | Zdiff (Ω) | differential signaling (LVDS, SERDES) | calc | §20.4 | high |
| COOMBS-2002 | transmission-line | Loss is the principal SI concern for fast signals over long paths; ISI appears when degraded rise time ≈ bit period | f > 1 GHz AND length > 10 in (25.4 cm) → loss-dominated | f (GHz), length (in) | serial links | sim | §20.4.1 | high |
| COOMBS-2003 | transmission-line | Every multi-Gb/s SERDES link needs an end-to-end attenuation (link) budget | typical budget 10–15 dB end-to-end; lower with RX equalization | channel loss (dB) | multi-Gb/s SERDES | calc | §20.4.2 | high |
| COOMBS-2004 | transmission-line | Interconnect loss budget derived from TX/RX voltage levels (before pre-emphasis/equalization) | Attenuation_budget (dB) = 20*log10(V_RX,min / V_TX,min) | V_RX,min (V) receiver min input; V_TX,min (V) transmitter min output | SERDES channels | calc | §20.4.2, Ref. 15 (Johnson & Graham) | high |
| COOMBS-2005 | transmission-line | Budget BGA package loss at each end of channel | ≤ 0.5 dB per package end at f < 2 GHz; 0.8 dB per package at 3.0 GHz | f (GHz) | backplane/line-card channels | calc | §20.4.3 | high |
| COOMBS-2006 | connectors | Choose connectors with matched differential impedance so connector loss stays small | connector Zdiff = 85–100 Ω → loss "well under 3 dB" at target frequency | Zdiff (Ω), f_target | high-speed connectors | calc/measure | §20.4.3 | high |
| COOMBS-2007 | via | Budget via loss; mitigate with blind/buried vias, backdrilling, minimal/small pads, large antipads, nearby stitching vias/bypass caps | poorly designed via: 0.5–1.0 dB each at Gb/s; mitigated via: < 0.25 dB each | via count, stub length, pad count | Gb/s nets | sim | §20.4.3 | high |
| COOMBS-2008 | transmission-line | Below the crossover frequency (where dielectric loss begins to dominate), widening the trace reduces loss more than lowering loss tangent | applies for f < f_crossover | f, W (mil), Df | loss-budget trimming | sim | §20.4.4 | high |
| COOMBS-2009 | transmission-line | Reference loss anchors for 4.5-mil stripline (see §2 table T-20.25): 5.0 dB total at 4 GHz over 12 in (Er 3.75, Df 0.009) vs 10.0 dB over 17 in (Er 3.9, Df 0.02) | see T-20.25 | length (in), Er, Df, W | stripline, 4 GHz | sim | §20.4.4, Fig. 20.25 | high |
| COOMBS-2010 | materials | Standard-loss FR-4 (Df 0.02) has a crossover frequency ~75 % lower than low-loss material (Df 0.009) | 1.78 GHz vs 7.86 GHz for the two Fig. 20.25 cases | Df | material selection | sim | §20.4.4 | high |
| COOMBS-2011 | transmission-line | Channels with 12–18 dB loss are buildable inexpensively if TX pre-emphasis and RX equalization correct the loss, leaving margin for crosstalk/reflections; verify only by simulator including crosstalk & reflections | 12–18 dB channel loss with equalization | channel loss (dB) | SERDES | sim | §20.4.5 | high |
| COOMBS-2012 | pdn | PDN must hold rail ripple/fluctuation at or below target | ripple ≤ 5 % of V_rail | V_rail, ripple | all digital PDNs | sim/measure | §20.5.1, §20.5.3 | high |
| COOMBS-2013 | pdn | Lower Z_PDN by minimizing loop inductance and increasing capacitance: reduce loop area (incl. z), put power/return planes adjacent and close, widen conductors | Z = V/I (Ohm's law, time & frequency domain; Eq. 20.3 not in text) | stackup, loop geometry | PDN layout | sim | §20.5.2 | medium |
| COOMBS-2014 | decoupling | Bulk bypass capacitors hold DC voltage/current and are effective only at low frequency | bulk C = 1–1000 µF; useful up to ~10 MHz | C (µF) | PDN | calc | §20.5.3 | high |
| COOMBS-2015 | decoupling | Decoupling capacitors supply edge-transition charge up to a limited frequency; above that only plane-pair or on-die capacitance works | decoupling caps effective to ~200 MHz; plane pair/on-die above 200 MHz | f (MHz) | PDN | sim | §20.5.3 | high |
| COOMBS-2016 | decoupling | Capacitor impedance minimum is at self-resonance, where Z = ESR; above SRF the part is inductive and useless for local charge | f_SRF = 1/(2*pi*sqrt(L_mounted*C)) (Eq. 20.4 not in text; standard form); Z(f_SRF) = ESR | C (F), L_mounted = ESL + via/trace inductance (H), ESR (Ω) | discrete decoupling | calc | §20.5.4 | medium |
| COOMBS-2017 | decoupling | Paralleling N identical capacitors divides ESL and ESR and multiplies C | ESL_total = ESL/N; ESR_total = ESR/N; C_total = N*C | N, ESL, ESR, C | PDN | calc | §20.5.4 | high |
| COOMBS-2018 | decoupling | Mixing two capacitor values creates an antiresonance peak between their SRFs; check switching harmonics against it | example: 100 nF (SRF 16 MHz) ∥ 1 nF (SRF 170 MHz) → antiresonance at 120 MHz; harmonics of 10/20/30/40/60 MHz can radiate at 120 MHz | C1, C2, ESL, switching f | mixed-value decoupling | sim | §20.5.4, Fig. 20.30 | high |
| COOMBS-2019 | decoupling | Mounted inductance (ESL) of a decap = footprint (via placement vs pad, trace length/width) + distance to plane + plane spreading inductance; minimize all three for energy delivery below 200 MHz | ESL_mounted = L_footprint + L_via(distance to plane) + L_spreading (Fig. 20.31 values not in text) | via-to-pad distance, trace length, plane depth | discrete decaps | inspect/calc | §20.5.5 | medium |
| COOMBS-2020 | pdn | Plane-pair capacitance scales with area and dielectric constant and inversely with spacing | C = eps0*eps_r*A/d (Eq. 20.5 not in text; standard parallel-plate form) | A (m^2), d (m), eps_r | power/return plane pairs | calc | §20.5.5 | medium |
| COOMBS-2021 | pdn | Embedded power/return planes are the least-inductive charge source and take over where discrete caps go inductive | planes supply from ~150 MHz up into GHz; discrete caps cease at ~250 MHz upper limit | f | multilayer PDN | sim | §20.5.5 | high |
| COOMBS-2022 | materials | Standard FR-4 plane-pair capacitance density is limited; ultra-thin high-Dk laminates give 10–50× more | FR-4: min 2 mil, Dk ≈ 4.0, 49–68 pF/cm² (0.31–0.43 nF/in²); thin cores 8–14 µm (0.31–0.55 mil), Dk double-digit → 0.3–3.6 nF/cm² (2–23 nF/in²) | dielectric thickness, Dk | embedded capacitance | calc | §20.5.5, Table 20.2 (contents not in text) | high |
| COOMBS-2023 | return-path | Above 100 kHz all signals are RF: return current follows the path of least inductance, i.e., the reference plane directly under the trace; DC return follows least resistance | f > 100 kHz | f, stackup | all signal routing | inspect | §20.6.3 | high |
| COOMBS-2024 | emc | A conductive return path must exist with impedance below free space, otherwise free space becomes the return (radiation) | Z_return < 377 Ω | Z_return | all nets | calc | §20.6.3 | high |
| COOMBS-2025 | emc | Single-sided PCBs with digital components are unlikely to pass EMC unless edges are very slow and routes very short; add a 0 V reference plane (multilayer) | exception only if t_r/t_f > 1 µs and short routes | t_r, t_f, layer count | low-cost boards | review | §20.6.3 | high |
| COOMBS-2026 | return-path | Inductive reactance dominates trace impedance above 100 kHz; resistance can be ignored | X_L = 2*pi*f*L; example L = 100 nH, R = 10 mΩ: X_L = 630 mΩ @1 MHz, 63 Ω @100 MHz, 630 Ω @1 GHz (>377 Ω → radiates) | f (Hz), L (H) | return-path analysis | calc | §20.6.3, Eq. 20.6 | high |
| COOMBS-2027 | return-path | No high-speed digital signal (or power/return trace) may cross a slot, gap or split in its adjacent reference plane | crossings = 0 | trace routes, plane cutouts | all high-speed nets | inspect (DRC) | §20.6.4, Fig. 20.34 | high |
| COOMBS-2028 | grounding | Single-point grounding is only appropriate when all switching is slow; otherwise use multipoint (multiple connections to a single-point reference) | single-point OK only if all switching < 100 kHz–1 MHz | max switching f | grounding architecture | review | §20.6.8–20.6.9 | high |
| COOMBS-2029 | grounding | All ground/reference nets (digital, analog, chassis, ESD…) must eventually connect at one 0 V reference; PCB-to-chassis bonds via low-inductance standoffs, not wires | exactly one 0 V reference in system | net list of grounds | mixed systems | inspect | §20.6.9 | high |
| COOMBS-2030 | compliance | Protective-earth bond is legally mandated when hazardous voltage present | hazardous if V ≥ 42.2 VAC or ≥ 60 VDC (mains 115/230 VAC always hazardous) | V_max | product safety | review | §20.6.11 | high |
| COOMBS-2031 | compliance | AC/high-voltage traces must meet creepage (along insulation surface) and clearance (through air) distances from safety standards, plus ampacity/heating | creepage & clearance per applicable safety standard (Fig. 20.40 values not in text) | V, pollution degree, material group | hazardous-voltage nets | calc/inspect | §20.6.11 | high |
| COOMBS-2032 | mechanical | Provide at least two datums; the primary datum is a nonfunctional hole or surface feature, never an edge machined in a late secondary operation | ≥ 2 datums | fab drawing | all PCBs | inspect | §20.7.2, Fig. 20.41 | high |
| COOMBS-2033 | mechanical | Mechanically mounted assemblies are supported near the edge on at least three sides | support within 25 mm of edge on ≥ 3 sides | mounting geometry | mechanically mounted PBAs | inspect | §20.7.3 | high |
| COOMBS-2034 | mechanical | Support-interval limits by board thickness | 0.7–1.6 mm thick: support intervals ≤ 100 mm; > 2.3 mm: "1.3-mm intervals" [sic in text; likely 130 mm] | board thickness (mm) | mechanically mounted PBAs | inspect | §20.7.3 | high (text as printed) |
| COOMBS-2035 | mechanical | Steinberg max-deflection formula (mm units) predicts solder-joint life; compliant-lead parts tolerate ~2× the deflection of rigid packages | rated 10e6 stress reversals (sinusoidal) / 20e6 (random) (Eq. 20.7 not in text) | board L, thickness, component size/position | shock & vibration | calc | §20.8.1 | medium |
| COOMBS-2036 | mechanical | Fundamental (first) mode dominates fatigue; components at board center see max strain; raise f_n above the threat by clamped guides, ribs/stiffeners, extra mounts, snubbers | f_n from plate stiffness D (Eqs. not in text) | E, thickness, edge conditions | vibration design | sim | §20.8.2, Fig. 20.44 | low |
| COOMBS-2037 | requirements | Assign IPC performance class from end use | Class 1 general electronics; Class 2 dedicated service (uninterrupted service desired); Class 3 high reliability (military/medical, interruption may be life-threatening) | product use | all PCBs | review | §21.2.1 | high |
| COOMBS-2038 | dfm | Record IPC producibility level of the design | Level A general (preferred); Level B moderate (standard); Level C high complexity (reduced producibility) | feature sizes | all PCBs | review | §21.2.2 | high |
| COOMBS-2039 | process | Schematic conventions: flow left→right, inputs left/outputs right, power pins top, ground pins bottom, all pins of every symbol/gate shown, decoupling caps drawn next to their IC, connector pins at page edge | — | schematic | all designs | inspect | §21.3.1 | high |
| COOMBS-2040 | components | Footprint must carry: correct pad count/locations, solder-mask opening, paste opening, silkscreen outline, ref des, pin numbers, placement boundary, origin (pick point), orientation, part height | — | library | all footprints | inspect | §21.4.1 | high |
| COOMBS-2041 | components | Use an IPC land-pattern density level consistently (minimum / nominal / maximum) and IPC naming convention (type, lead span, size, height, pin count) | one level per library | library policy | SMT | review | §21.5 | high |
| COOMBS-2042 | components | For high-speed parts prefer packages with power and ground pins physically adjacent | — | package pinout | high-speed ICs | review | §21.5 | low |
| COOMBS-2043 | mechanical | Import board outline, holes, keepouts and connector positions from mechanical CAD (.dxf/.emn) onto a nonfunctional layer rather than redrawing | — | MCAD file | all PCBs | inspect | §21.6 | high |
| COOMBS-2044 | process | Database precision: metric boards 4 decimal places; imperial boards on 0.001 in grid with 2 decimal places | — | units | CAD setup | inspect | §21.6 | high |
| COOMBS-2045 | fab | Ask fabricator for their "normal" via/pad size and the smallest via hole without up-charge before setting default via | — | fab capability | all PCBs | review | §21.6 | high |
| COOMBS-2046 | stackup | Fix board thickness at project start; most common thickness 0.062 in; plan copper weights from current need | 0.062 in (1.6 mm) default | current, layer count | all PCBs | review | §21.6 | high |
| COOMBS-2047 | placement | Place BGAs on a grid of half the ball pitch; route on a quarter-pitch grid so fanout vias/traces are uniformly spaced | placement grid = pitch/2 (0.8 mm → 0.4 mm); routing grid = pitch/4 (0.2 mm) | ball pitch (mm) | BGA fanout | inspect | §21.7 | high |
| COOMBS-2048 | placement | Keep analog parts/signals in their own region, input→output "clothesline" order, no digital parts or traces in or through the analog region | digital crossings of analog region = 0 | placement regions | mixed-signal | inspect | §21.7, Fig. 21.16 | high |
| COOMBS-2049 | placement | Group each IC with its decoupling caps and termination devices so they move together | — | groups | all | inspect | §21.7 | high |
| COOMBS-2050 | placement | Part orientation (N-S vs E-W) no longer matters for modern pick-and-place | — | — | SMT assembly | review | §21.7 | high |
| COOMBS-2051 | placement | Group parts by logic family and voltage so one power layer can be split per voltage and signals stay within their region | — | supply nets | multilayer | inspect | §21.7 | high |
| COOMBS-2052 | return-path | Every power plane and every routing layer must have a return plane (normally ground) adjacent in the stack | — | stackup | all multilayer | inspect | §21.8 | high |
| COOMBS-2053 | grounding | Ground planes are never split; power planes may be divided into voltage regions; a signal returning on a power plane must have the same voltage as that region and not cross splits | ground splits = 0 | plane shapes | multilayer | inspect | §21.8 | high |
| COOMBS-2054 | stackup | Plane layers are solid copper, not cross-hatched | — | plane fill | multilayer | inspect | §21.8 | high |
| COOMBS-2055 | stackup | Prefer foil construction (foil + prepreg outer, cores alternating with prepreg inside): fewer cores and etch steps → lower cost | — | stackup | multilayer | review | §21.9 | high |
| COOMBS-2056 | stackup | Even number of layers with layer types mirrored about the centerline (balanced) to prevent warp; pour copper into open areas (tied to power/ground) to balance etch | layer count even; mirror symmetry | stackup | multilayer | inspect | §21.9 | high |
| COOMBS-2057 | pdn | Put a power/ground plane pair adjacent near the stack center with thin spacing for plane capacitance (not achievable in 4-layer) | plane pair spacing 0.003–0.010 in | stackup | ≥ 6-layer | inspect | §21.9 | high |
| COOMBS-2058 | stackup | At most two signal layers adjacent, and only with return planes on both sides; the outermost signal layer must have a plane beneath it (never two signal layers at the surface) | adjacent signal layers ≤ 2; outer signal layer must be plane-referenced | stackup | multilayer | inspect | §21.9, Fig. 21.19 | high |
| COOMBS-2059 | stackup | Any controlled-impedance stackup is coordinated with/checked by the fabricator (widths, spacing, dielectric distances) | — | stackup | controlled-Z boards | review | §21.9 | high |
| COOMBS-2060 | transmission-line | Even without a spec, control trace impedance layer-to-layer: pick one Z0 near 50–60 Ω and hold it on every layer (widths differ per layer) | Z0 target 50–60 Ω, same on all layers | stackup | all routing | calc | §21.10 | high |
| COOMBS-2061 | dfm | Trace width and spacing are generally equal; give any extra room to spacing; never use narrower traces than needed; check width fits between IC/BGA leads | space ≥ width | W, S, fab capability | all routing | inspect | §21.10 | high |
| COOMBS-2062 | routing | Fan out power connections to vias first; place BGA fanout early (X or + pattern so planes reach the BGA center) | — | BGA | dense boards | inspect | §21.10, Fig. 21.21 | high |
| COOMBS-2063 | routing | Use one grid (metric or imperial) for all fanout/via patterns so routing channels align | — | grid | dense boards | inspect | §21.10 | high |
| COOMBS-2064 | routing | Route the densest area (e.g., BGA escape) first; it sets layer count; establish a per-layer routing direction; adjacent signal layers route perpendicular | — | placement | multilayer | inspect | §21.10 | high |
| COOMBS-2065 | routing | Route critical/high-speed signals on internal layers; slower signals may use outer layers | — | net classes | multilayer | inspect | §21.10 | high |
| COOMBS-2066 | routing | Topologies: buses daisy-chain driver→loads; clocks star / branch-by-n; T-routing for lumped load groups | — | net classes | all | inspect | §21.10, Fig. 21.25 | high |
| COOMBS-2067 | routing | Routing order: 1 power fanout vias, 2 I/O, 3 critical nets, 4 lock criticals, 5 analog (isolated), 6 location-specific, 7 general | — | net classes | all | review | §21.10 | high |
| COOMBS-2068 | crosstalk | Same-bus signals switching together may be channelled at spacing = trace width; dissimilar signals at minimum spacing risk crosstalk | S_bus = W acceptable; S_mixed > minimum | W, S, net classes | bus routing | inspect | §21.10, Fig. 21.26 | high |
| COOMBS-2069 | dfm | Trace entry into a pad must not form an acute angle | entry angle ≥ 90° | trace/pad geometry | all | inspect (DRC) | §21.10 | high |
| COOMBS-2070 | assembly | Trace width entering a pad ≤ ~60 % of pad width (thermal balance during soldering) | W_trace ≤ 0.6 * pad size | W, pad | SMT pads | inspect (DRC) | §21.10 | high |
| COOMBS-2071 | routing | Do not route traces on power or ground layers (they cut the return region) | traces on plane layers = 0 | layer usage | multilayer | inspect | §21.10 | high |
| COOMBS-2072 | decoupling | Via decoupling caps and IC power pins directly to the planes whenever pin-to-cap distance exceeds the limit | via to plane if distance > 0.100 in | cap-to-pin distance | all | inspect (DRC) | §21.10 | high |
| COOMBS-2073 | emc | Keep high-speed traces away from board edges | — | edge distance | high-speed nets | inspect | §21.10 | low |
| COOMBS-2074 | routing | Use larger vias for power connections layer-to-layer | — | via sizes | power nets | review | §21.10 | low |
| COOMBS-2075 | crosstalk | Extra spacing around clocks/strobes and around differential pairs relative to other routing and vias | — | net classes | clocks, diff pairs | inspect | §21.10 | low |
| COOMBS-2076 | timing | Serpentine length-matching loops keep 3–4 trace widths between segments so the signal does not couple across loops | loop gap = 3–4 × W | W | length-matched nets | inspect (DRC) | §21.10 | high |
| COOMBS-2077 | routing | Do not route unrelated signals through a BGA area | — | BGA regions | dense boards | inspect | §21.10 | high |
| COOMBS-2078 | routing | Layer-paired routing: when changing direction, switch to the signal layer on the other side of the same reference plane to contain return current | — | stackup | high-speed | inspect | §21.10, Fig. 21.27 | high |
| COOMBS-2079 | process | DRC must be clean (any accepted exceptions documented); also check unconnected nets/pins, differential pairs, noisy-signal adjacency, same-net spacing | DRC errors = 0 (or documented) | DRC report | all | inspect | §21.11 | high |
| COOMBS-2080 | process | Resequence reference designators in a grid (left→right, top→bottom; top side then bottom), back-annotate to schematic, re-import netlist to confirm sync | — | ref des | all | inspect | §21.11 | high |
| COOMBS-2081 | dfm | Silkscreen text/ref des must not fall on pads or vias (it is clipped in fab); use leader lines if needed | silkscreen-on-pad = 0 | silkscreen | all | inspect (DRC) | §21.11 | high |
| COOMBS-2082 | fab | Drill schedule lists every hole size, its tolerance, plated/nonplated, and quantity | hole tolerance usually ±0.003 in | drill table | fab drawing | inspect | §21.11 | high |
| COOMBS-2083 | fab | Stackup drawing lists layer name, copper weight, plating amount, dielectric thickness between layers, and impedance where controlled | — | stackup | fab drawing | inspect | §21.11 | high |
| COOMBS-2084 | fab | Deliver Gerber / ODB++ / IPC-2581, IPC-D-356 netlist, pick-and-place files, fab & assembly drawings, file list and contact; verify each output layer against the database after translation | — | output set | fab release | inspect | §21.11 | high |
| COOMBS-2085 | process | Save a dated copy of the design database daily and at milestones; on completion archive read-only master on network | ≥ several days retained | — | all | inspect | §21.12 | high |
| COOMBS-2086 | reliability | Arrhenius rule of thumb: every 10 °C rise halves component life; every 10 °C reduction doubles it — keep electronics as cool as possible | life(T+10 °C) = 0.5·life(T) | T_component | all | calc | §22.1 | high (as stated; author notes "whether exactly true or not") |
| COOMBS-2087 | current-carrying | Size traces with IPC-2152 baseline charts (not the superseded IPC-2221/MIL-STD-275 charts); baseline = polyimide, 1.78 mm (0.07 in) thick, no internal planes, still air, per IPC-TM-650 2.5.4.1a | ΔT_trace = f(I, cross-section) from IPC-2152 baseline chart (charts are figures, not in text) | I (A), W, Cu weight, ΔT allowed | all current-carrying traces | calc | §22.1, §22.3 | high |
| COOMBS-2088 | current-carrying | Cross-sectional area is the dominant variable for trace temperature rise; copper weight has only a small effect for the same area (most noticeable at high ΔT) | — | W × t (sq mil) | trace sizing | calc | §22.2.1, §22.3.1 | high |
| COOMBS-2089 | current-carrying | The old IPC-2221 internal chart was simply the external chart at ½ current (not test data); measured internal traces run similar to but slightly cooler than external traces (2001–2004 tests) | I_internal,old = 0.5·I_external,old | — | legacy designs | review | §22.2.1 | high |
| COOMBS-2090 | current-carrying | Trace temperature rise increases as board gets thinner; correct baseline ΔT for board thickness | example 1 oz internal 0.0088-in-wide trace at 1 A: ΔT = 10 °C @0.070 in; 12.1 °C @0.059 in; 13.3 °C @0.038 in board | board thickness (in) | thin boards, flex | calc | §22.3.4 | high |
| COOMBS-2091 | current-carrying | Board thermal conductivity is secondary to board thickness; dielectric k ≈ 0.354 W/m·K vs air 0.026 W/m·K, so traces in free air have the least capacity | k_dielectric ≈ 0.354 W/m·K; k_air ≈ 0.026 W/m·K | material | trace sizing | calc | §22.2.1, §22.3.3, Table 22.2 | high |
| COOMBS-2092 | current-carrying | A nearby copper plane reduces trace ΔT significantly; effect grows as trace-to-plane distance shrinks; IPC-2152 plane charts (ideal plane, no cutouts) are for margin estimation, not sizing | ΔT decreases with decreasing trace–plane distance (Fig. 22.9, values not in text) | trace-to-plane distance, plane size | boards with planes | calc | §22.2.1, §22.3.2 | medium |
| COOMBS-2093 | current-carrying | In vacuum, traces run hotter than in air and internal ≈ external temperature | vacuum charts (Fig. 22.10, values not in text) | environment | space/vacuum | calc | §22.3.5 | high |
| COOMBS-2094 | current-carrying | Use end-product (after-processing) copper thickness when sizing, per IPC-2221 Table 10-1 minimum internal foil thickness and external conductor thickness (Tables 22.3/22.4) | finished Cu thickness ≥ IPC-2221 Table 10-1 minimum (values not in text) | Cu weight, plating | all | inspect | §22.3.6 | medium |
| COOMBS-2095 | current-carrying | Parallel-conductor rule: closely spaced conductors carrying current simultaneously are evaluated as one conductor with equivalent cross-section = Σ areas and equivalent current = Σ currents (include traces above/below and side-to-side) | A_eq = ΣA_i; I_eq = ΣI_i | conductor list | buses, parallel power traces | calc | §22.3.7 | high |
| COOMBS-2096 | current-carrying | Estimate I²R power loss of all simultaneously energized conductors early; if it is a significant fraction of board power, redesign before layout | P_traces = Σ I_i²·R_i; compare to P_board | I, R | all | calc | §22.3.7 | high |
| COOMBS-2097 | current-carrying | Neck-downs around connector pins and planes with many via cutouts/keepouts are hot-spot risks requiring a thermal analysis tool | — | geometry | power distribution | sim | §22.3.7 | high |
| COOMBS-2098 | current-carrying | High-current pulses can fuse traces earlier than steady-state charts predict; do not extrapolate charts to pulses | — | pulse current | pulsed loads | measure | §22.3.8 | low |
| COOMBS-2099 | current-carrying | Baseline charts remain more accurate when extrapolating to higher current and cross-section > 700 sq mil | > 700 sq mil | area | heavy copper | calc | §22.3 | high |
| COOMBS-2100 | thermal | θ_ja is not a constant: it varies ≥ 2× with PCB layout; do not compute T_j = T_a + θ_ja·P for modern systems (JEDEC JESD51-2 §1.1) | θ_ja variation factor ≥ 2 | θ_ja | all component thermal estimates | review | §23.1, Ref. 1 | high |
| COOMBS-2101 | thermal | The PCB acts as the component heat sink and can dissipate 60–95 % of thermal energy if: large spreading planes, sparse population, long traces from component pins, adequate card spacing | 60–95 % | layout | all | sim | §23.2 | high |
| COOMBS-2102 | thermal | Conduction: Q = k·A·(T2−T1)/L (Fourier, Eq. 23.2 not in text); Cu conductivity is ~3 orders of magnitude above polymers, so Cu layout dominates | k_Cu ≈ 386 W/m·°C (also cited 380); k_FR-4 ≈ 0.8 W/m·°C; via Cu 0.389 W/mm·°C | k, A, L | all | calc | §23.3.1, §23.3.3–23.3.4, §23.6.3 | high |
| COOMBS-2103 | thermal | Table 23.1 conductivities valid at ~23 °C; re-source temperature-dependent data for operation > 85 °C or < −25 °C | — | T_op | extreme temps | review | §23.3.1 | high |
| COOMBS-2104 | thermal | Lengthen and widen traces attached to hot component pins; SOIC-8 @1 W on single-layer 1.57 mm FR-4: device ΔT changes ~40 % with trace length; diminishing returns beyond ~15 mm trace length | trace length ≥ 15 mm to pins where SI allows | trace L, W | leaded/SOIC parts | sim | §23.3.1, Fig. 23.3 | high |
| COOMBS-2105 | thermal | Use thickest available foil plus thickest electroplating for thermal traces; route them directly to thermal vias, side rails, or thermal screw holes | — | Cu thickness | thermal paths | review | §23.3.1 | high |
| COOMBS-2106 | thermal | Thermal-plane structure: thermal landing (collection plate) under exposed pad → thermal vias → continuous buried plane (power or ground); optional bottom landing for indirect heat sink; isolation so vias do not short other planes | — | stackup | exposed-pad packages | inspect | §23.3.2, Fig. 23.4 | high |
| COOMBS-2107 | thermal | Always solder exposed pads / thermal balls to a thermal collection land connected by thermal vias to a plane; use θ_jc / θ_jp from vendor; fix "floating package" by optimizing paste volume, never by deleting the thermal pad solder | — | package data | exposed-pad, BGA thermal balls | inspect | §23.3.2 | high |
| COOMBS-2108 | thermal | Maximize thermal spreading plane area near the component; 12×12 mm CSP with 49 thermal balls improves θ_ja by ≥ 2× going from small to large plane | improvement ≥ 2× | plane area | CSP/BGA | sim | §23.3.2, Fig. 23.6 | high |
| COOMBS-2109 | thermal | A dielectric break in a thermal plane is catastrophic: 1 mm FR-4 gap ≈ 1000 mm of Cu in thermal resistance; a 0.25 mm isolation slot halfway across a plane caused 29 °C drop across the slot and +33 °C component temperature (7×7 mm device) | k_Cu/k_FR4 ≈ 1000 | plane cuts | thermal planes | sim | §23.3.2, Fig. 23.7 | high |
| COOMBS-2110 | thermal | Deliberate isolation cuts may segregate parts that tolerate high T_j (e.g., regulators at 150 °C) from digital parts, provided the copper to the hot parts still carries the current | — | T_j limits, currents | mixed power/digital | sim | §23.3.2 | high |
| COOMBS-2111 | thermal | Use thickest Cu for thermal planes; if a plane is 0.5 oz (text: 23.8 µm), add a second plane to reach effective 1 oz; little gain once total spreading plane thickness > 2.8 oz | 0.5 oz → double; saturation at 2.8 oz total | plane Cu weights | thermal planes | calc | §23.3.2 | high |
| COOMBS-2112 | thermal | Thermal-via rules: ≥ 1 thermal via per BGA thermal ball; maximize via density under the landing within mechanical limits; maximize plating thickness; use nested (stacked) microvias in build-up, else shortest path to plane | ≥ 1 via/thermal ball | package, stackup | exposed pad, BGA | inspect | §23.3.3 | high |
| COOMBS-2113 | via | Thermal vias connect solid to the plane (no thermal-relief spokes/webs); exit side has a Cu ring; typical geometry 1.0–1.2 mm center-to-center, 0.3 mm drill, ≥ 0.025 mm Cu plating; through-hole thermal vias filled (solder, epoxy or solder mask) to prevent solder wicking | pitch 1.0–1.2 mm; drill 0.3 mm; plating ≥ 0.025 mm; relief spokes = 0 | via geometry | thermal vias | inspect (DRC) | §23.3.3, Fig. 23.8 | high |
| COOMBS-2114 | thermal | Single thermal via resistance from geometry; array resistance by parallel combination | R_via = L / (k·π·(r_o² − (r_o − t)²)) with r_o = d/2 [reconstructed from Eq. 23.3; reproduces the text's 45 °C/W]; R_array = R_via/N; example d = 0.3 mm, t = 0.025 mm, L = 0.38 mm, k = 0.389 W/mm·°C → 45 °C/W; 4×4 array → 2.8 °C/W; t = 0.015 mm → 73 °C/W | d (mm), t (mm), L (mm), k, N | thermal via arrays | calc | §23.3.3, Eqs. 23.3–23.4 | medium (formula reconstructed) / high (numbers) |
| COOMBS-2115 | fab | Verify thermal-via plating thickness by parallel polishing from the surface, not by cross-section (off-center sections under-read plating) | — | coupons | thermal vias | measure | §23.3.3 | high |
| COOMBS-2116 | thermal | Effective in-plane conductivity of a PCB is thickness-weighted; a single 0.036 mm plane in 1.57 mm FR-4 gives only 8.9 W/m·°C vs 386 for solid Cu | k_eff ≈ Σ(k_i·t_i)/Σt_i [reconstructed from Eq. 23.5; gives 8.85 for the example] | plane thicknesses, board thickness | spreading estimates | calc | §23.3.4 | medium |
| COOMBS-2117 | thermal | Spread power evenly; clustering four small devices on a 100×100 mm PCB with two buried planes raised max device T from 81.6 to 98.4 °C (≈30 % of rise above 25 °C ambient) | — | placement | all | sim | §23.3.4, Table 23.2 | high |
| COOMBS-2118 | thermal | Air heats 10–30 °C just downstream of a high-power device; place hot/critical parts upstream in the airflow; avoid leeward side of blockages, directly downstream of hot parts, and bottom center of a natural-convection board | ΔT_air = 10–30 °C downstream | airflow direction | forced/natural convection | sim | §23.3.4, §23.6.1 | high |
| COOMBS-2119 | thermal | Convection Q = h·A·ΔT (Eq. 23.6 not in text); h increases for smaller PCBs, vertical orientation, lower altitude, ducting | — | h, A | all | calc | §23.3.5 | medium |
| COOMBS-2120 | thermal | Radiation Q = ε·σ·A·(T⁴ − T_amb⁴) (Eq. 23.7 not in text; standard form); emissivity solder mask 0.85–0.95, bare Cu 0.1–0.3 | ε_mask = 0.85–0.95; ε_Cu = 0.1–0.3 | ε, A, T | all | calc | §23.3.5 | high (ε values) / medium (eq.) |
| COOMBS-2121 | thermal | Best-case natural-convection dissipation limits (horizontal, 25 °C, uniform power): 50 W cannot be dissipated by a 10×10 cm PCB; 15×15 cm rises 80 °C for 50 W; 20×20 cm rises 50 °C for 50 W | see T-23.9 | PCB area, P | natural convection sizing | calc | §23.3.5, Fig. 23.9 | high |
| COOMBS-2122 | thermal | Thermal chassis screw: PTH plated, tied to spreading plane, contact area for screw and standoff, located as close as possible to hot part; metal chassis (or Al plate molded into plastic); example gain 10 % | — | mount locations | chassis-cooled | inspect | §23.4.1 | high |
| COOMBS-2123 | thermal | Gap-filler selection: thickness, thermal conductivity, pliancy (higher k → less compliant) | — | gap, k | chassis-cooled | review | §23.4.2 | low |
| COOMBS-2124 | thermal | Extend thermal planes into edge-connector/edge-guide clamp zones with maximum contact area; cables plugged into connectors give unmodelled margin but must not block airflow | — | edge geometry | card-cage | inspect | §23.4.3 | low |
| COOMBS-2125 | emc | Perforate RF shields for airflow; hole size < λ/10 of the shielded frequency keeps shielding adequate; shield can be thermally bonded (epoxy/grease after soldering) to spread heat | perforation < λ/10 | f_shield | shielded RF/analog | calc | §23.4.4 | high |
| COOMBS-2126 | thermal | Components dissipating ≥ 2.5 W generally need attached heat sinks; 50–300 W parts need bolster-plate designs with 20–200 lb clamping, mylar isolation, and no components between PCB and bolster plate | P ≥ 2.5 W → heat sink; 50–300 W → bolster plate, 20–200 lb | P | high-power parts | review | §23.5 | high |
| COOMBS-2127 | thermal | Board thickness must carry heat-sink mass under shock/vibration when many heat sinks are attached | — | mass, thickness | heat-sinked boards | calc | §23.5 | low |
| COOMBS-2128 | thermal | Accuracy tiers for thermal prediction: CFD ±5 %; user-h codes ±10 % (without correlation); two-resistor (θ_jc, θ_jb) component model ±20 %; compact model ±5 % — request compact models from vendors | ±5 / ±10 / ±20 / ±5 % | model type | thermal sim | sim | §23.6, §23.6.2 | high |
| COOMBS-2129 | thermal | System thermal modeling in three phases: (1) airflow with all blockages (cables, shields, daughter cards, filters, drives…); (2) power areas on PCB; (3) detailed layout + components; also account for vents blocked by users and lifetime dust | — | — | system thermal | sim | §23.6.1 | high |
| COOMBS-2130 | thermal | Do not "smear" Cu layers by coverage-weighted averaging (100 % Cu 380 W/m·°C, 95 % → 360, 0 % → 0.8); it hides isolation cuts — model patches with parallel/series conductivities (Eqs. 23.8/23.9 not in text) | — | layer artwork | thermal sim | sim | §23.6.3 | high |
| COOMBS-2131 | thermal | In vacuum, θ_jc remains valid but case-to-board resistance degrades vs air; evaluate lead conduction per component; component-to-board radiation usually negligible | — | environment | space | calc | §23.7 | high |
| COOMBS-2132 | components | Embedded resistor value from sheet resistance and aspect ratio | R = R_s·(L/W) (Ω), R_s in Ω/square; 100 Ω/sq: 3 sq long × 1 wide = 300 Ω; 1 long × 2 wide = 50 Ω; 1 wide × 5 long = 500 Ω; 5 wide × 1 long = 20 Ω; general R = ρ·L/A with ρ_Cu = 7.09e−7 Ω·in²/in | R_s, L, W | embedded formed resistors | calc | §24.4.1, §24.6.1, Eq. 24.1 | high |
| COOMBS-2133 | components | Serpentine embedded resistor: count each straight square as 1.0·R_s and each right-angle corner square as 0.56·R_s | R = R_s·(N_straight + 0.56·N_corner) | square counts | serpentine resistors | calc | §24.4.1.3 | high |
| COOMBS-2134 | components | Embedded capacitor value | C = K·Dk·A/t with K = 8.854e−14 F/cm, A = L×W (cm²), t (cm) | A, t, Dk | planar/discrete formed caps | calc | §24.4.2, Eq. 24.2 | high |
| COOMBS-2135 | materials | Dk ranges for embedded capacitor dielectrics: epoxy/E-glass ≈ 4; BaTiO3-filled epoxy/polyimide 10–20; ceramic/inorganic 100–2000 | — | material | embedded caps | review | §24.4.2.2 | high |
| COOMBS-2136 | materials | Dielectric thickness options: 100 µm (4 mil) glass/epoxy baseline; 50 µm thin glass (2× C); filled polymer down to 8 µm (6–20× C of 100 µm baseline) | C ∝ 1/t | t | embedded caps | calc | §24.4.2.2 | high |
| COOMBS-2137 | materials | Capacitance density by dielectric type: PTF 20 pF/mm²; CTF ≈ 24 nF/mm²; planar capacitor dielectric ≈ 25 µm; values > 100 nF/cm² not commercially obtainable | — | material | embedded caps | review | §24.3.2, §24.5.3 | high |
| COOMBS-2138 | magnetics | Embedded spiral inductor limits: single-layer ≈ 10 nH max; multilayer up to 30 nH; with ferromagnetic core/layer ~100 nH; stored energy E = ½·L·I² (eq. not in text) | L ≤ 10 nH (1 layer), ≤ 30 nH (multilayer), ~100 nH (ferrite) | turns, W, S, layers | embedded inductors | calc/sim | §24.4.3, §24.5.4 | high |
| COOMBS-2139 | fab | Embedded resistor process temperatures: PTF cure 150–200 °C; ceramic paste fires at 900 °C in nitrogen before lamination | — | material | embedded resistors | review | §24.5.2.2 | high |
| COOMBS-2140 | components | Foil/plated resistor materials give one value (Ω/sq) per layer (one decade of values); pastes selected 10–15× apart, e.g., 100, 1000, 50,000 Ω/sq to cover 10–100,000 Ω | — | value range | embedded resistors | review | §24.3.2, §24.6.1 | high |
| COOMBS-2141 | components | Embedded formed resistors must be laser-trimmed; trimming is slow/expensive; form non-critical values, place discrete parts for close tolerance | — | tolerance | embedded | review | §24.3.2, §24.5.2.6, §24.6.3.4 | high |
| COOMBS-2142 | components | Embeddable discrete resistors: 0201 (0.23 mm thick) and 01005 (0.13 mm thick); thick film ±5 %, thin film ±0.5 % | — | package | embedded discretes | review | §24.6.2.1 | high |
| COOMBS-2143 | components | Embeddable discrete capacitors: C0G 01005/0201 5.0–100 pF; X7R 68–470 pF (01005), 68–10,000 pF (0201); thickness 0.20 mm (01005), 0.30 mm (0201), 0.15 mm thin family; Si MIS caps 0.13 mm thick, 0.8–1000 pF, 0.23×0.30 mm to 1.5×1.70 mm | — | package | embedded discretes | review | §24.6.2.2 | high |
| COOMBS-2144 | dfm | Never mix formed and placed components on the same layer; put placed discretes on separate layer(s); protect formed components with polymer coat or clad/RCC lamination | — | layer plan | embedded PCBs | inspect | §24.6.3.5, IPC-7092 | high |
| COOMBS-2145 | process | Embedded-component BOM is segmented by layer; reference designators encode the layer on the schematic | — | BOM | embedded PCBs | inspect | §24.6.3.6 | high |
| COOMBS-2146 | test | Embedded-component test constraints: test voltages may break down thin dielectrics; capacitor charge-up limits test speed; no rework inside the board | — | test plan | embedded PCBs | review | §24.3.2 | high |
| COOMBS-2147 | via | HDI board definition: average > 110–130 electrical connections per in² (20 per cm²) counting both sides | > 110–130 /in² | connection count, area | HDI decision | calc | §25.1 | high |
| COOMBS-2148 | via | IPC microvia definition ≤ 150 µm diameter; a surface blind via L1–L3 is typically 250 µm for reliable plating and is still a microvia (SBV) | d ≤ 150 µm; L1–L3 SBV ≈ 250 µm | via d | HDI | inspect | §25.2 | high |
| COOMBS-2149 | cost | Cost parity: 4-layer HDI microvia board ≈ 8-layer through-hole multilayer for similar wiring density; above 8-layer TH density, HDI is cheaper; HDI gives 4–8× wiring density of all-drilled TH | 4L HDI ≈ 8L TH cost; density ×4–8 | density demand | technology selection | calc | §25.2.4, §25.3, Fig. 25.2 | high |
| COOMBS-2150 | via | Classify HDI structure per IPC-2226 Types I–VI, notation x[C]x (x = build-up layers per side; [C] core); Type I 1[C]0/1[C]1 microvias + PTH; Type II same with filled core through vias; Type III 2[C]0/2[C]2; Type IV build-up on passive substrate [P]; Type V coreless colaminated with conductive paste; Type VI simultaneous interconnect/structure | — | stackup | HDI | review | §25.3.1 | high |
| COOMBS-2151 | dfm | Choose HDI design-rule category by supplier base: Category A (relaxed, ~100 % of HDI fabricators), B (conventional, ~75 %), C (top-level, ~20 %, smaller panels, lower yield, higher cost — only for COB/flip-chip/MCM) | — | feature sizes | HDI | review | §25.3.2, Fig. 25.5 (values not in text) | high |
| COOMBS-2152 | via | Skip vias (e.g., L1–L3) are only practical with laser drilling; photovia/plasma via only connect adjacent layers | — | via spans | HDI | review | §25.4.1 | high |
| COOMBS-2153 | materials | HDI dielectric acceptance: plated-copper peel ≥ 6 lb/in (1.08 kg/cm) per 1 oz (35.6 µm) copper; chemistry compatible with core; survives solder floats, thermal cycles, multiple reflows; platable to via bottom | peel ≥ 6 lb/in @1 oz | material data | HDI build-up | measure | §25.5.1 | high |
| COOMBS-2154 | materials | FR-4 for laser microvias: 106 or 1080 thin woven glass (1086 uniform weave made for laser), 1–2 ply, resin content ≈ 70 %; UV Nd:YAG or CO2 laser | RC ≈ 70 %; glass 106/1080/1086 | prepreg style | laser microvias | review | §25.5.1.1 | high |
| COOMBS-2155 | via | Thick base copper raises effective microvia aspect ratio and risks bottlenecking (via plates shut at top); use unclad or thin-copper dielectrics when L/S ≤ 75 µm or via < 75 µm | thin/unclad when L/S ≤ 75 µm or d_via < 75 µm | base Cu, via d | HDI fine features | review | §25.5.1.2, Fig. 25.9 | high |
| COOMBS-2156 | process | HDI CAD must support mixed-via optimization, near-zero via cost routing, blind/buried via layer control, landless padstacks, staggered vias, pad-in-pad, any-angle routing, manufacturing rules at all phases, buried components | — | tool features | HDI design | review | §25.4.2.1 | high |
| COOMBS-2157 | materials | Reinforced HDI dielectrics give better dimensional stability, lower CTE and less thermal cracking; nonreinforced give lower Dk and may be photoimageable | — | material class | HDI build-up | review | §25.5.2 | high |
| COOMBS-2158 | materials | Resin-coated copper (RCC): finished dielectric 1.0 mil (25 µm) to 3.0 mil (76 µm); foils ½ oz (18 µm) or 3/8 oz (13.34 µm); two-pass (C-stage stop + B-stage) gives better thickness control than one-pass | t_diel = 25–76 µm | RCC type | HDI build-up | review | §25.5.2.1.1, IPC-4104/12,13,19–22 | high |
| COOMBS-2159 | materials | Unclad photoimageable dielectrics need copper pretreatment (black oxide or oxide replacement) and provide plated-Cu adhesion ≥ 1.1 kg/cm at 25 µm Cu; metallized by solvent swell + permanganate | peel ≥ 1.1 kg/cm @25 µm | material | photovia | measure | §25.5.2.1.3, IPC-4104/1,2,7–10,16 | high |
| COOMBS-2160 | materials | Photoimageable dielectric forms all vias (any size) in one exposure; it is the only economical way to open large rectangular cavities for embedded passives | — | via count/size | HDI | review | §25.5.2.1.3 | high |
| COOMBS-2161 | materials | Nonwoven aramid laminates: in-plane CTE tailorable 10–16 ppm/°C by resin/Cu content; extends CSP solder-joint life up to 3× vs FR-4/RCF; no cracking after > 1000 cycles −40/+125 °C; allows laser skip-vias interconnecting up to four layers per side without sequential lamination | CTE 10–16 ppm/°C | material | CSP, avionics, satellites | review | §25.5.2.4, IPC-4104/5,23 | high |
| COOMBS-2162 | via | Via filling is required for: acid entrapment, vacuum handling, flux/solvent blowout, flux dripping, solder-mask migration/nodules, planarity of mask and SBU core, via-in-pad paste volume and solder migration | — | via-in-pad, SBU cores | HDI / via-in-pad | review | §25.5.3.1 | high |
| COOMBS-2163 | via | Core through-holes can be filled by the lamination itself (RCC/prepreg) only if plated hole diameter ≤ 0.3 mm and core thickness ≤ 0.6 mm (RCC resin 80 µm preferred); otherwise fill separately by screen printing, cure, planarize (#600–#800 belt or ceramic brush) | d_hole ≤ 0.3 mm AND t_core ≤ 0.6 mm | d, t_core | SBU cores | calc | §25.5.3.2.1, Fig. 25.15 | high |
| COOMBS-2164 | via | Photoimageable via-plug: one screen pass usually fills, two passes maximize; bed-of-nails/dimple plate for air release; cores ≤ 0.030 in (0.76 mm) require a secondary coating | — | core thickness | via plugging | review | §25.5.3.2.3 | high |
| COOMBS-2165 | via | Conductive (Ag/Cu/epoxy) paste via fill design rules: aspect ratio 1:1 to 6:1 (with vacuum assist); via size 6–25 mil (152–635 µm); core thickness 6–85 mil (152–2159 µm); essentially zero shrinkage; planarize and plate for solderable via-in-pad | AR ≤ 6:1; d = 152–635 µm; t = 152–2159 µm | d, t | conductive-fill via-in-pad | calc | §25.5.3.2.4 | high |
| COOMBS-2166 | via | Solder-mask ink as via fill leaves solvent craters at small holes and has lower Cu adhesion than dedicated fill resins; single-cure thermal resins must be filled void-free | — | fill material | via plugging | review | §25.5.3.2.5–25.5.3.2.6 | high |
| COOMBS-2167 | via | Laser-via dielectric is fully cured before drilling → stable hole position; photovia resin cures after imaging → random hole movement, forcing panels ≤ ~400×400 mm and difficult registration | photovia panel ≤ 400×400 mm | process | HDI process choice | review | §25.5.3.2.7, §25.6.1 | high |
| COOMBS-2168 | via | Mechanical through-via drilling below 0.20 mm (0.008 in) is possible but not cost-effective; use laser/other via formation below 0.20 mm | d < 0.20 mm → laser | via d | via formation | review | §25.6 | high |
| COOMBS-2169 | fab | Photovia dielectric full cure typically 160 °C for ~1 h; permanganate etch afterwards removes residual resin at via bottom and creates micro-porosity for peel | 160 °C / 1 h | process | photovia | review | §25.6.1 | high |
| COOMBS-2170 | materials | Peel-strength targets for HDI dielectrics: chip-package substrates min ≈ 600 g/cm² [sic; units as printed]; cell-phone motherboards ≥ 1.0 kg/m² [sic] to survive drop tests; laser-via (filled) resins reach higher peel than photovia resins | as printed | material | HDI | measure | §25.6.1 | high (values as printed; units suspect) |
| COOMBS-2171 | reliability | Residual palladium catalyst trapped in micro-porous resin causes migration; a removal step is mandatory for resin-dielectric HDI (photo or laser) | — | process | HDI | review | §25.6.1 | high |
| COOMBS-2172 | fab | Plasma via (DYCOstrate) bowl-shaped holes and copper overhang require secondary Cu etch (thins surface Cu, aids fine lines) but takes several times longer than other processes; best for flex through-holes etched from both sides | — | process | flex HDI | review | §25.6.2 | high |
| COOMBS-2173 | fab | Via-formation throughput: chemical etch/plasma/photo mass processes ≈ 40,000–50,000 vias/s; UV-YAG through glass-reinforced dielectric 3–50 holes/s; UV-YAG through RCC 100–300 holes/s; single-head CO2 on bare resin 20,000–25,000 holes/min; dual-head CO2 +70 %; CO2 laser direct drilling through darkened ultra-thin Cu −30–40 % vs bare resin | see T-25.laser | process, dielectric | HDI cost/throughput | calc | §25.6.3 | high |
| COOMBS-2174 | fab | Laser spot/fluence: high-fluence beams (~20 µm spot) cut metal and glass; low-fluence beams (100–350 µm spot) remove organics only | — | laser | HDI | review | §25.6.3 | high |
| COOMBS-2175 | via | Minimum laser microvia: UV-YAG 20–30 µm; CO2 50 µm in mass production; YAG needs trepanning (slower) for d ≥ 125 µm and is sensitive to dielectric thickness variation (can damage capture pad through thin spots or glass openings) | d_min YAG = 20–30 µm; d_min CO2 = 50 µm | via d | HDI | review | §25.6.3.1 | high |
| COOMBS-2176 | fab | CO2 cannot penetrate copper unless < 5 µm and darkened; RCC needs window pre-etch after half-etching surface Cu to ~6–7 µm (H2O2/H2SO4 etchant); YAG users also thin foil to 6–9 µm for speed | Cu ≤ 5 µm for CO2 direct; half-etch to 6–7 µm | foil thickness | CO2 laser vias | review | §25.6.3.1–25.6.3.2 | high |
| COOMBS-2177 | fab | Filled resins slow CO2 drilling; use two coats for 60 µm dielectric: 40 µm unfilled + 20 µm filled on top; taper holes by 2–3 pulses, applying a third pulse only in a second pass to avoid capture-pad overheating and smear | 60 µm = 40 + 20 µm; ≤ 2 consecutive pulses | coating plan | CO2 laser vias | review | §25.6.3.2 | high |
| COOMBS-2178 | via | Conformal drilling uses a beam larger than the Cu window (bowl-shaped unless pulsed); semiconformal uses a beam slightly smaller than the window (small plating step; half-etch minimizes); window-to-capture-pad misregistration becomes a serious defect when capture pad < 250 µm → use liquid resin, YAG, LDI windows or CO2 direct drilling | capture pad ≥ 250 µm for RCC window method | pad d | RCC laser vias | review | §25.6.3.2, Fig. 25.22 | high |
| COOMBS-2179 | materials | Ultra-thin-copper RCC for direct CO2 drilling: 70 µm (2 oz) carrier, 10–20 µm conductive release film, 3–5 µm plated foil; laser-direct method etches Cu to ~5 µm, oxide-darkens, and removes 1 µm more | foil 3–5 µm | material | CO2 direct drilling | review | §25.6.3.2 | high |
| COOMBS-2180 | fab | YAG/CO2 combination preferred for copper/prepreg (infrastructure, automotive) boards: YAG cuts Cu and part of glass, CO2 finishes; residual glass fibers removed mechanically by Al2O3 blasting (~20 µm particles) or excimer sweep, ~30 s per panel side | — | structure | copper/prepreg HDI | review | §25.6.3.3 | high |
| COOMBS-2181 | via | Microvia density benchmark: cell-phone boards reach 650,000–700,000 microvias per m²; infrastructure boards ~1 order of magnitude fewer | ≤ 7e5 vias/m² | design | HDI cost model | calc | §25.6.3.3 | high |
| COOMBS-2182 | via | Photoimageable dielectric build-up is most advantageous when via count per panel is very high (> 50,000 vias on an 18×24 in panel); zero incremental per-via cost | > 50,000 vias / 18×24 in panel | via count | HDI process choice | calc | §26.3.1.2 | high |
| COOMBS-2183 | via | Liquid PID gives tapered via walls (better plating coverage); dry-film PID gives near-vertical walls (smaller top opening and capture land for the same bottom diameter) and needs no leveling | — | PID form | photovia | review | §26.3.1.2.1–26.3.1.2.2 | high |
| COOMBS-2184 | via | Example HDI density: Sony DCR-PC7 2+4+2 SLC build-up with 0.5 mm pitch CSPs achieved > 612 pins/in² | 612 pins/in² | — | benchmark | calc | §26.3.1.2, Fig. 26.2 | high |
| COOMBS-2185 | fab | Ormet TLPS (Cu-Sn) paste vias: sinter in condensing fluorocarbon vapor at 215 °C for 2 min, post-cure 40 min at 175 °C; up to four layer pairs (8 metal layers) joined (OrmeLink) | 215 °C/2 min + 175 °C/40 min | process | paste-via HDI | review | §26.3.2.8 | high |
| COOMBS-2186 | via | Paste/parallel-lamination HDI (ALIVH, BBIT, NMBI): vias under surface lands relax registration; ALIVH 6–10 layers laminated in one step; DYCOstrate 0.075 mm plasma through-holes; PERL 4–12 layers | — | process | HDI alternatives | review | §26.3.2.9, §26.3.4, §26.3.5 | high |
| COOMBS-2187 | materials | Embedded polymer optical waveguides: 100 µm-wide waveguide carries ~10,000× the information of a 100 µm trace; optical cables 10× smaller than shielded HS cables, bussing 20× smaller, connectors 7× smaller and 20–40 % faster, waveguides 8× smaller than differential striplines | — | — | next-gen interconnect | review | §26.4.1 | high |
| COOMBS-2188 | materials | Optical polymer qualification: Telcordia 1209/1221 < 600 h at 85 °C/85 % RH, solder > 230 °C, degradation > 350 °C; POF unstable < 80 °C, POF loss 20 dB/km vs glass < 0.1 dB/km; polymer losses quoted in dB/cm near 840 nm; packaging ≈ 80 % of device cost | — | material | optical PCB | review | §26.4.1.3, Table 26.3 (not in text) | high |
| COOMBS-2189 | process | Fabrication data package per IPC-2610 family (2611 generic, 2612 schematic, 2613 assembly, 2614 board fab incl. embedded passives, 2615 dimensions/tolerances, 2616 part descriptions, 2617 discrete wiring, 2618 BOM) | — | documentation | fab release | inspect | §27.2 | high |
| COOMBS-2190 | process | Fab data must define: part number, fab/drill/subpanel drawings, notes, board type/size/shape, bow & twist allowance, thickness ± tol, tooling holes, markings, materials (class/grade/color), plating & coating type/thickness/tol, mask & ink type/min thickness/permanency, conductor dimensions & tolerances, coupon locations, acceptance documents, X-out policy, artwork, aperture list, drill data/tool files, netlist | — | documentation | fab release | inspect | §27.2.1 | high |
| COOMBS-2191 | process | CAM design-analysis tasks: design rule check, manufacturability analysis, single-image edits, DFM enhancements, panelization, fab-parameter extraction | — | CAM | fab tooling | review | §27.3 | high |
| COOMBS-2192 | dfm | Top causes of tooling problems to eliminate at design: poor documentation, malformed drill files, RS-274-D with separate aperture tables, insufficient solder-mask clearance, inadequate drill-to-copper clearance, misaligned layers, inadequate manufacturing clearances, missing IPC-D-356 netlist, positive plane layers instead of negative, poor designer–fabricator communication | — | data package | fab release | inspect | §27.3 | high |
| COOMBS-2193 | process | Use RS-274-X (embedded apertures) at minimum; prefer intelligent formats (ODB++, GenCAM, DirectCAM) with embedded netlist and design rules | — | output format | fab release | inspect | §27.3 | high |
| COOMBS-2194 | test | Fabricator electrical-test netlist (from artwork) must be compared to the supplied IPC-D-356 netlist; every difference (shorted/broken nets, missing plane ties) resolved before test file is finalized | mismatches = 0 | netlists | bare-board test | inspect | §27.4.2, §27.4.6.6 | high |
| COOMBS-2195 | assembly | Assembly tooling analyses: fiducials (global & fine-pitch), component overlap/data completeness, padstack vs vias/planes/mask/edges/gold fingers, testpoints vs vias/features/tooling holes/nets, solder-paste checks (Table 27.3 not in text) | — | assembly data | assembly tooling | inspect | §27.4.2.2 | high |
| COOMBS-2196 | process | Fab-side parameters extracted per part number: shear/label, foil thickness & etch rates, AOI files, lamination lay-up BOM/stack height, press cycle (time/temp/pressure), drill & rout file revisions, plating area & current density, ET programs, QC/coupon disposition, packing | — | CAM | fab tooling | inspect | §27.4.6 | high |
| COOMBS-2197 | fab | Plating current per rack = bath current density × plated area; after first run, measured plated thickness is used to correct the effective area | I = J × A_plated | J (A/ft² or A/dm²), A | electroplating setup | calc | §27.4.6.4 | high |
| COOMBS-2198 | process | Design changes made at fab/assembly must be fed back into the design database, else respins repeat the defect | — | change log | all | review | §27.4.2.2 | high |
| COOMBS-2199 | process | Archive customer data and generated tooling files for disaster recovery; large presses up to 48×48 in and rivet vs pin lamination may need extra tooling | — | archive | fab | review | §27.5 | high |
| COOMBS-2200 | fab | Drilling laminate facts: finished board thickness 0.010–0.300 in (most common ≈ 0.0625 in); larger glass-fiber bundles cause drill deflection (registration loss) and larger hole-wall voids | — | glass style | drilling | review | §28.2.1 | high |
| COOMBS-2201 | materials | Tg classes: standard FR-4 ≈ 130 °C, mid-Tg ≈ 150 °C, high-Tg ≈ 170 °C; filled high-Tg materials are more brittle/abrasive → reduce surface (spindle) speed to lower frictional heat and drill wear | Tg 130/150/170 °C | material | drilling params | review | §28.2.1.2 | high |
| COOMBS-2202 | fab | 1 oz Cu ≈ 1.4 mil (0.0014 in); more copper layers balance the stack (fewer voids) but require higher chip load to control nail-heading and lower max hit count per bit | 1 oz = 1.4 mil | Cu layers | drilling params | calc | §28.2.1.3 | high |
| COOMBS-2203 | fab | Drill bits: tungsten carbide > 90 wt % with 6–8 wt % Co binder (+1–2 wt % TiC/TaC); grain classes "ultrafine (> 0.5 µm), extra-fine (> 0.05 to 0.09 µm), fine (1 to 1.5 µm)" [as printed]; smaller diameter → finer grain; carbide is brittle — never let bits touch each other | — | bit spec | drilling | review | §28.2.2.1–28.2.2.2 | high (as printed) |
| COOMBS-2204 | fab | Drill geometry: wider margin → more friction/heat → smear and plowing; partial margin relief (~1/5 of flute length) raises drilling temperature ≥ 25 % and causes packed margins/breakage | — | bit design | small drills | review | §28.2.2.3 | high |
| COOMBS-2205 | fab | Flute length ≥ total drilled depth (laminate stack + entry + backup penetration) + 0.050 in of unused flute above the stack at bottom of stroke for chip evacuation | L_flute ≥ t_stack + t_entry + d_backup + 0.050 in | stack, entry, backup | drilling | calc | §28.2.2.4 | high |
| COOMBS-2206 | fab | Incoming drill bits inspected by AQL sampling (MIL-STD-105): point geometry, chips, drill & shank diameter, flute length, ring distance, size imprint; lot rejected if defects exceed plan | — | bit lot | drilling | inspect | §28.2.2.5 | high |
| COOMBS-2207 | fab | Repointing costs ~15 % of a new bit; small-diameter bits repointed only 1–3 times (large up to 10+); regrind removes 0.002–0.005 in; alternatively discard at a minimum overall length computed from required flute length; repointed bits must meet new-bit point specs and have clean, undamaged margins | ≤ 1–3 repoints (small d) | bit history | drilling | inspect | §28.2.2.6 | high |
| COOMBS-2208 | fab | Entry material ranking (centering, breakage, burrs, contamination, pressure-foot marks): Al-clad cellulose composite > solid Al > phenolic > Al-clad phenolic; phenolic contaminates hole walls (desmear cannot remove phenolic); solid Al ≥ 0.008 in raises small-drill breakage; entry must be flat, pit/dent-free | — | entry type | drilling | review | §28.2.4 | high |
| COOMBS-2209 | fab | Backup material with lubricating bonding agent cuts drilling temperature by ≥ 50 % (often below laminate Tg), allowing higher stacks/hit counts; phenolic and hardboard backups are unsuitable (contamination, thickness variation) | ΔT_drill −50 % | backup type | drilling | review | §28.2.5 | high |
| COOMBS-2210 | fab | Tooling pins must be hardened and large enough to hold the stack: pins < 1/8 in diameter allow stack movement; replace worn/mushroomed pins; bushings/slots must hold pins snugly | pin d > 1/8 in (ideal size garbled in text) | pin d | drilling | inspect | §28.2.6, §28.3.3 | high (as printed) |
| COOMBS-2211 | fab | Machine air must be clean and dry; equal pressure-foot pressure at every station; effective vacuum is essential (heat removal) | — | machine | drilling | inspect | §28.3.1–28.3.2 | high |
| COOMBS-2212 | fab | Ball-bearing spindle collets cleaned ≥ once per shift and returned to the same spindle; air-bearing collets cleaned when run-out is excessive | ≥ 1 clean/shift | spindle type | drilling | inspect | §28.3.4.1 | high |
| COOMBS-2213 | fab | Static TIR measured with a 1/8 in (0.1250 in) concentric pin, indicator ≈ 0.800 in from collet nose; max TIR 0.5 mil (0.0005 in) for drills > 0.020 in and 0.2 mil (0.0002 in) for drills ≤ 0.020 in; measure every spindle ≥ weekly | TIR ≤ 0.0005 in (d > 0.020 in); ≤ 0.0002 in (d ≤ 0.020 in) | drill d | drilling | measure | §28.3.4.2 | high |
| COOMBS-2214 | fab | Ch. 29 states static spindle run-out must not exceed 0.002 in (0.005 mm) TIR [inconsistent with Ch. 28's 0.0005 in; both as printed]; tool-metrology gauges can reject high-run-out bits at tool change | TIR ≤ 0.002 in (0.005 mm) | — | HDI drilling | measure | §29.4.6 | high (as printed) |
| COOMBS-2215 | fab | Verify actual spindle rpm every 6 months with a non-contact tachometer (≥ 150,000 rpm range, ≈ $300); wrong rpm = wrong surface speed → heat defects | 6-month check | — | drilling | measure | §28.3.4.3 | high |
| COOMBS-2216 | fab | Pressure-foot insert lead distance to drill point ≈ 0.050 in; check inserts daily; re-adjust pressure foot whenever spindle z-height changes (a gap steals vacuum) | lead = 0.050 in | machine | drilling | inspect | §28.3.4.4–28.3.4.5 | high |
| COOMBS-2217 | fab | Lead screws cleaned/lightly greased every 6 months; never clean the machine with compressed air; use black coolant hoses + inhibitor to stop algae | 6-month PM | — | drilling | inspect | §28.3.5–28.3.6 | high |
| COOMBS-2218 | fab | Spindle speed from surface speed and diameter; higher surface speed → more friction heat → smear/plowing and wear; reduce surface speed for abrasive high-Tg/filled/polyimide/cyanate materials and taller stacks | rpm = (sfm × 12)/(π × d_in) [Eq. 28.1 not in text; standard form]; metric n = 1000·v/(π·d_mm) | v (sfm or m/min), d | drilling params | calc | §28.4.1 | medium (formula) / high (guidance) |
| COOMBS-2219 | fab | Chip load (advance/rev, mils) sets infeed = chip load × rpm; higher infeed → higher entry burrs, more breakage and voids but less nail-heading and exit burrs; lower infeed the opposite | infeed (ipm) = chipload (in/rev) × rpm | chip load, rpm | drilling params | calc | §28.4.2, §29.4.8 | high |
| COOMBS-2220 | fab | Retract rate: machine max 500–1000 ipm (up to 1400 ipm / 35,560 mm/min on new machines); for drills 0.0250 in (#72) to 0.0135 in (#80) reduce to ≤ 500 ipm; smaller drills even lower | ≤ 500 ipm for d ≤ 0.025 in | d | drilling params | review | §28.4.3, §29.4.10 | high |
| COOMBS-2221 | fab | Backup penetration depth = drill point length + ≈ 0.010 in; rule of thumb = min(drill diameter, 0.040 in); excessive depth → wear/breakage; insufficient → incomplete holes; z-compensation (point length vs point angle) must be in the parameter file for any depth-controlled drilling | d_backup = min(d_drill, 0.040 in) | d, point angle | drilling params | calc | §28.4.4–28.4.5 | high |
| COOMBS-2222 | fab | Parameter-table example: target cutting speed 150 m/min; max spindle "1,250,000 rpm" [sic] reached at d = 0.35 mm (137 m/min); a 160,000 rpm spindle holds 150 m/min down to 0.3 mm; min 20,000 rpm reached at 2.4 mm; above shank diameter 3.175 mm point angle changes 130° → 165° requiring reduced infeed; rpm rounded to thousands | v_target = 150 m/min | d | drilling params | calc | §28.4.6.3 | high (as printed) |
| COOMBS-2223 | fab | Stack clearance ≥ 1/8 in (0.125 in) between drill point and stack top at top of stroke = 0.075 in between pressure foot and stack with 0.050 in lead; set with a 0.075 in shim; more clearance improves table settling, chip removal and small-drill survival | clearance ≥ 0.125 in | machine | drilling | inspect | §28.4.7 | high |
| COOMBS-2224 | fab | Maximum safe total drilled depth (panels × thickness + entry + backup penetration) ≈ 17 × drill diameter; add flute reserve for debris | depth_total ≤ 17 × d | d, stack | stack height | calc | §28.4.8 | high |
| COOMBS-2225 | fab | Stacking: deburr panel edges and pinning holes (remove lamination resin build-up), wipe with lint-free cloth, pins perpendicular, reject warped entry/backup; tape (never pin) entry sheet sized to clear pins and not overhang stack | — | stack build | drilling | inspect | §28.4.9 | high |
| COOMBS-2226 | via | Backdrilling removes the unused barrel below the signal layer; specify must-not-cut layer (target) and must-cut layer (min depth); remaining stub = distance from barrel end to must-not-cut layer; machine z capability is a few µm but PCB/process tolerances stack up and enlarge the stub | stub ≥ Σ tolerances | layer stack, thickness tolerances | high-frequency PTH | calc | §28.4.10, Fig. 28.12 | high |
| COOMBS-2227 | fab | Hole-defect diagnosis: voids (fiber tear-out) are mechanical → check chip load/infeed; plowing/smear are heat-related → check surface speed/spindle rpm; nail-heading → chip load, Cu layers; burrs inside stack → stacking/pinning/warp; entry/exit burrs → entry/backup material or infeed | — | defect type | drilling | inspect | §28.5, §28.7 | high |
| COOMBS-2228 | fab | Post-drill inspection of used bits: bonded debris / corner wear → high temperature, under-cured material, or excessive surface speed; primary cutting-edge wear → abrasive material → lower stack, hit count, or change entry/backup | — | used bits | drilling | inspect | §28.7, §29.4.5 | high |
| COOMBS-2229 | cost | Drilling cost model: cost per bit life = new price + N_repoints × repoint cost; uses per life = N_repoints + 1; bit uses = total hits / max hits per use; backup cost ÷ 2 (used twice); report cost per 1000 holes | see §28.8 | hits, stack, rates | drilling cost | calc | §28.8 | high |
| COOMBS-2230 | via | HDI mechanical drilling: HDI holes ≤ 0.006 in; mechanical drilling continues below 0.004 in, down to 0.002 in (0.05 mm) with tight control of location, room T/RH, vacuum, bit condition, dynamic run-out, entry/backup, max rpm, depth control | d_min mech = 0.002 in | d | HDI | review | §29.1–29.2 | high |
| COOMBS-2231 | via | Laser vs mechanical: via deeper than 0.016 in [text also says "(6.3 mm)" sic] → mechanical; hole larger than 0.012 in → mechanical (speed, wall quality); smear-prone materials → hybrid laser; laser > 500 holes/s (up to 1000/s) vs ≈ 200 holes/min mechanical | d > 0.012 in or depth > 0.016 in → mechanical | d, depth | via formation | review | §29.3 | high |
| COOMBS-2232 | via | Laser blind vias need no depth "safety" under the landing pad (CO2 reflects from Cu) whereas mechanical blind vias require extra dielectric under the target layer for thickness tolerance; lasers can form telescope (dual-diameter) vias | — | via type | blind vias | review | §29.3.1 | high |
| COOMBS-2233 | fab | Laser types: CO2 IR 9.4–10.6 µm (9,400–10,600 nm), thermal ablation, reflected by Cu, focus "~200 mm" [sic, µm], needs desmear; solid-state UV (Nd:YAG, Yb:YAG, Nd:YVO4, Nd:YLF) fundamental 1030–1070 nm (Nd:YAG 1064 nm), harmonics 532 nm and 355 nm, photo-ablation, focus "~20 mm" [sic, µm]; YAG pulse ≈ 120 ns; YVO4 ≈ 20 ns at ≈ 100 kHz (most common); YLF ≈ 50 ns, 5× YAG absorption at pump wavelength | — | laser | HDI | review | §29.3.2–29.3.7, §29.8.3–29.8.4 | high (as printed) |
| COOMBS-2234 | fab | Drill room held at 72 ± 2 °F (22 ± 1.1 °C) and 45–60 % RH; machines on granite bases, isolated on reinforced-concrete pads from presses/vibration | 22 ± 1.1 °C; 45–60 % RH | environment | HDI drilling | measure | §29.4.1–29.4.2 | high |
| COOMBS-2235 | fab | Spindles 15,000–300,000 rpm, ≈ 1 hp; keep cutting speed consistent across the diameter range (Table 29.3 not in text); chip loads > 0.001 in/rev need adequate cutting speed; 300 sfm reached for microdrills only with ≥ 180,000 rpm spindles | 300 sfm needs 180,000 rpm at micro diameters | d | microdrilling | calc | §29.4.6–29.4.9 | high |
| COOMBS-2236 | fab | Depth-control modes: manual down-limit (no stack reference), machine depth control referenced to top of stack (needs TMG pressure-foot-to-tip distance), controlled penetration referenced to backup top via mapping (touchdown every 2 in), electrical-contact zeroing on PCB surface | — | mode | blind vias, backdrill | review | §29.5, §29.6.1 | high |
| COOMBS-2237 | via | Mechanical blind via: aspect ratio (drill depth / diameter) must be within metallization capability; keep a minimum dielectric distance to the next conductive layer under the target for process tolerances | AR ≤ plating capability | depth, d, stackup | mechanical blind vias | calc | §29.6.1 | high |
| COOMBS-2238 | fab | Peck drilling: 3–5 increments (small first peck to center); effective AR = total z-stroke / smallest drill diameter; e.g., 0.209 in / 0.025 in = 8.36 → 2.08 with 4 pecks (Fig. 29.5: 0.285 in stack, 0.206 in stroke, AR 15.3 → 3.8 per peck); AR scale 1 (conservative) to 15 (aggressive); benefits: less breakage, better location, less bottom burr; costs: more nail-heading, smear, roughness, cycle time — mitigate with higher feed, fewer pecks, undercut (headed) bits | AR_eff = z_stroke / d_min | stroke, d | high-AR drilling | calc | §29.6.2 | high |
| COOMBS-2239 | fab | Slot drilling: overlapping holes for slots < 2–3 × tool diameter; for longer slots drill the two end holes then bisect remaining gaps so the bit always enters solid material | — | slot L, d | slots without router | review | §29.6.3 | high |
| COOMBS-2240 | fab | Predrill (pilot) holes for diameters ≥ 0.157 in (4.0 mm) with a pilot 15–35 % of final diameter; optional short-flute pilot for high-AR small holes to improve hole-to-hole tolerance | d ≥ 4.0 mm → pilot 0.15–0.35 × d | d | large holes | calc | §29.6.4 | high |
| COOMBS-2241 | fab | Pulse/step drilling (pause without full retract) prevents "bird-nest" continuous chips on large/countersink/heavy-copper holes that can falsely trigger contact-drilling depth zero | — | d, Cu weight | heavy copper | review | §29.6.5 | high |
| COOMBS-2242 | fab | Innerlayer registration verified by X-ray on stacked coupon pads (best-fit centering) and per-layer locating pads; check after tooling-hole drill and after final drill that holes are centered in pads | — | coupons | multilayer | measure | §29.7 | high |
| COOMBS-2243 | fab | Laser alignment references: X-ray-drilled holes, mechanically drilled holes, or innerlayer targets exposed by laser "skiving"; run laser immediately before/after mechanical drilling to share the desmear | — | targets | laser vias | review | §29.8.2 | high |
| COOMBS-2244 | fab | Laser process windows: pulsed UV 6–28 W, 40–300 kHz, 20–120 ns; pulsed CO2 6–250 W, 2–300 kHz, pulse 1–100 "ms" [sic]; ultrashort-pulse 6–50 W, 400–1000 kHz, 0.3–20 ps (minimizes via carbonization); UV parameters: drill type (spiral/trepan/punch), bite size, velocity, rep rate, spot size, inner diameter, revolutions, radial pitch, entry angle; CO2: pulse period, width, z-focus offset | see T-29.laser | laser | HDI | review | §29.8.3–29.8.6 | high (as printed) |
| COOMBS-2245 | via | Laser blind via is formed in two steps: (1) open surface Cu by UV or by etch/oxide window, (2) remove dielectric by UV or IR; UV dielectric removal must be tuned to avoid excessive landing-Cu removal (minor outer-diameter removal of the landing pad is normal); step-1 settings driven by Cu thickness, step-2 by glass style and filler | — | Cu thickness, glass, filler | laser vias | review | §29.9–29.10, Table 29.4 (not in text) | high |
| COOMBS-2246 | dfm | Imaging method by feature size: screen printing economical for features ≥ 200 µm; photolithography below 200 µm; HDI pushing to ≤ 10 µm; inkjet catalyst/resist can electroless-plate Cu 0.05–5 µm | ≥ 200 µm → screen; < 200 µm → photo | feature size | imaging | review | §30.1 | high |
| COOMBS-2247 | fab | Minimum production line width ≈ photoresist thickness + 10–25 µm; choose thin resist (liquid 6–15 µm resolves < 25 µm; dry film 25–50 µm) for fine lines | W_min ≈ t_resist + (10–25 µm) | t_resist | fine-line imaging | calc | §30.2.2, §30.3, §30.4 | high |
| COOMBS-2248 | fab | Negative resists (industry standard): phototool contamination → mousebite/open (print-and-etch); positive resists: contamination → extra metal/short; negative still preferred | — | tone | imaging yield | review | §30.2.1 | high |
| COOMBS-2249 | fab | Aqueous dry film: exposure at 365 nm, dose 25–90 mJ/cm² (330–405 nm) (semiconductor positive resists 200–500 mJ/cm²; LDI resists ≈ 10 mJ/cm²); develop in ≤ 1 wt % Na/K carbonate (pH 10.3); strip in ≥ 1 M NaOH/KOH hot (pH 13); sub-classes for acid etch, acid plating (pH < 1) and ammoniacal etch (pH 8–9) | dose 25–90 mJ/cm²; dev pH 10.3; strip pH 13 | resist | imaging | measure | §30.3.2 | high |
| COOMBS-2250 | fab | Dry-film coversheet optics matter for features < 100 µm; films ≤ 25 µm use high-clarity thin coversheet; liquid resists need hard contact—soft/off contact loses resolution/yield at ≤ 100 µm; liquid resist gives high yield at ≤ 50 µm features | — | resist, contact | fine lines | review | §30.3, §30.4 | high |
| COOMBS-2251 | fab | Mechanical (brush/pumice) cleaning only on cores > 0.020 in (text "0.52 mm"); thin/flex cores distort → registration loss; RTF/DSTF foils need no chemical roughening (roughening smooths the tooth) | t_core > 0.020 in for mechanical clean | core thickness | innerlayer prep | review | §30.6.2.1–30.6.2.2 | high |
| COOMBS-2252 | fab | Copper cleaning must remove Cr/Zn antitarnish (persulfate or peroxide/sulfuric microetch); thin seed layers tolerate very little etch; verify wetting by water-break/contact angle | — | surface | imaging prep | inspect | §30.6.2 | high |
| COOMBS-2253 | fab | Hot-roll lamination: roll rubber 40–50 Shore A (55–65 for extra conformance); preheat panels; wet lamination (water-alcohol) improves conformation and permits tenting inner via holes with smaller lands; automatic laminators trim resist 1–4 mm inside board edge; vacuum lamination for tall/dense features and thin unreinforced polyimide | 40–50 Shore A; trim 1–4 mm | — | dry-film application | review | §30.6.3.1–30.6.3.2 | high |
| COOMBS-2254 | fab | Liquid coating: roller coating up to 240 panels/h (gravure metering); electrostatic unsuitable for outerlayers (thick hole rim, bare barrel); electrophoretic film forms in 20 s–3 min; curtain/screen coating one-sided needs partial dry between sides | — | method | liquid resist / mask | review | §30.6.3.3–30.6.3.9 | high |
| COOMBS-2255 | fab | Phototools: diazo/polyester cheapest, Cr-on-glass sharpest edges and most stable; film dimensions shift with T and RH (Table 30.5 not in text); durability ≈ 100–400 contacts (glass, with repair) vs 20–50 (film); use 3-point pin registration; punched film holes wear; glass bushings drift and need resetting | glass 100–400; film 20–50 contacts | tool type | exposure | review | §30.6.4.1.1–30.6.4.1.2 | high |
| COOMBS-2256 | fab | Exposure control: dose = intensity × time (integrating radiometer matched to lamp spectrum); functional cure = dose where remaining thickness loss < 10 % on the contrast curve; monitor with step wedges; replace lamps at ≈ 1000 h (degraded spectrum, explosion risk) | lamp life ≈ 1000 h | dose | exposure | measure | §30.6.4.1.3–30.6.4.1.4 | high |
| COOMBS-2257 | fab | Contact printing: collimation and hard vacuum contact are the two controls for fine spaces; noncontact options: proximity (gap 125–500 µm, ≈ 75 µm resolution with thin liquid resist), scanning, stitching (≈ 6×6 in field, 12 changes per 18×24 in side), magnified projection (365 nm glass: 50 µm line / 63 µm space; earlier 436 nm LCD: 125 µm) | — | method | fine-line exposure | review | §30.6.4.1.4–30.6.4.1.7 | high |
| COOMBS-2258 | fab | LDI/DDI: no phototool; scales data and compensates SBU dimensional change; Ar+ lasers 3000–5000 h life and 60–80 kW → replaced by 355 nm solid-state polygon or 405 nm DMD (mirrors ≈ 1.5 µm, > 8000 dpi equivalent); throughput 60–180 panels/h (18×24 in, 50 µm features) with high-speed resist; drum architecture innerlayers only; smaller spot and finer addressability → steeper aerial sidewalls | 60–180 panels/h | resist speed | fine-line exposure | review | §30.6.4.2–30.6.4.3 | high |
| COOMBS-2259 | fab | DDI (DMD-based) typical capability: min feature 15 µm L&S; edge roughness ±1 µm; position repeatability ±1.0 µm; side-to-side registration ±10 µm (3σ); exposure 20 s per 530×650 mm panel; source 350–425 nm; source life > 3 yr; configurations up to 5000 panels/day, or fine pitch to 8 µm L/S, or "20 mm [sic] L/S at 2 panels/min" | min L/S 15 µm (8 µm fine-pitch config); reg ±10 µm 3σ | L/S target | fine-line imaging | review | §30.6.4.3 | high (as printed) |
| COOMBS-2260 | fab | Develop dwell ≈ 2 × time-to-clear (50 % breakpoint); control concentration, temperature, agitation; resist sidewalls must be vertical | t_dwell ≈ 2·t_clear | — | develop | measure | §30.6.5 | high |
| COOMBS-2261 | fab | Develop troubleshooting: image larger than phototool → incomplete development, overexposure, or poor contact; smaller → dose too low or development too aggressive; distorted → preclean, application or exposure problem | — | image vs phototool | develop | inspect | §30.6.5 | high |
| COOMBS-2262 | fab | Yield aids: plasma treatment after develop reduces shorts in print-and-etch; post-exposure heat treatment (some aqueous dry films) resolves spaces ≤ resist height; high-mineral rinse water improves aqueous resist image; strip with filtration and antitarnish | — | — | imaging | review | §30.6.5–30.6.6 | high |
| COOMBS-2263 | dfm | Print-and-etch capability is set by the minimum space that can be cleared, limited by final conductor height and etchant/equipment; use thin resist | — | Cu height, space | print-and-etch | review | §30.7.1 | high |
| COOMBS-2264 | dfm | Pattern plating: resist thickness ≥ max final plated Cu thickness above base Cu; resist channel = final conductor width; resist resolution ≈ its thickness, so channels < 38 µm are hard to resolve for 25 µm plating | t_resist ≥ t_plated; W_min ≈ 38 µm @ 25 µm plating | t_plated, W | pattern plating | calc | §30.7.1 | high |
| COOMBS-2265 | dfm | Fixed-pitch line/space split: print-and-etch → space larger than line gives higher yield at fine pitch (resist must resolve the space; etch undercut); pattern plating → equal L/S acceptable, a wider final line than space preferred (resist space becomes the line) — balance both | etch: S > W at fine pitch | pitch | fine pitch | review | §30.7.2 | high |
| COOMBS-2266 | dfm | Know the production line's conductor-thickness vs line/space capability plot before choosing panel-plate/print-and-etch vs pattern plating; features above the capability line → pattern plating, below → print-and-etch | Fig. 30.23 (values not in text) | t_Cu, L/S | process selection | review | §30.7.1, §30.7.3 | medium (graph) |
| COOMBS-2267 | dfm | Capture-pad size is set by drill placement accuracy and panel dimensional stability; where lines pass PTH pads, use an elongated pad oriented to the drill-wander/stability direction to widen line-to-pad spacing and raise yield | — | drill accuracy, stability | PTH pads near lines | review | §30.7.3 | high |
| COOMBS-2268 | fab | Inkjet legend/mask/etch-resist printers: 500×500 mm area; positional accuracy ±5 µm, repeatability ±1 µm; 1.5 mm depth of focus over thick traces; 128-jet heads, 1 or 10 pL drops | ±5 µm / ±1 µm | — | inkjet | review | §30.8 | high |
| COOMBS-2269 | test | AOI after imaging/etch detects line-width and spacing violations, excess copper, missing pads, slivers, thin resist/scumming, shorts, dust/debris, cuts, hole breakout; rules are rule-based (e.g., no line < 150 µm) or CAD-reference | — | artwork | bare-board AOI | inspect | §30.9 | high |
| COOMBS-2270 | materials | Lead-free reflow runs 30–40 °C above the eutectic SnPb melting point → new resins, curing agents, fillers; qualify finished boards, not only laminates | ΔT_reflow = +30–40 °C | — | lead-free | review | §31.1 | high |
| COOMBS-2271 | fab | High-frequency fab prints increasingly specify post-pressed thickness tolerance of each prepreg fill section, foil treatment-side roughness, and percent resin of prepreg/core | — | stackup | controlled-Z / RF | review | §31.1 | high |
| COOMBS-2272 | stackup | Classify ML-PWB: IPC-2222 Type 3 (no blind/buried vias), Type 4 (blind and/or buried); IPC-2226 Type I (1[C]0/1[C]1, through vias connect outerlayers), Type II (buried vias in core), Type III (≥ 2[C] ≥ 0) | — | via structure | multilayer | review | §31.2.1 | high |
| COOMBS-2273 | stackup | Foil-outer stack-up (foil + prepreg outside, imaged cores inside) is the cheapest and most popular; face the higher-resin-content prepreg ply toward the signal layer, especially for ≥ 2 oz signal copper | — | stackup | multilayer | inspect | §31.2.2.1 | high |
| COOMBS-2274 | stackup | Clad-outer stack-up: one more core (costlier) but smoother surface (no heavy-Cu "telegraphing"), tighter dielectric control (C-stage tolerance) for impedance/high-voltage pairs; yield risk from mask scratches through innerlayer steps | — | stackup | flatness/impedance critical | review | §31.2.2.2 | high |
| COOMBS-2275 | stackup | Odd layer counts: single-sided clad (release-sheet side needs aggressive bond prep) or etch one side off a double-sided clad (better bond); keep cores balanced (e.g., three equal core thicknesses) to limit warp | — | layer count | odd-layer boards | review | §31.2.2.3 | high |
| COOMBS-2276 | via | Build-up (HDI) technology = sequential processing with microvias < 0.15 mm; Type 4 sequential lamination with standard features is mature | microvia < 0.15 mm | via d | HDI | review | §31.2.3 | high |
| COOMBS-2277 | routing | Manhattan routing: horizontal on one layer of a pair, vertical on the other; a net needs 2 I/O vias + 1–2 routing vias; when via-starved, use buried vias on signal pairs that sit on opposite sides of one C-stage core | — | nets, stackup | dense multilayer | review | §31.2.3.1 | high |
| COOMBS-2278 | stackup | Place a power/ground plane between each signal layer pair (crosstalk isolation, impedance reference); buried vias on every pair require extra plane pairs (more layers, cost) | — | stackup | multilayer | inspect | §31.2.3.1 | high |
| COOMBS-2279 | rf | Use blind rather than through vias inside RF-shielded regions: through vias let RF fields escape the shield | — | via type | RF + digital boards | inspect | §31.2.3.2 | high |
| COOMBS-2280 | via | Via-in-pad: blind via in the SMT pad, plated shut/filled; dog-bone alternative places the via in an adjacent pad | — | pads | dense SMT | inspect | §31.2.3.2 | high |
| COOMBS-2281 | stackup | Building a board as two sub-assemblies (e.g., 2 × 8L → 16L) uses each via site twice so a 100-mil grid can replace a 50-mil grid; costly, largely replaced by HDI | — | stackup | dense double-sided SMT | review | §31.2.3.2 | high |
| COOMBS-2282 | materials | HDI build-up signal layers use low copper: dielectric-coated microfoils 9–12 µm (sacrificial carrier for handling); nonwoven aramid yields equivalent dielectric 1.9 mil; surface aramid for CTE match to area arrays/ceramic parts | foil 9–12 µm; dielectric 1.9 mil | — | HDI build-up | review | §31.2.3.3 | high |
| COOMBS-2283 | dfm | Benchmark HDI capability (imaging, etch, hole formation, plating, lamination registration) with IPC-9151 PCQR² test standard/database | — | — | HDI supplier qual | measure | §31.2.3.3 | high |
| COOMBS-2284 | via | HDI Type I: one lamination + one metallization cycle; CO2 conformal etched-dot mask imaged at primary print cuts misregistration; Type III and above: evaluate non-lamination build-up (repeated cycles costly), keep starting Cu minimal, final build-up resin must fill microvias and flush circuits | — | HDI type | HDI | review | §31.2.3.3.1–31.2.3.3.3 | high |
| COOMBS-2285 | via | Buried vias fill with prepreg resin at final lamination unless prefilled; resin demand scales with via diameter × length × count; insufficient prepreg resin starves the local bond → prefill or add resin | V_resin ≥ Σ π·(d/2)²·L | d, L, count, prepreg RC | buried vias | calc | §31.2.4 | medium (derived) |
| COOMBS-2286 | via | No industry via-fill material spec exists: name acceptable fill brand(s) on the drawing or via user/supplier agreement; obtain modulus/CTE/Tg (often missing from data sheets); qualify with a pre-production build in the end-use environment | — | fill material | filled vias | review | §31.2.4.1–31.2.4.2 | high |
| COOMBS-2287 | via | Planarization must preserve wrap copper: risk rises when wrap < 5 µm (0.0002 in); IPC-6012 Class 3 minimum wrap stated as 0.0005 in ("127 µm" as printed; 0.0005 in = 12.7 µm); MRB data accept 0.0002 in for some (Class 2) environments | wrap ≥ 0.0005 in (Class 3); ≥ 0.0002 in (some Class 2) | wrap thickness | filled/capped vias | measure | §31.2.4.2, §31.2.4.3.3 | high (as printed) |
| COOMBS-2288 | fab | Use a button plate as planarization gauge (once sanded away, further sanding removes wrap); eddy-current Cu thickness at multiple panel locations before and after each planarization pass | — | Cu thickness map | via fill | measure | §31.2.4.3.1–31.2.4.3.2 | high |
| COOMBS-2289 | fab | Screen fill materials for plateability (tape test) and compatibility (solder float + cross-section); some fills are permanganate-incompatible → plasma desmear pre-plate; ceramic-loaded fills over-roughen in aggressive plasma etchback; directly plated conductive fills need peel characterization; outgassing can lift cap plating | — | fill material | via fill | measure | §31.2.4.3.1 | high |
| COOMBS-2290 | fab | Vacuum pressure-assisted injection fill minimizes voids vs manual screen/roller methods | — | method | via fill | review | §31.2.4.3.2 | high |
| COOMBS-2291 | via | Specify via protection per IPC-4761 Types I–VII (Table 5-1 application guide); filled vias are Type V and VII (Class 3 capable) | — | via protection | all | inspect | §31.2.4.3.3 | high |
| COOMBS-2292 | cost | Via fill adds ≈ $25–$50 per panel (excl. setup/minimum lot); silver-filled conductive fill ≈ 2× nonconductive material cost | $25–50/panel | — | cost model | calc | §31.2.4.4 | high |
| COOMBS-2293 | reliability | Most filled-via failures stem from planarization; heavy copper and rigid-flex are risky (imprint makes panel several mils thicker at via structures); soft/unreinforced materials gouge; some users require bare-board lot thermal-shock cycling (esp. lead-free) | — | construction | filled vias | review | §31.2.4.4 | high |
| COOMBS-2294 | materials | Specify laminate by IPC-4101 slash sheet (e.g., IPC-4101/24) and copper foil per IPC-4562 | — | drawing | all | inspect | §31.3.2.1 | high |
| COOMBS-2295 | materials | Copper foil: ≥ 2 oz for high current, > 3 oz raises process difficulty; ≤ 18 µm for high-density signal layers and sequential buried-via cores (line definition, impedance); foil arrives at minimum thickness tolerance | — | Cu weight | foil selection | review | §31.3.2.2 | high |
| COOMBS-2296 | materials | Foil elongation classes: standard ED foil fails ≈ 3 %; IPC-4562/3 HTE 5–8 %; HD Type E (IPC-4562/2) ≥ 10 %; higher elongation resists trace fracture | see T-31.foil | foil grade | flex, thermal cycling | review | §31.3.2.2 | high |
| COOMBS-2297 | materials | Double-treated foil skips adhesion steps but is handling-sensitive, hard to rework, prone to resist-development shorts, and incompatible with blind/buried via plating; RTF (IPC-4562 code R) improves fine-line etch | — | foil type | fine lines | review | §31.3.2.2 | high |
| COOMBS-2298 | fab | Panel strategy: mass lamination sheets 24×48, 36×48, 48×52 in or 1.5×2 m (mainstream features, single resin, cores ≥ 0.004 in [text "(1.0 mm)" sic], some 0.002 in); standard cut panels 18×24, 20/21×27 in (4–8 sizes; high-end, mixed dielectric, sequential lam); flexible custom cuts with rivets (Asia) | — | board size, tech | panelization | review | §31.3.3.1 | high (as printed) |
| COOMBS-2299 | test | Bare-board test netlist in IPC-D-356 format; flying probe for prototypes and HDI (bed-of-nails grid limit); test parameters per IPC-9252 | — | netlist | electrical test | review | §31.3.3.2.6 | high |
| COOMBS-2300 | fab | Tooling holes 0.125–0.250 in diameter, slots 0.187×0.250 in; punch one laminate at a time; laminates > 0.032 in need slightly larger punch/die clearance (spring-back); low-stability materials drift after pre-punch → post-etch optical punch or X-ray drilled tooling | — | laminate | ML tooling | review | §31.3.4 | high |
| COOMBS-2301 | fab | Four-slot tooling tolerates growth/shrink; full-perimeter pin systems are overdetermined (panels stretched over pins); rivets or inductive bonding are pinless options | — | tooling | ML lamination | review | §31.3.5 | high |
| COOMBS-2302 | fab | Lay-up: bake innerlayers 105–110 °C for ≥ 1 h (shorter with some oxide-alternative chemistries); laminate promptly; store in nitrogen dry box if delayed; follow a stack-up sheet | 105–110 °C ≥ 1 h | — | lamination | inspect | §31.4.1 | high |
| COOMBS-2303 | fab | Press tooling: caul plates 3/8 in (9.525 mm) 4130 steel (Al not recommended, high in-plane expansion); separator plates 0.015–0.062 in, 400-series stainless (thicker resists print-through); stainless CTE ≈ MLB in-plane CTE → tight pin fit; Al plates need loose pins | — | tooling | lamination | inspect | §31.4.1.1–31.4.2 | high |
| COOMBS-2304 | fab | Press pads: Kraft paper, silicone rubber (reusable, leaches silicone oil near end of life), expanded mat paper (best results); release sheets or C-A-C (Cu-Al-Cu) sheets protect outer foil and cut book height | — | consumables | lamination | review | §31.4.1.3 | high |
| COOMBS-2305 | fab | Breakdown: automatic thickness check, edge finish (remove ooze-out, foil overhang), bevel/polish edges, bore tooling holes | — | — | post-lamination | inspect | §31.4.3 | high |
| COOMBS-2306 | fab | Hydraulic press: 4–8 openings; up to 96 low-layer panels per cycle (12 high × 8 openings); reduce stack for thick/high-layer boards; steam presses cannot reach high-temperature cures (post-bake PI/PPO/CE; not for PTFE thermoplastic adhesives); vacuum pre-cycle 15–60 min reduces edge voids | — | press type | lamination | review | §31.4.4 | high |
| COOMBS-2307 | fab | Cycle regions: B-stage melt (low "kiss" pressure), flow, cure, cooldown; hot-loaded press ≈ 20 °C/min → kiss only a few minutes; cold-loaded at 5 °C/min → ≈ 15 min kiss; LFAC: 0 psi, ≤ 15 °C/min to ≈ 90 °C internal, hold 30–40 min to drive moisture | see T-31.lam | material, press | lamination | measure | §31.4.5.1 | high |
| COOMBS-2308 | fab | Flow stage: up to 600 psi for fast-cure resin + fast ramp; ≈ 200 psi for slow ramp/long working time; critical range dicy FR-4 70–130 °C (4–8 °C/min at 200–300 psi); HF/LFAC 80–140 °C (2–4 °C/min at 225–360 psi); thermocouple at center-stack edge; improper melt staging → "footballing" (thick center) | see T-31.lam | material | lamination | measure | §31.4.5.2 | high |
| COOMBS-2309 | fab | Cure: epoxy ≈ 180 °C for 60 min; LFAC up to 200 °C internal for 120 min (longer if thick); polyimide higher/longer; cool through Tg isothermally, stress-free (controlled cooling press) to avoid warp | see T-31.lam | material | lamination | measure | §31.4.5.3–31.4.5.4 | high |
| COOMBS-2310 | materials | B-stage: solid melting near 90 °C; viscosity minimum = maximum flow; high-flow (long gel time) prepreg for fast-heating presses, low-flow for slow heating (else excess flow) | — | prepreg flow | lamination | review | §31.4.6 | high |
| COOMBS-2311 | stackup | Single-ply fill (e.g., one 7628 instead of two 1080) cuts cost, z-expansion and thickness variation; use two plies between planes with a large voltage bias (dielectric withstanding) or between layers with 70 µm copper (resin to encapsulate, avoid voids) | 2 plies if Cu ≥ 70 µm or high bias | V_bias, Cu | dielectric openings | review | §31.4.7 | high |
| COOMBS-2312 | fab | Lamination quality targets: flat, void- and moisture-free, fully cured, registered, thickness in spec, correct pressed dielectric around controlled-impedance layers; SPC per Table 31.4 variables (not in text) | — | coupons | lamination | measure | §31.5 | medium |
| COOMBS-2313 | fab | Voids: store B-stage dry (hygroscopic), dry C-stage cores; voids cluster at low-pressure panel edges → vacuum lamination or more pressure (not with high-flow resin → starvation) | — | — | lamination | inspect | §31.5.1.1 | high |
| COOMBS-2314 | dfm | Blisters/delamination form next to heavy copper borders: replace solid copper borders with dot or stripe patterns; match prepreg glass style/resin content to adjacent copper weight | — | artwork | ML boards | inspect | §31.5.1.2 | high |
| COOMBS-2315 | test | Cure check by two consecutive TMA Tg runs: ΔTg > 5 °C indicates under-cure (well-cured example: 3 °C) | ΔTg ≤ 5 °C | Tg1, Tg2 | lamination QC | measure | §31.5.1.3 | high |
| COOMBS-2316 | fab | Post-lamination bake (150 °C up to 4 h) is unnecessary with a proper cycle (polyimide excepted); baking beyond full cure degrades resin and lowers Tg; outer-board warp = non-uniform cooling; stress-relief bake only helps overdetermined tooling | — | — | lamination | review | §31.5.1.4, §31.6 | high |
| COOMBS-2317 | test | Non-dicy / halogen-free / LFAC boards: run finished parts through multiple production lead-free reflow cycles; inspect for blisters; cross-section high and low hole-density areas for delamination, laminate cracks, voids, hole-wall pull-away | ≥ multiple reflows | — | lead-free qual | measure | §31.5.2 | high |
| COOMBS-2318 | fab | PTH requirements: complete coverage, even thickness, no cracks, voids, nodules, inclusions, pull-away or epoxy smear, only minor resin recession, good metallurgy, ML compatibility ("hole-to-surface ratio of 0.001 in minimum" as printed) | — | cross-section | PTH | measure | §32.2.2 | high (as printed) |
| COOMBS-2319 | fab | ≈ 95 % of fabricators metallize holes with electroless copper; direct metallization (Pd, carbon-graphite, conductive polymer) avoids formaldehyde/chelators and heavy water use | — | — | hole metallization | review | §32.2.2 | high |
| COOMBS-2320 | fab | Process water: Ca, Si, Mg, Fe, Cl impurities cause oxidation, PTH residues, Cu-Cu peelers, staining, roughness, ionic contamination; RO at 1.4–4.2 MPa (200–600 psi) removes 90–98 % dissolved minerals and 100 % organics MW > 200; DI requirements pH 6.5–8.0, TOC 2.0 ppm, turbidity 1.0 NTU, chloride 2.0 ppm; mil-spec boards pass MIL-P-28809 ionic cleanliness (DI final rinse) | see T-32 | water analysis | wet process | measure | §32.3 | high |
| COOMBS-2321 | fab | Desmear/etchback baths need circulation and work-piece movement to push fresh solution through holes and avoid thermal stratification; high-AR holes may need vibration to release bubbles | — | AR | desmear | review | §32.4 | high |
| COOMBS-2322 | fab | Etchback exposes innerlayer Cu: two-point vs three-point connection; three-point (Cu protrudes) required on some mil-spec boards | — | spec | mil-spec PTH | measure | §32.4.2 | high |
| COOMBS-2323 | fab | Desmear choice: permanganate (preferred; electrolytic regeneration; texture for adhesion); plasma (any material, esp. PTFE; non-uniform; leaves ash → permanganate follow-up); chromic acid (Cr6+ neutralization voids; RoHS/waste → nonviable); sulfuric (out of favor); PTFE/Duroid need sodium-naphthalene pretreat; polyimide in chromic/plasma; lead-free/halogen-free resins need more aggressive cycles | — | resin system | desmear | review | §32.4.3–32.4.4 | high |
| COOMBS-2324 | fab | Electroless Cu sequence: clean/condition → microetch → (sulfuric) → predip → Pd/Sn catalyst → accelerator → electroless Cu 20–100 µin → antitarnish (rinses between; optional scrub and flash plate) | t_ELCu = 20–100 µin | — | hole metallization | review | §32.5.1, §32.5.4 | high |
| COOMBS-2325 | fab | Electroless defects: voids (check all tank times/temps/concentrations; low loading, low temp, high air agitation reduce activity; over-aggressive electrolytic preclean); hole-wall pull-away (poor texture, over-conditioning, over-catalyzation, insufficient acceleration, over-active stressed deposit); decomposition (imbalance, overload, overheat, idling, by-products); ICD (residues, poor rinse, insufficient microetch, stressed deposit); staining (moisture → antitarnish/DI rinse) | — | defect | electroless Cu | inspect | §32.5.3 | high |
| COOMBS-2326 | fab | Faraday's law anchor: 1.0 mil Cu needs 17.8 ASF for 60 min ("1.88 ASD" as printed; derived 1.92 ASD) → thickness_mil = J_ASF × t_h × η / 17.8 | 17.8 A·h/ft² per mil Cu | J, t, efficiency η | Cu electroplating | calc | §33.2, Eq. 33.1 (not in text), Table 33.1 | high (anchor) / medium (derived form) |
| COOMBS-2327 | fab | Throwing power TP = plated thickness at hole center / thickness at hole entrance; TP ≈ 100 % at 3:1 AR, ≈ 33 % at 15:1 (1.0 mil in hole → 3.0 mil on surface); optimized DC bath gave > 85 % TP on 15:1 at 8 ASF (text calls AR "hole diameter to board thickness" [sic, inverted]) | t_surface = t_hole / TP | AR, TP | high-AR PTH | calc | §33.3.1.2, Fig. 33.2 | high |
| COOMBS-2328 | fab | Plated copper: tensile strength > 35,000 psi and elongation > 15 % to survive fab/assembly thermal excursions; fine-grained equiaxed structure maximizes T&E | UTS > 35 kpsi; elongation > 15 % | T&E test | Cu plating | measure | §33.3.2 | high |
| COOMBS-2329 | fab | Surface uniformity: in pattern plating isolated traces/pads draw more current than ground-plane areas; panel plating gives uniform surface Cu but wastes copper and makes fine-line etch harder; hole knee over-plates ("dog bone") | — | pattern density | Cu plating | review | §33.3.1–33.3.1.1 | high |
| COOMBS-2330 | fab | Acid copper chemistry: CuSO4 (Cu ions), H2SO4 (conductivity), chloride (anode corrosion + carrier adsorption); low-CD bath = low Cu/high acid, high-CD bath = reverse (ratio table not in text); organics dosed by ampere-hours: carrier (suppressor, tighter grain, distribution), brightener (grain refiner, controls T&E), leveler (inhibits high-CD peaks) | — | CD | Cu plating | review | §33.3.3.1 | high |
| COOMBS-2331 | fab | Plating tank: inert PP/PVC; length = panel width + 12–16 in + 8–12 in weir well; breadth 18–30 in (anode basket-to-panel 6–12 in); depth = panel depth + 8–10 in; weir at the short end, top 5–8 in below solution surface; filter pump draws from the weir-well bottom and returns to the plating area (overflow also aerates) | see T-33.b | panel size | vertical Cu plating | review | §33.3.3.2 | high |
| COOMBS-2332 | fab | Soluble Cu anodes must be filmed (dummy plate at low CD) before use; use Ti baskets of Cu balls (constant area) rather than shrinking slabs; periodically remove small balls buried in sludge; PP anode bags loose, not napped, 2–3 in longer than basket; solution level below bag top | bag = basket + 2–3 in | — | vertical Cu plating | inspect | §33.3.3.3.1, §33.3.3.8.4 | high |
| COOMBS-2333 | fab | Insoluble MMO/Ti (iridium-oxide) anodes: constant area, no filming or anode maintenance, evolve O2, need an external Cu source (CuO dissolved outside the cell, dosed by Ah); standard in vertical/horizontal conveyorized lines | — | — | Cu plating | review | §33.3.3.3.1 | high |
| COOMBS-2334 | fab | Anode count/placement: panel plate 3–4 round baskets (2.5–3.5 in dia) per 18×24 in panel; pattern plate 2–3; distribute evenly on the bar; anodes 3–4 in shorter than the cathode and tucked 3–4 in inside the cathode window (less bottom/edge overplate) | 3–4 (panel) / 2–3 (pattern) baskets per 18×24 in | plating load | vertical Cu plating | inspect | §33.3.3.3.1, Fig. 33.7 | high |
| COOMBS-2335 | fab | Cathode racking: bar equidistant from front/back anodes; panels racked tightly and within 1.0 in of solution surface (deeper → top-edge overplate); rack full — fill gaps with dummy strips or isolate unmatched anodes | panel top ≤ 1.0 in below surface | rack | vertical Cu plating | inspect | §33.3.3.3.2 | high |
| COOMBS-2336 | fab | Agitation: cathodic through-hole agitation 1–3 in stroke at 10–20 strokes/min; solution agitation by air sparge (vigorous where leveler transport matters) or eductors (dual manifolds, staggered nozzles, nozzle top ≈ 6 in below panel bottom, laminar flow); air keeps Cu+ oxidized to Cu2+; knife-edge agitation unnecessary if anode-cathode distance is increased | 1–3 in, 10–20 strokes/min | — | Cu plating | review | §33.3.3.3.3–33.3.3.3.5 | high |
| COOMBS-2337 | fab | Filtration: continuous PP (polyspun) cartridges 5–10 µm; intake behind weir, return under the cathode; pump sized for 2–4 solution turnovers per hour (inert particles → pits; conductive → nodules) | 2–4 STO/h; 5–10 µm | bath volume | Cu plating | calc | §33.3.3.3.6 | high |
| COOMBS-2338 | fab | Acid Cu operates in a narrow temperature band (example 70–80 °F); eductor pumping heats the bath → Ti cooling coil with chiller | 70–80 °F (example) | T | Cu plating | measure | §33.3.3.3.7 | high |
| COOMBS-2339 | fab | DC rectifier: size to the load (don't plate 10–20 A on a 200 A unit); ripple < 5 % AC for fine-grained equiaxed deposit (T&E troubleshooting cites < 10 %); control resolution 1–2 % | ripple < 5 %; resolution 1–2 % | rectifier spec | Cu plating | measure | §33.3.3.4.1, §33.3.3.8.9 | high |
| COOMBS-2340 | fab | Periodic pulse reverse (PPR): e.g., forward 20 ASF for 10–20 ms then reverse 3× (60 ASF) for 0.5–1.0 ms, square wave, coaxial cables; improves distribution but gives a duller, different crystal structure → verify T&E; recipe per product | fwd 20 ASF 10–20 ms / rev 60 ASF 0.5–1.0 ms | waveform | high-AR plating | measure | §33.3.3.4.2 | high |
| COOMBS-2341 | fab | Lower CD improves thickness distribution (productivity cost); high-AR pattern plating uses 5–20 ASF long cycles, low-Cu/high-acid electrolyte with leveler, geometry and agitation for mass transfer | 5–20 ASF | AR | high-AR PTH | review | §33.3.3.4, §33.3.3.6.1 | high |
| COOMBS-2342 | fab | Horizontal conveyorized plating: module length = plating time × conveyor speed (20 ASF × 60 min at 1 m/min → 60 m; at 80 ASF → 15 m); high CD lowers throwing power; soluble anodes drop film particles → top-side nodules → use insoluble anodes; anode–cathode 8–10 mm (0.3–0.4 in) gives < 10 % surface variation (panel plate) | L = v·t; t = 17.8·mil/(J·η) h | v, J | horizontal plating | calc | §33.3.3.5–33.3.3.5.1 | high |
| COOMBS-2343 | fab | Horizontal plating limits: high capital; one panel dimension fixed to conveyor width; pattern-plate orders must clear before a different platable area enters; allow for anode gassing; learning curve; large spares inventory; all-or-nothing integration | — | — | horizontal plating | review | §33.3.3.5.2 | high |
| COOMBS-2344 | via | Blind-via fill plating: AR 1:1 common, up to 1.2:1 (deeper than diameter); electrolyte Cu 50–60 g/L with low H2SO4 30–60 g/L and strong leveler; vigorous laminar flow across the surface (else conformal, unfilled); 10–25 ASF, e.g., 12 ASF × 90 min, or 10 ASF × 30 min → 15 ASF × 20 min → 20 ASF × 20 min; dot-pattern plating needs planarization after strip | AR ≤ 1.2:1; Cu 50–60 g/L; acid 30–60 g/L | via d, depth | HDI filled microvias | calc | §33.3.3.6.2 | high |
| COOMBS-2345 | fab | Acid Cu control: titrate CuSO4, H2SO4, Cl−; Cu rises with soluble anodes → partial dump or plate-out on MMO anodes; organics by CVS (Hull cell only for simple premixed systems) | — | bath analysis | Cu plating | measure | §33.3.3.7.1–33.3.3.7.2 | high |
| COOMBS-2346 | fab | Organic contamination by TOC: baseline = fresh make-up (1×); carbon-treat at ≈ 4× (3× if deposit degrades); success when TOC falls to ≈ 70 % of the high value (e.g., 300 ppm base → run 850–1200 ppm); without TOC, treat every 100–120 Ah/L (dry-film pattern plate) | TOC_max = 4×base; post ≈ 0.7·TOC_max | TOC | Cu plating | measure | §33.3.3.7.3 | high |
| COOMBS-2347 | fab | Oxidative carbon treatment: 0.5 vol % of 35 % H2O2 + activated carbon ≈ 2 g/L, agitate at 120–140 °F for ≈ 4 h, cool, filter back; "carbon polish" = circulate through carbon without oxidant; duplicate the established recipe each time | — | — | Cu plating | review | §33.3.3.7.4 | high |
| COOMBS-2348 | fab | Acid Cu troubleshooting: knee (corner) cracking after thermal shock → coarse columnar crystals or over-leveling (adjust organics); columnar deposit → low brightener; hole voids → metallization voids, trapped air (cleaner wetting + vibration) or tin-resist voids (thicker tin); nodules → filtration/torn bags; burning → lower CD or higher-Cu bath; poor TP → CD too high for AR; excess leveling → step plating; low T&E → additives, organic contamination, ripple | — | defect | Cu plating | inspect | §33.3.3.8 | high |
| COOMBS-2349 | fab | Preplate: cleaner (solvent + acid + surfactant; wetting critical in small high-AR holes/blind vias; intermittent vibration; two-step rinse) → microetch (persulfate or peroxide/sulfuric; limited so electroless Cu is not etched through; double rinse) → predip 5–10 % H2SO4, no rinse before acid Cu | predip 5–10 % H2SO4 | — | Cu plating | review | §33.3.3.9 | high |
| COOMBS-2350 | fab | Tin etch resist (acid tin sulfate): ≈ 0.3 mil (7.5 µm) on traces and in holes for complete coverage; sacrificial, stripped after etch; 3–10 µm PP filtration, no air introduced, cathode-rod agitation for holes, continuous carbon filtration | t_Sn ≈ 7.5 µm | — | pattern plate etch resist | measure | §33.4.1 | high |
| COOMBS-2351 | fab | Tin bath contaminant limits: Cu 5–10 ppm (darkness), Cd 50 ppm, Zn 50 ppm (dullness), Ni 50 ppm (streaks), Fe 50–120 ppm (dullness), Cr 5 ppm, Cl− 75 ppm; remove metals by dummy plating at 2–5 ASF; electronic-grade chemicals | see T-33.d | bath analysis | tin plating | measure | §33.4.1.2–33.4.1.3 | high |
| COOMBS-2352 | fab | Tin problems: dull (acid < 10 %, tin > 3 oz/gal, additives, contamination, temperature > 65 °F); peeling (acid < 10 %, organics); slivers (over-etching → revise etch, thinner foil); pitting (preclean, balance, contaminants, high CD) | — | defect | tin plating | inspect | §33.4.1.4 | high |
| COOMBS-2353 | fab | Nickel is the undercoat/diffusion barrier under gold for contacts, soldering, wire bonding; MIL-STD-275 low-stress nickel ≥ 0.0002 in; sulfamate bath preferred at 125 °F (low T → stress, burning; high T → softer); lower pH only with sulfamic acid (never sulfuric); falling pH → check anodes; 5–10 µm filtration | t_Ni ≥ 0.0002 in (200 µin) | — | Ni/Au tabs | measure | §33.5–33.5.1.1 | high |
| COOMBS-2354 | fab | Nickel sulfamate rate: 0.5 mil in 25–30 min at 25 ASF; 0.2–0.3 mil in 15 min at 25 ASF | — | J, t | Ni plating | calc | §33.5.1.1.5 | high |
| COOMBS-2355 | fab | Nickel sulfamate contaminant limits: Fe 250, Cu 10, Cr 20, Al 60, Pb 3, Zn 10, Sn 10, Ca 0 ppm (Cu/Pb → dark brittle low-CD deposits; Fe/Sn/Pb/Ca → roughness, stress); dummy plate at 3–5 ASF; never add sulfates; batch carbon treat 140 °F, 3–5 lb carbon/100 gal, stir 4 h, settle 1–2 h, filter back (pH unadjusted) | see T-33.d | bath analysis | Ni plating | measure | §33.5.1.1.6–33.5.1.1.7 | high |
| COOMBS-2356 | fab | Nickel QC: Hull cell 2 A × 10 min; antipit test — bubble holds 5 s in a 3-in wire ring and < 5 s in a 5-in ring; severe pitting: cool, add 1 pt/200 gal 35 % H2O2, air, reheat to 140 °F, carbon treat; deposit stress < 10 kpsi (control pH, CD, boric acid; high chloride → stress, low chloride → poor anode corrosion); sulfate tab baths ≈ 20 kpsi, pH ≥ 1.5 via nickel carbonate, nickel anodes | stress < 10 kpsi (sulfamate) | stress, antipit | Ni plating | measure | §33.5.1.2, §33.5.2 | high |
| COOMBS-2357 | connectors | Edge-connector hard gold: MIL-STD-275 → MIL-G-45204 Type II Class 1, 50–100 µin (0.000050–0.000100 in); commercial 25–50 µin; always over low-stress nickel; Co/Ni/Fe-hardened acid gold (potassium gold cyanide); Type II hard gold is not wire-bondable | Au 50–100 µin (mil), 25–50 µin (commercial) | class | gold fingers | measure | §33.6.1 | high |
| COOMBS-2358 | fab | Gold bath control: gold content, pH (acid 3.5–5.0; neutral 6–8.5), density via conductivity salts (no Hull cell); replace platinized-Ti anodes on high voltage/coatings; replace solution after ≈ 10 gold turnovers or contamination; gold peeling from Ni → poor Ni activation (acid dip, fluoride activator or gold strike), leaky tape, poor solder strip | ≈ 10 turnovers | bath analysis | gold plating | measure | §33.6, §33.6.1.1 | high |
| COOMBS-2359 | assembly | Soft 99.99 % gold (MIL-G-45204 Types I & III) for die attach, wire bonding, glass-device soldering (neutral pH 6–8.5 or acid 3–6); alkaline noncyanide sulfite gold (pH 8.5–10, 180 Knoop) for body plating only — not for edge-connector wear | — | application | wire-bond/die-attach pads | review | §33.6.1.2, §33.6.2 | high |
| COOMBS-2360 | test | Gold QC: thickness by beta backscatter or XRF (to 1 µin on 5-mil pads); adhesion by tape pull; porosity by nitric-acid vapor or electrographic test; lead impurity < 0.1 %; also heat discoloration, contact resistance, wear | Pb < 0.1 % | — | gold plating | measure | §33.6.3 | high |
| COOMBS-2361 | fab | Direct metallization (DMT): holes need more thorough conditioning than for electroless; conductive media must be removed from Cu foil (except DMS-E); horizontal DMT ≈ 6–15 min per panel, panels 1 in apart; often better than electroless on PTFE, cyanate ester, polyimide | 6–15 min/panel | — | hole metallization | review | §34.1.1 | high |
| COOMBS-2362 | fab | DMT families: Pd-based (EE-1 with mandatory flash plate, 5–6 min coverage; DPS vanillin; Crimson PdS; ABC; Conductron; Neopact tin-free Pd), carbon/graphite (Black Hole II double carbon pass; Shadow graphite), conductive polymer (DMS-E poly-EDT via MnO2 at 80–90 °C; Compact CP polypyrrole) | — | — | hole metallization | review | §34.1.2–34.1.4 | high |
| COOMBS-2363 | test | DMT QA: little is visible in the hole after DMT; the only certain void check is flash electroplating (DPS suggests an ohm-meter check); some DMTs are more sensitive than electroless to organic contamination in acid Cu; rework is easy but can be abused | — | — | DMT lines | measure | §34.1.2.2, §34.1.8 | high |
| COOMBS-2364 | cost | PTH metallization is only 2–3 % of total PCB process cost; DMT gains are water, chemicals, waste, handling, labor and rejects rather than direct cost | 2–3 % | — | cost model | calc | §34.1.9 | high |
| COOMBS-2365 | solder | Pb-free assembly (WEEE/RoHS) changes finish selection: HASL (SnPb) increasingly obsolete; wettability, PTH fill and voiding worsen; higher soldering temperature shortens finish shelf life and solderability — select finish together with the solder alloy | — | alloy, finish | all finishes | review | §35.1.2 | high |
| COOMBS-2366 | requirements | Finish requirement checklist — fabricator: cheap equipment/high throughput, electrically testable, no mask attack, non-toxic, reworkable, measurable, handling-insensitive, long shelf life; assembler: flat for stencil, low ICT contact resistance, misprint-clean tolerant, incoming shelf life > 1 year, mid-assembly shelf life > 2 weeks, all pastes/fluxes, Al/Au wire bond, inspectable, predictable wetting, fiducial recognition, no warp, compliant-pin contact, Pb-free soldering without N2, no bridging/plugged holes; OEM: joint reliability, cost, field corrosion resistance, test point/EMI shield, keypad contact, high-speed signal performance, specs, documentation, audited supply base | shelf life: incoming > 1 yr; mid-assembly > 2 wk | finish choice | all | review | §35.1.4–35.1.6 | high |
| COOMBS-2367 | solder | HASL: SnPb or Pb-free (SnCu, SAC, SnCuNi, SnCuNiGe); thickness 2 to 20 µm or more (surface-tension driven, non-planar); excellent shelf life and handling tolerance; higher ionic residues (aggressive acid flux → aggressive rinse); extra thermal excursion consumes Cu, thickens IMC, warps/twists; bridging at fine pitch; dense circuitry < 0.5 mm pitch difficult or impossible; forms Cu/Sn IMC; cheapest finish | t = 2–20+ µm; pitch ≥ 0.5 mm | pitch | HASL | review | §35.3 | high |
| COOMBS-2368 | solder | ENIG thickness per IPC-4552 (2002): electroless Ni 3–6 µm (118.1–236.2 µin); immersion Au ≥ 0.05 µm (1.97 µin) at −4σ, typical 0.075–0.125 µm (2.955–4.925 µin), no upper limit (the "typical range" is not a spec limit); IPC-4552 Rev A draft: Au 1.6–4.0 µin plus a nickel-corrosion (black pad) acceptance chart | Ni 3–6 µm; Au ≥ 1.97 µin (−4σ) | XRF readings | ENIG | measure | §35.4.1 | high |
| COOMBS-2369 | solder | ENIG: flat coplanar (fine pitch), Ni/Sn IMC, Al and Cu wedge wire-bondable, contact surface, press-fit, shelf life > 12 months, Ni reinforces PTH ("rivet") and blocks Cu dissolution, no bussing needed; limitations: complex process, thick Ni may degrade high-frequency propagation, hard to rework, costly, black pad; not a reliable Au wire-bond surface (Ni diffuses through Au grain boundaries) | shelf life > 12 months | application | ENIG | review | §35.4, §35.4.4, §35.5 | high |
| COOMBS-2370 | reliability | Black pad (nickel corrosion under immersion Au): caused by extended dwell in an aggressive gold bath (Au concentration below supplier range) acting on compromised Ni (uneven, creviced deposit from uneven catalysis/initiation or out-of-range EN bath); symptoms poor wetting, weak joints, ball-pull failure at Ni–solder interface with dark pad; prevention = uniform catalysis/initiation and Au bath kept in range | — | process data | ENIG | inspect | §35.4.4 | high |
| COOMBS-2371 | fab | ENIG line: cleaner → microetch → catalyst (Pd or Ru by immersion) → electroless Ni → immersion Au (rinses, pre/post dips, dedicated drying); always vertical tanks (long dwell, high temperature); two EN tanks for throughput; stainless EN tanks require anodic passivation; board substrate and solder mask must tolerate the hot, long EN dwell | — | — | ENIG | review | §35.4.3 | high |
| COOMBS-2372 | solder | ENEPIG per IPC-4556 (2013): Ni 3–6 µm (118.1–236.2 µin) at ±4σ; Pd 0.05–0.15 µm (2–12 µin) at ±4σ; Au ≥ 0.025 µm (1.2 µin) at −4σ; measured on a 1.5×1.5 mm (0.060×0.060 in) pad; amendment draft caps Au at 2.8 µin (printed "0.7 µm", sic — 2.8 µin ≈ 0.07 µm) because thicker immersion Au (longer dwell) corrodes Ni under the Pd; prose values: Ni 120–240 µin, Pd 2–12 µin, Au flash 1–2 µin | see T-35 | XRF readings | ENEPIG | measure | §35.5, §35.5.1 | high (as printed) |
| COOMBS-2373 | assembly | ENEPIG is Au-wire-bondable (Pd blocks Ni diffusion) with Au as low as 1.2 µin (0.03 µm); 0.1–0.2 µm (4–8 µin) Au widens the bond window but exceeds standard immersion Au → use reduction-assisted immersion gold | Au ≥ 1.2 µin | Au thickness | Au wire bond | measure | §35.5, §35.5.3.2 | high |
| COOMBS-2374 | materials | Electroless Pd with hypophosphite reducer contains 4–5 % P → amorphous, ideal diffusion barrier; non-P Pd is crystalline | P = 4–5 % | reducer | ENEPIG | review | §35.5 | high |
| COOMBS-2375 | solder | ENEPIG gives the most robust joint with SAC alloys (Cu and Pd incorporated in the Ni/Sn IMC limit IMC growth under thermal stress/aging); "universal" finish: soldering, Au/Al/Cu wire bond, membrane and steel-dome contacts, LIF/ZIF edge connectors, press-fit; shelf life > 12 months; complex, costly, hard to rework | — | application | ENEPIG | review | §35.5.3–35.5.4 | high |
| COOMBS-2376 | solder | OSP (benzotriazole, imidazole, benzimidazole, phenyl-benzimidazole): meets J-STD-003 category 3 coating durability (12-month shelf life) when processed per vendor (some only cat 1–2); Pb-free peak 260 °C is 35 °C above 225 °C eutectic → use high-temperature OSP (up to 1.0 µm, survives multiple reflows); apply after ET/rout/depanel; stabilize at room T/controlled RH before packing; thickness by UV spectrophotometry of a dissolved coupon or optical-reflectivity interference | shelf 12 months (cat 3); t ≤ 1.0 µm | OSP type | OSP | measure | §35.6–35.6.1 | high |
| COOMBS-2377 | solder | OSP limitations: handling/fingerprint sensitive, soldering-only, limited shelf life, exposed Cu after assembly, hard to inspect/verify thickness, problematic for paste misprint cleaning, nonconductive surface (no probing); avoid for fine pitch and high-AR holes | — | application | OSP | review | §35.6, §35.6.2 | high |
| COOMBS-2378 | solder | Immersion silver per IPC-4553A (2009): 0.12 µm (5 µin) min to 0.4 µm (16 µin) max at ±4σ on a 2.25 mm² (1.5×1.5 mm) pad; typical 0.2–0.3 µm (8–12 µin); do not call out the obsolete 2005 IPC-4553; predip excludes chloride (AgCl precipitation) | 0.12–0.4 µm | XRF | ImAg | measure | §35.7 | high |
| COOMBS-2379 | dfm | Immersion silver design rules: anti-tarnish overlay; no solder-mask-defined pads; vias completely filled; print paste over the entire pad; keep test pads ≥ 80 mil apart; paste-and-reflow test pads; special packaging for 12-month shelf; exposed Ag tarnishes → creep corrosion; may attack mask interface | test-pad spacing ≥ 80 mil | layout | ImAg | inspect | §35.7.2 | high |
| COOMBS-2380 | solder | Immersion tin: typical 0.6–1.2 µm; IPC-4554 (2007): ≥ 1.0 µm (40 µin) at −4σ on a 2.25 mm² pad (printed "2.25² µm (3600² mils)"), typical 1.15–1.3 µm (46–52 µin); 2011 amendment on solderability stress tests and fluxes; Cu-Sn IMC grows with time/temperature so enough virgin tin must remain | t ≥ 1.0 µm (−4σ) | XRF | ImSn | measure | §35.8 | high (as printed) |
| COOMBS-2381 | solder | Immersion tin chemistry uses thiourea: dedicate the line (sulfur harms OSP, Ag, ENIG surfaces), treat thiourea in waste; limitations: oxidizes with moisture/air, whiskers, soft/handling-sensitive, may attack mask interface, IMC growth confounds thickness measurement; excellent for compliant (press-fit) pins, reworkable | — | — | ImSn | review | §35.8.1–35.8.3 | high |
| COOMBS-2382 | connectors | Electrolytic Ni/Au: several µm Ni + 0.50–1.5 µm Au for high-force contacts or Au wire bonding; not recommended as a soldering surface (thick Au embrittles the joint IMC); multi-insertion contacts need hard gold alloyed with ≈ 3 % Ni, Cr or Fe [as printed; Ch. 33 says Co, Ni or Fe]; Au wire bond needs soft 99.99 % Au, thick enough that Ni cannot diffuse to the surface | Au 0.50–1.5 µm | application | Ni/Au | review | §35.9.2 | high |
| COOMBS-2383 | solder | Other finishes: electroless Pd ≈ 0.1 µm (4.0 µin) solderable/contact (displaced by ImAg on Pd price); EPIG (no Ni) for very fine pitch and high-frequency (avoids Ni skin-effect loss), no IPC spec; EN + immersion Au + electroless soft Au for Au wire bond (uniform thickness, avoids embrittlement); direct immersion Au on Cu for short shelf life and single thermal excursion (discolors via Cu–Au interdiffusion but stayed solderable after 3+ years ambient); reflowed SnPb only for simple technology | — | application | special finishes | review | §35.9 | high |
| COOMBS-2384 | fab | > 98 % of solder mask is applied as liquid, mostly photoimageable (LPI); dry-film solder mask needs special equipment, is expensive, often not robust as a resist for ENIG/immersion tin, and too thick for some assembly | — | mask type | all | review | §36.1.3, §36.3.2 | high |
| COOMBS-2385 | dfm | Solder-mask webs (dams) between fine-pitch pads are frequently 0.003 in and can be as narrow as 0.001 in; typical 2.5–3.0 mil, some designs 1.0–1.5 mil (not all materials; modified imaging); fine webs require photoimageable mask | web ≥ 2.5–3.0 mil (standard); 1.0–1.5 mil (special) | web width | fine-pitch SMT | inspect (DRC) | §36.3.2, §36.4.4.2, Fig. 36.1 | high |
| COOMBS-2386 | fab | LPI enters holes during coating and must be developed out before cure: spray leaves least, single-sided screen most, curtain and double-sided screen moderate; over-aggressive tack dry (too hot/long) slows development; set developer chemistry, pressure, flow, nozzles, time per supplier | — | coating method | small holes | inspect | §36.2.1.2, §36.4.4.1 | high |
| COOMBS-2387 | via | HDI microvias under mask: develop cleanly so they receive final finish, protect first with an inert finish, or plug completely — partially masked microvias trap air → blister/eruption exposing Cu; plated-over microvias must be fully filled, planarized, roughened and catalyzed (conductive fill may skip catalysis); via-in-pad fill must not shrink (dimple), critical for wire-bond flatness | — | via protection | HDI | inspect | §36.2.3 | high |
| COOMBS-2388 | materials | Pb-free soldering raises mask stress: operating temperature up to 30 °C (54 °F) above eutectic SnPb (elsewhere "typically 10–20 °C"; SAC305 melts 34 °C higher) → verify mask resists embrittlement, discoloration, adhesion loss and cracking over repeated exposures | ΔT up to +30 °C | mask data | Pb-free | measure | §36.2.2, §36.4.3.2 | high |
| COOMBS-2389 | compliance | Solder mask must be RoHS-compliant (2002/95/EC; 2003/11/EC) and, where required, low-halogen (limits on Br, Cl and their sum — table not in text); mask Cl comes from pigments and resin-catalyst residue | Br/Cl limits (not in text) | material declaration | RoHS / low-halogen | review | §36.2.4, §36.4.3 | medium |
| COOMBS-2390 | compliance | Air-emission limits (HAPs, VOCs) can rule out curtain or spray mask coating (high solvent); screen printing at higher solids emits about half | — | local permits | mask coating | review | §36.2.4 | high |
| COOMBS-2391 | compliance | Mask qualification: IPC-SM-840 (predominant; physical, chemical, thermal, electrical; two classes; Class T accepted by Telcordia as equivalent to GR-78-CORE); UL94 flammability on the specific base/construction (thinner mask + thicker base scores better); MIL-P-55110 defers to IPC-SM-840; NASA outgassing TML ≤ 1.0 %, CVCM ≤ 0.10 %; AABUS extras; package substrates also need JEDEC tests (low moisture absorption) | TML ≤ 1.0 %; CVCM ≤ 0.10 % | mask data | mask selection | review | §36.4.2, §36.4.9 | high |
| COOMBS-2392 | assembly | Excess mask thickness causes tombstoning (reflow), opens on discretes (wave), paste-printing defects (excess paste, solder balls, paste on stencil back); flip-chip further limits max mask thickness (dry-film mask mostly eliminated) | — | mask thickness | SMT, flip-chip | measure | §36.4.5.1 | high |
| COOMBS-2393 | assembly | Qualify each mask through the full assembly flow: fluxes/pastes, cleaners, multiple heat exposures, adhesives, underfills, temporary masks, tapes; ionic and visual cleanliness; solder balls (satin/matte finish or supplier-approved cure change may reduce); conformal-coat adhesion tested after full assembly (coatings are not meant for no-clean residue) | — | assembly materials | mask/supplier change | measure | §36.4.5 | high |
| COOMBS-2394 | fab | Mask/finish compatibility: ENIG and immersion-tin baths attack masks to differing degrees → qualify the mask–chemistry pair (thicker mask helps); excessive pre-finish microetch undercuts mask → tape-test failures; immersion Ag and OSP are benign; Pb-free HASL adds stress and cleaning difficulty | — | finish chemistry | mask + finish | measure | §36.4.10 | high |
| COOMBS-2395 | fab | Mask surface prep: remove all tin/solder etch-resist residue (mask won't adhere to Sn, solder or Cu-Sn IMC); pumice (silica or Al2O3) brush or jet scrub to a uniform rosy-pink, matte, stain-free copper; replace media (silica fractures; Al2O3 rounds and peens); chemical microetch must leave a matte tooth; rinse, dry, passivate promptly | — | surface | mask prep | inspect | §36.5.1 | high |
| COOMBS-2396 | fab | Brush/compressed-pad abrasion is acceptable before mask on HASL boards but not for ENIG/immersion tin: directional scratches wick plating chemistry under the mask → adhesion loss around openings → follow with chemical micro-roughening; reduced-oxide treatment gives very good adhesion (oxide won't form on dirty/residue copper) | — | final finish | mask prep | review | §36.5.1.1.2 | high |
| COOMBS-2397 | fab | Rinse before mask with DI (or RO) water, not city/well water (minerals → mask blistering, Cu discoloration under mask); air knives clear surface and holes; never let droplets dry on panels | DI/RO water | water quality | mask prep | inspect | §36.5.1.1.3 | high |
| COOMBS-2398 | fab | Gold/tin/solder surfaces: no prep if clean, else rinse or mild detergent — never abrasive; mixed-metal panels (selective solder strip, gold fingers) → prep chosen for the most delicate metal | — | metals present | mask prep | review | §36.5.1.2 | high |
| COOMBS-2399 | fab | LPI screen printing (most common): non-calendared nylon mesh (e.g., 86-120, 83-100, 86-100, 92-100, 110-80 threads/in–thread µm; supplier gives theoretical ink volume); vertical double-sided printing puts less mask in holes (front/back squeegee alignment critical); single-sided: coat both sides (dimple plate) before tack dry so both see the same cycle | — | mesh | mask coating | review | §36.5.2.1.1, Table 36.1 (not in text) | high |
| COOMBS-2400 | fab | Spray (HVLP common; electrostatic needs Faraday-effect tuning and reformulated masks) gives most latitude for clean small holes but high VOCs; heated ink improves coverage; curtain coating is productive, uniform, high utilization but needs stable temperature/viscosity (else thick/thin, streaks, skips/"blips"), is sensitive to circuit height, thin panels fly and thick panels slip | — | method | mask coating | review | §36.5.2.1.1, Tables 36.2–36.3 (not in text) | high |
| COOMBS-2401 | fab | Tack dry promptly after coating; panels must not touch; allow 5–10 min maximum debubble; airflow parallel to panels; adequate purge air; clean condensate; profile time-at-temperature including ramp-up (don't open batch-oven doors); under-dry → sticky, artwork marking; over-dry → "lock-in" (undevelopable) | debubble ≤ 5–10 min | oven profile | LPI mask | measure | §36.5.2.1.2, Table 36.4 (not in text) | high |
| COOMBS-2402 | fab | Mask exposure: modern units use ≥ 7 kW lamps with lamp/frame cooling; verify intensity (mW/cm²) and energy (mJ/cm²) with a radiometer at the mask's wavelength; aging lamps lengthen exposure and add IR (hot frames → artwork sticking/marking); LDI removes mask registration error but is slower and costly (may need laser-sensitive mask) | lamp ≥ 7 kW | dose | mask exposure | measure | §36.5.2.1.3 | high |
| COOMBS-2403 | fab | Under-exposure → dull/chalky surface, lifted dams, undercut sidewalls, lifted mask; over-exposure → image growth, smaller openings, mask encroaching pads | — | exposure dose | mask exposure | inspect | §36.5.2.1.3 | high |
| COOMBS-2404 | fab | Mask develop: aqueous warm Na2CO3/K2CO3 at pH 10.6–11.3 with antifoam (or solvent: GBL, butyl carbitol); set breakpoint at 10–15 % of the developer chamber (vs ≈ 50 % for photoresist) so the smallest holes clear; inspect immediately after develop (registration, mask in holes, resolution, dam retention, lifting) — rework after cure is far harder | pH 10.6–11.3; breakpoint 10–15 % | developer | LPI mask | measure | §36.5.2.1.4 | high |
| COOMBS-2405 | fab | Dry-film solder mask must be vacuum laminated (heated platens + diaphragm); standard hot-roll lamination traps air along circuits (unacceptable except least demanding work) | — | laminator | DFSM | review | §36.5.2.2 | high |
| COOMBS-2406 | fab | Non-imageable UV/thermal masks need a patterned screen with accurate registration (no develop correction); inkjet solder mask (mostly UV-cure) removes photo steps and registration issues | — | method | non-LPI mask | review | §36.5.2.3 | high |
| COOMBS-2407 | fab | Cure per supplier (thermal time-at-temperature plus ramp; IR shorter/hotter with multiple recipes; calibrated UV units); undercure → blistering/adhesion loss in finish or assembly, high ionics, soldering residues, solder balls, soft coating; overcure → embrittlement, cracking, adhesion loss | — | cure profile | mask cure | measure | §36.5.3 | high |
| COOMBS-2408 | fab | Mask stripping gets harder at each step: after coating (tack dry, then develop off), after imaging (hot caustic; risks butter coat and mask-filled holes), after cure (may be impossible) → catch defects before cure | — | — | mask rework | review | §36.5.4 | high |
| COOMBS-2409 | via | Protect vias from both sides (IPC-4761, July 2006): single-sided protection before an "inert" final finish leaves a ring void at the barrel–plug interface that traps microetch/flux → corrosion; some plug materials leach (poison plating baths, high ionics, electrochemical migration) | two-sided protection | via plan | via protection | inspect | §36.6.1 | high |
| COOMBS-2410 | via | Plug materials (no official spec): apply UL94 and IPC-SM-840 tests (solvent/cleaner resistance, non-nutrient); solvent-bearing LPI shrinks → dimple and thin knee → use high-solids or 100 % solids inks; via-in-pad/sub-composites need platable fill (roughen, catalyze, plate, Cu adhesion); photoimageable plug near SMT pads; thermal vias use Ag/Cu-loaded fill; low-CTE/high-Tg benefit unproven | — | plug material | via plugging | review | §36.6.2–36.6.3 | high |
| COOMBS-2411 | fab | Legend: screened UV or thermal ink, photoimageable legend (high pigment → thinner, less chipping, best resolution over topography) or inkjet; contrasting color; no IPC spec (IPC-4781 drafted); military uses CID A-A-56032D epoxy ink (waivers possible); UL94 qualification required if any legend area exceeds a UL flame strip (½ × 5 in); poor adhesion over HASL flux residue; qualify legend with mask and final finish | legend area > ½×5 in → UL test | legend layout | nomenclature | inspect | §36.8 | high |
| COOMBS-2412 | fab | Mainstream etchants are continuous constant-rate alkaline ammonia and cupric chloride (also peroxide–sulfuric, persulfates, ferric chloride); chromic–sulfuric and ammonium persulfate are no longer practical (environmental); target fine-line 0.0015–0.003 in circuits in volume | lines 0.0015–0.003 in | — | etching | review | §37.1, §37.4 | high |
| COOMBS-2413 | fab | Screened etch resist: positive pattern (circuit only) for etch-only boards, negative (field only) for PTH/metal-resist boards; must adhere, resist etchant, be pinhole/bleed-free, strip cleanly; typical problems: excessive undercut, slivers, unetched areas, innerlayer shorts, line lifting (low peel or contamination) | — | resist | print-and-etch | inspect | §37.2.1 | high |
| COOMBS-2414 | fab | Photoresists protect better in acid than alkaline etchants (negative types more alkali-tolerant); positive resists stay light-sensitive after developing (protect from white light); liquid resists resolve finer but are less durable | — | resist tone | etching | review | §37.2.4 | high |
| COOMBS-2415 | fab | Metal etch resist vs etchant: tin (≈ 0.0002 in, SMOBC, stripped after etch) → alkaline ammonia (or special peroxide–sulfuric / persulfate–phosphoric for bright tin); cupric and ferric chloride attack tin and solder → never use; solder plate 60Sn/40Pb 0.0003–0.001 in for fusing (thin 0.0002 in gives no SMOBC benefit over tin), needs brightener; Sn-Ni (65/35) and Ni resist ammonia, peroxide–sulfuric, persulfates; gold over Ni or Sn-Ni resists all common etchants; rhodium over Ni is thin/porous and lifts; silver loses ≈ 0.0001 in "/mm" [as printed] in ammonia and is barred by MIL-STD-275 | see T-37.a | resist, etchant | etching | review | §37.2.5 | high |
| COOMBS-2416 | fab | After etch: immediate thorough water rinse plus acid neutralization (alkaline etch → acidic ammonium chloride; ferric/cupric → HCl or oxalic; persulfate → sulfuric); residues left before drying/reflow lower dielectric insulation resistance and degrade contact/solderability; strip plating resist fully (including under plating overhang); gold, solder and tin scratch easily | — | rinse sequence | post-etch | measure | §37.2.5.7 | high |
| COOMBS-2417 | dfm | Edges of printed areas clear faster than broad copper → fine lines undercut while field copper clears; use low-pooling etchers, fine-line etchants, high-resolution resists, thin-clad laminates, controlled plating distribution, thin base foil; some fine-line additives hinder cleanout in spaces ≤ 0.003 in | spaces ≤ 0.003 in need care | pattern density | fine-line etch | review | §37.2.5.7 | high |
| COOMBS-2418 | fab | Resist stripping: chlorinated solvents and cyclic aromatics banned, glycol ethers restricted → aqueous strippers; screen resists in 2 % NaOH or proprietary; alkaline strippers can attack polyimide/epoxy (measling, staining) → control concentration, temperature, dwell; dry film in conveyorized aqueous spray, strip promptly (lock-in), filter the skins (Pb content can make them hazardous waste); negative liquid resists need minimal bake; positive resists strip in 0.5 N NaOH + surfactants | NaOH 2 % (screen); 0.5 N (positive) | resist | stripping | review | §37.3 | high |
| COOMBS-2419 | fab | Tin/tin-lead resist stripping: oxidizing fluoride solutions (fluoboric acid + H2O2; ammonium bifluoride + H2O2 or HNO3) — machine must exclude titanium and glass; lead-fluoride deposits are hazardous waste; lead-free tin strippers (fluoride, or ferric chloride then nitric) with feed-and-bleed, filtration and periodic cleanout | — | stripper | SMOBC | review | §37.3.3 | high |
| COOMBS-2420 | fab | Alkaline ammonia etchant: NH4OH (complexer), NH4Cl (rate, Cu capacity, stability), Cu2+ (oxidizer), NH4HCO3 (buffer), (NH4)3PO4 and NH4NO3 (clean solder/holes), thiourea-type or thiourea-free sidewall additives; pH 7.5–9.5; holds 18–30 oz/gal Cu as Cu(NH3)4 2+; rate limited by diffusion of Cu(NH3)2+ and air re-oxidation; run 120–130 °F with slight negative-pressure exhaust but enough fresh air for O2; etches 1 oz (35 µm) Cu in ≤ 1 min at 18–24 oz/gal Cu | see T-37.b | chemistry | ammonia etch | measure | §37.4.1–37.4.1.2 | high |
| COOMBS-2421 | fab | Ammonia bleed-and-feed: density sensor triggers replenisher feed + etchant bleed; feed the replenisher through the first rinse (recaptures dragged Cu); pH 7.9–8.1 improves reliability with aqueous resists — control by anhydrous NH3 injection on pH (exhaust control is unreliable); also control free NH3, NH4Cl and O2; rinse immediately (never let boards dry), multi-stage cascade rinse, air-knife dry | pH 7.9–8.1 (aqueous resists) | pH, density | ammonia etch | measure | §37.4.1.3 | high |
| COOMBS-2422 | fab | Ammonia troubleshooting: low rate + pH < 8.0 (over-ventilation, heating, downtime → add anhydrous NH3); low rate + pH > 8.8 (high Cu, water, under-ventilation); low rate at optimum pH (Cu thickness error, O2 starvation, contamination); solder attack (excess chloride, bad Sn/Pb, low phosphate); sludge gritty dark-blue at pH < 8.0 (add NH3) vs fluffy light-blue at pH > 8.8 (Cu exceeds chloride capacity → add NH4Cl; water); fumes → leaks; Cu-bearing rinses treated separately from ammonia rinses; thin-clad panels drag more etchant | pH window 8.0–8.8 | pH, sludge color | ammonia etch | inspect | §37.4.1.5 | high |
| COOMBS-2423 | fab | Closed-loop ammonia regeneration (crystallization, liquid–liquid extraction with hydroxy-oximes → CuSO4 for electrowinning, electrolytic/membrane recovery) is capital- and labor-intensive and copper-price dependent; standard practice is supplier recycling of spent etchant with returned replenisher | — | — | etch waste | review | §37.4.1.4 | high |
| COOMBS-2424 | fab | Cupric chloride: etchant of choice for precision small features and photopolymer resists (fine-line innerlayers, print-and-etch, panel-plate/tent-and-etch; also screened inks, gold, Sn-Ni); must be regenerated continuously (Cu+ build-up slows it); incompatible with solder and tin resists; rate governed by chloride concentration and diffusion of the Cu(I) chloro-complex | — | resist | cupric etch | review | §37.4.2–37.4.2.1 | high |
| COOMBS-2425 | fab | Cupric chloride rates: CuCl2–NaCl–HCl at 130 °F etches 1 oz Cu in as little as 55 s at ≥ 20 oz/gal Cu; higher-Cu chemistries at 125 °F typically 75–90 s per 1 oz (inherently slower than ammonia) | 55 s @ 130 °F; 75–90 s @ 125 °F per 1 oz | T, Cu | cupric etch | measure | §37.4.2.2, Table 37.1 (not in text) | high |
| COOMBS-2426 | fab | Cupric regeneration: air/O2 too slow (O2 solubility 4–8 ppm hot; ozone < 3 %); direct chlorination (fast, no water/acid imbalance; ORP, density, level, temperature control; Cl2 safety — ventilation, leak detection, PPE, training, fire approval; excess NaCl at 18–20 oz/gal Cu co-precipitates on cooling; colorimeters foul); sodium chlorate (45 % solution, free acid < 0.1 N; oxidizer supports combustion; low acid then acid addition releases Cl2; watch water balance); H2O2 (≤ 35 %, adds water; decomposition catalyzed by Cu/Ni/Fe — pressure relief on piping); electrolytic (high capital/power, high acid/low Cu) | free acid < 0.1 N (chlorate) | regen type | cupric etch | review | §37.4.2.1–37.4.2.3 | high |
| COOMBS-2427 | fab | Cupric troubleshooting: slow etch (formulation, resist/chromate residue, low temperature, poor sump mixing; dark-green solution = low Cu2+ → oxidizer; cloudy → acid only after confirming no excess oxidizer); chart specific gravity, free acid and total chloride; sludge = low acid or water dilution | — | SG, acid, Cl | cupric etch | measure | §37.4.2.4 | high |
| COOMBS-2428 | fab | Cupric etcher maintenance: "goop" (leached photoresist, worse at high acid) limited by proper resist exposure and continuous carbon filtration, periodic drain-down and sulfamic-acid cleaning; yellow (cuprous hydroxide) or white (cuprous chloride) residues → final pre-rinse in 5 vol % HCl; spent etchant must be free of unreacted oxidizer before shipment; etchant carries Zn, Cr, As traces from foil treatments | pre-rinse 5 vol % HCl | — | cupric etch | inspect | §37.4.2.4 | high |
| COOMBS-2429 | fab | Sulfuric–peroxide: mainly a microetch; renewed use for fine-line etching of foils < ½ oz (slow, controllable); constituents H2O2, H2SO4, CuSO4, Mo ion (rate exaltant), aryl-sulfonic stabilizers, thiosulfates, H3PO4; peroxide decomposition while idle has caused equipment meltdowns → thermal management when idle; CuSO4·5H2O recovered by cooling to 50–70 °F; chloride contamination slows the rate | crystallizer 50–70 °F | — | peroxide etch | review | §37.4.3 | high |
| COOMBS-2430 | fab | Persulfates (now mainly microetch) accept all common resists; ammonium persulfate made at 20 %, pH falls 4 → 2 and cupric ammonium sulfate precipitates; capacity ≈ 7 oz/gal Cu at 100–130 °F (hold 130 °F above 5 oz/gal to avoid crystallization); rate 0.00027 in/min at 7 oz/gal and 118 °F; sodium persulfate batch 0.0018 → 0.0006 in/min over 0–7 oz/gal (age 16–72 h); decomposes rapidly near 150 °F — use soon after mixing; never mix with reducers/oxidizable organics | Cu ≤ 7 oz/gal; T < 150 °F | T, Cu | persulfate etch | measure | §37.4.4 | high |
| COOMBS-2431 | fab | Ferric chloride: limited PCB use (disposal cost, less support); compatible with screen ink, photoresist, gold — not tin or tin-lead; 28–42 wt % FeCl3 with HCl up to 5 % (customary 1.5–2.0 %) to prevent ferric hydroxide; alloy etching at 36 °Bé ≈ 4.0 lb/gal | — | resist | ferric etch | review | §37.4.5 | high |
| COOMBS-2432 | fab | Chromic–sulfuric etchant is eliminated (Cr6+): low Cu limit 4–6 oz/gal (discard > 5.5 oz/gal), 30 °Bé, pH ≈ 0.1, 80–90 °F, attacks PVC/PP, stains phenolic substrates, severe oxidizer hazard | — | — | legacy | review | §37.4.6 | high |
| COOMBS-2433 | fab | Nitric-acid etch: strongly exothermic (runaway), fumes, attacks resists/substrates; fast, high Cu capacity, cheap; 30 % copper nitrate + polymers + surfactants gave straight sidewalls with dry film but needs a specific foil grain structure hard to reproduce | — | — | experimental | review | §37.4.7 | high |
| COOMBS-2434 | materials | Laminate choices for etch precision: fine glass weave (flat foil surface); thin clad ≤ ¼ oz (9 µm) → minimal lateral etch (but pinholes/fragility) or etch ½ oz (18 µm) foil down to 3–9 µm (cupric or sodium persulfate, uniform start foil); reverse foil (drum side to dielectric, tooth up) stops etch at a flat interface; semi-additive base Cu 0.000050–0.000200 in shows no overhang/slivers | Cu ≤ 9 µm for fine lines | foil | fine-line etch | review | §37.5 | high |
| COOMBS-2435 | fab | Non-copper etching: Al (FeCl3 12–18 °Bé, NaOH 5–10 %, inhibited HCl, H3PO4 mixes, HCl+HF; 10 % HNO3 or chromic residue dip; DI spray rinse); Ni alloys (FeCl3 42 °Bé ≈ 100 °F; HNO3:HCl:H2O 1:1:3 or 1:4:1); stainless 300–400 (FeCl3 38–42 °Bé ± 3 % HCl; HCl:HNO3:H2O 1:1:1–3 ≈ 0.003 in/min at 175 °F); silver (HNO3:H2SO4 1:19; chromic/sulfuric then 25 % NH4OH; 55 wt % ferric nitrate for thin films; electrolytic 15 % HNO3 at 2 V) | see T-37.d | metal | special metals | review | §37.6 | high |
| COOMBS-2436 | fab | Phototool accuracy ≥ 10× better than the final feature tolerance (e.g., 0.0001 in line tolerance → 0.00001 in artwork); overlap plotted pulses/spots to minimize edge waviness | tol_art ≤ tol_product / 10 | tolerances | artwork | calc | §37.7.1.1 | high |
| COOMBS-2437 | test | Gauge image/etch capability periodically with standard test vehicles (Conductor Analysis Technologies protocol, IPC-9251): shorts/opens relate to resist integrity, repeating width patterns are image-related; map line geometry by panel position and orientation, and across time-lagged panel sequences (etch-control drift, plugged nozzles) | — | test coupons | etch SPC | measure | §37.7.1.2, §37.7.4.1, §37.7.4.6 | high |
| COOMBS-2438 | dfm | Etching is diffusion-limited: narrow, deep channels slow the etchant, so interior lines of closely spaced parallel groups and the inside corner of 90° bends etch slower than isolated/outer features | — | pattern | fine-line layout | review | §37.7.2 | high |
| COOMBS-2439 | fab | Etched-trace metrics: R resist width, B trace base, T trace top, t foil thickness; undercut U = average resist overhang after top reduction, etch factor F = sidewall taper per unit thickness (Eqs. 37.14–37.15 not in text; conventional U = (R − T)/2, F = 2t/(B − T) — assumed); extent of etch R/B (1.0 ideal, < 1 under-etched, > 1 over-etched); minimize U, maximize F; compare processes only at equal R/B with same foil, resist, artwork, panel size | R/B = 1 target | cross-section R, B, T, t | etch characterization | measure | §37.7.3.1–37.7.3.2, Fig. 37.4 | medium (formulas) / high (definitions) |
| COOMBS-2440 | fab | Etch sensitivity example (cupric, 3.0 mil L/S, 1.0 mil resist, 1 oz = 1.4 mil Cu): 140 s to R/B = 1 but only 25 s (18 %) more gives R/B = 1.25 (25 % overetch) → a 2× faster etchant with the same sensitivity is hard to dial in via conveyor speed; relative time = t / t(R/B = 1) | ΔR/B = 0.25 per +18 % time | etch time | etch control | calc | §37.7.3.3, Table 37.2 (not in text) | high |
| COOMBS-2441 | dfm | Widening artwork then over-etching raises F but also U; at tight spaces there is no room (etchant stagnates) → keep resist width near the final spec with precise etch control, or finish with a slow fine-tune etch to stop exactly | — | spaces | fine-line etch | review | §37.7.3.4 | high |
| COOMBS-2442 | dfm | Fine-line rule of thumb: minimum etched gap (and trace) ≈ resist thickness + foil thickness (1.2 mil dry film + 1 oz 1.4 mil → 2.6 mil; with R/B = 1 undercut a 2.6 mil line keeps only 1.1 mil top after 1.5 mil top reduction, as printed); 0.4 mil coated resist + ¼ oz (0.35 mil) → ≈ 0.75 mil (19 µm); demonstrated 30 µm L/S from 3–5 µm foil + 14 µm plating (17–19 µm traces) and 50 µm (2 mil) L/S in 1 oz (37 µm) Cu with 1.4 mil resist using fiber-assisted microchannel flow | S_min ≈ t_resist + t_Cu | t_resist, t_Cu | fine-line etch | calc | §37.7.4.2–37.7.4.4 | high (as printed) |
| COOMBS-2443 | dfm | "Fine line" is statistical: the linewidth where capability Cp = (USL − LSL)/(6σ) of the linewidth distribution drops below the production norm; allowed variation (usually % of line width) is set by customer and shop; measure with IPC-9251 vehicle or CAT program | Cp = (USL − LSL)/6σ | linewidth data | process capability | calc | §37.7.4.1 | high |
| COOMBS-2444 | fab | Etcher build and controls: materials rated for ≥ 130 °F (PVC, PP, CPVC, PVDF, Ti, Hastelloy C, Viton, Kel-F, EPDM, composites); key controls temperature (exothermic → cooling coils), pressure, conveyor speed, interlocks, plus conductivity/pH/density/ORP; separate top/bottom (ideally four-quadrant) spray controls; PVDF nozzles (fan = higher impact, cone = lower); a few clogged nozzles make arrays non-uniform → self-clearing nozzles or pump-to-spray filtration; validate spray systems with controlled trials/gauges | — | machine | etch equipment | inspect | §37.8.1 | high |
| COOMBS-2445 | fab | Horizontal conveyor etchers: balance top-puddle vs bottom etch with spray pressure; constant-speed rollers with flat compliant contact; wheel spacing trades bottom-spray shadowing vs thin-panel sag; thin cores 0.0015–0.003 in need guides/clips (a jam piles up panels); flex needs leading-edge carriers or roll-to-roll with synchronized speeds; vertical conveyors suit developing better than etching (down-flow gradient) | — | panel thickness | etch equipment | review | §37.8.2 | high |

## 2. Formulas & tables (numbers)

### T-20.25 Stripline loss examples (Fig. 20.25, HyperLynx simulations; W = 4.5 mil differential stripline)
| case | length (in) | Er | loss tangent | total loss @4 GHz (dB) | resistive (dB) | dielectric (dB) | crossover freq (GHz) | material |
|---|---|---|---|---|---|---|---|---|
| low-loss | 12 | 3.75 | 0.009 | 5.0 | 2.9 | 2.1 | 7.86 | Nan Ya NPG-170D (halogen-free) |
| standard | 17 | 3.9 | 0.02 | 10.0 | 4.0 | 6.0 | 1.78 | Nan Ya NP-175F FR-4 |
Source: §20.4.4.

### T-20.loss Channel loss budget anchors (§20.4.2–20.4.5)
| element | loss |
|---|---|
| End-to-end SERDES budget (typical) | 10–15 dB (lower with RX equalization); 12–18 dB buildable with TX/RX equalization |
| BGA package, each end | ≤ 0.5 dB (f < 2 GHz); 0.8 dB at 3.0 GHz |
| Connector (Zdiff 85–100 Ω) | well under 3 dB at target f |
| Via, poorly designed | 0.5–1.0 dB each |
| Via, optimized (blind/buried, backdrilled, small pads, large antipads) | < 0.25 dB each |

### T-20.pdn PDN frequency ranges (§20.5.3–20.5.5)
| element | value range | effective frequency |
|---|---|---|
| Bulk bypass capacitor | 1–1000 µF | DC to ~10 MHz |
| Decoupling capacitor | (per SRF) | up to ~200 MHz (absolute upper limit ~250 MHz) |
| Power/return plane pair | see capacitance density | ~150 MHz to GHz |
| On-die capacitance | — | > 200 MHz |
| Example SRFs | 100 nF → 16 MHz; 1 nF → 170 MHz; combined antiresonance 120 MHz | — |

### T-20.cap Plane-pair capacitance density (§20.5.5, Table 20.2 contents not in text)
| dielectric | thickness | Dk | capacitance density |
|---|---|---|---|
| Standard FR-4 (thinnest) | 2 mil (50 µm) | ≈ 4.0 | 49–68 pF/cm² (0.31–0.43 nF/in²) |
| Ultra-thin filled (e.g., barium titanate) | 8–14 µm (0.31–0.55 mil), < 1 mil | "double digits" | 0.3–3.6 nF/cm² (2–23 nF/in²) |

### T-20.XL Reactance example (§20.6.3, Eq. 20.6): R = 10 mΩ, L = 100 nH
| f | X_L = 2πfL |
|---|---|
| 1 MHz | 630 mΩ |
| 100 MHz | 63 Ω |
| 1 GHz | 630 Ω (> 377 Ω free space) |

### T-20.safety Safety thresholds (§20.6.11)
| item | value |
|---|---|
| Hazardous voltage threshold (protective earth mandatory) | ≥ 42.2 VAC or ≥ 60 VDC |
| Mains | 115 or 230 VAC |

### T-20.mech Mechanical support (§20.7.3, §20.8.1)
| item | value |
|---|---|
| Edge support | within 25 mm of edge, ≥ 3 sides |
| Board 0.7–1.6 mm thick | support interval ≤ 100 mm |
| Board > 2.3 mm thick | "1.3-mm intervals" (sic; text garbled) |
| Steinberg deflection rating | 10e6 reversals sinusoidal; 20e6 random |

### T-21 Chapter 21 numeric anchors
| item | value | source |
|---|---|---|
| Default board thickness | 0.062 in | §21.6 |
| BGA placement / routing grid | pitch/2 ; pitch/4 (0.8 mm → 0.4 / 0.2 mm) | §21.7 |
| Power–ground plane pair spacing | 0.003–0.010 in | §21.9 |
| Routing Z0 target | 50–60 Ω, uniform across layers | §21.10 |
| Trace width vs pad | ≤ 60 % of pad | §21.10 |
| Cap/IC via-to-plane trigger | > 0.100 in from plane connection | §21.10 |
| Serpentine loop gap | 3–4 × trace width | §21.10 |
| Drill tolerance (typical) | ±0.003 in | §21.11 |
| Database precision | metric 4 decimals; imperial 0.001 in grid, 2 decimals | §21.6 |

### T-22.1 IPC-2152 baseline test conditions and data scope (§22.1, §22.3)
| item | value |
|---|---|
| Baseline material / thickness | polyimide, 1.78 mm (0.07 in), no internal planes |
| Test method | IPC-TM-650 2.5.4.1a "Conductor Temperature Rise due to Current Changes in Conductors" |
| Baseline charts published | 3 oz ext, 2 oz ext, 3 oz int, 2 oz int, 1 oz int, ½ oz int (0.07 in polyimide, air) |
| Data collected | ½, 1, 2, 3 oz Cu; FR-4 and polyimide; thickness 0.965 mm (0.038 in), 1.498 mm (0.059 in), 1.78 mm (0.07 in); still air and vacuum; with modelled planes |
| Extrapolation advantage | cross-section > 700 sq mil, higher currents |
| Old NBS 1955 data | external only; phenolic & epoxy; cores 0.03125, 0.0625, 0.125 in; ½, 1, 2, 3 oz; with/without backside plane |
| Old internal chart | = external chart current × ½ (not measured) |

### T-22.2 Board-thickness effect (§22.3.4; 1 oz internal, 0.0088-in-wide trace, 1 A, air)
| board thickness | ΔT (°C) |
|---|---|
| 0.070 in (1.78 mm, baseline) | 10 |
| 0.059 in (1.498 mm) | 12.1 |
| 0.038 in (0.965 mm) | 13.3 |

### T-22.3 Dielectric thermal conductivity (Table 22.2 values not in text; prose anchors §22.2.1)
| material | k (W/m·K) |
|---|---|
| epoxy / phenolic core (approx.) | 0.354 |
| air | 0.026 |

### T-23.1 Thermal conductivities cited in prose (Table 23.1 not in text; §23.3–23.6; valid ~23 °C)
| material | k |
|---|---|
| Copper (pure) | 386 W/m·°C (§23.3.4); 380 W/m·°C (§23.6.3); 0.389 W/mm·°C (via plating, §23.3.3) |
| FR-4 | 0.8 W/m·°C (§23.6.3); Cu ≈ 1000× FR-4 (§23.3.2) |
| PCB with one 0.036 mm plane, 1.57 mm thick | 8.9 W/m·°C effective in-plane (§23.3.4) |
| Smeared layer 95 % Cu | 360 W/m·°C (incorrect averaging method, §23.6.3) |

### T-23.via Thermal via resistance examples (§23.3.3, Eqs. 23.3–23.4; k = 0.389 W/mm·°C, L = 0.38 mm, d = 0.3 mm)
| plating t (mm) | R_via (°C/W) | 4×4 array (°C/W) |
|---|---|---|
| 0.025 | 45 | 2.8 |
| 0.015 | 73 | (≈ 4.6 by R/16) |
Reconstruction check: A_Cu = π·(0.15² − 0.125²) = 0.0216 mm² → R = 0.38/(0.389·0.0216) = 45.2 °C/W; t = 0.015 → 72.7 °C/W.

### T-23.2 Component spacing case (Table 23.2 prose anchors, §23.3.4)
| condition | max device T (°C) |
|---|---|
| four small devices spread on 100×100 mm PCB, two buried planes, 25 °C ambient | 81.6 |
| same devices clustered | 98.4 (+30 % of rise above ambient) |

### T-23.9 Natural convection best case (Fig. 23.9; horizontal, 25 °C, uniform power, convection + radiation)
| PCB size | 50 W dissipation |
|---|---|
| 10×10 cm | not realistically possible |
| 15×15 cm | ΔT = 80 °C |
| 20×20 cm | ΔT = 50 °C |

### T-23.misc Other Ch. 23 anchors
| item | value | source |
|---|---|---|
| PCB share of component heat dissipation | 60–95 % | §23.2 |
| Trace-length diminishing return (SOIC-8, 1 W) | ~15 mm | §23.3.1 |
| Device ΔT sensitivity to trace length | ~40 % | §23.3.1 |
| 1 mm FR-4 plane gap | ≈ 1000 mm Cu equivalent | §23.3.2 |
| 0.25 mm isolation slot | 29 °C across slot; +33 °C component | §23.3.2 |
| 0.5 oz Cu (as stated) | 23.8 µm | §23.3.2 |
| Plane thickness saturation | > 2.8 oz total | §23.3.2 |
| Thermal via pitch / drill / plating | 1.0–1.2 mm / 0.3 mm / ≥ 0.025 mm | §23.3.3 |
| Downstream air heating | 10–30 °C | §23.3.4 |
| Emissivity solder mask / bare Cu | 0.85–0.95 / 0.1–0.3 | §23.3.5 |
| Chassis-screw example gain | 10 % | §23.4.1 |
| RF shield perforation | < λ/10 | §23.4.4 |
| Heat sink threshold | ≥ 2.5 W | §23.5 |
| High-power heat sink | 50–300 W; clamp 20–200 lb | §23.5 |
| Model accuracy: CFD / h-codes / 2-resistor / compact | ±5 % / ±10 % / ±20 % / ±5 % | §23.6 |
| Property validity window | −25 °C to 85 °C (re-source outside) | §23.3.1 |

### T-24 Embedded component numbers (Ch. 24)
| item | value | source |
|---|---|---|
| ρ_Cu | 7.09e−7 Ω·in²/in | §24.4.1.1 |
| Corner square factor (serpentine) | 0.56 R | §24.4.1.3 |
| Capacitance constant K | 8.854e−14 F/cm | §24.4.2.1 |
| Dk: epoxy/E-glass; filled polymer; ceramic | ≈ 4; 10–20; 100–2000 | §24.4.2.2 |
| Dielectric thickness steps | 100 µm (4 mil) → 50 µm (2×) → 8 µm (6–20×) | §24.4.2.2 |
| PTF / CTF capacitance density | 20 pF/mm² / ≈ 24 nF/mm² | §24.5.3 |
| Planar capacitor dielectric | ~25 µm | §24.5.3.1 |
| Max commercially available density | not > 100 nF/cm² | §24.3.2 |
| Spiral inductor: 1 layer / multilayer / with ferrite | ~10 nH / 30 nH / ~100 nH | §24.5.4 |
| PTF cure / ceramic fire | 150–200 °C / 900 °C (N2) | §24.5.2.2 |
| Paste value spacing | 10–15× (e.g., 100, 1000, 50,000 Ω/sq) | §24.6.1 |
| Discrete R thickness 01005 / 0201 | 0.13 / 0.23 mm; ±5 % thick film, ±0.5 % thin film | §24.6.2.1 |
| Discrete C 01005 / 0201 | C0G 5.0–100 pF; X7R 68–470 pF / 68–10,000 pF; 0.20 / 0.30 mm thick (0.15 mm family) | §24.6.2.2 |
| Si MIS capacitors | 0.13 mm thick; 0.8–1000 pF; 0.23×0.30 to 1.5×1.70 mm | §24.6.2.2 |
| Printed logic feature size | as small as 10 µm | §24.5.5.3 |

### T-25 HDI numbers (Ch. 25, part)
| item | value | source |
|---|---|---|
| HDI threshold | > 110–130 connections/in² (20/cm²), both sides | §25.1 |
| IPC microvia | ≤ 150 µm; L1–L3 SBV ≈ 250 µm | §25.2 |
| Cost parity | 4-layer HDI ≈ 8-layer TH | §25.2.4 |
| Density gain | 4–8× vs all-drilled TH | §25.3 |
| Fabricator coverage Cat. A / B / C | 100 % / 75 % / 20 % | §25.3.2 |
| Cu peel on HDI dielectric | ≥ 6 lb/in (1.08 kg/cm) per 1 oz (35.6 µm) | §25.5.1 |
| Laser-drillable FR-4 | 106/1080/1086 glass, 1–2 ply, RC ≈ 70 % | §25.5.1.1 |
| Unclad/thin-Cu trigger | L/S ≤ 75 µm or via < 75 µm | §25.5.1.2 |
| Japan unclad starts | 22 % | §25.5.1.2 |
| 2015 mobile forecast | L/S 5–15 µm; via 10 µm | §25.5.1.3 |
### T-25.mat HDI dielectric / via-fill numbers (§25.5–25.6)
| item | value | source |
|---|---|---|
| RCC finished dielectric | 1.0–3.0 mil (25–76 µm) | §25.5.2.1.1 |
| RCC foils | ½ oz (18 µm), 3/8 oz (13.34 µm) | §25.5.2.1.1 |
| PID plated-Cu adhesion | ≥ 1.1 kg/cm @ 25 µm Cu | §25.5.2.1.3 |
| Aramid nonwoven CTE | 10–16 ppm/°C; CSP joint life ×3; > 1000 cycles −40/+125 °C no cracks | §25.5.2.4 |
| Lamination-fill limit | hole ≤ 0.3 mm and core ≤ 0.6 mm (RCC resin 80 µm) | §25.5.3.2.1 |
| Planarization abrasive | #600–#800 belt sander or ceramic brush | §25.5.3.2.1 |
| PID plug secondary coat | cores ≤ 0.030 in (0.76 mm) | §25.5.3.2.3 |
| Conductive paste fill | AR 1:1–6:1 (vacuum); via 6–25 mil (152–635 µm); core 6–85 mil (152–2159 µm) | §25.5.3.2.4 |
| Mechanical via floor | 0.20 mm (0.008 in) | §25.6 |
| Photovia cure | 160 °C, ~1 h | §25.6.1 |
| Peel targets (as printed) | package ≈ 600 g/cm²; phone ≥ 1.0 kg/m² | §25.6.1 |
| Photovia panel limit | ≈ 400×400 mm | §25.6.1 |

### T-25.laser Laser via formation parameters (§25.6.3)
| parameter | value |
|---|---|
| Mass via processes (chemical/plasma/photo) | 40,000–50,000 vias/s |
| High-fluence spot (cuts Cu, glass) | ≈ 20 µm |
| Low-fluence spot (organics only) | 100–350 µm (4–14 mil) |
| UV-YAG through glass-reinforced dielectric | 3–50 holes/s |
| UV-YAG through RCC | 100–300 holes/s |
| UV-YAG trepanning threshold | d ≥ 125 µm |
| UV-YAG minimum hole | 20–30 µm |
| CO2 minimum hole (mass production) | 50 µm |
| CO2 single head, bare resin | 20,000–25,000 holes/min |
| CO2 dual head | +70 % |
| CO2 direct drilling through thin darkened Cu | −30–40 % speed |
| CO2 Cu penetration limit | < 5 µm, darkened |
| Half-etch surface Cu | 6–7 µm (CO2), 6–9 µm (YAG users) |
| Filled resin coating scheme | 40 µm unfilled + 20 µm filled = 60 µm |
| Pulses per hole | 2–3 (third in separate pass) |
| RCC window method capture-pad floor | 250 µm |
| Ultra-thin Cu RCC | 70 µm carrier / 10–20 µm release / 3–5 µm foil |
| Glass-fiber desmear | Al2O3 ~20 µm blast or excimer; ~30 s/side |
| Cell-phone microvia density | 650,000–700,000 /m² |

### T-26 Advanced HDI numbers (Ch. 26)
| item | value | source |
|---|---|---|
| Sony DCR-PC7 SLC | 2+4+2, 0.5 mm CSP, > 612 pins/in² | §26.3.1.2 |
| PID economic threshold | > 50,000 vias per 18×24 in panel | §26.3.1.2 |
| Ormet TLPS cure | 215 °C / 2 min vapor; 175 °C / 40 min post-cure; ≤ 4 layer pairs | §26.3.2.8 |
| ALIVH layer count | 6–10 | §26.3.2.9 |
| DYCOstrate through hole | 0.075 mm | §26.3.4.1 |
| PERL layer range | 4–12 | §26.3.4.3 |
| Optical vs electrical size | cables 10×, bussing 20×, connectors 7× (20–40 % faster), waveguide vs diff stripline 8× | §26.4.1 |
| Polymer waveguide qualification | Telcordia 1209/1221; < 600 h 85/85; solder > 230 °C; degradation > 350 °C | §26.4.1.3 |
| POF | unstable < 80 °C; 20 dB/km (glass < 0.1 dB/km) | §26.4.1.3 |

### T-28.a Drilling materials (§28.2)
| item | value |
|---|---|
| Board thickness range / common | 0.010–0.300 in / ≈ 0.0625 in |
| Tg standard / mid / high FR-4 | ≈ 130 / 150 / 170 °C |
| 1 oz Cu thickness | ≈ 1.4 mil (0.0014 in) |
| Carbide composition | WC > 90 wt %, Co 6–8 wt %, other carbides 1–2 wt % |
| Carbide grain classes (as printed) | ultrafine > 0.5 µm; extra-fine > 0.05–0.09 µm; fine 1–1.5 µm |
| Drill cassette capacity | ≥ 120 bits |
| Partial margin relief | ≈ 1/5 flute length; +≥ 25 % drilling temperature |
| Flute reserve | ≥ 0.050 in above stack |
| Repoint cost / count / stock removal | ≈ 15 % of new / 1–10 (small: 1–3) / 0.002–0.005 in per regrind |
| Solid Al entry breakage risk | ≥ 0.008 in thick with small drills |
### T-28.b Drilling machine & method parameters (§28.3–28.8)
| parameter | value |
|---|---|
| Collet cleaning (ball-bearing spindles) | ≥ once per shift |
| Static TIR test pin / indicator distance | 1/8 in (0.1250 in) pin; ≈ 0.800 in from collet nose |
| Max TIR (Ch. 28) | 0.0005 in for d > 0.020 in; 0.0002 in for d ≤ 0.020 in; check weekly |
| Max TIR (Ch. 29, as printed) | 0.002 in (0.005 mm) |
| Spindle rpm verification | every 6 months; tachometer ≥ 150,000 rpm (~$300) |
| Pressure-foot lead distance | ≈ 0.050 in; inserts checked daily |
| Lead-screw service | every 6 months |
| Retract rate | default max 500–1000 ipm (new machines to 1400 ipm = 35,560 mm/min); ≤ 500 ipm for 0.0135–0.0250 in drills |
| Backup penetration | point length + ≈ 0.010 in; rule: min(d, 0.040 in) |
| Stack clearance | ≥ 0.125 in (0.075 in foot-to-stack + 0.050 in lead) |
| Max total drilled depth | ≈ 17 × d |
| Parameter example | v = 150 m/min target; 160,000 rpm spindle holds to d = 0.3 mm; min 20,000 rpm at 2.4 mm; point angle 130° → 165° above 3.175 mm |
| Drill sizes cited | #72 = 0.0250 in; #80 = 0.0135 in |
| Backup reuse | 2× (halve cost) |
| Cost reporting | per 1000 holes |

### T-29 High-density & laser drilling numbers (Ch. 29)
| item | value | source |
|---|---|---|
| HDI hole definition | ≤ 0.006 in | §29.1 |
| Smallest mechanical hole | 0.002 in (0.05 mm) | §29.2 |
| Mechanical preferred | via depth > 0.016 in [text adds "(6.3 mm)" sic]; hole > 0.012 in | §29.3 |
| Laser rate vs mechanical | > 500 (to 1000) holes/s vs ≈ 200 holes/min | §29.3.1 |
| CO2 wavelength | 9.4–10.6 µm | §29.3.2, §29.8.4 |
| Solid-state fundamental | 1030–1070 nm; Nd:YAG 1064 nm → 532 nm (2nd), 355 nm (3rd) | §29.3.2, §29.8.3 |
| Laser focus (as printed) | CO2 ~200 "mm"; UV ~20 "mm" | §29.3.4–29.3.5 |
| UV pulse lengths | YAG ≈ 120 ns; YVO4 ≈ 20 ns @ ≈ 100 kHz; YLF ≈ 50 ns (5× absorption) | §29.3.7 |
| Drill room | 72 ± 2 °F (22 ± 1.1 °C); 45–60 % RH | §29.4.2 |
| Spindle range | 15,000–300,000 rpm; ≈ 1 hp | §29.4.6 |
| Chip load threshold | > 0.001 in/rev needs adequate cutting speed | §29.4.7 |
| Micro-drill cutting speed | 300 sfm achievable with 180,000 rpm | §29.4.7 |
| Mapping increment (controlled penetration) | 2 in | §29.5.3 |
| Peck example | 0.209 in / 0.025 in: AR 8.36 → 2.08 (4 pecks); Fig. 29.5: 15.3 → 3.8 | §29.6.2 |
| Peck count | 3–5 increments | §29.6.2 |
| Slot method threshold | < 2–3 × d overlapping; larger: bisection | §29.6.3 |
| Predrill | d ≥ 0.157 in (4.0 mm); pilot 15–35 % | §29.6.4 |

### T-29.laser Laser source configurations (§29.8)
| laser | average power | max rep rate | pulse duration |
|---|---|---|---|
| Pulsed UV (Nd:YAG harmonics) | 6–28 W | 40–300 kHz | 20–120 ns |
| Pulsed CO2 / IR | 6–250 W | 2–300 kHz | 1–100 "ms" (as printed) |
| Ultrashort pulse | 6–50 W | 400–1000 kHz | 0.3–20 ps |

### T-30.a Imaging numbers (§30.1–30.6.4)
| item | value | source |
|---|---|---|
| Screen print vs photo threshold | 200 µm | §30.1 |
| Inkjet electroless Cu | 0.05–5 µm | §30.1 |
| Min line width | resist thickness + 10–25 µm | §30.2.2 |
| Dry-film thickness | 25–50 µm typical | §30.3 |
| Liquid resist thickness | 6–15 µm; resolves < 25 µm; high yield ≤ 50 µm | §30.4 |
| Exposure wavelength | 365 nm (Hg); LDI 355 / 405 nm; legacy 450 nm | §30.3.2, §30.6.4.2 |
| Dry-film dose | 25–90 mJ/cm² (330–405 nm); LDI resists 10 mJ/cm²; IC positive resists 200–500 mJ/cm² | §30.3.2 |
| Develop / strip | ≤ 1 % Na/K carbonate, pH 10.3 / ≥ 1 M NaOH or KOH, pH 13 | §30.3.2 |
| Process pH extremes | acid Cu plating < 1; ammoniacal etch 8–9 | §30.3.2 |
| Mechanical clean min core | > 0.020 in (text "0.52 mm") | §30.6.2.1 |
| Laminator roll durometer | 40–50 Shore A (55–65 extra conformance) | §30.6.3.1 |
| Auto-laminator trim | 1–4 mm inside board edge | §30.6.3.1 |
| Roller coater throughput | ≤ 240 panels/h | §30.6.3.4 |
| Electrophoretic deposition | 20 s–3 min | §30.6.3.7 |
| Phototool life | glass 100–400 contacts (with repair); film 20–50 | §30.6.4.1.1 |
| Functional cure criterion | thickness loss < 10 % | §30.6.4.1.3 |
| Lamp life | ≈ 1000 h | §30.6.4.1.4 |
| Proximity gap / resolution | 125–500 µm / ≈ 75 µm | §30.6.4.1.6 |
| Stitcher field | ≈ 6×6 in; 12 exposures per 18×24 in side | §30.6.4.1.7 |
| Magnified projection | 50 µm line / 63 µm space (365 nm); 125 µm (436 nm LCD) | §30.6.4.1.7 |
| Ar+ LDI | 3000–5000 h life; 60–80 kW | §30.6.4.2 |
| DMD mirror size | ≈ 1.5 µm (> 8000 dpi polygon) | §30.6.4.2 |
| LDI throughput | 60–180 panels/h (18×24 in, 50 µm) | §30.6.4.2 |
### T-30.b DDI, inkjet, AOI and DFM numbers (§30.6.4.3–30.9)
| item | value | source |
|---|---|---|
| DDI min feature | 15 µm L&S (fine-pitch configuration to 8 µm L/S) | §30.6.4.3 |
| DDI edge roughness / position repeatability | ±1 µm / ±1.0 µm | §30.6.4.3 |
| DDI side-to-side registration | ±10 µm (3σ) | §30.6.4.3 |
| DDI exposure time | 20 s per 530×650 mm | §30.6.4.3 |
| DDI wavelength / source life | 350–425 nm (i- to h-line) / > 3 years | §30.6.4.3 |
| DDI throughput config | up to 5000 panels/day; "20 mm [sic] L/S at 2 panels/min" | §30.6.4.3 |
| Develop dwell | ≈ 2 × time to clear (50 % breakpoint) | §30.6.5 |
| Pattern-plate resist channel limit | ≈ 38 µm channel for 25 µm plating | §30.7.1 |
| Inkjet printer | 500×500 mm; ±5 µm accuracy; ±1 µm repeatability; 1.5 mm DOF; 128 jets, 1 or 10 pL | §30.8 |
| AOI rule example | no line < 150 µm | §30.9 |

### T-31.lam Lamination process numbers (§31.3–31.5)
| item | value |
|---|---|
| Mass-lamination sheet sizes | 24×48, 36×48, 48×52 in; 1.5×2 m |
| Mass-lam cores | ≥ 0.004 in (text "(1.0 mm)" sic); some 0.002 in (0.05 mm) |
| Standard cut panels | 18×24, 20×27, 21×27 in (also 14×18, 12×24 from 36×48 / 42×54 sheets); 4–8 sizes per shop |
| Tooling holes / slots | 0.125–0.250 in dia / 0.187×0.250 in |
| Punch spring-back allowance | laminates > 0.032 in |
| Innerlayer pre-bake | 105–110 °C, ≥ 1 h |
| Caul plate | 3/8 in (9.525 mm) 4130 steel |
| Separator plates | 0.015–0.062 in, 400-series stainless (or disposable Al) |
| Press openings / capacity | 4–8 / up to 96 panels (12 × 8) |
| Vacuum pre-cycle | 15–60 min |
| Hot-press heat rate / kiss | ≈ 20 °C/min / few minutes |
| Cold-press heat rate / kiss | 5 °C/min / ≈ 15 min |
| LFAC moisture drive-off | 0 psi, ≤ 15 °C/min to ≈ 90 °C, hold 30–40 min |
| Flow pressure | ≈ 200 psi (slow ramp) to 600 psi (fast cure + fast ramp) |
| Dicy FR-4 critical range / recipe | 70–130 °C / 4–8 °C/min at 200–300 psi |
| HF & LFAC critical range / recipe | 80–140 °C / 2–4 °C/min at 225–360 psi |
| Cure (epoxy / LFAC) | ≈ 180 °C × 60 min / up to 200 °C internal × 120 min |
| B-stage melt | ≈ 90 °C |
| Under-cure criterion | ΔTg > 5 °C between two TMA runs |
| Post-lam bake (usually unnecessary) | 150 °C, up to 4 h |
| Two-ply fill triggers | large voltage bias; 70 µm Cu adjacent |

### T-31.foil Copper foil elongation (§31.3.2.2, IPC-4562)
| foil | elongation |
|---|---|
| Standard ED | fails ≈ 3 % |
| HTE, IPC-4562/3 | 5–8 % |
| HD Type E, IPC-4562/2 | ≥ 10 % minimum |
| RTF | IPC-4562 code R (reverse-treated, both sides stain-proofed) |
| HDI microfoil | 9–12 µm |

### T-31.fill Via fill numbers (§31.2.4)
| item | value |
|---|---|
| Wrap Cu risk threshold | < 5 µm (0.0002 in) |
| IPC-6012 Class 3 min wrap (as printed) | "127 µm (0.0005 in)" → 0.0005 in = 12.7 µm |
| MRB-accepted wrap (some Class 2) | 0.0002 in |
| Fill cost | $25–$50 per panel; Ag conductive ≈ 2× nonconductive |
| IPC-4761 fill types | Type V and VII |

### T-32 Process water (§32.3)
| parameter | value |
|---|---|
| RO operating pressure | 1.4–4.2 MPa (200–600 lb/in²) |
| RO removal | 90–98 % dissolved minerals; 100 % organics MW > 200 |
| DI water pH | 6.5–8.0 |
| Total organic carbon | 2.0 ppm |
| Turbidity | 1.0 NTU |
| Chloride | 2.0 ppm |
| Ionic cleanliness test | MIL-P-28809 |
| Electroless Cu thickness | 20–100 µin |
| Typical fine features (Ch. 32) | lines 3–6 mil; holes 12 mil |

### T-33.a Electroplating basics (§33.2–33.3.2)
| item | value |
|---|---|
| Cu plating anchor | 1.0 mil in 60 min at 17.8 ASF ("1.88 ASD" printed; 1.92 ASD derived) |
| Throwing power vs AR | ≈ 100 % at 3:1; ≈ 33 % at 15:1 |
| Optimized bath example | > 85 % TP on 15:1 at 8 ASF DC |
| Plated Cu tensile / elongation | > 35,000 psi / > 15 % |
### T-33.b Acid copper plating cell & equipment (§33.3.3.2–33.3.3.5)
| parameter | value |
|---|---|
| Tank length | panel width + 12–16 in + 8–12 in weir well |
| Tank breadth (anode-cathode) | 18–30 in (6–12 in anode basket to panel) |
| Tank depth | panel depth + 8–10 in |
| Weir | short end; 8–12 in well; top 5–8 in below surface |
| Anode baskets per 18×24 in panel | panel plate 3–4 (2.5–3.5 in dia round); pattern plate 2–3 |
| Anode vs cathode length | anode 3–4 in shorter; tucked 3–4 in inside cathode window |
| Anode bag | loose, not napped, 2–3 in longer than basket |
| Panel racking depth | ≤ 1.0 in below solution surface |
| Cathode agitation | 1–3 in stroke, 10–20 strokes/min |
| Eductor nozzle top | ≈ 6 in below panel bottom |
| Filtration | 5–10 µm PP; 2–4 solution turnovers/h |
| Temperature (example) | 70–80 °F |
| DC ripple / control resolution | < 5 % / 1–2 % |
| PPR example | +20 ASF 10–20 ms / −60 ASF 0.5–1.0 ms |
| Horizontal module length | 60 m at 20 ASF, 1 m/min; 15 m at 80 ASF |
| Horizontal anode–cathode gap | 8–10 mm (0.3–0.4 in); surface variation < 10 % |
| High-AR pattern plating CD | 5–20 ASF |

### T-33.c Acid copper bath control & via fill (§33.3.3.6–33.3.3.9)
| item | value |
|---|---|
| Blind-via fill AR | 1:1 common; up to 1.2:1 |
| Via-fill electrolyte | Cu 50–60 g/L; H2SO4 30–60 g/L; strong leveler |
| Via-fill CD profiles | 12 ASF × 90 min; or 10 ASF × 30 → 15 ASF × 20 → 20 ASF × 20 min |
| TOC treat trigger / target | 4× make-up baseline (3× if degraded) / ≈ 70 % of high value |
| TOC example | 300 ppm base → operate 850–1200 ppm |
| Carbon-treat by usage | every 100–120 Ah/L (dry-film pattern plate) |
| Oxidative carbon treat | 0.5 vol % of 35 % H2O2 + ≈ 2 g/L carbon, 120–140 °F, ≈ 4 h |
| Predip | 5–10 % H2SO4, no rinse into bath |

### T-33.d Tin, nickel, gold plating (§33.4–33.6)
| item | value |
|---|---|
| Tin etch-resist thickness | ≈ 0.3 mil (7.5 µm) |
| Tin filtration | 3–10 µm PP |
| Tin max contaminants (ppm) | Cu 5–10; Cd 50; Zn 50; Ni 50; Fe 50–120; Cr 5; Cl− 75 |
| Tin dummy plate | 2–5 ASF |
| Tin dullness triggers | acid < 10 %; Sn > 3 oz/gal; T > 65 °F |
| Nickel minimum (MIL-STD-275) | 0.0002 in, low-stress |
| Nickel sulfamate temperature | 125 °F |
| Nickel rate | 0.5 mil / 25–30 min @ 25 ASF; 0.2–0.3 mil / 15 min @ 25 ASF |
| Nickel max contaminants (ppm) | Fe 250; Cu 10; Cr 20; Al 60; Pb 3; Zn 10; Sn 10; Ca 0 |
| Nickel dummy plate | 3–5 ASF |
| Nickel carbon treat | 140 °F; 3–5 lb/100 gal; 4 h stir; 1–2 h settle |
| Nickel stress | sulfamate < 10 kpsi; sulfate (tab) ≈ 20 kpsi, pH ≥ 1.5 |
| Nickel Hull cell / antipit | 2 A × 10 min / bubble 5 s in 3-in ring, < 5 s in 5-in ring |
| Hard gold, mil | MIL-G-45204 Type II Class 1: 50–100 µin |
| Hard gold, commercial | 25–50 µin |
| Gold bath pH | acid 3.5–5.0; neutral 6–8.5; pure-gold acid 3–6; sulfite 8.5–10 |
| Gold solution life | ≈ 10 gold turnovers |
| Sulfite gold hardness | 180 Knoop |
| Gold thickness metrology | beta backscatter / XRF, 1 µin on 5-mil pads |
| Gold lead impurity | < 0.1 % |

### T-34 Direct metallization (§34.1)
| item | value |
|---|---|
| Horizontal DMT cycle | 6–15 min per panel, 1 in spacing |
| EE-1 flash coverage | ≈ 5–6 min |
| DMS-E oxidative step | 80–90 °C |
| PTH metallization share of PCB cost | 2–3 % |
### T-35 Surface finish comparison (compiled from §35.3–35.9 prose; Table 35.1 itself is image-only)
| finish | thickness (spec / typical) | governing spec | shelf life | planar / fine pitch | solder joint IMC | wire bond | contact / press-fit | key issues | cost (per text) |
|---|---|---|---|---|---|---|---|---|---|
| HASL (SnPb or Pb-free SnCu, SAC, SnCuNi, SnCuNiGe) | 2–20 µm or more | — | excellent | no; < 0.5 mm pitch difficult/impossible | Cu/Sn (more reliable) | — | — | extra thermal cycle, Cu loss, IMC growth, warp, bridging, ionic residues, Pb/fire safety | inexpensive |
| ENIG | Ni 3–6 µm (118.1–236.2 µin); Au ≥ 0.05 µm (1.97 µin) at −4σ, typ 0.075–0.125 µm; Rev A draft Au 1.6–4.0 µin | IPC-4552 (2002), Rev A draft | > 12 months | yes | Ni/Sn | Al & Cu wedge (Au not reliable) | yes; press-fit | black pad, hard to rework, thick Ni hurts HF signals | more costly |
| ENEPIG | Ni 3–6 µm; Pd 0.05–0.15 µm (2–12 µin); Au ≥ 0.025 µm (1.2 µin) at −4σ (amendment max 2.8 µin); pad 1.5×1.5 mm | IPC-4556 (2013) + amendment | > 12 months | yes | Ni/Sn with Cu, Pd — most robust with SAC | Au, Al, Cu | yes; domes, LIF/ZIF, press-fit | complex, costly, hard to rework, Ni HF loss, Ni corrosion if Au too thick | more costly |
| OSP | high-temp types up to 1.0 µm | J-STD-003 category 3 (12 months) | 12 months (cat 3; some cat 1–2) | yes | Cu/Sn | no | no (nonconductive) | handling, exposed Cu, inspection, misprint cleaning, not for high-AR/fine pitch | cost effective |
| Immersion silver | 0.12–0.4 µm (5–16 µin) at ±4σ; typ 0.2–0.3 µm (8–12 µin); general 0.1–0.4 µm | IPC-4553A (2009) | 12 months with special packaging | yes | Cu/Sn | potential Al | yes; press-fit | tarnish, creep corrosion, mask attack, handling | — |
| Immersion tin | ≥ 1.0 µm (40 µin) at −4σ; typ 1.15–1.3 µm (46–52 µin); general 0.6–1.2 µm | IPC-4554 (2007, amended 2011) | limited by Cu-Sn IMC growth | yes | Cu/Sn | — | excellent compliant pin | whiskers, oxidation, IMC growth, thiourea (dedicated line), mask attack | — |
| Electrolytic Ni/Au | Ni several µm; Au 0.50–1.5 µm (hard ≈ 3 % alloy; soft 99.99 %) | — | — | — | not recommended for soldering (embrittlement) | Au (soft) | hard Au for insertions | needs bussing; selective plating | — |
| Electroless Pd | ≈ 0.1 µm (4.0 µin) | — | — | yes | — | — | yes | Pd price | — |
| EPIG | per supplier | none | — | yes (no Ni) | — | Au | yes | no IPC spec | — |
| EN + immersion Au + electroless Au | wire-bond thickness, uniform | — | — | yes | — | Au (soft) | some | cost, process control | — |
| Direct immersion Au on Cu | thin | — | solderable after 3+ yr ambient | yes | — | — | — | Cu–Au interdiffusion discoloration; single thermal excursion only | — |
| Reflowed SnPb | — | — | — | — | — | — | — | simple technology only | — |

### T-35.b Surface-finish process numbers (§35.1–35.8)
| item | value |
|---|---|
| Assembler shelf-life needs | incoming > 1 year; mid-assembly > 2 weeks |
| Pb-free peak vs eutectic | 260 °C vs 225 °C (+35 °C) |
| Electroless Pd phosphorus | 4–5 % P (amorphous) |
| ENEPIG Au for wide bond window | 0.1–0.2 µm (4–8 µin), reduction-assisted immersion Au |
| ImAg test-pad spacing | ≥ 80 mil |
| XRF measurement pad | 1.5×1.5 mm (2.25 mm², 0.060×0.060 in) |

### T-36.a Solder mask numbers (§36.1–36.5.1)
| item | value |
|---|---|
| Liquid share of mask applied | > 98 % |
| Mask web width | frequently 0.003 in; as narrow as 0.001 in; typical 2.5–3.0 mil; some 1.0–1.5 mil |
| Pb-free temperature increase | up to +30 °C (54 °F); typically +10–20 °C; SAC305 melts 34 °C above eutectic |
| NASA outgassing | TML ≤ 1.0 %; CVCM ≤ 0.10 % |
| Screen vs curtain/spray emissions | screen ≈ half |
### T-36.b Solder mask & legend processing (§36.5–36.8)
| item | value |
|---|---|
| Screen mesh examples (threads/in – thread µm) | 86-120, 83-100, 86-100, 92-100, 110-80 |
| Debubble before tack dry | ≤ 5–10 min |
| Exposure lamp | ≥ 7 kW (modern units) |
| Aqueous developer | Na2CO3 / K2CO3, pH 10.6–11.3 |
| Develop breakpoint | 10–15 % of chamber (photoresist ≈ 50 %) |
| Solvent developers | gamma-butyrolactone (GBL); butyl carbitol |
| UL flame strip (legend trigger) | ½ × 5 in |
| Military legend ink | CID A-A-56032D (epoxy) |
| Via protection guide | IPC-4761 (July 2006); protect both sides |

### T-37.a Etch resist / etchant compatibility (§37.2.5, §37.4.2)
| resist | thickness | alkaline ammonia | cupric chloride | ferric chloride | peroxide–sulfuric | persulfate |
|---|---|---|---|---|---|---|
| Organic (dry film, liquid, screen) | — | yes (negative more alkali-tolerant) | yes (preferred for fine features) | yes | yes | yes |
| Tin (SMOBC) | ≈ 0.0002 in | yes (favored) | no (attacks) | no (attacks) | special bright-tin formulations | persulfate–phosphoric (bright tin) |
| Solder 60Sn/40Pb | 0.0003–0.001 in (fusing); 0.0002 in (SMOBC) | yes | no | no | yes | — |
| Sn-Ni (65/35), Ni | — | yes | yes (Sn-Ni listed) | — | yes | yes |
| Gold over Ni or Sn-Ni | — | yes | yes | yes | yes | yes (slight dissolution possible) |
| Rhodium over Ni | thin, porous | lifts | — | — | — | — |
| Silver | — | yes (loss ≈ 0.0001 in "/mm" as printed); barred by MIL-STD-275 | — | — | — | — |

### T-37.b Etchant operating numbers (§37.4)
| parameter | alkaline ammonia | cupric chloride |
|---|---|---|
| pH / acidity | 7.5–9.5 (7.9–8.1 with aqueous resists; problems < 8.0 or > 8.8) | free acid < 0.1 N (chlorate regen) |
| Temperature | 120–130 °F | 125–130 °F |
| Dissolved Cu | 18–30 oz/gal (18–24 typical) | ≥ 20 oz/gal |
| Etch time for 1 oz (35 µm) Cu | ≤ 1 min | 55 s (130 °F) to 75–90 s (125 °F) |
| Replenishment control | density (SG) bleed-and-feed; pH via anhydrous NH3 | ORP + density; chlorine, chlorate, or H2O2 oxidizer |
| O2 solubility (hot) | — | 4–8 ppm; ozone < 3 % in O2 stream |
| Post-etch neutralizer | acidic ammonium chloride | HCl or oxalic acid |
### T-37.c Other copper etchants (§37.4.3–37.4.7)
| etchant | composition / operating point | Cu capacity / rate | compatible resists | cautions |
|---|---|---|---|---|
| Sulfuric–peroxide | H2O2 + H2SO4 + CuSO4; Mo ion, aryl-sulfonic stabilizer, thiosulfate, H3PO4 additives | slow; suited to fine lines on < ½ oz foil | metal resists, many organics | idle peroxide decomposition (meltdowns); CuSO4·5H2O crystallized at 50–70 °F |
| Ammonium persulfate | 20 % make-up; pH 4 → 2 | ≈ 7 oz/gal at 100–130 °F; 0.00027 in/min at 7 oz/gal, 118 °F | all common (solder, tin, Sn-Ni, inks, photoresist) | ≥ 130 °F above 5 oz/gal; rapid decomposition ≈ 150 °F |
| Sodium persulfate (batch) | 3 lb/gal + 15 ppm HgCl2 (obsolete) + additive + 57 mL/gal H3PO4; age 16–72 h | 0.0018 → 0.0006 in/min over 0–7 oz/gal | as above | disposal pH ≈ 2 |
| Ferric chloride | 28–42 wt % FeCl3; HCl ≤ 5 % (1.5–2.0 % customary); alloy etch 36 °Bé ≈ 4.0 lb/gal | high holding capacity | screen ink, photoresist, gold (not tin/solder) | costly disposal |
| Chromic–sulfuric (eliminated) | 30 °Bé, pH ≈ 0.1, 80–90 °F | 4–6 oz/gal; discard > 5.5 oz/gal | solder, Sn-Ni, gold, vinyl, photoresist | Cr6+; attacks PVC/PP; stains phenolic |
| Nitric acid (experimental) | 30 % copper nitrate + polymers + surfactants | fast; high capacity | dry film | exothermic runaway; needs specific foil grain |

### T-37.d Etchants for non-copper metals (§37.6)
| metal | etchants / conditions |
|---|---|
| Aluminum | FeCl3 12–18 °Bé; NaOH 5–10 %; inhibited HCl; H3PO4 mixtures; HCl + HF; FeCl3–HCl; residue dip 10 % HNO3 or chromic; DI spray rinse |
| Nickel & Ni alloys | FeCl3 42 °Bé at ≈ 100 °F; HNO3:HCl:H2O = 1:1:3 or 1:4:1 |
| Stainless (300–400 series) | FeCl3 38–42 °Bé (+3 % HCl optional); HCl (37 %):HNO3 (70 %):H2O = 1:1:1–3 by vol, ≈ 0.003 in/min at 175 °F; FeCl3 + HNO3; HCl:HNO3:H2O = 100:6.5:100 by wt |
| Silver | HNO3 (70 %):H2SO4 (96 %) = 1:19 on brass/Cu; 40 g CrO3 + 20 mL H2SO4 + 2000 mL H2O then 25 % NH4OH rinse; thin films 55 wt % ferric nitrate (water or ethylene glycol); alkaline cyanide + H2O2 (extreme caution); electrolytic 15 % HNO3 at 2 V, stainless cathode |

### T-37.e Etched-line formation numbers (§37.5, §37.7–37.8)
| item | value |
|---|---|
| Artwork accuracy | ≥ 10× product tolerance (0.0001 in → 0.00001 in) |
| Etch progression example | cupric; 3.0 mil L/S; 1.0 mil resist; 1 oz (1.4 mil) Cu; 140 s to R/B = 1; +25 s (18 %) → R/B = 1.25 |
| Undercut at R/B = 1 (example) | U = 0.525 mil |
| Gap limit rule of thumb | resist + foil: 1.2 + 1.4 = 2.6 mil; 0.4 + 0.35 ≈ 0.75 mil (19 µm) |
| Demonstrated fine lines | 30 µm L/S (3–5 µm foil + 14 µm plate, 17–19 µm traces); 50 µm (2 mil) L/S in 1 oz Cu with 1.4 mil resist (fiber-assisted flow) |
| Thin clad / etch-down | ≤ ¼ oz (9 µm); ½ oz (18 µm) etched to 3–9 µm |
| Semi-additive base Cu | 0.000050–0.000200 in |
| Hard-to-convey thin cores | 0.0015–0.003 in |
| Etcher material rating | ≥ 130 °F |

## 3. Mechanizable checks

- `CHECK-serdes-loss-budget`: inputs V_TX_min (V), V_RX_min (V), per-element losses (dB): BGA_end×2, connectors, vias×N, trace loss from sim → budget = 20*log10(V_RX_min/V_TX_min) → pass if Σloss ≤ |budget| (or ≤ 10–15 dB default; ≤ 18 dB with equalization) → margin = |budget| − Σloss (dB) → COOMBS-2003…2011.
- `CHECK-via-loss-allowance`: inputs via_count on Gb/s net, via style (through/blind/backdrilled) → per-via 0.75 dB (unoptimized) or 0.25 dB (optimized) → pass if Σ ≤ allocated via budget → COOMBS-2007.
- `CHECK-pdn-ripple`: inputs V_rail, simulated/measured ripple → pass if ripple/V_rail ≤ 0.05 → margin = 0.05 − ripple/V_rail → COOMBS-2012.
- `CHECK-decap-srf`: inputs C (F), ESL+L_mount (H) → f_SRF = 1/(2π√(LC)) → flag caps whose SRF < highest frequency they are expected to serve; flag mixed-value pairs whose antiresonance coincides with clock harmonics → COOMBS-2016, 2018.
- `CHECK-plane-capacitance`: inputs plane overlap area A (cm²), spacing d, Dk → C = ε0·εr·A/d; compare to 49–68 pF/cm² for 2-mil FR-4 → informational → COOMBS-2020, 2022.
- `CHECK-return-path-reactance`: inputs trace L (nH), f_knee → X_L = 2πfL → flag if X_L > 377 Ω (no adjacent plane) → COOMBS-2026.
- `CHECK-plane-split-crossing`: inputs high-speed net segments, reference-plane polygons per layer → count segments whose projection crosses a void/split of the adjacent plane → pass if 0 → COOMBS-2027, 2053.
- `CHECK-hazardous-voltage`: inputs net voltages → flag any net ≥ 42.2 VAC or ≥ 60 VDC → require PE bond + creepage/clearance review → COOMBS-2030, 2031.
- `CHECK-mount-support`: inputs board thickness (mm), mount-hole coordinates, outline → pass if ≥ 3 edges have a support within 25 mm and max support spacing ≤ 100 mm (0.7–1.6 mm boards) → COOMBS-2033, 2034.
- `CHECK-datums`: inputs fab drawing datum list → pass if ≥ 2 datums, none on a routed edge → COOMBS-2032.
- `CHECK-stackup-symmetry`: inputs layer list (type, copper weight) → pass if count even and types mirror about center → COOMBS-2056.
- `CHECK-adjacent-signal-layers`: inputs layer list → pass if no run of > 2 consecutive signal layers, each run bounded by planes, and each outer signal layer is adjacent to a plane → COOMBS-2052, 2058.
- `CHECK-plane-pair-spacing`: inputs stackup → pass if exists power/ground adjacent pair with 0.003 ≤ d ≤ 0.010 in (≥ 6 layers) → COOMBS-2057.
- `CHECK-z0-uniformity`: inputs per-layer computed Z0 → pass if all within 50–60 Ω (or spec) and layer-to-layer deviation small → COOMBS-2060.
- `CHECK-trace-pad-ratio`: inputs trace W entering SMT pad, pad width → pass if W ≤ 0.6·pad → COOMBS-2070.
- `CHECK-decap-distance`: inputs cap pad → nearest plane via distance → pass if ≤ 0.100 in else require dedicated via → COOMBS-2072.
- `CHECK-serpentine-gap`: inputs serpentine segment spacing, W → pass if gap ≥ 3W → COOMBS-2076.
- `CHECK-bga-grid`: inputs BGA pitch, placement grid, routing grid → pass if grid = pitch/2 and route grid = pitch/4 (or consistent) → COOMBS-2047.
- `CHECK-silk-on-pad`: inputs silkscreen objects, pads/vias → pass if no overlap → COOMBS-2081.
- `CHECK-drill-table`: inputs drill table → pass if every size has tolerance (default ±0.003 in), plated flag, count → COOMBS-2082.
- `CHECK-trace-ampacity-2152`: inputs I (A), W (mil), finished Cu thickness (mil), internal/external, board thickness (in), ΔT_allowed (°C) → area = W·t; ΔT_baseline from digitized IPC-2152 baseline chart (0.07 in polyimide, air); thickness correction factor from T-22.2 (10 → 12.1 → 13.3 °C for 0.070/0.059/0.038 in, ≈ ×1.21 / ×1.33); vacuum correction if applicable → pass if ΔT_corrected ≤ ΔT_allowed → margin = ΔT_allowed − ΔT_corrected → COOMBS-2087–2093. (Charts must be supplied as data; not in text.)
- `CHECK-parallel-conductors`: inputs group of simultaneously energized conductors within a proximity radius → A_eq = ΣA_i, I_eq = ΣI_i → evaluate CHECK-trace-ampacity-2152 on (A_eq, I_eq) → COOMBS-2095.
- `CHECK-trace-power-fraction`: inputs I_i, R_i (from ρ, L, A) → P_traces = ΣI_i²R_i → flag if P_traces/P_board > threshold (e.g., 5 %) → COOMBS-2096.
- `CHECK-thermal-via-array`: inputs d, t_plating, L, N, k = 0.389 W/mm·°C → R_via = L/(k·π·(r_o² − (r_o−t)²)); R_array = R_via/N → compare to required (θ_jp + R_array + R_spread) budget → COOMBS-2114.
- `CHECK-thermal-via-geometry`: inputs thermal via list → pass if pitch within 1.0–1.2 mm, drill ≈ 0.3 mm, plating ≥ 0.025 mm, no thermal relief on plane connection, filled if through-hole under exposed pad, ≥ 1 via per thermal ball → COOMBS-2112, 2113.
- `CHECK-thermal-plane-continuity`: inputs thermal plane polygon, isolation cuts → flag any cut that partitions the plane region under/around a hot component (each 1 mm gap ≈ 1000 mm Cu) → COOMBS-2109.
- `CHECK-plane-thickness-thermal`: inputs plane Cu weights → warn if spreading plane < 1 oz effective; note saturation at 2.8 oz → COOMBS-2111.
- `CHECK-natural-convection-capacity`: inputs PCB area (cm²), total P (W), orientation → interpolate Fig. 23.9 anchors (15×15 cm: 50 W → 80 °C; 20×20 cm: 50 W → 50 °C) → warn if predicted ΔT exceeds limit → COOMBS-2121.
- `CHECK-heatsink-needed`: inputs component P → flag ≥ 2.5 W without heat sink; flag 50–300 W without bolster-plate design → COOMBS-2126.
- `CHECK-rf-shield-perforation`: inputs hole size, f_max → pass if hole < c/(10·f_max) → COOMBS-2125.
- `CHECK-embedded-resistor`: inputs R_s, L, W, corner count → R = R_s·(L/W straight squares + 0.56·corners) → pass if within tolerance of target → COOMBS-2132, 2133.
- `CHECK-embedded-capacitor`: inputs A (cm²), t (cm), Dk → C = 8.854e−14·Dk·A/t → pass if within target ± tolerance → COOMBS-2134.
- `CHECK-embedded-inductor-limit`: inputs L_target, layers, ferrite → flag if L_target > 10 nH (1 layer) / 30 nH (multilayer) / 100 nH (ferrite) → COOMBS-2138.
- `CHECK-embedded-layer-mixing`: inputs per-layer component types → fail if a layer has both formed and placed embedded components → COOMBS-2144.
- `CHECK-hdi-needed`: inputs total connections, board area (both sides) → density = connections/in² → HDI recommended if > 110–130 → COOMBS-2147.
- `CHECK-microvia-aspect`: inputs via d, dielectric thickness, base Cu thickness → effective AR = (t_diel + t_Cu)/d → warn if L/S ≤ 75 µm or d < 75 µm with thick base Cu → COOMBS-2155.
- `CHECK-lamination-fill-eligibility`: inputs plated hole d (mm), core thickness (mm) → pass (fill by RCC/prepreg lamination) if d ≤ 0.3 and t ≤ 0.6, else require separate fill process → COOMBS-2163.
- `CHECK-paste-fill-rules`: inputs via d (µm), core t (µm) → AR = t/d → pass if 152 ≤ d ≤ 635, 152 ≤ t ≤ 2159, AR ≤ 6 → COOMBS-2165.
- `CHECK-via-formation-method`: inputs via d (in), depth (in) → mechanical if d > 0.012 or depth > 0.016 (Ch. 29) / laser if d < 0.008 in (0.20 mm) (Ch. 25); flag conflicts for review → COOMBS-2168, 2231.
- `CHECK-laser-min-via`: inputs via d, laser type → pass if d ≥ 50 µm (CO2 mass production) or ≥ 20–30 µm (UV-YAG) → COOMBS-2175.
- `CHECK-capture-pad-rcc`: inputs capture pad d, process (RCC window) → warn if pad < 250 µm → COOMBS-2178.
- `CHECK-drill-flute-length`: inputs stack thickness, entry thickness, backup penetration, bit flute length → pass if L_flute ≥ Σ + 0.050 in → COOMBS-2205.
- `CHECK-drill-stack-depth`: inputs panels × thickness + entry + backup penetration, drill d → pass if total ≤ 17·d → COOMBS-2224.
- `CHECK-backup-penetration`: inputs d → target = min(d, 0.040 in) (or point length + 0.010 in) → COOMBS-2221.
- `CHECK-spindle-rpm`: inputs d (in), target sfm, spindle max rpm → rpm = 12·sfm/(π·d) → warn if rpm > max (surface speed falls short) or < min → COOMBS-2218, 2222, 2235.
- `CHECK-retract-rate`: inputs d, retract ipm → warn if d ≤ 0.025 in and retract > 500 ipm → COOMBS-2220.
- `CHECK-mech-blind-via-ar`: inputs blind depth, d, plating capability AR_max, dielectric under target → pass if depth/d ≤ AR_max and dielectric-under-target ≥ tolerance stack → COOMBS-2237.
- `CHECK-peck-effective-ar`: inputs z stroke, d_min, N_pecks → AR_eff = stroke/(d_min·N) → informational vs 1–15 scale → COOMBS-2238.
- `CHECK-predrill-needed`: inputs d → if d ≥ 4.0 mm require pilot 0.15–0.35·d → COOMBS-2240.
- `CHECK-backdrill-stub`: inputs must-not-cut layer depth, must-cut layer depth, dielectric thickness tolerances, drill depth tolerance → stub_max = nominal stub + Σ tolerances → pass if stub_max ≤ spec and must-cut layer always cut → COOMBS-2226.
- `CHECK-min-line-vs-resist`: inputs resist thickness (µm), min line width (µm) → pass if W_min ≥ t_resist + 10 (warn) / + 25 (safe) → COOMBS-2247.
- `CHECK-imaging-method`: inputs min feature (µm) → screen print if ≥ 200, photolithography otherwise; flag < 25 µm as LDI/liquid-resist territory → COOMBS-2246, 2250.
- `CHECK-drill-room-env`: inputs T, RH → pass if 22 ± 1.1 °C and 45–60 % RH → COOMBS-2234.
- `CHECK-pattern-plate-resist`: inputs t_resist (µm), t_plated (µm), min conductor width (µm) → pass if t_resist ≥ t_plated and W ≥ max(t_resist, 1.5·t_plated) [ratio from 38 µm @ 25 µm; derived] → COOMBS-2264.
- `CHECK-fixed-pitch-split`: inputs pitch, W, S, process (etch/plate) → etch: warn if S < W at fine pitch; plate: warn if final W < S → COOMBS-2265.
- `CHECK-wrap-copper`: inputs measured wrap thickness (µm), class → pass if ≥ 12.7 µm (Class 3) or ≥ 5 µm (Class 2 MRB floor); margin = wrap − limit → COOMBS-2287.
- `CHECK-buried-via-resin`: inputs buried via list (d, L), prepreg resin volume available per area → pass if resin volume ≥ Σ π(d/2)²L + encapsulation need; else prefill → COOMBS-2285.
- `CHECK-prepreg-plies`: inputs opening: adjacent Cu thickness, plane-to-plane bias voltage → require ≥ 2 plies if Cu ≥ 70 µm or high bias → COOMBS-2311.
- `CHECK-lamination-recipe`: inputs material class, heat rate (°C/min), flow pressure (psi), cure T/time → pass if within T-31.lam window for that class (dicy FR-4 4–8 °C/min @ 200–300 psi, 180 °C/60 min; HF/LFAC 2–4 °C/min @ 225–360 psi, ≤ 200 °C/120 min) → COOMBS-2307–2309.
- `CHECK-cure-tg-shift`: inputs TMA Tg run 1, run 2 → pass if |Tg2 − Tg1| ≤ 5 °C → COOMBS-2315.
- `CHECK-odd-layer-balance`: inputs layer count, core thicknesses → flag odd count; pass if core thicknesses symmetric about center → COOMBS-2275.
- `CHECK-foil-elongation`: inputs foil grade, required elongation (flex/thermal cycling) → pass if grade elongation ≥ requirement (std 3 %, HTE 5–8 %, HD-E ≥ 10 %) → COOMBS-2296.
- `CHECK-di-water`: inputs pH, TOC, turbidity, chloride → pass if 6.5 ≤ pH ≤ 8.0, TOC ≤ 2.0 ppm, turbidity ≤ 1.0 NTU, Cl ≤ 2.0 ppm → COOMBS-2320.
- `CHECK-plating-time`: inputs target thickness (mil), J (ASF), efficiency η → t_h = 17.8·thickness/(J·η) → COOMBS-2326.
- `CHECK-throwing-power`: inputs required hole-wall Cu (mil), TP at the hole AR → required surface Cu = hole Cu / TP; flag if surface Cu exceeds etch/impedance budget → COOMBS-2327.
- `CHECK-plated-cu-ductility`: inputs tensile (psi), elongation (%) → pass if > 35,000 psi and > 15 % → COOMBS-2328.
- `CHECK-anode-count`: inputs plating mode, panel size → pass if baskets per 18×24 in panel = 3–4 (panel plate) or 2–3 (pattern plate), scaled by area → COOMBS-2334.
- `CHECK-filter-turnover`: inputs pump flow (gal/h), bath volume (gal) → turnovers = flow/volume → pass if 2 ≤ turnovers ≤ 4 (≥ 2 minimum) → COOMBS-2337.
- `CHECK-rectifier`: inputs ripple %, rated A, working A → pass if ripple < 5 % and working A is a reasonable fraction of rating → COOMBS-2339.
- `CHECK-horizontal-module-length`: inputs target Cu (mil), J (ASF), η, conveyor speed (m/min) → t_min = 60·17.8·mil/(J·η); L = v·t_min → compare to line length → COOMBS-2342.
- `CHECK-blind-via-fill-ar`: inputs microvia depth, diameter → pass if depth/diameter ≤ 1.2 (≤ 1.0 preferred) → COOMBS-2344.
- `CHECK-toc-window`: inputs TOC now, baseline → treat if TOC ≥ 4·baseline; after treatment expect ≈ 0.7·TOC_high → COOMBS-2346.
- `CHECK-tin-bath`: inputs ppm Cu, Cd, Zn, Ni, Fe, Cr, Cl → pass if ≤ 10, 50, 50, 50, 120, 5, 75 → COOMBS-2351.
- `CHECK-nickel-bath`: inputs ppm Fe, Cu, Cr, Al, Pb, Zn, Sn, Ca; stress (kpsi) → pass if ≤ 250, 10, 20, 60, 3, 10, 10, 0 and stress < 10 → COOMBS-2355, 2356.
- `CHECK-gold-finger-stack`: inputs Au (µin), Ni (µin), class/market → pass if Ni ≥ 200 and Au 50–100 (mil) or 25–50 (commercial); flag Type II hard gold on wire-bond pads → COOMBS-2353, 2357, 2359.
- `CHECK-finish-thickness`: inputs finish type, XRF readings (mean, σ) → compute mean ± 4σ → pass per spec: ENIG Ni 3–6 µm and Au(−4σ) ≥ 0.05 µm (Rev A: 1.6–4.0 µin); ENEPIG Ni 3–6 µm, Pd 0.05–0.15 µm (±4σ), Au(−4σ) ≥ 0.025 µm and ≤ 2.8 µin; ImAg 0.12–0.4 µm (±4σ); ImSn(−4σ) ≥ 1.0 µm → margin = distance of ±4σ bound to limit → COOMBS-2368, 2372, 2378, 2380.
- `CHECK-finish-selection`: inputs requirements {min pitch, Au wire bond, Al wire bond, ICT probing on finish, press-fit, contact/keypad, HF loss sensitivity, shelf life needed, Pb-free} → rules: pitch < 0.5 mm → exclude HASL; Au wire bond → ENEPIG, soft electrolytic Au, EN/ImAu/electroless Au (exclude ENIG, HASL, OSP); probing/contact → exclude OSP; HF-sensitive → flag Ni-bearing finishes (consider EPIG/ImAg/OSP); press-fit → ImSn preferred (also ENIG/ENEPIG/ImAg); shelf > 12 months → ENIG/ENEPIG (OSP cat 3 = 12 months) → COOMBS-2365–2383.
- `CHECK-imag-layout`: inputs finish = ImAg, pad definitions, test-pad pitch, via fill → fail on solder-mask-defined pads, partially filled vias, test pads < 80 mil apart → COOMBS-2379.
- `CHECK-mask-web`: inputs pad-to-pad gap, mask expansion per side → web = gap − 2·expansion → pass if web ≥ 3 mil (standard) or ≥ 1.0–1.5 mil with supplier confirmation; else gang-relieve → COOMBS-2385.
- `CHECK-mask-outgassing`: inputs TML %, CVCM % → pass if ≤ 1.0 and ≤ 0.10 (space use) → COOMBS-2391.
- `CHECK-mask-develop`: inputs developer pH, breakpoint position (% of chamber) → pass if 10.6 ≤ pH ≤ 11.3 and breakpoint 10–15 % → COOMBS-2404.
- `CHECK-legend-ul`: inputs legend polygons → flag any contiguous legend area larger than ½ × 5 in → require UL94 qualification of the legend → COOMBS-2411.
- `CHECK-via-protection-sides`: inputs via-protection spec per via class → fail if protected from one side only ahead of an inert final finish → COOMBS-2409.
- `CHECK-etchant-resist-compat`: inputs etch resist, etchant → fail tin or solder with cupric/ferric chloride; warn silver (MIL-STD-275) and rhodium → COOMBS-2415, 2424.
- `CHECK-ammonia-etch-window`: inputs pH, T (°F), Cu (oz/gal) → pass if 8.0 ≤ pH ≤ 8.8 (7.9–8.1 target with aqueous resists), 120 ≤ T ≤ 130, 18 ≤ Cu ≤ 24 (≤ 30 max) → COOMBS-2420–2422.
- `CHECK-cupric-etch-window`: inputs T, Cu, free acid, regen type → pass if 125–130 °F, Cu ≥ 20 oz/gal, chlorate free acid < 0.1 N; flag Cl2 risk when acid added to low-acid chlorate bath → COOMBS-2425–2426.
- `CHECK-persulfate-bath`: inputs T (°F), Cu (oz/gal) → pass if Cu ≤ 7, T ≥ 130 when Cu > 5, and T well below 150 → COOMBS-2430.
- `CHECK-artwork-tolerance`: inputs artwork positional/edge tolerance, product feature tolerance → pass if artwork ≤ product/10 → COOMBS-2436.
- `CHECK-fine-line-gap`: inputs resist thickness, final Cu thickness (foil + plating in etch), min designed space and line → pass if space ≥ t_resist + t_Cu and line top after undercut (≈ line − 2U) ≥ functional minimum → COOMBS-2442.
- `CHECK-etch-profile`: inputs cross-section R, B, T, t → R/B, U = (R − T)/2, F = 2t/(B − T) (conventional forms; source equations not in text) → pass if 0.95 ≤ R/B ≤ 1.05 (shop-set window) and F ≥ shop target; compare processes only at equal R/B → COOMBS-2439–2440.
- `CHECK-linewidth-cp`: inputs linewidth sample (µm), USL, LSL → Cp = (USL − LSL)/(6σ) → pass if Cp ≥ customer/shop target; also report by panel position and orientation → COOMBS-2443, 2437.

## 4. Verification procedures & plots

- **Channel insertion loss vs frequency (§20.4.4, Fig. 20.25):** x = frequency (0–10 GHz), y = loss (dB); plot total, resistive (skin) and dielectric components; mark the crossover frequency where dielectric loss overtakes resistive loss; good = total loss at Nyquist ≤ budget (10–15 dB; ≤ 18 dB with equalization). Companion: eye diagram vs PCI Express (or protocol) eye mask; pass = eye clear of mask with margin.
- **Capacitor / PDN impedance vs frequency (§20.5.4, Figs. 20.29–20.30):** x = frequency (log, 100 kHz–1 GHz), y = |Z| (Ω, log); show each cap's V-shaped curve (min = ESR at SRF), the parallel combination (look for antiresonant peaks, e.g., 120 MHz for 100 nF ∥ 1 nF) and the plane-pair contribution above ~150 MHz; pass = Z_PDN ≤ Z_target across band and no antiresonance peak at a clock harmonic.
- **Return-path/reactance sweep (§20.6.3):** x = frequency, y = |Z| of trace-loop (R + jωL); compare to 377 Ω; pass = loop impedance stays low because an adjacent plane is present (small L).
- **Board natural-frequency check (§20.8.2, Fig. 20.44):** FEA or plate formula for f_n under the actual edge conditions (free/supported/clamped); pass = f_n sufficiently above vibration threat; deflection ≤ Steinberg limit (10e6 sinusoidal / 20e6 random reversals).
- **Trace temperature rise chart (IPC-2152 style, §22.3):** x = current (A), y = cross-sectional area (sq mil) or trace width per Cu weight; family of curves at ΔT = 10, 20, 30, 45 °C (baseline 0.07 in polyimide, air, no planes; separate internal/external, ½–3 oz, vacuum); design point must lie on the safe side of the ΔT_allowed curve; apply thickness correction (T-22.2) and parallel-conductor summation; test per IPC-TM-650 2.5.4.1a if measuring.
- **Component temperature vs trace length / plane size (Figs. 23.3, 23.6):** x = trace length (mm) or plane edge length (mm), y = ΔT above ambient or effective θ_ja; good = curve flattening (diminishing return ~15 mm trace); use to pick minimum copper that reaches the plateau.
- **Thermal contour with plane cut (Fig. 23.7):** contour plot of board temperature with and without isolation slots; a step of tens of °C across a slot indicates a broken spreading path.
- **PCB power dissipation curve (Fig. 23.9):** x = power (W), y = ΔT above 25 °C for each board size (10×10 to 20×20 cm), horizontal natural convection; formatted like a heat-sink curve; pass = operating point below allowed ΔT.
- **Thermal via plating verification (§23.3.3):** parallel-polish coupon from the surface to measure barrel plating thickness (target ≥ 0.025 mm); cross-sections off-center under-read.
- **System CFD in three phases (§23.6.1):** (1) airflow/dead-zone map with all obstructions; (2) power-area map; (3) detailed layout with 2-resistor (±20 %) or compact (±5 %) component models; mesh-sensitivity study before critical runs.
- **Embedded passive verification (§24.4–24.5):** 4-wire resistance of each formed resistor vs square count (R = R_s·squares, corners 0.56); laser-trim with probe card or flying probe to tolerance; capacitance vs area/thickness (C = 8.854e−14·Dk·A/t); test voltage kept below dielectric breakdown of thin laminates.
- **Laser microvia cross-section (§25.6.3, §29.9–29.10):** section through via and capture pad; check taper, capture-pad penetration, residual glass fibers/smear, plating to via bottom; for RCC windows plot window-to-pad offset vs pad diameter (serious below 250 µm).
- **Spindle run-out chart (§28.3.4.2):** x = spindle ID (weekly), y = static TIR (mil); limit lines 0.5 mil (d > 0.020 in) and 0.2 mil (d ≤ 0.020 in); good = all below line after collet cleaning.
- **Hole quality vs hit count (§28.5, §28.7):** cross-sections at intervals of hits per tool; y = roughness/voids/nail-heading/smear; set max hits where defects rise; separate mechanical (chip load) from heat (surface speed) defects.
- **Backdrill stub (§28.4.10):** cross-section stub length distribution vs must-not-cut / must-cut layers; pass = stub ≤ spec with must-cut layer always severed.
- **Innerlayer registration (§29.7):** X-ray best-fit of stacked coupon pads; vector plot of per-layer offset; after final drill, hole-to-pad centering histogram.
- **Resist and mask contrast curve (§30.6.4.1.3):** x = log exposure dose (mJ/cm²), y = % film thickness remaining after develop; choose dose on plateau (loss < 10 %); monitor with step wedge each shift.
- **Lamination profile (§31.4.5, Fig. 31.32):** x = time; y1 = temperature from thermocouple at center-stack edge; y2 = pressure; mark kiss, flow window (dicy FR-4 70–130 °C at 4–8 °C/min; HF/LFAC 80–140 °C at 2–4 °C/min), cure hold (≈ 180 °C × 60 min epoxy; ≤ 200 °C × 120 min LFAC), controlled cool through Tg.
- **TMA double run (§31.5.1.3, Fig. 31.34):** dimension vs temperature for two consecutive scans; pass ΔTg ≤ 5 °C.
- **Lead-free reflow robustness (§31.5.2):** N production reflows at the assembly profile → visual blister check → cross-sections in high and low hole-density areas; pass = no delamination, laminate cracks, voids, hole-wall pull-away.
- **Filled-via planarization (§31.2.4.3):** eddy-current Cu map before/after each sanding pass; cross-section wrap Cu at panel center and edge; pass wrap ≥ 12.7 µm (Class 3) everywhere.
- **Throwing power vs aspect ratio (§33.3.1.2):** x = AR (3:1 to 15:1), y = TP % from cross-sections (center vs knee); anchors 100 % @ 3:1, 33 % @ 15:1 (conventional), > 85 % @ 15:1 at 8 ASF (optimized); use to set surface Cu = hole Cu / TP.
- **Plated copper T&E (§33.3.2):** tensile test on plated foil; pass UTS > 35,000 psi and elongation > 15 %; repeat after additive or rectifier changes.
- **TOC control chart (§33.3.3.7.3):** x = Ah/L or date, y = TOC (ppm); lines at 1× make-up, 4× (carbon-treat trigger), ≈ 0.7 × peak (post-treat target).
- **Surface-finish thickness (§35.4–35.8):** XRF on 1.5×1.5 mm pads; histogram with mean ± 4σ vs spec limits (ENIG, ENEPIG, ImAg, ImSn); SPC by bath age.
- **Black-pad screening (§35.4.4, IPC-4552 Rev A chart):** strip Au, SEM/cross-section Ni surface, classify corrosion (acceptable/debatable/rejectable); solder-ball pull test — failure at Ni/solder interface with dark pad = black pad.
- **OSP/finish solderability (§35.6, J-STD-003):** wetting tests after steam/thermal aging for the claimed durability category (cat 3 = 12 months); multiple reflow survivability for Pb-free.
- **Mask qualification (§36.4.10, §36.5.2.1.4):** tape test after final-finish chemistry; post-develop inspection (registration, mask in holes, dam retention); IPC-SM-840 tests; ionic cleanliness after assembly.
- **Etch progression (§37.7.3, Fig. 37.5):** x = relative etch time t/t(R/B = 1), y = R/B, U, F from cross-sections; slope near R/B = 1 is the sensitivity; operate where conveyor-speed resolution can hold R/B within window.
- **Linewidth capability map (§37.7.4.1, §37.7.4.6):** IPC-9251/CAT vehicle; histogram of linewidth with USL/LSL and Cp; heat map by panel position and trace orientation; time-lagged panel series to expose etch-rate drift.

## 5. Pitfalls, failure modes, review checklist

- Glass-weave skew: the two halves of a differential pair running over different weave regions get ps-level timing skew — align/rotate or use spread glass (§20.4).
- Any impedance discontinuity or ringing on a periodic signal is a guaranteed emissions source (§20.6.2).
- Mixed-value decoupling (e.g., 100 nF + 1 nF) creates an antiresonance (120 MHz in the example) that a switching harmonic can excite into radiated EMI (§20.5.4).
- Decoupling caps are useless above their SRF; via/trace inductance in the mounting lowers SRF (§20.5.4–20.5.5).
- Single-sided boards with digital logic generally fail EMC unless edges > 1 µs (§20.6.3).
- A trace over a plane slot forces return current around the slot: larger loop, crosstalk, PDN noise, EMI — even though the circuit still "works" (§20.6.4).
- Single-point ("star") grounding goes inductive above tens of kHz; ineffective for > 100 kHz–1 MHz (§20.6.8–20.6.9).
- Datum on a routed edge from a late machining step → registration errors (§20.7.2).
- Boards misused as structural support for heavy magnetics/transformers fail in vibration; largest strain at board center (§20.7.9–20.8.1).
- Plug-in module: only the free edge flexes — add a handle bar/restraining bar at the free edge (§20.7.9).
- Vibration + thermal-cycle strains superpose in fatigue-life models (§20.7.10).
- Placing parts solely by netlist ignores priority of critical nets (§21.7).
- Two signal layers at the outer surface leave no return for the outermost layer and make impedance uncontrollable (§21.9).
- A trace on a plane layer cuts off return current in that region (§21.10).
- Text/ref des on pads or vias is deleted in fab — useless (§21.11).
- Autorouters fail on high-density low-layer-count boards and produce longer, via-heavy routes (§21.10).
- Old IPC-2221 internal-trace chart was not measured data (external ÷ 2); companies that never migrated to IPC-2152 are sizing on a fiction that happened to be conservative (§22.2.1, §23.7).
- Thin boards and flex run hotter for the same trace/current (§22.3.4).
- Odd geometries: neck-downs at connector pins and via-perforated planes are hot spots invisible to charts (§22.3.7).
- Trace fusing under high-current pulses occurs earlier than steady-state extrapolation predicts (§22.3.8).
- θ_ja from a datasheet applied with T_j = T_a + θ_ja·P gives "wildly erroneous" results; PCB changes θ_ja by ≥ 2× (§23.1).
- "Floating" exposed-pad packages on excess paste → tilted package, open leads; the wrong fix (removing thermal-pad solder) causes field failures from overheating (§23.3.2).
- A 0.25 mm noise-isolation slot cut a thermal plane's effectiveness in half: +33 °C on the part (§23.3.2).
- Thermal-relief spokes on thermal vias throttle heat into the plane (§23.3.3).
- Unfilled through-hole thermal vias wick solder from the thermal joint/balls → opens (§23.3.3).
- Under-plated thermal vias (0.015 vs 0.025 mm) raise via resistance 45 → 73 °C/W; cross-section metrology can mis-measure plating (§23.3.3).
- Hot components downstream of other hot components see air 10–30 °C warmer (§23.3.4).
- Continuous RF shield cans create airflow dead zones over enclosed parts (§23.4.4).
- Smeared-copper thermal models (coverage-weighted k) hide plane isolation cuts (§23.6.3).
- Modelling without cables, shields, daughter cards, filters, dust and user-blocked vents → thermal shutdown in the field (§23.6.1).
- Embedded resistors: one value per layer for foil materials; trimming slow; no rework; test voltage can break down thin dielectric; capacitor charge-up slows test (§24.3.2).
- Mixing formed and placed embedded components on one layer damages the formed parts (§24.6.3.5).
- Microvia bottlenecking: thick base copper increases aspect ratio; via plates shut at the top with a void at the bottom (§25.5.1.2).
- Photovia and plasma-via processes cannot make skip vias (L1–L3) (§25.4.1).
- Photovia resin shrinks after via formation → random hole movement, registration failures; keeps photovia panels ≤ 400×400 mm (§25.6.1).
- RCC window-drilled CO2 vias misregister to capture pads < 250 µm (§25.6.3.2).
- Three consecutive CO2 pulses on one spot overheat the capture pad and smear epoxy (§25.6.3.2).
- YAG through woven glass: power set for glass crossovers blows through at glass openings and damages capture pads (§25.6.3.1).
- Residual glass fibers protruding into laser vias (YAG in prepreg) hurt reliability unless blasted out (§25.6.3.3).
- Trapped Pd catalyst in porous resin → electromigration (§25.6.1).
- Solder-mask ink used as via fill: solvent craters at small holes, low adhesion (§25.5.3.2.6).
- Plasma-via copper overhang → unreliable plating unless secondary etched (§25.6.2).
- RS-274-D with separate aperture tables has no standard → fabricator re-keying errors (§27.3).
- Positive plane layers supplied instead of negative confuse CAM (§27.3).
- Missing IPC-D-356 netlist means the fabricator cannot verify shorts/opens against design intent (§27.3, §27.4.6.6).
- Fab/assembly-side fixes not fed back to the design database resurface on the next spin (§27.4.2.2).
- Drill bits touching each other or pod walls chip the carbide (§28.2.2.2).
- Partial-margin-relief drills run ≥ 25 % hotter → smear, packed margins, breakage (§28.2.2.3).
- Insufficient flute length (no 0.050 in reserve) → debris packing, hole defects, breakage (§28.2.2.4).
- Repointed bits with damaged/packed margins contaminate holes from the first hit and cause run-out (§28.2.2.6).
- Loose drill rings shift during tool change → short drilling depth; tight rings crack; ring flash prevents collet seating (§28.2.3).
- Phenolic entry contaminates hole walls; desmear chemistry cannot remove phenolic (§28.2.4.3).
- Warped/pitted entry material → burrs, deflection, small-drill breakage (§28.2.4.3).
- Tooling pins < 1/8 in, worn bushings, or overlapping sub-tooling plates let the stack move → burrs, mislocation, breakage (§28.2.6, §28.3.3).
- Gap between spindle casing and pressure-foot window after a z-height change steals the vacuum → debris everywhere, breakage (§28.3.4.5).
- Excess backup penetration wears and breaks small drills; too little leaves incomplete holes — backup thickness variation matters (§28.4.5).
- Pinned (rather than taped) entry sheets separate from the stack → entry burrs, breakage (§28.4.9.3).
- Backdrill stub grows when PCB thickness/layer tolerances stack up even though the machine is accurate to µm (§28.4.10).
- Peck drilling: repeated pad contact increases nail-heading; reheating causes resin smear and roughness (§29.6.2).
- Bird-nest chips on large/heavy-copper holes falsely trigger contact-drilling zero → wrong depth or missing holes (§29.6.5).
- YAG set for glass crossovers damages capture pads at glass openings; UV dielectric removal can over-ablate the landing pad (§25.6.3.1, §29.9).
- Off-contact or poorly collimated exposure exposes under opaque areas → line-width loss for ≤ 100 µm features (§30.4, §30.6.4.1.4).
- Deep brush gouges prevent dry-film conformation → opens after etch, underplating/shorts after pattern plating (§30.6.2.1).
- Mechanical scrubbing of thin cores (< 0.020 in) distorts them → registration failures (§30.6.2.1).
- Residual pumice after inadequate rinse → resist defects (§30.6.2.1).
- Chemically roughening RTF/DSTF foil smooths its engineered tooth (§30.6.2.2).
- Electrostatic resist coating on outerlayers: thick rim, uncoated barrel (§30.6.3.6).
- Solvent-developable resists scum between features (§30.3.3).
- Worn punched film-artwork holes and drifting glass bushings degrade registration over use (§30.6.4.1.2).
- Un-replaced exposure lamps (> ~1000 h) drift spectrally and may explode into the optics (§30.6.4.1.4).
- Etching fine pitch with equal L/S forces the resist to resolve a space narrower than the line after undercut → shorts (§30.7.2).
- Round capture pads next to passing lines narrow the channel → shorts in print-and-etch, underplating in additive (§30.7.3).
- Clad-outer builds: outer foil mask scratched during innerlayer steps → shorts/opens (§31.2.2.2).
- Heavy-copper first layer on foil-outer builds telegraphs weave/circuit texture to the surface (§31.2.2.2).
- Single-sided clad release-sheet side bonds poorly without aggressive prep (§31.2.2.3).
- Buried-via clusters starve prepreg resin → local voids/weak bond (§31.2.4).
- Over-planarization removes wrap Cu → butt joint → pad rotation/knee crack; wrap < 5 µm is high risk (§31.2.4.2).
- Cap plating over outgassing fill separates during sequential lamination or thermal stress (§31.2.4.3.1).
- Some fills are attacked by permanganate; ceramic-filled fills over-roughen in aggressive plasma (§31.2.4.3.1).
- Filled-via defects are hard to find by coupon analysis; ESS may not screen them — latent field failures (§31.2.4.4).
- Double-treated foil: resist does not fully develop → shorts; incompatible with blind/buried via plating (§31.3.2.2).
- Overdetermined full-perimeter tooling stretches panels over pins (§31.3.5).
- Silicone press pads near end of life leach silicone oil → contamination (§31.4.1.3).
- Aluminum caul/separator plates expand more than the MLB → loose pins needed, registration loss (§31.4.1.1, §31.4.2).
- Too much pressure during B-stage melt crushes glass and increases print-through; improper melt staging → "footballing" (§31.4.5.1–31.4.5.2).
- High pressure with high-flow resin → resin starvation (§31.5.1.1).
- Solid copper borders adjacent to sparse circuitry → blisters/delamination (§31.5.1.2).
- Baking beyond full cure lowers Tg; post-bake warp fixes mask non-uniform cooling (§31.5.1.4).
- LFAC/halogen-free boards: delamination, voids, hole-wall pull-away may appear only after lead-free reflow (§31.5.2).
- Hard/impure process water → Cu-Cu peelers, PTH residues, staining, ionic contamination (§32.3.2).
- Chromic-acid desmear with insufficient Cr6+ neutralization → copper voids (§32.4.3.2).
- Plasma desmear leaves ash and little texture → poor hole-wall adhesion unless followed by permanganate (§32.4.3.4).
- Electroless: low loading/low temperature/high air agitation → voids; over-catalyzation/over-conditioning → pull-away and ICD (§32.5.3).
- High-AR holes: 15:1 at 33 % TP needs 3× surface Cu to hit hole-wall minimum — etch and impedance suffer (§33.3.1.2).
- Shrinking slab anodes change the current distribution; small anode balls buried in sludge (§33.3.3.3.1).
- Torn anode bags or solution above bag tops → sludge in bath → nodules (§33.3.3.8.4).
- Panels racked > 1 in below surface → top-edge overplate; cathode-bar gaps → edge overplate (§33.3.3.3.2).
- Oversized rectifier at low current or ripple ≥ 5 % → coarse deposit, poor T&E (§33.3.3.4.1).
- PPR changes the crystal structure (duller) — T&E can fail even when distribution improves (§33.3.3.4.2).
- Horizontal plating at 40–80 ASF loses throwing power; soluble-anode film particles nodulate the top side (§33.3.3.5).
- Blind-via fill without vigorous laminar flow plates conformally instead of filling (§33.3.3.6.2).
- Over-leveling thins the hole knee → corner cracks after thermal shock; excessive leveling → step plating (§33.3.3.8.1, §33.3.3.8.7).
- Cleaner drag-out poisons the acid Cu bath (two-step rinse) (§33.3.3.9.1).
- Aggressive microetch can etch through thin electroless Cu (§33.3.3.9.2).
- Thin/voided tin etch resist → etch-out voids in holes (§33.3.3.8.3).
- Adjusting sulfamate nickel pH with sulfuric acid or adding sulfates breaks the bath down (§33.5.1.1).
- Type II hard gold on wire-bond pads: not bondable (§33.6.1).
- Gold on under-activated nickel peels (§33.6.1.1.4).
- DMT: nothing visible in the hole to confirm coverage — only flash plating proves it (§34.1.8).
- HASL on < 0.5 mm pitch: non-planar pads, bridging, plugged vias; the extra thermal cycle warps the board and consumes copper (§35.3).
- Reading IPC-4552's "typical" Au range (0.075–0.125 µm) as spec limits (§35.4.1).
- Black pad: aggressive (low-Au) gold bath + long dwell on creviced nickel → weak joints failing at Ni–solder interface (§35.4.4).
- Specifying thick immersion Au on ENEPIG lengthens dwell and corrodes Ni under the Pd (§35.5.1).
- ENIG used for Au wire bonding: Ni diffuses to the Au surface over time → bond failures (§35.5).
- Thick electrolytic Au used as a solder surface → embrittled joints (§35.9.2).
- OSP handled/packaged before stabilizing → discoloration; fingerprints; cannot be probed at ICT (§35.6.1–35.6.2).
- Immersion silver left exposed after assembly tarnishes → creep corrosion; SMD pads and partially filled vias trap chemistry (§35.7.2).
- Immersion-tin thiourea (sulfur) contaminating shared OSP/Ag/ENIG lines; tin whiskers; IMC consuming the tin during storage (§35.8).
- Dry-film solder mask too thick for fine-pitch/flip-chip assembly and not robust in ENIG/ImSn baths (§36.3.2, §36.4.5.1).
- Partially developed mask in microvias traps air → blisters/eruptions exposing Cu (§36.2.3).
- Over-aggressive tack dry leaves mask in holes (§36.4.4.1).
- Mask over tin/solder residue or Cu-Sn IMC → adhesion loss (§36.5.1.1.1).
- Worn pumice (fractured silica, rounded Al2O3) peens instead of roughening copper → poor mask adhesion (§36.5.1.1.2).
- Temporary masks incompatible with the permanent mask → swelling, blistering (§36.3.3).
- Brushed copper before ENIG/immersion tin: scratches wick chemistry under the mask → lifting at openings (§36.5.1.1.2).
- City/well-water rinse before mask → blisters, discoloration; droplets dried on panels leave minerals (§36.5.1.1.3).
- Curtain coating "blips"/skips at tall circuits; thin panels fly, thick panels slip (§36.5.2.1.1).
- Tack-drying panels touching each other; over-dry "lock-in"; under-dry artwork marking/sticking (§36.5.2.1.2).
- Aging exposure lamps: longer exposures and hotter frames → artwork marking or mask transfer to phototool (§36.5.2.1.3).
- Develop breakpoint set like photoresist (≈ 50 %) leaves mask in small holes (§36.5.2.1.4).
- Hot-roll lamination of dry-film mask traps air along traces (§36.5.2.2.2).
- Stripping mask after cure may be impossible without laminate damage (§36.5.4.3).
- Single-sided via plugging before an inert finish → ring void at barrel–plug interface → trapped chemistry, corrosion (§36.6.1).
- Solvent-bearing LPI plugs shrink → dimples, thin knee coverage (§36.6.3.1).
- Legend over HASL flux residue loses adhesion (§36.8.3.2).
- Tin or solder resist in cupric/ferric chloride etchant is attacked (§37.2.5.1–37.2.5.2).
- Etchant residue left under traces before drying/reflow lowers insulation resistance (§37.2.5.7).
- Over-ventilating ammonia etchers drives pH < 8.0 → slow etch, dark-blue gritty sludge (§37.4.1.5).
- Chlorate-regenerated cupric bath run acid-starved, then acidified → uncontrolled Cl2 release (§37.4.2.3.2).
- Hydrogen peroxide trapped in closed piping with Cu/Ni/Fe traces can rupture explosively (§37.4.2.3.3).
- Fluoride tin strippers attack titanium and glass machine parts (§37.3.3).
- Idle sulfuric–peroxide etchers can self-heat from peroxide decomposition → equipment meltdown (§37.4.3.2).
- Persulfate baths decompose quickly near 150 °F and crystallize salts (streaks, plugged nozzles) at high copper (§37.4.4.3).
- Cuprous hydroxide (yellow) / cuprous chloride (white) residues left on copper without a 5 % HCl pre-rinse (§37.4.2.4).
- Interior lines of dense parallel groups and inside corners etch slower → width variation across a bus (§37.7.2.2).
- Fast etchants with the same R/B sensitivity cannot be tuned by conveyor speed → overetched fine lines (§37.7.3.3).
- Over-widened artwork plus over-etch fails at tight spaces where etchant stagnates (§37.7.3.4).
- A few clogged spray nozzles make the whole array non-uniform (§37.8.1.3.4).
- Thin cores (0.0015–0.003 in) jam and pile up in horizontal conveyors (§37.8.2.2.2).

## 6. Standards referenced

| standard | edition/year | clause/table | governs | source |
|---|---|---|---|---|
| IPC-2141A | 2004 | — | Design guide for high-speed controlled impedance circuit boards | §20.10 ref 7 |
| IPC-2221 | — | "PWB Design/Performance Tradeoff Checklist Considerations" chart; Table 10-1 (internal foil thickness after processing) | design tradeoffs; minimum copper thickness; superseded ampacity charts | §21.10, §22.3.6 |
| IPC-222x series | — | — | generic design standards incl. flex & MCM | §21.2 |
| IPC-2611 | — | — | documentation requirements | §21.2 |
| IPC-A-600 | — | — | acceptability of printed boards | §21.2 |
| IPC-A-610 | — | — | acceptability of assemblies | §21.2 |
| IPC-6011 | — | — | generic performance specification | §21.2 |
| IPC-6012 | — | — | qualification & performance of rigid PCBs | §21.2 |
| IPC-SM-840 | — | — | solder mask | §21.2 |
| IPC-4101 (4101B) | — | — | base materials for rigid boards; multilayer core materials for HDI | §21.2, §25.5 |
| IPC-ET-652 | — | — | electrical testing | §21.2 |
| IPC-T-50 | — | — | terms and definitions | §21.2 |
| IPC-D-356 | — | — | bare-board netlist test data format | §21.11 |
| IPC-2581 | — | — | design data exchange format | §21.11 |
| ANSI / EIA | — | — | dimensioning & tolerancing of electronic components | §21.2.3 |
| International product safety standards | — | creepage/clearance definitions | spacing for hazardous voltages ≥ 42.2 VAC / 60 VDC | §20.6.11 |
| IPC-2152 | — | baseline charts; plane-influence charts; appendix (chart history) | current carrying capacity in printed board design | §22 |
| IPC-TM-650 2.5.4.1a | — | — | conductor temperature rise due to current | §22.1, §22.3 |
| NBS Report 4283 | 1956 | — | original 1955 conductor heating data (tentative) | §22.2.1 |
| MIL-STD-275 / IPC-D-275 | — | — | carried the old NBS charts | §22.2.1 |
| IPC PCQR² database | — | — | end-process copper dimensions | §22.3.6 |
| JEDEC JESD51-2 | — | §1.1 | θ_ja natural convection test method; θ_ja not constant | §23.1, §23.9 |
| JEDEC θ_jb / θ_jc / compact models | — | — | component thermal parameters (air only) | §23.6.2, §23.7 |
| IPC-7092 | — | — | design & assembly process implementation for embedded components (150 pp.) | §24.7 |
| IPC-2315 | — | — | design guide for HDI structures and microvias | §25.2.5 |
| IPC-2226 | — | Types I–VI; categories A/B/C; Fig. 25.5 design rules | design standard for HDI structures and microvias | §25.2.5, §25.3 |
| IPC-4104 (IPC/JPCA-4104) | — | slash sheets IPC-4104/n | qualification & conformance of HDI materials | §25.2.5, §25.5 |
| IPC-6016 | — | — | qualification & performance of HDI structures | §25.2.5 |
| IPC-CF-148, IPC-MF-150, IPC-4102, IPC-4103 | — | — | material sets referenced with IPC-4104 | §25.2.5 |
| IPC-4104 slash sheets | — | /1,2,7–10,16 (photoimageable); /6,11,17,18 (non-photo nonreinforced); /12,13,19–22 (RCC); /5,23 (aramid) | HDI material data sheets | §25.5.2 |
| Telcordia (Bellcore) GR-1209 / GR-1221 | — | — | optical component reliability (85 °C/85 % RH) | §26.4.1.3 |
| IPC-2610 family: 2611, 2612, 2613, 2614, 2615, 2616, 2617, 2618 | — | — | complete electronic product documentation package | §27.2 |
| RS-274-D / RS-274-X Gerber; GenCAM; DirectCAM; ODB++ | — | — | artwork/data exchange formats | §27.3 |
| MIL-STD-105 | — | — | AQL sampling for incoming drill bits | §28.2.2.5 |
| IPC-2222 | — | Type 3, Type 4 | rigid organic board design (conventional features) | §31.2.1.2 |
| IPC-4562 (also printed "IPC-4652") | — | /2 HD Type E; /3 HTE; code R (RTF) | metal foil for printed wiring | §31.1.1, §31.3.2 |
| IPC-TM-650 | — | Table 31.1 laminate tests | test methods manual | §31.1.1 |
| IPC-9151 (PCQR²) | — | — | process capability, quality & relative reliability benchmark | §31.2.3.3 |
| IPC-4761 | — | Types I–VII; Table 5-1 application guide; fills = Type V, VII | design guide for protection of via structures | §31.2.4.3.3 |
| IPC-6012 / IPC-6010 series | — | wrap copper minimum (Class 3: 0.0005 in as printed) | rigid board performance | §31.2.4.3.3 |
| IPC-9252 | — | — | bare-board electrical test parameters | §31.3.3.2.6 |
| IPC-D-356 ("IPC-356") | — | — | electrical test netlist format | §31.3.3.2.6 |
| RoHS Directive | — | — | restriction of hazardous substances (lead-free) | §31.1, §32.4.3.2 |
| MIL-P-28809 | — | ionic cleanliness test | mil-spec board cleanliness | §32.3.3 |
| NEMA FR-4 / G-10 | — | — | laminate grades | §32.2.2 |
| MIL-STD-275 | — | nickel ≥ 0.0002 in low-stress; gold per MIL-G-45204 | printed wiring for military equipment | §33.5, §33.6.1 |
| MIL-G-45204 | — | Type I, Type II Class 1 (50–100 µin), Type III | gold electrodeposits | §33.6.1 |
| IPC-4552 | 2002; Rev A in draft | Ni 3–6 µm; Au ≥ 0.05 µm (−4σ); Rev A Au 1.6–4.0 µin + black-pad chart | ENIG | §35.4.1 |
| IPC-4553 / IPC-4553A | 2005 (obsolete) / 2009 | 0.12–0.4 µm at ±4σ | immersion silver | §35.7 |
| IPC-4554 | 2007, amended 2011 | ≥ 1.0 µm at −4σ; solderability stress/flux conditions | immersion tin | §35.8 |
| IPC-4556 | 2013 + amendment draft | Ni 3–6 µm; Pd 0.05–0.15 µm; Au ≥ 0.025 µm (max 2.8 µin in amendment) | ENEPIG | §35.5.1 |
| J-STD-003 | — | coating durability categories 1–3 (cat 3 = 12 months) | PCB solderability | §35.6 |
| WEEE directive | — | — | waste electrical & electronic equipment | §35.1.2 |
| RoHS 2002/95/EC; 2003/11/EC (24th amendment to 76/769/EEC) | 2003 | — | hazardous substances in EEE / mask formulations | §36.2.4, §36.4.3.1 |
| IPC-T-50 | — | "solder resist" definition | terms & definitions | §36.1.1 |
| IPC-SM-840 | Rev C (Class T) | two classes; Class T ≡ Telcordia GR-78-CORE | solder mask qualification & performance | §36.4.2.1 |
| UL94 | — | — | flammability (mask on specific base) | §36.4.2.2 |
| Telcordia GR-78-CORE | — | — | telecom equipment physical design (mask) | §36.4.2.3 |
| MIL-P-55110 | since mid-1990s revisions | references IPC-SM-840 | military printed boards | §36.4.2.4 |
| NASA outgassing (Goddard database) | — | TML ≤ 1.0 %, CVCM ≤ 0.10 % | space materials | §36.4.2.5 |
| JEDEC | — | package-substrate tests | semiconductor package substrates | §36.4.9 |
| ISO (quality/environmental) | — | — | supplier qualification indicator | §36.4.1 |
| IPC-4761 | July 2006 | via-protection types; protect from both sides | design guide for protection of via structures | §36.6.1 |
| IPC-4781 | draft (expected 2008) | — | legend/marking inks | §36.8.2.1 |
| CID A-A-56032D | — | — | ink, marking, epoxy base (military legend) | §36.8.2.2 |
| MIL-STD-275 | — | silver shall not be used | printed wiring for military equipment | §37.2.5.6 |
| IPC-9251 | — | — | test vehicle for process capability (linewidth) | §37.7.4.1 |
| Conductor Analysis Technologies (CAT) protocol | — | — | commercial etch/image capability gauging | §37.7.1.2, §37.7.4.1 |

## 7. Process / lifecycle guidance

| stage | activity | deliverable | exit criterion | source |
|---|---|---|---|---|
| Design start | Gather MCAD outline/keepouts, datasheets, fab capability (via/pad minimums), board thickness, layer count, copper weights, constraints | CAD setup (grids, precision, vias, constraints), stackup plan | outline imported; stackup agreed with fabricator | §21.6, §21.9 |
| Placement | Block diagram → grouped placement (analog isolated, IC+decaps grouped), BGA on pitch/2 grid, rough-in routing for channels | placed board, routing map | fixed parts locked; critical channels sized | §21.7 |
| Routing | Constraints/classes entered; pin/gate swap; fanout power first; order per COOMBS-2067; return path checked per layer | routed board | DRC = 0 (or exceptions documented) | §21.10–21.11 |
| Finishing | Resequence ref des, back-annotate, re-import netlist; silkscreen clean; fab drawing (drill table, stackup, notes reviewed by fabricator) | Gerber/ODB++/IPC-2581, IPC-D-356, P&P, fab/assy drawings, file list | fabricator confirms notes/stackup | §21.11 |
| Daily / close-out | Dated database backups; read-only master archive at completion | archive | ≥ several days retained; master frozen | §21.12 |
| Pre-layout thermal | Sum trace I²R and power density; preliminary thermal analysis before final layout | trace power budget | trace losses small vs board power; hot spots identified | §22.3.7 |
| Thermal modelling | Phase 1 airflow, Phase 2 power areas, Phase 3 detailed layout (CFD ±5 %) | component temperature report | all T_j within limits before tooling | §23.6 |
| Embedded components | Segment BOM by layer; separate formed vs placed layers; plan extended process flow (IPC-7092) | layer-segmented BOM, process flow | fabricator confirms flow | §24.6.3.5–24.6.3.6 |
| HDI technology selection | Compute connections/in²; compare to 110–130 threshold; cost parity (4L HDI ≈ 8L TH); choose IPC-2226 type and category A/B/C | HDI decision, stackup type | density achievable within chosen category | §25.1–25.3 |
| HDI process selection | Choose dielectric (clad/unclad, reinforced/RCC/PID), via formation (laser YAG/CO2/combination, photo, plasma, paste) and metallization by via count, min via size, panel size and capture-pad size | process route | throughput and registration meet design (T-25.laser) | §25.5–25.6, §26.2 |
| Via filling | Decide lamination-fill vs separate fill (hole ≤ 0.3 mm & core ≤ 0.6 mm), material (dual-cure epoxy, PID, conductive paste), planarize, cap-plate | filled/planarized cores | void-free, planar, adhesion OK | §25.5.3 |
| CAM tooling (fab) | Receive IPC-2610 package → DRC vs capability matrix → manufacturability review → single-image edits → DFM enhancements → panelization → parameter extraction (AOI, lamination, drill, plating, rout, ET) | tooling set, netlist-verified ET program | DRC dispositioned; ET netlist = IPC-D-356; parameters archived | §27.3–27.4 |
| CAM tooling (assembly) | BOM/machine-file checks: fiducial, component, padstack, testpoint, solder-paste analyses → P&P programs, stencil, ICT program, line balancing | assembly tooling | analyses pass ERF values | §27.4.2.2, §27.4.6.7 |
| Drilling prep | Select laminate-appropriate parameters (Tg/filler → surface speed; Cu layers → chip load, hit count), bits (grain, margin relief, flute length ≥ stack + 0.050 in), rings, entry/backup; AQL-inspect bits; manage repoint count | drill program & tool cassette | tool and material checks pass | §28.2 |
| Imaging | Preclean (mechanical only on cores > 0.020 in) → resist apply (hot-roll/vacuum/liquid) → expose (contact, projection, LDI/DDI) → develop (dwell 2× clear) → etch or plate → strip → AOI | imaged layer | AOI clean vs rules/CAD | §30.6–30.9 |
| Multilayer lamination | Innerlayer bake 105–110 °C ≥ 1 h → lay-up per stack-up sheet → press recipe (melt/kiss → flow → cure → controlled cool) → breakdown → thickness check → edge finish | laminated panel | thickness in spec; ΔTg ≤ 5 °C; no voids/blisters | §31.4–31.5 |
| Via fill | Pre-fill plating (wrap + button) → fill (vacuum injection preferred) → cure → planarize (eddy-current before/after) → optional cap plate | filled, planar vias | wrap ≥ spec; no voids; cap adhesion | §31.2.4.3 |
| Hole metallization | Desmear/etchback (permanganate or plasma+permanganate) → electroless Cu 20–100 µin or direct metallization → flash → image transfer | metallized holes | no voids/pull-away/ICD | §32.4–32.5 |
| New-material qualification | Build finished boards, reflow multiple lead-free cycles, blister check, cross-section high/low hole density | qual report | no delam/crack/void/pull-away | §31.5.2 |
| Electroplating (pattern plate) | Preplate (cleaner → 2 rinses → microetch → 2 rinses → 5–10 % H2SO4 predip) → acid Cu (J, t from Faraday; TP check) → tin 0.3 mil etch resist → resist strip → etch → tin strip | plated, etched panel | hole-wall Cu, T&E, no voids/nodules | §33.3.3.9, §33.4 |
| Bath maintenance | Titrate inorganics; CVS organics; TOC vs 4× baseline; carbon treat; filtration 2–4 STO/h; anode maintenance | bath logs | parameters within window | §33.3.3.7 |
| Edge-connector plating | Low-stress Ni ≥ 200 µin → hard Au 25–50 µin (commercial) / 50–100 µin (mil) → XRF/tape/porosity tests | gold fingers | thickness, adhesion, porosity, Pb < 0.1 % | §33.5–33.6 |
| Surface-finish selection | Collect fabricator/assembler/OEM requirements (shelf life > 1 yr incoming, > 2 wk mid-assembly, pitch, wire bond, contact, HF, Pb-free) → choose finish (T-35) → call out current spec revision → XRF thickness at ±4σ on 1.5×1.5 mm pads | finish callout on fab drawing | finish meets spec and assembly qualification | §35.1–35.9 |
| Solder mask qualification | Select IPC-SM-840 class (T for telecom), UL94 on actual construction, RoHS/low-halogen, outgassing if space; qualify with finish chemistry and full assembly flow (fluxes, cleaners, reflows, underfill, conformal coat) | mask qualification report | no adhesion loss, cracking, discoloration, solder balls, cleanliness failures | §36.4 |
| Solder mask application | Surface prep (strip Sn residue, pumice/chemical/oxide; DI rinse; air-knife dry) → coat (screen/spray/curtain) → debubble ≤ 5–10 min → tack dry (profiled) → expose (radiometer-verified) → develop (pH 10.6–11.3, breakpoint 10–15 %) → inspect → cure → legend | masked panel | registration, clean holes, dams retained, no lift; cure per supplier | §36.5 |
| Etching (SMOBC) | Resist strip → etch (ammonia with tin resist; cupric with organic resist) → immediate cascade rinse + acid neutralize → tin strip (fluoride or ferric/nitric) → dry | etched circuitry | no residues, undercut and slivers controlled | §37.2–37.4 |
| Etch process characterization | Run IPC-9251/CAT vehicles; cross-section at progressive etch times (R/B, U, F); set conveyor speed for R/B ≈ 1; map position/orientation variation; SPC of etch chemistry (pH/density/ORP) | etch capability report (Cp) | Cp meets customer/shop target at the design's min L/S | §37.7 |

## 8. Coverage log

- Lines 1–400 (front matter, TOC) read for orientation.
- Lines 4050–4649 read in full (Ch. 20 §20.4–20.10; Ch. 21 complete).
- Lines 4650–5249 read in full (Ch. 21 glossary; Ch. 22 complete; Ch. 23 complete; Ch. 24 complete; Ch. 25 §25.1–§25.5.1.3).
- Lines 5250–5849 read in full (Ch. 25 §25.5.2–25.9; Ch. 26 complete; Ch. 27 complete; Ch. 28 §28.1–28.2.5). Reference lists (§25.8, §26.5–26.6) skimmed only for standard names.
- Lines 5850–6449 read in full (Ch. 28 §28.2.5–28.9; Ch. 29 complete; Ch. 30 §30.1–§30.6.4.3 start). Note: §28.6 Troubleshooting is an empty heading in the text (table/figure only).
- Lines 6450–7049 read in full (Ch. 30 §30.6.4.3–30.10; Ch. 31 complete; Ch. 32 complete; Ch. 33 §33.1–33.3.3.2 start). Tables 31.1–31.4, 32.1–32.4, 33.1–33.2 are image-only in the text (not transcribable).
- Lines 7048–7347 read in full (Ch. 33 §33.3.3.2–33.6.3; Ch. 34 complete). Tables 33.3–33.7 and 34.1–34.3 are image-only in the text.
- Lines 7347–7646 read in full (Ch. 35 complete; Ch. 36 §36.1–36.5.1.1.2). Tables 35.1–35.4 (finish thickness table and process flows) are image-only; T-35 is compiled from the chapter prose.
- Lines 7646–7945 read in full (Ch. 36 §36.5.1.1.2–36.8.3.3 complete; Ch. 37 §37.1–37.4.2.4). Tables 36.1–36.4 and 37.1 and Eqs. 37.1–37.10 are image-only in the text.
- Lines 7945–8100 read in full (Ch. 37 §37.4.2.4 end through §37.8.2.2.2). The assigned range ends at the §37.8.3 "Rinsing" heading (line 8100); the rest of Ch. 37 onward belongs to the Part 3 extraction.
- Skipped per brief: reference and further-reading lists (§20.10, §22.5, §23.9, §25.8–25.9, §26.5–26.6, §29.12, §30.10, §31.9, §32.7, §34.2), acknowledgments, historical narrative (HDI origins §25.2/§26.1; NBS chart history kept only for numeric anchors), vendor product catalogs (Ch. 26 proprietary HDI processes and Ch. 34 DMT trade names condensed into summary rules).
- Extraction limitations: in the source text every figure and nearly every table/equation is an image placeholder ("Images"). Not transcribable, so only prose values were used: IPC-2152 ampacity charts (Figs. 22.6–22.10) and Tables 22.1–22.4 (IPC-2221 min copper thickness); Eqs. 20.3–20.7, 23.1–23.9, 24.1–24.2, 28.1, 33.1, 37.1–37.15; Tables 20.2, 23.1–23.2, 24.1–24.3, 25.1–25.11, 26.1–26.3, 27.1–27.3, 28.1–28.2, 29.1–29.4, 30.1–30.5, 31.1–31.4, 32.1–32.4, 33.1–33.7, 34.1–34.3, 35.1–35.4, 36.1–36.4, 37.1–37.2. Two equations were reconstructed and checked against the text's worked numbers (thermal-via resistance, COOMBS-2114; in-plane conductivity, COOMBS-2116); the etch-factor/undercut forms (COOMBS-2439) are conventional and are marked as assumptions. The surface-finish comparison T-35 is compiled from the prose, not from Table 35.1. Printed page numbers are missing from this extraction, so citations use §section/figure/table.
- Print/OCR inconsistencies are flagged [sic] and left uncorrected: "1.3-mm" support interval (§20.7.3); IPC-6012 wrap "127 µm (0.0005 in)" (§31.2.4.3.3); ENEPIG Au cap "2.8 µin (0.7 µm)" (§35.5.1); spindle TIR 0.0005 in (Ch. 28) vs 0.002 in (Ch. 29); laser focus "~200 mm/~20 mm" (µm meant); CO2 pulse "1–100 ms"; "1,250,000 rpm" spindle; DDI "20 mm L/S"; carbide grain classes; mass-lam core "0.004 in (1.0 mm)"; Faraday "1.88 ASD" (derived 1.92); "0.52 mm" for 0.020 in; "IPC-4652" for IPC-4562; the etch example's 1.5 mil top reduction vs U = 0.525 mil; ImSn pad area "2.25² µm (3600² mils)"; peel units "g/cm²", "kg/m²".
- Output: rules COOMBS-2001 to COOMBS-2445 (445 rules, IDs unique and sequential); tables T-20.25 to T-37.e; 91 mechanizable checks.
