# create program that gathers the user's name, age, and hometown, then crafts
# a summary sentence using this information.
name = input("Pls Enter ur name :").strip()
age = input("How old ar u ?").strip()
hometown = input("where do u live ?").strip()

print(f"nice to know u {name.capitalize()} . so u are {age} years old !from lovely {hometown.capitalize()} ")

# pet description 
# write a program that asks for a pet's name ,species, and age, then generates
# a sentence describing the pet
pet_name = input("ur pet's name :").strip()
species = input("What species is it :").strip()
p_age = input("how old ur pet is :").strip()

print(f"ur pet name is {pet_name.capitalize()} . it's a {species.capitalize()} . and it has {p_age.capitalize()} year old")

# travel planner
# develop a program that requests a destination , mode of transport, and duration 
# of stay, then prints a brief travel plan 
destination = input("Pls Enter ur destination :").strip()
transport = input ("What is ur preferred mode of transport :").strip()
while True:
    duration_input = input("How long are you gonna stay there (in days)? ").strip()
    try:
        duration = int(duration_input)  # try for having num
        break  # if user did it right break the cycle
    except ValueError:
        print("Please enter a valid number! Try again...")

print(f"ur destination is {destination.capitalize()}. so u picked {transport.capitalize()} for transportation . and u r gonna sta there for {int(duration)} ")

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
