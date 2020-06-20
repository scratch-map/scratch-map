import unittest

from scratch_map.countries import Countries


class TestCountries(unittest.TestCase):
    def setUp(self):
        self.countries = Countries()
        self.countries.country_list = ["UK", "Belgium", "China"]

    def test_add_country(self):
        self.countries.add_country("France")
        self.assertListEqual(
            self.countries.country_list, ["UK", "Belgium", "China", "France"]
        )

    def test_remove_country(self):
        self.countries.remove_country("China")
        self.assertListEqual(self.countries.country_list, ["UK", "Belgium"])
