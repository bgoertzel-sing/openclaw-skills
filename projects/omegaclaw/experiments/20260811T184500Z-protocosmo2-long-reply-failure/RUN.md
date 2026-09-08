# ProtoCosmo2 long-reply delivery failure

- Started: 2026-08-11T18:45:00Z
- Status: PASS — independently reviewed, guarded-deployed, and externally accepted
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

Independent review BLOCKED commit `6ace94f` on two remaining live-loop races:
an unsigned `output.txt` value could win when bridge authentication failed, and
an authenticated answer plus already-nonzero child in the same polling cycle
could be mislabeled as healthy. The follow-up removes `output.txt` as a live
answer authority entirely and classifies the child return code before accepting
the authenticated answer. Executable regressions prove unsigned competing
output is ignored and same-cycle answer/nonzero-exit is marked for incident
preservation.

- Follow-up focused runtime/bridge tests: `24 passed in 0.46s`.
- Follow-up full provider-free transport suite: `148 passed in 1.63s`.
- Follow-up compilation and scoped `git diff --check`: passed.

Independent re-review PASSED exact commits `6ace94f66df` +
`42c0461b41d`, including 35 tracked relevant tests in the review checkout and
confirmation that live `output.txt` is diagnostic-only, same-cycle nonzero
exit remains an incident, post-exit grace is bounded/authenticated, and no new
authority or lifecycle regression was found.

ProtoCosmo2 alone was guarded-restarted at 2026-08-11 13:46 PDT. Production
uses reviewed runner/ledger snapshot `7c57c98`, reviewed transport snapshot
`df06c29`, and the bridge driver from exact repair snapshot `42c0461`. Mutable
state stayed byte-identical across restart (SHA-256
`9b2061ad029a1980bfa861bfc3a107d9f9f4cb548298bc2d18aed3874c2d4457`),
cursor remained `387572903`, pending ingress remained zero, and exactly one
ProtoCosmo2 receiver is owned by supervisor PID `3177100` (receiver `3177114`).
Protomega and Protomega2 were not restarted.

External acceptance passed on 2026-08-11 at approximately 14:22 PDT. Ben sent
ProtoCosmo2 the Iter technical description and follow-up rollout instructions.
The durable state binds source messages `1017`, `1018`, and `1021` to delivered
deferred results with Telegram receipts `1023`, `1026`, and `1028`. This proves
the repaired long/deferred reply crossed the live inner bridge and outer
transport. The Iter handoff also exposed a separate limitation: the PDF's
embedded GitHub hyperlink was not presented to the model as an explicit URL;
that does not invalidate this delivery repair and should be handled as a
separate attachment-link extraction task.
