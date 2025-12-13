"""# todo 1: Get user input
import random
def generate_order_id():
    return random.randint(0, 10**12)

orders = []

slice = int(input("slices:"))
price = float (input("price:"))

order_id = {
    "order_id": generate_order_id(),
    "slices": slice,
    "price_per_slice": price 
}

orders.append(order_id)

print("\n All orders:")
for o in orders:
      print(f"Order ID: {o['order_id']}, Slices: {o['slices']}, Price per slice: {o['price_per_slice']}$")
# todo 2: Calculate total price
total = slice * price
# todo 3: Verify receipt
receipt = 123456
if total == receipt:
    print("verified")
else:
    print("Error")
"""




# Pizza Order Verification System
# Follow these TODO steps to complete the exercise!

# Problem Description:
# You are working as a developer for "Python Pizza Palace". They need a system
# to verify customer orders against receipt numbers. The system should take two inputs
# from the customer (number of slices and price per slice) and check if their
# # multiplication matches the receipt number stored in the system.
# while True:
#     try:
# # TODO 1: Create a variable called 'receipt_number' and assign it any four-digit number
# # Hint: This will be the number that customers need to match with their order details
#         receipt_number = 25  # Replace None with your number
# # TODO 2: Create an input statement to get the number of pizza slices from the customer
# # Hint: Remember to convert the input to an integer using int()
# # Hint: Use a descriptive prompt message for the customer
#         slice = int(input("How many slices:"))
# # TODO 3: Create another input statement to get the price per slice
# # Hint: Similar to TODO 2, remember to convert to integer
# # Hint: Use clear prompt message
#         price_per_slice = float(input("Price per slice:"))
# # TODO 4: Calculate the total by multiplying slices with price_per_slice
# # Hint: Create a variable to store the result of multiplication
#         total = slice * price_per_slice
# # TODO 5: Compare the calculated total with receipt_number and print the result
# # Hint: Use the == operator for comparison
# # Hint: This should print True if they match, False if they don't
#         print(total == receipt_number)

#         break
# # BONUS TODO 6: Add error handling for invalid inputs
# # Hint: What happens if someone enters "abc" instead of a number?
# # Hint: Look into try/except blocks
#     except ValueError:
#         print("That's not a valid number! Please try again.")

# Test your code with these cases:
# Test Case 1: If receipt_number is 2470
#   - Input 26 slices and 95 per slice
#   - Expected output: True (because 26 * 95 = 2470)
#
# Test Case 2: If receipt_number is 2468
#   - Input 28 slices and 88 per slice
#   - Expected output: False (because 28 * 88 = 2464)

while True:
    try:
        receipt_number = 2470
        slice = int(input("How many slices:"))
        price_per_slice = float(input("Price per slice:"))
        total = slice * price_per_slice
        print(total == receipt_number)

        break
    except ValueError:
        print("That's not a valid number! Please try again.")