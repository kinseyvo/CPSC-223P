print("---Enter \'q\' to quit at anytime---")

while True:
    try:
        number_1 = input("Enter a number: ")
        if number_1 == 'q':
            print("Have a good one")
            break
        number_1 = int(number_1)

        number_2 = input("Enter another number: ")
        if number_2 == 'q':
            print("Have a good one")
            break
        number_2 = int(number_2)

    except ValueError:
        print("Numbers only please.")

    else:
        sum = number_1 + number_2
        print(sum)