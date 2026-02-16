# part16b_copying_vs_aliasing_demo.py
# Python Crash Course – Chapter 4, Page 64
# Focus: Showing why aliasing (no slice) does NOT create a separate list.

print("=== Correct approach: slice copy ([:]) ===")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # ✅ makes a NEW list

# Add different items to each list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)            # ['pizza', 'falafel', 'carrot cake', 'cannoli']
print("\nMy friend's favorite foods are:")
print(friend_foods)        # ['pizza', 'falafel', 'carrot cake', 'ice cream']

print("\n=== Incorrect approach: aliasing (no copy) ===")
my_foods = ['pizza', 'falafel', 'carrot cake']
# ❌ This doesn't work as a copy — it just creates another name for the same list
friend_foods = my_foods

# Append to each name (both refer to the same list object)
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)            # both items appear here

print("\nMy friend's favorite foods are:")
print(friend_foods)        # and here too, because it's the same object

# Optional: identity check to make it explicit
print("\n--- Identity check ---")
print("id(my_foods):     ", id(my_foods))
print("id(friend_foods): ", id(friend_foods))
print("Same object? ->", my_foods is friend_foods)
