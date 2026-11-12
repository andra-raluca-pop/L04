# Bug reports for exercise1.py

Line: 3
Problem: is_even - returns True for odd numbers but the docstring says "true for even numbers".
Example: is_even(3) returns True, expected False.
Fix: return n % 2 == 0

Line: 8
Problem: rectangle_area - returns sum of width and height, not the product as described in the docstring.
Example: rectangle_area(4, 5) returns 9, expected 20.
Fix: return width * height

Line: 13
Problem: double - adds 2 to n, but the docstring says "twice the number n", meaning n * 2.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
