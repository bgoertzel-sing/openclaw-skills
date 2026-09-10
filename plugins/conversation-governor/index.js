import { homedir } from "node:os";
import { resolve } from "node:path";
import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";
import {
  applyAdmissionToHook,
  applyEgressToHook,
  admissionEnforcementMode,
  admissionIdentityKey,
  decideAdmission,
  decideEgress,
  normalizeEvent,
  recordEgressEnforcement
} from "./core.js";
import { appendLedgerRecord } from "./ledger.js";
import { deterministicId } from "./core.js";

function configOf(raw = {}) {
  return {
    ...raw,
    mode: raw.mode ?? "shadow",
    ledgerPath: String(raw.ledgerPath ?? "~/research-agent/plugins/conversation-governor/ledger/decisions.jsonl")
      .replace(/^~/, homedir())
  };
}

export default definePluginEntry({
  id: "conversation-governor",
  name: "Conversation Governor",
  description: "Shadow-only deterministic conversation governance.",
  register(api) {
    const seenKeys = new Set();
    // message_received retains the immutable transport envelope (messageId,
    // senderId, canonical sessionKey) that before_agent_run does not expose.
    // This remains an observation-only hook; active admission needs its own
    // later inbound_claim gate and approval.
    api.on("message_received", (event, ctx) => {
      const config = configOf(api.pluginConfig);
      if (config.enabled === false) return;
      try {
        const runtimeConfig = { ...config, agentId: ctx.agentId ?? config.agentId };
        const envelope = normalizeEvent(event, ctx, runtimeConfig);
        const decision = decideAdmission(envelope, { seenKeys }, runtimeConfig);
        const key = admissionIdentityKey(envelope);
        if (key !== null) seenKeys.add(key);
        const timestamp = new Date().toISOString();
        appendLedgerRecord(resolve(config.ledgerPath), {
          schema_version: "1.0.0", record_id: deterministicId("rec", { kind: "admission", event_id: envelope.event_id, timestamp }),
          timestamp, kind: "admission", data: { envelope, decision }
        });
        // E1a activates only the outbound slice. Admission remains explicitly
        // shadowed even when config.mode is "active" for egress.
        return applyAdmissionToHook(decision, admissionEnforcementMode());
      } catch (error) {
        api.logger.warn?.(`conversation-governor shadow admission failed open: ${error?.message ?? "unknown error"}`);
        return undefined;
      }
    }, { priority: 90, timeoutMs: 100 });

    // message_sending is the common outbound seam for interactive replies,
    // cron announce delivery, message-tool sends, and direct subagent posts.
    api.on("message_sending", (event, ctx) => {
      const config = configOf(api.pluginConfig);
      if (config.enabled === false) return;
      try {
        const decision = decideEgress({
          content: event.content,
          event_id: deterministicId("evt", {
            channel: ctx.channelId,
            account: ctx.accountId ?? "default",
            conversation: ctx.conversationId ?? event.to,
            session: ctx.sessionKey ?? "direct-post",
            content: event.content
          }),
          agent_id: config.agentId ?? "unknown",
          timestamp: new Date().toISOString()
        }, config.mode);
        const hookResult = applyEgressToHook(decision, event, config.mode);
        const recordedDecision = recordEgressEnforcement(decision, hookResult);
        const timestamp = new Date().toISOString();
        appendLedgerRecord(resolve(config.ledgerPath), {
          schema_version: "1.0.0", record_id: deterministicId("rec", { kind: "egress", event_id: decision.event_id, timestamp }),
          timestamp, kind: "egress", data: recordedDecision
        });
        return hookResult;
      } catch (error) {
        api.logger.warn?.(`conversation-governor egress failed open: ${error?.message ?? "unknown error"}`);
        return undefined;
      }
    }, { priority: 90, timeoutMs: 100 });
  }
});

export * from "./core.js";
export * from "./ledger.js";
