
 Base class for context

class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()



 Battery class — now with get_range()


class Battery:
    """Model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size  # kWh

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            _range = 150
        elif self.battery_size == 65:
            _range = 225
        else:
            # Simple fallback if other sizes are used
            # (Not in the book; included for completeness.)
            _range = int(self.battery_size * 3.5)

        print(f"This car can go about {_range} miles on a full charge.")



 ElectricCar uses Battery via composition


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # default 40-kWh per the page


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())    # "2024 Nissan Leaf"
my_leaf.battery.describe_battery()       # "This car has a 40-kWh battery."
my_leaf.battery.get_range()              # "This car can go about 150 miles..."


