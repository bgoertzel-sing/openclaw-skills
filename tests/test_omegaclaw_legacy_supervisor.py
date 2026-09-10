import fcntl
import os
import subprocess
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "projects/omegaclaw/local/omegaclaw-telegram-private-supervisor.sh"


def test_direct_legacy_start_and_stop_rejected_during_cutover(tmp_path):
    lock_path = tmp_path / "cutover.lock"
    env = os.environ.copy()
    env.update(
        OMEGACLAW_CUTOVER_LOCK=str(lock_path),
        OMEGACLAW_LEGACY_PID_FILE=str(tmp_path / "legacy.pid"),
        OMEGACLAW_TELEGRAM_ENV=str(tmp_path / "missing.env"),
    )
    with open(lock_path, "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        start = subprocess.run([str(SCRIPT), "start"], env=env, text=True, capture_output=True)
        stop = subprocess.run([str(SCRIPT), "stop"], env=env, text=True, capture_output=True)
    assert start.returncode == 1
    assert stop.returncode == 1
    assert "cutover in progress" in start.stderr
    assert "cutover in progress" in stop.stderr
