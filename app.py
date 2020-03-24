from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route("/")
def home():
    context = dict(
        years_of_experience='6+',
        age=9
    )

    ip_address = request.remote_addr
    if ip_address != '127.0.0.1':
        resp = requests.get('http://ip-api.com/json/' + ip_address)

        resp_json = json.loads(resp.text)

        lon = resp_json['lon']
        lat = resp_json['lat']

        print('LON ', lon)
        print('LAT ', lat)

    return render_template("home.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
