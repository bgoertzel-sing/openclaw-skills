"""Non-runnable CAROM integration skeleton for BridgeLearn 0.2.

This file has no dependency on a particular CAROM repository layout. Replace
the callbacks with the corresponding model and telemetry accessors. The
configuration intentionally starts in shadow mode.
"""

from __future__ import annotations

from typing import Any, Callable

import numpy as np

from bridgelearn import (
    BridgeController,
    CallbackReferencePolicy,
    Channel,
    ConfidenceProbePolicy,
    FilteredReferencePolicy,
    GaussianTransition,
    PatienceMetricGuard,
    ReferenceBridgePlanner,
    StepBatchActuator,
)
from bridgelearn.integrations.torch import (
    TorchGroupStatistics,
    TorchOptimizerAdapter,
)


def make_carom_weight_controller(
    *,
    optimizer: Any,
    statistics: Callable[[Any], TorchGroupStatistics],
    set_effective_batch: Callable[[Any, float], None],
    total_updates: int,
    terminal_variance: tuple[float, float, float, float] = (
        0.002,
        0.006,
        0.010,
        0.006,
    ),
    reference_lr: tuple[float, float, float, float] = (
        2.0e-4,
        4.0e-4,
        2.0e-4,
        3.0e-4,
    ),
    reference_batch: float = 128.0,
) -> BridgeController:
    """Create a four-block persistent CAROM weight controller.

    Suggested optimizer groups, in order:

    1. dependency/edge and command-routing parameters;
    2. shared operator core;
    3. GLV inhibition/fatigue/control parameters;
    4. workspace readout and downstream execution parameters.

    The statistics callback must supply ``ar1_adequacy`` for AdamW/momentum
    blocks. Low adequacy lowers confidence; the PyTorch adapter raises when the
    diagnostic is omitted.
    """

    eta_ref = np.asarray(reference_lr, dtype=np.float64)

    def commanded_reference(observation: Any) -> GaussianTransition:
        dynamics = observation.local_dynamics
        if dynamics is None:
            raise RuntimeError("CAROM reference requires local dynamics.")
        curvature = dynamics.curvature_at(eta_ref)
        contraction = 1.0 - eta_ref * curvature
        innovation = eta_ref**2 * dynamics.noise_scale / reference_batch
        return GaussianTransition(
            contraction=contraction,
            innovation=np.maximum(innovation, 1e-12),
        )

    reference_policy = FilteredReferencePolicy(
        alpha=0.03,
        source=CallbackReferencePolicy(commanded_reference).select,
        max_contraction_change=0.01,
        max_log_innovation_change=0.20,
    )

    adapter = TorchOptimizerAdapter(
        optimizer=optimizer,
        statistics=statistics,
        set_effective_batch=set_effective_batch,
        actuator=StepBatchActuator(
            step_bounds=(1e-6, 5e-3),
            batch_bounds=(32, 1024),
            batch_quantum=32,
            compute_reference=128,
            compute_price=0.01,
            resource_deadband=0.08,
            block_weights=[0.5, 1.0, 1.0, 1.5],
            max_log_step_change=0.15,
            max_log_batch_change=0.35,
            edge_of_stability_threshold=1.7,
        ),
        require_ar1_diagnostic=True,
        allow_first_order_momentum=False,
    )

    planner = ReferenceBridgePlanner(
        terminal_variance=terminal_variance,
        total_steps=total_updates,
        reference_policy=reference_policy,
        probe_policy=ConfidenceProbePolicy(
            confidence_threshold=0.40,
            cold_variance=0.01,
            max_probe_innovation=1e-7,
            max_total_probe=1e-5,
        ),
        max_horizon_multiplier=16.0,
        permit_approximate_progress=False,
        labels=("routing", "operators", "glv", "execution"),
    )

    # ``context.fixed_panel_score`` should combine endpoint performance and
    # trajectory evidence. It should not be edge accuracy alone.
    guard = PatienceMetricGuard(
        metric=lambda context: float(context.fixed_panel_score),
        mode="max",
        patience=3,
        relative_tolerance=0.05,
        latched=True,
    )

    return BridgeController(
        {
            "weights": Channel(
                name="weights",
                adapter=adapter,
                planner=planner,
                guard=guard,
            )
        },
        mode="shadow",  # activate only after calibration and adequacy checks
    )
