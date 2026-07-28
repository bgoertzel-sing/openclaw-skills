# Remote Job Record — CAROM GPT-2 Arm

## Final status

- Complete; artifacts retrieved and hash-verified.
- Pod `26u0p4wpyal9ki` stopped at 2026-07-21 18:39:41 PDT; provider status
  `EXITED`. The only remaining active RunPod pod was the separate approved
  RelaLeap job.
- Approximate pod lifetime: 2h09m, or USD 3.20 at USD 1.49/hr before provider
  rounding. The repair extension consumed about 3m16s, approximately USD 0.08.

## Approval
- Approved by Ben via Telegram at 2026-07-21 15:24 PDT
- Quote: "Yes, let's try the GPT-2 arm for CAROM... Let's also re-do R9."
- Re-approved 16:28 PDT after pod deletion incident

## Resource
- Provider: RunPod
- Pod: `26u0p4wpyal9ki`
- GPU: A100-SXM4-80GB
- Cloud: SECURE
- Cost: $1.49/hr
- Estimated duration: ~2h
- Estimated total: ~$3.00
- 2026-07-21 18:36 PDT extension: Ben authorized leaving this existing pod up
  for up to 30 additional minutes to repair the post-training corpus-unpacking
  failure and finish the intervention pass. Maximum incremental compute:
  approximately USD 0.75 at the recorded USD 1.49/hr price.

## Workload
- Script: `r9_carom_gpt2.py`
- Frozen GPT-2-small (124M, d=768) span encoder
- 4000 steps, checkpoint every 500 (9 checkpoints)
- 3 interventions: τ-decline, trajectory intervention, L=5 budget sweep
- Output: `/workspace/zerobot-runs/carom-gpt2/results/`

## Stop conditions
- Auto-stop after script prints "DONE"
- Manual stop if training diverges
- Stop if the repair-and-resume work reaches 30 minutes after the extension
- Ben may stop at any time

## Artifact return path
- Retrieve `/workspace/zerobot-runs/carom-gpt2/results/` to
  `projects/carom/experiments/20260721T222400Z-carom-gpt2-arm/artifacts/`

## Termination
- [x] Stop pod after artifacts retrieved and verified
- **HEARTBEAT: Do NOT delete this pod. This REMOTE_JOB.md is the approval record.**
