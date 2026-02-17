"""
Chapter 5 — Page 75: Mathematical Comparisons & Checking Multiple Conditions
Run:
  python page75_multiple_conditions.py
"""

print("=== Mathematical Comparisons (<, <=, >, >=) ===")
age = 19
print("age < 21 =>", age < 21)
age = 21
print("age < 21 =>", age < 21)
age = 22
print("age > 21 =>", age > 21)
print("age <= 21 =>", age <= 21)
print("age >= 21 =>", age >= 21)
print()

print("=== Checking Multiple Conditions with 'and' ===")
age_0 = 22
age_1 = 18
print("age_0 >= 21 and age_1 >= 21 =>", age_0 >= 21 and age_1 >= 21)

age_1 = 22
print("age_0 >= 21 and age_1 >= 21 =>", age_0 >= 21 and age_1 >= 21)
print()

print("=== Using Parentheses for Clarity ===")
print("(age_0 >= 21) and (age_1 >= 21) =>", (age_0 >= 21) and (age_1 >= 21))
