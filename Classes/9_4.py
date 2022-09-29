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


restaurant = Restaurant("Chen's Noodle House", "Chinese")
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} people so far!')
restaurant.number_served = 21
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} people so far!')

#With set_number_served() function
restaurant.set_number_served(69)
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} people so far!')

restaurant.increment_number_served(5)
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} people so far!')