import unittest
from city_functions import city_country

class TestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = city_country("delhi", "india")
        self.assertEqual(formatted_name, 'Delhi, India')
    def test_city_country_population(self):
        formatted_name = city_country('delhi', 'india', '30000000')
        self.assertEqual(formatted_name, 'Delhi, India - population 30000000')

unittest.main()