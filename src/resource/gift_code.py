from datetime import datetime
from datetime import timedelta

from flask import Blueprint
from flask import current_app
from flask_restful import Resource
from flask_restful import reqparse

from common.api import Api
from common.util.code import generate_code
from model.gift_code import GiftCode


app = Blueprint("gift_code", __name__)
api = Api(app, prefix="/gift_code")


class GiftCodeResource(Resource):
    def get(self, code: str=None):
        if code is None:
            # ToDo: ページング
            return api.make_response(
                # [GiftCode.__dict__ for GiftCode in GiftCode.query.all()[0]],
                None,
                200
            )
        else:
            return api.make_response(
                # GiftCode.query.filter_by(code=code).first().__dict__,
                None,
                200
            )

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

        code = generate_code()

        gift_code = GiftCode(
            code=code,
            balance=balance,
            expiration_date=expiration_date,
        )

        return api.make_response(
            gift_code, 201
        )

    def delete(self, code: str=None):
        return api.make_response(None, 204)


api.add_resource(
    GiftCodeResource,
    "/",
    "/<string:code>"
)
