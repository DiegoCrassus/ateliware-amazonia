import logging
import traceback
from amazon.api.settings import envs
from flask import request
from flask_restx import Resource
from amazon.api.project.restx import api
from amazon.api.project.constants import CodeHttp, Message
from amazon.api.project.utils import doc_swagger
from amazon.api.project.restx import objLogger, objResponse
from amazon.api.project.exception import DataAquisitionException
from amazon.api.project.bo.delivery import amazon_delivery

log = logging.getLogger(__name__)
ns = api.namespace(envs.DELIVERY_ENDPOINT, description="Post operação.")


@ns.route(envs.ROUTE, methods=["POST"])
class PostsCollection(Resource):
    @api.response(200, "Enviado com sucesso.")
    @api.marshal_with(doc_swagger.OUTPUT_DATA)
    @api.expect(doc_swagger.INPUT_DATA)
    def post(self):
        """
        Método de teste POST
        """
        objLogger.debug(Message.REQUEST)
        request_data = request.get_json()

        try:
            data = amazon_delivery(request_data)

        except KeyError as error:
            response = objResponse.send_exception(
                objError=error, messages=Message.ERROR_BO, status=CodeHttp.ERROR_500
            )
            objLogger.error(messages=Message.ERROR_BO)
            objLogger.debug(messages=traceback.format_exc())

        except TypeError as error:
            response = objResponse.send_exception(
                objError=error, messages=Message.ERROR_BO, status=CodeHttp.ERROR_500
            )
            objLogger.error(messages=Message.ERROR_BO)
            objLogger.debug(messages=traceback.format_exc())

        except DataAquisitionException as error:
            response = objResponse.send_exception(
                objError=error,
                messages=Message.ERROR_FAIL_DATA_ACQUISITION,
                status=CodeHttp.ERROR_404,
            )
            objLogger.error(messages=Message.ERROR_FAIL_DATA_ACQUISITION)
            objLogger.debug(messages=traceback.format_exc())

        except Exception as error:
            response = objResponse.send_exception(
                objError=error, messages=Message.ERROR_BO, status=CodeHttp.ERROR_500
            )
            objLogger.error(messages=Message.ERROR_BO)
            objLogger.debug(messages=traceback.format_exc())

        else:
            response = objResponse.send_success(
                messages=Message.SUCESS_EXEMPLO, status=CodeHttp.SUCCESS_200, data=data
            )
            objLogger.success(messages=Message.SUCESS_EXEMPLO)

        return response
