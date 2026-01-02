# writing multiple conditionals within each other-multiple block levels
x, y, z = 5, 10, 5
if x > y:
    print("greater")
elif x <= y:
    if x == z:
        print("x is equal to z") # resulting output
elif x != z:
    print("x is not equal to z") #wont get hit
print()

# testing output of two if statements in row that are both True
x, y, z = 5, 10, 5
if x < y:
    print("x is less")
if x == z:
    print("x is equal")
print()

# Testing output of an if and elif statement that are both true
x, y, z = 5, 10, 5
if x < y:
    print("x is less")
elif x == z:
    print("x is equal to z")