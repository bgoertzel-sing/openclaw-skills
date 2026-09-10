# Frozen OmegaSim-proxy calibration on Mackey--Glass and Lorenz--96

Frozen on 2026-07-16 before executing or inspecting this calibration. This is
an external calibration of the exact proxy path used by OmegaSim, not a change
to the CLA detector and not a response to OmegaSim outcomes.

## Question and provenance gate

Can the frozen OmegaSim proxy distinguish temporally ordered trajectories from
matched joint time-shuffles for both Mackey--Glass and Lorenz--96 across five
predeclared replicates?

Execution must fail before measurement unless OmegaSim is clean at
`18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`, the detector implementation file
has SHA-256 `29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c`,
and the detached chaoslang tree is clean at
`974af31efaf6e3cc239252f78367d20e657ac45c`. The frozen generator SHA-256 is
`3d9f370c553cfba600461bbec92c705fdb29773fc6bc0376ff3dea37988c9437`.

## Fixed benchmark design

- Detector seeds: `{211,223,227,229,233}`. All traces retain 1,024 eight-
  dimensional samples. The sole stratum is the existing `roles8` path.
- Mackey--Glass: frozen Euler generator, `dt=0.1`, `tau=170` discrete steps
  (17 time units), `beta=0.2`, `gamma=0.1`, `n=10`, 5,000 integration-step
  burn-in, and downsample by 10. Replicate initial histories are constant at
  `0.498,0.499,0.500,0.501,0.502`. Each detector vector is the current sample
  plus seven lags spaced by 17 downsampled samples.
- Lorenz--96: frozen RK4 generator, dimension 8, `F=8`, `dt=0.01`, 5,000-step
  burn-in, and downsample by 5. Replicate `i` starts at the all-8 vector with
  coordinate `i` increased by `0.008 + 0.001*i`, for `i=0..4`.
- Each matched control is a deterministic joint permutation of the 1,024
  eight-dimensional rows using `random.Random(seed * 1000 + 17)`. This keeps
  every vector and all coordinate marginals exact while destroying temporal
  order. It is not a coordinate-wise shuffle.
- Both original and matched control use the unchanged `evaluate_trace` call:
  train-fitted deterministic `k=8` centers on the first 60%, suffix-trie
  miner, JS categories, two greedy iterations, exact reconstruction, five
  marginal-preserving symbol surrogates, and held-out order-2 loss with
  `alpha=0.5`.

## Frozen success rule

A replicate is a win only if the ordered trajectory is detector-positive and
strictly exceeds its matched joint time-shuffle in compression-margin proxy
while also having strictly lower held-out loss. Each system passes only with
at least four wins among its five complete replicates. The calibration passes
only if both systems pass. Missing or nonfinite output fails closed.

This test validates sensitivity to temporal order under the same proxy; it
does not independently validate either numerical integrator, prove chaos,
identify an attractor, or establish semantic grammar. Any failure remains a
failed calibration gate. Thresholds and detector code will not be changed in
response to this result; detector work remains owned by separately
preregistered CLA work.

## Research-rule application

Rules 1, 2, 5, 6, and 7 apply. The estimand is explicitly tested against an
exact matched temporal null; the adapters and gate are specified before the
run; the ledger captures code, commands, seeds, hashes, raw metrics, and
limitations; the conceptual test is whether temporal dependency survives
symbolization and grammar induction rather than whether geometry alone looks
complex; and generator, adapter, detector, control, and scoring remain
separate replaceable seams.
