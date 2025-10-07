# #using the try and except blocks, use tab to indent where necessary
# try:
#     temp = float( input("Type a number to add: "))
#     print( '100 = {} = {}'.format(temp, 100 + temp) )
# # without try/except print statement would not get hit if error occurs
# print("the program did not break!")

# type a number to add: 11
# 100 + 11.0 = 111.0
# print("the program did not break !")
for num in range (2, 10 ,2):
    print("value: {}".format(num) )

for num in range (5):
    if num == 2:
        continue
    print(num)
