# Run 20260718T064500Z: A6 stratified CLA re-sweep batch 09

- Started: `2026-07-18T06:45:00Z`
- Finished: `2026-07-18T06:56:38Z`
- Status: `succeeded`
- Compute: `local CPU`

## Question

Do the eight remaining non-tight A6 parameter triples yield non-trivial frozen-CLA grammars or appraisal-specific matched-control deltas across roles4 and roles8?

## Frozen design

- Triples: `(1,.15,1)`, `(1,.35,0)`, `(1,.60,5)`, `(2,0,1)`, `(2,.35,1)`, `(2,.60,0)`, `(2,.80,1)`, `(5,.35,5)`.
- Seeds: `109,113,127`; controls: appraisal, linear, shuffled; strata: `core4` (roles4), `roles8`.
- 1,024 steps, 128 burn-in, five surrogates; unchanged frozen CLA implementation and identity gates.
- Pinned clean repositories: OmegaSim `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`; chaoslang `974af31efaf6e3cc239252f78367d20e657ac45c`.

## Results

- Completed 144 rows in 545.434 seconds; all reconstructed exactly; eight focused tests passed.
- Every grammar had exactly two productions and zero categories. No row met the non-trivial-grammar priority rule.
- Appraisal beat both exact controls on both proxy metrics in `4/6` seed/stratum rows at `(2,.60,0)`, `3/6` at `(1,.35,0)`, `2/6` at `(5,.35,5)`, and `1/6` at `(1,.15,1)`; the other four triples had `0/6` joint wins.
- Results JSON SHA-256: `8619fdc38e24f0abf57a77abdedebe3879c2f7cc65d2cfd44883b0e68ab1c59d`.
- Results CSV SHA-256: `555b27bda94bef2000ed722af955522e8d96b48c675c3e127ebcbeff6a1385b5`.
- `stderr.log` was empty and both frozen worktrees remained clean.

## Interpretation

The stratified series now covers all 112 cells outside the four tight parameter triples. With the four separately frozen tight-region roles8 cells, coverage is 116/120 planned roles-specific cells; only the four corresponding roles4 cells remain. Across all nine successful batches, every grammar remained trivial. This expanding negative result is not yet the full-grid closure. The quantitative matched-control wins do not meet the grammar-priority rule, rescue the failed stricter held-out coding benchmark, or support a chaos, attractor, or semantic-grammar claim. No detector change was made.

## Reproduction

Review and run `command.sh`; it refuses dirty or mismatched frozen repositories before measurement.
