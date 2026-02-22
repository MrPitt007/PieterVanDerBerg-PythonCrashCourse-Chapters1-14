
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



 MAKING AN INSTANCE (OBJECT) FROM THE CLASS


my_dog = Dog('willie', 6)

 Accessing attributes with dot notation:
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")

Output on the page is equivalent to:
My dog's name is Willie.
My dog is 6 years old.


CALLING METHODS ON THE INSTANCE


my_dog.sit()
my_dog.roll_over()
