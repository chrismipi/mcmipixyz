from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    context = dict(
        years_of_experience='6+',
        age=9
    )
    
    return render_template("home.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
