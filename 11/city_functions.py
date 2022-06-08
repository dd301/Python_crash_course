def city_country(city, country, population=''):
    if population:
        string = city.title() + ', ' + country.title() + ' - population ' + population
    else:
        string = city.title() + ', ' + country.title()
    return string
