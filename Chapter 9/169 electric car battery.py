 
 Parent class (Car) — minimal version for context


class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # from earlier pages

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make} {self.model}".title()




class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize parent attributes, then EV-specific ones.
        """
        super().__init__(make, model, year)
        self.battery_size = 40  # kWh (as shown on the page)

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


 Demo matching Page 169


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())   # -> "2024 Nissan Leaf"
my_leaf.describe_battery()              # -> "This car has a 40-kWh battery."





PAGE 169 SUMMARY

• After establishing inheritance, add child-specific state/behavior:
    - Attribute:  battery_size = 40
    - Method:     describe_battery()

• The child inherits base functionality (e.g., get_descriptive_name) from Car
  and adds EV-specific details without duplicating the parent code.
"""
print(summary)
