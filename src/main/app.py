from flask import Flask, render_template, request
from . import utils
from .services import get_location, get_woeid, get_weather_details, save_visit
from .models import SiteVisit

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
            location = get_location(ip_address)

            woeid = get_woeid(location.lat(), location.lon(), location.city())

            weather_details = get_weather_details(woeid)

            context['city'] = location.city()
            context['wd_img'] = weather_details.get_image()
            context['wd'] = weather_details.weather()

            visit = SiteVisit(ip_address, location.coordinates(),
                              location.city(), location.country(),
                              request.user_agent.platform)
            save_visit(visit)
        except Exception as ex:
            print('ex', ex)

    return render_template("home.html", **context)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
