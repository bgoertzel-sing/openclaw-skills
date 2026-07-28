# Synthetic phase-robustness comparison v1

- Status: completed; exit 0; all integrity gates passed; frozen detector rule failed.
- Freeze time: 2026-07-18T02:15:00-07:00 / 2026-07-18T09:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/synthetic-phase-robustness-v1` at
  `a0801998b2b429a979397f1e96abe5edac817e55` (clean).
- Protocol: `docs/synthetic-phase-robustness-preregistration-v1.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute, push, or remote mutation.

## Frozen hypothesis and rule

Test whether compact indexed CLA's bounded uniform-substitution competence is
robust to observation phase on one new three-state 2-uniform source. The two
length-5,120 views begin at offsets zero and one, each with a 1,024-symbol
prefix, untouched 4,096-symbol suffix, and exact-marginal shuffled null.

Pass only if every integrity gate passes, compact CLA beats every external
complete-code control at both positive phases, compact CLA beats JSON CLA on
every fixture, and neither shuffled null is promoted. Both phases are required
and ties fail. This is synthetic phase-robustness calibration only, not chaos,
attractor, or semantic-grammar evidence.

## Pre-run freeze

- Seed: 18071811; exact substitution, coding, phases, split, learner config,
  fixture hashes, shuffle seeds, control accounting, and rule are in
  `manifest.json`.
- Protocol SHA-256: `dc1575a257ce152a62f9adec834c08749a3d6624be88c6560cc2a6a69506f834`.
- Benchmark implementation SHA-256: `ab5486c9792eece993a80d46d709ece0997c775a482710150b27b87f7dd2fae9`.
- Declaration-test SHA-256: `775a2f08af11f7d03dfa2608a911a8493722a10758961f58be60e6123817c003`.
- Frozen manifest SHA-256: `bfb974031e644d3141f130970abcb3334d00d8a4150339f4b08868be2b387f37`.
- Frozen command SHA-256: `83983dde070e916ffa7649b693f09b781521976216c25e73c21d697790ec9186`.
- Environment: Python 3.10.12; Linux x86_64 kernel
  7.0.11-76070011-generic.
- Outcome-independent focused checks: 2 passed; full pytest suite: 213
  passed; benchmark/test `py_compile` and `git diff --check` passed.
- Decisive command: exactly `bash command.sh` from this directory.

No benchmark outcome was produced or inspected before this freeze.

## Results

The exact `bash command.sh` run exited 0 with empty stderr in 47.95 seconds
wall time and 26,160 KiB maximum RSS. Every persistence, deterministic-refit,
replay, JSON/compact indexed decode and byte-stability, LZ78 decode and
byte-stability, suffix-equality, and exact-reconstruction gate passed on all
four fixtures.

| fixture | compact CLA total bits | JSON CLA total bits | strongest external control | compact below strongest |
|---|---:|---:|---:|---|
| phase 0 positive | 4,257.000 | 4,593.000 | LZ78 2,760.000 | no |
| phase 0 shuffled | 12,223.778 | 12,879.778 | unigram 5,327.516 | no |
| phase 1 positive | 4,131.000 | 4,467.000 | LZ78 2,760.000 | no |
| phase 1 shuffled | 11,382.836 | 12,046.836 | unigram 5,331.045 | no |

Compact CLA saved 336 bits versus JSON CLA at both positive phases and
656--664 bits on the shuffled fixtures, but it lost both required positives
to canonical LZ78 by 1,497 and 1,371 bits respectively. Neither shuffled null
was promoted. The strict frozen gate therefore **failed**.

This is a phase-robustness calibration null, not evidence about chaos,
attractors, semantic grammar, or source-law recovery. The similar failure at
both offsets shows that moving the observation origin by one symbol does not
rescue complete-code competitiveness on this source; it does not isolate phase
as the cause of earlier outcomes. No phase, source, suffix, split, horizon,
learner, codec, or accounting tuning is authorized.

Post-run focused checks passed 2/2; the full pytest suite passed 213/213;
`py_compile` and `git diff --check` passed. The code worktree remained clean at
`a080199`. Artifact SHA-256 values:

- `results.json`: `64308055949316a4f803129da4325127885e30aced2f051f4d9af83dd383bb8e`
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `timing.txt`: `3fd23216464e99d817e710591d27c09ae2cfeac7caaa3f9168147db78e72cdeb`
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`
- `manifest.json`: `bfb974031e644d3141f130970abcb3334d00d8a4150339f4b08868be2b387f37`

## Next gate

Do not tune or rescore either phase. Another measured detector gate requires
a genuinely new outcome-independent hypothesis and untouched data, retaining
compact/JSON CLA continuity, canonical LZ78, and simple parametric controls.
The Mackey--Glass/Lorenz--96 nulls remain binding.

## Scope

No prior synthetic or Mackey--Glass/Lorenz--96 suffix is rescored. Neither
outcome authorizes phase, split, horizon, model, or source tuning, renewed
attractor calibration, or substitution of proxy compression for complete-code
comparison.
