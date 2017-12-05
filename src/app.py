from flask import Flask

from common.api import Api
from resource import gift_code
from resource import settlement
from resource import transition
from resource import product
from model import db


app = Flask(__name__)
api = Api(app)

db.bind('sqlite', 'db.sqlite3', create_db=True)
db.generate_mapping(create_tables=True)

app.register_blueprint(gift_code.app)
app.register_blueprint(settlement.app)
app.register_blueprint(transition.app)
app.register_blueprint(product.app)


if __name__ == '__main__':
    app.run()
