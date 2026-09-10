# Run 20260726T184453Z-p0-selftest-v1: p0-selftest-v1

- Project: `hdc-cgcct-transformers`
- Started: `2026-07-26T18:44:53Z`
- Finished: `2026-07-26T21:29:00Z` (checkpointed)
- Status: `partial-complete`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes`

## Question

Do the deterministic P0 HDC algebra/property tests pass before capacity-gate interpretation?

## Hypothesis or expected behavior

All exact wiring/property tests pass.

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

Observed: 13 exact tests passed in 1.03 seconds. This establishes only the P0
unit/property-test portion; this v1 command did not include the second independent
replay plus P0-G1 validator required for the capacity gate.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Use the v2 run for the complete replay contract.
