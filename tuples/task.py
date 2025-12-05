# Tasks
print("Python".isalpha()) # True
print("3rd".isalnum()) # True
print("A Cold Stormy Night".istitle()) # True
print("1003".isdigit()) # True

cm_height = "176"
print("cm height:", cm_height, "is all digits =", cm_height.isdigit()) # True

print("SAVE".islower()) # False
print("SAVE".isupper()) # True
print("Boolean".startswith("B")) # True

# test strings with .isalpha()
# Use .isalpha() on the string "alphabetical"
print("alphabetical".isalpha())   # True

# Use .isalpha() on the string: "Are spaces and punctuation Alphabetical?"
print("Are spaces and punctuation Alphabetical?".isalpha())   # False

# initialize variable alpha_test with input
alpha_test = input("Enter a word: ")
# use .isalpha() on string variable alpha_test
print(alpha_test.isalpha())