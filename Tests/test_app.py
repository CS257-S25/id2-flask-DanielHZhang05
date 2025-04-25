"""Tests for app.py"""
import unittest
import sys
import app
from io import StringIO

class TestCovidStats(unittest.TestCase):
   """This class tests our flask app"""
   def test_main(self):
      """Test the main function of the app."""
      sys.argv = ['cl.py', 'stats', 'Afghanistan', '2020-01-01', '2020-01-12']
      sys.stdout = StringIO()
      app.main()
      printed_output = sys.stdout.getvalue()
      self.assertEqual(printed_output, "To access Go to the url http://127.0.0.1:5000/covid_stats/Afghanistan/2021-01-01/2022-01-12 to get the total cases and deaths in Afghanistan between 2021-01-01 to 2022-01-12")

   def test_aboutpage(self):
      """Test the about page of the app."""
      self.assertEqual(app.covid_deaths('Afghanistan', '2021-01-01', '2021-01-12'), "Total cases in Afghanistan is: 0, total deaths in Afghanistan is: 0")