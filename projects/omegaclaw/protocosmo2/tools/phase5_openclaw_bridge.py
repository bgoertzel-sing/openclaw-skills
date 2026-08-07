#!/usr/bin/env python3
"""Loopback-only host bridge for Phase-5's isolated OpenClaw CLI provider."""
from __future__ import annotations

import argparse
import json
import os
import socket
import subprocess
import tempfile
import time
from pathlib import Path

MAX_SOURCE_BYTES = 512_000


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
           live_transport: bool = False) -> str:
    prompt = content.replace(":-:-:-:", " ") + source_context(sources) + transport_instruction(live_transport)
    path = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", prefix="omegaclaw-shadow-", delete=False) as f:
            f.write(prompt)
            path = f.name
        run = subprocess.run(["openclaw", "agent", "--session-id", session, "--model", model,
                              "--message-file", path, "--json", "--timeout", str(timeout)],
                             text=True, capture_output=True, timeout=timeout + 20, check=False)
        if run.returncode:
            raise RuntimeError(f"openclaw agent exited {run.returncode}: {run.stderr[-500:]}")
        payloads = json.loads(run.stdout).get("result", {}).get("payloads", [])
        if not payloads or not isinstance(payloads[0].get("text"), str):
            raise RuntimeError("unrecognized OpenClaw response")
        return payloads[0]["text"]
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
    p.add_argument("--timeout", type=int, default=100)
    p.add_argument("--source", type=Path, action="append", default=[])
    p.add_argument("--live-transport", action="store_true",
                   help="use the live Telegram contract rather than the Phase-5 shadow contract")
    args = p.parse_args()
    if args.directory is not None:
        args.directory.mkdir(mode=0o700, parents=True, exist_ok=True)
        request_path = args.directory / "request.json"
        response_path = args.directory / "response.json"
        print("READY", flush=True)
        while not request_path.exists():
            time.sleep(0.05)
        try:
            request = json.loads(request_path.read_text(encoding="utf-8"))
            result = {"answer": answer(request["content"], args.session, args.model,
                                       args.timeout, args.source, args.live_transport)}
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
                try: result = {"answer": answer(request["content"], args.session, args.model,
                                                args.timeout, args.source, args.live_transport)}
                except Exception as exc: result = {"error": str(exc)}
                conn.sendall((json.dumps(result, ensure_ascii=False) + "\n").encode("utf-8"))


if __name__ == "__main__":
    raise SystemExit(main())
