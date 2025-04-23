'''Flask app that has a basic route enabled'''
from flask import Flask
from ProductionCode import covid_stats

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def aboutpage():
    return "Go to the url http://127.0.0.1:5000/covid_stats/Afghanistan/2021-01-01/2022-01-12 to get the total cases and deaths in a country between two dates"

@app.route('/covid_stats/<country>/<beginning_date>/<ending_date>', strict_slashes=False)
def covid_deaths(country, beginning_date, ending_date):
    cases, deaths = covid_stats.stats(country, beginning_date, ending_date)
    return f"Total cases in {country} is: {cases}, total deaths in {country} is: {deaths}"


if __name__ == "__main__":
    covid_stats.load_data()
    app.run(debug=True)