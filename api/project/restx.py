import logging
from flask_restx import Api
from settings import envs
from project.constants import CodeHttp, Message
from project.utils import objLogger, objResponse
from project.exception.NotTreatementError import NotTreatmentException


log = logging.getLogger(__name__)

api = Api(
    version="1.0",
    title="Documentação",
    description="Documentação swagger.",
    doc="/doc",
)

objLogger.info(f"Running as {envs.ENVIRONMENT}.")


@api.errorhandler
def default_error_handler(e):
    objLogger.error(Message.ERROR_NOT_TREATMENT)

    if not envs.FLASK_DEBUG:
        return objResponse.send_exception(
            NotTreatmentException, Message.ERROR_NOT_TREATMENT, CodeHttp.ERROR_500
        )
