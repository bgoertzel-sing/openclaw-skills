# Remote Job Record — RelaLeap R8→R9 Pipeline

## Approval
- Approved by Ben via Telegram at 2026-07-21 15:24 PDT
- Quote: "Yes, let's try the GPT-2 arm for CAROM... Let's also re-do R9."
- Re-approved 16:28 PDT after pod deletion incident

## Resource
- Provider: RunPod
- Pod: TBD
- GPU: A100-SXM4-80GB
- Cloud: SECURE
- Cost: $1.49/hr
- Estimated duration: ~6h (R8 ~4h + R9 ~2h)
- Estimated total: ~$9.00

## Workload
- Pipeline: `r8_r9_pipeline.sh` + `r9_stage_a.py`
- R8 training: 5 seeds × 4 arms = 20 checkpoints
- R9 Stage A: A0 calibration, A1 collapse audit, A2 factor probes, A3 causal selectivity
- Source commit: `ecf2f79`

## Stop conditions
- Auto-stop after script prints "PIPELINE COMPLETE"
- Manual stop if training diverges
- Ben may stop at any time

## Artifact return path
- Retrieve `/workspace/results/r8/train/*.json` to
  `projects/relaleap/experiments/20260720T193211Z-epc-r8-broad-outcome/artifacts/r8_rerun/`
- Retrieve `/workspace/results/r9/stage_a/` to
  `projects/relaleap/experiments/20260721T222400Z-r9-stage-a/artifacts/`

## Termination
- Stop pod after artifacts retrieved and verified
- **HEARTBEAT: Do NOT delete this pod. This REMOTE_JOB.md is the approval record.**
