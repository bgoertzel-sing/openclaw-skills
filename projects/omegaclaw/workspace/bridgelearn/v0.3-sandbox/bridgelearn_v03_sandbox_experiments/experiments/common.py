from __future__ import annotations

import csv
import json
import math
import platform
import sys
from pathlib import Path
from typing import Any, Iterable, Mapping

import numpy as np


def to_builtin(value: Any) -> Any:
    """Convert NumPy-rich objects into JSON-serializable Python objects."""
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {str(key): to_builtin(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_builtin(item) for item in value]
    return value


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(to_builtin(payload), indent=2, sort_keys=True) + "\n")


def write_csv(path: Path, rows: Iterable[Mapping[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: to_builtin(row.get(key)) for key in fieldnames})


def rmse(predicted: np.ndarray, actual: np.ndarray) -> float:
    predicted = np.asarray(predicted, dtype=np.float64)
    actual = np.asarray(actual, dtype=np.float64)
    return float(np.sqrt(np.mean((predicted - actual) ** 2)))


def first_crossing(values: np.ndarray, threshold: float = 1.0) -> int | None:
    indices = np.flatnonzero(np.asarray(values) >= threshold)
    return None if indices.size == 0 else int(indices[0])


def safe_ratio(numerator: float, denominator: float) -> float:
    return float(numerator / denominator) if denominator != 0.0 else math.inf


def environment_record() -> dict[str, Any]:
    try:
        import bridgelearn

        bridgelearn_version = bridgelearn.__version__
        bridgelearn_path = bridgelearn.__file__
    except Exception as exc:  # pragma: no cover - defensive diagnostics
        bridgelearn_version = f"unavailable: {exc}"
        bridgelearn_path = None
    try:
        import matplotlib

        matplotlib_version = matplotlib.__version__
    except Exception as exc:  # pragma: no cover
        matplotlib_version = f"unavailable: {exc}"
    return {
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "matplotlib": matplotlib_version,
        "bridgelearn": bridgelearn_version,
        "bridgelearn_path": bridgelearn_path,
    }
