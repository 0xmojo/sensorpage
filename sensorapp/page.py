import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

bp = Blueprint('home', __name__)

@bp.route("/")
def index():
    #todo fetch a temperature and 
    # hand it over to the template render
    temperature = 24.4444

    try:
        from w1thermsensor import W1ThermSensor

        sensor = W1ThermSensor()
        temperature = sensor.get_temperature()

    except ModuleNotFoundError:
        print("No sensor connected or not executed on a raspberry pi")

    return render_template("index/home.html", temperature=temperature)