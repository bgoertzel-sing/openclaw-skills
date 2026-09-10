# Dynamic sharpness and momentum control in BridgeLearn 0.3

This document describes the v0.3 extension from first-order scalar covariance
control to companion-aware momentum control with a dynamic sharpness model.
It is an implementation document, not a claim that every neural block follows
these equations globally.

## 1. Why a static curvature response is insufficient

A local response such as

```text
h(eta) = h0 + slope * (eta - eta0)
```

can repair mild curvature of a response curve inside a small trust region. It
cannot represent two phenomena that dominate near the edge of stability:

1. sharpness responds with lag and path dependence, so it is a state;
2. realized sharpness can be attracted toward the momentum stability boundary,
   so the apparent static slope is regime-dependent and can be very large.

BridgeLearn therefore keeps the static model only as one rung of an adequacy
ladder.

## 2. Companion dynamics under momentum

For a centered scalar block with heavy-ball momentum, the local recursion is

```text
z[k+1] = c1[k] z[k] + c2[k] z[k-1] + epsilon[k+1]
c1[k]  = 1 + mu[k] - eta[k] h[k]
c2[k]  = -mu[k].
```

The companion matrix is

```text
A[k] = [[c1[k], c2[k]],
        [1,       0   ]].
```

Its characteristic polynomial is

```text
s**2 - c1*s - c2 = 0.
```

For `c2=-mu`, Jury stability becomes

```text
eta*h > 0,
eta*h < 2*(1+mu),
0 <= mu < 1.
```

The v0.3 implementation works in a margin-shrunk triangle and exposes all
three signed Jury margins.

The damping boundary is

```text
c1**2 + 4*c2 = 0.
```

In the underdamped region, the pole radius is `sqrt(mu)`. This creates a hard
cooling floor: reducing the learning rate alone cannot produce covariance
contraction faster than the momentum memory permits. The actuator must lower
momentum or the horizon governor must pay additional physical updates.

## 3. Gray-box identification with known commands

Fitting constant AR(2) coefficients over a window is biased when commands vary.
The commands are known, so the structural map can be inverted first:

```text
zeta[k] = ((1+mu[k])*z[k] - mu[k]*z[k-1] - z[k+1]) / eta[k]
        = h*z[k] + xi[k].
```

`GrayBoxMomentumObserver` estimates `h` with batch-weighted least squares and
estimates the unit-batch noise scale from weighted residual energy.

```python
from bridgelearn import GrayBoxMomentumObserver

observer = GrayBoxMomentumObserver(
    minimum_samples=32,
    instrument_lag=2,  # optional IV mode for noisy z observations
)

estimate = observer.estimate(
    histories=centered_state_histories,
    step_histories=eta_histories,
    momentum_histories=mu_histories,
    batch_histories=batch_histories,
)

print(estimate.curvature)
print(estimate.noise_scale)
print(estimate.contrast_standard_error)
```

### 3.1 Closed-loop consistency

The estimator uses commands that are measurable from past data. Under the
local martingale-difference assumption for `xi[k]`, feedback does not by itself
bias the regression. This is still a local structural assumption: Adam
preconditioner motion or strongly non-quadratic drift can violate it.

### 3.2 Errors in variables

A noisy centered state attenuates ordinary least squares. Setting
`instrument_lag` uses a deeper lag as an instrument. The instrument must be
correlated with the true regressor and approximately independent of the
measurement error; this is an application-level validity condition.

### 3.3 Structural adequacy

`StructuralAR2AdequacyObserver` compares gray-box one-step RMSE with a black-box
AR(2) one-step RMSE. Divergence lowers structural confidence and triggers a
fallback rather than silently absorbing misspecification into clipping.

```python
from bridgelearn import StructuralAR2AdequacyObserver

adequacy = StructuralAR2AdequacyObserver().estimate(
    histories=centered_state_histories,
    step_histories=eta_histories,
    momentum_histories=mu_histories,
    curvature=estimate.curvature,
)
```

When the structural model is not trusted, `ForgettingFactorAR2Observer` tracks
`c1,c2` directly. Its effective memory is approximately

```text
N_eff = 1 / (1 - forgetting).
```

The actuator should not command coefficient changes faster than the observer
can identify. The observer therefore reports a coefficient-slew contract,
which also supports slowly-time-varying companion stability.

## 4. The sharpness plant

The minimal dynamic model is

```text
h[k+1] = h[k]
       + gamma_p * g[k]
       - gamma_r * max(eta[k]*h[k] - theta[k], 0)
       + e[k],

theta[k] = 2*(1+mu[k]) - delta.
```

Here:

- `g[k]` is a non-negative progress proxy, such as squared update norm;
- `gamma_p` is progressive sharpening;
- `gamma_r` is the restoring response after the safety edge is pierced;
- `delta` is a declared edge offset;
- `e[k]` is model residual.

Given observed `h[k]`, the response is linear in `gamma_p,gamma_r`, so
`SharpnessPlant` uses forgetting-factor RLS with feature vector

```text
[g[k], -max(eta[k]*h[k]-theta[k], 0)].
```

```python
from bridgelearn import SharpnessPlant

plant = SharpnessPlant(
    gamma_p=1e-3,
    gamma_r=0.2,
    safety_offset=0.1,
    forgetting=0.995,
    residual_quantile=0.95,
    uncertainty_scale=2.5,
)

funnel = plant.update(
    previous_curvature=h_previous,
    current_curvature=h_current,
    step_size=eta_previous,
    momentum=mu_previous,
    progress_signal=squared_update_norm,
)
```

The object is blockwise even when initialized from scalars.

## 5. Robust curvature funnels

`CurvatureFunnel` contains

```text
h_lower <= h_center <= h_upper.
```

The interval combines parameter uncertainty and an empirical residual
quantile. `SharpnessPlant.predict_step()` propagates interval endpoints and the
edge kink by scalar interval/corner evaluation.

The control contract is asymmetric:

```text
stability promise: use h_upper
contraction promise: use h_lower.
```

This prevents certainty-equivalence inversion from claiming progress at an
optimistic curvature while checking stability at the same optimistic point.

A wide funnel is a confidence failure, not permission to average the bounds.
`SharpnessAwareReferenceBridgePlanner` can then:

- extend the horizon;
- hold the block;
- fall back to a trust-region command;
- permit a bounded identification probe.

## 6. Two-timescale planning

Sharpness is intentionally not inserted into the bridge state. The bridge still
solves covariance steering under a declared linear-Gaussian reference. During
each candidate-horizon test, the planner rolls the scalar sharpness plant
forward under the candidate controls:

```text
for j in candidate horizon:
    project bridge transition j through actuator using h_lower[j]
    reject if projection is infeasible
    reject if eta[j]*h_upper[j] crosses edge
    update sharpness funnel to j+1
    update predicted covariance and lag covariance
```

This is sequential substitution, not a joint nonlinear solve. The cost is
linear in candidate horizon and block count.

```python
from bridgelearn import SharpnessAwareReferenceBridgePlanner

planner = SharpnessAwareReferenceBridgePlanner(
    terminal_variance=[5e-3],
    total_steps=4000,
    reference_policy=reference_policy,
    probe_policy=probe_policy,
    sharpness_model=plant,
    max_relative_funnel_width=0.75,
    freeze_on_inadequacy=True,
)
```

By default, the full candidate horizon is rolled forward. Set
`sharpness_rollout_steps` only as an explicit approximation.

## 7. Curvature-model adequacy ladder

The implementation supplies three nested models:

1. `StaticLinearCurvatureModel`;
2. `SharpnessPlant`;
3. `GainScheduledSharpnessModel`, with local responses blended by edge margin.

`CurvatureAdequacyObserver` tracks normalized one-step error and interval
coverage. `CurvatureModelLadder` selects the shortest adequate description.
If none is adequate, the controller should use the independent trust-region
cap and stop making model-based covariance-progress promises.

`SharpnessJumpDetector` handles discontinuities. A sufficiently large relative
or absolute jump latches the detector, invalidates the current funnel, and
requires reset/re-identification. Catapult events are detected, not fitted by a
smooth plant.

## 8. Order-2 persistent excitation

For a stationary AR(2) process, the regressor moment matrix is approximately

```text
M = gamma0 * [[1, rho1],
              [rho1, 1]].
```

In a cold overdamped regime, `rho1` approaches one. The direction associated
with `c1-c2` is weakly identified. Increasing white-noise amplitude scales
signal and process innovation together and does not fundamentally reshape this
regressor geometry.

An alternating probe

```text
+delta, -delta
```

places excitation near the Nyquist frequency and targets the starved contrast
direction. `AntitheticProbePolicy` guarantees an exact committed pair: once
`+delta` is accepted, `-delta` is issued next even if confidence improves.

```python
from bridgelearn import AntitheticProbePolicy

probe = AntitheticProbePolicy(
    contrast_se_threshold=0.04,
    condition_threshold=500.0,
    cold_variance=1e-2,
    max_realized_variance=2e-5,
    max_total_realized_variance=2e-3,
    amplitude_levels=(0.5, 1.0),
)
```

The two amplitudes provide a minimal local check for response curvature. The
policy triggers from `contrast_standard_error` and `regressor_condition`
metadata and optionally uses `lyapunov_condition` to deflate its budget.

### 8.1 No double counting

For antithetic probes, `ProbeDecision` distinguishes:

- `transition`: total desired transition including probe disturbance;
- `actuator_transition`: transition to be realized by ordinary controls;
- `external_innovation`: innovation supplied by the signed probe itself.

A PyTorch or custom adapter must apply `probe_signal` exactly once. Batch/noise
selection must realize only `actuator_transition`.

## 9. Lyapunov-adapted covariance diagnostics

For momentum, covariance error is matrix-valued:

```text
E[k+1] = A[k] E[k] A[k].T + Delta[k].
```

Companion matrices can be non-normal. Spectral radius below one does not rule
out substantial transient amplification in Euclidean norm.

`lyapunov_metric(c1,c2)` chooses `rho_bar` above the spectral radius and solves

```text
rho_bar**2 * P - A.T @ P @ A = Q,    P > 0.
```

The covariance norm is

```text
||E||_P = ||P**(1/2) E P**(1/2)||_F.
```

The condition number `kappa(P)` quantifies the cost of converting back to a
Euclidean bound. It grows near repeated roots/Jordan behavior and is exposed as
a first-class diagnostic and actuator guard.

`companion_small_gain_bound()` evaluates the conditional inequality

```text
rho_bar**2 + L_P < 1
```

and reports

```text
sqrt(kappa(P)) * d_max / (1 - rho_bar**2 - L_P).
```

This is conditional on the declared disturbance Lipschitz bound; it is not a
general adaptive-control theorem.

## 10. Momentum actuator

`MomentumStepBatchActuator` realizes a scalar bridge transition by searching a
bounded momentum grid. For each candidate `mu`, it derives a step from the
requested contraction, checks the lower/upper curvature funnel asymmetrically,
and selects a shared effective batch from a discrete compute-priced set.

Key constraints include:

- margin-shrunk Jury triangle;
- upper-funnel edge threshold;
- maximum spectral radius;
- maximum Lyapunov condition number;
- step and momentum slew limits;
- observer-derived coefficient slew;
- underdamped `sqrt(mu)` cooling floor;
- integer accumulation/batch values and deadband;
- shared dominant-sharpness scaling.

```python
from bridgelearn import MomentumStepBatchActuator

actuator = MomentumStepBatchActuator(
    step_bounds=(1e-6, 2e-3),
    momentum_bounds=(0.0, 0.95),
    batch_values=(32, 64, 128, 256, 512),
    control_momentum=True,
    max_spectral_radius=0.995,
    max_lyapunov_condition=1e4,
    max_log_step_change=0.2,
    max_momentum_change=0.02,
    compute_price=2e-3,
)
```

A subtle implementation requirement is that stability diagnostics must be
recomputed after any shared global scaling. Reducing a step is not always more
contractive under momentum: it can move a dominant pole toward `+1`.

## 11. Shared dominant sharpness

Per-block curvature estimates are not independent because the top Hessian
mode is a property of the joint loss. `DominantSharpnessCoordinator` computes a
max or soft-max edge utilization across blocks and scales commands when a
shared edge would otherwise be crossed.

This is a conservative safety channel. It does not identify the coupled
cross-block Hessian dynamics.

## 12. PyTorch contract

When `MomentumStepBatchActuator` is used, `TorchGroupStatistics` must provide:

- current variance;
- previous variance;
- lag covariance;
- curvature center, lower, and upper bounds;
- noise scale;
- momentum;
- structural adequacy;
- optional contrast SE, regressor condition, and Lyapunov condition;
- optional coefficient slew limit.

`TorchOptimizerAdapter` refuses momentum/Adam active control without a
structural diagnostic unless `allow_first_order_momentum=True` is explicitly
set. Adam beta1 changes additionally require `allow_beta1_control=True`.

## 13. Checkpointing

The following v0.3 objects expose state suitable for controller checkpoints:

- `SharpnessPlant`;
- `GainScheduledSharpnessModel`;
- `CurvatureAdequacyObserver`;
- `SharpnessJumpDetector`;
- `CurvatureModelLadder`;
- `ForgettingFactorAR2Observer`;
- `AntitheticProbePolicy`;
- `SharpnessAwareReferenceBridgePlanner`.

An interrupted antithetic pair must be restored so the negative pulse is not
lost.

## 14. Failure semantics

The library distinguishes:

- **infeasible transition:** extend horizon or project explicitly;
- **wide funnel:** confidence failure;
- **structural inadequacy:** fall back from gray-box control;
- **catapult jump:** latch guard and re-identify;
- **ill-conditioned companion dynamics:** reduce allowed commands or hold;
- **probe budget exhausted:** slow/hold rather than probing without accounting;
- **shared edge violation:** scale all participating blocks and recompute roots;
- **unreachable cooling under momentum:** lower momentum or pay more updates.

These states should appear in traces and scientific reports rather than being
hidden by clipping.

## 15. Deliberate limitations

The current bridge itself is scalar/diagonal. The companion actuator uses
second-order local dynamics to realize and guard scalar marginal targets, but
it is not yet an exact finite-horizon bridge over the full augmented covariance
of `[z,v]`. That extension is a future research target.
