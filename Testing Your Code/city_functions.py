def city_country_name(city, country, population=''):
    """Returns a city and country with population number"""
    if population:
        combined = f'{city.title()}, {country.title()} - population {population}'
    else:
        combined = f'{city.title()}, {country.title()}'
    return combined
