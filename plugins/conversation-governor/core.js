import { createHash } from "node:crypto";

const EXACT_SILENCE = new Set(["NO_REPLY", "NO_RESPONSE"]);

function stable(value) {
  if (Array.isArray(value)) return value.map(stable);
  if (value && typeof value === "object") {
    return Object.fromEntries(Object.keys(value).sort().map((key) => [key, stable(value[key])]));
  }
  return value;
}

export function deterministicId(prefix, value) {
  const digest = createHash("sha256").update(JSON.stringify(stable(value))).digest("hex");
  return `${prefix}_${digest.slice(0, 21)}`;
}

export function normalizeEvent(event = {}, ctx = {}, config = {}) {
  const messageId = String(event.messageId ?? event.message_id ?? ctx.messageId ?? "unknown");
  const sessionKey = String(ctx.sessionKey ?? event.sessionKey ?? "unknown");
  const senderId = String(event.senderId ?? event.sender_id ?? event.from ?? "unknown");
  const senderKind = event.senderKind ?? (config.knownBotIds?.includes(senderId) ? "bot" : "human");
  const eventType = senderKind === "bot" ? "bot_message" : "human_message";
  const content = String(event.prompt ?? event.text ?? event.content ?? "");
  return {
    schema_version: "1.0.0",
    event_id: deterministicId("evt", { sessionKey, messageId, eventType }),
    event_type: eventType,
    timestamp: String(event.timestamp ?? ctx.timestamp ?? new Date(0).toISOString()),
    source: { channel_id: sessionKey, sender_id: senderId, sender_kind: senderKind, message_id: messageId },
    addressing: { explicit_agents: [...(event.explicitAgents ?? [])] },
    content: { text: content, content_hash: `sha256:${createHash("sha256").update(content).digest("hex")}` },
    causality: { origin_chain: [...(event.originChain ?? [`${senderKind}:${senderId}`])] }
  };
}

export function decideAdmission(envelope, snapshot = {}, config = {}) {
  let action = "ALLOW";
  let reason_code = "DEFAULT_ALLOW";
  const key = `${envelope.source.channel_id}:${envelope.source.message_id}:${envelope.event_type}`;
  if (snapshot.seenKeys?.has(key)) {
    action = "DROP";
    reason_code = "DUPLICATE_MESSAGE_ID";
  } else if (envelope.source.sender_kind === "bot" && envelope.source.sender_id === config.agentId) {
    action = "DROP";
    reason_code = "OWN_MESSAGE_LOOPBACK";
  } else if (
    envelope.source.sender_kind === "bot" &&
    config.knownBotIds?.includes(envelope.source.sender_id) &&
    !(envelope.addressing.explicit_agents ?? []).includes(config.agentId)
  ) {
    action = "DROP";
    reason_code = "SIBLING_NOT_ADDRESSED";
  }
  return {
    schema_version: "1.0.0",
    event_id: envelope.event_id,
    timestamp: envelope.timestamp,
    mode: "shadow",
    decision: action === "ALLOW" ? "ADMIT" : "DROP",
    reason_codes: [reason_code],
    public_owner: null,
    private_reviewers: [],
    router_action: null,
    lease_id: null,
    response_contract_id: null,
    cost: { cpu_ms: 0, model_calls: 0, tokens_used: 0 }
  };
}

export function decideEgress(payload) {
  const text = String(payload?.text ?? payload?.message ?? payload ?? "").trim();
  const action = EXACT_SILENCE.has(text) ? "SUPPRESS" : "SEND";
  const reason_code = action === "SUPPRESS" ? "STRUCTURED_SILENCE" : "DEFAULT_SEND";
  return {
    schema_version: "1.0.0",
    event_id: String(payload?.event_id ?? "egress-observation"),
    agent_id: String(payload?.agent_id ?? "unknown"),
    text,
    send_intent: action === "SEND",
    timestamp: String(payload?.timestamp ?? new Date(0).toISOString()),
    mode: "shadow",
    egress_decision: action,
    egress_reason: reason_code,
    repair_applied: null
  };
}

export function applyAdmissionToHook(_decision, mode = "shadow") {
  if (mode !== "shadow") throw new Error("Phase B supports shadow mode only");
  return undefined;
}

export function applyEgressToHook(_decision, _payload, mode = "shadow") {
  if (mode !== "shadow") throw new Error("Phase B supports shadow mode only");
  return undefined;
}
