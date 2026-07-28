# Run 20260724T082409Z-gpt2-distributional-controller-v4

- Project: `carom`
- Started: `2026-07-24T08:24:09Z`
- Finished: `2026-07-24T13:34:36Z` (last remote log timestamp)
- Status: `failed; pod terminated after log retrieval`
- Operator/agent: `ZeroBot`
- Local or remote: `RunPod Secure Cloud; pod jvr2wurue5sfva (A100 SXM4 80GB), deleted after failure`

## Question

Does CAROM's distributional controller choose useful learning-rate actions on
the frozen-GPT-2-small compiled-channel task, where the local toy v3 had almost
no action headroom?

## Frozen protocol

- Warm-start weights: retained CAROM GPT-2 step-4000 checkpoint, SHA-256
  `c7cdf33efd46852db5901f7c4d251df0a58893cf7911396e16c0d2cfa0b3fd3d`.
- Frozen GPT-2-small 124M span encoder; only CAROM modules train.
- AdamW, base LR `1e-4`, weight decay `1e-4`, batch `64`, clip `1.0`.
- Reset optimizer is explicit: the retained checkpoint lacks optimizer state.
- Build a 2,000-update base trajectory, preserving full model/optimizer and
  Python/Torch/CUDA RNG state at updates `0,500,1000,1500,2000`.
- At each checkpoint, use disjoint branch seeds. For each LR scale in
  `{0.5,1.0,1.5}`, run 12 calibration branches and 4 held-out branches for
  eight updates. The controller selects the action with lowest calibration
  mean frozen-validation loss; the oracle selects the lowest held-out mean.
- Compare informed, passive (`1.0`), variance-gated, and oracle actions.
- Primary gate: paired held-out loss no worse than passive, all finite, exact
  checkpoint replay, and no parent mutation. Report effect size even if the
  permissive gate passes.
- Secondary metrics: accuracy, calibration uncertainty, controller/oracle
  agreement, and action distribution by checkpoint.

## Inputs

- Prior runner:
  `../20260721T222400Z-carom-gpt2-arm/source/r9_carom_gpt2.py`.
- Model checkpoint:
  `../20260721T222400Z-carom-gpt2-arm/artifacts/checkpoints/step_4000.pt`.
- Synthetic task data only; no private corpus.
- Source is local-private because supplied-code licensing remains unstated.

## Environment

See `REMOTE_JOB.md`. Retrieved remote log:
`artifacts/experiment.log` SHA-256
`5dc916bd6ccebcd1c09a93786e101359426931624e6a48ae33f39298ce37164b`.

## Command

The base run completed 2,000 updates, then failed during the final checkpoint
branch evaluation.

## Results

No valid full-gate result. The final gate raised `ValueError: Tried to step
2001 times. The specified number of total steps is 2000` from
`OneCycleLR.step()`: branches inherited a terminal parent scheduler and then
attempted eight more updates.

Partial, non-dispositive log observations:

- Step 500: controller 0.5; passive/informed/oracle 1.9802/1.9805/1.9792.
- Step 1,000: controller 1.5; passive/informed/oracle 1.7234/1.7385/1.7234.

## Interpretation

The failure is an implementation boundary error, not controller evidence.

## Follow-up

Add a local terminal-scheduler regression test and define the branch scheduler
policy beyond the parent trajectory before considering a rerun.
