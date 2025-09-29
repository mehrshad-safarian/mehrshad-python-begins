# days to hours 
# develop program that asks for a number of days , converts it into an integer ,
# then calculates and prints the equivalent number into hours 
while True:
    days_input = input("Pls enter number of days :").strip()
    try:
        days = int(days_input)  # try for having num
        break  # if user did it right break the cycle
    except ValueError:
        print("Pls enter a valid number! Try again...")

hours =   days * 24
print(f"{days} days is equal to {hours} hours")