const required = {
  "event-envelope": ["event_id", "event_type", "timestamp", "source", "content", "causality"],
  "admission-decision": ["event_id", "decision", "timestamp", "mode", "reason_codes"],
  "response-lease": ["lease_id", "scope", "holder", "public_slots", "expires_at", "status"],
  "thread-state": ["thread_id", "state", "updated_at"],
  "egress-candidate": ["event_id", "agent_id", "text", "send_intent", "timestamp"],
  "ledger-record": ["record_id", "timestamp", "kind", "data"]
};

const patterns = {
  "event-envelope": { event_id: /^evt_[a-f0-9]{21}$/ },
  "response-lease": { lease_id: /^lease_[a-f0-9]{21}$/ },
  "ledger-record": { record_id: /^rec_[a-f0-9]{21}$/ }
};

export function validate(name, value) {
  const errors = [];
  if (!required[name]) return [`unknown schema: ${name}`];
  if (!value || typeof value !== "object" || Array.isArray(value)) return ["must be an object"];
  for (const key of required[name]) if (!(key in value)) errors.push(`missing required property: ${key}`);
  for (const [key, pattern] of Object.entries(patterns[name] ?? {})) {
    if (key in value && (typeof value[key] !== "string" || !pattern.test(value[key]))) errors.push(`invalid ${key}`);
  }
  if (value.schema_version !== undefined && value.schema_version !== "1.0.0") errors.push("invalid schema_version");
  return errors;
}
