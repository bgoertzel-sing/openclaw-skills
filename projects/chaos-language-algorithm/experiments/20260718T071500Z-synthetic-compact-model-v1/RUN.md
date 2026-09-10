# Synthetic compact-model comparison v1

- Status: preregistered and frozen; outcome not yet inspected.
- Freeze time: 2026-07-18T00:15:00-07:00 / 2026-07-18T07:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/synthetic-compact-model-v1` at
  `4174095c290c89fb46375189acc940015cf9aaf0` (clean).
- Protocol: `docs/synthetic-compact-model-preregistration-v1.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute, push, or remote mutation.

## Frozen hypothesis and rule

Test whether compact indexed model transmission makes the unchanged CLA
frozen-prefix coder competitive on two new constant-length substitution
sources while retaining canonical JSON CLA, canonical LZ78, and complete
literal/unigram/Markov-1/Markov-2 controls. Each fixture uses a 1,024-symbol
prefix and untouched 4,096-symbol suffix plus an exact-marginal shuffled null.

Pass only if every integrity gate passes, compact CLA beats every external
complete-code control on both positives, compact CLA beats JSON CLA on every
fixture, and neither shuffled null is promoted. Both positives are required
and ties fail. This is synthetic finite-model-cost calibration only, not chaos,
attractor, or semantic-grammar evidence.

## Pre-run freeze

- Seed: 18071801; exact generators, split, learner config, fixture hashes,
  shuffle seeds, control accounting, and rule are in `manifest.json`.
- Protocol SHA-256: `0a38f1587e70a75ff8bf4ec60a7a9012a7144b0e81db650df6d9bbefef6922a4`.
- Benchmark implementation SHA-256: `b7b11d697a8cf700c76e9178d88cb17e67ce993218c2a3d00c89de168e0099db`.
- Declaration-test SHA-256: `c49f52232ac4920214152ac1fda4087a209cc5d541a9466015198395bfb516ec`.
- Frozen manifest SHA-256: `0a86b1e19a0ad7737964c8cefe3b89c25a79be5ff5e63b9ca5e7d47877a7b1db`.
- Frozen command SHA-256: `9a2954de14c57805808c4e24a1afbe5f3ecd0b8b5e552d34547c2cf431eeae6d`.
- Environment: Python 3.10.12; Linux x86_64 kernel
  7.0.11-76070011-generic.
- Outcome-independent focused checks: 25 passed; full pytest suite: 211
  passed; benchmark/test `py_compile` and `git diff --check` passed.
- Decisive command: exactly `bash command.sh` from this directory.

No benchmark outcome was produced or inspected before this freeze.

## Results

The exact `bash command.sh` run exited 0 with empty stderr in 57.52 seconds
wall time and 26,300 KiB maximum RSS. Every persistence, deterministic-refit,
replay, JSON/compact indexed decode and byte-stability, LZ78 decode and
byte-stability, suffix-equality, and exact-reconstruction gate passed on all
four fixtures.

| fixture | compact CLA total bits | JSON CLA total bits | strongest external control | compact below strongest |
|---|---:|---:|---:|---|
| complementary 3-uniform positive | 5,865.104 | 6,377.104 | unigram 5,669.836 | no |
| complementary 3-uniform shuffled | 11,409.763 | 12,057.763 | unigram 5,671.814 | no |
| four-state 2-uniform positive | 5,146.362 | 5,610.362 | Markov-2 5,496.923 | yes |
| four-state 2-uniform shuffled | 10,842.984 | 11,482.984 | unigram 5,670.850 | no |

Compact transmission reduced JSON CLA by 464--648 bits with exactly identical
suffix bits. It was sufficient to turn the four-state positive into a bounded
350.562-bit win, but the complementary 3-uniform positive still lost to
unigram by 195.269 bits. Both shuffled nulls were correctly not promoted.
Because both positives were required, the strict frozen gate **failed**.

This is a finite-model-cost calibration null with one bounded positive. It
does not authorize generator, split, horizon, seed, learner, codec, or
accounting tuning against these suffixes. It does not revise either
Mackey--Glass/Lorenz--96 coding null or establish chaos, attractor, semantic,
or intensional grammar evidence.

Post-run focused checks passed 25/25; the full pytest suite passed 211/211;
`py_compile` and `git diff --check` passed. The code worktree remained clean at
`4174095`. Artifact SHA-256 values:

- `results.json`: `8013efd6707811d4bcf422d2c8373a889585f1a3250881a0e23c1e0a50b4fa51`
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `timing.txt`: `8f912918531944b24a10b9f175af5ce3f1a05fcf619e39e62aa59214aff3aed7`
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`
- `manifest.json`: `0a86b1e19a0ad7737964c8cefe3b89c25a79be5ff5e63b9ca5e7d47877a7b1db`

## Next gate

Do not tune or rescore either new suffix and do not renew attractor
calibration. A further measured detector gate requires a new
outcome-independent hypothesis on untouched data; canonical LZ78, compact and
JSON CLA continuity, and simple parametric controls remain required.

## Scope

No prior Zimin, Thue--Morse, Fibonacci, period-doubling, Rudin--Shapiro,
Cantor, paperfolding, Mackey--Glass, or Lorenz--96 suffix is rescored. Neither
outcome authorizes tuning on these new suffixes or renewed attractor
calibration. Proxy compression cannot replace the complete-code decision.
