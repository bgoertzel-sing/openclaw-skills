# Run 20260724T140310Z-e2-residual-adjoint-m0-v1-1: e2-residual-adjoint-m0-v1-1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T14:03:10Z`
- Finished: `2026-07-24T14:03:12Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Can plain teacher-free CE adjoints be extracted and persisted without
homotopy, and are they equivalent to `T=128` settled errors on the selected
residual substrate?

## Hypothesis or expected behavior

The fast path should preserve weights and share the settled-field schema. M0
would require aligned per-block direction/support and similar depth profiles.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed `1729`; residual terminal student and the same 128-sample probe.
- Plain `dCE/dx_l` at `epsilon=0`; settled CE at `T=128`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/e2_residual_adjoint_m0_v1_1.{json,npz}` and manifest.
- Focused tests: 17 passed.
- Result SHA-256:
  `46e195ed71b906af43b473667a3773391c221c729a4b01225ad809fa77c73caa`.
- Fields SHA-256:
  `d78d3b27d20b1e10fb99ee085986f4db874456c9b4ac8a885d1e775aefac5385`.

## Interpretation

**Observed:** extraction preserved weights and used `epsilon=0`. The adjoint
top-5% depth profile was `[0.531,0.303,0.111,0.043,0.012,0]`, opposite the
settled profile `[0,0,0,0,0,1]`. Depth-profile cosine and total-variation
agreement were both zero, below the random-field values `0.372` and `0.153`.
Late-block per-cell direction/support aligned strongly, but blocks 1--3 had
negligible settled magnitude.

**Inferred:** the adjoint fast path is operational, but M0 fails globally.
Settled and adjoint fields must be treated as independent E2 substrates.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Freeze Prediction 2 as adjoint blocks 1--2 versus settled block 6, then run
M5/estimator preflight before M3/M4.
