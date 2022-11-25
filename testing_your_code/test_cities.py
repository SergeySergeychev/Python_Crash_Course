import unittest
from city_functions import get_formatted_city_country

class CityCountryTestCase(unittest.TestCase):
    """Test for 'city_functions'."""

    def test_city_country(self):
        """Do name of city, country like 'Riga, Latvia' work?"""
        formatted_city_country = get_formatted_city_country('riga', 'latvia')
        self.assertEqual(formatted_city_country, 'Riga, Latvia.')

    def test_city_country_population(self):
        """Do string like 'Riga, Latvia - population xxxxxx' work"""
        formatted_city_country_pop = get_formatted_city_country('riga',
         'latvia', population=50000)
        self.assertEqual(formatted_city_country_pop,
            'Riga, Latvia - Population 50000.')
unittest.main()
