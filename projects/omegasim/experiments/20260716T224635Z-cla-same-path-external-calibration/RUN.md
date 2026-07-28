# Run 20260716T224635Z: frozen same-path external calibration

- Project: `omegasim`
- Started: `2026-07-16T22:48:35Z`
- Finished: `2026-07-16T22:52:36Z`
- Status: `succeeded; frozen same-path temporal-order gate passed`
- Local or remote: `local CPU`
- Preregistration: `../../docs/cla_same_path_benchmark_preregistration_20260716.md`

## Question

Does the exact frozen OmegaSim proxy distinguish ordered Mackey--Glass and
Lorenz--96 trajectories from matched joint time-shuffles in at least four of
five predeclared replicates for each system?

## Pinned implementation

- OmegaSim: clean `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`
- Frozen detector file SHA-256: `29b8283df90bc55929e2065650c998b00f676d5e4317a743656ead8e01c66e7c`
- chaoslang: clean detached `974af31efaf6e3cc239252f78367d20e657ac45c`
- Frozen generator SHA-256: `3d9f370c553cfba600461bbec92c705fdb29773fc6bc0376ff3dea37988c9437`
- Preregistration SHA-256: `d7356af45b33d9b1542a024c319a81c10324285cd2e94b33374dbb58f604d943`
- Benchmark adapter SHA-256: `ec21e49360f5c21375df9a0717371834a6d0b48210403701809a4a7d5fef01e2`
- Command SHA-256: `bfaac9d3855d3339d8560e79b566e991670738edca2023547b7967b5992a07d0`
- Exact measured command: `command.sh`

Pre-run checks: 14 focused detector/generator tests passed; adapter compile,
both clean-tree gates, and workspace `git diff --check` passed.

## Results

- Exit status: 0; elapsed: 241 seconds; `stderr.log` empty.
- Mackey--Glass: 5/5 matched-control wins; required 4/5.
- Lorenz--96: 5/5 matched-control wins; required 4/5.
- All ten ordered rows were detector-positive and strictly beat their exact
  joint time-shuffles on both higher compression margin and lower held-out
  order-2 loss.
- Results JSON SHA-256:
  `6734426f53b472bfa9ea553627e1447cc03df9ec1a8aaf47cd546f7ce19fb7a1`.
- Results CSV SHA-256:
  `da3dbf8f9b679fa8c710c1318d9b57d5950cf6393f6007e61fce104a18b20a9b`.

| system | seed | ordered margin | shuffled margin | ordered loss | shuffled loss |
|---|---:|---:|---:|---:|---:|
| Mackey--Glass | 211 | 186.6 | -1.8 | 0.6733 | 3.0943 |
| Mackey--Glass | 223 | 191.0 | 0.6 | 0.6769 | 3.1228 |
| Mackey--Glass | 227 | 182.2 | -7.0 | 0.6584 | 3.1533 |
| Mackey--Glass | 229 | 181.6 | 4.8 | 0.6586 | 3.0266 |
| Mackey--Glass | 233 | 190.6 | 6.8 | 0.6852 | 3.1111 |
| Lorenz--96 | 211 | 138.8 | -6.8 | 1.0081 | 3.2359 |
| Lorenz--96 | 223 | 147.8 | 3.0 | 1.0857 | 3.0906 |
| Lorenz--96 | 227 | 137.0 | -3.4 | 1.0858 | 3.2563 |
| Lorenz--96 | 229 | 124.8 | 5.4 | 1.1683 | 3.2104 |
| Lorenz--96 | 233 | 158.6 | 2.6 | 1.1135 | 3.2358 |

## Interpretation

Observed: the exact frozen OmegaSim proxy is sensitive to temporal order in
both predeclared benchmark systems under this train-fitted-k-means,
symbol-shuffle, and matched joint-time-shuffle test. This closes OmegaSim's
same-path benchmark task without changing the detector in response to OmegaSim
outcomes.

Limitation: this is a proxy sensitivity calibration, not independent numerical
integrator validation, proof of chaos, attractor identification, or semantic
grammar. The independent stricter decodable held-out CLA coding benchmark
still fails. Therefore this result supports the bounded OmegaSim proxy
interpretation but does not unlock strong attractor/grammar claims.

## Artifacts and replay

Raw JSON/CSV are under `artifacts/`; environment, repository identities,
stdout, stderr, and status are captured beside this record. Run `bash
command.sh` after reviewing its clean-tree and hash preflight.
