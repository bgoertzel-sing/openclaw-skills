from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np

from bridgelearn import CurvatureFunnel, SharpnessPlant

from .common import first_crossing, rmse, write_csv, write_json


def _simulate_truth(seed: int = 123) -> dict[str, np.ndarray | float]:
    rng = np.random.default_rng(seed)
    steps = 420
    momentum = np.full(steps, 0.85, dtype=np.float64)
    step_size = np.empty(steps, dtype=np.float64)
    step_size[:120] = np.linspace(0.10, 0.30, 120)
    step_size[120:220] = 0.30 + 0.015 * np.sin(np.linspace(0.0, 4.0 * np.pi, 100))
    step_size[220:320] = np.linspace(0.30, 0.13, 100)
    step_size[320:] = np.linspace(0.13, 0.28, 100)
    progress_signal = 0.8 + 0.4 * np.sin(np.linspace(0.0, 5.0 * np.pi, steps)) ** 2

    gamma_p = 0.028
    gamma_r = 0.42
    safety_offset = 0.10
    process_sd = 0.012
    measurement_sd = 0.018

    curvature = np.empty(steps + 1, dtype=np.float64)
    observed = np.empty(steps + 1, dtype=np.float64)
    curvature[0] = 8.5
    observed[0] = curvature[0] + rng.normal(0.0, measurement_sd)
    for index in range(steps):
        threshold = 2.0 * (1.0 + momentum[index]) - safety_offset
        edge_excess = max(step_size[index] * curvature[index] - threshold, 0.0)
        curvature[index + 1] = max(
            curvature[index]
            + gamma_p * progress_signal[index]
            - gamma_r * edge_excess
            + rng.normal(0.0, process_sd),
            1e-8,
        )
        observed[index + 1] = curvature[index + 1] + rng.normal(0.0, measurement_sd)

    return {
        "step_size": step_size,
        "momentum": momentum,
        "progress_signal": progress_signal,
        "curvature": curvature,
        "observed": observed,
        "gamma_p": gamma_p,
        "gamma_r": gamma_r,
        "safety_offset": safety_offset,
        "process_sd": process_sd,
        "measurement_sd": measurement_sd,
    }


def _fit_plant(data: dict[str, Any]) -> dict[str, np.ndarray | SharpnessPlant]:
    step_size = np.asarray(data["step_size"])
    momentum = np.asarray(data["momentum"])
    progress = np.asarray(data["progress_signal"])
    observed = np.asarray(data["observed"])
    steps = step_size.size

    plant = SharpnessPlant(
        gamma_p=0.005,
        gamma_r=0.08,
        safety_offset=float(data["safety_offset"]),
        forgetting=0.995,
        initial_covariance=10.0,
        residual_quantile=0.90,
        residual_window=96,
        uncertainty_scale=0.50,
    )
    funnel = CurvatureFunnel(
        lower=[max(observed[0] - 0.05, 1e-8)],
        center=[max(observed[0], 1e-8)],
        upper=[observed[0] + 0.05],
        confidence=[0.10],
        model_name="initial",
    )

    predicted = np.empty(steps)
    lower = np.empty(steps)
    upper = np.empty(steps)
    confidence = np.empty(steps)
    parameter_history = np.empty((steps, 2))
    for index in range(steps):
        forecast = plant.predict_step(
            funnel,
            step_size=[step_size[index]],
            momentum=[momentum[index]],
            progress_signal=[progress[index]],
        )
        predicted[index] = forecast.center[0]
        lower[index] = forecast.lower[0]
        upper[index] = forecast.upper[0]
        confidence[index] = forecast.confidence[0]
        funnel = plant.update(
            previous_curvature=[max(observed[index], 1e-8)],
            current_curvature=[max(observed[index + 1], 1e-8)],
            step_size=[step_size[index]],
            momentum=[momentum[index]],
            progress_signal=[progress[index]],
        )
        parameter_history[index] = plant.parameters[0]

    return {
        "plant": plant,
        "predicted": predicted,
        "lower": lower,
        "upper": upper,
        "confidence": confidence,
        "parameter_history": parameter_history,
    }


def _rolling_static_prediction(data: dict[str, Any], window: int = 40) -> np.ndarray:
    """Fit a static h(eta) curve on a rolling window, deliberately omitting state."""
    step_size = np.asarray(data["step_size"])
    observed = np.asarray(data["observed"])
    result = np.empty(step_size.size)
    for index in range(step_size.size):
        if index < window:
            result[index] = observed[index]
            continue
        design = np.column_stack(
            [np.ones(window), step_size[index - window : index]]
        )
        response = observed[index - window + 1 : index + 1]
        coefficients, *_ = np.linalg.lstsq(design, response, rcond=None)
        result[index] = coefficients[0] + coefficients[1] * step_size[index]
    return result


def _counterfactual_rollout(data: dict[str, Any], start: int = 150) -> dict[str, Any]:
    step_size = np.asarray(data["step_size"])
    momentum = np.asarray(data["momentum"])
    progress = np.asarray(data["progress_signal"])
    observed = np.asarray(data["observed"])
    true_curvature = np.asarray(data["curvature"])
    safety_offset = float(data["safety_offset"])

    plant = SharpnessPlant(
        gamma_p=0.005,
        gamma_r=0.08,
        safety_offset=safety_offset,
        forgetting=0.995,
        initial_covariance=10.0,
        residual_quantile=0.90,
        residual_window=96,
        uncertainty_scale=0.50,
    )
    funnel = CurvatureFunnel(
        lower=[max(observed[0] - 0.05, 1e-8)],
        center=[max(observed[0], 1e-8)],
        upper=[observed[0] + 0.05],
        confidence=[0.10],
    )
    for index in range(start):
        funnel = plant.update(
            previous_curvature=[max(observed[index], 1e-8)],
            current_curvature=[max(observed[index + 1], 1e-8)],
            step_size=[step_size[index]],
            momentum=[momentum[index]],
            progress_signal=[progress[index]],
        )

    horizon = 60
    candidate_step = 0.29
    candidate_momentum = 0.85
    candidate_progress = 1.0
    rollout = plant.rollout(
        funnel,
        step_sizes=np.full(horizon, candidate_step),
        momenta=np.full(horizon, candidate_momentum),
        progress_signals=np.full(horizon, candidate_progress),
    )
    center = np.asarray([item.center[0] for item in rollout[:-1]])
    lower = np.asarray([item.lower[0] for item in rollout[:-1]])
    upper = np.asarray([item.upper[0] for item in rollout[:-1]])
    threshold = 2.0 * (1.0 + candidate_momentum) - safety_offset
    center_utilization = candidate_step * center / threshold
    upper_utilization = candidate_step * upper / threshold

    true_path = np.empty(horizon)
    current = float(true_curvature[start])
    for index in range(horizon):
        true_path[index] = current
        edge_excess = max(candidate_step * current - threshold, 0.0)
        current = max(
            current
            + float(data["gamma_p"]) * candidate_progress
            - float(data["gamma_r"]) * edge_excess,
            1e-8,
        )
    true_utilization = candidate_step * true_path / threshold
    frozen_utilization = candidate_step * true_curvature[start] / threshold

    return {
        "start_step": start,
        "horizon": horizon,
        "candidate_step_size": candidate_step,
        "candidate_momentum": candidate_momentum,
        "threshold": threshold,
        "center": center,
        "lower": lower,
        "upper": upper,
        "true_path": true_path,
        "center_utilization": center_utilization,
        "upper_utilization": upper_utilization,
        "true_utilization": true_utilization,
        "frozen_utilization": frozen_utilization,
        "point_crossing": first_crossing(center_utilization),
        "upper_crossing": first_crossing(upper_utilization),
        "true_crossing": first_crossing(true_utilization),
        "estimated_parameters": plant.parameters[0].copy(),
        "initial_funnel_relative_width": float(funnel.relative_width[0]),
        "maximum_rollout_relative_width": float(
            max(item.relative_width[0] for item in rollout)
        ),
    }


def run(output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    data = _simulate_truth()
    fit = _fit_plant(data)
    static_prediction = _rolling_static_prediction(data)
    counterfactual = _counterfactual_rollout(data)

    curvature = np.asarray(data["curvature"])[1:]
    observed = np.asarray(data["observed"])[1:]
    predicted = np.asarray(fit["predicted"])
    lower = np.asarray(fit["lower"])
    upper = np.asarray(fit["upper"])
    parameters = np.asarray(fit["parameter_history"])
    burn = 60

    coverage = float(np.mean((curvature[burn:] >= lower[burn:]) & (curvature[burn:] <= upper[burn:])))
    plant_rmse = rmse(predicted[burn:], curvature[burn:])
    measurement_rmse = rmse(predicted[burn:], observed[burn:])
    static_rmse = rmse(static_prediction[burn:], curvature[burn:])
    final_parameters = parameters[-1]
    true_parameters = np.asarray([data["gamma_p"], data["gamma_r"]], dtype=np.float64)
    relative_parameter_error = (final_parameters - true_parameters) / true_parameters

    step_index = np.arange(np.asarray(data["step_size"]).size)
    threshold = 2.0 * (1.0 + np.asarray(data["momentum"])) - float(data["safety_offset"])
    true_utilization = np.asarray(data["step_size"]) * np.asarray(data["curvature"])[:-1] / threshold
    predicted_utilization = np.asarray(data["step_size"]) * predicted / threshold
    upper_utilization = np.asarray(data["step_size"]) * upper / threshold

    plt.figure(figsize=(10, 5.8))
    plt.plot(step_index, curvature, label="true next sharpness")
    plt.plot(step_index, predicted, label="SharpnessPlant one-step prediction")
    plt.plot(step_index, static_prediction, label="rolling static h(eta) model")
    plt.fill_between(step_index, lower, upper, alpha=0.2, label="predicted funnel")
    plt.xlabel("update")
    plt.ylabel("sharpness h")
    plt.title("Dynamic sharpness identification")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "dynamic_sharpness_tracking.png", dpi=180)
    plt.close()

    plt.figure(figsize=(10, 5.4))
    plt.plot(step_index, true_utilization, label="true edge utilization")
    plt.plot(step_index, predicted_utilization, label="predicted center utilization")
    plt.plot(step_index, upper_utilization, label="upper-funnel utilization")
    plt.axhline(1.0, linestyle="--", label="momentum stability edge")
    plt.xlabel("update")
    plt.ylabel("eta h / [2(1+mu)-delta]")
    plt.title("Edge-of-stability utilization")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "dynamic_sharpness_edge_utilization.png", dpi=180)
    plt.close()

    plt.figure(figsize=(10, 5.4))
    plt.plot(step_index, parameters[:, 0], label="estimated gamma_p")
    plt.plot(step_index, parameters[:, 1], label="estimated gamma_r")
    plt.axhline(float(data["gamma_p"]), linestyle="--", label="true gamma_p")
    plt.axhline(float(data["gamma_r"]), linestyle=":", label="true gamma_r")
    plt.xlabel("update")
    plt.ylabel("identified rate")
    plt.title("Sharpness-plant parameter identification")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "dynamic_sharpness_parameters.png", dpi=180)
    plt.close()

    rollout_index = np.arange(counterfactual["horizon"])
    plt.figure(figsize=(10, 5.4))
    plt.plot(rollout_index, counterfactual["true_path"], label="true counterfactual sharpness")
    plt.plot(rollout_index, counterfactual["center"], label="plant point forecast")
    plt.fill_between(
        rollout_index,
        counterfactual["lower"],
        counterfactual["upper"],
        alpha=0.2,
        label="plant funnel",
    )
    plt.axhline(
        counterfactual["threshold"] / counterfactual["candidate_step_size"],
        linestyle="--",
        label="edge sharpness for candidate command",
    )
    plt.xlabel("future update")
    plt.ylabel("sharpness h")
    plt.title("Counterfactual high-step rollout")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "dynamic_sharpness_counterfactual.png", dpi=180)
    plt.close()

    rows = []
    for index in range(step_index.size):
        rows.append(
            {
                "step": index,
                "step_size": np.asarray(data["step_size"])[index],
                "momentum": np.asarray(data["momentum"])[index],
                "progress_signal": np.asarray(data["progress_signal"])[index],
                "true_curvature": curvature[index],
                "observed_curvature": observed[index],
                "plant_prediction": predicted[index],
                "funnel_lower": lower[index],
                "funnel_upper": upper[index],
                "static_prediction": static_prediction[index],
                "gamma_p_estimate": parameters[index, 0],
                "gamma_r_estimate": parameters[index, 1],
                "true_edge_utilization": true_utilization[index],
                "predicted_edge_utilization": predicted_utilization[index],
                "upper_edge_utilization": upper_utilization[index],
            }
        )
    write_csv(
        output_dir / "dynamic_sharpness_trace.csv",
        rows,
        list(rows[0]),
    )

    counter_rows = []
    for index in range(counterfactual["horizon"]):
        counter_rows.append(
            {
                "future_step": index,
                "true_curvature": counterfactual["true_path"][index],
                "predicted_center": counterfactual["center"][index],
                "predicted_lower": counterfactual["lower"][index],
                "predicted_upper": counterfactual["upper"][index],
                "true_edge_utilization": counterfactual["true_utilization"][index],
                "center_edge_utilization": counterfactual["center_utilization"][index],
                "upper_edge_utilization": counterfactual["upper_utilization"][index],
            }
        )
    write_csv(
        output_dir / "dynamic_sharpness_counterfactual.csv",
        counter_rows,
        list(counter_rows[0]),
    )

    summary = {
        "experiment": "dynamic_sharpness",
        "seed": 123,
        "steps": int(step_index.size),
        "burn_in_for_metrics": burn,
        "true_gamma_p": float(data["gamma_p"]),
        "true_gamma_r": float(data["gamma_r"]),
        "estimated_gamma_p": float(final_parameters[0]),
        "estimated_gamma_r": float(final_parameters[1]),
        "relative_error_gamma_p": float(relative_parameter_error[0]),
        "relative_error_gamma_r": float(relative_parameter_error[1]),
        "plant_one_step_rmse_against_true": plant_rmse,
        "plant_one_step_rmse_against_measurement": measurement_rmse,
        "rolling_static_model_rmse": static_rmse,
        "rmse_improvement_over_static": static_rmse / plant_rmse,
        "funnel_coverage_against_true": coverage,
        "median_funnel_width": float(np.median(upper[burn:] - lower[burn:])),
        "maximum_true_edge_utilization": float(np.max(true_utilization)),
        "counterfactual": {
            "start_step": counterfactual["start_step"],
            "candidate_step_size": counterfactual["candidate_step_size"],
            "candidate_momentum": counterfactual["candidate_momentum"],
            "frozen_edge_utilization": counterfactual["frozen_utilization"],
            "true_edge_crossing_future_step": counterfactual["true_crossing"],
            "point_forecast_edge_crossing_future_step": counterfactual["point_crossing"],
            "upper_funnel_edge_crossing_future_step": counterfactual["upper_crossing"],
            "initial_funnel_relative_width": counterfactual["initial_funnel_relative_width"],
            "maximum_rollout_relative_width": counterfactual["maximum_rollout_relative_width"],
        },
        "artifacts": {
            "tracking_plot": "dynamic_sharpness_tracking.png",
            "edge_plot": "dynamic_sharpness_edge_utilization.png",
            "parameter_plot": "dynamic_sharpness_parameters.png",
            "counterfactual_plot": "dynamic_sharpness_counterfactual.png",
            "trace_csv": "dynamic_sharpness_trace.csv",
            "counterfactual_csv": "dynamic_sharpness_counterfactual.csv",
        },
    }
    write_json(output_dir / "summary.json", summary)
    return summary
