from flask import Blueprint
from flask_restful import Resource
from flask_restful import Api

from model.transition import Transition
from model_schema.transition import TransitionSchema


transition_bp = Blueprint("transition", __name__)
api = Api(transition_bp, prefix="/transition")


class TransitionResource(Resource):
    pass


api.add_resource(TransitionResource, "/")
