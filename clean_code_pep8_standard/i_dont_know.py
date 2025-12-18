# Bad version of thing we want
# def f(x,y):
#     z=x+y
#     return z

# Good version of thing we want
def add_numbers (number_one, number_two):
    """
    Add two numbers and return the result.
    Args:
    number_one (int): The first number to add
    number_one (int): The first number to add
    :param number_one:
    :param number_two:
    :return:
    """
    return number_one + number_two
# Usage example
result = add_numbers(number_one=5, number_two=10) 
print(f"the sum of 5 and 10 is: {result}")

# Using meaningful names 
# Less clear version
def calc(a, b):
    return a * b

# More clear version
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    Args:
    length (int): The length of the rectangle
    width (int): The width of the rectangle
    :param length:
    :param width:
    :return:
    """
    area = length * width
area = calculate_rectangle_area(length = 5, width = 10)
print(f"The area of a rectangle with length 5 and width 10 is: {area}")