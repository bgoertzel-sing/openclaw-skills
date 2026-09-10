# Run 20260724T200852Z-e4-nonceiling-calibration-seed-13121-v1: e4-nonceiling-calibration-seed-13121-v1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T20:08:52Z`
- Finished: `2026-07-24T20:08:56Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does one non-ceiling E4 calibration seed show material SC recovery of diagnostic TC headroom over FF?

## Hypothesis or expected behavior

SC is material only if CS headroom recovery G exceeds the frozen 0.2 bar; TC remains diagnostic only.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed is encoded in the run ID and command.
- Conditions: FF, diagnostic TC, OT, SC, and OT+SC on frozen ID and CS splits.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

The run completed without changing model weights. Across three calibration seeds, CS SC task-loss G was 0.1678, 0.1924, and 0.2347 (mean 0.1983); the frozen material bar fails and confirmation was not launched. See `../20260724T201046Z-e3-nonceiling-disposition-v1/RUN.md`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Retain as negative calibration evidence; do not tune the 0.2 bar.
