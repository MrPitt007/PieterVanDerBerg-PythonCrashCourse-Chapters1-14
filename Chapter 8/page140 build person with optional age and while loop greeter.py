

def build_person(first_name, last_name, age=None):
    """
    Return a dictionary representing a person.
    If age is provided (not None), include it in the dictionary.
    """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

 Example with an optional age:
musician = build_person('jimi', 'hendrix', age=27)
print(musician)  # {'first': 'jimi', 'last': 'hendrix', 'age': 27}


def get_formatted_name(first_name, last_name):
    """Return a neatly formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

 print("\nThis is an infinite loop (no quit condition yet)!")
 while True:
     print("\nPlease tell me your name:")
     f_name = input("First name: ")
     l_name = input("Last name: ")

     formatted_name = get_formatted_name(f_name, l_name)
     print(f"\nHello, {formatted_name}!")

# Single-iteration demonstration (safe to run):
f_name = "ada"
l_name = "lovelace"
formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")

