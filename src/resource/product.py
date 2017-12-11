from flask import Blueprint
from flask_restful import Resource
from flask_restful import Api

from model.product import Product
from model_schema.product import ProductSchema


product_bp = Blueprint("product", __name__)
api = Api(product_bp, prefix="/product")


class ProductResource(Resource):
    pass


api.add_resource(ProductResource, "/")
