# Sandbox results (checked-in run, seeds as in the scripts)

## Quadratic fixture (exact truth available everywhere)

**D1 — plumbing.** Max relative error, CRN paired rollout vs closed-form
counterfactual: 1.4e-12 (null) … 2.6e-8 (chain). The estimand and the
machinery agree to numerical precision.

**D2 — backbone vs exact truth** (margin-qualified states, all four
families, h ∈ {1,2,5,10,20}):

| metric | range across families/horizons |
|---|---|
| Spearman, validation-mode backbone | 0.998 – 1.000 |
| Spearman, decision-time backbone (noise-free preview) | 0.998 – 1.000 |
| median relative error | 0.09% – 0.56% |

The residual error is exactly the second-order term ½ Δ'Q_A Δ that the
first-order backbone omits — visible, bounded, and owned by the residual
head in the full design.

**D3 — synergy identity** (planted QA cross-block, rank-1, aligned with the
early incoming gradient; early-slice states):

| h | rel. err of u_m'H_A u_n vs pair−singles | planted / noise floor |
|---|---|---|
| 1 | 0.0000 | 22.2x |
| 5 | 0.0000 | 15.6x |
| 10 | 0.0000 | 8.7x |

Control pairs (no planted cross-block): synergy ≤ 1e-15. Note: the first
version of the plant came out at 0.1x the noise floor and was strengthened
per the effect-size precheck rule — the V2 tiny-utility failure mode,
caught by the protocol as designed.

**D4 — provably-aligned null.** Min first-order alignment over all states
and modules: +1.85e-4 (> 0, as the construction guarantees).
False-beneficials beyond 3 sigma: 0.

**D5 — margin decay (local family, 640-step trajectory).** Between-action
margin decays 0.188 → 9.0e-5, geometric (fitted −0.0100/step vs the
worst-case bound ln(1−eta·lambda_min) = −0.0054). No-signal fraction
(margin < 3 sigma): 0.00 in the first trajectory quartile → 1.00 in the
last. This is the V3 audit failure reproduced under a microscope: the
orderings don't "break," the estimand's signal provably drains away.

**D6a — insufficient statistics, constructive.** 400 states with V2-style
feature vectors identical to < 1e-10: exact tau at h=1 coincides to 5e-15
(first order + uniform curvature IS feature-determined), while exact tau at
h=10 spans [−3.2e-4, +9.0e-3] across the feature-equivalence class, with 7
sign flips vs the reference state.

**D6b — regressor ceiling, cross-instance** (train on 4 wide-spectrum
instances, test on a 5th, h=50):

| predictor | test Spearman |
|---|---|
| ridge on V2-style features | 0.21 |
| kNN-5 on V2-style features | 0.46 |
| backbone (same test set) | 1.00 |

The backbone survives instance transfer because it measures each instance's
curvature at runtime; features alias across instances.

## Real MLP + Adam (truth = CRN paired rollouts)

Backbone = exact injected perturbation of the full (theta, m, v) Adam state,
propagated by jax.jvp through the whole Adam update (exact-D) vs the
frozen-D approximation. Spearman vs rollout truth (margin-filtered):

| family | h=1 | h=5 | h=10 | h=25 |
|---|---|---|---|---|
| B1 input-perm, exact-D | 1.000 | 1.000 | 1.000 | 1.000 |
| B1 input-perm, frozen-D | 1.000 | 0.988 | 0.972 | 0.923 |
| B2 output-shift, exact-D | 1.000 | 1.000 | 1.000 | 1.000 |
| B2 output-shift, frozen-D | 1.000 | 0.979 | 0.925 | 0.852 |
| B1 stress (lr=1e-2), exact-D | 1.000 | 0.999 | 0.998 | 0.997 |
| B1 stress (lr=1e-2), frozen-D | 1.000 | **0.156** | **−0.054** | **0.203** |

Median relative error of exact-D: 0.03%–1.9% throughout. The stress row is
the practical headline: at 10x learning rate, differentiating through the
Adam moment recursions is not a refinement, it is the difference between a
working critic and noise — which is why Stage C2 makes the
frozen-D-vs-exact-D acceptance test mandatory.

**Synergy on a real network:** one-step identity u_m'H_A u_n vs measured
pair−singles: Spearman 0.996–1.000, median rel. err 0.7%–1.7%.

**Incoming-harm claim:** frac(tau^B ≥ 0) = 0.98–1.00 at h=1 (first-order
prediction: gating always costs incoming progress), decaying at longer
horizons where second-order effects enter — as the theory says it should.

**Measure, don't declare:** in B1 the conflict is *planted* in layer 1, but
the realized retention benefit at h=10 orders head > layer2 > layer1 —
architectural intent and causal effect are different things, which is the
V3 lesson in one table row.
