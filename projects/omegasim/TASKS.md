# Tasks

## Paused pending CLA

- [ ] Resume OmegaSim after CLA or an equivalent detector has passed known-attractor grammar/compressibility benchmarks, including dimensions comparable to starter OmegaSim traces.
- [ ] Keep routine OmegaSim scheduled/progress updates paused until Ben explicitly restarts OmegaSim after CLA works; answer only direct OmegaSim-specific requests meanwhile.

## Deferred until CLA is working

- [ ] Run OmegaSim under the collective experiment loop after CLA is available as an attractor-grammar detector. Protocol: `docs/collective_experiment_loop.md`.
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
