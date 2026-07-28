#!/usr/bin/env python3
"""Fail-closed repository and file identity verifier for measured runs."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.rstrip("\r\n")


def verify_repo(repo: Path, expected_commit: str) -> dict[str, object]:
    result: dict[str, object] = {
        "path": str(repo.resolve()),
        "expected_commit": expected_commit,
        "observed_commit": None,
        "clean": False,
        "status_porcelain": None,
        "ok": False,
    }
    try:
        observed_commit = git(repo, "rev-parse", "HEAD")
        status = git(repo, "status", "--porcelain")
    except (OSError, subprocess.CalledProcessError) as error:
        result["error"] = f"{type(error).__name__}: {error}"
        return result
    result.update(
        observed_commit=observed_commit,
        clean=not status,
        status_porcelain=status.splitlines(),
        ok=observed_commit == expected_commit and not status,
    )
    return result


def verify_file(path: Path, expected_sha256: str) -> dict[str, object]:
    result: dict[str, object] = {
        "path": str(path.resolve()),
        "expected_sha256": expected_sha256,
        "observed_sha256": None,
        "ok": False,
    }
    try:
        observed_sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as error:
        result["error"] = f"{type(error).__name__}: {error}"
        return result
    result.update(
        observed_sha256=observed_sha256,
        ok=observed_sha256 == expected_sha256,
    )
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", action="append", nargs=3, metavar=("NAME", "PATH", "COMMIT"), default=[])
    parser.add_argument("--file", action="append", nargs=3, metavar=("NAME", "PATH", "SHA256"), default=[])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if not args.repo or not args.file:
        parser.error("at least one --repo and one --file identity are required")
    repo_names = [name for name, _, _ in args.repo]
    file_names = [name for name, _, _ in args.file]
    if len(repo_names) != len(set(repo_names)) or len(file_names) != len(set(file_names)):
        parser.error("identity names must be unique within repositories and files")

    report = {
        "repositories": {name: verify_repo(Path(path), commit) for name, path, commit in args.repo},
        "files": {name: verify_file(Path(path), digest) for name, path, digest in args.file},
    }
    report["ok"] = all(item["ok"] for group in (report["repositories"], report["files"]) for item in group.values())
    serialized = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(serialized, encoding="utf-8")
    print(serialized, end="")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
