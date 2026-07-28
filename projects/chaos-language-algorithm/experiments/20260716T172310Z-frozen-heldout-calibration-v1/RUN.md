# Frozen held-out Mackey--Glass / Lorenz--96 calibration v1

- Status: completed; benchmark failed the preregistered aggregate gate.
- Frozen: 2026-07-16T10:23:10-07:00 (2026-07-16T17:23:10Z).
- Protocol: `../../docs/frozen-heldout-mdl-preregistration-v1.md`.
- Repository/worktree: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/frozen-suffix-scoring` at `c8e9e917db26499f3ab970642546f71af85fea5e` (clean).
- Compute boundary: bounded local CPU only; no paid/remote compute, push, or live integration.

## Frozen question and pass rule

Can a CLA grammar fitted only on each trajectory's first 70% encode the untouched
30% suffix with lower summed model-plus-data bits than the strongest frozen
literal, unigram, order-1 Markov, or order-2 Markov baseline? Every trajectory
must also pass byte-stable state round trips, canonical fact projection, edit-log
replay, deterministic refit, and exact prefix/suffix reconstruction. CLA passes
only if every integrity gate passes and its aggregate is strictly lower than the
strongest decodable baseline. No losing trajectory may be removed.

The current two-part CLA proxy is recorded only as a prefix-training diagnostic.
It is not a decodable held-out code and is excluded from the pass comparison.

## Frozen fixtures and configuration

- 512 retained samples after 1,024 discarded; split index 358 (358 prefix, 154 suffix).
- Prefix-fitted scalar equal-width M1, 8 bins, suffix values clamped to prefix bounds.
- CLA: seed 0, 8 iterations, max n-gram 5, categories enabled.
- Baselines: literal, frozen unigram, frozen Markov orders 1 and 2; one normalized
  ESC count per fitted row and canonical UTF-8 JSON literal payloads.
- Mackey--Glass: fixed-step Euler, `dt=0.1`, physical delay `tau=17.0`
  (170 integration steps), initial 0.5, beta 0.2, gamma 0.1, n 10.
- Lorenz--96: 8D fixed-step RK4, `dt=0.01`, F 8.0, initial
  `[8,8,8,8,8,8,8,8.01]`; observe coordinate x0 only. This is explicit
  low-cardinality calibration, not a full-state grammar claim.
- Full machine-readable declaration: `manifest.json`.

Frozen identifiers:

| fixture | trajectory SHA-256 | symbol-stream SHA-256 | prefix bound |
|---|---|---|---|
| Mackey--Glass | `c4cde4f71704d16127d327d5094fd015fe532c92264c4ca4b4a34e696e0181e6` | `b28b4e0ad063f0ee3e1d80685b2acc08681663dbd91c86fc613b7eef85095f98` | `[0.6051222241182614, 1.2368126562293273]` |
| Lorenz--96 x0 | `80c9b9c7a9732be4ca894863ca6e20220dc600eb97299eab4f8c847d52e43d02` | `1ad155ff5fb7c2955d40641642e0bb6170a60b34c5c2a2c9ccb0eef8ac54a101` | `[-5.395519408548922, 9.889904727307997]` |

## Exact commands

Manifest freeze (executed before scoring):

```bash
python3 -m chaoslang.benchmarks.frozen_heldout --manifest-only --steps 512 --discard 1024 --bins 8 --train-fraction 0.7
```

Decisive run: exactly `bash command.sh`. No benchmark outputs had been produced
or inspected when this record, manifest, hashes, seeds, split, and command were frozen.

## Pre-run verification

- Focused: `python3 -m pytest tests/test_mackey_glass_lorenz96.py tests/test_frozen_heldout_benchmark.py tests/test_frozen_suffix.py tests/test_persistence.py -q` — 45 passed.
- `python3 -m py_compile src/chaoslang/benchmarks/attractors.py src/chaoslang/benchmarks/frozen_heldout.py` — passed.
- `git diff --check` — passed.
- Environment: Python 3.10.12; Linux x86_64 kernel 7.0.11-76070011-generic.

## Results

Exact `bash command.sh` execution completed with exit 0, empty stderr, 1.95 s
wall time, and 20,028 KiB maximum RSS. Both trajectories passed every frozen
state/fact/replay/refit/reconstruction gate.

| fixture | method | model bits | suffix bits | total bits |
|---|---|---:|---:|---:|
| Mackey--Glass | frozen CLA | 32,512.000 | 174.295 | 32,686.295 |
| Mackey--Glass | unigram | 2,848.000 | 485.411 | 3,333.411 |
| Mackey--Glass | Markov-1 | 7,768.000 | 683.048 | 8,451.048 |
| Mackey--Glass | Markov-2 | 15,856.000 | 1,324.578 | 17,180.578 |
| Mackey--Glass | literal | 0.000 | 24,640.000 | 24,640.000 |
| Lorenz--96 x0 | frozen CLA | 32,464.000 | 826.326 | 33,290.326 |
| Lorenz--96 x0 | unigram | 2,784.000 | 471.032 | 3,255.032 |
| Lorenz--96 x0 | Markov-1 | 8,032.000 | 225.207 | 8,257.207 |
| Lorenz--96 x0 | Markov-2 | 17,752.000 | 382.771 | 18,134.771 |
| Lorenz--96 x0 | literal | 0.000 | 23,408.000 | 23,408.000 |

Aggregate totals were: frozen CLA 65,976.621 bits; unigram 6,588.443;
Markov-1 16,708.255; Markov-2 35,315.350; literal 48,048.000. The strongest
baseline was unigram. **CLA therefore failed**: although its Mackey--Glass
suffix data code was shorter than unigram's, its canonical transmitted model
was about 32.5 kbits per fixture and dominated total cost; on Lorenz--96 x0 it
also lost on suffix data bits. This is a coding/calibration null result, not
evidence that either attractor lacks dynamics or that CLA lacks all useful
grammar structure.

No held-out tuning is authorized from these suffix outcomes. Per the frozen
protocol, the next scientific step is a separately preregistered minimal joint
chunk/category diagnostic that can distinguish accounting/coding inadequacy
from greedy-search blindness.

Post-run verification covered all 143 collected tests in bounded shards: 76 +
7 logistic-sweep + 7 Lorenz--96/high-D sweep + 42 remaining + 11 fail-closed
persistence tests, all passed. `git diff --check` passed. Manifest regeneration
matched `manifest.json` exactly.

Artifact SHA-256: `manifest.json` `6295e5d9741961c6ae5fa73d8c32df1f5e21af146a3ba0b6216c9c5e7c10d174`;
`command.sh` `e54e04f5c1229eb225b97a7e2e686228806255fb35301eacafd7241f7c5005dc`;
`results.json` `cc128399193d8dfad2a887d1dad5f9f5a177caf3f6e29e51f6dff04a3440cf9c`;
`stderr.txt` `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
`timing.txt` `57daa237c8659a1d9cfecc66d056f696cd4fbbfe0a074ede895254d25afd8f94`.
