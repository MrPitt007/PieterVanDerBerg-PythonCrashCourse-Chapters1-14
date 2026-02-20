
def get_formatted_name_full(first_name, middle_name, last_name):
    """Return a full name including first, middle, and last."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

Example call (middle name required here)
musician = get_formatted_name_full('john', 'lee', 'hooker')
print(musician)



def get_formatted_name(first_name, last_name, middle_name=''):
    """
    Return a neatly formatted full name.
    Middle name is optional; if not provided, it is ignored.
    """
    if middle_name:  # middle name exists
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

 Example without middle name:
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

 Example with middle name:
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)



PAGE 138 SUMMARY

1) Functions can accept optional arguments by assigning default values.

2) A default value of '' (empty string) allows you to detect
   whether a middle name was provided and handle both cases.

3) Without a default, all parameters become required and the call must match
   the number of parameters in the function definition.

4) Optional arguments make functions more flexible and easier to reuse.
"""
print(summary)
