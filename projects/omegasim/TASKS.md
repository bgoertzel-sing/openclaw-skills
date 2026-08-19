# Tasks

## Now

- [x] 2026-08-19: Cron closure audit re-confirmed no unexplored stratum
  remaining. The 120/120 roles-specific grid was closed on 2026-07-18 and
  audited on 2026-07-31. No new commits or experiment directories since
  20260718T084500Z-a6-stratified-cla-resweep-10. No duplicate simulation
  launched. Further measurement requires a new preregistered grid or
  explicitly authorized denser follow-up.
- [x] 2026-07-31: Cron closure audit confirmed that the requested stratified
  A6 re-sweep has no unexplored stratum remaining. Batch 10 closed all 120/120
  roles-specific cells on 2026-07-18, with every frozen-CLA grammar trivial.
  No duplicate simulation was launched; further measurement requires a new
  preregistered grid or explicitly authorized denser follow-up.

- [x] 2026-07-18: Completed the four remaining tight-region roles4 cells with
  three seeds and exact controls, closing all 120 planned roles-specific A6
  grid cells. All 36 new grammars were trivial (two productions, zero
  categories), establishing the predeclared informative negative result for
  the full frozen-CLA stratified sweep. See
  `experiments/20260718T084500Z-a6-stratified-cla-resweep-10/RUN.md`.

- [x] 2026-07-17: Completed stratified frozen-CLA grid batch 09 over the eight
  remaining non-tight parameter triples (16 roles-specific cells), three seeds,
  and matched controls. All 144 grammars were trivial (two productions, zero
  categories). Together with the separately frozen tight roles8 cells, the
  planned grid now has 116/120-cell evidence; the four tight roles4 cells
  remain before the informative negative grammar result can close. See
  `experiments/20260718T064500Z-a6-stratified-cla-resweep-09/RUN.md`.

- [x] 2026-07-17: Completed stratified frozen-CLA grid batch 08 over eight
  additional parameter triples (16 roles-specific cells), three seeds, and
  matched controls. All 144 grammars were trivial (two productions, zero
  categories); `(2,.15,0)` reached an exploratory 6/6 joint matched-control
  result. Successful batch coverage is now 96/120 cells. See
  `experiments/20260718T044500Z-a6-stratified-cla-resweep-08/RUN.md`.

- [x] 2026-07-17: Completed successful stratified frozen-CLA grid batch 07
  over eight additional parameter triples (16 roles-specific cells), three
  seeds, and matched controls. All 144 grammars were trivial (two productions,
  zero categories); two triples reached exploratory 4/6 joint matched-control
  wins. Successful batch coverage is now 80/120 cells. See
  `experiments/20260718T024700Z-a6-stratified-cla-resweep-07/RUN.md`.

- [x] 2026-07-17: Completed stratified frozen-CLA grid batch 04 over eight
  additional parameter triples (16 roles-specific cells), three seeds, and
  matched controls. All 144 grammars were trivial (two productions, zero
  categories); `(5,.80,3)` reached 6/6 and `(2,.15,3)` reached 5/6 exploratory
  joint matched-control wins. See `experiments/20260717T224500Z-a6-stratified-cla-resweep-04/RUN.md`.

- [x] 2026-07-17: Completed stratified frozen-CLA grid batch 03 over eight
  additional parameter triples (16 roles-specific cells), three seeds, and
  matched controls. All 144 grammars were trivial (one or two productions,
  zero categories); two triples reached exploratory 4/6 joint matched-control
  wins. See `experiments/20260717T204500Z-a6-stratified-cla-resweep-03/RUN.md`.

- [x] 2026-07-17: Completed stratified frozen-CLA grid batch 02 over eight
  additional parameter triples (16 roles-specific grid cells), three seeds,
  and matched controls. All 144 grammars again had two productions and zero
  categories; joint matched-control wins were at most 1/6 per triple. See
  `experiments/20260717T184500Z-a6-stratified-cla-resweep-02/RUN.md`.

- [x] 2026-07-17: Completed stratified frozen-CLA grid batch 01 over eight
  previously uncovered A6 cells with three seeds, three controls, and roles4 /
  roles8 readouts. All 144 grammars had two productions and zero categories;
  `(gain,coupling,delay)=(2,.15,1)` and `(5,.80,1)` had exploratory joint
  matched-control wins in 5/6 seed/stratum rows. See
  `experiments/20260717T164500Z-a6-stratified-cla-resweep-01/RUN.md`.

- [x] 2026-07-16: Created interim isolated cron worker `f2347407-4c15-42c7-8587-a9f63f939a59`, scheduled every two hours at minute 45 of odd hours (`America/Vancouver`). It advances pinned-detector untouched-seed replication and is intended to migrate to a task-specific ThreadKeeper persistent agent once that runtime is ready.

- [x] Restart OmegaSim under the frozen 2026-07-15 CLA preregistration. One of 12 cells promoted: coupling `0.60`, delay `3`, `roles8`, four of five matched-seed wins. See `experiments/20260715T153049Z-cla-detector-preregistered/RUN.md`.
- [x] Replicate the promoted `coupling=0.60`, `delay=3`, `roles8` cell on untouched seeds without changing the detector or thresholds. The repaired pinned run met the confirmatory proxy criterion at 4/5 seeds; calibration gates remain open. See `experiments/20260716T164500Z-cla-roles8-untouched-replication/RUN.md`.
- [x] Close the untouched ledger's missing-environment reproducibility gap with a fully captured replay. All 45 CSV rows were byte-identical and normalized JSON matched exactly; this is reproducibility support, not new independent evidence. See `experiments/20260716T204500Z-cla-roles8-bitwise-replay/RUN.md`.
- [x] Re-run the previous best A6 region at gain `5.0`, couplings `{0.35,0.60}`, delays `{0,3}`, with appraisal/linear/shuffled controls.
- [x] Add leakage-safe train-fitted k-means microstates, suffix-trie reconstruction/compression proxy, surrogate margin, and held-out order-2 loss to the frozen CLA detector path.
- [x] Benchmark the same detector path on Mackey--Glass and Lorenz--96. The frozen proxy passed its preregistered temporal-order gate at 5/5 matched-control wins for each system; see `experiments/20260716T224635Z-cla-same-path-external-calibration/RUN.md`. This validates proxy sensitivity only. The independent stricter held-out coding benchmark remains failed (`65,976.621` CLA bits versus `6,588.443` unigram bits), so no strong attractor/grammar claim is unlocked and detector changes remain owned by the CLA lane.
- [x] Explore frozen CLA readouts over the five-seed A6 tight region plus a balanced 12-point broader sample. Four tight cells met the matched proxy rule, but all 486 grammars were structurally uniform (two productions, zero categories) and all appraisal/linear rows were positive; distinct attractor/grammar regimes were not resolved. See `experiments/20260717T000000Z-cla-dynamics-exploration/RUN.md`.
- [x] 2026-07-16: Harden experiment-ledger provenance before another measured exploration. `bin/new-experiment` now atomically rejects an existing second-resolution run directory instead of sharing it via `mkdir -p`, and `scripts/experiment_wrapper.py` provides fail-closed canonical row sorting for process results before serialization/hashing. Focused collision and row-order/duplicate/missing-key tests pass; implementation commit `f018ead`. This is wrapper-only provenance repair; the frozen detector and historical artifacts were not changed.
- [x] 2026-07-17: Add a reusable fail-closed frozen-identity verifier and plain-language contract for future measured wrappers. It checks both repository commits/cleanliness and implementation SHA-256 values before measurement and emits ledger-ready JSON, including structured failures for missing/unreadable identities; it does not import or change the detector. Five focused tests and the pinned roles8 identity recheck passed.
- [x] 2026-07-17: Preserve exact `git status --porcelain` lines in frozen-identity reports so dirty-tree refusals remain diagnosable after the worktree changes. The regression test exposed and repaired leading-space loss in the Git-output helper; eight provenance-helper tests, eight frozen OmegaSim tests, compilation, the full pinned identity gate, and `git diff --check` passed.
- [ ] Resume OmegaSim collective experiment loop using `docs/collective_experiment_loop.md`, with detailed bot-bot discussion in ProtoBots-BotBotChats and concise summaries in scheduled updates.

## Deferred until first restart run

- [ ] Run OmegaSim under the collective experiment loop after the first CLA-instrumented rerun completes. Protocol: `docs/collective_experiment_loop.md`.
- [ ] **Routing directive (Ben, 2026-07-03):** Use the dedicated bot-bot scheduled-discussion Telegram channel **ProtoBots-BotBotChats** (`telegram:-5459676079`) for collective-loop discussions between Protocosmobot/ZeroBot and Protomegabot; continue using **ProtoBots-updates** / scheduled-updates (`telegram:-1003983157420`) for scheduled/progress updates except the single daily 7AM Pacific summary, which stays in main Protobots; keep concise main-Protobots visibility summaries/directives.
- [ ] Extend exact-tuple matched excess scoring toward amplitude/variance-nearest matching across denser grids.
- [ ] Add residual-state/lobe discovery beyond `argmax(role_prob)` using CLA grammar/compressibility metrics once available.
- [ ] Run a denser phase diagram around matched-excess A6 region: `gain=5.0`, `coupling in {0.35,0.60}`, `delay in {0,3}`.
- [ ] Run a denser phase diagram around first live regions: appraisal `gain=5`, `coupling in {0.35,0.60}`, `delay in {0,3,7}`.
- [ ] Extend A6 with explicit costly prediction actions and delayed payoff accounting.
- [ ] Draft A7 semantic/artifact-field extension once A6 smoke metrics are stable.
- [ ] Draft A8 three-hive artifact-handoff ring after A7 has a minimal meaningful field.
- [ ] **Directive (Ben, 2026-07-03, superseded into CLA prerequisite):** Use Mackey-Glass and Lorenz-96 as external benchmarks for the detector pipeline. These benchmark requirements now belong first to CLA; after CLA passes them, apply the detector to OmegaSim traces.
- [ ] Decide repository publication path: new public `omegasim` repo versus integration into an existing OmegaSim codebase if one is provided.

## Done

- [x] Add exact-tuple matched excess-over-control scoring. Experiment `20260702T100000Z-a6-matched-excess-scoring` found 7/81 appraisal rows exceeding matched linear and shuffled controls, concentrated at high gain; broad claims remain fail-closed pending denser/residual analysis.
- [x] Tighten candidate criteria to require functional artifact/risk/debt/prediction-error dynamics, not only role switching. Experiment `20260702T040000Z-a6-functional-gate` found appraisal 24/81, linear 37/81, shuffled 2/81 functional candidates; result is fail-closed for appraisal-specific claims and points to excess-over-control scoring next.
- [x] Create project notebook `projects/omegasim`.
- [x] Create local prototype repo `projects/omegasim/repos/omegasim`.
- [x] Implement dependency-free A6 thresholded-appraisal model with appraisal, linear, and shuffled controls.
- [x] Add deterministic unit smoke tests for boundedness and reproducibility.
- [x] Run first A6 smoke sweep: `experiments/20260702T012924Z-a6-smoke-sweep/`; 243 local runs, bounded, 18 appraisal candidate regimes by naive criteria, but controls show the metrics need functional tightening.
# Restart direction accepted 2026-07-15

- [x] Write and freeze `docs/cla_detector_preregistration_20260715.md` before outcome inspection, including controls, five seeds, three strata, fixed thresholds, and fail-closed promotion rules.
- [ ] Inventory every completed CLA experiment and artifact, including the latest higher-dimensional Lorenz-96 / lifted / rank-conditioned work, and build a provenance table linking configuration, commit, command, metrics, and conclusions.
- [ ] Produce and compile a new comprehensive CLA experiments PDF that supersedes older summaries, clearly separating reproduced results, null results, detector failures, and hypotheses. Include the latest higher-dimensional experiments and state which claims remain unvalidated.
- [x] Execute the frozen preregistered restart locally; all invariants passed and one cell met the predeclared promotion rule.
