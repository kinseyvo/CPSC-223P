person_info1 = {'first_name': 'Bruce', 'last_name': 'Wayne', 'age': 35, 'city': 'Gotham City'}

person_info2 = {'first_name': 'Dick', 'last_name': 'Grayson', 'age': 18, 'city': 'Bludhaven'}

person_info3 = {'first_name': 'Barry', 'last_name': 'Allen', 'age': 32, 'city': 'Central City'}

people = [person_info1, person_info2, person_info3]

for ppl in people:
    print(f"{ppl['first_name']} {ppl['last_name']} is {ppl['age']} and lives in the city of {ppl['city']}.")