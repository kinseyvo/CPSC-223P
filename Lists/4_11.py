favorite_pizzas = ["pepperoni", "cheese", "combo"]

for pizza in favorite_pizzas:
    print(f"I enjoy eating {pizza} pizza!")

print("I really enjoy eating pizza like the TMNT.")

friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("hawaiian")

friend_pizzas.append("pineapple")

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)