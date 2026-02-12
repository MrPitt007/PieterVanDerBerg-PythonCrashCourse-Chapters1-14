# Chapter 4 – Part 12: Using the range() Function
# ------------------------------------------------
# Matches Page 57 of Chapter 4.
# Shows:
# - Basic usage of range()
# - Off-by-one behavior (end value not included)
# - Using different start/stop values

print("Using the range() function:\n")

print("Example 1: range(1, 5)")
for value in range(1, 5):
    print(value)

print("\nExplanation:")
print("- range(1, 5) starts at 1 and stops BEFORE 5, so it prints 1–4.\n")


print("Example 2: range(1, 6) → prints 1 through 5")
for value in range(1, 6):
    print(value)

print("\nExample 3: range(6) → starts at 0, prints 0 through 5")
for value in range(6):
    print(value)
