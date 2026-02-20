"""
Chapter 8 – Page 132 Summary
Topic: Positional Arguments & Multiple Function Calls
Python Crash Course – Notes and Examples
"""


 POSITONAL ARGUMENTS – how Python assigns arguments


def describe_pet(animal_type, pet_name):
    """Display information about a pet using positional arguments."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

 Example call from the book:
describe_pet('hamster', 'harry')


 MULTIPLE FUNCTION CALLS – calling with different data


Same function reused with new arguments
describe_pet('dog', 'willie')



PAGE 132 SUMMARY


1. Positional arguments are assigned based on their order in the function call.
   Example:
       describe_pet('hamster', 'harry')
   'hamster' → animal_type
   'harry'   → pet_name

2. The order matters. If you swap the arguments, the meaning changes.

3. You can call the same function as many times as needed with different values.

4. Functions become powerful when reused with different data, producing
   predictable and reusable results.

This page explains how argument order works and demonstrates making multiple
function calls using different sets of arguments.
"""

print(summary)
