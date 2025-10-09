# Loop through numbers from 2 to 8 with a step of 2
for num in range (2, 10 ,2):
    print("value: {}".format(num) )
print()

# Loop from 0 to 4, skip printing when the number is 2
for num in range (5):
    if num == 2:
        continue
    print(num)
print()

# Loop from 0 upwards, stop the loop completely when the number reaches 4
for num in range (10):
    if num == 4:
        break 
    print(num)