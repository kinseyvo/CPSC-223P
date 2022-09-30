filename = "guest_book.txt"

print("Enter 'q' to stop the program.\n")
while True:
    name = input("What's your name? ")
    if name == 'q':
        break
    else:
        with open(filename, 'a') as file:
            file.write(name.title() + "\n")
        print(f'Hi {name.title()}, your presence has been recorded!')