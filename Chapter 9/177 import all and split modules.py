
 car.py  (SIMULATED MODULE — defines Car)


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()



 electric_car.py (SIMULATED MODULE — imports Car and defines EV bits)
 In real files you would write:
     from car import Car


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            rng = 150
        elif self.battery_size == 65:
            rng = 225
        else:
            rng = int(self.battery_size * 3.5)
        print(f"This car can go about {rng} miles on a full charge.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()




 Simulate results of: from electric_car import 

print("\n--- Simulated 'import *' effect (not recommended) ---")
leaf = _ElectricCar('nissan', 'leaf', 2024)
print(leaf.get_descriptive_name())
leaf.battery.describe_battery()
leaf.battery.get_range()

 Simulate module namespace objects so we can demonstrate safely in one file.

class _CarModule:
    Car = Car

class _ElectricModule:
    Battery = Battery
    ElectricCar = ElectricCar

car = _CarModule()
electric_car = _ElectricModule()

print("\n--- Importing a module into a module (split modules) ---")
my_mustang = car.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = electric_car.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

