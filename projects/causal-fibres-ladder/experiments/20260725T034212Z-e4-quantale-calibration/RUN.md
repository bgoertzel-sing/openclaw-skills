# Run 20260725T034212Z-e4-quantale-calibration: e4-quantale-calibration

- Project: `causal-fibres-ladder`
- Started: `2026-07-25T03:42:12Z`
- Finished: `2026-07-25T03:42:13Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Can a distance-correlation evidence-novelty channel, combined with the
score-space CMCP ratio by a Schweizer--Sklar t-norm, separate exact,
systematically biased, independent, and partially redundant fixtures?

## Hypothesis or expected behavior

Constructed exact and deterministic bit-flip packets should receive zero
weight, independent repeats high weight, and 50%-overlap packets intermediate
weight. The parameter `p` is selected only on the three calibration seeds.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seeds: `51001, 52103, 53209`
- Grid: `p = 0.05 ... 1.5` as recorded in the config
- Raw artifact: `../../artifacts/e4-quantale-p-calibration-v1.json`

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

The selected grid point was `p=0.05`. Mean ratios were:

- exact duplicate: `0.0`
- systematic bit flip: `0.0`
- independent repeat: `0.870930`
- 50%-overlap partial redundancy: `0.363021`

The selection score decreased monotonically over the tested grid, from
`0.833950` at `p=0.05` to `0.553181` at `p=1.5`.

## Interpretation

**Observed:** The combined ratio separates all four constructed fixture
classes in the intended order.

**Boundary:** `p=0.05` is the smallest tested value. An auxiliary product-limit
check (`p=0.001`) gave independent/partial means `0.870967/0.367151`, slightly
better under the stated target-0.4 objective. Thus the calibration supports
the distance-correlation novelty channel, but does not identify a non-product
Schweizer--Sklar geometry. The partial-redundancy target `0.4` is a constructed
design choice, not independently estimated truth.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Use an unbiased or permutation-calibrated dependence estimator and include
the product limit explicitly in any next calibration. Freeze confirmation
criteria before opening new seeds.
