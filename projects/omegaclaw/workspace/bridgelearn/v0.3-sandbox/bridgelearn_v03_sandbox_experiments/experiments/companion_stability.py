from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np

from bridgelearn import (
    companion_matrix,
    companion_roots,
    companion_small_gain_bound,
    covariance_norm,
    damping_regime,
    inside_stability_triangle,
    jury_margins,
    lyapunov_metric,
    spectral_radius,
)

from .common import write_csv, write_json


def _case_metrics(name: str, c1: float, c2: float, horizon: int = 100) -> dict[str, Any]:
    matrix = companion_matrix(c1, c2)
    rho = spectral_radius(c1, c2)
    metric, rho_bar, condition = lyapunov_metric(c1, c2)
    powers = []
    current = np.eye(2)
    for _ in range(horizon + 1):
        powers.append(float(np.linalg.norm(current, ord=2)))
        current = matrix @ current
    powers_array = np.asarray(powers)
    peak_index = int(np.argmax(powers_array))
    small_gain = companion_small_gain_bound(
        c1,
        c2,
        disturbance_lipschitz=0.02,
        disturbance_bound=1e-4,
    )
    roots = companion_roots(c1, c2)
    return {
        "name": name,
        "c1": c1,
        "c2": c2,
        "root_1_real": float(np.real(roots[0])),
        "root_1_imag": float(np.imag(roots[0])),
        "root_2_real": float(np.real(roots[1])),
        "root_2_imag": float(np.imag(roots[1])),
        "spectral_radius": rho,
        "regime": damping_regime(c1, c2),
        "jury_margin_1": jury_margins(c1, c2)[0],
        "jury_margin_2": jury_margins(c1, c2)[1],
        "jury_margin_3": jury_margins(c1, c2)[2],
        "rho_bar": rho_bar,
        "lyapunov_condition": condition,
        "max_state_amplification": float(np.max(powers_array)),
        "max_covariance_amplification": float(np.max(powers_array) ** 2),
        "peak_amplification_step": peak_index,
        "small_gain_condition_satisfied": small_gain.condition_satisfied,
        "small_gain_asymptotic_bound": small_gain.asymptotic_bound,
        "recommended_matrix_slew": small_gain.recommended_matrix_slew,
        "powers": powers_array,
        "metric": metric,
    }


def run(output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    cases = {
        "near_repeated_root": (1.8, -0.81),
        "underdamped_same_radius": (0.4, -0.81),
        "separated_overdamped": (1.2, -0.27),
        "fast_underdamped": (0.5, -0.10),
    }
    metrics = {
        name: _case_metrics(name, c1, c2) for name, (c1, c2) in cases.items()
    }

    horizon = 60
    plt.figure(figsize=(10, 5.7))
    for name, item in metrics.items():
        powers = np.asarray(item["powers"])
        plt.plot(
            np.arange(horizon + 1),
            powers[: horizon + 1] ** 2,
            label=name,
        )
    plt.yscale("log")
    plt.xlabel("power k")
    plt.ylabel("worst Frobenius covariance amplification ||A^k||_2^2")
    plt.title("Schur stability does not rule out transient covariance growth")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "companion_transient_amplification.png", dpi=180)
    plt.close()

    repeated = metrics["near_repeated_root"]
    matrix = companion_matrix(repeated["c1"], repeated["c2"])
    peak = int(repeated["peak_amplification_step"])
    _, _, right_vectors = np.linalg.svd(np.linalg.matrix_power(matrix, peak))
    direction = right_vectors[0]
    initial_error = np.outer(direction, direction)
    metric = np.asarray(repeated["metric"])
    euclidean = []
    lyapunov = []
    bound = []
    euclidean_zero = np.linalg.norm(initial_error, ord="fro")
    lyapunov_zero = covariance_norm(initial_error, metric)
    for index in range(horizon + 1):
        power = np.linalg.matrix_power(matrix, index)
        error = power @ initial_error @ power.T
        euclidean.append(float(np.linalg.norm(error, ord="fro") / euclidean_zero))
        lyapunov.append(float(covariance_norm(error, metric) / lyapunov_zero))
        bound.append(float(repeated["rho_bar"] ** (2 * index)))
    euclidean = np.asarray(euclidean)
    lyapunov = np.asarray(lyapunov)
    bound = np.asarray(bound)

    plt.figure(figsize=(10, 5.7))
    plt.plot(np.arange(horizon + 1), euclidean, label="Euclidean covariance norm")
    plt.plot(np.arange(horizon + 1), lyapunov, label="Lyapunov-adapted norm")
    plt.plot(np.arange(horizon + 1), bound, linestyle="--", label="rho_bar^(2k) bound")
    plt.yscale("log")
    plt.xlabel("power k")
    plt.ylabel("norm relative to k=0")
    plt.title("Near-repeated roots: transient growth versus adapted contraction")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "companion_lyapunov_norm_comparison.png", dpi=180)
    plt.close()

    c1_values = np.linspace(-1.95, 1.95, 121)
    c2_values = np.linspace(-0.98, 0.95, 121)
    grid_rows = []
    scatter_c1 = []
    scatter_c2 = []
    scatter_log_condition = []
    for c2 in c2_values:
        for c1 in c1_values:
            if not inside_stability_triangle(c1, c2, margin=1e-5):
                continue
            rho = spectral_radius(c1, c2)
            if rho >= 0.995:
                continue
            try:
                _, rho_bar, condition = lyapunov_metric(c1, c2)
            except ValueError:
                continue
            scatter_c1.append(c1)
            scatter_c2.append(c2)
            scatter_log_condition.append(np.log10(condition))
            grid_rows.append(
                {
                    "c1": c1,
                    "c2": c2,
                    "spectral_radius": rho,
                    "rho_bar": rho_bar,
                    "lyapunov_condition": condition,
                    "log10_lyapunov_condition": np.log10(condition),
                    "damping_regime": damping_regime(c1, c2),
                }
            )

    plt.figure(figsize=(9.5, 7.0))
    points = plt.scatter(
        scatter_c1,
        scatter_c2,
        c=scatter_log_condition,
        s=10,
    )
    plt.colorbar(points, label="log10 cond(P)")
    curve_c1 = np.linspace(-1.9, 1.9, 400)
    curve_c2 = -0.25 * curve_c1**2
    valid = (curve_c2 > -1.0) & (curve_c2 < 1.0)
    plt.plot(curve_c1[valid], curve_c2[valid], linestyle="--", label="critical-damping boundary")
    annotation_positions = {
        "near_repeated_root": (1.25, -0.76),
        "underdamped_same_radius": (0.05, -0.77),
        "separated_overdamped": (0.78, -0.22),
        "fast_underdamped": (0.53, -0.04),
    }
    for name, (c1, c2) in cases.items():
        plt.scatter([c1], [c2], marker="x", s=70)
        text_x, text_y = annotation_positions[name]
        plt.text(text_x, text_y, name, fontsize=8)
    plt.xlim(-2.1, 2.2)
    plt.xlabel("c1")
    plt.ylabel("c2")
    plt.title("Lyapunov conditioning inside the AR(2) stability triangle")
    plt.legend(loc="lower left")
    plt.tight_layout()
    plt.savefig(output_dir / "companion_stability_triangle_conditioning.png", dpi=180)
    plt.close()

    case_rows = []
    for item in metrics.values():
        case_rows.append(
            {
                key: value
                for key, value in item.items()
                if key not in {"powers", "metric"}
            }
        )
    write_csv(output_dir / "companion_cases.csv", case_rows, list(case_rows[0]))
    write_csv(
        output_dir / "companion_stability_grid.csv",
        grid_rows,
        list(grid_rows[0]),
    )

    repeated_peak = int(repeated["peak_amplification_step"])
    summary = {
        "experiment": "companion_stability",
        "cases": {
            name: {
                key: value
                for key, value in item.items()
                if key not in {"powers", "metric"}
            }
            for name, item in metrics.items()
        },
        "repeated_root_norm_check": {
            "peak_step": repeated_peak,
            "euclidean_covariance_amplification_at_peak": float(euclidean[repeated_peak]),
            "lyapunov_norm_ratio_at_peak": float(lyapunov[repeated_peak]),
            "rho_bar_bound_at_peak": float(bound[repeated_peak]),
            "maximum_bound_violation": float(np.max(lyapunov - bound)),
        },
        "comparison": {
            "condition_ratio_repeated_vs_underdamped": repeated["lyapunov_condition"]
            / metrics["underdamped_same_radius"]["lyapunov_condition"],
            "covariance_amplification_ratio_repeated_vs_underdamped": repeated[
                "max_covariance_amplification"
            ]
            / metrics["underdamped_same_radius"]["max_covariance_amplification"],
            "small_gain_bound_ratio_repeated_vs_underdamped": repeated[
                "small_gain_asymptotic_bound"
            ]
            / metrics["underdamped_same_radius"]["small_gain_asymptotic_bound"],
        },
        "grid_points": len(grid_rows),
        "artifacts": {
            "transient_plot": "companion_transient_amplification.png",
            "lyapunov_plot": "companion_lyapunov_norm_comparison.png",
            "triangle_plot": "companion_stability_triangle_conditioning.png",
            "case_csv": "companion_cases.csv",
            "grid_csv": "companion_stability_grid.csv",
        },
    }
    write_json(output_dir / "summary.json", summary)
    return summary
