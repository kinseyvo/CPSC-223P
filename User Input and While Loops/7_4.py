pizza_toppings = []
prompt = "What topping would you like on your pizza?\nEnter 'quit' when done. "

active = True
while active:
    topping = input(prompt)
    if topping != 'quit':
        print(f'Adding {topping.upper()} to your pizza!')
        pizza_toppings.append(topping)
    else:
        active = False

print("\n---Toppings---")
for topping in pizza_toppings:
    print(topping.title())