"""
Chapter 5 — Page 83: Continuing Multiple Condition Testing
Run:
  python page83_testing_multiple_conditions_continued.py
"""

print("=== Testing multiple conditions (continued) ===")
requested_toppings = ['mushrooms', 'extra cheese']

# Same logic as book: independent conditions
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("Finished making your pizza!")
