tuple_0 = ("apple", 1, 2, 63.7, 44, False, "cat")
print(tuple_0)
print(f"units: {len(tuple_0)}")

tuple_1 = tuple(f for f in tuple_0 if f!= 2)
print(tuple_1)
