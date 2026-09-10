# Narrow activation proposal — 2026-08-12

## Decision requested and authorization

Ben asked to propose and try a narrow activation in Telegram message 18264.
This proposal treats that as authorization for a bounded production canary,
subject to the preregistered tests, independent review, rollback readiness,
and live acceptance checks below.

Research Rules most relevant at this pivot are Rule 2 (explicit routed-system
spec and invariants), Rule 5 (reproducible evidence), and Rule 7 (separate
policy classification from hook enforcement).

## Activated classes

Only two outbound classes may return `{ cancel: true }` at the global
`message_sending` hook:

1. Content whose trimmed text is exactly `NO_REPLY` or `NO_RESPONSE`.
2. Content matching the previously tested attachment-promise watchdog noise:
   a line beginning with `WATCHDOG_ALERT` or Telegram-rendered `🔍 Watchdog:`,
   immediately followed by `attachment promise not fulfilled`.

Every other outbound payload is sent unchanged. Admission remains entirely
shadow-only: duplicate IDs, own-message loopback, and sibling-not-addressed
recommendations cannot block inference or delivery in E1a.

## Invariants

- Active mode changes egress delivery only for the two allowlisted classes.
- Human-authored inbound messages are never dropped by this slice.
- Ordinary watchdog alerts, explanatory mentions of `NO_REPLY`, attachments,
  captions, and all non-text payloads pass unchanged.
- Shadow mode preserves the current observation-only behavior.
- A classifier, ledger, or hook exception fails open.
- The ledger records the effective mode and whether cancellation was applied;
  it must not label a shadow recommendation as an active suppression.
- Configuration defaults to shadow; active mode must be explicit.
- Rollback is a config reversion to shadow plus a supervisor restart; no
  mutable conversation state or transport cursor is changed.

## Canary and stop conditions

After provider-free tests and independent review pass:

1. Preserve hashes/copies of the installed plugin and effective config.
2. Install the reviewed files and set only this plugin to active mode.
3. Restart through `openclaw-agent.service`; verify exactly one gateway.
4. Send a dedicated exact structured-silence canary through the real outbound
   path and verify a suppressed delivery outcome plus one active ledger row.
5. Send a unique normal control through the same path and verify byte-identical
   Telegram delivery plus one `SEND/DEFAULT_SEND` row.

Immediately roll back to shadow on any hook exception, missing/duplicate
ledger row, suppressed control, delivered suppression canary, content
mutation, competing gateway, or loss of ordinary Telegram reply behavior.

## Attended first trial and next gate

The first E1a trial is operator-attended and lasts only for the two canaries.
Use the watchdog-form suppression string because exact `NO_REPLY` may be
consumed before reaching the outbound hook. After verifying the durable
`cancelled_by_message_sending_hook` outcome, one active suppression ledger
row, Telegram absence, and byte-identical normal control, restore shadow mode
and restart immediately. A 24-hour active window requires a separately tested
non-root kill switch/config reload or an explicitly available operator who
owns the stop condition. No additional class becomes active without a separate
decision; admission filtering, leases, incident coalescing, and semantic
deduplication remain shadow/design work.
