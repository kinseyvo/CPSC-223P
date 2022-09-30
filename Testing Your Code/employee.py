class Employee:
    """A class that models an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """Initializes the first name, last name, and annual salary"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, bonus=5000):
        """By default, bonus increases by 5000 unless otherwise stated"""
        self.annual_salary += bonus