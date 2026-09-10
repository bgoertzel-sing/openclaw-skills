# Run 20260719T233140Z-epc-correctness-scale-audit: epc-correctness-scale-audit

- Project: `relaleap`
- Started: `2026-07-19T23:31:40Z`
- Finished: `2026-07-19T23:32:03Z`
- Status: `failed`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc`

## Question

Fill in the precise question this run answers.

## Hypothesis or expected behavior

Fill in before interpreting the result.

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

**Observed:** Failed closed after processing all checkpoints because one
nearly rank-degenerate ePC layer made float32 feature-space and Gram-space CKA
differ beyond the frozen numerical tolerance. No scientific result accepted.

**Resolution:** The v2 run repeated both formulations in float64 and passed.
This failed attempt remains preserved as detector-validation evidence.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up
