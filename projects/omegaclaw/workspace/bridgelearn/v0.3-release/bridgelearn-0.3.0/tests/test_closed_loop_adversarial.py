from dataclasses import dataclass

import numpy as np

from bridgelearn import (
    BridgeController,
    Channel,
    DynamicsAdapter,
    FixedReferencePolicy,
    GaussianTransition,
    LocalDynamics,
    ReferenceBridgePlanner,
    StepBatchActuator,
)


@dataclass
class VariancePlant:
    variance: float = 0.06
    step_size: float = 0.005
    batch: float = 64.0
    h_est: float = 1.0
    nu_est: float = 2560.0


def test_closed_loop_survives_delayed_noisy_statistics_and_integer_batch() -> None:
    rng = np.random.default_rng(12)
    plant = VariancePlant()
    delayed_h = [1.0] * 5
    delayed_nu = [2560.0] * 5

    def read(p: VariancePlant) -> LocalDynamics:
        return LocalDynamics(
            variance=[p.variance],
            curvature=[p.h_est],
            noise_scale=[p.nu_est],
            step_size=[p.step_size],
            effective_batch=p.batch,
            confidence=[0.8],
            trust_region_step=[0.2],
        )

    def apply(p: VariancePlant, controls: dict[str, object]) -> None:
        p.step_size = float(np.asarray(controls["step_size"])[0])
        p.batch = float(controls["effective_batch"])

    controller = BridgeController(
        {
            "x": Channel(
                name="x",
                adapter=DynamicsAdapter(
                    read_dynamics=read,
                    apply_controls=apply,
                    actuator=StepBatchActuator(
                        step_bounds=(1e-5, 0.2),
                        batch_bounds=(16.0, 512.0),
                        batch_quantum=16.0,
                        compute_price=0.002,
                        resource_deadband=0.08,
                        max_log_step_change=0.5,
                        max_log_batch_change=0.7,
                        relative_tolerance=0.1,
                    ),
                ),
                planner=ReferenceBridgePlanner(
                    terminal_variance=[0.005],
                    total_steps=120,
                    reference_policy=FixedReferencePolicy(
                        GaussianTransition([0.995], [0.001])
                    ),
                    max_horizon_multiplier=32.0,
                ),
            )
        }
    )

    batches = []
    for step in range(400):
        h_true = 1.0 if step < 80 else 1.35
        nu_true = 2560.0 if step < 80 else 3900.0
        delayed_h.append(h_true * float(np.exp(0.06 * rng.normal())))
        delayed_nu.append(nu_true * float(np.exp(0.10 * rng.normal())))
        plant.h_est = delayed_h.pop(0)
        plant.nu_est = delayed_nu.pop(0)
        command = controller.plan("x", plant)
        controller.apply("x", plant, command)
        a = 1.0 - plant.step_size * h_true
        r = plant.step_size**2 * nu_true / plant.batch
        plant.variance = max(a * a * plant.variance + r, 0.0)
        batches.append(plant.batch)
        if controller.done("x"):
            break

    assert np.isfinite(plant.variance)
    assert plant.variance < 0.02
    assert controller.states["x"].progress > 0.9
    changes = np.count_nonzero(np.diff(batches))
    assert changes < 0.75 * len(batches)
