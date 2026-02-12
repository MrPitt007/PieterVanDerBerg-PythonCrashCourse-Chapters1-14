# Chapter 4 – Part 7: Avoiding Indentation Errors
# -----------------------------------------------
# Matches Page 53:
# - How Python uses indentation
# - Common indentation problems
# - Example: Forgetting to indent inside a loop

print("Avoiding Indentation Errors\n")

print("Python uses indentation to understand which lines belong together.")
print("For example, lines inside a for-loop MUST be indented.\n")

# Example list
magicians = ['alice', 'david', 'carolina']

print("Correct indentation (works):")
for magician in magicians:
    print(magician)   # <-- properly indented

print()

print("Incorrect indentation example (will cause an error):")
print("This code is NOT executed, it's only shown as text.")

incorrect_code = """
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)   # ❌ NOT indented -- this will fail
"""

print(incorrect_code)

print("If you run this incorrect version, Python will show an error like:\n")
print("IndentationError: expected an indented block after 'for' statement")
