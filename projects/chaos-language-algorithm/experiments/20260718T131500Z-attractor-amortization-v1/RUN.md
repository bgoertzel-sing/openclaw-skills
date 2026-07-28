# Attractor fixed-model amortization gate v1

- Status: completed; exit 0; all integrity gates passed; frozen detector rule failed.
- Freeze time: 2026-07-18T06:15:00-07:00 / 2026-07-18T13:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/attractor-amortization-v1` at
  `cbbebfd655d24a385fb16546aa3c26cdfb78b427` (clean).
- Protocol: `docs/attractor-amortization-preregistration-v1.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute, push, or remote mutation.

## Frozen hypothesis and rule

Test whether the unchanged compact indexed CLA frozen-prefix model amortizes
its one-time transmission on fresh scalar Mackey--Glass and Lorenz--96
calibration streams at predeclared longer horizons, while matched shuffled
nulls are not promoted. The new calibrations use Mackey--Glass initial 0.9 and
Lorenz--96 initial perturbation x4=7.985 with scalar x5 observed.

Fit prefix-only eight-bin M1 symbolization and CLA on 1,024 samples; score
untouched cumulative suffixes of 4,096, 16,384, and 65,536 samples. Pass only
if all integrity gates pass, compact CLA beats every external control at the
final horizon on both positives, beats JSON CLA throughout, and promotes
neither shuffled null. Both positives are required and ties fail.

This is held-out scalar coding calibration only. It cannot validate chaos,
strange-attractor structure, full-state Lorenz--96 grammar, source-law
recovery, or semantic grammar, and it cannot substitute proxy compression for
complete-code accounting.

## Pre-run freeze

- Seed: 18071831; source-specific shuffle seeds: 18071832 and 18071833.
- Exact dynamics, integration, discard, observed coordinate, partition bounds,
  fixture hashes, checkpoints, learner, controls, and decision rule are frozen
  in `manifest.json`.
- Protocol SHA-256:
  `f720dcd74077dea0524b0c0441a2cba560417d1b7641177e8b4e70c34d29c414`.
- Benchmark implementation SHA-256:
  `1969d2283d113d334600c9f51f6089dec4d56995c938f310bb2a406bdaa97de4`.
- Declaration-test SHA-256:
  `694e43cd5d9b9dc4a0f3adeff98cc05810b9fc0c4378ae79bccd460790702a96`.
- Frozen manifest SHA-256:
  `f3982930deb9278e85cb73c3e125e3c41637d4976d79155ce958a82f0674bb16`.
- Frozen command SHA-256:
  `3d4bf2f9330eb6323221a4d244ee0ffdefe3341f77fb73b69d03fc9411468a92`.
- Environment: Python 3.10.12; Linux x86_64 kernel
  7.0.11-76070011-generic.
- Outcome-independent focused checks: 2 passed; full pytest suite: 217
  passed; benchmark/test `py_compile` and `git diff --check` passed.
- Decisive command: exactly `bash command.sh` from this directory.

No benchmark outcome was produced or inspected before this freeze.

## Results

The exact `bash command.sh` run exited 0 with empty stderr in 2:10.60 wall
time and 73,620 KiB maximum RSS. Every integrity gate passed at every
checkpoint on all four fixtures. Neither positive crossed any checkpoint.

| fixture | suffix symbols | compact CLA bits | strongest external bits | CLA below strongest |
|---|---:|---:|---:|---|
| Mackey--Glass positive | 4,096 | 15,822.014 | LZ78 7,872.000 | no |
| Mackey--Glass positive | 16,384 | 27,101.735 | Markov-1 14,802.163 | no |
| Mackey--Glass positive | 65,536 | 72,723.386 | Markov-1 25,006.425 | no |
| Mackey--Glass shuffled | 65,536 | 215,249.196 | unigram 196,886.293 | no |
| Lorenz--96 x5 positive | 4,096 | 17,600.434 | LZ78 10,960.000 | no |
| Lorenz--96 x5 positive | 16,384 | 35,616.912 | Markov-1 19,591.889 | no |
| Lorenz--96 x5 positive | 65,536 | 103,647.803 | Markov-1 43,859.342 | no |
| Lorenz--96 x5 shuffled | 65,536 | 215,417.156 | unigram 198,449.519 | no |

Both shuffled nulls were correctly not promoted, but compact CLA lost both
required positives at every frozen horizon. The strict gate therefore
**failed**. Longer fixed-model amortization does not bridge the synthetic
positive to these scalar chaotic calibration streams under the frozen M1 and
complete-code protocol.

This is a coding null. It does not show that either system lacks chaotic
dynamics, assess the full Lorenz--96 state, or validate/refute attractor or
semantic grammar. No trajectory, coordinate, suffix, checkpoint, partition,
learner, codec, or accounting tuning is authorized, and proxy compression
cannot replace this result.

Post-run focused checks passed 2/2; full pytest passed 217/217; `py_compile`
and `git diff --check` passed. The code worktree remained clean at `cbbebfd`.

- `results.json`: `ab58fb48541d259ac7edf93bea62fca8f724a73f754adfc5719349963dc083bb`.
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
- `timing.txt`: `f200ab11bb6556e0f31c617f8f8bf45df1fe539008101c3e45cdc070175838f7`.
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`.

## Next gate

Do not renew scalar M1 attractor calibration or tune these inspected streams.
A next detector lane requires a genuinely different, outcome-independent
hypothesis about representation or dynamics, specified and unit-validated
before any new measured trajectory benchmark.
