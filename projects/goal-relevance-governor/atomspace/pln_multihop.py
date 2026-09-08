#!/usr/bin/env python3
"""PLN Multi-Hop Reasoning Chains v0.1
=====================================

Extends the single-hop PLNPropagator with multi-hop probabilistic
reasoning chains. Instead of only propagating evidence along direct
edges (task->goal), this module traces full paths through the graph
and computes path-weighted truth values.

Key concepts:
  - ReasoningChain: a path from a source node to a target goal,
    with accumulated truth value and path weight.
  - ChainMiner: discovers all chains up to max_depth hops.
  - ChainAggregator: combines multiple chains into a final score.
"""

from __future__ import annotations
import json
from dataclasses import dataclass, field, asdict
from typing import Optional
from collections import defaultdict

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from pln_propagation import TruthValue, _edge_confidence, _initial_tv


@dataclass
class ReasoningChain:
    """A single reasoning path from source to target."""
    source: str
    target: str
    path: list[str]
    relations: list[str]
    tv: TruthValue
    path_weight: float
    depth: int

    def to_dict(self) -> dict:
        return {
            'source': self.source,
            'target': self.target,
            'path': self.path,
            'relations': self.relations,
            'tv': self.tv.to_dict(),
            'path_weight': round(self.path_weight, 4),
            'depth': self.depth,
        }


@dataclass
class MultiHopResult:
    """Result of multi-hop reasoning for a single task."""
    task_id: str
    chains: list[ReasoningChain] = field(default_factory=list)
    aggregated_relevance: float = 0.0
    aggregated_tv: TruthValue = field(default_factory=TruthValue)
    goal_coverage: list[str] = field(default_factory=list)
    max_depth_reached: int = 0

    def to_dict(self) -> dict:
        return {
            'task_id': self.task_id,
            'chain_count': len(self.chains),
            'chains': [c.to_dict() for c in self.chains],
            'aggregated_relevance': round(self.aggregated_relevance, 4),
            'aggregated_tv': self.aggregated_tv.to_dict(),
            'goal_coverage': self.goal_coverage,
            'max_depth_reached': self.max_depth_reached,
        }


class ChainMiner:
    """Discovers multi-hop reasoning chains in the graph."""

    def __init__(self, data: dict):
        self.nodes = {}
        self.edges = data.get('edges', [])
        for key in ('goals', 'projects', 'tasks', 'resources',
                     'results', 'constraints'):
            for node in data.get(key, []):
                self.nodes[node['id']] = node
        self._adjacency = defaultdict(list)
        for e in self.edges:
            self._adjacency[e['from']].append(e)
        self._tvs = {nid: _initial_tv(node) for nid, node in self.nodes.items()}

    def _is_goal(self, nid: str) -> bool:
        return self.nodes.get(nid, {}).get('kind') == 'goal'

    def find_chains(self, source: str, max_depth: int = 4) -> list[ReasoningChain]:
        """Find all reasoning chains from source to any goal node via BFS."""
        chains: list[ReasoningChain] = []
        source_tv = self._tvs.get(source, TruthValue())
        queue = [(source, [source], [], source_tv, 1.0, {source})]

        while queue:
            node, path, rels, tv, weight, path_visited = queue.pop(0)

            if len(path) - 1 >= max_depth:
                continue

            for edge in self._adjacency.get(node, []):
                relation = edge.get('relation', '')
                target = edge.get('to', '')

                if target in path_visited:
                    continue
                if target not in self.nodes:
                    continue

                edge_conf = _edge_confidence(edge)
                new_weight = weight * edge_conf
                propagated = TruthValue(
                    strength=tv.strength * edge_conf,
                    confidence=tv.confidence * edge_conf,
                )

                new_path = path + [target]
                new_rels = rels + [relation]
                new_visited = path_visited | {target}

                if self._is_goal(target):
                    chain = ReasoningChain(
                        source=source,
                        target=target,
                        path=new_path,
                        relations=new_rels,
                        tv=propagated,
                        path_weight=new_weight,
                        depth=len(new_path) - 1,
                    )
                    chains.append(chain)

                queue.append((
                    target, new_path, new_rels, propagated,
                    new_weight, new_visited
                ))

        chains.sort(key=lambda c: c.path_weight, reverse=True)
        return chains

    def find_chains_all_tasks(self, max_depth: int = 4) -> dict[str, list[ReasoningChain]]:
        """Find chains for all active tasks in the graph."""
        results = {}
        for nid, node in self.nodes.items():
            if node.get('kind') == 'task' and node.get('status') == 'active':
                results[nid] = self.find_chains(nid, max_depth=max_depth)
        return results


class ChainAggregator:
    """Aggregates multiple reasoning chains into a single relevance score."""

    @staticmethod
    def aggregate(chains: list[ReasoningChain]) -> tuple[float, TruthValue]:
        """Aggregate chains using probabilistic OR for strength, and
        confidence-weighted sum for overall relevance.

        Returns (relevance_score, aggregated_truth_value).
        """
        if not chains:
            return 0.0, TruthValue()

        # OR-combine all chain truth values for strength
        agg_tv = TruthValue()
        for c in chains:
            agg_tv = agg_tv.combine_disjunction(c.tv)

        # Relevance: sum of path_weight * tv.strength * tv.confidence,
        # normalized by total path weight
        total_weight = sum(c.path_weight for c in chains)
        if total_weight > 0:
            relevance = sum(
                c.path_weight * c.tv.strength * c.tv.confidence
                for c in chains
            ) / total_weight
        else:
            relevance = 0.0

        return relevance, agg_tv

    @staticmethod
    def aggregate_to_result(task_id: str,
                            chains: list[ReasoningChain]) -> MultiHopResult:
        """Build a full MultiHopResult from chains."""
        if not chains:
            return MultiHopResult(task_id=task_id)

        relevance, agg_tv = ChainAggregator.aggregate(chains)

        goal_coverage = list(set(c.target for c in chains))
        max_depth = max(c.depth for c in chains)

        return MultiHopResult(
            task_id=task_id,
            chains=chains,
            aggregated_relevance=relevance,
            aggregated_tv=agg_tv,
            goal_coverage=goal_coverage,
            max_depth_reached=max_depth,
        )


class MultiHopEvaluator:
    """Full multi-hop evaluation across all tasks in a graph.

    Combines ChainMiner and ChainAggregator to produce a complete
    multi-hop reasoning result for every active task.
    """

    def __init__(self, data: dict, max_depth: int = 4):
        self.data = data
        self.max_depth = max_depth
        self.miner = ChainMiner(data)

    def evaluate(self) -> dict[str, MultiHopResult]:
        """Evaluate all active tasks and return per-task results."""
        results = {}
        task_chains = self.miner.find_chains_all_tasks(max_depth=self.max_depth)

        for task_id, chains in task_chains.items():
            results[task_id] = ChainAggregator.aggregate_to_result(task_id, chains)

        return results

    def evaluate_to_json(self) -> str:
        """Evaluate and return JSON string."""
        results = self.evaluate()
        return json.dumps(
            {tid: r.to_dict() for tid, r in results.items()},
            indent=2
        )


if __name__ == '__main__':
    import sys
    data = json.load(open(sys.argv[1]))
    evaluator = MultiHopEvaluator(data, max_depth=4)
    print(evaluator.evaluate_to_json())
