

def get_formatted_name(first_name, last_name, middle_name=''):
    """
    Return a neatly formatted full name.
    Middle name optional:
        - If provided → included
        - If empty ('') → ignored
    """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()

Examples from the book:
print(get_formatted_name('jimi', 'hendrix'))
print(get_formatted_name('john', 'hooker', 'lee'))



def build_person(first_name, last_name):
    """
    Return a dictionary representing a person.
    Keys:
        'first' : first_name
        'last'  : last_name
    """
    person = {'first': first_name, 'last': last_name}
    return person

Example:
musician = build_person('jimi', 'hendrix')
print(musician)



PAGE 139 SUMMARY

1) When using an optional argument (e.g., middle_name=''):
     - Python checks whether the argument is truthy.
     - If provided → included in the return value.
     - If not → ignored cleanly.

2) Optional arguments allow functions to support multiple use cases
   without requiring callers to provide unnecessary information.

3) A function can return ANY value, including dictionaries.
     build_person() returns a dictionary containing structured data.
     This makes returned information flexible and easy to extend later.

4) Returning dictionaries is useful for storing or passing around
   multiple related pieces of data from one function call.
"""
print(summary)
