#!/usr/bin/env python3
"""Verify the dedicated ProtoCosmo2 Telegram token without disclosing it."""

from __future__ import annotations

import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.request


TOKEN_RE = re.compile(r"^[0-9]{8,12}:[A-Za-z0-9_-]{30,80}$")


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        key, separator, value = line.partition("=")
        if not separator or not key:
            raise ValueError("malformed credential environment file")
        values[key] = value
    return values


def main() -> int:
    env_path = Path(os.environ.get(
        "PROTOCOSMO2_ENV",
        "/home/openclaw/.openclaw/protocosmo2.env",
    ))
    mode = env_path.stat().st_mode & 0o777
    if mode != 0o600:
        raise ValueError(f"credential file mode must be 0600, observed {mode:04o}")
    token = load_env(env_path).get("TG_BOT_TOKEN", "")
    if not TOKEN_RE.fullmatch(token):
        raise ValueError("dedicated Telegram token is absent or malformed")

    request = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/getMe",
        headers={"User-Agent": "ProtoCosmo2-Phase6-Identity/1"},
    )
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as exc:
        print(json.dumps({"ok": False, "error": "telegram_http_error", "status": exc.code}))
        return 2
    except Exception as exc:  # Never render exception text: it may contain the URL.
        print(json.dumps({"ok": False, "error": type(exc).__name__}))
        return 2
    finally:
        token = ""

    result = payload.get("result") if isinstance(payload, dict) else None
    if payload.get("ok") is not True or not isinstance(result, dict):
        print(json.dumps({"ok": False, "error": "malformed_getme_response"}))
        return 2

    safe = {
        "ok": True,
        "id": result.get("id"),
        "is_bot": result.get("is_bot"),
        "first_name": result.get("first_name"),
        "username": result.get("username"),
        "can_join_groups": result.get("can_join_groups"),
        "can_read_all_group_messages": result.get("can_read_all_group_messages"),
        "supports_inline_queries": result.get("supports_inline_queries"),
        "credential_file_mode": "0600",
    }
    print(json.dumps(safe, sort_keys=True))
    if safe["is_bot"] is not True or not isinstance(safe["username"], str):
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
