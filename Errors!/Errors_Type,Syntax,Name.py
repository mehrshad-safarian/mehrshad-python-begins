""" print("my number is" + "123") # string, represents a text character
    print("my number is" + 123)   # number, with numeric value

    my_num = 123
    num_intro = "my number is " + my_num
"""
# we only can combine string with string
# and number with number

"""
# Task 0
# Fix TypeError
# then fix any Errors
total_cost = 3 + "45"
print(total_cost)
# run the code - then fix any Errors
school_num = 123
print("the street number of Central School is " + school_num)
# write a hypothesis for what you observe adding float + int
# HYPOTHESIS:
print(type(3.3))
"""

# Fix TypeError
# then fix any Errors
total_cost = 3 + 45
print(total_cost)
# run the code - then fix any Errors
school_num = "123"
print("the street number of Central School is " + school_num)
# write a hypothesis for what you observe adding float + int
# HYPOTHESIS:
print(type(3.3))
# HYPOTHESIS:
# When adding a float and an int, Python converts the int to a float
# and the final result will be a float.
result = 3.0 + 2
print(result)
print(type(result))