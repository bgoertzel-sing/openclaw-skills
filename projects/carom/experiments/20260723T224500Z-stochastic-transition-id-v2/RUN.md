# CAROM Stochastic Transition Identification v2

- Run ID: `20260723T224500Z-stochastic-transition-id-v2`
- Started: `2026-07-23T22:45:00Z`
- Status: complete
- Local CPU only; autonomous spend: USD 0
- Repository: `projects/carom/repos/carom/`
- Branch: `agent/chat-room-identity-phase1` (shared dirty workspace)
- Commit: `cdd7ba976ed88a1deb10c1d2c05d42061eda093f`

## Question and frozen protocol

V1 established that calibrated AdamW innovation models pass one-step
prediction (Models 1–3: frozen-preconditioner, full one-step, empirical;
median ratios 1.01/1.00/1.00), but the deterministic 8-step state model
fails (1.02× vs 2× gate) and sharpness is too noisy (CV 0.74, width 1.43).

V2 tests whether the 8-step failure is due to:
  (A) Irreducible stochasticity (minibatch randomness),
  (B) State representation insufficiency (random projections),
  (C) Nonlinear optimizer dynamics.

Key design change: predict the **distribution** of 8-step outcomes (mean +
covariance) rather than individual trajectories. An oracle diagnostic
supplies actual future gradient means to separate irreducible minibatch
uncertainty from fixable model error.

### Parts

- **Part B2**: 32 branches × 8 updates per checkpoint (24 calibration / 8
  held-out). Compares random projection vs PCA projection. Scores:
  distributional coverage (90% interval), energy score, mean RMSE vs AR(1).
- **AdamW mean dynamics**: runs a deterministic trajectory using the
  calibration-set mean clipped gradient as forcing. If this matches the
  empirical branch mean, the AdamW mean dynamics are correct and the
  residual error is stochastic.
- **Oracle diagnostic**: runs a deterministic trajectory using ALL branches'
  mean clipped gradient. The gap between oracle and distributional mean RMSE
  estimates the irreducible uncertainty floor.

### Gates

- **Distributional calibration**: median coverage ratio in [0.5, 2.0].
- **Mean RMSE**: predicted mean RMSE ≤ AR(1) mean RMSE.
- **Oracle gap**: median oracle/distributional ratio < 0.6 (indicates
  irreducible uncertainty dominates).
- **AdamW mean dynamics**: median AdamW/cal RMSE ratio < 2.0 (mean dynamics
  correct; residual is stochastic).
- **Operational**: parent hashes unchanged, exact replay.

Research Rules 1, 2, 5, 7 apply. Exact command is in `command.sh`.
The reduced smoke and 5 focused invariant tests passed before this run.

## Results

- Exit status: `0`; local CPU only; wall time `1040.65 s`.
- Artifacts:
  - `artifacts/results.json`, SHA-256
    `b71b5c4114903d26b59dc4c91c39a9c7de9fbd89261a4b6fc003370ccee3edaa`;
  - `artifacts/results.npz`, SHA-256
    `34ae83a4d65e0688be0b272cf2119cae4eb18e6873bf77c6ce926eb819a58611`.
- All gates passed:
  - random/PCA distributional median coverage ratios: `0.9877` / `1.0532`;
  - mean-RMSE ratio versus AR(1): `0.9922`;
  - oracle/distributional error ratio: `0.00472`;
  - AdamW mean-dynamics/calibration RMSE ratio: `1.2777`;
  - five parent hashes unchanged and exact replay passed.

## Interpretation

**Observed:** calibration of an eight-step *distribution* predicts held-out
branches well, while the oracle supplied with actual future mean gradients
reduces error nearly to zero.

**Inferred:** v1's deterministic branch trajectory gate was mis-specified:
unobserved future minibatches dominate its error. At this scale there is no
evidence that a nonlinear state representation is required; calibrated AdamW
mean dynamics plus stochastic innovation suffice for short-horizon forecasts.

**Decision:** retain active BridgeLearn control as shadow-only until its
activation gate is reformulated and separately tested in distributional terms.
Sharpness remains a batch-conditioned uncertainty distribution, not a point
controller signal.
