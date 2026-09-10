# Run 20260714T182809Z-sgld-step-size-sweep-targeted: sgld-step-size-sweep-targeted

- Project: `relaleap`
- Started: `2026-07-14T18:28:09Z`
- Finished: `2026-07-14T18:28:12Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap`

## Question

Do the new SGLD step-size sweep and diagonal preconditioner satisfy their focused behavioral tests on a CPU quadratic model?

## Hypothesis or expected behavior

The sweep should reject divergent and poorly mixing candidates, select a reproducible interior step size, and the pilot preconditioner should reduce Hessian condition number.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds: 3, 4, 8, and 12 in `tests/test_step_size_sweep.py`; generated quadratic data only.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Observed: all four focused tests passed in 1.71 seconds. This validates the tested deterministic quadratic cases, including divergence/poor-mixing classification and improved diagonal Hessian conditioning. It does not establish convergence on the Tiny Shakespeare energy landscape; that requires the planned pilot sweep.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Run the complete repository suite and retain production gating at R-hat < 1.2 and mean ESS > 50.
