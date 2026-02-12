# Chapter 4 – Part 11: Making Numerical Lists
# -------------------------------------------
# This begins the next section on Page 56:
# - Why numerical lists are useful
# - Using range() to generate numbers

print("Making numerical lists:\n")

# Basic use of range()
print("Numbers from 1 to 5:")
for value in range(1, 6):
    print(value)

print("\nList of numbers using list(range()):")
numbers = list(range(1, 11))
print(numbers)
