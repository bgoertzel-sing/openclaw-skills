# Correlation-form 0--1 Stage-A calibration v1

- Status: completed; exit 0; frozen rule failed.
- Freeze time: 2026-07-19T20:15:00-07:00 / 2026-07-20T03:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/vector-recurrence-attractor-v1` at
  `76d5deb02a717205bd133f2eb8bd4cb0ff87ce3d` (clean).
- Protocol: `docs/zero-one-calibration-preregistration-v1.md`.
- Compute: bounded local CPU only; no paid/remote compute or remote mutation.

This frozen Stage-A gate applies sixteen fixed frequencies, maximum lag 100,
and strict threshold 0.5 to fresh 1,024-sample Mackey--Glass and full-state 8D
Lorenz--96 positive/stable pairs. Lorenz--96 scores every coordinate and uses
their median; no coordinate is selected. Both positives and no stable controls
must be promoted; ties fail. Stage B remains separate and prohibited.

Pre-outcome focused checks passed 7 tests / 18 subtests; full pytest passed 264
tests / 67 subtests; `compileall` and `git diff --check` passed.

- Protocol SHA-256: `32fee6a25bdac0253f8f1cbb0d3382360ccda10d6ed71fa950a64a85f4caf78a`.
- Benchmark SHA-256: `292caa07cfce32a20d3efaeb32febf8c01b6894f801a6232cc5d56a550a5c09e`.
- Declaration-test SHA-256: `6ab0ba251be25fa8285f9c056ca24eb4e90ea38bdf4edc80b321c49451558292`.
- Frozen command SHA-256: `d60a944e8e711d7ab8e598ada69d43580c26d9ed96a011816c6af5211ec25740`.
- Environment: Python 3.10.12; Linux x86_64 kernel 7.0.11-76070011-generic.
- Fixture SHA-256: Mackey--Glass positive `deca7ae8df6b227b2be750d6df77e68f7cec171d627184e1dfe292ad1e377521`; Mackey--Glass stable `1df8a73a6c837b03b387318121e259f00a6021298bf0c139718709465dcf4e2a`; Lorenz--96 positive `76f76752375f90b86b0103cc1dfdcff30f4dd9839d197e363b87284435610d46`; Lorenz--96 stable `1fac6a03e68ad6f525d1e014bf707011c479f5ce30e0d49dd60ab63195a68491`.
- Decisive command: exactly `bash command.sh` from this ledger directory.

No detector result was produced or inspected before this freeze. A pass is
bounded discrimination evidence only, not proof of chaos, attractor/source-law
identification, CLA validation, compression evidence, or semantic grammar.
Failure may not be tuned or rescored on these fixtures.

## Results

The exact command exited 0 with empty stderr in 6.33 seconds and 18,136 KiB
maximum RSS. Neither positive was promoted: Mackey--Glass scored
`-0.3768055509`, and the median across all eight Lorenz--96 coordinates was
`-0.0942887601`. Both stable controls were correctly rejected
(`-0.4702743650` and `-0.3512117932`). Thus there were two false negatives and
no false positives; the strict gate failed and Stage B remains prohibited.

The command hash was computed in the same shell invocation immediately before
the decisive command and printed before the child completed; all code,
fixtures, configuration, commit, and exact command text were already frozen.
No outcome was available or inspected before execution. This timing detail is
recorded explicitly as an orchestration-ledger deviation.

Post-run focused checks passed 7 tests / 18 subtests; full pytest passed 264
tests / 67 subtests; stdlib discovery passed 186 tests; `compileall` and
`git diff --check` passed. The code worktree remained clean at `76d5deb`.
No frequency, lag, threshold, observable, initial condition, or regime may be
tuned or rescored on these fixtures.

- `results.json`: `493ab01ded5a83595afbbf7694f9ddc1f23b021399a2a71e6444dbbc29164ebc`.
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- `timing.txt`: `053c0f70d1cd79e51589cdfaab52672495c118d305be6d41fdf0ff7fd4971ba6`.
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.
