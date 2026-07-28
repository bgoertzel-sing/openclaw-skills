# Run 20260715T154840Z-epc-local-credit-normalization: epc-local-credit-normalization

- Project: `relaleap`
- Started: `2026-07-15T15:48:40Z`
- Finished: `2026-07-15T15:48:42Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/worktrees/tinyshakespeare-hdpc`

## Question

Does batch-consistent hidden-error normalization restore nonzero ePC credit to
earlier transformer blocks while preserving the exact KD endpoint and monotone
activity energy?

## Hypothesis or expected behavior

Expected: depth one remains exact KD; depth four produces nonzero gradients in
both transformer blocks; every accepted relaxation step is non-increasing.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Synthetic deterministic seeds are fixed in `tests/test_hdpc_tinyshakespeare.py`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Observed: all eight transformer/Tiny Shakespeare component tests passed at
commit `cbe4c08`, including exact depth-one KD equality, monotone depth-four
relaxation, and nonzero credit in both the earlier and later residual blocks.
The complete repository suite separately passed 110 tests.

Inferred: the normalization bug exposed by the first corpus gate is corrected
at the intended software invariant level. This is not evidence of improved
held-out perplexity. A new frozen corpus protocol is required before evaluating
whether the corrected local credit is scientifically useful.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Preregister a second diagnostic that records layerwise norm-ratio ranges before
training and compares the corrected objective against the same BP/KD controls.
