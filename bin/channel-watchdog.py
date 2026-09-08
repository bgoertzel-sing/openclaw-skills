#!/usr/bin/env python3
"""Conservative interaction watchdog over local OpenClaw journals.

Read-only over journals; keeps a small persistent alert-state file so the
same finding cannot re-alert on every scheduled run.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re

DEFAULT_STATE = Path("/home/openclaw/research-agent/projects/channel-watchdog/state/alerted.json")
REMIND_AFTER = timedelta(hours=24)
PRUNE_AFTER = timedelta(days=7)
PUBLICLY_SUPPRESSED_PATTERNS = {"attachment promise not fulfilled"}

PROMISE = re.compile(
    r"\b(i(?:'ll| will) (?:report back|send|post|return)|working on it|on it|"
    r"compiling now|generating|writing it now|running now)\b",
    re.IGNORECASE,
)
ATTACHMENT = re.compile(r"\b(pdf|file|report|attachment)\b.*\b(ready|coming|send|post|attach)", re.IGNORECASE)
SPAWNED = re.compile(r"\b(spawned|delegated to|subagent .*running|work is running)\b", re.IGNORECASE)
ACK = re.compile(r"^(i(?:'ll| will) (?:look|check|work)|looking into it|on it|working on it)[.! ]*$", re.IGNORECASE)


def _timestamp(value):
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value / (1000 if value > 10_000_000_000 else 1), timezone.utc)
    if isinstance(value, str):
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    raise ValueError("missing timestamp")


def _text(content):
    if isinstance(content, str):
        return content.strip()
    if not isinstance(content, list):
        return ""
    return "\n".join(
        str(block.get("text", ""))
        for block in content
        if isinstance(block, dict) and block.get("type") in {"text", "output_text"}
    ).strip()


def _has_attachment(content):
    return isinstance(content, list) and any(
        isinstance(block, dict)
        and block.get("type") in {"image", "file", "document", "audio", "video"}
        for block in content
    )


def read_messages(path, cutoff):
    messages = []
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return messages
    for line in lines:
        try:
            record = json.loads(line)
            if record.get("type") != "message":
                continue
            message = record.get("message", {})
            when = _timestamp(message.get("timestamp", record.get("timestamp")))
            if when < cutoff:
                continue
            messages.append(
                {
                    "timestamp": when,
                    "role": message.get("role"),
                    "text": _text(message.get("content")),
                    "attachment": _has_attachment(message.get("content")),
                    "sender": message.get("senderName") or message.get("senderLabel") or "bot",
                }
            )
        except (ValueError, TypeError, json.JSONDecodeError):
            continue
    return sorted(messages, key=lambda item: item["timestamp"])


def scan(messages, now):
    alerts = []
    assistants = [message for message in messages if message["role"] == "assistant" and message["text"]]
    for index, message in enumerate(assistants):
        age = (now - message["timestamp"]).total_seconds()
        later = assistants[index + 1 :]
        if PROMISE.search(message["text"]) and age >= 15 * 60:
            timely = any((item["timestamp"] - message["timestamp"]).total_seconds() <= 15 * 60 for item in later)
            if not timely:
                alerts.append(("dropped continuation", message))
        if ATTACHMENT.search(message["text"]) and age >= 5 * 60:
            fulfilled = any(
                item["attachment"] and (item["timestamp"] - message["timestamp"]).total_seconds() <= 5 * 60
                for item in later
            )
            if not fulfilled:
                alerts.append(("attachment promise not fulfilled", message))
        if SPAWNED.search(message["text"]) and age >= 10 * 60:
            surfaced = any((item["timestamp"] - message["timestamp"]).total_seconds() <= 10 * 60 for item in later)
            if not surfaced:
                alerts.append(("completion not surfaced", message))
    for first, second in zip(assistants, assistants[1:]):
        if ACK.fullmatch(first["text"].strip()) and ACK.fullmatch(second["text"].strip()):
            alerts.append(("looping stock acknowledgement", second))
    deduped = []
    seen = set()
    for pattern, message in alerts:
        # Coarse per-run dedup: journal duplicates or a burst of near-identical
        # messages in the same minute collapse to one alert.
        key = (pattern, message["timestamp"].replace(second=0, microsecond=0), message["text"][:80])
        if key not in seen:
            seen.add(key)
            deduped.append((pattern, message))
    return deduped


def load_state(path):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def save_state(path, state):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(path)


def _state_time(value):
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def filter_fresh(groups, state, now):
    """Suppress already-alerted groups.

    A group re-alerts only when new violations appear (count grows) or the
    last alert is older than REMIND_AFTER. Returns (fresh, updated_state).
    """
    fresh = []
    for key, group in groups.items():
        stored = state.get(key)
        if stored is not None:
            alerted = _state_time(stored.get("alerted"))
            try:
                stored_count = int(stored.get("count", 0))
            except (TypeError, ValueError):
                stored_count = 0
            reminded = alerted is not None and now - alerted >= REMIND_AFTER
            if group["count"] <= stored_count and not reminded:
                continue
        state[key] = {"count": group["count"], "alerted": now.isoformat()}
        fresh.append((key, group))
    return fresh, state


def prune_state(state, now):
    return {
        key: entry
        for key, entry in state.items()
        if (_state_time(entry.get("alerted")) or now) >= now - PRUNE_AFTER
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sessions-dir", type=Path, default=Path("/home/openclaw/.openclaw/agents/main/sessions"))
    parser.add_argument("--now", help="ISO-8601 test clock; defaults to current UTC")
    parser.add_argument("--lookback-minutes", type=int, default=60)
    parser.add_argument("--state-file", type=Path, default=DEFAULT_STATE)
    args = parser.parse_args()
    now = _timestamp(args.now) if args.now else datetime.now(timezone.utc)
    cutoff = datetime.fromtimestamp(now.timestamp() - args.lookback_minutes * 60, timezone.utc)
    # Group by (session, pattern): one line per group, with a count, so a
    # burst of related violations produces one channel message, not many.
    groups = {}
    for path in sorted(args.sessions_dir.glob("*.jsonl")):
        for pattern, message in scan(read_messages(path, cutoff), now):
            if pattern in PUBLICLY_SUPPRESSED_PATTERNS:
                continue
            key = f"{path.stem}|{pattern}"
            group = groups.setdefault(key, {"count": 0, "first": message["timestamp"], "session": path.stem, "pattern": pattern})
            group["count"] += 1
            group["first"] = min(group["first"], message["timestamp"])
    state = prune_state(load_state(args.state_file), now)
    fresh, state = filter_fresh(groups, state, now)
    try:
        save_state(args.state_file, state)
    except OSError:
        pass  # alerting must not crash on an unwritable state file
    if fresh:
        lines = [
            f"WATCHDOG_ALERT {group['pattern']} session={group['session']} "
            f"time={group['first'].isoformat()} count={group['count']}"
            for _, group in fresh
        ]
        print("\n".join(lines[:8]))
    else:
        print("NO_REPLY")


if __name__ == "__main__":
    main()
