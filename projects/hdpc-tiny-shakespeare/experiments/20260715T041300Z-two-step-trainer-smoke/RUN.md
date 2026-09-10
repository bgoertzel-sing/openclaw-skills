# Run 20260715T041300Z-two-step-trainer-smoke: two-step-trainer-smoke

- Project: `hdpc-tiny-shakespeare`
- Started: `2026-07-15T04:13:00Z`
- Finished: `2026-07-15T04:13:00Z`
- Status: `failed`
- Local or remote: `local`
- Working directory: `projects/hdpc-tiny-shakespeare/repos/hdpc-tiny-shakespeare`

## Question

Can the two-step trainer smoke run directly from the repository checkout?

## Hypothesis or expected behavior

Expected the module to resolve from the checkout.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: record here when relevant.

## Results

- Exit status: 1
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

The command failed before model or data execution because the package was not
installed and `PYTHONPATH=src` was omitted. No scientific output was produced.
The corrected invocation is recorded in sibling run
`20260715T041310Z-two-step-trainer-smoke-pypath`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up
