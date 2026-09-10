# RelaLeap SLT Validation Large Run 1

## Summary

Heartbeat found the SLT-large Runpod job complete and idle, retrieved artifacts, verified the report JSON, and deleted the pod to stop paid compute.

## Timeline

- Pod created: 2026-07-11 03:44:42 UTC
- Completion/idle observed: 2026-07-11 05:35 UTC
- Pod deleted: 2026-07-11 05:37 UTC

## Resource

- Provider: Runpod
- Pod: `kfzk2c2pwp8rlk` (`relaleap-slt-large-run1`)
- Price: $1.49/hr
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Volume: 50GB

## Command observed

```bash
PYTHONPATH=src python3 run_slt_large.py --device cuda --epochs 3 --n-chains 8 --n-samples 1000
```

## Report verification

`artifacts/slt_large/slt_tinyshakespeare_report.json` parsed as valid JSON and reported:

- `status`: `complete`
- `device`: `cuda`
- `epochs`: 3
- `n_chains`: 8
- `n_samples`: 1000
- `elapsed_seconds`: 3873.441246986389

## Retrieved artifacts

- `artifacts/slt_large.log` — 2,342 bytes
- `artifacts/slt_large/slt_tinyshakespeare_report.json` — 21,342 bytes
- `artifacts/slt_large/tiny_char_transformer.pt` — 478,902 bytes
- `artifacts/slt_large/tinyshakespeare.txt` — 1,115,394 bytes

## Cost / cleanup

- Observed pod lifetime was about 1h53m from Runpod `createdAt` to deletion, so expected compute cost is roughly $2.80 before provider rounding/storage effects.
- Deletion returned `{ "deleted": true, "id": "kfzk2c2pwp8rlk" }`.

## Conclusion

The larger SLT validation run completed successfully, artifacts were preserved locally, and the paid pod was terminated.
