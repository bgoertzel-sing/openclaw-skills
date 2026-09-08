from pathlib import Path


ROOT = Path(__file__).parents[1]
SUPERVISOR = ROOT / "projects/omegaclaw/local/protomega2-outer-telegram-supervisor.sh"


def test_wrapper_freezes_protomega2_identity_and_isolated_paths():
    text = SUPERVISOR.read_text(encoding="utf-8")
    required = (
        "OMEGACLAW_OUTER_ENV_FILE=/home/openclaw/.openclaw/protomegabot2.env",
        "OMEGACLAW_OUTER_CONFIG=/home/openclaw/.openclaw/protomega2-outer.json",
        "OMEGACLAW_OUTER_STATE_DIR=/home/openclaw/.openclaw/protomega2-outer-state",
        "OMEGACLAW_OUTER_WORKER_STATE_DIR=\"$ROOT/local/protomega2-worker-state\"",
        "OMEGACLAW_OUTER_PID_FILE=\"$ROOT/local/run-state/protomega2-outer-telegram.pid\"",
        "OMEGACLAW_OUTER_START_LOCK=\"$ROOT/local/run-state/protomega2-outer-telegram.pid.start.lock\"",
        "OMEGACLAW_CUTOVER_LOCK=\"$ROOT/local/run-state/protomega2-cutover.lock\"",
        "OMEGACLAW_OUTER_DEFERRED_DISABLE_MARKER=\"$ROOT/local/run-state/protomega2-deferred-disabled\"",
        "OMEGACLAW_OUTER_IDENTITY=ProtoMegaBot2",
        "OMEGACLAW_OUTER_BOT_ID=8680999952",
        "OMEGACLAW_OUTER_BOT_USERNAME=@Protomega2bot",
        "OMEGACLAW_OUTER_AGENT_ID=protomegabot-opus",
        "OMEGACLAW_OUTER_MODEL=anthropic/claude-opus-4-6",
        "OMEGACLAW_OUTER_CHROMA_DB_PATH=/home/openclaw/.openclaw/protomega2-chroma-db",
        'exec "$ROOT/local/protomega-outer-telegram-supervisor.sh" "$@"',
    )
    assert all(fragment in text for fragment in required)
    assert '${OMEGACLAW_OUTER_STATE_DIR:-' not in text
    assert "printf '%s\\n' \"$$\" >\"$PID_FILE\"" not in text
    assert 'rm -f "$PID_FILE"' not in text
