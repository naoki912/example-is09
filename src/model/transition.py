from model import db
from model.mixin import TimestampMixin


class Transition(db.Model, TimestampMixin):
    __tablename__ = 'transitions'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.BigInteger, primary_key=True)
    settlement_id = db.Column(db.BigInteger, db.ForeignKey('settlement.id'), nullable=False)
    product_id = db.Column(db.BigInteger, db.ForeignKey('product.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)

