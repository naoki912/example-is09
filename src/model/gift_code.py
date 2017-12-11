from model import db
from model.mixin import TimestampMixin


class GiftCode(db.Model, TimestampMixin):
    __tablename__ = 'gift_code'
    __table_args__ = {'sqlite_autoincrement': True}
    # ToDo: sqliteとMySQLの両方に対応させる
    # sqliteだとBIGINTでautoincrementが使用できないので対応する
    # https://stackoverflow.com/questions/18835740/does-bigint-auto-increment-work-for-sqlalchemy-with-sqlite
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    code = db.Column(db.String(16), unique=True, nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    # 現状はUTCで保存されるはず
    expiration_date = db.Column(db.DateTime, nullable=False)
    settlement = db.relationship('Settlement')
