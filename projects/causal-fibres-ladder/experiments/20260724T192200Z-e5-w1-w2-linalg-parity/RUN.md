# Run 20260724T192200Z-e5-w1-w2-linalg-parity: e5-w1-w2-linalg-parity

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T19:22:00Z`
- Finished: `2026-07-24T19:22:00Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/morkql/repos/MORK`

## Question

Do pinned MORK linalg kernels reproduce a six-layer f32 forward pass and
five-step predictive relaxation at E5 numerical tolerances?

## Hypothesis or expected behavior

Fill in before interpreting the result.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- MORK branch/commit: `agent/e5-epc-kernel-probe` / `7673b02`.
- Independent Python f32 reference values are embedded in the Rust test.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Both tests pass. W1 maximum relative logit error is at most `1e-5` with exact
argmax; W2 terminal settled-state maximum absolute error is at most `1e-6`.
This validates standalone numerical kernels only. In-store rule application
and iterative tensor state require a new tensor-resource/sink adapter.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up
