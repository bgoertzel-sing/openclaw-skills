# Run 20260718T044500Z: A6 stratified CLA re-sweep batch 08

- Started: `2026-07-18T04:45:00Z`
- Finished: `2026-07-18T04:54:26Z`
- Status: `succeeded`
- Local or remote: `local CPU`

## Question

Do eight additional uncovered A6 parameter triples yield non-trivial frozen-CLA grammars or appraisal-specific matched-control deltas across roles4 and roles8?

## Frozen design

- Triples: `(1,0,3)`, `(1,.60,0)`, `(1,.80,3)`, `(2,.15,0)`, `(2,.35,3)`, `(2,.80,5)`, `(5,.35,1)`, `(5,.60,1)`.
- Seeds: `109,113,127`; controls: appraisal, linear, shuffled; strata: `core4` (roles4), `roles8`.
- 1,024 steps, 128 burn-in, five surrogates; unchanged frozen CLA implementation and identity gates.

## Results

- Completed 144 rows in 514.383 seconds; all reconstructed exactly.
- Every grammar had exactly two productions and zero categories. There were no priority rows under the predeclared `>2 productions or >0 categories` rule.
- Appraisal beat both exact controls on both proxy metrics in `6/6` seed/stratum rows at `(2,.15,0)`, `3/6` at `(5,.35,1)`, and `2/6` at `(2,.80,5)`; the other five triples had `0/6` joint wins.
- Results JSON SHA-256: `b20b7ec1282bb1988f5aaefb025ed71bf359a510f2a8aadf475744a575e066da`.
- Results CSV SHA-256: `2f515dd6cfe26418c390ebde1adbe733edaa5ffe308d0a1329637db4fc505cb2`.
- `stderr.log` was empty; both pinned worktrees remained clean; `git diff --check` passed.

## Interpretation

Successful batches now cover 96/120 roles-specific cells. The grammar result remains uniformly trivial. `(2,.15,0)` is a quantitative matched-control follow-up candidate only: it does not meet the grammar-priority rule, rescue the failed stricter held-out coding benchmark, or support a chaos/attractor/semantic-grammar claim. No detector change was made.
