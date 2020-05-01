import requests
import json
from .models import Location


def get_location(ip_address):
    resp = requests.get('http://ip-api.com/json/' + ip_address)

    resp_json = json.loads(resp.text)

    city = resp_json['city']
    lon = resp_json['lon']
    lat = resp_json['lat']

    location = Location(city, lon, lat)

    return location
