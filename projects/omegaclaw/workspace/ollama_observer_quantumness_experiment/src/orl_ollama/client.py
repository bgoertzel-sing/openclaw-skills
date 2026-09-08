from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass
from typing import Any

import requests


CHOICE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {"choice": {"type": "string", "enum": ["A", "B"]}},
    "required": ["choice"],
    "additionalProperties": False,
}


class OllamaError(RuntimeError):
    pass


@dataclass(frozen=True)
class ChoiceResponse:
    choice: str
    content: str
    thinking: str | None
    model: str | None
    total_duration_ns: int | None
    eval_count: int | None
    prompt_eval_count: int | None
    elapsed_seconds: float
    parse_method: str
    raw: dict[str, Any] | None = None


def parse_choice(content: str) -> tuple[str, str]:
    """Parse A/B robustly while preferring valid JSON."""
    text = content.strip()
    candidates = [text]
    first = text.find("{")
    last = text.rfind("}")
    if first >= 0 and last > first:
        candidates.append(text[first : last + 1])
    for candidate in candidates:
        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            value = str(parsed.get("choice", "")).strip().upper()
            if value in {"A", "B"}:
                return value, "json"

    match = re.search(r'["\'']?choice["\'']?\s*[:=]\s*["\'']?([AB])["\'']?', text, flags=re.IGNORECASE)
    if match:
        return match.group(1).upper(), "choice_regex"

    stripped = re.sub(r"[^A-Za-z]", "", text).upper()
    if stripped in {"A", "B"}:
        return stripped, "bare_label"
    raise ValueError(f"Could not parse A/B choice from: {content[:240]!r}")


class OllamaClient:
    def __init__(
        self,
        host: str = "http://localhost:11434",
        timeout_seconds: float = 120.0,
        save_full_response: bool = False,
    ) -> None:
        self.host = host.rstrip("/")
        self.timeout_seconds = timeout_seconds
        self.save_full_response = save_full_response
        self.session = requests.Session()

    def _get(self, path: str) -> dict[str, Any]:
        try:
            response = self.session.get(self.host + path, timeout=self.timeout_seconds)
            response.raise_for_status()
            value = response.json()
        except (requests.RequestException, ValueError) as exc:
            raise OllamaError(f"GET {self.host + path} failed: {exc}") from exc
        if not isinstance(value, dict):
            raise OllamaError(f"Unexpected response from {path}: expected an object")
        return value

    def version(self) -> dict[str, Any]:
        return self._get("/api/version")

    def tags(self) -> dict[str, Any]:
        return self._get("/api/tags")

    def available_models(self) -> list[str]:
        payload = self.tags()
        models = payload.get("models", [])
        result: list[str] = []
        if isinstance(models, list):
            for item in models:
                if isinstance(item, dict) and isinstance(item.get("name"), str):
                    result.append(item["name"])
        return result

    def ensure_model(self, model: str) -> None:
        available = self.available_models()
        if model not in available:
            shown = ", ".join(available) if available else "(none reported)"
            raise OllamaError(f"Model {model!r} is not installed. Ollama reports: {shown}")

    def chat_choice(
        self,
        *,
        model: str,
        messages: list[dict[str, str]],
        seed: int,
        temperature: float,
        top_p: float,
        num_predict: int,
        keep_alive: str,
        retries: int = 2,
        think: bool | str | None = None,
    ) -> ChoiceResponse:
        last_error: Exception | None = None
        for attempt in range(retries + 1):
            payload: dict[str, Any] = {
                "model": model,
                "messages": messages,
                "stream": False,
                "format": CHOICE_SCHEMA,
                "keep_alive": keep_alive,
                "options": {
                    "temperature": temperature,
                    "top_p": top_p,
                    "seed": int(seed + attempt * 104729),
                    "num_predict": num_predict,
                },
            }
            if think is not None:
                payload["think"] = think
            started = time.monotonic()
            try:
                response = self.session.post(
                    self.host + "/api/chat",
                    json=payload,
                    timeout=self.timeout_seconds,
                )
                response.raise_for_status()
                body = response.json()
                if not isinstance(body, dict):
                    raise OllamaError("Ollama returned a non-object response")
                message = body.get("message")
                if not isinstance(message, dict):
                    raise OllamaError("Ollama response has no message object")
                content = str(message.get("content", ""))
                choice, parse_method = parse_choice(content)
                elapsed = time.monotonic() - started
                return ChoiceResponse(
                    choice=choice,
                    content=content,
                    thinking=(str(message["thinking"]) if message.get("thinking") else None),
                    model=(str(body["model"]) if body.get("model") else None),
                    total_duration_ns=(int(body["total_duration"]) if body.get("total_duration") is not None else None),
                    eval_count=(int(body["eval_count"]) if body.get("eval_count") is not None else None),
                    prompt_eval_count=(int(body["prompt_eval_count"]) if body.get("prompt_eval_count") is not None else None),
                    elapsed_seconds=elapsed,
                    parse_method=parse_method,
                    raw=(body if self.save_full_response else None),
                )
            except (requests.RequestException, ValueError, OllamaError) as exc:
                last_error = exc
                if attempt >= retries:
                    break
                time.sleep(min(1.5 * (attempt + 1), 4.0))
        raise OllamaError(f"Ollama choice request failed after {retries + 1} attempts: {last_error}")
