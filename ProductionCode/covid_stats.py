import csv
from datetime import datetime

reader = csv.DictReader(open('ProductionCode/WHO-COVID-19-global-data.csv', 'r'))

def load_data():
    with open('ProductionCode/WHO-COVID-19-global-data.csv', 'r') as file:
        reader = csv.DictReader(file)
    return reader

def stats(country, beginning_date, ending_date):
    beginning = datetime.strptime(beginning_date, "%Y-%m-%d")
    ending = datetime.strptime(ending_date, "%Y-%m-%d")
    
    total_cases = 0
    total_deaths = 0

    for row in reader:
        if row['Country'] == country or row['Country_code'] == country:
            date = datetime.strptime(row['Date_reported'], "%Y-%m-%d")
            if beginning <= date <= ending:
                if row['New_cases'] != '':
                    total_cases += int(row['New_cases'])
                if row['New_deaths'] != '':
                    total_deaths += int(row['New_deaths'])
    return total_cases, total_deaths


def compare (countries, week):
    for country in countries:
        cases, deaths = stats(country, week, week)
        print(f"Total cases in {country} during {week}: {cases}")
        print(f"Total deaths in {country} from {week}: {deaths}\n")
        
    return cases, deaths


'''
def highest (week):
    with open('Data/WHO-COVID-19-global-data.csv', 'r' ) as file:
        reader = csv.DictReader(file)
        highest_cases = 0
        highest_country = ""
        for row in reader:
            if row['Date_reported'] == week:
                if int(row['New_cases']) > highest_cases:
                    highest_cases = int(row['New_cases'])
                    highest_country = row['Country']
        print(f"Country with the highest cases in {week}: {highest_country} with {highest_cases} cases")
'''

if __name__ == "__main__":
    print(reader)
    