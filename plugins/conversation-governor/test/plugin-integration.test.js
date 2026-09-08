import assert from "node:assert/strict";
import { chmodSync, mkdtempSync, readFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import governorPlugin from "../index.js";

function registerWith(ledgerPath) {
  const handlers = new Map();
  const warnings = [];
  governorPlugin.register({
    pluginConfig: { enabled: true, mode: "active", ledgerPath, agentId: "zero" },
    logger: { warn: (message) => warnings.push(message) },
    on: (name, handler) => handlers.set(name, handler)
  });
  return { handlers, warnings };
}

test("registered active hooks keep admission shadowed and ledger effective egress", () => {
  const ledgerPath = join(mkdtempSync(join(tmpdir(), "governor-hooks-")), "decisions.jsonl");
  const { handlers, warnings } = registerWith(ledgerPath);
  assert.equal(handlers.get("message_received")(
    { messageId: "1", senderId: "ben", content: "hello" },
    { sessionKey: "telegram:test", agentId: "zero" }
  ), undefined);
  assert.equal(handlers.get("message_sending")(
    { content: "NO_REPLY", to: "telegram:test" },
    { channelId: "telegram", conversationId: "test" }
  )?.cancel, true);
  assert.equal(handlers.get("message_sending")(
    { content: "ordinary control", to: "telegram:test" },
    { channelId: "telegram", conversationId: "test" }
  ), undefined);
  const rows = readFileSync(ledgerPath, "utf8").trim().split("\n").map(JSON.parse);
  assert.equal(rows[0].data.decision.mode, "shadow");
  assert.deepEqual(rows.slice(1).map((row) => [row.data.mode, row.data.enforcement_applied]), [
    ["active", true], ["active", false]
  ]);
  assert.deepEqual(warnings, []);
});

test("registered active egress fails open when ledger append fails", () => {
  const directory = mkdtempSync(join(tmpdir(), "governor-hooks-ro-"));
  chmodSync(directory, 0o500);
  const { handlers, warnings } = registerWith(join(directory, "missing", "decisions.jsonl"));
  assert.equal(handlers.get("message_sending")(
    { content: "NO_REPLY", to: "telegram:test" },
    { channelId: "telegram", conversationId: "test" }
  ), undefined);
  assert.equal(warnings.length, 1);
});
