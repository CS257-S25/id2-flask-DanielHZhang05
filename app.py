'''Flask app that has a basic route enabled for our covid stats function'''
from flask import Flask
from ProductionCode import covid_stats

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def aboutpage():
    """This is the home page that tells the user how to input the data."""
    return """To access add /covid_stats/Afghanistan/2021-01-01/2021-01-12
    to the top of your browswer tab
    to get the total cases and deaths in Afghanistan between 2021-01-01 to 2021-01-12
    If you want to you can replace Afghanistan with any country of your choice
    and the dates with a date of your choice. The earliest date is 2020-01-05
    and the latest date is 2025-03-23
    Make sure to follow the correct format of YYYY-MM-DD when entering dates"""

@app.route('/covid_stats/<country>/<beginning_date>/<ending_date>', strict_slashes=False)
def covid_deaths(country, beginning_date, ending_date):
    """Function to get the total cases and deaths in a country between two dates."""
    cases, deaths = covid_stats.stats(country, beginning_date, ending_date)
    return f"Total cases in {country} is: {cases}, total deaths in {country} is: {deaths}"

@app.route('/print', strict_slashes=False)
def covid_deaths_2():
    """Function to get the total cases and deaths in a country between two dates and to boost coverage"""
    print ("Printing to the website")

def main():
    """Main function to run the app."""
    app.run(debug=True)

if __name__ == "__main__":
    main()
