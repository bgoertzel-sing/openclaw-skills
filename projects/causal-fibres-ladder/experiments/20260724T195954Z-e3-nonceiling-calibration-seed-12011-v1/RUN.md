# Run 20260724T195954Z-e3-nonceiling-calibration-seed-12011-v1: e3-nonceiling-calibration-seed-12011-v1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T19:59:54Z`
- Finished: `2026-07-24T20:00:03Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the initial 75-update E3 calibration invocation expose non-ceiling quality differences?

## Hypothesis or expected behavior

At least two calibration seeds should retain measurable headroom; these runs precede the completed quality/proximal reporting patch and are retained as superseded evidence.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed is encoded in the run ID and command; ID is even parity and CS is held-out odd parity.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

The arm outputs were informative, but the reporting schema lacked final task-loss, intervention, peak-RSS, and proximal fields. The same deterministic seeds were rerun as v2 at commit `1d2cb6b`; use v2 for scientific interpretation.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Superseded by the corresponding v2 calibration run; retain for provenance.
