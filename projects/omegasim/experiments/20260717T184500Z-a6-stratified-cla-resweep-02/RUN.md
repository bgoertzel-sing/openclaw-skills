# Run 20260717T184500Z: A6 stratified CLA re-sweep 02

- Started: `2026-07-17T18:47:15Z`
- Finished: `2026-07-17T18:56:14Z`
- Status: `succeeded`
- Compute: `local CPU`

## Question

Do eight additional uncovered A6 parameter triples yield non-trivial frozen-CLA grammars or appraisal-specific matched-control deltas across the roles4 and roles8 strata?

## Frozen design

- Triples: `(1,.15,0)`, `(1,.60,1)`, `(2,0,5)`, `(2,.35,0)`, `(2,.80,3)`, `(5,0,1)`, `(5,.15,3)`, `(5,.60,5)` as `(gain,coupling,delay)`.
- Seeds: `109,113,127`; controls: appraisal, linear, shuffled; strata: `core4` (roles4), `roles8`.
- 1,024 steps, 128 burn-in, five surrogates; frozen detector and thresholds unchanged.
- Pinned clean repositories: OmegaSim `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`; chaoslang `974af31efaf6e3cc239252f78367d20e657ac45c`.
- Claim boundary: exploratory proxy readouts only; the stricter held-out coding benchmark remains failed.

## Results

- 144 rows completed in 504.602 seconds; exact reconstruction held throughout.
- Every grammar had exactly two productions and zero categories. No row met the non-trivial-grammar priority rule.
- Joint appraisal wins over both exact controls on both proxy metrics were sparse: `1/6` seed/stratum rows at `(1,.60,1)`, `(2,.80,3)`, `(5,0,1)`, and `(5,.60,5)`; `0/6` at the other four triples.
- `results.json` SHA-256: `268d165f303150639ccc3e64b520b758ae2f4d7ee720a90ffb6c1498207716cf`.
- `results.csv` SHA-256: `5db3a2f11986b42ba45c3f77b01f54a37d8c59e50f3b83a17cd4d65633ce4af1`.
- Frozen-repository worktrees remained clean; detector tests passed; `stderr.log` is empty.

## Interpretation

This expands the stratified sweep by 16 gain/coupling/delay/roles cells. Together, batches 01 and 02 cover 32 of the 120 full-grid cells, with the separately frozen tight-region runs providing additional prior coverage. The second batch reinforces the informative negative result: the frozen proxy remains temporally responsive but does not resolve a non-trivial grammar anywhere sampled here. No detector change or grammar-driven dense follow-up is warranted from this batch.

## Artifacts

- `artifacts/results.{json,csv}`: row-level detector outputs and exact matched-control deltas.
- `artifact_sha256.json`, `env.txt`, `git.txt`, test logs, stdout, and stderr: provenance and execution ledger.
- Replay: review and run `bash command.sh`; it refuses dirty or mismatched frozen repositories before measurement.
