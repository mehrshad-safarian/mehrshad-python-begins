#Tasks
# get user input for a city name in the variable named city
# print the city name
# create variables to store input: name, age, get_mail with prompts
# for name, age and yes/no to being on an email list
# print a description + variable value for each variable

city = input("pls enter the name of the city u live in :")
# lets a little bit magic :)
# groups of prefixes
special_prefixes = ('t', 'k', 'l', 'sh', 'bo', 'ah', 'ab')

if city.startswith(special_prefixes):
    print(city.title(), "is a lovely city")
else:
    print(city.title(), "is a nice city")

name = input("pls enter ur name :")
age = input("pls enter ur age :")
get_email = input("would u like to be on our email list ? (yes/no)")

print("nice to know u", name)
print(f"so u are {age} year old !")

email_Pcondictatin = ("yes", "y")
email_Ncondictatin = ("no", "n")

if get_email.lower() in email_Pcondictatin:
    print("Great u are on the vip guest list")
elif get_email.lower() in email_Ncondictatin:
    print("i\'m so sorry ! u are not invited")
else:
    print("sorry ur answer wasnt clear so u cant get in to the party !")