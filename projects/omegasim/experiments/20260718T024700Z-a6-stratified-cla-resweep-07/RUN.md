# Run 20260718T024700Z: A6 stratified CLA re-sweep 07

- Started: `2026-07-18T02:46:58Z`
- Finished: `2026-07-18T02:55:38Z`
- Status: `succeeded`
- Compute: `local CPU`

## Question

Do eight additional uncovered A6 parameter triples yield non-trivial frozen-CLA grammars or appraisal-specific matched-control deltas across roles4 and roles8?

## Frozen design and provenance

- Triples: `(1,.35,5)`, `(1,.80,1)`, `(2,0,0)`, `(2,.15,5)`, `(2,.60,3)`, `(5,0,0)`, `(5,.15,1)`, `(5,.80,0)`.
- Seeds: `109,113,127`; controls: appraisal, linear, shuffled; strata: `core4` (roles4), `roles8`.
- 1,024 steps, 128 burn-in, five surrogates; frozen detector unchanged.
- Pinned clean repositories: OmegaSim `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`; chaoslang `974af31efaf6e3cc239252f78367d20e657ac45c`.
- The closed batch-05 preflight supplied the prepared design. Batch 06 failed before simulation due only to dynamic-module multiprocessing registration. Batch 07 registered that unchanged module and used a new ledger.

## Results

- 144 rows completed in 519.994 seconds; all rows reconstructed exactly; eight focused tests passed.
- Every grammar had exactly two productions and zero categories. No row met the non-trivial-grammar priority rule.
- Joint matched-control wins were `4/6` at `(1,.35,5)` and `(2,.15,5)`, `2/6` at `(5,.80,0)`, `1/6` at `(5,0,0)`, and `0/6` elsewhere.
- `results.json` SHA-256: `7d10a63dec8d86f675693eb5e18d0424a2a0ed55a89beaa103af6561797b1bf5`.
- `results.csv` SHA-256: `5e57dca6f058ed9be81248a2517ec9a5c4290bb8c23232005566cbe04cfc2c38`.

## Interpretation

Batches 01--04 plus this successful batch cover 80/120 roles-specific cells. Grammar structure remains uniformly trivial. The two 4/6 triples are quantitative follow-up candidates only and do not meet the grammar-priority rule, rescue the failed stricter held-out coding benchmark, or support an attractor claim.

## Reproduction

Review and run `command.sh`; it refuses dirty or mismatched frozen repositories before measurement.
