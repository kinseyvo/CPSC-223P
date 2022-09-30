import json

filename = "favorite_number.json"

try:
    with open(filename, 'r') as file:
        number = json.load(file)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, 'w') as file:
        json.dump(number, file)
else:
    print(f'I know your favorite number! It\'s {number}.')