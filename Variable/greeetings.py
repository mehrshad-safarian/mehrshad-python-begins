# greeting program 
# Create a simple program that asks for user's name responds with
# personalized greeting .

name = input("Pls enter ur name :")
special_prefixes = ('m','a','v','r','s','f','gh','h')

if name.startswith(special_prefixes):
    print(f"welcome !".title(),name,"nice to know u !")
else:
    print("welcome",name )