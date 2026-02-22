"""
Chapter 9 – Page 161
Topic: Creating Multiple Instances from a Class
Python Crash Course – Notes and Examples
"""

Dog class (from previous pages)


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

 CREATING MULTIPLE INSTANCES

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

 Instance 1
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

 Instance 2
print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

 Expected textual output (same idea as the page):
 My dog's name is Willie.
 My dog is 6 years old.
 Willie is now sitting.
 Your dog's name is Lucy.
 Your dog is 3 years old.
 Lucy is now sitting.



 WHY MULTIPLE INSTANCES WORK
explanation = """
Each instance created from Dog has its own copy of attributes (name, age),
so my_dog and your_dog keep separate state. Both instances can call the same
methods (sit, roll_over) defined on the class, but the behavior uses data
stored on the specific instance (accessed through 'self').
"""
print(explanation)


1) You can create as many instances from a class as you need:
      my_dog = Dog('willie', 6)
      your_dog = Dog('lucy', 3)

2) Each instance stores its own attributes, so values don't collide.

3) Methods are shared by the class but act on the individual instance via 'self'.

4) Use dot notation to:
      • access attributes  → my_dog.name, your_dog.age
      • call methods       → my_dog.sit(), your_dog.roll_over()
"""
print(summary)
