# Run 20260724T000712Z-e1-homotopy-smoke: e1-homotopy-smoke

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T00:07:12Z`
- Finished: `2026-07-24T00:07:13Z`
- Status: `failed`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Launch the reduced E1 homotopy smoke from the isolated R8 worktree.

## Hypothesis or expected behavior

The runner should import the worktree package and execute.

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

**Observed:** the command failed before E1 execution because the isolated
worktree was not installed in the project venv and `src` was absent from
`PYTHONPATH` (`ModuleNotFoundError: relaleap`). No scientific artifact was
produced. The corrected final run is
`../20260724T000851Z-e1-homotopy-smoke-final/`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Use the isolated worktree's `src` explicitly in the command environment.
