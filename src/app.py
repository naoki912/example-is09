from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from resource import gift_code
from resource import settlement
from resource import transition
from resource import product
from config import Config
from model import db
from model.gift_code import GiftCode


app = Flask(__name__)
app.config.from_object(Config)

admin = Admin(app, name='carrier-design', template_mode='bootstrap3')
admin.add_view(ModelView(GiftCode, db.session))

with app.app_context():
    db.init_app(app)
    print(db.get_engine())
    db.create_all()

app.register_blueprint(gift_code.app, url_prefix='/api/v1')
app.register_blueprint(settlement.app, url_prefix='/api/v1')
app.register_blueprint(transition.app, url_prefix='/api/v1')
app.register_blueprint(product.app, url_prefix='/api/v1')


if __name__ == '__main__':
    app.run(
        app.config['HOST'],
        app.config['PORT'],
        app.config['DEBUG']
    )
