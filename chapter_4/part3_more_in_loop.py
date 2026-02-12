# Chapter 4 – Part 3: Doing More Inside a Loop
# --------------------------------------------
# This follows the next section in Chapter 4:
# - Performing multiple actions inside the loop
# - Adding more print statements
# - Using f-strings with list elements

magicians = ['alice', 'david', 'carolina']

print("Doing more inside a loop:\n")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you everyone, that was a great magic show!")
