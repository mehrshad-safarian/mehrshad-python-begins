# #using the try and except blocks, use tab to indent where necessary
# try:
#     temp = float( input("Type a number to add: "))
#     print( '100 = {} = {}'.format(temp, 100 + temp) )
# # without try/except print statement woould not get hit if error occurs
# print("the program did not break!")

# type a number to add: 11
# 100 + 11.0 = 111.0
# print("the program did not break !")
while True:
    transport = input("What is your preferred mode of transport: ").strip()
    if transport:          # یعنی خالی نباشه
        break
    else:
        print("Please enter at least one word!")
print(transport)
