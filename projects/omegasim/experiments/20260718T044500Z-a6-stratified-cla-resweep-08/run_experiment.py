#!/usr/bin/env python3
"""Execute batch 08 with the unchanged frozen CLA experiment implementation."""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "20260718T004500Z-a6-stratified-cla-resweep-05" / "run_experiment.py"
spec = importlib.util.spec_from_file_location("prepared_batch08", SOURCE)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
module.CELLS = (
    (1.0, 0.0, 3), (1.0, 0.6, 0), (1.0, 0.8, 3),
    (2.0, 0.15, 0), (2.0, 0.35, 3), (2.0, 0.8, 5),
    (5.0, 0.35, 1), (5.0, 0.6, 1),
)
module.__file__ = str(HERE / "run_experiment.py")
module.main()
