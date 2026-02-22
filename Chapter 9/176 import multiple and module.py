
car.py  (SIMULATED MODULE)


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()


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
        self.battery = Battery()  # default 40 kWh



 DEMO 1 — Importing multiple classes from a module
 Page example:
     from car import Car, ElectricCar
     my_mustang = Car('ford', 'mustang', 2024)
     my_leaf = ElectricCar('nissan', 'leaf', 2024)

 Since we're in a single file, we already have Car and ElectricCar available.
 We'll just run the same code to mirror the example.

print("\n--- Import multiple classes demo (as if: from car import Car, ElectricCar) ---")
my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())



 DEMO 2 — Importing an entire module
 Page concept:
     import car
     my_car = car.Car('audi', 'a4', 2024)
 In a single file we can't re-import ourselves as 'car', so we simulate a
 module namespace object that exposes the same classes.

class _ModuleNamespace:
    Car = Car
    Battery = Battery
    ElectricCar = ElectricCar

car = _ModuleNamespace()  # simulate: import car

print("\n--- Import entire module demo (as if: import car) ---")
my_audi = car.Car('audi', 'a4', 2024)
print(my_audi.get_descriptive_name())

my_ev = car.ElectricCar('nissan', 'leaf', 2024)
print(my_ev.get_descriptive_name())
my_ev.battery.describe_battery()
my_ev.battery.get_range()



