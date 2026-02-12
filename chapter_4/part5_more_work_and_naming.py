# Chapter 4 – Part 5: Loop Variable Naming + Doing More Work in a Loop
# --------------------------------------------------------------------
# This matches Page 51 of Chapter 4, including:
# - Choosing meaningful loop variable names
# - Doing more work inside a loop
# - Printing personalized messages using list items

# 1) Naming your loop variable meaningfully
print("Examples of good loop variable naming:\n")

cats = ['tiger', 'smokey', 'mittens']
dogs = ['rex', 'buddy', 'sparky']
items = ['apple', 'banana', 'orange']

for cat in cats:
    print(f"Cat: {cat}")

print()

for dog in dogs:
    print(f"Dog: {dog}")

print()

for item in items:
    print(f"Item: {item}")

print("\n---\n")


# 2) Doing more work within a loop (personalized messages)
magicians = ['alice', 'david', 'carolina']

print("Personalized messages for magicians:\n")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
