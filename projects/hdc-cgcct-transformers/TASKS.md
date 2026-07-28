# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [ ] **P1A full-grid calibration execution:** the complete metrics/calibration
  pipeline is implemented at nested commit `e4e1d65`. Its reduced two-replay
  smoke passed 18 tests and produced byte-identical payloads (SHA-256
  `dba950b8...c5bb`), while correctly remaining gate-ineligible. Next: run the
  frozen three-seed, 2,048-trial full grid without changing criteria. Evidence:
  `experiments/20260727T235800Z-p1a-metrics-smoke/RUN.md`.

- [x] **P1A fixture preflight (2026-07-27):** implemented deterministic F0
  independent, F1 coherent, F2 correlated-noise, and F3 planted-distance
  constructors.  A 256-trial non-gating preflight produced 30 cells and six
  F3 rows deterministically; 16 tests passed.  Evidence:
  `experiments/20260727T214823Z-p1a-fixture-preflight-r2/RUN.md`; commit
  `8ff1e35`. Next: full-grid metrics and calibration-only execution.

- [ ] **Conditionally approved P1B GPU calibration (2026-07-27):** after a
  passing local CPU smoke, run exactly the three calibration seeds on one
  compatible 24 GiB GPU under a 4-hour / USD 10 hard cap, then freeze the
  criteria artifact before confirmation. No pod is provisioned yet. Acceptance:
  smoke hash and remote-job preconditions pass; artifacts return and verify;
  provider resource is terminated. Plan:
  `experiments/20260727T225600Z-p1b-gpu-calibration-planned/REMOTE_JOB.md`.

- [x] **Authorized P0-v2 fixture/grid amendment (2026-07-27):** retained the
  P0-G1 gate and deterministic conventions, changed only the grid to
  `D={32,64,128,256,512,1024}`, `k={32,64,128}`, `M={32,256}`, and ran two
  2,048-trial payloads. Tests passed 13/13; both payloads hash to
  `96f3a7142111828cffa458a59ac35699c6ce0077748a14361063ecc4b4dd14f7`; every
  curve Spearman is 1.0 and P0-G1 passed. Evidence:
  `experiments/20260727T213214Z-p0-g1-v2-authorized-grid/RUN.md`; runner
  commit `ce7616d`.

- [ ] Persistent local P0/P1 worker: resume the interrupted P0-G1 replay,
  then progress through the recorded CPU-only P1 tasks with reproducible
  artifacts and fail-closed gates. Acceptance: each tick either leaves a
  verified artifact/test result or records its concrete blocker. It must not
  provision remote compute. Scheduler lane: `HDC CGCCT transformers progress
  worker`.
- [x] Complete and interpret P0-G1 independent-cleanup replay (failed closed, 2026-07-27). The P0 algebra/artifact
  implementation is committed at `repos/hdc-cgcct-probes/` commit `fa11721`; exact tests
  pass 13/13 and replay A exists. Acceptance: a fresh `p0-selftest-v2` execution writes
  identical `capacity-replay-a.json` and `capacity-replay-b.json`, writes a passing
  `p0-g1.json`, and its `RUN.md` records the outcome. Next command:
  `cd projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes && bash scripts/run_p0_gate.sh ../../artifacts/p0-selftest-v2`.
  Evidence path: `experiments/20260726T184741Z-p0-selftest-v2/` and
  `artifacts/p0-selftest-v2/`. The fresh replays are bit-identical, but the
  frozen gate is false because the `k=4,M=32` accuracy curve is saturated and
  has Spearman `0.0`; P1 is blocked pending an explicitly authorized P0
  fixture/grid or gate revision.

## Next

- [ ] Implement P1A independent/coherent/pathology/hierarchy-distance fixtures
  and run local preflight only.
- [ ] Implement the P1B planted-PCFG next-token fixture and six-layer
  transformer without reusing the causal-fibres classifier as scientific
  evidence.
- [ ] Freeze P1 criteria after three calibration seeds; do not open the five
  confirmation seeds before the criteria artifact exists.

## Waiting or blocked

- [x] P1A/P1B implementation and preflight was blocked by P0-G1 v1: the frozen
  `k=4,M=32` curve is saturated at accuracy 1.000 over all tested dimensions,
  yielding Spearman 0.0 instead of the required positive association. Owner:
  Benjamin Goertzel; recorded 2026-07-27 and reconfirmed by a clean local replay
  at `experiments/20260727T1158Z-p0-g1-replay-confirmation/` and the scheduled
  worker at `experiments/20260727T1558Z-p0-g1-replay-worker/`, then once more
  at `experiments/20260727T195800Z-p0-g1-replay-worker/` (same two payload
  hashes and validator hash). No P1 work may start under Section 8 until an
  explicitly authorized P0 revision is made and independently run. Benjamin
  authorized the v2 grid and P0-G1 passed on 2026-07-27; P1A now moves to
  `Next`.

## Someday or exploratory

- [ ]

## Done recently

Move durable conclusions into `PROJECT.md`, `DECISIONS.md`, or experiment results rather than relying on this list.

- [x] Created the source-grounded P0/P1 execution specification and theorem-
  assumption audit (2026-07-26). Acceptance met: explicit formulas, fixtures,
  deterministic conventions, gates, raw-artifact schemas, exact planned
  commands, source/conjecture table, and reusable-infrastructure disposition
  are in `docs/p0-p1-spec.md`. The source bundle is hashed at
  `../../library/hdc-cgcct-source-manuscripts-2026/SOURCE.md`; the reusable
  causal-fibres seam passed `11` focused CPU tests.
- [x] Created project notebook and assigned persistent research subagent (2026-07-26).
- [x] Implemented deterministic CPU P0 HDC algebra and fixtures (2026-07-26).
  Evidence: local commit `fa11721` on `agent/p0-core`; 13/13 exact tests.
