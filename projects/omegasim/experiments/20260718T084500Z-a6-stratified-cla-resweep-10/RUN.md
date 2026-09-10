# Run 20260718T084500Z: A6 stratified CLA re-sweep batch 10

- Started: `2026-07-18T08:45:00Z`
- Finished: `2026-07-18T08:49:15Z`
- Status: `succeeded; full planned grid closed`
- Compute: `local CPU`

## Question

Do the four remaining tight-region roles4 cells yield non-trivial frozen-CLA grammars or appraisal-specific matched-control deltas?

## Frozen design

- Cells: gain `5.0`, coupling `{0.35,0.60}`, delay `{0,3}`, stratum `core4` (roles4).
- Seeds: `109,113,127`; controls: appraisal, linear, shuffled.
- 1,024 steps, 128 burn-in, five surrogates; unchanged frozen CLA implementation and identity gates.
- Pinned clean repositories: OmegaSim `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`; chaoslang `974af31efaf6e3cc239252f78367d20e657ac45c`.

## Results

- Completed 36 rows in 129.421 seconds; all reconstructed exactly; eight focused tests passed.
- Every grammar had exactly two productions and zero categories. No row met the non-trivial-grammar priority rule.
- Appraisal beat both exact controls on both proxy metrics in `2/3` seeds at `(5,.60,3)` and `0/3` at the other three cells.
- Results JSON SHA-256: `52898641fd722a71ed834309d218d890fd841cb6b7cf85ff83f16958dd94fd8c`.
- Results CSV SHA-256: `92ce3d7602712ddc6a54e737775080339fe46f707b688cff1a513090dcd73cf7`.
- `stderr.log` was empty and both frozen worktrees remained clean.

## Interpretation

This closes all 120 planned roles-specific A6 grid cells when combined with batches 01--09 and the separately frozen tight-region roles8 evidence. Every grammar in the stratified sweep remained trivial. The full-grid result is therefore an informative negative for non-trivial frozen-CLA grammar under this design, not evidence that the dynamics are simple in general. Quantitative proxy wins do not rescue the failed stricter held-out coding benchmark or support chaos, attractor, or semantic-grammar claims. No detector change was made.

## Reproduction

Review and run `bash command.sh`; it refuses dirty or mismatched frozen repositories before measurement.
