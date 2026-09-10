# ProtoMegaTron Output and Telegram Pipeline Hardening Spec

Date: 2026-07-14

## Trigger

A fresh Telegram request asking ProtoMegaTron to elaborate the Ship of Theseus
reference reached the model and received a substantive answer, but no Telegram
reply was sent. The model returned a mixture of parenthesized prose and valid
`pin` actions. The permissive response normalizer converted the whole response
to executable-looking MeTTa forms; unknown prose forms produced inert values,
the pins executed, and the absent `send` action was not treated as a delivery
failure.

## Relevant research rules

- Rule 2: specify routed, stateful behavior and its invariants before editing.
- Rule 4: obtain independent review for this cross-layer hardening decision.
- Rule 7: separate model-output parsing, action validation, execution, and
  delivery acknowledgement so each layer can be replaced independently.

## Invariants

1. A model response is data until every proposed top-level action has passed an
   explicit allowlist and structural validation. Unknown forms must never be
   evaluated, even when mixed with valid actions.
2. The preferred prompt/parser grammar is the versioned
   `omegaclaw.action.v1` JSON envelope. User-facing reply text is a first-class
   field; tool actions are separately allowlisted and arity-checked before
   translation to MeTTa. A strict MeTTa-call form remains temporarily for
   hardcoded triage compatibility.
3. Plain natural-language output on a fresh inbound message remains a safe
   compatibility case and becomes one `send` action.
4. A non-empty mixed or malformed response on a fresh inbound message must not
   partially execute. It becomes a user-visible delivery diagnostic, with the
   malformed content retained only in local logs/history for diagnosis.
5. A fresh inbound response containing valid internal actions but no `send`
   must not silently terminate. The system adds a short user-visible diagnostic
   unless the provider explicitly returned the recognized intentional-no-op
   sentinel.
6. Every Telegram transport attempt returns and logs a structured outcome:
   sent, intentionally deduplicated, skipped because disconnected/unroutable,
   or failed with a sanitized error. Transport failure must not masquerade as a
   successful skill call.
7. Group messages intentionally addressed to another bot remain eligible for
   explicit policy skip and must not trigger a fallback reply.

## Initial implementation boundary

- Replace permissive partial-command normalization with fail-closed JSON and
  strict-legacy validation in `src/helper.py`.
- Replace the ambiguous output contract in `src/loop.metta` with the versioned
  JSON envelope.
- Make the Telegram `send` boundary return explicit status and raise on actual
  transport failure.
- Add focused unit/regression tests for the observed malformed reply, unknown
  mixed forms, valid tool batches, missing-send behavior, no-op handling, and
  Telegram outcomes.

Native Gateway structured-output enforcement is a desirable later enhancement;
the application still validates the schema because routed backends may not all
enforce it.
