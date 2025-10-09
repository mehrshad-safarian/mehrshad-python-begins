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

# using a remove method with a try and except
country = ["Iran", "Usa", "China", "japan"]
try:
    country.remove("China")
except:
    print("that item does not exist in the list")
print(country)

# using min, max, and sum
digits = [8, 2, 9]
print(min(digits))
print(max(digits))
print(sum(digits))
 # using the sorted list 
nums = [1,2,6,9]
sorted_nums = sorted(nums)
print(nums, sorted_nums)

# using conditional statement on a list 
names = ["arthur", "john", "dutch"]
if "arthur" in names:
    print("found") # will run since arthur is on the list
if "micah" not in names:
    print("not found") # will run since micah is not on the list

# using conditionals to see if a list is empty
nums = []
if not nums: # could also say 'if nums == []'
    print("empty")
if nums == []:
   print("empty")

# using a for loop to print all items in a list
cities = ["Tehran", "lahijan", "new york", "minnesota", "chicago", "utah", "dallas", "Albuquerque"]
for city in cities:
    print(city)

# using the while loop to remove a certain value
names = ["Rdr2", "tlou2", "mgs3", "tlou2", "gow2"]
while "tlou2" in names:
    names.remove("tlou2") # removes all the instance of 'tlou2'
print(names)