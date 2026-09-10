# Run 20260717T204500Z: A6 stratified CLA re-sweep 03

- Started: `2026-07-17T20:46:06Z`
- Finished: `2026-07-17T20:54:21Z`
- Status: `succeeded`
- Compute: `local CPU`

## Question

Do eight additional uncovered A6 parameter triples yield non-trivial frozen-CLA grammars or appraisal-specific matched-control deltas across the roles4 and roles8 strata?

## Frozen design

- Triples: `(1,0,5)`, `(1,.15,3)`, `(1,.35,1)`, `(1,.80,0)`, `(2,0,3)`, `(2,.60,1)`, `(5,.15,0)`, `(5,.80,5)` as `(gain,coupling,delay)`.
- Seeds: `109,113,127`; controls: appraisal, linear, shuffled; strata: `core4` (roles4), `roles8`.
- 1,024 steps, 128 burn-in, five surrogates; frozen detector and thresholds unchanged.
- Pinned clean repositories: OmegaSim `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`; chaoslang `974af31efaf6e3cc239252f78367d20e657ac45c`.
- Claim boundary: exploratory proxy readouts only; the stricter held-out coding benchmark remains failed.

## Results

- 144 rows completed in 494.759 seconds; exact reconstruction held throughout.
- Every grammar had one or two productions and zero categories. No row met the non-trivial-grammar priority rule (`productions > 2` or `categories > 0`).
- Appraisal beat both exact controls on both proxy metrics in `4/6` seed/stratum rows at `(1,.35,1)` and `(2,.60,1)`, and `1/6` at `(1,.15,3)`; the other five triples had `0/6` joint wins.
- `results.json` SHA-256: `0eeeedb4eae03806f5c7136e7a5b960d964ccbea9decf0bf7e74a63c25596a28`.
- `results.csv` SHA-256: `9e08984a26bc37043c534d6de84c78d301261cca72cbb8c057ca1523fa8a326b`.
- Frozen-repository worktrees remained clean; detector tests passed; `stderr.log` is empty.

## Interpretation

Batches 01--03 now cover 48 of the 120 roles-specific grid cells. This batch extends the informative negative grammar result: the frozen proxy found no non-trivial grammar in another diverse stratum. The two 4/6 triples are quantitative follow-up candidates only; they do not pass the grammar-priority rule and do not alter the failed stricter coding gate.

## Artifacts

- `artifacts/results.{json,csv}`: row-level detector outputs and exact matched-control deltas.
- `artifact_sha256.json`, `env.txt`, `git.txt`, test logs, stdout, and stderr: provenance and execution ledger.
- Replay: review and run `bash command.sh`; it refuses dirty or mismatched frozen repositories before measurement.
