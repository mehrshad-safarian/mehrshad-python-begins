# Using an if statement to only run code if the condition is met 
x, y = 5, 10 
if x < y :
    print("x is less than y")

# Checking user inputs 
tmp = int(input("What is 5 + 5?"))
if tmp == 10:
    print(" U got it right !")


# Using else statement
name = "mehrshad"
if name == "mehrshad":
    print("Hello", name)
else:
    print("hello{}!".format(name))

# Using the elif conditional statement
x, y = 5, 10 
if x > y:
    print("x is greater")
elif x > y:
    print("x is less")
# Checking more than one elif conditional statements
x, y = 5, 10 
if x > y:
    print("x is greater")
elif(x + 10) < y: #checking if 15 is less then 10
    print("x is less")
elif(x + 5) == y: # checking if 10 is equal to 10
    print("x is equal")