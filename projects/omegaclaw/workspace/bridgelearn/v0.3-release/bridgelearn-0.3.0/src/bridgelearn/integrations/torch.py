"""Optional PyTorch optimizer integration.

v0.3 supports a companion-aware momentum actuator when lag covariance is
reported.  First-order AR(1) deployment remains available only behind an
explicit adequacy gate.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Mapping

import numpy as np
import numpy.typing as npt

from ..actuators import MomentumStepBatchActuator, StepBatchActuator, TransitionActuator
from ..types import (
    ActuationPlan,
    ChannelObservation,
    ControlCommand,
    GaussianTransition,
    LocalDynamics,
    as_float_array,
    broadcast_array,
)


@dataclass(frozen=True, slots=True)
class TorchGroupStatistics:
    variance: npt.ArrayLike
    curvature: npt.ArrayLike
    noise_scale: npt.ArrayLike
    effective_batch: float
    confidence: npt.ArrayLike | float = 1.0
    labels: tuple[str, ...] = ()
    curvature_slope: npt.ArrayLike | float = 0.0
    trust_region_step: npt.ArrayLike | float = 1e30
    ar1_adequacy: npt.ArrayLike | float | None = None
    structural_adequacy: npt.ArrayLike | float | None = None
    momentum: npt.ArrayLike | float | None = None
    previous_variance: npt.ArrayLike | float | None = None
    lag_covariance: npt.ArrayLike | float | None = None
    curvature_lower: npt.ArrayLike | float | None = None
    curvature_upper: npt.ArrayLike | float | None = None
    curvature_adequacy: npt.ArrayLike | float = 1.0
    coefficient_slew_limit: npt.ArrayLike | float = 1e30
    contrast_standard_error: npt.ArrayLike | float | None = None
    regressor_condition: npt.ArrayLike | float | None = None
    lyapunov_condition: npt.ArrayLike | float | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


class TorchOptimizerAdapter:
    """Bridge adapter for a ``torch.optim.Optimizer``.

    One bridge block is associated with each optimizer parameter group.  For
    momentum or Adam-like optimizers, a structural adequacy score is required
    by default. Prefer ``TorchGroupStatistics.structural_adequacy`` from the
    gray-box-versus-black-box diagnostic; ``ar1_adequacy`` remains a backwards-
    compatible first-order gate.
    """

    def __init__(
        self,
        *,
        optimizer: Any,
        statistics: Callable[[Any], TorchGroupStatistics],
        set_effective_batch: Callable[[Any, float], None] | None = None,
        actuator: TransitionActuator | None = None,
        lr_key: str = "lr",
        require_ar1_diagnostic: bool = True,
        require_structural_diagnostic: bool | None = None,
        allow_first_order_momentum: bool = False,
        allow_beta1_control: bool = False,
        apply_probe_signal: Callable[[Any, npt.ArrayLike], None] | None = None,
    ) -> None:
        self.optimizer = optimizer
        self.statistics = statistics
        self.set_effective_batch = set_effective_batch
        self.actuator = actuator or StepBatchActuator()
        self.lr_key = lr_key
        self.require_ar1_diagnostic = require_ar1_diagnostic
        self.require_structural_diagnostic = (
            require_ar1_diagnostic
            if require_structural_diagnostic is None
            else bool(require_structural_diagnostic)
        )
        self.allow_first_order_momentum = allow_first_order_momentum
        self.allow_beta1_control = allow_beta1_control
        self.apply_probe_signal = apply_probe_signal

    def _group_momenta(self) -> np.ndarray:
        values: list[float] = []
        for group in self.optimizer.param_groups:
            if "momentum" in group:
                values.append(float(group.get("momentum", 0.0)))
            elif group.get("betas") is not None:
                values.append(float(group["betas"][0]))
            else:
                values.append(0.0)
        return np.asarray(values, dtype=np.float64)

    def _momentum_present(self) -> bool:
        for group in self.optimizer.param_groups:
            if float(group.get("momentum", 0.0)) > 0.0:
                return True
            betas = group.get("betas")
            if betas is not None and float(betas[0]) > 0.0:
                return True
        return False

    def observe(self, context: Any) -> ChannelObservation:
        stats = self.statistics(context)
        group_count = len(self.optimizer.param_groups)
        step_sizes = np.asarray(
            [float(group[self.lr_key]) for group in self.optimizer.param_groups],
            dtype=np.float64,
        )
        labels = stats.labels or tuple(
            str(group.get("name", f"group_{index}"))
            for index, group in enumerate(self.optimizer.param_groups)
        )
        momentum_present = self._momentum_present()
        companion_mode = isinstance(self.actuator, MomentumStepBatchActuator)
        adequacy_source = (
            stats.structural_adequacy
            if stats.structural_adequacy is not None
            else stats.ar1_adequacy
        )
        if adequacy_source is None:
            if (
                momentum_present
                and self.require_structural_diagnostic
                and not self.allow_first_order_momentum
            ):
                raise RuntimeError(
                    "momentum/Adam dynamics detected, but no structural adequacy "
                    "score was supplied. Use the gray-box/AR(2) observers and pass "
                    "TorchGroupStatistics.structural_adequacy, or explicitly opt "
                    "into an unvalidated approximation."
                )
            adequacy = np.ones(group_count, dtype=np.float64)
        else:
            adequacy = broadcast_array(
                adequacy_source, group_count, name="structural_adequacy"
            )
        inferred_momentum = self._group_momenta()
        momentum = (
            inferred_momentum
            if stats.momentum is None
            else broadcast_array(stats.momentum, group_count, name="momentum")
        )
        if companion_mode and momentum_present and (
            stats.previous_variance is None or stats.lag_covariance is None
        ):
            raise RuntimeError(
                "MomentumStepBatchActuator requires previous_variance and lag_covariance "
                "for every optimizer group."
            )
        dynamics = LocalDynamics(
            variance=broadcast_array(stats.variance, group_count, name="variance"),
            curvature=broadcast_array(stats.curvature, group_count, name="curvature"),
            noise_scale=broadcast_array(stats.noise_scale, group_count, name="noise_scale"),
            step_size=step_sizes,
            effective_batch=float(stats.effective_batch),
            confidence=broadcast_array(stats.confidence, group_count, name="confidence"),
            labels=labels,
            curvature_slope=broadcast_array(
                stats.curvature_slope, group_count, name="curvature_slope"
            ),
            trust_region_step=broadcast_array(
                stats.trust_region_step, group_count, name="trust_region_step"
            ),
            ar1_adequacy=(
                adequacy if stats.ar1_adequacy is not None else np.ones(group_count)
            ),
            structural_adequacy=adequacy,
            momentum=momentum,
            previous_variance=stats.previous_variance,
            lag_covariance=stats.lag_covariance,
            curvature_lower=stats.curvature_lower,
            curvature_upper=stats.curvature_upper,
            curvature_adequacy=broadcast_array(
                stats.curvature_adequacy, group_count, name="curvature_adequacy"
            ),
            coefficient_slew_limit=broadcast_array(
                stats.coefficient_slew_limit, group_count, name="coefficient_slew_limit"
            ),
        )
        current_c1, current_c2 = dynamics.companion_coefficients_at(
            dynamics.step_size
        )
        return ChannelObservation(
            state=dynamics.state(),
            reference=dynamics.reference_transition(),
            local_dynamics=dynamics,
            payload=stats,
            metadata={
                "momentum_present": momentum_present,
                "ar1_diagnostic_supplied": stats.ar1_adequacy is not None,
                "structural_diagnostic_supplied": adequacy_source is not None,
                "reference_source": "current_command",
                "companion_mode": companion_mode,
                "c1": current_c1.copy(),
                "c2": current_c2.copy(),
                **(
                    {}
                    if stats.contrast_standard_error is None
                    else {
                        "contrast_standard_error": broadcast_array(
                            stats.contrast_standard_error,
                            group_count,
                            name="contrast_standard_error",
                        )
                    }
                ),
                **(
                    {}
                    if stats.regressor_condition is None
                    else {
                        "regressor_condition": broadcast_array(
                            stats.regressor_condition,
                            group_count,
                            name="regressor_condition",
                        )
                    }
                ),
                **(
                    {}
                    if stats.lyapunov_condition is None
                    else {
                        "lyapunov_condition": broadcast_array(
                            stats.lyapunov_condition,
                            group_count,
                            name="lyapunov_condition",
                        )
                    }
                ),
                **dict(stats.metadata),
            },
        )

    def realize(
        self,
        *,
        target: GaussianTransition,
        observation: ChannelObservation,
    ) -> ActuationPlan:
        return self.actuator.realize(target=target, observation=observation)

    def apply(self, context: Any, command: ControlCommand) -> None:
        step_sizes = as_float_array(command.controls["step_size"], name="step_size")
        if step_sizes.size != len(self.optimizer.param_groups):
            raise ValueError("step-size command does not match optimizer groups.")
        for group, step_size in zip(self.optimizer.param_groups, step_sizes, strict=True):
            group[self.lr_key] = float(step_size)
        if "momentum" in command.controls:
            momenta = as_float_array(command.controls["momentum"], name="momentum")
            if momenta.size != len(self.optimizer.param_groups):
                raise ValueError("momentum command does not match optimizer groups.")
            for group, momentum in zip(self.optimizer.param_groups, momenta, strict=True):
                if "momentum" in group:
                    group["momentum"] = float(momentum)
                elif group.get("betas") is not None:
                    if not self.allow_beta1_control and not np.isclose(momentum, group["betas"][0]):
                        raise RuntimeError(
                            "controller requested Adam beta1 control; set allow_beta1_control=True "
                            "to permit this explicitly."
                        )
                    beta2 = float(group["betas"][1])
                    group["betas"] = (float(momentum), beta2)
                elif not np.isclose(momentum, 0.0):
                    raise RuntimeError("optimizer group does not expose a momentum control.")
        if "probe_signal" in command.controls:
            if self.apply_probe_signal is None:
                raise RuntimeError(
                    "an antithetic probe was requested but no apply_probe_signal callback was supplied."
                )
            self.apply_probe_signal(context, command.controls["probe_signal"])
        if "effective_batch" in command.controls:
            if self.set_effective_batch is None:
                raise RuntimeError(
                    "command contains effective_batch but no set_effective_batch callback was supplied."
                )
            self.set_effective_batch(context, float(command.controls["effective_batch"]))


def capture_parameter_groups(optimizer: Any) -> list[np.ndarray]:
    arrays: list[np.ndarray] = []
    for group in optimizer.param_groups:
        pieces = []
        for parameter in group["params"]:
            tensor = parameter.detach().reshape(-1).cpu()
            pieces.append(tensor.numpy().astype(np.float64, copy=True))
        arrays.append(np.concatenate(pieces) if pieces else np.empty(0, dtype=np.float64))
    return arrays


def capture_gradient_groups(optimizer: Any) -> list[np.ndarray]:
    arrays: list[np.ndarray] = []
    for group in optimizer.param_groups:
        pieces = []
        for parameter in group["params"]:
            if parameter.grad is None:
                pieces.append(np.zeros(parameter.numel(), dtype=np.float64))
            else:
                tensor = parameter.grad.detach().reshape(-1).cpu()
                pieces.append(tensor.numpy().astype(np.float64, copy=True))
        arrays.append(np.concatenate(pieces) if pieces else np.empty(0, dtype=np.float64))
    return arrays
