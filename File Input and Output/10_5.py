filename = "responses.txt"

print("Enter 'q' to stop the program.\n")
while True:
    poll = input("Why do you like programming? ")
    if poll == 'q':
        break
    else:
        with open(filename, 'a') as file:
            file.write(poll + "\n")