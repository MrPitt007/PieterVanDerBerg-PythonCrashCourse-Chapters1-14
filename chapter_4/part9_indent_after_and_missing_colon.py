# Chapter 4 – Part 9: Indenting After the Loop + Forgetting the Colon
# -------------------------------------------------------------------
# Matches Page 55 of Chapter 4:
# - Logical error: indentation accidentally placed under the loop
# - Syntax error: forgetting the colon after a for-loop header

magicians = ['alice', 'david', 'carolina']

print("\n--- Indenting Unnecessarily After the Loop (Logical Error) ---\n")

incorrect_example = """
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Thank you everyone, that was a great magic show!")   # ❌ Incorrectly indented
"""

print("Incorrect version:\n")
print(incorrect_example)

print("Explanation:")
print The 'thank you' line is incorrectly indented INSIDE the loop.")
print("- This causes it to print once per magician instead of once at the end.\n")

# Demonstrate the correct version
print("Correct version (thank you printed once):\n")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you everyone, that was a great magic show!")  # correctly placed


print("\n--- Forgetting the Colon (Syntax Error) ---\n")

incorrect_colon_example = """
magicians = ['alice', 'david', 'carolina']
for magician in magicians   # ❌ Missing colon
    print(magician)
"""

print("Incorrect version:\n")
print(incorrect_colon_example)

print("If you run this code, Python will show:")
print("SyntaxError: expected ':'")
