"""Tests for app.py"""
import unittest
import app


class TestCovidStats(unittest.TestCase):

    """This class tests our flask app"""
    def test_about_page(self):
        """Test the homepage function of the app."""
        self.app = app.test_client()
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b"""To access add /covid_stats/Afghanistan/2021-01-01/2022-01-12
    to the top of your browswer tab
    to get the total cases and deaths in Afghanistan between 2021-01-01 to 2022-01-12
    If you want to you can replace Afghanistan with any country of your choice
    and the dates with a date of your choice. The earliest date is 2020-01-05
    and the latest date is 2025-03-23
    Make sure to follow the correct format of YYYY-MM-DD when entering dates""", response.data)

    def test_covid_deaths_return(self):
        """Test the about page of the app."""
        self.app = app.test_client()
        response = self.app.get('/covid_stats/Afghanistan/2021-01-01/2022-01-12', follow_redirects=True)
        self.assertIn(b"Total cases in Afghanistan is: 1641, total deaths in Afghanistan is: 119", response.data)
