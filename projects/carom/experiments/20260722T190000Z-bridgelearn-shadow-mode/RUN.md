# BridgeLearn shadow mode on scheduled CAROM

- Run ID: `20260722T190000Z-bridgelearn-shadow-mode`
- Status: complete (`exit_status.txt` = 0)
- Question: Can BridgeLearn v0.3.0 observe CAROM's scheduled training under an
  unchanged OneCycleLR policy and emit useful predicted-versus-realized
  transition, calibration, and sharpness telemetry?
- Relevant research rules: 1 (validate the estimator), 2 (state shadow-mode
  invariants), 3 (use BridgeLearn's controller/trace framework), 5
  (reproducible reporting), and 7 (keep the controller behind an adapter).

## Protocol

- Repository: `/home/openclaw/research-agent/projects/carom/repos/carom`
- Workspace Git branch/commit before run:
  `agent/chat-room-identity-phase1` / `ffdc293`
- Repository state: shared dirty workspace; the new runner and this experiment
  record are uncommitted, and unrelated user/agent changes are present.
- BridgeLearn: local `bridgelearn-0.3.0-py3-none-any.whl`, installed into the
  dedicated venv (not imported from source).
- CAROM variant: `scheduled`, default model `d=48`, `K=8`.
- Training: 1,500 steps, AdamW, OneCycleLR active, batch 128, base/max LR
  0.002, seed 0, CPU.
- Observer cadence: every 150 training steps and the final step; evaluation
  batch 512.
- Parameter blocks: embeddings, routing, shared operator core, and readout.
- Sharpness proxy: absolute gradient secant between evaluation boundaries,
  exponentially smoothed with alpha 0.5. This is a diagnostic proxy, not a
  validated Hessian eigenvalue estimate.

## Invariants and acceptance checks

The BridgeController is constructed with `mode="shadow"`. Its plan is allowed
to update BridgeLearn's internal shadow state, but optimizer group learning
rates are compared immediately before and after every controller application;
any mutation raises an error. OneCycleLR remains the sole active scheduler.
Acceptance requires exit status zero, a parseable telemetry JSON, nonempty
observations, controller mode `shadow`, and finite calibration summaries.

Exact invocation is frozen in `command.sh`. Standard output and `/usr/bin/time`
diagnostics are preserved as `stdout.log` and `stderr.log`.

## Results

### Direct observations

- The run exited zero and produced 11 parseable shadow observations in
  `telemetry.json`. BridgeLearn reports version 0.3.0; PyTorch is 2.13.0+cpu.
- Wall time was 2:21.24 (`/usr/bin/time`), with 665,488 KiB maximum RSS. The
  runner's training-loop timer reported 139.26 seconds.
- Evaluation accuracy rose from 0.118 after step 0 to a trace maximum of 0.442
  at step 1,350 and ended at 0.414. This single run is an integration check,
  not a CAROM performance conclusion.
- OneCycleLR rose from 8.00e-5 after step 0 to 1.99998e-3 at step 450, then
  decayed to 1.25e-8 at step 1,499. The runner verified after every shadow
  application that optimizer group LRs were unchanged; no invariant violation
  occurred.
- The largest predicted-versus-realized contraction gap was 0.338 at step 450:
  for the operator-core block BridgeLearn predicted 0.999743 while the
  evaluation-interval variance ratio implied 1.337621. This coincided with the
  OneCycleLR peak. BridgeLearn's reference contraction at this boundary was
  near unity (0.999914 for operator core), so both its commanded-reference and
  planned models missed the interval-scale expansion.
- The maximum absolute variance calibration error was also at step 450
  (0.110872). Across all observations the per-block variance RMSE was 0.01080
  (embeddings), 0.05407 (routing), 0.000505 (operator core), and 0.002188
  (readout). Predicted/observed variance correlations were 0.964--0.978, but
  these correlations do not remove the cadence/model mismatch.
- The smoothed secant sharpness proxy began with a maximum of 12.236 (readout),
  fell to 1.564 at the LR peak, and was 0.563 at the end. Bridge diagnostics
  reported robust stability throughout and no edge-of-stability fraction,
  which conflicts with the observed interval expansion and shows that the
  current proxy/cadence is not adequate for stability claims.

### Interpretation and limitations

The shadow integration works mechanically and preserves OneCycleLR behavior.
The trace exposes a useful discrepancy near maximum LR, but it is not yet a
calibrated one-step comparison: BridgeLearn predicts a single transition at an
evaluation boundary, while realized variance spans 1 update for the first
record and then 149--150 updates. Parameter population variance is also only a
coarse state statistic, the secant estimator is not a top-Hessian eigenvalue,
and realized innovation is unidentifiable from one trajectory (recorded as
zero by convention). The apparent LR-associated divergence is therefore a
hypothesis-generating diagnostic, not evidence that BridgeLearn or OneCycleLR
has identified the underlying dynamics.

### Next steps

1. Observe every optimizer update (while exporting only evaluation-boundary
   summaries), so predicted and realized transitions have matched horizons.
2. Replace the gradient secant proxy with a validated Hessian-vector power
   estimate and use BridgeLearn's v0.3 structural AR(2)/momentum observers for
   AdamW adequacy.
3. Estimate innovation from repeated or split-batch transitions and add a
   fixed-LR control around the step-300--600 region before attributing the
   expansion to the OneCycleLR peak.
4. Repeat across seeds only after these estimator controls pass.

## Reproduction and artifacts

Run `bash command.sh` from this directory. Important SHA-256 values:

- `telemetry.json`: `d7809ff4d9d8d5e1cbed94aab7524d403b269884afa3ae9e8830887931bf661c`
- `stdout.log`: `cf00f94e11f33ca2b76df04671396b6bbc1def551e2b5a15c803af39cc535967`
- `stderr.log`: `903d7d21dfe6e2cedf9b648eb645039b2219ae274e0952367cfe72ad146cf811`
- `command.sh`: `506696d9fc627909e0b5995835136b112aa2b38b79575835b755119fd35130ef`
- `run_carom_bridge_shadow.py`:
  `ff12c7cdf67dc1a729fcdec950e17c9356093104f8751fd4858b59211dffb6b5`
