"""Controller orchestration for persistent and episodic bridge channels."""

from __future__ import annotations

from dataclasses import dataclass, field
import copy
from typing import Any, Generic, Literal, Mapping, TypeVar

import numpy as np

from .adapters import ChannelAdapter
from .clocks import FeasibilityClock
from .guards import ProgressGuard
from .paths import BridgePath
from .planners import PlannerDecision, TransitionPlanner
from .projectors import GaussianKLProjector, TransitionProjector
from .types import ChannelState, ControlCommand, GaussianTransition

ContextT = TypeVar("ContextT")


@dataclass(slots=True)
class Channel(Generic[ContextT]):
    """Configuration of one controlled stochastic update channel.

    Two planning modes are supported:

    * ``planner=ReferenceBridgePlanner(...)`` - recommended reference-consistent
      receding-horizon control;
    * ``path + clock + projector`` - legacy v0.1 marginal-path mode retained for
      theory, ablations, and backwards compatibility.
    """

    name: str
    adapter: ChannelAdapter[ContextT]
    path: BridgePath | None = None
    clock: FeasibilityClock | None = None
    projector: TransitionProjector = field(default_factory=GaussianKLProjector)
    planner: TransitionPlanner | None = None
    scope: Literal["persistent", "episode"] = "persistent"
    guard: ProgressGuard | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("channel name must be non-empty.")
        if self.scope not in {"persistent", "episode"}:
            raise ValueError("scope must be 'persistent' or 'episode'.")
        legacy = self.path is not None or self.clock is not None
        if self.planner is None:
            if self.path is None or self.clock is None:
                raise ValueError("a channel requires either planner or both path and clock.")
        elif legacy:
            raise ValueError("planner mode and path/clock mode are mutually exclusive.")


class BridgeController:
    """Bridge controller over arbitrary learning or inference channels."""

    def __init__(
        self,
        channels: Mapping[str, Channel[Any]],
        *,
        mode: Literal["active", "shadow"] = "active",
    ) -> None:
        if mode not in {"active", "shadow"}:
            raise ValueError("mode must be 'active' or 'shadow'.")
        self.mode = mode
        self.channels: dict[str, Channel[Any]] = dict(channels)
        if not self.channels:
            raise ValueError("at least one channel is required.")
        for key, channel in self.channels.items():
            if key != channel.name:
                raise ValueError(f"channel key {key!r} does not match channel.name {channel.name!r}.")
        self.states: dict[str, ChannelState] = {name: ChannelState() for name in self.channels}

    def plan(self, name: str, context: Any) -> ControlCommand:
        channel = self._channel(name)
        return self._plan(channel=channel, state=self.states[name], context=context)

    def apply(self, name: str, context: Any, command: ControlCommand) -> None:
        channel = self._channel(name)
        self._apply(channel=channel, state=self.states[name], context=context, command=command)

    def after_step(self, name: str, context: Any, command: ControlCommand) -> None:
        channel = self._channel(name)
        callback = getattr(channel.adapter, "after_step", None)
        if callback is not None:
            callback(context, command)

    def step(self, name: str, context: Any, update: Any) -> ControlCommand:
        command = self.plan(name, context)
        self.apply(name, context, command)
        update()
        self.after_step(name, context, command)
        return command

    def done(self, name: str) -> bool:
        channel = self._channel(name)
        state = self.states[name]
        if channel.planner is not None:
            return state.progress >= 1.0 - 1e-8
        assert channel.clock is not None
        return channel.clock.done(state)

    def reset(self, name: str) -> None:
        channel = self._channel(name)
        self.states[name] = ChannelState()
        reset = getattr(channel.planner, "reset", None) if channel.planner is not None else None
        if callable(reset):
            reset()

    def replan(self, name: str, path: BridgePath, *, reset_progress: bool = True) -> None:
        channel = self._channel(name)
        if channel.planner is not None:
            raise RuntimeError("replan(path=...) is only valid for legacy path channels.")
        channel.path = path
        if reset_progress:
            self.states[name] = ChannelState()

    def episode(self, name: str, *, path: BridgePath | None = None) -> "BridgeEpisode":
        channel = self._channel(name)
        if path is not None and channel.planner is not None:
            raise ValueError("an episodic path override is not valid for planner channels.")
        selected = channel
        if channel.planner is not None:
            selected = Channel(
                name=channel.name,
                adapter=channel.adapter,
                planner=copy.deepcopy(channel.planner),
                scope="episode",
                guard=channel.guard,
                metadata=dict(channel.metadata),
            )
        if path is not None:
            selected = Channel(
                name=channel.name,
                adapter=channel.adapter,
                path=path,
                clock=channel.clock,
                projector=channel.projector,
                scope="episode",
                guard=channel.guard,
                metadata=dict(channel.metadata),
            )
        return BridgeEpisode(controller=self, channel=selected)

    def state_dict(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "version": 3,
            "mode": self.mode,
            "channels": {},
        }
        for name, state in self.states.items():
            channel = self.channels[name]
            planner_state = None
            if channel.planner is not None:
                getter = getattr(channel.planner, "state_dict", None)
                planner_state = getter() if callable(getter) else None
            payload["channels"][name] = {
                "state": state.state_dict(),
                "path": None if channel.path is None else channel.path.state_dict(),
                "planner": planner_state,
                "metadata": dict(channel.metadata),
                "adapter": (
                    channel.adapter.state_dict()
                    if callable(getattr(channel.adapter, "state_dict", None))
                    else None
                ),
                "guard": (
                    channel.guard.state_dict()
                    if channel.guard is not None
                    and callable(getattr(channel.guard, "state_dict", None))
                    else None
                ),
            }
        return payload

    def load_state_dict(self, state: Mapping[str, Any], *, strict: bool = True) -> None:
        channel_states = state.get("channels", {})
        if strict and set(channel_states) != set(self.channels):
            raise ValueError("checkpoint channel names do not match controller channels.")
        for name, payload in channel_states.items():
            if name not in self.states:
                continue
            self.states[name] = ChannelState.from_state_dict(payload["state"])
            channel = self.channels[name]
            adapter_state = payload.get("adapter")
            adapter_loader = getattr(channel.adapter, "load_state_dict", None)
            if adapter_state is not None and callable(adapter_loader):
                adapter_loader(adapter_state)
            planner_state = payload.get("planner")
            planner_loader = (
                getattr(channel.planner, "load_state_dict", None)
                if channel.planner is not None
                else None
            )
            if planner_state is not None and callable(planner_loader):
                planner_loader(planner_state)
            guard_state = payload.get("guard")
            guard_loader = (
                getattr(channel.guard, "load_state_dict", None)
                if channel.guard is not None
                else None
            )
            if guard_state is not None and callable(guard_loader):
                guard_loader(guard_state)

    def _channel(self, name: str) -> Channel[Any]:
        try:
            return self.channels[name]
        except KeyError as exc:
            raise KeyError(f"unknown bridge channel {name!r}") from exc

    def _legacy_decision(
        self,
        *,
        channel: Channel[Any],
        state: ChannelState,
        observation: Any,
    ) -> PlannerDecision:
        assert channel.path is not None and channel.clock is not None
        if observation.state.size != channel.path.size:
            raise ValueError(
                f"channel {channel.name!r}: observation has {observation.state.size} blocks "
                f"but path has {channel.path.size}."
            )

        def evaluate(progress: float):
            target_variance = channel.path.variance(progress)
            desired = channel.projector.project(
                current_variance=observation.state.variance,
                target_variance=target_variance,
                reference=observation.reference,
            )
            return channel.adapter.realize(target=desired, observation=observation)

        clock_decision = channel.clock.choose(state=state, evaluate=evaluate)
        target = channel.path.variance(clock_decision.accepted_progress)
        desired = channel.projector.project(
            current_variance=observation.state.variance,
            target_variance=target,
            reference=observation.reference,
        )
        return PlannerDecision(
            requested_progress=clock_decision.requested_progress,
            accepted_progress=clock_decision.accepted_progress,
            desired=desired,
            plan=clock_decision.plan,
            diagnostics={
                "planner": "legacy_path_projector",
                "clock_governed": clock_decision.governed,
                "clock_evaluations": clock_decision.evaluations,
                "reference_consistent": False,
            },
        )

    def _plan(
        self,
        *,
        channel: Channel[Any],
        state: ChannelState,
        context: Any,
    ) -> ControlCommand:
        observation = channel.adapter.observe(context)
        if channel.planner is not None:
            decision = channel.planner.choose(
                state=state,
                observation=observation,
                realize=lambda target, obs: channel.adapter.realize(
                    target=target, observation=obs
                ),
            )
        else:
            decision = self._legacy_decision(
                channel=channel,
                state=state,
                observation=observation,
            )

        guard_diagnostics: dict[str, Any] = {}
        guard_tripped = False
        if channel.guard is not None:
            guard_decision = channel.guard.decide(
                context=context,
                current_progress=state.progress,
                proposed_progress=decision.accepted_progress,
            )
            guard_tripped = guard_decision.tripped
            guard_diagnostics = dict(guard_decision.diagnostics or {})
            guard_diagnostics["guard_reason"] = guard_decision.reason
            if guard_decision.max_progress < decision.accepted_progress - 1e-10:
                hold = getattr(channel.planner, "hold", None)
                if channel.planner is not None and callable(hold):
                    decision = hold(
                        state=state,
                        observation=observation,
                        realize=lambda target, obs: channel.adapter.realize(
                            target=target, observation=obs
                        ),
                    )
                else:
                    current = observation.state.variance
                    desired = channel.projector.project(
                        current_variance=current,
                        target_variance=current,
                        reference=observation.reference,
                    )
                    plan = channel.adapter.realize(target=desired, observation=observation)
                    decision = PlannerDecision(
                        requested_progress=state.progress,
                        accepted_progress=state.progress,
                        desired=desired,
                        plan=plan,
                        diagnostics={"planner": "guard_hold"},
                    )

        plan = decision.plan
        compute_units = float(plan.diagnostics.get("compute_units", 1.0))
        delta_progress = max(decision.accepted_progress - state.progress, 0.0)
        diagnostics = {
            **plan.diagnostics,
            **decision.diagnostics,
            "observer_confidence_min": float(np.min(observation.state.confidence)),
            "observer_confidence_mean": float(np.mean(observation.state.confidence)),
            "guard_tripped": guard_tripped,
            "progress_delta": delta_progress,
            "progress_per_compute": delta_progress / max(compute_units, 1e-12),
            **guard_diagnostics,
        }
        return ControlCommand(
            channel=channel.name,
            controls=plan.controls,
            desired=decision.desired,
            predicted=plan.predicted,
            target_variance=plan.target_variance,
            predicted_variance=plan.predicted_variance,
            requested_progress=decision.requested_progress,
            accepted_progress=decision.accepted_progress,
            next_step=state.step + 1,
            feasible=plan.feasible,
            diagnostics=diagnostics,
        )

    def _apply(
        self,
        *,
        channel: Channel[Any],
        state: ChannelState,
        context: Any,
        command: ControlCommand,
    ) -> None:
        if command.channel != channel.name:
            raise ValueError("command belongs to a different channel.")
        if command.next_step != state.step + 1:
            raise RuntimeError("stale or out-of-order control command.")
        if self.mode == "active":
            channel.adapter.apply(context, command)
        commit = getattr(channel.planner, "commit", None) if channel.planner is not None else None
        if callable(commit):
            commit(command)
        state.progress = float(command.accepted_progress)
        state.step = int(command.next_step)
        state.last_controls = dict(command.controls)
        state.last_target_variance = np.asarray(command.target_variance).copy()
        state.last_predicted_variance = np.asarray(command.predicted_variance).copy()
        innovation = np.asarray(command.predicted.innovation, dtype=np.float64)
        if state.cumulative_innovation is None:
            state.cumulative_innovation = np.zeros_like(innovation)
        state.cumulative_innovation += innovation
        probe = command.diagnostics.get("probe_innovation")
        if probe is not None:
            probe_array = np.asarray(probe, dtype=np.float64).reshape(-1)
            if state.cumulative_probe_innovation is None:
                state.cumulative_probe_innovation = np.zeros_like(probe_array)
            state.cumulative_probe_innovation += probe_array
        state.cumulative_compute += float(command.diagnostics.get("compute_units", 1.0))


class BridgeEpisode:
    """Independent ephemeral channel state for inference/relaxation episodes."""

    def __init__(self, *, controller: BridgeController, channel: Channel[Any]) -> None:
        self.controller = controller
        self.channel = channel
        self.state = ChannelState()

    def __enter__(self) -> "BridgeEpisode":
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> bool:
        return False

    def plan(self, context: Any) -> ControlCommand:
        return self.controller._plan(channel=self.channel, state=self.state, context=context)

    def apply(self, context: Any, command: ControlCommand) -> None:
        self.controller._apply(
            channel=self.channel,
            state=self.state,
            context=context,
            command=command,
        )

    def after_step(self, context: Any, command: ControlCommand) -> None:
        callback = getattr(self.channel.adapter, "after_step", None)
        if callback is not None:
            callback(context, command)

    def step(self, context: Any, update: Any) -> ControlCommand:
        command = self.plan(context)
        self.apply(context, command)
        update()
        self.after_step(context, command)
        return command

    @property
    def done(self) -> bool:
        if self.channel.planner is not None:
            return self.state.progress >= 1.0 - 1e-8
        assert self.channel.clock is not None
        return self.channel.clock.done(self.state)
