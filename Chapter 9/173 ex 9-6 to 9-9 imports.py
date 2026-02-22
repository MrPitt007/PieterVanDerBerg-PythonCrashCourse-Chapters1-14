

 9-6 — ICE CREAM STAND (inherit Restaurant)


class Restaurant:
    "Represent a restaurant with a name and cuisine type

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")


class IceCreamStand(Restaurant):
    A specific kind of Restaurant that sells ice cream."""

    def __init__(self, name, cuisine_type="ice cream"):
        super().__init__(name, cuisine_type)
        self.flavors = []  # list of strings

    def show_flavors(self):
        """Print the available ice cream flavors."""
        if not self.flavors:
            print("No flavors listed yet.")
            return
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Demo 9-6
stand = IceCreamStand("Arctic Scoops")
stand.flavors = ["vanilla", "chocolate", "strawberry", "pistachio"]
stand.describe_restaurant()
stand.show_flavors()



 9-7 — ADMIN (inherit User + privileges list)
 9-8 — PRIVILEGES (separate class used as attribute on Admin)


class User:
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, **profile):
        self.first_name = first_name
        self.last_name = last_name
        self.profile = profile

    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"\nUser: {full_name}")
        if self.profile:
            for k, v in self.profile.items():
                print(f"- {k}: {v}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()}!")


class Privileges:
    """Store admin privileges and provide a method to show them."""

    def __init__(self, privileges=None):
        self.privileges = privileges if privileges is not None else []

    def show_privileges(self):
        if not self.privileges:
            print("This admin has no privileges assigned.")
            return
        print("Admin privileges:")
        for p in self.privileges:
            print(f"- {p}")


class Admin(User):
    """A special kind of user with administrative privileges."""

    def __init__(self, first_name, last_name, **profile):
        super().__init__(first_name, last_name, **profile)
        # Composition: a Privileges instance as an attribute of Admin
        self.privileges = Privileges()


# Demo 9-7 & 9-8
admin = Admin("ada", "lovelace", role="admin")
admin.privileges.show_privileges()  # initially none
admin.privileges.privileges = ["can add post", "can delete post", "can ban user"]
admin.privileges.show_privileges()



 9-9 — BATTERY UPGRADE (revisit EV example)


class Battery:
    """Model a battery for an electric car."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size  # kWh

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Report an estimated range based on battery size."""
        if self.battery_size == 40:
            rng = 150
        elif self.battery_size == 65:
            rng = 225
        else:
            rng = int(self.battery_size * 3.5)
        print(f"This car can go about {rng} miles on a full charge.")

    def upgrade_battery(self):
        """
        If the battery isn't already 65 kWh, set it to 65.
        (Do nothing if already 65.)
        """
        if self.battery_size < 65:
            self.battery_size = 65


class Car:
    """Minimal base class."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()


class ElectricCar(Car):
    """Represent an electric car."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()  # start with default 40 kWh

