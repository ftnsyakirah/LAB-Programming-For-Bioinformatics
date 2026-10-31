# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 1
- Student name: Fatin Syakirah Binti Muhamad Hardon
- Matric no: A24CS0073
- Group ID: n/a
- AI level: 1 - see the assessment brief>
- Tools cited: Microsoft (2026), Copilot. Retrieved 23 October 2026 from https://copilot.microsoft.com 

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 22 October 2026, 9:30 PM
- Tool: Microsoft (2026). Copilot. Retrieved 23 October 2026 from https://copilot.microsoft.com
- Purpose: explain, setup
- Prompt: how to create a venv for a Python project
Output: AI explained to first ensure the correct project directory is used, then run `python -m venv .venv` and activate with `.venv\Scripts\activate`.
- Verified by: Navigated into the correct folder, ran commands in terminal, saw `(.venv)` appear in prompt.
- My change: Accepted instructions, created and activated venv in the right directory before installing packages.
- Used in: project setup (lab01/.venv)


## Entry 2

- Date: 22 October 2026, 11:25 PM
- Tool: Microsoft (2026), Copilot. Retrieved 23 October 2026 from https://copilot.microsoft.com 
- Purpose: explain,debug
- Prompt:  Python: 3.15.0 on Windows numpy NOT INSTALLED pandas NOT INSTALLED matplotlib NOT INSTALLED scikit-learn NOT INSTALLED biopython NOT INSTALLED pytest NOT INSTALLED
- Output: AI explained that packages were not installed and suggested using `pip install numpy --only-binary=:all:`, `pip install pandas matplotlib scikit-learn biopython pytest` and `pip list`
- Verified by: Ran python src/env_check.py and checked environment_report.txt 
- My change: Accepted the explanation, installed packages, reran script.
- Used in: src/env_check.py evidence report

## Entry 3

- Date: 23 October 2026, 2:30 PM
- Tool: Microsoft (2026). Copilot. Retrieved 23 October 2026 from https://copilot.microsoft.com
- Purpose: explain, guidance
- Prompt: just all these to commit right?
- Output: AI explained which files to stage (`src/basics.py`, `src/env_check.py`, `tests/test_lab01_own.py`, `results/environment_report.txt`, `AI_USE_LOG.md`, `README.md`) and showed the correct git add/commit/push commands.
- Verified by: Ran `git add`, `git commit -m`, and `git push` in terminal, confirmed changes appeared in GitHub repo.
- My change: Accepted instructions, committed all relevant files with proper messages.
- Used in: GitHub commit history for Lab 1 submission