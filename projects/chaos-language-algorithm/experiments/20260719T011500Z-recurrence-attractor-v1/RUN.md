# Recurrence-lag attractor calibration v1

- Status: completed; exit 0; all integrity gates passed; frozen detector rule failed.
- Freeze time: 2026-07-18T18:15:00-07:00 / 2026-07-19T01:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/causal-recurrence-symbolization-v1` at
  `9cd3cf0` (clean).
- Protocol: `docs/recurrence-attractor-preregistration-v1.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute or remote mutation.

The frozen gate uses fresh Mackey--Glass initial 1.3 and Lorenz--96 x7 scalar
observations, prefix-only nearest-rank 10th-percentile adjacent-increment
radius, causal nearest-return lag classes through lag 64, a 1,024-symbol
prefix, untouched 4,096-symbol suffix, and matched shuffled nulls. Complete
compact/JSON CLA, literal, unigram, Markov-1/2, and canonical LZ78 accounting
are retained. Both positives must beat every external control, neither null
may be promoted, compact CLA must beat JSON CLA throughout, and all integrity
gates must pass. Ties fail.

Pre-run checks: focused 10 tests / 13 subtests passed; full 237 tests / 23
subtests passed; `py_compile` and `git diff --check` passed. Exact trajectory,
symbol-stream, prefix, and suffix hashes are frozen in `manifest.json`.
Decisive command: exactly `bash command.sh` from this directory.

- Protocol SHA-256: `736fa08ba2ce160344df7648250b9c175abef41400fc1323bcc080df634fb8ae`.
- Benchmark SHA-256: `e63ac3eed36167cb19de36967a560b78108e5cc97d5ae03b123c2fd2d8e98a51`.
- Declaration-test SHA-256: `4720de20aab769729647226942a0408e70ce99cfef6fb552ad698323d7e27dc0`.
- Frozen manifest SHA-256: `bef5148b715fc3795479af599161a9a7fbbe047911c8e0994013930c4cd1165f`.
- Frozen command SHA-256: `69ad982731b92c10de2de800869850f4f9763474ef30ae0edc76dda18a66b2e7`.
- Environment: Python 3.10.12; Linux x86_64 kernel
  7.0.11-76070011-generic.

No benchmark outcome was produced or inspected before this freeze.

This is recurrence-projection coding calibration only, not chaos, attractor,
source-law, or semantic-grammar evidence. No inspected trajectory, coordinate,
radius rule, lag bin, suffix, split, learner, or codec may be tuned.

## Results

The exact `bash command.sh` run exited 0 with empty stderr in 83.87 seconds
wall time and 27,636 KiB maximum RSS. Every persistence, deterministic-refit,
replay, exact-reconstruction, compact/JSON byte-stability, and LZ78 integrity
gate passed on all four fixtures. Compact CLA beat JSON CLA throughout and
neither shuffled null was promoted.

| fixture | compact CLA bits | strongest external control | strongest bits | CLA below strongest |
|---|---:|---|---:|---|
| Mackey--Glass positive | 9,954.129 | LZ78 | 5,008.000 | no |
| Mackey--Glass shuffled | 12,000.834 | unigram | 5,618.036 | no |
| Lorenz--96 x7 positive | 13,697.457 | unigram | 7,814.621 | no |
| Lorenz--96 x7 shuffled | 14,822.745 | unigram | 7,937.155 | no |

Both required positives lost, so the strict all-positive rule **failed**.
The recurrence relation does not make the frozen CLA coder competitive on
these fresh scalar streams under this complete-code protocol. This is a
coding null, not evidence against chaotic dynamics and not attractor or
semantic-grammar evidence. The Mackey--Glass and Lorenz--96 calibration nulls
remain explicit and binding; no tuning or rescoring is authorized.

Post-run focused checks passed 10 tests / 13 subtests; the full suite passed
237 tests / 23 subtests; `py_compile` and `git diff --check` passed. The code
worktree remained clean at `9cd3cf0`. Artifact SHA-256 values:

- `results.json`: `2226f4a300f6c21bc1c70be8e0ea8564f663f0a59892c80ab6673cd267bbe934`.
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- `timing.txt`: `43f6d212053007f7662f8e4aa7e4477a86c7cc5c533e19b1b9b343f709bb89a7`.
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.

## Next gate

Do not tune this radius rule, lag partition, coordinate, trajectory, or
suffix. Another measured detector gate requires a genuinely new,
outcome-independent hypothesis and untouched data; proxy compression cannot
replace complete-code accounting.
