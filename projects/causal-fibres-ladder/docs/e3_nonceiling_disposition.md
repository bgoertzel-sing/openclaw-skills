# E3 non-ceiling disposition

Date: 2026-07-24

## Substrate

Option 1 retained the residual six-block E1 model and stopped guarded
homotopy after 75 updates. This was the smallest preregistered candidate whose
mean pre-E3 original-task accuracy over three calibration seeds and ID/CS
splits lay in `[0.70,0.90]` (`0.87890625`). Seed/split values ranged from
`0.71875` to `1.0`, so one seed remained saturated.

Fibres were the supplied coordinate-group basis required by E2-B. No JBD
output or C2 dictionary atom was promoted. Frontier discovery, selected
updates, residual writes, projection work, transport, wall time, and process
peak RSS were retained.

## E3 V1--V3

Three calibration seeds (`12011,13121,14251`) showed measurable CS headroom
on two seeds, so five disjoint confirmation seeds
(`15313,16417,17519,18637,19739`) ran.

| CS metric | Mean fibre advantage over DGC-20 | Strict paired wins | Bar |
|---|---:|---:|---|
| original-task accuracy | `+0.01094` | 3/5 | fail |
| original-task loss | `-0.00660` | 1/5 | fail |
| factor BCE | `-0.00168` | 0/5 | fail |
| factor exact accuracy | `-0.00156` | 0/5 | fail |

V1 ID task-accuracy means were dense `0.9219`, DGC-20 `0.9203`, fibre
`0.9188`, and BP `0.9109`. V2 CS means were dense `0.9438`, DGC-20 `0.9422`,
fibre `0.9531`, and BP `0.8500`. V3 routing was frozen on ID and reused on CS.
The fibre task-accuracy edge is not confirmatory because it misses the 4/5
sign bar and reverses on task loss and factor BCE.

Disposition: supplied imposed structure has no confirmed reduced-rig transfer
advantage over DGC at the metered budget.

## V4 and Prediction 1

Five sequential factor-stream seeds compared dense, raw BP, DGC-20,
factor-gated supplied fibre, and random-20 support. Dense and BP selected
scalar updates matched within 0.6% (`dense/BP=1.00599`).

Mean factor-BCE off-support drift was dense `-0.00226`, BP `+0.10792`,
DGC-20 `-0.00100`, fibre `-0.00114`, and random-20 `-0.00128`. Dense beat BP
materially on three seeds, while two seeds were effectively tied. The
dense/BP advantage did not positively co-vary with terminal proximal
trajectory divergence (Pearson `-0.1886`).

Prediction 1 is not cleanly supported on this reduced rig. Selected-scalar
matching does not guarantee matched effective optimization, which remains the
main alternative explanation. This is not evidence for fibre gating because
all three restricted/control arms remain near zero drift.

## E4

The 75-update substrate raised CS SC task-loss headroom recovery to
`0.1678, 0.1924, 0.2347` (mean `0.19828`) from the prior 6.2--9.8% range.
Only one calibration seed exceeded the frozen `0.2` material bar and the mean
remained below it. E4 confirmation was not launched.

## Evidence

- Aggregate: `experiments/20260724T201712Z-e3-nonceiling-disposition-v2/`
- Student selection:
  `experiments/20260724T195826Z-e3-partial-student-calibration/`
- Raw seed records are enumerated by the aggregate run command.
