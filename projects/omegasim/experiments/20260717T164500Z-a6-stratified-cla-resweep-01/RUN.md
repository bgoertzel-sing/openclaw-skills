# Run 20260717T164500Z: A6 stratified CLA re-sweep 01

- Started: `2026-07-17T16:45:00Z`
- Finished: `2026-07-17T16:55:16Z`
- Status: `succeeded`
- Compute: local CPU

## Question

Do eight previously uncovered cells from the specified 120-cell A6 grid yield non-trivial frozen-CLA grammars or appraisal-specific matched-control deltas?

## Frozen design

- Cells: `(1,0,0)`, `(1,.35,3)`, `(1,.80,5)`, `(2,.15,1)`, `(2,.60,5)`, `(5,0,3)`, `(5,.15,5)`, `(5,.80,1)` as `(gain,coupling,delay)`.
- Seeds: `101,103,107`; controls: appraisal, linear, shuffled; strata: `core4` (roles4), `roles8`.
- 1,024 steps, 128 burn-in, five surrogates; frozen detector and thresholds unchanged.
- Claim boundary: exploratory proxy readouts only; the stricter held-out coding benchmark remains failed.

## Results

- 144 rows completed in 481.029 seconds; exact reconstruction held throughout.
- Every grammar again had exactly two productions and zero categories, so no
  cell met the predeclared non-trivial-grammar priority rule.
- Appraisal beat both controls on both proxy metrics in 5/6 seed/stratum rows
  at `(2,.15,1)` and `(5,.80,1)`, and 3/6 at `(1,.35,3)`. These are
  exploratory matched-control readouts, not grammar or attractor evidence.
- The other cells produced 0--2/6 joint wins. Appraisal generally beat shuffled
  controls but was inconsistent against linear controls.
- `results.json` SHA-256: `8f24f7bc832ccb38d468241310fe4a4661cf6e697667faa90243cf8d2b26d89c`.
- `results.csv` SHA-256: `1ec70eba0a9f4920f493e02c3540098dcd9b1f10575a33efa0c2d46cf3c8f892`.

## Interpretation

This completes eight of 120 grid cells (excluding the four frozen tight-region
cells from future sampling). It extends the uniform trivial-grammar negative
result into valid low/mid-gain and extreme-coupling regions. The two strong
matched-control cells are useful quantitative follow-up candidates, but they
do not satisfy the grammar-priority criterion and do not alter the failed
stricter held-out coding gate.
