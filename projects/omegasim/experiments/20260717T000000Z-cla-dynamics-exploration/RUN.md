# Run 20260717T000000Z-cla-dynamics-exploration: CLA dynamics exploration

- Project: `omegasim`
- Started: `2026-07-17T00:21:38Z`
- Finished: `2026-07-17T00:46:42Z`
- Status: `succeeded after recorded experiment-wrapper recovery`
- Local or remote: `local` (no paid compute)
- Working directory: `/home/openclaw/research-agent/projects/omegasim/repos/omegasim`

## Question

What observed CLA detector fingerprints occur across the known A6 matched-excess
region and a small balanced sample of broader A6 configurations?

## Claim boundary

All outputs are **observed detector readouts**, not validated attractor
structure. The stricter held-out CLA coding benchmark failed, so claims of
chaos, strange attractors, or semantic grammar remain gated.

## Frozen design (recorded before execution)

- Tight sweep: gain `5.0`; coupling `{0.35,0.60}`; delay `{0,3,7}`; strata
  `core4,roles8,full20`; seeds `101,103,107,109,113`; controls
  `appraisal,linear,shuffled`; 1,024 steps; 128 burn-in; five surrogates.
- Broad characterization: balanced 12-point design spanning gain `{3,5,7}`,
  coupling `{0.15,0.35,0.60,0.80}`, and delay `{0,3,7,14}`, with seeds
  `{101,113}` and all three controls/strata. This is not the 48-point Cartesian
  product and is not a confirmatory sample.
- Frozen detector: exact reconstruction, occupancy at least four, compression
  margin greater than zero, and held-out advantage at least 0.10 bits/symbol.
- Qualitative clusters reuse those frozen thresholds; no outcome-dependent
  threshold tuning is permitted.

## Inputs and provenance

- OmegaSim branch `agent/cla-detector-prereg`, commit
  `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`, clean before run.
- chaoslang source from isolated detached worktree at commit
  `974af31efaf6e3cc239252f78367d20e657ac45c`, clean before run. The shared
  `agent/hd-embedding-cla` checkout was left untouched.
- `scripts/run_cla_detector.py` SHA-256:
  `29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c`.
- `scripts/run_a6_sweep.py` SHA-256:
  `02b46d161241ea28e30f0e516ea5710f2f87e5da8f700289af1c9db994fb9c0e`.
- Exact top-level command: `command.sh`.
- Per-step commands, exit statuses, and elapsed times: `steps_status.json`.
- Sanitized environment: `env.txt`.
- Repository state: `git.txt`.
- Relevant research rules: 1, 2, 3, 5, and 7.

## Results

- Attempt 1 exit status: `1`. All six tight shards completed, then the broad
  phase failed before measurement with `ModuleNotFoundError: scripts` in its
  experiment-local multiprocessing wrapper. See `attempt-1-error.log`.
- Recovery changed only the wrapper's worker import path and validates/reuses
  the completed tight artifacts; the frozen detector, thresholds, seeds,
  configurations, and controls are unchanged.
- Recovery/final exit status: `0`.
- Unit tests: 8 passed in 0.124 seconds. Broad measured phase: 72 simulation /
  control tasks, 216 detector rows, exit `0`, 911.686 seconds.
- Total: 486 rows (270 tight, 216 broad). Exact reconstruction held in 486/486;
  all rows occupied all eight microstates.
- Every grammar had exactly two productions and zero categories. Thus the
  readouts do not expose varying or nontrivial category structure despite
  positive compression/prediction metrics.
- Frozen row-positive counts:
  - tight appraisal 90/90; tight linear 90/90; tight shuffled 55/90;
  - broad appraisal 72/72; broad linear 72/72; broad shuffled 36/72.
- Tight matched promotions (appraisal positive and strictly better than both
  exact-tuple controls on compression margin and held-out loss in at least four
  of five seeds):
  - coupling `0.35`, delay `7`, `core4`: 5/5 seed wins;
  - coupling `0.35`, delay `7`, `roles8`: 4/5;
  - coupling `0.60`, delay `3`, `roles8`: 4/5;
  - coupling `0.60`, delay `3`, `full20`: 5/5.
- No `coupling=0.60, delay=7` stratum had a matched seed win. Other tight
  nonpromoted cells ranged from zero to three wins.
- Across all tight strata/seeds, appraisal minus linear averaged `-8.547`
  compression-proxy bits but `+0.122` bits/symbol held-out advantage. Appraisal
  minus shuffled averaged `+155.318` compression-proxy bits and `+2.075`
  bits/symbol held-out advantage. Broad appraisal minus linear averaged
  `-13.950` and `-0.026`, respectively; appraisal minus shuffled averaged
  `+163.683` and `+1.760`.
- All 72 broad appraisal rows landed in the predeclared
  `compression_and_predictive` cluster. The weakest sampled appraisal tuple was
  gain `5`, coupling `0.15`, delay `14` (mean compression margin `107.5`, mean
  held-out advantage `0.867` across strata/seeds; its core4 rows were lowest at
  margins `7.8` and `32.2`). No sampled appraisal tuple was flat/collapsed.
- Machine-readable artifacts and SHA-256 checks are in `artifacts/` and
  `artifact_sha256.json`; all ten manifest checks passed after completion.

### Concurrent replay provenance repair

A second cron invocation started at `2026-07-17T00:46:41Z` before this first
completion was visible to that invocation. It passed the same clean pins and
eight tests, reused the six tight shards, and recomputed the 72 broad tasks in
`826.267` seconds, finishing at `2026-07-17T01:00:28Z`. This unintentionally
overwrote the top-level broad/combined artifacts and `steps_status.json`.

The replay preserved all reported counts, promotions, qualitative conclusions,
and the aggregate JSON byte-for-byte (`3cdc05f1...`). Row-level hashes changed
because broad tasks are collected with `as_completed`, so output row ordering
depends on worker completion order. This is an experiment-wrapper provenance
defect, not a detector change or independent replication. The original
row-level files are no longer present; their recorded hashes below are retained
as historical provenance. Current replay hashes are captured in
`artifact_sha256.json` and `PROVENANCE_ADDENDUM.md`. Future measured runs must
use an exclusive new ledger directory and deterministically sort collected
rows before hashing.

Original-completion primary artifact hashes (recorded before overwrite):

- `all_fingerprints.json`: `78a175ee37ac46c0b7a7883f22cfcc788b18b45b5f94f2baeed7345af7b2d87f`
- `all_fingerprints.csv`: `5cfac7b7ddbd463ecc8a74d0effe335c8ddbf2327b40593d0aa414a63e928bcc`
- `appraisal_control_deltas.json`: `ecc79b608cefe6b7e23aaebbd1095bedadd1cbb27b72ac5d47b6760ce10e2e12`
- `fingerprint_aggregates.json`: `3cdc05f12771898aa7f80e03712329bbfdb3ccf1cf7d5d40f7053b6cc81fa4ca`

## Interpretation

**Observed detector readouts:** Appraisal and linear dynamics both produce
ubiquitous positive compression/prediction readouts. Shuffling temporal order
weakens these metrics substantially. Four tight appraisal cells also exceed
both matched controls reproducibly, centered on delay `7` at coupling `0.35`
and delay `3` at coupling `0.60`.

**Qualitative fingerprint types:**

1. `Appraisal matched-control dominant`: the four promoted tight cells above.
2. `Temporally structured but control-comparable`: all other appraisal cells;
   they have strong positive absolute readouts but usually do not beat the
   linear control consistently.
3. `Order-disrupted`: shuffled controls, split among 91/162
   compression-and-predictive, 53/162 compression-only, 15/162 weak, and 3/162
   predictive-only rows across both sweeps.

**Inference:** The sweep detects temporal-order structure, but it does not
resolve qualitatively different grammatical regimes: occupancy is saturated,
and production/category counts are identical everywhere. Compression margin
and held-out advantage distinguish appraisal from shuffled traces much more
readily than from linear controls. The broad sample therefore suggests a
quantitative continuum, not validated distinct attractor classes.

**Claim boundary:** These are observed detector readouts, not validated
attractor structure, chaos, or semantic grammar. The failed stricter held-out
CLA coding benchmark remains a hard gate on stronger claims. The broad sample
uses only two seeds and a balanced 12-point design, so it cannot support
full-factorial or confirmatory conclusions.

## Artifacts

- `artifacts/all_fingerprints.{json,csv}`: all 486 row-level readouts,
  qualitative labels, deltas, and aggregates.
- `artifacts/tight_fingerprints.{json,csv}`: 270 tight rows and frozen matched
  promotions.
- `artifacts/broad_fingerprints.{json,csv}`: 216 broad rows and exact sampled
  design.
- `artifacts/appraisal_control_deltas.{json,csv}`: exact-tuple appraisal-minus-
  linear/shuffled deltas.
- `artifacts/fingerprint_aggregates.{json,csv}`: configuration/control/stratum
  seed aggregates and cluster counts.
- `artifacts/tight-shards/`: official detector shard JSON/CSV and logs.
- `steps_status.json`, `attempt-1-error.log`, `tests.stderr.log`, `env.txt`,
  `git.txt`, and `artifact_sha256.json`: execution and provenance ledger.

## Reproduction

Review and run `command.sh`. It verifies both commit pins and clean worktrees
before tests or measurements.

## Follow-up

Do not tune the frozen detector from this outcome. The immediate scientific
limitation is its uniform two-production/zero-category grammar and pervasive
linear-control positivity; any richer category/miner work belongs to the CLA
lane and must be separately frozen and calibrated before another OmegaSim
attractor/grammar claim.
