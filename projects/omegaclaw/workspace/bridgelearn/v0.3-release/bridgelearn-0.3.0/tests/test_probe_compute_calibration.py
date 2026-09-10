import numpy as np

from bridgelearn import (
    BridgeTrace,
    ChannelObservation,
    ChannelState,
    ConfidenceProbePolicy,
    ControlCommand,
    GaussianState,
    GaussianTransition,
    LocalDynamics,
    StepBatchActuator,
)


def test_probe_spends_innovation_only_when_cold_and_uncertain() -> None:
    desired = GaussianTransition([0.9], [1e-5])
    observation = ChannelObservation(
        state=GaussianState([0.001], confidence=[0.1]),
        reference=GaussianTransition([0.9], [1e-5]),
    )
    policy = ConfidenceProbePolicy(
        confidence_threshold=0.5,
        cold_variance=0.01,
        max_probe_innovation=1e-3,
        max_total_probe=2e-3,
    )
    adjusted, probe = policy.apply(
        desired=desired, observation=observation, state=ChannelState()
    )
    assert probe[0] > 0.0
    assert adjusted.innovation[0] > desired.innovation[0]


def test_integer_compute_priced_batch_has_hysteresis() -> None:
    dynamics = LocalDynamics(
        variance=[0.08],
        curvature=[1.0],
        noise_scale=[64.0],
        step_size=[0.8],
        effective_batch=128.0,
    )
    observation = ChannelObservation(
        state=dynamics.state(),
        reference=dynamics.reference_transition(),
        local_dynamics=dynamics,
    )
    target = GaussianTransition([0.2], [0.0768])
    actuator = StepBatchActuator(
        step_bounds=(0.0, 1.5),
        batch_bounds=(32.0, 512.0),
        batch_quantum=32.0,
        compute_price=0.02,
        resource_deadband=0.10,
        max_log_step_change=None,
        max_log_batch_change=None,
        relative_tolerance=0.2,
    )
    plan = actuator.realize(target=target, observation=observation)
    batch = float(plan.controls["effective_batch"])
    assert np.isclose(batch / 32.0, round(batch / 32.0))
    assert plan.diagnostics["compute_units"] >= 1.0


def test_trace_calibration_report() -> None:
    trace = BridgeTrace()
    for step in range(1, 21):
        predicted = np.array([0.01 + 0.001 * step])
        command = ControlCommand(
            channel="x",
            controls={},
            desired=GaussianTransition([0.0], predicted),
            predicted=GaussianTransition([0.0], predicted),
            target_variance=predicted,
            predicted_variance=predicted,
            requested_progress=step / 20,
            accepted_progress=step / 20,
            next_step=step,
            feasible=True,
            diagnostics={"compute_units": 1.0, "progress_delta": 0.05},
        )
        trace.append(
            command,
            observed_variance=predicted + 0.0005,
            observed_variance_std=[0.001],
        )
    report = trace.calibration_report()
    assert report.count == 20
    assert np.isclose(report.bias[0], 0.0005)
    assert report.interval_coverage is not None
    assert report.interval_coverage[0] == 1.0
