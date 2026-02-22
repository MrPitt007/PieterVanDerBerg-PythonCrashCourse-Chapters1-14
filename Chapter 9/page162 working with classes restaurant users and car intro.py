

 9-1 — RESTAURANT
 Create a class Restaurant with attributes restaurant_name and cuisine_type.
 Add methods: describe_restaurant() and open_restaurant().

class Restaurant:
    """Represent a restaurant with a name and cuisine type."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print two pieces of information about the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message stating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


 Demo for 9-1
print("\n--- 9-1: Restaurant ---")
my_place = Restaurant("Polar Bistro", "nordic")
print(my_place.restaurant_name)
print(my_place.cuisine_type)
my_place.describe_restaurant()
my_place.open_restaurant()



 9-2 — THREE RESTAURANTS
 Make three different instances and call describe_restaurant() for each.


print("\n--- 9-2: Three Restaurants ---")
r1 = Restaurant("Sushi Hub", "japanese")
r2 = Restaurant("La Trattoria", "italian")
r3 = Restaurant("Spice Route", "indian")

for r in (r1, r2, r3):
    r.describe_restaurant()



 Create a User class with first_name and last_name (and a few profile fields).
Add methods: describe_user() and greet_user().


class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, **profile):
        """
        Initialize names and arbitrary profile fields.
        Examples of profile fields: location, role, age, etc.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.profile = profile  # store other attributes in a dict

    def describe_user(self):
        """Print a summary of the user's information."""
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"\nUser: {full_name}")
        if not self.profile:
            print("No extra profile fields.")
        else:
            for key, value in self.profile.items():
                print(f"- {key}: {value}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()}! Welcome back.")

 Demo for 9-3
print("\n--- 9-3: Users ---")
user_1 = User("pieter", "van der berg", location="övertorneå", role="applikationsutvecklare")
user_2 = User("ada", "lovelace", occupation="mathematician")
user_3 = User("eric", "matthes")  # no extra fields

for u in (user_1, user_2, user_3):
    u.describe_user()
    u.greet_user()


class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

Demo of Car class intro
print("\n--- Car Class (intro) ---")
my_car = Car("subaru", "outback", 2015)
print(my_car.get_descriptive_name())


summary = """
PAGE 162 SUMMARY
-----------------
• Exercises:
  9-1 Restaurant — define a class with basic attributes and methods.
  9-2 Three Restaurants — instantiate the class multiple times and call methods.
  9-3 Users — store core name fields plus arbitrary profile data; add greet/describe.

• New section begins: Working with Classes and Instances.
  Introduced Car class:
    - Attributes: make, model, year
    - Method: get_descriptive_name()

• Takeaway: Once a class is defined, you can create as many independent
  instances as needed and call shared methods on each object.
"""
print(summary)
