# Chapter 3 - Part 4: Sorting, Reversing, and Finding the Length of a List
# ------------------------------------------------------------------------
# Mirrors the Chapter 3 section that covers:
# - Permanent sorting with sort()
# - Reverse alphabetical sorting with sort(reverse=True)
# - Temporary sorting with sorted()
# - Reversing the list order with reverse()
# - Getting the length of a list using len()

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Original list:")
print(cars)
print()

# 1) Permanent alphabetical sort
cars_sorted_permanently = cars.copy()
cars_sorted_permanently.sort()
print("Permanently sorted list (sort()):")
print(cars_sorted_permanently)
print()

# 2) Permanent reverse alphabetical sort
cars_reverse_sorted = cars.copy()
cars_reverse_sorted.sort(reverse=True)
print("Permanently reverse-sorted list (sort(reverse=True)):")
print(cars_reverse_sorted)
print()

# 3) Temporary sorting
print("Temporarily sorted list (sorted()):")
print(sorted(cars))  # does NOT change the original list
print("Original list still unchanged:")
print(cars)
print()

# 4) Reverse the original list order
cars_reversed = cars.copy()
cars_reversed.reverse()
print("Reversed order (reverse()):")
print(cars_reversed)
print()

# 5) Length of the list
print("Length of the list (len()):")
print(len(cars))
print()
