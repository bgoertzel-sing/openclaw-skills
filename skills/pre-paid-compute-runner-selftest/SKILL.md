---
name: "pre-paid-compute-runner-selftest"
description: "Pre-flight self-tests for runner scripts before paid compute: realized-LR, eval cadence, frozen-param echo, gate presence, CPU dry-run."
---

# Pre-Paid-Compute Runner Self-Test

## Purpose

Before any runner script is approved for paid compute, it must pass a minimal
self-test harness that verifies the runner's actual runtime behavior matches
its frozen protocol. This catches framework API misuse (e.g., passing absolute
LRs as `LambdaLR` multipliers, wrong eval cadence, mismatched optimizer/scheduler
contracts) that unit tests alone miss because they test internal logic, not the
framework contract.

## Trigger

Apply this procedure when:
- A runner script will execute on paid remote compute (RunPod, ASI:Cloud, etc.)
- The runner uses framework schedulers, optimizers, or APIs with non-obvious
  contracts (PyTorch `LambdaLR`, `MultiplicativeLR`, HuggingFace `Trainer`
  args, etc.)
- The remote job has a preregistered RUN.md with frozen gates/parameters

## Procedure

1. **Realized-LR sanity check**: Run the optimizer + scheduler for 3–5 steps
   with a tiny dummy input. Assert that the optimizer's `param_groups[0]['lr']`
   at each step matches the intended schedule within tolerance (e.g., ±5%).
   This catches multiplier/absolute confusion, missing warmup, inverted
   schedules, etc.

2. **Eval cadence verification**: Assert that the runner's evaluation trigger
   fires at the frozen cadence (e.g., every 1000 steps, not 500). Use a mock
   or counter to verify the actual call count over a short run.

3. **Frozen-parameter echo**: Print/verify all frozen protocol parameters
   (LR, batch size, eval cadence, total steps, gate thresholds) and assert
   they match the RUN.md values. Fail closed on any mismatch.

4. **Gate-threshold presence**: Verify that all gates specified in the RUN.md
   have corresponding evaluation code in the runner. A missing gate evaluation
   is a fail-closed error.

5. **Short dry-run on CPU**: If feasible, run the runner for a few steps on
   CPU with a tiny model/dataset to confirm end-to-end execution without
   framework errors before provisioning remote compute.

6. **Record self-test results**: Append the self-test output (pass/fail per
   check) to the experiment record. Do not provision paid compute until all
   checks pass.

## Anti-patterns to avoid

- Testing only that the scheduler object is constructed without error.
- Asserting intended LR values by reading the config rather than the actual
  optimizer state after a step.
- Skipping the dry-run because "the code looks correct."
- Treating a passing unit test on internal logic as sufficient evidence of
  framework API correctness.

## Provenance

Created 2026-07-25 after the CAROM piecewise H100 run wasted USD 0.64 because
absolute LRs were passed as `LambdaLR` multipliers (peak 2e-3 became 4e-6),
and eval cadence was 500 instead of the frozen 1000. This was the second
instance of framework API misuse caught only at paid-compute runtime; the
first was the RelaLeap HDPC grid v1 API mismatch on 2026-07-11.
