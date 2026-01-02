# Using the keyword 'and' in an 'if statement'
x, y, z = 5, 10, 5
if x < y and x == z:
    print("Both statements were True")
print()

# Logical operator 'or'
x, y, z = 5, 10, 5
if x < y or x != z:
    print("One or both statement were True")
print()

# Using the keyword 'not' within an 'if statement'
flag = False
if not flag: # SaME as sying if not True
    print("Flag is False")
