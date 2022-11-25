def city_country(city, country):
    """Return neatly formatted city and country"""
    string = f"{city.title()}, {country.title()}"
    return print(string)

city_country('santiago', 'chile')
city_country('riga', 'latvia')
city_country('moscow', 'russia')
