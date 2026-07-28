# BridgeLearn 0.3 critique response

This file records how the software responds to the two new technical critiques:

1. edge-of-stability curvature should be modeled as a slow plant rather than a
   static `h(eta)` curve;
2. momentum identification and stability require order-2 excitation,
   gray-box command deconfounding, and companion-aware small-gain diagnostics.

The changes preserve the v0.2 reference-consistent bridge and compute-accounted
control design.

## Summary

| Suggestion | Assessment | v0.3 response |
|---|---|---|
| Promote curvature to a slow state | Accepted | Added `SharpnessPlant` with RLS-identified progressive-sharpening and edge-restoration rates. |
| Do not place sharpness inside the bridge state | Accepted | Added two-timescale `SharpnessAwareReferenceBridgePlanner`; sharpness is rolled forward as a predicted disturbance. |
| Use an interval/funnel rather than certainty equivalence | Accepted | Added `CurvatureFunnel`; stability uses `h_upper`, contraction inversion uses `h_lower`. |
| Add static/plant/LPV model ladder | Accepted | Added `StaticLinearCurvatureModel`, `SharpnessPlant`, `GainScheduledSharpnessModel`, `CurvatureAdequacyObserver`, and `CurvatureModelLadder`. |
| Detect catapult events instead of fitting through them | Accepted | Added latching `SharpnessJumpDetector`. |
| Add a shared dominant-sharpness channel | Accepted as a conservative guard | Added max/soft-max `DominantSharpnessCoordinator`; full cross-block Hessian dynamics remain open. |
| White probing is not persistent excitation of order 2 | Accepted | Added exact committed antithetic `+delta,-delta` probing at two amplitudes. |
| Trigger probing from `c1-c2` uncertainty/condition, not generic confidence alone | Accepted | `AntitheticProbePolicy` uses contrast SE, regressor condition, cold-width gate, and optional Lyapunov conditioning. |
| Deconfound known time-varying commands | Accepted | Added `GrayBoxMomentumObserver` based on reconstructed `zeta`; step, momentum, and batch commands are removed algebraically. |
| Handle errors in variables | Accepted conditionally | Added optional deeper-lag instrumental-variable mode; instrument validity remains an application assumption. |
| Use black-box AR(2) as an adequacy diagnostic | Accepted | Added `StructuralAR2AdequacyObserver`; gray-box control is gated by prediction agreement. |
| Quantify observer/control timescale separation | Accepted | `ForgettingFactorAR2Observer` reports an effective-memory-derived coefficient-slew contract. |
| Replace scalar small-gain reasoning with companion/Lyapunov geometry | Accepted | Added companion roots, Jury triangle, Lyapunov metric, condition number, common-metric grid check, and conditional small-gain report. |
| Account for non-normal transient amplification | Accepted | `lyapunov_condition` is a trace/actuator/probe diagnostic and can reject ill-conditioned commands. |
| Momentum imposes an underdamped cooling floor | Accepted | `MomentumStepBatchActuator` checks `sqrt(mu)` reachability and may lower momentum or force horizon extension. |
| Treat time-varying companion stability explicitly | Partly accepted | Added coefficient slew plus finite-grid common-Lyapunov verification. A general online LMI solver is not bundled. |

## 1. Dynamic sharpness plant

The v0.2 static response

```text
h(eta) = h0 + slope*(eta-eta0)
```

is retained only as a calibrated local fallback. The default v0.3 dynamic model
is

```text
h_next = h
       + gamma_p * progress_signal
       - gamma_r * max(eta*h - (2*(1+mu)-delta), 0)
       + residual.
```

`gamma_p` and `gamma_r` enter linearly, so `SharpnessPlant.update()` identifies
them by forgetting-factor RLS. The plant is one scalar state and two identified
rates per block.

The implementation deliberately does not claim that this is a universal law of
neural sharpness. It is a calibrated phenomenological plant whose adequacy must
be measured by one-step prediction and interval coverage.

## 2. Funnel-based robust inversion

`CurvatureFunnel` carries lower, center, and upper sharpness predictions.
`SharpnessAwareReferenceBridgePlanner` propagates the interval through the
candidate horizon. The actuator uses:

```text
h_lower -> requested contraction inversion
h_upper -> edge/Jury/stability constraint
```

A candidate is rejected when the upper funnel crosses the safety edge, the
relative interval becomes too wide, or the curvature model is inadequate. This
routes model uncertainty into the existing horizon/hold/probe mechanisms rather
than silently clipping a certainty-equivalent command.

## 3. Two-timescale MPC

Sharpness is not folded into the Schrödinger bridge covariance state. For each
candidate remaining horizon, the planner:

1. solves the same reference-consistent finite-horizon bridge;
2. realizes each desired transition against the current lower sharpness bound;
3. checks stability at the upper bound;
4. rolls the scalar sharpness plant forward;
5. advances predicted variance and lag covariance;
6. accepts only a feasible, calibrated candidate.

The computation is sequential and scalar per block. It does not introduce a
joint nonlinear covariance/sharpness optimization.

## 4. Model ladder and jump semantics

`CurvatureAdequacyObserver` compares one-step prediction error and funnel
coverage for three nested descriptions:

1. static linear response;
2. dynamic sharpness plant;
3. gain-scheduled local models indexed by edge margin.

`CurvatureModelLadder` uses the shortest adequate model. If none is adequate,
the safe floor is trust-region-only movement control with held/slowed bridge
progress.

`SharpnessJumpDetector` treats a catapult-like discontinuity as a regime
change. It latches a guard, invalidates the smooth funnel, and requires
re-identification. The software does not attempt to fit the discontinuity with
an ever-higher-order response curve.

## 5. Gray-box momentum identification

The v0.3 observer uses the known command sequence:

```text
zeta[k] = ((1+mu[k])*z[k] - mu[k]*z[k-1] - z[k+1]) / eta[k]
        = h*z[k] + xi[k].
```

This removes command variation before regression. Batch-weighted residuals
estimate unit-batch noise. Optional deeper-lag instruments address noisy
centered-state regressors.

The black-box AR(2) model is demoted to an adequacy check. This makes failures
such as fast Adam preconditioner motion or non-quadratic drift visible as a
structural confidence loss.

## 6. Persistent excitation of order 2

A generic white probe is retained for first-order channels but is no longer the
recommended momentum-identification probe. `AntitheticProbePolicy`:

- emits exact committed `+delta,-delta` pairs;
- cycles two amplitude levels;
- gates on `c1-c2` standard error and regressor condition;
- budgets predicted realized width disturbance;
- deflates the budget by `sqrt(kappa_P)` when the Lyapunov condition is known;
- stores in-progress pair state in checkpoints.

The probe's explicit innovation is separated from ordinary actuator innovation.
The planner and adapter therefore do not double count it through batch control.

## 7. Companion stability and small gain

The momentum plant is represented by

```text
A = [[c1,c2],[1,0]].
```

The software now exposes:

- roots and spectral radius;
- Jury triangle margins;
- damping regime;
- momentum edge margin;
- Lyapunov-adapted covariance metric;
- `cond(P)` as a non-normal transient-amplification diagnostic;
- finite-grid common-metric verification;
- a conditional ISS/small-gain report.

The small-gain object is explicitly conditional on a supplied disturbance
Lipschitz bound. It replaces the previous scalar heuristic but is not presented
as a universal adaptive-control proof.

## 8. Reachability under momentum

In the underdamped region, the pole radius is `sqrt(mu)`, independent of step
size. `MomentumStepBatchActuator` treats this as a reachability constraint.
When the bridge asks for faster cooling, the controller must:

- reduce momentum and cross toward the overdamped region;
- extend the physical horizon;
- or report infeasibility.

Annealing momentum is therefore an explicit control/compute tradeoff rather
than an unmodeled schedule convention.

## 9. Cross-block sharpness

`DominantSharpnessCoordinator` computes max or soft-max edge utilization and
can bind all participating blocks to a shared safety margin. This addresses the
fact that the globally dominant Hessian mode can migrate across parameter
blocks.

This is not a full coupled sharpness model. Cross-block Hessian dynamics and
optimal allocation of edge margin remain future work.

## 10. PyTorch/Adam policy

`TorchOptimizerAdapter` now carries structural adequacy, previous variance, lag
covariance, curvature funnel, contrast SE, regressor condition, Lyapunov
condition, and coefficient slew. Momentum/Adam channels require a structural
adequacy signal by default.

`MomentumStepBatchActuator` can control momentum for SGD. Adam beta1 control is
disabled unless the user explicitly sets `allow_beta1_control=True`. The safe
first CAROM deployment remains shadow mode with fixed beta1 until the companion
model is calibrated.

## 11. What remains deliberately unresolved

- The bridge path itself is still scalar/diagonal; v0.3 is not an exact
  augmented-state 2x2 Schrödinger bridge.
- The globally optimal dual-control probe schedule is not solved.
- A finite-grid common-Lyapunov check is not a general robust LMI certificate.
- The sharpness plant is phenomenological and may be rejected by its adequacy
  gate.
- Adam beta2/preconditioner motion can invalidate the heavy-ball gray-box map.
- The dominant-sharpness channel is conservative and does not model full
  cross-block Hessian coupling.

These are now explicit diagnostics and fallback states rather than silent
assumptions.
