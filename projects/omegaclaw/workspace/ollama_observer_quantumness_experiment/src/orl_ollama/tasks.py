from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Question:
    id: str
    prompt: str
    positive: str
    negative: str
    resolved_expected: int | None = None


@dataclass(frozen=True)
class Task:
    id: str
    family: str
    ambiguous_text: str
    resolved_text: str
    questions: tuple[Question, Question, Question, Question]

    def passage(self, condition: str) -> str:
        if condition == "ambiguous":
            return self.ambiguous_text
        if condition == "resolved":
            return self.resolved_text
        raise ValueError(f"Unknown condition: {condition}")


def _require_text(mapping: dict[str, Any], field: str, where: str) -> str:
    value = mapping.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{where}.{field} must be a non-empty string")
    return value.strip()


def load_tasks(path: str | Path) -> list[Task]:
    path = Path(path)
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("tasks"), list):
        raise ValueError("Task file must be an object with a 'tasks' array")

    tasks: list[Task] = []
    seen_tasks: set[str] = set()
    for task_index, raw_task in enumerate(payload["tasks"]):
        where = f"tasks[{task_index}]"
        if not isinstance(raw_task, dict):
            raise ValueError(f"{where} must be an object")
        task_id = _require_text(raw_task, "id", where)
        if task_id in seen_tasks:
            raise ValueError(f"Duplicate task id: {task_id}")
        seen_tasks.add(task_id)
        raw_questions = raw_task.get("questions")
        if not isinstance(raw_questions, list) or len(raw_questions) != 4:
            raise ValueError(f"{where}.questions must contain exactly four binary questions")
        questions: list[Question] = []
        seen_questions: set[str] = set()
        for question_index, raw_question in enumerate(raw_questions):
            qwhere = f"{where}.questions[{question_index}]"
            if not isinstance(raw_question, dict):
                raise ValueError(f"{qwhere} must be an object")
            question_id = _require_text(raw_question, "id", qwhere)
            if question_id in seen_questions:
                raise ValueError(f"Duplicate question id in {task_id}: {question_id}")
            seen_questions.add(question_id)
            raw_expected = raw_question.get("resolved_expected")
            if raw_expected is not None and raw_expected not in {-1, 1}:
                raise ValueError(f"{qwhere}.resolved_expected must be +1, -1, or omitted")
            questions.append(
                Question(
                    id=question_id,
                    prompt=_require_text(raw_question, "prompt", qwhere),
                    positive=_require_text(raw_question, "positive", qwhere),
                    negative=_require_text(raw_question, "negative", qwhere),
                    resolved_expected=(int(raw_expected) if raw_expected is not None else None),
                )
            )
        tasks.append(
            Task(
                id=task_id,
                family=_require_text(raw_task, "family", where),
                ambiguous_text=_require_text(raw_task, "ambiguous_text", where),
                resolved_text=_require_text(raw_task, "resolved_text", where),
                questions=tuple(questions),  # type: ignore[arg-type]
            )
        )
    if not tasks:
        raise ValueError("Task file contains no tasks")
    return tasks


def cycle_edges(task: Task) -> list[tuple[Question, Question]]:
    q = task.questions
    return [(q[0], q[1]), (q[1], q[2]), (q[2], q[3]), (q[3], q[0])]
