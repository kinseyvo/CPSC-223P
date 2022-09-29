def make_car(manufacturer, model, **info):
    """"A function that stores information about a car in a dictionary"""
    info['manufacturer'] = manufacturer
    info['model'] = model
    return info


car_1 = make_car('subaru', 'outback', color='blue', tow_package=True)
car_2 = make_car('toyota', 'corolla', color='white', edition='sports edition')
car_3 = make_car('honda', 'civic', year=2021, seats='leather')

cars = [car_1, car_2, car_3]
for car in cars:
    print(car)