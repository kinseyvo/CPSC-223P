automobileFile = "automobile.txt"
queensFile = "queens.txt"

try:
    with open(automobileFile, encoding='utf-8') as f:
        automobileContents = f.read()
except FileNotFoundError:
    print(f'Unfortunately, the file {automobileFile} was not found.')
else:
    automobile_list = automobileContents.split()
    count = 0
    for word in automobile_list:
        if word.lower() == 'the':
            count += 1
    print(f'{automobileFile} \'the\' count:', count)

try:
    with open(queensFile, encoding='utf-8') as f:
        queensContents = f.read()
except FileNotFoundError:
    print(f'Unfortunately, the file {queensFile} was not found.')
else:
    queens_list = queensContents.split()
    count = 0
    for word in queens_list:
        if word.lower() == 'the':
            count += 1
    print(f'\n{queensFile} \'the\' count:', count)