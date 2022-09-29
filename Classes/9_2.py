class Restaurant:
    """"A class that models a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """"Describes restaurant with given information"""
        print(f'{self.restaurant_name} is a {self.cuisine_type} restaurant.\n')

    def open_restaurant(self):
        """"Prints a message indicating that the restaurant is open"""
        print(f'{self.restaurant_name} is now open for business!')


restaurant_1 = Restaurant("Chen's Noodle House", "Chinese")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("Vegan Brand", "Vegan")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("Cafe Patio", "Fusion")
restaurant_3.describe_restaurant()