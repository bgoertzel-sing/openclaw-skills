# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [ ] Integrate the 2026-07-04 SLT estimator validation plan into the local RelaLeap code via parallel Wave 0/1 worktrees: shared interfaces/report schema, SGLD/WBIC core, analytic benchmarks, MAP/prior handling, gauge policies, RelaLeap-shaped benchmarks, reporting/CI gates, and adversarial review.
- [ ] Wave 0 interface freeze for SLT validation before spawning implementation subagents: define `EnergyModel`, `CalibrationBenchmark`, `EstimatorResult`, parameter-block, prior, gauge-policy, and report-schema contracts plus mock outputs.
- [ ] Implement the mandatory SLT-estimation validity contract from Ben's 2026-07-04 plan: exact Gaussian posterior check, WBIC temperature convention tests, known-SLT calibration suite, WBIC/SGLD sampler diagnostics, actual trainable parameter-block masks, MAP-reference validation, gauge/prior checks, sample-size sensitivity curves, module-vs-joint estimates, and null-normalized uncertainty.
- [ ] Validate all SLT estimators on a Tiny Shakespeare level corpus before proceeding to SLT-guided residual-layer work.
- [ ] Prepare parallel subagent work packages after Wave 0: SGLD/WBIC core, analytic registry, sample-size/multiplicity sweep, MAP/prior handling, gauge canonicalization, interaction protocols, RelaLeap-shaped benchmarks, estimator-specific nulls, minibatch/preconditioning diagnostics, reporting/CI gates, integration orchestrator, and adversarial reviewer.
- [ ] After estimator validation passes on Tiny Shakespeare: proceed with using SLT to guide construction of columnar PC residual layers on top of the transformer.
- [ ] Add a real training loop for the rank-one column learner and controls on the six synthetic regimes.
- [ ] Add quantitative synthetic pass/fail gates for known winners and fail-closed low-rank/null behavior.
- [ ] Add WBIC/LLC calibration benchmarks before interpreting any RelaLeap LLC estimates.

## Next

- [ ] Update `docs/slt_estimation_validation_checklist.md` to incorporate the sharper 2026-07-04 plan, especially total-energy vs mean-loss WBIC convention, negative-lambda policy, sample-size slope fitting, exact Gaussian posterior validation, and gauge policy.
- [ ] Add frozen-tail abstraction beyond the current linear test suffix.
- [ ] Add train/validation/test cache manifests and command manifests for larger reproducible runs.

## Waiting or blocked

- [ ] Do not spawn RelaLeap SLT implementation subagents until Ben's uploaded 2026-07-04 validation plan has been incorporated into the Wave 0 interface contract.

## Someday or exploratory

- [ ] Real transformer residual-cache validation after synthetic gates pass.
- [ ] GPU validation only after fail-closed synthetic and causal audit gates pass locally.
- [ ] Refinement-DAG controller for broader factorization search after the minimal train-time learner is stable.

## Done recently

- [x] 2026-07-04: Preserved Ben's uploaded `Validation of SLT Parameter Estimation for RelaLeap` PDF/text in project docs and library, and added `docs/slt_estimator_validation_plan_summary.md` as the current implementation-planning pointer.
- [x] 2026-07-03: Wrote `docs/slt_estimator_implementation_guide.tex` and compiled `docs/slt_estimator_implementation_guide.pdf`, an ASCII-only LaTeX guide explaining what is involved in implementing trustworthy finite-sample WBIC/SGLD/RLCT proxy estimators.
- [x] 2026-07-03: Implemented first coding slice in local repo `repos/relaleap` on branch `agent/train-time-causal-slice1`: synthetic generators for all six regimes, identity-initialized rank-one learner, flat/SVD controls, exact ablation auditor, dependency contracts/null specs, event log, fail-closed report, and unit tests.
- [x] 2026-07-03: Added a code-level guardrail that `scientific_status=pass` requires calibrated finite-sample SLT evidence fields over actual parameter blocks.
- [x] 2026-07-03: Created local `projects/relaleap/` project notebook.
- [x] 2026-07-03: Preregistered new train-time causal factor learner design at `docs/train_time_causal_factor_preregistration.md`.
