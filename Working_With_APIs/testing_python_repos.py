import unittest
import requests

class TestPythonRepos(unittest.TestCase):
    """A class to to test functions in python_repos.py."""
    def setUp(self):
        self.url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        self.r = requests.get(self.url)
        self.code = 200
        self.response_dict = self.r.json()
    def test_get_url(self):
        """Test if the requests.get(url) is equal to the code of 200."""
        self.assertEqual(self.r.status_code, self.code)

    def test_number_of_items(self):
        """Test that the number of items returned is expected."""
        self.assertEqual(len(self.response_dict['items']), int(30))

    def test_repos_greater_items(self):
        """Test does number of repositories is > than number of items."""
        self.assertGreater(self.response_dict['total_count'],
                            len(self.response_dict['items']))

unittest.main()
