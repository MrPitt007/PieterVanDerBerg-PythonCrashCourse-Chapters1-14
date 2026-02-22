
Chapter 9 – Page 164
Topic: Modifying Attribute Values (directly) + Intro to modifying via a method
Python Crash Course – Notes and Examples
"""
 CAR CLASS (recap from previous pages)


class Car:
    A simple attempt to model a car.

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car, plus a default odometer."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # default value (introduced on p.163)

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

  
     (Preview) Modifying via a method — introduced on p.164, detailed next:
     We'll include the methods now so this file is runnable both ways.
   
    def update_odometer(self, mileage):
        """
        Set the odometer to the given value.
        In later pages, we'll also protect against rolling back the odometer.
        """
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

 MODIFYING AN ATTRIBUTE'S VALUE DIRECTLY


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

 Default odometer value (0)
my_new_car.read_odometer()

 Set the value directly on the instance (as shown on page 164):
my_new_car.odometer_reading = 23
my_new_car.read_odometer()   # -> "This car has 23 miles on it."



 (Preview) MODIFYING THROUGH A METHOD
 The page mentions this approach; full treatment follows on the next page.
 We show it here so you can compare both styles quickly.


# Replace the value via a setter-like method:
my_new_car.update_odometer(100)
my_new_car.read_odometer()

# Increment the value via a method:
my_new_car.increment_odometer(50)
my_new_car.read_odometer()   # -> 150 total


PAGE 164 SUMMARY

1) You can change an attribute on an instance **directly**:
       my_new_car.odometer_reading = 23

2) Direct updates are simple and explicit, but methods can be useful when:
   • you want validation (e.g., prevent rolling back mileage),
   • you want to log or trigger side effects when values change,
   • you want a consistent API across your codebase.

3) Two common method patterns (introduced here, expanded on next pages):
   • update_odometer(new_value)    → set to a specific value
   • increment_odometer(delta)     → add a certain amount

Compare approaches and choose the clearer one for your use case.
"""
print(summary)
