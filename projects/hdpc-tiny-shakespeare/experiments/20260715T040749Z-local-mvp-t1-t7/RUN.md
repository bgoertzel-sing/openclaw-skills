# Run 20260715T040749Z-local-mvp-t1-t7: local-mvp-t1-t7

- Project: `hdpc-tiny-shakespeare`
- Started: `2026-07-15T04:07:49Z`
- Finished: `2026-07-15T04:07:54Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `projects/hdpc-tiny-shakespeare/repos/hdpc-tiny-shakespeare`

## Question

Does the local HDPC MVP satisfy its seven CPU correctness tests (T1-T7)?

## Hypothesis or expected behavior

Expected: all seven tests pass with the implementation-brief tolerances.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: deterministic fixture seeds 0, 3, and 7;
  tiny GPT-2-compatible random configuration (2 layers, 32 hidden units).

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Observation: 7/7 tests passed in 0.84 seconds on CPU. The only warning was the
host Python's unrelated `requests` dependency-version warning. This validates
the tested zero-error identity, anchor, energy descent, endpoint signatures,
crown identity, and controlled four-layer MLP equilibrium invariant. It is an
implementation smoke result, not evidence about language-model quality or
large-model PC behavior.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Run the two-step local pretrained-model/data trainer smoke before specifying a
paid pilot. LoRA remains intentionally outside this correctness scaffold.
