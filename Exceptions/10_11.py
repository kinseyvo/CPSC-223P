automobileFile = "automobile.txt"
queensFile = "queens.txt"

try:
    with open(automobileFile, encoding='utf-8') as f:
        automobileContents = f.read()
except FileNotFoundError:
    print(f'Unfortunately, the file {automobileFile} was not found.')
else:
    automobile_list = automobileContents.split()
    user_word = input("Enter a word and I will return how many times it occurs in the text: ")
    count = 0
    for word in automobile_list:
        if word.lower() == user_word.lower():
            count += 1
    print(f'{automobileFile} \'{user_word.lower()}\' count:', count)

try:
    with open(queensFile, encoding='utf-8') as f:
        queensContents = f.read()
except FileNotFoundError:
    print(f'Unfortunately, the file {queensFile} was not found.')
else:
    queens_list = queensContents.split()
    user_word = input("\nEnter a word and I will return how many times it occurs in the text: ")
    count = 0
    for word in queens_list:
        if word.lower() == user_word.lower():
            count += 1
    print(f'{queensFile} \'{user_word.lower()}\' count:', count)