# Circuit simulation

Choose simulations from requirement claims, operating corners and model validity. Use vendor
models with source/license/version recorded; pin every model and include in the release manifest.
Compare a known operating point/reference circuit before trusting an imported model. State
unsupported effects such as layout parasitics, thermal behavior or firmware interactions.

`sim/assertions.tsv` requires `id, measure, op, limit, units, corners, traces, circuit` as tab
columns. Each unique row names its exact relative circuit path. No global measurement-name
pooling or inferred association with another harness is allowed.

```text
id	measure	op	limit	units	corners	traces	circuit
A-1	vout_avg	within	3.3±3%	V	vin=4.5,5.5;iload=0,1	HR-1	buck.cir
```

In `buck.cir`, declare each swept parameter exactly once on its own line, for example
`.param vin=5` and `.param iload=0.5`, after the SPICE title. Corner values are finite decimal
or scientific-notation numbers in base units, not SPICE suffix abbreviations. Semicolon joins
parameters and comma lists values; Anvil executes the Cartesian product, up to 256 variants
per assertion. Use `nominal` for an intentionally single-condition assertion. Name non-nominal
model/temperature/load assumptions explicitly in the requirements and harness.

`sim <directory>` materializes a fresh circuit variant for each corner in a temporary directory
under the original circuit directory, invokes ngspice there with the original working directory,
checks exit status, and reads that run's log only. Relative includes keep their original meaning.
Each measurement must appear exactly once and be finite. Missing tools, missing/ambiguous
measures, malformed assertions, a failed run or unsupported corner declaration are errors.
An old `*.log` cannot satisfy a measurement. `SKIP_NGSPICE` is rejected.
The runner disables `.spiceinit` and follows included model dependencies, including files outside
the sim folder. Ambiguous relative include locations are conservatively both hashed; prefer
unambiguous paths. `.control` scripts require a separately reviewed runner; built-in assertions
use batch `.measure` so hidden interactive commands cannot change the execution contract.

One assertion passes only when all corners pass. The units column is a declared contract:
ngspice returns scalar values, so engineering review must confirm the expression's physical
units and sign. Anvil does not infer dimensional correctness from the measure name.
`within` uses the magnitude of the center for percent tolerance, including negative centers.
The transcript records each corner, observed value, margin and disposition. Gate recordings
also bind the assertions, circuits and local model dependencies to the release hashes.

`sim/plots.tsv` (`id, circuit, corners, vectors, x, title, traces`) re-runs each corner with a rawfile and
plots the named vectors (`v(out),i(l1)`) over `x` into `audit/plots/<id>.png`; `plots <project>` also
charts every recorded assertion margin. Plot what each requirement claims (startup, ripple, transient,
Bode) and look at the result before citing it.

Review convergence warnings, model applicability, startup and steady-state windows, sampling,
operating limits and fault behavior. Simulation is evidence for its modeled claim; it does not
replace physical EMC, environmental, safety, RF or production qualification tests.
