#!/usr/bin/env python3
"""Validate the unopened v12 gate without invoking an oracle or printing answers."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from collections import Counter
from pathlib import Path


REQUIRED_FIELDS = {
    "predicate", "entity_a", "entity_b", "polarity", "modality", "abstain"
}
PREDICATES = {"capital_of", "authored_by", "state", "located_in", "unknown"}
POLARITIES = {"affirmed", "negated", "unknown"}
MODALITIES = {"asserted", "possible", "unknown"}
STRATA = {
    "direct": 4,
    "explicit_negation": 6,
    "possible": 5,
    "paraphrase": 1,
    "abstention": 4,
    "world_knowledge_trap": 4,
}


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def exposed_sentences(
    worktree: Path, artifact: Path, prior_public: list[Path]
) -> set[str]:
    """Load comparison strings without emitting cases or overlap identifiers."""
    values: set[str] = set()
    for path in (
        worktree / "src/relaleap/hdpc/frame_oracle.py",
        worktree / "src/relaleap/hdpc/frame_oracle_v2.py",
        worktree / "src/relaleap/hdpc/frame_oracle_v3.py",
    ):
        tree = ast.parse(path.read_text())
        values.update(
            node.value
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
        )
    prior = load(artifact)
    values.update(row["sentence"] for row in prior["rows"] if "sentence" in row)
    for path in prior_public:
        values.update(row["sentence"] for row in load(path)["cases"])
    return values


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--public", type=Path, required=True)
    parser.add_argument("--answers", type=Path, required=True)
    parser.add_argument("--worktree", type=Path, required=True)
    parser.add_argument("--exposed-artifact", type=Path, required=True)
    parser.add_argument("--prior-public", type=Path, action="append", default=[])
    args = parser.parse_args()

    public = load(args.public)
    answers = load(args.answers)
    assert public["contract_version"] == answers["contract_version"] == "frame-oracle-v12-gate-1"
    digest = hashlib.sha256(args.answers.read_bytes()).hexdigest()
    assert public["answer_file_sha256"] == digest
    assert public["opened"] is False

    public_rows = public["cases"]
    answer_rows = answers["cases"]
    assert len(public_rows) == len(answer_rows) == 24
    public_ids = [row["case_id"] for row in public_rows]
    answer_ids = [row["case_id"] for row in answer_rows]
    assert len(set(public_ids)) == 24 and public_ids == answer_ids
    sentences = [row["sentence"] for row in public_rows]
    assert len(set(sentences)) == 24
    overlap = set(sentences) & exposed_sentences(
        args.worktree, args.exposed_artifact, args.prior_public
    )
    assert not overlap, f"exact sentence overlap count: {len(overlap)}"

    assert Counter(row["stratum"] for row in public_rows) == Counter(STRATA)
    expected = [row["expected"] for row in answer_rows]
    assert all(set(row) == REQUIRED_FIELDS for row in expected)
    assert {row["predicate"] for row in expected} == PREDICATES
    assert all(row["polarity"] in POLARITIES for row in expected)
    assert all(row["modality"] in MODALITIES for row in expected)
    assert sum(row["abstain"] for row in expected) == 4
    assert all((row["predicate"] == "unknown") == row["abstain"] for row in expected)
    assert all(
        row == {
            "predicate": "unknown",
            "entity_a": "",
            "entity_b": "",
            "polarity": "unknown",
            "modality": "unknown",
            "abstain": True,
        }
        for row in expected
        if row["abstain"]
    )
    assert sum(row["modality"] == "possible" for row in expected) == 5
    assert sum(row["polarity"] == "negated" for row in expected) == 6
    assert sum(row["predicate"] == "located_in" for row in expected) == 5
    assert all(
        (answer["expected"]["polarity"] == "negated") ==
        (public_row["stratum"] == "explicit_negation")
        for public_row, answer in zip(public_rows, answer_rows)
    )
    assert all(
        (answer["expected"]["modality"] == "possible") ==
        (public_row["stratum"] == "possible")
        for public_row, answer in zip(public_rows, answer_rows)
    )
    assert all(
        answer["expected"]["abstain"] ==
        (public_row["stratum"] == "abstention")
        for public_row, answer in zip(public_rows, answer_rows)
    )

    print(json.dumps({
        "answer_file_sha256": digest,
        "cases": len(public_rows),
        "exact_sentence_overlap_with_exposed_batteries": 0,
        "gate_opened": False,
        "located_in_cases": 5,
        "predicates": sorted(PREDICATES),
        "status": "sealed_gate_integrity_passed",
        "strata": STRATA,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
