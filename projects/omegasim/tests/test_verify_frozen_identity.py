import hashlib
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "verify_frozen_identity.py"
SPEC = importlib.util.spec_from_file_location("verify_frozen_identity", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class FrozenIdentityTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.repo = Path(self.tempdir.name)
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True)
        subprocess.run(["git", "-C", str(self.repo), "config", "user.email", "test@example.invalid"], check=True)
        subprocess.run(["git", "-C", str(self.repo), "config", "user.name", "Test"], check=True)
        self.artifact = self.repo / "detector.py"
        self.artifact.write_text("frozen = True\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.repo), "add", "detector.py"], check=True)
        subprocess.run(["git", "-C", str(self.repo), "commit", "-qm", "freeze"], check=True)
        self.commit = MODULE.git(self.repo, "rev-parse", "HEAD")

    def tearDown(self):
        self.tempdir.cleanup()

    def test_exact_clean_repo_and_file_pass(self):
        repo = MODULE.verify_repo(self.repo, self.commit)
        digest = hashlib.sha256(self.artifact.read_bytes()).hexdigest()
        artifact = MODULE.verify_file(self.artifact, digest)
        self.assertTrue(repo["ok"])
        self.assertEqual(repo["status_porcelain"], [])
        self.assertTrue(artifact["ok"])

    def test_dirty_repo_fails_closed(self):
        self.artifact.write_text("frozen = False\n", encoding="utf-8")
        result = MODULE.verify_repo(self.repo, self.commit)
        self.assertFalse(result["ok"])
        self.assertEqual(result["status_porcelain"], [" M detector.py"])

    def test_staged_repo_fails_closed_with_exact_status(self):
        self.artifact.write_text("frozen = False\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(self.repo), "add", "detector.py"], check=True)
        result = MODULE.verify_repo(self.repo, self.commit)
        self.assertFalse(result["ok"])
        self.assertEqual(result["status_porcelain"], ["M  detector.py"])

    def test_untracked_file_fails_closed_with_exact_status(self):
        (self.repo / "untracked.txt").write_text("not frozen\n", encoding="utf-8")
        result = MODULE.verify_repo(self.repo, self.commit)
        self.assertFalse(result["ok"])
        self.assertEqual(result["status_porcelain"], ["?? untracked.txt"])

    def test_wrong_commit_fails_closed(self):
        result = MODULE.verify_repo(self.repo, "0" * 40)
        self.assertFalse(result["ok"])
        self.assertEqual(result["observed_commit"], self.commit)
        self.assertTrue(result["clean"])

    def test_hash_mismatch_fails_closed(self):
        self.assertFalse(MODULE.verify_file(self.artifact, "0" * 64)["ok"])

    def test_missing_repo_returns_serializable_failure(self):
        result = MODULE.verify_repo(self.repo / "missing", self.commit)
        self.assertFalse(result["ok"])
        self.assertIsNone(result["observed_commit"])
        self.assertIsNone(result["status_porcelain"])
        self.assertIn("error", result)

    def test_missing_file_returns_serializable_failure(self):
        result = MODULE.verify_file(self.repo / "missing.py", "0" * 64)
        self.assertFalse(result["ok"])
        self.assertIsNone(result["observed_sha256"])
        self.assertIn("error", result)


if __name__ == "__main__":
    unittest.main()
