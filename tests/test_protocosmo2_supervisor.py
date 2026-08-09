import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).parents[1]
SUPERVISOR = ROOT / "projects/omegaclaw/protocosmo2/tools/protocosmo2_telegram_supervisor.sh"
GENERIC = ROOT / "projects/omegaclaw/local/protomega-outer-telegram-supervisor.sh"
WATCHDOG = ROOT / "bin/protocosmo2-watchdog.sh"


def fixture_env(tmp_path):
    env = os.environ.copy()
    env.update({
        "OMEGACLAW_OUTER_PID_FILE": str(tmp_path / "owner.pid"),
        "OMEGACLAW_OUTER_START_LOCK": str(tmp_path / "start.lock"),
        "OMEGACLAW_CUTOVER_LOCK": str(tmp_path / "cutover.lock"),
        "OMEGACLAW_OUTER_DEFERRED_DISABLE_MARKER": str(tmp_path / "rollback.marker"),
    })
    return env


def test_wrapper_freezes_protocosmo2_identity_and_isolated_paths():
    text = SUPERVISOR.read_text()
    assert "OMEGACLAW_OUTER_IDENTITY=ProtoCosmo2" in text
    assert "OMEGACLAW_OUTER_BOT_ID=8716054285" in text
    assert "protocosmo2-canary-state" in text
    assert "protocosmo2-worker-state" in text
    assert "protocosmo2-cutover.lock" in text
    assert "exec \"$ROOT/local/protomega-outer-telegram-supervisor.sh\"" in text


def test_shared_supervisor_keeps_protomega_defaults_and_parameterizes_runtime():
    text = GENERIC.read_text()
    assert "OMEGACLAW_OUTER_IDENTITY:-ProtomegaTron" in text
    assert "OMEGACLAW_OUTER_BOT_ID:-8562797306" in text
    assert '--identity "$IDENTITY"' in text
    assert '--bot-id "$BOT_ID"' in text
    assert '--model "$MODEL"' in text


def test_wrapper_creates_and_validates_secure_sync_rollback_marker(tmp_path):
    env = fixture_env(tmp_path)
    made = subprocess.run([str(SUPERVISOR), "enable-sync-rollback"], env=env,
                          text=True, capture_output=True)
    assert made.returncode == 0, made.stderr
    marker = tmp_path / "rollback.marker"
    info = marker.stat()
    assert info.st_mode & 0o777 == 0o600
    assert info.st_nlink == 1
    checked = subprocess.run([str(SUPERVISOR), "validate-sync-rollback"], env=env,
                             text=True, capture_output=True)
    assert checked.returncode == 0, checked.stderr


def test_wrapper_rejects_symlink_and_hardlinked_markers(tmp_path):
    env = fixture_env(tmp_path)
    target = tmp_path / "target"
    target.write_text("")
    target.chmod(0o600)
    marker = tmp_path / "rollback.marker"
    marker.symlink_to(target)
    result = subprocess.run([str(SUPERVISOR), "enable-sync-rollback"], env=env)
    assert result.returncode != 0
    marker.unlink()
    os.link(target, marker)
    result = subprocess.run([str(SUPERVISOR), "validate-sync-rollback"], env=env)
    assert result.returncode != 0


def test_watchdog_binds_protocosmo2_identity_state_and_cutover_lock():
    text = WATCHDOG.read_text()
    assert "OMEGACLAW_WATCHDOG_OUTER_IDENTITY=ProtoCosmo2" in text
    assert "protocosmo2-canary-state" in text
    assert "protocosmo2-cutover.lock" in text
