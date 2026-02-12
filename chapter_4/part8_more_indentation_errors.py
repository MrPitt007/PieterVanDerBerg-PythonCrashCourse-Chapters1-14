# Chapter 4 – Part 8: Forgetting Additional Indentation & Unnecessary Indentation
# ------------------------------------------------------------------------------
# Matches Page 54 of Chapter 4:
# - Forgetting to indent additional lines inside a loop
# - Indenting lines that should NOT be indented
# - Understanding logical errors vs syntax errors

print("\n--- Forgetting to Indent Additional Lines ---\n")

magicians = ['alice', 'david', 'carolina']

print("Incorrect indentation example (logical error):")

incorrect_example = """
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
"""

print(incorrect_example)

print("Explanation:")
print("- The FIRST print() is indented correctly, so it runs for each magician.")
print("- The SECOND print() is NOT indented, so it runs ONLY once — after the loop.")
print("- Because 'magician' ends on the last value ('carolina'),")
print("  the second message only prints for Carolina.\n")

# Demonstrate the correct version
print("Correct version (fully indented):\n")

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")


print("\n--- Indenting Unnecessarily ---\n")

print("Incorrect version (syntax error):")

incorrect_unnecessary_indent = """
message = "hello python world!"
    print(message)   # ❌ unexpected indent
"""

print(incorrect_unnecessary_indent)

print("If you run this, Python will report:")
print("IndentationError: unexpected indent")
print("\nExplanation:")
print("- The print() line is indented even though it is NOT inside a loop,")
print("- so Python throws a syntax error.")
