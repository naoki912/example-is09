from model_schema import ma
from model.product import Product


class ProductSchema(ma.ModelSchema):
    class Meta:
        model = Product
