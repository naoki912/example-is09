from model import db
from model.mixin import TimestampMixin


class GiftCode(db.Model, TimestampMixin):
    __tablename__ = 'gift_code'
    __table_args__ = {'sqlite_autoincrement': True}
    # primary_keyは自動的に`autoincrement=True`が設定されるはずなんだけどダメっぽい
    # https://stackoverflow.com/questions/20848300/
    # https://stackoverflow.com/questions/34581905/
    # ToDo: sqliteとMySQLの両方に対応させる
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    code = db.Column(db.String(16), unique=True, nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    # 現状はUTCで保存されるはず
    expiration_date = db.Column(db.DateTime, nullable=False)
    settlement = db.relationship('Settlement')
