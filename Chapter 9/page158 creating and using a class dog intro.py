
 DEFINING A SIMPLE CLASS: Dog

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name.title()} rolled over!")


 The class above is a blueprint; now we create a specific dog:

my_dog = Dog('willie', 6)

Call methods on the instance:
my_dog.sit()
my_dog.roll_over()

 Access attributes directly:
print("\nAttributes:")
print(f"name = {my_dog.name}")
print(f"age  = {my_dog.age}")


 WHY THIS MATTERS (quick notes)


notes = """
OOP BASICS SHOWN ON PAGE 158
----------------------------
• class Dog: defines a new type with attributes and behaviors.
• __init__(self, ...): runs automatically when a new Dog is created.
  - 'self' refers to the specific instance being constructed.
  - 'name' and 'age' become instance attributes stored on self.
• Methods (sit, roll_over): functions defined inside the class that
  operate on an instance via 'self'.
• After defining the class, you instantiate it:
      my_dog = Dog('willie', 6)
  and then call methods:
      my_dog.sit()
      my_dog.roll_over()
"""
print(notes)
