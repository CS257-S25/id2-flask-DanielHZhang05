"""Tests for app.py"""
import unittest
import app


class TestCovidStats(unittest.TestCase):
    app.main()
   
    """This class tests our flask app"""
    def test_main(self):
        """Test the homepage function of the app."""
        self.assertEqual(app.aboutpage, """To access add /covid_stats/Afghanistan/2021-01-01/2022-01-12
    to the top of your browswer tab
    to get the total cases and deaths in Afghanistan between 2021-01-01 to 2022-01-12
    If you want to you can replace Afghanistan with any country of your choice
    and the dates with a date of your choice. The earliest date is 2020-01-05
    and the latest date is 2025-03-23
    Make sure to follow the correct format of YYYY-MM-DD when entering dates""")

    def test_aboutpage(self):
        """Test the about page of the app."""
        self.assertEqual(app.covid_deaths('Afghanistan', '2021-01-01', '2021-01-12'),
       "Total cases in Afghanistan is: 1641, total deaths in Afghanistan is: 119")
