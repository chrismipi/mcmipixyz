import requests
import json
from .models import Location, WeatherDetails


def get_location(ip_address):
    resp = requests.get('http://ip-api.com/json/' + ip_address)

    resp_json = json.loads(resp.text)

    city = resp_json['city']
    lon = resp_json['lon']
    lat = resp_json['lat']

    location = Location(city, lon, lat)

    return location


def get_woeid(lat, lon, city):
    url = "https://www.metaweather.com/api/location/search/?lattlong={},{}".format(
        lat, lon)
    woeid_resp = requests.get(url)
    woeid_json = json.loads(woeid_resp.text)

    woeid = '1582504'  # default is for Johannesburg, Gauteng, South Africa
    for data in woeid_json:
        if city == data['title']:
            woeid = data['woeid']

    return woeid


def get_weather_details(woeid):
    weather_url = 'https://www.metaweather.com/api/location/{}/'.format(
        woeid)

    weather = requests.get(weather_url)
    weather_json = json.loads(weather.text)

    consolidated = weather_json['consolidated_weather'][0]
    abbr = weather_json['consolidated_weather'][0]['weather_state_abbr']
    details = WeatherDetails(consolidated, abbr)

    return details
