# Run 20260702T012924Z-a6-smoke-sweep: a6-smoke-sweep

- Project: `omegasim`
- Started: `2026-07-02T01:29:24Z`
- Finished: `2026-07-02T01:29:30Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/omegasim/repos/omegasim`

## Question

Can a minimal A6 single-hive thresholded-appraisal model run reproducibly and identify bounded, structured, nonperiodic candidate regimes over gain/delay/coupling sweeps, with linear and shuffled controls available for comparison?

## Hypothesis or expected behavior

The first dependency-free harness should preserve bounded state variables, produce deterministic results per seed, and expose at least some high-gain delayed/coupled appraisal regimes with nontrivial role/lobe switching and artifact dynamics. This smoke run is not expected to establish a real strange attractor.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds: `7,11,17`
- Sweep: controls `appraisal, linear, shuffled`; gains `1.5,3.0,5.0`; delays `0,3,7`; couplings `0.15,0.35,0.60`; steps `500`.
- Output directory: `projects/omegasim/artifacts/a6-smoke-sweep-20260701/`

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `projects/omegasim/artifacts/a6-smoke-sweep-20260701/`
  - `summary.csv` / `summary.json`: 243 condition summaries.
  - Per-condition JSON files with full time series and metrics.
  - `aggregate_notes.md`: compact control comparison.

Observed stdout summary:

```text
wrote 243 runs to /home/openclaw/research-agent/projects/omegasim/artifacts/a6-smoke-sweep-20260701
bounded appraisal candidate structured-nonperiodic runs: 18
```

Aggregate post-run control comparison:

| control | n | naive candidates | nonperiodic tails | mean switch rate | mean role entropy | mean artifact tail range |
|---|---:|---:|---:|---:|---:|---:|
| appraisal | 81 | 18 | 65 | 0.040 | 1.391 | 0.095 |
| linear | 81 | 36 | 72 | 0.078 | 1.745 | 0.134 |
| shuffled | 81 | 81 | 81 | 0.758 | 1.995 | 0.008 |

## Interpretation

**Observed:** The A6 harness runs locally, is deterministic under fixed seeds, keeps all modeled state variables bounded in tests and in the smoke sweep, and produces high-gain appraisal regimes with mixed roles and visible artifact-state movement.

**Observed:** The naive macro-role criteria are too weak. Shuffled controls look highly active by entropy/switching and nonperiodic-tail tests while artifact dynamics are nearly flat (`mean artifact tail range 0.008`). Linear controls also score well under role-symbol criteria.

**Inferred:** The next OmegaSim metric pass should focus less on raw role-symbol entropy and more on functional recurrence: artifact utility/maturity movement, risk/debt recovery, lobe grammar conditioned on artifact state, and amplitude-matched appraisal-vs-control contrasts.

**Conclusion:** This is a successful reboot/smoke experiment, not yet evidence for a strange-attractor-like cognitive regime.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it, or from the repository:

```bash
python3 scripts/run_a6_sweep.py --steps 500 --out /home/openclaw/research-agent/projects/omegasim/artifacts/a6-smoke-sweep-20260701
```

## Follow-up

1. Tighten candidate criteria to require functional artifact/risk/debt dynamics, not only role switching.
2. Add recurrence/compressibility metrics over residual latent state.
3. Run a denser phase diagram around appraisal `gain=5`, `coupling in {0.35,0.60}`, `delay in {0,3,7}`.
4. Feed the resulting A6 spec back into Hyperseed note 0004 revision.
