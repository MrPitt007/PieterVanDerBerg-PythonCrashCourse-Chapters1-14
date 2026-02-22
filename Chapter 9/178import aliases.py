

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
        self.battery = Battery()


print("\n--- Using imports with an alias (as) ---")
my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = EC('nissan', 'leaf', 2024)   # alias instead of ElectricCar
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

PAGE 178 SUMMARY
-----------------
• Import classes from separate modules:
      from car import Car
      from electric_car import ElectricCar

• Use an alias with 'as' to shorten or clarify names:
      from electric_car import ElectricCar as EC
      my_ev = EC('nissan', 'leaf', 2024)

• Benefits of aliases:
  - Less typing for long class/function names
  - Avoid name collisions
  - Keep code readable while making origin clear in the import line
"""
print(summary)
