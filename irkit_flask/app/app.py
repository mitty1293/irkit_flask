from flask import Flask, render_template
import post_irkit
from const import *

app = Flask(__name__)
irkit = post_irkit.Post_irkit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/light")
def light():
    irkit.req_post(LIGHT_SIG)

@app.route("/ac-on")
def ac_on():
    irkit.req_post(AC_ON_SIG)

@app.route("/ac-off")
def ac_off():
    irkit.req_post(AC_OFF_SIG)

@app.route("/heater-on")
def heater_on():
    irkit.req_post(HEATER_ON_SIG)

@app.route("/heater-off")
def heater_off():
    irkit.req_post(HEATER_OFF_SIG)

if __name__ == '__main__':
    app.run()