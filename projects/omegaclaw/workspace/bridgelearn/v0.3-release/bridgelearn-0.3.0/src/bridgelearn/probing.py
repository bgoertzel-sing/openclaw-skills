"""Bounded dual-control probing policies.

White innovation can lift a signal above measurement noise, but it does not
repair the weak ``(1,-1)`` regressor direction of a cold AR(2) process.  v0.3
therefore adds an order-2 antithetic probe: ``+delta`` followed by ``-delta``.
It is pairwise mean-zero, concentrates power at the Nyquist frequency, and
budgets the predicted *realized* width perturbation rather than raw amplitude.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterator, Mapping, Protocol

import numpy as np
import numpy.typing as npt

from .types import ChannelObservation, ChannelState, FloatArray, GaussianTransition, broadcast_array


@dataclass(frozen=True, slots=True)
class ProbeDecision:
    """Result of a probe policy.

    ``transition`` is the total desired transition after probing.
    ``actuator_transition`` is what the ordinary actuator should realize before
    an explicit probe signal is injected.  For white probes they are identical;
    for antithetic probes the explicit signal realizes ``external_innovation``
    and must not be purchased a second time through batch/noise control.

    Iteration yields ``(transition, innovation)`` for backward-compatible tuple
    unpacking used by v0.2 code.
    """

    transition: GaussianTransition
    innovation: FloatArray
    signal: FloatArray
    diagnostics: Mapping[str, Any] = field(default_factory=dict)
    actuator_transition: GaussianTransition | None = None
    external_innovation: FloatArray | None = None

    def __post_init__(self) -> None:
        innovation = broadcast_array(
            self.innovation, self.transition.size, name="probe_innovation"
        )
        signal = broadcast_array(self.signal, self.transition.size, name="probe_signal")
        actuator = self.transition if self.actuator_transition is None else self.actuator_transition
        if actuator.size != self.transition.size:
            raise ValueError("probe actuator and total transitions must have matching sizes.")
        external = (
            np.zeros(self.transition.size, dtype=np.float64)
            if self.external_innovation is None
            else broadcast_array(
                self.external_innovation,
                self.transition.size,
                name="external_innovation",
            )
        )
        if np.any(external < 0.0):
            raise ValueError("external probe innovation must be non-negative.")
        object.__setattr__(self, "innovation", innovation)
        object.__setattr__(self, "signal", signal)
        object.__setattr__(self, "actuator_transition", actuator)
        object.__setattr__(self, "external_innovation", external)

    def __iter__(self) -> Iterator[Any]:
        yield self.transition
        yield self.innovation


class ProbePolicy(Protocol):
    def apply(
        self,
        *,
        desired: GaussianTransition,
        observation: ChannelObservation,
        state: ChannelState,
    ) -> ProbeDecision:
        ...


@dataclass(frozen=True, slots=True)
class NoProbePolicy:
    def apply(
        self,
        *,
        desired: GaussianTransition,
        observation: ChannelObservation,
        state: ChannelState,
    ) -> ProbeDecision:
        zero = np.zeros(desired.size, dtype=np.float64)
        return ProbeDecision(desired, zero, zero, {"probe_type": "none"})


@dataclass(frozen=True, slots=True)
class ConfidenceProbePolicy:
    """Add bounded white innovation under low confidence and low active width."""

    confidence_threshold: float = 0.35
    cold_variance: float | np.ndarray = 0.01
    max_probe_innovation: float | np.ndarray = 1e-4
    max_total_probe: float | np.ndarray = np.inf
    power: float = 2.0

    def __post_init__(self) -> None:
        if not 0.0 < self.confidence_threshold <= 1.0:
            raise ValueError("confidence_threshold must lie in (0, 1].")
        if self.power <= 0.0:
            raise ValueError("power must be positive.")

    def apply(
        self,
        *,
        desired: GaussianTransition,
        observation: ChannelObservation,
        state: ChannelState,
    ) -> ProbeDecision:
        size = desired.size
        cold = broadcast_array(self.cold_variance, size, name="cold_variance")
        maximum = broadcast_array(
            self.max_probe_innovation, size, name="max_probe_innovation"
        )
        total = broadcast_array(self.max_total_probe, size, name="max_total_probe")
        if np.any(cold <= 0.0) or np.any(maximum < 0.0) or np.any(total < 0.0):
            raise ValueError("probe scales must be non-negative and cold_variance positive.")
        confidence_deficit = np.clip(
            (self.confidence_threshold - observation.state.confidence)
            / self.confidence_threshold,
            0.0,
            1.0,
        )
        cold_factor = np.clip(
            (cold - observation.state.variance) / cold,
            0.0,
            1.0,
        )
        proposal = maximum * (confidence_deficit * cold_factor) ** self.power
        spent = (
            np.zeros(size, dtype=np.float64)
            if state.cumulative_probe_innovation is None
            else broadcast_array(
                state.cumulative_probe_innovation, size, name="cumulative_probe_innovation"
            )
        )
        probe = np.minimum(proposal, np.maximum(total - spent, 0.0))
        zero = np.zeros(size, dtype=np.float64)
        return ProbeDecision(
            transition=GaussianTransition(
                contraction=desired.contraction,
                innovation=desired.innovation + probe,
            ),
            innovation=probe,
            signal=zero,
            diagnostics={
                "probe_type": "white",
                "probe_active_fraction": float(np.mean(probe > 0.0)),
            },
        )


@dataclass(slots=True)
class AntitheticProbePolicy:
    """Persistent-excitation probe for momentum/AR(2) identification.

    The probe is emitted as an *exact committed pair*: ``+delta`` on one
    applied command and ``-delta`` on the next.  Once the first pulse commits,
    the second pulse is completed with the same amplitude even if confidence
    improves in the meantime.  This preserves pairwise zero mean and prevents
    the centering observer from reclassifying an incomplete probe as drift.

    Activation is driven by uncertainty in ``c1-c2`` or by the condition number
    of the AR(2) regressor moment matrix.  Expected metadata keys are
    ``contrast_standard_error`` (or ``ar2_contrast_standard_error``),
    ``regressor_condition`` (or ``ar2_regressor_condition``), and optionally
    ``lyapunov_condition``.  ``c1`` and ``c2`` are used to translate a raw
    Nyquist-frequency innovation into its predicted realized width cost.

    ``amplitude_levels`` cycles over completed pairs.  The default two levels
    provide the two-amplitude antithetic experiment needed to detect local
    response curvature without abandoning the order-2 excitation pattern.
    Values are relative multipliers and are normalized by their maximum, so the
    largest level respects ``max_realized_variance``.

    ``max_realized_variance`` is a per-pulse width budget before the conservative
    ``sqrt(kappa_P)`` deflation.  A newly started pair reserves budget for both
    pulses.  Raw probe innovation is selected as

        raw = realized_budget * |1 + c1 - c2|**2 / sqrt(kappa_P),

    and the explicit signal is ``+sqrt(raw), -sqrt(raw)``.
    """

    contrast_se_threshold: float = 0.05
    condition_threshold: float = 1e3
    confidence_threshold: float = 0.35
    cold_variance: float | npt.ArrayLike = 0.01
    max_realized_variance: float | npt.ArrayLike = 1e-4
    max_total_realized_variance: float | npt.ArrayLike = 1e30
    amplitude_levels: tuple[float, ...] = (0.5, 1.0)
    power: float = 1.0
    signal_control_name: str = "probe_signal"
    _pair_raw_innovation: FloatArray | None = field(default=None, init=False, repr=False)
    _pair_realized_cost: FloatArray | None = field(default=None, init=False, repr=False)
    _candidate_raw_innovation: FloatArray | None = field(default=None, init=False, repr=False)
    _candidate_realized_cost: FloatArray | None = field(default=None, init=False, repr=False)
    _candidate_completes_pair: bool = field(default=False, init=False, repr=False)
    _level_index: int = field(default=0, init=False, repr=False)

    def __post_init__(self) -> None:
        if self.contrast_se_threshold <= 0.0:
            raise ValueError("contrast_se_threshold must be positive.")
        if self.condition_threshold <= 1.0:
            raise ValueError("condition_threshold must exceed one.")
        if not 0.0 < self.confidence_threshold <= 1.0:
            raise ValueError("confidence_threshold must lie in (0,1].")
        if self.power <= 0.0:
            raise ValueError("power must be positive.")
        if not self.amplitude_levels or any(level <= 0.0 for level in self.amplitude_levels):
            raise ValueError("amplitude_levels must contain positive values.")

    def _metadata_array(
        self,
        metadata: Mapping[str, Any],
        names: tuple[str, ...],
        size: int,
        default: float,
    ) -> FloatArray:
        for name in names:
            if name in metadata:
                return broadcast_array(metadata[name], size, name=name)
        return np.full(size, default, dtype=np.float64)

    def _completion_decision(
        self,
        *,
        desired: GaussianTransition,
    ) -> ProbeDecision:
        assert self._pair_raw_innovation is not None
        assert self._pair_realized_cost is not None
        raw = self._pair_raw_innovation.copy()
        realized = self._pair_realized_cost.copy()
        signal = -np.sqrt(np.maximum(raw, 0.0))
        self._candidate_raw_innovation = raw
        self._candidate_realized_cost = realized
        self._candidate_completes_pair = True
        return ProbeDecision(
            transition=GaussianTransition(
                contraction=desired.contraction,
                innovation=desired.innovation + raw,
            ),
            innovation=realized,
            signal=signal,
            diagnostics={
                "probe_type": "antithetic_order2",
                "probe_signal_control_name": self.signal_control_name,
                "probe_pair_completion": True,
                "probe_active_fraction": float(np.mean(raw > 0.0)),
                "probe_raw_innovation": raw,
                "probe_realized_variance_budget": realized,
                "probe_phase": -np.ones(raw.size, dtype=np.float64),
                "probe_amplitude_level_index": self._level_index,
            },
            actuator_transition=desired,
            external_innovation=raw,
        )

    def apply(
        self,
        *,
        desired: GaussianTransition,
        observation: ChannelObservation,
        state: ChannelState,
    ) -> ProbeDecision:
        size = desired.size
        if self._pair_raw_innovation is not None:
            if self._pair_raw_innovation.size != size:
                raise ValueError("antithetic probe block count changed.")
            return self._completion_decision(desired=desired)

        cold = broadcast_array(self.cold_variance, size, name="cold_variance")
        maximum = broadcast_array(
            self.max_realized_variance, size, name="max_realized_variance"
        )
        total = broadcast_array(
            self.max_total_realized_variance, size, name="max_total_realized_variance"
        )
        if np.any(cold <= 0.0) or np.any(maximum < 0.0) or np.any(total < 0.0):
            raise ValueError(
                "probe scales must be non-negative and cold_variance positive."
            )

        contrast_se = self._metadata_array(
            observation.metadata,
            ("contrast_standard_error", "ar2_contrast_standard_error"),
            size,
            0.0,
        )
        condition = self._metadata_array(
            observation.metadata,
            ("regressor_condition", "ar2_regressor_condition"),
            size,
            1.0,
        )
        kappa = self._metadata_array(
            observation.metadata,
            ("lyapunov_condition", "companion_lyapunov_condition"),
            size,
            1.0,
        )
        c1 = self._metadata_array(observation.metadata, ("c1", "ar2_c1"), size, 0.0)
        c2 = self._metadata_array(observation.metadata, ("c2", "ar2_c2"), size, 0.0)

        uncertainty = np.maximum(
            contrast_se / self.contrast_se_threshold,
            np.sqrt(np.maximum(condition / self.condition_threshold, 0.0)),
        )
        confidence_deficit = np.clip(
            (self.confidence_threshold - observation.state.confidence)
            / self.confidence_threshold,
            0.0,
            1.0,
        )
        activation = np.clip(
            np.maximum(uncertainty - 1.0, confidence_deficit), 0.0, 1.0
        )
        cold_factor = np.clip(
            (cold - observation.state.variance) / np.maximum(cold, 1e-30),
            0.0,
            1.0,
        )

        levels = np.asarray(self.amplitude_levels, dtype=np.float64)
        level_scale = float(levels[self._level_index % levels.size] / np.max(levels))
        requested_per_pulse = (
            maximum * level_scale**2 * (activation * cold_factor) ** self.power
        )
        spent = (
            np.zeros(size, dtype=np.float64)
            if state.cumulative_probe_innovation is None
            else broadcast_array(
                state.cumulative_probe_innovation,
                size,
                name="cumulative_probe_innovation",
            )
        )
        # Reserve the same amount for the required second pulse.
        remaining_per_pulse = np.maximum(total - spent, 0.0) / 2.0
        declared_realized = np.minimum(requested_per_pulse, remaining_per_pulse)
        transfer_denominator = np.maximum(
            np.abs(1.0 + c1 - c2) ** 2, 1e-12
        )
        raw_innovation = (
            declared_realized
            * transfer_denominator
            / np.sqrt(np.maximum(kappa, 1.0))
        )
        signal = np.sqrt(np.maximum(raw_innovation, 0.0))
        conservative_realized = raw_innovation / transfer_denominator

        self._candidate_raw_innovation = raw_innovation.copy()
        self._candidate_realized_cost = conservative_realized.copy()
        self._candidate_completes_pair = False
        return ProbeDecision(
            transition=GaussianTransition(
                contraction=desired.contraction,
                innovation=desired.innovation + raw_innovation,
            ),
            innovation=conservative_realized,
            signal=signal,
            diagnostics={
                "probe_type": "antithetic_order2",
                "probe_signal_control_name": self.signal_control_name,
                "probe_pair_completion": False,
                "probe_active_fraction": float(np.mean(raw_innovation > 0.0)),
                "probe_raw_innovation": raw_innovation,
                "probe_realized_variance_budget": conservative_realized,
                "probe_declared_preconditioning_budget": declared_realized,
                "probe_transfer_denominator": transfer_denominator,
                "probe_phase": np.ones(size, dtype=np.float64),
                "probe_amplitude_level": level_scale,
                "probe_amplitude_level_index": self._level_index,
                "probe_condition_trigger_fraction": float(
                    np.mean(condition >= self.condition_threshold)
                ),
                "probe_contrast_trigger_fraction": float(
                    np.mean(contrast_se >= self.contrast_se_threshold)
                ),
            },
            actuator_transition=desired,
            external_innovation=raw_innovation,
        )

    def commit(self, _command: Any | None = None) -> None:
        """Commit the planned pulse and maintain exact pair state."""

        if self._candidate_raw_innovation is None:
            return
        if self._candidate_completes_pair:
            self._pair_raw_innovation = None
            self._pair_realized_cost = None
            self._level_index = (self._level_index + 1) % len(self.amplitude_levels)
        elif np.any(self._candidate_raw_innovation > 0.0):
            self._pair_raw_innovation = self._candidate_raw_innovation.copy()
            assert self._candidate_realized_cost is not None
            self._pair_realized_cost = self._candidate_realized_cost.copy()
        self._candidate_raw_innovation = None
        self._candidate_realized_cost = None
        self._candidate_completes_pair = False

    def reset(self) -> None:
        self._pair_raw_innovation = None
        self._pair_realized_cost = None
        self._candidate_raw_innovation = None
        self._candidate_realized_cost = None
        self._candidate_completes_pair = False
        self._level_index = 0

    def state_dict(self) -> dict[str, Any]:
        return {
            "type": "antithetic_order2",
            "pair_raw_innovation": (
                None
                if self._pair_raw_innovation is None
                else self._pair_raw_innovation.tolist()
            ),
            "pair_realized_cost": (
                None
                if self._pair_realized_cost is None
                else self._pair_realized_cost.tolist()
            ),
            "level_index": self._level_index,
        }

    def load_state_dict(self, state: Mapping[str, Any]) -> None:
        raw = state.get("pair_raw_innovation")
        realized = state.get("pair_realized_cost")
        self._pair_raw_innovation = (
            None if raw is None else np.asarray(raw, dtype=np.float64)
        )
        self._pair_realized_cost = (
            None if realized is None else np.asarray(realized, dtype=np.float64)
        )
        if (self._pair_raw_innovation is None) != (self._pair_realized_cost is None):
            raise ValueError("probe checkpoint contains an incomplete pair state.")
        self._level_index = int(state.get("level_index", 0)) % len(
            self.amplitude_levels
        )
        self._candidate_raw_innovation = None
        self._candidate_realized_cost = None
        self._candidate_completes_pair = False

