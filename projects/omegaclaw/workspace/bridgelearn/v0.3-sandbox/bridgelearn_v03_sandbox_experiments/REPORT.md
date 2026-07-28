# BridgeLearn 0.3 sandbox experiments

Generated: 2026-07-23T01:48:52.332981+00:00

BridgeLearn version: `0.3.0`

## Purpose

These four synthetic experiments exercise the v0.3 mechanisms that were added
for nonlinear sharpness response and momentum dynamics:

1. online identification and forward prediction of a dynamic sharpness plant;
2. order-2 antithetic excitation for the weak AR(2) contrast direction;
3. companion-matrix stability and Lyapunov-adapted covariance norms;
4. momentum-limited covariance reachability and actuator projection.

They are mechanism tests, not neural-network, CAROM, predictive-coding, or RL
performance claims.

## Executive results

| Experiment | Main result |
|---|---|
| Dynamic sharpness | `SharpnessPlant` recovered gamma_p=0.0270407 and gamma_r=0.41506 from truths 0.028 and 0.42. One-step RMSE was 0.022797, versus 0.22321 for a rolling static h(eta) fit. |
| Antithetic identification | At nearly equal added state width, contrast RMSE for c1-c2 was 0.0024928, versus 0.042051 for white excitation and 0.077219 without a probe. |
| Companion stability | The near-repeated-root matrix had spectral radius 0.9 yet transient covariance amplification 49.472x and Lyapunov condition number 5104.96. |
| Momentum reachability | Cooling V=0.08 to V=0.005 with fixed mu=0.9 has an asymptotic floor requiring at least 27 updates. The one-step actuator found 0/5 fixed-momentum targets feasible and 5/5 feasible when momentum could move. |

# 1. Dynamic sharpness as a plant

## Model

The simulated plant was

```text
h[k+1] = h[k]
       + gamma_p * g[k]
       - gamma_r * max(eta[k] h[k] - (2(1+mu[k])-delta), 0)
       + process noise.
```

The command schedule warmed, oscillated near the edge, cooled, and rewarmed.
This creates lag and hysteresis that cannot be represented by a static curve
`h(eta)`.

`bridgelearn.SharpnessPlant` was updated by forgetting-factor RLS and generated
one-step interval forecasts. Metrics exclude the first 60
updates.

## Results

- True parameters: gamma_p=0.028, gamma_r=0.42.
- Final estimates: gamma_p=0.02704072, gamma_r=0.4150601.
- Relative errors: -3.426% and -1.176%.
- Plant one-step RMSE against latent sharpness: 0.02279678.
- Rolling static-response RMSE: 0.223211.
- RMSE improvement over the static response: 9.7913x.
- Empirical funnel coverage: 100%.

The counterfactual held eta=0.29 and
mu=0.85 after update
150. A frozen-curvature calculation reported
edge utilization 0.96795, so
it would have treated the command as safe indefinitely. The true plant crossed
the edge after 15
future updates. The plant point forecast crossed after
17,
while the robust upper funnel warned after
4.

Artifacts:

- [tracking plot](artifacts/dynamic_sharpness/dynamic_sharpness_tracking.png)
- [edge-utilization plot](artifacts/dynamic_sharpness/dynamic_sharpness_edge_utilization.png)
- [parameter identification](artifacts/dynamic_sharpness/dynamic_sharpness_parameters.png)
- [counterfactual rollout](artifacts/dynamic_sharpness/dynamic_sharpness_counterfactual.png)
- [full trace](artifacts/dynamic_sharpness/dynamic_sharpness_trace.csv)

# 2. Antithetic order-2 identification

## Model and resource matching

The cold AR(2) plant was

```text
z[k+1] = 1.8 z[k] - 0.81 z[k-1] + u[k] + epsilon[k],
```

which has a repeated pole at 0.9. Its weakly identified combination is
`c1-c2`. The experiment compared no probe, white known excitation, and the
library's exact committed `+delta,-delta` probe pairs.

The white and antithetic probe amplitudes were chosen to add approximately the
same stationary state width, 0.01. Known probe
commands were subtracted from the regression response, so the comparison is
about regressor geometry rather than unmodeled forcing.

## Results over 1000 trials

| Mode | Contrast RMSE | Median cond(M) | Median smallest eigenvalue | Added state variance |
|---|---:|---:|---:|---:|
| None | 0.077219 | 340.726 | 2.28057e-05 | 0 |
| White | 0.0420514 | 333.223 | 7.61912e-05 | 0.00857942 |
| Antithetic | 0.00249278 | 2.56382 | 0.00780988 | 0.00999251 |

Antithetic excitation reduced contrast RMSE by
16.869x relative
to equal-width white excitation and improved the median smallest regressor
eigenvalue by 102.5x.
The median condition number fell by
129.97x.

Artifacts:

- [contrast error distribution](artifacts/antithetic_identification/antithetic_contrast_error.png)
- [online RLS standard error](artifacts/antithetic_identification/antithetic_online_standard_error.png)
- [regressor information](artifacts/antithetic_identification/antithetic_regressor_information.png)
- [probe signals](artifacts/antithetic_identification/antithetic_probe_signals.png)
- [trial-level data](artifacts/antithetic_identification/antithetic_trial_results.csv)

# 3. Companion stability and non-normality

Four stable companion matrices were compared. Two had essentially the same
spectral radius, 0.9, but very different geometry.

| Case | Regime | rho(A) | cond(P) | Max covariance amplification | Peak step |
|---|---|---:|---:|---:|---:|
| Near repeated root | critical | 0.9 | 5104.957 | 49.47224 | 9 |
| Underdamped, same radius | underdamped | 0.9 | 1.625854 | 1.318482 | 1 |

For the near-repeated-root case, an initial covariance error chosen along the
worst transient direction grew by
49.47224x
in Euclidean Frobenius norm at step
9. In the Lyapunov-adapted norm
it had already contracted to
0.242798,
below the theoretical bound
0.2457827.

This is the practical reason BridgeLearn exposes both spectral radius and
`cond(P)`: the former describes asymptotic stability, while the latter prices
transient amplification and conversion back to Euclidean error bounds.

Artifacts:

- [transient amplification](artifacts/companion_stability/companion_transient_amplification.png)
- [Euclidean versus Lyapunov norms](artifacts/companion_stability/companion_lyapunov_norm_comparison.png)
- [conditioning over the stability triangle](artifacts/companion_stability/companion_stability_triangle_conditioning.png)
- [case table](artifacts/companion_stability/companion_cases.csv)

# 4. Momentum reachability

For heavy-ball dynamics with fixed momentum, the pole-radius floor is

```text
rho_min = sqrt(mu),
```

so the corresponding asymptotic covariance contraction floor is `mu` per
update. Reducing variance by a ratio r therefore requires at least

```text
N >= ceil(log(r) / log(mu)).
```

For r=0.0625 and mu=0.9, this gives
27 updates even before noise, command slew,
and non-normality are charged.

The actuator experiment asked for five pure one-step marginal contractions.
With momentum fixed at 0.9, none passed the full transition and companion
feasibility checks. With momentum allowed to change, all five were exactly or
closely realized; the unconstrained search selected low momentum because that
was the only way to match both the desired adjacent cross-covariance and next
variance.

| Target ratio | Fixed predicted | Fixed feasible | Adaptive predicted | Selected adaptive mu |
|---:|---:|:---:|---:|---:|
| 0.95 | 1.380803 | no | 0.950000 | 0.0000 |
| 0.90 | 1.330803 | no | 0.900000 | 0.0000 |
| 0.80 | 1.230803 | no | 0.800000 | 0.0000 |
| 0.70 | 1.130803 | no | 0.700000 | 0.0000 |
| 0.50 | 0.930803 | no | 0.500000 | 0.0000 |


Artifacts:

- [minimum-horizon curve](artifacts/momentum_reachability/momentum_minimum_horizon.png)
- [one-step reachability](artifacts/momentum_reachability/momentum_one_step_reachability.png)
- [momentum lower-bound sweep](artifacts/momentum_reachability/momentum_lower_bound_sweep.png)
- [one-step results](artifacts/momentum_reachability/momentum_one_step_results.csv)

# Interpretation

The experiments support four narrow conclusions.

1. Treating sharpness as a slow state captures path dependence that a static
   response curve misses, and it can warn about a future edge crossing before
   the current command is unsafe.
2. In a cold AR(2) regime, temporal probe design matters much more than merely
   increasing white amplitude. The antithetic pair directly repairs the
   `(1,-1)` information direction.
3. A spectral-radius check alone is insufficient near repeated roots. A
   Lyapunov metric and its condition number are operationally meaningful
   diagnostics.
4. Momentum is a reachability actuator, not just a smoothing constant. High
   fixed momentum imposes a physical cooling horizon and can make a requested
   transition impossible even when a scalar variance target looks benign.

# Limitations

- Every plant here is scalar or 2x2 and synthetic.
- The sharpness law is the same phenomenological form assumed by the library;
  the experiment checks identification and planning behavior under that model,
  not model universality.
- The antithetic result assumes the external probe is known and removed from
  the regression response. Unknown or clipped probe realization would require
  additional calibration.
- The companion experiment is local linear analysis. Neural training can move
  between blocks and Hessian eigendirections.
- The momentum actuator still targets a scalar marginal transition rather than
  an exact augmented-state Schrödinger bridge. Infeasibility therefore includes
  both the momentum floor and cross-time coupling mismatch.
- No result here demonstrates improved task loss, generalization, CAROM
  routing, predictive-coding inference, or RL returns.

# Reproduction

From this directory:

```bash
python -m pip install --no-deps vendor/bridgelearn-0.3.0-py3-none-any.whl
python run_all.py --output artifacts
```

The complete machine-readable summary is in [`summary.json`](summary.json).
