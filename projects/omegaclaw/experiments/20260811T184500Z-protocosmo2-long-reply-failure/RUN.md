# ProtoCosmo2 long-reply delivery failure

- Started: 2026-08-11T18:45:00Z
- Status: corrected request-bound candidate locally validated; independent review open; production unaccepted
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

Obtain independent review of the exact clean corrected commit, then guarded
deploy only to ProtoCosmo2 if it passes.

## Repair iterations

The first recovery candidate accepted a nonblank atomic `response.json` during
a two-second post-exit grace. It passed 21 focused and 148 full provider-free
tests, but independent review BLOCKED it: the response lacked exact
request/session/prompt binding, could be substituted by another same-UID
producer, silently converted an early inner failure into driver success, and
the race test only inspected source text.

The corrected candidate uses a fresh 256-bit request ID and 256-bit secret per
driver invocation. The secret crosses to the separately owned bridge only via
an inherited anonymous pipe, never argv/environment/disk. The bridge verifies
the exact prompt SHA-256, then atomically publishes an HMAC-SHA256-bound tuple
of status, request ID, prompt digest, session, and raw answer. The driver
accepts only that exact tuple with constant-time MAC comparison. A rescued
answer is emitted for the outer responder but the driver still exits nonzero,
so the runtime failure remains ledgered.

Executable regressions now delay and atomically publish the authenticated
answer during the bounded early-exit grace; reject request, prompt, session,
answer, and MAC substitutions; reject cross-request signed output; and prove
that rescue emits the answer while retaining the nonzero incident signal.

- Focused runtime/bridge tests: `22 passed in 0.36s`.
- Full provider-free transport suite: `148 passed in 1.55s`.
- Compilation and scoped `git diff --check`: passed.
