# Run 20260716T201500Z-gpt2-pilot-cpu-dry-run

- Project: `relaleap`
- Date: `2026-07-16`
- Status: `succeeded`
- Local or remote: `local CPU only`
- Worktree: `projects/relaleap/worktrees/tinyshakespeare-hdpc`
- Source commit: `c310230` (local, not pushed)

## Question

Does a two-layer stub traverse the frozen three-seed arm, objective, metric,
and validation interfaces twice without configuration, shape, relaxation, or
serialization failures before any GPU request?

## Inputs and command

- Frozen protocol: `configs/gpt2_small_epc_pilot.json`, protocol commit
  `886acdc`.
- Seeds: exactly `1729, 3253, 6421`; arms: `bp_ce`, `bp_kd`, `epc_kd`.
- Stub: two transformer blocks, width 8, two heads, context 8, two updates;
  synthetic tokens only. This intentionally cannot be promotion evidence.

```text
PYTHONPATH=src python3 scripts/run_gpt2_pilot_cpu_dry_run.py \
  --protocol configs/gpt2_small_epc_pilot.json \
  --output projects/relaleap/experiments/20260716T201500Z-gpt2-pilot-cpu-dry-run/artifacts/metrics.json

PYTHONPATH=src python3 -m pytest tests/ -q
git diff --check
```

## Results

- Nine structured metric records completed, one per seed/arm.
- A second complete execution matched exactly after excluding only the declared
  `elapsed_seconds` field.
- Every ePC arm recorded four-state monotone energy traces and finite credit
  diagnostics for both student blocks, plus accepted step sizes and backtrack
  counts for every relaxation transition.
- Metrics SHA-256:
  `004d42b2a9d7a5e8e451a1542ea398038801a226b179bb0703bb21982e60b447`.
- Focused tests before the recorded run: 15 passed. Full suite: 118 passed in
  14.41 seconds. `git diff --check` passed.

## Interpretation and boundary

This is implementation evidence: the frozen arm/objective/serialization seam
works deterministically on CPU, and malformed/non-finite metric records fail
closed. A lazy Hugging Face constructor seam was added, defaulting to staged
local files only. The production GPT-2 adapter/training runner, dependency lock,
immutable image digest, and measured GPU smoke runtime remain incomplete.
Therefore this does not establish GPU readiness and is not a corpus result,
null result, or promotion result. No model/dataset download, remote access, or
paid compute occurred.
