
 Parent class (Car) — minimal features for the demo


class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()

     Method that makes sense for gas cars; will be overridden in ElectricCar.
    def fill_gas_tank(self):
        print("Filling the gas tank...")



 Child class — override a method that doesn't fit EVs


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Composition: give each ElectricCar its own Battery instance.
        self.battery = Battery(battery_size=40)

     OVERRIDE: This replaces Car.fill_gas_tank for ElectricCar objects.
    def fill_gas_tank(self):
        print("This car doesn't have a gas tank!")

     Convenience passthrough to show battery information
    def describe_battery(self):
        self.battery.describe_battery()


Composition — Battery as a separate class used by ElectricCar


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size  # kWh

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

Overridden behavior:
my_leaf.fill_gas_tank()       # -> "This car doesn't have a gas tank!"

Child-specific/Composed behavior:
my_leaf.describe_battery()    # -> "This car has a 40-kWh battery."
my_leaf.battery.describe_battery()  # same, via the composed object directly



