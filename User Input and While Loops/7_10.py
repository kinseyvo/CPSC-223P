responses = {}

polling_status = True

while polling_status:
    name = input("What is your name? ")
    first_dream = input("Which country would your first dream vacation be in? ")
    second_dream = input("Which country would your second dream vacation be in? ")
    
    #Put dream vacations into a list
    dream_list = [first_dream, second_dream]

    #KEY=name and VALUE=dream_list 
    responses[name] = dream_list

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_status = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to visit {response[0].title()} and {response[1].title()}.")

print("\nDictionary contents:", responses)