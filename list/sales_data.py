sales_data = [
    [110, 520, 340, 800], # Product A daily sales
    [250, 660, 420, 720], # Product B daily sales
    [730, 800, 910, 500], # Product C daily sales
    [110, 340, 800, 900], # Product E daily sales
]

daily_encome = (sum(day) for day in sales_data)
"""
daily_encome = (sum(day) for day in sales_data)
This creates a generator expression that sums each inner list (day) one by one.
next(daily_encome) moves the generator forward and gives the next product's total.
Example:
For Product A → sum([110, 520, 340, 800]) = 1770
For Product B → sum([250, 660, 420, 720]) = 2050
...and so on.
"""
print(f"A Product Encome : ${next(daily_encome)}")
print(f"B Product Encome : ${next(daily_encome)}")
print(f"C Product Encome : ${next(daily_encome)}")
print(f"E Product Encome : ${next(daily_encome)}")

Total_Encome = list(map(sum, sales_data))
print(f"Total Encome: {Total_Encome}")
"""
Total_Encome = list(map(sum, sales_data))
map(sum, sales_data) applies the sum() function to each list inside sales_data.
Then list() converts it into [1770, 2050, 2940, 2150].
So Total_Encome gives the same result as the generator — but all at once, not lazily.
"""
# {sale for product in sales_data for sale in product}
unique_sales = []
for product in sales_data:
    for sale in product:
        unique_sales.append(sale)
print("unique sale value:", sorted(unique_sales, reverse = True))
"""
the key point:
**`.add()` only works with a `set`**, not with a `list`.
Let’s see why:
---
### `.add()` belongs to `set`, not `list`
| Data Type | Method for adding item |
| --------- | ---------------------- |
| **list**  | `.append()`            |
| **set**   | `.add()`               |
So if you write this:
```python
all_sales = []
all_sales.add(520)   #❌Error
```
You’ll get:
```
AttributeError: 'list' object has no attribute 'add'
```
--
###✅If you *must* use `.add()`, it means you’re using a `set`:
```python
all_sales = set()
for product in sales_data:
    for sale in product:
        all_sales.add(sale)  # works fine
print(all_sales)
explain of it :
A set only stores unique values (no duplicates).
We go through every product (each inner list),
then every sale (number in that list),
and add it to the set.
After this loop, unique_sales will contain all distinct sale numbers.
```
But remember: a **set removes duplicates** automatically.
---
###✅If you want duplicates to stay:
You must use `.append()` instead:
```python
all_sales = []
for product in sales_data:
    for sale in product:
        all_sales.append(sale)  # keeps duplicates
print(all_sales)
```
---
So to summarize clearly:
> 🔹 Use `.append()` → keeps duplicates (list)
> 🔹 Use `.add()` → removes duplicates (set)
---
Would you like me to show a version that **uses `.add()` (set)** and another that **uses `.append()` (list)** side-by-side so you can see the difference in output?
"""

daily_increases = [day2 - day1 for day1, day2 in zip(sales_data[0][:-1], sales_data[0][1:])]
print(daily_increases)
# sales_data[0][:-1] → all numbers except the last one
# sales_data[0][1:]  → all numbers except the first one
# zip(...) pairs them together → [(110, 520), (520, 340), (340, 800)]
# day2 - day1 → finds the difference between each day
# result → list of daily increases or decreases

# Loop over each product
for i, product in enumerate(sales_data, start=1):
    daily_increases = [day2 - day1 for day1, day2 in zip(product[:-1], product[1:])]
    print(f"Product {i} daily increases: {daily_increases}")
# Explanation:
# for i, product in enumerate(sales_data, start=1)
# → Loops through each product’s list and gives it a number (i) starting from 1.
# product[:-1] → all but the last day’s sales.
# product[1:] → all but the first day’s sales.
# zip(...) pairs them:
# e.g. [110, 520, 340] and [520, 340, 800] → [(110, 520), (520, 340), (340, 800)]
# day2 - day1 → gives increase or decrease for each day.
