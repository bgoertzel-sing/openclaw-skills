# RelaLeap r5 Runpod Pilot — 2026-07-19

## Status: COMPLETE — Promotion eval FAILED (negative result)

## Run context

- **Pod:** oo20lk2075y0dx (Runpod, deleted)
- **Provisioned:** 2026-07-19 15:32 UTC
- **Completed:** 2026-07-19 18:08 UTC (~2.6h wall)
- **Source commit:** dc61f3165a95653561e01d478eee5d3b75a7a50d
- **Protocol SHA256:** ac073e74808a41c98c11a892f78ca0460f99d56a4177791fb342dd3eb4d744b8
- **Device:** CUDA (single GPU)
- **Dataset:** wikitext-103-raw-v1 (cached), TinyStories (downloaded, caused offline-mode error but after eval was done)
- **Seeds:** 1729, 3253, 6421

## Arms

| Arm | Description | Updates | Wall time |
|-----|-------------|---------|-----------|
| bp_ce | BP + cross-entropy | 1000 | ~265s |
| bp_kd | BP + knowledge distillation | 1000 | ~280s |
| epc_kd | ePC + knowledge distillation (experimental) | 1000 | ~1170s |
| bp_kd_wallclock | BP+KD matched to epc_kd wall time | ~4185 | ~1170s |

## Results (student val_loss, lower is better)

| Seed | bp_ce | bp_kd | epc_kd | bp_kd_wallclock |
|------|-------|-------|--------|-----------------|
| 1729 | 5.301 | 5.997 | 6.489 | 4.966 |
| 3253 | 5.249 | 6.004 | 6.505 | 4.941 |
| 6421 | 5.283 | 5.970 | 6.539 | 4.949 |

Teacher val_loss: ~4.13–4.15.

## Promotion evaluation

```
passes_all: false
passes_no_seed_regression: false
passes_update_matched_gain: false    (mean gain: -0.52 nats — ePC_KD WORSE)
passes_wall_clock_matched_gain: false (mean gain: -1.56 nats — ePC_KD WORSE)
max_per_seed_regression_vs_update_matched_bp_kd_nats: 0.569
```

## Interpretation

**ePC_KD is strictly worse than BP+KD** at this scale and configuration:

1. **Update-matched:** ePC_KD (6.49–6.54) is ~0.5 nats worse than BP+KD (5.97–6.00) with the same 1000 updates, despite ePC_KD taking ~4× longer per update.
2. **Wall-clock-matched:** ePC_KD (6.49–6.54) is ~1.6 nats worse than BP+KD given the same wall time (~1170s), because BP+KD can do ~4× more updates in that time.
3. ePC_KD is also worse than plain BP+CE (5.25–5.30), which is the weakest baseline.
4. activity_energy_monotone: true for all epc_kd runs (the one positive signal).
5. kd_gap_nats is very high (~880–893), suggesting the student is not learning effectively from the teacher under ePC.

## Notable issue

After the promotion eval completed, the script attempted to load `roneneldan/TinyStories` for a secondary evaluation but hit a `ConnectionError` because HF offline mode was enabled. This did not affect the primary promotion eval results.

## Artifacts

All 13 JSON files + summary.json retrieved to:
`projects/relaleap/experiments/r5-runpod-20260719/`

## Cost

Pod ran ~2.6h on a single GPU. Terminated promptly after completion.
