from flask_swagger_ui import get_swaggerui_blueprint

import config
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(config.Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "flask-pet-users"}
)
app.register_blueprint(SWAGGER_BLUEPRINT)

from src import routes
