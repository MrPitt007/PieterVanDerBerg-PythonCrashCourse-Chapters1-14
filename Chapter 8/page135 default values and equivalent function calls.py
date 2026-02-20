
def describe_pet(pet_name, animal_type='dog'):
    """
    Display information about a pet.
    - pet_name: required
    - animal_type: optional, defaults to 'dog' if not provided
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('willie')


describe_pet(pet_name='harry', animal_type='hamster')



 EQUIVALENT FUNCTION CALLS (POSITIONAL vs KEYWORD)

 With the definition above (pet_name required, animal_type default='dog'),
 these calls all work and demonstrate style options:

 A dog named Willie (default animal_type)
describe_pet('willie')                  # positional for pet_name
describe_pet(pet_name='willie')         # keyword for pet_name
 A hamster named Harry (override default)
describe_pet('harry', 'hamster')                         # positional for both
describe_pet('harry', animal_type='hamster')             # mixed: pet_name positional, animal_type keyword
describe_pet(pet_name='harry', animal_type='hamster')    # both keywords
describe_pet(animal_type='hamster', pet_name='harry')    # keywords in swapped order (still valid)



summary = """
PAGE 135 SUMMARY

1) Default values let a function supply a fallback when an argument is omitted.
   - In 'describe_pet(pet_name, animal_type=\"dog\")', calling describe_pet('willie')
     prints information for a dog because animal_type defaults to 'dog'.

2) Parameters with defaults must be listed AFTER parameters without defaults,
   so Python can interpret positional arguments correctly.

3) Equivalent calls:
   - You can mix positional and keyword arguments, or use all keywords,
     and produce the same output. Choose the style that is clearest.

4) Keyword arguments allow any order; positional arguments depend on order.
"""
print(summary)
