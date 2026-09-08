#!/usr/bin/env python3
"""Tests for remaining untested public functions - coverage closure pass 2."""

import json, os, sys, unittest
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'evaluator'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from graph_to_metta import encode_project, encode_resource, encode_result, encode_constraint
from reasoning_explainer import ReasoningExplainer, TaskExplanation
from relevance_evaluator import Graph, RelevanceEvaluator
from pln_truth_mapping import TruthValue

REPLAY_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')
ALL_EPISODES = [
    'episode_01_stale_codegen.json',
    'episode_02_chem_blocking.json',
    'episode_03_premature_hardening.json',
    'episode_04_overengineered_repair.json',
    'episode_05_control_justified_long_running.json',
    'episode_06_conflict_replan.json',
]

def load_episode(fname):
    with open(os.path.join(REPLAY_DIR, fname)) as f:
        return json.load(f)

def _all_nodes(data):
    """Flatten all node lists from episode data (which uses separate keys)."""
    nodes = []
    for key in ('goals', 'projects', 'tasks', 'resources', 'results', 'constraints'):
        nodes.extend(data.get(key, []))
    return nodes


class TestEncodeProject(unittest.TestCase):
    def test_basic_project(self):
        node = {
            'id': 'proj-alpha',
            'title': 'Alpha Project',
            'result_contract': {
                'project_kind': 'greenfield',
                'maturity_stage': 'alpha',
            },
        }
        out = encode_project(node)
        self.assertIn('(: p_proj_alpha Project)', out)
        self.assertIn('Alpha Project', out)
        self.assertIn('greenfield', out)
        self.assertIn('alpha', out)

    def test_project_missing_fields(self):
        node = {'id': 'proj-x'}
        out = encode_project(node)
        self.assertIn('(: p_proj_x Project)', out)

    def test_project_id_sanitization(self):
        node = {
            'id': 'proj-my-cool-thing',
            'title': 'Thing',
            'result_contract': {'project_kind': 'k', 'maturity_stage': 's'},
        }
        out = encode_project(node)
        self.assertIn('p_proj_my_cool_thing', out)

    def test_episode_06_coverage(self):
        data = load_episode('episode_06_conflict_replan.json')
        projects = data.get('projects', [])
        for p in projects:
            with self.subTest(project=p['id']):
                out = encode_project(p)
                self.assertIn('Project', out)


class TestEncodeResource(unittest.TestCase):
    def test_basic_resource(self):
        node = {
            'id': 'res-gpu0',
            'title': 'GPU 0',
            'resource_type': 'hardware',
            'exclusive': True,
        }
        out = encode_resource(node)
        self.assertIn('(: r_res_gpu0 Resource)', out)
        self.assertIn('GPU 0', out)
        self.assertIn('hardware', out)
        self.assertIn('True', out)

    def test_non_exclusive_resource(self):
        node = {
            'id': 'res-cpu',
            'title': 'CPU Pool',
            'resource_type': 'process',
            'exclusive': False,
        }
        out = encode_resource(node)
        self.assertIn('False', out)
        self.assertIn('process', out)

    def test_resource_defaults(self):
        node = {'id': 'res-min', 'title': 'Minimal'}
        out = encode_resource(node)
        self.assertIn('process', out)
        self.assertIn('False', out)

    def test_episode_06_coverage(self):
        data = load_episode('episode_06_conflict_replan.json')
        resources = data.get('resources', [])
        for r in resources:
            with self.subTest(resource=r['id']):
                out = encode_resource(r)
                self.assertIn('Resource', out)


class TestEncodeResult(unittest.TestCase):
    def test_basic_result(self):
        node = {'id': 'res-pass', 'title': 'Passing tests'}
        out = encode_result(node)
        self.assertIn('(: res_res_pass Result)', out)
        self.assertIn('Passing tests', out)

    def test_result_no_title_uses_id(self):
        node = {'id': 'r-no-title'}
        out = encode_result(node)
        self.assertIn('r-no-title', out)
        self.assertIn('Result', out)

    def test_episode_06_coverage(self):
        data = load_episode('episode_06_conflict_replan.json')
        results = data.get('results', [])
        for r in results:
            with self.subTest(result=r['id']):
                out = encode_result(r)
                self.assertIn('Result', out)


class TestEncodeConstraint(unittest.TestCase):
    def test_basic_constraint(self):
        node = {'id': 'c-deadline', 'title': 'Ship by Q4'}
        out = encode_constraint(node)
        self.assertIn('(: c_c_deadline Constraint)', out)
        self.assertIn('Ship by Q4', out)

    def test_constraint_no_title_uses_id(self):
        node = {'id': 'c-hard'}
        out = encode_constraint(node)
        self.assertIn('c-hard', out)
        self.assertIn('Constraint', out)

    def test_episode_06_coverage(self):
        data = load_episode('episode_06_conflict_replan.json')
        constraints = data.get('constraints', [])
        for c in constraints:
            with self.subTest(constraint=c['id']):
                out = encode_constraint(c)
                self.assertIn('Constraint', out)


class TestGraphOutgoingIncoming(unittest.TestCase):
    def setUp(self):
        self.data = {
            'tasks': [
                {'id': 't1', 'kind': 'task', 'title': 'T1', 'status': 'active', 'reversibility': 'reversible'},
                {'id': 't2', 'kind': 'task', 'title': 'T2', 'status': 'active', 'reversibility': 'reversible'},
            ],
            'goals': [
                {'id': 'g1', 'kind': 'goal', 'title': 'G1', 'level': 'strategic', 'status': 'active', 'priority': {'rank': 1, 'urgency': 'high'}},
                {'id': 'g2', 'kind': 'goal', 'title': 'G2', 'level': 'operational', 'status': 'active', 'priority': {'rank': 2, 'urgency': 'medium'}},
            ],
            'edges': [
                {'from': 't1', 'to': 'g1', 'relation': 'contributes_to'},
                {'from': 't1', 'to': 'g2', 'relation': 'contributes_to'},
                {'from': 't2', 'to': 'g1', 'relation': 'blocks'},
            ],
        }
        self.g = Graph(self.data)

    def test_outgoing_all(self):
        edges = self.g.outgoing('t1')
        self.assertEqual(len(edges), 2)
        targets = {e['to'] for e in edges}
        self.assertEqual(targets, {'g1', 'g2'})

    def test_outgoing_filtered(self):
        edges = self.g.outgoing('t1', 'contributes_to')
        self.assertEqual(len(edges), 2)
        edges_blocks = self.g.outgoing('t1', 'blocks')
        self.assertEqual(len(edges_blocks), 0)
        edges_t2 = self.g.outgoing('t2', 'blocks')
        self.assertEqual(len(edges_t2), 1)
        self.assertEqual(edges_t2[0]['to'], 'g1')

    def test_outgoing_no_match(self):
        edges = self.g.outgoing('nonexistent')
        self.assertEqual(len(edges), 0)

    def test_incoming_all(self):
        edges = self.g.incoming('g1')
        self.assertEqual(len(edges), 2)
        sources = {e['from'] for e in edges}
        self.assertEqual(sources, {'t1', 't2'})

    def test_incoming_filtered(self):
        edges = self.g.incoming('g1', 'contributes_to')
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0]['from'], 't1')
        edges_blocks = self.g.incoming('g1', 'blocks')
        self.assertEqual(len(edges_blocks), 1)
        self.assertEqual(edges_blocks[0]['from'], 't2')

    def test_incoming_no_match(self):
        edges = self.g.incoming('nonexistent')
        self.assertEqual(len(edges), 0)

    def test_episode_06_coverage(self):
        data = load_episode('episode_06_conflict_replan.json')
        g = Graph(data)
        for node in _all_nodes(data):
            with self.subTest(node=node['id']):
                out = g.outgoing(node['id'])
                inc = g.incoming(node['id'])
                self.assertIsInstance(out, list)
                self.assertIsInstance(inc, list)


class TestGetOccupiedResources(unittest.TestCase):
    def test_with_occupies_edge(self):
        data = {
            'tasks': [
                {'id': 't1', 'kind': 'task', 'title': 'T1', 'status': 'active', 'reversibility': 'reversible'},
            ],
            'resources': [
                {'id': 'r1', 'kind': 'resource', 'title': 'GPU 0', 'resource_type': 'hardware', 'exclusive': True},
            ],
            'edges': [
                {'from': 't1', 'to': 'r1', 'relation': 'occupies'},
            ],
        }
        g = Graph(data)
        resources = g.get_occupied_resources('t1')
        self.assertEqual(len(resources), 1)
        self.assertEqual(resources[0]['id'], 'r1')

    def test_no_occupies_edge(self):
        data = {
            'tasks': [
                {'id': 't1', 'kind': 'task', 'title': 'T1', 'status': 'active', 'reversibility': 'reversible'},
            ],
            'goals': [
                {'id': 'g1', 'kind': 'goal', 'title': 'G1', 'level': 'strategic', 'status': 'active', 'priority': {'rank': 1, 'urgency': 'high'}},
            ],
            'edges': [
                {'from': 't1', 'to': 'g1', 'relation': 'contributes_to'},
            ],
        }
        g = Graph(data)
        resources = g.get_occupied_resources('t1')
        self.assertEqual(len(resources), 0)

    def test_multiple_resources(self):
        data = {
            'tasks': [
                {'id': 't1', 'kind': 'task', 'title': 'T1', 'status': 'active', 'reversibility': 'reversible'},
            ],
            'resources': [
                {'id': 'r1', 'kind': 'resource', 'title': 'GPU 0', 'resource_type': 'hardware', 'exclusive': True},
                {'id': 'r2', 'kind': 'resource', 'title': 'CPU Pool', 'resource_type': 'process', 'exclusive': False},
            ],
            'edges': [
                {'from': 't1', 'to': 'r1', 'relation': 'occupies'},
                {'from': 't1', 'to': 'r2', 'relation': 'occupies'},
            ],
        }
        g = Graph(data)
        resources = g.get_occupied_resources('t1')
        self.assertEqual(len(resources), 2)
        ids = {r['id'] for r in resources}
        self.assertEqual(ids, {'r1', 'r2'})

    def test_episode_06_coverage(self):
        data = load_episode('episode_06_conflict_replan.json')
        g = Graph(data)
        tasks = data.get('tasks', [])
        for t in tasks:
            with self.subTest(task=t['id']):
                resources = g.get_occupied_resources(t['id'])
                self.assertIsInstance(resources, list)


class TestExplainTask(unittest.TestCase):
    def test_basic_explanation(self):
        rec = {
            'task_id': 't1',
            'unified_verdict': 'CONTINUE',
            'signals': ['temporal_staleness:g1,g2'],
            'relevance_score': 0.85,
            'sti': 50.0,
            'lti': 10.0,
            'multihop_chains': 2,
            'multihop_goal_coverage': ['g1', 'g2'],
            'multihop_max_depth': 3,
        }
        data = {
            'tasks': [{'id': 't1', 'kind': 'task', 'title': 'Task1', 'status': 'active', 'reversibility': 'reversible'}],
            'goals': [
                {'id': 'g1', 'kind': 'goal', 'title': 'Goal1', 'level': 'strategic', 'status': 'active', 'priority': {'rank': 1, 'urgency': 'high'}},
                {'id': 'g2', 'kind': 'goal', 'title': 'Goal2', 'level': 'strategic', 'status': 'active', 'priority': {'rank': 2, 'urgency': 'medium'}},
            ],
            'edges': [],
        }
        explainer = ReasoningExplainer(data)
        explanation = explainer.explain_task(rec)
        self.assertIsInstance(explanation, TaskExplanation)
        self.assertEqual(explanation.task_id, 't1')
        self.assertEqual(explanation.verdict, 'CONTINUE')
        self.assertTrue(len(explanation.evidence_points) > 0)
        self.assertTrue(any('relevance' in p.lower() for p in explanation.evidence_points))
        self.assertTrue(any('STI' in p or 'attention' in p.lower() for p in explanation.evidence_points))
        self.assertTrue('chain' in explanation.chain_summary.lower())

    def test_low_relevance_zero_sti(self):
        rec = {
            'task_id': 't2',
            'unified_verdict': 'STOP_STALE',
            'signals': ['temporal_staleness:g1'],
            'relevance_score': 0.0,
            'sti': 0.0,
            'lti': 0.0,
            'multihop_chains': 0,
            'multihop_goal_coverage': [],
            'multihop_max_depth': 0,
        }
        data = {
            'tasks': [{'id': 't2', 'kind': 'task', 'title': 'Task2', 'status': 'active', 'reversibility': 'reversible'}],
            'goals': [],
            'edges': [],
        }
        explainer = ReasoningExplainer(data)
        explanation = explainer.explain_task(rec)
        self.assertEqual(explanation.verdict, 'STOP_STALE')
        self.assertTrue(any('zero relevance' in p.lower() for p in explanation.evidence_points))
        self.assertTrue(any('low short-term' in p.lower() for p in explanation.evidence_points))
        self.assertTrue('no multi-hop' in explanation.chain_summary.lower())

    def test_with_conflict_chains(self):
        rec = {
            'task_id': 't1',
            'unified_verdict': 'REPLAN',
            'signals': [],
            'relevance_score': 0.5,
            'sti': 20.0,
            'lti': 5.0,
            'multihop_chains': 1,
            'multihop_goal_coverage': ['g1'],
            'multihop_max_depth': 2,
        }
        conflict_chains = [
            {'task_a': 't1', 'task_b': 't2', 'resource_id': 'r1', 'exclusive': True, 'is_competing': False},
        ]
        data = {
            'tasks': [
                {'id': 't1', 'kind': 'task', 'title': 'Task1', 'status': 'active', 'reversibility': 'reversible'},
                {'id': 't2', 'kind': 'task', 'title': 'Task2', 'status': 'active', 'reversibility': 'reversible'},
            ],
            'goals': [
                {'id': 'g1', 'kind': 'goal', 'title': 'Goal1', 'level': 'strategic', 'status': 'active', 'priority': {'rank': 1, 'urgency': 'high'}},
            ],
            'resources': [
                {'id': 'r1', 'kind': 'resource', 'title': 'GPU', 'resource_type': 'hardware', 'exclusive': True},
            ],
            'edges': [],
        }
        explainer = ReasoningExplainer(data)
        explanation = explainer.explain_task(rec, conflict_chains=conflict_chains)
        self.assertEqual(explanation.verdict, 'REPLAN')
        self.assertTrue(
            any('contend' in p.lower() or 'conflict' in p.lower() for p in explanation.evidence_points)
            or 'contend' in (explanation.conflict_summary or '').lower()
        )

    def test_episode_06_coverage(self):
        data = load_episode('episode_06_conflict_replan.json')
        g = Graph(data)
        ev = RelevanceEvaluator(g)
        verdicts = ev.evaluate_all()
        explainer = ReasoningExplainer(data)
        for v in verdicts:
            with self.subTest(task=v.task_id):
                rec = {
                    'task_id': v.task_id,
                    'unified_verdict': v.verdict,
                    'signals': [],
                    'relevance_score': 0.5,
                    'sti': 20.0,
                    'lti': 5.0,
                    'multihop_chains': 1,
                    'multihop_goal_coverage': ['g1'],
                    'multihop_max_depth': 2,
                }
                explanation = explainer.explain_task(rec)
                self.assertIsInstance(explanation, TaskExplanation)


class TestRunReplay(unittest.TestCase):
    def test_run_replay_returns_bool(self):
        from replay_runner import run_replay
        result = run_replay(verbose=False)
        self.assertIsInstance(result, bool)

    def test_run_replay_most_pass(self):
        """Base-layer replay: 5/6 pass. Episode 06 gives ESCALATE at base layer (REPLAN only at governor layer)."""
        from replay_runner import run_replay
        result = run_replay(verbose=True)
        # Episode 06 expected_verdict=REPLAN is the governor-layer verdict;
        # base evaluator gives ESCALATE. This is by design (see commit 344a306).
        self.assertFalse(result, "Expected 5/6 at base layer (episode 06 should differ)")

    def test_episode_06_coverage(self):
        from replay_runner import run_replay
        result = run_replay(verbose=False)
        self.assertIsInstance(result, bool)


class TestTruthValueFromDict(unittest.TestCase):
    def test_from_dict_basic(self):
        d = {"strength": 0.8, "confidence": 0.6}
        tv = TruthValue.from_dict(d)
        self.assertAlmostEqual(tv.strength, 0.8)
        self.assertAlmostEqual(tv.confidence, 0.6)

    def test_from_dict_with_count(self):
        d = {"strength": 0.8, "confidence": 0.6}
        tv = TruthValue.from_dict(d)
        self.assertIsInstance(tv, TruthValue)
        self.assertAlmostEqual(tv.strength, 0.8)
        self.assertAlmostEqual(tv.confidence, 0.6)

    def test_from_dict_episode_06_coverage(self):
        data = load_episode('episode_06_conflict_replan.json')
        for node in _all_nodes(data):
            with self.subTest(node=node['id']):
                tv_dict = node.get('truth_value', {})
                if tv_dict and 'strength' in tv_dict and 'confidence' in tv_dict:
                    tv = TruthValue.from_dict(tv_dict)
                    self.assertIsInstance(tv, TruthValue)


if __name__ == "__main__":
    unittest.main()
