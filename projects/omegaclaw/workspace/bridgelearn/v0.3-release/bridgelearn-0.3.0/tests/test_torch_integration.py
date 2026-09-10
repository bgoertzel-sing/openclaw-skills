import numpy as np
import pytest

torch = pytest.importorskip("torch")

from bridgelearn import (  # noqa: E402
    BridgeController,
    Channel,
    FeasibilityClock,
    GaussianBridgePath,
    StepBatchActuator,
)
from bridgelearn.integrations.torch import (  # noqa: E402
    TorchGroupStatistics,
    TorchOptimizerAdapter,
)


def test_torch_optimizer_adapter_updates_parameter_groups_and_batch() -> None:
    first = torch.nn.Parameter(torch.tensor([1.0]))
    second = torch.nn.Parameter(torch.tensor([2.0]))
    optimizer = torch.optim.SGD(
        [
            {"params": [first], "lr": 0.1, "name": "first"},
            {"params": [second], "lr": 0.05, "name": "second"},
        ]
    )
    context = {"effective_batch": 64.0}

    def statistics(ctx):
        return TorchGroupStatistics(
            variance=[0.04, 0.03],
            curvature=[1.0, 3.0],
            noise_scale=[8.0, 12.0],
            effective_batch=ctx["effective_batch"],
        )

    def set_batch(ctx, value):
        ctx["effective_batch"] = value

    adapter = TorchOptimizerAdapter(
        optimizer=optimizer,
        statistics=statistics,
        set_effective_batch=set_batch,
        actuator=StepBatchActuator(
            step_bounds=([0.001, 0.001], [1.0, 0.4]),
            batch_bounds=(16.0, 256.0),
            max_log_step_change=None,
            max_log_batch_change=None,
            relative_tolerance=0.2,
        ),
    )
    path = GaussianBridgePath.from_peak(
        start_variance=[0.04, 0.03],
        peak_variance=[0.05, 0.04],
        terminal_variance=[0.005, 0.01],
    )
    controller = BridgeController(
        {
            "weights": Channel(
                name="weights",
                path=path,
                adapter=adapter,
                clock=FeasibilityClock.from_name(total_steps=10),
            )
        }
    )
    command = controller.plan("weights", context)
    controller.apply("weights", context, command)
    learned_lrs = np.asarray([group["lr"] for group in optimizer.param_groups])
    np.testing.assert_allclose(learned_lrs, command.controls["step_size"])
    assert context["effective_batch"] == command.controls["effective_batch"]


def test_torch_companion_mode_exposes_structural_metadata() -> None:
    from bridgelearn import MomentumStepBatchActuator

    parameter = torch.nn.Parameter(torch.tensor([1.0]))
    optimizer = torch.optim.SGD(
        [{"params": [parameter], "lr": 0.05, "momentum": 0.8, "name": "block"}]
    )

    def statistics(_ctx):
        return TorchGroupStatistics(
            variance=[0.04],
            previous_variance=[0.05],
            lag_covariance=[0.03],
            curvature=[2.0],
            curvature_lower=[1.8],
            curvature_upper=[2.2],
            noise_scale=[4.0],
            effective_batch=64.0,
            structural_adequacy=[0.9],
            contrast_standard_error=[0.02],
            regressor_condition=[20.0],
        )

    adapter = TorchOptimizerAdapter(
        optimizer=optimizer,
        statistics=statistics,
        actuator=MomentumStepBatchActuator(
            step_bounds=(1e-4, 0.5),
            momentum_bounds=(0.0, 0.95),
            batch_bounds=(16.0, 256.0),
        ),
    )
    observation = adapter.observe({})
    assert observation.metadata["structural_diagnostic_supplied"]
    assert np.isclose(np.asarray(observation.metadata["c1"])[0], 1.7)
    assert np.isclose(np.asarray(observation.metadata["c2"])[0], -0.8)
    assert np.isclose(observation.state.confidence[0], 0.9)


def test_torch_momentum_requires_structural_adequacy_by_default() -> None:
    from bridgelearn import MomentumStepBatchActuator

    parameter = torch.nn.Parameter(torch.tensor([1.0]))
    optimizer = torch.optim.SGD(
        [{"params": [parameter], "lr": 0.05, "momentum": 0.8}]
    )

    def statistics(_ctx):
        return TorchGroupStatistics(
            variance=[0.04],
            previous_variance=[0.05],
            lag_covariance=[0.03],
            curvature=[2.0],
            noise_scale=[4.0],
            effective_batch=64.0,
        )

    adapter = TorchOptimizerAdapter(
        optimizer=optimizer,
        statistics=statistics,
        actuator=MomentumStepBatchActuator(),
    )
    with pytest.raises(RuntimeError, match="structural adequacy"):
        adapter.observe({})
