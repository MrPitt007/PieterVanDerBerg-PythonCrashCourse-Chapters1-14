# part7_slicing2.py
# Python Crash Course – Chapter 4
# Pages 61–62: Working with list slices
# Topics:
#   - Basic slices: start:stop (stop is exclusive)
#   - Omitting start or stop
#   - Negative-index slices (e.g., last N items)
#   - Third value (step)
#   - Looping through a slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("\n--- Page 61: Basic Slicing ---")

# First three players (indices 0,1,2)
print("First three players:", players[0:3])

# From index 1 up to (but not including) 4 → indices 1,2,3
print("Slice 1:4:", players[1:4])

# From start to index 4 (exclusive)
print("Start to 4:", players[:4])

# From index 2 to the end
print("From index 2 to end:", players[2:])

print("\n--- Page 62: Negative-Index and Step Slices ---")

# Last three players regardless of list size
print("Last three players:", players[-3:])

# Third value is step. ::2 means take every second element
print("Every second player (step=2):", players[::2])

# Start at index 1 and step by 2
print("From index 1 stepping by 2:", players[1::2])

print("\n--- Page 62: Looping Through a Slice ---")
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\n--- End of part7_slicing2.py ---")
