# Validation of SLT Parameter Estimation for RelaLeap

- Type: PDF technical plan
- Date on document: 2026-07-04
- Received: 2026-07-04
- Source file: Telegram upload from Ben Goertzel in Protobots
- Local PDF: `library/relaleap-slt-estimator-validation-plan/source/relaleap_slt_estimator_validation_plan.pdf`
- Project copy: `projects/relaleap/docs/relaleap_slt_estimator_validation_plan.pdf`
- SHA-256: `0c5a59f2911f1f8cafaf8aa1e3b03d5cb424a0085f4dabf3c2661a2e2707295d`
- Related project: `projects/relaleap/`
- Privacy/access: shared by project owner for project use; no credentials observed.
- Tags: RelaLeap, SLT, WBIC, SGLD, LLC, RLCT, calibration, subagents

## Summary

This document sharpens the RelaLeap SLT estimator validation program. It emphasizes that WBIC/SGLD LLC/RLCT quantities are finite-sample calibrated diagnostics, not exact RLCTs or causal certificates. It requires analytic target recovery, sample-size scaling, gauge control, MAP-reference validation, interaction protocols, null normalization, and RelaLeap-shaped benchmark families before SLT estimates can guide residual-column factorization decisions.

Key additions beyond the earlier checklist:

- WBIC temperature convention is clarified: when using total energy `E_n`, use coefficient `1 / log n`; if using mean loss internally, the effective coefficient is `n / log n`. A path multiplying total energy by `1/(n log n)` must fail validation.
- Mandatory sample-size scaling over `n in {256,512,1024,2048,4096,8192}`, fitting `Delta E_n = a log n + b log log n + c`, with both single-n and slope-fit estimates reported.
- Negative estimated LLC/RLCT proxies must not be clipped; they indicate MAP/reference, target, consistency, or Monte Carlo problems and should fail or downgrade the result.
- Gauge symmetries for rank-one atoms and dictionaries require explicit canonicalization policies and invariance tests.
- Block-wise LLC interaction information must be cross-checked with shared-core-conditioned and full-adapter projected protocols.
- The benchmark suite is expanded: exact Gaussian posterior, product singularity with negative synergy, nonzero product ridge redundancy, cusp/crossing singularities, overparameterized mixtures, composition benchmarks, and RelaLeap-shaped cases such as dead-column, mediator, router-collapse, low-rank trap, and oblique dictionary.
- A parallel subagent plan is proposed with shared interfaces first, then separate agents for SGLD/WBIC core, analytic registry, sample-size sweeps, priors/MAP, gauge, interactions, RelaLeap-shaped benchmarks, nulls, minibatch/preconditioning diagnostics, reporting/CI, integration orchestration, and adversarial review.

## Relevance

This becomes the strongest current guidance for RelaLeap's SLT estimator validation. It supports parallelization, but only after a Wave 0 interface freeze defines common contracts such as `EnergyModel`, `CalibrationBenchmark`, and `EstimatorResult` plus report schemas.

## Important caution

Treat the document as project guidance, not proof that the proposed estimators are valid. The project must still implement and test the calibration gates before using SLT estimates for model-selection or residual-column promotion.
