# Generalized complete-code synthetic decision gate v1

- Status: preregistered; not yet executed.
- Protocol: `../../docs/generalized-complete-code-gate-preregistration-v1.md`.
- Scope: frozen 19-frame synthetic fixture only; no attractor suffixes.
- Compute boundary: bounded local CPU only; no remote/paid compute, push, or integration.

## Frozen intent

Compare the initial literal state against exactly one intended joint
category/generalized-chunk state using the complete decodable canonical state
code. Classification and integrity gates are fixed by the protocol. This
cannot revise the Mackey--Glass/Lorenz--96 coding null or establish chaos or
semantic grammar.

## Exact command

```bash
bash command.sh
```

Repository commit, hashes, environment, and outcome-independent verification
will be recorded before executing the command. Results and artifact hashes
will be appended only after execution.

## Pre-run freeze

Frozen at 2026-07-16T22:15:00-07:00 (2026-07-17T05:15:00Z), before
`results.json` existed and before the benchmark module was executed.

- Repository/worktree: `/home/openclaw/research-agent/scratch/chaoslang-strict-replay`.
- Branch/commit: `agent/frozen-suffix-scoring` at
  `ee92bdc72fbaefc2adeb9494433800dea2816826` (clean).
- Fixture: 19 frames / 76 tokens; frozen canonical-symbol SHA-256
  `c828bafa0955f0e30ee947865a944e03ac3081203e6bc9e5d34578951310af89`.
- Implementation SHA-256:
  `2730e94a799fcc68fc6fc0850535e984126bb06f26181d1b901f27d0ebe6f2de`.
- Protocol SHA-256:
  `8def4c462e2bc8d470017cb990be289e9c4e1b93be2210b221240446e994c7e0`.
- Command SHA-256:
  `78731a4494b3d0815e2943b70b48c3d7a144486fee0c0c4349749d2ad5005434`.
- Environment: Python 3.10.12, GCC 11.4.0; Linux x86_64 kernel
  7.0.11-76070011-generic.
- Outcome-independent focused verification:
  `python3 -m pytest tests/test_category_slot.py tests/test_state_code.py -q`
  — 13 passed; benchmark `py_compile` passed; `git diff --check` passed.

## Failed attempt 1

The exact command exited 1 before either state was encoded or scored.
`joint.corpus.symbols` (tokens) was compared with the raw string fixture,
causing the harness-only `joint state changed the source corpus` check to fail.
`results.json` was empty. SHA-256: empty `results.json`
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`;
`stderr.txt` `1fa73df2b079678129a5cd1bd7843faf285b93e03c1ca4456fcb811f0ebe959e`.
No codelength outcome was produced or inspected. The protocol, fixture,
candidate, code, and classification remain unchanged; the corrective attempt
compares against `initial.corpus.symbols`.

## Corrective freeze for attempt 2

Frozen before rerun at clean commit
`8ffa31cf56c75e8c6de4884cee44c1fbbd0b6cc5`. Corrected implementation
SHA-256: `28dc7c627f97f3cd37268690376caf0c2481aa66d70075009bb16422961bcec2`.
Protocol and command hashes remain respectively
`8def4c462e2bc8d470017cb990be289e9c4e1b93be2210b221240446e994c7e0`
and `78731a4494b3d0815e2943b70b48c3d7a144486fee0c0c4349749d2ad5005434`.
The same 13 focused tests, `py_compile`, and `git diff --check` passed. No
benchmark outcome had been produced or inspected.

## Results

Corrective attempt 2 ran the exact `bash command.sh`, exited 0, and emitted
empty stderr. Every frozen fixture, proposal-determinism, exact-reconstruction,
decode, and canonical byte-stability gate passed.

| state | model bits | data bits | total bits |
|---|---:|---:|---:|
| initial literal | 856 | 33,496 | 34,352 |
| intended joint | 7,152 | 27,264 | 34,416 |

The joint move saved 6,232 data bits but added 6,296 model bits, for a frozen
delta of **+64 bits**. Classification: **`complete_code_rejects_joint`**.
Therefore the joint proposal seam remains disabled in `CLA.fit_symbols` and
must not be accepted under the sprint-1 proxy. This is a synthetic coding null;
it does not revise the Mackey--Glass/Lorenz--96 held-out null, establish or
reject chaos/semantic grammar, or authorize a new attractor benchmark.

## Post-run verification

- All 158 tests passed in bounded per-file processes.
- Benchmark `py_compile` and `git diff --check` passed.
- Corrective code worktree remained clean at `8ffa31c`.
- Artifact SHA-256: `results.json`
  `9bf815602b7963d1218ee55a02cc95dc479ca8476880e0c22b8c9a61147e644c`;
  empty `stderr.txt`
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Next gate

Do not enable generalized joint acceptance. Before any new measured benchmark,
specify an outcome-independent, decodable coding refinement, justify its
accounting, and preregister acceptance plus controls. No attractor suffix may
be used to tune that code.
