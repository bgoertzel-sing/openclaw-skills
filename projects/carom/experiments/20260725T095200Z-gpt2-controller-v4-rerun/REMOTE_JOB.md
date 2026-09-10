# Remote job — CAROM GPT-2 distributional controller v4 rerun

## Approval status

**APPROVED** by Ben, 2026-07-25 02:42 PDT. Max USD 10.00.

## Fix from prior failure

The prior v4 run (20260724T082409Z) failed because `branch_trajectory` and
`mean_gradient_trajectory` called `scheduler.step()` on a parent OneCycleLR
that had already reached its `total_steps` limit.  Fix: branches now use a
constant LR (parent's current LR × scale) with NO scheduler.step().  This is
the correct design — branches are short 8-update probes that should not
advance the parent's LR schedule.  Regression tests added
(`test_v4_scheduler_fix.py`).

## Provider and resource

- Provider/account: RunPod, bengoertzel@gmail.com
- Cloud: Secure Cloud
- GPU: one NVIDIA A100 SXM4 80GB
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Container disk: 50GB; no persistent volume
- Network: SSH only plus template defaults
- Current observed price: USD 1.49/hr

## Time and cost

- Expected duration: 45–75 minutes
- Expected cost: ~USD 1.12–1.86
- Hard guardrail: 2 hours / USD 3.00 (well within $10 max)
- Auto-terminate deadline: 2 hours

## Data and privacy

Upload only CAROM Python sources (exp2_compiled_channel.py,
run_carom_gpt2_controller_v4.py, test_v4_scheduler_fix.py).  Dataset is
synthetic, generated on-pod.  No credentials, Git metadata, or private data
transferred.

## Artifact and cleanup plan

Retrieve results JSON, logs, and environment record.  Verify SHA-256 hashes.
Terminate (not stop) the pod.  Verify empty provider inventory.
