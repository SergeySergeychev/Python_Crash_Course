from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        elif 'Libya' == country_name:
            return 'ly'
        elif 'Bolivia' == country_name:
            return 'bo'
        elif 'Congo, Dem. Rep.' == country_name:
            return 'cd'
        elif 'Dominica' == country_name:
            return 'do'
        elif 'Egypt, Arab Rep.' == country_name:
            return 'eg'
        elif 'Gambia, The' == country_name:
            return 'gm'
        elif 'Hong Kong SAR, China' == country_name:
            return 'hk'
        elif 'Iran, Islamic Rep.' == country_name:
            return 'ir'
        elif 'Korea, Dem. Rep.' == country_name:
            return 'kp'
        elif 'Korea, Rep.' == country_name:
            return 'kr'
        elif 'Kyrgyz Republic' == country_name:
            return 'kr'
        elif 'Lao PDR' == country_name:
            return 'la'
        elif 'Libya' == country_name:
            return 'ly'
        elif 'Macao SAR, China' == country_name:
            return 'mo'
        elif 'Macedonia, FYR' == country_name:
            return 'mk'
        elif 'Moldova' == country_name:
            return 'md'
        elif 'Slovak Republic' == country_name:
            return 'sk'
        elif 'Tanzania' == country_name:
            return 'tz'
        elif 'Venezuela, RB' == country_name:
            return 've'
        elif 'Vietnam ' == country_name:
            return 'vn'
        elif 'Yemen, Rep.' == country_name:
            return 'ye'
    # If the country wasn't found return None.
    return None
