# Chapter 3 - Part 2: Accessing Elements in a List
# ------------------------------------------------
# This file mirrors the section from Chapter 3 that teaches:
# - Accessing list elements by index
# - Using methods on list elements
# - Understanding zero-based indexing
# - Using negative indexing

# Create the list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print("Full list:")
print(bicycles)
print()

# 1) Access elements by positive index
print("Accessing elements by index:")
print("bicycles[0]:", bicycles[0])   # First item
print("bicycles[1]:", bicycles[1])   # Second item
print("bicycles[2]:", bicycles[2])   # Third item
print("bicycles[3]:", bicycles[3])   # Fourth item
print()

# 2) Apply string method to an element
print("Using string methods:")
print(bicycles[0].title())  # Capitalizes 'trek'
print()

# 3) Negative indexing
print("Negative indexing:")
print("bicycles[-1]:", bicycles[-1])  # Last item
print("bicycles[-2]:", bicycles[-2])  # Second-to-last item
print()

# 4) Reminder about zero-based indexing
print("Reminder: Indexes start at 0, not 1.")
