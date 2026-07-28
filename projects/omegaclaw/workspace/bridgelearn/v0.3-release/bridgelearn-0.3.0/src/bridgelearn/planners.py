"""Reference-consistent receding-horizon planners."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Any, Callable, Protocol, Sequence

import numpy as np
import numpy.typing as npt

from .paths import LinearGaussianBridgePath
from .probing import NoProbePolicy, ProbeDecision, ProbePolicy
from .references import FilteredReferencePolicy, ReferencePolicy
from .types import (
    ActuationPlan,
    ChannelObservation,
    ChannelState,
    FloatArray,
    GaussianTransition,
    as_float_array,
    broadcast_array,
)


@dataclass(frozen=True, slots=True)
class PlannerDecision:
    requested_progress: float
    accepted_progress: float
    desired: GaussianTransition
    plan: ActuationPlan
    diagnostics: dict[str, Any] = field(default_factory=dict)


class TransitionPlanner(Protocol):
    def choose(
        self,
        *,
        state: ChannelState,
        observation: ChannelObservation,
        realize: Callable[[GaussianTransition, ChannelObservation], ActuationPlan],
    ) -> PlannerDecision:
        ...




def _attach_probe_controls(
    plan: ActuationPlan,
    decision: ProbeDecision,
    *,
    current_variance: FloatArray,
) -> ActuationPlan:
    """Compose an ordinary actuator plan with an explicit probe channel.

    Antithetic probe energy is realized by ``probe_signal`` itself.  The
    ordinary actuator therefore plans against ``decision.actuator_transition``;
    this function adds the external innovation exactly once to the predicted
    transition and retargets diagnostics to the total probed transition.
    """

    external = np.asarray(decision.external_innovation, dtype=np.float64)
    predicted = GaussianTransition(
        contraction=plan.predicted.contraction,
        innovation=plan.predicted.innovation + external,
    )
    target_variance = decision.transition.next_variance(current_variance)
    predicted_variance = predicted.next_variance(current_variance)
    difference = predicted_variance - target_variance
    scale = np.maximum.reduce(
        [
            np.abs(target_variance),
            np.abs(np.asarray(current_variance, dtype=np.float64)),
            np.full_like(target_variance, 1e-12),
        ]
    )
    controls = dict(plan.controls)
    if np.any(np.abs(decision.signal) > 0.0):
        control_name = str(
            decision.diagnostics.get("probe_signal_control_name", "probe_signal")
        )
        controls[control_name] = decision.signal.copy()
    diagnostics = {
        **dict(plan.diagnostics),
        **dict(decision.diagnostics),
        "probe_external_innovation": external.copy(),
        "probe_innovation_composed_once": True,
    }
    return replace(
        plan,
        controls=controls,
        predicted=predicted,
        target_variance=target_variance,
        predicted_variance=predicted_variance,
        error=difference / scale,
        diagnostics=diagnostics,
    )

@dataclass(slots=True)
class ReferenceBridgePlanner:
    """Finite-horizon scalar covariance steering relative to one plant model.

    At every control opportunity the planner:

    1. selects a slowly varying or explicitly fixed reference transition;
    2. solves the exact linear-Gaussian bridge from the current variance to the
       terminal variance over the remaining horizon;
    3. takes the bridge's first exact Markov transition;
    4. optionally adds a bounded dual-control probe;
    5. extends the horizon when the actuator cannot realize the transition.

    This is the recommended v0.2 planner.  Brownian paths and one-step KL
    projection remain available as a legacy/diagnostic mode.
    """

    terminal_variance: FloatArray | Sequence[float] | npt.ArrayLike
    total_steps: int
    reference_policy: ReferencePolicy = field(default_factory=FilteredReferencePolicy)
    probe_policy: ProbePolicy = field(default_factory=NoProbePolicy)
    max_horizon_multiplier: float = 8.0
    horizon_search_points: int = 24
    permit_approximate_progress: bool = False
    innovation_floor: float = 1e-12
    labels: tuple[str, ...] = ()
    remaining_horizon: int | None = None
    pending_horizon: int | None = None

    def __post_init__(self) -> None:
        terminal = as_float_array(self.terminal_variance, name="terminal_variance")
        if np.any(terminal < 0.0):
            raise ValueError("terminal_variance must be non-negative.")
        if self.total_steps <= 0:
            raise ValueError("total_steps must be positive.")
        if self.max_horizon_multiplier < 1.0:
            raise ValueError("max_horizon_multiplier must be at least 1.")
        if self.horizon_search_points < 2:
            raise ValueError("horizon_search_points must be at least 2.")
        if self.innovation_floor <= 0.0:
            raise ValueError("innovation_floor must be positive.")
        if self.labels and len(self.labels) != terminal.size:
            raise ValueError("labels must have one entry per block.")
        self.terminal_variance = terminal

    @property
    def size(self) -> int:
        return int(np.asarray(self.terminal_variance).size)

    def _candidate_horizons(self, nominal: int) -> list[int]:
        maximum = max(nominal, int(np.ceil(nominal * self.max_horizon_multiplier)))
        if maximum == nominal:
            return [nominal]
        geometric = np.geomspace(nominal, maximum, self.horizon_search_points)
        values = sorted({nominal, maximum, *(int(np.ceil(value)) for value in geometric)})
        return [value for value in values if value >= 1]

    def choose(
        self,
        *,
        state: ChannelState,
        observation: ChannelObservation,
        realize: Callable[[GaussianTransition, ChannelObservation], ActuationPlan],
    ) -> PlannerDecision:
        if observation.state.size != self.size:
            raise ValueError("observation and terminal variance sizes do not match.")
        reference = self.reference_policy.select(observation)
        reference = GaussianTransition(
            contraction=reference.contraction,
            innovation=np.maximum(reference.innovation, self.innovation_floor),
        )
        nominal_horizon = max(
            1,
            self.total_steps if self.remaining_horizon is None else self.remaining_horizon,
        )
        requested_progress = max(
            float(state.progress),
            float(np.clip(1.0 - (nominal_horizon - 1) / self.total_steps, 0.0, 1.0)),
        )

        candidates: list[tuple[int, float, GaussianTransition, ActuationPlan, FloatArray, dict[str, Any]]] = []
        for horizon in self._candidate_horizons(nominal_horizon):
            bridge = LinearGaussianBridgePath(
                start_variance=observation.state.variance,
                terminal_variance=self.terminal_variance,
                horizon_steps=horizon,
                reference_contraction=reference.contraction,
                reference_innovation=reference.innovation,
                labels=observation.state.labels or self.labels,
            )
            exact = bridge.transition_at(0)
            probe_decision = self.probe_policy.apply(
                desired=exact,
                observation=observation,
                state=state,
            )
            desired = probe_decision.transition
            assert probe_decision.actuator_transition is not None
            plan = realize(probe_decision.actuator_transition, observation)
            plan = _attach_probe_controls(
                plan,
                probe_decision,
                current_variance=observation.state.variance,
            )
            progress = max(
                float(state.progress),
                float(np.clip(1.0 - (horizon - 1) / self.total_steps, 0.0, 1.0)),
            )
            diagnostics = {
                "planner": "reference_bridge",
                "candidate_horizon": horizon,
                "nominal_horizon": nominal_horizon,
                "reference_contraction": reference.contraction.copy(),
                "reference_innovation": reference.innovation.copy(),
                "probe_innovation": probe_decision.innovation.copy(),
                "probe_signal": probe_decision.signal.copy(),
                **dict(probe_decision.diagnostics),
                "bridge_next_variance": exact.next_variance(observation.state.variance),
                "reference_consistent": True,
            }
            candidates.append((horizon, progress, desired, plan, probe_decision.innovation, diagnostics))
            if plan.feasible:
                self.pending_horizon = horizon
                return PlannerDecision(
                    requested_progress=requested_progress,
                    accepted_progress=progress,
                    desired=desired,
                    plan=plan,
                    diagnostics={**diagnostics, "horizon_governed": horizon != nominal_horizon},
                )

        # No exact actuator realization was found.  Either freeze progress and
        # use the gentlest candidate, or permit the lowest-error approximation.
        def score(item: tuple[int, float, GaussianTransition, ActuationPlan, FloatArray, dict[str, Any]]) -> float:
            plan = item[3]
            return float(np.max(np.abs(plan.error)))

        selected = min(candidates, key=score)
        horizon, progress, desired, plan, _probe, diagnostics = selected
        accepted = progress if self.permit_approximate_progress else float(state.progress)
        self.pending_horizon = horizon
        return PlannerDecision(
            requested_progress=requested_progress,
            accepted_progress=accepted,
            desired=desired,
            plan=plan,
            diagnostics={
                **diagnostics,
                "horizon_governed": True,
                "no_feasible_horizon": True,
                "selected_approximation_error": score(selected),
            },
        )

    def hold(
        self,
        *,
        state: ChannelState,
        observation: ChannelObservation,
        realize: Callable[[GaussianTransition, ChannelObservation], ActuationPlan],
    ) -> PlannerDecision:
        """Hold the current active width while a validation/safety guard is tripped."""

        reference = self.reference_policy.select(observation)
        current = observation.state.variance
        # Exact one-step minimum-KL hold under the selected reference.
        a0 = reference.contraction
        r0 = np.maximum(reference.innovation, self.innovation_floor)
        discriminant = r0**2 + 4.0 * a0**2 * current**2
        denominator = r0 + np.sqrt(discriminant)
        contraction = np.divide(
            2.0 * a0 * current,
            denominator,
            out=np.zeros_like(current),
            where=denominator > 0.0,
        )
        maximum = np.ones_like(current)
        contraction = np.clip(contraction, -maximum, maximum)
        innovation = np.maximum(current - contraction**2 * current, 0.0)
        desired = GaussianTransition(contraction=contraction, innovation=innovation)
        plan = realize(desired, observation)
        return PlannerDecision(
            requested_progress=float(state.progress),
            accepted_progress=float(state.progress),
            desired=desired,
            plan=plan,
            diagnostics={"planner": "reference_bridge_hold", "reference_consistent": True},
        )

    def commit(self, command: Any) -> None:
        """Commit the chosen remaining horizon after the command is applied."""

        if self.pending_horizon is not None:
            self.remaining_horizon = max(int(self.pending_horizon) - 1, 0)
            self.pending_horizon = None
        probe_commit = getattr(self.probe_policy, "commit", None)
        if callable(probe_commit):
            probe_commit(command)

    def reset(self) -> None:
        self.remaining_horizon = None
        self.pending_horizon = None
        reset = getattr(self.reference_policy, "reset", None)
        if callable(reset):
            reset()
        probe_reset = getattr(self.probe_policy, "reset", None)
        if callable(probe_reset):
            probe_reset()

    def state_dict(self) -> dict[str, Any]:
        state: dict[str, Any] = {
            "type": "reference_bridge_planner",
            "terminal_variance": np.asarray(self.terminal_variance).tolist(),
            "total_steps": self.total_steps,
            "remaining_horizon": self.remaining_horizon,
        }
        reference_state = getattr(self.reference_policy, "state_dict", None)
        if callable(reference_state):
            state["reference_policy"] = reference_state()
        probe_state = getattr(self.probe_policy, "state_dict", None)
        if callable(probe_state):
            state["probe_policy"] = probe_state()
        return state

    def load_state_dict(self, state: dict[str, Any]) -> None:
        self.remaining_horizon = (
            None if state.get("remaining_horizon") is None else int(state["remaining_horizon"])
        )
        self.pending_horizon = None
        reference_state = state.get("reference_policy")
        loader = getattr(self.reference_policy, "load_state_dict", None)
        if reference_state is not None and callable(loader):
            loader(reference_state)
        probe_state = state.get("probe_policy")
        probe_loader = getattr(self.probe_policy, "load_state_dict", None)
        if probe_state is not None and callable(probe_loader):
            probe_loader(probe_state)


@dataclass(slots=True)
class SharpnessAwareReferenceBridgePlanner(ReferenceBridgePlanner):
    """Two-timescale MPC wrapper around :class:`ReferenceBridgePlanner`.

    The covariance bridge is *not* enlarged with curvature as an additional
    bridge state.  Instead, a slow scalar sharpness model is rolled forward as
    a predicted disturbance for every candidate physical horizon.  By default
    the complete candidate horizon is rolled forward; ``sharpness_rollout_steps``
    may cap this for very long horizons. Candidate commands are inverted against
    the lower curvature edge (promised
    contraction) and accepted only when the upper edge stays inside the
    momentum stability threshold.
    """

    sharpness_model: Any = None
    sharpness_rollout_steps: int | None = None
    max_relative_funnel_width: float = 1.0
    minimum_curvature_confidence: float = 0.05
    safety_offset: float = 0.1
    progress_signal: float | Sequence[float] | npt.ArrayLike = 1.0
    freeze_on_inadequacy: bool = True

    def __post_init__(self) -> None:
        ReferenceBridgePlanner.__post_init__(self)
        if self.sharpness_model is None:
            raise ValueError("SharpnessAwareReferenceBridgePlanner requires sharpness_model.")
        if self.sharpness_rollout_steps is not None and self.sharpness_rollout_steps <= 0:
            raise ValueError("sharpness_rollout_steps must be positive when supplied.")
        if self.max_relative_funnel_width <= 0.0:
            raise ValueError("max_relative_funnel_width must be positive.")
        if not 0.0 <= self.minimum_curvature_confidence <= 1.0:
            raise ValueError("minimum_curvature_confidence must lie in [0,1].")
        if self.safety_offset < 0.0:
            raise ValueError("safety_offset must be non-negative.")

    def _initial_funnel(self, observation: ChannelObservation) -> Any:
        from .sharpness import CurvatureFunnel

        dynamics = observation.local_dynamics
        if dynamics is None:
            raise ValueError("sharpness-aware planning requires local_dynamics.")
        adequate = (
            dynamics.curvature_adequacy >= self.minimum_curvature_confidence
        )
        jump_latched = observation.metadata.get("sharpness_jump_latched")
        if jump_latched is not None:
            adequate = adequate & ~broadcast_array(
                jump_latched, dynamics.size, name="sharpness_jump_latched"
            ).astype(bool)
        return CurvatureFunnel(
            lower=dynamics.curvature_lower,
            center=dynamics.curvature,
            upper=dynamics.curvature_upper,
            confidence=dynamics.curvature_adequacy,
            model_name=str(observation.metadata.get("curvature_model", "sharpness_plant")),
            adequate=adequate,
        )

    def _synthetic_observation(
        self,
        observation: ChannelObservation,
        *,
        funnel: Any,
        variance: FloatArray,
        previous_variance: FloatArray,
        lag_covariance: FloatArray,
        step_size: FloatArray,
        momentum: FloatArray,
        effective_batch: float,
    ) -> ChannelObservation:
        dynamics = observation.local_dynamics
        assert dynamics is not None
        updated = replace(
            dynamics,
            variance=variance,
            previous_variance=previous_variance,
            lag_covariance=lag_covariance,
            curvature=funnel.center,
            curvature_lower=funnel.lower,
            curvature_upper=funnel.upper,
            curvature_adequacy=funnel.confidence,
            step_size=step_size,
            momentum=momentum,
            effective_batch=effective_batch,
        )
        return ChannelObservation(
            state=updated.state(),
            reference=updated.reference_transition(),
            local_dynamics=updated,
            payload=observation.payload,
            metadata={**dict(observation.metadata), "synthetic_rollout": True},
        )

    def _rollout_candidate(
        self,
        *,
        bridge: LinearGaussianBridgePath,
        horizon: int,
        observation: ChannelObservation,
        realize: Callable[[GaussianTransition, ChannelObservation], ActuationPlan],
        first_desired: GaussianTransition,
        first_plan: ActuationPlan,
    ) -> tuple[bool, dict[str, Any]]:
        dynamics = observation.local_dynamics
        assert dynamics is not None
        funnel = self._initial_funnel(observation)
        if self.freeze_on_inadequacy and not np.all(funnel.adequate):
            return False, {
                "sharpness_rollout_feasible": False,
                "sharpness_failure": "initial_model_inadequate",
                "sharpness_fallback_fraction": float(np.mean(~np.asarray(funnel.adequate))),
            }
        signal = broadcast_array(
            observation.metadata.get("sharpness_progress_signal", self.progress_signal),
            dynamics.size,
            name="sharpness_progress_signal",
        )
        current_observation = observation
        maximum_steps = (
            horizon
            if self.sharpness_rollout_steps is None
            else min(horizon, self.sharpness_rollout_steps)
        )
        maximum_width = float(np.max(funnel.relative_width))
        maximum_utilization = 0.0
        maximum_projection_error = 0.0
        for index in range(maximum_steps):
            desired = first_desired if index == 0 else bridge.transition_at(index)
            plan = first_plan if index == 0 else realize(desired, current_observation)
            maximum_projection_error = max(
                maximum_projection_error, float(np.max(np.abs(plan.error)))
            )
            if not plan.feasible:
                return False, {
                    "sharpness_rollout_feasible": False,
                    "sharpness_failure": "actuator_projection",
                    "sharpness_failure_step": index,
                    "sharpness_max_projection_error": maximum_projection_error,
                }
            current_dynamics = current_observation.local_dynamics
            assert current_dynamics is not None
            step = broadcast_array(
                plan.controls.get("step_size", current_dynamics.step_size),
                current_dynamics.size,
                name="step_size",
            )
            momentum = broadcast_array(
                plan.controls.get("momentum", current_dynamics.momentum),
                current_dynamics.size,
                name="momentum",
            )
            effective_batch = float(
                plan.controls.get("effective_batch", current_dynamics.effective_batch)
            )
            threshold = np.maximum(
                2.0 * (1.0 + momentum) - self.safety_offset, 1e-12
            )
            utilization = step * funnel.upper / threshold
            maximum_utilization = max(maximum_utilization, float(np.max(utilization)))
            if np.any(utilization >= 1.0):
                return False, {
                    "sharpness_rollout_feasible": False,
                    "sharpness_failure": "upper_funnel_crosses_edge",
                    "sharpness_failure_step": index,
                    "sharpness_max_edge_utilization": maximum_utilization,
                }
            funnel = self.sharpness_model.predict_step(
                funnel,
                step_size=step,
                momentum=momentum,
                progress_signal=signal,
            )
            maximum_width = max(maximum_width, float(np.max(funnel.relative_width)))
            if maximum_width > self.max_relative_funnel_width:
                return False, {
                    "sharpness_rollout_feasible": False,
                    "sharpness_failure": "funnel_too_wide",
                    "sharpness_failure_step": index,
                    "sharpness_max_relative_width": maximum_width,
                }
            if self.freeze_on_inadequacy and not np.all(funnel.adequate):
                return False, {
                    "sharpness_rollout_feasible": False,
                    "sharpness_failure": "future_model_inadequate",
                    "sharpness_failure_step": index,
                }
            next_variance = plan.predicted_variance
            lag = plan.predicted.contraction * current_dynamics.variance
            current_observation = self._synthetic_observation(
                current_observation,
                funnel=funnel,
                variance=next_variance,
                previous_variance=current_dynamics.variance,
                lag_covariance=lag,
                step_size=step,
                momentum=momentum,
                effective_batch=effective_batch,
            )
        return True, {
            "sharpness_rollout_feasible": True,
            "sharpness_rollout_steps": maximum_steps,
            "sharpness_max_relative_width": maximum_width,
            "sharpness_max_edge_utilization": maximum_utilization,
            "sharpness_max_projection_error": maximum_projection_error,
            "sharpness_model": funnel.model_name,
        }

    def choose(
        self,
        *,
        state: ChannelState,
        observation: ChannelObservation,
        realize: Callable[[GaussianTransition, ChannelObservation], ActuationPlan],
    ) -> PlannerDecision:
        if observation.local_dynamics is None:
            raise ValueError("sharpness-aware planner requires local_dynamics.")
        initial = self._initial_funnel(observation)
        if self.freeze_on_inadequacy and not np.all(initial.adequate):
            held = self.hold(state=state, observation=observation, realize=realize)
            return replace(
                held,
                diagnostics={
                    **held.diagnostics,
                    "planner": "sharpness_aware_reference_bridge",
                    "sharpness_gate": "trust_region_hold",
                    "curvature_confidence": initial.confidence.copy(),
                },
            )

        reference = self.reference_policy.select(observation)
        reference = GaussianTransition(
            contraction=reference.contraction,
            innovation=np.maximum(reference.innovation, self.innovation_floor),
        )
        nominal_horizon = max(
            1,
            self.total_steps if self.remaining_horizon is None else self.remaining_horizon,
        )
        requested_progress = max(
            float(state.progress),
            float(np.clip(1.0 - (nominal_horizon - 1) / self.total_steps, 0.0, 1.0)),
        )
        candidates: list[tuple[int, float, GaussianTransition, ActuationPlan, dict[str, Any]]] = []
        for horizon in self._candidate_horizons(nominal_horizon):
            bridge = LinearGaussianBridgePath(
                start_variance=observation.state.variance,
                terminal_variance=self.terminal_variance,
                horizon_steps=horizon,
                reference_contraction=reference.contraction,
                reference_innovation=reference.innovation,
                labels=observation.state.labels or self.labels,
            )
            exact = bridge.transition_at(0)
            probe_decision = self.probe_policy.apply(
                desired=exact, observation=observation, state=state
            )
            desired = probe_decision.transition
            assert probe_decision.actuator_transition is not None
            plan = _attach_probe_controls(
                realize(probe_decision.actuator_transition, observation),
                probe_decision,
                current_variance=observation.state.variance,
            )
            rollout_feasible, rollout_diagnostics = self._rollout_candidate(
                bridge=bridge,
                horizon=horizon,
                observation=observation,
                realize=realize,
                first_desired=desired,
                first_plan=plan,
            )
            progress = max(
                float(state.progress),
                float(np.clip(1.0 - (horizon - 1) / self.total_steps, 0.0, 1.0)),
            )
            diagnostics = {
                "planner": "sharpness_aware_reference_bridge",
                "candidate_horizon": horizon,
                "nominal_horizon": nominal_horizon,
                "reference_contraction": reference.contraction.copy(),
                "reference_innovation": reference.innovation.copy(),
                "probe_innovation": probe_decision.innovation.copy(),
                "probe_signal": probe_decision.signal.copy(),
                **dict(probe_decision.diagnostics),
                **rollout_diagnostics,
                "reference_consistent": True,
            }
            candidates.append((horizon, progress, desired, plan, diagnostics))
            if plan.feasible and rollout_feasible:
                self.pending_horizon = horizon
                return PlannerDecision(
                    requested_progress=requested_progress,
                    accepted_progress=progress,
                    desired=desired,
                    plan=plan,
                    diagnostics={**diagnostics, "horizon_governed": horizon != nominal_horizon},
                )

        selected = min(
            candidates,
            key=lambda item: (
                not bool(item[4].get("sharpness_rollout_feasible", False)),
                float(np.max(np.abs(item[3].error))),
            ),
        )
        horizon, progress, desired, plan, diagnostics = selected
        self.pending_horizon = horizon
        return PlannerDecision(
            requested_progress=requested_progress,
            accepted_progress=(progress if self.permit_approximate_progress else float(state.progress)),
            desired=desired,
            plan=plan,
            diagnostics={
                **diagnostics,
                "horizon_governed": True,
                "no_robustly_feasible_horizon": True,
            },
        )

    def reset(self) -> None:
        ReferenceBridgePlanner.reset(self)
        reset = getattr(self.sharpness_model, "reset", None)
        if callable(reset):
            reset()

    def state_dict(self) -> dict[str, Any]:
        state = ReferenceBridgePlanner.state_dict(self)
        state["type"] = "sharpness_aware_reference_bridge_planner"
        getter = getattr(self.sharpness_model, "state_dict", None)
        if callable(getter):
            state["sharpness_model"] = getter()
        return state

    def load_state_dict(self, state: dict[str, Any]) -> None:
        ReferenceBridgePlanner.load_state_dict(self, state)
        model_state = state.get("sharpness_model")
        loader = getattr(self.sharpness_model, "load_state_dict", None)
        if model_state is not None and callable(loader):
            loader(model_state)

