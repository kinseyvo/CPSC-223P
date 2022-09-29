#Using list from 7-12 and printing numbers in formatted output using an str.format()
number_list = [123.45, -5.12345, 0.056789]

print("Formatted number list:\n")

for number in number_list:
    print('{:_^20}'.format(number))