
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

 Example from the book:
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def make_shirt(size='large', message='I love Python'):
    """
    Print a summary of the shirt that is going to be made.
    Default:
        size='large'
        message='I love Python'
    """
    print(f"\nMaking a {size} T-shirt with the message: '{message}'.")

# Exercise calls:
make_shirt()                            # large shirt, default message
make_shirt(size='medium')                # medium shirt, default message
make_shirt(size='small', message='Code is life!')



def describe_city(city, country='iceland'):
    """Print a simple sentence about a city and its country."""
    print(f"{city.title()} is in {country.title()}.")

# Exercise calls:
describe_city('reykjavik')               # uses default country
describe_city('akureyri')                # also default
describe_city('oslo', country='norway')  # overridden country

summary = """
PAGE 137 SUMMARY
-----------------
1) Functions can return values using the return keyword.
   This sends a value back to the line of code that called the function.

2) Returning a formatted value lets the caller store the result,
   reuse it, or print it later.

3) Exercises 8-4 and 8-5 introduce:
     - Using default values in function definitions.
     - Overriding defaults when needed.
     - Choosing clear, descriptive output.

4) Return values help you separate the work of computing information
   from the work of displaying it.
"""
print(summary)
