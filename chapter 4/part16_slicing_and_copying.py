# part16_slicing_and_copying.py
# Python Crash Course – Chapter 4, Pages 61–63
# Topics:
#   - Basic slices: start:stop (stop exclusive)
#   - Omitting start or stop
#   - Negative-index slices (last N items)
#   - Step / third value in slice
#   - Looping through a slice
#   - Copying lists: aliasing vs slice copy

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("\n=== Page 61: Basic Slicing ===")

# First three players (indices 0,1,2)
print("First three players:", players[0:3])

# From index 1 up to (not including) 4 → indices 1,2,3
print("Slice 1:4:", players[1:4])

# From start to index 4 (exclusive)
print("Start to 4:", players[:4])

# From index 2 to the end
print("From index 2 to end:", players[2:])


print("\n=== Page 62: Negative Index & Step Slices ===")

# Last three players regardless of list size
print("Last three players:", players[-3:])

# Every second element using step
print("Every second player (step=2):", players[::2])

# Start at index 1 and step by 2
print("From index 1 stepping by 2:", players[1::2])

print("\nLooping through a slice (first three):")
for player in players[:3]:
    print("-", player.title())


print("\n=== Page 63: Copying Lists (aliasing vs slice copy) ===")

print("\nIncorrect (aliasing - no copy):")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods_alias = my_foods          # ⚠️ alias, same object
my_foods.append('cannoli')
friend_foods_alias.append('ice cream') # modifies the same list
print("my_foods:           ", my_foods)
print("friend_foods_alias: ", friend_foods_alias)
print("Note: Both changed because they reference the same list (alias).")

print("\nCorrect (slice copy - new list):")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]             # ✅ real (shallow) copy
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my_foods (independent):     ", my_foods)
print("friend_foods (independent): ", friend_foods)
print("Different lists now; changes are independent.")

print("\nLoop over each list:")
print("My favorite foods:")
for food in my_foods:
    print(" •", food.title())

print("\nMy friend's favorite foods:")
for food in friend_foods:
    print(" •", food.title())

