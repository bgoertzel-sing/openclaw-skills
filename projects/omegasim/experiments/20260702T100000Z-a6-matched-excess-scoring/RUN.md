# Run 20260702T100000Z-a6-matched-excess-scoring: A6 matched excess-over-control scoring

- Project: `omegasim`
- Started: `2026-07-02T10:00:00-07:00`
- Finished: `2026-07-02T10:08:59-07:00`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/omegasim/repos/omegasim`
- Code commit after implementation: `463a2de0af84e01dc8d73a11e8cf8d85908440e0`
- Artifact directory: `projects/omegasim/artifacts/a6-matched-excess-20260702T100000Z/`

## Question

Can A6 appraisal candidates be scored fail-closed against matched linear and shuffled controls, so candidates require excess functional movement above controls for the same seed/gain/delay/coupling tuple?

## Implementation

Added `matched_excess_scores(summary_rows)` in `src/omegasim/a6_model.py` and extended `scripts/run_a6_sweep.py` to emit:

- `matched_excess_summary.csv`
- `matched_excess_summary.json`

Matching strategy: exact `(seed, gain, delay, coupling)` tuple, requiring both linear and shuffled controls. Missing controls fail closed.

Candidate gate requires appraisal functional-candidate status plus bounded matched controls, positive excess over the strongest matched control in functional tail range and artifact tail range, at least two positive functional-component excess terms, no detected short tail period, no flat artifact tail, and no collapsed risk tail. If matched controls tie or dominate functional/artifact excess, the reason is `matched_control_dominates_or_ties`.

## Command

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
python3 -m py_compile src/omegasim/a6_model.py scripts/run_a6_sweep.py
python3 scripts/run_a6_sweep.py --steps 500 --out /home/openclaw/research-agent/projects/omegasim/artifacts/a6-matched-excess-20260702T100000Z
```

## Results

- Unit tests: 5 passed.
- `py_compile`: passed.
- Sweep: 243 local conditions over controls `appraisal`, `linear`, `shuffled`; seeds `7,11,17`; gains `1.5,3.0,5.0`; delays `0,3,7`; couplings `0.15,0.35,0.60`.
- Absolute functional candidates remain: appraisal 24/81, linear 37/81, shuffled 2/81.
- Matched excess-over-control candidates: 7/81 appraisal rows.
- Reason counts among appraisal rows: `matched_control_dominates_or_ties` 72, `appraisal_exceeds_matched_controls` 7, `absolute_or_excess_gate_failed` 2.
- Mean functional excess over strongest matched control: -0.2594; max: 0.3459.
- Mean artifact-range excess over strongest matched control: -0.0407; max: 0.0989.

Matched excess candidate runs:

| run | functional excess | artifact excess | entropy excess |
|---|---:|---:|---:|
| appraisal_seed7_g5_d0_c0p6 | 0.088 | 0.059 | -0.025 |
| appraisal_seed11_g5_d0_c0p35 | 0.125 | 0.027 | -0.021 |
| appraisal_seed11_g5_d0_c0p6 | 0.186 | 0.042 | -0.025 |
| appraisal_seed11_g5_d3_c0p6 | 0.070 | 0.006 | -0.020 |
| appraisal_seed17_g5_d0_c0p6 | 0.107 | 0.014 | -0.016 |
| appraisal_seed17_g5_d3_c0p35 | 0.051 | 0.029 | 0.001 |
| appraisal_seed17_g5_d3_c0p6 | 0.346 | 0.078 | -0.015 |

Candidate parameter concentration: all matched-excess candidates have `gain=5.0`; couplings are `0.60` (5 rows) or `0.35` (2 rows); delays are `0` (4 rows) or `3` (3 rows).

## Interpretation

**Observed:** Exact-tuple matched scoring is now in the sweep artifact. Most appraisal rows fail because matched controls tie or dominate; this preserves the previous fail-closed posture for broad appraisal-specific claims.

**Observed:** A small, localized high-gain region (`gain=5.0`, `coupling in {0.35,0.60}`, `delay in {0,3}`) exceeds both matched controls on the configured functional/artifact excess gate.

**Inferred:** The promising region is narrow and seed-sensitive, not yet evidence of a robust strange attractor. It is appropriate as a denser next slice and as input to residual-state/lobe/recurrence analysis.

## Artifacts

- Full sweep: `projects/omegasim/artifacts/a6-matched-excess-20260702T100000Z/`
- Experiment-local metrics: `metrics_summary.json`, `metrics_matched_excess_summary.csv`, `metrics_matched_excess_summary.json`
- Logs: `stdout.log`, `stderr.log`, `status.json`, `git.txt`, `env.txt`, `command.sh`

## Limitations / risks

- Matching is exact-tuple rather than nearest amplitude/variance matching across parameter space; exact tuple is conservative and clear for the existing balanced grid.
- Current excess metrics use coarse tail ranges and role entropy, not recurrence geometry or grammatical lobe structure.
- Candidate thresholds are heuristic and should be preregistered/refined before stronger claims.
