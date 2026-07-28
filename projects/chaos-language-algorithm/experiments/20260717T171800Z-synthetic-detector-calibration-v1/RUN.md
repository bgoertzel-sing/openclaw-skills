# Synthetic detector calibration v1

- Status: completed; exit 0; integrity gates passed; frozen detector rule failed.
- Freeze time: 2026-07-17T10:18:00-07:00 / 2026-07-17T17:18:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/synthetic-detector-calibration-v1` at `64b3b333a92128220b6792c4dd2d502784ac3dc5` (clean).
- Protocol: `docs/synthetic-detector-calibration-preregistration-v1.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute, push, or remote mutation.

## Frozen question and rule

Test the indexed frozen CLA coder on one explicit repeated order-5 binary de
Bruijn cycle and a seed-1701 shuffled null preserving the complete stream's
length and exact marginal counts. Each fixture has a 2,048-symbol prefix and an
untouched 1,024-symbol suffix. Compare with literal, unigram, Markov-1, and
Markov-2 codes.

Pass only if every deterministic, persistence/replay, canonical-decode, and
exact-reconstruction gate passes; indexed CLA strictly beats the strongest
baseline on the repeated grammar-positive fixture; and it does not strictly
beat the strongest baseline on the shuffled null. This is a necessary
synthetic detector check, not chaos, attractor, or semantic-grammar evidence,
and it cannot revise the Mackey--Glass/Lorenz--96 v1 or v2 coding nulls.

## Pre-run freeze

- Seed: 1701; exact fixture/config/hashes are in `manifest.json`.
- Implementation SHA-256: `8b4ace6eafe58db14ef908a33b851717844de98b9ed6af1989ff7c1971b5cfdd`.
- Protocol SHA-256: `9020fdfffdbdb058bee5b733683258c0235e9a9aa1c48978d5f6f40a25301766`.
- Declaration-test SHA-256: `da45b5c01e6e4064cf0c749cf8502559491c6b6e495b9ab056ff1b85cd7d9a63`.
- Frozen manifest SHA-256: `c5fa9269ebfd4a97a17f89ecab1cea0df60e0825fddca9f84fc5c5ffdd934cd0`.
- Frozen command SHA-256: `be81c724df82b1f36f5fe3cf4463585486a8e4b97bc73c77e28b40696d466d6c`.
- Environment: Python 3.10.12; Linux x86_64 kernel 7.0.11-76070011-generic.
- Outcome-independent focused checks: 19 passed; declaration checks: 2 passed;
  full suite: 178 passed; benchmark `py_compile` and `git diff --check` passed.
- Decisive command: exactly `bash command.sh` from this directory.

No benchmark outcome was produced or inspected before this freeze.

## Results

The exact `bash command.sh` run exited 0 with empty stderr in 1:41.26 wall
time and 37,836 KiB maximum RSS. Every integrity gate passed on both fixtures.

| fixture | method | model bits | suffix bits | total bits |
|---|---|---:|---:|---:|
| repeated de Bruijn-5 | indexed CLA | 4,600.000 | 0.700 | 4,600.700 |
| repeated de Bruijn-5 | unigram | 1,584.000 | 1,024.721 | 2,608.721 |
| repeated de Bruijn-5 | Markov-1 | 2,464.000 | 1,025.443 | 3,489.443 |
| repeated de Bruijn-5 | Markov-2 | 3,344.000 | 1,026.887 | 4,370.887 |
| shuffled matched null | indexed CLA | 6,608.000 | 1,264.124 | 7,872.124 |
| shuffled matched null | unigram | 1,584.000 | 1,024.753 | 2,608.753 |

The indexed CLA suffix code captured the repeated fixture almost perfectly,
but its 4,600-bit transmitted model exceeded the complete 2,608.721-bit
unigram comparator. The shuffled null was correctly not promoted. Because the
positive condition failed, the preregistered detector calibration **failed**.

This is a bounded synthetic coding null. It shows that the current indexed
frozen detector does not clear even this necessary finite-sample repeated-
grammar gate under complete model transmission. It neither invalidates the
learned repetition nor provides chaos, attractor, or semantic-grammar evidence.
No fixture-length/model-code tuning or renewed attractor run is authorized.

Artifact SHA-256 values:

- `results.json`: `58294e9b22460c2de428219f299c10c4f4ba55007ebbe39fe58c052011285e63`
- empty `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `timing.txt`: `f7226059b32008699593816ed3f0f99af2da72985c40acaf7b3d338cbee84299`
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`

## Next gate

Keep both attractor nulls binding. Before another measured run, specify a new
outcome-independent detector hypothesis and synthetic validation design. Any
model-code refinement or sample-complexity study needs its own frozen ledger,
controls, and rule; this fixture and suffix may not become tuning data.
