# Chapter 3 – Exercises
# ---------------------
# This file contains ALL the Chapter 3 exercises from Python Crash Course.
# Each exercise is clearly labeled and separated.

#   3-1. Names
names = ['adam', 'sarah', 'john', 'emily']
print("3-1. Names:")
for name in names:
    print(name.title())
print()

#   3-2. Greetings
print("3-2. Greetings:")
for name in names:
    print(f"Hello {name.title()}, I hope you're having a good day!")
print()

#   3-3. Your Own List
print("3-3. Your Own List:")
vehicles = ['motorbike', 'car', 'bicycle']
for v in vehicles:
    print(f"I would like to own a {v}.")
print()

#   3-4. Guest List
print("3-4. Guest List:")
guests = ['albert einstein', 'nelson mandela', 'marie curie']
for guest in guests:
    print(f"Dear {guest.title()}, please join me for dinner.")
print()

#   3-5. Changing Guest List
print("3-5. Changing Guest List:")
print(f"Unfortunately, {guests[1].title()} can't make it.")
guests[1] = 'elon musk'
for guest in guests:
    print(f"Dear {guest.title()}, please join me for dinner.")
print()

#   3-6. More Guests
print("3-6. More Guests:")
print("Good news! We found a bigger dinner table.")
guests.insert(0, 'leonardo da vinci')
guests.insert(2, 'ada lovelace')
guests.append('nikola tesla')

for guest in guests:
    print(f"Dear {guest.title()}, you are invited to dinner!")
print()

#   3-7. Shrinking Guest List
print("3-7. Shrinking Guest List:")
print("Sorry, the new table won’t arrive in time. Only two guests can come.")

while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry {removed.title()}, there's no space left.")

for guest in guests:
    print(f"{guest.title()}, you are still invited.")

del guests[0]
del guests[0]
print("Final guest list:", guests)
print()

#   3-8. Seeing the World
print("3-8. Seeing the World:")
locations = ['japan', 'new zealand', 'iceland', 'greece', 'canada']
print("Original list:", locations)
print("Sorted:", sorted(locations))
print("Original still unchanged:", locations)
locations.reverse()
print("Reversed:", locations)
locations.reverse()
print("Back to original:", locations)
locations.sort()
print("Alphabetical:", locations)
locations.sort(reverse=True)
print("Reverse alphabetical:", locations)
print()

#   3-9. Dinner Guests
print("3-9. Dinner Guests:")
friends = ['anna', 'mark', 'selena']
print("Number of guests invited:", len(friends))
print()

#   3-10. Every Function
print("3-10. Every Function:")
fruits = ['apple', 'banana', 'orange']
print("Original:", fruits)

fruits.append('kiwi')
print("After append:", fruits)

fruits.insert(1, 'grape')
print("After insert:", fruits)

del fruits[0]
print("After del:", fruits)

popped = fruits.pop()
print("Popped item:", popped)
print("After pop:", fruits)

fruits.remove('banana')
print("After remove 'banana':", fruits)

print("Sorted:", sorted(fruits))
fruits.sort()
print("Sort():", fruits)

fruits.sort(reverse=True)
print("Sort reverse:", fruits)

fruits.reverse()
print("Reverse():", fruits)

print("Length:", len(fruits))
print()

#   3-11. Intentional Error
print("3-11. Intentional Error:")
numbers = [1, 2, 3]
print("Numbers:", numbers)
# Index error on purpose:
# print(numbers[3])  # Uncomment to see the error
print("Attempting to access numbers[3] would cause an IndexError.")
