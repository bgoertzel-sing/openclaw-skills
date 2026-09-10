# Synthetic source-family generalization v1

- Status: preregistered and frozen; outcome not yet inspected.
- Freeze time: 2026-07-17T14:15:00-07:00 / 2026-07-17T21:15:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/synthetic-family-generalization-v1` at `e6e3ed2183d22779ed44013d272d150a4f5961fa` (clean).
- Protocol: `docs/synthetic-family-generalization-preregistration-v1.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute, push, or remote mutation.

## Frozen hypothesis and rule

Test whether the unchanged indexed CLA coder generalizes from the earlier Zimin
positive to two structurally distinct non-Zimin morphic families: Thue--Morse
and Fibonacci word. Fit on a 2,048-symbol prefix and score an untouched 8,192-
symbol suffix. Pass only if every integrity gate passes, CLA strictly beats the
strongest literal/unigram/Markov-1/Markov-2 complete code on both positives,
and it does not do so on either exact-marginal shuffled null. No family may be
dropped and ties fail.

This is a synthetic symbolic generalization gate, not chaos, attractor, or
semantic-grammar evidence. It cannot revise either Mackey--Glass/Lorenz--96
coding null or authorize suffix tuning.

## Pre-run freeze

- Seed: 170717; exact generators, split, learner config, hashes, and null seeds
  are in `manifest.json`.
- Implementation SHA-256: `36a353aafc0f512a9cb8d0ef276d41b782ef1c8d4774c5cba27a0451722a922f`.
- Protocol SHA-256: `efefecb9a49ccc66e4f8e84220823f693feab16467b55a74800f37cd75866583`.
- Declaration-test SHA-256: `162d4e3f1cb661ad79941d71b20e5430a390fdce2fca98585e954471757f1a87`.
- Frozen manifest SHA-256: `c298906901219d3ba27c3a605f2ffcea5800b2d90210708baa7c9fd15f2ba380`.
- Frozen command SHA-256: `2f4d3288062ef0c3a3b4d7bbe6082d28d6439dd72102b8e3871e6ccac5e06fb2`.
- Environment: Python 3.10.12; Linux x86_64 kernel 7.0.11-76070011-generic.
- Outcome-independent focused checks: 2 passed; full discovery suite: 135
  passed; benchmark/test `py_compile` and `git diff --check` passed.
- One pre-outcome test-sharding harness attempt failed because a filesystem
  path was passed to `unittest` instead of a dotted module name; no benchmark
  scorer ran, and the corrected full discovery suite passed.
- Decisive command: exactly `bash command.sh` from this directory.

No benchmark outcome was produced or inspected before this freeze. Results,
artifact hashes, and post-run verification will be appended after execution.

## Results

The exact `bash command.sh` run exited 0 with empty stderr in 180.49 s wall
time and 39,196 KiB maximum RSS. Every persistence, deterministic-refit,
canonical-decode, replay, and exact-reconstruction gate passed on all four
fixtures.

| fixture | indexed CLA total bits | strongest baseline total bits | CLA below baseline |
|---|---:|---:|---|
| Thue--Morse positive | 7,195.523 | Markov-2 8,700.081 | yes |
| Thue--Morse shuffled | 16,742.813 | unigram 9,782.792 | no |
| Fibonacci-word positive | 6,131.278 | Markov-2 5,843.219 | no |
| Fibonacci-word shuffled | 16,807.407 | unigram 9,436.270 | no |

CLA generalized successfully to Thue--Morse and correctly rejected both nulls,
but missed the Fibonacci-word positive by 288.059 bits. Its Fibonacci suffix
code was substantially shorter than Markov-2 (227.278 versus 3,019.219 bits),
but the complete 5,904-bit CLA model versus the 2,824-bit Markov model reversed
the decision. Because both positives were required, the frozen gate **failed**.

This is a bounded source-family generalization null. It does not erase the
Thue--Morse positive, revise the Zimin result, or license Fibonacci suffix,
split, model-code, or horizon tuning. Both Mackey--Glass/Lorenz--96 coding nulls
remain binding.

Post-run focused checks passed 2/2; full discovery passed 135/135; benchmark
and test `py_compile` and `git diff --check` passed. The code worktree remained
clean at `e6e3ed2`. Artifact SHA-256 values:

- `results.json`: `21707b2db0f582c8f738dba1eac427d6bbb61c6c702734076bfc94cc2c46f83b`
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `timing.txt`: `39f53f7c20cd751e3b20754ba2180a96d5633d64436649ddd041f5d62f5f3117`
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`
- `actual-manifest.json`: `c298906901219d3ba27c3a605f2ffcea5800b2d90210708baa7c9fd15f2ba380`

## Scope

Passing would establish bounded complete-code competence on two classic
morphic source families only. Failure requires a new outcome-independent
hypothesis; neither result licenses tuning on these suffixes or renewed
attractor calibration.
