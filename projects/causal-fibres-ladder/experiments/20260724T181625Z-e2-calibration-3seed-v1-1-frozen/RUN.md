# Run 20260724T181625Z-e2-calibration-3seed-v1-1-frozen: e2-calibration-3seed-v1-1-frozen

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T18:16:25Z`
- Finished: `2026-07-24T18:16:25Z`
- Status: `failed`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Can the frozen three-seed calibration campaign start in the recorded venv?

## Hypothesis or expected behavior

The runner should import the local RelaLeap source and then execute all seeds.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seeds: `2111, 3253, 4517`.

## Results

- Exit status: 1
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

The run failed before any seed began because `PYTHONPATH=src` was absent and
`relaleap` could not be imported. No scientific artifact was produced. The
failure is retained; the corrected rerun is
`../20260724T181654Z-e2-calibration-3seed-v1-1-frozen-rerun/`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Relaunch with the repository source path explicit.
