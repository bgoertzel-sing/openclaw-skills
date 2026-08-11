# ProtoCosmo2 long-reply delivery failure

- Started: 2026-08-11T18:45:00Z
- Status: diagnosis in progress; production unaccepted
- Scope: ProtoCosmo2 long migration-planning request at Telegram 11:28--11:29 PDT

## Deliverable

Repair the routed failure in which ProtoCosmo2 generated a substantive long
answer internally but the outer transport delivered only the bounded failure.

## Acceptance

- Preserve the screenshot request as a provider-free regression.
- Deliver a long multiline answer containing punctuation/quoting through the
  bridge and outer transport without substitution or unsafe action parsing.
- Pass the focused and full provider-free suites.
- Obtain independent review before deployment.
- Restore exactly one supervised receiver and bind a fresh human-authored
  Telegram request to ingress, provider result, and delivery receipt.

## Observed baseline

- Telegram showed a durable-task acknowledgement followed by the bounded
  failure one minute later.
- The inner OmegaClaw history contains the full intended migration-plan answer
  at 11:29:20 PDT, repeated as a `send` action.
- The outer responder ledger recorded `omegaclaw_runtime_failure` with no
  accepted captured bridge answer.
- After the OpenClaw gateway restart, all three outer Omega receivers were
  inactive. They remain stopped while the exact production/staging code split
  is resolved.

## Next command

Reproduce the inner-answer/outer-capture boundary in isolated staging, then
add the smallest provider-free regression and repair.
