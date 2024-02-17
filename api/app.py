import logging.config
import warnings
import os
from settings import envs

from loguru import logger
from flask import Flask, Blueprint
from flask_cors import CORS
from project.api.health import ns as health_operation
from project.api.amazon import ns as amazon_operation
from project.restx import api

app = Flask(__name__)
logging_conf_path = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "../logging.conf")
)
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)
logger.add(envs.PATH_LOG, rotation="1 week")


def configure_app(flask_app):
    flask_app.config["SERVER_NAME"] = envs.FLASK_SERVER_NAME
    flask_app.config["SWAGGER_UI_DOC_EXPANSION"] = envs.RESTX_SWAGGER_UI_DOC_EXPANSION
    flask_app.config["RESTX_VALIDATE"] = envs.RESTX_VALIDATE
    flask_app.config["RESTX_MASK_SWAGGER"] = envs.RESTX_MASK_SWAGGER
    flask_app.config["ERROR_404_HELP"] = envs.RESTX_ERROR_404_HELP
    flask_app.config["CORS_HEADERS"] = "Content-Type"


def initialize_app(flask_app):
    configure_app(flask_app)
    CORS(
        flask_app,
        allow_headers=["access-control-allow-origin", "Content-Type"],
        resources={r"/api/*": {"origins": "*"}},
        supports_credentials=True,
    )

    blueprint = Blueprint("api", __name__, url_prefix=envs.FLASK_URL_FIX)
    api.init_app(blueprint)
    api.add_namespace(health_operation)
    api.add_namespace(amazon_operation)
    flask_app.register_blueprint(blueprint)


def main():
    warnings.filterwarnings("ignore")
    initialize_app(app)
    logger.debug(
        "[+] --- starting at: {}:{}{}".format(
            envs.FLASK_HOST, envs.FLASK_PORT, envs.FLASK_URL_FIX
        )
    )
    app.run(host=envs.FLASK_HOST, port=envs.FLASK_PORT, debug=envs.FLASK_DEBUG)


if __name__ == "__main__":
    main()
