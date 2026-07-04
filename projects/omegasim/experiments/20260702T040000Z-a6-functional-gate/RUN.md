# Run 20260702T040000Z-a6-functional-gate: A6 functional candidate gate

- Project: `omegasim`
- Started: `2026-07-02T04:00:00Z`
- Finished: `2026-07-02T04:00:??Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/omegasim/repos/omegasim`

## Question

Can the A6 smoke sweep use stricter functional criteria requiring artifact/debt/risk/prediction-error movement, rather than accepting role-switching alone?

## Preregistration

- `projects/omegasim/docs/a6_functional_candidate_gate.md`

## Command

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
python3 scripts/run_a6_sweep.py --steps 500 --out /home/openclaw/research-agent/projects/omegasim/artifacts/a6-functional-gate-20260701
```

## Results

- Unit tests: 3 passed.
- Sweep: 243 local conditions over controls `appraisal`, `linear`, `shuffled`; seeds `7,11,17`; gains `1.5,3.0,5.0`; delays `0,3,7`; couplings `0.15,0.35,0.60`.
- Artifacts: `projects/omegasim/artifacts/a6-functional-gate-20260701/`.

| control | n | functional candidates | mean switch rate | mean entropy | mean artifact tail range | mean functional tail range |
|---|---:|---:|---:|---:|---:|---:|
| appraisal | 81 | 24 | 0.040 | 1.391 | 0.095 | 0.481 |
| linear | 81 | 37 | 0.078 | 1.745 | 0.134 | 0.698 |
| shuffled | 81 | 2 | 0.758 | 1.995 | 0.008 | 0.173 |

## Interpretation

**Observed:** The functional gate strongly reduces shuffled-control false positives compared with role-symbol-only criteria: shuffled controls fall to 2/81 candidates and have almost flat artifact tails.

**Observed:** Linear controls still pass more often than appraisal controls: 37/81 versus 24/81. Therefore this is not evidence for an appraisal-specific nonperiodic cognitive regime.

**Inferred:** The next metric pass should compare matched appraisal conditions against linear/shuffled controls directly, e.g. excess artifact/debt/risk/prediction-error movement and recurrence structure above control baselines.

**Conclusion:** OmegaSim is moving again locally, with an explicit fail-closed result. Continue A6 by adding amplitude-matched/excess-over-control scoring before any denser phase diagram or attractor-like language.
