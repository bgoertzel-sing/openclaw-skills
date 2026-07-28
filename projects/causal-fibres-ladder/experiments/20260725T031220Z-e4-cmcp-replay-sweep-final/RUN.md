# Run 20260725T031220Z-e4-cmcp-replay-sweep-final: e4-cmcp-replay-sweep-final

- Project: `causal-fibres-ladder`
- Started: `2026-07-25T03:12:20Z`
- Finished: `2026-07-25T03:12:46Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does increasing the replay coefficient expose the late-episode CMCP
plasticity advantage suggested by the earlier typed-retention calibration?

## Hypothesis or expected behavior

Because naive precision reaches 21 while CMCP remains near the oracle value
of 7.5, stronger replay should make naive accumulation increasingly rigid and
move the Task-B crossover earlier.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seeds: `61001, 62119, 63241`
- Replay coefficients: `0.15, 0.30, 0.50`
- Raw artifact:
  `../../artifacts/e4-cmcp-replay-sweep-v1.json`

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

Episode-6 three-seed means:

| Replay | First mean Task-B crossover | CMCP Task-B | Naive Task-B | CMCP Task-A | Naive Task-A |
|---:|---:|---:|---:|---:|---:|
| 0.15 | 6 | 0.848958 | 0.817708 | 0.736979 | 0.872396 |
| 0.30 | 5 | 0.869792 | 0.770833 | 0.880208 | 0.869792 |
| 0.50 | 3 | 0.848958 | 0.716146 | 0.898438 | 0.833333 |

Naive episode-6 effective precision was exactly `21.0` in all nine runs.
CMCP-minus-naive Task-B accuracy grew from `+0.03125` to `+0.09896` and
`+0.13281` as replay increased. Naive retained lower ECE at all three
coefficients.

## Interpretation

**Observed:** Stronger replay moved the mean Task-B crossover earlier and
increased CMCP's final Task-B advantage. At coefficients `0.30` and `0.50`,
CMCP also exceeded naive Task-A accuracy at episode 6.

**Inferred:** CMCP's bounded precision can preserve plasticity when replay
pressure is consequential. This is a controlled coefficient sweep on the
three already-open calibration seeds, not an independently confirmed effect.
Naive's better ECE shows that the advantage is not uniform across metrics.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Freeze a separate confirmation protocol only if this coefficient-dependent
tradeoff is worth promoting; do not reuse the reserved typed-retention seeds
without new thresholds.
