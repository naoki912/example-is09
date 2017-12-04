from flask import Blueprint
from flask import make_response
from flask_restful import Resource
from flask_restful import Api
from pony.orm import db_session
from pony.orm import select
from pony.orm.serialization import to_json

from model import GiftCode


app = Blueprint("gift_code", __name__, url_prefix="/gift_code")
api = Api(app)


class GiftCodeResource(Resource):
    @db_session
    def get(self, id: int=None):
        if id is None:
            return make_response(
                to_json(select(i for i in GiftCode).order_by(GiftCode.id)),
                200
            )
        else:
            gift_code = GiftCode[id]
            return make_response(to_json(gift_code), 200)

    @db_session
    def post(self):
        GiftCode()


api.add_resource(
    GiftCodeResource,
    "/",
    "/<int:id>"
)
