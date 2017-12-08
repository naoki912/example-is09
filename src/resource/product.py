from flask import Blueprint
from flask_restful import Resource
from flask_restful import Api

from model.product import Product

app = Blueprint("product", __name__, url_prefix="/product")
api = Api(app)


class ProductResource(Resource):
    pass


api.add_resource(ProductResource, "/")
