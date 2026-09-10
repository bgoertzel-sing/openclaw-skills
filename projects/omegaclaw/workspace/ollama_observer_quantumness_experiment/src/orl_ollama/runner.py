from __future__ import annotations

import hashlib
import json
import platform
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from .client import ChoiceResponse, OllamaClient, OllamaError
from . import __version__
from .design import SYSTEM_PROMPT, TrialPrompt, build_trial_prompt
from .tasks import Task, cycle_edges, load_tasks
from .util import append_jsonl, atomic_write_json, file_sha256, load_jsonl, stable_seed


@dataclass(frozen=True)
class RunConfig:
    model: str
    host: str
    tasks_path: str
    repeats: int = 8
    conditions: tuple[str, ...] = ("ambiguous", "resolved")
    directions: str = "both"
    base_seed: int = 20260812
    temperature: float = 0.85
    top_p: float = 0.95
    num_predict: int = 24
    keep_alive: str = "10m"
    timeout_seconds: float = 120.0
    retries: int = 2
    think: bool | str | None = None
    save_full_response: bool = False
    selected_task_ids: tuple[str, ...] = ()
    max_trials: int | None = None


@dataclass(frozen=True)
class TrialSpec:
    task: Task
    condition: str
    edge_index: int
    direction: str
    repeat: int

    @property
    def first_question(self):
        left, right = cycle_edges(self.task)[self.edge_index]
        return left if self.direction == "forward" else right

    @property
    def second_question(self):
        left, right = cycle_edges(self.task)[self.edge_index]
        return right if self.direction == "forward" else left

    @property
    def canonical_left_id(self) -> str:
        return cycle_edges(self.task)[self.edge_index][0].id

    @property
    def canonical_right_id(self) -> str:
        return cycle_edges(self.task)[self.edge_index][1].id

    @property
    def context_id(self) -> str:
        return f"{self.first_question.id}__then__{self.second_question.id}"

    @property
    def canonical_edge_id(self) -> str:
        return f"{self.canonical_left_id}__{self.canonical_right_id}"

    @property
    def trial_id(self) -> str:
        return "|".join(
            [
                self.task.id,
                self.condition,
                str(self.edge_index),
                self.direction,
                str(self.repeat),
            ]
        )


def enumerate_trials(config: RunConfig, tasks: list[Task]) -> list[TrialSpec]:
    if config.repeats <= 0:
        raise ValueError("repeats must be positive")
    directions = ("forward", "reverse") if config.directions == "both" else ("forward",)
    chosen = [task for task in tasks if not config.selected_task_ids or task.id in config.selected_task_ids]
    if not chosen:
        raise ValueError("No tasks remain after task selection")
    trials = [
        TrialSpec(task=task, condition=condition, edge_index=edge, direction=direction, repeat=repeat)
        for task in chosen
        for condition in config.conditions
        for edge in range(4)
        for direction in directions
        for repeat in range(config.repeats)
    ]
    if config.max_trials is not None:
        trials = trials[: config.max_trials]
    return trials


def _compact_response(response: ChoiceResponse, save_thinking: bool = False) -> dict[str, Any]:
    result: dict[str, Any] = {
        "choice": response.choice,
        "content": response.content,
        "model": response.model,
        "total_duration_ns": response.total_duration_ns,
        "eval_count": response.eval_count,
        "prompt_eval_count": response.prompt_eval_count,
        "elapsed_seconds": response.elapsed_seconds,
        "parse_method": response.parse_method,
    }
    if save_thinking and response.thinking:
        result["thinking"] = response.thinking
    if response.raw is not None:
        result["raw"] = response.raw
    return result


def _run_trial(client: OllamaClient, config: RunConfig, spec: TrialSpec) -> dict[str, Any]:
    trial_seed = stable_seed(config.base_seed, spec.trial_id)
    prompt: TrialPrompt = build_trial_prompt(
        task=spec.task,
        condition=spec.condition,
        first_question=spec.first_question,
        second_question=spec.second_question,
        base_seed=config.base_seed,
        trial_key=spec.trial_id,
    )
    first_response = client.chat_choice(
        model=config.model,
        messages=prompt.first_messages,
        seed=trial_seed,
        temperature=config.temperature,
        top_p=config.top_p,
        num_predict=config.num_predict,
        keep_alive=config.keep_alive,
        retries=config.retries,
        think=config.think,
    )
    second_messages = [
        *prompt.first_messages,
        {"role": "assistant", "content": json.dumps({"choice": first_response.choice})},
        {"role": "user", "content": prompt.second_user_message},
    ]
    second_response = client.chat_choice(
        model=config.model,
        messages=second_messages,
        seed=trial_seed + 1,
        temperature=config.temperature,
        top_p=config.top_p,
        num_predict=config.num_predict,
        keep_alive=config.keep_alive,
        retries=config.retries,
        think=config.think,
    )
    first_value = prompt.first.label_values[first_response.choice]
    second_value = prompt.second.label_values[second_response.choice]

    if spec.direction == "forward":
        canonical_left_value, canonical_right_value = first_value, second_value
    else:
        canonical_left_value, canonical_right_value = second_value, first_value

    return {
        "trial_id": spec.trial_id,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "task_id": spec.task.id,
        "family": spec.task.family,
        "condition": spec.condition,
        "edge_index": spec.edge_index,
        "direction": spec.direction,
        "context_id": spec.context_id,
        "canonical_edge_id": spec.canonical_edge_id,
        "canonical_left_question_id": spec.canonical_left_id,
        "canonical_right_question_id": spec.canonical_right_id,
        "first_question_id": spec.first_question.id,
        "second_question_id": spec.second_question.id,
        "repeat": spec.repeat,
        "seed": trial_seed,
        "first_label_texts": prompt.first.label_texts,
        "first_label_values": prompt.first.label_values,
        "second_label_texts": prompt.second.label_texts,
        "second_label_values": prompt.second.label_values,
        "first_choice": first_response.choice,
        "second_choice": second_response.choice,
        "first_value": first_value,
        "second_value": second_value,
        "canonical_left_value": canonical_left_value,
        "canonical_right_value": canonical_right_value,
        "first_response": _compact_response(first_response),
        "second_response": _compact_response(second_response),
        "complete": True,
    }


def run_experiment(config: RunConfig, output_dir: str | Path, dry_run: bool = False) -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    records_path = output_dir / "records.jsonl"
    errors_path = output_dir / "errors.jsonl"
    manifest_path = output_dir / "manifest.json"

    tasks = load_tasks(config.tasks_path)
    trials = enumerate_trials(config, tasks)
    existing = {record.get("trial_id") for record in load_jsonl(records_path)}
    tasks_snapshot_path = output_dir / "tasks_snapshot.json"
    task_source_text = Path(config.tasks_path).read_text(encoding="utf-8")
    if tasks_snapshot_path.exists():
        if file_sha256(tasks_snapshot_path) != file_sha256(config.tasks_path):
            raise ValueError("The run's tasks_snapshot.json does not match the selected task file")
    else:
        tasks_snapshot_path.write_text(task_source_text, encoding="utf-8")

    client = OllamaClient(
        host=config.host,
        timeout_seconds=config.timeout_seconds,
        save_full_response=config.save_full_response,
    )
    version: dict[str, Any] | None = None
    models: list[str] = []
    selected_model_metadata: dict[str, Any] | None = None
    if not dry_run:
        version = client.version()
        tags_payload = client.tags()
        raw_models = tags_payload.get("models", [])
        if isinstance(raw_models, list):
            for item in raw_models:
                if isinstance(item, dict) and isinstance(item.get("name"), str):
                    models.append(item["name"])
                    if item["name"] == config.model:
                        selected_model_metadata = item
        if config.model not in models:
            raise OllamaError(f"Model {config.model!r} is not installed. Available: {models}")

    experiment_identity = {
        "protocol_version": 1,
        "package_version": __version__,
        "model": config.model,
        "model_digest": (selected_model_metadata or {}).get("digest"),
        "tasks_sha256": file_sha256(config.tasks_path),
        "conditions": sorted(config.conditions),
        "directions": config.directions,
        "selected_task_ids": sorted(config.selected_task_ids),
        "base_seed": config.base_seed,
        "temperature": config.temperature,
        "top_p": config.top_p,
        "num_predict": config.num_predict,
        "think": config.think,
        "system_prompt_sha256": hashlib.sha256(SYSTEM_PROMPT.encode("utf-8")).hexdigest(),
    }

    now = datetime.now(timezone.utc).isoformat()
    if manifest_path.exists():
        existing_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if existing_manifest.get("experiment_identity") != experiment_identity:
            raise ValueError(
                "The output directory already belongs to a different experimental identity. "
                "Use a new output directory rather than mixing models, prompts, task files, or generation settings."
            )
        manifest = existing_manifest
        manifest["last_resumed_utc"] = now
        manifest["latest_config"] = asdict(config)
        manifest["planned_trials_current"] = len(trials)
        manifest["ollama_version_latest"] = version
    else:
        manifest = {
            "created_utc": now,
            "config": asdict(config),
            "experiment_identity": experiment_identity,
            "ollama_version": version,
            "selected_model_metadata": selected_model_metadata,
            "available_models_at_start": models,
            "python": sys.version,
            "platform": platform.platform(),
            "planned_trials": len(trials),
            "note": "Each complete trial makes two sequential /api/chat calls.",
        }
    atomic_write_json(manifest_path, manifest)

    if dry_run:
        preview = []
        for spec in trials[: min(3, len(trials))]:
            prompt = build_trial_prompt(
                task=spec.task,
                condition=spec.condition,
                first_question=spec.first_question,
                second_question=spec.second_question,
                base_seed=config.base_seed,
                trial_key=spec.trial_id,
            )
            preview.append(
                {
                    "trial_id": spec.trial_id,
                    "first_messages": prompt.first_messages,
                    "second_user_message": prompt.second_user_message,
                }
            )
        atomic_write_json(output_dir / "dry_run_prompt_preview.json", preview)
        return output_dir

    completed_now = 0
    for index, spec in enumerate(trials, 1):
        if spec.trial_id in existing:
            continue
        print(f"[{index}/{len(trials)}] {spec.trial_id}", flush=True)
        try:
            record = _run_trial(client, config, spec)
            append_jsonl(records_path, record)
            existing.add(spec.trial_id)
            completed_now += 1
        except Exception as exc:  # retain the run and make failure auditable
            append_jsonl(
                errors_path,
                {
                    "trial_id": spec.trial_id,
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                },
            )
            print(f"  ERROR: {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
    print(f"Completed {completed_now} new trials; records are in {records_path}")
    return output_dir
