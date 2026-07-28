# Run 20260724T201046Z-e3-nonceiling-disposition-v1: e3-nonceiling-disposition-v1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T20:10:46Z`
- Finished: `2026-07-24T20:10:47Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

On a preregistered 75-update partially trained student, do supplied fibres
beat matched-budget DGC on E3 V1--V3, does V4 support Prediction 1, and does
the E4 SC condition recover more than 20% of diagnostic TC headroom?

## Hypothesis or expected behavior

The non-ceiling substrate should make quality differences measurable.
Supplied fibres pass only if they beat DGC on confirmation mean and at least
four of five paired seeds. Dense ungated settlement should not outperform
matched-compute BP beyond noise unless the difference tracks the proximal
ablation. E4 is material only if CS `G > 0.2`.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- E3 calibration seeds: `12011,13121,14251`.
- E3 confirmation/V4 seeds: `15313,16417,17519,18637,19739`.
- E4 calibration seeds: `12011,13121,14251`.
- Repository commit: `b1191f4`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Result SHA256:
  `f8d4df8976460a28666958fddc9f851a51f8f7e974899c13426dd9bbbe1a743d`.
- V1 ID task accuracy means: dense `0.9219`, DGC-20 `0.9203`,
  supplied fibre `0.9188`, BP `0.9109`.
- V2 CS task accuracy means: dense `0.9438`, DGC-20 `0.9422`,
  supplied fibre `0.9531`, BP `0.8500`.
- Supplied fibre versus DGC-20: task-accuracy mean advantage `+0.01094`
  but only 3/5 strict wins; task-loss mean advantage `-0.00660` with 1/5
  wins; factor-BCE mean advantage `-0.00168` with 0/5 wins.
- V3 routing was frozen on ID and reused on CS in all eight E3 runs.
- V4 selected-scalar ratio dense/BP: `1.00599`. Mean factor-BCE drift was
  dense `-0.00226` versus BP `+0.10792`; advantage/proximal-divergence
  Pearson correlation was `-0.1886`.
- E4 CS SC task-loss G: `0.1678, 0.1924, 0.2347`; mean `0.19828`.

## Interpretation

E3 is quality-informative but the supplied-fibre confirmation bar fails on
every reported CS metric. Its small mean task-accuracy edge is not supported
by four paired wins and reverses on task loss and factor BCE. Imposed fibre
structure therefore shows no confirmed reduced-rig transfer advantage over
DGC at the metered budget.

V4 does not cleanly support Prediction 1. Dense settlement shows substantially
less off-support drift than BP on three seeds despite matched selected-scalar
work, and that difference does not positively co-vary with the measured
proximal trajectory divergence. This may reflect unequal effective
optimization despite scalar matching; it is a reduced-rig falsifier/ambiguity,
not evidence for fibre gating, because DGC, fibre, and random support all
remain near zero drift.

The non-ceiling E4 substrate raises SC loss-headroom recovery from the prior
6.2--9.8% range to a mean of 19.83%, but only one seed exceeds the frozen 20%
bar and the mean remains below it. E4 confirmation was therefore not launched.
C2 dictionary atoms were never promoted; all fibre arms use supplied imposed
structure.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Do not relax either frozen bar. A future Prediction-1 audit should match
effective parameter displacement or learning-rate trajectory, not only scalar
update count, and must be separately preregistered.

Superseded for reproduction by
`../20260724T201712Z-e3-nonceiling-disposition-v2/`, whose command reads the
durable raw experiment artifacts rather than transient scratch copies.
