#!/usr/bin/env python3
"""Execute the closed batch-05 prepared design in a fresh immutable ledger."""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "20260718T004500Z-a6-stratified-cla-resweep-05" / "run_experiment.py"
spec = importlib.util.spec_from_file_location("prepared_batch05", SOURCE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.__file__ = str(HERE / "run_experiment.py")
module.main()
