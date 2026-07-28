# Run 20260724T184902Z-e2-c2-dictionary-5seed-v1-1-vectorized: e2-c2-dictionary-5seed-v1-1-vectorized

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T18:49:02Z`
- Finished: `running`
- Status: `running`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does vectorized MI calibration make the frozen C2 campaign tractable?

## Hypothesis or expected behavior

Vectorized MI should match the scalar statistic exactly and permit all seeds
to finish without changing permutations or model settings.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: record here when relevant.

## Results

- Exit status: pending
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

The run was manually interrupted after a second runtime audit. Vectorization
removed the MI loop, but the four-factor matcher exhaustively enumerated
`48P4` assignments for each 48-atom dictionary and every permutation. No seed
was sealed and no result is used.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Replace exhaustive rectangular matching with exact Hungarian assignment,
test equality against exhaustive matching on small cases, and rerun.
