# to do : print numbers from 1 to 100 that are divisble by 3
for i in range (1, 100):
    if i % 3 == 0:
        print(i)
# to do : take user input and print only the vowels
text = input ("Pls enter a word :")
for letter in text : 
    if letter.lower() in "aeiou":
        print(letter)