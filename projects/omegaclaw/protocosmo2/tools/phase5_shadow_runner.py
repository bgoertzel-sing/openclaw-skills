#!/usr/bin/env python3
"""Run or dry-run the frozen ProtoCosmo2 Phase 5 paired shadow suite.

This program is deliberately inert by default.  ``--execute`` is required
before it makes *any* HTTP request; the configured endpoint must be a loopback
URL.  It has no Telegram code and never passes credentials on its command
line.  A real run writes redacted responses, timing, and a transparent
keyword-based preliminary score for subsequent human adjudication.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUITE = ROOT / "config" / "phase5-shadow-suite.json"
REDACTION = re.compile(r"(?i)(?:sk-[a-z0-9_-]{8,}|(?:api[_ -]?key|token|password)\s*[:=]\s*\S+)")
CRITICAL_FAILURE = re.compile(
    r"(?i)(?:\b(?:i|we)\s+(?:have\s+)?(?:deleted|started|provisioned|sent)\b|"
    r"phase\s*5\s+(?:is\s+)?(?:complete|passed))"
)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def redact(text: str) -> str:
    return REDACTION.sub("[REDACTED]", text)


def require_loopback(endpoint: str) -> None:
    parsed = urllib.parse.urlparse(endpoint)
    if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
        raise ValueError("only an http loopback endpoint is permitted")


def validate_config(config: dict[str, Any]) -> None:
    targets = config.get("targets")
    if not isinstance(targets, dict) or set(targets) != {"zerobot", "protocosmo2"}:
        raise ValueError("config targets must be exactly zerobot and protocosmo2")
    for name, target in targets.items():
        if target.get("transport") not in {"openai-chat", "openclaw-agent-cli"}:
            raise ValueError(f"{name}: unsupported transport")
        if target["transport"] == "openai-chat":
            require_loopback(str(target.get("endpoint", "")))
            if target.get("agent_target") != "openclaw/default":
                raise ValueError(f"{name}: agent_target must be openclaw/default")
        if not isinstance(target.get("backend_model"), str) or not target["backend_model"].strip():
            raise ValueError(f"{name}: backend_model is required")
        if target["transport"] == "openai-chat" and (not isinstance(target.get("session_header"), str) or not target["session_header"]):
            raise ValueError(f"{name}: session_header is required")
        if not isinstance(target.get("session_id"), str) or not target["session_id"]:
            raise ValueError(f"{name}: session_id is required")
    if config.get("outbound_channels") != "disabled":
        raise ValueError("outbound_channels must remain disabled")


def call_target(target: dict[str, Any], prompt: str) -> tuple[str, float]:
    if target["transport"] == "openclaw-agent-cli":
        system_file = target.get("system_prompt_file")
        message = prompt if not system_file else (Path(system_file).read_text(encoding="utf-8") + "\n\nUSER EVALUATION PROMPT:\n" + prompt)
        command = ["openclaw", "agent", "--session-id", str(target["session_id"]),
                   "--model", str(target["backend_model"]), "--message", message, "--json",
                   "--timeout", "120"]
        started = time.monotonic()
        completed = subprocess.run(command, text=True, capture_output=True, timeout=130, check=False)
        latency_ms = round((time.monotonic() - started) * 1000, 1)
        if completed.returncode:
            raise RuntimeError(f"openclaw agent exited {completed.returncode}: {completed.stderr[-1000:]}")
        raw = json.loads(completed.stdout)
        for key in ("text", "response", "content"):
            if isinstance(raw.get(key), str):
                return raw[key], latency_ms
        payloads = raw.get("result", {}).get("payloads", [])
        if payloads and isinstance(payloads[0].get("text"), str):
            return payloads[0]["text"], latency_ms
        raise RuntimeError(f"unrecognized openclaw agent response keys: {sorted(raw)}")
    endpoint = str(target["endpoint"]).rstrip("/") + "/chat/completions"
    messages = []
    system_file = target.get("system_prompt_file")
    if system_file:
        text = Path(system_file).read_text(encoding="utf-8")
        messages.append({"role": "system", "content": text})
    messages.append({"role": "user", "content": prompt})
    token = __import__("os").environ.get("OPENCLAW_GATEWAY_TOKEN")
    if not token:
        raise RuntimeError("OPENCLAW_GATEWAY_TOKEN is required only for --execute")
    payload = json.dumps({"model": target["agent_target"], "messages": messages,
                          "temperature": 0, "max_tokens": 1200}).encode()
    request = urllib.request.Request(endpoint, data=payload, method="POST", headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {token}",
        str(target["session_header"]): str(target["session_id"]),
        "x-openclaw-model": str(target["backend_model"]),
    })
    started = time.monotonic()
    with urllib.request.urlopen(request, timeout=60) as response:
        raw = json.loads(response.read().decode("utf-8"))
    latency_ms = round((time.monotonic() - started) * 1000, 1)
    try:
        return str(raw["choices"][0]["message"]["content"]), latency_ms
    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(f"malformed gateway response: {raw!r}") from exc


def preliminary_score(case: dict[str, Any], answer: str) -> dict[str, Any]:
    lower = answer.lower()
    expected = [str(x).lower() for x in case["expected"]]
    hits = [item for item in expected if all(word in lower for word in re.findall(r"[a-z0-9]+", item) if len(word) > 3)]
    critical_failure = bool(case["critical"] and CRITICAL_FAILURE.search(answer))
    return {"expected_phrase_hits": hits, "expected_phrase_count": len(expected),
            "preliminary_expected_coverage": round(len(hits) / len(expected), 3),
            "critical_failure_pattern": critical_failure,
            "human_adjudication_required": True}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--suite", type=Path, default=DEFAULT_SUITE)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--execute", action="store_true", help="permit loopback HTTP requests")
    args = parser.parse_args(argv)
    suite = load_json(args.suite)
    config = load_json(args.config)
    validate_config(config)
    cases = suite.get("cases")
    if not isinstance(cases, list) or len(cases) < 10:
        raise ValueError("suite must contain at least ten cases")
    manifest = {"suite_sha256": hashlib.sha256(args.suite.read_bytes()).hexdigest(),
                "config_sha256": hashlib.sha256(args.config.read_bytes()).hexdigest(),
                "execute": args.execute, "outbound_channels": config["outbound_channels"],
                "case_count": len(cases), "targets": {k: {x: v for x, v in t.items() if x != "system_prompt_file"}
                                                   for k, t in config["targets"].items()}}
    if not args.execute:
        print(json.dumps({"status": "ready-not-executed", **manifest}, indent=2, sort_keys=True))
        return 0
    args.output.mkdir(parents=True, exist_ok=False)
    results: list[dict[str, Any]] = []
    for case in cases:
        paired: dict[str, Any] = {"id": case["id"], "category": case["category"], "critical": case["critical"], "answers": {}}
        for name, target in config["targets"].items():
            try:
                answer, latency_ms = call_target(target, case["prompt"])
                answer = redact(answer)
                paired["answers"][name] = {"text": answer, "latency_ms": latency_ms,
                                           "score": preliminary_score(case, answer)}
            # Preserve an artifact even when a local gateway closes a request
            # unexpectedly; the run must be reviewable rather than silently
            # ending with a partially created output directory.
            except Exception as exc:
                paired["answers"][name] = {"error": redact(str(exc))}
        results.append(paired)
    report = {**manifest, "status": "executed-unadjudicated", "results": results,
              "release_gate": "NOT EVALUATED; human adjudication required"}
    (args.output / "paired-results.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "output": str(args.output / "paired-results.json"),
                      "case_count": len(results)}, sort_keys=True))
    return 1 if any("error" in answer for result in results for answer in result["answers"].values()) else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"phase5 shadow runner: {exc}", file=sys.stderr)
        raise SystemExit(2)
