from flask import Blueprint
from flask_restful import Resource
from pony.orm import db_session
from pony.orm import select
from pony.orm.serialization import to_dict

from common.api import Api
from model import GiftCode


app = Blueprint("gift_code", __name__)
api = Api(app, prefix="/gift_code")


class GiftCodeResource(Resource):
    @db_session
    def get(self, id: int=None):
        if id is None:
            return api.make_response(
                to_dict(select(i for i in GiftCode).order_by(GiftCode.id)),
                200
            )
        else:
            gift_code = GiftCode[id]
            return api.make_response(
                to_dict(gift_code),
                200
            )

    @db_session
    def post(self):
        GiftCode()


api.add_resource(
    GiftCodeResource,
    "/",
    "/<int:id>"
)
