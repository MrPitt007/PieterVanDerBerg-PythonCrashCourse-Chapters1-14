
Chapter 9 – Page 163
Topic: Car class — default attribute value and read_odometer()
Python Crash Course – Notes and Examples


class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car, plus a default odometer."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # default value introduced on page 163

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


 DEMO — creating an instance and using the methods


my_new_car = Car('audi', 'a4', 2024)

 Show the descriptive name (as in the page)
print(my_new_car.get_descriptive_name())

Read the default odometer value (0 miles)
my_new_car.read_odometer()



 EXTRA: show that each instance starts at 0 and is independent


another_car = Car('subaru', 'outback', 2015)
another_car.read_odometer()  # also 0 by default

 Change one instance's reading without affecting the other
my_new_car.odometer_reading = 125
print("\nAfter updating my_new_car's mileage:")
my_new_car.read_odometer()
print("another_car remains:")
another_car.read_odometer()




summary = """
PAGE 163 SUMMARY
-----------------
1) You can define attributes with **default values** in __init__.
   Example: self.odometer_reading = 0

2) Adding the method read_odometer() lets the object report its state:
       def read_odometer(self):
           print(f"This car has {self.odometer_reading} miles on it.")

3) Each instance has its own copy of attributes. Updating the odometer on one
   car does not affect other car instances.

4) Pattern recap:
   - Define attributes (some from parameters, some with defaults).
   - Provide methods to return strings (get_descriptive_name)
     and to display or manipulate internal state (read_odometer).
"""
print(summary)
