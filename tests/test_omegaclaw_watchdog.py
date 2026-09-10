import os
import subprocess
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "bin" / "omegaclaw-watchdog.sh"


def run_watchdog(tmp_path, *args, pid_file=None, outer_pid_file=None):
    supervisor = tmp_path / "supervisor"
    outer_supervisor = tmp_path / "outer-supervisor"
    if not supervisor.exists():
        supervisor.write_text("#!/bin/sh\n[ \"$1\" = status ] && exit 0\nexit 1\n")
        supervisor.chmod(0o700)
    if not outer_supervisor.exists():
        outer_supervisor.write_text(
            "#!/bin/sh\n"
            "case \"$1\" in\n"
            "  owner-alive|status) [ -f \"$OMEGACLAW_WATCHDOG_OUTER_PID_FILE\" ] ;;\n"
            "  start) sleep 30 >/dev/null 2>&1 & echo $! >\"$OMEGACLAW_WATCHDOG_OUTER_PID_FILE\" ;;\n"
            "  *) exit 2 ;;\n"
            "esac\n"
        )
        outer_supervisor.chmod(0o700)
    env = os.environ.copy()
    env.update(
        OMEGACLAW_WATCHDOG_SUPERVISOR=str(supervisor),
        OMEGACLAW_WATCHDOG_OUTER_SUPERVISOR=str(outer_supervisor),
        OMEGACLAW_WATCHDOG_PID_FILE=str(pid_file or tmp_path / "legacy.pid"),
        OMEGACLAW_WATCHDOG_OUTER_PID_FILE=str(outer_pid_file or tmp_path / "outer.pid"),
        OMEGACLAW_WATCHDOG_OUTER_STATE_DIR=str(tmp_path / "outer-state"),
        OMEGACLAW_WATCHDOG_LEASE_FILE=str(tmp_path / "lease"),
        OMEGACLAW_WATCHDOG_CUTOVER_LOCK=str(tmp_path / "cutover.lock"),
    )
    return subprocess.run([str(SCRIPT), *args], env=env, text=True, capture_output=True)


def test_lease_lifecycle_and_bound(tmp_path):
    entered = run_watchdog(tmp_path, "enter-maintenance", "60")
    assert entered.returncode == 0
    assert "MAINTENANCE_ENTERED" in entered.stdout
    assert run_watchdog(tmp_path, "maintenance-status").returncode == 0
    assert run_watchdog(tmp_path, "enter-maintenance", "901").returncode == 2
    assert run_watchdog(tmp_path, "clear-maintenance").returncode == 0
    assert run_watchdog(tmp_path, "maintenance-status").returncode == 1


def test_malformed_expired_and_symlink_leases_fail_closed(tmp_path):
    supervisor = tmp_path / "supervisor"
    supervisor.write_text("#!/bin/sh\nexit 1\n")
    supervisor.chmod(0o700)
    outer_supervisor = tmp_path / "outer-supervisor"
    outer_supervisor.write_text("#!/bin/sh\nexit 1\n")
    outer_supervisor.chmod(0o700)
    for content in ("garbage\n", "maintenance_until_epoch=1000000000\n", "x" * 65):
        (tmp_path / "lease").write_text(content)
        result = run_watchdog(tmp_path)
        assert result.returncode == 1
        assert "OUTER_RESTART_FAILED" in result.stdout
    (tmp_path / "lease").unlink()
    target = tmp_path / "target"
    target.write_text("maintenance_until_epoch=9999999999\n")
    (tmp_path / "lease").symlink_to(target)
    assert run_watchdog(tmp_path).returncode == 1


def test_active_legacy_owner_is_retained(tmp_path):
    pid_file = tmp_path / "legacy.pid"
    pid_file.write_text(f"{os.getpid()}\n")
    result = run_watchdog(tmp_path, pid_file=pid_file)
    assert result.returncode == 0
    assert "LEGACY_ROLLBACK_RUNNING" in result.stdout


def test_missing_owner_restarts_outer_not_legacy(tmp_path):
    legacy = tmp_path / "supervisor"
    legacy.write_text("#!/bin/sh\necho legacy-called >>\"$0.calls\"\nexit 1\n")
    legacy.chmod(0o700)
    outer_pid = tmp_path / "outer.pid"
    result = run_watchdog(tmp_path, outer_pid_file=outer_pid)
    try:
        assert result.returncode == 0, result.stderr
        assert "OUTER_RESTARTED" in result.stdout
        assert not (tmp_path / "supervisor.calls").exists()
    finally:
        if outer_pid.exists():
            os.kill(int(outer_pid.read_text()), 15)


def test_outer_restart_failure_never_falls_back_to_legacy(tmp_path):
    legacy = tmp_path / "supervisor"
    legacy.write_text("#!/bin/sh\necho legacy-called >>\"$0.calls\"\nexit 0\n")
    legacy.chmod(0o700)
    outer = tmp_path / "outer-supervisor"
    outer.write_text("#!/bin/sh\nexit 1\n")
    outer.chmod(0o700)
    result = run_watchdog(tmp_path)
    assert result.returncode == 1
    assert "OUTER_RESTART_FAILED" in result.stdout
    assert not (tmp_path / "supervisor.calls").exists()


def test_active_outer_owner_suppresses_legacy_restart(tmp_path):
    outer = tmp_path / "outer.pid"
    outer.write_text(f"{os.getpid()}\n")
    result = run_watchdog(tmp_path, outer_pid_file=outer)
    assert result.returncode == 0
    assert "OUTER_OWNER_RUNNING" in result.stdout


def test_outer_owner_is_retained_during_child_readiness_failure(tmp_path):
    outer = tmp_path / "outer.pid"
    outer.write_text(f"{os.getpid()}\n")
    outer_supervisor = tmp_path / "outer-supervisor"
    outer_supervisor.write_text(
        "#!/bin/sh\n[ \"$1\" = owner-alive ] && exit 0\n[ \"$1\" = status ] && exit 1\nexit 2\n"
    )
    outer_supervisor.chmod(0o700)
    result = run_watchdog(tmp_path, outer_pid_file=outer)
    assert result.returncode == 0
    assert "OUTER_OWNER_RUNNING" in result.stdout


def test_live_outer_pid_with_invalid_identity_blocks_restart(tmp_path):
    outer = tmp_path / "outer.pid"
    outer.write_text(f"{os.getpid()}\n")
    outer_supervisor = tmp_path / "outer-supervisor"
    outer_supervisor.write_text("#!/bin/sh\nexit 1\n")
    outer_supervisor.chmod(0o700)
    result = run_watchdog(tmp_path, outer_pid_file=outer)
    assert result.returncode == 1
    assert "OUTER_STATE_UNSAFE" in result.stderr


def test_live_legacy_pid_with_invalid_identity_blocks_outer_restart(tmp_path):
    legacy_pid = tmp_path / "legacy.pid"
    legacy_pid.write_text(f"{os.getpid()}\n")
    legacy = tmp_path / "supervisor"
    legacy.write_text("#!/bin/sh\nexit 1\n")
    legacy.chmod(0o700)
    result = run_watchdog(tmp_path, pid_file=legacy_pid)
    assert result.returncode == 1
    assert "LEGACY_STATE_UNSAFE" in result.stderr


def test_active_lease_suppresses_restart(tmp_path):
    assert run_watchdog(tmp_path, "enter-maintenance", "60").returncode == 0
    result = run_watchdog(tmp_path)
    assert result.returncode == 0
    assert "MAINTENANCE_ACTIVE" in result.stdout


def test_active_cutover_lock_suppresses_watchdog(tmp_path):
    import fcntl

    with open(tmp_path / "cutover.lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        result = run_watchdog(tmp_path)
    assert result.returncode == 0
    assert "CUTOVER_IN_PROGRESS" in result.stdout


def test_cutover_lock_symlink_is_rejected(tmp_path):
    target = tmp_path / "target"
    target.write_text("unchanged")
    (tmp_path / "cutover.lock").symlink_to(target)
    result = run_watchdog(tmp_path)
    assert result.returncode == 2
    assert target.read_text() == "unchanged"
