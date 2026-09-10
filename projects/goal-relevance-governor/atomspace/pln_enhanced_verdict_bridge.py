#!/usr/bin/env python3
"""PLN-Verdict Bridge v0.2: Inference-Enhanced Integration.

Extends PLNVerdictBridge to use the InferenceEnhancedMultiHopEvaluator
instead of the naive PLNPropagator.  This means:

  - Truth values are propagated using PLN inference rules (deduction,
    induction, abduction, revision, inhibitory) rather than naive
    strength*confidence multiplication.
  - Chain aggregation uses PLN revision instead of simple disjunction.
  - Inference rule usage statistics are exposed.

The enhanced bridge produces the same VerdictEnhanced output format
as v0.1, but with more principled truth values.

Usage:
    bridge = EnhancedPLNVerdictBridge(graph_data)
    results = bridge.evaluate()
    for r in results:
        print(r.task_id, r.unified_verdict, r.priority_band)
"""

import json
import sys
import os
from dataclasses import asdict
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'evaluator'))
sys.path.insert(0, os.path.dirname(__file__))

from atomspace.pln_propagation import TruthValue, PLNPropagator
from atomspace.pln_enhanced_multihop import InferenceEnhancedMultiHopEvaluator
from atomspace.pln_verdict_bridge import (
    VerdictEnhanced, compute_staleness, _confidence_modifier,
    _priority_band, STALENESS_DECAY_FACTOR,
)
from evaluator.relevance_evaluator import Graph, RelevanceEvaluator


class EnhancedPLNVerdictBridge:
    """Fuse inference-enhanced PLN reasoning with rule-based verdicts.

    Drop-in replacement for PLNVerdictBridge that uses
    InferenceEnhancedMultiHopEvaluator for truth value computation.
    """

    def __init__(self, data: dict, now: datetime | None = None,
                 max_depth: int = 4):
        self.data = data
        self.now = now or datetime.now(timezone.utc)
        self.max_depth = max_depth

        # Rule-based evaluator
        self._graph = Graph(data)
        self._evaluator = RelevanceEvaluator(self._graph)

        # Inference-enhanced PLN evaluator
        self._enhanced = InferenceEnhancedMultiHopEvaluator(
            data, max_depth=max_depth
        )

        # Also run the naive propagator for comparison
        self._propagator = PLNPropagator(data)
        self._naive_result = self._propagator.evaluate()

        # Run enhanced evaluation
        self._enhanced_result = self._enhanced.evaluate_enhanced()
        self._inference_stats = self._enhanced.get_inference_stats()

    def _get_pln_task_naive(self, task_id: str) -> dict | None:
        """Get naive PLN result for comparison."""
        for t in self._naive_result.get("tasks", []):
            if t["task_id"] == task_id:
                return t
        return None

    def _get_goal_staleness(self, task_id: str) -> tuple[bool, list[str]]:
        """Check if any of the task's active goals are stale."""
        stale_goals = []
        goals = self._graph.get_active_goals_for(task_id)
        for g in goals:
            if compute_staleness(g, self.now):
                stale_goals.append(g["id"])
        return (len(stale_goals) > 0, stale_goals)

    def evaluate(self) -> list[VerdictEnhanced]:
        """Evaluate all active tasks with inference-enhanced PLN."""
        py_verdicts = {v.task_id: v for v in self._evaluator.evaluate_all()}

        results = []
        for task_id, py_v in py_verdicts.items():
            # Get enhanced PLN result
            enhanced = self._enhanced_result.get(task_id, {})

            # Get naive PLN result for comparison
            naive_task = self._get_pln_task_naive(task_id) or {}
            naive_relevance = naive_task.get("relevance_score", 0.0)
            naive_verdict = naive_task.get("suggested_verdict", "CONTINUE")

            # Enhanced truth value
            tv_dict = enhanced.get("aggregated_tv", {"strength": 0.5, "confidence": 0.5})
            tv = TruthValue(tv_dict["strength"], tv_dict["confidence"])

            # Enhanced relevance (from ChainAggregator)
            enhanced_relevance = enhanced.get("relevance_score", 0.0)

            # Blend enhanced and naive relevance:
            # - Enhanced PLN captures chain structure quality (inference-aware)
            # - Naive captures task-specific signals (priority, blocking, staleness)
            # Blend weight: 60% naive (task-specific), 40% enhanced (chain quality)
            BLEND_NAIVE = 0.6
            BLEND_ENHANCED = 0.4
            if enhanced_relevance > 0:
                relevance = (BLEND_NAIVE * naive_relevance +
                             BLEND_ENHANCED * enhanced_relevance)
            else:
                relevance = naive_relevance

            # PLN verdict from naive (rule-based PLN verdict)
            pln_verdict = naive_verdict

            # Compute staleness
            is_stale, stale_goal_ids = self._get_goal_staleness(task_id)

            # Compute confidence modifier
            conf_mod = _confidence_modifier(tv, is_stale=is_stale)

            # Determine priority band
            band = _priority_band(relevance)

            # Build signals
            signals = []
            if is_stale:
                signals.append(f"temporal_staleness:goals={stale_goal_ids}")
            if conf_mod < 0:
                signals.append("low_confidence")

            # Check if enhanced and naive relevance differ significantly
            blended_relevance = relevance
            if abs(blended_relevance - naive_relevance) > 0.05:
                signals.append(
                    f"relevance_shift:naive={naive_relevance:.4f},"
                    f"enhanced={enhanced_relevance:.4f},"
                    f"blended={blended_relevance:.4f}"
                )

            if self.verdicts_disagree(py_v.verdict, pln_verdict):
                signals.append(
                    f"verdict_disagreement:rule={py_v.verdict},pln={pln_verdict}"
                )
            if py_v.verdict == "CONTINUE" and band == "STALE":
                signals.append("stale_relevance_downgrade")

            # Chain info
            chain_count = enhanced.get("chain_count", 0)
            goal_coverage = enhanced.get("goal_coverage", [])

            evidence = py_v.evidence + [
                f"pln_relevance={relevance:.4f}",
                f"enhanced_tv={tv_dict}",
                f"chain_count={chain_count}",
                f"goal_coverage={goal_coverage}",
            ]

            # Adjust confidence for staleness
            adj_confidence = round(
                tv.confidence * (STALENESS_DECAY_FACTOR if is_stale else 1.0), 4
            )

            results.append(VerdictEnhanced(
                task_id=task_id,
                verdict=py_v.verdict,
                pln_verdict=pln_verdict,
                truth_value={
                    "strength": round(tv.strength, 4),
                    "confidence": adj_confidence,
                },
                relevance_score=round(relevance, 4),
                priority_band=band,
                confidence_modifier=round(conf_mod, 3),
                staleness_flag=is_stale,
                signals=signals,
                evidence=evidence,
                reasons=py_v.reasons,
            ))

        return results

    @staticmethod
    def verdicts_disagree(rule_verdict: str, pln_verdict: str) -> bool:
        """Check if rule-based and PLN verdicts disagree."""
        return rule_verdict != pln_verdict

    def get_inference_stats(self) -> dict:
        """Return inference rule usage statistics."""
        return self._inference_stats

    def evaluate_to_json(self) -> str:
        """Evaluate and return JSON string."""
        results = self.evaluate()
        return json.dumps({
            "format": "Enhanced-PLN-Verdict-Bridge-v0.2",
            "generated_at": self.now.isoformat(),
            "task_count": len(results),
            "inference_stats": self._inference_stats,
            "tasks": [r.to_dict() for r in results],
        }, indent=2)

    def evaluate_to_json_enhanced(self) -> str:
        """Full JSON output with enhanced PLN details."""
        results = self.evaluate()
        return json.dumps({
            "format": "Enhanced-PLN-Verdict-Bridge-v0.2-detailed",
            "generated_at": self.now.isoformat(),
            "task_count": len(results),
            "inference_stats": self._inference_stats,
            "enhanced_pln": self._enhanced_result,
            "tasks": [r.to_dict() for r in results],
        }, indent=2)


if __name__ == "__main__":
    data = json.load(open(sys.argv[1]))
    bridge = EnhancedPLNVerdictBridge(data)
    print(bridge.evaluate_to_json())
