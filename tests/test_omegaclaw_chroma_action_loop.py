import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).parents[1]
PROJECT = ROOT / "projects/omegaclaw"
PETTA_SOURCE = PROJECT / "protocosmo2/phase2-checked-baseline/repos/PeTTa"
LIVE_CORE_SOURCE = PROJECT / "repos/PeTTa/repos/OmegaClaw-Core"
CORE_SOURCE = LIVE_CORE_SOURCE
CHROMA_SOURCE = PROJECT / "repos/PeTTa/repos/petta_lib_chromadb"
DRIVER = PROJECT / "protocosmo2/tools/phase5_omegaclaw_case.py"
PYTHON = PROJECT / "repos/PeTTa/.venv/bin/python"
REMEMBER_FIXTURE = ROOT / "tests/fixtures/omegaclaw/chroma_remember_rounds.json"
REMEMBER_NATIVE_FIXTURE = ROOT / "tests/fixtures/omegaclaw/chroma_remember_native_rounds.json"
QUERY_FIXTURE = ROOT / "tests/fixtures/omegaclaw/chroma_query_rounds.json"


def clone_shared(source: Path, destination: Path) -> None:
    subprocess.run(
        ["git", "clone", "-q", "--shared", str(source), str(destination)],
        check=True,
    )


def isolated_layout(root: Path) -> tuple[Path, Path, Path]:
    repos = root / "repos"
    repos.mkdir(parents=True)
    petta = repos / "PeTTa"
    core = repos / "OmegaClaw-Core"
    chroma_lib = repos / "petta_lib_chromadb"
    clone_shared(PETTA_SOURCE, petta)
    clone_shared(CORE_SOURCE, core)
    clone_shared(CHROMA_SOURCE, chroma_lib)
    (petta / "repos").mkdir()
    os.symlink("../../OmegaClaw-Core", petta / "repos/OmegaClaw-Core")
    os.symlink("../../petta_lib_chromadb", petta / "repos/petta_lib_chromadb")
    for relative in (
        "lib_llm_ext.py", "run.metta", "src/channels.metta", "src/loop.metta",
        "channels/file_shadow.py",
    ):
        source = CORE_SOURCE / relative
        destination = core / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    shutil.copy2(
        CHROMA_SOURCE / "lib_chromadb.py", chroma_lib / "lib_chromadb.py"
    )
    (core / "MEMORY.md").write_text(
        "REAL_METTA_CHROMA_20260813 = WRONG MARKDOWN DECOY 9999\n",
        encoding="utf-8",
    )
    return petta, core, chroma_lib


def run_case(*, petta: Path, core: Path, chroma: Path, prompt: str,
             session: str, fixture: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update({
        "OMEGACLAW_ALLOW_BRIDGE_FIXTURE": "1",
        "CHROMA_DB_PATH": str(chroma),
    })
    return subprocess.run(
        [
            str(PYTHON), str(DRIVER), "--petta", str(petta), "--core", str(core),
            "--prompt", prompt, "--session", session,
            "--provider", "OpenClawFileBridge", "--bridge-fixture", str(fixture),
            "--timeout", "60", "--file-channel", "--live-transport",
        ],
        cwd=ROOT, env=env, text=True, capture_output=True, timeout=75, check=False,
    )


def test_real_metta_remember_then_fresh_query_uses_chroma_not_markdown():
    with tempfile.TemporaryDirectory(prefix=".pytest-chroma-loop-", dir=PROJECT) as raw:
        trial = Path(raw)
        chroma = trial / "chroma"
        chroma.mkdir(mode=0o700)

        remember_petta, remember_core, chroma_lib = isolated_layout(trial / "remember")
        remembered = run_case(
            petta=remember_petta, core=remember_core, chroma=chroma,
            prompt=("Remember this only through OmegaClaw Chroma: "
                    "REAL_METTA_CHROMA_20260813 = amber otter 4517."),
            session="provider-free-chroma-remember", fixture=REMEMBER_FIXTURE,
        )
        assert remembered.returncode == 0, remembered.stderr[-4000:]
        assert json.loads(remembered.stdout)["answer"] == "REMEMBER_THROUGH_PETTA_OK"
        history = (remember_core / "memory/history.metta").read_text(encoding="utf-8")
        assert '(remember "REAL_METTA_CHROMA_20260813 = amber otter 4517")' in history

        db_env = os.environ.copy()
        db_env.update({
            "CHROMA_DB_PATH": str(chroma),
            "PYTHONPATH": str(chroma_lib),
        })
        direct = subprocess.run(
            [
                str(PYTHON), "-c",
                "import json,lib_chromadb; print(json.dumps({"
                "'count':lib_chromadb.COLLECTION.count(),"
                "'documents':lib_chromadb.COLLECTION.get(include=['documents'])['documents']}))",
            ],
            cwd=ROOT, env=db_env, text=True, capture_output=True, check=True,
        )
        evidence = json.loads(direct.stdout)
        assert evidence == {
            "count": 1,
            "documents": ["REAL_METTA_CHROMA_20260813 = amber otter 4517"],
        }

        query_petta, query_core, _ = isolated_layout(trial / "query")
        queried = run_case(
            petta=query_petta, core=query_core, chroma=chroma,
            prompt=("Query OmegaClaw Chroma for REAL_METTA_CHROMA_20260813 "
                    "and recall the exact value."),
            session="provider-free-chroma-query", fixture=QUERY_FIXTURE,
        )
        assert queried.returncode == 0, queried.stderr[-4000:]
        assert json.loads(queried.stdout)["answer"] == (
            "QUERY_THROUGH_PETTA_OK: amber otter 4517"
        )
        query_history = (query_core / "memory/history.metta").read_text(
            encoding="utf-8"
        )
        assert '(query "REAL_METTA_CHROMA_20260813")' in query_history
        assert "amber otter 4517" in query_history
        assert "WRONG MARKDOWN DECOY 9999" not in query_history

        process_listing = subprocess.run(
            ["ps", "-eo", "args="], text=True, capture_output=True, check=True
        ).stdout
        assert str(trial) not in process_listing


def test_real_metta_remember_is_single_effect_with_live_history_shape():
    """One PeTTa action must produce exactly one persistent Chroma write.

    The live canary exposed repeated Python side effects while PeTTa was
    evaluating a single ``remember`` proposal.  Preserve the deployed
    history size/content shape here while keeping all writes disposable.
    """
    with tempfile.TemporaryDirectory(prefix=".pytest-chroma-live-history-", dir=PROJECT) as raw:
        trial = Path(raw)
        chroma = trial / "chroma"
        chroma.mkdir(mode=0o700)
        petta, core, chroma_lib = isolated_layout(trial / "remember")
        shutil.copy2(LIVE_CORE_SOURCE / "memory/history.metta", core / "memory/history.metta")
        db_env = os.environ.copy()
        db_env.update({
            "CHROMA_DB_PATH": str(chroma),
            "PYTHONPATH": str(chroma_lib),
        })
        subprocess.run(
            [
                str(PYTHON), "-c",
                "import lib_chromadb; i=lib_chromadb.remember('dimension-probe', [0.0]*384, 'probe'); lib_chromadb.forget_id(i); assert lib_chromadb.COLLECTION.count()==0",
            ],
            cwd=ROOT, env=db_env, text=True, capture_output=True, check=True,
        )

        remembered = run_case(
            petta=petta, core=core, chroma=chroma,
            prompt=("Remember this only through OmegaClaw Chroma: "
                    "REAL_METTA_SINGLE_EFFECT_20260813 = copper ibis 5174."),
            session="provider-free-chroma-live-history",
            fixture=REMEMBER_NATIVE_FIXTURE,
        )
        assert remembered.returncode == 0, remembered.stderr[-4000:]

        direct = subprocess.run(
            [
                str(PYTHON), "-c",
                "import json,lib_chromadb; print(json.dumps({"
                "'count':lib_chromadb.COLLECTION.count(),"
                "'documents':lib_chromadb.COLLECTION.get(include=['documents'])['documents']}))",
            ],
            cwd=ROOT, env=db_env, text=True, capture_output=True, check=True,
        )
        evidence = json.loads(direct.stdout)
        assert evidence == {
            "count": 1,
            "documents": ["REAL_METTA_CHROMA_20260813 = amber otter 4517"],
        }


def test_three_supervisors_bind_distinct_absolute_chroma_paths():
    expected = {
        PROJECT / "local/protomega-outer-telegram-supervisor.sh":
            ("/home/openclaw/.openclaw/protomega-chroma-db",),
        PROJECT / "local/protomega2-outer-telegram-supervisor.sh":
            ("/home/openclaw/.openclaw/protomega2-chroma-db",),
        PROJECT / "protocosmo2/tools/protocosmo2_telegram_supervisor.sh":
            ("protocosmo2/phase2-checked-baseline/repos/PeTTa", "$PETTA/chroma_db"),
    }
    for script, fragments in expected.items():
        source = script.read_text(encoding="utf-8")
        assert all(fragment in source for fragment in fragments)
        assert "CHROMA_DB_PATH=\"$CHROMA_DB_PATH\"" in source or (
            "OMEGACLAW_OUTER_CHROMA_DB_PATH=" in source
        )

    runner = (PROJECT / "protocosmo2/tools/phase6_private_canary_runner.py").read_text(
        encoding="utf-8"
    )
    assert 'key != "TG_BOT_TOKEN"' in runner
    assert 'os.environ.get("CHROMA_DB_PATH", "")' in runner
    assert "live receiver requires an absolute CHROMA_DB_PATH" in runner
    assert 'process = subprocess.Popen(command, env=clean_env' in runner

    driver = (PROJECT / "protocosmo2/tools/phase5_omegaclaw_case.py").read_text(
        encoding="utf-8"
    )
    assert 'env.get("CHROMA_DB_PATH", "")' in driver
    assert "live runtime requires an absolute CHROMA_DB_PATH" in driver


def test_live_metta_loop_commits_each_effectful_action_once():
    for core in (
        PROJECT / "repos/PeTTa/repos/OmegaClaw-Core",
        PROJECT / "worktrees/protocosmo2-phase6-live",
        PROJECT / "protocosmo2/phase2-checked-baseline/repos/OmegaClaw-Core",
    ):
        loop = (core / "src/loop.metta").read_text(encoding="utf-8")
        assert "(let $R (once (eval $s))" in loop
        assert "(once (COMMAND_RETURN:" in loop
        assert "(let $R (eval $s)" not in loop
