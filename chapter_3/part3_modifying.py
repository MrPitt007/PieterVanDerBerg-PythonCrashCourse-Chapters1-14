
# Chapter 3 - Part 3: Modifying, Adding, and Removing Elements
# ------------------------------------------------------------
# Mirrors the book's flow:
# - Change list items by index
# - Add items with append() and insert()
# - Remove items with del, pop(), and remove()
# - Use popped values in messages
# - Note: remove() deletes only the first occurrence

# Start with a simple list
motorcycles = ['honda', 'yamaha', 'suzuki']
print("Original list:", motorcycles)

# 1) Modify an element (replace by index)
motorcycles[0] = 'ducati'
print("After modifying index 0:", motorcycles)

# 2) Add elements
# 2a) Append adds to the end
motorcycles.append('harley-davidson')
print("After append:", motorcycles)

