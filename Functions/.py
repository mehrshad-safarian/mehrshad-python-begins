# Function parameter
def say_this(phrase):
    print(phrase)
say_this("Hi")

def yell_this(phrase):
    print(phrase.upper() + "!")
yell_this("good morning")
print()
# Default Argument
def yell_this(phrase = "good night"):
    print(phrase.upper() + "!")
yell_this("good morning")
yell_this()
"""
This function uses a default argument.
The parameter phrase has a default value "good night", which means:
If you call the function with a value (e.g., "good morning"), it uses that value.
If you call the function without any argument, it automatically uses the default value.
The function converts the text to uppercase using .upper() and then prints it with an exclamation mark."""

# Function return value
def msg_double(phrase):
    # Create a new string that repeats the phrase twice
    double = phrase + " " + phrase
    return double

# Call the function and store the result
msg_2x = msg_double("let's go")

# Print the output
print(msg_2x)
