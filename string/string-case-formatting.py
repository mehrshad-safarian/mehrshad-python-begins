# format with .capitalize, .lower(), .upper(), . swapcase()
 #NOTE: use print()
msg0 = "Iran"
print(msg0.capitalize(),msg0.lower(),msg0.upper(), "iran".swapcase())

# get input for a variable , fav_food, that describes a favorite food 
fav_food = input("what is ur fav food ?")
print("so ! ur fav food is :",fav_food)
# display fav_food as ALL CAPS, used in a sentence
print("so ! ur fav food is :", fav_food.upper())
# display fav_food as all lower case, used in a sentence 
print("so ! ur fav food is :", fav_food.lower())
# display fav_food with swapped case used in sentence 
print("so ! ur fav food is :", fav_food.swapcase())
# display fav_food with capitalization, used in a sentence
#fav_color + "Forest Green"
msg01 = fav_food + " " + "Forest Green"
print("so ! ur fav food is :", msg01.capitalize())
# display the fav_color variable as upper, lower, swapcase, and capitalize formatting in a single print
print(f"{fav_food.upper()} {fav_food.lower()} {fav_food.swapcase()} {fav_food.capitalize()}")
# and also it works with this to :
# print(fav_food.upper(), fav_food.lower(), fav_food.swapcase(), fav_food.capitalize())
