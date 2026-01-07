favorite_book = input("pls enter the name of ur fav book:")
if favorite_book.istitle():
    print(favorite_book,"- nice capitalization in that title!")
else:
    print(favorite_book,"- Tip: capitalize each word for book titles.")

####

a_number = input("enter positive integer number:")
if a_number.isdigit():
    print(a_number, "is a positive integer")
else:
    print(a_number, "is not a positive integer")
# another if
if a_number.isalpha():
    print(a_number, "is more like a word")
else:
    pass
print()

####
