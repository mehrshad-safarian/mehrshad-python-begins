# todo 1: Get user input
import random
while True:
    try:
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
        break
    except ValueError:
        print("That's not a valid number! Please try again.")
