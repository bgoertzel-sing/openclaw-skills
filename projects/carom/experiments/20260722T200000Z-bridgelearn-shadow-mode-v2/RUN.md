# BridgeLearn shadow-mode v2: per-update calibration

- Run ID: `20260722T200000Z-bridgelearn-shadow-mode-v2`
- Status: complete (timed command exit status 0)
- Question: Does matched per-update observation, HVP sharpness, split-batch
  innovation, and an AR(2) diagnostic make BridgeLearn sufficiently calibrated
  for an active CAROM control experiment?
- Relevant research rules: 1 (validate the estimator), 2 (freeze the shadow
  protocol), 5 (preserve reproducible evidence), and 7 (keep control behind the
  BridgeLearn adapter).

## Protocol

- Repository:
  `/home/openclaw/research-agent/projects/carom/repos/carom`
- Workspace branch/commit:
  `agent/chat-room-identity-phase1` / `ffdc2934e8006a27ed9e0f7d0e7137f8456833fd`
  in a shared dirty workspace. This runner and experiment are uncommitted; no
  existing CAROM or BridgeLearn file was modified.
- Environment: Python 3.10.12, BridgeLearn 0.3.0 from the dedicated venv,
  PyTorch 2.13.0+cpu, Linux x86_64, CPU only.
- CAROM: `scheduled`, `d=48`, `K=8`, seed 0, batch 128, 1,500 AdamW updates,
  OneCycleLR with maximum/base argument 0.002, and evaluation batch 512 every
  150 updates.
- Observation cadence: before and after every optimizer update. BridgeLearn
  plans and applies in `shadow` mode once per update. The runner checks equality
  of all optimizer-group LRs immediately before and after every shadow apply,
  and also checks that `optimizer.step()` itself did not alter them. Only
  OneCycleLR changes LR.
- Parameter blocks: embeddings, routing, shared operator core, and readout.
- Sharpness: independent random unit vectors per block; PyTorch autograd
  computes `H*v`, and the recorded estimate is the absolute Rayleigh quotient
  `|v' H v|`, smoothed with EMA alpha 0.1. This is a stochastic
  trace-per-dimension-style curvature probe, not a largest-eigenvalue power
  iteration.
- Innovation: every 50 updates, the batch is divided into two independent
  halves. BridgeLearn `SplitBatchNoiseObserver` converts their blockwise
  gradient differences to unit-batch noise estimates and applies EMA alpha
  0.2. The latest estimate is supplied to BridgeLearn on intervening updates.
- Transition: BridgeLearn `EmpiricalTransitionObserver` estimates contraction
  and innovation from paired pre/post-update parameter samples.
- AR(2): BridgeLearn `AR2AdequacyObserver` uses a rolling 128-update history of
  16 fixed parameter coordinates per block. `ForgettingFactorAR2Observer`
  supplies an online cross-check, and Jury margins are recorded.
- Sharpness dynamics: BridgeLearn `SharpnessPlant` consumes consecutive HVP
  estimates and emits a lower/center/upper one-step forecast. Forecast `k-1`
  is compared with realized pre-update sharpness at `k`.

Exact invocation is frozen in `command.sh`. Output is in `stdout.log`;
`stderr.log` contains `/usr/bin/time -v` resource data. The 8.2 MB telemetry
keeps all 1,500 compact per-step records plus 11 evaluation summaries.

## Acceptance checks

- Timed command exited 0 after 11:46.49 wall time; maximum RSS was 1,008,852
  KiB.
- `telemetry.json` parses as strict JSON and reports BridgeLearn 0.3.0,
  controller mode `shadow`, 1,500 per-update records, 30 split-batch
  measurements, 1,498 available AR(2) fits, 11 evaluation summaries, and a
  1,500-record calibration report.
- Every one of the 1,500 LR non-mutation checks passed.
- No traceback, exception, non-finite JSON value, or diff-whitespace error was
  found.
- Final evaluation accuracy was 0.414; the evaluation maximum was 0.442 at
  step 1,350, matching v1 to displayed precision. This is an integration
  check, not a performance claim.

## Results

### Matched-cadence transition and variance calibration

Per-update matching changes the v1 story substantially. Absolute variance
calibration MAE by block was:

| Block | MAE | RMSE | maximum absolute error |
|---|---:|---:|---:|
| embeddings | 6.58e-5 | 1.03e-4 | 5.33e-4 |
| routing | 3.74e-4 | 4.84e-4 | 1.24e-3 |
| operator core | 2.62e-6 | 3.62e-6 | 1.04e-5 |
| readout | 1.21e-5 | 1.60e-5 | 5.08e-5 |

Predicted/observed variance correlations were 0.999996, 0.999998, 0.999999,
and 0.999999. The largest error was routing at step 444, near the OneCycleLR
peak. Contraction MAE was 3.19e-5, 1.76e-4, 7.42e-4, and 2.68e-4 respectively.
Thus v1's maximum variance error 0.111 and contraction gap 0.338 were primarily
evaluation-interval/matched-horizon artifacts, although routing retains a
small positive variance bias (3.74e-4).

There is still a material innovation mismatch. Median BridgeLearn-predicted
innovations were approximately 1.09e-12, 2.07e-11, 5.11e-14, and 1.09e-11,
whereas median empirical-transition innovations were 9.25e-8, 3.07e-7,
1.06e-7, and 6.62e-8. Their mean absolute gaps were 2.25e-7, 7.52e-7,
2.16e-7, and 1.39e-7. Split-batch unit-noise medians were 1.96e-4, 6.17e-3,
1.15e-5, and 1.08e-3. This scale mismatch may reflect the controller's
`eta^2 / batch` mapping, AdamW preconditioning/momentum, and the fact that
empirical innovation is estimated across parameter coordinates rather than
replicated stochastic trajectories. It is not calibrated enough for active
innovation control.

### Sharpness estimate and plant

EMA HVP estimates ranged over the run from 2.04e-5--6.99e-3 (embeddings),
1.60e-6--9.77e-2 (routing), 4.94e-6--8.28e-4 (operator core), and
1.88e-3--1.49e-2 (readout). This is many orders below v1's gradient-secant
values and shows that the former proxy was not a valid substitute for the
random-direction Hessian response.

The plant center's one-step MAE was 9.84e-5, 1.59e-3, 1.81e-5, and 2.27e-4.
Nominal empirical coverage was 99.8--100%, but this is not good calibration:
median relative funnel widths after warm-up were about 73x, 3.70x, 537x, and
16.0x the center, while final confidence was only 5.47e-7 for every block.
The forecast is therefore conservative but uninformative. Coverage must not be
read as plant validation.

### AR(2) adequacy

AR(1) adequacy failed for every block on every available rolling-window fit
(adequate fraction 0 at threshold 0.5). Mean scores were 1.18e-8, 4.00e-10,
8.67e-9, and 6.41e-9. At the final step, fitted `(phi1, phi2)` pairs were
`(1.631,-0.641)`, `(1.818,-0.823)`, `(1.567,-0.579)`, and `(1.518,-0.528)`;
spectral radii were 0.971, 0.971, 0.970, and 0.979. Jury stability held for
97.8%, 90.5%, 100%, and 99.2% of available fits respectively, so the result is
mostly stable second-order behavior, not evidence of explosive dynamics.
AdamW momentum is the dominant reason the scalar AR(1) assumption is
structurally inadequate.

## Interpretation

Per-update observation resolves the dramatic v1 contraction/variance anomaly:
BridgeLearn tracks one-step parameter variance very closely, including through
the LR peak. It does not pass the broader calibration gate. The innovation map
underpredicts empirical transition innovation by several orders, the
sharpness funnel obtains coverage only by being extremely wide and
near-zero-confidence, and the AR(1) approximation is decisively rejected in
favor of stable AR(2)-like dynamics.

Active control should therefore **not** begin from this scalar AR(1)
configuration. The next gate is a shadow-only companion/momentum adapter using
the measured AR(2) coefficients and lag covariance, plus replicated
same-parameter stochastic transitions to reconcile split-batch noise with
realized parameter innovation. Sharpness also needs multiple HVP probes or a
short power iteration and a plant warm-start/regularization study that yields
usefully narrow, calibrated intervals. Only after those pass should a bounded
active-control experiment be considered.

## Reproduction and artifacts

Run `bash command.sh > stdout.log 2> stderr.log` from this directory. SHA-256
values are listed in `sha256sums.txt`.
