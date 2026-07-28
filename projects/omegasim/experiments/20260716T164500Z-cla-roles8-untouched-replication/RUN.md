# Run 20260716T164500Z-cla-roles8-untouched-replication

- Project: `omegasim`
- Started: `2026-07-16T16:49:44Z`
- Finished: `2026-07-16T16:56:34Z`
- Status: `succeeded; confirmatory proxy criterion met`
- Local or remote: `local CPU`
- Preregistration: `repos/omegasim/docs/cla_roles8_untouched_replication_preregistration_20260716.md`

## Question

Does the predeclared `coupling=0.60`, `delay=3`, `roles8` cell reproduce under
the exact frozen detector on untouched seeds `101,103,107,109,113` with exact
matched linear and shuffled controls?

## Pinned implementation

- OmegaSim preregistration HEAD: `18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d`
- OmegaSim detector implementation parent: `5a6002bd134ffb60e4f20b6c506a1ff6795e7afa`
- chaoslang: `974af31efaf6e3cc239252f78367d20e657ac45c`
- Exact command: `command.sh`

## Result

The confirmatory `roles8` row met its frozen criterion with four of five
untouched-seed wins. All five appraisal rows were detector-positive. Seed 107
missed the matched win because its compression margin (`124.0`) was below the
linear control (`128.6`), despite lower held-out loss. The operational
byproducts were `core4=3/5` and `full20=5/5`; they were not confirmatory and do
not alter the roles8 result.

| seed | matched win | appraisal margin | linear margin | appraisal loss | linear loss |
|---:|:---:|---:|---:|---:|---:|
| 101 | yes | 123.0 | 109.4 | 0.7121 | 0.8700 |
| 103 | yes | 127.4 | 52.6 | 0.6792 | 2.4552 |
| 107 | no | 124.0 | 128.6 | 0.6347 | 0.8841 |
| 109 | yes | 156.0 | 66.6 | 0.7541 | 1.6190 |
| 113 | yes | 137.2 | 102.0 | 0.6969 | 0.8752 |

## Checks and provenance

- An initial launch at `16:49:15Z` failed before measurement because the
  checksum preflight used the wrong working directory. `command.sh` was
  corrected to change to the pinned OmegaSim tree before checking hashes; no
  detector, threshold, seed, control, or analysis behavior changed.
- Focused unit tests: 8 passed; `py_compile` and pre-run `git diff --check`
  passed.
- Measured command exit: 0; elapsed: 410 seconds; 45 rows.
- JSON SHA-256:
  `020d9adc7d7bbf1ef423e3e82b398eb86f227b5476b161aa880db9c66b615ccc`
- CSV SHA-256:
  `6b7ad6c2edc6e3828be1781e6eb2ff0804b3e13eb492c798e13c40ff39bfe45b`
- Final command SHA-256:
  `5a7067119ac74178a6ad9e9c6673abf5b5dbd2291d9c2be617d8d7330262dcd7`

## Interpretation

This is a successful untouched-seed replication of an appraisal-versus-matched
control difference under the frozen CLA proxy. It is not evidence of chaos,
strange-attractor geometry, or semantic grammar. Mackey--Glass and Lorenz--96
calibration remain prerequisites for stronger structure claims.
