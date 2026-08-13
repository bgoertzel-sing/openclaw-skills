#!/usr/bin/env python3
"""Run the bounded ProtoCosmo2 Telegram private canary.

The token is read only from a 0600 environment file.  The transport is the
only process retaining it; child OmegaClaw/provider processes receive a
scrubbed environment.  No unsolicited send is performed.
"""
from __future__ import annotations

import argparse
import ctypes
import hashlib
import io
import json
import os
from pathlib import Path
from pathlib import PurePosixPath
import signal
import stat
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request
import urllib.error
import uuid
import re
import unicodedata
import zipfile

MAX_DOCUMENT_BYTES = 10_000_000
MAX_OUTBOUND_DOCUMENT_BYTES = 50_000_000
# Extraction remains bounded independently of prompt/history limits.  The
# previous 60k ceiling silently cut ordinary long papers; 2M characters admits
# the supplied 104-page OmegaSelf paper in full while still failing closed on
# pathological expansion.
MAX_EXTRACTED_DOCUMENT_CHARS = 2_000_000
MAX_ZIP_ENTRIES = 64
MAX_ZIP_UNCOMPRESSED_BYTES = 5_000_000
MAX_ZIP_ENTRY_BYTES = 1_000_000
MAX_ZIP_COMPRESSION_RATIO = 100
ZIP_TEXT_SUFFIXES = {
    ".txt", ".md", ".csv", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg",
    ".py", ".sh", ".metta", ".pl", ".rs", ".js", ".ts", ".html", ".css",
}
MAX_INCIDENT_BYTES = 4096
SEND_WRAPPER = re.compile(r'^\(send\s+("(?:\\.|[^"\\])*")\s*\)$', re.DOTALL)


def arm_parent_death_signal() -> None:
    """Terminate this receiver if its explicitly bound supervisor disappears."""
    expected_text = os.environ.get("OMEGACLAW_EXPECTED_PARENT_PID")
    if expected_text is None:
        return
    if not expected_text.isdigit() or int(expected_text) < 1:
        raise RuntimeError("invalid expected parent pid")
    expected = int(expected_text)
    if os.getppid() != expected:
        raise RuntimeError("receiver parent identity mismatch")
    libc = ctypes.CDLL(None, use_errno=True)
    if libc.prctl(1, signal.SIGTERM, 0, 0, 0) != 0:  # PR_SET_PDEATHSIG
        raise OSError(ctypes.get_errno(), "PR_SET_PDEATHSIG failed")
    # Close the race where the parent exits between the first check and prctl.
    if os.getppid() != expected:
        raise RuntimeError("receiver parent exited during startup")


def validate_extracted_document_text(text: str) -> str:
    if len(text) > MAX_EXTRACTED_DOCUMENT_CHARS:
        raise RuntimeError("telegram_document_text_too_large")
    return text


def extract_bounded_zip_text(raw: bytes) -> str:
    """Inspect a ZIP in memory without writing or executing archive members."""
    try:
        archive = zipfile.ZipFile(io.BytesIO(raw))
    except (zipfile.BadZipFile, OSError):
        raise RuntimeError("zip_invalid") from None
    with archive:
        members = archive.infolist()
        if not members or len(members) > MAX_ZIP_ENTRIES:
            raise RuntimeError("zip_entry_count_invalid")
        seen: set[str] = set()
        total_uncompressed = 0
        inventory: list[str] = []
        extracted: list[str] = []
        for member in members:
            normalized_name = unicodedata.normalize("NFC", member.filename.replace("\\", "/"))
            raw_parts = normalized_name.rstrip("/").split("/")
            path = PurePosixPath(normalized_name)
            if (
                not normalized_name or len(normalized_name) > 512
                or path.is_absolute() or normalized_name.startswith("//")
                or any(not part or part in {".", ".."} for part in raw_parts)
                or (raw_parts and re.fullmatch(r"[A-Za-z]:.*", raw_parts[0]) is not None)
                or any(ord(char) < 32 or ord(char) == 127 for char in normalized_name)
                or member.flag_bits & 0x1
            ):
                raise RuntimeError("zip_member_unsafe")
            canonical_name = normalized_name.casefold()
            if canonical_name in seen:
                raise RuntimeError("zip_member_unsafe")
            seen.add(canonical_name)
            mode = (member.external_attr >> 16) & 0o170000
            if mode == 0o120000:
                raise RuntimeError("zip_member_unsafe")
            if member.is_dir():
                continue
            total_uncompressed += member.file_size
            if (
                member.file_size < 0 or member.file_size > MAX_ZIP_ENTRY_BYTES
                or total_uncompressed > MAX_ZIP_UNCOMPRESSED_BYTES
            ):
                raise RuntimeError("zip_uncompressed_size_invalid")
            if member.file_size and (
                member.compress_size <= 0
                or member.file_size > member.compress_size * MAX_ZIP_COMPRESSION_RATIO
            ):
                raise RuntimeError("zip_compression_ratio_invalid")
            inventory.append(normalized_name)
            if path.suffix.casefold() not in ZIP_TEXT_SUFFIXES:
                continue
            try:
                content = archive.read(member)
                text = content.decode("utf-8")
            except (KeyError, RuntimeError, UnicodeDecodeError, zipfile.BadZipFile):
                raise RuntimeError("zip_text_member_invalid") from None
            if "\x00" in text:
                raise RuntimeError("zip_text_member_invalid")
            # JSON-string framing plus escaped angle/ampersand characters makes
            # both names and content incapable of closing the surrounding
            # untrusted-document envelope or forging an XML-like boundary.
            safe_name = json.dumps(normalized_name, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
            safe_text = json.dumps(text, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
            extracted.append(
                f"ZIP_MEMBER name={safe_name} utf8_chars={len(text)} text={safe_text}"
            )
        if not inventory:
            raise RuntimeError("zip_has_no_files")
        safe_inventory = [
            json.dumps(name, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
            for name in inventory
        ]
        result = "ZIP inventory (JSON-string names):\n" + "\n".join(f"- {name}" for name in safe_inventory)
        if extracted:
            result += "\n\n" + "\n\n".join(extracted)
        return validate_extracted_document_text(result)


def append_responder_incident(path: Path, *, returncode: int, stderr: str) -> None:
    """Append non-secret failure metadata to a private regular file."""
    record = {
        "code": "omegaclaw_runtime_failure",
        "observed_at": int(time.time()),
        "returncode": returncode,
        "stderr_bytes": len(stderr.encode("utf-8", errors="replace")),
        "stderr_sha256": hashlib.sha256(stderr.encode("utf-8", errors="replace")).hexdigest(),
    }
    encoded = (json.dumps(record, ensure_ascii=True) + "\n").encode("ascii")
    if len(encoded) > MAX_INCIDENT_BYTES:
        raise RuntimeError("responder_incident_too_large")
    flags = os.O_WRONLY | os.O_CREAT | os.O_APPEND | os.O_NOFOLLOW | os.O_CLOEXEC | os.O_NONBLOCK
    fd = os.open(path, flags, 0o600)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1 or stat.S_IMODE(info.st_mode) != 0o600:
            raise RuntimeError("unsafe_responder_incident_file")
        view = memoryview(encoded)
        while view:
            written = os.write(fd, view)
            if written <= 0:
                raise RuntimeError("responder_incident_write_failed")
            view = view[written:]
    finally:
        os.close(fd)


def read_env(path: Path) -> dict[str, str]:
    if path.stat().st_mode & 0o777 != 0o600:
        raise RuntimeError("credential file must have mode 0600")
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            if line.startswith("export "):
                line = line[len("export "):].lstrip()
            key, marker, value = line.partition("=")
            if not marker:
                raise RuntimeError("credential file is malformed")
            values[key.strip()] = value
    token = (
        values.get("TG_BOT_TOKEN")
        or values.get("OMEGACLAW_TG_BOT_TOKEN")
        or values.get("PROTOMEGABOT2_TG_BOT_TOKEN")
    )
    if not token:
        raise RuntimeError("Telegram bot token is absent")
    values["TG_BOT_TOKEN"] = token
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

    def delete_message(self, *, chat_id: int, message_id: str) -> None:
        if type(chat_id) is not int or chat_id == 0 or not message_id.isdigit():
            raise RuntimeError("telegram_delete_target_invalid")
        data = urllib.parse.urlencode(
            {"chat_id": chat_id, "message_id": int(message_id)}
        ).encode("utf-8")
        request = urllib.request.Request(f"{self.base}/deleteMessage", data=data)
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                payload = json.load(response)
        except urllib.error.HTTPError as exc:
            # Bot API deletion is semantically idempotent. A crash may occur
            # after Telegram deletes the message but before the durable marker
            # is written; the retry then reports an already-absent target.
            try:
                raw = exc.read(4097)
                error_payload = json.loads(raw) if len(raw) <= 4096 else None
            except Exception:
                error_payload = None
            if (exc.code == 400 and isinstance(error_payload, dict)
                    and error_payload.get("description") == "Bad Request: message to delete not found"):
                return
            raise RuntimeError("telegram_HTTPError") from None
        except Exception as exc:
            raise RuntimeError(f"telegram_{type(exc).__name__}") from None
        if (not isinstance(payload, dict) or payload.get("ok") is not True
                or payload.get("result") is not True):
            raise RuntimeError("telegram_delete_unconfirmed")

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
        lower_name = name.casefold()
        is_pdf = mime == "application/pdf" and lower_name.endswith(".pdf")
        text_suffix = name.casefold().endswith((".txt", ".md", ".csv", ".json"))
        # Telegram clients commonly upload Markdown with the generic binary
        # MIME type. Keep the existing bounded extension allowlist authoritative
        # for that one generic case; all other MIME/extension mismatches still
        # fail closed before download.
        is_text = text_suffix and (
            mime.startswith("text/") or mime == "application/octet-stream"
        )
        is_zip = lower_name.endswith(".zip") and mime in {
            "application/zip", "application/x-zip-compressed", "application/octet-stream"
        }
        if not (is_pdf or is_text or is_zip):
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
        elif is_zip:
            text = extract_bounded_zip_text(raw)
        else:
            text = raw.decode("utf-8", errors="replace")
        return validate_extracted_document_text(text)


def clean_rendered_answer(answer: str) -> str:
    """Unwrap one exact send action and reject malformed action-shaped output."""
    stripped = answer.strip()
    match = SEND_WRAPPER.fullmatch(stripped)
    if match is None:
        if stripped.startswith("(send"):
            raise RuntimeError("unsafe_send_wrapper")
        return answer
    try:
        unwrapped = json.loads(match.group(1))
    except json.JSONDecodeError:
        raise RuntimeError("unsafe_send_wrapper") from None
    if not isinstance(unwrapped, str) or not unwrapped:
        raise RuntimeError("unsafe_send_wrapper")
    return unwrapped


def captured_bridge_answer(stdout: str) -> str | None:
    """Return the last complete bridge answer payload from captured stdout."""
    for line in reversed(stdout.splitlines()):
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        answer = payload.get("answer") if isinstance(payload, dict) else None
        if payload.get("status") == "ok" and isinstance(answer, str) and answer:
            return answer
    return None


def write_private_prompt(text: str) -> Path:
    """Create and durably publish a private prompt, cleaning every failed write."""
    handle = None
    path = None
    try:
        handle = tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", prefix="omegaclaw-outer-prompt-", delete=False
        )
        path = Path(handle.name)
        handle.write(text)
        handle.flush()
        os.fsync(handle.fileno())
        handle.close()
        handle = None
        return path
    except BaseException:
        if handle is not None:
            try:
                handle.close()
            except BaseException:
                pass
        if path is not None:
            try:
                path.unlink()
            except FileNotFoundError:
                pass
        raise


def terminate_process_group(process: subprocess.Popen, *, term_timeout: float = 10.0,
                            kill_timeout: float = 5.0) -> None:
    """Boundedly terminate the dedicated group even if its leader exited."""
    pgid = process.pid

    def signal_group(sig: int) -> bool:
        try:
            os.killpg(pgid, sig)
            return True
        except ProcessLookupError:
            return False

    signal_group(15)
    deadline = time.monotonic() + term_timeout
    while time.monotonic() < deadline:
        try:
            os.killpg(pgid, 0)
        except ProcessLookupError:
            break
        time.sleep(0.05)
    else:
        signal_group(9)
        deadline = time.monotonic() + kill_timeout
        while time.monotonic() < deadline:
            try:
                os.killpg(pgid, 0)
            except ProcessLookupError:
                break
            time.sleep(0.05)
    if process.poll() is None:
        try:
            process.wait(timeout=max(0.1, kill_timeout))
        except subprocess.TimeoutExpired:
            signal_group(9)
            process.wait(timeout=max(0.1, kill_timeout))


def responder(prompt: str, args: argparse.Namespace, isolation_key: str | None = None) -> str:
    clean_env = {key: value for key, value in os.environ.items() if key != "TG_BOT_TOKEN"}
    worker_state_dir = args.worker_state_dir
    if isolation_key is not None:
        worker_state_dir = args.worker_state_dir / "deferred" / isolation_key
        worker_state_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    clean_env["OMEGACLAW_WORKER_STATE_DIR"] = str(worker_state_dir)
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
    prompt_path = write_private_prompt(prompt + attachment_instruction)
    command = [sys.executable, str(args.driver), "--petta", str(args.petta), "--core", str(args.core),
               "--prompt-file", str(prompt_path), "--session", f"{args.session_prefix}-{int(time.time())}",
               "--model", args.model, "--provider", "OpenClawFileBridge", "--timeout", str(args.provider_timeout),
               "--agent", args.agent_id,
               "--file-channel", "--live-transport"]
    # Own the driver as a process group. If an outer timeout kills only the
    # Python driver, its nested PeTTa/SWI group otherwise survives and can
    # compete with the next live request.
    process = None
    try:
        process = subprocess.Popen(command, env=clean_env, text=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, start_new_session=True)
        stdout, stderr = process.communicate(timeout=args.provider_timeout + 30)
    except subprocess.TimeoutExpired as exc:
        terminate_process_group(process)
        raise RuntimeError("omegaclaw_runtime_timeout") from exc
    except BaseException:
        if process is not None:
            terminate_process_group(process)
        raise
    finally:
        if process is not None:
            # The leader may have exited after forking PeTTa/SWI descendants.
            # Always drain its dedicated group on every terminal turn outcome.
            terminate_process_group(process)
        try:
            prompt_path.unlink()
        except FileNotFoundError:
            pass
    assert process is not None
    # The bridge result is a completed immutable handoff from the inner
    # runtime.  PeTTa can still fail while finalizing after that handoff (the
    # message-848 production incident).  Preserve the incident, but do not
    # discard an already captured and outer-validated answer.  A non-zero exit
    # without such an answer remains a bounded failure.
    raw_answer = captured_bridge_answer(stdout)
    if process.returncode != 0:
        diagnostic = args.worker_state_dir / "responder-incidents.jsonl"
        append_responder_incident(diagnostic, returncode=process.returncode, stderr=stderr)
        if raw_answer is not None:
            return clean_rendered_answer(raw_answer)
        raise RuntimeError("omegaclaw_runtime_failure")
    if raw_answer is not None:
        return clean_rendered_answer(raw_answer)
    raise RuntimeError("omegaclaw_result_missing")


def main() -> int:
    arm_parent_death_signal()
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", type=Path, default=Path("/home/openclaw/.openclaw/protocosmo2.env"))
    parser.add_argument("--config", type=Path, default=Path("/home/openclaw/.openclaw/protocosmo2-canary.json"))
    parser.add_argument("--state-dir", type=Path, default=Path("/home/openclaw/.openclaw/protocosmo2-canary-state"))
    parser.add_argument("--worker-state-dir", type=Path, default=Path("/home/openclaw/.openclaw/protocosmo2-worker-state"))
    parser.add_argument("--core", type=Path, required=True)
    parser.add_argument("--transport-core", type=Path,
                        help="core tree providing the durable outer transport modules")
    parser.add_argument("--petta", type=Path, required=True)
    parser.add_argument("--driver", type=Path, required=True)
    parser.add_argument("--model", default="openai/gpt-5.6-sol")
    parser.add_argument("--agent-id", default="main")
    parser.add_argument("--identity", default="ProtoCosmo2")
    parser.add_argument("--bot-id", type=int, default=8716054285)
    parser.add_argument("--bot-username", default="@protocosmo2bot")
    parser.add_argument("--session-prefix", default="protocosmo2-canary")
    parser.add_argument("--provider-timeout", type=int, default=240)
    parser.add_argument("--poll-timeout", type=int, default=15)
    parser.add_argument("--disable-deferred-jobs", action="store_true",
                        help="schema-compatible rollback mode: process long requests synchronously")
    args = parser.parse_args()
    worker_info = args.worker_state_dir.lstat()
    if args.worker_state_dir.is_symlink() or not args.worker_state_dir.is_dir():
        raise RuntimeError("worker state root must be a real directory")
    if worker_info.st_mode & 0o777 != 0o700:
        raise RuntimeError("worker state root must have mode 0700")
    transport_core = args.transport_core or args.core
    sys.path.insert(0, str(transport_core))
    from channels.private_canary import CanaryContract, load_config
    from channels.private_canary_telegram import PrivateCanaryTelegramTransport

    secret = read_env(args.env)
    api = Api(secret.pop("TG_BOT_TOKEN"))
    contract = CanaryContract(
        load_config(args.config, expected_identity=args.identity), args.state_dir
    )
    deferred_callback = None
    if not args.disable_deferred_jobs:
        deferred_callback = lambda text, task_id: responder(text, args, task_id)
    transport = PrivateCanaryTelegramTransport(
        contract, api, lambda text: responder(text, args), bot_id=args.bot_id,
        bot_username=args.bot_username, attachment_label=args.identity,
        deferred_responder=deferred_callback,
    )
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
