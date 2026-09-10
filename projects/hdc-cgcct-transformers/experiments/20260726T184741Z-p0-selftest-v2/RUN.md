# Run 20260726T184741Z-p0-selftest-v2: p0-selftest-v2

- Project: `hdc-cgcct-transformers`
- Started: `2026-07-26T18:47:41Z`
- Finished: `2026-07-27T08:07:22Z` (local replay completion)
- Status: `failed_closed`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/hdc-cgcct-transformers/repos/hdc-cgcct-probes`

## Question

Does the full P0-G1 deterministic independent-cleanup replay contract pass twice,
then validate both replays?

## Hypothesis or expected behavior

The 36-cell replay payload is deterministic across the two replays and passes the
P0-G1 validator.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: record here when relevant.

## Results

- Exit status: `1` (the replay/validator process completed; P0-G1 returned false)
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Observed after a fresh single-threaded local process: the 13 exact tests passed
(`13 passed in 1.14s`); both 36-cell replays were written and have the identical
SHA-256 `e0602a37c97dde9d7fa8704bf0d4fe9aa0ccae7be5196dd267e3cdcae4d23f46`.
The validator wrote `p0-g1.json` with SHA-256
`719215ee8b08f88ced2847b55eddc277b488d2e21407e1af52f60203ae5c89e1`, but
returned `P0-G1 passed=False`. The deterministic replay contract is resolved,
but the scientific gate is failed closed.

The sole failing required condition is a non-positive association for the
`k=4, M=32` curve: all six dimensions had accuracy `1.000`, so the recorded
Spearman `D/k`--accuracy value is `0.0` rather than strictly positive. This is
saturation in the frozen P0 grid, not evidence that capacity decreases. The
other curve associations are `0.6546536707`, `0.9411239481`, `0.9411239481`,
`1.0`, and `1.0`; all maximum accuracy reversals are at most `0.0`, and the
maximum matched-M improvement is `0.0`. These facts do not override the frozen
all-curves requirement.

## Reproduction

From the repository directory, the completed command was:

```bash
bash scripts/run_p0_gate.sh ../../artifacts/p0-selftest-v2
```

It uses `OMP_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, fixture seed `12011`, and
2,048 trials in each of 36 cells. The first automation attempt was cut short
by its command window after replay A; the persistent clean local rerun above
completed both replays and validation.

## Follow-up

Do not begin P1A/P1B: Section 8 of the execution specification permits P1 only
after P0-G0/G1 pass. A future explicitly authorized repair must revise the P0
fixture/grid or gate contract before a new independent run; it must preserve
this failed artifact and must not retrofit the conclusion.
