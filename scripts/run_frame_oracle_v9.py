#!/usr/bin/env python3
"""Consume a committed v9 gate once with conservative atomic state."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import tempfile
from typing import Any
from urllib.request import Request, urlopen

from frame_oracle_v9_provenance import attest_and_record


IMPORT_PROVENANCE = attest_and_record()

from relaleap.hdpc.frame_oracle_v2 import closed_schema
from relaleap.hdpc.frame_oracle_v9 import SYSTEM_PROMPT_V9, normalize_proposal_v9, semantic_key


SEED = 3141592
DECODE = {"temperature": 0, "num_predict": 128, "paired_runs": 2}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_write_json(path: Path, value: dict[str, Any]) -> None:
    """Durably replace *path* with JSON, or leave the prior record intact."""
    parent = path.parent
    if not parent.is_dir():
        raise RuntimeError(f"output parent directory does not exist: {parent}")
    descriptor, raw_temporary = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=parent
    )
    temporary = Path(raw_temporary)
    try:
        with os.fdopen(descriptor, "w") as stream:
            json.dump(value, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0)
        directory_fd = os.open(parent, flags)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
    except BaseException:
        try:
            temporary.unlink(missing_ok=True)
        finally:
            raise


def ask(model: str, sentence: str) -> dict[str, Any]:
    payload = json.dumps(
        {
            "model": model,
            "system": SYSTEM_PROMPT_V9,
            "prompt": sentence,
            "format": closed_schema(),
            "stream": False,
            "think": False,
            "options": {"temperature": 0, "seed": SEED, "num_predict": 128},
        }
    ).encode()
    request = Request(
        "http://127.0.0.1:11434/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"},
    )
    with urlopen(request, timeout=300) as response:
        raw = json.load(response)
    return {"raw": raw, "frame": json.loads(raw["response"])}


def local_model_digest(model: str) -> str:
    """Read the model digest from the running local Ollama registry."""
    request = Request("http://127.0.0.1:11434/api/tags", method="GET")
    with urlopen(request, timeout=30) as response:
        registry = json.load(response)
    for entry in registry.get("models", []):
        if model in {entry.get("name"), entry.get("model")}:
            digest = entry.get("digest")
            if not isinstance(digest, str) or not digest:
                raise RuntimeError(f"local model {model!r} has no digest")
            return digest
    raise RuntimeError(f"local model {model!r} is absent from Ollama registry")


def verify_model_digest(expected: str, actual: str) -> None:
    expected_hex = expected.removeprefix("sha256:").lower()
    actual_hex = actual.removeprefix("sha256:").lower()
    if len(expected_hex) < 12 or not actual_hex.startswith(expected_hex):
        raise RuntimeError(f"local model digest mismatch: {actual} != {expected}")


def expected_key(value: dict[str, Any]) -> tuple[str, str, str, str, str, bool]:
    return (
        value["predicate"],
        value["entity_a"],
        value["entity_b"],
        value["polarity"],
        value["modality"],
        value["abstain"],
    )


def frozen_identifiers(
    args: argparse.Namespace, public: dict[str, Any], actual_digest: str
) -> dict[str, Any]:
    return {
        "version": 8,
        "contract_version": public["contract_version"],
        "answer_file_sha256": public["answer_file_sha256"],
        "public_file_sha256": sha256_file(args.public),
        "model": args.model,
        "model_digest_expected": args.model_digest,
        "model_digest_actual": actual_digest,
        "seed": SEED,
        "decode": DECODE,
        "system_prompt_sha256": hashlib.sha256(SYSTEM_PROMPT_V9.encode()).hexdigest(),
        "schema_sha256": hashlib.sha256(
            json.dumps(closed_schema(), sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
        "normalization": "v9 empty-slot fail-closed plus v7 proposal union-to-unknown and v6 all-occurrence union masking",
        "import_provenance": IMPORT_PROVENANCE,
    }


def run_gate(args: argparse.Namespace) -> dict[str, Any]:
    """Execute a resumeless one-use gate and return its terminal record."""
    if args.output.exists():
        raise RuntimeError(f"refusing to resume or replace existing output: {args.output}")

    public = json.loads(args.public.read_text())
    if public.get("contract_version") != "frame-oracle-v9-gate-1" or public.get("opened") is not False:
        raise RuntimeError("public gate does not match the frozen unopened contract")
    if public.get("answer_file_sha256") != args.answer_commitment:
        raise RuntimeError("public answer commitment differs from frozen CLI commitment")
    cases = public.get("cases")
    if not isinstance(cases, list) or not cases:
        raise RuntimeError("public gate has no cases")

    actual_digest = local_model_digest(args.model)
    verify_model_digest(args.model_digest, actual_digest)
    identifiers = frozen_identifiers(args, public, actual_digest)
    record: dict[str, Any] = {
        **identifiers,
        "state": "consumed_pending",
        "gate_consumed": True,
        "attempted_at": utc_now(),
        "completed_calls": 0,
        "total_calls": 2 * len(cases),
        "calls": [],
        "rows": [],
    }

    atomic_write_json(args.output, record)
    try:
        for case in cases:
            pair: list[dict[str, Any]] = []
            for repeat in (1, 2):
                response = ask(args.model, case["sentence"])
                call = {
                    "case_id": case["case_id"],
                    "repeat": repeat,
                    "raw": response["raw"],
                    "frame": response["frame"],
                }
                record["calls"].append(call)
                record["completed_calls"] = len(record["calls"])
                record["state"] = "consumed_partial"
                atomic_write_json(args.output, record)

                normalized = normalize_proposal_v9(case["sentence"], response["frame"])
                call["normalized"] = normalized.__dict__
                atomic_write_json(args.output, record)
                pair.append({"response": response, "normalized": normalized})

            row = {
                "case_id": case["case_id"],
                "sentence": case["sentence"],
                "stratum": case["stratum"],
                "first": pair[0]["response"],
                "second": pair[1]["response"],
                "first_normalized": pair[0]["normalized"].__dict__,
                "second_normalized": pair[1]["normalized"].__dict__,
                "deterministic": pair[0]["normalized"] == pair[1]["normalized"],
            }
            record["rows"].append(row)
            atomic_write_json(args.output, record)

        record["state"] = "consumed_decoded"
        atomic_write_json(args.output, record)

        answer_digest = sha256_file(args.answers)
        if answer_digest != public["answer_file_sha256"]:
            raise RuntimeError("answer commitment mismatch after paired decode")
        answers = json.loads(args.answers.read_text())
        if answers.get("contract_version") != public["contract_version"]:
            raise RuntimeError("answer contract mismatch after paired decode")
        answer_rows = answers.get("cases")
        if not isinstance(answer_rows, list):
            raise RuntimeError("answer cases are missing after paired decode")
        rows = record["rows"]
        if [row["case_id"] for row in answer_rows] != [row["case_id"] for row in rows]:
            raise RuntimeError("answer IDs differ from paired-decode IDs")

        failures = []
        for row, answer in zip(rows, answer_rows, strict=True):
            row["expected_semantic"] = expected_key(answer["expected"])
            row["exact"] = (
                semantic_key(normalize_proposal_v9(row["sentence"], row["first"]["frame"]))
                == tuple(row["expected_semantic"])
            )
            if not row["deterministic"]:
                failures.append(f"{row['case_id']}: paired normalized output differs")
            if not row["exact"]:
                failures.append(f"{row['case_id']}: semantic key mismatch")

        strata = sorted({row["stratum"] for row in rows})
        per_stratum = {
            stratum: {
                "count": sum(row["stratum"] == stratum for row in rows),
                "exact": sum(row["stratum"] == stratum and row["exact"] for row in rows),
            }
            for stratum in strata
        }
        summary = {
            "count": len(rows),
            "valid": len(rows),
            "deterministic": sum(row["deterministic"] for row in rows),
            "exact": sum(row["exact"] for row in rows),
            "per_stratum": per_stratum,
            "failures": failures,
            "gate": "passed" if not failures and len(rows) == 24 else "failed",
        }
        record["summary"] = summary
        record["state"] = "consumed_passed" if summary["gate"] == "passed" else "consumed_failed"
        atomic_write_json(args.output, record)
        return record
    except BaseException as exc:
        record["state"] = "consumed_failed"
        record["error"] = f"{type(exc).__name__}: {exc}"
        atomic_write_json(args.output, record)
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--public", type=Path, required=True)
    parser.add_argument("--answers", type=Path, required=True)
    parser.add_argument("--answer-commitment", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", default="qwen2.5:7b")
    parser.add_argument("--model-digest", required=True)
    return parser.parse_args()


def main() -> None:
    record = run_gate(parse_args())
    summary = record["summary"]
    print(json.dumps(summary, indent=2, sort_keys=True))
    if record["state"] != "consumed_passed":
        raise RuntimeError("frame oracle v9 gate failed closed")


if __name__ == "__main__":
    main()

