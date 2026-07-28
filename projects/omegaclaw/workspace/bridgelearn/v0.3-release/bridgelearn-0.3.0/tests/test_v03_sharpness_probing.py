import numpy as np

from bridgelearn import (
    AntitheticProbePolicy,
    ChannelObservation,
    ChannelState,
    CurvatureAdequacyObserver,
    CurvatureFunnel,
    GaussianState,
    GaussianTransition,
    SharpnessJumpDetector,
    SharpnessPlant,
)


def test_antithetic_probe_alternates_and_accounts_transfer() -> None:
    policy = AntitheticProbePolicy(
        contrast_se_threshold=0.01,
        condition_threshold=10.0,
        confidence_threshold=0.5,
        cold_variance=0.02,
        max_realized_variance=2e-4,
    )
    observation = ChannelObservation(
        state=GaussianState([0.001], confidence=[0.1]),
        reference=GaussianTransition([0.9], [1e-6]),
        metadata={
            "c1": [1.8],
            "c2": [-0.81],
            "contrast_standard_error": [0.2],
            "regressor_condition": [1e5],
            "lyapunov_condition": [4.0],
        },
    )
    first = policy.apply(
        desired=GaussianTransition([0.9], [1e-6]),
        observation=observation,
        state=ChannelState(),
    )
    policy.commit(None)
    quiet = ChannelObservation(
        state=GaussianState([0.001], confidence=[1.0]),
        reference=GaussianTransition([0.9], [1e-6]),
        metadata={"c1": [1.8], "c2": [-0.81]},
    )
    # Pair completion is exact even after the trigger disappears.
    second = policy.apply(
        desired=GaussianTransition([0.9], [1e-6]),
        observation=quiet,
        state=ChannelState(cumulative_probe_innovation=first.innovation.copy()),
    )
    assert first.signal[0] > 0.0
    assert second.signal[0] < 0.0
    assert np.isclose(first.signal[0] + second.signal[0], 0.0)
    denominator = abs(1.0 + 1.8 - (-0.81)) ** 2
    expected_raw = first.innovation[0] * denominator
    assert np.isclose(first.signal[0] ** 2, expected_raw)
    assert np.allclose(first.innovation, second.innovation)
    policy.commit(None)
    third = policy.apply(
        desired=GaussianTransition([0.9], [1e-6]),
        observation=quiet,
        state=ChannelState(cumulative_probe_innovation=np.array([1e-3])),
    )
    assert np.allclose(third.signal, 0.0)


def test_sharpness_plant_identifies_progress_and_restoration_rates() -> None:
    rng = np.random.default_rng(8)
    gamma_p = 0.025
    gamma_r = 0.45
    delta = 0.1
    estimator = SharpnessPlant(
        gamma_p=0.002,
        gamma_r=0.05,
        safety_offset=delta,
        forgetting=0.997,
        initial_covariance=1e4,
        residual_window=256,
    )
    h = 4.2
    mu = 0.85
    for k in range(500):
        eta = 0.75 if k % 5 < 2 else 0.35
        g = 0.5 + 0.5 * (k % 7) / 6.0
        theta = 2.0 * (1.0 + mu) - delta
        next_h = h + gamma_p * g - gamma_r * max(eta * h - theta, 0.0)
        next_h += 0.001 * rng.normal()
        funnel = estimator.update(
            previous_curvature=[h],
            current_curvature=[next_h],
            step_size=[eta],
            momentum=[mu],
            progress_signal=[g],
        )
        h = next_h
    parameters = estimator.parameters[0]
    assert abs(parameters[0] - gamma_p) < 0.01
    assert abs(parameters[1] - gamma_r) < 0.08
    predicted = estimator.predict_step(
        funnel,
        step_size=[0.8],
        momentum=[mu],
        progress_signal=[1.0],
    )
    assert predicted.lower[0] <= predicted.center[0] <= predicted.upper[0]
    assert predicted.confidence[0] > 0.1


def test_curvature_adequacy_selects_shortest_calibrated_model() -> None:
    observer = CurvatureAdequacyObserver(smoothing=1.0)
    predictions = {
        "static_linear": CurvatureFunnel([1.9, 0.5], [2.0, 0.6], [2.1, 0.7], model_name="static_linear"),
        "sharpness_plant": CurvatureFunnel([1.8, 2.8], [2.0, 3.0], [2.2, 3.2], model_name="sharpness_plant"),
    }
    report = observer.update(observed_curvature=[2.02, 3.05], predictions=predictions)
    assert report.selected_model[0] == "static_linear"
    assert report.selected_model[1] == "sharpness_plant"


def test_catapult_jump_detector_latches_until_reset() -> None:
    detector = SharpnessJumpDetector(relative_threshold=0.25)
    detector.update([4.0, 2.0])
    report = detector.update([2.0, 2.1])
    assert report.jumped[0] == 1.0
    assert report.latched[0] == 1.0
    detector.reset([True, False])
    report = detector.update([2.1, 2.2])
    assert report.latched[0] == 0.0


def test_antithetic_probe_cycles_two_amplitudes_by_completed_pair() -> None:
    policy = AntitheticProbePolicy(
        contrast_se_threshold=0.01,
        condition_threshold=10.0,
        confidence_threshold=0.5,
        cold_variance=0.02,
        max_realized_variance=2e-4,
        amplitude_levels=(0.5, 1.0),
    )
    observation = ChannelObservation(
        state=GaussianState([0.001], confidence=[0.1]),
        reference=GaussianTransition([0.9], [1e-6]),
        metadata={
            "c1": [1.8],
            "c2": [-0.81],
            "contrast_standard_error": [0.2],
            "regressor_condition": [1e5],
        },
    )
    desired = GaussianTransition([0.9], [1e-6])
    first = policy.apply(desired=desired, observation=observation, state=ChannelState())
    policy.commit(None)
    policy.apply(desired=desired, observation=observation, state=ChannelState())
    policy.commit(None)
    second_level = policy.apply(
        desired=desired, observation=observation, state=ChannelState()
    )
    assert np.isclose(second_level.signal[0] ** 2, 4.0 * first.signal[0] ** 2)


def test_sharpness_aware_planner_checkpoints_identified_plant() -> None:
    from bridgelearn import FixedReferencePolicy, SharpnessAwareReferenceBridgePlanner

    plant = SharpnessPlant(initial_covariance=10.0)
    plant.update(
        previous_curvature=[2.0],
        current_curvature=[2.01],
        step_size=[0.2],
        momentum=[0.5],
        progress_signal=[1.0],
    )
    planner = SharpnessAwareReferenceBridgePlanner(
        terminal_variance=[0.01],
        total_steps=20,
        reference_policy=FixedReferencePolicy(GaussianTransition([0.9], [1e-3])),
        sharpness_model=plant,
        sharpness_rollout_steps=4,
    )
    state = planner.state_dict()

    restored_plant = SharpnessPlant(initial_covariance=10.0)
    restored = SharpnessAwareReferenceBridgePlanner(
        terminal_variance=[0.01],
        total_steps=20,
        reference_policy=FixedReferencePolicy(GaussianTransition([0.9], [1e-3])),
        sharpness_model=restored_plant,
        sharpness_rollout_steps=4,
    )
    restored.load_state_dict(state)
    np.testing.assert_allclose(restored_plant.parameters, plant.parameters)


def test_planner_composes_explicit_probe_innovation_exactly_once() -> None:
    from bridgelearn import (
        DirectTransitionActuator,
        FixedReferencePolicy,
        ReferenceBridgePlanner,
    )

    probe = AntitheticProbePolicy(
        contrast_se_threshold=0.01,
        condition_threshold=10.0,
        confidence_threshold=0.5,
        cold_variance=0.02,
        max_realized_variance=1e-4,
        amplitude_levels=(1.0,),
    )
    planner = ReferenceBridgePlanner(
        terminal_variance=[0.002],
        total_steps=5,
        reference_policy=FixedReferencePolicy(GaussianTransition([0.9], [1e-4])),
        probe_policy=probe,
    )
    observation = ChannelObservation(
        state=GaussianState([0.001], confidence=[0.1]),
        reference=GaussianTransition([0.9], [1e-4]),
        metadata={
            "c1": [1.8],
            "c2": [-0.81],
            "contrast_standard_error": [0.2],
            "regressor_condition": [1e5],
        },
    )
    actuator = DirectTransitionActuator()
    decision = planner.choose(
        state=ChannelState(),
        observation=observation,
        realize=lambda target, obs: actuator.realize(target=target, observation=obs),
    )
    raw = float(np.asarray(decision.plan.diagnostics["probe_raw_innovation"])[0])
    base_innovation = float(decision.plan.controls["innovation"][0])
    assert np.isclose(decision.plan.predicted.innovation[0], base_innovation + raw)
    assert np.isclose(decision.desired.innovation[0], base_innovation + raw)
    assert np.isclose(decision.plan.controls["probe_signal"][0] ** 2, raw)
