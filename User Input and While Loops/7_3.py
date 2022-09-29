number = input("Enter a number and I will report if it's a multiple of 10. ")
number = int(number)
if number % 10 == 0:
    print(f'{number} is a multiple of 10!')
else:
    print(f'{number} is NOT a multiple of 10!')