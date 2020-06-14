from flask import render_template, Flask
from structlog import get_logger

from config import Config

logger = get_logger()

app = Flask(__name__)
app.config.from_object(Config)
app.strict_slashes = False


@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')


import scratch_map.views  # NOQA
