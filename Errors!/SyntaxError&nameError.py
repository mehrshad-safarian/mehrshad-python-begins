# 1) print needs parentheses → SyntaxError
#    print("Hello") ✔️   |   print "Hello" ✘

# 2) Strings must have matching quotes → SyntaxError
#    "Hi" ✔️   |   "Hi ✘

# 3) print must be lowercase and spelled right → NameError
#    print("Hi") ✔️   |   Print("Hi") ✘

# 4) Variable names cannot start with a number → SyntaxError
#    my_var = 5 ✔️   |   1st_var = 5 ✘

# 6) type(3.3( → SyntaxError
#    type(3.3) ✔️   |   type(3.3( ✘

# 7)print(days_of_week) → NameError (if days_of_week is not defined)
#    days_of_week = 7; print(days_of_week) ✔️   |   print(days_of_week) ✘

# SyntaxError → You broke Python grammar.
# Example: print "Hi"

# TypeError → You used the wrong data types together.
# Example: 3 + "5"

# NameError → You used a name that doesn’t exist.
# Example: Print("Hi")
