# Conditional transition-entropy Stage-A calibration v1

- Status: failed pre-outcome execution; exit 1; no score produced.
- Freeze time: 2026-07-20T08:15:00-07:00 / 2026-07-20T15:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/vector-recurrence-attractor-v1` at
  `26b52b547c1da659b9cd53071168b662bf5d29ea` (clean).
- Protocol: `docs/conditional-transition-entropy-calibration-preregistration-v1.md`.
- Compute: bounded local CPU only; no paid/remote compute or remote mutation.

The frozen causal representation is scalar sample-to-sample direction for
Mackey--Glass and the complete eight-coordinate direction tuple for Lorenz--96.
It uses fresh initial 2.1 / 8.09 perturbation fixtures, tau 17/F 8 positives,
tau 2/F 1 stable controls, and deterministic shuffled-symbol controls. The
exclusive promotion interval is `(0.02, 0.90)`. Both positives and no control
must be promoted; Stage B remains prohibited.

Pre-outcome checks passed: focused pytest 5 tests / 5 subtests; full pytest 273
tests / 80 subtests; stdlib discovery 195 tests; `compileall`; and
`git diff --check`.

- Protocol SHA-256: `4f3c8aec137411019c1b4a0e180741a336a854d4b4eccf86a34d45fbb0ed4359`.
- Benchmark SHA-256: `597368bac3b460d2a2a02ce5900cc9a0fd1eba7a8851b250b0d4e9548989f5a4`.
- Declaration-test SHA-256: `b374a12309eebc0e8dd4a5313fb9108aa5b6c379d264438793a926030a5da0b9`.
- Frozen command SHA-256: `25c1a3c52db54ba8dbe92144c491392564e757d08aa12b36cc4e7f3fccf2f45f`.
- Serialized initial-state SHA-256: Mackey--Glass `ad78cfa0ead35ff9d0d6de11ae996a470b257a7342d2a53073df0ce8cda04c4d`;
  Lorenz--96 `2584f06356fcc4b6e18701f8ade5df492ba98fd0c6e00a73a6112ed3fa75f85c`.
- Seeds: dynamics none; shuffle seeds 731921 and 731922.
- Decisive command: exactly `bash command.sh` from this ledger directory.

At freeze time no detector score had been produced or inspected. This can
establish only bounded finite-protocol discrimination, not proof of chaos,
attractor/source-law identification, CLA/compression validation, or semantic
grammar. Failure may not be tuned or rescored on these fixtures.

## Failed execution

The exact command exited 1 before serializing any result because the benchmark
requested nonexistent result attribute `normalized_bits`; the validated API
field is `normalized_entropy`. `results.json` is empty and no fixture score was
produced or inspected. This exposed a missing end-to-end declaration test. The
implementation must be corrected, tested through `run()`, committed cleanly,
and separately refrozen before measurement.

- Empty `results.json`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- `stderr.txt`: `c32dfc5046b8f2f5a617ab03d3beb592b967e026f187a8d2afb3696be33a829b`.
- `timing.txt`: `61760e7fc7f7ef7d84ced0f7ac1313b3da96ccb3d72aa4b52727189ea4840cbc`.
- `exit-status.txt`: `4355a46b19d348dc2f57c046f8ef63d4538ebb936000f3c9ee954a27460dd865`.
