nums = [5, 10 ,15]
print(nums[ -2 : :])
print(nums[: : 2])

#adding a value to the beginning of the list 
word = ["Tehran", "Iran"]
word.insert(1, "shiraz") # first number is the index and second is the value
print(word)

# using pop to remove items and saving to a variable to use later
items = [5, "kermanshah", True]
items.pop() # by default removes the last item 
removed_item = items.pop(0) # removes 5 and saves it into the variable
print(removed_item, "\n", items)