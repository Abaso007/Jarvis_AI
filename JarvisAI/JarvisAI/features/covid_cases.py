import requests
import pycountry


def check_command_is_for_covid_cases(*args, **kwargs):
    command = kwargs.get('query')
    try:
        command = command.title()
        entities = kwargs.get('entities')
        if len(entities) > 0:
            country = [entity[0] for entity in entities if entity[1] == 'GPE'][0]
        else:
            country = get_country(command)
        cases = get_covid_cases(country)
        return f"The current active cases in {country} are {cases}"
    except Exception as e:
        print("Error: ", e)
        return "Sorry, I couldn't find the country you are looking for. Or server is down."


def get_country(command):  # For getting only the country name for the whole query
    for country in pycountry.countries:
        if country.name in command:
            return country.name


def get_covid_cases(country):  # For getting current covid cases
    response = requests.get(
        f'https://api.covid19api.com/live/country/{country}/status/confirmed'
    ).json()
    return sum(data.get('Active') for data in response)


if __name__ == '__main__':
    print(check_command_is_for_covid_cases('active Covid India cases?'))  # Example
