from flask import Flask
from flask_restful import Api

from resource.gift_code import GiftCodeResource
from resource.settlement import SettlementResource
from resource.transition import TransitionResource
from resource.product import ProductResource


app = Flask(__name__)
api = Api(app)


api.add_resource(GiftCodeResource,
                 '/gift_code',
                 '/gift_code/',
                 '/gift_code/<int:id>',
                 '/gift_code/<int:id>')

api.add_resource(SettlementResource)

api.add_resource(TransitionResource)

api.add_resource(ProductResource,
                 '/product',
                 '/product/',
                 '/product/<int:id>',
                 '/product/<int:id>')


if __name__ == '__main__':
    app.run()
