
Parent class used for the inheritance example

class Car:
    """A simple attempt to model a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make} {self.model}".title()


 Inheritance — child class with its own __init__

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)   # call parent __init__
        # Child-specific attributes can be added here; a battery placeholder:
        self.battery_size = 75  # kWh, demo default

    # Optional: a child-specific behavior
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


Demo that matches the page narrative (simple instantiation)
ecar = ElectricCar('audi', 'a4', 2024)  # model choice here is illustrative
print(ecar.get_descriptive_name())
ecar.describe_battery()



 Exercise 9-5 — Login Attempts


class User:
    """Represent a simple user profile with login attempt tracking."""
    def __init__(self, first_name, last_name, **profile):
        self.first_name = first_name
        self.last_name = last_name
        self.profile = profile
        self.login_attempts = 0  # required by 9-5

    def describe_user(self):
        """Print a summary of the user's information."""
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"\nUser: {full_name}")
        if self.profile:
            for key, value in self.profile.items():
                print(f"- {key}: {value}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()}!")

     9-5 methods:
    def increment_login_attempts(self):
        """Increase login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


 Demo for 9-5
u = User("pieter", "van der berg", role="applikationsutvecklare")
u.describe_user()
u.greet_user()

print("\nIncrementing login attempts...")
for _ in range(3):
    u.increment_login_attempts()
    print("login_attempts =", u.login_attempts)

print("Resetting login attempts...")
u.reset_login_attempts()
print("login_attempts =", u.login_attempts)




PAGE 167 SUMMARY

• Inheritance lets a child class reuse the parent class's attributes and methods.
  Use super().__init__(...) inside the child to initialize the parent's part.

• ElectricCar demonstrates a child class that calls Car.__init__ and can add
  EV-specific attributes (e.g., battery_size) and methods.

• Exercise 9-5 adds login_attempts to User with:
     increment_login_attempts() and reset_login_attempts().

Takeaway: extend behavior by inheriting from a base class, and add only what is
unique to the child.
"""
print(summary)
