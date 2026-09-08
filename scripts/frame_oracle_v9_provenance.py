"""Fail-closed import attestation for the one-use frame-oracle v9 runner."""
from __future__ import annotations

import hashlib
import importlib
import json
import os
from pathlib import Path
import sys
from types import ModuleType
from typing import Any


_SCRIPT_DIR = Path(__file__).resolve().parent
_CONTRACT_PATH = _SCRIPT_DIR / "frame_oracle_v9_import_contract.json"
_SOURCE_ROOT_ENV = "RELALEAP_FRAME_ORACLE_V9_SOURCE_ROOT"
_OUTPUT_ENV = "RELALEAP_FRAME_ORACLE_V9_PROVENANCE_OUTPUT"


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _resolved_module_file(module: ModuleType, package_root: Path) -> Path:
    raw_path = getattr(module, "__file__", None)
    if raw_path is None:
        raise RuntimeError(f"imported module {module.__name__!r} has no source file")
    path = Path(raw_path).resolve(strict=True)
    try:
        path.relative_to(package_root)
    except ValueError as exc:
        raise RuntimeError(
            f"imported module {module.__name__!r} escaped source root: {path}"
        ) from exc
    return path


def attest_and_record() -> dict[str, Any]:
    """Verify one source root and persist evidence before CLI parsing."""
    raw_source_root = os.environ.get(_SOURCE_ROOT_ENV)
    raw_output = os.environ.get(_OUTPUT_ENV)
    if not raw_source_root or not raw_output:
        raise RuntimeError(
            f"{_SOURCE_ROOT_ENV} and {_OUTPUT_ENV} are required; use the pinned wrapper"
        )

    source_root = Path(raw_source_root).resolve(strict=True)
    package_root = (source_root / "relaleap").resolve(strict=True)
    try:
        package_root.relative_to(source_root)
    except ValueError as exc:
        raise RuntimeError(f"relaleap package symlink escapes source root: {package_root}") from exc

    python_path = os.environ.get("PYTHONPATH")
    if python_path != str(source_root):
        raise RuntimeError(
            f"PYTHONPATH must contain exactly the pinned source root: {source_root}"
        )

    contract = json.loads(_CONTRACT_PATH.read_text())
    if contract.get("contract_version") != "frame-oracle-v9-import-provenance-1":
        raise RuntimeError("unexpected import-provenance contract version")

    expected_modules = contract.get("modules")
    if not isinstance(expected_modules, dict) or not expected_modules:
        raise RuntimeError("import-provenance contract has no module registry")

    imported: dict[str, ModuleType] = {
        name: importlib.import_module(name) for name in expected_modules
    }
    resolved: dict[str, dict[str, str]] = {}
    for name, expected in expected_modules.items():
        module_path = _resolved_module_file(imported[name], package_root)
        expected_path = (source_root / expected["path"]).resolve(strict=True)
        if module_path != expected_path:
            raise RuntimeError(
                f"module {name!r} resolved to {module_path}, expected {expected_path}"
            )
        actual_hash = _sha256(module_path)
        if actual_hash != expected["sha256"]:
            raise RuntimeError(
                f"module {name!r} hash mismatch: {actual_hash} != {expected['sha256']}"
            )
        resolved[name] = {"path": str(module_path), "sha256": actual_hash}

    all_relaleap_modules: dict[str, str] = {}
    for name, module in sorted(sys.modules.items()):
        if name != "relaleap" and not name.startswith("relaleap."):
            continue
        if module is None or getattr(module, "__file__", None) is None:
            continue
        all_relaleap_modules[name] = str(_resolved_module_file(module, package_root))

    interpreter = Path(sys.executable).resolve(strict=True)
    record: dict[str, Any] = {
        "status": "verified",
        "contract_version": contract["contract_version"],
        "source_root": str(source_root),
        "package_root": str(package_root),
        "pythonpath": python_path,
        "interpreter": {
            "argv0": sys.executable,
            "realpath": str(interpreter),
            "version": sys.version,
        },
        "contract": {
            "path": str(_CONTRACT_PATH),
            "sha256": _sha256(_CONTRACT_PATH),
        },
        "attestor": {
            "path": str(Path(__file__).resolve()),
            "sha256": _sha256(Path(__file__).resolve()),
        },
        "modules": resolved,
        "all_imported_relaleap_modules": all_relaleap_modules,
    }

    output = Path(raw_output)
    if not output.is_absolute():
        raise RuntimeError(f"{_OUTPUT_ENV} must be an absolute path")
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".tmp")
    temporary.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    temporary.replace(output)
    return record


__all__ = ["attest_and_record"]

