#!/usr/bin/env python3
"""Create a deterministic, sanitized ProtoCosmo2 source snapshot.

The script deliberately has no runtime, network, provider, or credential
integration. It copies only an explicit allowlist of regular files into a new
destination and emits JSON receipts. A suspicious path or text match aborts
before destination creation.
"""
from __future__ import annotations

import argparse, hashlib, json, os, re, shutil, stat, sys
from pathlib import Path

MAX_BYTES = 4 * 1024 * 1024
ROOT_FILES = ("AGENTS.md", "SOUL.md", "IDENTITY.md", "USER.md", "TOOLS.md", "MEMORY.md")
PROJECT_FILES = ("PROJECT.md", "TASKS.md", "DECISIONS.md", "NOTES.md")
# Filename words such as "token" occur legitimately in scientific experiment
# names. Deny concrete credential locations/names instead; content scanning is
# the second, independent gate.
PATH_DENY = re.compile(r"(^|/)(?:\.openclaw)(?:/|$)|(^|/)\.env[^/]*$|(^|/)(?:id_rsa|id_ed25519|credentials(?:\.json)?|secrets?(?:\.[^/]+)?|.*\.pem)$", re.I)
CONTENT_DENY = re.compile(r"(?:BEGIN (?:[A-Z ]*PRIVATE KEY|OPENSSH PRIVATE KEY)|(?:api[_-]?key|token|password|secret)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,})", re.I)

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def candidates(root: Path):
    for name in ROOT_FILES:
        yield root / name, "identity-policy" if name != "MEMORY.md" else "curated-memory"
    for path in sorted((root / "memory").glob("*.md")):
        yield path, "daily-memory"
    for path in sorted((root / "catalog").glob("*.md")):
        yield path, "catalog"
    for project in sorted((root / "projects").iterdir()):
        if not project.is_dir(): continue
        for name in PROJECT_FILES:
            yield project / name, "project-record"
        for path in sorted((project / "docs").glob("*.md")) if (project / "docs").is_dir() else ():
            yield path, "project-doc"
        for path in sorted((project / "experiments").glob("*/RUN.md")) if (project / "experiments").is_dir() else ():
            yield path, "experiment-record"
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        yield path, "skill"
    for path in sorted((root / "bin").iterdir()):
        if path.is_file() and os.access(path, os.X_OK): yield path, "helper-script"

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--destination", type=Path, required=True)
    args = p.parse_args(); root = args.source.resolve(); dest = args.destination
    if dest.exists(): raise SystemExit(f"refusing existing destination: {dest}")
    rows, exclusions, failures = [], [], []
    seen = set()
    for path, source_class in candidates(root):
        rel = path.relative_to(root).as_posix()
        if rel in seen: continue
        seen.add(rel)
        if not path.exists():
            exclusions.append({"path": rel, "reason": "absent optional candidate"}); continue
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode) or not stat.S_ISREG(mode):
            exclusions.append({"path": rel, "reason": "non-regular or symlink candidate refused"}); continue
        if PATH_DENY.search(rel):
            failures.append({"path": rel, "reason": "denied path class"}); continue
        size = path.stat().st_size
        if size > MAX_BYTES:
            exclusions.append({"path": rel, "reason": f"exceeds {MAX_BYTES} byte cap", "size": size}); continue
        data = path.read_bytes()
        if CONTENT_DENY.search(data.decode("utf-8", errors="replace")):
            failures.append({"path": rel, "reason": "secret-like content match"}); continue
        rows.append({"path": rel, "source_class": source_class, "bytes": size, "sha256": hashlib.sha256(data).hexdigest()})
    receipt = {"format": "protocosmo2-phase1-manifest-v1", "source": str(root), "included": rows, "exclusions": exclusions, "failures": failures,
               "policy": "regular non-symlink files only; explicit allowlist; 4 MiB cap; no credentials, sessions, runtime state, repositories, binaries, or caches"}
    if failures:
        print(json.dumps(receipt, indent=2, sort_keys=True)); return 2
    dest.mkdir(parents=True)
    for row in rows:
        src, out = root / row["path"], dest / row["path"]
        out.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(src, out); os.chmod(out, 0o400)
    (dest / "manifest.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    os.chmod(dest / "manifest.json", 0o400)
    print(json.dumps({"included_count": len(rows), "excluded_count": len(exclusions), "aggregate_sha256": hashlib.sha256("".join(r["sha256"] for r in rows).encode()).hexdigest()}, sort_keys=True))
    return 0
if __name__ == "__main__": raise SystemExit(main())
