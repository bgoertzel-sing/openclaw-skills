import importlib.util
import json
from pathlib import Path
import threading
import time
from types import SimpleNamespace
import pytest


MODULE_PATH = Path(__file__).parents[1] / "projects/omegaclaw/protocosmo2/tools/phase5_openclaw_bridge.py"
MODEL_RUN_HELPER = MODULE_PATH.with_name("phase5_openclaw_model_run.mjs")
SPEC = importlib.util.spec_from_file_location("phase5_openclaw_bridge_test", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def test_plain_answer_is_wrapped_as_exact_send():
    assert MODULE.normalize_model_answer('hello\n"Ben"\\world') == '(send "hello \'Ben\'/world")'


def test_exact_single_send_is_preserved():
    assert MODULE.normalize_model_answer('(send "already-ok")') == '(send "already-ok")'


def test_multiple_or_non_send_commands_are_inert_text():
    result = MODULE.normalize_model_answer('(send "one") (continue-thinking "two")')
    assert result.startswith('(send "')
    assert "'one'" in result
    assert result.endswith('")')


def test_plain_answer_is_bounded_to_one_parseable_line():
    result = MODULE.normalize_model_answer(("line\n" * 3000) + '"tail"')
    assert "\n" not in result
    assert len(result) <= 4009


def test_live_driver_requires_petta_channel_send_and_has_no_raw_answer_seam():
    case = (MODULE_PATH.with_name("phase5_omegaclaw_case.py")).read_text(encoding="utf-8")
    bridge = MODULE_PATH.read_text(encoding="utf-8")
    assert '"raw_answer": raw_answer' not in bridge
    assert "read_bridge_raw_answer(" not in case
    assert "answer = output_answer" in case
    assert "responses are action proposals" in case


def test_gateway_failure_sentinel_is_not_a_successful_answer():
    with pytest.raises(RuntimeError, match="openclaw_nonanswer"):
        MODULE.require_substantive_answer(
            "Agent couldn't generate a response. Some tool actions may have already been executed."
        )


def test_requested_provider_and_model_are_required():
    result = {"meta": {"agentMeta": {"provider": "anthropic", "model": "claude-opus-4-6"}}}
    MODULE.require_requested_route(result, "anthropic/claude-opus-4-6")
    with pytest.raises(RuntimeError, match="openclaw_route_mismatch"):
        MODULE.require_requested_route(result, "openai/gpt-5.6-sol")
    with pytest.raises(RuntimeError, match="openclaw_route_missing"):
        MODULE.require_requested_route({}, "anthropic/claude-opus-4-6")


def raw_boundary():
    return {
        "systemPromptChars": 0,
        "toolListChars": 0,
        "toolSchemaChars": 0,
        "messageCount": 0,
    }


@pytest.mark.parametrize("answer", [
    'remember one marker',
    'query OC-PROTO-20260813-A',
    'send one final answer',
    '(remember "one marker")',
    '(query "one marker")',
    '(send "one answer with (quoted parentheses)")',
    '(metta (foo (bar baz)))',
])
def test_bridge_accepts_exactly_one_listed_balanced_metta_action(answer):
    assert MODULE.require_single_metta_action(answer) == answer


@pytest.mark.parametrize("answer", [
    'plain prose',
    '(memory_search "one marker")',
    '(remember "one")\n(pin "two")',
    '(remember "one") (send "two")',
    '((remember "one") (send "two"))',
    '(remember "unterminated)',
])
def test_bridge_rejects_prose_openclaw_tools_and_multiple_actions(answer):
    with pytest.raises(RuntimeError, match="answer|action"):
        MODULE.require_single_metta_action(answer)


def test_answer_rejects_success_payload_from_wrong_route(monkeypatch, tmp_path):
    envelope = {
        "result": {
            "payloads": [{"text": "wrong route"}],
            "meta": {"agentMeta": {
                "provider": "openai", "model": "gpt-5.6-sol",
                "rawModelBoundary": raw_boundary(),
            }},
        }
    }
    monkeypatch.setattr(
        MODULE.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(returncode=0, stdout=json.dumps(envelope), stderr=""),
    )
    with pytest.raises(RuntimeError, match="openclaw_route_mismatch"):
        MODULE.answer("hello", "session", "anthropic/claude-opus-4-6", 5, [], True, "protomegabot-opus")


def test_answer_rejects_route_bound_payload_after_nonzero_model_run_exit(monkeypatch):
    envelope = {
        "result": {
            "payloads": [{"text": '(send "completed exact answer")'}],
            "meta": {"agentMeta": {
                "provider": "anthropic", "model": "claude-opus-4-6",
                "rawModelBoundary": raw_boundary(),
            }},
        }
    }
    monkeypatch.setattr(
        MODULE.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(
            returncode=1, stdout=json.dumps(envelope),
            stderr="post-answer finalization failed",
        ),
    )
    with pytest.raises(RuntimeError, match="openclaw model run exited 1"):
        MODULE.answer(
            "hello", "session", "anthropic/claude-opus-4-6", 5, [], True,
            "protomegabot-opus",
        )


def test_nonzero_exit_without_complete_route_bound_payload_still_fails(monkeypatch):
    monkeypatch.setattr(
        MODULE.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(
            returncode=1, stdout="not-json", stderr="runtime failed",
        ),
    )
    with pytest.raises(RuntimeError, match="openclaw model run exited 1"):
        MODULE.answer(
            "hello", "session", "anthropic/claude-opus-4-6", 5, [], True,
            "protomegabot-opus",
        )


def test_answer_uses_raw_model_helper_over_stdin_not_agent_cli_or_prompt_argv(monkeypatch):
    observed = {}
    envelope = {
        "result": {
            "payloads": [{"text": '(query "marker")'}],
            "meta": {"agentMeta": {
                "provider": "anthropic", "model": "claude-opus-4-6",
                "rawModelBoundary": raw_boundary(),
            }},
        }
    }

    def fake_run(command, **kwargs):
        observed["command"] = command
        observed["request"] = json.loads(kwargs["input"])
        observed["timeout"] = kwargs["timeout"]
        return SimpleNamespace(returncode=0, stdout=json.dumps(envelope), stderr="")

    monkeypatch.setattr(MODULE.subprocess, "run", fake_run)
    result = MODULE.answer(
        "FULL OMEGACLAW CONTEXT", "fresh-round-session",
        "anthropic/claude-opus-4-6", 5, [], True, "protomegabot-opus",
    )
    assert result == '(query "marker")'
    assert observed["command"] == ["node", str(MODEL_RUN_HELPER)]
    assert "FULL OMEGACLAW CONTEXT" not in observed["command"]
    assert observed["request"]["agent"] == "protomegabot-opus"
    assert observed["request"]["session"] == "fresh-round-session"
    assert "FULL OMEGACLAW CONTEXT" in observed["request"]["message"]
    assert observed["request"]["timeout_ms"] == 5000
    assert observed["timeout"] == 25


def test_raw_model_helper_enforces_prompt_none_zero_tools_and_zero_context():
    source = MODEL_RUN_HELPER.read_text(encoding="utf-8")
    assert 'modelRun: true' in source
    assert 'promptMode: "none"' in source
    assert 'report.systemPrompt?.chars !== 0' in source
    assert 'report.tools?.listChars !== 0' in source
    assert 'report.tools?.schemaChars !== 0' in source
    assert 'agentMeta.contextBudgetStatus?.messageCount !== 0' in source
    assert 'response.result.meta?.finalPromptText !== message' in source
    assert 'readFileSync(0, "utf8")' in source


def test_live_action_contract_overrides_five_lines_and_forbids_markdown_memory():
    instruction = MODULE.transport_instruction(True)
    assert "OVERRIDE only the earlier action-count" in instruction
    assert "one native OmegaClaw action on exactly one line" in instruction
    assert "Do not use OpenClaw tools or OpenClaw Markdown memory" in instruction


def test_live_request_uses_omegaclaw_provider_context_not_raw_transport_substitution():
    case = MODULE_PATH.with_name("phase5_omegaclaw_case.py").read_text(encoding="utf-8")
    bridge = MODULE_PATH.read_text(encoding="utf-8")
    assert 'prefix="omegaclaw-live-request-"' not in case
    assert '"--live-request-file"' not in case
    assert 'args.live_request_file' not in bridge
    assert "verified_round_request(" in bridge
    assert "request_content, args.session" in bridge


def test_round_request_authentication_and_tamper_rejection(tmp_path):
    secret = b"s" * 32
    request_id = "a" * 64
    content = "PROMPT: OmegaClaw context :-:-:-: HUMAN-MSG: remember marker"
    signed = {
        "protocol": MODULE.FILE_BRIDGE_PROTOCOL,
        "request_id": request_id,
        "round": 1,
        "content_sha256": MODULE.hashlib.sha256(content.encode()).hexdigest(),
        "content": content,
    }
    payload = dict(signed)
    payload["hmac_sha256"] = MODULE.canonical_mac(signed, secret)
    path = tmp_path / "request-1.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    assert MODULE.verified_round_request(
        path, request_id=request_id, round_number=1, secret=secret
    ) == (content, signed["content_sha256"])
    payload["content"] += " tampered"
    path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(RuntimeError, match="authentication"):
        MODULE.verified_round_request(
            path, request_id=request_id, round_number=1, secret=secret
        )


def load_core_provider(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.OpenClawFileBridgeProvider()


@pytest.mark.parametrize("relative", [
    "repos/PeTTa/repos/OmegaClaw-Core/lib_llm_ext.py",
    "worktrees/protocosmo2-phase6-live/lib_llm_ext.py",
])
def test_core_provider_runs_two_authenticated_distinct_rounds(monkeypatch, tmp_path, relative):
    root = MODULE_PATH.parents[2]
    request_id = "b" * 64
    secret = b"k" * 32
    monkeypatch.setenv("OMEGACLAW_SHADOW_FILE_BRIDGE", str(tmp_path))
    monkeypatch.setenv("OMEGACLAW_SHADOW_BRIDGE_REQUEST_ID", request_id)
    monkeypatch.setenv("OMEGACLAW_SHADOW_BRIDGE_SECRET_HEX", secret.hex())
    monkeypatch.setenv("OMEGACLAW_SHADOW_MAX_ROUNDS", "4")
    monkeypatch.setenv("OMEGACLAW_SHADOW_TIMEOUT", "3")
    provider = load_core_provider(root / relative, "provider_" + relative.replace("/", "_"))
    observed = []

    def host():
        for round_number, answer in enumerate((
            '(remember "unique-chroma-marker")', 'send stored'
        ), 1):
            request_path = tmp_path / f"request-{round_number}.json"
            deadline = time.monotonic() + 3
            while not request_path.exists() and time.monotonic() < deadline:
                time.sleep(0.01)
            content, digest = MODULE.verified_round_request(
                request_path, request_id=request_id,
                round_number=round_number, secret=secret,
            )
            observed.append(content)
            response = MODULE.signed_response(
                answer=answer, request_id=request_id, round_number=round_number,
                content_sha256=digest, secret=secret,
            )
            (tmp_path / f"response-{round_number}.json").write_text(
                json.dumps(response), encoding="utf-8"
            )

    thread = threading.Thread(target=host)
    thread.start()
    assert provider.chat("full OmegaClaw prompt round one") == '(remember "unique-chroma-marker")'
    assert provider.chat("full OmegaClaw prompt with REMEMBER-SUCCESS") == 'send stored'
    assert provider.chat("post-send loop iteration") == "()"
    assert not (tmp_path / "request-3.json").exists()
    thread.join(timeout=3)
    assert not thread.is_alive()
    assert observed == [
        "full OmegaClaw prompt round one",
        "full OmegaClaw prompt with REMEMBER-SUCCESS",
    ]


def test_core_provider_rejects_tampered_round_response(monkeypatch, tmp_path):
    root = MODULE_PATH.parents[2]
    request_id = "c" * 64
    secret = b"z" * 32
    monkeypatch.setenv("OMEGACLAW_SHADOW_FILE_BRIDGE", str(tmp_path))
    monkeypatch.setenv("OMEGACLAW_SHADOW_BRIDGE_REQUEST_ID", request_id)
    monkeypatch.setenv("OMEGACLAW_SHADOW_BRIDGE_SECRET_HEX", secret.hex())
    monkeypatch.setenv("OMEGACLAW_SHADOW_TIMEOUT", "3")
    provider = load_core_provider(
        root / "worktrees/protocosmo2-phase6-live/lib_llm_ext.py", "provider_tamper"
    )

    def host():
        request_path = tmp_path / "request-1.json"
        while not request_path.exists():
            time.sleep(0.01)
        _, digest = MODULE.verified_round_request(
            request_path, request_id=request_id, round_number=1, secret=secret
        )
        response = MODULE.signed_response(
            answer='(send "forged")', request_id=request_id, round_number=1,
            content_sha256=digest, secret=secret,
        )
        response["answer"] = '(send "tampered")'
        (tmp_path / "response-1.json").write_text(json.dumps(response), encoding="utf-8")

    thread = threading.Thread(target=host)
    thread.start()
    with pytest.raises(RuntimeError, match="invalid authenticated"):
        provider.chat("context")
    thread.join(timeout=3)


def test_core_provider_has_bounded_round_budget(monkeypatch, tmp_path):
    root = MODULE_PATH.parents[2]
    monkeypatch.setenv("OMEGACLAW_SHADOW_FILE_BRIDGE", str(tmp_path))
    monkeypatch.setenv("OMEGACLAW_SHADOW_BRIDGE_REQUEST_ID", "d" * 64)
    monkeypatch.setenv("OMEGACLAW_SHADOW_BRIDGE_SECRET_HEX", (b"q" * 32).hex())
    monkeypatch.setenv("OMEGACLAW_SHADOW_MAX_ROUNDS", "4")
    provider = load_core_provider(
        root / "worktrees/protocosmo2-phase6-live/lib_llm_ext.py",
        "provider_round_budget",
    )
    provider._round = 4
    with pytest.raises(RuntimeError, match="round budget exhausted"):
        provider.chat("fifth provider exchange")
    assert not (tmp_path / "request-5.json").exists()


def test_core_provider_response_wait_is_bounded(monkeypatch, tmp_path):
    root = MODULE_PATH.parents[2]
    monkeypatch.setenv("OMEGACLAW_SHADOW_FILE_BRIDGE", str(tmp_path))
    monkeypatch.setenv("OMEGACLAW_SHADOW_BRIDGE_REQUEST_ID", "e" * 64)
    monkeypatch.setenv("OMEGACLAW_SHADOW_BRIDGE_SECRET_HEX", (b"w" * 32).hex())
    monkeypatch.setenv("OMEGACLAW_SHADOW_TIMEOUT", "0")
    provider = load_core_provider(
        root / "worktrees/protocosmo2-phase6-live/lib_llm_ext.py",
        "provider_timeout",
    )
    started = time.monotonic()
    with pytest.raises(TimeoutError, match="no response"):
        provider.chat("provider exchange with no host response")
    assert time.monotonic() - started < 1
    assert (tmp_path / "request-1.json").exists()
