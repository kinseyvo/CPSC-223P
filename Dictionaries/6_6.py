favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

poll_people = ['edward', 'deez', 'bruce', 'jen']

for ppl in poll_people:
    if ppl in favorite_languages.keys():
        print(f"Thank you for responding, {ppl.title()}!")
    else:
        print(f"{ppl.title()}, please take the poll!")