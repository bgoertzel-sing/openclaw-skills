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
class Plant:
    variance: float = 0.06
    step_size: float = 0.005
    batch: float = 64.0


def test_reference_planner_uses_one_coherent_reference() -> None:
    reference = GaussianTransition([0.995], [0.001])
    plant = Plant()

    def read(p: Plant) -> LocalDynamics:
        return LocalDynamics(
            variance=[p.variance],
            curvature=[1.0],
            noise_scale=[2560.0],
            step_size=[p.step_size],
            effective_batch=p.batch,
        )

    def apply(p: Plant, controls: dict[str, object]) -> None:
        p.step_size = float(np.asarray(controls["step_size"])[0])
        p.batch = float(controls["effective_batch"])

    adapter = DynamicsAdapter(
        read_dynamics=read,
        apply_controls=apply,
        actuator=StepBatchActuator(
            step_bounds=(1e-5, 0.5),
            batch_bounds=(16.0, 512.0),
            max_log_step_change=None,
            max_log_batch_change=None,
            relative_tolerance=0.02,
        ),
    )
    planner = ReferenceBridgePlanner(
        terminal_variance=[0.005],
        total_steps=200,
        reference_policy=FixedReferencePolicy(reference),
    )
    controller = BridgeController(
        {"x": Channel(name="x", adapter=adapter, planner=planner)}
    )
    command = controller.plan("x", plant)
    assert command.diagnostics["reference_consistent"]
    np.testing.assert_allclose(
        command.diagnostics["reference_contraction"], reference.contraction
    )
    np.testing.assert_allclose(
        command.diagnostics["reference_innovation"], reference.innovation
    )
    assert command.accepted_progress > 0.0
