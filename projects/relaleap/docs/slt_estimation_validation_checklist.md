# SLT Estimation Validation Checklist

- Project: RelaLeap SLT residual-layer causal factors
- Date: 2026-07-03
- Status: draft checklist for gating any SLT-based promotion decision
- Purpose: Ensure that WBIC/SGLD proxy estimates of RLCT/LLC are meaningful before any scientific or engineering conclusion is drawn.

## Context

Practical SLT applications are bottlenecked by estimation quality, not theory. The v1 seven-arm pregate demonstrated this directly: the "LLC" was a handcrafted complexity proxy, and the "WBIC" table was a tiny bounded SGLD run over frozen output-amplitude parameters only. Neither captured singularity structure.

This checklist defines what must be true before we treat an SLT estimate as evidence. It operationalizes section 3.4.1 of the preregistration into concrete, testable gates.

## 1. Parameter Block Coverage

**Gate**: The SGLD/WBIC sampler must run over the actual trainable parameter blocks of the adapter, not a frozen or hand-picked subset.

| Check | Requirement | Fail condition |
|---|---|---|
| Block enumeration | All trainable adapter parameters are partitioned into named blocks: column amplitudes, gate/router params, atom directions `a_g`, `b_g`, shared-core params, declared joint blocks | Any trainable parameter excluded without documented justification |
| Block mask test | For each block, a parameter-masked run exists where only that block is sampled and all others are frozen at trained values | Missing blocks |
| Joint block test | For each declared joint block (e.g., `{a, b}` for synergy test), a run exists where the union is sampled | Joint blocks not tested |
| Full-adapter run | At least one run samples all adapter parameters jointly | Not performed |

**Key principle**: Frozen-output-amplitude proxies are diagnostic only, never promotable evidence.

## 2. SGLD Sampler Diagnostics

**Gate**: The SGLD chain must show sufficient mixing, stability, and effective sample size for the energy landscape near the trained minimum to be meaningfully explored.

| Diagnostic | Minimum requirement | Report format |
|---|---|---|
| Chain count | ≥ 4 independent chains with different seeds | Per-chain and multi-chain summary |
| Total steps per chain | ≥ 10,000 for small synthetic regimes (n ≤ 512, d ≤ 32); ≥ 50,000 for larger | Step count + burn-in count |
| Burn-in | ≥ 20% of total steps, discarded | Pre/post burn-in energy trace |
| Step size | Tuned so acceptance rate ∈ [0.5, 0.9] for Langevin moves; report step size schedule | Acceptance rate per phase |
| Effective sample size (ESS) | ≥ 200 per chain for the negative log-likelihood (NLL) statistic; report autocorrelation time | ESS + autocorrelation plot |
| Energy trace stability | Post-burn-in NLL trace shows no trend (Mann-Kendall p > 0.05) and no single-step jumps > 5σ | Trace plot + Mann-Kendall test result |
| Seed sensitivity | Point estimates of λ (RLCT proxy) across seeds have coefficient of variation (CV) < 0.25 | Per-seed λ table + CV |

**If ESS < 200 or CV ≥ 0.25**: the estimate is diagnostic only. Report `slt_evidence_status = uncalibrated`.

## 3. WBIC Temperature Protocol

**Gate**: WBIC estimation must use the theoretically correct inverse temperature and demonstrate temperature sensitivity.

| Check | Requirement |
|---|---|
| WBIC temperature | β = 1 / (n · log n) where n = number of data points in the estimation set |
| Temperature sensitivity | At least 3 temperatures run: β/4, β, 4β. The WBIC estimate at β should be between the two extremes in a sensible way (not divergent) |
| Temperature report | All temperatures, their NLL means, and their λ estimates reported |
| Prior specification | The prior over adapter parameters is explicitly stated and is the same across all WBIC runs unless a sensitivity run is declared |

**If β is not set to 1/(n log n) or no temperature sensitivity is shown**: do not call it WBIC. Call it "fixed-temperature SGLD proxy" and downgrade evidence strength.

## 4. Known-Singularity Calibration Suite

**Gate**: Before interpreting any RelaLeap SLT estimate, the estimator must pass benchmark models with known or analytically checkable RLCT/LLC behavior.

### 4.1 Calibration benchmarks

| Benchmark | Known RLCT behavior | Expected estimator output |
|---|---|---|
| Regular identifiable linear regression | RLCT = d/2 (regular, no singularity) | λ ≈ d/2 within ±20% |
| Rank-deficient linear regression (rank r < d) | RLCT = r/2 (true rank, not parameter count) | λ ≈ r/2 within ±20% |
| Overparameterized mixture with K-fold symmetry | RLCT < d/2 (singular due to permutation symmetry) | λ < d/2; detects singularity |
| Independent two-module composition | λ(A∪B) ≈ λ(A) + λ(B); I_λ(A;B) ≈ 0 | Additivity holds within ±15% |
| Redundant/shared-core composition | λ(A∪B) < λ(A) + λ(B); I_λ(A;B) > 0 | Detects redundancy |
| Synergistic composition | λ(A∪B) > λ(A) + λ(B) or I_λ(A;B) < 0 (depending on generator) | Detects synergy with correct sign |

### 4.2 Pass criteria

- At least 5 of 6 benchmarks must show the correct sign and rough magnitude.
- The estimator must distinguish regular (λ ≈ d/2) from singular (λ < d/2 or λ > d/2 with explanation).
- Independent composition must show near-zero I_λ.
- Redundant and synergistic compositions must show the correct I_λ sign.

**If < 5 of 6 pass**: `slt_evidence_status = uncalibrated`. The estimator cannot be trusted on RelaLeap regimes.

### 4.3 Calibration reporting

For each benchmark:
- Model specification (dimensions, rank, symmetry structure)
- Analytical RLCT (if known) or expected qualitative behavior
- Estimated λ with CI
- Number of chains, steps, ESS
- WBIC temperature used
- Pass/fail status

## 5. Regime Discriminability Test

**Gate**: The SLT estimator must produce distinguishable outputs for RelaLeap synthetic regimes with different ground-truth singularity structure.

| Regime pair | Expected discrimination |
|---|---|
| `exact_factorized` vs `synergistic_pair` | I_λ near 0 vs I_λ with significant sign |
| `exact_factorized` vs `shared_core_redundant` | I_λ near 0 vs I_λ > 0 |
| `exact_factorized` vs `random_null` | λ values should not be artificially lower for null |
| `low_rank_trap` vs `exact_factorized` | SVD/low-rank control should explain low_rank_trap; SLT should not falsely indicate columnar structure |

**Discrimination metric**: For each regime pair, the 95% bootstrap CI of the I_λ difference must not contain zero (for pairs where I_λ is expected to differ) OR must contain zero (for pairs where I_λ is expected to be similar).

**If the estimator cannot distinguish `exact_factorized` from `synergistic_pair`**: the SLT pregate is decorative. Report `scientific_status = fail_closed`.

## 6. Null-Normalized Uncertainty

**Gate**: Any reported I_λ or λ value must be compared against matched null controls with bootstrap uncertainty.

| Check | Requirement |
|---|---|
| Null controls | At least: target-shuffle null, hidden-shuffle null, support-frequency-matched random null |
| Bootstrap | ≥ 200 bootstrap resamples of the estimation set for both real and null |
| Margin | Real I_λ must beat null I_λ by a margin whose 95% CI excludes zero |
| Reporting | Real estimate, null estimate, difference, CI, p-value, and margin all reported |

**If the 95% CI of (real − null) includes zero**: the SLT interpretation is blocked. Report `slt_evidence_status = uncalibrated`.

## 7. Finite-Sample Wording

**Gate**: All reports, logs, and decision documents must use precise language.

| Correct wording | Incorrect wording |
|---|---|
| "finite-sample WBIC/SGLD proxy for RLCT" | "the RLCT" |
| "estimated LLC proxy λ̂" | "the LLC" |
| "I_λ proxy suggests redundancy" | "columns are redundant" |
| "calibrated against 6 benchmark models" | "the RLCT is estimated" |

**If exact-RLCT language is used without analytical proof**: the report is invalid.

## 8. Promotion Decision Integration

**Gate**: The SLT evidence panel must be complete before any promotion decision.

Required fields in the decision report:

```
slt_evidence_status: calibrated | uncalibrated
estimator_type: WBIC | SGLD | fixed-temperature-proxy
estimated_parameter_blocks: [list]
wbic_temperature: <value>
wbic_n: <sample count>
chain_count: <int>
total_steps_per_chain: <int>
ess_per_chain: [list]
seed_cv: <float>
calibration_benchmarks_passed: <int>/6
calibration_benchmark_details: [list]
null_normalized_margin: <float>
null_normalized_ci: [<lo>, <hi>]
regime_discriminability: pass | fail
finite_sample_caveat: "These are finite-sample WBIC/SGLD proxies, not exact RLCTs."
```

**If any required field is missing or `slt_evidence_status = uncalibrated`**: `scientific_status = fail_closed`, regardless of task loss, reconstruction, or causal audit results.

## 9. Compute Budget Notes

- SGLD over small adapter parameter blocks (≤ few thousand parameters) with 4 chains × 10K steps is feasible on CPU in minutes for synthetic regimes.
- The calibration suite (6 benchmarks) can run in under 1 hour on CPU for small models.
- GPU is not required for SLT estimation on synthetic regimes. GPU is only relevant for real transformer residual caches, which is out of scope until all synthetic gates pass.
- If estimation time becomes a bottleneck, reduce parameter block size or use surrogate-assisted SGLD, but document the approximation and its validation.

## 10. Relationship to Preregistration

This checklist operationalizes section 3.4.1 of `docs/train_time_causal_factor_preregistration.md`. If the preregistration and this checklist conflict, the more conservative requirement governs unless Ben explicitly approves an exception.

## 11. Open Questions

1. **SGLD vs. NUTS/HMC for WBIC**: SGLD is the standard practical choice, but for small synthetic models NUTS may give better ESS. Should we allow NUTS as an alternative with the same diagnostics?
2. **Analytical RLCT for calibration benchmarks**: Some benchmarks (e.g., rank-deficient linear regression) have known RLCT from Watanabe's theory. Others (e.g., synergistic composition) may require simulation-based ground truth. Should we derive analytical values where possible?
3. **Block-wise vs. full-adapter λ**: When computing I_λ(A;B), should we estimate λ(A), λ(B), λ(A∪B) by sampling only those blocks (block-wise) or by sampling the full adapter and masking? Block-wise is cheaper but may miss cross-block singularity structure.
