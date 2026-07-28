# Synthetic universal-control comparison v1

- Status: completed; exit 0; all integrity gates passed; frozen detector rule failed.
- Freeze time: 2026-07-17T20:20:27-07:00 / 2026-07-18T03:20:27Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/synthetic-universal-control-v1` at
  `49418908b73bbdd49691707f55e608bbd2526b2e` (clean).
- Protocol: `docs/synthetic-universal-control-preregistration-v1.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute, push, or remote mutation.

## Frozen hypothesis and rule

Test the unchanged indexed CLA frozen-prefix coder on two new deterministic
binary sources, Cantor ternary substitution and regular paperfolding coding,
against complete literal, unigram, Markov-1, Markov-2, and canonical LZ78 v1
controls. Each fixture has a 1,024-symbol prefix and untouched 4,096-symbol
suffix, plus an exact-marginal shuffled null.

Pass only if every integrity gate passes, indexed CLA strictly beats every
complete-code control including canonical LZ78 on both positives, and it does
not beat the strongest control on either shuffled null. Both positives are
required and ties fail. This is synthetic sequence-code calibration only, not
chaos, attractor, or semantic-grammar evidence.

## Pre-run freeze

- Seed: 18071701; exact generators, split, learner config, fixture hashes,
  shuffle seeds, control accounting, and rule are in `manifest.json`.
- Benchmark implementation SHA-256:
  `9cff441a68af368467f6f5947d494f20d13721951c16659807e9055995ead92b`.
- Protocol SHA-256:
  `03961572b34ba3fc79cec81ba6da6dd6c7a111c5255e7dbd3a57b886ed46cd72`.
- Declaration-test SHA-256:
  `835021abceb46375b2742a09318fd36df0f91aa475f6e2201846155b7048fb69`.
- Frozen manifest SHA-256:
  `88b4a4ca0920fd8a1ad80f28efa3bb855148913caf8f7dd558021fed37abf9e3`.
- Frozen command SHA-256:
  `eedae93bd72ec4c2669b0baff23c3d0b4a9caed0836b19bcd783371fd0d975df`.
- Environment: Python 3.10.12; Linux x86_64 kernel
  7.0.11-76070011-generic.
- Outcome-independent declaration checks: 2 passed; full pytest suite: 200
  passed; benchmark/test `py_compile` and `git diff --check` passed.
- Decisive command: exactly `bash command.sh` from this directory.

No benchmark outcome was produced or inspected before this freeze. Results,
artifact hashes, post-run verification, interpretation, and stop-rule status
will be appended only after the decisive command completes.

## Results

The exact `bash command.sh` run exited 0 with empty stderr in 41.51 seconds
wall time and 25,904 KiB maximum RSS. Every persistence, deterministic-refit,
replay, indexed decode, LZ78 canonical decode, byte-stability, and exact
reconstruction gate passed on all four fixtures.

| fixture | indexed CLA total bits | LZ78 total bits | strongest control total bits | CLA below strongest |
|---|---:|---:|---:|---|
| Cantor positive | 7,219.814 | 2,728.000 | unigram 2,447.226 | no |
| Cantor shuffled | 7,920.631 | 3,560.000 | unigram 2,491.537 | no |
| paperfolding positive | 7,380.844 | 8,056.000 | unigram 5,669.774 | no |
| paperfolding shuffled | 11,760.062 | 11,440.000 | unigram 5,670.444 | no |

CLA correctly did not beat the strongest control on either shuffled null, but
it failed both required positives. On Cantor, its 6,864-bit transmitted model
plus 355.814 suffix bits lost even to LZ78. On paperfolding, CLA beat LZ78 by
675.156 bits, but its 7,040-bit model plus 340.844 suffix bits still lost to
the much cheaper complete unigram code by 1,711.071 bits. The strict frozen
gate therefore **failed**.

This is a bounded complete-code calibration null. It does not erase the short
CLA suffix codes, but those cannot substitute for complete model accounting.
It does not authorize fixture, split, horizon, seed, model-code, or source
tuning, and it provides no chaos, attractor, or semantic-grammar evidence.
Both Mackey--Glass/Lorenz--96 nulls remain binding.

Post-run focused checks passed 16/16; the full pytest suite passed 200/200;
`py_compile` and `git diff --check` passed. The code worktree remained clean at
`4941890`. Artifact SHA-256 values:

- `results.json`: `f638887f0868490011332fb035bd7ee6856106cf7bfaddc641fe21e1614252e1`
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `timing.txt`: `a7af8c41a8aba1204838f8d7d555d50a63874c6e485d6d6cd5c983bc98cc5792`
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`
- `manifest.json`: `88b4a4ca0920fd8a1ad80f28efa3bb855148913caf8f7dd558021fed37abf9e3`

## Next gate

Do not renew attractor calibration or tune either inspected suffix. A next
detector experiment requires a new outcome-independent hypothesis addressing
finite complete-model cost, separately frozen on untouched data with LZ78 and
simple parametric controls retained. Proxy compression cannot replace that
gate.

## Scope

No previously inspected Zimin, Thue--Morse, Fibonacci, period-doubling,
Rudin--Shapiro, Mackey--Glass, or Lorenz--96 suffix is rescored. Neither result
authorizes tuning on these new suffixes or renewed attractor calibration.
