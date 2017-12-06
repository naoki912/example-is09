from datetime import datetime
from datetime import timedelta

from flask import Blueprint
from flask import current_app
from flask_restful import Resource
from flask_restful import reqparse
from pony.orm import db_session
from pony.orm import select
from pony.orm.serialization import to_dict
from pony.orm import commit

from common.api import Api
from common.util.code import generate_code
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

        parser = reqparse.RequestParser()
        parser.add_argument(
            'balance',
            type=int
        )
        args = parser.parse_args()

        balance = args['balance'] if args['balance'] is not None else current_app.config['DEFAULT_BALANCE']

        # ToDo: 期限をConfigで設定できるようにする
        expiration_date = datetime.now() + timedelta(days=1)

        gift_code = GiftCode(
            code=generate_code(),
            balance=balance,
            expiration_date=expiration_date,
        )

        # ここでcommitをしないとgift_code変数内がNoneのままになる
        commit()

        return api.make_response(
            to_dict(gift_code), 201
        )


api.add_resource(
    GiftCodeResource,
    "/",
    "/<int:id>"
)
