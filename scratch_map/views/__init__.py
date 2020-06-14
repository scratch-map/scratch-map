from scratch_map import app
from scratch_map.views.info import info_bp


app.register_blueprint(info_bp, url_prefix="/info")
