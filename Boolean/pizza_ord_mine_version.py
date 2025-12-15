"""
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
"""
import random

def generate_order_id():
    """
    Generates a unique order ID for each order.
    """
    return random.randint(100000, 999999)


def show_menu():
    """
    Displays the pizza menu.
    """
    print("\nIRAN PIZZA CENTER")
    print("\nPIZZA MENU")
    print("1. Margherita  - $8")
    print("2. Pepperoni   - $10")
    print("3. Veggie      - $9")


def show_addons():
    """
    Displays available add-ons.
    """
    print("\nADD-ONS MENU")
    print("1. Sausage    - $2")
    print("2. Soda       - $1")
    print("3. Onion      - $1")
    print("4. Mushrooms  - $2")
    print("5. Fries      - $3")


def get_pizza_choice():
    """
    Gets and validates the user's pizza choice.
    """
    while True:
        choice = input("Choose a pizza (1-3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def get_quantity():
    """
    Gets and validates the pizza quantity.
    """
    while True:
        try:
            quantity = int(input("How many pizzas do you want? "))
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid number.")


def get_addons():
    """
    Allows the user to select multiple add-ons.
    """
    addons = {
        "1": ("Sausage", 2),
        "2": ("Soda", 1),
        "3": ("Onion", 1),
        "4": ("Mushrooms", 2),
        "5": ("Fries", 3)
    }

    selected_addons = []
    total_addon_price = 0

    show_addons()
    print("Enter add-on numbers one by one. Type 'done' when finished.")

    while True:
        choice = input("Add-on choice: ")

        if choice.lower() == "done":
            break

        if choice in addons:
            selected_addons.append(addons[choice][0])
            total_addon_price += addons[choice][1]
            print(f"{addons[choice][0]} added.")
        else:
            print("Invalid add-on choice.")

    return selected_addons, total_addon_price


def calculate_pizza_price(pizza_choice, quantity):
    """
    Calculates pizza price.
    """
    prices = {
        "1": 8,
        "2": 10,
        "3": 9
    }
    return prices[pizza_choice] * quantity


def main():
    """
    Main function that runs the ordering system.
    """
    print("Welcome to IRAN Pizza Center")

    show_menu()
    pizza_choice = get_pizza_choice()
    quantity = get_quantity()

    pizza_price = calculate_pizza_price(pizza_choice, quantity)
    addons, addons_price = get_addons()

    total_price = pizza_price + addons_price
    order_id = generate_order_id()

    print("\nORDER SUMMARY")
    print(f"Order ID: {order_id}")
    print(f"Pizzas Ordered: {quantity}")
    print(f"Pizza Price: ${pizza_price}")

    if addons:
        print("Add-ons:", ", ".join(addons))
        print(f"Add-ons Price: ${addons_price}")
    else:
        print("Add-ons: None")

    print(f"TOTAL PRICE: ${total_price}")
    print("\nThank you for choosing IRAN Pizza Center")


# Run the program
main()
