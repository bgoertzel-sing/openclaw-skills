"""Portable regression tests for the live Bot API 10 loop guards."""
from pathlib import Path
import importlib
import sys

ROOT = Path(__file__).resolve().parents[2] if "patches" in Path(__file__).parts else Path(__file__).resolve().parents[1]
CHANNELS = ROOT / "channels"
if str(CHANNELS) not in sys.path:
    sys.path.insert(0, str(CHANNELS))


def _telegram():
    return importlib.import_module("telegram")


def _reset(t):
    t._self_bot_id = None
    t._bot_sender_last_ts.clear()
    t._bot_interaction_chain.clear()


def test_self_bot_id_filter():
    t = _telegram(); _reset(t)
    t._self_bot_id = 3333333333
    assert t._is_self_bot_message({"id": 3333333333, "is_bot": True})
    assert not t._is_self_bot_message({"id": 2222222222, "is_bot": True})


def test_human_messages_bypass_bot_loop_guard():
    t = _telegram(); _reset(t)
    assert not t._bot_to_bot_loop_guard({"id": 111111111, "is_bot": False}, "-1005555555555")


def test_per_sender_rate_limit(monkeypatch):
    t = _telegram(); _reset(t)
    monkeypatch.setattr(t.time, "time", lambda: 100.0)
    bot = {"id": 2222222222, "is_bot": True}
    assert not t._bot_to_bot_loop_guard(bot, "-1005555555555")
    assert t._bot_to_bot_loop_guard(bot, "-1005555555555")


def test_chain_depth_cap(monkeypatch):
    t = _telegram(); _reset(t)
    times = iter(100.0 + i * 1.1 for i in range(t._BOT_MAX_CHAIN_DEPTH + 1))
    monkeypatch.setattr(t.time, "time", lambda: next(times))
    results = [
        t._bot_to_bot_loop_guard({"id": 2000000000 + i, "is_bot": True}, "-1005555555555")
        for i in range(t._BOT_MAX_CHAIN_DEPTH + 1)
    ]
    assert results[:-1] == [False] * t._BOT_MAX_CHAIN_DEPTH
    assert results[-1] is True


def test_live_defaults_are_bot_api_and_one_second_rate():
    t = _telegram()
    assert t._receive_transport == "bot_api"
    assert t._BOT_RATE_LIMIT_S == 1.0
    assert t._BOT_MAX_CHAIN_DEPTH == 8
