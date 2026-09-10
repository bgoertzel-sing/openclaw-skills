"""Reference-consistent BridgeLearn v0.2 example.

The controlled plant is a noisy scalar quadratic represented by an ensemble of
particles.  A finite-horizon AR(1) Schrodinger bridge supplies exact marginal
and cross-time targets relative to a fixed commanded reference transition.
The actuator uses learning rate for contraction and quantized effective batch
for innovation, with a small compute price and hysteresis.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from bridgelearn import (
    BridgeController,
    BridgeTrace,
    Channel,
    ConfidenceProbePolicy,
    DynamicsAdapter,
    FixedReferencePolicy,
    GaussianTransition,
    LocalDynamics,
    ReferenceBridgePlanner,
    StepBatchActuator,
)


@dataclass
class QuadraticPlant:
    particles: np.ndarray
    step_size: float = 0.005
    effective_batch: float = 64.0
    curvature_estimate: float = 1.0
    noise_estimate: float = 2560.0
    confidence: float = 1.0

    @property
    def variance(self) -> float:
        return float(np.var(self.particles))

    def update(self, *, curvature: float, noise_scale: float, rng: np.random.Generator) -> None:
        contraction = 1.0 - self.step_size * curvature
        innovation_std = self.step_size * np.sqrt(noise_scale / self.effective_batch)
        self.particles = (
            contraction * self.particles
            + innovation_std * rng.normal(size=self.particles.shape)
        )


def onecycle(step: int, total: int, low: float, high: float, final: float, peak: float = 0.3) -> float:
    progress = step / max(total - 1, 1)
    if progress <= peak:
        phase = progress / peak
        return low + 0.5 * (high - low) * (1.0 - np.cos(np.pi * phase))
    phase = (progress - peak) / (1.0 - peak)
    return final + 0.5 * (high - final) * (1.0 + np.cos(np.pi * phase))


def simulate_baseline(
    initial: np.ndarray,
    *,
    steps: int,
    batch: float,
    lr_low: float,
    lr_high: float,
    lr_final: float,
    seed: int,
    shock_step: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    particles = initial.copy()
    variances = [float(np.var(particles))]
    means = [float(np.mean(particles))]
    losses = [0.5 * float(np.mean(particles**2))]
    rates = []
    for step in range(steps):
        eta = onecycle(step, steps, lr_low, lr_high, lr_final)
        curvature = 1.0 if step < shock_step else 1.35
        noise = 2560.0 if step < shock_step else 3900.0
        contraction = 1.0 - eta * curvature
        particles = particles * contraction + eta * np.sqrt(noise / batch) * rng.normal(
            size=particles.shape
        )
        rates.append(eta)
        variances.append(float(np.var(particles)))
        means.append(float(np.mean(particles)))
        losses.append(0.5 * curvature * float(np.mean(particles**2)))
    return (
        np.asarray(variances),
        np.asarray(means),
        np.asarray(losses),
        np.asarray(rates),
    )


def main() -> None:
    output = Path(__file__).resolve().parents[1] / "artifacts" / "reference_consistent_quadratic"
    output.mkdir(parents=True, exist_ok=True)

    nominal_steps = 200
    max_updates = 1200
    particle_count = 30_000
    rng = np.random.default_rng(20260722)
    initial = rng.normal(loc=1.5, scale=np.sqrt(0.06), size=particle_count)
    plant = QuadraticPlant(initial.copy())

    reference = GaussianTransition(contraction=[0.995], innovation=[0.001])

    def read_dynamics(system: QuadraticPlant) -> LocalDynamics:
        return LocalDynamics(
            variance=[system.variance],
            curvature=[system.curvature_estimate],
            noise_scale=[system.noise_estimate],
            step_size=[system.step_size],
            effective_batch=system.effective_batch,
            confidence=[system.confidence],
            trust_region_step=[0.20],
        )

    def apply_controls(system: QuadraticPlant, controls: dict[str, object]) -> None:
        system.step_size = float(np.asarray(controls["step_size"])[0])
        system.effective_batch = float(controls["effective_batch"])

    actuator = StepBatchActuator(
        step_bounds=(1e-5, 0.20),
        batch_bounds=(16.0, 512.0),
        batch_quantum=16.0,
        compute_price=0.004,
        compute_reference=64.0,
        resource_deadband=0.06,
        max_log_step_change=0.45,
        max_log_batch_change=0.70,
        relative_tolerance=0.05,
    )
    adapter = DynamicsAdapter(
        read_dynamics=read_dynamics,
        apply_controls=apply_controls,
        actuator=actuator,
    )
    planner = ReferenceBridgePlanner(
        terminal_variance=[0.005],
        total_steps=nominal_steps,
        reference_policy=FixedReferencePolicy(reference),
        probe_policy=ConfidenceProbePolicy(
            confidence_threshold=0.45,
            cold_variance=0.012,
            max_probe_innovation=2.5e-5,
            max_total_probe=5e-4,
        ),
        max_horizon_multiplier=64.0,
        permit_approximate_progress=False,
    )
    controller = BridgeController(
        {"weights": Channel(name="weights", adapter=adapter, planner=planner)}
    )
    trace = BridgeTrace()

    targets = [plant.variance]
    empirical = [plant.variance]
    rates: list[float] = []
    batches: list[float] = []
    progress: list[float] = [0.0]
    losses = [0.5 * float(np.mean(plant.particles**2))]

    for step in range(max_updates):
        true_curvature = 1.0 if step < nominal_steps // 2 else 1.35
        true_noise = 2560.0 if step < nominal_steps // 2 else 3900.0
        # The observer is deliberately noisy and less confident around the shock.
        plant.curvature_estimate = true_curvature * float(np.exp(0.03 * rng.normal()))
        plant.noise_estimate = true_noise * float(np.exp(0.06 * rng.normal()))
        plant.confidence = (
            0.30
            if nominal_steps // 2 <= step < nominal_steps // 2 + 12
            else (0.25 if 500 <= step < 525 and plant.variance < 0.012 else 0.90)
        )

        command = controller.plan("weights", plant)
        controller.apply("weights", plant, command)
        plant.update(curvature=true_curvature, noise_scale=true_noise, rng=rng)
        controller.after_step("weights", plant, command)

        observed = plant.variance
        variance_std = np.sqrt(2.0 / max(particle_count - 1, 1)) * observed
        trace.append(
            command,
            observed_variance=[observed],
            observed_variance_std=[variance_std],
            extra={"true_curvature": true_curvature, "true_noise": true_noise},
        )
        targets.append(float(command.target_variance[0]))
        empirical.append(observed)
        rates.append(plant.step_size)
        batches.append(plant.effective_batch)
        progress.append(command.accepted_progress)
        losses.append(0.5 * true_curvature * float(np.mean(plant.particles**2)))
        if controller.done("weights"):
            break

    actual_steps = len(rates)
    target_array = np.asarray(targets)
    empirical_array = np.asarray(empirical)
    rates_array = np.asarray(rates)
    batches_array = np.asarray(batches)
    average_batch = float(np.mean(batches_array))

    baseline_variance, baseline_mean, baseline_loss, baseline_rates = simulate_baseline(
        initial,
        steps=actual_steps,
        batch=average_batch,
        lr_low=float(rates_array[0]),
        lr_high=float(np.max(rates_array)),
        lr_final=float(rates_array[-1]),
        seed=20260723,
        shock_step=nominal_steps // 2,
    )

    calibration = trace.calibration_report()
    effort = trace.control_effort()
    summary = {
        "bridge": {
            "tracking_rmse": float(np.sqrt(np.mean((empirical_array[1:] - target_array[1:]) ** 2))),
            "final_variance": float(empirical_array[-1]),
            "final_mean_error": float(np.mean(plant.particles)),
            "final_task_loss": float(losses[-1]),
            "cumulative_task_loss": float(np.sum(losses[1:])),
            "final_progress": float(progress[-1]),
            "actual_updates": actual_steps,
            "nominal_updates": nominal_steps,
            "mean_effective_batch": average_batch,
            "total_examples_equivalent": float(np.sum(batches_array)),
            "step_size_min": float(np.min(rates_array)),
            "step_size_max": float(np.max(rates_array)),
            "probe_innovation": controller.states["weights"].cumulative_probe_innovation.tolist(),
            "calibration": calibration.to_dict(),
            "control_effort": effort,
        },
        "compute_matched_onecycle": {
            "fixed_batch": average_batch,
            "final_variance": float(baseline_variance[-1]),
            "final_mean_error": float(baseline_mean[-1]),
            "final_task_loss": float(baseline_loss[-1]),
            "cumulative_task_loss": float(np.sum(baseline_loss[1:])),
            "tracking_rmse_to_bridge_target": float(
                np.sqrt(np.mean((baseline_variance[1:] - target_array[1:]) ** 2))
            ),
            "total_examples_equivalent": float(average_batch * actual_steps),
        },
    }
    (output / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    trace.to_json(output / "trace.json")
    trace.to_csv(output / "trace.csv")
    calibration.to_json(output / "calibration.json")

    try:
        import matplotlib.pyplot as plt

        axis = np.arange(actual_steps + 1)
        plt.figure(figsize=(8.0, 4.6))
        plt.plot(axis, target_array, label="reference-consistent target")
        plt.plot(axis, empirical_array, label="BridgeLearn empirical")
        plt.plot(axis, baseline_variance, label="compute-matched OneCycle")
        plt.xlabel("optimizer update")
        plt.ylabel("active variance")
        plt.legend()
        plt.tight_layout()
        plt.savefig(output / "variance_tracking.png", dpi=180)
        plt.close()

        plt.figure(figsize=(8.0, 4.2))
        plt.plot(np.arange(actual_steps), rates_array, label="BridgeLearn step")
        plt.plot(np.arange(actual_steps), baseline_rates, label="OneCycle step")
        plt.xlabel("optimizer update")
        plt.ylabel("step size")
        plt.legend()
        plt.tight_layout()
        plt.savefig(output / "step_size.png", dpi=180)
        plt.close()

        plt.figure(figsize=(8.0, 4.2))
        plt.step(np.arange(actual_steps), batches_array, where="post")
        plt.xlabel("optimizer update")
        plt.ylabel("quantized effective batch")
        plt.tight_layout()
        plt.savefig(output / "effective_batch.png", dpi=180)
        plt.close()

        predicted_next = np.asarray(
            [record["predicted_variance"][0] for record in trace.records],
            dtype=np.float64,
        )
        observed_next = np.asarray(
            [record["observed_variance"][0] for record in trace.records],
            dtype=np.float64,
        )
        plt.figure(figsize=(5.2, 5.0))
        plt.scatter(predicted_next, observed_next, s=8, alpha=0.45)
        limits = [
            float(min(np.min(predicted_next), np.min(observed_next))),
            float(max(np.max(predicted_next), np.max(observed_next))),
        ]
        plt.plot(limits, limits, linestyle="--", linewidth=1.0)
        plt.xlabel("predicted next variance")
        plt.ylabel("realized next variance")
        plt.tight_layout()
        plt.savefig(output / "one_step_calibration.png", dpi=180)
        plt.close()
    except ImportError:
        pass

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
