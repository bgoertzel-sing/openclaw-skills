# Run 20260725T095107Z-cmcp-phase7-8-full-suite-venv: cmcp-phase7-8-full-suite-venv

- Project: `relaleap`
- Started: `2026-07-25T09:51:07Z`
- Finished: `2026-07-25T09:51:55Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the Phase 7 credit-highway implementation and Phase 8 sealed-confirmation
harness pass their 24 focused tests without regressing the existing 388-test
RelaLeap E1 suite?

## Hypothesis or expected behavior

The complete suite should report 412 passed tests (388 existing plus 24 new)
with no failures. The repository's established virtual environment is required
because the system interpreter does not contain the sibling `causal_fibres`
package.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: deterministic unit-test fixtures; no external
  data.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Direct observation: `412 passed, 1 skipped in 46.85s`.
- Result commit: `cad8d9a11b70148de82e2c9c21f1990239eeaa46`
- `stdout.log` SHA-256:
  `202df37a99341ac700e90a9f02b41ec7731ed3e15f081b553bd98be13c7682a2`
- `command.sh` SHA-256:
  `8b4b3618452a64d8e2083aa7d1f998e5d6036382dc7719fcb9503abba0f43c4e`

## Interpretation

The expected 412 tests passed and one pre-existing test was skipped. This is
local implementation/regression evidence, not a scientific claim that typed
routing improves a real model. A preceding system-interpreter attempt is
recorded separately at
`20260725T095037Z-cmcp-phase7-8-full-suite`; it failed collection because that
interpreter lacked `causal_fibres`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Inspect the staged diff, scan for accidental artifacts or secrets, and commit
only the two implementation modules and their two test modules.
