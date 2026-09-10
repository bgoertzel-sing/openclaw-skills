import importlib.util
import json
import os
from pathlib import Path
import threading
import time


MODULE_PATH = Path(__file__).parents[1] / "projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core/lib_llm_ext.py"


def load_module():
    spec = importlib.util.spec_from_file_location("protomega_lib_llm_ext_test", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_registered_file_bridge_round_trip(tmp_path, monkeypatch):
    module = load_module()
    monkeypatch.setenv("OMEGACLAW_SHADOW_FILE_BRIDGE", str(tmp_path))
    monkeypatch.setenv("OMEGACLAW_SHADOW_BRIDGE_REQUEST_ID", "a" * 64)
    monkeypatch.setenv("OMEGACLAW_SHADOW_BRIDGE_SECRET_HEX", (b"s" * 32).hex())
    monkeypatch.setenv("OMEGACLAW_SHADOW_TIMEOUT", "5")
    provider = module._get_provider("OpenClawFileBridge")
    assert provider is not None and provider.is_available

    def respond():
        request = tmp_path / "request-1.json"
        deadline = time.monotonic() + 3
        while not request.exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        payload = json.loads(request.read_text(encoding="utf-8"))
        assert payload["content"] == "bridge-probe"
        response = {
            "protocol": provider._PROTOCOL,
            "status": "ok",
            "request_id": "a" * 64,
            "round": 1,
            "content_sha256": payload["content_sha256"],
            "answer": "bridge-ok",
            "cause_code": None,
        }
        response["hmac_sha256"] = provider._mac(response, b"s" * 32)
        (tmp_path / "response-1.json").write_text(
            json.dumps(response), encoding="utf-8"
        )

    worker = threading.Thread(target=respond)
    worker.start()
    try:
        assert provider.chat("bridge-probe") == "bridge-ok"
    finally:
        worker.join(timeout=5)
