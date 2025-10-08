# to do : print numbers from 0 to 50 that are divisble by 5
for i in range (0, 50):
    if i % 5 == 0:
        print(i)      
        
print()

#to do : ask user to input a sentence and print only consonants(letters that are not vowels)
sentence = input("pls enter ur sentence :")
for letters in sentence :
    if letters not in "aeiou" :
        print(letters)