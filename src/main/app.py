from flask import Flask, render_template, request
import requests
import json
from . import utils

app = Flask(__name__)


@app.route("/")
def home():
    user = utils.get_user_details(request.user_agent.platform)

    context = dict(
        **user,
        years_of_experience=6,
        age=9,
        wd=dict(weather_state_name='No Weather details', the_temp=0),
        city="Johannesurg"
    )

    ip_address = utils.get_ip_address(request)

    if utils.valid_ip_address(ip_address):
        try:
            resp = requests.get('http://ip-api.com/json/' + ip_address)

            resp_json = json.loads(resp.text)

            city = resp_json['city']
            lon = resp_json['lon']
            lat = resp_json['lat']
            url = "https://www.metaweather.com/api/location/search/?lattlong={},{}".format(
                lat, lon)
            woeid_resp = requests.get(url)
            woeid_json = json.loads(woeid_resp.text)

            woeid = '1582504'  # default is for Johannesburg, Gauteng, South Africa
            for data in woeid_json:
                if city == data['title']:
                    woeid = data['woeid']

            weather_url = 'https://www.metaweather.com/api/location/{}/'.format(
                woeid)

            weather = requests.get(weather_url)
            weather_json = json.loads(weather.text)
            context['city'] = city
            context['wd_img'] = 'https://www.metaweather.com/static/img/weather/{}.svg'.format(
                weather_json['consolidated_weather'][0]['weather_state_abbr'])
            context['wd'] = weather_json['consolidated_weather'][0]

        except Exception as ex:
            print('ex', ex)

    return render_template("home.html", **context)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
