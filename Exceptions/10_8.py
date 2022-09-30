catFile = "cats.txt"
dogFile = "dogs.txt"

try:
    with open(catFile, encoding='utf-8') as f:
        catContents = f.read()
except FileNotFoundError:
    print(f'The file {catFile} was not found.')
else:
    print(f'Contents of {catFile}:')
    print(catContents)

try:
    with open(dogFile, encoding='utf-8') as f:
        dogContents = f.read()
except FileNotFoundError:
    print(f'The file {dogFile} was not found.')
else:
    print(f'\nContents of {dogFile}:')
    print(dogContents)