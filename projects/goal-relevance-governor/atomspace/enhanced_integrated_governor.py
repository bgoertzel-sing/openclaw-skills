#!/usr/bin/env python3
"""Enhanced Integrated Governor Pipeline v0.2
=============================================

Extends the IntegratedGovernorPipeline by replacing the naive MultiHopEvaluator
with InferenceEnhancedMultiHopEvaluator, which uses PLN inference rules
(deduction, induction, abduction, revision, inhibitory) to find deeper
reasoning chains that the naive evaluator misses.

Key improvement: Naive PLN propagation returns 0.0000 relevance for all 6
replay episodes. The enhanced evaluator finds meaningful chains (0.16-0.43)
by applying inference rules along the path.
"""

import json
import sys
import os
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'evaluator'))

from pln_propagation import PLNPropagator
from ecan_attention import ECANAttentionAllocator
from pln_verdict_bridge import PLNVerdictBridge
from pln_enhanced_multihop import InferenceEnhancedMultiHopEvaluator
from integrated_governor import (
    ACTION_MAP,
    TaskRecommendation,
    IntegratedGovernorResult,
)


@dataclass
class EnhancedGovernorResult(IntegratedGovernorResult):
    """Extends the base result with enhanced PLN inference stats."""
    enhanced_pln_task_count: int = 0
    enhanced_pln_total_relevance: float = 0.0
    enhanced_pln_inference_stats: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        base = super().to_dict()
        base["enhanced_pln_layer"] = {
            "task_count": self.enhanced_pln_task_count,
            "total_relevance": round(self.enhanced_pln_total_relevance, 4),
            "inference_stats": self.enhanced_pln_inference_stats,
        }
        return base


class EnhancedIntegratedGovernorPipeline:
    """Enhanced pipeline using PLN inference-rule-enhanced multi-hop.

    Same flow as IntegratedGovernorPipeline but swaps MultiHopEvaluator
    for InferenceEnhancedMultiHopEvaluator.
    """

    def __init__(self, data: dict, now: Optional[datetime] = None):
        self.data = data
        if now is None:
            frozen_at = data.get("frozen_at")
            if frozen_at:
                self.now = datetime.fromisoformat(frozen_at.replace("Z", "+00:00"))
            else:
                self.now = datetime.now(timezone.utc)
        else:
            self.now = now

        # Layer 1: PLN propagation (naive baseline for comparison)
        self.propagator = PLNPropagator(data)
        self.pln_result = self.propagator.evaluate()

        # Layer 2: ECAN attention
        self.allocator = ECANAttentionAllocator(data, now=self.now)

        # Layer 3: Verdict bridge
        self.bridge = PLNVerdictBridge(data, now=self.now)

        # Layer 3.5: ENHANCED multi-hop chain reasoning
        self.multihop = InferenceEnhancedMultiHopEvaluator(data, max_depth=4)

    def run(self, ecan_cycles: int = 10) -> EnhancedGovernorResult:
        """Run the enhanced pipeline and produce unified output."""

        # Run ECAN dynamics
        ecan_result = self.allocator.run(cycles=ecan_cycles)
        ecan_dict = ecan_result.to_dict()

        # Run verdict bridge
        bridge_results = self.bridge.evaluate()

        # Run ENHANCED multi-hop chain reasoning
        multihop_results = self.multihop.evaluate()
        inference_stats = self.multihop.get_inference_stats()

        # Run conflict chain detection (inherited from enhanced)
        conflict_chains = self.multihop.evaluate_conflicts()

        recommendations = []
        verdict_counts = {}

        for r in bridge_results:
            av = self.allocator.attention.get(r.task_id)
            sti = av.sti if av else 0.0
            lti = av.lti if av else 0.0
            eviction = av.eviction_candidate if av else False

            action = ACTION_MAP.get(r.unified_verdict, "No specific action.")

            # Get enhanced multi-hop chain data
            mh = multihop_results.get(r.task_id)
            mh_chains = len(mh.chains) if mh else 0
            mh_goals = mh.goal_coverage if mh else []
            mh_depth = mh.max_depth_reached if mh else 0
            mh_relevance = mh.aggregated_relevance if mh else 0.0
            mh_tv_strength = mh.aggregated_tv.strength if mh else 0.0
            mh_tv_confidence = mh.aggregated_tv.confidence if mh else 0.0

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
        if conflict_chains:
            rec_map = {r.task_id: r for r in recommendations}
            for cf in conflict_chains:
                task_a, task_b = cf.get('task_a'), cf.get('task_b')
                shared = cf.get('shared_goals', [])
                competing = cf.get('competing_goals', [])
                if not shared or competing:
                    continue
                rec_a = rec_map.get(task_a)
                rec_b = rec_map.get(task_b)
                if not rec_a or not rec_b:
                    continue
                weaker, stronger = (rec_a, rec_b) if rec_a.sti <= rec_b.sti else (rec_b, rec_a)
                override_verdicts = {'CONTINUE', 'ESCALATE', 'PAUSE_RECOVERABLY', 'DEFER'}
                if weaker.unified_verdict in override_verdicts:
                    old_v = weaker.unified_verdict
                    verdict_counts[old_v] = max(0, verdict_counts.get(old_v, 0) - 1)
                    verdict_counts['REPLAN'] = verdict_counts.get('REPLAN', 0) + 1
                    weaker.unified_verdict = 'REPLAN'
                    weaker.recommended_action = ACTION_MAP.get('REPLAN', weaker.recommended_action)
                    if 'resource_conflict_replan' not in weaker.signals:
                        weaker.signals.append('resource_conflict_replan')

        recommendations.sort(key=lambda x: x.sti, reverse=True)

        # Enhanced PLN stats
        enhanced_total_rel = sum(
            mh.aggregated_relevance for mh in multihop_results.values()
        )

        summary = self._build_summary(
            recommendations, verdict_counts, ecan_dict, conflict_chains, inference_stats
        )

        top3 = ecan_dict["priority_queue"][:3]

        mh_total_chains = sum(len(r.chains) for r in multihop_results.values())
        mh_max_depth = max((r.max_depth_reached for r in multihop_results.values()), default=0)

        return EnhancedGovernorResult(
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
            recommendations=recommendations,
            executive_summary=summary,
            enhanced_pln_task_count=len(multihop_results),
            enhanced_pln_total_relevance=enhanced_total_rel,
            enhanced_pln_inference_stats=inference_stats,
        )

    def _build_summary(self, recs, verdict_counts, ecan_dict, conflict_chains, inference_stats):
        lines = []
        lines.append(f"Pipeline evaluated {len(recs)} tasks.")
        verdict_str = ", ".join(f"{k}={v}" for k, v in sorted(verdict_counts.items()))
        lines.append(f"Verdict distribution: {verdict_str}")
        if recs:
            top = recs[0]
            lines.append(
                f"Top priority: {top.task_id} "
                f"(STI={top.sti:.1f}, {top.unified_verdict}, "
                f"rel={top.relevance_score:.3f})"
            )
        total_chains = sum(r.multihop_chains for r in recs)
        max_d = max