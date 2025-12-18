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

# Example 5: Comments and Docstrings
#this function calculates the factorial of a number
def factorial(n):
    """
    Calculate factorial of a number.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1

    return n * factorial(n - 1)


# Get input from the user
number = int(input("Please enter a number: "))

# Call the function and print the result
result = factorial(number)
print(result)
