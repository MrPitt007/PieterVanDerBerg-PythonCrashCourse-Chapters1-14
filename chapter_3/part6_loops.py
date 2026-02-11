# Chapter 3 - Part 6: Looping, Ranges, and List Comprehensions
# ------------------------------------------------------------
# Matches Chapter 3 sections on:
# - Looping through lists
# - Doing more inside a loop
# - Using range()
# - Making numerical lists
# - Basic statistics (min, max, sum)
# - List comprehensions

# 1) Looping through a list
magicians = ['alice', 'david', 'carolina']
print("Looping through the magicians list:")
for magician in magicians:
    print(magician)
print()

# 2) Doing more inside a loop
print("Doing more inside a loop:")
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you everyone, that was a great magic show!")
print()

# 3) Using range() to generate numbers
print("Using range(1, 6):")
for value in range(1, 6):
    print(value)
print()

# 4) Creating a list of numbers with list()
numbers = list(range(1, 11))
print("List of numbers from 1 to 10:")
print(numbers)
print()

# 5) Even numbers using step in range()
even_numbers = list(range(2, 11, 2))
print("Even numbers from 2 to 10:")
print(even_numbers)
print()

# 6) Make a list of squares using a loop
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print("Squares from 1 to 10 (loop method):")
print(squares)
print()

# 7) Simple statistics on a list
digits = list(range(1, 11))
print("Simple statistics (1–10):")
print("min:", min(digits))
print("max:", max(digits))
print("sum:", sum(digits))
print()

# 8) List comprehension (quick method for building lists)
squares_comp = [value ** 2 for value in range(1, 11)]
print("Squares from 1 to 10 (list comprehension):")
print(squares_comp)
print()
