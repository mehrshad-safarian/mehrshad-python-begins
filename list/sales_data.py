sales_data = [
    [110, 520, 340, 800], # Product A daily sales
    [250, 660, 420, 720], # Product B daily sales
    [730, 800, 910, 500], # Product C daily sales
    [110, 340, 800, 900], # Product E daily sales
]

daily_encome = (sum(day) for day in sales_data)
print(f"A Product Encome : ${next(daily_encome)}")
print(f"B Product Encome : ${next(daily_encome)}")
print(f"C Product Encome : ${next(daily_encome)}")
print(f"E Product Encome : ${next(daily_encome)}")

Total_Encome = list(map(sum, sales_data))
print(f"Total Encome: {Total_Encome}")
# {sale for product in sales_data for sale in product}
unique_sales = []
for product in sales_data:
    for sale in product:
        unique_sales.append(sale)

print("unique sale value:", sorted(unique_sales, reverse = True))


"""
the key point:
👉 **`.add()` only works with a `set`**, not with a `list`.
Let’s see why:
---
### 🧩 `.add()` belongs to `set`, not `list`
| Data Type | Method for adding item |
| --------- | ---------------------- |
| **list**  | `.append()`            |
| **set**   | `.add()`               |
So if you write this:
```python
all_sales = []
all_sales.add(520)   # ❌ Error
```
You’ll get:
```
AttributeError: 'list' object has no attribute 'add'
```
--
### ✅ If you *must* use `.add()`, it means you’re using a `set`:
```python
all_sales = set()
for product in sales_data:
    for sale in product:
        all_sales.add(sale)  # works fine
print(all_sales)
```
But remember: a **set removes duplicates** automatically.
---
### ✅ If you want duplicates to stay:
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