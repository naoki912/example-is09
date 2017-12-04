from flask import Flask
from flask_restful import Api

from resource import gift_code
from resource import settlement
from resource import transition
from resource import product


app = Flask(__name__)
api = Api(app)

app.register_blueprint(gift_code.app)
app.register_blueprint(settlement.app)
app.register_blueprint(transition.app)
app.register_blueprint(product.app)


if __name__ == '__main__':
    app.run()
