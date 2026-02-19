# Chapter 3 - Part 1: Creating Lists & Accessing Elements
# -------------------------------------------------------
# This file mirrors the early pages of Chapter 3:
# - Creating a list
# - Printing the list
# - Accessing elements by index
# - Using string methods on list items
# - Reminder: indexes start at 0, not 1

# 1) Create a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# 2) Print the full list (shows Python's literal representation)
print("Full list:")
print(bicycles)  # -> ['trek', 'cannondale', 'redline', 'specialized']
print()  # blank line for readability

# 3) Accessing elements by index (zero-based)
print("Accessing elements by index:")
print("First item (index 0):", bicycles[0])        # -> trek
print("Second item (index 1):", bicycles[1])       # -> cannondale
print("Third item (index 2):", bicycles[2])        # -> redline
print("Fourth item (index 3):", bicycles[3])       # -> specialized
print()

# 4) Using string methods on a list element
print("String method on an element:")
print("Title-cased first item:", bicycles[0].title())  # -> Trek
print()

# 5) Negative indexing (from the end of the list)
print("Negative indexing:")
print("Last item (index -1):", bicycles[-1])       # -> specialized
print("Second to last (index -2):", bicycles[-2])  # -> redline
print()

# 6) Friendly reminder about indexes
print("Reminder: Index positions start at 0, not 1.")
