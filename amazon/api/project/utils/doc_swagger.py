from flask_restx import fields
from amazon.api.project.restx import api

# expected input values of api
INPUT_DATA = api.model(
    "input",
    {
        "start": fields.String(
            required=True, description="Starter point", example="A1"
        ),
        "checkpoint": fields.String(
            required=True, description="Checkpoint position", example="C5"
        ),
        "finish": fields.String(
            required=True, description="Delivery point", example="G5"
        ),
    },
)

OUTPUT_DATA = api.model(
    "Output",
    {
        "messages": fields.String(required=True, description="Sucess or Error mensage"),
        "status": fields.String(required=True, description="Status code"),
        "data": fields.Raw(required=False, description="response"),
    },
)
