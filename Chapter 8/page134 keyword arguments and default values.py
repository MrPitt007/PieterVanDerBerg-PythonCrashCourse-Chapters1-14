
def describe_pet(animal_type, pet_name):
    Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

Thse two calls are equivalent when using keyword arguments:
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


 Display information about a pet.
    If animal_type is not provided, it defaults to 'dog'.
    """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
