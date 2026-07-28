# Planned remote job: P1B GPU calibration

- Status: `approved conditionally; fail-closed before provisioning`
- Approval: Benjamin Goertzel, Telegram, 2026-07-27. Scope: three P1B
  calibration seeds after a passing local CPU smoke, hard total cap USD 10.
- Project/run: `hdc-cgcct-transformers` / `p1b-gpu-calibration`

## Preconditions

1. Exact planted-PCFG six-layer next-token fixture exists at a pinned commit.
2. Local CPU smoke passes deterministic split, one training update, residual
   extraction, and artifact/replay checks.
3. The smoke record names the exact command, input manifest hash, and expected
   calibration artifact schema.

No pod may be created before all three conditions are recorded as passed.

## 2026-07-28 launch audit

RunPod CLI health checks passed. The live Community Cloud RTX 3090 offer was
USD 0.22/hour for one 24-GiB GPU (30 GB RAM, 6 vCPU), under the approved
USD 1/hour ceiling; the proposed official image was
`runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04`, with 40 GB
container disk and 30 GB temporary workspace. Ben explicitly authorized
launch within the USD 10/four-hour cap.

The source audit then found that commit `b4593f4144e10acd56675b96f88a70e77bf40d7e`
only supplies the one-update `run_p1b_cpu_smoke.py`. It has no calibration
runner or artifact schema covering the frozen 10,000-update/early-stop
procedure, per-D code arms, ridge/probe measurements, or three calibration
seeds. This fails precondition 3. No P1B pod was created; implementing and
testing the frozen calibration runner is now required before a fresh priced
launch check.

## Proposed resource envelope

- Provider/account: RunPod, configured operator account.
- Resource: one single 24 GiB-or-larger NVIDIA GPU; choose the lowest-priced
  compatible on-demand/secure availability at launch, with price at or below
  USD 1/hour. No multi-GPU resource.
- Image: a pinned official PyTorch CUDA image compatible with the committed
  Torch version; exact image digest/tag recorded before provisioning.
- Storage/network: minimum ephemeral storage sufficient for code, generated
  PCFG data, three checkpoints, and returned artifacts; no public endpoint;
  outbound access only for ordinary dependency installation if the smoke did
  not already vendor the required wheels.
- Time/cost guardrails: target 2--5 GPU-hours; hard termination at 4 hours or
  USD 10 total, whichever comes first. Terminate immediately after verified
  artifact return.

## Transfer and execution

Transfer only the pinned repository files, a generated/sanitized split manifest
or its deterministic generator, and the remote runner. Do not transfer
OpenClaw state, credentials, SSH keys, `.git` metadata, unrelated project
files, or user data. Run the three fixed calibration seeds in named tmux,
with per-seed logs/checkpoints/metrics and no hyperparameter changes during the
run.

## Stop conditions and return

Stop without using remaining budget if CPU-smoke invariants fail remotely,
split-manifest or replay hashes differ, non-finite loss occurs, the artifact
schema is missing, or any threshold/hyperparameter would need changing.
Return logs, metrics, checkpoints required by the frozen readout procedure,
and hashes to this experiment directory; verify the artifact manifest locally;
then terminate the pod and record provider status/final observed cost.

## Boundary

The three calibration seeds set criteria; they are not confirmation evidence.
The five confirmation seeds remain sealed until the criteria artifact is
written and hashed.
