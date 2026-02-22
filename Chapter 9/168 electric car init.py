
Parent class (Car) — as built on previous pages

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
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Validated set (no rollback)."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Validated increment."""
        if miles < 0:
            print("You can't roll back an odometer by adding negative miles!")
            return
        self.odometer_reading += miles



 Child class — ElectricCar calls parent __init__ with super()


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class, then EV-specific ones.
        Using super() calls Car.__init__(...) so make/model/year are set.
        """
        super().__init__(make, model, year)
        # Child-specific attributes (simple placeholder for this page):
        self.battery_size = 40  # kWh, minimal example for Page 168

     Optional child behavior to show EV-specific data
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


 Demo matching the page narrative
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())  # Expected style: "2024 Nissan Leaf"
my_leaf.describe_battery()



PAGE 168 SUMMARY

• Define a child class by placing the parent in parentheses:
      class ElectricCar(Car):

• In the child's __init__, call the parent's __init__ with super():
      super().__init__(make, model, year)

• After calling super(), add attributes/methods that are unique
  to the child (e.g., battery_size, describe_battery()).

• Result: ElectricCar inherits Car behavior (like get_descriptive_name)
  and extends it with EV-specific details.
"""
print(summary)
