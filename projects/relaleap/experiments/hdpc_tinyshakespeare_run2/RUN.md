# HDPC/ePC Tiny Shakespeare Run 2

## Summary

Approved non-smoke Runpod RTX A6000 HDPC/ePC Tiny Shakespeare run completed, artifacts were retrieved, and the pod was terminated.

## Timeline

- Approved by Benjamin Goertzel: 2026-07-10 18:50 PDT
- Pod provisioned: 2026-07-11 01:51:47 UTC
- Heartbeat completion check: 2026-07-11 02:50 UTC
- Pod deleted/terminated: 2026-07-11 02:52 UTC

## Resource

- Provider: Runpod
- Pod: `j0xlf52ahsoqa7` (`relaleap-hdpc-ts-run2`)
- GPU: 1× NVIDIA RTX A6000, 48GB VRAM
- Price: $0.49/hr on-demand
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Source commit: `projects/relaleap/worktrees/tinyshakespeare-hdpc`, branch `agent/tinyshakespeare-hdpc`, commit `fc5efa9`

## Task

Non-smoke HDPC/ePC training: 5 epochs, 200 steps/epoch, batch 128, d_model 256, 4 heads, 6 layers, d_ff 1024, seq_len 256; homotopy KD with λ=0.05 and T={1,2,4,8}; PC-gradient/BP-gradient diagnostics, held-out perplexity, energy profiles, update sparsity, detached crown.

## Result

- Exit status: completed; no training process remained at retrieval time.
- GPU at check time: idle (`0%` utilization, 1 MiB VRAM used).
- Summary JSON present and parseable.
- Top-level summary fields include: `config`, `teacher_perplexity`, `student_perplexity`, `perplexity_delta`, `gradient_diagnostics`, `energy_profile_*`, `update_sparsity_histogram`, `teacher_parameters`, `student_parameters`, and `artifact_path`.

## Retrieved artifacts

Artifacts copied to `projects/relaleap/experiments/hdpc_tinyshakespeare_run2/artifacts/`:

- `training.log` — 8,658 bytes
- `hdpc_tinyshakespeare/summary.json` — 19,248 bytes
- `hdpc_tinyshakespeare/hdpc_tinyshakespeare_smoke.pt` — 38,844,433 bytes

## Cost / cleanup

- Guardrail was 6 hours / $2.94, with auto-terminate by 2026-07-11T04:00:00Z.
- Observed pod lifetime was about 60 minutes from Runpod `createdAt` to deletion, so expected compute cost is about $0.49 before any provider rounding/storage effects.
- Pod deletion command returned `{ "deleted": true, "id": "j0xlf52ahsoqa7" }`.
- `runpodctl pod list` returned `[]` after deleting both active RelaLeap pods.

## Conclusion

The remote non-smoke HDPC/ePC run completed under budget, artifacts were retrieved, and the pod was terminated before the guardrail deadline.
