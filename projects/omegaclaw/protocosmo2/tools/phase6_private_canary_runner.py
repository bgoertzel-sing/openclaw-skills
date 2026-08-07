#!/usr/bin/env python3
"""Run the bounded ProtoCosmo2 Telegram private canary.

The token is read only from a 0600 environment file.  The transport is the
only process retaining it; child OmegaClaw/provider processes receive a
scrubbed environment.  No unsolicited send is performed.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import uuid

MAX_DOCUMENT_BYTES = 10_000_000
MAX_OUTBOUND_DOCUMENT_BYTES = 50_000_000
# Extraction remains bounded independently of prompt/history limits.  The
# previous 60k ceiling silently cut ordinary long papers; 2M characters admits
# the supplied 104-page OmegaSelf paper in full while still failing closed on
# pathological expansion.
MAX_EXTRACTED_DOCUMENT_CHARS = 2_000_000


def validate_extracted_document_text(text: str) -> str:
    if len(text) > MAX_EXTRACTED_DOCUMENT_CHARS:
        raise RuntimeError("telegram_document_text_too_large")
    return text


def read_env(path: Path) -> dict[str, str]:
    if path.stat().st_mode & 0o777 != 0o600:
        raise RuntimeError("credential file must have mode 0600")
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#"):
            key, marker, value = line.partition("=")
            if not marker:
                raise RuntimeError("credential file is malformed")
            values[key] = value
    if not values.get("TG_BOT_TOKEN"):
        raise RuntimeError("TG_BOT_TOKEN is absent")
    return values


class Api:
    def __init__(self, token: str):
        self.token = token
        self.base = f"https://api.telegram.org/bot{token}"

    def _call(self, method: str, params: dict[str, object], timeout: int) -> object:
        data = urllib.parse.urlencode(params).encode("utf-8")
        request = urllib.request.Request(f"{self.base}/{method}", data=data)
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                payload = json.load(response)
        except Exception as exc:
            raise RuntimeError(f"telegram_{type(exc).__name__}") from None
        if not isinstance(payload, dict) or payload.get("ok") is not True:
            raise RuntimeError("telegram_non_ok")
        return payload.get("result")

    def get_updates(self, offset: int | None, timeout: int):
        params: dict[str, object] = {"timeout": timeout, "allowed_updates": json.dumps(["message"])}
        if offset is not None:
            params["offset"] = offset
        result = self._call("getUpdates", params, timeout + 15)
        return result if isinstance(result, list) else []

    def send_message(self, *, chat_id: int, text: str, reply_to_message_id: int) -> str:
        result = self._call("sendMessage", {"chat_id": chat_id, "text": text,
                                              "reply_parameters": json.dumps({"message_id": reply_to_message_id})}, 20)
        if not isinstance(result, dict) or type(result.get("message_id")) is not int:
            raise RuntimeError("telegram_missing_receipt")
        return str(result["message_id"])

    def send_document(self, *, chat_id: int, path: Path, filename: str, mime_type: str,
                      caption: str, reply_to_message_id: int | None = None) -> str:
        if (not path.is_file() or path.is_symlink() or path.stat().st_size > MAX_OUTBOUND_DOCUMENT_BYTES
                or len(caption) > 1024):
            raise RuntimeError("telegram_outbound_document_invalid")
        boundary = f"----ProtoCosmo2{uuid.uuid4().hex}"
        fields = {"chat_id": str(chat_id), "caption": caption}
        if reply_to_message_id is not None:
            fields["reply_parameters"] = json.dumps({"message_id": reply_to_message_id})
        body = bytearray()
        for name, value in fields.items():
            body.extend(f"--{boundary}\r\nContent-Disposition: form-data; name=\"{name}\"\r\n\r\n{value}\r\n".encode())
        body.extend((f"--{boundary}\r\nContent-Disposition: form-data; name=\"document\"; filename=\"{filename}\"\r\n"
                     f"Content-Type: {mime_type}\r\n\r\n").encode())
        body.extend(path.read_bytes())
        body.extend(f"\r\n--{boundary}--\r\n".encode())
        request = urllib.request.Request(
            f"{self.base}/sendDocument", data=bytes(body),
            headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                payload = json.load(response)
        except Exception as exc:
            raise RuntimeError(f"telegram_{type(exc).__name__}") from None
        result = payload.get("result") if isinstance(payload, dict) and payload.get("ok") is True else None
        if not isinstance(result, dict) or type(result.get("message_id")) is not int:
            raise RuntimeError("telegram_missing_receipt")
        return str(result["message_id"])

    def extract_document(self, document: dict[str, object]) -> str:
        file_id = document.get("file_id")
        size = document.get("file_size")
        name = document.get("file_name")
        mime = document.get("mime_type")
        if not isinstance(file_id, str) or not file_id or len(file_id) > 512:
            raise RuntimeError("telegram_document_id_invalid")
        if type(size) is not int or not 0 < size <= MAX_DOCUMENT_BYTES:
            raise RuntimeError("telegram_document_size_invalid")
        if not isinstance(name, str) or len(name) > 512 or not isinstance(mime, str):
            raise RuntimeError("telegram_document_metadata_invalid")
        is_pdf = mime == "application/pdf" and name.casefold().endswith(".pdf")
        is_text = mime.startswith("text/") and name.casefold().endswith((".txt", ".md", ".csv", ".json"))
        if not (is_pdf or is_text):
            raise RuntimeError("telegram_document_type_blocked")
        metadata = self._call("getFile", {"file_id": file_id}, 20)
        file_path = metadata.get("file_path") if isinstance(metadata, dict) else None
        if not isinstance(file_path, str) or not file_path or ".." in file_path:
            raise RuntimeError("telegram_file_path_invalid")
        try:
            with urllib.request.urlopen(
                f"https://api.telegram.org/file/bot{self.token}/{file_path}", timeout=30
            ) as response:
                raw = response.read(MAX_DOCUMENT_BYTES + 1)
        except Exception as exc:
            raise RuntimeError(f"telegram_download_{type(exc).__name__}") from None
        if len(raw) > MAX_DOCUMENT_BYTES:
            raise RuntimeError("telegram_document_too_large")
        if is_pdf:
            completed = subprocess.run(["pdftotext", "-", "-"], input=raw, stdout=subprocess.PIPE,
                                       stderr=subprocess.DEVNULL, timeout=30, check=False)
            if completed.returncode != 0:
                raise RuntimeError("pdf_extraction_failed")
            text = completed.stdout.decode("utf-8", errors="replace")
        else:
            text = raw.decode("utf-8", errors="replace")
        return validate_extracted_document_text(text)


def responder(prompt: str, args: argparse.Namespace) -> str:
    clean_env = {key: value for key, value in os.environ.items() if key != "TG_BOT_TOKEN"}
    clean_env["OMEGACLAW_WORKER_STATE_DIR"] = str(args.worker_state_dir)
    attachment_instruction = (
        "\n\n<trusted_transport_capability>This is a live Telegram request. The inner file channel is an "
        "implementation containment boundary only: your completed reply is sent by the outer Bot-API "
        "transport to the originating Telegram message. Never describe this inner boundary as shadow mode, "
        "mock transport, or an inability to reach Telegram. To send an already-created PDF or LaTeX source "
        "as a Telegram attachment, put MEDIA:/absolute/path/to/file.pdf (or .tex/.latex) on the first line "
        "of your reply, followed by an optional caption. The outer transport validates and sends it; only "
        "regular files beneath /home/openclaw/research-agent are allowed. Do not use MEDIA: for ordinary "
        "prose. Only claim a completed delivery when the outer transport returns its correlated receipt." 
        "</trusted_transport_capability>"
    )
    command = [sys.executable, str(args.driver), "--petta", str(args.petta), "--core", str(args.core),
               "--prompt", prompt + attachment_instruction, "--session", f"protocosmo2-canary-{int(time.time())}",
               "--model", args.model, "--provider", "OpenClawFileBridge", "--timeout", str(args.provider_timeout),
               "--file-channel"]
    completed = subprocess.run(command, env=clean_env, text=True, stdout=subprocess.PIPE,
                               stderr=subprocess.DEVNULL, timeout=args.provider_timeout + 30, check=False)
    if completed.returncode != 0:
        raise RuntimeError("omegaclaw_runtime_failure")
    for line in reversed(completed.stdout.splitlines()):
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        answer = payload.get("answer") if isinstance(payload, dict) else None
        if payload.get("status") == "ok" and isinstance(answer, str) and answer:
            return answer
    raise RuntimeError("omegaclaw_result_missing")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", type=Path, default=Path("/home/openclaw/.openclaw/protocosmo2.env"))
    parser.add_argument("--config", type=Path, default=Path("/home/openclaw/.openclaw/protocosmo2-canary.json"))
    parser.add_argument("--state-dir", type=Path, default=Path("/home/openclaw/.openclaw/protocosmo2-canary-state"))
    parser.add_argument("--worker-state-dir", type=Path, default=Path("/home/openclaw/.openclaw/protocosmo2-worker-state"))
    parser.add_argument("--core", type=Path, required=True)
    parser.add_argument("--petta", type=Path, required=True)
    parser.add_argument("--driver", type=Path, required=True)
    parser.add_argument("--model", default="openai/gpt-5.6-sol")
    parser.add_argument("--provider-timeout", type=int, default=240)
    parser.add_argument("--poll-timeout", type=int, default=15)
    args = parser.parse_args()
    worker_info = args.worker_state_dir.lstat()
    if args.worker_state_dir.is_symlink() or not args.worker_state_dir.is_dir():
        raise RuntimeError("worker state root must be a real directory")
    if worker_info.st_mode & 0o777 != 0o700:
        raise RuntimeError("worker state root must have mode 0700")
    sys.path.insert(0, str(args.core))
    from channels.private_canary import CanaryContract, load_config
    from channels.private_canary_telegram import PrivateCanaryTelegramTransport

    secret = read_env(args.env)
    api = Api(secret.pop("TG_BOT_TOKEN"))
    contract = CanaryContract(load_config(args.config), args.state_dir)
    transport = PrivateCanaryTelegramTransport(contract, api, lambda text: responder(text, args))
    running = True
    def stop(_signum, _frame):
        nonlocal running
        running = False
    signal.signal(signal.SIGTERM, stop); signal.signal(signal.SIGINT, stop)
    offset = transport.start_from_now()
    print(json.dumps({"event": "started", "offset": offset, "identity": contract.config.identity}), flush=True)
    recovery = transport.recover_startup()
    if recovery["status"] != "clean":
        print(json.dumps({"event": "startup_recovery", "status": recovery["status"]}), flush=True)
    while running:
        try:
            result = transport.run_once(poll_timeout=args.poll_timeout)
            if any(result.values()):
                print(json.dumps({"event": "cycle", **result}), flush=True)
        except Exception as exc:
            print(json.dumps({"event": "transport_failure", "error": type(exc).__name__}), flush=True)
            time.sleep(2)
    print(json.dumps({"event": "stopped"}), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
