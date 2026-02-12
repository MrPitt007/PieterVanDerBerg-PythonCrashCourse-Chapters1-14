# Chapter 4 – Part 13: Making Lists With range() + Squares Example
# ----------------------------------------------------------------
# Matches Page 58 of Chapter 4:
# - Converting range() to a list
# - Using a step argument in range()
# - Building lists with loops (squares example)

print("\n--- Using range() to Make a List of Numbers ---\n")

numbers = list(range(1, 6))
print("List produced by list(range(1, 6)):")
print(numbers)   # [1, 2, 3, 4, 5]


print("\n--- Using range() With a Step Value ---\n")

even_numbers = list(range(2, 11, 2))
print("Even numbers from 2 to 10 using range(2, 11, 2):")
print(even_numbers)   # [2, 4, 6, 8, 10]


print("\n--- Creating a List of Squares (Loop + Append) ---\n")

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print("Squares of numbers 1 through 10:")
print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
