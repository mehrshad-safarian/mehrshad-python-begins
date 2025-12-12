if True: # This condition is literally True, so this block will always run
    print("This prints if statement after 'if' is True")  # This line will be executed
else:  
    print("This prints if statements is not True")        # This line will NOT run

print()

if not True: # not True becomes False(also we can use False instead of not True), so this condition is False
    print("This prints if statement after 'if' is True")  # This line will NOT run
else:
    print("This prints if statements is not True")        # Because the if is False, this runs
print()

someone_i_know = False
if someone_i_know:
    print("how u doin?")
else:
    print("who the heel r u ?")

someone_i_know = True
if someone_i_know:
    print("how u doin?")
else:
    print("who the heel r u ?")

someone_i_know = not True
if someone_i_know:
    print("how u doin?")
else:
    pass


favorite_book = input ("Enter the title of a favorite book:") 
if favorite_book.istitle():
    print(favorite_book,"-nice capitalization in that title!")
else:
    print(favorite_book,"-Tip: capitalize each word for book titles.")
print()

a_number = input("Enter a positive integer number: ")
if a_number.isdigit():
    print(a_number, "is a positive integer number.")
else:
    print(a_number, "is NOT a positive integer number.")
# another if
if a_number.isalpha():
    print(a_number, "is more like a word")
else:
    pass






# write a code in that the someone u know is the q if u know him/her
# Loop forever until the user gives a valid answer
""""while True:
    # Ask the question
    answer = input("hey buddy do u know me? i'm ur classmate! (answer with Yes/No): ")
    # Normalize the input
    answer = answer.lower()  # makes YES, Yes, yEs all become "yes"
    # Check for valid answers
    if answer == "yes":
        print("hey how u doin ?")
        break  # exit the loop because the user answered correctly
    elif answer == "no":
        print("who the f r u?")
        break  # also exit the loop
    else:
        # If it's not Yes or No, tell the user and repeat the loop
        print("bro answer with Yes or No only…")
"""""