

CAR CLASS (adds validated update + increment methods)


class Car:
    """A simple attempt to model a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car, plus a default odometer."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # default value introduced on p.163

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

  
     p.165 — set value via a method

    def update_odometer(self, mileage):
        """
        Set the odometer to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

   
     p.165 — increment an attribute via a method
        def update_odometer(self, mileage):
        """
        Add the given amount to the odometer reading.
        Reject negative increments to avoid accidental rollbacks.
        """
        if miles < 0:
            print("You can't roll back an odometer by adding negative miles!")
            return
        self.odometer_reading += miles



 DEMOS — mirrored from the page, plus safe checks


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

# Start at the default 0 and display it
my_new_car.read_odometer()

# Set via the validated method (OK: 23 >= 0)
my_new_car.update_odometer(23)
my_new_car.read_odometer()   # -> 23 miles

Try to roll back (NOT OK: 10 < 23)
my_new_car.update_odometer(10)   # -> prints warning
my_new_car.read_odometer()       # still 23

Increment mileage properly
my_new_car.increment_odometer(100)
my_new_car.read_odometer()       # -> 123

 Guard against negative increments
my_new_car.increment_odometer(-50)  # -> prints warning
my_new_car.read_odometer()          # still 123


1) Methods can update attributes and also **validate** inputs:
     - update_odometer(mileage): sets mileage only if it's not less than
       the current reading (prevents rolling back the odometer).

2) Incrementing with a method:
     - increment_odometer(miles): adds a delta to the current reading.
       (This example rejects negative increments for safety.)

3) Why use methods instead of direct assignment?
     - Centralize validation rules.
     - Keep calling code clean and consistent.
     - Make state changes auditable and easier to test.

Pattern recap:
  car.update_odometer(NEW_VALUE)   # validated set
  car.increment_odometer(DELTA)    # validated add
"""
print(summary)
