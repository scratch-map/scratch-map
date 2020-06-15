import os

from scratch_map import app
from structlog import get_logger

from config import Config

logger = get_logger()

if __name__ == "__main__":
    if not os.getenv("APP_SETTINGS"):
        os.environ["APP_SETTINGS"] = "DevelopmentConfig"
    logger.info("Starting listening on port {}".format(Config.PORT))
    app.run(debug=False, host="0.0.0.0", port=int(Config.PORT))
