from random import randint, choice

def get_winning_ticket_number(series):
    candidate = ""
    for i in range(4):
        candidate += series[randint(0,9)]
    for i in range(4):
        candidate += choice(series[10:])
    
    winning_ticket_list.append(candidate)


def get_ticket(series):
    """Makes and returns a new ticket without being added to a list"""
    candidate = ""
    for i in range(4):
        candidate += series[randint(0,9)]
    for i in range(4):
        candidate += choice(series[10:])
    
    return candidate


def compare_tickets(winning_ticket, random_ticket):
    """Compares a ticket in the list with the random ticket that was generated"""
    if winning_ticket != random_ticket:
        return False
    else:
        return True


series = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D"]

winning_ticket_list = list()

for i in range(1,11):  
    get_winning_ticket_number(series)

print("winning ticket list:", winning_ticket_list)

#Chooses a random ticket to win
ticket_number = randint(0, 9)
your_ticket = winning_ticket_list[ticket_number]

flag = False
number_of_tries = 0

while not flag:
    random_ticket = get_ticket(series)
    #print("Winning ticket:", new_new)
    number_of_tries += 1
    if compare_tickets(your_ticket, random_ticket) == True:
        flag = True
        print("\nnumber_of_tries to win:", number_of_tries)
        break

print("\npossible winner:", your_ticket)