"""Record this design's audit trail through `anvil.py log` (the same command an agent runs after each step)."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANVIL = [sys.executable, "-B", str(ROOT.parents[1] / "scripts" / "anvil.py"), "log", str(ROOT)]

research = [
    dict(kind="book", source="bowick2008", locator="rulebook BOWICK", claim="RF chain topology: DC blocks, bias tee, choke reactance", used_for="architecture", rules="BOWICK-023"),
    dict(kind="book", source="horowitz2015", locator="AOE-3330", claim="choke reactance above line impedance at all operating frequencies; DC block sized for the lowest frequency", used_for="L1/C1/C2 sizing", rules="AOE-3330"),
    dict(kind="book", source="wilson2011", locator="WILSON-394", claim="derate resistor power by at least 2x", used_for="bias resistor rating", rules="WILSON-394"),
    dict(kind="book", source="archambeault2002", locator="ARCH-065, ARCH-067", claim="fence vias <= lambda/10; MLCC ESL/ESR by dielectric and package", used_for="via fence, PDN", rules="ARCH-065;ARCH-067"),
    dict(kind="book", source="williams2016", locator="WILLIAMS-2038", claim="ground conductors shorter than lambda/20 stay below resonance", used_for="pour stitching", rules="WILLIAMS-2038"),
    dict(kind="book", source="bogatin2018", locator="BOGATIN-2110, 2132, 2135, 2147", claim="target impedance; via-pair, spreading and plane-capacitance models", used_for="+3V3 PDN", rules="BOGATIN-2110;BOGATIN-2132;BOGATIN-2135;BOGATIN-2147"),
    dict(kind="book", source="brooks2021", locator="BROOKS-017, 046, 052", claim="IPC-2152 fits, laminate conductivity, still-air HTC", used_for="trace heating, thermal model", rules="BROOKS-017;BROOKS-046;BROOKS-052"),
    dict(kind="book", source="paul2022", locator="PAUL-1024, 1044, 2011", claim="CISPR 32 Class B limits; trapezoid spectrum; loop radiation", used_for="clock emission estimate", rules="PAUL-1024;PAUL-1044;PAUL-2011"),
    dict(kind="datasheet", source="Mini-Circuits GALI-84+", locator="typical Vd/Id (to confirm)", claim="Vd 4.4 V at Id 100 mA; DC-6 GHz", used_for="bias design", rules=""),
    dict(kind="book", source="johnson2003", locator="JOHNSON03-1307, 1278", claim="an oversized connector pad over a close plane adds parasitic C; cut the plane back under the signal pad and verify in a 3-D solver or by TDR", used_for="SMA launch cut-out", rules="JOHNSON03-1307;JOHNSON03-1278"),
    dict(kind="book", source="bogatin2018", locator="BOGATIN-167, 2128, 222", claim="a real MLCC is a series R-L-C; above its self-resonance it is an inductor set by its ESL", used_for="DC-block and bypass values; EM capacitor model", rules="BOGATIN-167;BOGATIN-2128;BOGATIN-222"),
]
decisions = [
    dict(topic="RF line", decision="0.32 mm grounded coplanar, 0.3 mm pour gap, 0.2 mm prepreg to In1 GND: 49.7 ohm", alternatives="0.36 mm microstrip without pour (48.4 ohm)", rules="-", sources="tools/size_rf_line.py field solver", requirement="HR-002"),
    dict(topic="Bias", decision="12 V through 3 x 220R 2512 (73.3 ohm) + 22 nH choke; 104 mA", alternatives="2 x 150R (failed 2x derating at 13.2 V)", rules="AOE-3330;WILSON-394", sources="design/rules.tsv R-01..R-03", requirement="HR-003;HR-004"),
    dict(topic="Stackup", decision="4 layers: F.Cu RF over In1 GND, In2 +3V3 plane, B.Cu GND pour", alternatives="2 layers (no continuous RF reference at 0.2 mm)", rules="BOGATIN-2147", sources="tools/make_template.py", requirement="HR-002;HR-006"),
    dict(topic="Routing", decision="RF, clock output, fences, stitching and plane fanouts pre-routed and locked; Freerouting for the rest", alternatives="autoroute everything (planes left floating, pour fragmented)", rules="ARCH-065;WILLIAMS-2038", sources="tools/make_routes.py", requirement="HR-001;HR-002"),
    dict(topic="Edge launch", decision="SMA pads pulled back 0.3 mm; board floor 0.25 mm, 0.5 mm rule for everything else", alternatives="global 0 mm edge clearance", rules="-", sources="pcb/rffe.kicad_dru", requirement="HR-001"),
    dict(topic="RF rule frequency", decision="fence/stitching judged at 5 GHz (2nd harmonic of the 2.5 GHz band edge)", alternatives="6 GHz device limit (needs ~0.9 mm stitching grid)", rules="ARCH-065;WILLIAMS-2038", sources="design/rf.tsv", requirement="HR-002"),
    dict(topic="Track floor", decision="board minimum track 0.15 mm (fab capability); Freerouting necks the bias line to 0.15 mm at pins", alternatives="pre-route BIAS by hand", rules="BROOKS-046", sources="layout check: BIAS IPC-2152 rise on the narrowest segment", requirement="HR-009"),
    dict(topic="SMA launch", decision="In1 and In2 cut out under the J1/J2 centre pads (1.0 mm beyond each side): the 1.5 mm pad references B.Cu, 47.8 ohm field-solved", alternatives="pad over In1 at 0.2 mm (18 ohm, openEMS S11 -6.8 dB); narrower custom pad", rules="JOHNSON03-1307;JOHNSON03-1278", sources="johnson2003; openEMS rf_in; tools/make_template.py", requirement="HR-001"),
    dict(topic="DC blocks and RF bypass", decision="C1/C2/C3 10 pF C0G 0402: series-resonant near the band with the body ESL, |X| <= 3.1 ohm from 2.3 to 2.5 GHz", alternatives="100 pF (8.0-8.8 ohm inductive in band: far above its self-resonance)", rules="BOGATIN-167;BOGATIN-2128;ARCH-067;AOE-3330", sources="design/rules.tsv R-05/R-06/R-11", requirement="HR-001"),
]
iterations = [
    dict(phase="schematic", change="first wired schematic", metric="netlist_match", value="MISMATCH (1 label fallback)", checks="schematic", result="discard", files="sch/circuit.json", rules="-", note="traced to set-order nondeterminism in the generator; fixed and made byte-identical across runs"),
    dict(phase="schematic", change="regenerate after generator fix + fp-lib-table", metric="erc_violations", value="0", checks="schematic,erc", result="keep", files="pcb/rffe.kicad_sch", rules="-", note="netlist MATCH, 57 wires, 0 labels"),
    dict(phase="layout", change="first place + Freerouting", metric="drc_violations", value="137->20", checks="drc", result="discard", files="design/placement.tsv", rules="-", note="edge-launch pads, zone islands, silkscreen"),
    dict(phase="layout", change="plane fanouts + stitching grid + island removal", metric="drc_violations", value="15", checks="drc", result="keep", files="tools/make_routes.py", rules="-", note="+3V3 plane was isolated, GND pour fragmented"),
    dict(phase="layout", change="SMA pullback 0.3 mm + scoped edge rule", metric="drc_violations", value="0", checks="drc", result="keep", files="pcb/rffe.kicad_dru", rules="-", note="board floor 0.25 mm, others 0.5 mm"),
    dict(phase="layout", change="denser fence/stitching + launch vias + pre-routed clock", metric="layout_pass", value="53/58->58/58", checks="layout,drc", result="keep", files="tools/make_routes.py", rules="ARCH-065;WILLIAMS-2038", note="gap-fill pass drives worst pour-to-via distance under lambda/20 at 5 GHz"),
    dict(phase="design", change="bias 2x150R -> 3x220R", metric="rules_pass", value="9/10->10/10", checks="rules", result="keep", files="sch/circuit.json;design/rules.tsv", rules="WILSON-394", note="R-03 derating 51.6 % -> 35.2 % at 13.2 V"),
    dict(phase="thermal", change="R1 moved away from U2; 2x3 thermal vias under the GALI tab", metric="tj_U2", value="130.3->129.0 C", checks="thermal,drc", result="keep", files="design/placement.tsv;tools/make_routes.py", rules="BROOKS-017", note="limit 130 C (150 C max - 20 C); margin 1 C, thin"),
    dict(phase="verify", change="SI deck: merge line fragments shorter than the time step", metric="si_pass", value="stall->4/4", checks="si", result="keep", files="scripts/anvil_si.py", rules="-", note="ngspice 'timestep too small' on sub-ps T-line fragments; fixed in Anvil"),
    dict(phase="verify", change="openEMS: capacitors as series ESR-ESL-C, only the analysed and ground nets modelled, band-limited pulse, S-settling row", metric="em_energy_db", value="-11 (never decayed)->-50 in 28.8k steps", checks="em", result="keep", files="scripts/anvil_em.py", rules="ARCH-067;BOGATIN-167", note="16 field probes found no late field; removing the ideal 100 pF lumped C let the energy decay: an ideal C spread over the mesh rings losslessly. Fixed in Anvil"),
    dict(phase="layout", change="In1/In2 cut-out under the SMA centre pads", metric="rf_in_S11_db", value="-6.8->-15.9", checks="em,layout,drc", result="keep", files="tools/make_template.py", rules="JOHNSON03-1307", note="the first converged EM run showed the 1.5 mm SMA pad over In1 at 0.2 mm (18 ohm): S11 -6.8 dB, S21 -1.26 dB against -15/-0.6"),
    dict(phase="design", change="DC blocks and RF bypass 100 pF -> 10 pF C0G (series-resonant near 2.4 GHz)", metric="R-05_ohm", value="8.8->3.1", checks="rules,em", result="keep", files="sch/circuit.json;design/rules.tsv;design/em.tsv", rules="BOGATIN-2128;ARCH-067", note="with its ESL the 100 pF block is an 8.8 ohm inductor at 2.5 GHz (fails the Z0/10 block rule). EM then read S11 -14.95 dB: the inductive 100 pF had masked the launch port's own inductance (next row)"),
    dict(phase="verify", change="EM launch port driven across the coplanar gaps instead of a 1.5 mm tall vertical sheet to B.Cu", metric="rf_in_S11_db", value="-14.95->-17.1", checks="em", result="keep", files="scripts/anvil_em.py", rules="-", note="Zin 42+j14 ohm: the tall port added ~0.44 nH the SMA does not have. Validated on a CPW over a 1.53 mm ground: Z0 from the S-matrix within 3 % of the 2-D solver. Fixed in Anvil"),
]
for name in ("iterations", "decisions", "research"):  # rebuilt from this script, never appended twice
    (ROOT / "audit" / f"{name}.tsv").unlink(missing_ok=True)
for name, rows in (("research", research), ("decision", decisions), ("iteration", iterations)):
    for row in rows:
        run = subprocess.run(ANVIL + [name] + [f"{k}={v}" for k, v in row.items()], capture_output=True, text=True)
        if run.returncode:
            sys.exit(run.stderr)
print(f"LEDGERS: {len(research)} research, {len(decisions)} decisions, {len(iterations)} iterations")
