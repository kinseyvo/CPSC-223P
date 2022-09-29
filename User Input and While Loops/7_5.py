print("Welcome to the movie theater!\nEnter 'quit' when done.\n")
ticket_price = 0

active = True
while active:
    age = input("How old are you? ")
    if age == 'quit':
        print("\nHave a great day!")
        break
    age = int(age)

    if age < 3:
        print("The ticket is free!")
        ticket_price = 0
    elif ((age >= 3) & (age <= 12)):
        ticket_price = 10
        print("The ticket will be $10.")
    else:
        ticket_price = 15
        print("The ticket will be $15.")
