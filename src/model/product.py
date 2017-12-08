from model import db
from model.mixin import TimestampMixin


class Product(db.Model, TimestampMixin):
    __tablename__ = 'product'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    overview = db.Column(db.String(255), nullable=False)
    site_url = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    transition = db.relationship('Transition')
