import json

from flask import Blueprint

info_bp = Blueprint('info_bp', __name__, static_folder='static', template_folder='templates')


@info_bp.route("/")
def info():
    return json.dumps(
        {
            "version": "0.0.0"
        }
    )
