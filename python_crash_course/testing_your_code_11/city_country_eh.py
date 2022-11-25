# EX 11-2

# Code from ehmatthes.github.io

"""A collection of functions for working with cities."""

def city_country(city, country, population=0):
    """Return a string representing a city-country pair."""
    
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += ' - population ' + str(population)
    return output_string

city_country('riga', 'latvia', 5000000)