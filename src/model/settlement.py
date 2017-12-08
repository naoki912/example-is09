from model import db
from model.mixin import TimestampMixin


class Settlement(db.Model, TimestampMixin):
    __tablename__ = 'settlement'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.BigInteger, primary_key=True)
    gift_code_id = db.Column(db.BigInteger, db.ForeignKey('gift_code.id'), nullable=False)
    transition = db.relationship('Transition')
