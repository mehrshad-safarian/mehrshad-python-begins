# #using the try and except blocks, use tab to indent where necessary
# try:
#     temp = float( input("Type a number to add: "))
#     print( '100 = {} = {}'.format(temp, 100 + temp) )
# # without try/except print statement would not get hit if error occurs
# print("the program did not break!")

# type a number to add: 11
# 100 + 11.0 = 111.0
# print("the program did not break !")
words = [] #empty list to store words.
while True: #a while loop that keeps asking the user for input.
    word = input(" Enter a word (type 'quit' to stop ) :").strip()
    if word.lower() == "quit":
         break
    if not word: 
         print("You entered nothing  try again.")
         continue
    words.append(word)

print("\nU enterd these words:")
for w in words:
    print(w)
