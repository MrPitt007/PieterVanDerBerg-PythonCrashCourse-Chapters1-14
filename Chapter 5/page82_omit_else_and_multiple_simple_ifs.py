"""
Chapter 5 — Page 81: Refactoring if-elif-else + Multiple elif Blocks
Run:
  python page81_price_refactor_and_multiple_elif.py
"""

print("=== Refactored pricing using a single print() ===")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")
print()

print("=== Using multiple elif blocks (including seniors 65+) ===")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")
