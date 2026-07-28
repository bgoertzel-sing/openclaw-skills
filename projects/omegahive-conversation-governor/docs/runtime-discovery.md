# Phase A: Runtime and Repository Discovery

Date: 2026-07-24
Status: complete
Acceptance: identifies inbound dispatch, router, outbound-send, event-ID, and persistence seams without changing runtime behavior.

## Installed runtime

- OpenClaw `2026.7.1` (commit `2d2ddc4`), installed at `/home/openclaw/.npm-global/lib/node_modules/openclaw/`.
- Gateway mode: `local`, port 18789, loopback bind.
- Config: `~/.openclaw/openclaw.json` (JSON5, hot-reloaded by gateway).

## Agent topology

All four agents are configured in the same `openclaw.json` and share one gateway instance:

| Agent ID | Workspace | Model |
|---|---|---|
| `main` (ZeroBot/ProtoCosmoBot) | `~/research-agent` | `openrouter/moonshotai/kimi-k3` (default) |
| `protomegabot-simple` | `~/research-agent/projects/omegaclaw/workspace` | `openrouter/moonshotai/kimi-k3` |
| `protomegabot-opus` | same omegaclaw workspace | kimi-k3 → gpt-5.6-terra → glm-5.2 |
| `protomegabot-fable` | same omegaclaw workspace | kimi-k3 |

**Critical finding:** OmegaClaw agents (protomegabot-*) are separate agent IDs in the same gateway, not external processes. They share the same plugin event pipeline. This confirms the design premise: a shared pre-inference seam exists at the plugin hook layer.

## Plugin hook surface

The full ordered plugin hook lifecycle (from `hook-types-DQ9eTy2x.d.ts`):

### Inbound path (pre-inference)

1. **`inbound_claim`** — earliest point. Channel-agnostic; receives content, sender, conversation, thread, session key. Can claim or reject messages.
2. **`message_received`** — after claim, before agent run. Has `from`, `content`, `sessionKey`, `runId`, `messageId`, `replyToId`, `replyToBody`, `replyToSender`.
3. **`before_agent_run`** — **input gate**. Receives `prompt`, `messages`, `systemPrompt`, `channelId`, `senderId`, `senderIsOwner`. Returns `InputGateDecision` (`pass` or `block`). This is the admission gate the governor needs.
4. **`before_model_resolve`** — model selection. Receives `prompt` and `attachments`. Returns `providerOverride`/`modelOverride`. Currently used by `intent-model-router`.
5. **`before_prompt_build`** — receives `prompt` and `messages`. Can inject `prependContext`, `appendContext`, `prependSystemContext`, `appendSystemContext`.

### Agent runtime (inference)

6. **`agent_turn_prepare`** — before LLM call.
7. **`before_agent_reply`** — receives `cleanedBody`. Can modify the reply text.
8. **`llm_input`** — before model call. Has `sessionKey`, `runId`.
9. **`llm_output`** — after model call. Has `usage`, `resolvedRef`, `provider`, `model`, `runId`. Currently used by `intent-model-router` for cost tracking.
10. **`before_agent_finalize`** — can `continue`, `revise` (retry with instruction), or `finalize`.
11. **`agent_end`** — run complete. Has `runId`, `messages`, `success`, `error`, `durationMs`.

### Outbound path (post-inference)

12. **`reply_payload_sending`** — before delivery. Receives `payload`, `kind` (`tool`/`block`/`final`), `channel`, `sessionKey`, `runId`. Returns `{ cancel?, reason?, payload? }`. **This is the egress gate.**
13. **`message_sending`** — before channel send. Receives `to`, `content`, `replyToId`, `threadId`. Returns `{ cancel?, cancelReason?, content? }`.
14. **`message_sent`** — after delivery. Receives `to`, `content`, `success`, `messageId`, `sessionKey`, `runId`.

### Other relevant hooks

- **`session_start` / `session_end`** — session lifecycle.
- **`before_dispatch` / `reply_dispatch`** — dispatch pipeline.
- **`gateway_start` / `gateway_stop`** — gateway lifecycle.
- **`heartbeat_prompt_contribution`** — heartbeat/cron prompt augmentation.
- **`cron_changed`** — cron job lifecycle.
- **`subagent_spawned` / `subagent_ended`** — subagent lifecycle.

## Existing plugins and integrations

### `intent-model-router` (workspace plugin)

Location: `~/research-agent/plugins/intent-model-router/`

Hooks used:
- `before_model_resolve` (priority 100) — classifies prompt into routine/semi-routine/deep/fable, overrides model.
- `reply_payload_sending` (priority 100) — suppresses false fallback notices from intentional routing.
- `llm_output` (priority 0) — logs cost/usage to JSONL.

Classification: regex-based keyword matching. Has OmegaClaw-specific path (`classifyOmegaClawPrompt`). `fixedAgentIds` prevents router from overriding OmegaClaw agent models.

This is the **existing extended smart router** from the design doc. The governor's `DROP|LOG_ONLY|TEMPLATE|CHEAP_MODEL|NORMAL_MODEL|DEEP_MODEL` action space is a superset of what this router does.

### `thread-ownership` (built-in extension)

Slack-specific thread claim coordination. Hooks: `message_received`, `message_sending`. Not currently active for Telegram. Demonstrates the pattern for ownership-based routing.

### `inbound-dedupe` (built-in)

Internal deduplication module (`inbound-dedupe-ySEx5MpS.js`). Provides `resetInboundDedupe()`. This is an existing deterministic dedup seam.

## Key seams for governor integration

### 1. Admission gate: `before_agent_run`

This is the primary pre-inference checkpoint. It receives the prompt, messages, channel, and sender. It returns `pass` or `block`. A governor plugin can hook here to:
- drop events that should never reach inference (own-message echoes, sibling acknowledgments, duplicate system events);
- record admission decisions to a ledger;
- assign response ownership;
- enforce response leases.

**Limitation:** The `before_agent_run` hook fires per-agent-run. For shared decisions (e.g., "only one agent should answer"), the governor needs shared state (a ledger or cache) readable across hook invocations. Since all agents share one gateway process, an in-process Map or file-based ledger is sufficient.

### 2. Egress gate: `reply_payload_sending`

This fires before any reply is delivered. Returns `{ cancel?, reason? }`. A governor plugin can hook here to:
- suppress no-op outputs (NO_REPLY, bare acknowledgments);
- enforce response contracts (required sections, length limits);
- detect semantic duplicates against recent messages;
- ensure the sender holds an active response lease.

### 3. Model routing: `before_model_resolve`

Already occupied by `intent-model-router`. The governor should not replace this hook but coordinate with it — the governor decides *whether* to invoke, and the router decides *which model*. The governor's `DROP` action maps to `before_agent_run` block; `LOG_ONLY` maps to block + log; `TEMPLATE` maps to a pre-inference shortcut.

### 4. Event identity: `runId` + `sessionKey` + `messageId`

- `runId`: per-turn UUID, stable across retries and multi-payload replies. Generated in `agent-runner-execution.ts` via `crypto.randomUUID()`.
- `sessionKey`: canonical conversation key, same across all hooks for one conversation.
- `messageId`: channel message ID (e.g., Telegram message ID).

These provide the idempotency keys the design doc needs. The governor can key on `(sessionKey, runId)` for per-turn dedup and `(sessionKey, messageId)` for per-event dedup.

**Limitation:** `runId` is not yet plumbed through the outbound delivery path (`message_sending`/`message_sent`). Cross-agent correlation via `runId` is not possible for outbound hooks today; use `sessionKey` for outbound→inbound correlation.

### 5. Inbound context: `PluginHookInboundClaimEvent` / `PluginHookMessageReceivedEvent`

These carry sender identity (`senderId`, `senderName`), reply context (`replyToId`, `replyToBody`, `replyToSender`, `replyToIsQuote`), thread context (`threadId`), and conversation identity (`conversationId`, `parentConversationId`). Sufficient for the event normalization envelope in the design doc.

### 6. Agent identity: `agentId` in context

The hook context (`PluginHookAgentContext`) includes `agentId`, `sessionKey`, `channelId`, `senderId`. The governor can determine which agent is processing and whether it's the designated public owner.

## Placement decision

**Confirmed:** A shared pre-inference seam exists. All four agents share one gateway, one plugin pipeline, and one hook lifecycle. A single governor plugin hooking `before_agent_run` and `reply_payload_sending` can observe and gate all agents.

**Implementation target:** A new workspace plugin at `~/research-agent/plugins/conversation-governor/` using `definePluginEntry`. It will:
- hook `before_agent_run` for admission (shadow mode first);
- hook `reply_payload_sending` for egress observation;
- hook `llm_output` for cost/usage correlation (optional, for governor overhead metric);
- maintain an in-process ledger (Map) and optionally a JSONL audit log;
- coordinate with `intent-model-router` by running at a different priority.

No fallback topology (per-agent local governors) is needed at this time.

## Open findings for Phase B

1. The `before_agent_run` hook can `block` but cannot redirect to a different agent. The governor can suppress an agent's run but cannot reassign ownership to another agent within the hook. Ownership must be resolved before the run starts, or by suppressing non-owner agents and letting the owner proceed.
2. No built-in cross-agent response lease mechanism exists. The governor must implement leases in shared in-process state.
3. The `reply_payload_sending` hook can `cancel` and modify `payload`, which is sufficient for egress suppression and non-semantic repair (truncation, reformatting).
4. Telegram group messages currently set `requireMention: false` for the main Protobots group, meaning ZeroBot processes every message. The governor can apply deterministic drop conditions here.
5. The `intent-model-router` already has cost tracking infrastructure (`usage.jsonl`) that the governor can reuse for the governor-overhead metric.
