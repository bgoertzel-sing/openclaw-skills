# ProtoMegaBot output and Telegram delivery hardening plan

Date: 2026-07-14  
Review target: `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core` at commit `be050e58a12b8a86da739d04826e667cf4420446`, branch `agent/telegram-runtime-mods-checkpoint`  
Checkout state: dirty. In particular, `lib_llm_ext.py` and `src/skills.metta` contain uncommitted routing/skill changes, so this plan refers to the inspected working tree, not only the named commit.

## Executive recommendation

ProtoMegaBot needs an explicit turn-and-delivery state machine. The invariant should be:

> Every accepted inbound message keeps the same `correlation_id` through processing and eventually reaches exactly one terminal state: `delivered`, `explicitly_suppressed`, or `failed_visible_to_operator`. `continuation_pending` is an observable intermediate state, never a terminal substitute for a reply. A non-empty model response, parse error, provider error, or Telegram error may not end in an unrecorded no-op.

The clean target output protocol is a versioned JSON envelope in which user-facing text is not a tool call:

```json
{
  "protocol": "omegaclaw.action.v1",
  "reply": {"text": "The user-facing answer"},
  "actions": [
    {"name": "pin", "args": ["working state"]}
  ],
  "continue": null
}
```

For an acknowledgement turn, `reply` is present and `continue` contains a bounded reason. For a tool-only continuation, `reply` may be `null` only if `continue` is non-null. For a message intentionally addressed to another bot, no provider call is needed and the turn ends as `explicitly_suppressed`.

Python should parse and validate this envelope, send `reply.text` through the channel adapter, and translate only validated `actions` into MeTTa calls. Raw LLM text must not be passed to `sread` or `eval`. Native Gateway structured-output support (`response_format: json_schema` or native tool calls) can be enabled when verified, but the application must validate the schema itself because not every routed model/Gateway path is guaranteed to enforce it.

Do not merely change `_looks_like_known_command_response()` from `any(...)` to `all(...)`. That would leave arbitrary command heads, malformed quoting, stale skill names, mixed prose, action-count overflow, and `eval` injection unresolved.

## Confirmed failure paths

1. **The live prompt and executor disagree.** `src/loop.metta:35-43` asks for five plain `toolName arg` lines. The repository's own documentation says the expected shape is `((skillName "arg") ...)` (`docs/reference-internals-skill-dispatch.md:5-13`). `memory/prompt_OpenClaw.txt:65-69` only says “composition of skill calls” and does not settle the syntax.

2. **Partial-command output loses the answer.** `src/helper.py:155-170` considers a response command-like if *any* non-empty line begins with a known command. `balance_parentheses()` at `src/helper.py:173-239` then converts every line into an S-expression, including prose. An observed reproduction against the current file is:

   ```text
   input:  pin working\nHere is the substantive answer.\nMore detail.
   output: ((pin "working") (Here "is the substantive answer.") (More "detail."))
   ```

   The `pin` may execute; the answer becomes invalid MeTTa calls and is never sent.

3. **The parser is not actually a command validator.** `balance_parentheses()` accepts any first token as a command (`src/helper.py:186-237`), does not enforce the prompt's five-action limit, does not enforce arity, and does not reject variables or nested executable forms. The static `LLM_COMMANDS` list (`src/helper.py:7-22`) is also already stale relative to GoalChainer and deontic/directive skills advertised in `src/skills.metta:32-45`. A newly added legitimate command can therefore be sent to the user as literal text, while an unadvertised arbitrary head can reach `eval`.

4. **Parse/evaluation failure is not a delivery failure.** `src/loop.metta:75-89` records errors and stops unless `continue-thinking` ran. There is no check that a `send` action existed or that Telegram accepted it. A substantive raw response can therefore be logged and added to history without a reply.

5. **Telegram cannot report delivery success.** `_send_message_to()` logs and returns `None` for empty text, disconnected state, missing chat, dedup suppression, success, and failure (`channels/telegram.py:1004-1040`). MeTTa's `send` wrapper (`src/channels.metta:29-31`) has no usable receipt.

6. **Deduplication reserves before delivery.** `_is_duplicate_send()` updates `_last_sent_key` and `_last_sent_time` before the API call (`channels/telegram.py:662-685`, called at `1022`). If `sendMessage` then fails at `1031-1039`, an immediate retry is suppressed as a duplicate.

7. **Poll health incorrectly gates send health.** `_send_message_to()` skips the API call whenever `_connected` is false (`channels/telegram.py:1018-1020`). `_connected` reflects the last `getUpdates` call (`channels/telegram.py:860-876`), not whether `sendMessage` is currently reachable. A transient poll error can silently prevent an otherwise valid outbound request.

8. **Newness is inferred from message text, not message identity.** `src/loop.metta:62-67` compares received text with `&prevmsg`. Two distinct Telegram updates with identical text make the second one a continuation, do not reset the loop budget, and disable the new-message prose fallback.

9. **Triage state is global and can attach to the wrong message.** `_triage_pending` and `_pending_route_model` are provider-instance fields (`lib_llm_ext.py:221-227`, `662-716`), not keyed by `MessageEnvelope.correlation_id`. Meanwhile `src/loop.metta:62` dequeues on every iteration, including the continuation after an acknowledgement. Message B can replace message A while A's pending route is active.

10. **The “thread-local” routing envelope is process-global.** `channels/message_envelope.py:72-86` declares one global `_current_envelope` behind a lock. `channels/telegram.py:856` can overwrite it from the polling thread during authentication. `channels/telegram.py:1043-1056` also contradicts the fail-closed module contract at `channels/message_envelope.py:1-6` by falling back to mutable global chat IDs.

11. **Accepted inbound updates are volatile.** `_handle_updates()` advances `_offset` before durable processing (`channels/telegram.py:783-790`) and puts messages only in the in-memory `_pending_messages` list (`channels/telegram.py:151-168`). The next poll acknowledges the update to Telegram. A process crash before delivery loses it. On ordinary startup, `_initialize_offset()` advances past all pending updates (`channels/telegram.py:621-637`, called at `978-981`) unless a confusingly named flag changes the behavior.

12. **Provider success and failure are both represented as strings.** `_subprocess_call()` returns user-facing `(send ...)` text for most main-call failures (`lib_llm_ext.py:490-539`). `_call_with_tier_fallback()` treats any non-empty string as success (`lib_llm_ext.py:623-651`), so its fallback chain is normally bypassed. Similarly, an escalated failure string satisfies the non-empty check at `lib_llm_ext.py:516-518`, preventing the intended chunking fallback.

13. **Prompt/history encoding encourages malformed imitation.** `getContext()` applies `string-safe` to the whole prompt (`src/loop.metta:35-43`); `string-safe` replaces newlines and apostrophes with `_newline_` and `_apostrophe_` (`src/utils.metta:20-24`). History is raw MeTTa-ish output read from a file tail (`src/memory.metta:24-34`), including malformed model calls and errors. The provider splits system and user data using an in-band `:-:-:-:` delimiter (`src/loop.metta:72`, `lib_llm_ext.py:662-667`). The source defaults allow 30,000 history characters and 50,000 result characters (`src/memory.metta:8-14`); the active Telegram launcher currently lowers each to 8,000, but the prompt is still roughly 6 KB of persona plus skills, history, results, and escape artifacts.

14. **Execution is nondeterministic at a side-effect boundary.** `src/loop.metta:82` uses `superpose` over side-effecting calls. The channel layer already has special deduplication because MeTTa alternatives can repeat sends (`src/channels.metta:25-31`). The batch is not fully validated before any action runs, so a later bad action does not mean “nothing was done,” despite the error label.

## Prioritized implementation plan

### 1. Ship a narrow legacy-parser and no-silent-reply hotfix

**Priority:** P0 — silent message loss  
**Effort:** S (less than one day, including focused tests)

**Problem solved:** The active bot can lose plain prose or mixed command/prose today. The larger protocol migration should not be a prerequisite for protecting the live path.

**Code change:**

- In `src/helper.py`, replace `_looks_like_known_command_response()` (`155-159`) with a full-consumption legacy parser returning a typed result, for example:

  ```python
  @dataclass(frozen=True)
  class ParseResult:
      status: Literal["valid", "plain_text", "mixed", "invalid", "empty"]
      actions: tuple[Action, ...]
      unconsumed_text: str
      error: str
  ```

- `parse_legacy_response()` must accept only either:
  - a complete canonical outer tuple `((send "...") (pin "..."))`; or
  - temporarily, complete one-action-per-line legacy commands where every line parses, every head exists in the registry, arity is valid, and the full input is consumed.
- Classify command-free non-empty output as `plain_text`. Classify a mixture of valid commands and any unconsumed text as `mixed`; never discard the unconsumed span.
- For an ordinary fresh human message, convert `plain_text` to one user reply. Do not auto-send `mixed` text because it may include tool syntax or internal material; route it to the repair/fallback guard in Step 2.
- Keep `_is_suppressed_noop_response()` only as an explicitly named provider compatibility case. Do not treat arbitrary empty output as successful suppression.
- In `src/loop.metta:35-43`, immediately replace the current five plain-line examples with one unambiguous legacy transition instruction:

  ```text
  OUTPUT_PROTOCOL (temporary legacy): Return exactly one outer list of 0-5 calls.
  Example: ((send "user-facing text") (pin "working state"))
  Every argument is a quoted JSON-compatible string. No prose outside the list.
  ```

- Align `memory/prompt_OpenClaw.txt:65-69` with exactly the same temporary contract.

**Before/after sketch:**

```python
# before
if new and not any(line_looks_like_command):
    return wrap_everything_as_send(raw)
return balance_parentheses(raw)  # also invents calls from prose

# after
parsed = parse_legacy_response(raw, registry)
if parsed.status == "valid":
    return parsed
if new and parsed.status == "plain_text":
    return ParseResult.reply(raw)
return ParseResult.invalid_with_unconsumed_text(...)
```

**Acceptance tests:** Add `Autotests/test_output_protocol.py` cases for pure prose, `pin` plus prose, parenthesized `pin` plus prose, Markdown/code fences, quoted multiline send, unknown head, stale/new skill, variables, nested expressions, empty output, no-op compatibility text, six actions, and Unicode. The exact reproduction above must retain the prose in `unconsumed_text` and must not execute `Here` or `More`.

### 2. Add a per-turn delivery guard with one repair attempt and a visible fallback

**Priority:** P0 — silent message loss  
**Effort:** M (1–3 days)

**Problem solved:** A non-empty answer, malformed batch, failed `send`, or tool-only terminal output currently ends silently.

**Code change:**

- Add `src/turn_delivery.py` (or equivalently named module) with `TurnState`, keyed by immutable correlation ID:

  ```python
  TurnState(
      correlation_id,
      response_policy,
      phase,                 # received/model_called/parsed/executing/...
      raw_response_hash,
      parse_status,
      reply_required,
      send_attempted,
      send_delivered,
      continuation_pending,
      repair_attempted,
      terminal_status,
  )
  ```

- In `src/loop.metta:74-89`, call a Python coordinator rather than deciding completion only from `$sexpr` and `&continueRequested`. At the end of each ordinary turn:
  1. If a validated reply was delivered, mark `delivered`.
  2. Else if a validated, bounded continuation is pending, mark `continuation_pending` and retain the same message envelope.
  3. Else, if parsing was `mixed`/`invalid` and no repair was attempted, make one formatter-only model call. The repair prompt must quote the raw output as untrusted data and ask only for the JSON envelope; it must not re-run triage or tools.
  4. If repair fails, attempt a fixed, non-model fallback message such as: “I generated a response but could not safely format it. I’ve recorded the failure for retry.”
  5. If Telegram cannot deliver even the fallback, mark `failed_visible_to_operator` in the event journal and supervisor health state. Do not call the turn successful.
- Add `OpenClawProvider.repair_output(raw, protocol_schema, correlation_id)` in `lib_llm_ext.py`. Use a small token limit, no history, no triage, and at most one call. Return a typed provider result, not a string (see Step 9).
- Never send raw `mixed` output as the fallback. Pure prose can be safely promoted to `reply.text` because it contains no recognized action syntax; mixed output may contain internal commands or sensitive diagnostics.
- Bound continuations per inbound message (for example, 3) and total wall time. At the bound, require a final reply or send the fixed fallback.

**Before/after sketch:**

```metta
; before: stop if continue-thinking was not called
(if (get-state &continueRequested) _ (change-state! &loops 0))

; after: Python returns delivered | continue_same_turn | repair | fallback | operator_failure
($terminal (py-call (turn_delivery.finalize $correlation $parse $results)))
(dispatch-turn-terminal $terminal)
```

**Acceptance tests:** A table-driven end-to-end fake-provider/fake-Telegram test must cover: prose-only, valid reply, valid tool-only plus continuation, tool-only without continuation, malformed/mixed output repaired, repair failure with fallback delivered, and Telegram-down fallback failure. Every ordinary input must end in one named terminal state.

### 3. Make Telegram sends return durable, structured receipts and fix deduplication

**Priority:** P0 — silent delivery failure  
**Effort:** M

**Problem solved:** `send_message()` cannot distinguish success from every failure mode, and a failed first attempt poisons deduplication.

**Code change:**

- Change `_send_message_to()` and `send_message()` in `channels/telegram.py:1004-1056` to return a serializable receipt:

  ```python
  {
    "status": "delivered" | "duplicate_delivered" | "partial" | "failed",
    "correlation_id": "...",
    "target_chat_id": "...",
    "delivery_id": "...",
    "chunks_total": 2,
    "chunks_delivered": 2,
    "telegram_message_ids": [123, 124],
    "retryable": false,
    "error_code": null
  }
  ```

- Use `require_current_envelope()` for ordinary replies; introduce a separate explicit `send_admin_message(text, target_chat)` API for administrative broadcasts. Remove the ordinary fallback to `_active_chat_id`, `_reply_chat_id`, or `_chat_id` at `1053-1056`.
- Do not gate send on `_connected`. Attempt `sendMessage` whenever credentials and a target exist. Track polling and outbound health separately.
- Replace `_is_duplicate_send()` with a delivery ledger keyed by `(correlation_id, action_index, text_hash, target_chat)`. Reserve `in_flight`, but mark `delivered` only after Telegram returns success. A failed reservation must be retryable.
- For chunks, persist each returned Telegram message ID before sending the next chunk. On a retry, send only chunks not known delivered. A timeout after Telegram accepted a request is inherently ambiguous; record `unknown` and prefer possible duplicate delivery over silent loss, with an operator-visible metric.
- Add bounded retries for network errors, HTTP 429 using Telegram's `retry_after`, and 5xx. Do not retry permanent 4xx such as invalid chat or blocked bot.
- Change `src/channels.metta:29-31` so the `send` skill returns the receipt to the coordinator instead of discarding it behind `$temp`.

**Before/after sketch:**

```python
# before
if _is_duplicate_send(text, chat):  # records key now
    return
try:
    _api_call("sendMessage", ...)
except Exception:
    print(...)
    return

# after
reservation = ledger.begin(delivery_key)
if reservation.already_delivered:
    return receipt("duplicate_delivered")
try:
    result = send_with_retry(...)
except TelegramError as exc:
    ledger.mark_failed(delivery_key, exc)
    return receipt("failed", retryable=exc.retryable)
ledger.mark_delivered(delivery_key, result["message_id"])
return receipt("delivered", ...)
```

**Acceptance tests:** Extend `Autotests/test_telegram_send_dedupe.py` with failure-then-immediate-retry, success-then-duplicate, partial chunk failure/resume, 429, 5xx, permanent 4xx, poll-disconnected/send-success, and missing-envelope refusal.

### 4. Replace text-equality message detection with correlation-ID turn ownership

**Priority:** P0 — message loss and cross-message state  
**Effort:** M

**Problem solved:** Identical messages are conflated, continuation turns dequeue a different message, and triage routing can migrate across messages.

**Code change:**

- Expose one atomic dequeue API in `channels/telegram.py`, for example `dequeue_message_envelope_json()`, returning text and all safe envelope metadata together. Do not fetch text and correlation in separate calls.
- In `src/loop.metta:21,62-70`, replace `&prevmsg` text comparison with `&activeCorrelationId`. A dequeued envelope is new if its `correlation_id` differs, even when text is identical.
- While `continueRequested` is true, do not call `receive`; continue the current envelope. Leave later inputs queued. After the current turn reaches a terminal state, clear the active envelope and dequeue the next input.
- Pass `correlation_id` explicitly to `callProvider()` and all delivery calls. Do not let the provider import a mutable `telegram.should_skip_response()` global as at `lib_llm_ext.py:669-677`; pass `response_policy` in the call.
- Replace `_triage_pending`/`_pending_route_model` with a per-turn route record keyed by correlation ID, or better, store `selected_route` in `TurnState`. Delete the record on delivery, suppression, timeout, or exception.
- Make the current envelope context-local (`contextvars.ContextVar`) if calls can span threads, or pass the envelope explicitly. The existing global lock does not make a variable thread-local.

**Before/after sketch:**

```metta
; before
($msgnew (and (> (string_length $msgrcv) 0)
              (!= $msgrcv (get-state &prevmsg))))

; after
($incoming (if (get-state &continueRequested)
               (py-call (turn_delivery.active_envelope_json))
               (py-call (telegram.dequeue_message_envelope_json))))
($msgnew (!= (envelope-correlation $incoming)
             (get-state &activeCorrelationId)))
```

**Acceptance tests:** Enqueue A and B from different chats while A receives a triage acknowledgement; verify A's full continuation completes against A and B remains queued. Test two identical text messages with different Telegram update/message IDs. Test an auth event arriving while a normal response is in flight. Test skip-policy messages interleaved with ordinary messages.

### 5. Move to the versioned JSON reply/action protocol

**Priority:** P0 — output safety and correctness  
**Effort:** L (4–8 days including migration and integration tests)

**Problem solved:** Free-text-to-MeTTa repair is intrinsically ambiguous. Treating user communication as a side-effecting tool makes it possible to generate a good answer yet omit its delivery action.

**Code change:**

- Add `src/output_protocol.py` with a checked-in JSON Schema and parser for `omegaclaw.action.v1`.
- Make `reply` a first-class field. Do not represent ordinary user-visible text as a `send` action in the model contract. Preserve `send` only as an internal compatibility mapping during migration.
- Validate:
  - exact protocol version;
  - no unknown top-level fields;
  - UTF-8 string and size limits;
  - 0–5 actions;
  - known action name and exact arity/types;
  - no MeTTa variables or executable nested values;
  - `reply != null` for terminal ordinary turns;
  - `continue != null` only within continuation/time budgets;
  - explicit `null`, not omitted, for absent reply/continuation.
- In `lib_llm_ext.py:_subprocess_call()` (`383-539`), send `response_format: {"type":"json_schema", ...}` when the selected Gateway route has been capability-tested. Otherwise prompt for JSON and still validate locally. Record whether the provider claimed/enforced structured output.
- Update `getContext()` and `memory/prompt_OpenClaw.txt` to show exactly one JSON example and the concise schema. Remove all legacy `toolName arg` and raw MeTTa output examples.
- Delete `balance_parentheses_for_message()` from the live path after a measured compatibility window. Keep a separately named legacy parser only for fixture replay, not production execution.

**Before/after sketch:**

```text
# before model output
pin working
Here is the answer ...

# after model output
{"protocol":"omegaclaw.action.v1",
 "reply":{"text":"Here is the answer ..."},
 "actions":[{"name":"pin","args":["working"]}],
 "continue":null}
```

**Acceptance tests:** Property/fuzz tests must establish that malformed JSON, extra fields, nested objects in arguments, overlong replies, variables, unknown actions, and trailing prose are rejected without execution. Round-trip tests must cover quotes, backslashes, newlines, emojis, astral Unicode, Markdown, parentheses, and strings containing `:-:-:-:`.

### 6. Create one authoritative skill registry and prevalidate the whole batch

**Priority:** P0 — arbitrary execution and stale-contract safety  
**Effort:** M

**Problem solved:** `LLM_COMMANDS`, `getSkills`, and actual MeTTa definitions disagree. The current parser will synthesize and evaluate arbitrary heads.

**Code change:**

- Create one declarative registry, e.g. `src/skill_registry.json`, containing public name, argument schema, user-facing description, risk class, enabled-by-default flag, and MeTTa target.
- Generate or load both:
  - the prompt skill catalogue currently hand-written at `src/skills.metta:1-45`; and
  - the Python validator allowlist currently hand-written at `src/helper.py:7-22`.
- Late-loaded skills must register explicitly at extension load time; an advertised-but-unregistered or registered-but-disabled skill is a startup error.
- Prevalidate the entire action batch before executing the first action. Reject unknown heads, wrong arity, variables, non-string arguments where strings are required, disabled skills, and action count overflow.
- High-risk actions (`shell`, `write-file`, `append-file`, unrestricted `metta`) should pass the existing policy guard before execution, not just rely on prompt wording.

**Before/after sketch:**

```python
# before: static heuristic list and any cmd emitted by balance_parentheses()
if cmd in special_two_arg_cmds: ...
sexprs.append(f'({cmd} "{rest}")')

# after
spec = registry.require_enabled(action.name)
validated_args = spec.validate(action.args)
safe_call = translate_to_metta(spec.target, validated_args)
```

**Acceptance tests:** Registry parity test between all advertised and callable skills, including GoalChainer and deontic/directive extensions; startup failure on duplicates; disabled-skill rejection; policy-guard test for every high-risk class.

### 7. Execute actions sequentially and deterministically

**Priority:** P0 — duplicate/partial side effects  
**Effort:** M

**Problem solved:** `superpose` is a poor execution primitive for ordered external side effects. A malformed later action can follow an already completed earlier side effect, and duplicate alternatives can produce duplicate sends.

**Code change:**

- Replace `superpose` dispatch at `src/loop.metta:82` with a recursive ordered executor over the fully validated list, or implement the coordinator in Python while calling a narrow MeTTa `execute-one-validated-action` bridge.
- Assign each action an index and stable idempotency key `(correlation_id, action_index)`.
- Define ordering explicitly. Recommended default:
  1. validate all actions;
  2. execute internal/read-only actions;
  3. execute approved mutations in listed order;
  4. deliver the reply and record its receipt;
  5. schedule continuation.
- If reply content depends on a tool result, require a continuation rather than pretending actions and a precomputed answer are causally ordered in one batch.
- Record `not_started`, `succeeded`, `failed`, or `unknown` for each action. Never label a partially executed batch “NOTHING_WAS_DONE.”

**Acceptance tests:** Verify stable ordering, one execution per action, no later action after a configured stop-on-error, accurate partial result reporting, and idempotent replay after a crash.

### 8. Persist inbound work before acknowledging Telegram offsets

**Priority:** P0 — crash-induced silent message loss  
**Effort:** L

**Problem solved:** Telegram updates are acknowledged while they exist only in RAM, and normal startup can skip a backlog.

**Code change:**

- Replace `_pending_messages` with a bounded durable queue (SQLite with WAL is sufficient) keyed uniquely by Telegram `update_id`, chat ID, and message ID. Persist the full `MessageEnvelope` plus status, attempts, and timestamps.
- In `_handle_updates()` (`channels/telegram.py:783-857`), validate/authenticate, write accepted envelopes transactionally, then advance the poll offset. On restart, drain `received`/`in_progress` rows before fetching newer work.
- Mark an envelope `completed` only after a terminal turn state has been durably written. On restart, replay `in_progress` with the same correlation and action/delivery idempotency keys.
- Make startup semantics explicit:
  - default: preserve and process backlog;
  - optional operator command: discard backlog with a logged count and reason;
  - remove or rename `TG_SKIP_INITIAL_OFFSET`, whose behavior is hard to infer from `start_telegram():978-981`.
- Bound queue depth and age. If full, do not silently drop. Log an overflow event, expose unhealthy status, and, where possible, send an operator/admin warning.

**Acceptance tests:** Kill the process after durable receive, after model output, after first chunk, and after Telegram success but before local completion; restart and verify at-least-once processing without cross-chat delivery. Verify duplicate Telegram updates are coalesced by update ID. Verify backlog behavior at startup.

### 9. Return typed provider results; do not encode errors as fake assistant text

**Priority:** P1 — fallback reliability and safe diagnostics  
**Effort:** M

**Problem solved:** Non-empty error strings defeat model fallback/chunking logic and mix internal diagnostics with user responses.

**Code change:**

- In `lib_llm_ext.py`, make `_subprocess_call()`, `_chat_subprocess()`, `_call_with_tier_fallback()`, and `chat()` return a typed `ProviderResult` internally:

  ```python
  ProviderResult(
      ok=False,
      content="",
      error_kind="timeout" | "auth" | "overflow" | "transport" | "empty",
      retryable=True,
      model=...,
      attempts=...,
      public_message="The model backend is temporarily unavailable.",
      diagnostic=...,
  )
  ```

- Only the turn coordinator converts final provider failure into the JSON reply/fallback path. Keep detailed stderr in secret-safe operator logs; do not embed up to 900 characters of arbitrary backend detail in a Telegram message as `_failure_response()` currently does at `lib_llm_ext.py:272-281`.
- Make tier fallback check `result.ok`, not `result.strip()`. Make overflow escalation and chunking check error kinds. Narrow `_TRANSIENT_PATTERNS`; the literal `"gateway"` at `lib_llm_ext.py:460-475` is too broad.
- Reset per-turn route state in `finally` and on every terminal outcome.

**Acceptance tests:** Primary error then fallback success, primary overflow then escalation success, primary+escalation overflow then chunking, auth failure without retry storm, empty successful HTTP response, timeout exhaustion, and diagnostic redaction.

### 10. Build structured messages and human-readable bounded history

**Priority:** P1 — model reliability and prompt injection containment  
**Effort:** L

**Problem solved:** The model sees a single escaped blob containing identity, skills, results, raw MeTTa history, and the current message. This makes boundaries unclear and encourages imitation of malformed history.

**Code change:**

- Replace the in-band `:-:-:-:` split with a structured provider API:

  ```python
  callProvider(
      provider_name,
      system_prompt,
      current_user_text,
      history_messages_json,
      tool_schema_json,
      correlation_id,
      response_policy,
      ...,
  )
  ```

- Stop applying `string-safe` to the whole prompt. Preserve ordinary UTF-8/newlines in Python strings and escape only at the narrow MeTTa/Python serialization boundary.
- Replace prompt inclusion of `history.metta` with a normalized sequence of `{role, content}` messages. Exclude raw invalid model output and internal error atoms from conversational history; include a compact operator-safe note such as `[previous response formatting failed]` only when useful.
- Keep an append-only audit record separately (JSONL or SQLite) with correlation ID, raw response hash/location, parsed envelope, action outcomes, and delivery receipt. Raw content retention should be access-controlled and bounded.
- Budget by estimated tokens per section, not only characters. Suggested initial budget:
  - identity/policy: 2–3k tokens;
  - skill JSON/schema: 1–2k;
  - recent dialogue: 4–6k;
  - compact task state/results: 1–2k;
  - current user message/attachment: a separately enforced budget.
- Preserve the last few complete turns, then a provenance-marked summary. Never cut blindly through a MeTTa expression or a UTF-8/JSON object as `read_file_tail` can.
- Treat Telegram attachment and replied-to blocks as explicitly delimited untrusted user content. The existing `_compact_for_triage()` (`lib_llm_ext.py:541-571`) is a useful idea but should operate on structured attachment fields rather than regex over one concatenated string.

**Before/after sketch:**

```python
# before
messages = [{"role":"system", "content": sys_blob_with_history},
            {"role":"user", "content": user_blob}]

# after
messages = [
  {"role":"system", "content": stable_identity_and_policy},
  *bounded_clean_dialogue,
  {"role":"user", "content": current_message_with_structured_attachments},
]
```

**Acceptance tests:** Snapshot the exact messages sent to triage and main models. Assert no `_newline_`, `_apostrophe_`, raw history S-expressions, stale output-format examples, or in-band delimiter. Test malicious `:-:-:-:`, `HUMAN-MSG:`, fake `SYSTEM`, and fake skill-call strings inside user/attachment content.

### 11. Wire the existing event journal into the real path and expose delivery health

**Priority:** P1 — diagnosability  
**Effort:** S–M

**Problem solved:** `channels/event_journal.py` already defines privacy-safe receive/dequeue/send events, but no production channel code calls them. Logs show raw output yet cannot answer “which accepted message never delivered?”

**Code change:**

- Configure `event_journal` at startup and call it from actual ingress, durable dequeue, model start/end, parse, action execution, send attempt/result, repair, fallback, and terminal-state paths.
- Add event kinds for `model_result`, `parse_result`, `action_result`, `repair_result`, and `turn_terminal`. Store content hashes/lengths and classifications, not message bodies or tokens.
- Add counters/gauges:
  - accepted messages without terminal state;
  - ordinary messages without delivered reply beyond SLA;
  - parse/repair/fallback rates;
  - send failure and ambiguous-send rates;
  - queue depth/oldest age;
  - continuation age/count;
  - cross-correlation invariant violations.
- Update supervisor health to fail when an ordinary turn remains nonterminal beyond the configured SLA, not merely when the process/poller is alive.
- Reduce `_log_raw()` at `lib_llm_ext.py:10-12` to a gated debug mode or bounded protected artifact. Full model content in normal stdout can contain private user data or secrets.

**Acceptance tests:** Extend `Autotests/test_event_journal.py` with a full correlation chain and an assertion that every accepted ordinary message ends in exactly one terminal event. Assert journal fields pass `is_secret_safe()` and contain no message bodies.

### 12. Add a failure-injection delivery test suite and make it blocking CI

**Priority:** P1 — regression prevention  
**Effort:** M

**Problem solved:** Existing tests cover send dedupe and simple interleaving, but they do not prove the end-to-end “accepted input implies terminal delivery state” invariant. CI currently treats many integration tests as non-blocking.

**Code change:**

- Add `Autotests/test_turn_delivery_matrix.py` using fake provider and fake Telegram servers.
- Cover at minimum:
  - pure substantive prose without `send`;
  - partial command plus prose;
  - malformed JSON/S-expression;
  - unknown/disabled action and wrong arity;
  - no reply/no continuation;
  - triage ack then final answer;
  - two interleaved chats and identical message texts;
  - skip-policy message;
  - provider timeout/empty/error/fallback;
  - Telegram 429/5xx/4xx/disconnect/partial chunk;
  - crash/restart at every state transition;
  - duplicate model evaluation and duplicate Telegram update;
  - continuation budget exhaustion.
- Add a model-output corpus test from redacted historical failures. Preserve only minimal synthetic fixtures or hashes where private content is involved.
- Make parser, turn-state, routing, send-receipt, and crash-replay suites blocking in `.github/workflows/common.yml`; do not leave delivery invariants in the non-blocking phase.
- Add one bounded local canary that injects a known correlation ID and proves receive → parse → fake Telegram receipt without contacting a paid/external model.

**Acceptance criterion:** For a large randomized/failure-injected run, every accepted ordinary correlation has exactly one terminal outcome, no reply targets a different chat, no invalid action reaches evaluation, and no simulated successful Telegram response is reported as failed or vice versa.

### 13. Clean up content transformations at the Telegram boundary

**Priority:** P2 — output quality  
**Effort:** S

**Problem solved:** `_send_message_to()` performs lossy global transformations (`channels/telegram.py:1004-1013`): every literal `\\n` becomes a newline, and bare tokens resembling `u2014` may be rewritten as Unicode. These transformations can corrupt code and technical text.

**Code change:**

- Carry real newlines and Unicode through the JSON protocol; remove global `.replace("\\\\n", "\n")` and bare-`uXXXX` repair.
- If legacy decoding is temporarily needed, apply it once at the legacy parser boundary and tag the compatibility path in telemetry.
- Split long Telegram messages at paragraph/newline boundaries when possible, while preserving code fences. Continue using a safety margin below Telegram's length limit.
- Optionally set `reply_parameters.message_id` so replies visibly attach to the source message, while retaining `source_chat_id` routing from the immutable envelope.

**Acceptance tests:** Literal backslash-n in code, Unicode escape-like identifiers, emoji, Markdown fences across chunk boundaries, and long paragraphs.

### 14. Reconcile documentation, defaults, and operational controls

**Priority:** P2 — maintainability  
**Effort:** S–M

**Problem solved:** Repository docs, prompt text, source defaults, and launcher overrides describe different contracts and budgets, making regressions likely.

**Code change:**

- Update `docs/reference-internals-loop.md`, `docs/reference-internals-skill-dispatch.md`, `docs/reference-failure-modes.md`, and `docs/reference-python-bridges.md` to describe the JSON envelope, validation, ordered execution, and delivery terminal states.
- Document effective prompt budgets and the launcher overrides (`OMEGACLAW_MAX_HISTORY`/`OMEGACLAW_MAX_FEEDBACK` currently default to 8,000 in the Telegram launcher, versus 30,000/50,000 in `src/memory.metta`).
- Add feature flags for staged rollout:
  - `OMEGACLAW_OUTPUT_PROTOCOL=json_v1|legacy_strict`;
  - `OMEGACLAW_LEGACY_PLAIN_TEXT_REPLY=1` during transition;
  - `OMEGACLAW_REPAIR_ONCE=1`;
  - `OMEGACLAW_REQUIRE_DELIVERY_RECEIPT=1` (default on);
  - explicit backlog policy.
- Remove compatibility flags after measured clean operation; do not leave the permissive parser as an indefinite fallback.

## Recommended rollout order

### Phase A — immediate containment

Implement Steps 1–3 together: strict full-consumption legacy parsing, one repair/fallback guard, and truthful Telegram receipts/dedup. Disable live autonomous wakes during rollout. Run the focused synthetic matrix before restarting the bot.

Exit gate: substantive prose, mixed command/prose, provider failure, and Telegram failure all produce a named terminal state; no raw mixed output is executed.

### Phase B — correct ownership and crash behavior

Implement Steps 4, 7, and 8: correlation-owned turns, deterministic execution, and durable ingress/action/delivery state.

Exit gate: interleaved chats, identical messages, continuation, authentication, and crash/restart tests pass without cross-chat delivery or silent loss.

### Phase C — protocol and prompt migration

Implement Steps 5, 6, 9, and 10: JSON reply/actions, authoritative skill registry, typed provider results, and structured history/messages. Run `legacy_strict` in shadow comparison only, without executing its result, until the JSON path is stable.

Exit gate: at least 100 representative synthetic/redacted turns produce valid JSON or a safely handled repair/fallback; zero unknown actions reach MeTTa; malformed-output rate and fallback rate are reported.

### Phase D — observability and cleanup

Complete Steps 11–14, make invariant tests blocking, update docs, then remove the permissive `balance_parentheses_for_message()` production path.

Exit gate: the supervisor can report received/dequeued/modelled/parsed/executed/delivered counts by correlation, and alert on any nonterminal ordinary message.

## Decisions to record before implementation

1. **Delivery semantics:** Telegram cannot provide perfect exactly-once semantics when a network timeout occurs after server acceptance. Adopt at-least-once delivery with stable idempotency records and explicit `unknown` outcomes; prefer a possible duplicate over silent loss.
2. **Reply versus tool:** User-facing reply is a protocol field owned by the delivery coordinator, not an LLM-selected side-effecting MeTTa skill.
3. **Continuation policy:** One acknowledgement plus a small bounded number of continuations per inbound correlation; continuations retain the same envelope and cannot dequeue a new message.
4. **Legacy behavior:** Pure prose on an ordinary new message may become a reply during transition. Mixed prose/action output is repaired once, never partially executed or blindly sent.
5. **Administrative sends:** They use a separate explicit API with an explicit target. Ordinary reply code must fail closed without an envelope.
6. **History:** Human-readable dialogue context and machine audit history are separate stores. Malformed raw action syntax is not fed back as conversational history.

## Definition of done

The hardening is complete only when all of the following are demonstrated:

- Every accepted ordinary Telegram message has a correlation ID and exactly one durable terminal outcome.
- A substantive prose-only response reaches the correct chat without requiring the model to remember a `send` call.
- Mixed prose/action output cannot lose prose or execute a partial action batch.
- Raw model output cannot invoke an unregistered MeTTa head, exceed action limits, or inject nested executable forms.
- Telegram send failure, deduplication, partial chunks, and retries produce truthful receipts.
- Identical messages and interleaved chats retain distinct turn state and correct routing.
- Provider errors trigger the intended fallback chain because success/failure is typed.
- Prompt messages contain normal UTF-8/newlines, clear role boundaries, one output schema, and bounded clean history.
- Crash/restart tests show durable replay with stable idempotency keys.
- Blocking CI covers the end-to-end delivery invariant, and production health reports nonterminal correlations rather than only process liveness.

