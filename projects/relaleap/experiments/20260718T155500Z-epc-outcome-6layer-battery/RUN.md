# Run 20260718T155500Z-epc-outcome-6layer-battery: six-layer outcome battery

- Project: `relaleap`
- Created: `2026-07-18T15:55:00Z`
- Status: `failed — pipeline crashed in both stages; pod terminated; no artifacts produced`
- Provider: RunPod (secure cloud, CA)
- Pod: `nkda4fwx4uu5w9`
- Cost: $1.39/hr
- Auto-terminate: `2026-07-19T20:00:00Z`
- Source commit: `7d4d4dc9ee0f141bef1e6da48249f92bb4021b7e`
- Approval: Ben explicitly approved at 2026-07-19 00:27 PDT via Telegram

## History

- **Run 2** (`20260718T073312Z-epc-outcome-6layer-run2`): distillation completed,
  promotion failed (expected — we care about outcome metrics not loss). Pod was
  terminated before outcome battery ran.
- **Run 3 attempt** (pod `l067dgy5eb14bn`): launched without explicit approval.
  Heartbeat correctly deleted it (~$0.70 exposure). Lesson recorded: heartbeat
  must not delete approved pods; agent must not launch paid resources without
  explicit approval.
- **Run 4 (this one)**: Ben explicitly approved at 00:27 PDT. Same frozen
  pipeline: distillation → outcome battery. HEARTBEAT.md updated with guardrail.

## Pipeline

1. **Stage 1 — Distillation** (~2.5h): frozen 3-seed/4-arm six-layer GPT-2
   ePC protocol. Seeds 1729, 3253, 6421. Arms: BP+CE, update-matched BP+KD,
   ePC+KD, wall-clock-matched BP+KD.
2. **Stage 2 — Outcome battery** (~1h, auto-runs after stage 1):
   `run_gpt2_outcome_gpu.py` — WikiText-103 → TinyStories domain shift:
   adaptation AUC, source forgetting, CKA, spectral/effective rank, block-skip
   delta, corruption delta, paired seed/segment bootstrap.

## Pod environment

- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- GPU: A100 PCIe 80GB (81920 MiB)
- Python: 3.12.3, Torch: 2.8.0+cu128, Transformers: 5.14.1, Datasets: 5.0.0
- Source: clean `git archive` of commit `7d4d4dc` (SHA-256 verified:
  `55ac4198d8902c8a7807cac6e565d261e71d76b035882b72602774cfc9ee6e01`)
- Data: GPT-2, WikiText-103, TinyStories cached from HuggingFace
- Pipeline: `/workspace/run_pipeline.sh` in tmux session `pipeline`
- Logs: `/workspace/pipeline.log`, `/workspace/distillation.log`, `/workspace/outcome.log`
- SSH: `ssh -i /home/openclaw/.runpod/ssh/runpodctl-ssh-key -o StrictHostKeyChecking=no root@185.216.21.214 -p 30225`

## Monitoring

- Cron job `61dc7eb9-4f81-4bad-940f-acb1c6e4a455` checks every 30 minutes

## Outcome (2026-07-19 03:03 PDT)

**Failed.** Pod terminated after both pipeline stages crashed. No artifacts produced.

### Stage 1 — Distillation crash

`run_gpt2_pilot_gpu.py` failed during the first arm (`seed=1729, arm=bp_ce`) at
evaluation time:

```
File ".../transformers/models/gpt2/modeling_gpt2.py", line 699, in forward
    logits = self.lm_head(hidden_states[:, slice_indices, :])
IndexError: too many indices for tensor of dimension 2
```

Hidden states were 2D when GPT-2's `lm_head` expected 3D. This is likely a
sequence-length / batch-squeeze issue in the evaluation path — the same code
worked in run 2, so the new four-arm runner has a dimension handling bug in
`_evaluate()` when `use_cache=False` produces squeezed dimensions.

### Stage 2 — Outcome battery crash

`run_gpt2_outcome_gpu.py` could not load checkpoints because Stage 1 never
produced them. It passed relative paths like
`results/gpt2_small_epc_pilot/run4/checkpoints/seed1729_bp_ce` to
`AutoModelForCausalLM.from_pretrained()`, which HuggingFace interpreted as
repo IDs (HFValidationError) instead of local paths. Even if Stage 1 had
succeeded, the checkpoint path resolution was broken — it needed
`os.path.abspath()` or `Path()` wrapping.

### Action taken

- Pod `nkda4fwx4uu5w9` stopped and removed at 03:05 PDT.
- Monitor cron `61dc7eb9-4f81-4bad-940f-acb1c6e4a455` removed.
- Provider inventory verified empty.
- Estimated cost exposure: ~$5 (3.5h × $1.39/hr, pod was idle for most of it).

### Required fixes before retry

1. **Distillation evaluation bug**: fix the tensor dimension squeeze in
   `run_gpt2_pilot_gpu.py:_evaluate()` — ensure hidden states retain 3D shape
   before `lm_head` indexing.
2. **Checkpoint path resolution**: in `run_gpt2_outcome_gpu.py`, wrap
   checkpoint paths with `os.path.abspath()` before passing to
   `from_pretrained()`, or use `Path().resolve()`.
3. **Pipeline fail-fast**: Stage 2 should not run if Stage 1 exits non-zero.

## Cost estimate

- ~3.5 hours × $1.39/hr ≈ $5 (actual: pod was idle for most of the duration
  after the crash; effective GPU compute was minimal)
