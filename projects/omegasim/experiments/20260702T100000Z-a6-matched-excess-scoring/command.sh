PYTHONPATH=src python3 -m unittest discover -s tests -v
python3 -m py_compile src/omegasim/a6_model.py scripts/run_a6_sweep.py
python3 scripts/run_a6_sweep.py --steps 500 --out /home/openclaw/research-agent/projects/omegasim/artifacts/a6-matched-excess-20260702T100000Z
