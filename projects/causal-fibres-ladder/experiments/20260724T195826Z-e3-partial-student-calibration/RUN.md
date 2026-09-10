# Run 20260724T195826Z-e3-partial-student-calibration: e3-partial-student-calibration

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T19:58:26Z`
- Finished: `2026-07-24T19:58:47Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Which preregistered early-stop update count yields a partially trained E1
student with 70--90% mean held-out task accuracy before any E3 arm is run?

## Hypothesis or expected behavior

At least one of 50, 75, 100, 150, or 200 homotopy updates will retain
meaningful task-loss headroom. Select the smallest candidate whose mean across
three seeds and ID/CS splits is in the closed interval `[0.70, 0.90]`.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds: `12011, 13121, 14251`.
- Candidate updates: `50, 75, 100, 150, 200`.
- Contract: `configs/e3_partial_student_calibration_v1.json` at repository
  commit `58965e1`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Result SHA256:
  `2e1ff07c5e0d22c298d58bbaf6cf01b82d56172f301d6879a0df1cb1e39be852`.
- Candidate mean task accuracies: 50=`0.65625`, 75=`0.87890625`,
  100=`0.98697917`, 150=`1.0`, 200=`1.0`.
- Selected update count: `75`.
- Three seed-specific deterministic checkpoints and hashes are in
  `artifacts/`.

## Interpretation

The preregistered rule selects 75 updates. The aggregate target is met, with
six seed/split observations ranging from `0.71875` to `1.0`; two seeds retain
clear headroom and one seed is saturated on both splits. This is materially
less ceiling-limited than the prior factor-probe read but not uniformly
non-ceiling, so calibration must report seed-level results and may still fail
the informativeness gate. No E3 arm outcome influenced this selection.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Freeze `updates=75` in a dedicated config, verify checkpoint replay, and run
the existing E3 arms on the three calibration seeds.
