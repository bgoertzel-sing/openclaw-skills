# Reduced v1.1 E3--E5 disposition

- Date: `2026-07-24`
- Compute: local CPU only
- E2 branch entering E3: E2-B; supplied fibres are imposed structure

## E3: calibration ceiling, no confirmation claim

The E3 update contract and implementation now cover dense, top-k at
1%/5%/20%, exact DGC error feedback at the same fractions, supplied
four-factor fibres, random-k, and raw-BP/C3. Metering separates source-gradient
work, frontier discovery, selected updates, residual writes, fibre projection,
and transport.

Sparse conditions were matched to dense's activity-update count by using
proportionally more settle steps. This exposes the cost hidden by update-only
accounting: at 20%, top-k/DGC inspect `138,240` source scalars and top-k also
performs `138,240` discovery reads to deliver about `27,680` selected updates,
versus dense's `27,648` source/selected updates. The supplied-fibre arm delivers
`27,648` coefficients but incurs `1,327,104` projection multiply-adds and
`165,888` transported scalars.

The three frozen calibration seeds are scientifically non-discriminating.
The no-update frozen factor interface is already `1.000` exact on ID and
`0.9974` exact on held-out factor combinations. Dense and DGC-20% remain
`0.9974`; top-k-20% and raw BP reach `1.000`; supplied fibres and random-k-20%
are `0.9948`. These one-example differences at ceiling cannot test whether
structure improves transfer. The five confirmation seeds and V4 continual
claim were not launched. E3 is **inconclusive on quality, informative on
cost**; no supplied-fibre advantage is claimed.

## E4: negative reduced calibration

E4 uses the original 16-class task, where FF has real headroom. Conditions are
FF, diagnostic-only TC, OT using observed factors 0--1, SC using symbolic
constraints for factors 2--3, and OT+SC. Weights remain frozen.

Across three calibration seeds on CS, mean task accuracy is:

- FF `0.1484`
- TC diagnostic anchor `0.1797`
- OT, SC, and OT+SC each `0.1536`

SC's loss-headroom recovery values are `0.0743`, `0.0618`, and `0.0980`,
well below the frozen material bar `G > 0.2`; no condition shows a consistent
task-accuracy recovery. Confirmation was therefore not launched. The reduced
rig provides no material symbolic-constraint benefit.

## E5: W1/W2 kernel parity, store integration still blocked

Pinned MORK commit `5464713539c1c1cb491397f4c7bb1d9cdc8b74a0` contains a
standalone `linalg` crate with dense tensors, einsum, CSR, blocked kernels, and
JIT support. Its 34 library tests pass under nightly Rust 1.99.0.

On local branch `agent/e5-epc-kernel-probe`, commit `7673b02` adds a
six-layer f32 parity probe:

- W1 forward matches the independent Python reference within the required
  `1e-5` maximum relative logit error and preserves exact argmax.
- W2 five-step predictive relaxation matches the Python settled terminal state
  within `1e-6` maximum absolute error.

This is numerical-kernel evidence, not an in-store MORK implementation. The
kernel sink registry exposes scalar pure operations and path-space sinks but
does not expose typed tensor resources, matmul/neural-layer sinks, or an
in-store iterative tensor-state seam. W1 rule hosting and W2 in-store
iteration therefore require a new reviewed tensor-resource/sink adapter.
W3--W5 remain downstream and unimplemented. From-scratch in-store training
remains out of scope.

## Evidence

- E3 calibration:
  `experiments/20260724T191338Z-e3-calibration-seed-12011-v1-1-rerun/`,
  `20260724T191419Z-e3-calibration-seed-13121-v1-1/`,
  `20260724T191437Z-e3-calibration-seed-14251-v1-1/`
- E4 calibration:
  `experiments/20260724T191739Z-e4-calibration-seed-12011-v1-1/`,
  `20260724T191808Z-e4-calibration-seed-13121-v1-1/`,
  `20260724T191823Z-e4-calibration-seed-14251-v1-1/`
- E5:
  `experiments/20260724T191959Z-e5-mork-linalg-api-smoke/`,
  `experiments/20260724T192200Z-e5-w1-w2-linalg-parity/`
