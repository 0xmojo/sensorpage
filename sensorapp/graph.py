import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for

bp = Blueprint("graph", __name__)

@bp.route("/graph", methods=("GET",))
def graph():
    return render_template("graph/graph.html")