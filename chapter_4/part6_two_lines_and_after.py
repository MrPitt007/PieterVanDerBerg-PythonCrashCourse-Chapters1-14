# Chapter 4 – Part 6: Multiple Lines in a Loop + Doing Something After the Loop
# -----------------------------------------------------------------------------
# This file matches Page 52:
# - Adding multiple statements inside a loop
# - Using \n for blank lines
# - Code that runs AFTER the loop (not indented)

magicians = ['alice', 'david', 'carolina']

print("Messages inside the loop:\n")

# Multiple lines inside the loop
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Code AFTER the loop (not indented)
print("Thank you, everyone. That was a great magic show!")
