def modify_city_country(city_name, country_name, population=''):
    """Get a city name and a country name in the special form."""
    if population:
        city_country = f"{city_name.title()}, {country_name.title()} {population}"
    else:
        city_country = f"{city_name.title()}, {country_name.title()}"
    return(city_country)