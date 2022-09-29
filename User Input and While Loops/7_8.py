sandwich_orders = ["Sandwich 1", "Sandwich 2", "Sandwich 3"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Just completed: {current_sandwich}')
    finished_sandwiches.append(current_sandwich)

print("\nEach sandwich has been made:")
for sandwich in finished_sandwiches:
    print(f'\t- {sandwich}')