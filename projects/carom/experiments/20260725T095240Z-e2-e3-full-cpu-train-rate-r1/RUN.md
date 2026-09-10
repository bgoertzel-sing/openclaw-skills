# Run 20260725T095240Z-e2-e3-full-cpu-train-rate-r1: e2-e3-full-cpu-train-rate-r1

- Project: `carom`
- Started: `2026-07-25T09:52:40Z`
- Finished: `2026-07-25T09:56:07Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/carom/repos/carom`

## Question

What is the local CPU training rate at the exact frozen E2/E3 model and batch
shape when full-corpus evaluation is removed from the timing?

## Hypothesis or expected behavior

Ten updates for each of the five arms (50 arm-updates total), with a one-example
evaluation corpus, will give a conservative local training-rate estimate.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed: `7`; evaluation seed `20260720`.
- Frozen training shape: batch 128, `d=64`, `K=16`, 70 controller steps.
- Deliberately reduced evaluation size: 1 example.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

### Direct observations

- All five arms completed 10 updates and repeated evaluation exactly.
- Wall time was 3:26.47 for 50 arm-updates; peak RSS was 7,796,664 KB.
- This is `4.1294` wall seconds per arm-update on the current host, including
  negligible one-example repeated evaluations.
- The frozen confirmation requires 25 arms/seeds x 3,000 updates = 75,000
  arm-updates.
- SHA-256: `stdout.log`
  `821b84697d0511d5ce92cd85e45f424ae0723312713c5b4b3d584dc3fe5da60a`;
  `stderr.log`
  `ef56995855ca6dab705fc3d9772785d47acd0ba34544ce6ba353e4da878ab558`.
- Preserved artifacts: `artifacts/train-slice/`; SHA-256: `summary.json`
  `8843356f9b1261985fbf7fcf28d5df6570b08bf077db65cb8c2fbff9621337f5`;
  `paired_eval_corpus.pt`
  `398624f81b7c2922b643ec0e3b5efc4b6e2c31061220f3382527af4155bdfcb7`.

### Interpretation

Linear projection is about 86.0 wall hours for training alone, before the
full-corpus evaluations. Host load and memory pressure make the exact duration
uncertain, but not the conclusion: the accepted full run is not a practical
local-CPU session. This calibration is not a scientific E2/E3 result.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Keep E4 closed. The existing GPU runner may be used only in a separately
authorized paid-compute action, after numerical paired accuracy, trajectory,
and exposure thresholds are frozen. No remote resource was provisioned or used
for this audit.
