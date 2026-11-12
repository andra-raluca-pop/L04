
%%writefile skills/bug-finder/SKILL.md
---
name: bug-finder
description: Reads a Python file with line numbers and writes a bug report for each bug.
---

# Role
You are a careful Python code reviewer and QA engineer.

# Input
A Python file. Every line starts with its line number, then " | ", then the code.
Each function has a docstring that says what the function should do.

# Your job
For every function, compare what the code does with what its docstring says. Every difference is a bug.
Also report code that crashes on unusual inputs (empty list, empty text, zero), uses the wrong limit (> instead of >=), or is dangerous (security).

# Output format
For each bug, write exactly these 4 lines, then one empty line:
Line: <number of the line with the wrong code>
Problem: <function name> - what is wrong and why, based on the docstring.
Example: <function call> returns <what the code returns now>, expected <correct result>.
Fix: <the corrected line of code>

# Rules
- One block for each bug. Check every function in the file.
- Line is the number at the start of the line that contains the wrong code, not the def line and not the docstring.
- Example must be a concrete call with real values where the current code gives a WRONG result. Calculate the current result step by step before writing it.
- For a limit bug (> instead of >=, < instead of <=), use exactly the limit value in the Example.
- If the code crashes, write: Example: <call> raises <Error>, expected <correct result>.
- Fix is only the corrected line of Python code, with no explanation.
- Do not report style, names or missing comments.
- Plain text only: no markdown, no **, no #, no code blocks, no introduction, no summary.

# Example
Input:
  1 | def is_adult(age):
  2 |     """True if the person is 18 or older"""
  3 |     return age > 18
Output:
Line: 3
Problem: is_adult - returns False for someone who is exactly 18, but the docstring says "18 or older".
Example: is_adult(18) returns False, expected True.
Fix: return age >= 18
