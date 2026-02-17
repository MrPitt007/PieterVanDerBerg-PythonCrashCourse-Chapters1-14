
"""
Chapter 5 — Page 73: Equality tests & case-insensitive comparisons

Run:
    python page73_case_tests.py
"""

# 1) Equality tests
print("=== Equality tests (==) ===")
car = 'audi'
print("car == 'bmw' =>", car == 'bmw')  # False
print("car == 'audi' =>", car == 'audi')  # True
print()

# 2) Case sensitivity
print("=== Case-sensitive comparisons ===")
car = 'Audi'
print("'Audi' == 'audi' =>", car == 'audi')  # False
print()

# 3) Case-insensitive comparison using .lower()
print("=== Case-insensitive using .lower() ===")
print("car.lower() == 'audi' =>", car.lower() == 'audi')  # True
print("car remains =>", car)  # Demonstrate original value unchanged
print()

# 4) Practical example: case-insensitive username check
print("=== Practical: username check (ignore case) ===")
stored_username = 'pieter'
user_inputs = ['Pieter', 'PIETER', 'pieTer', 'pieter', 'pieteR!']
for u in user_inputs:
    match = (u.lower() == stored_username.lower())
    print(f"input={u!r:10} -> match={match}")
print("Note: 'pieteR!' fails because punctuation differs, not just case.")
