from flask import Blueprint
from flask_restful import Resource
from flask_restful import Api

from model.settlement import Settlement

app = Blueprint("settlement", __name__, url_prefix="/settlement")
api = Api(app)


class SettlementResource(Resource):
    pass


api.add_resource(SettlementResource, "/")
