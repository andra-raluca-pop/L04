# Bug reports for exercise2.py

Line: 3
Problem: is_passing - returns False for a grade of exactly 5, but the docstring says "5 or more".
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password - fails for passwords with exactly 8 characters (should pass if at least 8 and has a digit).
Example: is_valid_password("12345678") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 13
Problem: clamp - uses low twice in min(x, low), should be min(x, high) to clamp to high.
Example: clamp(10, 1, 5) returns 1, expected 5.
Fix: return max(low, min(x, high))
