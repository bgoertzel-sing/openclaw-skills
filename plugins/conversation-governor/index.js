import { homedir } from "node:os";
import { resolve } from "node:path";
import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";
import {
  applyAdmissionToHook,
  applyEgressToHook,
  decideAdmission,
  decideEgress,
  normalizeEvent
} from "./core.js";
import { appendLedgerRecord } from "./ledger.js";
import { deterministicId } from "./core.js";

function configOf(raw = {}) {
  return {
    ...raw,
    mode: "shadow",
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
    api.on("before_agent_run", (event, ctx) => {
      const config = configOf(api.pluginConfig);
      if (config.enabled === false) return;
      try {
        const runtimeConfig = { ...config, agentId: ctx.agentId ?? config.agentId };
        const envelope = normalizeEvent(event, ctx, runtimeConfig);
        const decision = decideAdmission(envelope, { seenKeys }, runtimeConfig);
        const key = `${envelope.source.channel_id}:${envelope.source.message_id}:${envelope.event_type}`;
        seenKeys.add(key);
        const timestamp = new Date().toISOString();
        appendLedgerRecord(resolve(config.ledgerPath), {
          schema_version: "1.0.0", record_id: deterministicId("rec", { kind: "admission", event_id: envelope.event_id, timestamp }),
          timestamp, kind: "admission", data: { envelope, decision }
        });
        return applyAdmissionToHook(decision, config.mode);
      } catch (error) {
        api.logger.warn?.(`conversation-governor shadow admission failed open: ${error?.message ?? "unknown error"}`);
        return undefined;
      }
    }, { priority: 90, timeoutMs: 100 });

    api.on("reply_payload_sending", (event) => {
      const config = configOf(api.pluginConfig);
      if (config.enabled === false) return;
      try {
        const decision = decideEgress(event.payload);
        const timestamp = new Date().toISOString();
        appendLedgerRecord(resolve(config.ledgerPath), {
          schema_version: "1.0.0", record_id: deterministicId("rec", { kind: "egress", event_id: decision.event_id, timestamp }),
          timestamp, kind: "egress", data: decision
        });
        return applyEgressToHook(decision, event.payload, config.mode);
      } catch (error) {
        api.logger.warn?.(`conversation-governor shadow egress failed open: ${error?.message ?? "unknown error"}`);
        return undefined;
      }
    }, { priority: 90, timeoutMs: 100 });
  }
});

export * from "./core.js";
export * from "./ledger.js";
