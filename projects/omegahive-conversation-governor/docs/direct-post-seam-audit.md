# Direct-post delivery seam audit

- Date: 2026-08-11
- Runtime: OpenClaw 2026.7.1 (`2d2ddc4`)
- Scope: cron `announce`, message-tool, direct subagent, and interactive reply
  delivery; shadow observation only

## Result

The installed runtime has a common instrumentable outbound seam. Cron
announcements do not require an OpenClaw core patch: `deliverCronAnnouncePayload`
calls `sendDurableMessageBatch`, whose `deliverOutboundPayloads` path invokes the
global `message_sending` hook before the channel adapter sends each payload.
The same hook is used for the ordinary durable outbound path.

The governor had registered `reply_payload_sending`, which is narrower and is
not reliable coverage for direct cron/subagent delivery. The staged repair
registers `message_sending` instead. It records a counterfactual egress decision
and returns no cancellation or mutation in the hard-locked shadow mode.

## Immutable ingress identity

The existing `before_agent_run` observation loses Telegram transport identity:
697 of 698 admission records have either an unknown channel or unknown message
ID. The staged observer therefore moves shadow admission capture to
`message_received`, whose typed event/context expose `messageId`, `senderId`,
and canonical `sessionKey`.

Duplicate recommendations now require both a stable channel/session identity
and stable message ID. Sentinel values such as empty, `unknown`, `undefined`,
`null`, `none`, and `n/a` are never inserted into the seen-key set and can never
produce `DROP/DUPLICATE_MESSAGE_ID`. Stable Telegram identities still detect a
true replay.

This repairs observation and replay data quality. It does not activate an
admission gate. A future active phase must use the dedicated `inbound_claim`
gate after replay/canary evidence and explicit approval.

## Source trace

1. `dist/server-cron-DlkxL-F-.js`: `deliverCronAnnouncePayload` ->
   `sendDurableMessageBatch`.
2. `dist/deliver-DGDN_7sT.js`: `deliverOutboundPayloads` obtains the global
   hook runner and invokes `applyMessageSendingHook` before adapter delivery.
3. `dist/hook-types-DQ9eTy2x.d.ts`: `message_sending`, `message_received`, and
   their immutable identity fields are part of the installed typed hook API.

Installed source SHA-256 values:

- `server-cron-DlkxL-F-.js`: `beb1252eea4e0fccdc39b618aae202814c9b3eb826cc9a7d29a29d1777f28d72`
- `deliver-DGDN_7sT.js`: `416069640fd9fd15123d8696daffbbaa7ceba527e4dba5a8ae52c17f32215d08`
- `hook-types-DQ9eTy2x.d.ts`: `fbb4cd0a6254050fa377d4aa97b2d8176caeddea7fead3dbcfba35a987aa10c0`

## Staged change and tests

- `plugins/conversation-governor/index.js`: use `message_received` for ingress
  observation and `message_sending` for all outbound observation.
- `plugins/conversation-governor/core.js`: reject unstable duplicate keys and
  accept typed hook `content` for egress classification.
- Provider-free focused suite: 12/12 passed.
- `git diff --check`: passed for the plugin and project record.
- Experiment:
  `experiments/20260811T232122Z-b7-seam-identity-deployability/`.

## Deployment gate

The workspace implementation is staged only. The installed global extension
and running gateway were not changed. Before shadow deployment: independently
review the hook selection and fail-open behavior, install the exact reviewed
files, restart through the owning supervisor, verify one gateway, and issue one
bounded synthetic cron announce to a dedicated test destination. Acceptance is
a new ledger egress record at `message_sending` plus a real Telegram receipt,
with unchanged payload and no suppression.

Active suppression remains unauthorized.
