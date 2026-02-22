
 car.py (simulated module)


class Car:
    """A simple attempt to represent gas or electric cars."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer to the given value with rollback protection."""
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


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

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
            _range = int(self.battery_size * 3.5)
        print(f"This car can go about {_range} miles on a full charge.")


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Composition: ElectricCar contains a Battery instance
        self.battery = Battery()



 Example usage (like my_car.py)


if __name__ == "__main__":
    my_ecar = ElectricCar('nissan', 'leaf', 2024)
    print(my_ecar.get_descriptive_name())
    my_ecar.battery.describe_battery()
    my_ecar.battery.get_range()
