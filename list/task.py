# task num 0 remove the duplicate names
# names = ['Bob', 'kenny', 'amanda', 'Bob', 'kenny']
names = ["Bob", "kenny", "amanda", "Bob", "kenny"]
while "Bob" in names:
    names.remove("Bob")
while "kenny" in names:
    names.remove("kenny")
print(names)
""" we also can do the task by the following codes 
#num0 
names = ["Bob", "kenny", "amanda", "Bob", "kenny"]
for name in ["Bob", "kenny"]:
    while name in names:
        names.remove(name)
print(names)

#num1
names = ["Bob", "kenny", "amanda", "Bob", "kenny"]
names = [n for n in names if n not in ["Bob", "kenny"]]
print(names)

#num2
names = ["Bob", "kenny", "amanda", "Bob", "kenny"]
names = list(set(names))
print(names)
"""

# Use a while loop to continually ask the user to input a word, until
# they type "quit". Once they type a word in, add it to a list. Once they
# quit, use a for loop to output all items within the list.bbt  war  
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
