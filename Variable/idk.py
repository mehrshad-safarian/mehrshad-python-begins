# Write a program that:
# asks the user for a character name, a place, and an adjective,
# then weaves those three inputs into a short short story and prints it.
name = input("Pls enter a character name :").strip()
place = input("Pls enter a place:").strip()
obj = input("Pls enter an object:").strip()
print(f"One day, {name.capitalize()} went to {place.capitalize()} and  discovered a mysterious {obj.capitalize()}.")
print(f"and {name.capitalize()}  loved the {obj.capitalize()}")