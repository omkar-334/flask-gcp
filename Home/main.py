import webbrowser

from flask import Flask, render_template
from flask_ipfilter import IPFilter, Whitelist

app = Flask(__name__)

ip_filter = IPFilter(app, ruleset=Whitelist())
ip_filter.ruleset.permit("127.0.0.1")


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/marks")
def marks():
    webbrowser.open("https://flask-marks.el.r.appspot.com/")
    return render_template("home.html")


@app.route("/fees")
def fees():
    webbrowser.open("https://flask-fees.el.r.appspot.com/")
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
