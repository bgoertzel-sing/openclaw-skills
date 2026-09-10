# RunPod remote job: RelaLeap six-layer outcome gate run 2

- Project: `relaleap`
- Created: `2026-07-18T07:33:12Z`
- Status: terminated after verified distillation retrieval; downstream outcome
  battery not run
- Provider: RunPod
- Account context: Ben's RunPod account
- Endpoint: `38.128.233.132:47335` (SSH)
- Provider pod ID: `xkgkjbake2tpe1`
- Approval: Ben's owner-authenticated Telegram message at 2026-07-18
  00:32 PDT accepts USD 1.49/hour and approximately USD 20 total cost.
- Initial cost estimate: approximately USD 20 total. At `2026-07-18T07:53Z`,
  Ben explicitly removed USD 20 as a hard cutoff and said a valid run may cost
  more, while retaining the requirement not to waste cycles. Terminate after
  verified artifact retrieval or on a scientific/progress stop condition.
- Provider CLI reports GPU charge USD 1.39/hour; Ben's UI reports USD
  1.49/hour, likely including the 50 GB container disk. Use the higher UI rate
  for the ceiling.

## Requested and frozen envelope

- One NVIDIA A100 PCIe 80 GB verified remotely (`81920 MiB`).
- Expected workload duration: approximately 3.5 hours; investigate/stop if the
  one-update smoke projects beyond the approved ceiling.
- Source commit: `7d4d4dc9ee0f141bef1e6da48249f92bb4021b7e`.
- Distillation protocol SHA-256:
  `ba89ac189a5e8635806157794f4d66c87b2ca6d011ead39dd3505a98b9a473ab`.
- Outcome protocol SHA-256:
  `4a572da67cffce1ff9a32110e00e60c94413f3a974998b86575f2f1894288ab2`.
- Actual image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`; Ubuntu
  24.04.3, Python 3.12.3, Torch 2.8.0+cu128, CUDA runtime 12.8, NVIDIA driver
  570.195.03. Region: CA-MTL-3. Container disk: 50 GB; `/workspace` is a
  provider-managed shared mount and no user network volume is attached.
- Stop condition triggered before source transfer: the actual image differs
  from the frozen preflight image
  `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04` and its recorded
  digest. At `2026-07-18T07:36Z`, Ben explicitly accepted the configuration
  change and directed that this pod be kept. Dependencies were installed in an
  isolated environment; source and protocol hashes were verified before the
  scientific runner started.
- Network: SSH only; no public HTTP endpoint is needed.

## Data and credential boundary

- Transfer only a clean `git archive` of the pinned commit and public model,
  tokenizer, WikiText-103, and TinyStories specifications.
- Do not transfer OpenClaw state, Telegram tokens, gateway credentials, Git
  credentials, private SSH keys, unrelated workspace files, or private data.
- The pod receives only the dedicated public SSH key.

## Execution and cleanup

1. Verify GPU, CUDA, image, disk, price, and provider pod ID.
2. Transfer and hash-check the clean source archive.
3. Install the pinned dependency lock, cache/hash public inputs, then run
   offline.
4. Run the one-update GPU smoke in a named tmux session and stop if provenance,
   numerics, memory, or projected-runtime gates fail.
5. Run the frozen three-seed/four-arm six-layer outcome gate only after the
   smoke passes.
6. Retrieve metrics, logs, checkpoints, manifests, and exit status to this
   experiment's `artifacts/`; verify hashes locally.
7. Terminate the pod after retrieval. Stopping without termination is not final
   cleanup because retained storage may remain billable.

## Running observation

- `2026-07-18T08:07Z`: source commit and protocol hashes had been verified;
  the frozen distillation runner was active in tmux session `train`.
- Command: `PYTHONPATH=src python3 scripts/run_gpt2_pilot_gpu.py --protocol
  configs/gpt2_small_epc_pilot.json --output
  results/gpt2_small_epc_pilot/run2 --device cuda --source-commit
  7d4d4dc9ee0f141bef1e6da48249f92bb4021b7e`.
- GPU observation: A100 PCIe 80 GB, 96% utilization, 4,941 MiB used. The log
  had updated within three minutes. This was active progress, not idle cost.

## Final cleanup

- Distillation completed at `2026-07-18T10:23Z`; its frozen promotion rule
  failed.
- Forty result files and the training log were retrieved locally. Strict
  per-file result hashes and the log hash matched the pod.
- Pod `xkgkjbake2tpe1` was deleted at approximately `10:56Z`; provider pod
  inventory was then empty. No job-created network volume existed.
- The downstream structural/adaptation outcome runner was not executed before
  termination. No replacement allocation is authorized by this record.
