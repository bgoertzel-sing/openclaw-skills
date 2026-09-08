#!/usr/bin/env python3
"""PLN Chain Integration: Connects inference rules to multi-hop reasoning.

Upgrades the ChainMiner's naive truth-value propagation (simple multiplication)
with proper PLN inference rules:

  - contributes_to edges use DEDUCTION (task strength -> goal strength)
  - provides_evidence_for edges use INDUCTION (result -> goal inference)
  - blocks edges use ABDUCTION (infer cause from observed blocking)
  - occupies/part_of edges use REVISION (merge competing evidence)
  - supersedes edges use negation + DEDUCTION

This produces more principled truth-value propagation along reasoning chains,
respecting the confidence hierarchy: deduction >= induction >= abduction.
"""

import json
from dataclasses import dataclass, field
from collections import defaultdict
from typing import Optional

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from pln_propagation import TruthValue, _edge_confidence, _initial_tv, normalize_status
from pln_inference_rules import (
    deduction, induction, abduction, revision,
    confidence_to_count, count_to_confidence,
    relevance_blend,
)


# ─── Relation-to-Rule Mapping ────────────────────────────────────────

RELATION_RULE_MAP = {
    "contributes_to": "deduction",
    "provides_evidence_for": "induction",
    "part_of": "revision",
    "occupies": "revision",
    "blocks": "abduction",
    "supersedes": "deduction",
    "depends_on": "deduction",
    "subsumes": "deduction",
}


def propagate_with_rules(
    source_tv: TruthValue,
    edge_conf: float,
    relation: str,
    target_prevalence: float = 0.5,
) -> TruthValue:
    """Propagate a truth value along an edge using the appropriate PLN rule.

    Args:
        source_tv: Truth value of the source node.
        edge_conf: Confidence of the edge relation (from _edge_confidence).
        relation: The relation type (contributes_to, blocks, etc.).
        target_prevalence: Estimated prevalence of the target node
                          (for induction/abduction s_a/s_b parameter).

    Returns:
        Propagated truth value after applying the inference rule.
    """
    # Construct the edge TV: relation is believed with edge_conf confidence
    edge_tv = TruthValue(strength=edge_conf, confidence=edge_conf)

    rule = RELATION_RULE_MAP.get(relation, "deduction")

    if rule == "deduction":
        result = deduction(source_tv, edge_tv)
    elif rule == "induction":
        result = induction(source_tv, edge_tv, s_a=target_prevalence)
    elif rule == "abduction":
        result = abduction(source_tv, edge_tv, s_b=target_prevalence)
    elif rule == "revision":
        result = revision(source_tv, edge_tv)
    else:
        result = deduction(source_tv, edge_tv)

    return result


# ─── Enhanced Chain Miner ────────────────────────────────────────────

class RuleAwareChainMiner:
    """ChainMiner that uses PLN inference rules for truth-value propagation.

    Unlike the base ChainMiner which uses naive strength*confidence multiplication,
    this miner applies the appropriate PLN inference rule based on the relation type,
    producing more principled and differentiated truth values along chains.
    """

    def __init__(self, data: dict, max_depth: int = 4):
        self.nodes = {}
        self.edges = data.get("edges", [])
        self.max_depth = max_depth

        for key in ("goals", "projects", "tasks", "resources",
                     "results", "constraints"):
            for node in data.get(key, []):
                self.nodes[node["id"]] = node

        self._adjacency = defaultdict(list)
        for e in self.edges:
            self._adjacency[e["from"]].append(e)

        self._tvs = {nid: _initial_tv(node) for nid, node in self.nodes.items()}

        # Estimate prevalence for each node type
        self._prevalence = self._estimate_prevalences()

    def _estimate_prevalences(self) -> dict:
        """Estimate prevalence (base rate) for each node type."""
        type_counts = defaultdict(int)
        type_strengths = defaultdict(list)

        for nid, node in self.nodes.items():
            kind = node.get("kind", "unknown")
            type_counts[kind] += 1
            tv = self._tvs.get(nid)
            if tv:
                type_strengths[kind].append(tv.strength)

        prevalences = {}
        for kind, count in type_counts.items():
            strengths = type_strengths[kind]
            if strengths:
                prevalences[kind] = sum(strengths) / len(strengths)
            else:
                prevalences[kind] = 0.5
        return prevalences

    def _get_prevalence(self, nid: str) -> float:
        """Get estimated prevalence for a node."""
        node = self.nodes.get(nid, {})
        kind = node.get("kind", "unknown")
        return self._prevalence.get(kind, 0.5)

    def _is_goal(self, nid: str) -> bool:
        return self.nodes.get(nid, {}).get("kind") == "goal"

    def find_chains(self, source: str) -> list[dict]:
        """Find all reasoning chains from source to any goal node.

        Returns list of chain dicts with:
          - path: list of node IDs
          - relations: list of relation types
          - tv: final TruthValue after rule-based propagation
          - path_weight: accumulated edge confidence product
          - depth: number of hops
          - rules_applied: list of rule names used
        """
        chains = []
        source_tv = self._tvs.get(source, TruthValue())

        # BFS: (current_node, path, relations, accumulated_tv, path_weight, visited, rules)
        queue = [(source, [source], [], source_tv, 1.0, {source}, [])]

        while queue:
            node, path, rels, tv, weight, visited, rules = queue.pop(0)

            if len(path) - 1 >= self.max_depth:
                continue

            for edge in self._adjacency.get(node, []):
                relation = edge.get("relation", "")
                target = edge.get("to", "")

                if target in visited or target not in self.nodes:
                    continue

                edge_conf = _edge_confidence(edge)
                target_prev = self._get_prevalence(target)

                propagated = propagate_with_rules(
                    tv, edge_conf, relation, target_prevalence=target_prev
                )

                rule_name = RELATION_RULE_MAP.get(relation, "deduction")
                new_weight = weight * edge_conf
                new_path = path + [target]
                new_rels = rels + [relation]
                new_visited = visited | {target}
                new_rules = rules + [rule_name]

                if self._is_goal(target):
                    chains.append({
                        "source": source,
                        "target": target,
                        "path": new_path,
                        "relations": new_rels,
                        "tv": propagated,
                        "path_weight": new_weight,
                        "depth": len(new_path) - 1,
                        "rules_applied": new_rules,
                    })

                queue.append((
                    target, new_path, new_rels, propagated,
                    new_weight, new_visited, new_rules
                ))

        chains.sort(key=lambda c: c["path_weight"], reverse=True)
        return chains

    def find_chains_all_tasks(self) -> dict:
        """Find chains for all active tasks."""
        results = {}
        for nid, node in self.nodes.items():
            if (node.get("kind") == "task" and
                    normalize_status(node.get("status", "active")) == "active"):
                results[nid] = self.find_chains(nid)
        return results


# ─── Chain Comparison ────────────────────────────────────────────────

def compare_propagation(naive_tv: TruthValue, rule_tv: TruthValue) -> dict:
    """Compare naive vs rule-based propagation results.

    Returns a dict with the difference metrics useful for validation.
    """
    return {
        "naive_strength": naive_tv.strength,
        "rule_strength": rule_tv.strength,
        "strength_delta": rule_tv.strength - naive_tv.strength,
        "naive_confidence": naive_tv.confidence,
        "rule_confidence": rule_tv.confidence,
        "confidence_delta": rule_tv.confidence - naive_tv.confidence,
        "rule_more_confident": rule_tv.confidence > naive_tv.confidence,
    }


# ─── Integration with VerdictBridge ──────────────────────────────────

def enhance_relevance_with_rules(
    base_relevance: float,
    rule_based_relevance: float,
    pln_confidence: float,
    w: float = 0.3,
) -> float:
    """Blend heuristic relevance with PLN rule-based relevance.

    Uses the relevance_blend function from pln_inference_rules, but
    operates on raw floats for integration with the verdict bridge.

    Args:
        base_relevance: Heuristic relevance score from the evaluator.
        rule_based_relevance: Relevance computed via rule-aware chains.
        pln_confidence: Confidence of the PLN truth value.
        w: Weight on the PLN rule-based score (0-1).

    Returns:
        Blended relevance score ∈ [0, 1].
    """
    pln_tv = TruthValue(
        strength=rule_based_relevance,
        confidence=pln_confidence,
    )
    blended = relevance_blend(pln_tv, base_relevance, w=w)
    # Clamp to [0, 1]
    return max(0.0, min(1.0, blended.strength))


if __name__ == "__main__":
    import sys
    data = json.load(open(sys.argv[1]))
    miner = RuleAwareChainMiner(data, max_depth=4)
    results = miner.find_chains_all_tasks()
    print(json.dumps(
        {tid: [{"target": c["target"],
                "tv": c["tv"].to_dict(),
                "rules": c["rules_applied"],
                "depth": c["depth"]}
               for c in chains]
         for tid, chains in results.items()},
        indent=2
    ))
