# Run 20260724T200302Z-e3-nonceiling-calibration-seed-12011-v2: e3-nonceiling-calibration-seed-12011-v2

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T20:03:02Z`
- Finished: `2026-07-24T20:03:12Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does one frozen E3 calibration seed expose non-ceiling V1--V3 quality differences while preserving exact cost metering?

## Hypothesis or expected behavior

The 75-update student should retain measurable CS headroom; supplied fibres remain imposed structure and are compared against DGC-20 without changing the frozen confirmation bar.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed is encoded in the run ID and command; ID is even factor parity and CS is held-out odd parity.
- Configs: `e3_partial_student_v1.json` and frozen `e3_acceptance_v1_1_frozen.json`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

The run completed all arms, intervention metrics, proximal trajectory diagnostics, and exact discovery/update/transport meters. It contributes to an informative three-seed calibration; aggregate interpretation is in `../20260724T201046Z-e3-nonceiling-disposition-v1/RUN.md`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Use only the disjoint frozen confirmation seeds; do not tune thresholds from this result.
