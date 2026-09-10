# SLT Large Validation Run 1

## Summary

The approved Runpod SLT large validation job completed successfully. Heartbeat retrieved artifacts, verified the report JSON, and deleted the paid pod.

## Timeline

- Approved by Benjamin Goertzel: 2026-07-11 09:51 PDT
- Pod created: 2026-07-11 16:56:26 UTC
- Completion/idle observed: 2026-07-11 19:06 UTC
- Pod deleted: 2026-07-11 19:09 UTC

## Resource

- Provider: Runpod
- Pod: `pmqngq3cxcd5bw` (`relaleap-slt-large-run1`)
- GPU: 1× A100-SXM4-80GB
- Price: $1.49/hr
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Source: `projects/relaleap/worktrees/slt-integration`, branch `agent/slt-integration`, commit `52f5171`

## Command

```bash
cd /workspace/relaleap && PYTHONPATH=src python3 scripts/run_slt_tinyshakespeare.py \
  --device cuda --epochs 3 --n_chains 8 --n_samples 1000
```

## Report verification

`artifacts/slt_tinyshakespeare/slt_tinyshakespeare_report.json` parsed as valid JSON and reported:

- `status`: `complete`
- `device`: `cuda`
- `epochs`: 3
- `n_chains`: 8
- `n_samples`: 1000
- `elapsed_seconds`: 3978.461749792099

Top-level fields include `blocks`, `calibration`, `checkpoint`, `num_model_parameters`, `num_parameter_blocks`, `n_tokens_for_wbic`, and `seq_len`.

## Retrieved artifacts

Copied to `projects/relaleap/experiments/slt_large_run1/artifacts/`:

- `slt_large.log` — 21,355 bytes
- `slt_tinyshakespeare/slt_tinyshakespeare_report.json` — 21,354 bytes
- `slt_tinyshakespeare/tiny_char_transformer.pt` — 478,902 bytes
- `slt_tinyshakespeare/tinyshakespeare.txt` — 1,115,394 bytes

## Cost / cleanup

- Guardrail: 16h / $24 compute, auto-terminate by 2026-07-12T03:00:00Z.
- Observed pod lifetime was about 2h13m from Runpod `createdAt` to deletion, so expected compute cost is roughly $3.31 before provider rounding/storage effects.
- Pod deletion returned `{ "deleted": true, "id": "pmqngq3cxcd5bw" }`.
- `runpodctl pod list` returned `[]` after cleanup.

## Conclusion

The SLT large validation run completed under guardrail, artifacts were preserved locally, and all visible Runpod pods were terminated.
