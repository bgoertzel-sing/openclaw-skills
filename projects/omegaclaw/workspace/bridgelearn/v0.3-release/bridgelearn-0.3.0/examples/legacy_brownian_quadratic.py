"""Legacy v0.1 Brownian-path example.

Retained only as a path/reference consistency ablation. The recommended v0.2
example is ``reference_consistent_quadratic.py``.
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
    BridgeTrace,
    Channel,
    DynamicsAdapter,
    FeasibilityClock,
    GaussianBridgePath,
    GaussianKLProjector,
    LocalDynamics,
    StepBatchActuator,
)


@dataclass
class QuadraticPopulation:
    particles: np.ndarray
    rng: np.random.Generator
    curvature: float
    unit_batch_noise: float
    step_size: np.ndarray
    effective_batch: float

    @property
    def variance(self) -> float:
        return float(np.var(self.particles))

    def update(self) -> None:
        eta = float(self.step_size[0])
        noise_std = np.sqrt(self.unit_batch_noise / self.effective_batch)
        innovation = eta * noise_std * self.rng.normal(size=self.particles.size)
        self.particles = (1.0 - eta * self.curvature) * self.particles + innovation


def run(output_dir: Path, *, seed: int = 7, steps: int = 200) -> dict[str, float]:
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)

    start_variance = 0.060
    peak_variance = 0.080
    terminal_variance = 0.005
    curvature = 1.0
    unit_batch_noise = 64.0
    initial_batch = 128.0
    # This is the local equilibrium step corresponding to the start width.
    initial_q = unit_batch_noise / initial_batch
    initial_step = 2.0 * curvature * start_variance / (
        initial_q + curvature**2 * start_variance
    )

    population = QuadraticPopulation(
        particles=rng.normal(scale=np.sqrt(start_variance), size=50_000),
        rng=rng,
        curvature=curvature,
        unit_batch_noise=unit_batch_noise,
        step_size=np.array([initial_step], dtype=np.float64),
        effective_batch=initial_batch,
    )

    path = GaussianBridgePath.from_peak(
        start_variance=[start_variance],
        peak_variance=[peak_variance],
        terminal_variance=[terminal_variance],
        labels=("quadratic_mode",),
    )

    def read_dynamics(context: QuadraticPopulation) -> LocalDynamics:
        return LocalDynamics(
            variance=[context.variance],
            curvature=[context.curvature],
            noise_scale=[context.unit_batch_noise],
            step_size=context.step_size,
            effective_batch=context.effective_batch,
            labels=("quadratic_mode",),
        )

    def apply_controls(context: QuadraticPopulation, controls: dict[str, object]) -> None:
        context.step_size = np.asarray(controls["step_size"], dtype=np.float64)
        context.effective_batch = float(controls["effective_batch"])

    adapter = DynamicsAdapter(
        read_dynamics=read_dynamics,
        apply_controls=apply_controls,
        actuator=StepBatchActuator(
            step_bounds=(0.005, 1.5),
            batch_bounds=(32.0, 512.0),
            stability_margin=1.7,
            relative_tolerance=0.06,
            max_log_step_change=0.45,
            max_log_batch_change=0.90,
        ),
    )

    controller = BridgeController(
        {
            "weights": Channel(
                name="weights",
                path=path,
                projector=GaussianKLProjector(contraction_bounds=(0.0, 1.0)),
                adapter=adapter,
                clock=FeasibilityClock.from_name(
                    total_steps=steps,
                    warp="smootherstep",
                    permit_approximate_progress=False,
                ),
            )
        }
    )

    trace = BridgeTrace()
    rows: list[dict[str, float | bool]] = []

    for _ in range(steps):
        command = controller.plan("weights", population)
        controller.apply("weights", population, command)
        population.update()
        controller.after_step("weights", population, command)

        target = float(command.target_variance[0])
        observed = population.variance
        rows.append(
            {
                "step": float(command.next_step),
                "progress": float(command.accepted_progress),
                "target_variance": target,
                "observed_variance": observed,
                "step_size": float(population.step_size[0]),
                "effective_batch": float(population.effective_batch),
                "feasible": bool(command.feasible),
            }
        )
        trace.append(command, observed_variance=[observed])

    target_values = np.asarray([row["target_variance"] for row in rows], dtype=float)
    observed_values = np.asarray([row["observed_variance"] for row in rows], dtype=float)
    rmse = float(np.sqrt(np.mean((target_values - observed_values) ** 2)))
    maximum_error = float(np.max(np.abs(target_values - observed_values)))
    governed_fraction = float(
        np.mean([record["diagnostics"]["clock_governed"] for record in trace.records])
    )

    summary = {
        "seed": seed,
        "steps": steps,
        "rmse": rmse,
        "maximum_absolute_error": maximum_error,
        "final_target_variance": float(target_values[-1]),
        "final_observed_variance": float(observed_values[-1]),
        "final_progress": float(controller.states["weights"].progress),
        "governed_fraction": governed_fraction,
        "peak_progress": float(path.peak_progress()[0]),
        "peak_variance": float(path.peak_variance()[0]),
    }

    trace.to_json(output_dir / "trace.json")
    trace.to_csv(output_dir / "trace.csv")
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    steps_axis = np.arange(1, steps + 1)
    figure, axis = plt.subplots(figsize=(8, 4.8))
    axis.plot(steps_axis, target_values, label="bridge target")
    axis.plot(steps_axis, observed_values, label="empirical variance")
    axis.set_xlabel("update")
    axis.set_ylabel("active variance")
    axis.set_title("BridgeLearn control of a noisy quadratic")
    axis.legend()
    figure.tight_layout()
    figure.savefig(output_dir / "variance_tracking.png", dpi=160)
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(8, 4.8))
    axis.plot(steps_axis, [row["step_size"] for row in rows], label="step size")
    axis.set_xlabel("update")
    axis.set_ylabel("step size")
    axis.set_title("Realized contraction control")
    figure.tight_layout()
    figure.savefig(output_dir / "step_size.png", dpi=160)
    plt.close(figure)

    figure, axis = plt.subplots(figsize=(8, 4.8))
    axis.plot(steps_axis, [row["effective_batch"] for row in rows], label="effective batch")
    axis.set_xlabel("update")
    axis.set_ylabel("effective batch")
    axis.set_title("Realized innovation control")
    figure.tight_layout()
    figure.savefig(output_dir / "effective_batch.png", dpi=160)
    plt.close(figure)

    print(json.dumps(summary, indent=2))
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("artifacts/stochastic_quadratic"),
    )
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--steps", type=int, default=200)
    arguments = parser.parse_args()
    run(arguments.output_dir, seed=arguments.seed, steps=arguments.steps)
