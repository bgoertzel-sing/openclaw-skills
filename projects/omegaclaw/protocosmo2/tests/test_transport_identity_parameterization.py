import importlib.util
import json
import os
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "worktrees" / "protocosmo2-phase6-live"
sys.path.insert(0, str(CORE))

from channels.private_canary import CanaryContract, ConfigError, load_config
from channels.private_canary_telegram import PrivateCanaryTelegramTransport, _safe_update

RUNNER_PATH = ROOT / "protocosmo2" / "tools" / "phase6_private_canary_runner.py"
_runner_spec = importlib.util.spec_from_file_location("phase6_private_canary_runner", RUNNER_PATH)
assert _runner_spec and _runner_spec.loader
runner = importlib.util.module_from_spec(_runner_spec)
_runner_spec.loader.exec_module(runner)


def _config(tmp_path: Path, identity: str) -> Path:
    path = tmp_path / "config.json"
    path.write_text(json.dumps({
        "schema_version": 2, "identity": identity,
        "allowed_chat_ids": [402314199], "allowed_user_ids": [402314199],
        "allow_all_group_chats": False, "allow_all_group_users": False,
        "max_outbound_messages": 10, "rate_window_seconds": 60,
        "max_reply_depth": 1, "max_text_chars": 2000,
        "attachments": "extract_text", "autonomous_schedules": False,
        "state_changing_extras": False,
    }), encoding="utf-8")
    return path


def test_nondefault_identity_and_failure_text(tmp_path):
    config = load_config(_config(tmp_path, "ProtomegaTron"), expected_identity="ProtomegaTron")
    contract = CanaryContract(config, tmp_path / "state")
    admitted = contract.admit_inbound({
        "update_id": 4, "message_id": 8, "chat_id": 402314199,
        "user_id": 402314199, "text": "hello", "reply_depth": 0,
        "attachments": [],
    }, now=100)
    assert admitted["status"] == "accepted"
    queued = contract.fail_inbound("fixture", now=101)
    assert queued["outbox"]["text"].startswith("ProtomegaTron could not complete")


def test_identity_mismatch_fails_closed(tmp_path):
    path = _config(tmp_path, "ProtoCosmo2")
    try:
        load_config(path, expected_identity="ProtomegaTron")
    except ConfigError:
        pass
    else:
        raise AssertionError("identity mismatch accepted")


def test_addressing_uses_selected_bot_identity():
    raw = {"update_id": 7, "message": {
        "message_id": 9, "chat": {"id": -123},
        "from": {"id": 402314199, "is_bot": False},
        "text": "@Protomegabot hello",
    }}
    parsed = _safe_update(raw, bot_id=8562797306, bot_username="@Protomegabot")
    assert parsed is not None and parsed["addressed"] is True
    other = _safe_update(raw, bot_id=8716054285, bot_username="@protocosmo2bot")
    assert other is not None and other["addressed"] is False


class _Api:
    pass


def test_transport_rejects_invalid_identity_parameters(tmp_path):
    config = load_config(_config(tmp_path, "ProtomegaTron"), expected_identity="ProtomegaTron")
    contract = CanaryContract(config, tmp_path / "state")
    try:
        PrivateCanaryTelegramTransport(contract, _Api(), lambda _: "ok", bot_id=0,
                                       bot_username="@Protomegabot", attachment_label="ProtomegaTron")
    except ValueError:
        pass
    else:
        raise AssertionError("invalid bot id accepted")


def test_read_env_accepts_shell_export_syntax(tmp_path):
    env = tmp_path / "telegram.env"
    env.write_text("export OMEGACLAW_TG_BOT_TOKEN=fixture-token\n", encoding="utf-8")
    env.chmod(0o600)
    values = runner.read_env(env)
    assert values["TG_BOT_TOKEN"] == "fixture-token"


def test_receiver_parent_binding_rejects_wrong_parent(monkeypatch):
    monkeypatch.setenv("OMEGACLAW_EXPECTED_PARENT_PID", str(os.getppid() + 100000))
    try:
        runner.arm_parent_death_signal()
    except RuntimeError as exc:
        assert "parent identity mismatch" in str(exc)
    else:
        raise AssertionError("wrong receiver parent accepted")


def _chroma_with_dimension(tmp_path: Path, dimension: int | None) -> Path:
    root = tmp_path / f"chroma-{dimension}"
    root.mkdir()
    with sqlite3.connect(root / "chroma.sqlite3") as connection:
        connection.execute("CREATE TABLE collections (name TEXT, dimension INTEGER)")
        connection.execute(
            "INSERT INTO collections(name, dimension) VALUES (?, ?)",
            ("memories", dimension),
        )
    return root


def test_receiver_chroma_preflight_accepts_fresh_and_384_dimension(tmp_path):
    runner.validate_live_chroma_dimension(tmp_path / "fresh")
    runner.validate_live_chroma_dimension(_chroma_with_dimension(tmp_path, None))
    runner.validate_live_chroma_dimension(_chroma_with_dimension(tmp_path, 384))


def test_receiver_chroma_preflight_rejects_probe_dimension(tmp_path):
    try:
        runner.validate_live_chroma_dimension(_chroma_with_dimension(tmp_path, 3))
    except RuntimeError as exc:
        assert str(exc) == "live Chroma embedding dimension mismatch"
    else:
        raise AssertionError("three-dimensional activation-probe store accepted")


def test_receiver_dies_when_bound_parent_exits(tmp_path):
    child_pid = tmp_path / "child.pid"
    code = (
        "import importlib.util, os, pathlib, time; "
        f"s=importlib.util.spec_from_file_location('r', {str(RUNNER_PATH)!r}); "
        "m=importlib.util.module_from_spec(s); s.loader.exec_module(m); "
        "os.environ['OMEGACLAW_EXPECTED_PARENT_PID']=str(os.getppid()); "
        "m.arm_parent_death_signal(); "
        f"pathlib.Path({str(child_pid)!r}).write_text(str(os.getpid())); "
        "time.sleep(30)"
    )
    parent = subprocess.Popen(["bash", "-c", f"python3 -c {json.dumps(code)} & while [ ! -f {child_pid} ]; do sleep 0.01; done"])
    parent.wait(timeout=5)
    pid = int(child_pid.read_text())
    for _ in range(100):
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            break
        stat = Path(f"/proc/{pid}/stat")
        if not stat.exists() or stat.read_text().split()[2] == "Z":
            break
        time.sleep(0.02)
    else:
        os.kill(pid, 9)
        raise AssertionError("receiver survived bound parent exit")
