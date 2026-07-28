# Changelog

## 0.3.0 - July 2026

Dynamic-sharpness and companion-momentum release.

- Promoted curvature from a static `h(eta)` response to an identified slow
  `SharpnessPlant` with progressive-sharpening and edge-restoration terms.
- Added `CurvatureFunnel` interval forecasts. Actuators invert at the lower
  bound while stability and edge constraints are checked at the upper bound.
- Added `SharpnessAwareReferenceBridgePlanner`, which rolls the sharpness plant
  through every candidate remaining horizon before accepting a bridge step.
- Added the curvature model ladder: static linear, dynamic plant,
  gain-scheduled/LPV, adequacy observer, jump detector, and trust-region fallback.
- Added a shared `DominantSharpnessCoordinator` for cross-block edge constraints.
- Added `GrayBoxMomentumObserver`, reconstructing the gradient sample under
  known time-varying step, momentum, and batch commands.
- Added optional deeper-lag instrumental variables for noisy centered-state
  observations.
- Added `StructuralAR2AdequacyObserver` and `ForgettingFactorAR2Observer`, with
  an explicit observer-bandwidth/command-slew contract.
- Added exact committed `+delta, -delta` antithetic probing with two amplitude
  levels, contrast-SE/condition triggers, Lyapunov-condition deflation, and
  realized-width budget accounting.
- Separated explicit probe innovation from ordinary batch/noise actuation to
  prevent double counting.
- Added companion-matrix roots, Jury stability margins, damping regimes,
  momentum edge margins, the underdamped `sqrt(mu)` contraction floor,
  Lyapunov-adapted covariance norms, common-metric checks, and conditional
  small-gain diagnostics.
- Added `MomentumStepBatchActuator` for blockwise step/momentum control and one
  shared compute-priced effective batch.
- Recomputed companion stability after shared dominant-sharpness scaling; this
  catches the fact that reducing the step can move a pole back toward `+1`.
- Extended the PyTorch adapter with structural adequacy, lag-covariance,
  sharpness-funnel, AR(2)-probe, optional beta1-control, and explicit-probe APIs.
- Added v0.3 checkpoint state for sharpness plants, model ladders, planners,
  probes, and fallback observers.
- Expanded the suite to 38 unit and adversarial closed-loop regression tests.

No new task-level benchmark is claimed in this release. Dedicated synthetic
sharpness/momentum experiments are intentionally deferred to the next testing
stage.

## 0.2.0 - July 2026

Critique-driven reference-consistency release.

- Added exact scalar/diagonal finite-horizon linear-Gaussian bridge paths.
- Added receding-horizon `ReferenceBridgePlanner` with remaining-horizon state.
- Added fixed, callback, filtered, and observed reference policies.
- Added bounded confidence-triggered innovation probing.
- Added local curvature-response inversion, trust-region caps, and
  edge-of-stability diagnostics.
- Added AR(2) adequacy diagnostics and a PyTorch momentum/Adam safety gate.
- Added explicit centering plus variance, trimmed, IQR, and MAD scales.
- Added compute-priced, quantized resource control with deadband/hysteresis.
- Added `CalibrationReport` and expanded trace/control-effort accounting.
- Added adversarial closed-loop, heavy-tail, AR(2), probe, curvature,
  calibration, and projector-property tests.
- Replaced the headline example with a compute-matched reference-consistent
  quadratic and retained Brownian control as a legacy ablation.

## 0.1.0 - July 2026

Initial research release.

- Added backend-neutral bridge paths, Gaussian KL transition projection,
  feasibility clocks, generic adapters, persistent/episodic channels, and
  scalar step/batch/noise actuators.
- Added PyTorch parameter-group integration and callback-based relaxation/local
  learning interfaces.
