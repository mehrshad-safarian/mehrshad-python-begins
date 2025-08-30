# use .isalpha() on the string "alphabetical"    
print("alphabetical".isalpha())  # True

# use .isalpha() on the string "Are spaces and punctuation Alphabetical?"
print("Are spaces and punctuation Alphabetical?".isalpha())  # False

# initialize variable alpha_test with input 
# use .isalpha() on string variable alpha_test
the_test = input ("enter single alphabetical word that has no digit,spaces and spacial symbol\,s :")
print("have u write it correct ?",the_test.isalpha())