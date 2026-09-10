"""Provenance helpers for OmegaSim experiment wrappers.

These helpers are intentionally independent of the frozen CLA detector. They
only make concurrently computed records canonical before serialization.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


ROW_ORDER = (
    "sweep",
    "gain",
    "coupling",
    "delay",
    "seed",
    "control",
    "stratum",
)


def canonical_sort_rows(
    rows: Iterable[Mapping[str, Any]],
    *,
    fields: tuple[str, ...] = ROW_ORDER,
) -> list[Mapping[str, Any]]:
    """Return rows in a stable order and fail closed on ambiguous identities."""
    materialized = list(rows)
    for index, row in enumerate(materialized):
        missing = tuple(field for field in fields if field not in row)
        if missing:
            raise ValueError(f"row {index} is missing canonical fields: {missing}")

    def key(row: Mapping[str, Any]) -> tuple[tuple[str, str], ...]:
        return tuple((type(row[field]).__name__, repr(row[field])) for field in fields)

    ordered = sorted(materialized, key=key)
    identities = [key(row) for row in ordered]
    if len(identities) != len(set(identities)):
        raise ValueError("duplicate canonical row identity")
    return ordered
