# Run 20260725T015158Z-e4-cmcp-persistent-smoke: e4-cmcp-persistent-smoke

- Project: `causal-fibres-ladder`
- Started: `2026-07-25T01:51:58Z`
- Finished: `2026-07-25T01:51:59Z`
- Status: `failed`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the newly implemented eight-episode persistent CMCP runner execute with
the frozen calibration configuration and emit the required artifact?

## Hypothesis or expected behavior

The runner should train the 75-update student, execute all four ledger arms
without changing model weights, and write an eight-episode JSON result.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seed: `61001`.
- Configuration: `configs/e4_cmcp_persistent_calibration_v1.json`.

## Results

- Exit status: 1
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

The launch failed before model construction because the experiment wrapper did
not set `PYTHONPATH=src`; Python could not import `relaleap`. This is an
operational command failure, not evidence about the implementation or
hypothesis. The failure is retained and superseded by the v2 smoke record.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Relaunch with `/usr/bin/env PYTHONPATH=src` in the recorded command.
