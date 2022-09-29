class Restaurant:
    """"A class that models a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """"Describes restaurant with given information"""
        print(f'{self.restaurant_name} is a {self.cuisine_type} restaurant.')

    def open_restaurant(self):
        """"Prints a message indicating that the restaurant is open"""
        print(f'{self.restaurant_name} is now open for business!')


restaurant = Restaurant("Chen's Noodle House", "Chinese")
print(f'Restaurant name: {restaurant.restaurant_name}')
print(f'Cuisine type: {restaurant.cuisine_type}')

restaurant.describe_restaurant()
restaurant.open_restaurant()
