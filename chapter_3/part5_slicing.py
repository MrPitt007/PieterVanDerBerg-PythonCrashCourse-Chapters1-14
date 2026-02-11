
# Chapter 3 - Part 5: Slicing Lists
# ---------------------------------
# Mirrors Chapter 3 section on:
# - Basic slicing: list[start:end]
# - Omitting start or end
# - Slicing the end of a list
# - Looping through a slice
# - Copying lists using slices

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Original list of players:")
print(players)
print()

# 1) Basic slicing
print("Slicing players[0:3] (indexes 0, 1, 2):")
print(players[0:3])
print()

# 2) Middle slicing
print("Slicing players[1:4] (indexes 1, 2, 3):")
print(players[1:4])
print()

# 3) Omitting the start gives players[:4]
print("Slicing players[:4] (start → index 3):")
print(players[:4])
print()

# 4) Omitting the end gives players[2:]
print("Slicing players[2:] (from index 2 → end):")
print(players[2:])
print()

# 5) Last 3 items using negative indexes
print("Last three players players[-3:]:")
print(players[-3:])
print()


# 6) Looping through a slice
print("Loop through the first three players:")
for player in players[:3]:
    print(player.title())
print()

# 7) Copying a list using slices
print("Copying lists using slices:")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # Proper way to copy the list

print("My favorite foods:", my_foods)
print("My friend's favorite foods:", friend_foods)

# Demonstrate that they are independent lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nAfter adding different foods:")
print("My favorite foods:", my_foods)
print("My friend's favorite foods:", friend_foods)
print()





