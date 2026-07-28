"""Algorithm adapters.

Adapters are the only layer that needs to know whether a channel comes from
backpropagation, predictive coding, reinforcement learning, a fixed-point
solver, or a custom dynamical system.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Generic, Protocol, TypeVar

from .actuators import TransitionActuator
from .types import (
    ActuationPlan,
    ChannelObservation,
    ControlCommand,
    GaussianTransition,
    LocalDynamics,
)

ContextT = TypeVar("ContextT")


class ChannelAdapter(Protocol, Generic[ContextT]):
    def observe(self, context: ContextT) -> ChannelObservation:
        ...

    def realize(
        self,
        *,
        target: GaussianTransition,
        observation: ChannelObservation,
    ) -> ActuationPlan:
        ...

    def apply(self, context: ContextT, command: ControlCommand) -> None:
        ...


@dataclass(slots=True)
class DynamicsAdapter(Generic[ContextT]):
    """Compose a local-dynamics callback with a reusable actuator."""

    read_dynamics: Callable[[ContextT], LocalDynamics]
    apply_controls: Callable[[ContextT, dict[str, Any]], None]
    actuator: TransitionActuator
    after_step_callback: Callable[[ContextT, ControlCommand], None] | None = None
    read_reference: Callable[[ContextT, LocalDynamics], GaussianTransition] | None = None
    read_metadata: Callable[[ContextT, LocalDynamics], dict[str, Any]] | None = None

    def observe(self, context: ContextT) -> ChannelObservation:
        dynamics = self.read_dynamics(context)
        reference = (
            dynamics.reference_transition()
            if self.read_reference is None
            else self.read_reference(context, dynamics)
        )
        metadata = {
            "reference_source": "current_command"
            if self.read_reference is None
            else "commanded_callback"
        }
        if self.read_metadata is not None:
            metadata.update(self.read_metadata(context, dynamics))
        return ChannelObservation(
            state=dynamics.state(),
            reference=reference,
            local_dynamics=dynamics,
            metadata=metadata,
        )

    def realize(
        self,
        *,
        target: GaussianTransition,
        observation: ChannelObservation,
    ) -> ActuationPlan:
        return self.actuator.realize(target=target, observation=observation)

    def apply(self, context: ContextT, command: ControlCommand) -> None:
        self.apply_controls(context, dict(command.controls))

    def after_step(self, context: ContextT, command: ControlCommand) -> None:
        if self.after_step_callback is not None:
            self.after_step_callback(context, command)


@dataclass(slots=True)
class CallbackAdapter(Generic[ContextT]):
    """Fully generic callback adapter.

    This is the escape hatch for unusual predictive-coding, CAROM, or RL
    implementations.  No gradients or optimizer objects are assumed.
    """

    observe_callback: Callable[[ContextT], ChannelObservation]
    realize_callback: Callable[[GaussianTransition, ChannelObservation], ActuationPlan]
    apply_callback: Callable[[ContextT, ControlCommand], None]
    after_step_callback: Callable[[ContextT, ControlCommand], None] | None = None

    def observe(self, context: ContextT) -> ChannelObservation:
        return self.observe_callback(context)

    def realize(
        self,
        *,
        target: GaussianTransition,
        observation: ChannelObservation,
    ) -> ActuationPlan:
        return self.realize_callback(target, observation)

    def apply(self, context: ContextT, command: ControlCommand) -> None:
        self.apply_callback(context, command)

    def after_step(self, context: ContextT, command: ControlCommand) -> None:
        if self.after_step_callback is not None:
            self.after_step_callback(context, command)
