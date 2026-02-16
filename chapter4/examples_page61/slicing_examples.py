# slicing_examples.py — examples from Python Crash Course, Chapter 4 (page 61)

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# 0:3 -> elements 0,1,2
print(players[0:3])  # ['charles', 'martina', 'michael']

# 1:4 -> elements 1,2,3
print(players[1:4])  # ['martina', 'michael', 'florence']

# :4 -> start at 0, stop before 4
print(players[:4])   # ['charles', 'martina', 'michael', 'florence']

# 2: -> start at 2, go to end
print(players[2:])   # ['michael', 'florence', 'eli']
``
