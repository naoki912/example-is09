from datetime import datetime
from datetime import timedelta

from flask import Blueprint
from flask import current_app
from flask_restful import Resource
from flask_restful import reqparse

from common.api import Api
from common.util.gift_code import generate_code
from model.gift_code import GiftCode
from model_schema.gift_code import GiftCodeSchema
from model import db
from common.util.auth import auth


app = Blueprint("gift_code", __name__)
api = Api(app, prefix="/gift_code")


class GiftCodeResource(Resource):

    def get(self, code: str=None):

        if code is None:
            # ToDo: ページング
            gift_code = GiftCode.query.all()
            body = GiftCodeSchema(many=True).dump(gift_code).data
        else:
            gift_code = GiftCode.query.filter_by(code=code).first()

            if gift_code is None:
                return api.make_response(None, 404)

            body = GiftCodeSchema().dump(gift_code).data

        return api.make_response(
            body,
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
        db.session.add(gift_code)
        db.session.commit()
        body = GiftCodeSchema().dump(gift_code).data

        return api.make_response(
            body,
            201
        )

    @auth
    def put(self, code: str=None):
        """
        PUTの参考実装
        - authデコレータの使い方
        - RequestParserの使い方

        :param code:
        :return:
        """

        gift_code = GiftCode.query.filter_by(code=code).first()

        if gift_code is None:
            return api.make_response(None, 404)

        # RequestParserは削除予定
        # http://flask-restful.readthedocs.io/en/0.3.5/reqparse.html#request-parsing
        parser = reqparse.RequestParser()
        parser.add_argument(
            'balance',
            type=int,
        )
        parser.add_argument(
            'expiration_date',
            type=datetime,
        )
        args = parser.parse_args()

        if args['balance'] is not None:
            gift_code.balance = args['balance']

        if args['expiration_date'] is not None:
            gift_code.expiration_date = args['expiration_date']

        db.session.commit()

        body = GiftCodeSchema().dump(gift_code).data

        return api.make_response(body, 200)

    def delete(self, code: str=None):

        gift_code = GiftCode.query.filter_by(code=code).first()

        if gift_code is None:
            return api.make_response(None, 404)

        db.session.delete(gift_code)
        db.session.commit()

        return api.make_response(None, 204)


api.add_resource(
    GiftCodeResource,
    "/",
    "/<string:code>"
)
