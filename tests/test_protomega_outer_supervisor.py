import os
import subprocess
import fcntl
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "projects/omegaclaw/local/protomega-outer-telegram-supervisor.sh"


def process_start(pid):
    return Path(f"/proc/{pid}/stat").read_text().split()[21]


def command_hash(pid):
    import hashlib
    return hashlib.sha256(Path(f"/proc/{pid}/cmdline").read_bytes()).hexdigest()


def invoke(pid_file, command, **extra):
    env = os.environ.copy()
    env["OMEGACLAW_OUTER_PID_FILE"] = str(pid_file)
    env["OMEGACLAW_CUTOVER_LOCK"] = str(pid_file.parent / "cutover.lock")
    env.update(extra)
    return subprocess.run([str(SCRIPT), command], env=env, text=True, capture_output=True)


def test_real_start_does_not_leave_cutover_lock_in_long_lived_owner(tmp_path):
    env_file = tmp_path / "fixture.env"
    config = tmp_path / "fixture.json"
    log = tmp_path / "outer.log"
    env_file.write_text("FIXTURE=1\n")
    config.write_text("{}\n")
    runner = tmp_path / "runner.py"
    runner.write_text("import signal, time\nsignal.signal(signal.SIGTERM, lambda *_: exit(0))\nwhile True: time.sleep(1)\n")
    pid_file = tmp_path / "outer.pid"
    extra = dict(
        OMEGACLAW_OUTER_ENV_FILE=str(env_file),
        OMEGACLAW_OUTER_CONFIG=str(config),
        OMEGACLAW_OUTER_LOG=str(log),
        OMEGACLAW_OUTER_RUNNER=str(runner),
        OMEGACLAW_OUTER_STATE_DIR=str(tmp_path / "transport-state"),
        OMEGACLAW_OUTER_WORKER_STATE_DIR=str(tmp_path / "worker-state"),
    )
    started = invoke(pid_file, "start", **extra)
    assert started.returncode == 0, started.stderr
    owner = int(pid_file.read_text())
    try:
        assert Path(f"/proc/{owner}").exists()
        lock_path = pid_file.parent / "cutover.lock"
        with lock_path.open("w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        start_lock_path = Path(f"{pid_file}.start.lock")
        with start_lock_path.open("w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    finally:
        stopped = invoke(pid_file, "stop", **extra)
        assert stopped.returncode == 0, stopped.stderr


def test_owner_alive_binds_pid_start_time_and_command(tmp_path):
    proc = subprocess.Popen(
        ["bash", "-c", "while :; do sleep 1; done", str(SCRIPT), "run"]
    )
    try:
        pid_file = tmp_path / "outer.pid"
        pid_file.write_text(f"{proc.pid}\n")
        Path(f"{pid_file}.identity").write_text(f"{proc.pid} {process_start(proc.pid)} {command_hash(proc.pid)}\n")
        assert invoke(pid_file, "owner-alive").returncode == 0

        Path(f"{pid_file}.identity").write_text(f"{proc.pid} {int(process_start(proc.pid)) + 1} {command_hash(proc.pid)}\n")
        assert invoke(pid_file, "owner-alive").returncode == 1

        Path(f"{pid_file}.identity").write_text(f"{proc.pid} {process_start(proc.pid)} {'0' * 64}\n")
        assert invoke(pid_file, "owner-alive").returncode == 1
    finally:
        proc.terminate()
        proc.wait(timeout=5)


def test_owner_alive_rejects_pid_file_symlink(tmp_path):
    target = tmp_path / "target"
    target.write_text(f"{os.getpid()}\n")
    pid_file = tmp_path / "outer.pid"
    pid_file.symlink_to(target)
    Path(f"{pid_file}.identity").write_text(f"{os.getpid()} {process_start(os.getpid())} {command_hash(os.getpid())}\n")
    assert invoke(pid_file, "owner-alive").returncode == 1


def test_direct_start_is_rejected_while_cutover_lock_is_held(tmp_path):
    pid_file = tmp_path / "outer.pid"
    lock_path = tmp_path / "cutover.lock"
    with open(lock_path, "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        result = invoke(pid_file, "start")
    assert result.returncode == 1
    assert "cutover in progress" in result.stderr
    assert not pid_file.exists()


def test_direct_stop_is_rejected_while_cutover_lock_is_held(tmp_path):
    pid_file = tmp_path / "outer.pid"
    lock_path = tmp_path / "cutover.lock"
    with open(lock_path, "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        result = invoke(pid_file, "stop")
    assert result.returncode == 1
    assert "cutover in progress" in result.stderr


def test_stop_terminates_bound_owner_group_and_removes_identity(tmp_path):
    proc = subprocess.Popen(
        ["bash", "-c", "trap 'exit 0' TERM; while :; do sleep 1; done", str(SCRIPT), "run"],
        preexec_fn=os.setsid,
    )
    pid_file = tmp_path / "outer.pid"
    try:
        pid_file.write_text(f"{proc.pid}\n")
        identity = Path(f"{pid_file}.identity")
        identity.write_text(f"{proc.pid} {process_start(proc.pid)} {command_hash(proc.pid)}\n")
        result = invoke(pid_file, "stop")
        assert result.returncode == 0, result.stderr
        proc.wait(timeout=5)
        assert not pid_file.exists()
        assert not identity.exists()
    finally:
        if proc.poll() is None:
            os.killpg(proc.pid, 9)
            proc.wait(timeout=5)
