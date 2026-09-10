import os
import signal
import subprocess
import time
from pathlib import Path


ROOT = Path(__file__).parents[1]
WATCHDOG = ROOT / "bin" / "omegaclaw-watchdog.sh"
SUPERVISOR = ROOT / "projects/omegaclaw/local/protomega-outer-telegram-supervisor.sh"
REAL_RUNNER = ROOT / "projects/omegaclaw/protocosmo2/tools/phase6_private_canary_runner.py"


def _running(pid: int) -> bool:
    stat = Path(f"/proc/{pid}/stat")
    return stat.exists() and stat.read_text().split()[2] != "Z"


def _wait_not_running(pid: int) -> None:
    for _ in range(200):
        if not _running(pid):
            return
        time.sleep(0.02)
    raise AssertionError(f"process remained active: {pid}")


def _children(pid: int) -> list[int]:
    result = subprocess.run(
        ["ps", "-ww", "--ppid", str(pid), "-o", "pid=,args="], text=True, capture_output=True, check=True
    )
    return [
        int(line.split(None, 1)[0])
        for line in result.stdout.splitlines()
        if len(line.split(None, 1)) == 2
        and "phase6_private_canary_runner.py" in line
    ]


def _wait_one_child(pid: int) -> int:
    last = ""
    for _ in range(200):
        probe = subprocess.run(["ps", "-ww", "--ppid", str(pid), "-o", "pid=,args="], text=True, capture_output=True)
        last = probe.stdout
        children = _children(pid)
        if len(children) == 1:
            return children[0]
        time.sleep(0.02)
    raise AssertionError(f"owner did not reach one receiver child: {pid}; last={last!r}")


def test_sigkill_owner_recovers_outer_without_orphan_or_state_loss(tmp_path):
    pid_file = tmp_path / "outer.pid"
    env_file = tmp_path / "fixture.env"
    config = tmp_path / "fixture.json"
    state_dir = tmp_path / "transport-state"
    worker_state = tmp_path / "worker-state"
    log = tmp_path / "outer.log"
    runner = tmp_path / "phase6_private_canary_runner.py"
    legacy_calls = tmp_path / "legacy.calls"
    legacy = tmp_path / "legacy"
    env_file.write_text("FIXTURE=1\n")
    env_file.chmod(0o600)
    config.write_text("{}\n")
    state_dir.mkdir(mode=0o700)
    worker_state.mkdir(mode=0o700)
    sentinel = state_dir / "cursor-outbox.sentinel"
    sentinel.write_text("cursor=940522238 outbox=delivered\n")
    runner.write_text(
        "import importlib.util, signal, time\n"
        f"s=importlib.util.spec_from_file_location('real_runner', {str(REAL_RUNNER)!r})\n"
        "m=importlib.util.module_from_spec(s); s.loader.exec_module(m)\n"
        "m.arm_parent_death_signal()\n"
        "signal.signal(signal.SIGTERM, lambda *_: exit(0))\n"
        "while True: time.sleep(1)\n"
    )
    legacy.write_text(f"#!/bin/sh\necho \"$1\" >>{legacy_calls!s}\nexit 1\n")
    legacy.chmod(0o700)
    env = os.environ.copy()
    env.update(
        OMEGACLAW_OUTER_PID_FILE=str(pid_file),
        OMEGACLAW_OUTER_START_LOCK=str(tmp_path / "start.lock"),
        OMEGACLAW_CUTOVER_LOCK=str(tmp_path / "cutover.lock"),
        OMEGACLAW_OUTER_ENV_FILE=str(env_file),
        OMEGACLAW_OUTER_CONFIG=str(config),
        OMEGACLAW_OUTER_STATE_DIR=str(state_dir),
        OMEGACLAW_OUTER_WORKER_STATE_DIR=str(worker_state),
        OMEGACLAW_OUTER_LOG=str(log),
        OMEGACLAW_OUTER_RUNNER=str(runner),
        OMEGACLAW_WATCHDOG_SUPERVISOR=str(legacy),
        OMEGACLAW_WATCHDOG_OUTER_SUPERVISOR=str(SUPERVISOR),
        OMEGACLAW_WATCHDOG_PID_FILE=str(tmp_path / "legacy.pid"),
        OMEGACLAW_WATCHDOG_OUTER_PID_FILE=str(pid_file),
        OMEGACLAW_WATCHDOG_OUTER_STATE_DIR=str(state_dir),
        OMEGACLAW_WATCHDOG_LEASE_FILE=str(tmp_path / "lease"),
        OMEGACLAW_WATCHDOG_CUTOVER_LOCK=str(tmp_path / "cutover.lock"),
    )
    started = subprocess.run([str(SUPERVISOR), "start"], env=env, text=True, capture_output=True)
    assert started.returncode == 0, started.stderr
    first_owner = int(pid_file.read_text())
    try:
        first_child = _wait_one_child(first_owner)
        os.kill(first_owner, signal.SIGKILL)
        _wait_not_running(first_owner)
        _wait_not_running(first_child)
        recovered = subprocess.run([str(WATCHDOG), "check"], env=env, text=True, capture_output=True)
        assert recovered.returncode == 0, recovered.stderr
        assert "OUTER_RESTARTED" in recovered.stdout
        second_owner = int(pid_file.read_text())
        assert second_owner != first_owner
        _wait_one_child(second_owner)
        assert sentinel.read_text() == "cursor=940522238 outbox=delivered\n"
        assert not legacy_calls.exists()
    finally:
        subprocess.run([str(SUPERVISOR), "stop"], env=env, text=True, capture_output=True)
