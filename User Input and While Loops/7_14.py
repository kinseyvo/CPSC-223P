print(f'{"Name":16} {"Birthdate":15} {"Birthplace":18}{"Quote"}')
print('{:->72}'.format(''))

person_1 = {'first': 'Duke', 'last': 'Ellington', 'month': 'April', 'day': 29, 'year': 1899,
            'birthplace': 'Washington D.C.', 'quote': "Gray skies are just clouds passing over."}
person_2 = {'first': 'Miles', 'last': 'Davis', 'month': 'May', 'day': 26, 'year': 1926,
            'birthplace': 'Alton, IL', 'quote': "I always listen for what I can leave out."}
person_3 = {'first': 'Goro', 'last': 'Masamune', 'month': 'May', 'day': 26, 'year': 1926,
            'birthplace': 'Japan', 'quote': "I made the Honjo Masamune."}

famous_people = [person_1, person_2, person_3]

for ppl in famous_people:
    #First Attempt
    #print('{}, {:17}'.format(ppl['last'], ppl['first']), '{} {}, {:<11}'.format(ppl['month'], ppl['day'], 
    #             ppl['year']), '{:<25}'.format(ppl['birthplace']), ppl['quote'])

    name = ppl['last'] + ', ' + ppl['first']
    b_date = ppl['month'] + ' ' + str(ppl['day']) + ', ' + str(ppl['year'])
    b_place = ppl['birthplace']
    quote = ppl['quote']
    print(f'{name:16} {b_date:15} {b_place:18}{quote}\n')