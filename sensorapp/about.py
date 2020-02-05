import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

bp = Blueprint("about", __name__)

@bp.route("/about", methods=("GET",))
def about():
    return render_template("about/about.html")