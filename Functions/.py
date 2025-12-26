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
"""
Line-by-line Explanation
def msg_double(phrase):
This defines a function called msg_double that takes one parameter named phrase.
double = phrase + " " + phrase
Inside the function, a new variable called double is created.
It combines the input text twice with a space between them.
For example: "let's go" + " " + "let's go" becomes → "let's go let's go"
return double
The function sends the final value (the doubled phrase) back to where the function was called.
In other words, this is the output of the function.
msg_2x = msg_double("let's go")
The function is called with the argument "let's go", and the returned value is stored in msg_2x.
print(msg_2x)
This prints the value stored in msg_2x.
"""

"""
What is a Function Return Value?
A return value is the final result that a function gives back after it finishes running.
When you use the return keyword:
The function ends immediately.
The value after return is sent back to where the function was called.
You can save it in a variable, print it, or use it in another calculation.
Simple definition:
A return value is what a function gives you back so you can use it later.
"""

"""
| Concept      | Meaning                                   |
| ------------ | ----------------------------------------- |
| Function     | A block of code that does something       |
| Parameter    | Input for the function                    |
| Return value | The result/output the function gives back |
| `return`     | Sends the result to the caller            |

"""



def half_value(value):
    return value / 2
print(half_value(float(input("pls enter number you want it to be half : "))))
      
# math square op
import math  # for using math.sqrt()
def square_root_value(value):
    # Return the square root of the input number
    return math.sqrt(value)
number = float(input("pls enter the number you want to take the square root of: "))
print(square_root_value(number))
