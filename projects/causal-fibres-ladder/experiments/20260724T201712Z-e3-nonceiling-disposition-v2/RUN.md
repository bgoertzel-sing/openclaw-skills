# Run 20260724T201712Z-e3-nonceiling-disposition-v2: e3-nonceiling-disposition-v2

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T20:17:12Z`
- Finished: `2026-07-24T20:17:13Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Do the durable E3/E4 raw artifacts establish a supplied-fibre advantage,
support Prediction 1, or cross the E4 material headroom bar?

## Hypothesis or expected behavior

Supplied fibres require a positive confirmation mean and at least four of
five paired CS wins over DGC. Dense should not beat matched-work BP beyond
noise unless the effect tracks proximal divergence. E4 requires CS `G>0.2`.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Inputs are the durable raw result artifacts from three E3 calibration, five
  E3 confirmation, five V4, and three E4 calibration runs enumerated in
  `command.sh`.
- Repository commit: `b1191f4`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Result SHA256:
  `f8d4df8976460a28666958fddc9f851a51f8f7e974899c13426dd9bbbe1a743d`.
- Reproduction replay after record completion produced the identical SHA256
  and byte-for-byte output.
- Supplied fibre versus DGC-20: task accuracy `+0.01094`, 3/5 wins;
  task loss `-0.00660`, 1/5; factor BCE `-0.00168`, 0/5.
- V4 dense/BP selected-scalar ratio `1.00599`; mean BCE drift dense
  `-0.00226`, BP `+0.10792`; advantage/divergence Pearson `-0.1886`.
- E4 CS SC task-loss G mean `0.19828` (1/3 seeds above `0.2`).

## Interpretation

Supplied fibres fail the frozen CS bar on every reported metric. Prediction 1
is not cleanly supported: dense has less drift than BP on three seeds but the
effect does not positively track proximal divergence, leaving effective-step
matching unresolved. E4 improves substantially over the previous ceiling
run but remains below the frozen material bar, so confirmation is not
launched. Fibres remain supplied imposed structure and C2 atoms are unused.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Do not relax the E3 or E4 bars. Any new V4 audit must preregister effective
displacement/step matching.
