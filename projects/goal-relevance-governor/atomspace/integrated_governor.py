#!/usr/bin/env python3
"""Integrated Governor Pipeline v0.2
====================================

Ties together PLN propagation, ECAN attention allocation, and the
PLN-Verdict Bridge into a single unified pipeline.

Flow:
  Graph Data
    → PLNPropagator (continuous relevance + truth values)
    → ECANAttentionAllocator (STI/LTI attention dynamics)
    → PLNVerdictBridge (rule + PLN fusion → unified verdicts)
    → [InferenceEnhanced]MultiHopEvaluator (chain reasoning)
    → IntegratedGovernorResult (unified output)

The pipeline produces a single JSON document that combines:
  1. PLN relevance scores and truth values for all tasks
  2. ECAN attention map with priority queue and eviction candidates
  3. Unified verdicts with temporal staleness and confidence modifiers
  4. Multi-hop chain reasoning with optional inference-rule enhancement
5. Executive summary with top-priority tasks and recommended actions

v0.2: Added use_enhanced_multihop flag for InferenceEnhancedMultiHopEvaluator
      and inference_stats in IntegratedGovernorResult.
"""

import json
from dataclasses import dataclass, field, asdict
from typing import Optional
import sys
import os
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'evaluator'))

from pln_propagation import PLNPropagator
from ecan_attention import ECANAttentionAllocator
from pln_verdict_bridge import PLNVerdictBridge
from pln_multihop import MultiHopEvaluator


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
    multihop_chains: int = 0
    multihop_goal_coverage: list = field(default_factory=list)
    multihop_max_depth: int = 0

    def to_dict(self) -> dict:
        """Return a dictionary representation of this object."""
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

    # Multi-hop layer
    multihop_task_count: int
    multihop_total_chains: int
    multihop_max_depth: int
    conflict_count: int
    conflict_details: list

    # Recommendations
    recommendations: list
    executive_summary: str

    # Inference layer (v0.2)
    inference_stats: dict = field(default_factory=dict)

    # Cross-layer agreement (v0.2.1)
    pln_bridge_agreement: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Return a dictionary representation of this object."""
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
            "multihop_layer": {
                "task_count": self.multihop_task_count,
                "total_chains": self.multihop_total_chains,
                "max_depth": self.multihop_max_depth,
            },
            "conflict_layer": {
                "conflict_count": self.conflict_count,
                "conflicts": self.conflict_details,
            },
            "inference_layer": self.inference_stats,
            "cross_layer_agreement": self.pln_bridge_agreement,
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

    def __init__(
        self,
        data: dict,
        now: Optional[datetime] = None,
        use_enhanced_multihop: bool = False,
    ):
        self.data = data
        self.use_enhanced_multihop = use_enhanced_multihop
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
        self.allocator = ECANAttentionAllocator(data, now=self.now)

        # Layer 3: Verdict bridge
        self.bridge = PLNVerdictBridge(data, now=self.now)

        # Layer 3.5: Multi-hop chain reasoning
        if use_enhanced_multihop:
            from pln_enhanced_multihop import InferenceEnhancedMultiHopEvaluator
            self.multihop = InferenceEnhancedMultiHopEvaluator(data, max_depth=4)
            self._enhanced = True
        else:
            self.multihop = MultiHopEvaluator(data, max_depth=4)
            self._enhanced = False

    def run(self, ecan_cycles: int = 10) -> IntegratedGovernorResult:
        """Run the full pipeline and produce unified output."""

        # Run ECAN dynamics
        ecan_result = self.allocator.run(cycles=ecan_cycles)
        ecan_dict = ecan_result.to_dict()

        # Run verdict bridge
        bridge_results = self.bridge.evaluate()

        # Run multi-hop chain reasoning
        multihop_results = self.multihop.evaluate()
        if self._enhanced:
            inference_stats = self.multihop.get_inference_stats()
        else:
            inference_stats = {}

        # Run conflict chain detection
        if hasattr(self.multihop, 'evaluate_conflicts'):
            conflict_chains = self.multihop.evaluate_conflicts()
        else:
            # Enhanced evaluator: fall back to naive for conflict detection
            _naive = MultiHopEvaluator(self.data, max_depth=4)
            conflict_chains = _naive.evaluate_conflicts()

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

            # Get multi-hop chain data for this task
            mh = multihop_results.get(r.task_id)
            if mh is not None:
                if hasattr(mh, 'chains'):
                    mh_chains = len(mh.chains)
                    mh_goals = mh.goal_coverage if hasattr(mh, 'goal_coverage') else []
                    mh_depth = mh.max_depth_reached if hasattr(mh, 'max_depth_reached') else 0
                elif isinstance(mh, dict):
                    mh_chains = mh.get('chain_count', 0)
                    mh_goals = mh.get('goal_coverage', [])
                    mh_depth = mh.get('max_depth', 0)
                else:
                    mh_chains = 0
                    mh_goals = []
                    mh_depth = 0
            else:
                mh_chains = 0
                mh_goals = []
                mh_depth = 0

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
                multihop_chains=mh_chains,
                multihop_goal_coverage=mh_goals,
                multihop_max_depth=mh_depth,
            )
            recommendations.append(rec)

            verdict_counts[r.unified_verdict] = verdict_counts.get(r.unified_verdict, 0) + 1

        # ── Conflict-aware verdict override ────────────────────────────
        # If a task is involved in a resource conflict with another task
        # that shares the same goals, the weaker task (lower STI) should
        # get a REPLAN verdict to consolidate on one approach.
        if conflict_chains:
            # Build a map of task_id -> recommendation for quick lookup
            rec_map = {r.task_id: r for r in recommendations}
            for cf in conflict_chains:
                task_a, task_b = cf.get('task_a'), cf.get('task_b')
                shared = cf.get('shared_goals', [])
                # Only override when tasks share at least one goal AND
                # have NO competing (different) goals. This means both tasks
                # pursue the same objective via different approaches → consolidate.
                # Tasks with competing goals (different objectives) should keep
                # their original verdict (e.g. PAUSE_RECOVERABLY for resource blocking).
                competing = cf.get('competing_goals', [])
                if not shared or competing:
                    continue
                rec_a = rec_map.get(task_a)
                rec_b = rec_map.get(task_b)
                if not rec_a or not rec_b:
                    continue
                # Determine weaker task (lower STI)
                weaker, stronger = (rec_a, rec_b) if rec_a.sti <= rec_b.sti else (rec_b, rec_a)
                # Override weaker task to REPLAN if not already a stronger verdict
                override_verdicts = {'CONTINUE', 'ESCALATE', 'PAUSE_RECOVERABLY', 'DEFER'}
                if weaker.unified_verdict in override_verdicts:
                    # Update verdict counts
                    old_v = weaker.unified_verdict
                    verdict_counts[old_v] = max(0, verdict_counts.get(old_v, 0) - 1)
                    verdict_counts['REPLAN'] = verdict_counts.get('REPLAN', 0) + 1
                    # Override the recommendation
                    weaker.unified_verdict = 'REPLAN'
                    weaker.recommended_action = ACTION_MAP.get('REPLAN', weaker.recommended_action)
                    if 'resource_conflict_replan' not in weaker.signals:
                        weaker.signals.append('resource_conflict_replan')

        # Sort recommendations by STI (highest first)
        recommendations.sort(key=lambda x: x.sti, reverse=True)

        # Executive summary
        summary = self._build_summary(
            recommendations, verdict_counts, ecan_dict, conflict_chains
        )

        # Top 3 priority from ECAN
        top3 = ecan_dict["priority_queue"][:3]

        # Aggregate multi-hop stats
        if self._enhanced:
            mh_total_chains = sum(
                (len(r.chains) if hasattr(r, 'chains') else r.get('chain_count', 0) if isinstance(r, dict) else 0)
                for r in multihop_results.values()
            )
            mh_max_depth = max(
                (r.max_depth_reached if hasattr(r, 'max_depth_reached')
                 else r.get('max_depth', 0) if isinstance(r, dict) else 0)
                for r in multihop_results.values()
            )
        else:
            mh_total_chains = sum(len(r.chains) for r in multihop_results.values())
            mh_max_depth = max((r.max_depth_reached for r in multihop_results.values()), default=0)

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
            multihop_task_count=len(multihop_results),
            multihop_total_chains=mh_total_chains,
            multihop_max_depth=mh_max_depth,
            conflict_count=len(conflict_chains),
            conflict_details=conflict_chains,
            inference_stats=inference_stats,
            pln_bridge_agreement=self._compute_agreement(recommendations),
            recommendations=recommendations,
            executive_summary=summary,
        )

    def _compute_agreement(self, recommendations: list) -> dict:
        """Compute agreement between PLN layer verdicts and final bridge verdicts."""
        pln_verdicts = {
            t.get("task_id"): t.get("suggested_verdict")
            for t in self.pln_result.get("tasks", [])
        }
        bridge_verdicts = {r.task_id: r.unified_verdict for r in recommendations}
        all_tasks = sorted(set(pln_verdicts.keys()) | set(bridge_verdicts.keys()))
        agreements = []
        disagreements = []
        for tid in all_tasks:
            pv = pln_verdicts.get(tid)
            bv = bridge_verdicts.get(tid)
            if pv is None or bv is None:
                continue
            if pv == bv:
                agreements.append(tid)
            else:
                disagreements.append({"task_id": tid, "pln_verdict": pv, "final_verdict": bv})
        return {
            "total_tasks": len(all_tasks),
            "agreements": len(agreements),
            "disagreements": len(disagreements),
            "disagreement_details": disagreements,
        }

    def _build_summary(self, recs: list, verdict_counts: dict, ecan_dict: dict, conflict_chains: list = None) -> str:
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

        # Multi-hop chains
        total_chains = sum(r.multihop_chains for r in recs)
        max_d = max((r.multihop_max_depth for r in recs), default=0)
        lines.append(f"Multi-hop: {total_chains} chains found, max depth={max_d}")

        # Resource conflicts
        if conflict_chains:
            competing = [c for c in conflict_chains if c.get('is_competing')]
            lines.append(f"Conflicts: {len(conflict_chains)} resource conflicts ({len(competing)} competing goals)")

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

        # Inference rule stats (enhanced mode only)
        if self._enhanced:
            stats = self.multihop.get_inference_stats()
            if stats.get('total', 0) > 0:
                rule_str = ", ".join(f"{k}={v}" for k, v in sorted(stats.items()) if k != 'total' and v > 0)
                lines.append(f"Inference rules: {rule_str}")

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
