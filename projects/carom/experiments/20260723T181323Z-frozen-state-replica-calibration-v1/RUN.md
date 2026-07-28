# CAROM Frozen-State Replica Calibration v1

- Run ID: `20260723T181323Z-frozen-state-replica-calibration-v1`
- Started: `2026-07-23T18:13:23Z`
- Status: complete
- Local CPU only; autonomous spend: USD 0
- Repository commit: `cdd7ba976ed88a1deb10c1d2c05d42061eda093f`
- Branch: `agent/chat-room-identity-phase1` (shared dirty workspace)

## Question and frozen protocol

Can replicated transitions from identical CAROM AdamW states identify a
calibrated innovation mapping, a state model materially better than AR(1), and
a repeatable Adam-preconditioned top-curvature estimator?

Scheduled CAROM uses `d=48`, `K=8`, four named parameter blocks, AdamW
(`max_lr=0.002`, weight decay `1e-4`), OneCycleLR, clipping at 1.0, seed 0,
batch 128, and 1,500 updates. Complete model/optimizer/scheduler/Python RNG/
Torch RNG states are captured after updates 150, 450, 900, 1350, and 1499.

Part A uses 64 one-step replicas at batch 128 and 32 each at batches 64 and
256. Updates 450 and 900 additionally use common-random batch-128 controls at
0.5x and 1.25x LR. Part B uses 32 branches of eight updates and a 24/8
train/held-out split for AR(1), AR(2), frozen-v companion, and augmented
v-aware predictors. Part C uses four starts and six HVP power iterations for
each checkpoint/block on batch 64.

## Preregistered gates

- Innovation: held-out median predicted/replicated ratio in `[0.5, 2]`.
- State: augmented eight-step error at least 2x lower than AR(1).
- Sharpness: maximum repeated-estimate CV below 0.30 and maximum 90% relative
  width below 0.50.
- Operational: unchanged parent hashes and exact deterministic replay.

Research Rules 1, 2, 5, and 7 apply. Exact command is in `command.sh`.
The reduced smoke and four focused invariant tests passed before this run.

## Results

- Exit status: 0; local CPU only.
- Wall time reported by the experiment: 806.609 seconds. The enclosing tmux
  job completed cleanly; no paid resource was used.
- Artifacts:
  - `artifacts/results.json`, SHA-256
    `7e10ac69ef99d74144b25a3eaa1056ab8ea5751e524cb73fb911c1717fa3b969`;
  - `artifacts/results.npz`, SHA-256
    `439c2b32696c8014fbd0515baf933ace7348ff0fff06896455d8a073c2267def`.

### Gate outcomes

| Gate | Outcome | Measurement |
|---|---|---|
| Innovation model 0: scalar rescaling | fail | held-out median predicted/replicated `4.0726` |
| Innovation model 1: frozen-preconditioner AdamW | pass | median `1.0144` |
| Innovation model 2: full one-step AdamW | pass | median `1.0000` |
| Innovation model 3: empirical fallback | pass | median `1.0000` |
| Augmented state versus AR(1) | fail | median 8-step improvement `1.0235x`, gate `>=2x` |
| Curvature repeatability | fail | maximum CV `0.7374`, 90% relative width `1.4277`; gates `<0.30`, `<0.50` |
| Operational | pass | all five parent hashes unchanged; exact replay passed |

The run covers updates 150, 450, 900, 1350, and 1499 of the scheduled CAROM
model, with one-step replicas across batch/LR conditions, 32 eight-step
branches per checkpoint, and repeated blockwise power-iteration curvature
estimates. The machine-readable result marks the run `complete`.

## Interpretation

**Observed:** the naive scalar innovation map is wrong by roughly fourfold.
Accounting for AdamW's anisotropic preconditioner is enough to calibrate
one-step innovation on held-out conditions: both the frozen-preconditioner and
full one-step models pass the preregistered `[0.5, 2]` band.

**Observed:** this repair does not identify useful eight-step dynamics. The
v-aware augmented transition only improves AR(1) by `1.0235x`, far short of
the required `2x`. The current linearized `(theta,m,v)` representation is not
an adequate multi-step state model for active control.

**Observed:** repeated curvature estimates are too variable for use as a
sharpness control signal. In particular, the high maximum CV/width precludes
using a point curvature estimate to tune the controller.

**Decision:** retain the calibrated AdamW-preconditioned innovation model as a
shadow uncertainty component. Keep active BridgeLearn control blocked. The
next experiment is a conservative state-identification v2: test time-varying
and nonlinear stochastic transition representations on fresh checkpoint/LR/
batch interventions, and estimate curvature as a conditional distribution
over batches rather than a single deterministic signal.
