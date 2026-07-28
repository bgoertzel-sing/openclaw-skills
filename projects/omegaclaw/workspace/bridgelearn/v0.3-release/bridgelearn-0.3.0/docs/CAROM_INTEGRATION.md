# CAROM integration plan for BridgeLearn 0.3

This note proposes a conservative BridgeLearn integration for CAROM. It
separates persistent weight control from episodic fixed-point and itinerant
state control. The first deployment should remain **shadow mode**: compute
commands, sharpness forecasts, companion diagnostics, and validation guards
without changing the optimizer or recurrent dynamics.

## 1. Why CAROM needs multiple channels

The CAROM evidence is not consistent with a single global optimization state.
Dependency-edge prediction remained strong while itinerary structure,
trajectory coverage, causal dependence, and downstream execution degraded.
The first weight partition should therefore separate:

1. dependency-edge and command-routing parameters;
2. shared operator attention/transform/gating parameters;
3. GLV inhibition, growth, fatigue, leak, and halt parameters;
4. workspace/readout and downstream execution parameters.

Each group should have an independent covariance state, terminal intent,
sharpness plant, adequacy score, and bridge clock. A shared dominant-sharpness
channel may still impose a global edge constraint.

## 2. Preserve reference consistency

Each weight channel should declare a conservative baseline command and derive
its reference transition from that command. The bridge path and cross-time
coupling must use the same local reference process.

For a first-order block:

```text
a_ref = 1 - eta_ref*h_ref
r_ref = eta_ref**2*nu_ref/batch_ref.
```

For a companion block, use the declared baseline `eta_ref,mu_ref` and identified
`h_ref` to form `c1_ref,c2_ref`; the current v0.3 path remains a scalar marginal
bridge, while the companion actuator realizes and guards the requested
transition.

Use `FixedReferencePolicy` for the cleanest initial experiment or
`FilteredReferencePolicy` for slow baseline drift. Do not use the last realized
controller command as the next reference in the primary experiment.

## 3. AdamW and momentum identification

CAROM currently uses AdamW, so first-order AR(1) control is not an acceptable
silent approximation. In shadow mode, collect per-block centered trajectories,
step sizes, beta1 values, and effective batches. Run:

- `GrayBoxMomentumObserver` for curvature/noise reconstruction;
- `StructuralAR2AdequacyObserver` against a black-box AR(2) fit;
- `ForgettingFactorAR2Observer` as a fallback and slew-rate estimator;
- companion root, Jury-margin, damping-regime, and Lyapunov-condition
  diagnostics.

The reconstructed regression is

```text
zeta[k] = ((1+mu[k])*z[k] - mu[k]*z[k-1] - z[k+1]) / eta[k]
        = h*z[k] + xi[k].
```

If centered-state measurements are noisy, use the deeper-lag IV option and
report the instrument choice. Low structural adequacy should freeze active
bridge steering for that block.

## 4. Dynamic sharpness rather than static `h(eta)`

Use one `SharpnessPlant` per weight block:

```text
h_next = h
       + gamma_p*progress_signal
       - gamma_r*max(eta*h - (2*(1+mu)-delta), 0)
       + residual.
```

A suitable first progress signal is squared preconditioned update norm. Do not
assume the model is valid because it is plausible: report one-step sharpness
prediction error and interval coverage.

`SharpnessAwareReferenceBridgePlanner` should roll the plant through candidate
remaining horizons. Reject a plan today when it would walk into progressive
sharpening later, even if it is feasible at the current curvature.

## 5. Robust funnel and shared edge

Supply `curvature_lower`, `curvature`, and `curvature_upper` to every weight
channel. The contraction command is derived from the lower bound, while
stability is checked at the upper bound.

CAROM blocks are not independent in the Hessian. Use
`DominantSharpnessCoordinator` across the four weight groups. A max coordinator
is the conservative initial choice; a low-temperature soft-max is a smoother
ablation. After shared scaling, recompute companion roots and conditioning.

## 6. Curvature adequacy ladder

The recommended ladder is:

1. calibrated static linear response;
2. dynamic `SharpnessPlant`;
3. gain-scheduled local response indexed by edge margin;
4. trust-region-only control when none is adequate.

`CurvatureAdequacyObserver` should use held-out one-step prediction windows.
`SharpnessJumpDetector` should latch after a catapult-like sharpness jump, freeze
bridge progress, return to conservative baseline commands, and collect a new
identification window.

## 7. Antithetic order-2 probes

Cold momentum blocks can lose identifiability in the `c1-c2` direction. A white
probe is insufficient as the main persistent-excitation mechanism. Use
`AntitheticProbePolicy` with exact `+delta,-delta` pairs and two amplitudes.

Recommended gates:

- cold active width;
- high standard error of `c1-c2`;
- high AR(2) regressor condition number;
- no active validation guard;
- remaining probe budget.

The probe must be injected in the same centered/preconditioned coordinate used
by the observer. Its signed signal must be applied exactly once. Log the
realized width perturbation and keep an interrupted pair in the checkpoint.

For an initial CAROM study, probes should be small, sparse, and restricted to a
shadow/calibration window before the historical failure region. Active probing
inside a validation collapse should be disabled.

## 8. Momentum reachability and compute

Use `MomentumStepBatchActuator` only for blocks with adequate companion models.
The actuator should:

- search a bounded momentum grid;
- enforce a shrunk Jury triangle;
- cap spectral radius and Lyapunov condition;
- use observer-derived coefficient slew;
- choose one shared discrete effective batch with a compute price;
- reject cooling faster than the underdamped `sqrt(mu)` floor.

If a terminal cooling request is infeasible, the controller must explicitly
lower momentum, extend the physical horizon, or hold. Extra optimizer updates,
examples, recurrent solver calls, and wall time must be charged and reported.

For AdamW, keep beta1 fixed in the first active experiment. Enabling beta1
control should be a separate preregistered ablation because Adam preconditioner
motion can violate the heavy-ball gray-box map.

## 9. Centering and active width

The controlled width is observer-relative. Declare the center filter and its
mixing time. A practical first weight observable is robust width in
Adam-preconditioned coordinates. Run ordinary variance alongside IQR/MAD or
trimmed variance in shadow mode. If rare jumps dominate variance, plan on the
robust width and retain ordinary variance as a diagnostic.

Record:

- center-filter alpha and effective mixing time;
- control interval;
- ratio of ordinary to robust scale;
- lag covariance and previous variance;
- one-step calibration by block.

## 10. Fixed-point workspace channel

Create an episodic channel for workspace residuals. The fixed-point screen
showed monotone contraction but non-negligible residual after the fixed sweep
budget, so adaptive inference depth is a natural BridgeLearn use.

Use `ResidualDecayObserver` or an empirical transition observer. The actuator
may control relaxation step/damping and explicit state noise. Terminate only
when both conditions hold:

1. the episodic bridge reaches its terminal neighborhood;
2. an absolute residual/utility guard is satisfied.

For momentum-like accelerated solvers, the same companion/AR(2) machinery can
be applied to residual histories, but only after the local structural map is
declared and calibrated.

## 11. Itinerant activity channel

Treat GLV mode activities as a separate episodic channel. Candidate observables
include:

- transversal robust width around the realized heteroclinic channel;
- itinerary entropy or distance from simplex vertices;
- dwell-time dispersion;
- innovation amplitude near saddles;
- halt-mode confidence.

`StepNoiseActuator` is appropriate when GLV state noise is explicit. Because
noise sets saddle-exit timing, report dwell-time and route statistics directly;
matching a covariance target is not enough. Every GLV integration step counts
as physical compute.

A sharpness/jump analogue may also be useful for recurrent Jacobian changes,
but it should be calibrated separately from the weight sharpness plant.

## 12. Validation guard

A CAROM-specific guard should freeze weight-channel progress after persistent
joint degradation on a fixed cached panel. Include:

- endpoint accuracy;
- itinerary coverage/order and exact transition recall;
- natural-minus-shuffled causal gap;
- held-out L5 performance;
- edge accuracy;
- routing entropy and GLV diagnostics;
- per-loss terms;
- sharpness, companion, and calibration metrics.

Do not trigger or select solely on edge accuracy. The historical run showed
that edge prediction can survive while routing/execution collapses.

## 13. Required trace artifacts

Every shadow or active run should emit per channel:

- target, predicted, and realized next width;
- one-step calibration report;
- gray-box and black-box RMSE;
- structural/curvature adequacy;
- sharpness funnel and edge utilization;
- companion roots, damping regime, Jury margins, spectral radius, and
  Lyapunov condition;
- `c1-c2` standard error and regressor condition;
- selected curvature model and jump latch;
- step, momentum, effective batch, saturation, and slew;
- probe signal, realized probe cost, and cumulative probe budget;
- intrinsic progress, physical updates, examples, recurrent evaluations,
  wall time, and progress per compute unit;
- task-level utility and causal trajectory metrics.

Without one-step calibration, a task outcome cannot be interpreted as evidence
for or against the bridge model.

## 14. Staged experiment plan

### Stage A: shadow identification

Run the original optimizer/schedule unchanged across several seeds. Collect the
new state histories and diagnostics through the old failure window. Fit and
compare static, dynamic, and gain-scheduled sharpness models. Test whether the
gray-box companion model is calibrated blockwise.

### Stage B: trust-region-only safety

Hold the original schedule but activate only the upper-funnel shared edge guard.
This isolates the benefit of dynamic sharpness prediction from covariance-path
tracking.

### Stage C: step-only bridge control

Use reference-consistent paths, fixed batch, fixed beta1, and blockwise step
control for adequate blocks. Match examples, updates, and wall time.

### Stage D: companion actuation

Permit SGD momentum or, in a separate Adam ablation, beta1 control. Test the
momentum cooling-floor prediction and horizon extension.

### Stage E: antithetic identification probes

Compare no probe, white probe, and two-amplitude antithetic probe under matched
realized perturbation budget. Primary identification outcomes are `c1-c2`
standard error, regressor condition, structural one-step calibration, and task
regret.

### Stage F: recurrent channels

Apply episodic BridgeLearn control to fixed-point sweeps or GLV activity only
after the weight-channel study is understood.

## 15. Scientific comparisons

Every comparison should be compute matched and report both mean optimization
and stochastic width. Include:

- OneCycle baseline;
- shadow BridgeLearn;
- trust-region-only dynamic-sharpness guard;
- reference-consistent first-order BridgeLearn;
- companion-aware BridgeLearn;
- probe ablations;
- legacy Brownian-path ablation.

Measure endpoint utility, causal trajectory evidence, sharpness proxies,
SWA-versus-iterate gap, basin/trajectory statistics, and calibration. A matched
covariance path does not imply matched implicit regularization or
generalization.

## 16. Current CAROM blockers

Before active deployment, require:

- stable centering convention;
- calibrated gray-box model in at least the intended controlled blocks;
- acceptable sharpness funnel coverage;
- bounded Lyapunov condition;
- declared beta1 policy;
- working signed-probe injection callback;
- checkpoint restoration of an in-progress probe pair;
- compute-matched validation guard and stop rule.

Until those gates pass, v0.3 should remain a diagnostic/shadow controller.
