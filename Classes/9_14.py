from random import randint, choice

def get_winning_ticket_number(series):
    candidate = ""
    for i in range(4):
        candidate += series[randint(0,9)]
    for i in range(4):
        candidate += choice(series[10:])
    
    winning_ticket_list.append(candidate)


series = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D"]

winning_ticket_list = list()

for i in range(1,11):  
    get_winning_ticket_number(series)

print(winning_ticket_list)