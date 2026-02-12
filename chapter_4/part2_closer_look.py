# Chapter 4 – Part 2: A Closer Look at Looping
# --------------------------------------------
# Matches the "A Closer Look at Looping" section on page 50.

magicians = ['alice', 'david', 'carolina']

print("A closer look at how Python processes a loop:\n")

for magician in magicians:
    print(f"Python assigned '{magician}' to the variable 'magician'.")

print("\nExplanation:")
print("- Python starts with 'alice' and prints it.")
print("- Then 'david'.")
print("- Then 'carolina'.")
print("This continues until all items have been processed.")
