#!/usr/bin/env python3
"""PLN Inference-Enhanced Multi-Hop Reasoning v0.1
===================================================

Integrates the inference-rule-aware propagation from
pln_inference_propagation into the multi-hop ChainMiner pipeline.

This replaces the naive strength*confidence multiplication in
ChainMiner.find_chains() with rule-appropriate propagation:
  - deduction for transitive edges (contributes_to, part_of)
  - revision for evidential edges (provides_evidence_for)
  - abduction for backward edges (supersedes)
  - inhibitory for blocking edges (blocks, occupies)

The enhanced miner also aggregates chains to the same goal using
PLN revision instead of simple disjunction.
"""

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from dataclasses import dataclass, field
from collections import defaultdict
from typing import Optional

from pln_propagation import (
    TruthValue, _edge_confidence, _initial_tv, normalize_status,
)
from pln_inference_rules import deduction, revision
from pln_inference_propagation import (
    select_inference_rule, propagate_edge,
    aggregate_chains_by_revision, InferenceRuleStats,
)
from pln_multihop import (
    ReasoningChain, MultiHopResult, ChainAggregator,
)


class InferenceEnhancedChainMiner:
    """ChainMiner variant that uses PLN inference rules for propagation.

    Drop-in replacement for ChainMiner.find_chains() with the same
    interface, but internally uses propagate_edge() instead of naive
    multiplication.
    """

    def __init__(self, data: dict):
        self.nodes = {}
        self.edges = data.get("edges", [])
        for key in ("goals", "projects", "tasks", "resources",
                     "results", "constraints"):
            for node in data.get(key, []):
                self.nodes[node["id"]] = node
        self._adjacency = defaultdict(list)
        for e in self.edges:
            self._adjacency[e["from"]].append(e)
        self._tvs = {nid: _initial_tv(node) for nid, node in self.nodes.items()}
        self.stats = InferenceRuleStats()

    def _is_goal(self, nid: str) -> bool:
        return self.nodes.get(nid, {}).get("kind") == "goal"

    def find_chains(self, source: str, max_depth: int = 4) -> list[ReasoningChain]:
        """Find all reasoning chains using PLN inference rules.

        Same interface as ChainMiner.find_chains() but uses
        propagate_edge() for truth value propagation along edges.
        """
        chains: list[ReasoningChain] = []
        source_tv = self._tvs.get(source, TruthValue())
        queue = [(source, [source], [], source_tv, 1.0, {source})]

        while queue:
            node, path, rels, tv, weight, path_visited = queue.pop(0)

            if len(path) - 1 >= max_depth:
                continue

            for edge in self._adjacency.get(node, []):
                relation = edge.get("relation", "")
                target = edge.get("to", "")

                if target in path_visited:
                    continue
                if target not in self.nodes:
                    continue

                # Record rule usage
                self.stats.record(relation)

                edge_conf = _edge_confidence(edge)

                # Use inference-rule-aware propagation
                propagated = propagate_edge(tv, edge, edge_conf=edge_conf)

                new_weight = weight * edge_conf
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
                    new_weight, new_visited,
                ))

        chains.sort(key=lambda c: c.path_weight, reverse=True)
        return chains

    def find_chains_aggregated(
        self, source: str, max_depth: int = 4
    ) -> tuple[list[ReasoningChain], TruthValue]:
        """Find chains and aggregate them using PLN revision.

        Returns (chains, aggregated_truth_value).
        """
        chains = self.find_chains(source, max_depth=max_depth)
        agg_tv = aggregate_chains_by_revision(chains)
        return chains, agg_tv

    def find_chains_all_tasks(
        self, max_depth: int = 4
    ) -> dict[str, list[ReasoningChain]]:
        """Find chains for all active tasks."""
        results = {}
        for nid, node in self.nodes.items():
            if (node.get("kind") == "task"
                    and normalize_status(node.get("status", "active")) == "active"):
                results[nid] = self.find_chains(nid, max_depth=max_depth)
        return results

    def get_stats(self) -> dict:
        """Return inference rule usage statistics."""
        return self.stats.to_dict()


class InferenceEnhancedMultiHopEvaluator:
    """Multi-hop evaluator using inference-enhanced chain mining.

    Drop-in replacement for MultiHopEvaluator that uses
    InferenceEnhancedChainMiner instead of ChainMiner.
    """

    def __init__(self, data: dict, max_depth: int = 4):
        self.data = data
        self.max_depth = max_depth
        self.miner = InferenceEnhancedChainMiner(data)

    def evaluate(self) -> dict[str, MultiHopResult]:
        """Evaluate all active tasks with inference-enhanced chains."""
        results = {}
        task_chains = self.miner.find_chains_all_tasks(
            max_depth=self.max_depth
        )
        for task_id, chains in task_chains.items():
            results[task_id] = ChainAggregator.aggregate_to_result(
                task_id, chains
            )
        return results

    def evaluate_enhanced(self) -> dict[str, dict]:
        """Evaluate with revision-based aggregation.

        Returns dict mapping task_id to {chains, aggregated_tv, stats}.
        """
        results = {}
        task_chains = self.miner.find_chains_all_tasks(
            max_depth=self.max_depth
        )
        for task_id, chains in task_chains.items():
            agg_tv = aggregate_chains_by_revision(chains)
            relevance, _ = ChainAggregator.aggregate(chains)
            results[task_id] = {
                "chain_count": len(chains),
                "aggregated_tv": agg_tv.to_dict(),
                "relevance_score": round(relevance, 4),
                "goal_coverage": list(set(c.target for c in chains)),
                "max_depth": max((c.depth for c in chains), default=0),
            }
        return results

    def get_inference_stats(self) -> dict:
        """Return statistics about which inference rules were used."""
        return self.miner.get_stats()


    def evaluate_conflicts(self) -> list[dict]:
        """Find resource conflict chains across all tasks.
        
        Delegates to ChainMiner for conflict detection since conflicts
        are based on resource occupation patterns, not inference rules.
        """
        from pln_multihop import ChainMiner
        miner = ChainMiner(self.data)
        return miner.find_conflict_chains(max_depth=self.max_depth)

    def evaluate_to_json(self) -> str:
        """Evaluate and return JSON string."""
        import json
        results = self.evaluate_enhanced()
        stats = self.get_inference_stats()
        output = {"tasks": results, "inference_stats": stats}
        return json.dumps(output, indent=2)
