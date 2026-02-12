# Chapter 4 – Part 15: Try It Yourself (Exercises 4-3 through 4-9)
# ---------------------------------------------------------------

print("\n--- 4-3 Counting to Twenty ---")
for number in range(1, 21):
    print(number)


print("\n--- 4-4 One Million ---")
# WARNING: Printing 1,000,000 numbers is slow.
# Uncomment the loop below if you actually want to run it.
# for number in range(1, 1_000_001):
#     print(number)


print("\n--- 4-5 Summing a Million ---")
numbers = list(range(1, 1_000_001))
print("min:", min(numbers))
print("max:", max(numbers))
print("sum:", sum(numbers))


print("\n--- 4-6 Odd Numbers ---")
for number in range(1, 21, 2):
    print(number)


print("\n--- 4-7 Threes ---")
for number in range(3, 31, 3):
    print(number)


print("\n--- 4-8 Cubes ---")
for number in range(1, 11):
    print(number ** 3)


print("\n--- 4-9 Cube Comprehension ---")
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)
