

def make_sandwich(*items):
    """
    Summarize a sandwich order by listing all requested items.
    Accepts an arbitrary number of toppings/fillings.
    """
    print("\nMaking a sandwich with the following items:")
    if not items:
        print("- (no items specified)")
        return
    for item in items:
        print(f"- {item}")

Example calls (use different numbers of arguments)
make_sandwich('turkey')
make_sandwich('ham', 'cheddar', 'mustard')
make_sandwich('falafel', 'hummus', 'lettuce', 'tomato', 'cucumber')


def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.

    Required:
        first (str) : first name
        last  (str) : last name
    Arbitrary keyword args (**user_info) capture other key=value fields.
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
  
 Create your own profile; add a few key/value pairs that describe you.
my_profile = build_profile(
    'pieter', 'van der berg',
    location='övertorneå',
    role='applikationsutvecklare',
    favorite_lang='python'
)
print("\n8-13 — My profile dictionary:")
print(my_profile)



def make_car(manufacturer, model, **options):
    """
    Store information about a car in a dictionary.
    Required:
        manufacturer (str)
        model (str)
    Arbitrary options (**options) may include color, tow_package, etc.
    """
    car_dict = {
        'manufacturer': manufacturer,
        'model': model,
    }
    car_dict.update(options)
    return car_dict
  
Example call shown in the book's prompt:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print("\n8-14 — Car dictionary:")
print(car)

Additional examples
print(make_car('tesla', 'model 3', color='white', autopilot=True))
print(make_car('volvo', 'xc40', color='black', ev=True, year=2024))



