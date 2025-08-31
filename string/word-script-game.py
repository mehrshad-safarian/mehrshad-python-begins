# get a word frrom the user
word = input("Enter a word: ")

# Find the length of the word
word_length = len(word)
print(f"the word'{word}' has {word_length} characters")

# Reverse the word
reverse_word = word[::-1]
print(f"the reverse word is : {reverse_word}")

# Create a new word by repeating the first character
char = word[0]
new_word = char * word_length
print(F"A new word which created by repeating the first character is: {new_word}")

# Concatenate the original word with a suffix
# Concatenate the original word with a suffix based on "type"
if word.endswith("e"):  # guess verb (like 'love', 'make')
    suffix_word = word + "ing"   # -> loving, making
    print(f"Looks like a verb, so with suffix: {suffix_word}")

elif word.endswith("y"):  # guess adjective (like 'happy')
    suffix_word = word[:-1] + "iness"   # -> happiness
    print(f"Looks like an adjective, so with suffix: {suffix_word}")

else:  # treat as noun by default
    suffix_word = word + "s"   # plural
    print(f"Looks like a noun, so with suffix: {suffix_word}")

# Convert the word to uppercase
uppercase_word = word.upper()
print(f"ur word in upper case : {uppercase_word}")

# Replace a character in the word
replacement_char = "x"
replaced_word = replacement_char + word[1:]
print(f"The word after replacing the first character with '{replacement_char}': {replaced_word}")
print(word[1:])