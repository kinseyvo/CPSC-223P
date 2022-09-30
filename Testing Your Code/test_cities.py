import unittest
from city_functions import city_country_name

class CityTestCase(unittest.TestCase):
    """"Tests for 'cit_funcions.py'."""

    def test_city_country(self):
        """"Do cities like 'Santiago, Chile' work?'"""
        city_country = city_country_name('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cities w/ population numbers like 'Santiago, Chile - population 5000000' work?'"""
        city_country_population = city_country_name('santiago', 'chile', 5000000)
        self.assertEqual(city_country_population, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()