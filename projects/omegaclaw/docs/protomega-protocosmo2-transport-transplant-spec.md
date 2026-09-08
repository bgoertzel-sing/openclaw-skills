# Protomega transport transplant specification

Date: 2026-08-07
Status: staging implementation authorized by Ben; production cutover pending gates

## Objective

Replace Protomega's unreliable in-process threaded Telegram receive/queue path
with the proven ProtoCosmo2 outer Bot-API transport and durable transaction
contract, while retaining Protomega's identity, prompt, history, provider
routing, OmegaClaw skills, and native bounded document behavior.

## Component boundary

Reuse/adapt from ProtoCosmo2:

- single-process Bot API long polling;
- durable update cursor, pending-inbound record, outbox, delivery receipts,
  deduplication, crash recovery, rate/reply-depth controls, and bounded
  attachment handling;
- one bounded OmegaClaw child invocation per admitted request;
- explicit source chat/message binding for every reply.

Retain from Protomega:

- Telegram bot identity and existing approved chat/user scope;
- the live Protomega OmegaClaw-Core checkout at pinned commit;
- `memory/prompt*.txt`, `memory/history.metta`, skills, security policy, and
  OpenClaw model routing;
- the existing PDF/LaTeX workspace, type, size, and receipt constraints.

Never copy from ProtoCosmo2:

- its bot token or identity constants;
- its prompt, memory, state/cursor, worker state, session IDs, PID/log files,
  or persona-specific failure text;
- its production chat defaults without explicit Protomega configuration.

## Required invariants

1. Exactly one receiver owns `@Protomegabot`.
2. Staging and production have disjoint tokens/identities, state, cursors,
   histories, logs, PID files, attachments, and worker-state directories.
3. Each accepted update is durably recorded before provider execution.
4. A reply/document is durably queued before delivery and marked delivered
   only after a Telegram receipt.
5. Replies always target the originating chat and message.
6. A crash never silently re-executes a possibly-started provider request.
7. Idle operation directly reaches Bot API polling without depending on an
   OmegaClaw/MeTTa receive call or Python thread inside SWI.
8. Provider children receive no Telegram credential.
9. A human-addressed request produces a correlated reply or a bounded visible
   failure.
10. Production cutover is reversible to OmegaClaw-Core commit `f4d7a0b` and
    the preceding supervisor/state archive.

## Acceptance gates

1. Provider-free unit tests cover identity parameterization, cursor recovery,
   duplicate suppression, route preservation, failure reply, document bounds,
   and credential scrubbing.
2. Isolated staging uses a distinct Telegram identity and mutable state, and
   passes repeated idle-first-message and restart trials.
3. An independent frontier-model review finds no unresolved ingress,
   concurrency, identity, credential, or side-effect defect.
4. Production is stopped before the new receiver starts; topology proves one
   receiver and no competing bridge.
5. A fresh Ben-authored production request is correlated across Telegram
   update/message ID, durable inbound, provider result, outbox, delivery
   receipt, and observed reply.

