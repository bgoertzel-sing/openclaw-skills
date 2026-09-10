# ProtoMegaBot transient-overload control

## Problem

The live Telegram worker exposed an upstream `HTTP 503` traceback as a normal
`send` action. Channel activity addressed to a sibling bot could therefore
produce an acknowledgement, a failed Opus continuation, and a large diagnostic
message for every new activity update. Repeating the request or increasing the
timeout cannot repair an upstream-overload response.

## Required behavior

1. A group message addressed only to another named bot is dropped before
   enqueue, even when Telegram omits mention entities and leaves only literal
   `@handle` text. It must incur no triage or model call.
2. A transient `429`, `502`, `503`, or `504` response is logged locally and is
   never serialized as a user-facing traceback.
3. After transient overload, the failed model enters a bounded cooldown. Calls
   during that interval bypass it rather than repeatedly probing it.
4. The only automatic overload fallback is the inexpensive
   `openclaw/protomegabot-simple` route. Fable is opt-in and must never be an
   automatic fallback.
5. If the inexpensive fallback also fails, the turn ends silently. Nontransient
   backend notices are concise and rate-limited; full diagnostics remain in the
   supervisor log.
6. The Telegram supervisor remains healthy; no restart loop or timeout increase
   is part of overload recovery.

## Verification

- Unit tests cover raw-text sibling mentions, self-mention precedence,
  transient overload recognition, cooldown bypass, cheap fallback, quiet
  double failure, and rate-limited nontransient notices.
- Direct health checks must show the simple route healthy before deployment.
- Restart the supervised worker once so the new Python and launcher policy are
  loaded, then verify exactly one worker and no unexpected MTProto bridge.
