# Run 20260702T170555Z-a6-excess-control: A6 matched excess-over-control scoring

- Project: `omegasim`
- Started: `2026-07-02T17:05:55Z`
- Finished: `2026-07-02T17:06:??Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/omegasim/repos/omegasim`

## Question

Do any A6 thresholded-appraisal conditions exceed matched linear and shuffled controls with the same seed/gain/delay/coupling under comparable amplitude/state-movement criteria?

## Preregistered criterion

See `projects/omegasim/docs/a6_matched_excess_control_gate.md`, written before interpreting the sweep output. In short, appraisal candidates must have matched linear and shuffled controls, pass the absolute functional gate, exceed the strongest matched control on combined functional movement by at least `0.05`, exceed artifact tail movement by at least `0.005`, have at least two positive state-range excess terms, avoid short-period tails, avoid risk collapse, and avoid trivial flat artifact tails.

## Commands and exit statuses

Recorded in `command.sh`; exact outputs are in `stdout.log` and `stderr.log`.

| command | exit |
|---|---:|
| `PYTHONPATH=src python3 -m unittest discover -s tests -v` | 0 |
| `python3 scripts/run_a6_sweep.py --steps 500 --out /home/openclaw/research-agent/projects/omegasim/artifacts/a6-excess-control-20260702T170555Z` | 0 |
| `git diff --check` | 0 |

## Results

- Unit tests: 5 passed.
- Sweep: 243 local conditions over controls `appraisal`, `linear`, `shuffled`; seeds `7,11,17`; gains `1.5,3.0,5.0`; delays `0,3,7`; couplings `0.15,0.35,0.60`.
- Absolute A6 functional candidates remain: appraisal 24/81, linear 37/81, shuffled 2/81.
- Matched excess-over-control candidates: 7/81 appraisal runs.
- Artifacts: `projects/omegasim/artifacts/a6-excess-control-20260702T170555Z/`.
- Candidate extracts: `candidates.csv`, `candidates.json`.

| run | score | functional excess | artifact excess | debt excess | risk excess | pred-error excess |
|---|---:|---:|---:|---:|---:|---:|
| `appraisal_seed17_g5_d3_c0p6` | 0.383 | 0.346 | 0.078 | 0.099 | 0.199 | -0.030 |
| `appraisal_seed11_g5_d0_c0p6` | 0.204 | 0.186 | 0.042 | 0.084 | 0.093 | -0.033 |
| `appraisal_seed11_g5_d0_c0p35` | 0.136 | 0.125 | 0.027 | 0.049 | 0.072 | -0.023 |
| `appraisal_seed7_g5_d0_c0p6` | 0.115 | 0.088 | 0.059 | 0.046 | 0.016 | -0.032 |
| `appraisal_seed17_g5_d0_c0p6` | 0.112 | 0.107 | 0.014 | 0.070 | 0.055 | -0.032 |
| `appraisal_seed11_g5_d3_c0p6` | 0.071 | 0.070 | 0.006 | 0.045 | 0.042 | -0.024 |
| `appraisal_seed17_g5_d3_c0p35` | 0.066 | 0.051 | 0.029 | 0.010 | 0.029 | -0.017 |

Candidate concentration: all matched-excess candidates occur at `gain=5.0`; couplings are `0.35` or `0.60`; delays are `0` or `3`; none occur at `delay=7` or `coupling=0.15`. The strongest tuple is `gain=5.0, coupling=0.60, delay=3`, especially seed 17.

Reason counts across appraisal rows: `appraisal_exceeds_matched_controls=7`, `matched_control_dominates_or_ties=72`, `absolute_or_excess_gate_failed=2`.

## Interpretation

Observed: Several high-gain appraisal runs exceed exact matched linear and shuffled controls on combined functional state movement and artifact movement while retaining high role entropy and nontrivial switching. This supports a narrow next phase-diagram slice around high gain and moderate/high coupling.

Observed limitation: Prediction-error tail range is lower than controls in all seven candidates, so the excess signal is artifact/debt/risk dominated rather than a broad excess across every functional variable. This is not evidence for strange attractors or full appraisal-specific cognition.

## Recommended next slice

Run a denser local phase diagram around the matched-excess region:

- `gain in {4.25, 4.75, 5.0, 5.25, 5.75}`;
- `coupling in {0.30, 0.35, 0.45, 0.55, 0.60, 0.70}`;
- `delay in {0, 1, 2, 3, 4}`;
- more seeds, e.g. `7,11,17,23,29`;
- preserve exact matched linear/shuffled controls and add residual-state/lobe metrics before any attractor language.
