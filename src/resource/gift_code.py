from flask import Blueprint
from flask_restful import Resource
from flask_restful import Api
from pony.orm import db_session

from model import GiftCode


app = Blueprint("gift_code", __name__, url_prefix="/gift_code")
api = Api(app)


class GiftCodeResource(Resource):
    @db_session
    def get(self, id: int):
        a = GiftCode[id]
        if id is None:
            return "hello"
        else:
            return a

    @db_session
    def post(self):
        gift_code = GiftCode()


api.add_resource(
    GiftCodeResource,
    "/",
    "/<int:id>"
)
