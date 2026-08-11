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
import tempfile
import time
from pathlib import Path

MAX_SOURCE_BYTES = 512_000
EXACT_SEND = re.compile(r'^\(send\s+"(?:\\.|[^"\\])*"\)$', re.DOTALL)
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
    expected_provider, expected_model = requested_model.split("/", 1)
    if not isinstance(result, dict):
        raise RuntimeError("openclaw_route_missing")
    meta = result.get("meta")
    agent_meta = meta.get("agentMeta") if isinstance(meta, dict) else None
    if not isinstance(agent_meta, dict):
        raise RuntimeError("openclaw_route_missing")
    if agent_meta.get("provider") != expected_provider or agent_meta.get("model") != expected_model:
        raise RuntimeError("openclaw_route_mismatch")


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


def signed_response(*, raw_answer: str, request_id: str, prompt_sha256: str,
                    session: str, secret: bytes) -> dict[str, str]:
    payload = {
        "status": "ok",
        "request_id": request_id,
        "prompt_sha256": prompt_sha256,
        "session": session,
        "raw_answer": raw_answer,
    }
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True,
                           separators=(",", ":")).encode("utf-8")
    payload["hmac_sha256"] = hmac.new(secret, canonical, hashlib.sha256).hexdigest()
    return payload


def read_correlation_fd(fd: int) -> tuple[str, str, bytes]:
    with os.fdopen(fd, "r", encoding="ascii") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise RuntimeError("invalid bridge correlation")
    request_id = payload.get("request_id")
    prompt_sha256 = payload.get("prompt_sha256")
    secret_hex = payload.get("secret_hex")
    if (not isinstance(request_id, str) or len(request_id) != 64
            or not isinstance(prompt_sha256, str) or len(prompt_sha256) != 64
            or not isinstance(secret_hex, str) or len(secret_hex) != 64):
        raise RuntimeError("invalid bridge correlation")
    try:
        int(request_id, 16)
        int(prompt_sha256, 16)
        secret = bytes.fromhex(secret_hex)
    except ValueError:
        raise RuntimeError("invalid bridge correlation") from None
    return request_id, prompt_sha256, secret


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


def transport_instruction(live_transport: bool) -> str:
    if live_transport:
        return (
            "\n\nLIVE TELEGRAM TRANSPORT NOTE: this request arrived through a live Telegram "
            "receiver. The file bridge is an internal implementation boundary; the outer Bot-API "
            "transport delivers your completed reply to the originating Telegram message. Return "
            "the final user-facing answer as exactly one MeTTa command: (send \"answer text\")."
        )
    return (
        "\n\nSHADOW TRANSPORT NOTE: the send skill is bound only to an in-process mock "
        "capture and cannot reach Telegram or any external channel. Return the final user-facing "
        "answer as exactly one MeTTa command: (send \"answer text\")."
    )


def answer(content: str, session: str, model: str, timeout: int, sources: list[Path],
           live_transport: bool = False, agent: str | None = None) -> str:
    prompt = content.replace(":-:-:-:", " ") + source_context(sources) + transport_instruction(live_transport)
    path = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", prefix="omegaclaw-shadow-", delete=False) as f:
            f.write(prompt)
            path = f.name
        run = subprocess.run(["openclaw", "agent", *( ["--agent", agent] if agent else [] ),
                              "--session-id", session, "--model", model,
                              "--message-file", path, "--json", "--timeout", str(timeout)],
                             text=True, capture_output=True, timeout=timeout + 20, check=False)
        if run.returncode:
            raise RuntimeError(f"openclaw agent exited {run.returncode}: {run.stderr[-500:]}")
        envelope = json.loads(run.stdout)
        result = envelope.get("result", {}) if isinstance(envelope, dict) else {}
        require_requested_route(result, model)
        payloads = result.get("payloads", [])
        if not payloads or not isinstance(payloads[0].get("text"), str):
            raise RuntimeError("unrecognized OpenClaw response")
        return require_substantive_answer(payloads[0]["text"])
    finally:
        if path:
            try: os.unlink(path)
            except FileNotFoundError: pass


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
    p.add_argument("--live-request-file", type=Path)
    p.add_argument("--correlation-fd", type=int)
    args = p.parse_args()
    if args.directory is not None:
        if args.correlation_fd is None:
            raise RuntimeError("missing bridge correlation")
        request_id, expected_prompt_sha256, correlation_secret = read_correlation_fd(
            args.correlation_fd
        )
        args.directory.mkdir(mode=0o700, parents=True, exist_ok=True)
        request_path = args.directory / "request.json"
        response_path = args.directory / "response.json"
        print("READY", flush=True)
        while not request_path.exists():
            time.sleep(0.05)
        try:
            request = json.loads(request_path.read_text(encoding="utf-8"))
            request_content = (args.live_request_file.read_text(encoding="utf-8")
                               if args.live_request_file is not None else request["content"])
            observed_prompt_sha256 = hashlib.sha256(
                request_content.encode("utf-8")
            ).hexdigest()
            if observed_prompt_sha256 != expected_prompt_sha256:
                raise RuntimeError("bridge prompt correlation mismatch")
            raw_answer = answer(request_content, args.session, args.model,
                                args.timeout, args.source, args.live_transport, args.agent)
            result = signed_response(
                raw_answer=raw_answer,
                request_id=request_id,
                prompt_sha256=observed_prompt_sha256,
                session=args.session,
                secret=correlation_secret,
            )
            result["answer"] = normalize_model_answer(raw_answer)
        except Exception as exc:
            result = {"error": str(exc)}
        temporary_path = response_path.with_suffix(".tmp")
        temporary_path.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
        os.replace(temporary_path, response_path)
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
                    request_content = (args.live_request_file.read_text(encoding="utf-8")
                                       if args.live_request_file is not None else request["content"])
                    raw_answer = answer(request_content, args.session, args.model,
                                        args.timeout, args.source, args.live_transport, args.agent)
                    result = {"answer": normalize_model_answer(raw_answer), "raw_answer": raw_answer}
                except Exception as exc: result = {"error": str(exc)}
                conn.sendall((json.dumps(result, ensure_ascii=False) + "\n").encode("utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
