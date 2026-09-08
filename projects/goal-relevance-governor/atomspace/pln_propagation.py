#!/usr/bin/env python3
"""PLN-style Evidence Propagation for the Goal Relevance Atomspace.

This module implements a simplified Probabilistic Logic Network (PLN)
evidence propagation layer on top of the Goal Relevance Graph v0.1.
It assigns TruthValue (strength, confidence) pairs to atoms and propagates
evidence through relation edges to compute relevance scores.

TruthValue conventions (simplified PLN):
  strength ∈ [0,1]   -- how true the atom is believed to be
  confidence ∈ [0,1] -- how much evidence backs the belief

Propagation rules (simplified):
  contributes_to:  child evidence propagates upward to parent goals
  part_of:         task evidence propagates to project
  occupies:        resource occupation creates a conflict cost
  blocks:          blocking constraint reduces task confidence
  supersedes:      superseded goal inherits (1 - strength) from superseder
  provides_evidence_for: result evidence propagates to goal

Relevance score for a task:
  relevance(task) = Σ over active goals: goal_strength * goal_confidence * path_weight(task→goal)
  minus: blocking_penalty + resource_conflict_penalty

This is exploratory — not a full PLN implementation.  It demonstrates
how evidence flows through the graph and how relevance scores could
drive the verdict rules.
"""

import json
from dataclasses import dataclass, field


# ─── TruthValue ───────────────────────────────────────────────────────

@dataclass
class TruthValue:
    """Simplified PLN truth value: (strength, confidence)."""
    strength: float = 0.0       # ∈ [0,1]
    confidence: float = 0.0     # ∈ [0,1]

    def combine_conjunction(self, other: 'TruthValue') -> 'TruthValue':
        """AND combination: min strength, product confidence."""
        return TruthValue(
            strength=min(self.strength, other.strength),
            confidence=self.confidence * other.confidence,
        )

    def combine_disjunction(self, other: 'TruthValue') -> 'TruthValue':
        """OR combination: max strength, probabilistic sum confidence."""
        return TruthValue(
            strength=max(self.strength, other.strength),
            confidence=self.confidence + other.confidence
                       - self.confidence * other.confidence,
        )

    def negate(self) -> 'TruthValue':
        """NOT: invert strength, keep confidence."""
        return TruthValue(
            strength=1.0 - self.strength,
            confidence=self.confidence,
        )

    def weighted_average(self, other: 'TruthValue', w: float) -> 'TruthValue':
        """Weighted average of two truth values."""
        return TruthValue(
            strength=w * self.strength + (1 - w) * other.strength,
            confidence=w * self.confidence + (1 - w) * other.confidence,
        )

    def to_dict(self) -> dict:
        """Return a dictionary representation of this object."""
        return {"strength": round(self.strength, 4),
                "confidence": round(self.confidence, 4)}


# ─── Confidence from edge metadata ────────────────────────────────────

CONFIDENCE_MAP = {
    "high": 0.9,
    "medium": 0.6,
    "low": 0.3,
}


def _edge_confidence(edge: dict) -> float:
    return CONFIDENCE_MAP.get(edge.get("confidence", "medium"), 0.6)


# ─── Initial truth values ────────────────────────────────────────────

STATUS_STRENGTH = {
    "active": 0.8,
    "achieved": 1.0,
    "cancelled": 0.0,
    "superseded": 0.1,
    "blocked": 0.2,
    "completed": 1.0,
}

STATUS_CONFIDENCE = {
    "active": 0.7,
    "achieved": 0.95,
    "cancelled": 0.95,
    "superseded": 0.9,
    "blocked": 0.8,
    "completed": 0.95,
}

# Aliases for common real-world status strings → canonical status.
# This prevents silent dropping of tasks/goals whose status field uses
# non-canonical conventions (e.g. "in_progress", "pending", "done").
STATUS_ALIASES = {
    # active canonical group
    "in_progress": "active",
    "in-progress": "active",
    "inprogress": "active",
    "pending": "active",
    "queued": "active",
    "running": "active",
    "waiting": "active",
    "ready": "active",
    "started": "active",
    "open": "active",
    "wip": "active",
    # completed canonical group
    "done": "completed",
    "finished": "completed",
    "succeeded": "completed",
    "success": "completed",
    "resolved": "completed",
    "closed": "completed",
    # achieved canonical group (primarily goals)
    "met": "achieved",
    "reached": "achieved",
    # blocked canonical group
    "stalled": "blocked",
    "stuck": "blocked",
    "paused": "blocked",
    "suspended": "blocked",
    # cancelled canonical group
    "abandoned": "cancelled",
    "dropped": "cancelled",
    "rejected": "cancelled",
    # superseded canonical group
    "deprecated": "superseded",
    "obsolete": "superseded",
    "replaced": "superseded",
    # failed — not a canonical status, but common; map to cancelled
    "failed": "cancelled",
    "error": "cancelled",
}


def normalize_status(raw) -> str:
    """Normalize a status string to a canonical status.

    Handles case-insensitivity, spaces/hyphens, and common aliases.
    Returns 'active' for None/missing values.
    """
    if raw is None:
        return "active"
    s = str(raw).strip().lower().replace(" ", "_").replace("-", "_")
    return STATUS_ALIASES.get(s, s)

PRIORITY_URGENCY = {
    "urgent": 0.95,
    "high": 0.8,
    "medium": 0.5,
    "low": 0.3,
}


def _initial_tv(node: dict) -> TruthValue:
    """Assign an initial truth value based on node properties."""
    status = normalize_status(node.get("status", "active"))
    strength = STATUS_STRENGTH.get(status, 0.5)
    confidence = STATUS_CONFIDENCE.get(status, 0.5)

    # Goals get urgency-adjusted strength
    if node.get("kind") == "goal":
        urgency = node.get("priority", {}).get("urgency", "medium")
        urgency_w = PRIORITY_URGENCY.get(urgency, 0.5)
        strength = strength * (0.5 + 0.5 * urgency_w)

    # Tasks get reversibility penalty on confidence
    if node.get("kind") == "task":
        if node.get("reversibility") == "irreversible":
            confidence *= 0.7  # less confident about irreversible actions

    return TruthValue(strength, confidence)


# ─── PLN Propagator ──────────────────────────────────────────────────

@dataclass
class PropagationResult:
    """Result of evidence propagation for a single node."""
    node_id: str
    node_kind: str
    initial_tv: TruthValue
    propagated_tv: TruthValue
    incoming_evidence: list = field(default_factory=list)
    outgoing_relevance: list = field(default_factory=list)


class PLNPropagator:
    """Propagate evidence through the Goal Relevance Graph.

    The propagator works in two passes:
    1. Upward propagation: task → goal evidence flows
    2. Downward propagation: goal → task relevance activation
    """

    def __init__(self, data: dict):
        self.nodes = {}
        self.edges = data.get("edges", [])
        for key in ("goals", "projects", "tasks", "resources",
                     "results", "constraints"):
            for node in data.get(key, []):
                self.nodes[node["id"]] = node

        # Initialize truth values
        self.tvs: dict[str, TruthValue] = {}
        for nid, node in self.nodes.items():
            self.tvs[nid] = _initial_tv(node)

    def _outgoing(self, nid: str, relation: str | None = None) -> list[dict]:
        return [e for e in self.edges
                if e["from"] == nid
                and (relation is None or e["relation"] == relation)]

    def _incoming(self, nid: str, relation: str | None = None) -> list[dict]:
        return [e for e in self.edges
                if e["to"] == nid
                and (relation is None or e["relation"] == relation)]

    # ── Upward: task → goal evidence ──────────────────────────────────

    def propagate_upward(self) -> dict[str, TruthValue]:
        """Propagate evidence from tasks/results upward through
        contributes_to and provides_evidence_for edges."""
        updated = dict(self.tvs)

        # Tasks propagate to goals via contributes_to
        for nid, node in self.nodes.items():
            if node.get("kind") in ("task", "result"):
                tv = self.tvs[nid]
                for edge in self._outgoing(nid, "contributes_to"):
                    target_id = edge["to"]
                    target_node = self.nodes.get(target_id)
                    if not target_node:
                        continue
                    edge_conf = _edge_confidence(edge)
                    propagated = TruthValue(
                        strength=tv.strength * edge_conf,
                        confidence=tv.confidence * edge_conf,
                    )
                    # Combine with existing (disjunction = OR)
                    if target_id in updated:
                        updated[target_id] = updated[target_id].combine_disjunction(propagated)
                    else:
                        updated[target_id] = propagated

        # Results propagate to goals via provides_evidence_for
        for nid, node in self.nodes.items():
            if node.get("kind") == "result":
                tv = self.tvs[nid]
                for edge in self._outgoing(nid, "provides_evidence_for"):
                    target_id = edge["to"]
                    edge_conf = _edge_confidence(edge)
                    propagated = TruthValue(
                        strength=tv.strength * edge_conf,
                        confidence=tv.confidence * edge_conf * 1.2,  # evidence boosts confidence
                    )
                    propagated.confidence = min(propagated.confidence, 1.0)
                    if target_id in updated:
                        updated[target_id] = updated[target_id].combine_disjunction(propagated)
                    else:
                        updated[target_id] = propagated

        # Intermediate goals propagate to top goals
        for nid, node in self.nodes.items():
            if node.get("kind") == "goal" and node.get("level") == "intermediate":
                tv = updated.get(nid, self.tvs[nid])
                for edge in self._outgoing(nid, "contributes_to"):
                    target_id = edge["to"]
                    target_node = self.nodes.get(target_id)
                    if not target_node or target_node.get("kind") != "goal":
                        continue
                    edge_conf = _edge_confidence(edge)
                    propagated = TruthValue(
                        strength=tv.strength * edge_conf,
                        confidence=tv.confidence * edge_conf,
                    )
                    if target_id in updated:
                        updated[target_id] = updated[target_id].combine_disjunction(propagated)
                    else:
                        updated[target_id] = propagated

        # Superseded goals weaken
        for nid, node in self.nodes.items():
            if node.get("kind") == "goal":
                for edge in self._incoming(nid, "supersedes"):
                    superseder_id = edge["from"]
                    superseder_tv = updated.get(superseder_id, self.tvs.get(superseder_id))
                    if superseder_tv:
                        # Superseded goal inherits weakness
                        updated[nid] = updated[nid].weighted_average(
                            superseder_tv.negate(), 0.7
                        )

        self.tvs = updated
        return updated

    # ── Downward: goal → task relevance ──────────────────────────────

    def _goal_active(self, goal_id: str) -> bool:
        node = self.nodes.get(goal_id)
        if not node:
            return False
        return normalize_status(node.get("status", "active")) == "active"

    def propagate_downward(self) -> dict[str, float]:
        """Propagate truth values downward from goals to tasks."""
        relevance: dict[str, float] = {}
        self._task_meta: dict[str, dict] = {}

        for nid, node in self.nodes.items():
            if node.get("kind") != "task":
                continue

            score = 0.0
            has_active = False
            has_achieved = False
            has_superseded = False
            has_cancelled = False
            has_blocker = False
            has_res_conflict = False

            for edge in self._outgoing(nid, "contributes_to"):
                goal_id = edge["to"]
                gn = self.nodes.get(goal_id)
                if not gn or gn.get("kind") != "goal":
                    continue
                edge_conf = _edge_confidence(edge)
                status = normalize_status(gn.get("status", "active"))

                if status == "active":
                    has_active = True
                    goal_tv = self.tvs.get(goal_id, TruthValue())
                    trans = 0.0
                    for e2 in self._outgoing(goal_id, "contributes_to"):
                        pid = e2["to"]
                        pn = self.nodes.get(pid)
                        if not pn or pn.get("kind") != "goal":
                            continue
                        if not self._goal_active(pid):
                            continue
                        ptv = self.tvs.get(pid, TruthValue())
                        pconf = _edge_confidence(e2)
                        trans += ptv.strength * ptv.confidence * pconf
                    ga = goal_tv.strength * goal_tv.confidence
                    score += ga * edge_conf + trans * 0.5
                elif status == "achieved":
                    has_achieved = True
                elif status == "superseded":
                    has_superseded = True
                elif status == "cancelled":
                    has_cancelled = True

            block_pen = 0.0
            for edge in self._incoming(nid, "blocks"):
                cn = self.nodes.get(edge["from"])
                if cn:
                    has_blocker = True
                    ctv = self.tvs.get(edge["from"], TruthValue())
                    block_pen += ctv.strength * ctv.confidence

            res_pen = 0.0
            for edge in self._outgoing(nid, "occupies"):
                rid = edge["to"]
                rn = self.nodes.get(rid)
                if not rn or not rn.get("exclusive"):
                    continue
                for e2 in self._incoming(rid, "occupies"):
                    if e2["from"] == nid:
                        continue
                    on = self.nodes.get(e2["from"])
                    if not on or normalize_status(on.get("status", "active")) != "active":
                        continue
                    for og in self._outgoing(e2["from"], "contributes_to"):
                        ogn = self.nodes.get(og["to"])
                        if ogn and ogn.get("kind") == "goal" and normalize_status(ogn.get("status") or "active") == "active":
                            orank = ogn.get("priority", {}).get("rank", 999)
                            for tg in self._outgoing(nid, "contributes_to"):
                                tgn = self.nodes.get(tg["to"])
                                if tgn and tgn.get("kind") == "goal" and normalize_status(tgn.get("status") or "active") == "active":
                                    trank = tgn.get("priority", {}).get("rank", 999)
                                    if orank < trank:
                                        has_res_conflict = True
                                        res_pen += 0.6 * _edge_confidence(e2)

            self._task_meta[nid] = {
                "has_active": has_active, "has_achieved": has_achieved,
                "has_superseded": has_superseded, "has_cancelled": has_cancelled,
                "has_blocker": has_blocker, "has_res_conflict": has_res_conflict,
            }
            relevance[nid] = max(0.0, score - block_pen - res_pen)

        return relevance

    # ── Full propagation + verdict mapping ────────────────────────────

    def _get_direct_goals(self, nid: str) -> list[str]:
        return [e["to"] for e in self._outgoing(nid, "contributes_to")
                if self.nodes.get(e["to"], {}).get("kind") == "goal"]

    def _get_transitive_goals(self, nid: str) -> list[str]:
        goals = []
        for e in self._outgoing(nid, "contributes_to"):
            gid = e["to"]
            gn = self.nodes.get(gid)
            if not gn or gn.get("kind") != "goal":
                continue
            goals.append(gid)
            if gn.get("level") == "intermediate":
                for e2 in self._outgoing(gid, "contributes_to"):
                    pid = e2["to"]
                    pn = self.nodes.get(pid)
                    if pn and pn.get("kind") == "goal":
                        goals.append(pid)
        return goals

    def _get_project_for_task(self, nid: str) -> dict | None:
        for e in self._outgoing(nid, "part_of"):
            pn = self.nodes.get(e["to"])
            if pn and pn.get("kind") == "project":
                return pn
        return None

    def _get_superseding_goals(self, gid: str) -> list[str]:
        return [e["from"] for e in self._incoming(gid, "supersedes")
                if self.nodes.get(e["from"], {}).get("kind") == "goal"]

    def _has_evidence_for(self, gid: str) -> bool:
        return any(self._incoming(gid, "provides_evidence_for"))

    def evaluate(self) -> dict:
        """Evaluate the graph and return results."""
        self.propagate_upward()
        relevance = self.propagate_downward()

        results = []
        for nid, node in self.nodes.items():
            if node.get("kind") != "task" or node.get("status") != "active":
                continue
            tv = self.tvs.get(nid, TruthValue())
            rel = relevance.get(nid, 0.0)

            direct_goals = self._get_direct_goals(nid)
            transitive_goals = self._get_transitive_goals(nid)
            active_transitive = [g for g in transitive_goals
                                 if self.nodes.get(g, {}).get("status") == "active"]

            suggested = "CONTINUE"
            signals = ["healthy"]

            # Rule 1: STOP_STALE
            if direct_goals and all(
                normalize_status(self.nodes.get(g, {}).get("status", "active")) in ("achieved", "cancelled")
                for g in direct_goals
            ):
                suggested = "STOP_STALE"
                signals = ["all_direct_goals_terminal"]
            # Rule 2: BLOCKED
            elif any(self._incoming(nid, "blocks")):
                suggested = "BLOCKED"
                signals = ["blocked_by_constraint"]
            # Rule 3: PAUSE_RECOVERABLY (resource conflict + checkpointable)
            elif node.get("reversibility") == "checkpointable":
                paused = False
                for e in self._outgoing(nid, "occupies"):
                    rid = e["to"]
                    rn = self.nodes.get(rid)
                    if not rn or not rn.get("exclusive"):
                        continue
                    for e2 in self._incoming(rid, "occupies"):
                        other_id = e2["from"]
                        if other_id == nid:
                            continue
                        other_node = self.nodes.get(other_id)
                        if not other_node or normalize_status(other_node.get("status", "active")) != "active":
                            continue
                        other_goals = self._get_transitive_goals(other_id)
                        for og in other_goals:
                            ogn = self.nodes.get(og)
                            if not ogn or normalize_status(ogn.get("status", "active")) != "active":
                                continue
                            for tg in active_transitive:
                                tgn = self.nodes.get(tg)
                                if not tgn or normalize_status(tgn.get("status", "active")) != "active":
                                    continue
                                orank = ogn.get("priority", {}).get("rank", 999)
                                trank = tgn.get("priority", {}).get("rank", 999)
                                if orank < trank:
                                    paused = True
                                    suggested = "PAUSE_RECOVERABLY"
                                    signals = ["resource_contention", f"resource={rid}", f"higher_priority_task={other_id}"]
                                    break
                            if paused:
                                break
                        if paused:
                            break
                    if paused:
                        break
            # Rule 4: DEFER (irreversible on early-stage research)
            if suggested == "CONTINUE" and node.get("reversibility") == "irreversible":
                project = self._get_project_for_task(nid)
                if project:
                    rc = project.get("result_contract", {})
                    stage = rc.get("maturity_stage", "")
                    kind = rc.get("project_kind", "")
                    if kind in ("exploratory_research", "confirmatory_research") and stage in ("E0_exploration", "E1_signal_validation"):
                        suggested = "DEFER"
                        signals = ["irreversible_on_early_stage_research", f"project_kind={kind}", f"stage={stage}"]
            # Rule 5: REPLAN (goal superseded)
            if suggested == "CONTINUE":
                for g in transitive_goals:
                    gn = self.nodes.get(g)
                    if gn and normalize_status(gn.get("status") or "active") == "superseded":
                        superseding = self._get_superseding_goals(g)
                        if superseding:
                            suggested = "REPLAN"
                            signals = ["goal_superseded", f"superseded_goal={g}", f"superseded_by={superseding[0]}"]
                            break
            # Rule 6: ESCALATE (multiple active goals, no evidence)
            if suggested == "CONTINUE":
                if len(active_transitive) > 1:
                    has_evidence = any(self._has_evidence_for(g) for g in active_transitive)
                    if not has_evidence:
                        suggested = "ESCALATE"
                        signals = ["multiple_active_goals_no_evidence", f"{len(active_transitive)}_active_goals"]

            results.append({
                "task_id": nid,
                "title": node.get("title", ""),
                "truth_value": tv.to_dict(),
                "relevance_score": round(rel, 4),
                "suggested_verdict": suggested,
                "signals": signals,
            })

        return {"tasks": results}


if __name__ == "__main__":
    import sys
    data = json.load(open(sys.argv[1]))
    prop = PLNPropagator(data)
    result = prop.evaluate()
    print(json.dumps(result, indent=2))
