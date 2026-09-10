import hashlib
import importlib.util
import json
from pathlib import Path
import stat
import subprocess
import sys
from types import SimpleNamespace

import pytest


MODEL = "qwen2.5:7b"
MODEL_DIGEST = "845dbda0ea48"
ACTUAL_MODEL_DIGEST = "sha256:845dbda0ea48deadbeef"


def test_pinned_wrapper_is_executable_and_direct_help_reaches_parser(tmp_path):
    repo_root = Path(__file__).resolve().parents[1]
    wrapper = repo_root / "scripts" / "run_frame_oracle_v9_pinned.sh"
    provenance = tmp_path / "direct-help-import-provenance.json"

    assert wrapper.stat().st_mode & stat.S_IXUSR
    completed = subprocess.run(
        [
            "/usr/bin/env",
            f"RELALEAP_FRAME_ORACLE_V9_PYTHON={sys.executable}",
            f"RELALEAP_FRAME_ORACLE_V9_PROVENANCE_OUTPUT={provenance}",
            str(wrapper),
            "--help",
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    assert "--public" in completed.stdout
    record = json.loads(provenance.read_text())
    assert record["status"] == "verified"
    assert Path(record["source_root"]) == (repo_root / "src").resolve()


@pytest.fixture
def runner(tmp_path, monkeypatch):
    repo_root = Path(__file__).resolve().parents[1]
    script_dir = repo_root / "scripts"
    monkeypatch.syspath_prepend(str(script_dir))
    monkeypatch.setenv("PYTHONPATH", str((repo_root / "src").resolve()))
    monkeypatch.setenv(
        "RELALEAP_FRAME_ORACLE_V9_SOURCE_ROOT", str((repo_root / "src").resolve())
    )
    monkeypatch.setenv(
        "RELALEAP_FRAME_ORACLE_V9_PROVENANCE_OUTPUT",
        str((tmp_path / "import-provenance.json").resolve()),
    )
    sys.modules.pop("frame_oracle_v9_provenance", None)
    module_name = f"frame_oracle_v9_runner_test_{tmp_path.name.replace('-', '_')}"
    spec = importlib.util.spec_from_file_location(
        module_name, script_dir / "run_frame_oracle_v9.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "local_model_digest", lambda _model: ACTUAL_MODEL_DIGEST)
    return module


def frame():
    return {
        "predicate": "state",
        "entity_a": "beacon",
        "entity_b": "active",
        "polarity": "affirmed",
        "modality": "asserted",
        "abstain": False,
        "confidence": 1.0,
    }


def response(value=None):
    value = frame() if value is None else value
    return {"raw": {"response": json.dumps(value)}, "frame": value}


def fixture_args(tmp_path, *, case_count=1, answer_exists=True, expected=None):
    expected = frame() if expected is None else expected
    answers = {
        "contract_version": "frame-oracle-v9-gate-1",
        "cases": [
            {"case_id": f"synthetic-{index:02d}", "expected": expected}
            for index in range(case_count)
        ],
    }
    answer_path = tmp_path / "synthetic-answers.json"
    answer_bytes = (json.dumps(answers, sort_keys=True) + "\n").encode()
    if answer_exists:
        answer_path.write_bytes(answer_bytes)
    commitment = hashlib.sha256(answer_bytes).hexdigest()
    public = {
        "contract_version": "frame-oracle-v9-gate-1",
        "opened": False,
        "answer_file_sha256": commitment,
        "cases": [
            {
                "case_id": f"synthetic-{index:02d}",
                "sentence": "The beacon is active.",
                "stratum": "synthetic",
            }
            for index in range(case_count)
        ],
    }
    public_path = tmp_path / "synthetic-public.json"
    public_path.write_text(json.dumps(public, sort_keys=True) + "\n")
    return SimpleNamespace(
        public=public_path,
        answers=answer_path,
        answer_commitment=commitment,
        output=tmp_path / "state.json",
        model=MODEL,
        model_digest=MODEL_DIGEST,
    )


def read_state(args):
    return json.loads(args.output.read_text())


def test_failure_before_consumption_does_not_infer_or_create_state(runner, tmp_path, monkeypatch):
    args = fixture_args(tmp_path)
    public = json.loads(args.public.read_text())
    public["opened"] = True
    args.public.write_text(json.dumps(public) + "\n")
    calls = 0

    def forbidden_ask(*_args):
        nonlocal calls
        calls += 1
        raise AssertionError("inference must not start")

    monkeypatch.setattr(runner, "ask", forbidden_ask)
    with pytest.raises(RuntimeError, match="unopened contract"):
        runner.run_gate(args)
    assert calls == 0
    assert not args.output.exists()


def test_first_request_failure_is_terminally_consumed(runner, tmp_path, monkeypatch):
    args = fixture_args(tmp_path, answer_exists=False)
    monkeypatch.setattr(
        runner, "ask", lambda *_args: (_ for _ in ()).throw(RuntimeError("first"))
    )
    with pytest.raises(RuntimeError, match="first"):
        runner.run_gate(args)
    state = read_state(args)
    assert state["version"] == 8
    assert state["state"] == "consumed_failed"
    assert state["gate_consumed"] is True
    assert state["completed_calls"] == 0
    assert state["calls"] == []


def test_second_request_failure_preserves_first_response(runner, tmp_path, monkeypatch):
    args = fixture_args(tmp_path, answer_exists=False)
    calls = 0

    def fail_second(*_args):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise RuntimeError("second")
        return response()

    monkeypatch.setattr(runner, "ask", fail_second)
    with pytest.raises(RuntimeError, match="second"):
        runner.run_gate(args)
    state = read_state(args)
    assert state["state"] == "consumed_failed"
    assert state["gate_consumed"] is True
    assert state["completed_calls"] == 1
    assert state["calls"][0]["repeat"] == 1
    assert state["calls"][0]["normalized"]["entity_a"] == "beacon"


def test_failure_after_complete_pair_preserves_pair_and_progress(runner, tmp_path, monkeypatch):
    args = fixture_args(tmp_path, case_count=2, answer_exists=False)
    calls = 0

    def fail_third(*_args):
        nonlocal calls
        calls += 1
        if calls == 3:
            raise RuntimeError("third")
        return response()

    monkeypatch.setattr(runner, "ask", fail_third)
    with pytest.raises(RuntimeError, match="third"):
        runner.run_gate(args)
    state = read_state(args)
    assert state["gate_consumed"] is True
    assert state["completed_calls"] == 2
    assert len(state["rows"]) == 1
    assert state["rows"][0]["deterministic"] is True


def test_answer_commitment_mismatch_occurs_only_after_all_calls(runner, tmp_path, monkeypatch):
    args = fixture_args(tmp_path, case_count=2)
    args.answers.write_text('{"tampered": true}\n')
    calls = 0

    def successful_ask(*_args):
        nonlocal calls
        calls += 1
        return response()

    monkeypatch.setattr(runner, "ask", successful_ask)
    with pytest.raises(RuntimeError, match="answer commitment mismatch"):
        runner.run_gate(args)
    state = read_state(args)
    assert calls == 4
    assert state["gate_consumed"] is True
    assert state["completed_calls"] == 4
    assert state["state"] == "consumed_failed"


def test_atomic_write_failure_before_pending_state_prevents_inference(runner, tmp_path, monkeypatch):
    args = fixture_args(tmp_path, answer_exists=False)
    calls = 0

    def forbidden_ask(*_args):
        nonlocal calls
        calls += 1
        return response()

    monkeypatch.setattr(runner, "ask", forbidden_ask)
    monkeypatch.setattr(
        runner, "atomic_write_json", lambda *_args: (_ for _ in ()).throw(OSError("disk"))
    )
    with pytest.raises(OSError, match="disk"):
        runner.run_gate(args)
    assert calls == 0
    assert not args.output.exists()


def test_atomic_write_failure_after_consumption_keeps_pending_record(runner, tmp_path, monkeypatch):
    args = fixture_args(tmp_path, answer_exists=False)
    original_atomic_write = runner.atomic_write_json
    writes = 0
    calls = 0

    def fail_after_pending(path, value):
        nonlocal writes
        writes += 1
        if writes > 1:
            raise OSError("checkpoint disk failure")
        original_atomic_write(path, value)

    def successful_ask(*_args):
        nonlocal calls
        calls += 1
        return response()

    monkeypatch.setattr(runner, "atomic_write_json", fail_after_pending)
    monkeypatch.setattr(runner, "ask", successful_ask)
    with pytest.raises(OSError, match="checkpoint disk failure"):
        runner.run_gate(args)
    state = read_state(args)
    assert calls == 1
    assert state["state"] == "consumed_pending"
    assert state["gate_consumed"] is True
    assert state["completed_calls"] == 0


def test_existing_output_is_never_resumed_or_replaced(runner, tmp_path, monkeypatch):
    args = fixture_args(tmp_path)
    args.output.write_text('{"state": "prior"}\n')
    monkeypatch.setattr(runner, "ask", lambda *_args: pytest.fail("must not infer"))
    with pytest.raises(RuntimeError, match="refusing to resume"):
        runner.run_gate(args)
    assert json.loads(args.output.read_text()) == {"state": "prior"}


def test_actual_model_digest_mismatch_blocks_before_consumption(runner, tmp_path, monkeypatch):
    args = fixture_args(tmp_path)
    monkeypatch.setattr(runner, "local_model_digest", lambda _model: "sha256:wrong")
    monkeypatch.setattr(runner, "ask", lambda *_args: pytest.fail("must not infer"))
    with pytest.raises(RuntimeError, match="model digest mismatch"):
        runner.run_gate(args)
    assert not args.output.exists()


def test_synthetic_twenty_four_case_gate_reaches_consumed_passed(runner, tmp_path, monkeypatch):
    args = fixture_args(tmp_path, case_count=24)
    calls = 0

    def successful_ask(*_args):
        nonlocal calls
        calls += 1
        return response()

    monkeypatch.setattr(runner, "ask", successful_ask)
    state = runner.run_gate(args)
    assert calls == 48
    assert state["state"] == "consumed_passed"
    assert state["gate_consumed"] is True
    assert state["completed_calls"] == 48
    assert state["model_digest_actual"] == ACTUAL_MODEL_DIGEST
    assert state["summary"]["gate"] == "passed"


def test_runner_uses_v9_union_to_unknown_for_mismatched_proposal(runner, tmp_path, monkeypatch):
    unknown = {
        "predicate": "unknown",
        "entity_a": "",
        "entity_b": "",
        "polarity": "unknown",
        "modality": "unknown",
        "abstain": True,
        "confidence": 0.4,
    }
    mismatch = {
        "predicate": "state",
        "entity_a": "beacon",
        "entity_b": "active",
        "polarity": "affirmed",
        "modality": "asserted",
        "abstain": True,
        "confidence": 0.4,
    }
    args = fixture_args(tmp_path, case_count=24, expected=unknown)
    monkeypatch.setattr(runner, "ask", lambda *_args: response(mismatch))
    state = runner.run_gate(args)
    assert state["state"] == "consumed_passed"
    assert state["summary"]["exact"] == 24
    assert all(call["normalized"]["predicate"] == "unknown" for call in state["calls"])


def test_runner_uses_v9_empty_slot_fail_closed_rule(runner, tmp_path, monkeypatch):
    unknown = {
        "predicate": "unknown",
        "entity_a": "",
        "entity_b": "",
        "polarity": "unknown",
        "modality": "unknown",
        "abstain": True,
        "confidence": 0.4,
    }
    empty_slot = {
        "predicate": "state",
        "entity_a": "   ",
        "entity_b": "active",
        "polarity": "affirmed",
        "modality": "asserted",
        "abstain": False,
        "confidence": 0.4,
    }
    args = fixture_args(tmp_path, case_count=24, expected=unknown)
    monkeypatch.setattr(runner, "ask", lambda *_args: response(empty_slot))
    state = runner.run_gate(args)
    assert state["state"] == "consumed_passed"
    assert state["summary"]["exact"] == 24
    assert all(call["normalized"]["predicate"] == "unknown" for call in state["calls"])

