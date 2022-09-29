from restaurant import Restaurant

restaurant = Restaurant("Chen's Noodle House", "Chinese")
restaurant.set_number_served(69)
print(f'{restaurant.restaurant_name} has served {restaurant.number_served} people so far!')