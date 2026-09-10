# Run 20260724T140913Z-e2-dual-m1-m5-v1-1: e2-dual-m1-m5-v1-1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T14:09:13Z`
- Finished: `2026-07-24T14:09:23Z`
- Status: `failed`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Can the frozen-prediction dual-substrate M1--M5 battery complete and emit a
finite machine-readable record?

## Hypothesis or expected behavior

Estimator computation should complete; non-finite upstream diagnostics must
fail closed rather than silently disappear.

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

All M1--M5 computations completed, but serialization rejected an infinite
signature-gap diagnostic emitted by the JBD library. No scientific artifact
was emitted. This run is retained as an operational failure; the fixed rerun
persists only finite JBD loss/convergence/orthogonality fields.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Run the identical battery with finite-only JBD serialization.
