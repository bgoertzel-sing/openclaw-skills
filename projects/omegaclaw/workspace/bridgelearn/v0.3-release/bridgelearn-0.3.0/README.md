# BridgeLearn 0.3.0

**BridgeLearn** is an experimental, backend-neutral control layer for iterative
learning and inference systems. It replaces a fixed learning-rate curve with a
reference-consistent, finite-horizon covariance-steering problem and then
projects the requested transition onto the controls exposed by the learning
system.

```text
identified reference dynamics + terminal intent
        -> finite-horizon linear-Gaussian bridge
        -> desired cross-time contraction and innovation
        -> sharpness/momentum-aware feasibility projection
        -> learning-rate, momentum, batch, damping, or explicit-noise controls
        -> calibrated observation, probing, and receding-horizon replanning
```

The core package does not require gradients. A channel can represent
backpropagated weights, a predictive-coding activity state, a local Hebbian
update, a fixed-point residual, an RL actor or critic, or a recurrent subsystem
such as CAROM.

Version 0.3.0 extends the reference-consistent v0.2 design in two places that
are first-order for realistic momentum training:

1. curvature is promoted from a static response curve to a slow, identified
   **sharpness plant** with a robust prediction funnel;
2. momentum channels are treated as companion-form AR(2) systems, with
   gray-box identification, order-2 persistent excitation, stability-triangle
   constraints, and non-normal transient-amplification diagnostics.

The package remains alpha research software. The safe deployment sequence is
`shadow -> calibrate -> adequacy gate -> bounded active ablation`.

## Why this is not another scheduler

OneCycle-style schedules prescribe a learning rate as a function of update
index. BridgeLearn instead separates four objects:

1. **Path:** what active stochastic width should be reached at each intrinsic
   bridge time?
2. **Coupling:** how much of the next state should remember the current state?
3. **Actuation:** which learning rate, momentum, batch, damping, or noise command
   realizes that transition?
4. **Clock:** how quickly is the requested path physically reachable under the
   current plant, confidence, and compute limits?

For a scalar first-order channel,

```text
z[k+1] = a[k] z[k] + epsilon[k],       Var(epsilon[k]) = r[k]
V[k+1] = a[k]**2 V[k] + r[k].
```

For a heavy-ball or momentum channel,

```text
z[k+1] = c1[k] z[k] + c2[k] z[k-1] + epsilon[k+1]
c1[k]  = 1 + mu[k] - eta[k] h[k]
c2[k]  = -mu[k].
```

The bridge asks for a covariance transition. The actuator decides whether that
transition is reachable and how to realize it. Marginal width is therefore not
identified with learning rate.

## Release highlights

### Reference-consistent finite-horizon bridges

`LinearGaussianBridgePath` and `ReferenceBridgePlanner` derive both marginal
variances and cross-time transitions from the same declared scalar/diagonal
linear-Gaussian reference. The legacy Brownian path remains available for
scientific ablations and for explaining OneCycle-like covariance humps, but it
is not the recommended operational controller.

### Dynamic sharpness plant

Edge-of-stability sharpness is modeled as a slow state rather than as a static
function of the current step size:

```text
h[k+1] = h[k]
       + gamma_p * g[k]
       - gamma_r * max(eta[k] * h[k] - theta[k], 0)
       + model_error,

theta[k] = 2 * (1 + mu[k]) - safety_offset.
```

`SharpnessPlant` identifies `gamma_p` and `gamma_r` by forgetting-factor
recursive least squares. `CurvatureFunnel` propagates a lower, center, and upper
sharpness forecast. Planning is asymmetric:

- stability and the edge margin are checked at the upper bound;
- promised contraction is evaluated at the lower bound.

`SharpnessAwareReferenceBridgePlanner` rolls this plant forward over each
candidate remaining horizon. Sharpness is a predicted disturbance, not another
component of the bridge state, so planning remains scalar and sequential.

### Model ladder and discontinuity handling

The curvature layer includes:

- `StaticLinearCurvatureModel` for a calibrated local response;
- `SharpnessPlant` for slow progressive sharpening and edge restoration;
- `GainScheduledSharpnessModel` for local responses indexed by edge margin;
- `CurvatureAdequacyObserver` to select the shortest calibrated model;
- `CurvatureModelLadder` to apply the selected model;
- `SharpnessJumpDetector` to detect catapult-like discontinuities and force
  re-identification rather than fitting a smooth model through a jump;
- `DominantSharpnessCoordinator` to impose a shared global edge constraint when
  the block that binds stability can change.

If no model is adequate, the intended fallback is trust-region-only movement
control with the bridge clock held or slowed.

### Gray-box momentum identification

Known step-size, momentum, and batch commands are removed algebraically before
estimating the plant. `GrayBoxMomentumObserver` reconstructs

```text
zeta[k] = ((1 + mu[k]) z[k] - mu[k] z[k-1] - z[k+1]) / eta[k]
        = h z[k] + xi[k]
```

and estimates curvature and unit-batch gradient-noise scale by weighted least
squares. An optional deeper-lag instrumental-variable mode mitigates
errors-in-variables from noisy centered-state observations.

The black-box AR(2) fit remains useful as an adequacy diagnostic:
`StructuralAR2AdequacyObserver` compares gray-box and black-box one-step
predictions. `ForgettingFactorAR2Observer` is the fallback when the declared
structural map is not trustworthy; it also exposes an identification-bandwidth
slew contract for the actuator.

### Order-2 antithetic probing

White probing can raise signal above a measurement floor, but it does not repair
the weak AR(2) contrast direction in cold, highly correlated regimes.
`AntitheticProbePolicy` emits an exact committed pair

```text
+delta, -delta
```

with two configurable amplitude levels. The pair is mean-zero over two updates,
concentrates excitation near the Nyquist frequency, and is triggered by the
standard error of `c1-c2` or by the regressor condition number. The policy
budgets predicted realized width disturbance, deflated by the square root of a
Lyapunov condition number when supplied.

The explicit probe signal is separated from ordinary actuator innovation so it
is not purchased twice through batch or state-noise control.

### Companion stability and non-normality

`stability.py` provides:

- exact companion roots and spectral radius;
- Jury stability-triangle margins;
- over/critical/underdamped classification;
- the momentum edge margin `2*(1+mu) - eta*h`;
- the underdamped contraction floor `sqrt(mu)`;
- a Lyapunov-adapted covariance norm;
- finite-grid common-Lyapunov verification;
- a conditional companion small-gain report.

`MomentumStepBatchActuator` searches a bounded momentum grid and jointly chooses
step size, momentum, and a shared compute-priced effective batch. It checks the
upper sharpness funnel, stability triangle, spectral-radius cap, Lyapunov
conditioning, coefficient slew, integer batch choices, and the underdamped
cooling floor.

### Explicit compute and calibration

Shared batch or accumulation is discrete and priced. The controller reports
optimizer updates, example-equivalent compute, intrinsic progress, progress per
compute unit, resource saturation, probe expenditure, and one-step prediction
error. `CalibrationReport` summarizes bias, MAE, RMSE, correlation, residual
quantiles, and interval coverage.

## Installation

From the wheel:

```bash
python -m pip install bridgelearn-0.3.0-py3-none-any.whl
```

From source:

```bash
python -m pip install -e .
```

The core dependency is NumPy. Optional extras are available for PyTorch,
plotting, and development:

```bash
python -m pip install -e '.[torch]'
python -m pip install -e '.[dev]'
```

## Minimal first-order channel

The v0.2 first-order path remains useful for SGD without momentum and for
relaxation dynamics:

```python
from bridgelearn import (
    BridgeController,
    Channel,
    DynamicsAdapter,
    FixedReferencePolicy,
    GaussianTransition,
    LocalDynamics,
    ReferenceBridgePlanner,
    StepBatchActuator,
)

reference = GaussianTransition(
    contraction=[0.995],
    innovation=[1e-3],
)

planner = ReferenceBridgePlanner(
    terminal_variance=[5e-3],
    total_steps=200,
    reference_policy=FixedReferencePolicy(reference),
    max_horizon_multiplier=32.0,
)


def read_dynamics(system):
    return LocalDynamics(
        variance=[system.active_variance],
        curvature=[system.curvature],
        noise_scale=[system.unit_batch_noise],
        step_size=[system.step_size],
        effective_batch=system.effective_batch,
        confidence=[system.observer_confidence],
        trust_region_step=[system.trust_region_step],
    )


def apply_controls(system, controls):
    system.step_size = float(controls["step_size"][0])
    system.effective_batch = float(controls["effective_batch"])


adapter = DynamicsAdapter(
    read_dynamics=read_dynamics,
    apply_controls=apply_controls,
    actuator=StepBatchActuator(
        step_bounds=(1e-5, 0.2),
        batch_values=(16, 32, 64, 128, 256, 512),
        compute_price=0.004,
        resource_deadband=0.06,
    ),
)

controller = BridgeController(
    {
        "weights": Channel(
            name="weights",
            adapter=adapter,
            planner=planner,
        )
    },
    mode="shadow",  # change to "active" only after calibration
)
```

## Momentum/sharpness-aware configuration

The following fragment shows the intended object graph. A real integration must
supply centered state histories, lag covariance, and a callback that applies an
explicit antithetic probe in the same coordinate used by the observer.

```python
from bridgelearn import (
    AntitheticProbePolicy,
    DominantSharpnessCoordinator,
    FixedReferencePolicy,
    GaussianTransition,
    MomentumStepBatchActuator,
    SharpnessAwareReferenceBridgePlanner,
    SharpnessPlant,
)

sharpness = SharpnessPlant(
    gamma_p=1e-3,
    gamma_r=0.2,
    safety_offset=0.1,
    forgetting=0.995,
    uncertainty_scale=2.5,
)

probe = AntitheticProbePolicy(
    contrast_se_threshold=0.04,
    condition_threshold=500.0,
    cold_variance=1e-2,
    max_realized_variance=2e-5,
    max_total_realized_variance=2e-3,
    amplitude_levels=(0.5, 1.0),
)

planner = SharpnessAwareReferenceBridgePlanner(
    terminal_variance=[5e-3],
    total_steps=4_000,
    reference_policy=FixedReferencePolicy(
        GaussianTransition(contraction=[0.99], innovation=[1e-4])
    ),
    probe_policy=probe,
    sharpness_model=sharpness,
    max_relative_funnel_width=0.75,
    freeze_on_inadequacy=True,
)

actuator = MomentumStepBatchActuator(
    step_bounds=(1e-6, 2e-3),
    momentum_bounds=(0.0, 0.95),
    batch_values=(32, 64, 128, 256, 512),
    control_momentum=True,
    safety_offset=0.1,
    max_spectral_radius=0.995,
    max_lyapunov_condition=1e4,
    compute_price=2e-3,
    dominant_coordinator=DominantSharpnessCoordinator(
        safety_offset=0.1,
        maximum_utilization=0.95,
    ),
)
```

At every control interval, update the sharpness plant from consecutive
curvature observations:

```python
funnel = sharpness.update(
    previous_curvature=previous_h,
    current_curvature=current_h,
    step_size=previous_eta,
    momentum=previous_mu,
    progress_signal=squared_update_norm,
)

statistics = {
    **funnel.local_dynamics_kwargs(),
    "structural_adequacy": structural_confidence,
    "coefficient_slew_limit": ar2_rls.slew_limit,
}
```

The planner then forecasts the funnel through each candidate horizon and
rejects a candidate before it walks into predicted progressive sharpening.

## PyTorch integration

`bridgelearn.integrations.torch.TorchOptimizerAdapter` associates one bridge
block with each optimizer parameter group. It wraps an ordinary optimizer; it
does not own the training loop.

For momentum or Adam-like optimizers, the default gate requires a structural
adequacy score. In companion mode, `previous_variance` and `lag_covariance` are
also required. Adam `beta1` control is disabled unless explicitly enabled.

```python
from bridgelearn.integrations.torch import (
    TorchGroupStatistics,
    TorchOptimizerAdapter,
)


def statistics(context):
    return TorchGroupStatistics(
        variance=context.width,
        previous_variance=context.previous_width,
        lag_covariance=context.lag_covariance,
        curvature=context.curvature_funnel.center,
        curvature_lower=context.curvature_funnel.lower,
        curvature_upper=context.curvature_funnel.upper,
        curvature_adequacy=context.curvature_funnel.confidence,
        noise_scale=context.unit_batch_noise,
        effective_batch=context.effective_batch,
        structural_adequacy=context.structural_adequacy,
        momentum=context.momentum,
        contrast_standard_error=context.contrast_standard_error,
        regressor_condition=context.regressor_condition,
        lyapunov_condition=context.lyapunov_condition,
        coefficient_slew_limit=context.coefficient_slew_limit,
    )

adapter = TorchOptimizerAdapter(
    optimizer=optimizer,
    statistics=statistics,
    actuator=actuator,
    set_effective_batch=set_accumulation,
    apply_probe_signal=apply_antithetic_probe,
    allow_beta1_control=False,
)
```

A probe callback must inject the requested signed signal exactly once. The
controller already accounts for its innovation separately from the batch/noise
actuator.

## Predictive coding and fixed-point inference

Use an episodic channel for activity or residual relaxation. The first-order
`StepNoiseActuator` is often a better initial model than the momentum actuator:
step size or damping realizes contraction, while explicit state noise realizes
innovation and optional identification probes.

```python
with controller.episode("activities") as inference:
    while not inference.done:
        command = inference.plan(pc_state)
        inference.apply(pc_state, command)
        pc_state.relax_once()
        inference.after_step(pc_state, command)
```

Useful observables include precision-weighted activity width, prediction-error
width, and fixed-point residual width. Catapult/jump detection may also be used
for abruptly changing recurrent Jacobians.

## Backpropagation RL

The framework does not impose an RL algorithm. Typical persistent channels are:

- actor parameters;
- critic parameters;
- representation/encoder parameters;
- entropy-temperature parameters;
- target-network update dynamics.

Rollout collection, replay sampling, target-update cadence, and gradient
accumulation remain user-owned. This is important because those operations are
part of the plant and compute budget, not mere optimizer metadata.

## CAROM deployment sketch

The recommended CAROM split is:

1. dependency-edge and command-routing parameters;
2. shared operator attention/transform/gating parameters;
3. GLV inhibition, growth, fatigue, leak, and halt parameters;
4. workspace/readout and downstream execution parameters.

Use a shared dominant-sharpness coordinator across weight blocks because the
block that binds the global Hessian edge may change. Treat fixed-point workspace
relaxation and itinerant activity as separate episodic channels. Start in shadow
mode, calibrate the gray-box transition model and sharpness funnel through the
known failure window, and activate controls only for adequate blocks. See
`docs/CAROM_INTEGRATION.md`.

## Diagnostics and safe fallback ladder

A production-facing integration should record, per block:

- predicted and realized next width;
- gray-box and black-box one-step RMSE;
- structural and curvature adequacy;
- sharpness funnel width and upper-edge utilization;
- `c1-c2` standard error and AR(2) regressor condition;
- companion roots, damping regime, spectral radius, Jury margins, and
  Lyapunov condition number;
- command slew, resource saturation, probe cost, and intrinsic progress per
  compute unit;
- jump-detector state and selected curvature model.

The intended fallback ladder is:

```text
reference-consistent bridge + sharpness plant + companion actuator
    -> gain-scheduled curvature model
    -> static calibrated response
    -> trust-region-only movement control
    -> hold/freeze block and continue observing
```

A catapult-like jump invalidates the smooth funnel and should latch the guard
until re-identification.

## Validation status

The v0.3 source distribution includes 38 unit and closed-loop regression tests
covering:

- finite-horizon reference-consistent bridges;
- projector invariants and reference-planner state;
- sharpness-plant RLS identification and funnel propagation;
- model adequacy, gain scheduling, and jump latching;
- exact antithetic pairs, two amplitude levels, probe budget, and no double
  counting of explicit probe innovation;
- gray-box momentum identification, instrumental variables, structural
  adequacy, and forgetting-factor slew contracts;
- Jury stability, damping regimes, momentum cooling floors, Lyapunov metrics,
  common-metric checks, and small-gain diagnostics;
- companion-aware step/momentum/batch actuation, shared-edge scaling, and
  recomputation of stability after scaling;
- PyTorch structural gates and probe metadata;
- earlier robust-width, centering, integer-resource, delayed-observer, and
  calibration behavior.

No new scientific benchmark is claimed by this release. The next appropriate
step is a separate set of synthetic experiments specifically exercising the
new sharpness, probing, and momentum components.

## Current limitations

- The bridge path remains scalar/diagonal. Companion-aware actuation is not yet
  a full finite-horizon 2x2 augmented-state Schrödinger bridge.
- The sharpness plant is phenomenological. Its funnel is set-membership/RLS
  based, not a theorem that neural sharpness follows the model globally.
- The antithetic probe budget is bounded and accounted, but the globally optimal
  dual-control tradeoff is not solved.
- Instrumental variables require valid lag instruments; they do not eliminate
  every centering or subsampling bias.
- Adam preconditioner motion can invalidate the heavy-ball structural map. The
  structural adequacy gate is therefore mandatory by default.
- Common-Lyapunov verification is finite-grid unless the user supplies an
  external LMI certificate.
- Blockwise sharpness is coupled through the joint Hessian. The dominant-channel
  coordinator is a conservative guard, not a full cross-block curvature model.
- Covariance tracking is not sufficient evidence for generalization, basin
  selection, implicit regularization, or downstream task performance.

## Repository layout

```text
src/bridgelearn/
    paths.py            bridge marginals and transitions
    planners.py         receding-horizon and sharpness-aware planning
    actuators.py        step, batch, noise, and momentum realization
    sharpness.py        dynamic curvature plants and adequacy ladder
    identification.py   gray-box momentum and AR(2) fallback observers
    probing.py          white and antithetic identification probes
    stability.py        companion stability and Lyapunov diagnostics
    observers.py        generic transition/noise/curvature observers
    scales.py           centered and robust active-width estimators
    integrations/       optional framework adapters

docs/
    SHARPNESS_AND_MOMENTUM.md
    CAROM_INTEGRATION.md
    CRITIQUE_RESPONSE.md
    MIGRATION_0_3.md
```

## Scientific status

BridgeLearn is a falsifiable control framework, not a claim that neural-network
training is literally a Schrödinger bridge. Its scientific value depends on
one-step calibration, adequate plant identification, compute-matched
comparisons, and task-level measurements beyond covariance.
