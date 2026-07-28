import numpy as np

from bridgelearn import (
    ActuationPlan,
    ChannelState,
    FeasibilityClock,
    GaussianTransition,
)


def _fake_plan(progress: float) -> ActuationPlan:
    feasible = progress <= 0.37
    target = np.array([progress])
    predicted = np.array([min(progress, 0.37)])
    transition = GaussianTransition([0.0], predicted)
    return ActuationPlan(
        controls={},
        predicted=transition,
        feasible=feasible,
        target_variance=target,
        predicted_variance=predicted,
        error=predicted - target,
    )


def test_clock_governs_to_feasible_boundary() -> None:
    clock = FeasibilityClock.from_name(total_steps=1, warp="linear")
    decision = clock.choose(state=ChannelState(), evaluate=_fake_plan)
    assert decision.governed
    assert decision.plan.feasible
    assert abs(decision.accepted_progress - 0.37) < 1e-5
