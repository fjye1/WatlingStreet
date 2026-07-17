from flask import Blueprint, render_template, request
from sqlalchemy import func



home_bp = Blueprint('home', __name__)


@home_bp.route("/")
def index():
    # Preload products with boxes and comments

    return render_template(
        "home/index.html")
