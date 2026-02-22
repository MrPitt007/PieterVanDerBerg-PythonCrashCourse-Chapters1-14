 CAR CLASS — increment miles + validated update


class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize attributes and set default odometer to 0."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make} {self.model}".title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("You can't roll back an odometer by adding negative miles!")
            return
        self.odometer_reading += miles


 Demo from page 166 (used car, set then increment)
my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)   # set starting mileage
my_used_car.read_odometer()

my_used_car.increment_odometer(100)  # add miles driven since purchase
my_used_car.read_odometer()



EXERCISE 9-4 — NUMBER SERVED (Restaurant)

class Restaurant:
    """Represent a restaurant and its customer count."""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # default value

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

    def set_number_served(self, count):
        """Set the served count to a specific value (reject negatives)."""
        if count < 0:
            print("number_served cannot be negative.")
            return
        self.number_served = count

    def increment_number_served(self, count):
        """Increment the served count (reject negatives)."""
        if count < 0:
            print("Cannot decrement number_served via increment.")
            return
        self.number_served += count

 Demo for 9-4
print("\n--- Exercise 9-4: Number Served ---")
resto = Restaurant("Polar Bistro", "nordic")
print("Initial number served:", resto.number_served)  # default 0

resto.set_number_served(23)
print("After set_number_served(23):", resto.number_served)

resto.increment_number_served(17)
print("After increment_number_served(17):", resto.number_served)  # total 40




PAGE 166 SUMMARY

• Car.increment_odometer(miles) adds to the current odometer reading.
  Combine with update_odometer(value) for clear, validated state changes.

• Exercise 9-4:
  Add an attribute 'number_served' to Restaurant (default 0), print it,
  change the value, and print again. Optional helpers:
  set_number_served(value) and increment_number_served(value).
"""
print(summary)
