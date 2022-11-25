import unittest
from pygal.maps.world import COUNTRIES
from get_country_code import get_country_code, get_country_list, get_code_list

class TestGetCountryCode(unittest.TestCase):
    """Test for get_country_code function."""

    def setUp(self):
        self.country_name = 'Albania'
        self.wrong_country_name = 'albania'
        self.country_list = get_country_list()
        self.code_list = get_code_list()
    def test_get_cc_correct_name(self):
        """Does Andorra is equal to ad?"""
        cc = get_country_code(self.country_name)
        self.assertEqual(cc, 'al')

    def test_get_cc_wrong_name(self):
        """Does Andora is not equal to ad?"""
        w_cc = get_country_code(self.wrong_country_name)
        self.assertNotEqual(w_cc,'ad')

    def test_get_cc_list_(self):
        """Does list of country names will produce correct codes."""
        country_code = []
        for country in self.country_list:
            country_code.append(get_country_code(country))
        self.assertEqual(country_code, self.code_list)


unittest.main()
