#!/usr/bin/env python3
"""Execute batch 10 with the unchanged frozen CLA experiment implementation."""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "20260718T004500Z-a6-stratified-cla-resweep-05" / "run_experiment.py"
spec = importlib.util.spec_from_file_location("prepared_batch10", SOURCE)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
module.CELLS = (
    (5.0, 0.35, 0), (5.0, 0.35, 3),
    (5.0, 0.60, 0), (5.0, 0.60, 3),
)
module.STRATA = ("core4",)
module.__file__ = str(HERE / "run_experiment.py")
module.main()
