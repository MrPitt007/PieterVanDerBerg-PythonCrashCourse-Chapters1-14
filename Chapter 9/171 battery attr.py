 Parent class (Car) — minimal context


class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()



Battery as a separate class (composition)


class Battery:
    """Model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size  # kWh

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")



 ElectricCar uses a Battery instance as an attribute


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize parent attributes, then add a Battery instance."""
        super().__init__(make, model, year)
        self.battery = Battery()  # default 40 kWh per the page


 Demo matching Page 171


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())     # "2024 Nissan Leaf"
my_leaf.battery.describe_battery()        # access composed object's method

