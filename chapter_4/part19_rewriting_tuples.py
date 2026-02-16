# part19_rewriting_tuples.py
# Python Crash Course – Chapter 4, Page 67
# Topic: "Writing Over a Tuple" (reassigning the variable to a NEW tuple)

# Define initial tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# Reassign variable to a NEW tuple (this is allowed)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

print("\nNote:")
print("You cannot modify a tuple item in place (e.g., dimensions[0] = 250 is invalid).")
print("But you CAN rebind the name 'dimensions' to a completely new tuple.")
