try:
    number_1 = input("Enter a number: ")
    number_1 = int(number_1)

    number_2 = input("Enter another number: ")
    number_2 = int(number_2)

except ValueError:
    print("Numbers only please.")

else:
    sum = number_1 + number_2
    print(sum)
