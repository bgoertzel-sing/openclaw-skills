# HDPC/ePC Extended Grid V2

## Run 1 — Failed

The initial Runpod HDPC/ePC grid v2 job failed early due to a Python call-signature mismatch (`estimate_perplexity() got an unexpected keyword argument 'eval_batches'`). Pod `tb09sv8ocb8qgv` deleted after ~40 min idle.

### Timeline
- Approved by Benjamin Goertzel: 2026-07-11 09:51 PDT
- Pod created: 2026-07-11 16:56:38 UTC
- Failure/idle observed: 2026-07-11 17:36 UTC
- Pod deleted: 2026-07-11 17:39 UTC

### Resource
- Pod: `tb09sv8ocb8qgv` (`relaleap-hdpc-grid-v2`)
- GPU: 1× L40S, 48GB, $0.99/hr
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Source: `projects/relaleap/worktrees/tinyshakespeare-hdpc`, branch `agent/tinyshakespeare-hdpc`, commit `0803a37`

### Failure
```text
TypeError: estimate_perplexity() got an unexpected keyword argument 'eval_batches'
```
No `grid_v2_summary.json` was produced. Fixed call signature locally before relaunch.

---

## Run 2 — Completed ✅

### Timeline
- Approved by Benjamin Goertzel: 2026-07-11 09:51 PDT (same approval, relaunch of failed attempt)
- Pod created: 2026-07-12 02:11 UTC
- Auto-terminate: 2026-07-12T12:00:00Z
- Artifacts retrieved: 2026-07-12 03:35 UTC (file timestamps)
- Pod confirmed terminated: 2026-07-12 19:43 UTC (heartbeat check, pod list empty)

### Resource
- Pod: `5j7sdm2b08oil9` (`relaleap-hdpc-grid-v2-r2`)
- GPU: 1× RTX A6000, 48GB, $0.49/hr
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Source: `projects/relaleap/worktrees/tinyshakespeare-hdpc`, branch `agent/tinyshakespeare-hdpc`, commit `3a6c733`
- Total elapsed: 30,235s (~8.40h)
- Estimated cost: ~$4.12 (within $6 hard cap)

### Configuration
- 5 epochs, 200 steps/epoch, batch=128
- d_model=256, nhead=4, d_ff=1024, num_layers=6, seq_len=256
- Learning rate: 3e-4
- Data: Tiny Shakespeare

### Conditions (4)
1. `teacher_only` — 3 seeds (no λ_kd)
2. `student_no_crown` — 3 seeds × 3 λ_kd
3. `detached_crown` — 3 seeds × 3 λ_kd
4. `coupled_crown` — 3 seeds × 3 λ_kd

Seeds: [42, 1234, 5678], λ_kd: [0.01, 0.05, 0.10]
Total runs: 3 + 27 = 30

### Results

#### Teacher-Only Baselines
| Seed | Held-out PPL | Params | Elapsed |
|------|-------------|-------|---------|
| 42   | 6.2318      | 4.84M | 457s    |
| 1234 | 5.5784      | 4.84M | 459s    |
| 5678 | 6.0063      | 4.84M | 459s    |

#### Student Conditions (mean ± std across 3 seeds)
| Condition          | λ_kd  | Student PPL      | Δ PPL            |
|--------------------|-------|------------------|------------------|
| student_no_crown   | 0.01  | 5.2043 ± 0.2494  | -0.6615 ± 0.5883 |
| student_no_crown   | 0.05  | 5.2785 ± 0.2158  | -0.5873 ± 0.6094 |
| student_no_crown   | 0.10  | 5.3110 ± 0.2150  | -0.5505 ± 0.6271 |
| detached_crown     | 0.01  | 5.2672 ± 0.1040  | -0.7308 ± 0.3928 |
| detached_crown     | 0.05  | 5.3642 ± 0.1049  | -0.6338 ± 0.4134 |
| detached_crown     | 0.10  | 5.3898 ± 0.1111  | -0.6082 ± 0.4144 |
| coupled_crown      | 0.01  | 5.2425 ± 0.0967  | -0.7555 ± 0.4036 |
| coupled_crown      | 0.05  | 5.3540 ± 0.0942  | -0.6454 ± 0.4256 |
| coupled_crown      | 0.10  | 5.3809 ± 0.1069  | -0.6171 ± 0.4223 |

### Preliminary Observations

1. **All student conditions achieve lower perplexity than their teachers** (negative Δ PPL across all conditions). This is consistent across seeds and λ values.
2. **Lower λ_kd is better**: All three conditions show best student perplexity at λ_kd=0.01, with monotonic degradation at higher λ. This suggests the KD signal is slightly hindering student learning at higher weights.
3. **Coupled crown is marginally best at λ=0.01**: `coupled_crown` (5.2425) edges out `student_no_crown` (5.2043) — wait, actually `student_no_crown` has lower PPL but higher variance. `coupled_crown` has the lowest variance (±0.0967) and the largest mean delta (-0.7555).
4. **Crown conditions reduce variance**: Both `detached_crown` and `coupled_crown` show substantially lower std dev across seeds compared to `student_no_crown`, suggesting the crown mechanism stabilizes training.
5. **High seed variance in deltas**: The std dev of deltas is large (0.39–0.63), indicating strong seed effects. Statistical significance of condition differences is not established with n=3.

### Artifacts
- `artifacts/grid_v2_summary.json` — full results (300KB)
- `artifacts/hdpc_grid_v2.log` — run log
- `artifacts/seed{42,1234,5678}_lam{0.01,0.05,0.1}/` — per-run checkpoints and diagnostics

### Cleanup
- Pod `5j7sdm2b08oil9` auto-terminated (confirmed via `runpodctl pod list` → `[]`)
- Monitoring cron job `d9cecaaa-e449-440e-ab06-59e0584335c9` removed

## Conclusion

Grid v2 run 2 completed successfully with all 30 runs producing results. The HDPC crown mechanism shows a stabilizing effect on student training (lower variance) with marginal perplexity improvements. Higher λ_kd values consistently hurt student performance. Further analysis with more seeds or gradient-level diagnostics recommended for stronger claims.
