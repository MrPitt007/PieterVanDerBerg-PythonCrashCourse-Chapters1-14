# Chapter 4 – Part 14: Simple Statistics + List Comprehensions
# ------------------------------------------------------------
# Matches Page 59 of Chapter 4:
# - Using value**2 directly in append()
# - Simple statistics: min, max, sum
# - List comprehensions for generating lists in one line

print("\n--- More Concise Squares List ---\n")

# Building the squares list in one concise line inside the loop
squares = []
for value in range(1, 11):
    squares.append(value**2)  # append value squared directly

print("Squares (concise loop version):")
print(squares)


print("\n--- Simple Statistics with a List of Numbers ---\n")

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("Digits list:", digits)
print("Minimum value:", min(digits))
print("Maximum value:", max(digits))
print("Sum of digits:", sum(digits))


print("\n--- List Comprehensions ---\n")

# Build the same squares list using a list comprehension
squares_comp = [value**2 for value in range(1, 11)]

print("Squares (list comprehension version):")
print(squares_comp)
