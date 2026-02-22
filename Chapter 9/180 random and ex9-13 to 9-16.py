"""
Chapter 9 – Page 180
Topic: random module (randint, choice) + Exercises 9-13 to 9-16
Python Crash Course – Notes, Examples, and Solutions
"""


 RANDOM MODULE DEMOS: randint, choice

from random import randint, choice

 randint: random integer between (and including) the endpoints
print("randint(1, 6) example:", randint(1, 6))

# choice: pick a random element from a sequence
players = ["charles", "martina", "michael", "florence", "eli"]
first_up = choice(players)
print("choice(players) example:", first_up.title())



 9-13 — DICE
 Make a class Die; roll_die() prints random number between 1 and sides.
 Roll a 6-sided, 10-sided, and 20-sided die ten times each.


class Die:
    """Represent a die with a configurable number of sides."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Return a random roll between 1 and the number of sides."""
        return randint(1, self.sides)


print("\n--- 9-13 Dice ---")
for sides in (6, 10, 20):
    d = Die(sides)
    rolls = [d.roll_die() for _ in range(10)]
    print(f"{sides}-sided die rolls:", rolls)



 9-14 — LOTTERY
 Create a list/tuple with 10 numbers and 5 letters.
 Randomly select 4 items; if a ticket matches, print a winner message.

print("\n--- 9-14 Lottery ---")
pool = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        "A", "B", "C", "D", "E")

def draw_ticket(pool, draw_count=4):
    """Return a list of 'draw_count' unique choices from pool."""
    # To keep it simple and avoid repeats, copy the pool and pop
    local = list(pool)
    out = []
    for _ in range(draw_count):
        pick = choice(local)
        out.append(pick)
        local.remove(pick)
    return out

winning_ticket = draw_ticket(pool)
print("Winning ticket:", winning_ticket)

my_ticket = draw_ticket(pool)  # your random ticket
print("My ticket     :", my_ticket)
if my_ticket == winning_ticket:
    print("You won a prize!")
else:
    print("Not a winner this time.")


 9-15 — LOTTERY ANALYSIS
 Loop until a generated ticket matches the winning ticket.
Print how many attempts it took.

print("\n--- 9-15 Lottery Analysis ---")
# Keep the same winning ticket from above; generate new tickets until match.
attempts = 0
while True:
    attempts += 1
    trial = draw_ticket(pool)
    if trial == winning_ticket:
        break
print(f"It took {attempts} attempts to draw the winning ticket {winning_ticket}.")


 9-16 — PYTHON MODULE OF THE WEEK (PMOTW)
 A note to explore https://pymotw.com/ for standard-library deep dives.
 (No direct code required; we print a brief tip.)

pmotw_tip = """
9-16 — Python Module of the Week

Browse https://pymotw.com/ and skim a standard-library module that interests you.
For this page we used: 'random' with randint() and choice().
"""
