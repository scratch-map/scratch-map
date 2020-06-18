from flask import render_template, Flask, request
from structlog import get_logger

from config import Config

logger = get_logger()

app = Flask(__name__)
app.config.from_object(Config)
app.strict_slashes = False

countries = []


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        countries.append(request.form["add_country"])

    return render_template("index.html")


import scratch_map.views  # NOQA
