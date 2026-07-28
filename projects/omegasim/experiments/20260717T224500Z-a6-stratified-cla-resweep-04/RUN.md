# Run 20260717T224500Z: A6 stratified CLA re-sweep 04

- Started: `2026-07-17T22:45:00Z`
- Finished: `2026-07-17T22:54:00Z`
- Status: `succeeded`
- Compute: `local CPU`

## Question

Do eight additional uncovered A6 parameter triples yield non-trivial frozen-CLA grammars or appraisal-specific matched-control deltas across roles4 and roles8?

## Frozen design

- Triples: `(1,0,1)`, `(1,.15,5)`, `(1,.60,3)`, `(2,.15,3)`, `(2,.35,5)`, `(2,.80,0)`, `(5,0,5)`, `(5,.80,3)`.
- Seeds: `109,113,127`; controls: appraisal, linear, shuffled; strata: `core4` (roles4), `roles8`.
- 1,024 steps, 128 burn-in, five surrogates; frozen detector unchanged.
- Pinned clean repositories: OmegaSim `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`; chaoslang `974af31efaf6e3cc239252f78367d20e657ac45c`.

## Results

- 144 rows completed in 481.911 seconds; exact reconstruction held throughout.
- Every grammar had exactly two productions and zero categories. No row met the non-trivial-grammar priority rule.
- Joint matched-control wins were `6/6` at `(5,.80,3)`, `5/6` at `(2,.15,3)`, `1/6` at `(2,.80,0)` and `(5,0,5)`, and `0/6` elsewhere.
- `results.json` SHA-256: `6a26b04b5b18fa061036eba8b490870718823b2dbb5ac87fd5aab2999111b9e8`.
- `results.csv` SHA-256: `e849123227d0ab99662766dc887f7cf5c1a44bb11f854e81436887676acc53b6`.

## Interpretation

Batches 01--04 now cover 64/120 roles-specific cells. The grammar result remains uniformly trivial. The two high matched-control triples are quantitative follow-up candidates only and do not alter the failed stricter held-out coding gate or support an attractor claim.

## Reproduction

Review and run `command.sh`; it refuses dirty or mismatched frozen repositories before measurement.
