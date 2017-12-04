from flask import Blueprint
from flask_restful import Resource
from flask_restful import Api


app = Blueprint("gift_code", __name__, url_prefix="/gift_code")
api = Api(app)


class GiftCodeResource(Resource):
    def get(self):
        return "hello"


api.add_resource(GiftCodeResource, "/")
