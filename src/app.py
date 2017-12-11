from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from resource.gift_code import gift_code_bp
from resource.settlement import settlement_bp
from resource.transition import transition_bp
from resource.product import product_bp
from config import Config
from model import db
from model.gift_code import GiftCode
from model_schema import ma


app = Flask(__name__)
app.config.from_object(Config)

admin = Admin(app, name='carrier-design', template_mode='bootstrap3')
admin.add_view(ModelView(GiftCode, db.session))

db.init_app(app)

with app.app_context():
    db.create_all()

ma.init_app(app)

app.register_blueprint(gift_code_bp, url_prefix='/api/v1')
app.register_blueprint(settlement_bp, url_prefix='/api/v1')
app.register_blueprint(transition_bp, url_prefix='/api/v1')
app.register_blueprint(product_bp, url_prefix='/api/v1')


if __name__ == '__main__':
    app.run(
        app.config['HOST'],
        app.config['PORT'],
        app.config['DEBUG']
    )
