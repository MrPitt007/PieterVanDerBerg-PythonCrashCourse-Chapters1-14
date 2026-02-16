# part16_slicing_and_copying.py
# Python Crash Course – Chapter 4, Page 63
# Topic: Copying a list using a slice ([:]) vs aliasing (same reference)

# --- Code that mirrors the book (foods.py on page 63) ---

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # slice copy -> creates a new list

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Prove they are separate lists by appending different items
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nAfter appending different items:")
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# --- Optional: show the common mistake (aliasing) and why it's different ---
print("\n--- Optional demonstration: aliasing (no copy) ---")
my_foods_alias = ['pizza', 'falafel', 'carrot cake']
friend_foods_alias = my_foods_alias   # ❌ aliasing: both names point to the same list

my_foods_alias.append('cannoli')
friend_foods_alias.append('ice cream')  # modifies the same list object

print("my_foods_alias:", my_foods_alias)
print("friend_foods_alias:", friend_foods_alias)
print("Note: Both changed together because they reference the same list (alias).")

# Optional: show that the copied lists are different objects
print("\n--- Object identity check ---")
print("id(my_foods):        ", id(my_foods))
print("id(friend_foods):    ", id(friend_foods))
print("Are the copied lists the same object?", my_foods is friend_foods)
