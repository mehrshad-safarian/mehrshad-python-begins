#  write program that inquires about the user's favorite color and responds with
# the comment about the color

fav_color = input("Pls Enter ur fav color :")
special_colors = ('green','blue,','yellow','turquoise')
bad_colors = ('red','black')

if fav_color in special_colors :
    print("ow!!!! u have got good taste to ur self congrats to that ;)")
elif fav_color in bad_colors :
    print("u got be kiding right ? u saying that for real ???")
else :
    print("nice !")