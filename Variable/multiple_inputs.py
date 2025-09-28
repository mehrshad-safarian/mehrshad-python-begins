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