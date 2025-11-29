# Tuples. Tuples are immutable
# Creating tuples
# Create an empty tuple
empty_tuple = ()
# Tuples with mixed data types
mixed_tuple = ("monitor", 2.1, False, 70)
# Tuples without parentheses
numbers = 1, 2, 3, 4, 4, 5, 6
#  1. What is numbers = 1, 2, 3, 4, 4, 5, 6 ?
# You might think this creates 6 separate variables,
# but Python actually turns this into one tuple:
# # numbers = (1, 2, 3, 4, 5, 6)

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
# Tuples methods 
# Count (element)
# index(element)
print(numbers.count(2))
print(numbers.count(4))
# Tuples as Return Values
def get_name_and_age():
    name = "arthur"
    age = 36
    return name, age # is equivalent to return (name, age)
result = get_name_and_age()
print(result)

# the return tuple can be unpacked into individual variables if desired 
name, age = get_name_and_age()
print(f"Name: {name}, Age: {age}") # in this case the return tuple is unpacked into name and age variables allowing us to access individual values separately . 