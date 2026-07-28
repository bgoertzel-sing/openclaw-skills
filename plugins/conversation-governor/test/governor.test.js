import assert from "node:assert/strict";
import { mkdtempSync, readFileSync, readdirSync, statSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import {
  applyAdmissionToHook,
  applyEgressToHook,
  decideAdmission,
  decideEgress,
  normalizeEvent
} from "../core.js";
import { appendLedgerRecord } from "../ledger.js";
import { validate } from "../schema.js";

const config = { agentId: "zero", knownBotIds: ["zero", "omega"] };

test("normalization and IDs are deterministic", () => {
  const input = { messageId: 7, senderId: "ben", text: "hello" };
  assert.deepEqual(normalizeEvent(input, { sessionKey: "telegram:group" }, config),
    normalizeEvent(input, { sessionKey: "telegram:group" }, config));
});

test("retry, own loopback, and unaddressed sibling are counterfactually dropped", () => {
  const human = normalizeEvent({ messageId: 7, senderId: "ben" }, { sessionKey: "s" }, config);
  const key = "s:7:human_message";
  assert.equal(decideAdmission(human, { seenKeys: new Set([key]) }, config).reason_codes[0], "DUPLICATE_MESSAGE_ID");
  const own = normalizeEvent({ messageId: 8, senderId: "zero", senderKind: "bot" }, { sessionKey: "s" }, config);
  assert.equal(decideAdmission(own, {}, config).reason_codes[0], "OWN_MESSAGE_LOOPBACK");
  const sibling = normalizeEvent({ messageId: 9, senderId: "omega", senderKind: "bot" }, { sessionKey: "s" }, config);
  assert.equal(decideAdmission(sibling, {}, config).reason_codes[0], "SIBLING_NOT_ADDRESSED");
});

test("explicitly addressed sibling is allowed", () => {
  const event = normalizeEvent({ messageId: 9, senderId: "omega", senderKind: "bot", explicitAgents: ["zero"] }, { sessionKey: "s" }, config);
  assert.equal(decideAdmission(event, {}, config).decision, "ADMIT");
});

test("exact silence is counterfactually suppressed but substrings are sent", () => {
  assert.equal(decideEgress({ text: "NO_REPLY" }).egress_decision, "SUPPRESS");
  assert.equal(decideEgress({ text: "The token NO_REPLY is documented." }).egress_decision, "SEND");
});

test("shadow adapters never block, cancel, or mutate", () => {
  const payload = { text: "NO_REPLY", nested: { n: 1 } };
  const before = structuredClone(payload);
  assert.equal(applyAdmissionToHook({ action: "DROP" }), undefined);
  assert.equal(applyEgressToHook({ action: "SUPPRESS" }, payload), undefined);
  assert.deepEqual(payload, before);
  assert.throws(() => applyAdmissionToHook({}, "active"), /shadow mode only/);
});

test("ledger is private JSONL", () => {
  const path = join(mkdtempSync(join(tmpdir(), "governor-")), "decisions.jsonl");
  appendLedgerRecord(path, { kind: "test", content_sha256: "abc" });
  assert.deepEqual(JSON.parse(readFileSync(path, "utf8")), { kind: "test", content_sha256: "abc" });
  assert.equal(statSync(path).mode & 0o077, 0);
});

test("all ten canonical fixtures validate against their intended schemas", () => {
  const fixtures = new URL("../fixtures/", import.meta.url);
  const names = readdirSync(fixtures).filter((name) => name.endsWith(".json"));
  assert.equal(names.length, 10);
  for (const name of names) {
    const fixture = JSON.parse(readFileSync(new URL(name, fixtures), "utf8"));
    if (fixture.event) assert.deepEqual(validate("event-envelope", fixture.event), [], name);
    if (fixture.lease) assert.deepEqual(validate("response-lease", fixture.lease), [], name);
    if (fixture.thread) assert.deepEqual(validate("thread-state", fixture.thread), [], name);
    if (fixture.candidate?.event_id) assert.deepEqual(validate("egress-candidate", fixture.candidate), [], name);
    if (fixture.decision) assert.deepEqual(validate("admission-decision", fixture.decision), [], name);
  }
});

test("schemas reject missing required data and bad deterministic IDs", () => {
  assert.match(validate("event-envelope", { event_id: "bad" }).join(" "), /missing required property/);
  assert.match(validate("ledger-record", { record_id: "bad", timestamp: "t", kind: "admission", data: {} }).join(" "), /invalid record_id/);
});
