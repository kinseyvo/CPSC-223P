cities = {
    'garden grove': {
        'county': 'Orange County',
        'population': 173258,
        'fact': 'The Strawberry Festivals are hosted here every year in May'
    },
    'riverside': {
        'county': 'Riverside County',
        'population': 326414,
        'fact': 'Riverside is also known as the Inland Empire'
    },
    'fountain valley': {
        'county': 'Orange County',
        'population': 56026,
        'fact': 'It has Mile Square Park'
    }
}

for city, info in cities.items():
    print(f"{city.title()}:")
    print(f"\tCounty: {info['county']}\n\tPopulation: {info['population']}\n\tFact: {info['fact']}\n")