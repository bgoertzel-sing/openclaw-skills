# Run 20260717T002225Z-gpt2-runner-fail-closed-review

- Project: `relaleap`
- Date: `2026-07-16 PDT` / `2026-07-17 UTC`
- Status: `succeeded locally; remote approval remains blocked`
- Local or remote: `local CPU only; read-only Hugging Face metadata lookup`
- Worktree: `projects/relaleap/worktrees/tinyshakespeare-hdpc`
- Source commit: `e4f2f58` (local, not pushed)

## Question

Does the newly added production runner implement the frozen matched-control and
promotion contract fail-closed before any paid GPU provisioning?

## Findings and corrections

- The first runner revision labeled a second fixed 1,000-update BP+KD run as
  wall-clock matched. It now stops before starting the first optimizer update
  after the measured ePC training-time budget.
- The first promotion evaluator could report zero worst-seed regression because
  it selected the maximum from negative gains together with zero. It now uses
  `max(0, -gain)` and requires all frozen seeds.
- The credit gate used `any` within a record. It now requires finite, positive
  ePC credit for each of the six unique student blocks.
- Missing/duplicate update- or wall-clock-matched records and non-finite scalar
  metrics now fail promotion.
- Pod preflight now verifies the archive commit marker plus the pinned teacher,
  tokenizer, and source parquet SHA-256 values before training.
- An overlapping automation run asserted Ben approval without an approving
  inbound message. The approval claim was withdrawn; no provider action ran.

## Commands and results

```text
PYTHONPATH=src python3 -m pytest \
  tests/test_gpt2_pilot_gpu_runner.py tests/test_gpt2_epc.py \
  tests/test_gpt2_pilot_protocol.py tests/test_gpt2_pilot_dry_run.py -q
# 15 passed in 5.53s

PYTHONPATH=src python3 -m pytest tests/ -q
# 126 passed in 29.32s

bash -n launch_runpod.sh
python3 -m py_compile scripts/run_gpt2_pilot_gpu.py
git diff --check
# all passed
```

## Interpretation and boundary

This is implementation and validation evidence only. The production path has
not completed its same-runner one-update GPU smoke, immutable image-digest
check, or measured runtime estimate. It is not corpus evidence, a null result,
or promotion evidence. Explicit bounded approval from Ben is still required
before provisioning any RunPod resource.
