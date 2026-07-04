# RelaLeap SLT Residual-Layer Causal Factors

- Slug: `relaleap`
- Status: `active` (SLT estimator validation is current focus)
- Created: `2026-07-03`
- Last reviewed: `2026-07-04`
- Owner: Benjamin Goertzel

## Purpose

Develop and evaluate SLT-informed residual-layer learning methods for discovering causal factor structure in transformer failure modes. The current focus is a new **train-time causal factor learner**: columns should be discovered jointly during task training, not fit posthoc to frozen residual caches.

## Success criteria

- A preregistered train-time design exists with hypothesis, architecture, training procedure, synthetic ground-truth plan, causal audit gates, null controls, and fail-closed criteria.
- Later implementation recovers expected behavior on synthetic regimes: `exact_factorized`, `shared_core_redundant`, `synergistic_pair`, `low_rank_trap`, `oblique_dictionary`, and `random_null`.
- Any promoted residual factorization beats matched flat/SVD/dense controls, beats dependency-aware nulls, passes exact ablation and commutator gates, and shows sparse interpretable LLC interaction structure.
- Reports distinguish prediction, reconstruction, causal modularity, and SLT/free-energy evidence instead of collapsing them into one handcrafted score.
- SLT evidence is considered meaningful only after calibrated finite-sample WBIC/SGLD proxy estimation over actual trained parameter blocks, with sampler diagnostics, explicit WBIC temperature accounting, MAP-reference validation, gauge policy checks, sample-size sensitivity, interaction/null normalization, and finite-sample caveats.

## Scope

### In scope

- Local design and preregistration under `projects/relaleap/`.
- SLT estimator validation package: SGLD/WBIC core, analytic calibration registry, sample-size sweeps, MAP/prior checks, gauge canonicalization, interaction protocols, RelaLeap-shaped benchmarks, nulls, minibatch/preconditioning diagnostics, reporting/CI gates, integration orchestrator, and adversarial reviewer.
- Synthetic ground-truth regimes with known causal structure.
- Train-time residual-column learners with identity initialization, sparse supports, SLT-informed regularizers, and auditable split/merge/transfer events.
- Causal audits: exact ablation calibration, pair synergy, support regret, commutator leakage, off-support leakage, and LLC interaction information.
- Fail-closed decision criteria and null controls.
- Tiny Shakespeare corpus as the first real-text validation target for SLT estimators.

### Out of scope for now

- Implementing code in this task.
- GPU-scale validation.
- Paid or remote compute.
- Pushing branches or opening PRs.
- Claiming real transformer causal columns before synthetic and audit gates pass.

## Current state

Earlier RelaLeap phases did not justify promotion:

1. `v0` seven-arm posthoc pregate was a reproducible smoke scaffold only: small toy data, handcrafted LLC proxy, and no arm beat required null controls.
2. `v2` parameterized arms fitted to cached residuals improved engineering realism but deployable mechanisms failed winner recovery, lost to controls, and failed null specificity.

Ben's 2026-07-03 directive is to **try a new train-time causal factor approach**. The preregistration is recorded at `docs/train_time_causal_factor_preregistration.md`.

Ben's 2026-07-04 directive: make SLT estimator validation the current focus for RelaLeap. Once all estimators are validated on a Tiny Shakespeare level corpus, proceed with the prior idea of using SLT to help guide the residual layer on top of the transformer.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| Active RelaLeap implementation | not present in this local workspace | TBD, likely external/Mac-side from prior notes | TBD | TBD |

## Environments

No local implementation environment is required for this preregistration. No GPU, paid compute, or remote resources were used.

## Key results

- 2026-07-03: Created local project notebook and preregistered the train-time causal factor learner design: `projects/relaleap/docs/train_time_causal_factor_preregistration.md`.
- 2026-07-03: Drafted SLT estimation validation checklist (`docs/slt_estimation_validation_checklist.md`) with 10 operational gates: parameter block coverage, SGLD sampler diagnostics (ESS ≥ 200, CV < 0.25, ≥ 4 chains), WBIC temperature protocol (β = 1/n log n), known-singularity calibration suite (6 benchmarks with analytical RLCT), regime discriminability, null-normalized uncertainty, finite-sample wording, and promotion decision integration.
- 2026-07-03: Wrote ASCII-only LaTeX/PDF explainer `docs/slt_estimator_implementation_guide.tex` / `.pdf` describing the full estimator implementation pipeline: block masks, WBIC/SGLD sampling, diagnostics, calibration benchmarks, input coverage, module-vs-joint estimates, null-normalized uncertainty, and fail-closed promotion gates.
- 2026-07-04: Preserved Ben's uploaded `Validation of SLT Parameter Estimation for RelaLeap` plan at `docs/relaleap_slt_estimator_validation_plan.pdf` and `library/relaleap-slt-estimator-validation-plan/SOURCE.md` (SHA-256 `0c5a59f2911f1f8cafaf8aa1e3b03d5cb424a0085f4dabf3c2661a2e2707295d`). Added `docs/slt_estimator_validation_plan_summary.md`.
- Source context: `library/slt-residual-layers/SOURCE.md`, `library/slt-hyperseed-synthesis/`, `library/relaleap-slt-estimator-validation-plan/SOURCE.md`, and `scratch/relaleap_gpt55_pro_final_plan.md`.

## Open questions

- Where should the eventual implementation live: local `projects/relaleap/repos/`, the Mac-side RelaLeap worktree, or a new coordinated branch?
- What minimal transformer or synthetic-only harness should be used for the first train-time implementation slice?
- What Tiny Shakespeare corpus version and tokenization should be used for the first real-text SLT estimator validation runs?
- What input-count schedule and stopping rule should be used for the first WBIC/SGLD sample-size sensitivity curves? Ben's 2026-07-04 plan proposes `n = {256,512,1024,2048,4096,8192}` and slope-fitting `Delta E_n = a log n + b log log n + c`.
- Which finite-sample WBIC/LLC calibration suite should be implemented first? The 2026-07-04 plan expands the suite to include exact Gaussian posterior, product singularity, nonzero product ridge, cusp/crossing singularities, composition benchmarks, and RelaLeap-shaped cases.

## Related projects and concepts

- SLT and residual layers library record: `library/slt-residual-layers/SOURCE.md`.
- Broader SLT/Hyperseed synthesis material: `library/slt-hyperseed-synthesis/`.
- RelaLeap Mac-side prior work referenced in memory entries from 2026-07-02 and 2026-07-03.

## Risks

- Reconstruction or task-loss gains may be mistaken for causal factorization.
- Sparse columns may merely encode capacity, router frequency, or low-rank structure unless matched controls are strict.
- LLC/WBIC estimates are finite-sample proxies and require calibration before interpretation; never clip negative lambda estimates, and fail/downgrade if MAP reference, sampler target, or Monte Carlo consistency is suspect.
- Uncalibrated, under-sampled, or frozen-parameter SLT proxies could recreate the earlier failure mode; code and preregistration now block scientific promotion without a calibrated SLT evidence contract including input coverage and sample-size sensitivity.
- Synthetic success may not transfer to real transformer residual streams.
- Hidden posthoc leakage into train-time structural decisions would invalidate claims.
- Frontier-model API access may be topic-sensitive: Claude Fable, GPT-5.6-class, or similar controlled models could throttle, downgrade, or refuse advanced neural-network/LLM-development work. Treat this as an empirical operations risk for RelaLeap; record model behavior by task type; keep prompts truthful while deliberately framing work by the immediate legitimate subgoal / nearest safe category (for example SLT estimator validation rather than generic frontier-model optimization); and avoid relying on a single proprietary model for critical estimator or architecture decisions.
