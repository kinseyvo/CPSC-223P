class Restaurant:
    """"A class that models a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """"Describes restaurant with given information"""
        print(f'{self.restaurant_name} is a {self.cuisine_type} restaurant.')

    def open_restaurant(self):
        """"Prints a message indicating that the restaurant is open"""
        print(f'{self.restaurant_name} is now open for business!')

    def set_number_served(self, number_served):
        """Sets the number of customers served at the restaurant"""
        if number_served > self.number_served:
            self.number_served = number_served

    def increment_number_served(self, new_customers):
        """Adds more customers who were served"""
        if new_customers > 0:
            self.number_served += new_customers


class IceCreamStand(Restaurant):
    """"A class that models a Ice Cream Stand"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes ice cream instance"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """"Displays all ice cream flavors"""
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print('\t-', flavor.title())