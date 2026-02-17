"""
Chapter 5 — Page 74: Inequality (!=) and Numerical Comparisons
Run:
  python page74_inequality_and_numerical_comparisons.py
"""
print("=== Checking for Inequality (!=) ===")
requested_topping='mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
print()

print("=== Numerical Comparisons (==) ===")
age=18
print("age == 18 =>", age==18)
print()

print("=== Numerical Inequality (!=) ===")
answer=17
if answer!=42:
    print("That is not the correct answer. Please try again!")
