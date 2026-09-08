#!/usr/bin/env python3
"""PLN-Verdict Bridge: Deep integration of PLN evidence with verdict rules.

This module bridges the PLNPropagator's continuous relevance scores and truth
values with the discrete verdict rules from RelevanceEvaluator.  It produces
a unified VerdictEnhanced result that combines:

  - The rule-based verdict (STOP_STALE, BLOCKED, PAUSE_RECOVERABLY, etc.)
  - The PLN truth value (strength, confidence)
  - A PLN-derived relevance score ∈ [0,1]
  - A confidence modifier that adjusts the verdict's certainty
  - Temporal staleness detection from edge metadata

The bridge works in three phases:

  1. Run PLNPropagator.evaluate() to get truth values + relevance scores
  2. Run RelevanceEvaluator to get rule-based verdicts
  3. Fuse the two into VerdictEnhanced objects

Key insight: The PLN relevance score provides a *continuous* signal that the
rule-based verdict system cannot express.  A task with verdict CONTINUE but
relevance_score=0.15 is very different from one with relevance_score=0.95.
The bridge exposes this distinction via a `priority_band` field.

Priority bands (based on PLN relevance score):
  CRITICAL:  score >= 0.70   — high-confidence, high-relevance
  NORMAL:    0.35 <= score < 0.70 — moderate relevance
  LOW:       0.10 <= score < 0.35 — marginal relevance, candidate for deferral
  STALE:     score < 0.10    — effectively dead, even if verdict says CONTINUE

Temporal staleness:
  If a goal's `last_updated` timestamp is older than a staleness threshold
  (default 14 days), the goal's truth value confidence is decayed.  Tasks
  connected to only stale goals get a STALE flag.

Confidence modifier:
  The PLN confidence of the task's truth value modifies the verdict's
  certainty.  Low confidence (< 0.3) adds a "low_confidence" signal.

This is exploratory — not a production enforcement layer.  It demonstrates
how PLN continuous reasoning can enhance discrete rule-based decisions.
"""

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone, timedelta

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'evaluator'))
sys.path.insert(0, os.path.dirname(__file__))

from pln_propagation import PLNPropagator, TruthValue
from relevance_evaluator import Graph, RelevanceEvaluator


# ─── Configuration ───────────────────────────────────────────────────

STALENESS_THRESHOLD_DAYS = 14  # goals older than this are considered stale
STALENESS_DECAY_FACTOR = 0.5    # stale goals decay confidence by this factor

PRIORITY_BANDS = [
    (0.70, "CRITICAL"),
    (0.35, "NORMAL"),
    (0.10, "LOW"),
    (0.00, "STALE"),
]


# ─── Data classes ────────────────────────────────────────────────────

@dataclass
class VerdictEnhanced:
    """A rule-based verdict enhanced with PLN continuous signals."""
    task_id: str
    verdict: str                          # from RelevanceEvaluator
    pln_verdict: str                      # from PLNPropagator
    truth_value: dict                     # {strength, confidence}
    relevance_score: float                # PLN relevance ∈ [0,1]
    priority_band: str                    # CRITICAL/NORMAL/LOW/STALE
    confidence_modifier: float            # ±adjustment to verdict certainty
    staleness_flag: bool                  # True if goal is temporally stale
    signals: list = field(default_factory=list)
    evidence: list = field(default_factory=list)
    reasons: list = field(default_factory=list)

    def to_dict(self) -> dict:
        """Return a dictionary representation of this object."""
        return asdict(self)

    @property
    def unified_verdict(self) -> str:
        """The fused verdict: PLN-enhanced rule-based verdict.

        If both engines agree, use the rule-based verdict.
        If they disagree, use the rule-based verdict but add a signal.
        If the PLN priority_band is STALE and the verdict is CONTINUE,
        downgrade to PAUSE_RECOVERABLY (stale relevance).
        """
        if self.verdict == "CONTINUE" and self.priority_band == "STALE":
            return "PAUSE_RECOVERABLY"
        return self.verdict


# ─── Temporal staleness ──────────────────────────────────────────────

def _parse_timestamp(ts: str | None) -> datetime | None:
    """Parse an ISO timestamp, return None on failure."""
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


def compute_staleness(goal_node: dict, now: datetime | None = None,
                      threshold_days: int = STALENESS_THRESHOLD_DAYS) -> bool:
    """Check if a goal node is temporally stale.

    A goal is stale if its `last_updated` or `as_of` timestamp is older
    than threshold_days from now.
    """
    if now is None:
        now = datetime.now(timezone.utc)

    for field_name in ("last_updated", "as_of", "updated_at"):
        ts = goal_node.get(field_name)
        dt = _parse_timestamp(ts)
        if dt:
            age = now - dt
            return age > timedelta(days=threshold_days)

    # No timestamp available — can't determine staleness
    return False


def _confidence_modifier(tv: TruthValue, is_stale: bool = False) -> float:
    """Compute a confidence modifier from a truth value.

    Returns a value in [-0.4, +0.1]:
      - High confidence (>= 0.8): +0.1 boost
      - Medium confidence (0.3-0.8): 0.0 neutral
      - Low confidence (< 0.3): -0.3 penalty
      - Stale goals: additional -0.1 penalty on top of decay

    If is_stale is True, apply a multiplicative decay to the truth
    value's confidence *before* computing the modifier, so that stale
    goals with moderate confidence get pushed into the low-confidence
    penalty band.  An additional flat -0.1 penalty ensures stale
    tasks always have a negative modifier even if decayed confidence
    stays in the neutral band.
    """
    c = tv.confidence
    stale_penalty = 0.0
    if is_stale:
        c = c * STALENESS_DECAY_FACTOR
        stale_penalty = -0.1
    if c >= 0.8:
        return 0.1 + stale_penalty
    elif c >= 0.3:
        return 0.0 + stale_penalty
    else:
        return -0.3 + stale_penalty


def _priority_band(score: float) -> str:
    """Map a relevance score to a priority band."""
    for threshold, band in PRIORITY_BANDS:
        if score >= threshold:
            return band
    return "STALE"


# ─── Bridge ──────────────────────────────────────────────────────────

class PLNVerdictBridge:
    """Fuse PLN continuous reasoning with rule-based verdicts.

    Usage:
        bridge = PLNVerdictBridge(graph_data)
        results = bridge.evaluate()
        for r in results:
            print(r.task_id, r.unified_verdict, r.priority_band)
    """

    def __init__(self, data: dict, now: datetime | None = None):
        self.data = data
        self.now = now or datetime.now(timezone.utc)

        # Run both engines
        self._graph = Graph(data)
        self._evaluator = RelevanceEvaluator(self._graph)
        self._propagator = PLNPropagator(data)
        self._pln_result = self._propagator.evaluate()

    def _get_pln_task(self, task_id: str) -> dict | None:
        """Get PLN result for a specific task."""
        for t in self._pln_result.get("tasks", []):
            if t["task_id"] == task_id:
                return t
        return None

    def _get_goal_staleness(self, task_id: str) -> tuple[bool, list[str]]:
        """Check if any of the task's active goals are stale.

        Returns (is_stale, stale_goal_ids).
        """
        stale_goals = []
        goals = self._graph.get_active_goals_for(task_id)
        for g in goals:
            if compute_staleness(g, self.now):
                stale_goals.append(g["id"])
        return (len(stale_goals) > 0, stale_goals)

    def evaluate(self) -> list[VerdictEnhanced]:
        """Evaluate all active tasks and return enhanced verdicts."""
        # Get rule-based verdicts
        py_verdicts = {v.task_id: v for v in self._evaluator.evaluate_all()}

        # Build PLN verdict lookup
        pln_verdicts = {t["task_id"]: t for t in self._pln_result.get("tasks", [])}

        results = []
        for task_id, py_v in py_verdicts.items():
            pln_task = pln_verdicts.get(task_id, {})
            pln_verdict = pln_task.get("suggested_verdict", "CONTINUE")
            tv_dict = pln_task.get("truth_value", {"strength": 0.5, "confidence": 0.5})
            tv = TruthValue(tv_dict["strength"], tv_dict["confidence"])
            relevance = pln_task.get("relevance_score", 0.0)
            pln_signals = pln_task.get("signals", [])

            # Compute staleness
            is_stale, stale_goal_ids = self._get_goal_staleness(task_id)

            # Compute confidence modifier (stale goals get decayed confidence)
            conf_mod = _confidence_modifier(tv, is_stale=is_stale)

            # Determine priority band
            band = _priority_band(relevance)

            # Build signals
            signals = list(pln_signals)
            if is_stale:
                signals.append(f"temporal_staleness:goals={stale_goal_ids}")
            if conf_mod < 0:
                signals.append("low_confidence")
            if self.verdicts_disagree(py_v.verdict, pln_verdict):
                signals.append(f"verdict_disagreement:rule={py_v.verdict},pln={pln_verdict}")
            if py_v.verdict == "CONTINUE" and band == "STALE":
                signals.append("stale_relevance_downgrade")

            results.append(VerdictEnhanced(
                task_id=task_id,
                verdict=py_v.verdict,
                pln_verdict=pln_verdict,                truth_value=({**tv_dict, "confidence": round(tv.confidence * (STALENESS_DECAY_FACTOR if is_stale else 1.0), 4)}),
                relevance_score=round(relevance, 4),
                priority_band=band,
                confidence_modifier=round(conf_mod, 3),
                staleness_flag=is_stale,
                signals=signals,
                evidence=py_v.evidence + [f"pln_relevance={relevance:.4f}"],
                reasons=py_v.reasons,
            ))

        return results

    @staticmethod
    def verdicts_disagree(rule_verdict: str, pln_verdict: str) -> bool:
        """Check if the rule-based and PLN verdicts disagree.

        CONTINUE and CONTINUE are agreement.
        Any mismatch is disagreement.
        """
        return rule_verdict != pln_verdict

    def evaluate_to_json(self) -> str:
        """Evaluate and return JSON string."""
        results = self.evaluate()
        return json.dumps({
            "format": "PLN-Verdict-Bridge-v0.1",
            "generated_at": self.now.isoformat(),
            "task_count": len(results),
            "tasks": [r.to_dict() for r in results],
        }, indent=2)


if __name__ == "__main__":
    import sys
    data = json.load(open(sys.argv[1]))
    bridge = PLNVerdictBridge(data)
    print(bridge.evaluate_to_json())
