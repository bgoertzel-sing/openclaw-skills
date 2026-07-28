# Run 20260725T094800Z-e2-e3-full-cpu-feasibility-r1: e2-e3-full-cpu-feasibility-r1

- Project: `carom`
- Started: `2026-07-25T09:48:00Z`
- Finished: `2026-07-25T09:51:59Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/carom/repos/carom`

## Question

Can the frozen five-seed E2/E3 confirmation protocol be completed locally on
the current CPU host within a practical single-session resource bound?

## Hypothesis or expected behavior

One full-configuration seed/arm slice with only one training update will
measure the fixed-corpus evaluation cost and peak memory. All five arms should
execute and repeat evaluation exactly.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed: `7`.
- Evaluation corpus: 2,048 examples, seed `20260720`; reported corpus digest
  `57b2444d3bd22df5be885e14d0ba248ca5b53f8f804a79f9bb4fb7abdb829e1a`.
- Frozen shape: batch 128, `d=64`, `K=16`, 70 controller steps.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

### Direct observations

- All five arms completed and both deterministic evaluations matched exactly.
- Wall time was 3:58.60; peak RSS was 5,158,384 KB.
- Per-arm elapsed times were 42.75--49.51 seconds.
- All arms had slot accuracy `0.1377766927` and exact-workspace accuracy `0`
  after the deliberately non-scientific single update.
- Preserved artifacts: `artifacts/full-slice/`.
- SHA-256: `summary.json`
  `ea11b83fc01c93f387f199c3c5d3bcd0025e4fe2147d24f4e58d324e227838cf`;
  `paired_eval_corpus.pt`
  `060dbfd69849c77a69806f66827b38966abaf59c6b707b446b3cfcd03b765e46`.

### Interpretation

The frozen evaluation is locally executable, but this slice does not measure
the dominant 75,000-update training cost and is not an E2/E3 scientific
disposition. Use the separate training-rate ledger for the feasibility
decision.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Do not launch the full local confirmation unless an approximately
multi-day CPU occupation is explicitly accepted. Freeze numerical scientific
gates before any confirmatory run.
