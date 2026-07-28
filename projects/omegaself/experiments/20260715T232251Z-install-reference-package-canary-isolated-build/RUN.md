# Run 20260715T232251Z-install-reference-package-canary-isolated-build: install-reference-package-canary-isolated-build

- Project: `omegaself`
- Started: `2026-07-15T23:22:51Z`
- Finished: `2026-07-15T23:22:53Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `projects/omegaself/repos/omegaself-coding-agent-pack/python`

## Question

Can pip build and install OmegaSelf 1.0.0 into the canary venv using the package-declared isolated build requirements?

## Hypothesis or expected behavior

An isolated setuptools build should produce a dependency-free wheel and install it only in the canary venv.

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

Observed: exit status 0. Pip built `omegaself_reference-1.0.0-py3-none-any.whl` (SHA-256 `016d8b9c082aa27b9a417cc7aae4b514e4187f44813a61c51a5a7cd090e3c709`) and installed it in the ProtoMegaBot2 venv. A subsequent `pip show` confirms version 1.0.0 and no runtime dependencies.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Import the package only through a fail-isolated, default-off OmegaClaw bridge.
