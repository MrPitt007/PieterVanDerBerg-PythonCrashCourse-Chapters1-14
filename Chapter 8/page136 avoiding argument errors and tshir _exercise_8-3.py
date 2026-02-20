
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


def make_shirt(size, message):
    """
    Print a sentence summarizing the size of the shirt
    and the message printed on it.
    """
    print(f"\nMaking a {size} shirt with the message: '{message}'.")

Exercise demonstration: Positional arguments:
make_shirt('large', 'Python is awesome!')

 Keyword arguments:
make_shirt(size='medium', message='Code more, stress less!')



PAGE 136 SUMMARY

1) Unmatched arguments cause errors:
     - Too few arguments → missing required parameters.
     - Too many arguments → extra values provided.
   Python's traceback helps identify exactly what is wrong.

2) Naming variables and parameters clearly reduces confusion
   and makes errors easier to diagnose.

3) Exercise 8-3 reinforces:
     - Writing a simple function
     - Using both positional and keyword arguments
     - Printing formatted output
"""
print(summary)
