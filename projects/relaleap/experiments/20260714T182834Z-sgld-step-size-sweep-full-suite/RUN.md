# Run 20260714T182834Z-sgld-step-size-sweep-full-suite: sgld-step-size-sweep-full-suite

- Project: `relaleap`
- Started: `2026-07-14T18:28:34Z`
- Finished: `2026-07-14T18:28:50Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap`

## Question

Does adding the SGLD tuning sweep and diagonal preconditioner regress any existing RelaLeap tests?

## Hypothesis or expected behavior

All existing and new tests should pass using the repository's declared CPU test command.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data: deterministic synthetic fixtures in the test suite; no external data.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Observed: 97 of 97 tests passed in 15.51 seconds. The new public imports, generic model wrapper, and sweep logic integrate without a detected regression. This is software verification, not evidence that a production SGLD run has converged.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Run the short sweep on the actual production energy model before authorizing another paid chain.
