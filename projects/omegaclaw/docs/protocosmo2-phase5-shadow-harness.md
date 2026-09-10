# ProtoCosmo2 Phase 5 paired shadow harness

Status: ready for an explicitly approved model execution; no provider or
channel was started while preparing this harness.

## Components

- `protocosmo2/tools/phase5_build_runtime_prompt.py` composes the reviewed
  Phase 3 `SOUL.md`, `IDENTITY.md`, and `AGENTS.md` drafts into
  `config/phase5-runtime-prompt.txt`, carrying source hashes.
- `protocosmo2/tools/phase5_shadow_runner.py` validates and replays the frozen
  ten-case suite. It is inert without `--execute`, restricts executions to an
  HTTP loopback endpoint, passes distinct session identities for ZeroBot and
  ProtoCosmo2, contains no Telegram code, and requires
  `outbound_channels: "disabled"` in its configuration.
- `protocosmo2/config/phase5-shadow-runtime.example.json` is a secret-free
  configuration template. `REPLACE_WITH_APPROVED_MODEL` is intentionally not a
  model selection or approval.

## Execution gate

Before execution, copy the example configuration to an ignored local file,
replace only the model identifiers with Ben-approved values, and verify the
gateway's required session-header contract. Then invoke the runner with
`--execute` and a fresh experiment output directory. The result is explicitly
`executed-unadjudicated`: the machine checks are preliminary and a human must
adjudicate each critical case and paired difference before any Phase 6 decision.

## Boundary

This harness is a gateway-level paired prompt replay, not a claim that the
stock OmegaClaw loop was started. The composed ProtoCosmo2 policy prompt makes
the intended behavioral contract inspectable; an adapter that exercises the
full MeTTa skill-dispatch loop is a separate fidelity extension.
