import json
from pathlib import Path
import sys

import pytest

LOCAL = Path(__file__).parents[1] / "projects/omegaclaw/local"
sys.path.insert(0, str(LOCAL))

from omegaclaw_chroma_acceptance_controller import (  # noqa: E402
    AcceptanceController,
    AcceptanceError,
    BotApiGroupDriver,
    BotApiDriverPool,
    CommandSupervisors,
    IdentitySpec,
    TelegramReceipt,
    validate_configured_agent_routes,
    validate_isolated_specs,
)


class FakeDriver:
    def __init__(self, label):
        self.label = label
        self.calls = []

    def transact(self, **kwargs):
        self.calls.append(kwargs)
        return self.label


class FakeSupervisor:
    def __init__(self, names):
        self.active = set()
        self.names = set(names)
        self.stop_calls = []

    def start(self, identity):
        self.active.add(identity)

    def stop(self, identity):
        self.stop_calls.append(identity)
        self.active.discard(identity)

    def active_identities(self):
        return set(self.active)


class FakeStore:
    def __init__(self, names):
        self.documents = {name: [] for name in names}

    def snapshot(self, identity, marker=None):
        documents = list(self.documents[identity])
        return {
            "count": len(documents),
            "dimension": 384,
            "exact_matches": documents.count(marker) if marker else 0,
            "documents_sha256": str(hash(tuple(documents))),
        }


class FakeTelegram:
    def __init__(self, store):
        self.store = store
        self.next_message_id = 100
        self.sent = []

    def transact(self, *, identity, username, chat_id, text, predicate, timeout):
        self.next_message_id += 1
        source = TelegramReceipt(chat_id, self.next_message_id, "driverbot", None, text)
        marker = text.split("MARKER:", 1)[1].splitlines()[0].strip()
        if "WRITE" in text:
            self.store.documents[identity].append(marker)
            reply_text = f"WRITE OK {marker}"
        elif "RECALL" in text:
            reply_text = marker if marker in self.store.documents[identity] else "NOT FOUND"
        else:
            reply_text = "NOT FOUND" if marker not in self.store.documents[identity] else marker
        self.next_message_id += 1
        result = TelegramReceipt(
            chat_id, self.next_message_id, username.lstrip("@"),
            source.message_id, reply_text,
        )
        assert predicate(result)
        self.sent.append((identity, text, source, result))
        return source, result


def make_specs(root: Path):
    specs = []
    for name in ("protomega", "protomega2", "protocosmo2"):
        identity_root = root / name
        for child in ("state", "worker", "chroma"):
            (identity_root / child).mkdir(parents=True, mode=0o700, exist_ok=True)
        specs.append(IdentitySpec(
            name=name,
            username=f"@{name}bot",
            state_dir=identity_root / "state",
            worker_state_dir=identity_root / "worker",
            chroma_dir=identity_root / "chroma",
        ))
    return specs


def test_provider_free_full_three_identity_staging_run(tmp_path):
    staging = tmp_path / "staging"
    staging.mkdir(mode=0o700)
    specs = make_specs(staging)
    store = FakeStore(spec.name for spec in specs)
    telegram = FakeTelegram(store)
    supervisor = FakeSupervisor(spec.name for spec in specs)
    controller = AcceptanceController(
        specs=specs,
        staging_root=staging,
        production_mutable_roots=[tmp_path / "production"],
        chat_id=-1001234567890,
        telegram=telegram,
        supervisors=supervisor,
        stores=store,
        evidence_dir=staging / "evidence",
        marker_factory=lambda name: f"OC-STAGE-{name}-UNIQUE = value-{name}",
        timeout=2,
    )

    report = controller.run()

    assert report["status"] == "passed"
    assert set(report["identities"]) == {spec.name for spec in specs}
    assert supervisor.active_identities() == set()
    assert len(telegram.sent) == 9
    write_prompts = [text for _name, text, _source, _result in telegram.sent if "WRITE" in text]
    assert len(write_prompts) == 3
    assert all("remember" in text.casefold() for text in write_prompts)
    assert all("Markdown" in text for text in write_prompts)
    recall_prompts = [text for _name, text, _source, _result in telegram.sent if "RECALL" in text]
    assert len(recall_prompts) == 3
    assert all("do not add RECALL OK" in text for text in recall_prompts)
    for name, evidence in report["identities"].items():
        assert evidence["write"]["db_after"]["exact_matches"] == 1
        assert evidence["recall"]["result"]["reply_to_message_id"] == evidence["recall"]["source"]["message_id"]
        assert evidence["isolation"]["result"]["text"] == "NOT FOUND"
        assert store.documents[name] == [evidence["marker"]]

    persisted = json.loads((staging / "evidence" / "report.json").read_text())
    assert persisted == report


def test_ambiguity_stops_every_identity_and_fails_closed(tmp_path):
    staging = tmp_path / "staging"
    staging.mkdir(mode=0o700)
    specs = make_specs(staging)
    store = FakeStore(spec.name for spec in specs)
    telegram = FakeTelegram(store)
    supervisor = FakeSupervisor(spec.name for spec in specs)
    supervisor.active.update({"protomega", "protomega2"})
    controller = AcceptanceController(
        specs=specs, staging_root=staging,
        production_mutable_roots=[tmp_path / "production"],
        chat_id=-1001234567890, telegram=telegram, supervisors=supervisor,
        stores=store, evidence_dir=staging / "evidence", timeout=2,
    )

    with pytest.raises(AcceptanceError, match="active identity ambiguity"):
        controller.run()
    assert supervisor.active_identities() == set()
    assert set(supervisor.stop_calls) == {spec.name for spec in specs}


def test_isolation_validation_rejects_shared_or_production_state(tmp_path):
    staging = tmp_path / "staging"
    production = tmp_path / "production"
    staging.mkdir(mode=0o700)
    production.mkdir(mode=0o700)
    specs = make_specs(staging)
    specs[1] = IdentitySpec(
        name=specs[1].name,
        username=specs[1].username,
        state_dir=specs[0].state_dir,
        worker_state_dir=specs[1].worker_state_dir,
        chroma_dir=specs[1].chroma_dir,
    )
    with pytest.raises(AcceptanceError, match="mutable path is shared"):
        validate_isolated_specs(specs, staging, [production])

    specs = make_specs(staging)
    specs[2] = IdentitySpec(
        name=specs[2].name,
        username=specs[2].username,
        state_dir=production,
        worker_state_dir=specs[2].worker_state_dir,
        chroma_dir=specs[2].chroma_dir,
    )
    with pytest.raises(AcceptanceError, match="outside staging root"):
        validate_isolated_specs(specs, staging, [production])


def test_agent_route_preflight_rejects_model_drift(tmp_path):
    specs = make_specs(tmp_path)
    specs = [IdentitySpec(
        name=item.name, username=item.username, state_dir=item.state_dir,
        worker_state_dir=item.worker_state_dir, chroma_dir=item.chroma_dir,
        supervisor_env={
            "OMEGACLAW_OUTER_AGENT_ID": "main" if item.name == "protocosmo2" else "opus",
            "OMEGACLAW_OUTER_MODEL": "openai/gpt-5.6-sol" if item.name == "protocosmo2" else "anthropic/claude-opus-4-6",
        },
    ) for item in specs]

    validate_configured_agent_routes(specs, {
        "main": "openai/gpt-5.6-sol", "opus": "anthropic/claude-opus-4-6",
    })
    with pytest.raises(AcceptanceError, match="configured provider route mismatch"):
        validate_configured_agent_routes(specs, {
            "main": "anthropic/claude-opus-4-6", "opus": "anthropic/claude-opus-4-6",
        })

def test_unbound_result_receipt_is_rejected():
    source = TelegramReceipt(-1001, 41, "driverbot", None, "prompt")
    wrong = TelegramReceipt(-1001, 42, "protomegabot", 40, "WRITE OK marker")
    assert not wrong.is_bound_reply(source, "@protomegabot")
    right = TelegramReceipt(-1001, 43, "protomegabot", 41, "WRITE OK marker")
    assert right.is_bound_reply(source, "@protomegabot")


def test_driver_pool_uses_a_distinct_explicit_driver_per_target():
    drivers = {name: FakeDriver(name) for name in ("protomega", "protomega2", "protocosmo2")}
    pool = BotApiDriverPool(drivers)

    result = pool.transact(
        identity="protomega2", username="@protomega2bot", chat_id=-1001,
        text="marker", predicate=lambda _receipt: True, timeout=2,
    )

    assert result == "protomega2"
    assert len(drivers["protomega2"].calls) == 1
    assert not drivers["protomega"].calls
    assert not drivers["protocosmo2"].calls
    with pytest.raises(AcceptanceError, match="no Telegram driver"):
        pool.transact(
            identity="unknown", username="@unknown", chat_id=-1001,
            text="marker", predicate=lambda _receipt: True, timeout=2,
        )


def test_bot_api_driver_rejects_a_late_duplicate_final(monkeypatch):
    driver = object.__new__(BotApiGroupDriver)
    driver.poll_timeout = 1
    driver.duplicate_settle_seconds = 0.05
    source_message = {
        "chat": {"id": -1001}, "from": {"username": "driverbot"},
        "message_id": 51, "text": "source",
    }
    monkeypatch.setattr(driver, "_call", lambda *_args, **_kwargs: source_message)
    batches = iter([
        [],
        [{"message": {
            "chat": {"id": -1001}, "from": {"username": "protomegabot"},
            "message_id": 52, "text": "DONE",
            "reply_to_message": {"message_id": 51},
        }}],
        [{"message": {
            "chat": {"id": -1001}, "from": {"username": "protomegabot"},
            "message_id": 53, "text": "DONE",
            "reply_to_message": {"message_id": 51},
        }}],
    ])
    monkeypatch.setattr(driver, "_updates", lambda _timeout: next(batches, []))

    with pytest.raises(AcceptanceError, match="duplicate final"):
        driver.transact(
            identity="protomega", username="@protomegabot", chat_id=-1001,
            text="source", predicate=lambda receipt: receipt.text == "DONE", timeout=1,
        )


def test_bot_api_driver_drains_stale_target_messages_before_source(monkeypatch):
    driver = object.__new__(BotApiGroupDriver)
    driver.poll_timeout = 1
    driver.duplicate_settle_seconds = 0
    source_message = {
        "chat": {"id": -1001}, "from": {"username": "driverbot"},
        "message_id": 71, "text": "source",
    }
    monkeypatch.setattr(driver, "_call", lambda *_args, **_kwargs: source_message)
    batches = iter([
        [{"message": {
            "chat": {"id": -1001}, "from": {"username": "protomegabot"},
            "message_id": 60, "text": "STALE",
        }}],
        [{"message": {
            "chat": {"id": -1001}, "from": {"username": "protomegabot"},
            "message_id": 72, "text": "DONE",
            "reply_to_message": {"message_id": 71},
        }}],
    ])
    monkeypatch.setattr(driver, "_updates", lambda _timeout: next(batches, []))

    source, result = driver.transact(
        identity="protomega", username="@protomegabot", chat_id=-1001,
        text="source", predicate=lambda receipt: receipt.text == "DONE", timeout=1,
    )

    assert source.message_id == 71
    assert result.message_id == 72


def test_orphan_process_counts_as_active_and_stop_drains_it(tmp_path, monkeypatch):
    staging = tmp_path / "staging"
    staging.mkdir(mode=0o700)
    specs = make_specs(staging)
    supervisor = CommandSupervisors(specs)
    orphaned = {"protomega": {111: 222}}

    class Result:
        returncode = 1

    monkeypatch.setattr(supervisor, "_run", lambda _identity, _action: Result())
    monkeypatch.setattr(
        supervisor, "_matching_processes",
        lambda identity: dict(orphaned.get(identity, {})),
    )
    monkeypatch.setattr(
        supervisor, "_terminate_process_groups",
        lambda identity, groups: orphaned.pop(identity, None),
    )

    assert supervisor.active_identities() == {"protomega"}
    supervisor.stop("protomega")
    assert supervisor.active_identities() == set()
