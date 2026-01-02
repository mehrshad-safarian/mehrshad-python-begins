# Using the keyword 'in' within an if statement 
word = "Baseball"
if 'b' in word:
    print("{} contains the character 'b' ".format(word))

# Using the keyword 'not in' within an if statement 
word = "Baseball"
if 'x' not in word:
    print("{} does not contain the character 'b' ".format(word))


# Case sensitivity matter
word = "XBaseball"
if 'x' in word.lower():
    print("{} contain the character 'x' ".format(word))
