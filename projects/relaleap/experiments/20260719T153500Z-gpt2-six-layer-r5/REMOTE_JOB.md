# RunPod remote job: RelaLeap six-layer GPT-2 retry r5

- Project: `relaleap`
- Created: `2026-07-19T15:35:00Z`
- Status: `approved by Ben 2026-07-19 08:30 PDT; provisioned and running`
- Provider/account: RunPod, authenticated account `bengoertzel@gmail.com`
- Local implementation commit: `dc61f31` (amended to `b58ba44` after adding SOURCE_COMMIT)
- Pod ID: `oo20lk2075y0dx`
- Pod provisioned: 2026-07-19 15:32 UTC
- Actual GPU: A100 SXM 80GB (Secure Cloud, US) — A100 PCIe unavailable, SXM is equivalent
- Actual rate: $1.49/hr
- Ben explicitly approved letting the pipeline run through Stage 2 completion (2026-07-19 11:03 PDT)

## Purpose and acceptance

Run the frozen three-seed/four-arm six-layer distillation followed by the
frozen outcome battery using the repaired, versioned pipeline. Stage 2 must run
if and only if Stage 1 exits zero. Retrieve and validate all JSON, checkpoint,
manifest, and log artifacts; a scientifically negative result is still valid.

## Requested resource and current availability

- One NVIDIA A100 PCIe 80 GB, Secure Cloud, Canada preferred.
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`.
- Storage: 80 GB ephemeral container disk; no network volume.
- Network: SSH for source/artifact transfer and HTTPS only for pinned public
  Hugging Face artifacts during preflight; scientific execution is offline.
- `runpodctl doctor` passed on 2026-07-19; `runpodctl gpu list` reported A100
  PCIe available on Secure and Community Cloud with low stock.

## Time and cost bound

- Price source: latest observed same-account Secure Cloud A100 PCIe allocation
  (`nkda4fwx4uu5w9`, 2026-07-19): USD 1.39/hour.
- Expected duration: 3.5 hours; expected GPU charge: USD 4.87.
- Hard termination: 5 hours after provisioning.
- Maximum approved compute envelope requested: USD 7.00, including incidental
  ephemeral storage. Stop immediately on a repeated systems failure.

## Frozen inputs and transfer/privacy boundary

- Clean archive of commit `dc61f31`, frozen configs, dependency lock, and only
  the pinned public GPT-2/WikiText-103/TinyStories cache inputs.
- Data classification: public source/code/model/data only; no private research
  datasets or personal data.
- Never transfer OpenClaw state, Telegram/gateway/provider credentials, Git
  credentials, unrelated workspace files, or private SSH keys. Authentication
  remains in local provider/SSH credential stores.

## Execution and monitoring

1. Verify source/config hashes, GPU, CUDA, dependencies, and pinned public
   artifact hashes.
2. Run `scripts/run_gpt2_full_pipeline.sh` in tmux session `relaleap-r5` with
   stdout/stderr and exit status captured.
3. Monitor at most every 30 minutes and terminate immediately on nonzero exit,
   provenance drift, missing/non-finite output, OOM, or time/cost breach.
4. The launcher uses `set -euo pipefail`; Stage 2 cannot follow failed Stage 1.

## Artifact return and cleanup

Retrieve results, checkpoints, manifests, environment freeze, and logs into
this experiment's `artifacts/`; verify JSON schemas/counts and SHA-256 hashes.
Then terminate (not stop) the pod. Query active provider inventory again and
record final observed lifetime/cost. Stopped pods may retain billable storage,
so stopping is not the completion state.
