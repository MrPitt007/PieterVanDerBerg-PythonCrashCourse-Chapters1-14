# part18_tuples_basics.py
# Python Crash Course – Chapter 4, Page 66
# Topic: Introduction to tuples, immutability, and looping through tuples


print("\n=== Defining and Accessing a Tuple ===")

dimensions = (200, 50)
print("Dimensions tuple:", dimensions)
print("First element:", dimensions[0])
print("Second element:", dimensions[1])


print("\n=== Tuples Are Immutable (This Raises an Error) ===")

# This code is supposed to FAIL on purpose.
# Uncomment it to see the TypeError.

# dimensions[0] = 250  # ❌ TypeError: 'tuple' object does not support item assignment

print("Tuples cannot be modified. Attempting to change an item raises an error.")


print("\n=== Tuple with One Element Requires a Trailing Comma ===")

my_t = (3,)  # correct way to define a single-element tuple
not_a_tuple = (3)  # this is just an integer

print("Single‑element tuple:", my_t)
print("Type of (3,):", type(my_t))
print("Type of (3):", type(not_a_tuple))


print("\n=== Looping Through All Values in a Tuple ===")

dimensions = (200, 50)
print("Looping through dimensions:")
for dimension in dimensions:
    print(" •", dimension)


print("\n=== Summary ===")
print("Tuples look like lists, but they are immutable.")
print("They use parentheses instead of square brackets.")
print("To define a 1‑element tuple, include a trailing comma: (value,)")
print("You can loop through tuples just like lists.")


print("\n--- End of part18_tuples_basics.py ---")
