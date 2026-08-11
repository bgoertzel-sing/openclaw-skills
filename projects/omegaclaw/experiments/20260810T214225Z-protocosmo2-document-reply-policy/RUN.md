# ProtoCosmo2 document reply-policy repair

- Started: 2026-08-10T21:42:25Z
- Status: reviewer-blocking defects repaired in staging; fresh independent review and production acceptance open
- Production identity: `@Protocosmo2bot` / ProtoCosmo2
- Production pin before repair: `a73a3127d025028c09e46b99afe470ecf2eaa379`

## Observed failure

Ben's Telegram screenshot in source 18004 shows an ordinary request for more
thoughts about `petta-memory`, accompanied by Markdown documents, receiving the
generic immediate response that the long/document request was queued.

The transport's `_is_deferred()` currently selects immediate deferral whenever
the composed prompt is at least 16,000 characters or contains an extracted
document envelope. Thus document presence, rather than explicit user intent or
observed execution time, determines reply policy.

## Intended behavior

Only narrow explicit persistent/background-work intent should preselect the
immediate deferred lane. Ordinary long/document requests should start exactly
once under a durable reservation, receive the direct answer if they finish
inside the fast grace period, and otherwise atomically promote the same running
execution with a truthful continuation acknowledgement.

## Staging result

Commit `1d68390` removes document presence and extracted prompt length as
immediate-deferral signals. Only narrow explicit persistent/background intent
in the human's current instruction can select that lane. Quoted group context
and extracted document content are excluded from intent classification, so an
untrusted document cannot request background execution.

The screenshot-shaped two-Markdown regression answers directly and proves both
documents reach one prompt. Existing tests prove genuinely slow requests
promote the same execution without rerunning and explicit background work still
queues immediately. Full provider-free suite: 90 passed in 4.72 seconds.
Compilation and `git diff --check` passed. Production is unchanged.

## Remaining gate

Obtain independent frontier review, then explicit authorization for one guarded
ProtoCosmo2 restart and a fresh ordinary multi-document analysis canary.

## Independent review block and staging repair

The independent review of `1d68390` blocked deployment despite 90/90 passing
tests. It reproduced a lane-authority injection: extracted document text could
embed an escaped group-context closing delimiter followed by `run this as a
background job`, and `_is_deferred()` would select the background lane. It also
found missed explicit human phrasings including `please do this in the
background` and `background this job`.

Follow-up staging commit `c701ab5` no longer recovers authority by parsing the composed
prompt. `run_once()` captures the immutable current human instruction before
attachment extraction or group-context composition and passes only that value
to `_is_deferred()`. The bounded intent recognizer now covers the reviewer's
natural-language examples. Regressions preserve the malicious text in the
model prompt while proving it cannot select a lane, and prove three explicit
background phrasings queue immediately.

Observed validation before committing, followed by a clean-commit replay:

- initial focused invocation without the workspace import path failed during
  collection with `ModuleNotFoundError: projects`; zero tests ran;
- corrected focused command passed 40/40 in 2.91 seconds;
- full provider-free command passed 94/94 in 4.24 seconds;
- Python compilation and `git diff --check` passed.

Exact commands are preserved in `command.sh`. Production remained unchanged
throughout staging work.

### Review of c701ab5 and second repair

Fresh independent review BLOCKED `c701ab5` while confirming that document and
group-context lane-authority separation was structurally fixed and replaying
40/40 focused plus 94/94 full tests. It found false deferral for negated or
quoted phrases and missed common affirmative forms such as `Please work on this
in the background`, `Could you handle this in the background?`, and `Make this
a background task`.

Commit `c1fd506` strips quoted spans before classification, fails negated
background intent closed to the ordinary/promotable lane, recognizes those
affirmative forms, and narrows generic job language so questions such as `How
do I run this job?` and `Can you explain how background jobs work?` remain
ordinary. Focused tests pass 49/49; the full provider-free suite passes 103/103;
compilation and `git diff --check` pass. Production remains unchanged pending a
fresh independent review of `c1fd506`.

### Review of c1fd506 and clause-scoped repair

Fresh independent review BLOCKED `c1fd506` after replaying 49/49 focused and
103/103 full tests. Whole-message negation could suppress an affirmative later
clause, while descriptive background-system language and unquoted reported
speech could falsely select immediate deferral.

Commit `9b1d4dc` classifies anchored request clauses independently, scopes
negation to its clause, requires explicit background-lane syntax rather than
generic `background job` vocabulary, and rejects descriptive/reported-speech
forms. All reviewer counterexamples are regressions. Focused tests pass 56/56;
the full provider-free suite passes 110/110; compilation and `git diff --check`
pass. Production remains unchanged pending a fresh independent review of
`9b1d4dc`.

### Review of 9b1d4dc and extended clause repair

Fresh independent review BLOCKED `9b1d4dc` after replaying 56/56 focused and
110/110 full tests. It found four missing explicit action forms, affirmative
commands after comma-linked `then`/`and` clauses, and a trailing reported-speech
false positive.

Commit `7c75810` adds those exact action and clause forms, trailing
reported-speech rejection, and modal-negation coverage. Focused tests pass
64/64; the full provider-free suite passes 118/118; compilation and `git diff
--check` pass. Production remains unchanged pending a fresh independent review
of `7c75810`.

### Review of 7c75810 and remaining variant repair

Fresh independent review BLOCKED `7c75810` after replaying 64/64 focused and
118/118 full tests. It found two `keep/let ... run` affirmative variants, two
trailing reported-speech forms, and one meta-question false positive.

Commit `cc84b72` covers those exact distinctions. Focused tests pass 69/69; the
full provider-free suite passes 123/123; compilation and `git diff --check`
pass. Production remains unchanged pending a fresh independent review of
`cc84b72`.

### Review of cc84b72 and persistent/reported-source repair

Fresh independent review BLOCKED `cc84b72` after replaying 69/69 focused and
123/123 full tests. It found persistent-job/workflow affirmative misses, generic
`according to <source>` reported-speech false deferral, and a meta-question.

Commit `a44abca` covers those distinctions. Focused tests pass 76/76; the full
provider-free suite passes 130/130; compilation and `git diff --check` pass.
Production remains unchanged pending fresh independent review of `a44abca`.

### Independent deployment review of a44abca

PASS for exact clean commit `a44abca6c907c2f1c91e0c2e2af04c44da1c1acc`.
The independent reviewer replayed 76/76 focused and 130/130 full provider-free
tests and found accumulated injection isolation, quoted/reported/meta/negated
language, explicit persistent variants, routing, promotion, state, and rollback
checks green. Production was not touched. Guarded production restart and fresh
external canaries remain authorization-gated.

## Fresh production reproduction under old code

Ben's screenshot in Telegram source 18016 shows the ordinary follow-up being
pre-queued and then ending in the visible bounded failure. Local durable state
correlates source message 920 to deferred acknowledgement receipt 921 and
deferred-failure receipt 922. Task
`5aa5f26e...b53bf` is terminal `failed`; incident sequence advanced to 342,
pending inbound state is empty, and the live pre-fix process remains one
watchdog-owned receiver. This is production reproduction evidence, not repair
acceptance. Independent review was reissued as
`document_reply_policy_review_r2` after the first isolated review session ended
without a retained verdict.

## Production authorization and acceptance

Ben explicitly authorized guarded production restarts of ProtoCosmo2 and
Protomega in Telegram source 18061 on 2026-08-11. Acceptance requires each bot
to restart on exact clean commit `a44abca6c907c2f1c91e0c2e2af04c44da1c1acc`,
preserve its schema-3 production state projection, return with exactly one
watchdog-owned receiver and no pending work, and pass a fresh externally
initiated ordinary-document canary. Any failed restart or canary triggers an
immediate rollback to the recorded pre-restart owner and state baseline.

Next command: guarded ProtoCosmo2 restart under its cutover lock and watchdog
maintenance lease. Evidence path: this record and `artifacts/production-acceptance/`.

The authorized guarded restarts completed on exact clean commit `a44abca`:

- ProtoCosmo2 old owner `2851672` drained and new owner `3079772` returned
  with exactly one receiver. All protected state fields remained identical;
  only `next_update_offset` advanced from `387572858` to `387572859` as the
  receiver acquired the next Telegram update. Its watchdog is healthy,
  maintenance is inactive, and the cutover lock is free.
- Protomega old owner `2851329` drained and new owner `3080233` returned with
  exactly one receiver. Its complete state file remained byte-identical at
  SHA-256 `7a26cbc2bb8e51be47cdd484722bbe1ce568311ad3dd4c594897a2496b22d01e`.
  Its watchdog is healthy and maintenance is inactive.
- Protected runtime-local rollback copies were retained beside each state file.
  Rollback was not activated.

Production acceptance remains open only for fresh human-authored ordinary
Markdown-document messages to each bot. The local agent cannot originate a
message as Ben into another bot's private Telegram conversation; a bot-authored
transport diagnostic would not be equivalent acceptance evidence.

### Production acceptance failed and rollback completed

Fresh human-authored acceptance failed for both identities. Protomega source
`9920` produced visible failure receipt `9921`; ProtoCosmo2 sources `974` and
`979` produced visible failure receipts `975` and `980`. Their private incident
ledgers classify all three as `attachment_unavailable`. ProtoCosmo2's later
source `989` also terminated failed during rollback recovery. This is an
attachment-ingestion defect, not evidence of a provider or lane-selection
failure.

Both owners were stopped under their independent watchdog maintenance leases,
the shared production transport was restored to recorded baseline
`a73a3127d025028c09e46b99afe470ecf2eaa379`, and current cursors/audit state
were preserved to prevent message replay. Protomega restarted as owner
`3122401`; ProtoCosmo2 restarted as owner `3122460`. Each has exactly one
receiver, healthy watchdog ownership, inactive maintenance, and no pending
inbound item. Rollback therefore completed as required; `a44abca` is not in
production.

### Generic-MIME Markdown staging repair

Observed cause: Telegram can label an `.md` document as
`application/octet-stream`; the bounded extractor previously required
`text/*`, so it rejected `INSTALL_LINUX.md` before download. The staging repair
accepts generic MIME only when the existing filename extension allowlist is one
of `.txt`, `.md`, `.csv`, or `.json`; a generic-MIME `.bin` remains blocked.
Focused transport tests pass 78/78 and the full provider-free suite passes
132/132; compilation and `git diff --check` pass. Production remains on the
rollback baseline pending clean commits, independent review, and fresh
deployment authorization.

Independent review PASSED exact transport/test commit
`b424c0d9957e33362895e6a5730cdb11744a532c` and workspace runner commit
`7293ca9aac3397cae111e6b1ec3e72ff63f374f1`. It replayed 78/78 focused and
132/132 full tests, compilation, and diff checks; independently confirmed the
four bounded text suffixes accept generic MIME case-insensitively while `.bin`,
generic `.pdf`, PDF-MIME `.md`, and text-MIME `.exe` fail closed. Existing
size, extraction, path, routing, and bounded-failure controls remain intact.
Production remains on `a73a312`; a new guarded deployment requires Ben's
explicit authorization.

### ZIP acceptance defect and staging repair

Ben's follow-up screenshot showed `ASI CLOUD.zip` receiving visible failures,
followed by ProtoCosmo2 incorrectly claiming that ZIP support existed and that
the upload had stalled. The extractor in fact allowed only PDF and bounded
plain-text types, so this was another `attachment_unavailable` policy rejection
and a misleading model explanation.

The candidate now inspects ZIP archives entirely in memory without writing or
executing members. It bounds archive count, per-entry and aggregate expanded
bytes, compression ratio, path shape, duplicates, encryption, and symlinks;
extracts only an explicit source/text suffix allowlist as strict UTF-8; rejects
NUL-bearing disguised binaries; and exposes a bounded inventory for other file
types. Traversal and binary-disguise regressions fail closed. Focused tests pass
81/81 and the full provider-free suite passes 135/135; compilation and diff
checks pass. Production remains on the rollback baseline pending a new exact
commit review and authorization.
