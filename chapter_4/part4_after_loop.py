# Chapter 4 – Part 4: Doing Something After a Loop
# ------------------------------------------------
# This matches the section that explains that code not indented
# beneath the loop runs AFTER the loop is complete.

magicians = ['alice', 'david', 'carolina']

print("Messages during the loop:\n")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# This line is **not** indented, so it runs AFTER the loop ends.
print("Thank you everyone, that was a great magic show!")
