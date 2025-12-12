def is_price_valid(price):
    MIN_PRICE = 10.00   # minimum allowed price
    MAX_PRICE = 99.99   # maximum allowed price

    # returns True if price is within allowed range
    return MIN_PRICE <= price <= MAX_PRICE
print(f"50 is a valid price: {is_price_valid(50)}")   # True
print(f"5 is a valid price: {is_price_valid(5)}")    # False
input_price = float(input("Enter a price: "))
if is_price_valid(input_price):
    print("The price is valid.")
else:
    print("The price is invalid.")