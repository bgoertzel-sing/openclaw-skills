# RunPod remote job: RelaLeap six-layer ePC outcome battery

- Project: `relaleap`
- Created: `2026-07-18T22:33:00Z`
- Status: `pending provisioning`
- Provider: RunPod
- Account context: Ben's RunPod account (bengoertzel@gmail.com)
- Approval: Ben's Telegram message at 2026-07-18 15:33 PDT directing the
  outcome battery run regardless of distillation loss quality.

## Requested resource and cost bound

- GPU: one Community Cloud NVIDIA A100 PCIe 80 GB.
- Expected duration: ~2 hours (outcome battery only; no training).
- Hard termination: 4 hours after provisioning.
- Expected GPU charge: ~USD 2.50-3.00.
- Maximum GPU charge: USD 8.00 including incidental storage.
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404` (matches run 2).
- Storage: 80 GB ephemeral container storage; no network volume.

## Frozen scientific and source inputs

- Source commit: `7d4d4dc9ee0f141bef1e6da48249f92bb4021b7e`
- Outcome config: `configs/gpt2_epc_outcome_6layer.json`, SHA-256
  `4a572da67cffce1ff9a32110e00e60c94413f3a974998b86575f2f1894288ab2`
- Outcome runner SHA-256:
  `68e7c67350aec0042a06f6facc11f3a59c45b1d022f71fe8dfe15a990a7b3ef3`
- Dependency lock: `requirements-gpu.lock.txt`
- Checkpoints: nine safetensors from run 2
  (`20260718T073312Z-epc-outcome-6layer-run2/artifacts/results/checkpoints/`),
  3 seeds × 3 arms (bp_ce, bp_kd, epc_kd), ~313 MB each, ~2.8 GB total.
- Public inputs: pinned GPT-2 model/tokenizer, WikiText-103, TinyStories.

## Execution command

```
PYTHONPATH=src python3 scripts/run_gpt2_outcome_gpu.py \
  --config configs/gpt2_epc_outcome_6layer.json \
  --checkpoints /workspace/checkpoints \
  --output /workspace/results/gpt2_epc_outcome_6layer.json \
  --device cuda --offline
```

## Data and credential boundary

- Transfer only: clean git archive of pinned commit, nine checkpoint
  directories, frozen config, dependency lock, and GPT-2 tokenizer/model cache.
- No OpenClaw state, Telegram tokens, gateway credentials, Git credentials,
  private SSH keys, unrelated workspace files, or private data.

## Stop conditions

- Source/config drift; missing checkpoint; non-finite metric; OOM;
  price/cost/time breach; failed artifact retrieval.

## Cleanup

1. Retrieve `gpt2_epc_outcome_6layer.json` and training log to
   `artifacts/`.
2. Verify output JSON is parseable and contains expected 9 rows + 3
   comparisons + promotion evaluation.
3. Terminate (not stop) the pod.
4. Verify provider pod inventory is empty.
