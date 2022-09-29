sandwich_orders = ["Sandwich 1", "pastrami", "pastrami", "Sandwich 2", "Sandwich 3", "pastrami"]
finished_sandwiches = []

print("The deli has run out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Just completed: {current_sandwich}')
    finished_sandwiches.append(current_sandwich)

print("\nEach sandwich has been made:")
for sandwich in finished_sandwiches:
    print(f'\t- {sandwich}')