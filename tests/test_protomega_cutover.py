import os
import subprocess
import time
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "projects/omegaclaw/local/protomega-cutover.sh"


def make_executable(path, body):
    path.write_text("#!/bin/sh\nset -eu\n" + body)
    path.chmod(0o700)


def fixture(tmp_path, outer_start_fails=False):
    state = tmp_path / "state"
    state.write_text("1 0\n")
    bindir = tmp_path / "bin"
    bindir.mkdir()
    make_executable(
        bindir / "ps",
        'read legacy outer <"$CUTOVER_TEST_STATE"\n'
        'i=0; while [ "$i" -lt "$legacy" ]; do echo "main.pl -- run.metta commchannel=telegram"; i=$((i+1)); done\n'
        'i=0; while [ "$i" -lt "$outer" ]; do echo "phase6_private_canary_runner.py --identity ProtomegaTron"; i=$((i+1)); done\n',
    )
    make_executable(
        tmp_path / "legacy",
        'read legacy outer <"$CUTOVER_TEST_STATE"\n'
        'case "$1" in stop) [ "${CUTOVER_FAIL_LEGACY_STOP:-0}" = 0 ] || exit 1; [ -z "${CUTOVER_TEST_DELAY:-}" ] || sleep "$CUTOVER_TEST_DELAY"; legacy=0;; start) [ "${CUTOVER_FAIL_LEGACY_START:-0}" = 0 ] || exit 1; legacy=1;; status) [ "$legacy" -eq 1 ];; esac\n'
        'printf "%s %s\\n" "$legacy" "$outer" >"$CUTOVER_TEST_STATE"\n',
    )
    fail = "exit 1" if outer_start_fails else "outer=1"
    make_executable(
        tmp_path / "outer",
        'read legacy outer <"$CUTOVER_TEST_STATE"\n'
        f'case "$1" in stop) [ "${{CUTOVER_FAIL_OUTER_STOP:-0}}" = 0 ] || exit 1; [ "${{CUTOVER_LEAVE_OUTER_ON_STOP:-0}}" = 0 ] || {{ printf "%s %s\\n" "$legacy" "$outer" >"$CUTOVER_TEST_STATE"; exit 0; }}; outer=0;; start) {fail};; status) [ "$outer" -eq 1 ];; esac\n'
        'printf "%s %s\\n" "$legacy" "$outer" >"$CUTOVER_TEST_STATE"\n',
    )
    make_executable(tmp_path / "watchdog", '[ "${CUTOVER_FAIL_CLEAR:-0}" = 0 ] || [ "$1" != clear-maintenance ] || exit 1\nexit 0\n')
    env = os.environ.copy()
    env.update(
        PATH=f"{bindir}:{env['PATH']}",
        CUTOVER_TEST_STATE=str(state),
        OMEGACLAW_CUTOVER_WATCHDOG=str(tmp_path / "watchdog"),
        OMEGACLAW_CUTOVER_LEGACY_SUPERVISOR=str(tmp_path / "legacy"),
        OMEGACLAW_CUTOVER_OUTER_SUPERVISOR=str(tmp_path / "outer"),
        OMEGACLAW_CUTOVER_LOCK=str(tmp_path / "lock"),
    )
    return state, env


def test_cutover_transaction_reaches_outer_only(tmp_path):
    state, env = fixture(tmp_path)
    result = subprocess.run([str(SCRIPT), "cutover"], env=env, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
    assert state.read_text() == "0 1\n"
    assert "CUTOVER_TOPOLOGY_READY" in result.stdout


def test_failed_outer_start_rolls_back_to_legacy_only(tmp_path):
    state, env = fixture(tmp_path, outer_start_fails=True)
    result = subprocess.run([str(SCRIPT), "cutover"], env=env, text=True, capture_output=True)
    assert result.returncode != 0
    assert state.read_text() == "1 0\n"


def test_cutover_rejects_wrong_in_lock_baseline(tmp_path):
    state, env = fixture(tmp_path)
    state.write_text("0 1\n")
    result = subprocess.run([str(SCRIPT), "cutover"], env=env, text=True, capture_output=True)
    assert result.returncode != 0
    assert state.read_text() == "0 1\n"


def test_cutover_lock_symlink_is_rejected_without_touching_target(tmp_path):
    state, env = fixture(tmp_path)
    target = tmp_path / "target"
    target.write_text("unchanged")
    (tmp_path / "lock").symlink_to(target)
    result = subprocess.run([str(SCRIPT), "cutover"], env=env, text=True, capture_output=True)
    assert result.returncode == 2
    assert target.read_text() == "unchanged"


def test_two_concurrent_cutovers_have_one_winner(tmp_path):
    state, env = fixture(tmp_path)
    env["CUTOVER_TEST_DELAY"] = "0.3"
    first = subprocess.Popen([str(SCRIPT), "cutover"], env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(0.05)
    second = subprocess.run([str(SCRIPT), "cutover"], env=env, text=True, capture_output=True)
    first_out, first_err = first.communicate(timeout=5)
    assert first.returncode == 0, first_err
    assert second.returncode != 0
    assert "cutover lock busy" in second.stderr
    assert state.read_text() == "0 1\n"


def test_invalid_baseline_still_clears_maintenance(tmp_path):
    state, env = fixture(tmp_path)
    state.write_text("0 1\n")
    log = tmp_path / "watchdog.log"
    make_executable(tmp_path / "watchdog", 'echo "$1" >>"$CUTOVER_WATCHDOG_LOG"\n')
    env["CUTOVER_WATCHDOG_LOG"] = str(log)
    result = subprocess.run([str(SCRIPT), "cutover"], env=env, text=True, capture_output=True)
    assert result.returncode != 0
    assert log.read_text().splitlines() == ["enter-maintenance", "clear-maintenance"]
    assert state.read_text() == "0 1\n"


def test_explicit_rollback_restores_legacy_only(tmp_path):
    state, env = fixture(tmp_path)
    state.write_text("0 1\n")
    result = subprocess.run([str(SCRIPT), "rollback"], env=env, text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
    assert state.read_text() == "1 0\n"
    assert "ROLLBACK_TOPOLOGY_READY" in result.stdout


def test_explicit_rollback_reports_legacy_start_failure_and_clears_maintenance(tmp_path):
    state, env = fixture(tmp_path)
    state.write_text("0 1\n")
    env["CUTOVER_FAIL_LEGACY_START"] = "1"
    log = tmp_path / "watchdog.log"
    make_executable(tmp_path / "watchdog", 'echo "$1" >>"$CUTOVER_WATCHDOG_LOG"\n')
    env["CUTOVER_WATCHDOG_LOG"] = str(log)
    result = subprocess.run([str(SCRIPT), "rollback"], env=env, text=True, capture_output=True)
    assert result.returncode == 3
    assert state.read_text() == "0 0\n"
    assert log.read_text().splitlines() == ["enter-maintenance", "clear-maintenance"]
    assert "ROLLBACK_FAILED" in result.stderr


def test_explicit_rollback_reports_maintenance_clear_failure(tmp_path):
    state, env = fixture(tmp_path)
    state.write_text("0 1\n")
    env["CUTOVER_FAIL_CLEAR"] = "1"
    result = subprocess.run([str(SCRIPT), "rollback"], env=env, text=True, capture_output=True)
    assert result.returncode == 3
    assert state.read_text() == "1 0\n"
    assert "ROLLBACK_FAILED" in result.stderr


def test_explicit_rollback_does_not_start_legacy_when_outer_stop_fails(tmp_path):
    state, env = fixture(tmp_path)
    state.write_text("0 1\n")
    env["CUTOVER_FAIL_OUTER_STOP"] = "1"
    result = subprocess.run([str(SCRIPT), "rollback"], env=env, text=True, capture_output=True)
    assert result.returncode == 3
    assert state.read_text() == "0 1\n"
    assert "ROLLBACK_ABORTED_UNSAFE_TO_START_LEGACY" in result.stderr


def test_explicit_rollback_does_not_start_legacy_when_outer_remains(tmp_path):
    state, env = fixture(tmp_path)
    state.write_text("0 1\n")
    env["CUTOVER_LEAVE_OUTER_ON_STOP"] = "1"
    result = subprocess.run([str(SCRIPT), "rollback"], env=env, text=True, capture_output=True)
    assert result.returncode == 3
    assert state.read_text() == "0 1\n"
    assert "ROLLBACK_ABORTED_UNSAFE_TO_START_LEGACY" in result.stderr


def test_err_trap_does_not_start_legacy_when_outer_stop_fails(tmp_path):
    state, env = fixture(tmp_path, outer_start_fails=True)
    env["CUTOVER_FAIL_OUTER_STOP"] = "1"
    result = subprocess.run([str(SCRIPT), "cutover"], env=env, text=True, capture_output=True)
    assert result.returncode == 3
    assert state.read_text() == "0 0\n"
    assert "ROLLBACK_ABORTED_UNSAFE_TO_START_LEGACY" in result.stderr
