#!/usr/bin/env python3
"""Manifest-verified, idempotent ProtoCosmo2 memory snapshot importer.

This tool intentionally has no default namespace.  Callers must name an isolated
ChromaDB directory, which prevents accidental writes to OmegaClaw's live store.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

COLLECTION = "protocosmo2_imported_v1"
EMBEDDING = "hashing-token-v1-384"
DIMENSIONS = 384
INDEXED_CLASSES = {
    "curated-memory", "daily-memory", "catalog", "project-doc",
    "project-record", "experiment-record",
}
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TOKEN = re.compile(r"[a-z0-9][a-z0-9_.:/+-]*", re.I)
OBLIGATION = re.compile(r"^\s*[-*]\s*\[[ xX]\]\s+(.+)$")
DATE_PATH = re.compile(r"(?:^|/)(20\d{2}-\d{2}-\d{2})(?:[^/]*)\.md$")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def document_id(source_path: str, digest: str) -> str:
    return "doc_" + sha256((source_path + "\0" + digest).encode())


def chunk_id(doc_id: str, start: int, end: int, text: str) -> str:
    material = f"{doc_id}\0{start}\0{end}\0{sha256(text.encode())}"
    return "chunk_" + sha256(material.encode())


def embedding(text: str) -> list[float]:
    """Deterministic signed feature hashing; suitable for offline validation."""
    vector = [0.0] * DIMENSIONS
    tokens = TOKEN.findall(text.lower())
    features = tokens + [f"{a}::{b}" for a, b in zip(tokens, tokens[1:])]
    for feature in features:
        raw = hashlib.sha256(feature.encode()).digest()
        index = int.from_bytes(raw[:4], "big") % DIMENSIONS
        vector[index] += 1.0 if raw[4] & 1 else -1.0
    norm = math.sqrt(sum(value * value for value in vector)) or 1.0
    return [value / norm for value in vector]


def source_date(path: str) -> str:
    match = DATE_PATH.search(path)
    return match.group(1) if match else ""


def project_name(path: str) -> str:
    parts = Path(path).parts
    return parts[1] if len(parts) > 2 and parts[0] == "projects" else ""


def authority(path: str, source_class: str) -> tuple[str, int]:
    name = Path(path).name.upper()
    if source_class == "project-record" and name in {"PROJECT.MD", "TASKS.MD", "DECISIONS.MD", "NOTES.MD"}:
        return "project-source-of-truth", 100
    if source_class == "catalog":
        return "cross-project-source-of-truth", 95
    if source_class == "experiment-record":
        return "experiment-evidence", 90
    if source_class == "curated-memory":
        return "curated-memory", 75
    if source_class in {"project-record", "project-doc"}:
        return "project-supporting-record", 70
    return "daily-memory", 35


def supersession(text: str) -> str:
    lowered = text.lower()
    if "supersed" in lowered:
        return "explicit-supersession-text"
    if any(word in lowered for word in ("correction", "retired belief", "deprecated")):
        return "correction-or-retirement-text"
    return "none-declared"


def markdown_chunks(text: str, max_chars: int = 5000) -> list[dict]:
    """Return heading-aware chunks with inclusive 1-based source line ranges."""
    lines = text.splitlines()
    if not lines:
        return []
    headings: list[tuple[int, int, str]] = []
    for number, line in enumerate(lines, 1):
        match = HEADING.match(line)
        if match:
            headings.append((number, len(match.group(1)), match.group(2).strip()))
    boundaries = [item[0] for item in headings] or [1]
    if boundaries[0] != 1:
        boundaries.insert(0, 1)
    stack: dict[int, str] = {}
    heading_by_line = {line: (level, title) for line, level, title in headings}
    chunks: list[dict] = []
    for pos, start in enumerate(boundaries):
        end = (boundaries[pos + 1] - 1) if pos + 1 < len(boundaries) else len(lines)
        if start in heading_by_line:
            level, title = heading_by_line[start]
            for old in list(stack):
                if old >= level:
                    del stack[old]
            stack[level] = title
        breadcrumb = " > ".join(stack[level] for level in sorted(stack))
        cursor = start
        while cursor <= end:
            candidate_end = cursor
            size = 0
            while candidate_end <= end:
                addition = len(lines[candidate_end - 1]) + 1
                if size and size + addition > max_chars:
                    break
                size += addition
                candidate_end += 1
            actual_end = max(cursor, candidate_end - 1)
            body = "\n".join(lines[cursor - 1:actual_end]).strip()
            if body:
                chunks.append({"text": body, "start": cursor, "end": actual_end,
                               "heading": breadcrumb})
            cursor = actual_end + 1
    return chunks


def load_manifest(snapshot: Path) -> tuple[dict, list[dict]]:
    manifest_path = snapshot / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = [entry for entry in manifest["included"] if entry["source_class"] in INDEXED_CLASSES]
    return manifest, entries


def prepare(snapshot: Path) -> tuple[list[dict], dict]:
    manifest, entries = load_manifest(snapshot)
    records: list[dict] = []
    document_counts = Counter()
    obligation_keys: set[str] = set()
    for entry in entries:
        path = entry["path"]
        source = snapshot / path
        raw = source.read_bytes()
        actual = sha256(raw)
        if actual != entry["sha256"]:
            raise RuntimeError(f"manifest digest mismatch: {path}: expected {entry['sha256']}, got {actual}")
        text = raw.decode("utf-8")
        doc_id = document_id(path, actual)
        authority_name, priority = authority(path, entry["source_class"])
        for line in text.splitlines():
            match = OBLIGATION.match(line)
            if match and (Path(path).name.upper() == "TASKS.MD" or path == "catalog/KANBAN.md"):
                obligation_keys.add(sha256((path + "\0" + match.group(1).strip()).encode()))
        for chunk in markdown_chunks(text):
            cid = chunk_id(doc_id, chunk["start"], chunk["end"], chunk["text"])
            metadata = {
                "namespace": COLLECTION,
                "document_id": doc_id,
                "source_path": path,
                "source_digest": actual,
                "source_class": entry["source_class"],
                "source_date": source_date(path),
                "project": project_name(path),
                "authority": authority_name,
                "authority_priority": priority,
                "line_start": chunk["start"],
                "line_end": chunk["end"],
                "heading": chunk["heading"],
                "supersession": supersession(chunk["text"]),
                "embedding": EMBEDDING,
            }
            records.append({"id": cid, "document": chunk["text"], "metadata": metadata})
        document_counts[entry["source_class"]] += 1
    receipt = {
        "format": "protocosmo2-memory-import-receipt-v1",
        "collection": COLLECTION,
        "snapshot_manifest_sha256": sha256((snapshot / "manifest.json").read_bytes()),
        "documents": len(entries),
        "chunks": len(records),
        "embeddings": len(records),
        "unique_obligations": len(obligation_keys),
        "documents_by_class": dict(sorted(document_counts.items())),
        "corpus_digest": sha256(canonical_json([
            [record["id"], record["metadata"]["source_digest"]] for record in records
        ]).encode()),
    }
    return records, receipt


def batches(items: list[dict], size: int = 128) -> Iterable[list[dict]]:
    for offset in range(0, len(items), size):
        yield items[offset:offset + size]


def open_collection(namespace: Path):
    import chromadb
    namespace.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(namespace))
    return client.get_or_create_collection(name=COLLECTION, embedding_function=None)


def do_import(snapshot: Path, namespace: Path) -> dict:
    records, receipt = prepare(snapshot)
    collection = open_collection(namespace)
    before = collection.count()
    for batch in batches(records):
        collection.upsert(
            ids=[row["id"] for row in batch],
            documents=[row["document"] for row in batch],
            metadatas=[row["metadata"] for row in batch],
            embeddings=[embedding(row["document"]) for row in batch],
        )
    after = collection.count()
    receipt.update({"count_before": before, "count_after": after,
                    "inserted_or_updated": len(records), "idempotent_count": after == len(records)})
    receipt_path = namespace / "import-receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return receipt


def query(namespace: Path, text: str, limit: int) -> list[dict]:
    collection = open_collection(namespace)
    # The baseline hashing embedding is deliberately provider-free and coarse.
    # Retrieve the full imported corpus so lexical/authority reranking cannot
    # miss an authoritative record merely because it fell outside a small ANN
    # candidate window. A later semantic model may safely reduce this window.
    raw = collection.query(query_embeddings=[embedding(text)], n_results=collection.count(),
                           include=["documents", "metadatas", "distances"])
    query_terms = set(TOKEN.findall(text.lower()))
    ranked = []
    for cid, document, metadata, distance in zip(raw["ids"][0], raw["documents"][0],
                                                  raw["metadatas"][0], raw["distances"][0]):
        doc_terms = set(TOKEN.findall(document.lower()))
        lexical = len(query_terms & doc_terms) / max(1, len(query_terms))
        semantic = 1.0 - float(distance)
        authority_boost = int(metadata["authority_priority"]) / 500.0
        stale_penalty = 0.12 if metadata["source_class"] == "daily-memory" else 0.0
        score = semantic + (0.65 * lexical) + authority_boost - stale_penalty
        ranked.append({"id": cid, "score": round(score, 6), "distance": round(float(distance), 6),
                       "source_path": metadata["source_path"], "lines": [metadata["line_start"], metadata["line_end"]],
                       "heading": metadata["heading"], "authority": metadata["authority"],
                       "source_class": metadata["source_class"], "document": document,
                       "_priority": int(metadata["authority_priority"])})
    ranked.sort(key=lambda row: (-row["score"], -row["_priority"], row["id"]))
    for row in ranked[:limit]:
        del row["_priority"]
    return ranked[:limit]


def stats(namespace: Path) -> dict:
    collection = open_collection(namespace)
    data = collection.get(include=["documents", "metadatas"])
    ids = data["ids"]
    documents = {meta["document_id"] for meta in data["metadatas"]}
    obligations = set()
    canonical = []
    for cid, document, meta in zip(ids, data["documents"], data["metadatas"]):
        canonical.append([cid, sha256(document.encode()), meta])
        if Path(meta["source_path"]).name.upper() == "TASKS.MD" or meta["source_path"] == "catalog/KANBAN.md":
            for line in document.splitlines():
                match = OBLIGATION.match(line)
                if match:
                    obligations.add(sha256((meta["source_path"] + "\0" + match.group(1).strip()).encode()))
    return {"collection": COLLECTION, "chunks": len(ids), "unique_chunk_ids": len(set(ids)),
            "documents": len(documents), "unique_obligations": len(obligations),
            "duplicate_chunk_ids": len(ids) - len(set(ids)),
            "content_digest": sha256(canonical_json(sorted(canonical)).encode())}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--namespace", required=True, type=Path,
                        help="isolated ChromaDB directory (no default by design)")
    sub = parser.add_subparsers(dest="command", required=True)
    imp = sub.add_parser("import")
    imp.add_argument("--snapshot", required=True, type=Path)
    qry = sub.add_parser("query")
    qry.add_argument("text")
    qry.add_argument("--limit", type=int, default=5)
    sub.add_parser("stats")
    args = parser.parse_args()
    if args.command == "import":
        result = do_import(args.snapshot.resolve(), args.namespace.resolve())
    elif args.command == "query":
        result = query(args.namespace.resolve(), args.text, args.limit)
    else:
        result = stats(args.namespace.resolve())
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"memory_import.py: ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
