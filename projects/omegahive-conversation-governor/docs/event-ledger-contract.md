# Phase B: Event and Ledger Contract

Date: 2026-07-24
Status: draft (frozen for implementation after review)
Derived from: Revision 2 design §6.1–6.5, §6.12, §13; Phase A runtime discovery.

## Purpose

This document freezes the data contract for the conversation governor before any
implementation. It defines the canonical event envelope, admission decision,
response lease, thread state, egress candidate, and audit ledger record. The
schemas are JSON Schema candidates suitable for validation in the governor plugin.

All schemas are versioned (`schema_version`). Breaking changes require a new
version and migration note.

## Invariants

1. **Admission before inference.** An event must be admitted or dropped before
   any model call. The admission decision is recorded in the ledger regardless
   of outcome.
2. **One public owner per event.** At most one agent holds an ACTIVE public
   response lease for a given event or task scope. Multiple private review
   slots are allowed.
3. **Silence is structured.** A DROP or no-send decision is recorded as a
   structured ledger entry, never as user-visible prose.
4. **Idempotency by key.** The tuple
   `(sessionKey, messageId, event_type)` uniquely identifies a handled inbound
   event. Retries preserve `retry_of_event_id`. Exact duplicates are dropped
   without model use.
5. **Origin chains are preserved.** Every event carries its causality chain.
   A bot's own outbound message returning through the channel must be
   identifiable as a loopback, not a fresh human request.
6. **Shadow mode is observation-only.** When `mode = shadow`, all decisions
   are recorded but never enforced. The ledger is the source of truth for
   false-silence measurement.
7. **Egress repair is non-semantic.** The egress governor may truncate,
   reformat, or strip narration. It must not add, delete, or alter substantive
   claims (semantic firewall, §6.12.2).
8. **Human intent overrides defaults.** Explicit human addressing, override
   commands (§11), or requests for multiple viewpoints bypass quietness
   policies. Override scope is one message unless explicitly extended.
9. **Governor cost is budgeted.** Every decision records its cost
   (CPU time, model calls, tokens). Net efficiency ratio must be favorable
   (§6.6.1, §13).

---

## Schema 1: EventEnvelope

The canonical representation of an inbound or internal event, normalized from
the OpenClaw plugin hook context.

```jsonschema
{
  "$id": "https://openclaw.ai/schemas/governor/event-envelope.json",
  "type": "object",
  "required": ["event_id", "event_type", "timestamp", "source", "content", "causality"],
  "additionalProperties": false,
  "properties": {
    "schema_version": { "const": "1.0.0" },
    "event_id": {
      "type": "string",
      "description": "Deterministic ID: sha256(sessionKey:messageId:event_type) truncated to 25 chars, prefixed 'evt_'.",
      "pattern": "^evt_[a-f0-9]{21}$"
    },
    "event_type": {
      "type": "string",
      "enum": [
        "human_message",
        "bot_message",
        "system_event",
        "cron_completion",
        "tool_result",
        "review_request",
        "review_response"
      ]
    },
    "timestamp": { "type": "string", "format": "date-time" },
    "source": {
      "type": "object",
      "required": ["channel_id", "sender_id", "sender_kind"],
      "additionalProperties": false,
      "properties": {
        "channel_id": { "type": "string" },
        "channel_type": {
          "type": "string",
          "enum": ["mixed_human_ai", "ai_only", "human_dm", "internal"]
        },
        "sender_id": { "type": "string" },
        "sender_kind": { "type": "string", "enum": ["human", "bot", "system"] },
        "sender_name": { "type": "string" },
        "message_id": { "type": "string", "description": "Channel-native message ID (e.g. Telegram message_id)." }
      }
    },
    "addressing": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "explicit_agents": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Agent IDs explicitly addressed by name or mention."
        },
        "reply_to_agent": { "type": ["string", "null"] },
        "reply_to_event_id": { "type": ["string", "null"] },
        "reply_to_sender": { "type": ["string", "null"] },
        "reply_to_body": { "type": ["string", "null"] },
        "reply_to_is_quote": { "type": "boolean" }
      }
    },
    "causality": {
      "type": "object",
      "required": ["origin_chain"],
      "additionalProperties": false,
      "properties": {
        "caused_by_event_id": { "type": ["string", "null"] },
        "origin_chain": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Ordered list of sender:kinds. human:ben → bot:protocosmo → ..."
        },
        "retry_of_event_id": { "type": ["string", "null"] }
      }
    },
    "scope": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "project_id": { "type": "string" },
        "task_id": { "type": "string" },
        "thread_id": { "type": "string" },
        "state_version": { "type": "integer", "minimum": 0 }
      }
    },
    "content": {
      "type": "object",
      "required": ["text"],
      "additionalProperties": false,
      "properties": {
        "text": { "type": "string" },
        "content_hash": {
          "type": "string",
          "pattern": "^sha256:[a-f0-9]{64}$"
        },
        "attachments": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "kind": { "type": "string" },
              "mime_type": { "type": "string" }
            }
          }
        }
      }
    },
    "policy": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "privacy": { "type": "string", "enum": ["mixed-room", "ai-only", "private"] },
        "urgency": { "type": "string", "enum": ["low", "normal", "high", "critical"] },
        "human_response_expected": { "type": "boolean" },
        "human_override": {
          "type": ["string", "null"],
          "enum": [null, "everyone_answer", "quiet_mode", "show_suppressed", "solo"],
          "description": "Explicit human override command (§11). Scope is one message unless extended."
        }
      }
    },
    "runtime": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "session_key": { "type": "string" },
        "run_id": { "type": "string" },
        "agent_id": { "type": "string" },
        "channel_id": { "type": "string" }
      }
    }
  }
}
```

### Mapping from OpenClaw hook context

| Envelope field | Hook source |
|---|---|
| `source.message_id` | `messageId` (from `PluginHookMessageContext`) |
| `runtime.session_key` | `sessionKey` (from `PluginHookMessageContext`) |
| `runtime.run_id` | `runId` (from `PluginHookMessageContext`) |
| `runtime.agent_id` | `agentId` (from `PluginHookAgentContext`) |
| `runtime.channel_id` | `channelId` (from `PluginHookAgentContext`) |
| `addressing.reply_to_*` | `replyToId`, `replyToBody`, `replyToSender`, `replyToIsQuote` |
| `source.sender_id` | `senderId` |
| `source.sender_kind` | derived: `human` if `senderIsOwner` or not a bot ID; `bot` for known bot agent IDs |
| `content.text` | `prompt` (from `PluginHookBeforeAgentRunEvent`) |

---

## Schema 2: AdmissionDecision

The result of the admission gate. Recorded in the ledger for every event,
whether admitted or dropped.

```jsonschema
{
  "$id": "https://openclaw.ai/schemas/governor/admission-decision.json",
  "type": "object",
  "required": ["event_id", "decision", "timestamp", "mode", "reason_codes"],
  "additionalProperties": false,
  "properties": {
    "schema_version": { "const": "1.0.0" },
    "event_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "mode": { "type": "string", "enum": ["shadow", "active"], "description": "shadow = observe only, active = enforce" },
    "decision": {
      "type": "string",
      "enum": ["ADMIT", "DROP", "LOG_ONLY", "AGGREGATE", "TEMPLATE", "DEFER_UNTIL_COMPLETE"]
    },
    "reason_codes": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "EXPLICITLY_ADDRESSED",
          "HUMAN_QUESTION",
          "HUMAN_OVERRIDE",
          "OWNER_LEASE_ACTIVE",
          "OWN_MESSAGE_LOOPBACK",
          "SIBLING_NOT_ADDRESSED",
          "DUPLICATE_EVENT_ID",
          "DUPLICATE_MESSAGE_ID",
          "REPEATED_INCIDENT_NO_CHANGE",
          "VISIBLE_SILENCE_MARKER",
          "ACKNOWLEDGMENT_ONLY",
          "STATE_VERSION_UNCHANGED",
          "TOOL_PROGRESS_INTERNAL",
          "LEASE_HELD_BY_OTHER",
          "CAPABILITY_MATCH",
          "CONVERSATIONAL_STICKINESS",
          "DEFAULT_OWNER",
          "HUMAN_OVERRIDE_BYPASS"
        ]
      }
    },
    "public_owner": { "type": ["string", "null"], "description": "Agent ID of the public response owner." },
    "private_reviewers": { "type": "array", "items": { "type": "string" } },
    "router_action": {
      "type": ["string", "null"],
      "enum": [null, "DROP", "LOG_ONLY", "TEMPLATE", "CHEAP_MODEL", "NORMAL_MODEL", "DEEP_MODEL"]
    },
    "lease_id": { "type": ["string", "null"] },
    "response_contract_id": { "type": ["string", "null"] },
    "cost": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "cpu_ms": { "type": "number", "minimum": 0 },
        "model_calls": { "type": "integer", "minimum": 0 },
        "tokens_used": { "type": "integer", "minimum": 0 }
      }
    }
  }
}
```

---

## Schema 3: ResponseLease

Prevents two agents from independently answering the same event or task scope.

```jsonschema
{
  "$id": "https://openclaw.ai/schemas/governor/response-lease.json",
  "type": "object",
  "required": ["lease_id", "scope", "holder", "public_slots", "expires_at", "status"],
  "additionalProperties": false,
  "properties": {
    "schema_version": { "const": "1.0.0" },
    "lease_id": {
      "type": "string",
      "pattern": "^lease_[a-f0-9]{21}$"
    },
    "scope": {
      "type": "object",
      "required": ["event_id"],
      "additionalProperties": false,
      "properties": {
        "event_id": { "type": "string" },
        "thread_id": { "type": ["string", "null"] },
        "task_id": { "type": ["string", "null"] },
        "state_version": { "type": ["integer", "null"], "minimum": 0 }
      }
    },
    "holder": { "type": "string", "description": "Agent ID of the public owner." },
    "reviewers": { "type": "array", "items": { "type": "string" } },
    "public_slots": { "type": "integer", "minimum": 0, "default": 1 },
    "expires_at": { "type": "string", "format": "date-time" },
    "status": {
      "type": "string",
      "enum": ["ACTIVE", "EXPIRED", "COMPLETED", "RELEASED", "REASSIGNED"]
    },
    "created_at": { "type": "string", "format": "date-time" },
    "outbound_event_id": { "type": ["string", "null"], "description": "Set when the lease holder delivers a public response. Prevents retries from creating another answer." }
  }
}
```

### Lease lifecycle

```
CREATED → ACTIVE → COMPLETED
                  ↘ EXPIRED → REASSIGNED → ACTIVE
                  ↘ RELEASED
```

- Default TTL: 5 minutes (configurable).
- Stickiness window (§6.3.1): holder remains sticky for 10 minutes of
  inactivity within the same task/thread. Renewed by human continuation or
  evidence-bearing progress by the owner.
- Expiry: if the holder fails to deliver within TTL, the lease expires and
  ownership can be reassigned.
- Completion: when the holder delivers a public response, the lease records
  `outbound_event_id` and transitions to COMPLETED.

---

## Schema 4: ThreadState

Explicit lifecycle state for a conversation thread, preventing echo loops
and closed-thread reopening by acknowledgments.

```jsonschema
{
  "$id": "https://openclaw.ai/schemas/governor/thread-state.json",
  "type": "object",
  "required": ["thread_id", "state", "updated_at"],
  "additionalProperties": false,
  "properties": {
    "schema_version": { "const": "1.0.0" },
    "thread_id": { "type": "string" },
    "state": {
      "type": "string",
      "enum": ["OPEN", "WAITING_FOR_TOOL", "WAITING_FOR_HUMAN", "REVIEWING", "ANSWERED", "CLOSED", "REOPENED"]
    },
    "owner": { "type": ["string", "null"], "description": "Current response owner agent ID." },
    "state_version": { "type": "integer", "minimum": 0 },
    "last_event_id": { "type": ["string", "null"] },
    "last_outbound_event_id": { "type": ["string", "null"] },
    "updated_at": { "type": "string", "format": "date-time" },
    "closed_reason": { "type": ["string", "null"] },
    "reopen_conditions_met": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["new_evidence", "human_followup", "consequential_correction", "state_version_change", "explicit_reopen_command"]
      }
    }
  }
}
```

### Thread state transitions

```
OPEN → WAITING_FOR_TOOL → OPEN
OPEN → WAITING_FOR_HUMAN → OPEN
OPEN → REVIEWING → ANSWERED → CLOSED
CLOSED → REOPENED (requires ≥1 reopen condition) → OPEN
```

A CLOSED thread must NOT be reopened by: acknowledgments, repeated status,
sibling echoes, or visible silence markers.

---

## Schema 5: EgressCandidate

The post-inference outbound message, examined by the egress governor before
delivery.

```jsonschema
{
  "$id": "https://openclaw.ai/schemas/governor/egress-candidate.json",
  "type": "object",
  "required": ["event_id", "agent_id", "text", "send_intent", "timestamp"],
  "additionalProperties": false,
  "properties": {
    "schema_version": { "const": "1.0.0" },
    "event_id": { "type": "string" },
    "lease_id": { "type": ["string", "null"] },
    "agent_id": { "type": "string" },
    "message_class": {
      "type": "string",
      "enum": ["direct_answer", "tool_result", "status_update", "acknowledgment", "no_reply", "error", "progress"]
    },
    "text": { "type": "string" },
    "claims": { "type": "array", "items": { "type": "string" } },
    "new_facts": { "type": "array", "items": { "type": "string" } },
    "references": { "type": "array", "items": { "type": "string" } },
    "send_intent": { "type": "boolean" },
    "timestamp": { "type": "string", "format": "date-time" },
    "egress_decision": {
      "type": ["string", "null"],
      "enum": [null, "SEND", "SUPPRESS", "REPAIR_THEN_SEND", "AGGREGATE"]
    },
    "egress_reason": { "type": ["string", "null"] },
    "repair_applied": {
      "type": ["string", "null"],
      "enum": [null, "truncation", "reformatting", "narration_stripped"],
      "description": "Non-semantic transform only. Semantic content must not be altered (§6.12.2)."
    }
  }
}
```

### Hard suppression patterns (exact-match, Phase 2)

Messages that are exactly or effectively equivalent to these strings are
suppressed as structured no-send results:

- `NO_REPLY`
- `Noted.`
- `Acknowledged.`
- `Nothing to add.`
- `Staying quiet.`
- `Already covered.`
- `Not my task.`
- `I will take a look.`
- `Let me inspect.`
- `Continuing...`

Suppression is supplemented by `message_class` classification: a message
classified as `no_reply` or `acknowledgment` with no `new_facts` and no
`claims` is a suppression candidate even if the exact string differs.

### Semantic firewall (§6.12.2)

The egress governor may perform ONLY these transforms:
1. **Truncation** — enforce hard word limit.
2. **Reformatting** — adjust whitespace, line breaks, or markdown structure.
3. **Narration stripping** — remove tool-progress narration if channel policy
   marks it internal.

It must NOT:
- add new claims, facts, or references not present in the original;
- delete or alter substantive claims;
- rewrite the argument or conclusion;
- insert acknowledgments, greetings, or sign-offs.

---

## Schema 6: LedgerRecord

The durable audit record for every governor decision. Written as JSONL.

```jsonschema
{
  "$id": "https://openclaw.ai/schemas/governor/ledger-record.json",
  "type": "object",
  "required": ["record_id", "timestamp", "kind", "data"],
  "additionalProperties": false,
  "properties": {
    "schema_version": { "const": "1.0.0" },
    "record_id": {
      "type": "string",
      "pattern": "^rec_[a-f0-9]{21}$"
    },
    "timestamp": { "type": "string", "format": "date-time" },
    "kind": {
      "type": "string",
      "enum": ["admission", "egress", "lease_created", "lease_completed", "lease_expired", "thread_state_change", "incident"]
    },
    "data": {
      "type": "object",
      "description": "The full AdmissionDecision, EgressCandidate, ResponseLease, ThreadState, or Incident object."
    }
  }
}
```

### Ledger file layout

```
<workspace>/plugins/conversation-governor/ledger/
  ├── decisions.jsonl     # all admission and egress decisions
  ├── leases.jsonl         # lease lifecycle events
  ├── threads.jsonl        # thread state transitions
  └── incidents.jsonl      # incident records
```

In-process state (Map) is the primary store for active leases and thread
state. The JSONL ledger is the durable audit trail, written on every
transition.

---

## Test fixtures

The following fixtures validate the contract. They live in
`projects/omegahive-conversation-governor/fixtures/` and are used by the
Phase B test suite.

### Fixture 1: retry idempotency

A human message is processed, admitted, and answered. The same message
arrives again (retry). The second event must be dropped with
`DUPLICATE_MESSAGE_ID`.

### Fixture 2: own-message loopback

A bot's outbound message returns through Telegram. The origin chain shows
`bot:protocosmo`. The event must be dropped with `OWN_MESSAGE_LOOPBACK`.

### Fixture 3: sibling not addressed

ProtomegaTron sends a message in the group. ZeroBot is not mentioned. The
event must be dropped with `SIBLING_NOT_ADDRESSED` for ZeroBot's
`before_agent_run`.

### Fixture 4: lease prevents parallel answer

Ben asks a question. ZeroBot claims the lease. ProtomegaTron's
`before_agent_run` fires; the governor must return block with
`LEASE_HELD_BY_OTHER`.

### Fixture 5: visible silence marker suppression (egress)

The model outputs `NO_REPLY`. The egress governor classifies it as
`no_reply` with no claims or facts. The egress decision is `SUPPRESS`.

### Fixture 6: human override bypasses quietness

Ben sends "everyone answer" in the group. Both agents' admission decisions
must include `HUMAN_OVERRIDE_BYPASS` and both may receive active leases.

### Fixture 7: thread closed, no reopen by acknowledgment

A thread is in `CLOSED` state. An acknowledgment message arrives. The
admission decision must be `DROP` with `ACKNOWLEDGMENT_ONLY` and the thread
must remain `CLOSED`.

### Fixture 8: shadow mode is observation-only

All of the above fixtures run with `mode = shadow`. Decisions are recorded
in the ledger but never enforced. The `before_agent_run` hook always
returns `pass`. The `reply_payload_sending` hook always returns the
unmodified payload. The ledger records what *would* have happened.

### Fixture 9: governor cost is recorded

Every admission decision includes a `cost` object with `cpu_ms`,
`model_calls`, and `tokens_used`. In shadow mode, `model_calls` is always
0 (no model calls needed for deterministic checks).

### Fixture 10: semantic firewall — non-semantic repair only

An egress candidate exceeds the hard word limit. The egress governor
truncates it (`repair_applied: "truncation"`). The truncated text must
not add, delete, or alter any claim present in the original.

---

## Open questions for implementation

1. **Project ID resolution.** How to map a `sessionKey` to a `project_id`?
   Options: explicit config mapping, workspace path matching, or omit
   project scope for Phase B and add it in Phase H.
2. **Semantic fingerprint.** Deferred to Phase J. The `content_hash` field
   (SHA-256 of normalized text) is sufficient for Phase B exact dedup.
3. **Lease store.** In-process Map for Phase B–D. A file-based store may
   be needed if the gateway restarts mid-conversation. Defer until
   measured.
4. **Config schema.** The governor plugin will need a `configSchema` with
   `mode` (shadow/active), `feature_flags` per phase, and `thresholds`
   for go/no-go gates. To be defined in Phase D implementation.
