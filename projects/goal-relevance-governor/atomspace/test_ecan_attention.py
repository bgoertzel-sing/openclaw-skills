#!/usr/bin/env python3
"""Tests for ECAN Attention Allocation v0.1."""
import json, sys, os
import unittest

sys.path.insert(0, os.path.dirname(__file__))
from ecan_attention import (
    ECANAttentionAllocator, AttentionValue, ECANResult,
    STI_INITIAL_SCALE, LTI_INITIAL_SCALE, STI_FLOOR,
    STI_DECAY, LTI_DECAY, SPREAD_FACTOR, RENT,
)

REPLAY_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')


def load_episode(fname):
    path = os.path.join(REPLAY_DIR, fname)
    with open(path) as f:
        return json.load(f)


ALL_EPISODES = [
    'episode_01_stale_codegen.json',
    'episode_02_chem_blocking.json',
    'episode_03_premature_hardening.json',
    'episode_04_overengineered_repair.json',
    'episode_05_control_justified_long_running.json',
]


class TestECANAttention(unittest.TestCase):
    """Test ECAN Attention Allocation on all replay episodes."""

    def test_allocator_initializes_attention_for_all_nodes(self):
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                alloc = ECANAttentionAllocator(data)
                node_count = sum(len(data.get(k, [])) for k in
                    ('goals', 'projects', 'tasks', 'resources', 'results', 'constraints'))
                self.assertEqual(len(alloc.attention), node_count,
                    f'{fname}: attention map size mismatch')

    def test_sti_initialized_from_pln_relevance(self):
        """Tasks should get STI from PLN relevance_score."""
        data = load_episode('episode_05_control_justified_long_running.json')
        alloc = ECANAttentionAllocator(data)
        av = alloc.attention['t-run-benchmark']
        self.assertAlmostEqual(av.sti, 92.5, delta=1.0,
            msg='STI should be relevance * STI_INITIAL_SCALE')

    def test_lti_initialized_from_pln_confidence(self):
        """LTI should come from truth_value.confidence (no staleness decay)."""
        from datetime import datetime, timezone
        data = load_episode('episode_02_chem_blocking.json')
        # Use now close to data timestamps so staleness decay doesn't apply
        alloc = ECANAttentionAllocator(data, now=datetime(2026, 8, 2, tzinfo=timezone.utc))
        for nid, av in alloc.attention.items():
            tv = alloc.propagator.tvs[nid]
            expected_lti = tv.confidence * LTI_INITIAL_SCALE
            self.assertAlmostEqual(av.lti, expected_lti, places=4,
                msg=f'{nid}: LTI mismatch')

    def test_lti_staleness_decay(self):
        """Stale nodes (as_of > STALENESS_THRESHOLD_DAYS ago) get decayed LTI."""
        from datetime import datetime, timezone
        from atomspace.ecan_attention import STALENESS_THRESHOLD_DAYS, STALENESS_LTI_DECAY
        data = load_episode('episode_02_chem_blocking.json')
        # g-long-horizon-research: as_of=2026-08-01
        # t-petta-chem: as_of=2026-08-20
        # Fresh: Aug 2 -> g-long is 1 day old (not stale)
        alloc_fresh = ECANAttentionAllocator(data, now=datetime(2026, 8, 2, tzinfo=timezone.utc))
        # Stale: Aug 22 -> g-long is 21 days old (stale), t-petta-chem is 2 days (not stale)
        alloc_stale = ECANAttentionAllocator(data, now=datetime(2026, 8, 22, tzinfo=timezone.utc))
        fresh_av = alloc_fresh.attention['g-long-horizon-research']
        stale_av = alloc_stale.attention['g-long-horizon-research']
        self.assertLess(stale_av.lti, fresh_av.lti,
            msg='Stale node should have lower LTI than fresh')
        self.assertAlmostEqual(stale_av.lti, fresh_av.lti * STALENESS_LTI_DECAY, places=4,
            msg='Stale LTI should be fresh LTI * STALENESS_LTI_DECAY')
        # Non-stale node (t-petta-chem, 2 days old on Aug 22) should be unchanged
        tv = alloc_stale.propagator.tvs['t-petta-chem']
        expected_lti = tv.confidence * LTI_INITIAL_SCALE
        self.assertAlmostEqual(alloc_stale.attention['t-petta-chem'].lti, expected_lti,
            places=4, msg='Non-stale node LTI should equal raw confidence * scale')

    def test_vlti_for_terminal_goals(self):
        """Achieved/terminal/abandoned nodes get VLTI=True."""
        data = load_episode('episode_01_stale_codegen.json')
        alloc = ECANAttentionAllocator(data)
        for nid, av in alloc.attention.items():
            node = alloc.nodes[nid]
            if node.get('status') in ('achieved', 'terminal', 'abandoned'):
                self.assertTrue(av.vlti, f'{nid}: should have VLTI')

    def test_run_returns_result(self):
        data = load_episode('episode_02_chem_blocking.json')
        alloc = ECANAttentionAllocator(data)
        result = alloc.run(cycles=5)
        self.assertIsInstance(result, ECANResult)
        self.assertEqual(result.cycle, 5)

    def test_sti_changes_over_cycles(self):
        """STI should change over time due to decay + rent + spread."""
        data = load_episode('episode_05_control_justified_long_running.json')
        alloc = ECANAttentionAllocator(data)
        initial_sti = alloc.attention['t-run-benchmark'].sti
        alloc.run(cycles=5)
        final_sti = alloc.attention['t-run-benchmark'].sti
        self.assertNotAlmostEqual(initial_sti, final_sti, places=2,
            msg='STI should change over cycles')

    def test_priority_queue_sorted_by_sti(self):
        data = load_episode('episode_02_chem_blocking.json')
        alloc = ECANAttentionAllocator(data)
        result = alloc.run(cycles=3)
        pq = result.priority_queue
        for i in range(len(pq) - 1):
            sti1 = alloc.attention[pq[i]].sti
            sti2 = alloc.attention[pq[i+1]].sti
            self.assertGreaterEqual(sti1, sti2,
                'Priority queue should be sorted by STI descending')

    def test_eviction_candidates_below_floor(self):
        """Nodes with STI < STI_FLOOR should be eviction candidates."""
        data = load_episode('episode_01_stale_codegen.json')
        alloc = ECANAttentionAllocator(data)
        result = alloc.run(cycles=10)
        for nid in result.eviction_candidates:
            av = alloc.attention[nid]
            self.assertLess(av.sti, STI_FLOOR,
                f'{nid}: eviction candidate should have STI < floor')
            self.assertFalse(av.vlti,
                f'{nid}: VLTI nodes should not be eviction candidates')

    def test_high_relevance_task_ranks_higher(self):
        """In ep02, t-restore-agents (rel=0.939) should rank above t-petta-chem (rel=0.246)."""
        data = load_episode('episode_02_chem_blocking.json')
        alloc = ECANAttentionAllocator(data)
        result = alloc.run(cycles=5)
        pq = result.priority_queue
        idx_restore = pq.index('t-restore-agents')
        idx_chem = pq.index('t-petta-chem')
        self.assertLess(idx_restore, idx_chem,
            'High-relevance task should rank above low-relevance task')

    def test_json_export_serializable(self):
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                alloc = ECANAttentionAllocator(data)
                s = alloc.run_to_json(cycles=3)
                d = json.loads(s)
                self.assertEqual(d['cycle'], 3)
                self.assertGreater(len(d['priority_queue']), 0)

    def test_rent_charged_each_cycle(self):
        """Total rent should be RENT * non_vlti_count * cycles."""
        data = load_episode('episode_02_chem_blocking.json')
        alloc = ECANAttentionAllocator(data)
        non_vlti = sum(1 for av in alloc.attention.values() if not av.vlti)
        result = alloc.run(cycles=5)
        self.assertAlmostEqual(result.rent_paid, RENT * non_vlti * 5,
            msg='Rent should be RENT * non_vlti_count * cycles')

    def test_cycles_alive_increments(self):
        data = load_episode('episode_05_control_justified_long_running.json')
        alloc = ECANAttentionAllocator(data)
        alloc.run(cycles=7)
        for av in alloc.attention.values():
            self.assertEqual(av.cycles_alive, 7,
                f'{av.node_id}: cycles_alive should be 7')

    def test_empty_graph_does_not_crash(self):
        """ECAN should handle empty/minimal graphs gracefully."""
        data = {'goals': [], 'tasks': [], 'edges': [], 'resources': []}
        alloc = ECANAttentionAllocator(data)
        result = alloc.run(cycles=3)
        self.assertEqual(len(result.priority_queue), 0)
        self.assertEqual(len(result.eviction_candidates), 0)


    def test_lti_floor_eviction(self):
        """Nodes with LTI below LTI_FLOOR become eviction candidates."""
        from atomspace.ecan_attention import LTI_FLOOR, LTI_INITIAL_SCALE, STALENESS_LTI_DECAY
        from datetime import datetime, timezone
        data = load_episode('episode_02_chem_blocking.json')
        # g-long-horizon-research: as_of=2026-08-01, confidence=0.6
        # On Sept 8 (38 days old), LTI = 0.6 * 100 * 0.5 = 30.0 (above LTI_FLOOR=5)
        # To test LTI_FLOOR eviction, we need a node with very low confidence * staleness
        # Let's use a node with low confidence and high staleness
        # g-long-horizon-research has conf=0.6, so after staleness: 0.6*100*0.5=30
        # That's still above LTI_FLOOR=5. Let's verify it's NOT evicted by LTI alone.
        alloc = ECANAttentionAllocator(data, now=datetime(2026, 9, 8, tzinfo=timezone.utc))
        alloc.run(cycles=30)  # Run enough cycles to drain STI below floor
        # Check that staleness-decayed nodes with low LTI get flagged
        # Nodes with very low confidence would have LTI < LTI_FLOOR after decay
        # g-long-horizon-research: LTI = 30 (not below floor)
        av = alloc.attention['g-long-horizon-research']
        self.assertGreater(av.lti, LTI_FLOOR,
            msg='g-long LTI=30 should be above LTI_FLOOR=5')
        # But if we had a node with conf=0.05, LTI = 0.05*100*0.5 = 2.5 < 5.0
        # Let's verify the eviction logic includes LTI check
        # Create a minimal test: set LTI below floor manually
        av2 = alloc.attention['t-petta-chem']
        original_lti = av2.lti
        av2.lti = 2.0  # Below LTI_FLOOR
        av2.sti = 50.0  # Above STI_FLOOR
        av2.vlti = False
        alloc._step()  # Step to update eviction_candidate
        self.assertTrue(av2.eviction_candidate,
            msg='Node with LTI < LTI_FLOOR should be eviction candidate')
        # Restore
        av2.lti = original_lti


    def test_dynamic_lti_floor_memory_pressure(self):
        """When >20 non-VLTI nodes exist, LTI_FLOOR scales up with memory pressure."""
        data = load_episode('episode_02_chem_blocking.json')
        # Add extra nodes to exceed 20 non-VLTI threshold
        for i in range(15):
            data['tasks'].append({
                'id': f'filler-task-{i}',
                'kind': 'wmtm_test',
                'goal_id': 'g-production-readiness',
                'status': 'pending',
                'confidence': 0.3,
            })
            data.setdefault('edges', []).append({
                'from': 'g-production-readiness',
                'to': f'filler-task-{i}',
                'type': 'subgoal'
            })
        from atomspace.ecan_attention import LTI_FLOOR
        alloc = ECANAttentionAllocator(data)
        alloc.run(cycles=30)
        # With >20 non-VLTI nodes, dynamic floor > base LTI_FLOOR
        n_non_vlti = sum(1 for av in alloc.attention.values() if not av.vlti)
        self.assertGreater(n_non_vlti, 20)
        # Filler tasks with low confidence (0.3) have LTI=30, which should be above
        # the dynamic floor (LTI_FLOOR * (1 + 0.1*(n-20)))
        # With ~30 non-VLTI: floor = 5 * (1 + 0.1*10) = 10.0; LTI=30 > 10, not evicted
        # But after 30 cycles of LTI decay (0.99^30 ≈ 0.74), LTI ≈ 22.2 > 10, still safe
        # Verify dynamic floor is active by checking a filler node is NOT evicted
        filler_av = alloc.attention.get('filler-task-0')
        self.assertIsNotNone(filler_av)
        # The key test: with 20+ nodes, the floor is higher than base 5.0
        # Let's verify by checking a node with LTI between 5 and dynamic floor
        # After 30 cycles: filler LTI ≈ 30 * 0.99^30 ≈ 22.2
        # Dynamic floor with ~30 nodes: 5*(1+0.1*10) = 10.0
        # 22.2 > 10.0 so NOT evicted — correct behavior
        # With LTI=5.3, after decay=5.247, below dynamic 5.5 but above base 5.0
        av_test = alloc.attention['t-petta-chem']
        original_lti = av_test.lti
        av_test.lti = 5.3  # Above base LTI_FLOOR=5, below dynamic floor=5.5
        av_test.sti = 50.0  # Above STI_FLOOR
        av_test.vlti = False
        alloc._step()
        self.assertTrue(av_test.eviction_candidate,
            msg='LTI=5.3->5.247 after decay should be evicted under dynamic floor (5.5) but not static floor (5.0)')
        av_test.lti = original_lti


if __name__ == '__main__':
    unittest.main()
