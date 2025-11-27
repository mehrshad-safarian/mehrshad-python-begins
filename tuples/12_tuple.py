# Tuples. Tuples are immutable
# Creating tuples
# Create an empty tuple
empty_tuple = ()
# Tuples with mixed data types
mixed_tuple = ("monitor", 2.1, False, 70)
# Tuples without parentheses
numbers = 1, 2, 3, 4, 5, 6
# Accessing tuple elements
print(mixed_tuple[1])  # Output: 2.1
# Tuple immutability
# numbers[0] = 10  # This will raise a TypeError because tuples are immutable
new_numbers = numbers + (7, 8)  # Creating a new tuple by concatenation
print(new_numbers)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)
# Tuple packing and unpacking
# Tuple packing
coordinates = 10, 20, 30
# Tuple unpacking
x, y, z = coordinates
print(f"X:{x}, Y:{y}, Z:{z}")
