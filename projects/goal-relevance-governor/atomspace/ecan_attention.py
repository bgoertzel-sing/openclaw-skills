#!/usr/bin/env python3
"""ECAN Attention Allocation v0.1
================================

Economic Constraint Attention Network (ECAN) layer that uses PLN relevance
scores to allocate attention values (STI/LTI) across graph nodes.

In OpenCog's ECAN, nodes compete for attention via economic dynamics:
  - STI (Short-Term Importance): transient, decays over cycles
  - LTI (Long-Term Importance): persistent, updated slowly
  - VLTI (Very Long-Term Importance): boolean, grants rent-free status

Here we adapt this to the Goal Relevance Graph:
  - STI is initialized from PLN relevance_score (immediate salience)
  - LTI is initialized from truth_value.confidence (evidence quality)
  - Attention flows along edges: high-STI nodes spread attention to neighbors
  - An attention rent is charged each cycle (STI decays)
  - Nodes below STI_FLOOR become candidates for eviction (deferral)

The output is an attention map that can be used to:
  1. Prioritize which tasks to work on (highest STI first)
  2. Decide which goals to keep active (LTI threshold)
  3. Identify nodes that should be evicted from working memory (STI < floor)

This is exploratory — demonstrates how PLN continuous values map to
attention-based resource allocation.
"""

from __future__ import annotations
import json
from dataclasses import dataclass, field, asdict
from typing import Optional
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'evaluator'))
sys.path.insert(0, os.path.dirname(__file__))

from pln_propagation import PLNPropagator, TruthValue
from datetime import datetime, timezone
from pln_propagation import normalize_status

# Staleness settings (mirrors pln_verdict_bridge.py)
STALENESS_THRESHOLD_DAYS = 14
STALENESS_LTI_DECAY = 0.5  # stale nodes get LTI * 0.5


# --- Configuration ---

STI_INITIAL_SCALE = 100.0     # PLN relevance [0,1] -> STI [0, 100]
LTI_INITIAL_SCALE = 100.0     # PLN confidence [0,1] -> LTI [0, 100]
STI_FLOOR = 10.0              # Below this, node is a deferral candidate
LTI_FLOOR = 5.0               # Below this LTI, stale nodes face eviction
STI_DECAY = 0.95              # Per-cycle STI decay multiplier
LTI_DECAY = 0.99              # Per-cycle LTI decay (slower)
SPREAD_FACTOR = 0.15          # Fraction of STI spread to neighbors per cycle
RENT = 1.0                    # STI rent charged per cycle


@dataclass
class AttentionValue:
    """ECAN attention value for a single node."""
    node_id: str
    node_kind: str
    sti: float                    # Short-Term Importance
    lti: float                    # Long-Term Importance
    vlti: bool = False            # Very Long-Term Importance (rent-free)
    cycles_alive: int = 0         # How many ECAN cycles this node has survived
    eviction_candidate: bool = False

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class ECANResult:
    """Full ECAN evaluation result."""
    cycle: int
    total_sti: float
    attention_map: dict           # node_id -> AttentionValue
    priority_queue: list          # sorted by STI descending
    eviction_candidates: list     # node_ids below STI floor
    rent_paid: float
    spread_amount: float

    def to_dict(self) -> dict:
        return {
            "cycle": self.cycle,
            "total_sti": round(self.total_sti, 2),
            "priority_queue": [
                {"node_id": nid, "sti": round(self.attention_map[nid].sti, 2),
                 "lti": round(self.attention_map[nid].lti, 2),
                 "kind": self.attention_map[nid].node_kind}
                for nid in self.priority_queue
            ],
            "eviction_candidates": self.eviction_candidates,
            "rent_paid": round(self.rent_paid, 2),
            "spread_amount": round(self.spread_amount, 2),
        }


class ECANAttentionAllocator:
    """Allocate and dynamics attention values using PLN relevance scores.

    Usage:
        allocator = ECANAttentionAllocator(graph_data)
        result = allocator.run(cycles=5)
        for entry in result.priority_queue:
            print(entry)
    """

    def __init__(self, data: dict, now: datetime | None = None):
        """Initialize ECAN allocator.

        Args:
            data: Goal relevance graph data.
            now: Optional reference timestamp for staleness detection.
                 If provided, nodes older than STALENESS_THRESHOLD_DAYS get
                 their LTI decayed by STALENESS_LTI_DECAY, making them more
                 likely to become eviction candidates over time.
        """
        self.data = data
        self._now = now or datetime.now(timezone.utc)
        self.propagator = PLNPropagator(data)
        self._pln_result = self.propagator.evaluate()
        self._pln_tasks = {t["task_id"]: t for t in self._pln_result.get("tasks", [])}

        # Build node index
        self.nodes = {}
        for key in ("goals", "projects", "tasks", "resources", "results", "constraints"):
            for node in data.get(key, []):
                self.nodes[node["id"]] = node

        self.edges = data.get("edges", [])

        # Initialize attention values
        self.attention = {}
        self._init_attention()

        self.cycle = 0

    def _init_attention(self):
        """Initialize STI/LTI from PLN truth values."""
        for nid, node in self.nodes.items():
            tv = self.propagator.tvs.get(nid, TruthValue(0.5, 0.5))

            # Tasks get STI from PLN relevance_score
            if nid in self._pln_tasks:
                sti = self._pln_tasks[nid]["relevance_score"] * STI_INITIAL_SCALE
            else:
                # Non-task nodes: STI from strength
                sti = tv.strength * STI_INITIAL_SCALE

            # Apply staleness decay to LTI
            lti = tv.confidence * LTI_INITIAL_SCALE
            as_of = node.get("as_of")
            if as_of:
                try:
                    ts = datetime.fromisoformat(as_of.replace("Z", "+00:00"))
                    age_days = (self._now - ts).days
                    if age_days > STALENESS_THRESHOLD_DAYS:
                        lti *= STALENESS_LTI_DECAY
                except (ValueError, TypeError):
                    pass  # Unparseable timestamp, skip staleness

            # VLTI for terminal/achieved goals (rent-free)
            vlti = normalize_status(node.get("status", "active")) in ("achieved", "cancelled")

            self.attention[nid] = AttentionValue(
                node_id=nid,
                node_kind=node.get("kind", "unknown"),
                sti=sti,
                lti=lti,
                vlti=vlti,
            )

    def _neighbors(self, nid: str) -> list:
        """Get neighbor node IDs (both directions)."""
        neighbors = set()
        for edge in self.edges:
            if edge["from"] == nid:
                neighbors.add(edge["to"])
            elif edge["to"] == nid:
                neighbors.add(edge["from"])
        return list(neighbors)

    def _step(self):
        """Run one ECAN cycle: rent, decay, spread.

        Returns (total_rent, total_spread).
        """
        self.cycle += 1
        total_rent = 0.0
        total_spread = 0.0

        # 1. Charge rent (except VLTI nodes)
        for nid, av in self.attention.items():
            if not av.vlti:
                av.sti -= RENT
                total_rent += RENT

        # 2. STI decay
        for nid, av in self.attention.items():
            av.sti *= STI_DECAY
            av.lti *= LTI_DECAY
            av.cycles_alive += 1

        # 3. Attention spreading
        spread_amounts = {}
        for nid, av in self.attention.items():
            if av.sti <= 0:
                continue
            neighbors = self._neighbors(nid)
            if not neighbors:
                continue
            per_neighbor = (av.sti * SPREAD_FACTOR) / len(neighbors)
            for nb_id in neighbors:
                if nb_id in self.attention:
                    spread_amounts[nb_id] = spread_amounts.get(nb_id, 0) + per_neighbor
                    total_spread += per_neighbor

        # Deduct from senders
        for nid, av in self.attention.items():
            if av.sti > 0:
                neighbors = self._neighbors(nid)
                if neighbors:
                    av.sti -= av.sti * SPREAD_FACTOR

        # Add to receivers
        for nid, amount in spread_amounts.items():
            self.attention[nid].sti += amount

        # 4. Update eviction candidates
        # Dynamic LTI floor: scales with number of non-VLTI nodes (memory pressure)
        n_non_vlti = sum(1 for av in self.attention.values() if not av.vlti)
        if n_non_vlti > 20:
            dynamic_lti_floor = LTI_FLOOR * (1.0 + 0.1 * (n_non_vlti - 20))
        else:
            dynamic_lti_floor = LTI_FLOOR
        for nid, av in self.attention.items():
            av.eviction_candidate = (av.sti < STI_FLOOR or av.lti < dynamic_lti_floor) and not av.vlti

        return total_rent, total_spread

    def run(self, cycles: int = 5) -> ECANResult:
        """Run ECAN dynamics for N cycles."""
        total_rent = 0.0
        total_spread = 0.0
        for _ in range(cycles):
            rent, spread = self._step()
            total_rent += rent
            total_spread += spread

        return self._build_result(total_rent, total_spread)

    def _build_result(self, rent: float, spread: float) -> ECANResult:
        """Build the final ECANResult."""
        total_sti = sum(av.sti for av in self.attention.values())

        # Priority queue: sort by STI descending
        priority = sorted(
            self.attention.keys(),
            key=lambda nid: self.attention[nid].sti,
            reverse=True
        )

        eviction = [
            nid for nid, av in self.attention.items()
            if av.eviction_candidate
        ]

        return ECANResult(
            cycle=self.cycle,
            total_sti=round(total_sti, 2),
            attention_map=self.attention,
            priority_queue=priority,
            eviction_candidates=eviction,
            rent_paid=rent,
            spread_amount=spread,
        )

    def run_to_json(self, cycles: int = 5) -> str:
        """Run and return JSON string."""
        result = self.run(cycles)
        return json.dumps(result.to_dict(), indent=2)


if __name__ == "__main__":
    import sys
    data = json.load(open(sys.argv[1]))
    allocator = ECANAttentionAllocator(data)
    print(allocator.run_to_json(int(sys.argv[2]) if len(sys.argv) > 2 else 5))
