import importlib.util
from datetime import datetime, timedelta, timezone
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "bin" / "channel-watchdog.py"
SPEC = importlib.util.spec_from_file_location("channel_watchdog", MODULE_PATH)
WATCHDOG = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(WATCHDOG)


def test_attachment_alert_class_is_not_public():
    assert "attachment promise not fulfilled" in WATCHDOG.PUBLICLY_SUPPRESSED_PATTERNS


def test_other_watchdog_alert_classes_remain_enabled():
    now = datetime(2026, 8, 7, 22, 0, tzinfo=timezone.utc)
    messages = [{
        "timestamp": now - timedelta(minutes=16),
        "role": "assistant",
        "text": "I'll report back.",
        "attachment": False,
        "sender": "bot",
    }]
    assert [pattern for pattern, _ in WATCHDOG.scan(messages, now)] == ["dropped continuation"]
