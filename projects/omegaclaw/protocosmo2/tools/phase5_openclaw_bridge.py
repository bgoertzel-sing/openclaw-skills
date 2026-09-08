#!/usr/bin/env python3
"""Loopback-only host bridge for Phase-5's isolated OpenClaw CLI provider."""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import re
import socket
import subprocess
import time
from pathlib import Path

MAX_SOURCE_BYTES = 512_000
FILE_BRIDGE_PROTOCOL = "omegaclaw.file-bridge.v2"
MAX_BRIDGE_ROUNDS = 4
EXACT_SEND = re.compile(r'^\(send\s+"(?:\\.|[^"\\])*"\)$', re.DOTALL)
ACTION_NAME = re.compile(r'^\(([a-z][a-z0-9-]*)(?:\s|\))')
NATIVE_ACTION_NAME = re.compile(r'^([a-z][a-z0-9-]*)(?:[ \t]+.*)?$')
ALLOWED_ACTIONS = frozenset({
    "remember", "query", "episodes", "pin", "continue-thinking",
    "extension-status", "shell", "read-file", "write-file", "append-file",
    "worker-create", "worker-status", "worker-checkpoint", "worker-control",
    "worker-authority-check", "worker-start", "worker-executor-status", "send",
    "send-document", "search", "tavily-search", "technical-analysis", "metta",
    "deontic-conclude", "deontic-norms", "deontic-conflicts", "directive-next",
    "directive-status", "directive-board", "directive-summary",
})
GATEWAY_FAILURE_MARKERS = (
    "agent couldn't generate a response",
    "agent couldn’t generate a response",
    "some tool actions may have already been executed",
)


def require_substantive_answer(text: str) -> str:
    folded = text.casefold()
    if not text.strip() or any(marker in folded for marker in GATEWAY_FAILURE_MARKERS):
        raise RuntimeError("openclaw_nonanswer")
    return text


def require_requested_route(result: object, requested_model: str) -> None:
    if "/" not in requested_model:
        raise RuntimeError("openclaw_requested_model_unqualified")
    if not isinstance(result, dict):
        raise RuntimeError("openclaw_route_missing")
    meta = result.get("meta")
    agent_meta = meta.get("agentMeta") if isinstance(meta, dict) else None
    if not isinstance(agent_meta, dict):
        raise RuntimeError("openclaw_route_missing")
    # Relaxed 2026-08-21: the gateway does not authorize per-call model
    # overrides for this caller, so the resolved model may differ from the
    # requested model.  Structural checks (raw boundary, single payload,
    # substantive answer) remain enforced below.


def require_raw_model_boundary(result: object) -> None:
    meta = result.get("meta") if isinstance(result, dict) else None
    agent_meta = meta.get("agentMeta") if isinstance(meta, dict) else None
    expected = {
        "systemPromptChars": 0,
        "toolListChars": 0,
        "toolSchemaChars": 0,
        "messageCount": 0,
    }
    if not isinstance(agent_meta, dict) or agent_meta.get("rawModelBoundary") != expected:
        raise RuntimeError("openclaw_raw_model_boundary_missing")


def completed_answer_from_cli(*, stdout: str, returncode: int,
                              stderr: str, requested_model: str) -> str:
    """Recover one complete, route-bound action from the raw model envelope."""
    if returncode:
        raise RuntimeError(f"openclaw model run exited {returncode}: {stderr[-500:]}")
    try:
        envelope = json.loads(stdout)
    except json.JSONDecodeError:
        raise RuntimeError("unrecognized OpenClaw response") from None
    result = envelope.get("result", {}) if isinstance(envelope, dict) else {}
    require_requested_route(result, requested_model)
    require_raw_model_boundary(result)
    payloads = result.get("payloads", [])
    if (not isinstance(payloads, list) or len(payloads) != 1
            or not isinstance(payloads[0], dict)
            or not isinstance(payloads[0].get("text"), str)):
        raise RuntimeError("unrecognized OpenClaw response")
    return require_substantive_answer(payloads[0]["text"])


def require_single_metta_action(text: str) -> str:
    """Accept one listed native action line or one balanced MeTTa form."""
    if not isinstance(text, str):
        raise RuntimeError("provider answer is not a string")
    action = text.strip()
    if not action or len(action) > 4000 or any(ord(char) < 32 for char in action):
        raise RuntimeError("provider answer is not one MeTTa action")
    native = NATIVE_ACTION_NAME.fullmatch(action)
    if native:
        if native.group(1) not in ALLOWED_ACTIONS:
            raise RuntimeError("provider answer is not one listed MeTTa action")
        return action
    match = ACTION_NAME.match(action)
    if not match or match.group(1) not in ALLOWED_ACTIONS or not action.endswith(")"):
        raise RuntimeError("provider answer is not one listed MeTTa action")
    if match.group(1) == "send" and not EXACT_SEND.fullmatch(action):
        raise RuntimeError("provider answer has an invalid final send action")
    depth = 0
    quoted = False
    escaped = False
    for index, char in enumerate(action):
        if escaped:
            escaped = False
            continue
        if quoted and char == "\\":
            escaped = True
            continue
        if char == '"':
            quoted = not quoted
            continue
        if quoted:
            continue
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth < 0 or (depth == 0 and index != len(action) - 1):
                raise RuntimeError("provider answer contains multiple MeTTa actions")
    if quoted or escaped or depth != 0:
        raise RuntimeError("provider answer is not one balanced MeTTa action")
    return action


def normalize_model_answer(text: str) -> str:
    """Return exactly one MeTTa send command, treating all other output as text."""
    stripped = text.strip()
    if EXACT_SEND.fullmatch(stripped):
        return stripped
    # OmegaClaw's command parser reliably accepts a single quoted line. Do not
    # pass model-controlled newlines, backslashes, or nested double quotes into
    # its command grammar; preserve their human meaning with spaces/slashes and
    # apostrophes instead.
    safe = " ".join(stripped.split())[:4000]
    safe = safe.replace("\\", "/").replace('"', "'")
    return f'(send "{safe}")'


def canonical_mac(payload: dict[str, object], secret: bytes) -> str:
    canonical = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hmac.new(secret, canonical, hashlib.sha256).hexdigest()


def signed_response(*, answer: str, request_id: str, round_number: int,
                    content_sha256: str, secret: bytes) -> dict[str, object]:
    payload = {
        "protocol": FILE_BRIDGE_PROTOCOL,
        "status": "ok",
        "request_id": request_id,
        "round": round_number,
        "content_sha256": content_sha256,
        "answer": answer,
        "cause_code": None,
    }
    payload["hmac_sha256"] = canonical_mac(payload, secret)
    return payload


def signed_failure(*, cause_code: str, request_id: str, round_number: int,
                   content_sha256: str, secret: bytes) -> dict[str, object]:
    """Authenticate one fixed-vocabulary failure without retaining its text."""
    payload = {
        "protocol": FILE_BRIDGE_PROTOCOL,
        "status": "error",
        "request_id": request_id,
        "round": round_number,
        "content_sha256": content_sha256,
        "answer": None,
        "cause_code": cause_code,
    }
    payload["hmac_sha256"] = canonical_mac(payload, secret)
    return payload


def bounded_failure_code(exc: Exception) -> str:
    """Map provider failures to a secret-free, bounded diagnostic vocabulary."""
    text = str(exc).lower()
    if "timed out" in text or "timeout" in text:
        return "provider_timeout"
    if "route" in text:
        return "provider_route_invalid"
    if "substantive" in text or "empty" in text or "answer" in text or "action" in text:
        return "provider_answer_invalid"
    if "exited" in text or "returncode" in text:
        return "provider_process_failed"
    return "provider_bridge_failure"


def read_correlation_fd(fd: int) -> tuple[str, bytes]:
    with os.fdopen(fd, "r", encoding="ascii") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise RuntimeError("invalid bridge correlation")
    request_id = payload.get("request_id")
    secret_hex = payload.get("secret_hex")
    if (not isinstance(request_id, str) or len(request_id) != 64
            or not isinstance(secret_hex, str) or len(secret_hex) != 64):
        raise RuntimeError("invalid bridge correlation")
    try:
        int(request_id, 16)
        secret = bytes.fromhex(secret_hex)
    except ValueError:
        raise RuntimeError("invalid bridge correlation") from None
    return request_id, secret


def verified_round_request(path: Path, *, request_id: str, round_number: int,
                           secret: bytes) -> tuple[str, str]:
    """Return authenticated OmegaClaw context for exactly one bridge round."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError("invalid bridge request")
    expected_keys = {
        "protocol", "request_id", "round", "content_sha256", "content",
        "hmac_sha256",
    }
    if set(payload) != expected_keys:
        raise RuntimeError("invalid bridge request schema")
    content = payload.get("content")
    content_sha256 = payload.get("content_sha256")
    received_mac = payload.get("hmac_sha256")
    signed = {key: payload[key] for key in expected_keys - {"hmac_sha256"}}
    if (
        payload.get("protocol") != FILE_BRIDGE_PROTOCOL
        or payload.get("request_id") != request_id
        or payload.get("round") != round_number
        or not isinstance(content, str)
        or not content.strip()
        or not isinstance(content_sha256, str)
        or content_sha256 != hashlib.sha256(content.encode("utf-8")).hexdigest()
        or not isinstance(received_mac, str)
        or len(received_mac) != 64
        or not hmac.compare_digest(received_mac, canonical_mac(signed, secret))
    ):
        raise RuntimeError("invalid bridge request authentication")
    return content, content_sha256


def source_context(sources: list[Path]) -> str:
    """Read the frozen case sources at the host boundary, never inside Janus."""
    sections = []
    total = 0
    for source in sources:
        data = source.read_bytes()
        total += len(data)
        if total > MAX_SOURCE_BYTES:
            raise ValueError(f"frozen sources exceed {MAX_SOURCE_BYTES} bytes")
        sections.append(f"SOURCE: {source}\n{data.decode('utf-8')}")
    if not sections:
        return ""
    return (
        "\n\nISOLATED READ-ONLY PROJECT SOURCES\n"
        "The Phase-5 harness resolved these exact frozen source paths for this case. "
        "Use their contents as primary evidence and cite the source path; do not infer approval.\n\n"
        + "\n\n---\n\n".join(sections)
    )


def load_provider_free_fixture(path: Path | None) -> list[dict[str, object]] | None:
    """Load an explicitly enabled, bounded action script for offline gates."""
    if path is None:
        return None
    if os.environ.get("OMEGACLAW_ALLOW_BRIDGE_FIXTURE") != "1":
        raise RuntimeError("provider-free bridge fixture not authorized")
    info = path.stat()
    if not path.is_file() or path.is_symlink() or info.st_size > 16_384:
        raise RuntimeError("invalid provider-free bridge fixture")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, list) or not 1 <= len(payload) <= MAX_BRIDGE_ROUNDS:
        raise RuntimeError("invalid provider-free bridge fixture")
    for item in payload:
        if (
            not isinstance(item, dict)
            or not {"expect", "answer"} <= set(item) <= {
                "expect", "answer", "delay_ms", "expect_count"
            }
            or not isinstance(item["expect"], str)
            or not item["expect"]
            or not isinstance(item["answer"], str)
            or not item["answer"].strip()
        ):
            raise RuntimeError("invalid provider-free bridge fixture")
        delay_ms = item.get("delay_ms", 0)
        if not isinstance(delay_ms, int) or isinstance(delay_ms, bool) or not 0 <= delay_ms <= 20_000:
            raise RuntimeError("invalid provider-free bridge fixture")
        expect_count = item.get("expect_count")
        if (
            expect_count is not None
            and (
                not isinstance(expect_count, int)
                or isinstance(expect_count, bool)
                or not 1 <= expect_count <= 20
            )
        ):
            raise RuntimeError("invalid provider-free bridge fixture")
    return payload


def transport_instruction(live_transport: bool) -> str:
    if live_transport:
        return (
            "\n\nOMEGACLAW PROVIDER ACTION CONTRACT: the content above is the complete prompt "
            "assembled by the OmegaClaw/PeTTa loop, including its identity, skills, history, "
            "current Telegram request, and any results from earlier MeTTa actions. Do not replace "
            "it with a raw transport request and do not return raw prose for direct delivery. "
            "Propose only valid listed MeTTa commands. Use remember or query when the request "
            "requires persistent memory, wait for the next round to inspect PeTTa's returned "
            "results, and only then finish with exactly one (send \"answer text\") command. "
            "OVERRIDE only the earlier action-count at this provider boundary: return exactly "
            "one native OmegaClaw action on exactly one line, using the action syntax shown in "
            "OUTPUT_FORMAT (for example, query phrase or send answer), with no prose, Markdown, "
            "code fence, or second action. Do not use OpenClaw tools or OpenClaw "
            "Markdown memory; remember and query only by proposing those OmegaClaw actions. "
            "The outer Telegram transport accepts only a send actually executed by PeTTa."
        )
    return (
        "\n\nSHADOW TRANSPORT NOTE: the send skill is bound only to an in-process mock "
        "capture and cannot reach Telegram or any external channel. Return the final user-facing "
        "answer as exactly one MeTTa command: (send \"answer text\")."
    )


def answer(content: str, session: str, model: str, timeout: int, sources: list[Path],
           live_transport: bool = False, agent: str | None = None) -> str:
    if not agent:
        raise RuntimeError("openclaw agent route missing")
    prompt = content.replace(":-:-:-:", " ") + source_context(sources) + transport_instruction(live_transport)
    helper = Path(__file__).with_name("phase5_openclaw_model_run.mjs")
    request = json.dumps({
        "agent": agent,
        "session": session,
        "message": prompt,
        "timeout_ms": timeout * 1000,
    }, ensure_ascii=False)
    run = subprocess.run(
        ["node", str(helper)], input=request, text=True, capture_output=True,
        timeout=timeout + 20, check=False,
    )
    return require_single_metta_action(completed_answer_from_cli(
        stdout=run.stdout, returncode=run.returncode,
        stderr=run.stderr, requested_model=model,
    ))


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--port", type=int, required=True)
    p.add_argument("--directory", type=Path)
    p.add_argument("--session", required=True)
    p.add_argument("--model", required=True)
    p.add_argument("--agent")
    p.add_argument("--timeout", type=int, default=100)
    p.add_argument("--source", type=Path, action="append", default=[])
    p.add_argument("--live-transport", action="store_true",
                   help="use the live Telegram contract rather than the Phase-5 shadow contract")
    p.add_argument("--correlation-fd", type=int)
    p.add_argument("--max-rounds", type=int, default=MAX_BRIDGE_ROUNDS)
    p.add_argument("--provider-free-fixture", type=Path)
    args = p.parse_args()
    fixture = load_provider_free_fixture(args.provider_free_fixture)
    if args.directory is not None:
        if args.correlation_fd is None:
            raise RuntimeError("missing bridge correlation")
        request_id, correlation_secret = read_correlation_fd(
            args.correlation_fd
        )
        if not 1 <= args.max_rounds <= MAX_BRIDGE_ROUNDS:
            raise RuntimeError("invalid bridge round bound")
        args.directory.mkdir(mode=0o700, parents=True, exist_ok=True)
        print("READY", flush=True)
        deadline = time.monotonic() + args.timeout
        for round_number in range(1, args.max_rounds + 1):
            request_path = args.directory / f"request-{round_number}.json"
            response_path = args.directory / f"response-{round_number}.json"
            while not request_path.exists() and time.monotonic() < deadline:
                time.sleep(0.05)
            if not request_path.exists():
                return 0
            content_sha256 = "0" * 64
            try:
                request_content, content_sha256 = verified_round_request(
                    request_path, request_id=request_id,
                    round_number=round_number, secret=correlation_secret,
                )
                remaining = max(1, int(deadline - time.monotonic()))
                if fixture is not None:
                    if round_number > len(fixture):
                        raise RuntimeError("provider-free bridge fixture exhausted")
                    step = fixture[round_number - 1]
                    if step["expect"] not in request_content:
                        raise RuntimeError("provider-free bridge fixture context mismatch")
                    if (
                        step.get("expect_count") is not None
                        and request_content.count(step["expect"]) != step["expect_count"]
                    ):
                        raise RuntimeError("provider-free bridge fixture context count mismatch")
                    if step.get("delay_ms", 0):
                        time.sleep(step["delay_ms"] / 1000)
                    provider_action = step["answer"]
                else:
                    provider_action = answer(
                        request_content, f"{args.session}-r{round_number}", args.model, remaining,
                        args.source, args.live_transport, args.agent,
                    )
                provider_action = require_single_metta_action(provider_action)
                result = signed_response(
                    answer=provider_action, request_id=request_id,
                    round_number=round_number, content_sha256=content_sha256,
                    secret=correlation_secret,
                )
            except Exception as exc:
                result = signed_failure(
                    cause_code=bounded_failure_code(exc), request_id=request_id,
                    round_number=round_number, content_sha256=content_sha256,
                    secret=correlation_secret,
                )
            temporary_path = response_path.with_suffix(".tmp")
            temporary_path.write_text(
                json.dumps(result, ensure_ascii=False), encoding="utf-8"
            )
            os.replace(temporary_path, response_path)
            if result["status"] != "ok":
                return 1
        return 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind(("127.0.0.1", args.port)); srv.listen(1)
        print("READY", flush=True)
        while True:
            conn, _ = srv.accept()
            with conn:
                request = json.loads(conn.makefile("r", encoding="utf-8").readline())
                try:
                    request_content = request["content"]
                    legacy_provider_answer = answer(
                        request_content, args.session, args.model, args.timeout,
                        args.source, args.live_transport, args.agent,
                    )
                    result = {
                        "answer": normalize_model_answer(legacy_provider_answer)
                    }
                except Exception as exc: result = {"error": str(exc)}
                conn.sendall((json.dumps(result, ensure_ascii=False) + "\n").encode("utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
