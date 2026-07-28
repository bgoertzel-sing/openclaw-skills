# Run 20260716T181500Z-gpt2-pilot-protocol-freeze

- Project: `relaleap`
- Date: `2026-07-16`
- Status: `succeeded`
- Local or remote: `local CPU; read-only public metadata lookup`
- Worktree: `projects/relaleap/worktrees/tinyshakespeare-hdpc`

## Question

Is the minimum GPT-2-small ePC pilot specified precisely enough to validate
before any paid GPU work, including provenance, controls, deterministic metrics,
promotion rules, and remote-compute bounds?

## Inputs and provenance

- GPT-2 git revision: `607a30d783dfa663caf39e06633721c8d4cfcd7e`
- GPT-2 safetensors LFS SHA-256:
  `248dfc3911869ec493c76e65bf2fcf7f615828b0254c12b473182f0f81d3a707`
- WikiText git revision: `b08601e04326c79dfdd32d625aee71d232d685c3`
- Exact tokenizer and parquet LFS hashes: frozen JSON contract.
- Source before changes: clean worktree at `65666f9`.
- Frozen protocol implementation commit: `886acdc` (local, not pushed).
- Approval-draft pin follow-up: `6b0886b` (local, not pushed).

## Commands and results

```text
PYTHONPATH=src python3 -m pytest tests/test_gpt2_pilot_protocol.py tests/test_hdpc_tinyshakespeare.py -q
11 passed in 0.97s

PYTHONPATH=src python3 -m pytest tests/ -q
113 passed in 13.39s
```

## Interpretation

The protocol contract and existing two-layer transformer invariants validate.
This is protocol/implementation evidence only. It is not the required complete
same-interface CPU dry-run and contains no scientific outcome. Remote execution
remains fail closed pending the listed approval gaps and Ben's explicit bound.
