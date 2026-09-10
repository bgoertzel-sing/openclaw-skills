# Synthetic constant-length substitution gate v1

- Status: completed; exit 0; all integrity gates and frozen pass rule passed.
- Freeze time: 2026-07-17T16:19:08-07:00 / 2026-07-17T23:19:08Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/synthetic-uniform-morphism-v1` at
  `d854bc7bb01d768878d202f84afc3a2a7ab86996` (clean).
- Protocol: `docs/synthetic-uniform-morphism-preregistration-v1.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute, push, or remote mutation.

## Frozen hypothesis and rule

The prior Thue--Morse positive and Fibonacci-word null motivate a narrower,
new-data prediction: the unchanged bounded chunk learner is competent on
constant-length substitutions because their aligned reusable blocks match its
representation. Test that prediction on previously unscored period-doubling
and binary-coded Rudin--Shapiro sources, each with a 2,048-symbol prefix and an
untouched 8,192-symbol suffix.

Pass only if every integrity gate passes, indexed CLA strictly beats the
strongest complete literal/unigram/Markov-1/Markov-2 code on both positives,
and it does not do so on either exact-marginal shuffled null. No source may be
dropped and ties fail. This cannot revise the Fibonacci or either
Mackey--Glass/Lorenz--96 coding null and is not chaos or semantic evidence.

## Pre-run freeze

- Seed: 17071702; exact substitutions, codings, split, learner config, fixture
  hashes, and null seeds are in `manifest.json`.
- Benchmark implementation SHA-256:
  `930812022372f8c016b85aed84ee6a6b2b4fe10eda6d1bf92229601490d2da3b`.
- Protocol SHA-256:
  `3100bc81608d8269713aad068b3ec36c7610acaef5d00520b756c53360cabe9f`.
- Declaration-test SHA-256:
  `17af2af4d21971ea3e6cb03cbe1783fdbdd210a07d2813b1ea1ee1e4457bb2b9`.
- Frozen manifest SHA-256:
  `81352ac83b6089e92d6686f45cc3f87e3d1a962e65f271e454fae164ebd72446`.
- Frozen command SHA-256:
  `9e1dcd4675fa7df89ee845ff5b73433a886645c5ac54feb3f050933041f7cf86`.
- Environment: Python 3.10.12; Linux x86_64 kernel
  7.0.11-76070011-generic.
- Outcome-independent focused checks: 2 passed; full discovery suite: 137
  passed; benchmark/test `py_compile` and `git diff --check` passed.
- Decisive command: exactly `bash command.sh` from this directory.

No benchmark outcome was produced or inspected before this freeze.

## Results

The exact `bash command.sh` run exited 0 with empty stderr in 186.65 seconds
wall time and 40,528 KiB maximum RSS. Every persistence, deterministic-refit,
canonical-decode, replay, and exact-reconstruction gate passed on all four
fixtures.

| fixture | indexed CLA total bits | strongest baseline total bits | CLA below baseline |
|---|---:|---:|---|
| period-doubling positive | 5,452.003 | Markov-1 7,872.544 | yes |
| period-doubling shuffled | 16,727.505 | unigram 9,082.929 | no |
| Rudin--Shapiro positive | 9,602.305 | unigram 9,773.770 | yes |
| Rudin--Shapiro shuffled | 16,690.893 | unigram 9,782.987 | no |

Both new 2-uniform positives beat their strongest preregistered complete-code
controls, and neither exact-marginal shuffled null was promoted. The narrower
mechanism gate therefore **passed**. The Rudin--Shapiro margin was only 171.466
bits; it must remain visible and must not be enlarged by suffix/config tuning.

Post-run focused checks passed 2/2; full discovery passed 137/137; benchmark
and test `py_compile` and `git diff --check` passed. The code worktree remained
clean at `d854bc7`. Artifact SHA-256 values:

- `results.json`: `9bbbacb277548c7f3b1cc450aba34401f6f4986d139bd760f054d5d73fe33b34`
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `timing.txt`: `84c60716cd084c7a5677059e55cc8a766f4ebd19f8172bd22e0a01d0147ddf02`
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`
- `actual-manifest.json`: `10cc7e3259dd5c230b5029c0f78d0cff4df41ae81bcc26ddfa65ee31e68c0c16`

## Scope

Passing establishes only bounded complete-code competence on two new uniform
substitution sources. It does not show recovery of the substitution operators,
validate chaos/attractor structure/semantic grammar, or authorize tuning or
renewed attractor calibration. Failure rejects this finite mechanism gate and
does not authorize outcome-sensitive changes.

## Next gate

Do not renew Mackey--Glass/Lorenz--96 calibration from this bounded synthetic
positive. Before another detector claim, specify and unit-validate a fair,
decodable universal-sequence-code control (for example a frozen LZ-family or
context-tree code with explicit model/accounting conventions), then freeze a
new untouched synthetic comparison. Do not rescore these inspected suffixes.
