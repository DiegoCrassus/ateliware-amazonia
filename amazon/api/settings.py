from os import environ
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.VERSION = environ.get("VERSION")
        self.FLASK_SERVER_NAME = None
        self.RESTX_VALIDATE = True
        self.RESTX_MASK_SWAGGER = False
        self.RESTX_SWAGGER_UI_DOC_EXPANSION = list
        self.RESTX_ERROR_404_HELP = False
        self.ENVIRONMENT = environ.get("ENVIRONMENT", "local")
        self.ENVIRONMENT = "local" if self.ENVIRONMENT == "local" else self.ENVIRONMENT

        # Env_vars
        self.FLASK_DEBUG = True if self.ENVIRONMENT == "local" else False
        self.FLASK_HOST = environ.get("FLASK_HOST", "0.0.0.0")
        self.FLASK_PORT = environ.get("FLASK_PORT", "5000")
        self.FLASK_URL_FIX = environ.get("FLASK_URL_FIX", "/api")
        self.ROUTE = environ.get("ROUTE", "/")
        self.HEALTH_ENDPOINT = environ.get("HEALTH_ENDPOINT", "status")
        self.DELIVERY_ENDPOINT = environ.get("DELIVERY_ENDPOINT", "delivery")
        self.PATH_LOG = environ.get("PATH_LOG", "./log_amazon")

        self.URL_WEIGHTS = environ.get(
            "URL_WEIGHTS", "https://mocki.io/v1/10404696-fd43-4481-a7ed-f9369073252f"
        )


envs = Config()
