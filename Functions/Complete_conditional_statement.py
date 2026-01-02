name = input("Pls enter ur name :")
if name[0] == "A":
    print("ur name starts with a 'a' ")
elif name[0] == "B":
    print("ur name starts with a 'b' ")
else: # Covers all other letters
    print("ur name starts with a {}".format( name[0]))