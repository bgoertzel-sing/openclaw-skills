import importlib.util
import json
import os
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest


RUNTIME_PROMPT = (
    Path(__file__).resolve().parents[2]
    / "protocosmo2"
    / "phase2-checked-baseline"
    / "repos"
    / "PeTTa"
    / "repos"
    / "OmegaClaw-Core"
    / "memory"
    / "prompt.txt"
)
RUNTIME_HISTORY = RUNTIME_PROMPT.with_name("history.metta")
RUNNER = Path(__file__).resolve().parents[1] / "tools" / "phase6_private_canary_runner.py"
BRIDGE = Path(__file__).resolve().parents[1] / "tools" / "phase5_openclaw_bridge.py"
CASE = Path(__file__).resolve().parents[1] / "tools" / "phase5_omegaclaw_case.py"
RUNNER_SPEC = importlib.util.spec_from_file_location("phase6_runner_test", RUNNER)
RUNNER_MODULE = importlib.util.module_from_spec(RUNNER_SPEC)
assert RUNNER_SPEC.loader is not None
RUNNER_SPEC.loader.exec_module(RUNNER_MODULE)
CASE_SPEC = importlib.util.spec_from_file_location("phase5_case_test", CASE)
CASE_MODULE = importlib.util.module_from_spec(CASE_SPEC)
assert CASE_SPEC.loader is not None
CASE_SPEC.loader.exec_module(CASE_MODULE)


def test_production_prompt_declares_live_bounded_telegram_capabilities():
    text = RUNTIME_PROMPT.read_text(encoding="utf-8")
    assert text.startswith("# ProtoCosmo2 live Telegram runtime contract\n")
    assert "This is an offline behavioral evaluation" not in text
    assert "shadow-only runtime contract" not in text
    assert "Native PDF" in text
    assert "MEDIA:/absolute/path" in text
    assert "correlated receipt" in text


def test_production_history_begins_with_explicit_live_transition():
    text = RUNTIME_HISTORY.read_text(encoding="utf-8")
    assert "SYSTEM_TRANSITION: Phase-5 shadow evaluation history was retired" in text
    assert "now uses live Telegram ingress and bounded reply/document delivery" in text


def test_inner_file_channel_is_explicitly_declared_an_implementation_boundary():
    text = RUNNER.read_text(encoding="utf-8")
    assert "This is a live Telegram request" in text
    assert "implementation containment boundary only" in text
    assert "Never describe this inner boundary as shadow mode" in text
    assert "outer Bot-API" in text


def test_live_runner_selects_live_bridge_contract_not_phase5_shadow_contract():
    assert '"--live-transport"' in RUNNER.read_text(encoding="utf-8")
    assert 'parser.add_argument("--live-transport"' in CASE.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")
    assert "LIVE TELEGRAM TRANSPORT NOTE" in bridge
    assert "transport_instruction(live_transport)" in bridge


def test_live_runner_owns_and_cleans_up_inner_process_group():
    text = RUNNER.read_text(encoding="utf-8")
    assert "start_new_session=True" in text
    assert "os.killpg(process.pid, 15)" in text
    assert "omegaclaw_runtime_timeout" in text


def test_live_runner_preserves_bounded_private_responder_diagnostic():
    text = RUNNER.read_text(encoding="utf-8")
    assert "stderr=subprocess.PIPE" in text
    assert '"stderr_sha256"' in text
    assert '"stderr_bytes"' in text
    assert '"stderr_tail"' not in text
    assert 'os.O_NOFOLLOW' in text
    assert 'os.O_NONBLOCK' in text
    assert 'stat.S_ISREG' in text
    assert 'info.st_nlink != 1' in text
    assert 'stat.S_IMODE(info.st_mode) != 0o600' in text
    assert 'responder-incidents.jsonl' in text


def test_responder_incident_is_private_regular_and_does_not_persist_stderr(tmp_path):
    path = tmp_path / "incident.jsonl"
    secret = "super-secret-provider-token"
    RUNNER_MODULE.append_responder_incident(path, returncode=7, stderr=f"failure {secret}")
    assert path.stat().st_mode & 0o777 == 0o600
    record = json.loads(path.read_text(encoding="ascii"))
    assert record["returncode"] == 7
    assert record["stderr_bytes"] > 0
    assert len(record["stderr_sha256"]) == 64
    assert secret not in path.read_text(encoding="ascii")


def test_responder_incident_rejects_fifo_and_permissive_existing_file(tmp_path):
    fifo = tmp_path / "fifo"
    os.mkfifo(fifo, 0o600)
    with pytest.raises((OSError, RuntimeError)):
        RUNNER_MODULE.append_responder_incident(fifo, returncode=1, stderr="failure")
    permissive = tmp_path / "permissive.jsonl"
    permissive.write_text("", encoding="ascii")
    permissive.chmod(0o644)
    with pytest.raises(RuntimeError, match="unsafe_responder_incident_file"):
        RUNNER_MODULE.append_responder_incident(permissive, returncode=1, stderr="failure")
    linked = tmp_path / "linked.jsonl"
    linked.write_text("", encoding="ascii")
    linked.chmod(0o600)
    os.link(linked, tmp_path / "linked-alias.jsonl")
    with pytest.raises(RuntimeError, match="unsafe_responder_incident_file"):
        RUNNER_MODULE.append_responder_incident(linked, returncode=1, stderr="failure")


def test_protomega_bridge_routes_through_explicit_agent_identity():
    runner = RUNNER.read_text(encoding="utf-8")
    case = CASE.read_text(encoding="utf-8")
    bridge = BRIDGE.read_text(encoding="utf-8")
    assert '"--agent", args.agent_id' in runner
    assert 'parser.add_argument("--agent")' in case
    assert '["--agent", agent]' in bridge


def test_production_supervisor_has_schema_compatible_deferred_rollback_mode():
    runner = RUNNER.read_text(encoding="utf-8")
    supervisor = (Path(__file__).resolve().parents[2] / "local" /
                  "protomega-outer-telegram-supervisor.sh").read_text(encoding="utf-8")
    assert 'parser.add_argument("--disable-deferred-jobs", action="store_true"' in runner
    assert "if not args.disable_deferred_jobs:" in runner
    assert "deferred_responder=deferred_callback" in runner
    assert "OMEGACLAW_OUTER_DEFERRED_DISABLE_MARKER" in supervisor
    assert "deferred_args+=(--disable-deferred-jobs)" in supervisor
    assert "os.O_EXCL" in supervisor
    assert 'getattr(os, "O_NOFOLLOW", 0)' in supervisor
    assert "stat.S_IMODE(info.st_mode) != 0o600" in supervisor
    assert "info.st_nlink != 1" in supervisor


def test_production_supervisor_creates_and_validates_private_rollback_marker(tmp_path):
    supervisor = Path(__file__).resolve().parents[2] / "local" / "protomega-outer-telegram-supervisor.sh"
    marker = tmp_path / "rollback.marker"
    env = os.environ.copy()
    env["OMEGACLAW_OUTER_DEFERRED_DISABLE_MARKER"] = str(marker)
    created = subprocess.run(
        [str(supervisor), "enable-sync-rollback"], env=env,
        text=True, capture_output=True, check=False,
    )
    assert created.returncode == 0, created.stderr
    info = marker.stat()
    assert info.st_mode & 0o777 == 0o600
    assert info.st_nlink == 1
    validated = subprocess.run(
        [str(supervisor), "validate-sync-rollback"], env=env,
        text=True, capture_output=True, check=False,
    )
    assert validated.returncode == 0, validated.stderr


def test_production_supervisor_rejects_symlink_and_hardlinked_rollback_markers(tmp_path):
    supervisor = Path(__file__).resolve().parents[2] / "local" / "protomega-outer-telegram-supervisor.sh"
    target = tmp_path / "target"
    target.write_text("", encoding="ascii")
    target.chmod(0o600)
    marker = tmp_path / "marker"
    marker.symlink_to(target)
    env = os.environ.copy()
    env["OMEGACLAW_OUTER_DEFERRED_DISABLE_MARKER"] = str(marker)
    symlinked = subprocess.run(
        [str(supervisor), "enable-sync-rollback"], env=env,
        text=True, capture_output=True, check=False,
    )
    assert symlinked.returncode != 0
    marker.unlink()
    os.link(target, marker)
    hardlinked = subprocess.run(
        [str(supervisor), "validate-sync-rollback"], env=env,
        text=True, capture_output=True, check=False,
    )
    assert hardlinked.returncode != 0


def test_case_reads_large_private_prompt_file_and_rejects_unsafe_file(tmp_path):
    prompt_path = tmp_path / "prompt.txt"
    prompt = "document text\n" * 50_000
    prompt_path.write_text(prompt, encoding="utf-8")
    prompt_path.chmod(0o600)
    assert CASE_MODULE.read_prompt(None, prompt_path) == prompt
    prompt_path.chmod(0o644)
    with pytest.raises(RuntimeError, match="must not be accessible"):
        CASE_MODULE.read_prompt(None, prompt_path)
    with pytest.raises(RuntimeError, match="exactly one"):
        CASE_MODULE.read_prompt("inline", prompt_path)


def test_case_fails_closed_when_path_is_substituted_after_open(tmp_path, monkeypatch):
    prompt_path = tmp_path / "prompt.txt"
    replacement = tmp_path / "replacement.txt"
    prompt_path.write_text("ORIGINAL", encoding="utf-8")
    replacement.write_text("REPLACEMENT", encoding="utf-8")
    prompt_path.chmod(0o600)
    replacement.chmod(0o600)
    real_open = CASE_MODULE.os.open

    def open_then_replace(path, flags):
        fd = real_open(path, flags)
        Path(path).unlink()
        Path(path).symlink_to(replacement)
        return fd

    monkeypatch.setattr(CASE_MODULE.os, "open", open_then_replace)
    with pytest.raises(RuntimeError, match="private regular file"):
        CASE_MODULE.read_prompt(None, prompt_path)


def test_private_prompt_write_failure_removes_partial_file(tmp_path, monkeypatch):
    created = tmp_path / "partial.txt"

    class FailingPrompt:
        name = str(created)

        def write(self, text):
            created.write_text(text, encoding="utf-8")

        def flush(self):
            raise OSError("injected flush failure")

        def fileno(self):
            return 99

        def close(self):
            return None

    monkeypatch.setattr(RUNNER_MODULE.tempfile, "NamedTemporaryFile", lambda *a, **k: FailingPrompt())
    with pytest.raises(OSError, match="injected flush failure"):
        RUNNER_MODULE.write_private_prompt("sensitive document")
    assert not created.exists()


def test_responder_transfers_large_prompt_by_private_file_not_argv(tmp_path, monkeypatch):
    observed = {}

    class FakeProcess:
        returncode = 0
        pid = 999999

        def __init__(self, command, **_kwargs):
            observed["command"] = command
            prompt_path = Path(command[command.index("--prompt-file") + 1])
            observed["prompt_path"] = prompt_path
            observed["prompt_mode"] = prompt_path.stat().st_mode & 0o777
            observed["prompt_size"] = prompt_path.stat().st_size

        def communicate(self, timeout):
            observed["timeout"] = timeout
            return json.dumps({"status": "ok", "answer": "LARGE-OK"}) + "\n", ""

        def poll(self):
            return self.returncode

    monkeypatch.setattr(RUNNER_MODULE.subprocess, "Popen", FakeProcess)
    worker_state = tmp_path / "worker"
    worker_state.mkdir(mode=0o700)
    args = SimpleNamespace(
        worker_state_dir=worker_state,
        driver=tmp_path / "driver.py",
        petta=tmp_path / "petta",
        core=tmp_path / "core",
        session_prefix="large-regression",
        model="anthropic/claude-opus-4-6",
        provider_timeout=10,
        agent_id="protomegabot-opus",
    )
    large_prompt = "PDF-LINE\n" * 80_000
    assert RUNNER_MODULE.responder(large_prompt, args, "task-large") == "LARGE-OK"
    command = observed["command"]
    assert "--prompt" not in command
    assert large_prompt not in command
    assert observed["prompt_mode"] == 0o600
    assert observed["prompt_size"] > 500_000
    assert not observed["prompt_path"].exists()


def responder_args(tmp_path):
    worker_state = tmp_path / "worker"
    worker_state.mkdir(mode=0o700)
    return SimpleNamespace(
        worker_state_dir=worker_state,
        driver=tmp_path / "driver.py",
        petta=tmp_path / "petta",
        core=tmp_path / "core",
        session_prefix="post-answer-regression",
        model="openai/gpt-5.6-sol",
        provider_timeout=10,
        agent_id="main",
    )


def fake_completed_process(*, returncode, stdout, stderr):
    class FakeProcess:
        pid = 999999

        def __init__(self, _command, **_kwargs):
            self.returncode = returncode

        def communicate(self, timeout):
            assert timeout == 40
            return stdout, stderr

        def poll(self):
            return self.returncode

    return FakeProcess


def test_responder_preserves_valid_answer_after_post_answer_runtime_failure(tmp_path, monkeypatch):
    stdout = json.dumps({"status": "ok", "answer": "HANDOFF-READY"}) + "\n"
    monkeypatch.setattr(
        RUNNER_MODULE.subprocess, "Popen",
        fake_completed_process(returncode=1, stdout=stdout, stderr="fatal after bridge handoff"),
    )
    args = responder_args(tmp_path)
    assert RUNNER_MODULE.responder("message 848", args) == "HANDOFF-READY"
    incident = json.loads((args.worker_state_dir / "responder-incidents.jsonl").read_text())
    assert incident["returncode"] == 1
    assert incident["stderr_bytes"] > 0


def test_responder_rejects_malformed_answer_after_runtime_failure(tmp_path, monkeypatch):
    stdout = json.dumps({"status": "ok", "answer": '(send "one") (send "two")'}) + "\n"
    monkeypatch.setattr(
        RUNNER_MODULE.subprocess, "Popen",
        fake_completed_process(returncode=1, stdout=stdout, stderr="failed after malformed output"),
    )
    args = responder_args(tmp_path)
    with pytest.raises(RuntimeError, match="unsafe_send_wrapper"):
        RUNNER_MODULE.responder("message 848 malformed", args)
    assert (args.worker_state_dir / "responder-incidents.jsonl").is_file()


def test_responder_still_fails_closed_when_nonzero_exit_has_no_answer(tmp_path, monkeypatch):
    monkeypatch.setattr(
        RUNNER_MODULE.subprocess, "Popen",
        fake_completed_process(returncode=1, stdout="diagnostic only\n", stderr="runtime failed"),
    )
    args = responder_args(tmp_path)
    with pytest.raises(RuntimeError, match="omegaclaw_runtime_failure"):
        RUNNER_MODULE.responder("message 848 no result", args)
    assert (args.worker_state_dir / "responder-incidents.jsonl").is_file()
