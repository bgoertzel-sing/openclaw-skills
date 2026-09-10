from datetime import datetime, timedelta, timezone
import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).parents[1] / "bin" / "runpod-heartbeat-sensor.py"
SPEC = importlib.util.spec_from_file_location("runpod_heartbeat_sensor", MODULE_PATH)
sensor = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = sensor
SPEC.loader.exec_module(sensor)


class RunPodHeartbeatSensorTests(unittest.TestCase):
    def test_zero_provider_uptime_does_not_override_active_ssh_evidence(self):
        now = datetime(2026, 7, 22, 5, 0, tzinfo=timezone.utc)
        details = {
            "id": "healthy",
            "name": "training",
            "desiredStatus": "RUNNING",
            "uptimeSeconds": 0,
            "createdAt": "2026-07-22T04:00:00+00:00",
            "costPerHr": 1.49,
        }
        evidence = sensor.SshEvidence(
            reachable=True, gpu_util=36, gpu_mem_mib=1800, compute_processes=1
        )
        result, _ = sensor.inspect_pod(details, details, evidence, None, now)
        self.assertEqual(result["work_state"], "ready_active")
        self.assertEqual(result["provider_uptime_seconds_advisory"], 0)
        self.assertFalse(result["unreachable_confirmed"])
        self.assertAlmostEqual(result["estimated_compute_cost"], 1.49)

    def test_reachable_idle_is_not_mislabeled_stalled_or_unready(self):
        evidence = sensor.SshEvidence(reachable=True)
        self.assertEqual(sensor.classify_work("RUNNING", evidence), "ready_idle")

    def test_cpu_bound_preprocessing_counts_as_active(self):
        evidence = sensor.SshEvidence(reachable=True, cpu_active_processes=1)
        self.assertEqual(sensor.classify_work("RUNNING", evidence), "ready_active")

    def test_nonrunning_provider_state_is_not_probed_as_unreachable(self):
        evidence = sensor.SshEvidence(reachable=False, error="no endpoint")
        self.assertEqual(sensor.classify_work("EXITED", evidence), "not_running")

    def test_unreachable_requires_repetition_and_elapsed_time(self):
        start = datetime(2026, 7, 22, 5, 0, tzinfo=timezone.utc)
        first, confirmed = sensor.update_unreachable_state(None, "unreachable", start)
        self.assertFalse(confirmed)
        second, confirmed = sensor.update_unreachable_state(
            first, "unreachable", start + timedelta(minutes=10)
        )
        self.assertFalse(confirmed)
        third, confirmed = sensor.update_unreachable_state(
            second, "unreachable", start + timedelta(minutes=16)
        )
        self.assertTrue(confirmed)
        self.assertEqual(third["consecutive_unreachable"], 3)

    def test_reachability_resets_unreachable_history(self):
        previous = {
            "consecutive_unreachable": 4,
            "unreachable_since": "2026-07-22T04:00:00+00:00",
        }
        state, confirmed = sensor.update_unreachable_state(
            previous,
            "ready_active",
            datetime(2026, 7, 22, 5, 0, tzinfo=timezone.utc),
        )
        self.assertFalse(confirmed)
        self.assertEqual(state["consecutive_unreachable"], 0)
        self.assertIsNone(state["unreachable_since"])

    def test_probe_parser_defaults_missing_fields_safely(self):
        evidence = sensor.parse_probe_output("GPU_UTIL=92\nCOMPUTE_PROCS=2\n")
        self.assertTrue(evidence.reachable)
        self.assertEqual(evidence.gpu_util, 92)
        self.assertEqual(evidence.compute_processes, 2)
        self.assertEqual(evidence.gpu_mem_mib, 0)

    def test_runpod_created_at_format_supports_elapsed_cost(self):
        parsed = sensor.parse_time("2026-07-21 23:31:00.003 +0000 UTC")
        self.assertEqual(
            parsed,
            datetime(2026, 7, 21, 23, 31, 0, 3000, tzinfo=timezone.utc),
        )


if __name__ == "__main__":
    unittest.main()
