# Run 20260716T221908Z-gpt2-production-adapter

- Project: `relaleap`
- Date: `2026-07-16`
- Status: `succeeded`
- Local or remote: `local CPU only`
- Worktree: `projects/relaleap/worktrees/tinyshakespeare-hdpc`
- Source commit: `0cdc70a` (local, not pushed)

## Question

Can the frozen pilot's local ePC activity relaxation traverse actual Hugging
Face GPT-2 residual blocks while preserving native forward logits, the exact
ordinary-KD endpoint, monotone energy, and finite earlier-block credit?

## Inputs and commands

- `transformers==4.57.6` already installed locally; no network or model/data
  download.
- Random two-block GPT-2 test config: vocab 31, context 8, width 16, two heads,
  FFN 32, all dropout zero, KV cache disabled.

```text
PYTHONPATH=src python3 -m pytest tests/test_gpt2_epc.py -q
PYTHONPATH=src python3 -m pytest tests/test_gpt2_epc.py tests/test_gpt2_pilot_protocol.py tests/test_gpt2_pilot_dry_run.py tests/test_hdpc_tinyshakespeare.py -q
PYTHONPATH=src python3 -m pytest tests/ -q
git diff --check
```

## Results

- Adapter forward logits matched native `GPT2LMHeadModel` logits exactly.
- One-state objective matched ordinary KD exactly.
- Four-state relaxation emitted four monotone energy values, three accepted
  step sizes/backtrack counts, finite gradients, and nonzero first-block credit.
- Cache-enabled, nonzero-dropout, wrong-token-dtype, incompatible-model, and
  positional-overflow configurations are rejected before execution.
- Focused adapter tests: 3 passed. Relevant pilot/transformer tests: 19 passed.
  Complete suite: 121 passed in 15.57 seconds. `git diff --check` passed.

## Interpretation and boundary

This closes the production GPT-2 block-state adaptation seam only. It is
implementation evidence, not a corpus diagnostic, null result, GPU-readiness
result, or promotion evidence. No checkpoint/corpus download, provider access,
remote resource, or paid compute was used. The production arm/evaluation CLI,
frozen dependency lock, immutable image digest, live RunPod quote/region,
measured one-update GPU runtime, final clean launch commit, and Ben's explicit
bounded approval remain required before provisioning.
