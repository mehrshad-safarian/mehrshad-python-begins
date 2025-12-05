# Boolean string methods
"""
.isalpha() - Returns True if all characters in the string are alphabetic
.isdigit() - Returns True if all characters in the string are digits
.isalnum() - Returns True if all characters in the string are alphanumeric
.islower() - Returns True if all characters in the string are lowercase
.isupper() - Returns True if all characters in the string are uppercase
.isspace() - Returns True if all characters in the string are whitespace
.istitle() - Returns True if the string is in title case (first letter of each word is uppercase)
.isprintable() - Returns True if all characters in the string are printable
.isnumeric() - Returns True if all characters in the string are numeric
.isdecimal() - Returns True if all characters in the string are decimal characters
.startswith(prefix) - Returns True if the string starts with the specified prefix
.endswith(suffix) - Returns True if the string ends with the specified suffix
.isidentifier() - Returns True if the string is a valid identifier
"""
"hello".isalpha()  # Returns: True
"python ".isalpha()  # Returns: False (contains space)

"3rd".isalnum()  # Returns: True (contains letters and digits)
"A Cold Stormy Night".istitle()  # Returns: True (title case)
"123".isdigit()  # Returns: True

cm_height = "1900"
cm_height.isdigit()  # Returns: True (all characters are digits)

cm_height = "1900"
print("cm_height:", cm_height, "is all digits =", cm_height.isdigit()) # Returns: True

print("SAVE".islower())  # Returns: False (uppercase)
print("SAVE".isupper())  # Returns: True (uppercase)

B = "Boolaen".startswith("B")  # Returns: True
print(B)