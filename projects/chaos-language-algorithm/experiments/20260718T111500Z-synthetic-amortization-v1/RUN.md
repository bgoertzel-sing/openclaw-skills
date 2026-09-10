# Synthetic fixed-model amortization gate v1

- Status: completed; exit 0; all integrity gates and frozen pass rule passed.
- Freeze time: 2026-07-18T04:15:00-07:00 / 2026-07-18T11:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/synthetic-amortization-v1` at
  `d299b2fa68bb15658a00291d1463c9d8d0ee4696` (clean).
- Protocol: `docs/synthetic-amortization-preregistration-v1.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute, push, or remote mutation.

## Frozen hypothesis and rule

Test whether the unchanged compact indexed CLA frozen-prefix model amortizes
its one-time transmission against canonical LZ78 and simple complete codes at
predeclared longer horizons on one new five-state 2-uniform source. Fit on
1,024 symbols and score cumulative untouched suffixes of 4,096, 16,384, and
65,536 symbols, plus an exact-marginal shuffled null.

Pass only if every integrity gate passes, compact CLA beats every external
control at the final positive horizon, beats JSON CLA throughout, and does not
beat the strongest external control at the final shuffled horizon. Ties fail.
This is synthetic amortization calibration, not chaos, attractor, semantic, or
source-law evidence; it cannot revise the Mackey--Glass/Lorenz--96 nulls.

## Pre-run freeze

- Seed: 18071821; exact source, coding, split, checkpoints, learner, controls,
  fixture hashes, and shuffled-null seed are in `manifest.json`.
- Protocol SHA-256: `69d47bdbf3c12399e91233964b70dd35418e332e11ab6619363a9378f464b526`.
- Benchmark implementation SHA-256: `268eefba1f58dca66ad01eb975e4a76d1c29023e3cec55b93d19deb2911af5a4`.
- Declaration-test SHA-256: `89df67406e6084ea2faf29577345b944c5feb31efe91aa1241abc771214c4e49`.
- Frozen manifest SHA-256: `bc129962f0b3bff0e966842a3cd9c841f18d6aaef799b243716161dc159f4499`.
- Frozen command SHA-256: `cff589dfbbc84f50b301eb5dce5e8cae001821a460031157d6f4e16f6da25d2f`.
- Environment: Python 3.10.12; Linux x86_64 kernel 7.0.11-76070011-generic.
- Outcome-independent focused checks: 2 passed; full pytest suite: 215
  passed; benchmark/test `py_compile` and `git diff --check` passed.
- Decisive command: exactly `bash command.sh` from this directory.

No benchmark outcome was produced or inspected before this freeze.

## Results

The exact `bash command.sh` run exited 0 with empty stderr in 40.67 seconds
wall time and 28,768 KiB maximum RSS. Every integrity gate passed at every
checkpoint.

| fixture | suffix symbols | compact CLA bits | strongest external bits | CLA below strongest |
|---|---:|---:|---:|---|
| positive | 4,096 | 8,167.534 | unigram 5,550.550 | no |
| positive | 16,384 | 12,292.467 | unigram 17,498.784 | yes |
| positive | 65,536 | 28,828.051 | Markov-2 60,768.987 | yes |
| shuffled | 4,096 | 11,079.476 | unigram 5,559.172 | no |
| shuffled | 16,384 | 26,372.954 | unigram 17,497.461 | no |
| shuffled | 65,536 | 87,472.081 | unigram 65,293.673 | no |

The positive first crossed at the frozen 16,384-symbol checkpoint. Canonical
LZ78 used 72,272 bits at the final positive horizon. The shuffled null never
crossed, and compact CLA beat JSON CLA throughout, so the strict gate **passed**.

This establishes one bounded synthetic fixed-model amortization example. It
does not recover the substitution law, validate a general detector, revise any
prior null, or provide chaos, attractor, or semantic-grammar evidence.

Post-run focused checks passed 2/2; full pytest passed 215/215; `py_compile`
and `git diff --check` passed. The worktree remained clean at `d299b2f`.

- `results.json`: `a4746801bf0f7290513bccdfd93fccc383b777dbbecabd750abbf011def4bc22`
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `timing.txt`: `971310d165fca1f56a95d6556e723456581f357ebf87bbe144f83241a53f1f4f`
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`

## Next gate

Do not tune or rescore this source or its checkpoints. A renewed attractor run
still requires a separately justified, frozen bridge from symbolic
amortization competence to chaotic trajectory symbol streams.

## Scope

No prior synthetic or Mackey--Glass/Lorenz--96 suffix is rescored. Neither
outcome authorizes source/checkpoint tuning, renewed attractor calibration, or
substitution of proxy compression for complete-code accounting.
