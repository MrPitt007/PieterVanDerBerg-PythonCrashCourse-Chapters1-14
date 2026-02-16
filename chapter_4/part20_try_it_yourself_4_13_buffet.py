# part20_try_it_yourself_4_13_buffet.py
# Python Crash Course – Chapter 4, Page 67
# Exercise 4-13: Buffet

print("\n=== Buffet: initial menu (tuple) ===")
menu = ("pasta", "salad", "soup", "bread", "fish")

print("Restaurant offers:")
for item in menu:
    print(" •", item.title())

print("\n=== Attempt to modify an item (should FAIL if uncommented) ===")
# The next line would raise: TypeError: 'tuple' object does not support item assignment
# menu[0] = "ravioli"

print("Tuples are immutable; you can't change an element directly.")

print("\n=== Menu changes (reassign a NEW tuple) ===")
# Replace two items by reassigning the variable to a new tuple
menu = ("ravioli", "salad", "soup", "naan", "chicken")

print("Updated restaurant offers:")
for item in menu:
    print(" •", item.title())

print("\n--- End of part20_try_it_yourself_4_13_buffet.py ---")
