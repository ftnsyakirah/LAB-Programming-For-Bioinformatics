# SECB3203 Lab 5 - Functions and modules: sequence_utils.py and normalize.py

Student: Fatin Syakirah Binti Muhamad Hardon A24CS0073

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `src/sequence_utils.py` : clean_sequence, is_valid_dna, gc_content, reverse_complement, find_motif
- `src/normalize.py` : proportions, cpm (never change the caller's data)
- `tests/` : visible tests and my own tests (test_lab05_own.py)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)

## Design decisions
proportions() raises ValueError when the total is zero because dividing by zero is not valid. The input list is not changed because the function returns a new list using a list comprehension instead of modifying the original list. The same approach is used in cpm().
