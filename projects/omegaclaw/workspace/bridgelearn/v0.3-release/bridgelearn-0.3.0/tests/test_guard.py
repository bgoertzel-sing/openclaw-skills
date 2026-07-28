from bridgelearn import PatienceMetricGuard


def test_patience_guard_freezes_after_persistent_degradation() -> None:
    context = {"score": 1.0}
    guard = PatienceMetricGuard(
        metric=lambda ctx: ctx["score"],
        mode="max",
        patience=2,
        absolute_tolerance=0.05,
    )
    first = guard.decide(context=context, current_progress=0.1, proposed_progress=0.2)
    assert not first.tripped
    context["score"] = 0.8
    second = guard.decide(context=context, current_progress=0.2, proposed_progress=0.3)
    assert not second.tripped
    third = guard.decide(context=context, current_progress=0.2, proposed_progress=0.3)
    assert third.tripped
    assert third.max_progress == 0.2
