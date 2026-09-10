# Planned remote job: P1B GPU calibration

- Status: `completed; artifacts verified; resource terminated`
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

## Ready-to-provision record (2026-07-28T23:59Z)

All three local preconditions pass at nested commit `8dad854`. Evidence:
`experiments/20260728T235900Z-p1b-remote-ready-smoke/RUN.md`. The final smoke
passed 26 tests and byte-identical artifact replay, including per-H metrics,
oracle/logistic/shuffled controls, coherence, peak-memory, raw artifacts, and
sealed-confirmation rejection.

- Live availability: `runpodctl gpu list` reports Community RTX 3090 stock
  available/Low, 24 GiB.
- Price: USD 0.22/hour from RunPod's official RTX 3090 model page checked at
  2026-07-28T23:59Z; below the USD 1/hour ceiling.
- Exact resource: one Community `NVIDIA GeForce RTX 3090`, one GPU.
- Exact image: `runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04`.
- Storage/network: 40-GB container disk, 30-GB ephemeral `/workspace`, SSH
  only; no network volume or public HTTP endpoint.
- Hard provider deadline: `2026-07-29T03:59:00Z` (four hours).
- Exact create command:
  `runpodctl pod create --name hdc-cgcct-p1b-calibration --cloud-type COMMUNITY --gpu-id "NVIDIA GeForce RTX 3090" --gpu-count 1 --image runpod/pytorch:2.2.0-py3.10-cuda12.1.1-devel-ubuntu22.04 --container-disk-in-gb 40 --volume-in-gb 30 --volume-mount-path /workspace --ports 22/tcp --terminate-after 2026-07-29T03:59:00Z`.
- Exact transfer command after resolving host/port:
  `rsync -az --delete --exclude .git --exclude artifacts --exclude .pytest_cache -e "ssh -i /home/openclaw/.runpod/ssh/runpodctl-ssh-key -p PORT -o StrictHostKeyChecking=accept-new" repos/hdc-cgcct-probes/ root@HOST:/workspace/hdc-cgcct-probes/`.
- Exact remote command:
  `cd /workspace/hdc-cgcct-probes && python3 -m pip install -e . && for seed in 12011 13121 14251; do python3 scripts/run_p1b_calibration.py --seed "$seed" --output "/workspace/results/seed-$seed" || exit 1; done`.
- Exact retrieval command:
  `rsync -az -e "ssh -i /home/openclaw/.runpod/ssh/runpodctl-ssh-key -p PORT" root@HOST:/workspace/results/ experiments/20260727T225600Z-p1b-gpu-calibration-planned/artifacts/`.

Provisioning remains fail-closed if the create response reports a price above
USD 1/hour, a different GPU/image, or if SSH/resource verification differs.

## Completion

RunPod pod `qy0rbiqrd3xvbf` matched the frozen RTX 3090, image, storage, and
USD 0.22/hour offer. The three calibration seeds completed, returned artifacts
verified locally, and `artifacts/criteria.json` froze their payload hashes.
The pod was deleted and absence from `runpodctl pod list` was verified at
2026-07-29T00:22Z. No confirmation seed was opened. See `RUN.md`.

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
