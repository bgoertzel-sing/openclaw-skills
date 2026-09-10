from __future__ import annotations

from dataclasses import dataclass

from .tasks import Question, Task
from .util import randomized_labels, stable_seed


SYSTEM_PROMPT = """You are participating in a repeated psycholinguistic choice experiment.
Treat every trial as independent of all other trials. Use only the passage and the announced pair of questions.
The passage may remain genuinely ambiguous. Choose the interpretation that currently seems more plausible; do not invent extra facts.
Do not explain your answer. Return exactly one JSON object of the form {"choice":"A"} or {"choice":"B"}.
""".strip()


@dataclass(frozen=True)
class DisplayedQuestion:
    question: Question
    label_texts: dict[str, str]
    label_values: dict[str, int]


@dataclass(frozen=True)
class TrialPrompt:
    first_messages: list[dict[str, str]]
    second_user_message: str
    first: DisplayedQuestion
    second: DisplayedQuestion


def _display_question(question: Question, seed: int) -> DisplayedQuestion:
    texts, values = randomized_labels(question.positive, question.negative, seed)
    return DisplayedQuestion(question=question, label_texts=texts, label_values=values)


def _question_block(title: str, displayed: DisplayedQuestion) -> str:
    return (
        f"{title} [{displayed.question.id}]\n"
        f"{displayed.question.prompt}\n"
        f"A. {displayed.label_texts['A']}\n"
        f"B. {displayed.label_texts['B']}"
    )


def build_trial_prompt(
    *,
    task: Task,
    condition: str,
    first_question: Question,
    second_question: Question,
    base_seed: int,
    trial_key: str,
) -> TrialPrompt:
    first_seed = stable_seed(base_seed, trial_key, "labels", "first")
    second_seed = stable_seed(base_seed, trial_key, "labels", "second")
    first = _display_question(first_question, first_seed)
    second = _display_question(second_question, second_seed)
    passage = task.passage(condition)

    first_user = f"""PASSAGE
{passage}

This trial contains two binary judgments in the following order:
1. {first.question.prompt}
2. {second.question.prompt}

Both questions are part of the announced context. Answer only the FIRST question now. You will answer the second after your first response.

{_question_block('FIRST QUESTION', first)}

For context only, the SECOND question will be:
{_question_block('SECOND QUESTION (do not answer yet)', second)}

Return only the required JSON object for the FIRST question."""

    second_user = f"""Now answer the SECOND question in the announced pair. Keep the same passage in mind and do not revise the first answer.

{_question_block('SECOND QUESTION', second)}

Return only the required JSON object for the SECOND question."""

    return TrialPrompt(
        first_messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": first_user},
        ],
        second_user_message=second_user,
        first=first,
        second=second,
    )
