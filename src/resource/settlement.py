from flask import Blueprint
from flask_restful import Resource
from flask_restful import Api

from model.settlement import Settlement
from model_schema.settlement import SettlementSchema


app = Blueprint("settlement", __name__)
api = Api(app, prefix="/settlement")


class SettlementResource(Resource):
    pass


api.add_resource(SettlementResource, "/")
