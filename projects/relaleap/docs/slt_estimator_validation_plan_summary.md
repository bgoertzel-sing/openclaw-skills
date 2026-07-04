# SLT Estimator Validation Plan Summary

Source: `projects/relaleap/docs/relaleap_slt_estimator_validation_plan.pdf` / library sidecar `library/relaleap-slt-estimator-validation-plan/SOURCE.md`.

This 2026-07-04 plan supersedes or sharpens the earlier SLT estimator checklist where more specific. Most important changes:

1. Freeze shared interfaces before parallel work: `EnergyModel`, `CalibrationBenchmark`, `EstimatorResult`, and report schema.
2. Treat WBIC/SGLD LLC estimates as finite-sample diagnostics, not exact RLCTs or causal certificates.
3. Validate temperature conventions explicitly: total energy coefficient should be `1/log(n)`; mean-loss code should apply effective coefficient `n/log(n)`.
4. Add exact Gaussian posterior validation for sampler mean/covariance/energy.
5. Require sample-size sweeps over `n = {256,512,1024,2048,4096,8192}` and slope fitting of `Delta E_n = a log n + b log log n + c`.
6. Never clip negative lambda estimates; downgrade/fail instead.
7. Add explicit MAP-reference refinement, prior sensitivity, and gauge canonicalization policies.
8. Cross-check block-wise interactions with shared-core-conditioned and full-adapter projected protocols.
9. Expand calibration and RelaLeap-shaped benchmark families.
10. Use parallel subagents only after Wave 0 interface freeze, with a dedicated integration orchestrator and adversarial reviewer.
