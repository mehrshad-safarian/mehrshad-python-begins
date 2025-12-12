# is&is not
a = [1, 2, 3]
b = [1, 2, 3]
c = a 
print(a is c)
print(a is b)
print(a is not b)
print()

# in&not in
print(2 in a)
print(6 not in a)
print()

# Age validation
def validate_age(age):
    return 0 <= age <= 120
print(validate_age(25))   # True
print(validate_age(-5))   # False
print(validate_age(130))  # False