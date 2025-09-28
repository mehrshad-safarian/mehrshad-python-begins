# #using the try and except blocks, use tab to indent where necessary
# try:
#     temp = float( input("Type a number to add: "))
#     print( '100 = {} = {}'.format(temp, 100 + temp) )
# # without try/except print statement woould not get hit if error occurs
# print("the program did not break!")

# type a number to add: 11
# 100 + 11.0 = 111.0
# print("the program did not break !")
destination = input("Pls Enter ur destination :").strip()
transport = input ("What is ur preferred mode of transport :").strip()
while True:
    duration_input = input("How long are you gonna stay there (in days)? ").strip()
    try:
        duration = int(duration_input)  # try for having num
        break  # if user did it right break the cycle
    except ValueError:
        print("Please enter a valid number! Try again...")

print(f"ur destination is {destination.capitalize()}. so u picked {transport.capitalize()} for transportation . and u r gonna sta there for {int(duration)} ")