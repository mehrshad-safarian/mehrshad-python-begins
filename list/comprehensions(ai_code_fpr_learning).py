# Original list of numbers
numbers = [1, 2, 3, 4, 5]

# Example 1: Regular for loop version
# We create an empty list, then use a loop to add each squared number
squares = []
for n in numbers:
    squares.append(n * n)

print("Squares (loop version):", squares)
# Output: [1, 4, 9, 16, 25]


# Example 2: List comprehension version (same result, shorter code)
# This creates a new list by taking each 'n' from 'numbers' and squaring it
squares_comprehension = [n * n for n in numbers]

print("Squares (list comprehension):", squares_comprehension)
# Output: [1, 4, 9, 16, 25]


# Example 3: List comprehension with a condition
# This only includes 'n' if it's even (n % 2 == 0)
even_squares = [n * n for n in numbers if n % 2 == 0]

print("Even squares only:", even_squares)
# Output: [4, 16]
