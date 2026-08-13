#!/usr/bin/env python3
"""Run one frozen prompt through the real isolated OmegaClaw MeTTa loop."""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import re
import secrets
import stat
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def find_project_root(core: Path) -> Path:
    """Resolve the OmegaClaw project root without assuming worktree depth."""
    for candidate in (core, *core.parents):
        if candidate.name == "omegaclaw" and (candidate / "local").is_dir():
            return candidate
    raise RuntimeError("cannot locate the OmegaClaw project root from --core")


def read_prompt(prompt: str | None, prompt_file: Path | None) -> str:
    """Read one prompt without requiring large documents to cross argv."""
    if (prompt is None) == (prompt_file is None):
        raise RuntimeError("exactly one prompt source is required")
    if prompt is not None:
        return prompt
    assert prompt_file is not None
    flags = os.O_RDONLY | os.O_CLOEXEC | os.O_NOFOLLOW
    fd = os.open(prompt_file, flags)
    try:
        info = os.fstat(fd)
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise RuntimeError("prompt file must be a private regular file")
        if info.st_mode & 0o077:
            raise RuntimeError("prompt file must not be accessible by group or other")
        with os.fdopen(fd, "r", encoding="utf-8") as handle:
            fd = -1
            return handle.read()
    finally:
        if fd >= 0:
            os.close(fd)


def read_bridge_raw_answer(response_path: Path, *, request_id: str,
                           prompt_sha256: str, session: str,
                           secret: bytes) -> str | None:
    """Read only an authenticated handoff for this exact live request."""
    try:
        payload = json.loads(response_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    if not isinstance(payload, dict):
        return None
    raw_answer = payload.get("raw_answer")
    received_mac = payload.get("hmac_sha256")
    signed = {
        "status": payload.get("status"),
        "request_id": payload.get("request_id"),
        "prompt_sha256": payload.get("prompt_sha256"),
        "session": payload.get("session"),
        "raw_answer": raw_answer,
    }
    if (signed["status"] != "ok" or signed["request_id"] != request_id
            or signed["prompt_sha256"] != prompt_sha256
            or signed["session"] != session
            or not isinstance(raw_answer, str) or not raw_answer.strip()
            or not isinstance(received_mac, str) or len(received_mac) != 64):
        return None
    canonical = json.dumps(signed, ensure_ascii=False, sort_keys=True,
                           separators=(",", ":")).encode("utf-8")
    expected_mac = hmac.new(secret, canonical, hashlib.sha256).hexdigest()
    if not hmac.compare_digest(received_mac, expected_mac):
        return None
    return raw_answer


def await_bridge_answer_after_exit(response_path: Path, *, request_id: str,
                                   prompt_sha256: str, session: str,
                                   secret: bytes, timeout: float = 2.0) -> str | None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        answer = read_bridge_raw_answer(
            response_path, request_id=request_id, prompt_sha256=prompt_sha256,
            session=session, secret=secret,
        )
        if answer:
            return answer
        time.sleep(0.05)
    return None


def terminate_process_group(process: subprocess.Popen, *, term_timeout: float = 10.0,
                            kill_timeout: float = 5.0) -> None:
    """Boundedly terminate a dedicated group even after its leader exits."""
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


def emit_case_answer(answer: str, *, started: float, command: list[str],
                     rescued_after_early_exit: bool) -> None:
    print(json.dumps({"status": "ok", "answer": answer,
                      "latency_ms": round((time.monotonic() - started) * 1000, 1),
                      "command": command}, sort_keys=True), flush=True)
    if rescued_after_early_exit:
        # Preserve the authenticated answer on stdout for the outer responder,
        # but keep the nonzero incident signal so recovery is never silently
        # relabeled as a healthy inner run.
        raise RuntimeError("OmegaClaw exited after authenticated bridge handoff")


def select_polled_answer(*, live_transport: bool, output_answer: str,
                         authenticated_answer: str | None,
                         child_returncode: int | None) -> tuple[str, bool]:
    """Select one answer and whether it coincided with an exited child."""
    # Live transport has exactly one authority-bearing answer seam: the
    # authenticated bridge receipt. ``output.txt`` is an inner diagnostic and
    # can never substitute for that receipt.
    answer = (authenticated_answer or "") if live_transport else output_answer
    return answer, bool(answer and child_returncode is not None)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--petta", type=Path, required=True)
    parser.add_argument("--core", type=Path, required=True)
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt")
    prompt_group.add_argument("--prompt-file", type=Path)
    parser.add_argument("--session", required=True)
    parser.add_argument("--model", default="openai/gpt-5.6-terra")
    parser.add_argument("--agent")
    parser.add_argument("--provider", default="OpenClawCLI",
                        choices=("OpenClawCLI", "OpenClawBridge", "OpenClawFileBridge", "Test", "SubprocessProbe"))
    parser.add_argument("--test-answer",
                        help="deterministic Test-provider response; requires --provider Test")
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--file-channel", action="store_true")
    parser.add_argument("--live-transport", action="store_true",
                        help="use the live Telegram instruction for an outer Bot-API delivery path")
    parser.add_argument("--source", type=Path, action="append", default=[],
                        help="frozen project source to expose read-only to the host bridge")
    args = parser.parse_args()
    args.prompt = read_prompt(args.prompt, args.prompt_file)
    args.petta = args.petta.resolve()
    args.core = args.core.resolve()
    args.source = [source.resolve() for source in args.source]

    mock_dir = args.core / "Autotests" / "mock"
    sys.path.insert(0, str(mock_dir))
    from comm import CommMockServer, COMM_MOCK_PORT  # type: ignore
    from llm import LlmMockController, LLM_MOCK_PORT  # type: ignore
    from rpc import LOCALHOST  # type: ignore

    env = os.environ.copy()
    # ``core`` lives under the isolated Phase-2 baseline while the recorded
    # SWI build is project-local.  Phase 2 did not create a venv inside the
    # detached PeTTa checkout; use it if present, otherwise use the existing
    # project-scoped PeTTa venv recorded by provisioning.  This is an explicit
    # dependency seam, not an ambient/global Python fallback.
    project_root = find_project_root(args.core)
    swipl_bin = project_root / "local" / "swipl-9.3.36" / "bin"
    venv_roots = [args.petta / ".venv", project_root / "repos" / "PeTTa" / ".venv"]
    site_packages = next(
        (candidate for venv_root in venv_roots
         for candidate in (venv_root / "lib").glob("python*/site-packages")
         if (candidate / "py_landlock").is_dir()),
        None,
    )
    if site_packages is None:
        raise RuntimeError("no project-scoped PeTTa site-packages with py_landlock found")
    env.update({
        "TEST_SERVER_IP": LOCALHOST,
        "OMEGACLAW_SHADOW_SESSION": args.session,
        "OMEGACLAW_SHADOW_MODEL": args.model,
        "OMEGACLAW_SHADOW_TIMEOUT": str(max(30, args.timeout - 20)),
        "OMEGACLAW_SHADOW_HASH_EMBEDDING": "1",
        "OMEGACLAW_SUBPROCESS_PROBE": "1" if args.provider == "SubprocessProbe" else "0",
        "IMPORT_KB_ON_START": "0",
        "PYTHONDONTWRITEBYTECODE": "1",
        "PATH": str(swipl_bin) + os.pathsep + env.get("PATH", ""),
        "PYTHONPATH": os.pathsep.join([
            str(args.core), str(args.core / "src"), str(args.core / "profile"),
            str(args.core / "channels"), str(args.petta / "repos" / "petta_lib_chromadb"),
            str(site_packages) if site_packages else "",
            env.get("PYTHONPATH", ""),
        ]),
    })
    channel_directory = None
    if args.file_channel:
        channel_directory = tempfile.TemporaryDirectory(prefix="omegaclaw-file-channel-")
        env["OMEGACLAW_SHADOW_CHANNEL_DIR"] = channel_directory.name
    bridge_process = None
    bridge_log = None
    bridge_directory = None
    live_request_path = None
    bridge_request_id = secrets.token_hex(32)
    bridge_prompt_sha256 = hashlib.sha256(args.prompt.encode("utf-8")).hexdigest()
    bridge_secret = secrets.token_bytes(32)
    if args.provider == "OpenClawBridge":
        bridge_log = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
        bridge_port = 19765
        env["OMEGACLAW_SHADOW_BRIDGE"] = f"127.0.0.1:{bridge_port}"
        bridge_process = subprocess.Popen(
            [sys.executable, str(Path(__file__).with_name("phase5_openclaw_bridge.py")),
             "--port", str(bridge_port), "--session", args.session, "--model", args.model,
             "--timeout", str(max(30, args.timeout - 20))],
            text=True, stdout=bridge_log, stderr=subprocess.STDOUT, start_new_session=True)
        time.sleep(0.3)
    elif args.provider == "OpenClawFileBridge":
        bridge_log = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
        bridge_directory = tempfile.TemporaryDirectory(prefix="omegaclaw-file-bridge-")
        env["OMEGACLAW_SHADOW_FILE_BRIDGE"] = bridge_directory.name
        if args.live_transport:
            request_handle = tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", prefix="omegaclaw-live-request-", delete=False
            )
            request_handle.write(args.prompt)
            request_handle.close()
            live_request_path = request_handle.name
        correlation_read_fd, correlation_write_fd = os.pipe()
        bridge_process = subprocess.Popen(
            [sys.executable, str(Path(__file__).with_name("phase5_openclaw_bridge.py")),
             "--port", "0", "--directory", bridge_directory.name,
             "--session", args.session, "--model", args.model,
             "--correlation-fd", str(correlation_read_fd),
             *( ["--agent", args.agent] if args.agent else [] ),
             # Reserve forty seconds of the case budget for bridge process
             # collection plus authenticated handoff/finalization.  The
             # bridge itself adds a bounded twenty-second subprocess grace,
             # leaving another twenty seconds before the case deadline.
             "--timeout", str(max(30, args.timeout - 40)),
             *( ["--live-transport"] if args.live_transport else [] ),
             *( ["--live-request-file", live_request_path] if live_request_path else [] ),
             *[item for source in args.source for item in ("--source", str(source))]],
            text=True, stdout=bridge_log, stderr=subprocess.STDOUT,
            start_new_session=True, pass_fds=(correlation_read_fd,))
        os.close(correlation_read_fd)
        try:
            correlation_payload = json.dumps({
                "request_id": bridge_request_id,
                "prompt_sha256": bridge_prompt_sha256,
                "secret_hex": bridge_secret.hex(),
            }, separators=(",", ":")).encode("ascii")
            os.write(correlation_write_fd, correlation_payload)
        finally:
            os.close(correlation_write_fd)
        time.sleep(0.3)
    command = ["sh", str(args.petta / "run.sh"), str(args.core / "run.metta"),
               "commchannel=file-shadow" if args.file_channel else "commchannel=mock",
               f"provider={args.provider}", "maxNewInputLoops=4", "maxWakeLoops=0",
               "onlyOnNewInput=True", "sleepInterval=0", "maxOutputToken=1400", "embeddingprovider=Local",
               "securityPolicyPath="]
    server = None if args.file_channel else CommMockServer((LOCALHOST, COMM_MOCK_PORT))
    llm_controller = (LlmMockController((LOCALHOST, LLM_MOCK_PORT))
                      if args.provider == "Test" else None)
    history_path = args.core / "memory" / "history.metta"
    history_offset = history_path.stat().st_size if history_path.exists() else 0
    # The PeTTa loop is chatty.  Leaving its stdout unread until teardown can
    # fill a pipe and make a successful mock send look like a transport hang.
    # Use a temporary file and a separate process group so both capture and
    # shutdown remain bounded even if the shell wrapper forks SWI-Prolog.
    transcript_file = tempfile.TemporaryFile(mode="w+t", encoding="utf-8")
    process = subprocess.Popen(command, cwd=args.petta, env=env, text=True,
                               stdout=transcript_file, stderr=subprocess.STDOUT,
                               start_new_session=True)
    started = time.monotonic()
    transcript = ""
    rescued_after_early_exit = False
    try:
        if server is not None:
            deadline = started + min(45, args.timeout / 3)
            while time.monotonic() < deadline:
                try:
                    if server.ping(1):
                        break
                except Exception:
                    time.sleep(0.25)
            else:
                raise RuntimeError("OmegaClaw mock channel did not initialize")
        if llm_controller is not None:
            if not args.test_answer:
                raise RuntimeError("--provider Test requires --test-answer")
            llm_deadline = time.monotonic() + 15
            while time.monotonic() < llm_deadline:
                try:
                    if llm_controller.ping(1):
                        break
                except Exception:
                    time.sleep(0.25)
            else:
                raise RuntimeError("OmegaClaw Test provider did not initialize")
            if not llm_controller.set_answer(args.prompt, args.test_answer, timeout=5):
                raise RuntimeError("failed to register deterministic Test-provider response")
        if channel_directory is not None:
            # Publish input only after every responder dependency is ready.
            # Otherwise the fast file-channel loop can consume the prompt
            # before a deterministic provider fixture or bridge is prepared.
            (Path(channel_directory.name) / "input.txt").write_text(args.prompt, encoding="utf-8")
        if server is not None and not server.send_message(args.prompt, timeout=5):
            raise RuntimeError("failed to inject frozen prompt")
        deadline = started + args.timeout
        answer = ""
        while time.monotonic() < deadline:
            # A history entry is evidence that the MeTTa loop emitted a send
            # command, not evidence of delivery.  Count a response only after
            # the isolated mock server acknowledges and captures it.
            if server is not None:
                answer = server.getLastMessage()
            else:
                output_path = Path(channel_directory.name) / "output.txt"
                output_answer = (
                    output_path.read_text(encoding="utf-8")
                    if output_path.exists() else ""
                )
                authenticated_answer = None
                if args.live_transport and bridge_directory is not None:
                    bridge_response = Path(bridge_directory.name) / "response.json"
                    authenticated_answer = read_bridge_raw_answer(
                        bridge_response, request_id=bridge_request_id,
                        prompt_sha256=bridge_prompt_sha256, session=args.session,
                        secret=bridge_secret,
                    )
                child_returncode = process.poll()
                answer, exited_with_answer = select_polled_answer(
                    live_transport=args.live_transport,
                    output_answer=output_answer,
                    authenticated_answer=authenticated_answer,
                    child_returncode=child_returncode,
                )
                rescued_after_early_exit |= exited_with_answer
            if answer:
                break
            child_returncode = process.poll()
            if child_returncode is not None:
                # The PeTTa process can exit during finalization just as the
                # separately owned bridge atomically publishes a valid answer.
                # Give that immutable handoff a short bounded grace.
                if args.live_transport and bridge_directory is not None:
                    bridge_response = Path(bridge_directory.name) / "response.json"
                    answer = await_bridge_answer_after_exit(
                        bridge_response, request_id=bridge_request_id,
                        prompt_sha256=bridge_prompt_sha256, session=args.session,
                        secret=bridge_secret,
                    )
                    if answer:
                        rescued_after_early_exit = True
                        break
                raise RuntimeError(f"OmegaClaw exited early with {process.returncode}")
            time.sleep(0.25)
        if not answer:
            raise TimeoutError("OmegaClaw produced no send result before timeout")
        emit_case_answer(
            answer, started=started, command=command,
            rescued_after_early_exit=rescued_after_early_exit,
        )
        return 0
    finally:
        # Both commands own dedicated sessions and may fork descendants whose
        # group leaders exit first. Always drain the groups at turn teardown.
        terminate_process_group(process)
        if server is not None:
            server.stop(5)
        if llm_controller is not None:
            llm_controller.stop(5)
        if bridge_process is not None:
            terminate_process_group(bridge_process)
        if bridge_log is not None:
            bridge_log.seek(0)
            print("OMEGACLAW_BRIDGE_LOG", file=sys.stderr)
            print(bridge_log.read()[-4000:], file=sys.stderr)
            bridge_log.close()
        if bridge_directory is not None:
            bridge_directory.cleanup()
        if live_request_path is not None:
            try: os.unlink(live_request_path)
            except FileNotFoundError: pass
        if channel_directory is not None:
            channel_directory.cleanup()
        transcript_file.seek(0)
        transcript = transcript_file.read()
        transcript_file.close()
        print("OMEGACLAW_TRANSCRIPT_BEGIN", file=sys.stderr)
        print(transcript[-20000:], file=sys.stderr)
        print("OMEGACLAW_TRANSCRIPT_END", file=sys.stderr)
        # A captured mock answer is not a passing gate if SWI/PeTTa emitted a
        # fatal native crash while the harness was shutting it down.  Raise
        # after preserving the transcript so callers cannot mistake exit 0
        # for runtime stability.
        if "fatal signal" in transcript.lower() or "(segv)" in transcript.lower():
            raise RuntimeError("OmegaClaw transcript contains a fatal native crash")


if __name__ == "__main__":
    raise SystemExit(main())
