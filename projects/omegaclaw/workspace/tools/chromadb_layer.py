#!/usr/bin/env python3
"""
OmegaClaw ChromaDB Layer — activation and query interface.

This bridges the OmegaClaw-Core RAG infrastructure (rag.py + lib_chromadb)
into a standalone CLI tool that ProtomegaTron can invoke from any session.

Usage:
    python3 chromadb_layer.py init          # Ingest knowledge-priors into ChromaDB
    python3 chromadb_layer.py query "text"  # Semantic search over stored knowledge
    python3 chromadb_layer.py remember "text" # Store a runtime memory
    python3 chromadb_layer.py status        # Show collection stats
    python3 chromadb_layer.py recall "text" # Query runtime memories only
"""

import os
import sys
import json
import glob
import hashlib
import re
import uuid
import time

import chromadb

# --- Paths ---------------------------------------------------------------

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT = os.path.dirname(WORKSPACE)
RESEARCH = os.path.dirname(os.path.dirname(PROJECT))  # /home/openclaw/research-agent
REPO = os.path.join(RESEARCH, "repos", "OmegaClaw-Core")

DB_PATH = os.environ.get(
    "CHROMA_DB_PATH",
    os.path.join(PROJECT, "chroma_db")
)

KNOWLEDGE_DIR = os.path.join(REPO, "knowledge-priors")

# --- Constants -----------------------------------------------------------

KNOWLEDGE_COLLECTION = "knowledge_priors"
MEMORY_COLLECTION = "memories"
TOP_K = 8
MIN_CHUNK_CHARS = 100
MAX_CHUNK_CHARS = 6000

# --- Client --------------------------------------------------------------

_client = None

def get_client():
    global _client
    if _client is None:
        os.makedirs(DB_PATH, exist_ok=True)
        _client = chromadb.PersistentClient(path=DB_PATH)
    return _client

def get_collection(name):
    return get_client().get_or_create_collection(
        name=name,
        metadata={"hnsw:space": "cosine"}
    )

# --- Embedding (using chromadb's built-in default) -----------------------
# ChromaDB >= 0.4 uses all-MiniLM-L6-v2 by default via sentence-transformers.
# This gives us local embeddings without needing OpenAI API calls.

def embed_texts(texts):
    """Use chromadb's default embedding function (all-MiniLM-L6-v2)."""
    from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
    ef = DefaultEmbeddingFunction()
    return ef(texts)

# --- Chunking (adapted from rag.py) --------------------------------------

HEADING_RE = re.compile(r"^(#{1,4})\s+(.+)$", re.MULTILINE)

def chunk_markdown(text, filename):
    """Heading-aware markdown chunking with breadcrumb tracking."""
    matches = list(HEADING_RE.finditer(text))
    if not matches:
        return [{"text": text.strip(), "breadcrumb": filename}]

    sections = []
    stack = {}

    for i, m in enumerate(matches):
        level = len(m.group(1))
        heading = m.group(2).strip()

        for lvl in list(stack):
            if lvl >= level:
                del stack[lvl]
        stack[level] = heading

        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()

        breadcrumb = filename + " > " + " > ".join(
            stack[k] for k in sorted(stack)
        )
        sections.append({"text": body, "breadcrumb": breadcrumb, "heading": heading})

    # Skip TOC
    sections = [s for s in sections if "table of contents" not in s.get("heading", "").lower()]

    # Merge small sections
    merged = []
    carry = ""
    carry_bc = ""
    for s in sections:
        combined = (carry + "\n\n" + s["text"]).strip() if carry else s["text"]
        bc = carry_bc or s["breadcrumb"]
        if len(combined) < MIN_CHUNK_CHARS and s is not sections[-1]:
            carry = combined
            carry_bc = bc
        else:
            merged.append({"text": combined, "breadcrumb": bc})
            carry = ""
            carry_bc = ""
    if carry:
        if merged:
            merged[-1]["text"] += "\n\n" + carry
        else:
            merged.append({"text": carry, "breadcrumb": carry_bc})

    # Split large sections
    final = []
    for s in merged:
        if len(s["text"]) <= MAX_CHUNK_CHARS:
            final.append(s)
            continue
        paragraphs = s["text"].split("\n\n")
        chunk_text = ""
        for p in paragraphs:
            if chunk_text and len(chunk_text) + len(p) > MAX_CHUNK_CHARS:
                final.append({"text": chunk_text.strip(), "breadcrumb": s["breadcrumb"]})
                chunk_text = p
            else:
                chunk_text = (chunk_text + "\n\n" + p).strip()
        if chunk_text.strip():
            final.append({"text": chunk_text.strip(), "breadcrumb": s["breadcrumb"]})

    return final

# --- Init Knowledge ------------------------------------------------------

def file_hash(filepath):
    return hashlib.md5(open(filepath, "rb").read()).hexdigest()

def init_knowledge():
    """Chunk, embed, and store knowledge-prior files."""
    collection = get_collection(KNOWLEDGE_COLLECTION)

    if not os.path.isdir(KNOWLEDGE_DIR):
        print(f"ERROR: Knowledge dir not found: {KNOWLEDGE_DIR}")
        return False

    md_files = sorted(glob.glob(os.path.join(KNOWLEDGE_DIR, "*.md")))
    if not md_files:
        print("No markdown files found in knowledge-priors/")
        return False

    total_chunks = 0
    for filepath in md_files:
        filename = os.path.basename(filepath)
        current_hash = file_hash(filepath)

        # Check if already indexed with same hash
        try:
            existing = collection.get(
                ids=[f"hash_{filename}"],
                include=["metadatas"]
            )
            if existing["ids"] and existing["metadatas"][0].get("hash") == current_hash:
                print(f"  {filename}: unchanged (skipped)")
                continue
        except Exception:
            pass

        # Delete old chunks for this file
        try:
            old = collection.get(where={"source": filename}, include=[])
            if old["ids"]:
                collection.delete(ids=old["ids"])
        except Exception:
            pass

        # Chunk
        text = open(filepath, "r", encoding="utf-8").read()
        chunks = chunk_markdown(text, filename)
        if not chunks:
            continue

        texts = [c["text"] for c in chunks]
        embeddings = embed_texts(texts)

        # Store chunks
        ids = [f"{filename}_chunk_{i}" for i in range(len(chunks))]
        metadatas = [
            {
                "source": filename,
                "breadcrumb": c["breadcrumb"],
                "type": "chunk",
                "time": "knowledge_prior"
            }
            for c in chunks
        ]
        collection.upsert(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas,
        )

        # Store hash sentinel
        dim = len(embeddings[0])
        collection.upsert(
            ids=[f"hash_{filename}"],
            embeddings=[[0.0] * dim],
            documents=[f"hash sentinel for {filename}"],
            metadatas=[{"type": "hash", "hash": current_hash, "source": filename}],
        )

        print(f"  {filename}: indexed {len(chunks)} chunks")
        total_chunks += len(chunks)

    print(f"\nTotal: {total_chunks} new chunks indexed")
    return True

# --- Query ---------------------------------------------------------------

def query_knowledge(query_text, top_k=TOP_K):
    """Semantic search over knowledge priors."""
    collection = get_collection(KNOWLEDGE_COLLECTION)
    embedding = embed_texts([query_text])[0]

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k,
        where={"type": "chunk"},
        include=["documents", "metadatas", "distances"],
    )

    hits = []
    for i in range(len(results["ids"][0])):
        hits.append({
            "id": results["ids"][0][i],
            "text": results["documents"][0][i],
            "breadcrumb": results["metadatas"][0][i].get("breadcrumb", ""),
            "source": results["metadatas"][0][i].get("source", ""),
            "distance": results["distances"][0][i],
        })
    return hits

# --- Runtime Memory (remember/recall) ------------------------------------

def remember(content, metadata=None):
    """Store a runtime memory with embedding."""
    collection = get_collection(MEMORY_COLLECTION)
    embedding = embed_texts([content])[0]
    item_id = str(uuid.uuid4())
    meta = {
        "type": "memory",
        "time": str(int(time.time())),
    }
    if metadata:
        meta.update(metadata)
    collection.add(
        ids=[item_id],
        embeddings=[embedding],
        documents=[content],
        metadatas=[meta],
    )
    return item_id

def recall(query_text, top_k=TOP_K):
    """Query runtime memories."""
    collection = get_collection(MEMORY_COLLECTION)
    count = collection.count()
    if count == 0:
        return []
    embedding = embed_texts([query_text])[0]
    results = collection.query(
        query_embeddings=[embedding],
        n_results=min(top_k, count),
        include=["documents", "metadatas", "distances"],
    )
    hits = []
    for i in range(len(results["ids"][0])):
        hits.append({
            "id": results["ids"][0][i],
            "text": results["documents"][0][i],
            "time": results["metadatas"][0][i].get("time", ""),
            "distance": results["distances"][0][i],
        })
    return hits

# --- Status --------------------------------------------------------------

def status():
    """Show collection statistics."""
    client = get_client()
    info = {"db_path": DB_PATH, "collections": {}}
    for name in [KNOWLEDGE_COLLECTION, MEMORY_COLLECTION]:
        try:
            col = client.get_or_create_collection(name=name)
            count = col.count()
            # Count non-sentinel entries
            try:
                chunks = col.get(where={"type": "chunk"}, include=[])
                chunk_count = len(chunks["ids"])
            except Exception:
                chunk_count = "?"
            try:
                mems = col.get(where={"type": "memory"}, include=[])
                mem_count = len(mems["ids"])
            except Exception:
                mem_count = "?"
            info["collections"][name] = {
                "total_entries": count,
                "chunks": chunk_count,
                "memories": mem_count,
            }
        except Exception as e:
            info["collections"][name] = {"error": str(e)}
    return info

# --- CLI -----------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "init":
        print(f"Initializing ChromaDB at {DB_PATH}")
        print(f"Knowledge priors from {KNOWLEDGE_DIR}\n")
        init_knowledge()
        s = status()
        print(f"\nStatus: {json.dumps(s, indent=2)}")

    elif cmd == "query":
        if len(sys.argv) < 3:
            print("Usage: chromadb_layer.py query 'search text'")
            sys.exit(1)
        query_text = " ".join(sys.argv[2:])
        hits = query_knowledge(query_text)
        for i, h in enumerate(hits):
            print(f"\n--- Hit {i+1} (dist={h['distance']:.4f}) [{h['breadcrumb']}] ---")
            print(h["text"][:500])

    elif cmd == "remember":
        if len(sys.argv) < 3:
            print("Usage: chromadb_layer.py remember 'content to store'")
            sys.exit(1)
        content = " ".join(sys.argv[2:])
        item_id = remember(content)
        print(f"Stored memory: {item_id}")

    elif cmd == "recall":
        if len(sys.argv) < 3:
            print("Usage: chromadb_layer.py recall 'query text'")
            sys.exit(1)
        query_text = " ".join(sys.argv[2:])
        hits = recall(query_text)
        if not hits:
            print("No runtime memories stored yet.")
        for i, h in enumerate(hits):
            print(f"\n--- Memory {i+1} (dist={h['distance']:.4f}, t={h['time']}) ---")
            print(h["text"][:500])

    elif cmd == "status":
        s = status()
        print(json.dumps(s, indent=2))

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)

if __name__ == "__main__":
    main()
