# Migrating BridgeLearn 0.2 integrations to 0.3

Version 0.3 is source-compatible with ordinary first-order v0.2 channels. The
new requirements apply when momentum, Adam beta1, or dynamic sharpness control
is enabled.

## 1. Keep first-order channels unchanged when appropriate

SGD without momentum, predictive-coding relaxation, and explicit-noise
recurrent channels may continue to use:

- `ReferenceBridgePlanner`;
- `StepBatchActuator`, `StepNoiseActuator`, or `StepOnlyActuator`;
- scalar `LocalDynamics` without lag covariance.

## 2. Replace static curvature response with a funnel

Old v0.2 integrations often supplied:

```python
curvature=h
curvature_slope=slope
```

A v0.3 momentum integration should instead update `SharpnessPlant` and supply:

```python
curvature=funnel.center
curvature_lower=funnel.lower
curvature_upper=funnel.upper
curvature_adequacy=funnel.confidence
```

The static slope remains supported as a fallback/ablation.

## 3. Supply second-order state summaries

`MomentumStepBatchActuator` requires:

```python
previous_variance=...
lag_covariance=...
momentum=...
```

For each block, `lag_covariance` is the adjacent cross-covariance associated
with the centered state. It is not a raw uncentered parameter dot product.

## 4. Use structural adequacy

Replace an AR(1)-only gate with gray-box-versus-black-box adequacy:

```python
gray = GrayBoxMomentumObserver(...).estimate(...)
adequacy = StructuralAR2AdequacyObserver().estimate(
    ...,
    curvature=gray.curvature,
)
```

Pass `adequacy.confidence` as `structural_adequacy`.

## 5. Derive command slew from observer bandwidth

When the gray-box map is not adequate and `ForgettingFactorAR2Observer` is used,
pass its reported `coefficient_slew_limit` into `LocalDynamics` or
`TorchGroupStatistics`. Do not leave the actuator free to move the plant faster
than the observer can track.

## 6. Replace white cold probes for momentum identification

`ConfidenceProbePolicy` remains appropriate for first-order channels. Momentum
channels should normally use `AntitheticProbePolicy` and provide:

```python
contrast_standard_error=...
regressor_condition=...
lyapunov_condition=...
```

The adapter must implement `probe_signal` application. Do not map the explicit
probe back into batch innovation; v0.3 separates those paths.

## 7. Use the companion actuator

Replace:

```python
StepBatchActuator(...)
```

with:

```python
MomentumStepBatchActuator(...)
```

for validated heavy-ball/momentum channels. Choose whether momentum is a
controller actuator with `control_momentum`. For Adam, beta1 control remains
disabled by default even when companion diagnostics are enabled.

## 8. Upgrade the planner only after the plant is calibrated

`SharpnessAwareReferenceBridgePlanner` should be enabled after shadow-mode
sharpness identification. Until then, retain `ReferenceBridgePlanner` and use a
trust-region cap.

## 9. Handle jumps explicitly

Add `SharpnessJumpDetector`. When latched:

- freeze bridge progress;
- invalidate the funnel/model adequacy;
- return to baseline trust-region controls;
- collect a new identification window;
- reset the detector only after the new model is calibrated.

## 10. Checkpoint pair state

Controller checkpoints move to version 3. Preserve the state of the antithetic
probe policy. Restoring after `+delta` must still issue the matching `-delta`.

## 11. Re-run shadow calibration

Do not activate v0.3 by loading v0.2 observer statistics and assuming they are
compatible. The centering convention, lag covariance, gray-box regression,
sharpness funnel, and companion condition number must be calibrated under the
actual optimizer and block partition.
