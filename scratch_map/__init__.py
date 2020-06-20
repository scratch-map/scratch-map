from flask import render_template, Flask, request
from structlog import get_logger

from config import Config
from scratch_map.countries import Countries

logger = get_logger()

app = Flask(__name__)
app.config.from_object(Config)
app.strict_slashes = False

countries = Countries()


@app.route("/", methods=["GET", "POST"])
def root():
    if request.method == "POST":
        countries.add_country(request.form["add_country"])

    return render_template("index.html", country_list=countries.country_list)


import scratch_map.views  # NOQA
