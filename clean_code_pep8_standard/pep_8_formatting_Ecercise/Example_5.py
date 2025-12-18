# Example 5: Comments and Docstrings
#this function calculates the factorial of a number
# def factorial(n):
#     """Calculate factorial"""
#     if n == 0: return 1
#     else: return n * factorial(n - 1)

""" Violation:
Incorrect comment formatting
Insufficient docstring
Multiple statements on one line
"""

def factorial(n):
    """Calculate factorial"""
    if n == 0: return 1
    else: return n * factorial(n - 1)