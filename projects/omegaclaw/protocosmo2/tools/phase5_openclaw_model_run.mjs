#!/usr/bin/env node
/** Tool-free, context-free OpenClaw modelRun adapter for the OmegaClaw bridge. */
import { createHash, randomUUID } from "node:crypto";
import { readdirSync, readFileSync } from "node:fs";
import { pathToFileURL } from "node:url";

const DIST = process.env.OPENCLAW_DIST
  ?? "/home/openclaw/.npm-global/lib/node_modules/openclaw/dist";
const MAX_REQUEST_BYTES = 4_000_000;

function fail() {
  process.stderr.write("raw model gateway call failed\n");
  process.exit(1);
}

async function loadCallGateway() {
  const candidate = readdirSync(DIST)
    .filter((name) => /^call-[A-Za-z0-9_-]+\.js$/.test(name))
    .find((name) => {
      const source = readFileSync(`${DIST}/${name}`, "utf8");
      return source.includes("async function callGateway(opts)")
        && source.includes("callGateway as c");
    });
  if (!candidate) throw new Error("gateway adapter unavailable");
  const module = await import(pathToFileURL(`${DIST}/${candidate}`).href);
  if (typeof module.c !== "function") throw new Error("gateway adapter invalid");
  return module.c;
}

function exactRequest(raw) {
  if (Buffer.byteLength(raw, "utf8") > MAX_REQUEST_BYTES) {
    throw new Error("request too large");
  }
  const request = JSON.parse(raw);
  if (!request || typeof request !== "object" || Array.isArray(request)
      || Object.keys(request).sort().join(",") !== "agent,message,session,timeout_ms") {
    throw new Error("request schema invalid");
  }
  if (typeof request.agent !== "string" || !/^[a-zA-Z0-9_-]{1,128}$/.test(request.agent)
      || typeof request.session !== "string" || !/^[a-zA-Z0-9._:-]{1,256}$/.test(request.session)
      || typeof request.message !== "string" || !request.message.trim()
      || !Number.isInteger(request.timeout_ms)
      || request.timeout_ms < 1_000 || request.timeout_ms > 300_000) {
    throw new Error("request value invalid");
  }
  return request;
}

function requireRawBoundary(response, message) {
  if (!response || response.status !== "ok" || response.summary !== "completed"
      || !response.result || !Array.isArray(response.result.payloads)
      || response.result.payloads.length !== 1
      || typeof response.result.payloads[0]?.text !== "string") {
    throw new Error("model response invalid");
  }
  const agentMeta = response.result.meta?.agentMeta;
  const report = response.result.meta?.systemPromptReport;
  if (!agentMeta || typeof agentMeta.provider !== "string"
      || typeof agentMeta.model !== "string" || !report
      || report.systemPrompt?.chars !== 0
      || report.systemPrompt?.projectContextChars !== 0
      || report.systemPrompt?.nonProjectContextChars !== 0
      || report.tools?.listChars !== 0 || report.tools?.schemaChars !== 0
      || !Array.isArray(report.tools?.entries) || report.tools.entries.length !== 0
      || !Array.isArray(report.injectedWorkspaceFiles)
      || report.injectedWorkspaceFiles.length !== 0
      || report.currentTurn?.runtimeContextChars !== 0
      || agentMeta.contextBudgetStatus?.messageCount !== 0
      || response.result.meta?.finalPromptText !== message) {
    throw new Error("raw model boundary invalid");
  }
  return {
    result: {
      payloads: response.result.payloads,
      meta: {
        agentMeta: {
          provider: agentMeta.provider,
          model: agentMeta.model,
          rawModelBoundary: {
            systemPromptChars: 0,
            toolListChars: 0,
            toolSchemaChars: 0,
            messageCount: 0,
          },
        },
      },
    },
  };
}

try {
  const request = exactRequest(readFileSync(0, "utf8"));
  const callGateway = await loadCallGateway();
  const idempotencyKey = createHash("sha256")
    .update(`${request.agent}\0${request.session}\0${randomUUID()}`)
    .digest("hex");
  const response = await callGateway({
    method: "agent",
    params: {
      agentId: request.agent,
      sessionId: request.session,
      sessionKey: `agent:${request.agent}:explicit:${request.session}`,
      message: request.message,
      thinking: "off",
      modelRun: true,
      promptMode: "none",
      cleanupBundleMcpOnRunEnd: true,
      idempotencyKey,
    },
    expectFinal: true,
    timeoutMs: request.timeout_ms,
  });
  process.stdout.write(JSON.stringify(requireRawBoundary(response, request.message)));
} catch (error) {
  const name = typeof error?.name === "string" ? error.name : "Error";
  const message = typeof error?.message === "string" ? error.message : "unknown failure";
  process.stderr.write(`raw model gateway call failed: ${name}: ${message}\n`);
  process.exit(1);
}
