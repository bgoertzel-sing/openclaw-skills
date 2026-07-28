# EPC r8 Broad Outcome — RUN.md

## Status: COMPLETE

- **Experiment ID:** 20260720T193211Z-epc-r8-broad-outcome
- **Pod:** `sgmngeyziytvbv` (A100 PCIe 80GB, $1.39/hr)
- **Source commit:** `ecf2f79`
- **Schema:** `relaleap.epc_r8_train.v1`
- **Config:** `configs/gpt2_epc_r8.json` (frozen_pre_run, pinned teacher/dataset revisions and SHAs)
- **Protocol:** `docs/epc_r8_broad_outcome_protocol.md`
- **Seeds:** 1729, 3253, 6421, 8191, 10103 (5 seeds)
- **Arms:** bp_ce, bp_kd, epc_original, epc_deep, bp_kd_wallclock (5 arms)
- **Total records:** 25 (5 seeds × 5 arms)
- **Started:** ~2026-07-20 21:43 PDT (relaunch after bug fix)
- **Completed:** ~2026-07-21 01:54 PDT (last arm seed 10103 bp_kd_wallclock)
- **Wall-clock duration:** ~4h 11m

## Results Summary

| Arm | val_loss (mean±sd) | val_ppl (mean) | kd_gap (mean nats) | updates (mean) | elapsed (mean s) |
|---|---|---|---|---|---|
| bp_ce | 6.261±0.060 | 524.3 | 1160.9 | 200 | 78 |
| bp_kd | 7.039±0.056 | 1141.6 | 823.8 | 200 | 74 |
| epc_original | 6.781±0.146 | 888.6 | 978.0 | 200 | 445 |
| epc_deep | 6.754±0.131 | 863.2 | 960.6 | 200 | 1738 |
| bp_kd_wallclock | 5.785±0.135 | 327.5 | 469.8 | 1334 | 445 |

Teacher reference: val_loss=4.124, val_perplexity=61.8.

### activity_energy_monotone

All 10 EPC records (5 seeds × {epc_original, epc_deep}) have `activity_energy_monotone: true`.

## Key Findings

1. **bp_kd_wallclock dominates on val loss/perplexity** at matched wall-clock time (val_ppl ~327 vs ~524 for bp_ce, ~863 for epc_deep, ~889 for epc_original). This is because plain KD completes ~6.7x more update steps (1334 vs 200) in the same time budget.

2. **At matched update count (200), bp_ce has lower val_loss than both EPC arms** (6.261 vs 6.754–6.781). EPC does not beat plain cross-entropy on raw validation loss at equal updates.

3. **EPC arms satisfy activity_energy_monotone across all 5 seeds** — the structural energy-monotonicity property holds robustly. This is the primary positive EPC finding.

4. **epc_deep (T=12) is slightly better than epc_original on val_loss** (6.754 vs 6.781) but within seed variance (±0.13).

5. **bp_kd (200 updates) is worst on val_loss** (7.039) — plain KD at matched updates produces worse students than plain CE, consistent with the KD signal being noisier at low update counts.

6. **kd_gap ordering:** bp_ce (1161) > epc_original (978) > epc_deep (961) > bp_kd (824) > bp_kd_wallclock (470). bp_kd_wallclock closes the KD gap most effectively through sheer volume of updates.

## Artifacts

- `artifacts/r8/results/r8/train/training_summary.json` — 25-record summary
- `artifacts/r8/results/r8/train/seed*.json` — per-seed per-arm detailed metrics (including credit_assignment, evaluation_manifest, checkpoint_manifest for EPC arms)
- `artifacts/r8/results/r8/train/checkpoints/` — 20 checkpoints (4 arms × 5 seeds; bp_kd_wallclock not checkpointed)
- `artifacts/r8/r8_train.log` — training log

## Interpretation

The headline finding is that EPC's energy-monotonicity property is structurally validated (10/10 EPC records), but EPC does not beat plain baselines on raw validation loss at either matched update count or matched wall-clock time. The wallclock-matched KD baseline dominates on raw performance because it simply completes far more gradient steps. The scientific interest in EPC would need to come from properties other than raw val loss — e.g., the energy-monotonicity structure, credit assignment patterns, or generalization properties not captured by val perplexity.

## Exit status: 0 (all 25 records produced, no crashes)
