from flask import Blueprint
from flask_restful import Resource
from flask_restful import Api

from model.transition import Transition


app = Blueprint("transition", __name__, url_prefix="/transition")
api = Api(app)


class TransitionResource(Resource):
    pass


api.add_resource(TransitionResource, "/")
