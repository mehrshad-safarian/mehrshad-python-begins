# create program that gathers the user's name, age, and hometown, then crafts
# a summary sentence using this information.
while True:
    name = input("Pls Enter ur name :").strip()
    if name:         
        break
    else:
        print("Pls enter at least one word!")

while True:
    age_input = input("How old ar u ?").strip()
    try:
        age = int(age_input)  # try for having num
        break  # if user did it right break the cycle
    except ValueError:
        print("Pls enter a valid number! Try again...")

while True:
    hometown = input("where do u live ?").strip()
    if hometown:         
        break
    else:
        print("Pls enter at least one word!")


print(f"nice to know u {name.capitalize()} . so u are {age} years old !from lovely {hometown.capitalize()} ")

# pet description 
# write a program that asks for a pet's name ,species, and age, then generates
# a sentence describing the pet
while True:
    pet_name = input("ur pet's name :").strip()
    if pet_name:         
        break
    else:
        print("Pls enter at least one word!")

while True:
    species = input("What species is it :").strip()
    if species:         
        break
    else:
        print("Pls enter at least one word!")

while True:
    p_age0 = input("how old ur pet is :").strip()
    try:
        p_age = int(p_age0)  # try for having num
        break  # if user did it right break the cycle
    except ValueError:
        print("Pls enter a valid number! Try again...")

print(f"ur pet name is {pet_name.capitalize()} . it's a {species.capitalize()} . and it has {p_age} year old")

# travel planner
# develop a program that requests a destination , mode of transport, and duration 
# of stay, then prints a brief travel plan 
while True:
    destination = input("Pls Enter ur destination :").strip()
    if destination:          
        break
    else:
        print("Pls enter at least one word!")

while True:
    transport = input("What is your preferred mode of transport: ").strip()
    if transport:         
        break
    else:
        print("Pls enter at least one word!")

while True:
    duration_input = input("How long are you gonna stay there (in days)? ").strip()
    try:
        duration = int(duration_input)  # try for having num
        break  # if user did it right break the cycle
    except ValueError:
        print("Pls enter a valid number! Try again...")

print(f"ur destination is {destination.capitalize()}. so u picked {transport.capitalize()} for transportation . and u r gonna stay there for {int(duration)} day's")

# summary 
summary = f"""
--- User Info ---
Name: {name.capitalize()}
Age: {age}
Hometown: {hometown.capitalize()}

--- Pet Info ---
Pet Name: {pet_name.capitalize()}
Species: {species.capitalize()}
Pet Age: {p_age} years old

--- Travel Plan ---
Destination: {destination.capitalize()}
Transport: {transport.capitalize()}
Duration: {duration} days
"""

print(summary)
