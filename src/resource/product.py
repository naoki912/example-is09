from flask import Blueprint
from flask_restful import Resource
from flask_restful import Api

from model.product import Product
from model_schema.product import ProductSchema


app = Blueprint("product", __name__)
api = Api(app, prefix="/product")


class ProductResource(Resource):
    pass


api.add_resource(ProductResource, "/")
