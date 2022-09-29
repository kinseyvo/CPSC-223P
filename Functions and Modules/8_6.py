def city_country(city, country):
    """Return a concatenated string"""
    pair = city.title() + ', ' + country.title()
    return pair


print(city_country('paris', 'france'))
print(city_country('new york city', 'united states'))
print(city_country('london', 'england'))