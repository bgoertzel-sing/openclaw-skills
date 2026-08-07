from pathlib import Path


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
