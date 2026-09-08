import fcntl
import hashlib
import os
from pathlib import Path
import subprocess


SCRIPT = Path(__file__).parents[1] / "projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh"


LEGACY_BODY = '''
trap "exit 0" TERM INT
while true; do
  echo "starting OmegaClaw Telegram runner" >/dev/null
  true "$RUNNER"
  rc=0
  echo "OmegaClaw Telegram runner exited with status $rc; restarting in 5s" >/dev/null
  sleep 1
done
'''


def command_hash(pid):
    return hashlib.sha256(Path(f"/proc/{pid}/cmdline").read_bytes()).hexdigest()


def invoke(pid_file, command, **extra):
    env = os.environ.copy()
    env.update(
        OMEGACLAW_LEGACY_PID_FILE=str(pid_file),
        OMEGACLAW_CUTOVER_LOCK=str(pid_file.parent / "cutover.lock"),
        OMEGACLAW_TELEGRAM_ENV=str(pid_file.parent / "absent.env"),
        **extra,
    )
    return subprocess.run([str(SCRIPT), command], env=env, text=True, capture_output=True)


def test_real_start_does_not_leave_cutover_lock_in_long_lived_owner(tmp_path):
    runner = tmp_path / "runner.sh"
    runner.write_text("#!/bin/sh\ntrap 'exit 0' TERM INT\nwhile :; do sleep 1; done\n")
    runner.chmod(0o700)
    pid_file = tmp_path / "state" / "legacy.pid"
    pid_file.parent.mkdir()
    env = dict(
        OMEGACLAW_LEGACY_RUNNER=str(runner),
        OMEGACLAW_LEGACY_STATE_DIR=str(pid_file.parent),
        OMEGACLAW_LEGACY_LOG_DIR=str(tmp_path / "logs"),
        OMEGACLAW_TG_BOT_TOKEN="fixture-token",
    )
    started = invoke(pid_file, "start", **env)
    assert started.returncode == 0, started.stderr
    owner = int(pid_file.read_text())
    try:
        assert Path(f"/proc/{owner}").exists()
        lock_path = pid_file.parent / "cutover.lock"
        with lock_path.open("w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    finally:
        stopped = invoke(pid_file, "stop", **env)
        assert stopped.returncode == 0, stopped.stderr


def test_bind_current_identity_and_status_bind_start_time_and_command(tmp_path):
    proc = subprocess.Popen(["bash", "-c", LEGACY_BODY], preexec_fn=os.setsid)
    pid_file = tmp_path / "legacy.pid"
    try:
        pid_file.write_text(f"{proc.pid}\n")
        result = invoke(
            pid_file,
            "bind-current-identity",
            OMEGACLAW_LEGACY_BIND_PID=str(proc.pid),
            OMEGACLAW_LEGACY_BIND_START_TICKS=Path(f"/proc/{proc.pid}/stat").read_text().split()[21],
            OMEGACLAW_LEGACY_BIND_CMDLINE_SHA256=command_hash(proc.pid),
        )
        assert result.returncode == 0, result.stderr
        identity = Path(f"{pid_file}.identity")
        fields = identity.read_text().split()
        assert fields[0] == str(proc.pid)
        assert fields[1] == Path(f"/proc/{proc.pid}/stat").read_text().split()[21]
        assert fields[2] == command_hash(proc.pid)

        fields[1] = str(int(fields[1]) + 1)
        identity.write_text(" ".join(fields) + "\n")
        assert invoke(pid_file, "status").returncode == 0
        assert "inactive" in invoke(pid_file, "status").stdout
    finally:
        if proc.poll() is None:
            os.killpg(proc.pid, 9)
            proc.wait(timeout=5)


def test_bind_rejects_wrong_expected_command_hash(tmp_path):
    proc = subprocess.Popen(["bash", "-c", LEGACY_BODY], preexec_fn=os.setsid)
    pid_file = tmp_path / "legacy.pid"
    try:
        pid_file.write_text(f"{proc.pid}\n")
        result = invoke(
            pid_file,
            "bind-current-identity",
            OMEGACLAW_LEGACY_BIND_PID=str(proc.pid),
            OMEGACLAW_LEGACY_BIND_START_TICKS=Path(f"/proc/{proc.pid}/stat").read_text().split()[21],
            OMEGACLAW_LEGACY_BIND_CMDLINE_SHA256="0" * 64,
        )
        assert result.returncode == 1
        assert not Path(f"{pid_file}.identity").exists()
    finally:
        if proc.poll() is None:
            os.killpg(proc.pid, 9)
            proc.wait(timeout=5)


def test_stop_refuses_unbound_pid_target(tmp_path):
    pid_file = tmp_path / "legacy.pid"
    pid_file.write_text(f"{os.getpid()}\n")
    result = invoke(pid_file, "stop")
    assert result.returncode == 1
    assert "refusing to signal" in result.stderr


def test_bind_rejects_observed_start_time_mismatch(tmp_path):
    proc = subprocess.Popen(["bash", "-c", LEGACY_BODY], preexec_fn=os.setsid)
    pid_file = tmp_path / "legacy.pid"
    try:
        pid_file.write_text(f"{proc.pid}\n")
        actual_start = int(Path(f"/proc/{proc.pid}/stat").read_text().split()[21])
        result = invoke(
            pid_file,
            "bind-current-identity",
            OMEGACLAW_LEGACY_BIND_PID=str(proc.pid),
            OMEGACLAW_LEGACY_BIND_START_TICKS=str(actual_start + 1),
            OMEGACLAW_LEGACY_BIND_CMDLINE_SHA256=command_hash(proc.pid),
        )
        assert result.returncode == 1
        assert "start-time mismatch" in result.stderr
        assert not Path(f"{pid_file}.identity").exists()
    finally:
        if proc.poll() is None:
            os.killpg(proc.pid, 9)
            proc.wait(timeout=5)


def test_bind_is_rejected_while_cutover_lock_is_held(tmp_path):
    pid_file = tmp_path / "legacy.pid"
    pid_file.write_text(f"{os.getpid()}\n")
    lock_path = tmp_path / "cutover.lock"
    with lock_path.open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        result = invoke(
            pid_file,
            "bind-current-identity",
            OMEGACLAW_LEGACY_BIND_PID=str(os.getpid()),
            OMEGACLAW_LEGACY_BIND_START_TICKS=Path(f"/proc/{os.getpid()}/stat").read_text().split()[21],
            OMEGACLAW_LEGACY_BIND_CMDLINE_SHA256=command_hash(os.getpid()),
        )
    assert result.returncode == 1
    assert "cutover in progress" in result.stderr
