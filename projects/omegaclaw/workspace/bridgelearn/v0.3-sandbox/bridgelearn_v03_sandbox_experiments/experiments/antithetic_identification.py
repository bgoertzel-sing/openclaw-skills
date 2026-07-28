from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np

from bridgelearn import (
    AntitheticProbePolicy,
    ChannelObservation,
    ChannelState,
    ForgettingFactorAR2Observer,
    GaussianState,
    GaussianTransition,
)

from .common import rmse, write_csv, write_json


def _stationary_state_gain(c1: float, c2: float) -> float:
    matrix = np.asarray([[c1, c2], [1.0, 0.0]], dtype=np.float64)
    innovation = np.asarray([[1.0, 0.0], [0.0, 0.0]], dtype=np.float64)
    covariance = np.linalg.solve(
        np.eye(4) - np.kron(matrix, matrix), innovation.reshape(-1)
    ).reshape(2, 2)
    return float(covariance[0, 0])


def _antithetic_sequence(
    length: int,
    *,
    c1: float,
    c2: float,
    realized_width_per_pulse: float,
) -> np.ndarray:
    policy = AntitheticProbePolicy(
        contrast_se_threshold=0.01,
        condition_threshold=2.0,
        confidence_threshold=0.90,
        cold_variance=1.0,
        max_realized_variance=realized_width_per_pulse,
        max_total_realized_variance=1e30,
        amplitude_levels=(1.0,),
    )
    observation = ChannelObservation(
        state=GaussianState([0.0], confidence=[0.0]),
        reference=GaussianTransition([0.0], [0.0]),
        metadata={
            "contrast_standard_error": [1.0],
            "regressor_condition": [1e9],
            "lyapunov_condition": [1.0],
            "c1": [c1],
            "c2": [c2],
        },
    )
    state = ChannelState()
    desired = GaussianTransition([0.0], [0.0])
    result = np.empty(length)
    for index in range(length):
        decision = policy.apply(
            desired=desired,
            observation=observation,
            state=state,
        )
        result[index] = decision.signal[0]
        policy.commit()
    return result


def _simulate_trials(
    *,
    mode: str,
    rng: np.random.Generator,
    trials: int,
    estimation_steps: int,
    burn_steps: int,
    c1: float,
    c2: float,
    process_sd: float,
    white_probe_variance: float,
    antithetic_signal: np.ndarray,
) -> dict[str, np.ndarray]:
    total = estimation_steps + burn_steps
    state = np.zeros((trials, total + 2), dtype=np.float64)
    if mode == "none":
        probe = np.zeros((trials, total + 1), dtype=np.float64)
    elif mode == "white":
        probe = rng.normal(
            0.0, np.sqrt(white_probe_variance), size=(trials, total + 1)
        )
    elif mode == "antithetic":
        signs = rng.choice(np.asarray([-1.0, 1.0]), size=trials)
        probe = signs[:, None] * antithetic_signal[None, : total + 1]
    else:  # pragma: no cover - guarded by caller
        raise ValueError(f"unknown mode: {mode}")
    process_noise = rng.normal(0.0, process_sd, size=(trials, total + 1))
    for index in range(1, total + 1):
        state[:, index + 1] = (
            c1 * state[:, index]
            + c2 * state[:, index - 1]
            + probe[:, index]
            + process_noise[:, index]
        )

    start = burn_steps + 1
    response = state[:, start + 1 : total + 2] - probe[:, start : total + 1]
    z1 = state[:, start : total + 1]
    z2 = state[:, start - 1 : total]

    s11 = np.sum(z1 * z1, axis=1)
    s22 = np.sum(z2 * z2, axis=1)
    s12 = np.sum(z1 * z2, axis=1)
    t1 = np.sum(z1 * response, axis=1)
    t2 = np.sum(z2 * response, axis=1)
    determinant = np.maximum(s11 * s22 - s12 * s12, 1e-30)
    c1_hat = (s22 * t1 - s12 * t2) / determinant
    c2_hat = (s11 * t2 - s12 * t1) / determinant

    trace = (s11 + s22) / estimation_steps
    discriminant = np.sqrt(
        np.maximum(((s11 - s22) / estimation_steps) ** 2 + 4.0 * (s12 / estimation_steps) ** 2, 0.0)
    )
    eigen_max = 0.5 * (trace + discriminant)
    eigen_min = np.maximum(0.5 * (trace - discriminant), 1e-30)
    condition = eigen_max / eigen_min
    state_variance = np.var(z1, axis=1)

    return {
        "c1": c1_hat,
        "c2": c2_hat,
        "contrast": c1_hat - c2_hat,
        "condition": condition,
        "smallest_eigenvalue": eigen_min,
        "state_variance": state_variance,
    }


def _online_rls_trace(
    *,
    mode: str,
    seed: int,
    replicates: int,
    steps: int,
    c1: float,
    c2: float,
    process_sd: float,
    white_probe_variance: float,
    antithetic_signal: np.ndarray,
) -> dict[str, np.ndarray]:
    rng = np.random.default_rng(seed)
    state_previous_previous = np.zeros(replicates)
    state_previous = np.zeros(replicates)
    observer = ForgettingFactorAR2Observer(
        blocks=1,
        forgetting=0.99,
        initial_covariance=1e3,
        slew_fraction=0.25,
    )
    contrast = np.empty(steps)
    contrast_se = np.empty(steps)
    c1_estimate = np.empty(steps)
    c2_estimate = np.empty(steps)
    for index in range(steps):
        if mode == "none":
            probe = np.zeros(replicates)
        elif mode == "white":
            probe = rng.normal(0.0, np.sqrt(white_probe_variance), size=replicates)
        else:
            pair_signal = antithetic_signal[index]
            random_pair_sign = 1.0 if (index // 2) % 2 == 0 else -1.0
            probe = np.full(replicates, random_pair_sign * pair_signal)
        current = (
            c1 * state_previous
            + c2 * state_previous_previous
            + probe
            + rng.normal(0.0, process_sd, size=replicates)
        )
        # The probe is a known command, so subtract it from the response before
        # fitting the autonomous AR(2) coefficients.
        estimate = observer.update(
            state_previous_previous[None, :],
            state_previous[None, :],
            (current - probe)[None, :],
        )
        c1_estimate[index] = estimate.c1[0]
        c2_estimate[index] = estimate.c2[0]
        contrast[index] = estimate.c1[0] - estimate.c2[0]
        contrast_se[index] = estimate.contrast_standard_error[0]
        state_previous_previous, state_previous = state_previous, current
    return {
        "c1": c1_estimate,
        "c2": c2_estimate,
        "contrast": contrast,
        "contrast_se": contrast_se,
    }


def run(output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    c1 = 1.8
    c2 = -0.81
    true_contrast = c1 - c2
    process_sd = 0.004
    trials = 1_000
    estimation_steps = 240
    burn_steps = 80
    realized_width = 0.01
    state_gain = _stationary_state_gain(c1, c2)
    white_probe_variance = realized_width / state_gain
    transfer_denominator = abs(1.0 + c1 - c2) ** 2
    antithetic_raw_variance = realized_width * transfer_denominator
    antithetic_signal = _antithetic_sequence(
        estimation_steps + burn_steps + 1,
        c1=c1,
        c2=c2,
        realized_width_per_pulse=realized_width,
    )

    rng = np.random.default_rng(1_234)
    results: dict[str, dict[str, np.ndarray]] = {}
    modes = ("none", "white", "antithetic")
    for mode in modes:
        results[mode] = _simulate_trials(
            mode=mode,
            rng=rng,
            trials=trials,
            estimation_steps=estimation_steps,
            burn_steps=burn_steps,
            c1=c1,
            c2=c2,
            process_sd=process_sd,
            white_probe_variance=white_probe_variance,
            antithetic_signal=antithetic_signal,
        )

    mode_summaries: dict[str, dict[str, float]] = {}
    baseline_state_variance = float(np.mean(results["none"]["state_variance"]))
    for mode in modes:
        values = results[mode]
        contrast_rmse = rmse(values["contrast"], np.full(trials, true_contrast))
        mode_summaries[mode] = {
            "c1_mean": float(np.mean(values["c1"])),
            "c2_mean": float(np.mean(values["c2"])),
            "contrast_mean": float(np.mean(values["contrast"])),
            "contrast_rmse": contrast_rmse,
            "c1_rmse": rmse(values["c1"], np.full(trials, c1)),
            "c2_rmse": rmse(values["c2"], np.full(trials, c2)),
            "median_regressor_condition": float(np.median(values["condition"])),
            "median_smallest_eigenvalue": float(
                np.median(values["smallest_eigenvalue"])
            ),
            "mean_state_variance": float(np.mean(values["state_variance"])),
            "added_state_variance": float(
                np.mean(values["state_variance"]) - baseline_state_variance
            ),
        }

    online = {
        mode: _online_rls_trace(
            mode=mode,
            seed=7_000 + index,
            replicates=128,
            steps=220,
            c1=c1,
            c2=c2,
            process_sd=process_sd,
            white_probe_variance=white_probe_variance,
            antithetic_signal=_antithetic_sequence(
                220,
                c1=c1,
                c2=c2,
                realized_width_per_pulse=realized_width,
            ),
        )
        for index, mode in enumerate(modes)
    }

    plt.figure(figsize=(9.5, 5.4))
    errors = [results[mode]["contrast"] - true_contrast for mode in modes]
    plt.boxplot(errors, tick_labels=["none", "white", "antithetic"], showfliers=False)
    plt.axhline(0.0, linestyle="--")
    plt.ylabel("estimated (c1-c2) minus truth")
    plt.title("Weak-direction identification error")
    plt.tight_layout()
    plt.savefig(output_dir / "antithetic_contrast_error.png", dpi=180)
    plt.close()

    plt.figure(figsize=(9.5, 5.4))
    for mode in modes:
        plt.plot(online[mode]["contrast_se"], label=mode)
    plt.yscale("log")
    plt.xlabel("online RLS update")
    plt.ylabel("reported standard error of c1-c2")
    plt.title("Online order-2 identification uncertainty")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "antithetic_online_standard_error.png", dpi=180)
    plt.close()

    plt.figure(figsize=(9.5, 5.4))
    x = np.arange(len(modes))
    smallest = [mode_summaries[mode]["median_smallest_eigenvalue"] for mode in modes]
    plt.bar(x, smallest)
    plt.xticks(x, modes)
    plt.yscale("log")
    plt.ylabel("median smallest eigenvalue of regressor moment")
    plt.title("Temporal excitation repairs the starved AR(2) direction")
    plt.tight_layout()
    plt.savefig(output_dir / "antithetic_regressor_information.png", dpi=180)
    plt.close()

    plt.figure(figsize=(9.5, 5.4))
    shown = 32
    plt.plot(np.arange(shown), antithetic_signal[:shown], marker="o", label="antithetic signal")
    white_example = np.random.default_rng(99).normal(
        0.0, np.sqrt(white_probe_variance), size=shown
    )
    plt.plot(np.arange(shown), white_example, marker=".", label="equal-width white signal")
    plt.xlabel("probe update")
    plt.ylabel("known additive probe")
    plt.title("Probe temporal structure")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / "antithetic_probe_signals.png", dpi=180)
    plt.close()

    distribution_rows = []
    for mode in modes:
        for trial in range(trials):
            distribution_rows.append(
                {
                    "mode": mode,
                    "trial": trial,
                    "c1_estimate": results[mode]["c1"][trial],
                    "c2_estimate": results[mode]["c2"][trial],
                    "contrast_estimate": results[mode]["contrast"][trial],
                    "regressor_condition": results[mode]["condition"][trial],
                    "smallest_eigenvalue": results[mode]["smallest_eigenvalue"][trial],
                    "state_variance": results[mode]["state_variance"][trial],
                }
            )
    write_csv(
        output_dir / "antithetic_trial_results.csv",
        distribution_rows,
        list(distribution_rows[0]),
    )

    online_rows = []
    for mode in modes:
        for index in range(online[mode]["contrast"].size):
            online_rows.append(
                {
                    "mode": mode,
                    "step": index,
                    "c1_estimate": online[mode]["c1"][index],
                    "c2_estimate": online[mode]["c2"][index],
                    "contrast_estimate": online[mode]["contrast"][index],
                    "contrast_standard_error": online[mode]["contrast_se"][index],
                }
            )
    write_csv(
        output_dir / "antithetic_online_rls.csv",
        online_rows,
        list(online_rows[0]),
    )

    summary = {
        "experiment": "antithetic_identification",
        "seed": 1234,
        "trials": trials,
        "estimation_steps": estimation_steps,
        "burn_steps": burn_steps,
        "true_c1": c1,
        "true_c2": c2,
        "true_contrast_c1_minus_c2": true_contrast,
        "process_noise_sd": process_sd,
        "equal_realized_probe_width": realized_width,
        "unit_white_state_variance_gain": state_gain,
        "white_probe_raw_variance": white_probe_variance,
        "antithetic_transfer_denominator": transfer_denominator,
        "antithetic_raw_variance": antithetic_raw_variance,
        "antithetic_signal_amplitude_from_policy": float(abs(antithetic_signal[0])),
        "modes": mode_summaries,
        "improvement": {
            "contrast_rmse_antithetic_vs_none": mode_summaries["none"]["contrast_rmse"]
            / mode_summaries["antithetic"]["contrast_rmse"],
            "contrast_rmse_antithetic_vs_white": mode_summaries["white"]["contrast_rmse"]
            / mode_summaries["antithetic"]["contrast_rmse"],
            "smallest_eigenvalue_antithetic_vs_white": mode_summaries["antithetic"]["median_smallest_eigenvalue"]
            / mode_summaries["white"]["median_smallest_eigenvalue"],
            "condition_white_vs_antithetic": mode_summaries["white"]["median_regressor_condition"]
            / mode_summaries["antithetic"]["median_regressor_condition"],
        },
        "online_rls_final": {
            mode: {
                "contrast_estimate": float(online[mode]["contrast"][-1]),
                "contrast_standard_error": float(online[mode]["contrast_se"][-1]),
            }
            for mode in modes
        },
        "artifacts": {
            "contrast_plot": "antithetic_contrast_error.png",
            "online_se_plot": "antithetic_online_standard_error.png",
            "information_plot": "antithetic_regressor_information.png",
            "signal_plot": "antithetic_probe_signals.png",
            "trial_csv": "antithetic_trial_results.csv",
            "online_csv": "antithetic_online_rls.csv",
        },
    }
    write_json(output_dir / "summary.json", summary)
    return summary
