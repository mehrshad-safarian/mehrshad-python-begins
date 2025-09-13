# Basic Variables Naming Rules

# 1. Start with a letter or underscore (a-z, A-Z)(_).
age = 25
_secret = "Shh!"
# 2fast = "Speedy!"  # This will cause an error

# 2. Use letters, numbers or underscores (az, a_)
user_age_2 = 30
best_friend_1 = "Alice"
# my-variable = 10  # Hyphens are not allowed.

# 3. Case sensitive (az, aZ, A_, a_).
Age =25
age = 27
AGE = 30

print(Age)
print(age)
print(AGE)

# 4. No reserved words (from, del).
# from = "New York"  # This will cause an error.
# if = 5  # This too.
# print = "Hello"

# Best practices.

# 1. Be descriptive.
user_age = 25
a = 25  # Not so good! What does 'a' mean?

# 2. Use underscores for spaces.
first_name = "John"
second_name = "Doe"
firsname = "Hohn"  # Okay, but less readable.
secondname = "Boe"  # Okay, but less readable.

# 3. Keep it simple.
max_speed = 100  # Excellent!
maximum_car_speed_on_highway = 150  # Too long!

# Common mistakes

# 1. Starting with a number
# 1st_place = "gold"  # Nope can't start with a number

# 2. Using spaces
# my variable = 10  # Incorrect

# 3. Using special characters
# user@mail = 'mymail@mydomain.com'  # Incorrect
