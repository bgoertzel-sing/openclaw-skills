from dataclasses import dataclass

import numpy as np

from bridgelearn import (
    BridgeController,
    Channel,
    DynamicsAdapter,
    FeasibilityClock,
    GaussianBridgePath,
    LocalDynamics,
    StepNoiseActuator,
)


@dataclass
class Context:
    samples: np.ndarray
    step_size: np.ndarray
    noise_std: np.ndarray
    curvature: float = 1.0


def test_controller_episode_and_checkpoint_roundtrip() -> None:
    rng = np.random.default_rng(2)
    context = Context(
        samples=rng.normal(scale=np.sqrt(0.04), size=20_000),
        step_size=np.array([0.1]),
        noise_std=np.array([0.01]),
    )

    def read(ctx: Context) -> LocalDynamics:
        return LocalDynamics(
            variance=[float(np.var(ctx.samples))],
            curvature=[ctx.curvature],
            noise_scale=[1.0],
            step_size=ctx.step_size,
            effective_batch=1.0,
        )

    def apply(ctx: Context, controls: dict[str, object]) -> None:
        ctx.step_size = np.asarray(controls["step_size"], dtype=float)
        ctx.noise_std = np.asarray(controls["noise_std"], dtype=float)

    adapter = DynamicsAdapter(
        read_dynamics=read,
        apply_controls=apply,
        actuator=StepNoiseActuator(
            step_bounds=(0.0, 1.5),
            noise_std_bounds=(0.0, 1.0),
            max_log_step_change=None,
        ),
    )
    path = GaussianBridgePath.from_peak(
        start_variance=[0.04],
        peak_variance=[0.05],
        terminal_variance=[0.005],
    )
    channel = Channel(
        name="state",
        path=path,
        adapter=adapter,
        clock=FeasibilityClock.from_name(total_steps=5, warp="smoothstep"),
        scope="episode",
    )
    controller = BridgeController({"state": channel})

    with controller.episode("state") as episode:
        command = episode.plan(context)
        episode.apply(context, command)
        assert episode.state.step == 1
        assert controller.states["state"].step == 0

    command = controller.plan("state", context)
    controller.apply("state", context, command)
    checkpoint = controller.state_dict()
    restored = BridgeController({"state": channel})
    restored.load_state_dict(checkpoint)
    assert restored.states["state"].step == 1
    assert restored.states["state"].progress == controller.states["state"].progress
