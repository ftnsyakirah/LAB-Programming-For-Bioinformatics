# SECB3203 Lab 1 - Python fundamentals and a reproducible project

Student: Fatin Syakirah Binti Muahamad Hardon (matric no: A24CS0073)

## Setup
### Windows (cmd)
```bash
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
pip freeze > requirements-frozen.txt

## Run
python -m pytest
ruff check src
python src/env_check.py > results/environment_report.txt

## What is in this repository
- `src/` → basics.py, env_check.py 
- `tests/` → test_visible.py, test_lab01_own.py
- `data/` → qc_records.csv (read-only input data)  
- `results/` → environment_report.txt  
- `requirements.txt`, `requirements-frozen.txt`, `pytest.ini`, `.gitignore`, `README.md`, `AI_USE_LOG.md`

## What is not committed, and why
<Two sentences in your own words: which folders are ignored by Git and what could go wrong if they were committed.>
The `.venv/` folder is ignored because it contains the virtual environment, which is large and specific to each computer.  
The `results/` folder is ignored because it stores output files, and committing them would make the repository messy and less reproducible.