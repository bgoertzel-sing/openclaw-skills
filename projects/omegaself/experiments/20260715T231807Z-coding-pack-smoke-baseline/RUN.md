# Run 20260715T231807Z-coding-pack-smoke-baseline: coding-pack-smoke-baseline

- Project: `omegaself`
- Started: `2026-07-15T23:18:07Z`
- Finished: `2026-07-15T23:18:08Z`
- Status: `failed`
- Local or remote: `local`
- Working directory: `projects/omegaself/repos/omegaself-coding-agent-pack`

## Question

Does the coding pack run unchanged via its documented `./scripts/smoke_test.sh` command on this host?

## Hypothesis or expected behavior

The packaged script should be executable and should enter the reference validation suite.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: record here when relevant.

## Results

- Exit status: 126
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Observed: the command exited 126 before tests because `scripts/smoke_test.sh` has mode `0644`. This is a packaging/documentation discrepancy, not a runtime test failure. The file was not modified.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Invoke the same unchanged script through `bash` and preserve this failed run.
