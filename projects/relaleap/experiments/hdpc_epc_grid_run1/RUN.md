# HDPC/ePC Grid Run 1

## Summary

Heartbeat found the remaining HDPC/ePC Runpod grid job complete and idle, retrieved artifacts, verified `grid_summary.json`, and deleted the pod to stop paid compute.

## Timeline

- Pod created: 2026-07-11 03:44:41 UTC
- Completion/idle observed: 2026-07-11 07:19 UTC
- Pod deleted: 2026-07-11 07:24 UTC

## Resource

- Provider: Runpod
- Pod: `zivpxu06yhmx40` (`relaleap-hdpc-grid-run1`)
- Price: $0.49/hr
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Volume: 30GB

## Command observed

```bash
PYTHONPATH=src python3 run_grid.py --device cuda --epochs 5 --steps-per-epoch 200 --batch-size 128 --d-model 256 --nhead 4 --d-ff 1024 --num-layers 6 --seq-len 256
```

## Report verification

`artifacts/hdpc_grid/grid_summary.json` parsed as valid JSON. Top-level fields:

- `config`
- `seeds`
- `lambdas`
- `temperatures`
- `results`
- `total_elapsed`

The `results` list contains 9 grid entries.

## Retrieved artifacts

Copied to `projects/relaleap/experiments/hdpc_epc_grid_run1/artifacts/`:

- `grid.log` — 2,402 bytes
- `hdpc_grid/grid_summary.json` — 148,737 bytes
- 9 checkpoint files under `hdpc_grid/seed*_lam*/hdpc_tinyshakespeare_smoke.pt`, each 38,844,433 bytes

## Cost / cleanup

- Observed pod lifetime was about 3h40m from Runpod `createdAt` to deletion, so expected compute cost is roughly $1.80 before provider rounding/storage effects.
- Deletion returned `{ "deleted": true, "id": "zivpxu06yhmx40" }`.
- `runpodctl pod list` returned `[]` after cleanup.

## Conclusion

The HDPC/ePC grid run completed, all visible artifacts were preserved locally, and the final paid Runpod pod was terminated.
