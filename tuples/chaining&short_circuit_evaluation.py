x = -5
y = 10
z = 12
result00 = x < y and y <= z # True because both conditions are true
print(result00)

result01 = 10 < (100 * 100) <= 10000  # True because 10 < 10000 and 10000 <= 10000
print(result01)


a = 1
b = 2
c = 3
e = 4
f = 5
g = 6
result03 = b + c <= e or f + g >= e == f == 5 # False or(True and False) --> False
print(result03)

# This is called short-circuit evaluation:
result04 = b + c * f >= e and (f + g) * c # True and 33 → 33 Because and returns the second value when the first is True.
print(result04)
result05 = (f + g) * c or b + c * f <= e 
print(result05)
"""result05 = 33 or False
⚠️ IMPORTANT Python rule:
or returns the first truthy value.
Not True/False — the actual value.
33 is truthy
So Python stops and returns 33
➡️ The right side (False) is completely ignored.
✔ Final result:
ini
Copy code
result05 = 33"""

print()