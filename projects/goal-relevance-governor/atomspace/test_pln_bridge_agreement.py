"""
Tests for cross-layer agreement tracking (pln_bridge_agreement) in IntegratedGovernorPipeline v0.2.1.
"""
import sys, os, json, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from atomspace.integrated_governor import IntegratedGovernorPipeline

CORPUS_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')

EPISODES = [
    'episode_01_stale_codegen.json',
    'episode_02_chem_blocking.json',
    'episode_03_premature_hardening.json',
    'episode_04_overengineered_repair.json',
    'episode_05_control_justified_long_running.json',
    'episode_06_conflict_replan.json',
]


class TestPLNBridgeAgreement(unittest.TestCase):
    """Test cross-layer agreement between PLN and final verdicts."""

    def _run(self, episode: str, enhanced: bool = False):
        with open(os.path.join(CORPUS_DIR, episode)) as f:
            data = json.load(f)
        p = IntegratedGovernorPipeline(data, use_enhanced_multihop=enhanced)
        return p.run(ecan_cycles=10)

    def test_agreement_field_exists(self):
        """pln_bridge_agreement should be a dict on every result."""
        r = self._run(EPISODES[0])
        self.assertIsInstance(r.pln_bridge_agreement, dict)

    def test_agreement_has_required_keys(self):
        """Agreement dict should have total_tasks, agreements, disagreements, disagreement_details."""
        r = self._run(EPISODES[0])
        a = r.pln_bridge_agreement
        for key in ('total_tasks', 'agreements', 'disagreements', 'disagreement_details'):
            self.assertIn(key, a)

    def test_total_equals_agree_plus_disagree(self):
        """total_tasks should equal agreements + disagreements for all episodes."""
        for ep in EPISODES:
            with self.subTest(episode=ep):
                r = self._run(ep)
                a = r.pln_bridge_agreement
                self.assertEqual(a['total_tasks'], a['agreements'] + a['disagreements'])

    def test_episode_01_full_agreement(self):
        """Episode 01 should have 0 disagreements (no conflict override)."""
        r = self._run(EPISODES[0])
        self.assertEqual(r.pln_bridge_agreement['disagreements'], 0)

    def test_episode_05_full_agreement(self):
        """Episode 05 (control) should have 0 disagreements."""
        r = self._run(EPISODES[4])
        self.assertEqual(r.pln_bridge_agreement['disagreements'], 0)

    def test_episode_06_has_one_disagreement(self):
        """Episode 06 should have exactly 1 disagreement (conflict override)."""
        r = self._run(EPISODES[5])
        a = r.pln_bridge_agreement
        self.assertEqual(a['disagreements'], 1)
        detail = a['disagreement_details'][0]
        self.assertEqual(detail['task_id'], 't-rest-wrapper')
        self.assertEqual(detail['pln_verdict'], 'ESCALATE')
        self.assertEqual(detail['final_verdict'], 'REPLAN')

    def test_disagreement_details_structure(self):
        """Each disagreement detail should have task_id, pln_verdict, final_verdict."""
        r = self._run(EPISODES[5])
        for d in r.pln_bridge_agreement['disagreement_details']:
            self.assertIn('task_id', d)
            self.assertIn('pln_verdict', d)
            self.assertIn('final_verdict', d)

    def test_to_dict_includes_agreement(self):
        """to_dict should include cross_layer_agreement."""
        r = self._run(EPISODES[0])
        d = r.to_dict()
        self.assertIn('cross_layer_agreement', d)

    def test_enhanced_mode_agreement_consistent(self):
        """Enhanced mode should produce same agreement as naive mode."""
        for ep in EPISODES:
            with self.subTest(episode=ep):
                r_naive = self._run(ep, enhanced=False)
                r_enh = self._run(ep, enhanced=True)
                self.assertEqual(
                    r_naive.pln_bridge_agreement['disagreements'],
                    r_enh.pln_bridge_agreement['disagreements']
                )

    def test_all_episodes_at_least_one_task(self):
        """Every episode should have at least 1 task in agreement tracking."""
        for ep in EPISODES:
            with self.subTest(episode=ep):
                r = self._run(ep)
                self.assertGreater(r.pln_bridge_agreement['total_tasks'], 0)


if __name__ == '__main__':
    unittest.main()
