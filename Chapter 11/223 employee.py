Chapter 11/223 employee.py

class Employee:
    """Represent an employee with first name, last name, and annual salary."""

    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add $5000 to the annual salary by default, or a custom amount."""
        self.annual_salary += amount
