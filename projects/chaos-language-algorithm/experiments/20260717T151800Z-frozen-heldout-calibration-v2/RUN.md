# Frozen held-out indexed CLA calibration v2

- Status: completed; exit 0; all integrity gates passed; coding pass failed.
- Freeze time: 2026-07-17T08:18:00-07:00 / 2026-07-17T15:18:00Z.
- Repository: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/frozen-suffix-scoring` at full commit recorded in `command.sh`.
- Protocol: `docs/frozen-heldout-mdl-preregistration-v2.md` in that commit.
- Compute: bounded local CPU only; no paid/remote compute, push, or remote mutation.

## Frozen question and pass rule

Test whether the opt-in indexed complete-code learner with joint category/
generalized-chunk proposals has lower aggregate total model-plus-untouched-
suffix bits than the strongest literal, unigram, Markov-1, or Markov-2 baseline
on both new preregistered scalar calibration fixtures. Every deterministic,
canonical-decode, and exact-reconstruction gate must pass. Ties fail and no
fixture may be excluded. Indexed-no-joint and canonical-v1 CLA are controls and
cannot weaken the baseline threshold.

This is a coding calibration only, not evidence of chaos, strange-attractor
structure, or semantic grammar. The v1 suffixes were not inspected or reused.

## Frozen data and configuration

The complete machine-readable declaration is `manifest.json`. Mackey--Glass
uses initial 0.7. Lorenz--96 uses initial `[8,8,8,8,8,8,8,7.99]` and observes
x3 only. Both retain 384 samples after 1,536 discarded samples, use a contiguous
268/116 split, and use prefix-fitted 8-bin scalar M1. The primary seed is 1701.

| fixture | trajectory SHA-256 | symbol-stream SHA-256 | prefix bound |
|---|---|---|---|
| Mackey--Glass v2 | `002fbe083cf81b85bb88a4994f1847cc8674750c5b41a7538ed68fd1abf4af5c` | `a06e1ff9ed766a881683b05ee83dec42b6d8cdb466d79662485758195a0a0671` | `[0.905324640791327, 1.1500804130495688]` |
| Lorenz--96 x3 v2 | `b3e27e6517f2e890f9379ba03cd8a2974220bfa30369fd48854ddf99cfa8f064` | `4dcafb537537ad8ff8254b64afd1b7b5275fe114dc267b7bde3ff8ecbb806084` | `[-5.055615864410875, 7.574880010943145]` |

## Frozen commands and pre-run checks

Manifest generation, executed before any scoring:

```bash
python3 -m chaoslang.benchmarks.frozen_heldout_v2 --manifest-only
```

Decisive command: exactly `bash command.sh`. The script fails closed unless the
repository is clean at the frozen commit and the regenerated manifest matches.

- Focused tests: 21 passed.
- Full suite: 176 passed in bounded per-file processes.
- `py_compile`: passed.
- `git diff --check`: passed.
- No benchmark result had been produced or inspected when this ledger,
  protocol, code/config, seeds, commands, and hashes were frozen.
- Frozen `manifest.json` SHA-256:
  `b10aa115f6d1803e9e34fc300c857219f21a803033d78f30f1f407ca35bca1c9`.
- Frozen `command.sh` SHA-256:
  `bd1847174f5499eef4fb55b85013b9d7912e3aa53226474f7412286b15612406`.

## Results

Exact `bash command.sh` execution completed with exit 0 and empty stderr in
3.76 s wall time with 20,292 KiB maximum RSS. Both fixtures passed every frozen
determinism, canonical-decode, replay, and exact-reconstruction gate.

| fixture | method | model bits | suffix bits | total bits |
|---|---|---:|---:|---:|
| Mackey--Glass v2 | indexed CLA joint | 10,520.000 | 276.021 | 10,796.021 |
| Mackey--Glass v2 | unigram | 3,016.000 | 449.080 | 3,465.080 |
| Mackey--Glass v2 | Markov-1 | 8,200.000 | 972.722 | 9,172.722 |
| Mackey--Glass v2 | canonical CLA v1 control | 31,144.000 | 254.911 | 31,398.911 |
| Lorenz--96 x3 v2 | indexed CLA joint | 11,064.000 | 129.303 | 11,193.303 |
| Lorenz--96 x3 v2 | unigram | 2,968.000 | 306.824 | 3,274.824 |
| Lorenz--96 x3 v2 | Markov-1 | 8,928.000 | 53.151 | 8,981.151 |
| Lorenz--96 x3 v2 | canonical CLA v1 control | 30,400.000 | 135.310 | 30,535.310 |

Aggregate primary indexed CLA was 21,989.324 bits versus the strongest baseline,
unigram, at 6,739.904 bits. Other aggregate baselines were Markov-1 18,153.874,
Markov-2 38,944.549, and literal 41,760.000 bits. **V2 failed its frozen coding
pass rule.** Indexed transmission reduced the canonical-v1 CLA control
(61,934.221 bits), but model cost still dominated the unigram comparator.

No joint proposal was accepted on either prefix: indexed joint and indexed
no-joint controls were identical. This is a coding null, not evidence about
chaos or semantic grammar. No suffix tuning is authorized.

Post-run focused checks passed 21/21; the full suite passed 176/176 in bounded
per-file processes; `git diff --check` passed. Artifact SHA-256 values:

- `results.json`: `8348fa952e0659a01cd3016fbd47f2b579872737f47b9391c37757365bc8dbac`
- `stderr.txt`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `timing.txt`: `298a03059d63cd7fdc173b8f793bcb57b3066df03bfee60fa00c85014da90fb3`
- `exit-status.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`
- `environment.txt`: `70dc38bfe62212671c53c78a1b90fe6307cf324d97e7a36cdcbf43afef600d2c`
