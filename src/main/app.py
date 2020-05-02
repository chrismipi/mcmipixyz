from flask import Flask, render_template, request
import requests
import json
from . import utils
from .services import get_location, get_woeid

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

    ip_address = '41.144.78.241'  # utils.get_ip_address(request)

    if utils.valid_ip_address(ip_address):
        try:
            location = get_location(ip_address)

            woeid = get_woeid(location.lat(), location.lon(), location.city())

            weather_url = 'https://www.metaweather.com/api/location/{}/'.format(
                woeid)

            weather = requests.get(weather_url)
            weather_json = json.loads(weather.text)
            context['city'] = location.city()
            context['wd_img'] = 'https://www.metaweather.com/static/img/weather/{}.svg'.format(
                weather_json['consolidated_weather'][0]['weather_state_abbr'])
            context['wd'] = weather_json['consolidated_weather'][0]

        except Exception as ex:
            print('ex', ex)

    return render_template("home.html", **context)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
