from flask import Flask

from common.api import Api
from resource import gift_code
from resource import settlement
from resource import transition
from resource import product
from model import db
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db.bind(
    app.config['DB']['TYPE'],
    app.config['DB']['NAME'],
    create_db=True
)
db.generate_mapping(create_tables=True)

api = Api(app)
app.register_blueprint(gift_code.app)
app.register_blueprint(settlement.app)
app.register_blueprint(transition.app)
app.register_blueprint(product.app)


if __name__ == '__main__':
    app.run(
        app.config['HOST'],
        app.config['PORT'],
        app.config['DEBUG']
    )
