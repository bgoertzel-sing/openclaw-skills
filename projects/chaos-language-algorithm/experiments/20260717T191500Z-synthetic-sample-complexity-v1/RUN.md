# Synthetic sample-complexity calibration v1

- Status: completed; exit 0; all integrity gates and frozen pass rule passed.
- Freeze time: 2026-07-17T12:15:00-07:00 / 2026-07-17T19:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/synthetic-sample-complexity-v1` at
  `b3709d88412ed1ab97c09abc47803088996263df` (clean).
- Protocol: `docs/synthetic-sample-complexity-preregistration-v1.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute, push, or remote mutation.

## Frozen hypothesis and rule

Test whether the unchanged indexed CLA model has a finite sample-complexity
region on a new repeated Zimin-5 hierarchical symbolic source: one-time model
transmission should eventually be amortized, while an exact-marginal shuffled
null must not be promoted. This does not reuse the failed de Bruijn fixture or
either attractor suffix.

Fit once on 64 motif repeats and score untouched cumulative suffix checkpoints
of 32, 64, 128, and 256 repeats. Pass only if every deterministic, persistence,
replay, canonical-decode, and reconstruction gate passes; CLA strictly beats
the strongest literal/unigram/Markov-1/Markov-2 baseline at the frozen final
positive checkpoint; and it does not do so on the shuffled null. All
checkpoints and the first crossing are reported.

## Pre-run freeze

- Seed: 260717; exact fixture/config/hashes are in `manifest.json`.
- Protocol SHA-256:
  `ac5566dfa589c5d4ee32bc63bd489595d19bac9b7a02322d575453bd5d723f7c`.
- Implementation SHA-256:
  `81ec085796afdcaf97e4f4731e6d1469c73ef4ceafcfab9e6a4f61aae61d219b`.
- Declaration-test SHA-256:
  `01fc916817758dcef0770083e312208c8d93fc534922a8cdf80dbae522fd327f`.
- Frozen manifest SHA-256:
  `3ab8e0c9ee8885c6c46a841dbbae202c8a297abf8d0977e93580d8aa829e44a6`.
- Frozen command SHA-256:
  `78d36d4bdbfd4032a9a316f03b9f1b8c8161c0f5db47f2b629ac2d52cfb69905`.
- Environment: Python 3.10.12; Linux x86_64 kernel
  7.0.11-76070011-generic.
- Outcome-independent focused checks: 7 passed; full suite: 180 passed;
  benchmark `py_compile` and `git diff --check` passed.
- Decisive command: exactly `bash command.sh` from this directory.

No benchmark outcome was produced or inspected before this freeze. Results,
artifact hashes, and post-run verification will be appended after execution.

## Results

The exact `bash command.sh` run completed with exit 0 and empty stderr in
142.04 s wall time with 51,520 KiB maximum RSS. Every deterministic,
persistence, replay, canonical-decode, prefix-reconstruction, and cumulative
suffix-reconstruction gate passed on both fixtures.

| fixture | suffix repeats | suffix symbols | indexed CLA total bits | strongest baseline total bits | CLA below baseline |
|---|---:|---:|---:|---:|---|
| repeated Zimin-5 | 32 | 992 | 4,712.644 | unigram 3,539.284 | no |
| repeated Zimin-5 | 64 | 1,984 | 4,713.288 | unigram 5,318.568 | yes |
| repeated Zimin-5 | 128 | 3,968 | 4,714.575 | Markov-2 6,697.933 | yes |
| repeated Zimin-5 | 256 | 7,936 | 4,717.151 | Markov-2 8,515.866 | yes |
| shuffled matched null | 32 | 992 | 9,386.122 | unigram 3,512.952 | no |
| shuffled matched null | 64 | 1,984 | 11,332.986 | unigram 5,327.396 | no |
| shuffled matched null | 128 | 3,968 | 15,153.058 | unigram 8,836.640 | no |
| shuffled matched null | 256 | 7,936 | 23,030.353 | unigram 16,040.265 | no |

The positive first crossed at the preregistered 64-repeat checkpoint. At the
decisive horizon, its 4,712-bit indexed model plus 5.151 suffix bits was
3,798.715 bits below Markov-2. The null never crossed. The frozen detector rule
therefore **passed**.

This establishes a bounded finite-sample competence region on one new,
strongly repetitive hierarchical symbolic family. It does not revise the
failed de Bruijn checkpoint, either Mackey--Glass/Lorenz--96 null, or validate
chaos, attractor structure, semantic grammar, or general detector calibration.

Post-run focused checks passed 7/7; the full suite passed 180/180;
`py_compile` and `git diff --check` passed. The code worktree remained clean at
`b3709d8`. Artifact SHA-256 values:

- `results.json`: `af8cf7ab896d342a2baf7fe58ec5cc20fae50c5f307ee96ef1ce175ddacf728e`
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `timing.txt`: `7d92572dc26dbd49f1b4355f8598e610f8d007c6056f719ad5cdb7cf7e047264`
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`
- `actual-manifest.json`: `3ab8e0c9ee8885c6c46a841dbbae202c8a297abf8d0977e93580d8aa829e44a6`

## Scope

This is synthetic symbolic sample-complexity calibration only. Passing cannot
revise either Mackey--Glass/Lorenz--96 held-out null or support chaos,
attractor, or semantic-grammar claims. Failure does not authorize fixture,
horizon, or code tuning against these suffixes.

## Next gate

Do not renew attractor calibration from this one-family positive. Specify a
new frozen generalization test over structurally distinct, non-Zimin synthetic
sources with held-out generation parameters and matched nulls. The Zimin
fixture, checkpoints, and suffix may not become tuning data.
