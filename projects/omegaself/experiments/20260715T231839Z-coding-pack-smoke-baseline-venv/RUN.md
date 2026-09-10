# Run 20260715T231839Z-coding-pack-smoke-baseline-venv: coding-pack-smoke-baseline-venv

- Project: `omegaself`
- Started: `2026-07-15T23:18:39Z`
- Finished: `2026-07-15T23:18:41Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `projects/omegaself/repos/omegaself-coding-agent-pack`

## Question

Does the unchanged coding pack satisfy its reference smoke tests under the ProtoMegaBot2 isolated Python environment?

## Hypothesis or expected behavior

All 44 reference tests, demonstrations, ledger verification, and pack validation should pass without changing the package.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: record here when relevant.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Observed: exit status 0; 44/44 unit tests passed twice (direct smoke stage and pack validation). The demo ledger contained four records with root `d174bc3b3c998a02a60a894722bc8911896bbe483013a4fecb0e417a9290355b`. Dependence grouping reduced four raw outcomes to two independent units; staleness preserved the ledger; two context paths admitted one evidence identity; reasoner adapters produced compatible normalized output; high-impact cache miss returned `RequireReview`; pack validation passed. The root is demo-run-specific because event IDs are generated, not a stable deployment root.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Validate all 21 schemas with the Draft 2020-12 validator and establish the provider-free canary baseline.
