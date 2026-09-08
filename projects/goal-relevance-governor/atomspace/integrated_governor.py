#!/usr/bin/env python3
"""Integrated Governor Pipeline v0.1
====================================

Ties together PLN propagation, ECAN attention allocation, and the
PLN-Verdict Bridge into a single unified pipeline.

Flow:
  Graph Data
    → PLNPropagator (continuous relevance + truth values)
    → ECANAttentionAllocator (STI/LTI attention dynamics)
    → PLNVerdictBridge (rule + PLN fusion → unified verdicts)
    → IntegratedGovernorResult (unified output)

The pipeline produces a single JSON document that combines:
  1. PLN relevance scores and truth values for all tasks
  2. ECAN attention map with priority queue and eviction candidates
  3. Unified verdicts with temporal staleness and confidence modifiers
  4. Executive summary with top-priority tasks and recommended actions
"""

from __future__ import annotations
import json
from dataclasses import dataclass, field, asdict
from typing import Optional
import sys
import os
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'evaluator'))

from pln_propagation import PLNPropagator, TruthValue
from ecan_attention import ECANAttentionAllocator
from pln_verdict_bridge import PLNVerdictBridge


@dataclass
class TaskRecommendation:
    """Actionable recommendation for a single task."""
    task_id: str
    unified_verdict: str
    relevance_score: float
    priority_band: str
    sti: float
    lti: float
    eviction_candidate: bool
    staleness_flag: bool
    confidence_modifier: float
    signals: list
    recommended_action: str

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class IntegratedGovernorResult:
    """Unified output from the integrated governor pipeline."""
    timestamp: str
    episode_id: str
    cycle: int

    # PLN layer
    pln_task_count: int
    pln_total_relevance: float

    # ECAN layer
    ecan_total_sti: float
    ecan_eviction_count: int
    ecan_priority_top3: list

    # Verdict layer
    verdict_counts: dict

    # Recommendations
    recommendations: list
    executive_summary: str

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "episode_id": self.episode_id,
            "cycle": self.cycle,
            "pln_layer": {
                "task_count": self.pln_task_count,
                "total_relevance": round(self.pln_total_relevance, 4),
            },
            "ecan_layer": {
                "total_sti": round(self.ecan_total_sti, 2),
                "eviction_count": self.ecan_eviction_count,
                "priority_top3": self.ecan_priority_top3,
            },
            "verdict_layer": {
                "verdict_counts": self.verdict_counts,
            },
            "recommendations": [r.to_dict() for r in self.recommendations],
            "executive_summary": self.executive_summary,
        }


# Action mapping: verdict → human-readable action
ACTION_MAP = {
    "CONTINUE": "Proceed with current task as planned.",
    "PAUSE_RECOVERABLY": "Pause task — it may recover. Re-evaluate after addressing blockers.",
    "DEFER": "Defer this task in favor of higher-priority work.",
    "REPLAN": "Replan: the task approach needs revision before proceeding.",
    "STOP_STALE": "Stop: goal is stale and no longer relevant. Consider abandoning.",
    "ESCALATE": "Escalate: this task blocks critical goals. Prioritize immediately.",
    "BLOCKED": "Task is blocked. Resolve the blocking dependency first.",
}


class IntegratedGovernorPipeline:
    """Unified pipeline: PLN → ECAN → Verdict Bridge.

    Usage:
        pipeline = IntegratedGovernorPipeline(data)
        result = pipeline.run(ecan_cycles=10)
        print(result.executive_summary)
    """

    def __init__(self, data: dict, now: Optional[datetime] = None):
        self.data = data
        # Default 'now' to the episode's frozen_at timestamp for realistic
        # staleness detection during replay. Falls back to current time.
        if now is None:
            frozen_at = data.get("frozen_at")
            if frozen_at:
                self.now = datetime.fromisoformat(frozen_at.replace("Z", "+00:00"))
            else:
                self.now = datetime.now(timezone.utc)
        else:
            self.now = now

        # Layer 1: PLN propagation
        self.propagator = PLNPropagator(data)
        self.pln_result = self.propagator.evaluate()

        # Layer 2: ECAN attention
        self.allocator = ECANAttentionAllocator(data)

        # Layer 3: Verdict bridge
        self.bridge = PLNVerdictBridge(data, now=self.now)

    def run(self, ecan_cycles: int = 10) -> IntegratedGovernorResult:
        """Run the full pipeline and produce unified output."""

        # Run ECAN dynamics
        ecan_result = self.allocator.run(cycles=ecan_cycles)
        ecan_dict = ecan_result.to_dict()

        # Run verdict bridge
        bridge_results = self.bridge.evaluate()

        # Build recommendations by combining all layers
        recommendations = []
        verdict_counts = {}

        for r in bridge_results:
            # Get ECAN attention for this task
            av = self.allocator.attention.get(r.task_id)
            sti = av.sti if av else 0.0
            lti = av.lti if av else 0.0
            eviction = av.eviction_candidate if av else False

            action = ACTION_MAP.get(r.unified_verdict, "No specific action.")

            rec = TaskRecommendation(
                task_id=r.task_id,
                unified_verdict=r.unified_verdict,
                relevance_score=r.relevance_score,
                priority_band=r.priority_band,
                sti=round(sti, 2),
                lti=round(lti, 2),
                eviction_candidate=eviction,
                staleness_flag=r.staleness_flag,
                confidence_modifier=r.confidence_modifier,
                signals=r.signals,
                recommended_action=action,
            )
            recommendations.append(rec)

            verdict_counts[r.unified_verdict] = verdict_counts.get(r.unified_verdict, 0) + 1

        # Sort recommendations by STI (highest first)
        recommendations.sort(key=lambda x: x.sti, reverse=True)

        # Executive summary
        summary = self._build_summary(
            recommendations, verdict_counts, ecan_dict
        )

        # Top 3 priority from ECAN
        top3 = ecan_dict["priority_queue"][:3]

        return IntegratedGovernorResult(
            timestamp=self.now.isoformat(),
            episode_id=self.data.get("episode_id", "unknown"),
            cycle=ecan_cycles,
            pln_task_count=len(self.pln_result.get("tasks", [])),
            pln_total_relevance=sum(
                t.get("relevance_score", 0.0)
                for t in self.pln_result.get("tasks", [])
            ),
            ecan_total_sti=ecan_dict["total_sti"],
            ecan_eviction_count=ecan_dict["eviction_candidates"].__len__(),
            ecan_priority_top3=top3,
            verdict_counts=verdict_counts,
            recommendations=recommendations,
            executive_summary=summary,
        )

    def _build_summary(self, recs: list, verdict_counts: dict, ecan_dict: dict) -> str:
        """Build a human-readable executive summary."""
        lines = []
        lines.append(f"Pipeline evaluated {len(recs)} tasks.")

        # Verdict distribution
        verdict_str = ", ".join(f"{k}={v}" for k, v in sorted(verdict_counts.items()))
        lines.append(f"Verdict distribution: {verdict_str}")

        # Top priority task
        if recs:
            top = recs[0]
            lines.append(
                f"Top priority: {top.task_id} "
                f"(STI={top.sti:.1f}, {top.unified_verdict}, "
                f"rel={top.relevance_score:.3f})"
            )

        # Eviction candidates
        evictions = [r for r in recs if r.eviction_candidate]
        if evictions:
            ev_names = ", ".join(r.task_id for r in evictions)
            lines.append(f"Eviction candidates: {ev_names}")

        # Stale tasks
        stale = [r for r in recs if r.staleness_flag]
        if stale:
            stale_names = ", ".join(r.task_id for r in stale)
            lines.append(f"Stale tasks: {stale_names}")

        # Escalation needed
        escalations = [r for r in recs if r.unified_verdict == "ESCALATE"]
        if escalations:
            esc_names = ", ".join(r.task_id for r in escalations)
            lines.append(f"⚠ ESCALATE: {esc_names}")

        return " | ".join(lines)

    def run_to_json(self, ecan_cycles: int = 10) -> str:
        """Run pipeline and return JSON."""
        result = self.run(ecan_cycles=ecan_cycles)
        return json.dumps(result.to_dict(), indent=2)


if __name__ == "__main__":
    import sys
    data = json.load(open(sys.argv[1]))
    pipeline = IntegratedGovernorPipeline(data)
    print(pipeline.run_to_json())
