
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

# 2b) Insert adds at a specific position
motorcycles.insert(1, 'kawasaki')  # insert at index 1
print("After insert at index 1:", motorcycles)

# 3) Remove elements
# 3a) del removes by index (no return value)
del motorcycles[2]  # delete the item currently at index 2
print("After del index 2:", motorcycles)

# 3b) pop() removes by index and returns the value (default is last item)
popped_bike = motorcycles.pop()  # removes last element
print("Popped (last) item:", popped_bike)
print("After pop():", motorcycles)


# pop with an explicit index (e.g., remove the first item)
first_owned = motorcycles.pop(0)
print("Popped (index 0):", first_owned)
print("After pop(0):", motorcycles)


# 3c) remove() deletes by value (first matching occurrence)
motorcycles.extend(['honda', 'triumph', 'honda'])  # add duplicates to demonstrate
print("Before remove('honda'):", motorcycles)

motorcycles.remove('honda')  # removes the FIRST 'honda' it finds
print("After remove('honda'):", motorcycles)

# If you need to remove all occurrences of a value, loop until it's gone
value_to_remove = 'honda'
while value_to_remove in motorcycles:
    motorcycles.remove(value_to_remove)
print("After removing all 'honda':", motorcycles)

# 4) Using popped values in sentences (common in the examples)
cars = ['bmw', 'audi', 'toyota']
last_owned = cars.pop()
print(f"I recently sold my {last_owned.title()}.")
print("Cars list now:", cars)


