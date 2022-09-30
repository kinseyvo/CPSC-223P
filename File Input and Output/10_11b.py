import json

filename = "favorite_number.json"

with open(filename, 'r') as file:
    number = json.load(file)
    print(f'I know your favorite number! It\'s {number}.')