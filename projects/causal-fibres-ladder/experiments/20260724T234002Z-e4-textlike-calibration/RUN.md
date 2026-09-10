# Run 20260724T234002Z-e4-textlike-calibration

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T23:40:02Z`
- Finished: `2026-07-24T23:41:02Z`
- Status: `failed non-ceiling substrate gate`
- Local or remote: `local CPU`
- Working directory:
  `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Which controlled-noise subset condition, among those with mean posthoc
extraction fidelity no greater than 92%, best recovers CS task-loss headroom
on the text-like grammar, and does the 75-update student remain non-ceiling?

## Frozen inputs

- Protocol: `docs/e4_textlike_external_validity_protocol.md`.
- Config: `configs/e4_textlike_bridge_calibration_v1.json`.
- Seeds: `42013, 43117, 44221`.
- Reserved confirmation seeds: `45329,46433,47543,48649,49757`.
- Exact command: `command.sh`.
- Repository branch/starting commit: `agent/e1-guarded-homotopy`,
  `5377d1ec9b369c239e87adcf9dfa94af9764fbb7`, with the recorded E4 bridge
  implementation diff.

## Expected behavior

The inherent surface fallback should yield about 96% extraction fidelity at
zero controlled noise and keep FF exact task accuracy below 92%. At least one
eligible subset condition should have defined positive mean G, permitting a
primary and thresholds to be frozen before confirmation.

## Results

- Final exit status: `0` after two retained pre-execution dependency failures.
- Raw per-seed JSON and aggregate: `artifacts/`.
- Initial invocation exited `1` before model construction because the
  repository-local package was not on `PYTHONPATH`; `command.sh` was corrected
  to export `PYTHONPATH=src` and the failed stderr was retained as
  `stderr.initial.log`.
- The second invocation exposed an unnecessary transitive import of the
  optional `causal_fibres` package through a shared scalar helper. The helper
  was made local to the bridge runner; stderr was retained as
  `stderr.second.log`.

## Interpretation

The extractor met its expected behavior (`96.09%` surface fidelity), but the
inherited width-24 homotopy/KD student reached only `15.36%` mean CS FF task
accuracy. This is far below the `[70%,92%]` non-ceiling interval, so no sink
result is scientifically eligible. The run triggered the preregistered
calibration correction to a direct supervised 75-update student.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.
