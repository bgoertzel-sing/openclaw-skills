#!/usr/bin/env python3
"""Run one OmegaSim A6 condition and write an experiment ledger directory."""
from __future__ import annotations

import argparse
import json
import platform
import shlex
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

from analysis import analyze_result
from conditions import get_condition
from omegasim_a6 import ACTIONS, FIELD_DIMS, ROLES, SimConfig, run_simulation
from sweeps import SWEEP_GRID


def parse_gain(value: str | float, table: dict) -> float:
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(value)
    except ValueError:
        return float(table[value])


def git_info() -> dict:
    repo = Path(__file__).resolve().parents[2] / "repos" / "hyperseed-formalizations"
    info = {"repo": str(repo)}
    if repo.exists():
        for key, cmd in {
            "commit": ["git", "rev-parse", "HEAD"],
            "branch": ["git", "branch", "--show-current"],
            "status_short": ["git", "status", "--short"],
        }.items():
            try:
                info[key] = subprocess.check_output(cmd, cwd=repo, text=True).strip()
            except Exception as e:
                info[key] = f"unavailable: {e}"
    return info


def save_plots(result: dict, metrics: dict, outdir: Path) -> None:
    try:
        import matplotlib.pyplot as plt
    except Exception:
        return
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    axes[0].plot(result["fields"])
    axes[0].set_title("Semantic field A(t)")
    axes[0].legend(FIELD_DIMS, fontsize=6, ncol=2)
    axes[1].plot(result["artifacts"])
    axes[1].set_title("Artifact maturity / utility / queue health")
    axes[1].legend(["maturity", "utility", "queue_health"], fontsize=7)
    axes[2].plot(result["states"][:, :, 6].mean(axis=1), label="fatigue")
    axes[2].plot(result["states"][:, :, 7].mean(axis=1), label="threshold")
    axes[2].set_title("Mean fatigue and adaptive threshold")
    axes[2].legend()
    fig.tight_layout()
    fig.savefig(outdir / "timeseries.png", dpi=140)
    plt.close(fig)
    pca_path = outdir / "pca_scores.npy"
    if pca_path.exists():
        scores = np.load(pca_path)
        labels = np.load(outdir / "lobe_labels.npy")
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.scatter(scores[:, 0], scores[:, 1], c=labels, s=12, cmap="tab10")
        ax.set_title("Residual delay embedding PCA lobes")
        fig.tight_layout()
        fig.savefig(outdir / "pca_lobes.png", dpi=140)
        plt.close(fig)


def write_run_md(outdir: Path, args: argparse.Namespace, config: SimConfig, condition, metrics: dict, elapsed: float, command: str) -> None:
    md = f"""# OmegaSim A6 run

## Status

completed

## Question

Can a single-hive role-coupled motivational model produce bounded, structured residual dynamics under condition {condition.id} (`{condition.name}`)?

## Command

```bash
{command}
```

## Environment

- Python: `{sys.version.split()[0]}`
- Platform: `{platform.platform()}`
- NumPy: `{np.__version__}`
- Git: `{json.dumps(git_info(), indent=2)}`

## Configuration

```json
{json.dumps({"config": config.__dict__, "condition": condition.__dict__, "roles": ROLES, "actions": ACTIONS}, indent=2)}
```

## Results

```json
{json.dumps(metrics, indent=2, sort_keys=True)}
```

## Interpretation

This short run is a smoke/verification run, not evidence for a strange attractor.
It verifies bounded semantic fields, valid role actions, full latent-state output,
residual delay embedding, and preliminary lobe/recurrence metrics.

## Artifacts

- `result.npz`: raw arrays
- `metadata.json`: roles, fields, actions, condition, config
- `metrics.json`: analysis metrics
- `observable.npy`, `residuals.npy`, `embedding.npy`, `pca_scores.npy`, `lobe_labels.npy`
- `timeseries.png`, `pca_lobes.png` when matplotlib is available
- `stdout.log`, `stderr.log`, `command.sh`

## Timing

Wall time seconds: {elapsed:.3f}
"""
    (outdir / "RUN.md").write_text(md)


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--condition", type=int, default=5)
    p.add_argument("--timesteps", type=int, default=300)
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--outdir", type=Path, default=None)
    p.add_argument("--k", type=float, default=2.0)
    p.add_argument("--theta", type=float, default=50.0)
    p.add_argument("--tau", type=int, default=None)
    p.add_argument("--rho", type=float, default=None)
    p.add_argument("--fatigue-gain", default="medium")
    p.add_argument("--prediction-cost", default="medium")
    p.add_argument("--noise", type=float, default=0.03)
    args = p.parse_args(argv)

    fatigue_gain = parse_gain(args.fatigue_gain, SWEEP_GRID["fatigue_gain"])
    prediction_cost = parse_gain(args.prediction_cost, SWEEP_GRID["prediction_cost"])
    config = SimConfig(
        condition_id=args.condition, timesteps=args.timesteps, seed=args.seed,
        coupling_slope_k=args.k, threshold_percentile_theta=args.theta,
        delay_tau=args.tau, memory_rho=args.rho, fatigue_gain=fatigue_gain,
        prediction_cost=prediction_cost, noise=args.noise,
    )
    condition = get_condition(args.condition, delay_tau=args.tau, hysteresis_rho=args.rho)
    outdir = args.outdir or Path("runs") / f"condition-{args.condition}-seed-{args.seed}-{int(time.time())}"
    outdir.mkdir(parents=True, exist_ok=True)
    command = " ".join(shlex.quote(x) for x in [sys.executable, *sys.argv])
    (outdir / "command.sh").write_text("#!/usr/bin/env bash\nset -euo pipefail\n" + command + "\n")
    start = time.time()
    try:
        result = run_simulation(config)
        np.savez_compressed(outdir / "result.npz", **{k: v for k, v in result.items() if isinstance(v, np.ndarray)})
        (outdir / "metadata.json").write_text(json.dumps(result["metadata"], indent=2))
        metrics = analyze_result(result, outdir)
        save_plots(result, metrics, outdir)
        elapsed = time.time() - start
        write_run_md(outdir, args, config, condition, metrics, elapsed, command)
        (outdir / "stdout.log").write_text(f"completed condition={args.condition} outdir={outdir}\n")
        (outdir / "stderr.log").write_text("")
        print(json.dumps({"outdir": str(outdir), "metrics": metrics}, indent=2, sort_keys=True))
        return 0
    except Exception as e:
        (outdir / "stderr.log").write_text(repr(e) + "\n")
        raise


if __name__ == "__main__":
    raise SystemExit(main())
