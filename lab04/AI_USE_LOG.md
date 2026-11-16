# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 4
- Student name: Fatin Syakirah Binti Muhamad Hardon
- Matric no: A24CS0073
- Group ID: n/a
- AI level: 1 
- Tools cited: Microsoft (2026), Copilot. Retrieved 15 November 2026 from https://copilot.microsoft

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 15 November 2026, 7:30 PM
- Tool: Microsoft (2026), Copilot. Retrieved 15 November 2026 from https://copilot.microsoft
- Purpose: explain
- Prompt: can you help me to explain this lab04 step by step?
- Output: Explained the requirements for T1-T4, including the use of lists, NamedTuple, dictionaries, sets, sorting with keys, and handling edge cases. Provided guidance on the logic and algorithm for each function
- Verified by: ran python -m pytest after implementing the functions and checked code quality using ruff check src
- My change: Used the explanations to implement the functions myself, adapting the logic to the starter code and testing the results before accepting them.
- Used in: src/panel.py 

## Entry 2

- Date: 16 November 2026, approximately 5:00 PM
- Tool:  Microsoft (2026), Copilot. Retrieved 16 November 2026 from https://copilot.microsoft
- Purpose: review
- Prompt: can you help me check this lookup.py whether my implementation is correct and help me complete the remaining functions?
- Output: Reviewed the code structure, explained the expected behaviour of CODON_TABLE, count_bases(), kmer_counts(), shared_genes(), safe_expression(), and translate(), and pointed out important edge cases such as handling 0.0, invalid codons, and k-mer validation.
- Verified by: Ran python -m pytest until all tests passed and ran ruff check src to confirm there were no style issues.
- My change: Compared the explanations against the assignment requirements, implemented the functions in my own code, and adjusted the solutions where necessary to match the starter template and test expectations.
- Used in: src/lookup.py

## Entry 3

- Date: 16 November 2026, 8:30 PM
- Tool: Microsoft (2026), Copilot. Retrieved 16 November 2026 from https://copilot.microsoft
- Purpose: review
- Prompt: can you check whether my test\_lab04\_own.py code is correct and covers the required cases?
- Output: Reviewed the test file against the lab requirements and confirmed that the tests covered preservation of the original list, chromosome ordering, k-mer edge cases, and expression lookup behaviour. Also checked that the assertions matched the expected function outputs
- Verified by: Ran python -m pytest and confirmed that all tests passed successfully.
- My change: Updated and refined my test cases based on the review, then reran the test suite to verify correctness
- Used in: tests/test\_lab04\_own.py