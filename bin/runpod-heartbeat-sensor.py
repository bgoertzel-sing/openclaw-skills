#!/usr/bin/env python3
"""Conservative RunPod heartbeat sensor.

Provider ``uptimeSeconds`` is recorded as advisory telemetry only. Readiness is
established by SSH reachability; activity is established by GPU compute
processes, GPU utilization, or a high-CPU training process. Unreachability is
confirmed only after repeated observations spanning a minimum duration.

This tool never starts, stops, or deletes provider resources.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import tempfile
from typing import Any


REMOTE_PROBE = r"""
gpu_util=$(nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits 2>/dev/null | head -1 | tr -d ' ')
gpu_mem=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits 2>/dev/null | head -1 | tr -d ' ')
compute=$(nvidia-smi --query-compute-apps=pid,process_name --format=csv,noheader 2>/dev/null | sed '/^[[:space:]]*$/d' | wc -l)
cpu_active=$(ps -eo pcpu=,args= | awk '$1+0 >= 20 && $0 ~ /(python|torchrun|pipeline)/ {n++} END {print n+0}')
printf 'GPU_UTIL=%s\nGPU_MEM_MIB=%s\nCOMPUTE_PROCS=%s\nCPU_ACTIVE=%s\n' "${gpu_util:-0}" "${gpu_mem:-0}" "${compute:-0}" "${cpu_active:-0}"
""".strip()


@dataclass(frozen=True)
class SshEvidence:
    reachable: bool
    gpu_util: int = 0
    gpu_mem_mib: int = 0
    compute_processes: int = 0
    cpu_active_processes: int = 0
    error: str | None = None


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    normalized = value.strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        parsed = None
        for pattern in (
            "%Y-%m-%d %H:%M:%S.%f %z UTC",
            "%Y-%m-%d %H:%M:%S %z UTC",
        ):
            try:
                parsed = datetime.strptime(value.strip(), pattern)
                break
            except ValueError:
                continue
        if parsed is None:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def as_int(value: Any, default: int = 0) -> int:
    try:
        return int(float(str(value).strip()))
    except (TypeError, ValueError):
        return default


def parse_probe_output(output: str) -> SshEvidence:
    fields: dict[str, str] = {}
    for line in output.splitlines():
        key, separator, value = line.partition("=")
        if separator:
            fields[key.strip()] = value.strip()
    return SshEvidence(
        reachable=True,
        gpu_util=as_int(fields.get("GPU_UTIL")),
        gpu_mem_mib=as_int(fields.get("GPU_MEM_MIB")),
        compute_processes=as_int(fields.get("COMPUTE_PROCS")),
        cpu_active_processes=as_int(fields.get("CPU_ACTIVE")),
    )


def classify_work(api_status: str, evidence: SshEvidence) -> str:
    if api_status.upper() not in {"RUNNING", "RESTARTING"}:
        return "not_running"
    if not evidence.reachable:
        return "unreachable"
    if (
        evidence.compute_processes > 0
        or evidence.gpu_util >= 5
        or evidence.cpu_active_processes > 0
    ):
        return "ready_active"
    return "ready_idle"


def update_unreachable_state(
    previous: dict[str, Any] | None,
    work_state: str,
    now: datetime,
    min_observations: int = 3,
    min_seconds: int = 15 * 60,
) -> tuple[dict[str, Any], bool]:
    previous = previous or {}
    if work_state != "unreachable":
        return {
            "consecutive_unreachable": 0,
            "unreachable_since": None,
            "last_observed": now.isoformat(),
        }, False

    previous_count = as_int(previous.get("consecutive_unreachable"))
    previous_since = parse_time(previous.get("unreachable_since"))
    since = previous_since or now
    count = previous_count + 1
    confirmed = count >= min_observations and (now - since).total_seconds() >= min_seconds
    return {
        "consecutive_unreachable": count,
        "unreachable_since": since.isoformat(),
        "last_observed": now.isoformat(),
    }, confirmed


def estimated_cost(details: dict[str, Any], now: datetime) -> tuple[float | None, float | None]:
    created = parse_time(details.get("createdAt"))
    if created is None:
        return None, None
    elapsed_hours = max(0.0, (now - created).total_seconds() / 3600.0)
    try:
        hourly = float(details.get("costPerHr"))
    except (TypeError, ValueError):
        return elapsed_hours, None
    return elapsed_hours, elapsed_hours * hourly


def run_json(command: list[str], timeout: int = 25) -> Any:
    completed = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return json.loads(completed.stdout)


def probe_ssh(details: dict[str, Any], timeout: int = 12) -> SshEvidence:
    ssh = details.get("ssh") or {}
    key = (ssh.get("ssh_key") or {}).get("path")
    host = ssh.get("ip")
    port = ssh.get("port")
    if not key or not host or not port:
        return SshEvidence(reachable=False, error="SSH endpoint unavailable")
    command = [
        "ssh",
        "-o", "BatchMode=yes",
        "-o", f"ConnectTimeout={timeout}",
        "-o", "StrictHostKeyChecking=accept-new",
        "-i", str(key),
        "-p", str(port),
        f"root@{host}",
        REMOTE_PROBE,
    ]
    try:
        completed = subprocess.run(
            command,
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout + 5,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return SshEvidence(reachable=False, error=type(error).__name__)
    if completed.returncode != 0:
        message = completed.stderr.strip().splitlines()
        return SshEvidence(
            reachable=False,
            error=(message[-1][:240] if message else f"ssh exit {completed.returncode}"),
        )
    return parse_probe_output(completed.stdout)


def load_state(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def save_state(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(value, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, path)
    finally:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass


def inspect_pod(
    summary: dict[str, Any],
    details: dict[str, Any],
    evidence: SshEvidence,
    previous: dict[str, Any] | None,
    now: datetime,
) -> tuple[dict[str, Any], dict[str, Any]]:
    api_status = str(details.get("desiredStatus") or summary.get("desiredStatus") or "UNKNOWN")
    work_state = classify_work(api_status, evidence)
    next_state, unreachable_confirmed = update_unreachable_state(previous, work_state, now)
    elapsed_hours, cost = estimated_cost(details, now)
    result = {
        "id": details.get("id") or summary.get("id"),
        "name": details.get("name") or summary.get("name"),
        "api_status": api_status,
        "work_state": work_state,
        "ssh_reachable": evidence.reachable,
        "gpu_util_percent": evidence.gpu_util,
        "gpu_memory_mib": evidence.gpu_mem_mib,
        "gpu_compute_processes": evidence.compute_processes,
        "high_cpu_training_processes": evidence.cpu_active_processes,
        "provider_uptime_seconds_advisory": details.get("uptimeSeconds"),
        "elapsed_hours_from_created_at": round(elapsed_hours, 3) if elapsed_hours is not None else None,
        "estimated_compute_cost": round(cost, 2) if cost is not None else None,
        "consecutive_unreachable": next_state["consecutive_unreachable"],
        "unreachable_confirmed": unreachable_confirmed,
        "probe_error": evidence.error,
    }
    return result, next_state


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--state-file",
        type=Path,
        default=Path("/home/openclaw/research-agent/scratch/runpod-heartbeat-state.json"),
    )
    parser.add_argument("--no-write-state", action="store_true")
    parser.add_argument("--now", help="ISO-8601 test clock")
    args = parser.parse_args()

    now = parse_time(args.now) if args.now else datetime.now(timezone.utc)
    if now is None:
        parser.error("invalid --now timestamp")
    prior = load_state(args.state_file)
    next_state: dict[str, Any] = {}
    try:
        summaries = run_json(["runpodctl", "pod", "list", "--output", "json"])
    except (OSError, subprocess.SubprocessError, json.JSONDecodeError) as error:
        print(json.dumps({"sensor_error": type(error).__name__, "pods": []}, indent=2))
        return 2

    results = []
    for summary in summaries:
        pod_id = str(summary.get("id", ""))
        if not pod_id:
            continue
        try:
            details = run_json(["runpodctl", "pod", "get", pod_id, "--output", "json"])
            evidence = probe_ssh(details)
        except (OSError, subprocess.SubprocessError, json.JSONDecodeError) as error:
            details = summary
            evidence = SshEvidence(reachable=False, error=type(error).__name__)
        result, pod_state = inspect_pod(
            summary, details, evidence, prior.get(pod_id), now
        )
        results.append(result)
        next_state[pod_id] = pod_state

    if not args.no_write_state:
        save_state(args.state_file, next_state)
    payload = {
        "observed_at": now.isoformat(),
        "policy": {
            "uptime_seconds_is_advisory": True,
            "destructive_actions_allowed": False,
            "unreachable_confirmation": "3 observations spanning at least 15 minutes",
        },
        "pods": results,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
