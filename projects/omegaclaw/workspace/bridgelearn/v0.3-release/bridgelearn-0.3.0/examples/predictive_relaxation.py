"""Predictive-coding-style episodic relaxation example.

The example controls an ensemble of local prediction errors under a linearized
relaxation step.  It uses an episodic channel, a step-size actuator for
contraction, and explicit state noise for innovation.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from bridgelearn import (
    BridgeController,
    Channel,
    DynamicsAdapter,
    FixedReferencePolicy,
    GaussianTransition,
    ReferenceBridgePlanner,
    LocalDynamics,
    StepNoiseActuator,
)


@dataclass
class RelaxationState:
    errors: np.ndarray
    rng: np.random.Generator
    curvature: float
    step_size: np.ndarray
    noise_std: np.ndarray

    @property
    def variance(self) -> float:
        return float(np.var(self.errors))

    def relax_once(self) -> None:
        eta = float(self.step_size[0])
        sigma = float(self.noise_std[0])
        self.errors = (
            (1.0 - eta * self.curvature) * self.errors
            + sigma * self.rng.normal(size=self.errors.size)
        )


def run(output_dir: Path, *, seed: int = 11, sweeps: int = 60) -> dict[str, float]:
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)
    start_variance = 0.25
    terminal_variance = 0.001
    state = RelaxationState(
        errors=rng.normal(scale=np.sqrt(start_variance), size=40_000),
        rng=rng,
        curvature=1.5,
        step_size=np.array([0.12]),
        noise_std=np.array([0.015]),
    )

    reference = GaussianTransition(
        contraction=[1.0 - 0.12 * state.curvature],
        innovation=[0.015**2],
    )


    def read_dynamics(context: RelaxationState) -> LocalDynamics:
        eta = max(float(context.step_size[0]), 1e-8)
        equivalent_noise_scale = (float(context.noise_std[0]) / eta) ** 2
        return LocalDynamics(
            variance=[context.variance],
            curvature=[context.curvature],
            noise_scale=[equivalent_noise_scale],
            step_size=context.step_size,
            effective_batch=1.0,
            labels=("prediction_error",),
        )

    def apply_controls(context: RelaxationState, controls: dict[str, object]) -> None:
        context.step_size = np.asarray(controls["step_size"], dtype=np.float64)
        context.noise_std = np.asarray(controls["noise_std"], dtype=np.float64)

    adapter = DynamicsAdapter(
        read_dynamics=read_dynamics,
        apply_controls=apply_controls,
        actuator=StepNoiseActuator(
            step_bounds=(0.001, 1.0),
            noise_std_bounds=(0.0, 0.25),
            stability_margin=1.5,
            max_log_step_change=None,
            relative_tolerance=0.03,
        ),
    )

    controller = BridgeController(
        {
            "activities": Channel(
                name="activities",
                scope="episode",
                adapter=adapter,
                planner=ReferenceBridgePlanner(
                    terminal_variance=[terminal_variance],
                    total_steps=sweeps,
                    reference_policy=FixedReferencePolicy(reference),
                    max_horizon_multiplier=4.0,
                ),
            )
        }
    )

    targets: list[float] = []
    observed: list[float] = []
    step_sizes: list[float] = []
    noise_stds: list[float] = []

    with controller.episode("activities") as episode:
        while not episode.done:
            command = episode.plan(state)
            episode.apply(state, command)
            state.relax_once()
            episode.after_step(state, command)
            targets.append(float(command.target_variance[0]))
            observed.append(state.variance)
            step_sizes.append(float(state.step_size[0]))
            noise_stds.append(float(state.noise_std[0]))

    target_array = np.asarray(targets)
    observed_array = np.asarray(observed)
    summary = {
        "seed": seed,
        "sweeps": len(targets),
        "rmse": float(np.sqrt(np.mean((target_array - observed_array) ** 2))),
        "final_target_variance": float(target_array[-1]),
        "final_observed_variance": float(observed_array[-1]),
        "final_error_rms": float(np.sqrt(np.mean(state.errors**2))),
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    axis_values = np.arange(1, len(targets) + 1)
    figure, axis = plt.subplots(figsize=(8, 4.8))
    axis.plot(axis_values, target_array, label="bridge target")
    axis.plot(axis_values, observed_array, label="prediction-error variance")
    axis.set_xlabel("relaxation sweep")
    axis.set_ylabel("variance")
    axis.set_title("Episodic bridge control of predictive relaxation")
    axis.legend()
    figure.tight_layout()
    figure.savefig(output_dir / "relaxation_tracking.png", dpi=160)
    plt.close(figure)

    print(json.dumps(summary, indent=2))
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("artifacts/predictive_relaxation"),
    )
    parser.add_argument("--seed", type=int, default=11)
    parser.add_argument("--sweeps", type=int, default=60)
    args = parser.parse_args()
    run(args.output_dir, seed=args.seed, sweeps=args.sweeps)
